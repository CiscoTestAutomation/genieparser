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
        'available': str,
        'used': str
    }

# =================
# Parser for:
#  * 'show bootflash:'
# =================
class ShowBootflash(ShowBootflashSchema):
    """Parser for show bootflash:"""

    cli_command = 'show bootflash:'

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        #         available used
        p1 = re.compile(r"(?P<available>\d+)\s+bytes available\s+\((?P<used>\d+)\s+bytes used\)")


        # initial variables
        ret_dict = {}

        for line in out.splitlines():
            line_strip = line.strip()
            m = p1.match(line_strip)
            if m:
                group = m.groupdict()
                ret_dict.update({k:str(v) for k, v in group.items()})
                continue

        return ret_dict
# ----------------------
