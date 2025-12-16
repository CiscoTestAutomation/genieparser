"""show_privilege.py

IOSXE parsers for the following show commands:

    * show privilege

"""

# Python
import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Optional, Or


# ==============================================
#  Schema for show privilege
# ==============================================
class ShowPrivilegeSchema(MetaParser):
    """Schema for show privilege"""

    schema = {
        'current_privilege_level': int,
    }

# ==============================================
#  Parser for show privilege
# ==============================================
class ShowPrivilege(ShowPrivilegeSchema):
    """Parser for show privilege"""

    cli_command = 'show privilege'

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        # Current privilege level is 15
        p1 = re.compile(r'^Current\s+privilege\s+level\s+is\s+(?P<level>\d+)$')

        ret_dict = {}

        for line in output.splitlines():
            line = line.strip()

            # Current privilege level is 15
            m = p1.match(line)
            if m:
                group = m.groupdict()
                ret_dict['current_privilege_level'] = int(group['level'])
                continue

        return ret_dict