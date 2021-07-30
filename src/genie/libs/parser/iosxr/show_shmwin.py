# Python
''' show_shmwin.py

IOSXR parsers for the following show commands:
    * show shmwin summary
    * show shmwin summary location <WORD>
'''

import re
# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Optional


# ==================================================
# Parser for 'show shmwin summary [location <WORD>]'
# ==================================================
class ShowShmwinSummarySchema(MetaParser):
    """Schema for show shmwin summary
                  show shmwin summary location {location}
    """

    schema = {
        'summary': {
            str: {
                'virtual_mem_size': int,
                'virtual_mem_range_start': str,
                'virtual_mem_range_end': str,
            },
            'total_shmwin_usage': int,
        },
        Optional('windows'): {
            int: {
                'window_name': str,
                'id': int,
                'group': str,
                'num_users': int,
                'num_writers': int,
                'owner': str,
                'usage': int,
                'peak': int,
                'peak_date': str,
                'peak_time': str,
            },
        }
    }


class ShowShmwinSummary(ShowShmwinSummarySchema):
    """ Parser for show shmwin summary
                   show shmwin summary location {location}"""

    cli_command = ['show shmwin summary', 'show shmwin summary location {location}']
    exclude = ['age']

    def cli(self, location='', cmd=None, output=None):  # noqa
        if output is None:
            if not cmd:
                cmd = self.cli_command[0]
                if location:
                    cmd = self.cli_command[1].format(location=location)

            out = self.device.execute(cmd)
        else:
            out = output

        # Virtual Memory size  : 1536 MBytes
        # Virtual Memory Group 2 size  : 384 MBytes
        p1 = re.compile(r'Virtual Memory\s+(Group (?P<group>\d+)\s+)?size\s+:\s+(?P<virtual_mem_size>\d+) +MBytes')
        # Virtual Memory Range : 0x50000000 - 0xb0000000
        # Virtual Memory Group 2 Range : 0xb8000000 - 0xd0000000
        p2 = re.compile(r'Virtual Memory\s+(Group (?P<group>\d+)\s+)?Range\s+:\s+(?P<virtual_mem_range_start>\S+) +- +(?P<virtual_mem_range_end>\w+)')

        # Window Name      ID  GRP #Usrs #Wrtrs Ownr Usage(KB) Peak(KB) Peak Timestamp
        # ---------------- --- --- ----- ------ ---- --------- -------- -------------------
        # Data for Window "sub_ses_ut_db":
        # -----------------------------
        # sub_ses_ut_db    82  1   1     1      0    3         0        --/--/---- --:--:--
        # Data for Window "subsession_db":
        # -----------------------------
        # subsession_db    81  1   2     2      0    9859      9859     03/21/2021 21:13:51
        # Data for Window "ifo_ea_shm":
        # -----------------------------
        # ifo_ea_shm       130 P   1     1      0    2795      2795     03/18/2021 02:09:01

        p3 = re.compile(
            r'\s*(?P<window_name>\S+)\s+(?P<id>\d+)\s+(?P<group>\S+)\s+(?P<num_users>\d+)\s+(?P<num_writers>\d+)'
            r'\s+(?P<owner>\S+)\s+(?P<usage>\d+)\s+(?P<peak>\d+)\s+(?P<peak_date>\S+)\s+(?P<peak_time>\S+)'
        )

        # ---------------------------------------------
        # Total SHMWIN memory usage : 984 MBytes
        p4 = re.compile(r'Total SHMWIN memory usage\s+:\s+(?P<total_shmwin_usage>\d+) +MBytes')

        # initial variables
        ret_dict = {}
        index = 0

        for line in out.splitlines():
            line = line.strip()

            # Virtual Memory size  : 1536 MBytes
            # Virtual Memory Group 2 size  : 384 MBytes
            m = p1.match(line)
            if m:
                group = m.groupdict()
                summary_dict = ret_dict.setdefault('summary', {})
                grp = group.get('group') or '1'
                summary_dict.setdefault(grp, {})['virtual_mem_size'] = int(group['virtual_mem_size'])
                continue

            # Virtual Memory Range : 0x50000000 - 0xb0000000
            # Virtual Memory Group 2 Range : 0xb8000000 - 0xd0000000
            m = p2.match(line)
            if m:
                group = m.groupdict()
                grp = group.get('group') or '1'
                summary_dict[grp]['virtual_mem_range_start'] = group['virtual_mem_range_start']
                summary_dict[grp]['virtual_mem_range_end'] = group['virtual_mem_range_end']
                continue

            # sub_ses_ut_db    82  1   1     1      0    3         0        --/--/---- --:--:--
            # subsession_db    81  1   2     2      0    9859      9859     03/21/2021 21:13:51
            m = p3.match(line)
            if m:
                group = m.groupdict()
                window_dict = ret_dict.setdefault('windows', {}).setdefault(index, {})
                index += 1
                window_dict['window_name'] = group['window_name']
                window_dict['id'] = int(group['id'])
                window_dict['num_users'] = int(group['num_users'])
                window_dict['num_writers'] = int(group['num_writers'])
                window_dict['usage'] = int(group['usage'])
                window_dict['peak'] = int(group['peak'])
                window_dict['group'] = group['group']
                window_dict['owner'] = group['owner']
                if '--' in group['peak_date']:
                    window_dict['peak_date'] = ''
                    window_dict['peak_time'] = ''
                else:
                    window_dict['peak_date'] = group['peak_date']
                    window_dict['peak_time'] = group['peak_time']
                continue

            # Total SHMWIN memory usage : 984 MBytes
            m = p4.match(line)
            if m:
                group = m.groupdict()
                summary_dict = ret_dict.setdefault('summary', {})
                summary_dict['total_shmwin_usage'] = int(group['total_shmwin_usage'])
                continue

        return ret_dict
