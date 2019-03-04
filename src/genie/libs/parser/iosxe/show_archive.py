''' show_archive.py

IOSXE parsers for the following show commands:
    * show archive
'''

# Python
import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Optional


# =============================================
# Parser for 'show archive'
# =============================================

class ShowArchiveSchema(MetaParser):
    """
    Schema for show archive
    """

    schema = {'archive': {
                'total': int,
                Optional('max_archive_configurations'): int,
                'most_recent_file': str,
                Any(): {
                    'file': str,
                },
            }
        }

class ShowArchive(ShowArchiveSchema):
    """ Parser for show archive """

    # Parser for 'show archive'
    cli_command = 'show archive'

    def cli(self,output=None):
        if output is None:
            # excute command to get output
            out = self.device.execute(self.cli_command)
        else:
            out = output

        # initial variables
        ret_dict = {}

        for line in out.splitlines():
            line = line.strip()

            # The maximum archive configurations allowed is 10.
            p1 = re.compile(r'^The +maximum +archive +configurations +allowed +is +(?P<max>\d+)\.$')
            m = p1.match(line)
            if m:
                if 'archive' not in ret_dict:
                    ret_dict['archive'] = {}
                ret_dict['archive']['max_archive_configurations'] = int(m.groupdict()['max'])
                continue

            # There are currently 1 archive configurations saved.
            p2 = re.compile(r'^There +are +currently +(?P<total>\d+) +archive +configurations +saved\.$')
            m = p2.match(line)
            if m:
                if 'archive' not in ret_dict:
                    ret_dict['archive'] = {}
                    
                ret_dict['archive']['total'] = int(m.groupdict()['total'])
                continue

            # 1        bootflash:uncfgIntfgigabitethernet0_0_0-Sep-27-15-04-18.414-PDT-0 <- Most Recent
            p3 = re.compile(r'^(?P<num>[0-9]+) +'
                             '(?P<file>[\w\:\-\.]+)(?P<recent> +\<\- +Most +Recent)?$')
            m = p3.match(line)
            if m:
                num = m.groupdict()['num']
                file = m.groupdict()['file']
                recent = m.groupdict()['recent']

                if 'archive' not in ret_dict:
                    ret_dict['archive'] = {}

                if num not in ret_dict['archive']:
                    ret_dict['archive'][num] = {}

                ret_dict['archive'][num]['file'] = file
                if recent:
                    ret_dict['archive']['most_recent_file'] = file                
                continue

        return ret_dict
