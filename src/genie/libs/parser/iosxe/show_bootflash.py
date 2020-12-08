''' show_bootflash.py

IOSXE parsers for the following show commands:
    * show bootflash:
'''

# Python

import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Optional

# parser utils
from genie.libs.parser.utils.common import Common

# =================
# Schema for:
#  * 'show bootflash:'
# =================

class ShowBootflashSchema(MetaParser):
    """Schema for show bootflash:."""
    schema = {
        'bytes_available': int,
        'bytes_used': int,
        'files': {
            Any(): {
                'file_length': int,
                'file_date': str,
                'file_name': str
                }
            }
    }

# =================
# Parser for:
#  * 'show bootflash:'
# =================
class ShowBootflash(ShowBootflashSchema):
    """Parser for show bootflash:"""

    cli_command = 'show bootflash:'

    def cli(self, output=None):
        #print("DEBUG: cli")
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        # 13755338752 bytes available (489017344 bytes used)
        p1 = re.compile(r"(?P<bytes_available>\d+)\s+bytes available\s+\((?P<bytes_used>\d+)\s+bytes used\)")
        #12         11 Oct 12 2020 07:27:04 +00:00 /bootflash/tracelogs/timestamp
        p2 = re.compile(r"(?P<file_index>\d+)\s+(?P<file_length>\d+)\s+(?P<file_date>[a-zA-Z]+\s+\d+\s+\d+\s+[0-9:.]+\s+[0-9+:]+)\s+(?P<file_name>\S+)")

        # initial variables
        ret_dict = {}

        for line in out.splitlines():
            line_strip = line.strip()
            # 13755338752 bytes available (489017344 bytes used)
            m = p1.match(line_strip)
            if m:
                group = m.groupdict()
                ret_dict.update({k:int(v) for k, v in group.items()})
                continue
            #12         11 Oct 12 2020 07:27:04 +00:00 /bootflash/tracelogs/timestamp
            m = p2.match(line_strip)
            if m:
                group=m.groupdict()
                index=int(group['file_index'])
                if 'files' not in ret_dict:
                    ret_dict['files']={}
                if index not in ret_dict['files']:
                    ret_dict['files'][index]={}
                ret_dict['files'][index]['file_length']=int(group['file_length'])
                ret_dict['files'][index]['file_date']=group['file_date']
                ret_dict['files'][index]['file_name']=group['file_name']

        return ret_dict
# ----------------------
