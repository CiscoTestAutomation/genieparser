'''show_service.py
IOSXE parser for the following show command
	* show service-group state
'''

# Python
import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, \
												Any

# ====================================================
#  schema for show service-group traffic-stats
# ====================================================
class ShowServiceGroupTrafficStatsSchema(MetaParser):
    """Schema for:
        show service-group traffic-stats
        show service-group traffic-stats <group> """

    schema = {
        'group': {
            Any(): {
                'pkts_in': int, 
                'pkts_out': int, 
                'bytes_in': int, 
                'bytes_out': int, 
            },
        }
    }


# ====================================================
#  parser for show service-group traffic-stats
# ====================================================
class ShowServiceGroupTrafficStats(ShowServiceGroupTrafficStatsSchema):
    """Parser for :
        show service-group traffic-stats
        show service-group traffic-stats <group> """

    cli_command = ['show service-group traffic-stats' ,'show service-group traffic-stats {group}']

    def cli(self, group="", output=None):
        if output is None:
            if group:
                cmd = self.cli_command[1].format(group=group)
            else:
                cmd = self.cli_command[0]
            out = self.device.execute(cmd)
        else:
            out = output

        # initialize result dict
        result_dict = {}
        
        # Group    Pkts In   Bytes In   Pkts Out  Bytes Out
        #     1         78      10548        172      18606
        p1 = re.compile(r'^\s*(?P<num>[\d]+) +(?P<pkts_in>[\d]+) +(?P<bytes_in>[\d]+)'
                        ' +(?P<pkts_out>[\d]+) +(?P<bytes_out>[\d]+)$')

        for line in out.splitlines():
            line = line.rstrip()

            m = p1.match(line)
            if m:
                group = m.groupdict()
                num = int(group.pop('num'))
                g_dict = result_dict.setdefault('group', {}).setdefault(num, {})
                g_dict.update({k: int(v) for k, v in group.items()})
                continue

        return result_dict