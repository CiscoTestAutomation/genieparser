"""show_fips.py
    supported commands:
        * show fips authorization-key 
"""

import re

from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Optional


# =================================================
# Schema for:
#  * 'show_fips_authorization_key '
# =================================================

class ShowFipsAuthorizationKeySchema(MetaParser):
    """Schema for show fips authorization-key"""

    schema = {
        "fips": {
            "stored_key": str
        }
    }


# =================================================
# Parser for:
#  * 'show_fips_authorization_key'
# =================================================
class ShowFipsAuthorizationKey(ShowFipsAuthorizationKeySchema):
    """Parser for show fips authorization-key"""

    cli_command = 'show fips authorization-key'

    def cli(self, output=None):
        out = self.device.execute(self.cli_command) if output is None else output

        ret_dict = {}
        #                  FIPS: Stored key (16) : 12345678901234567890123456789012
        p1 = re.compile(r'^FIPS: +Stored key +\((\d+)\) +: +(?P<stored_key>\S+)$')

        for line in out.splitlines():
            line = line.strip()
            #  FIPS: Stored key (16) : 12345678901234567890123456789012
            m =  p1.match(line)
            if m:
                group = m.groupdict()
                fp_dict = ret_dict.setdefault('fips', {})
                fp_dict.update({
                    'stored_key': (group['stored_key'])
                })
            else:
                fp_dict = ret_dict.setdefault('fips', {})
                fp_dict.update({
                    'stored_key': 'No key installed'
                })
                continue
        return ret_dict