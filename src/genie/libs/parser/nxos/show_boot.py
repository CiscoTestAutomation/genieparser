"""show_boot.py
NXOS parsers for the following show commands:
* 'show boot mode'
"""

import re
from genie.libs.parser.utils.common import Common
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Optional


# ===========================
# Schema for 'show boot mode'
# ===========================
class ShowBootModeSchema(MetaParser):
    """ Schema for:
       * 'show boot mode'
    """
    schema = {
        'bootmode': str,
    }


# ===========================================
# Parser for 'show boot mode'
# ===========================================
class ShowBootMode(ShowBootModeSchema):
    """ Parser for 'show boot mode' """

    cli_command = "show boot mode"

    def cli(self, output=None):

        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        parsed_dict = {}

        # Current mode is native.
        # Current mode is lxc.
        p1 = re.compile(r'^Current mode is (?P<mode>\w+)')

        for line in out.splitlines():
            line_strip = line.strip()

            # Current mode is native.
            m = p1.match(line)
            if m:
                parsed_dict['bootmode'] = m.groupdict()['mode']
                continue

        return parsed_dict
