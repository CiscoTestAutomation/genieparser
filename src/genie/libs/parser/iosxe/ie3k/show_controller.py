''' show_controller.py

IOSXE parsers for the following show commands:

    * 'show controllers power inline'
'''

import re
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Or, Optional, Use
# import parser utils
from genie.libs.parser.utils.common import Common


# =============================================
# Schema for 'show controllers power inline'
# =============================================
class ShowControllersPowerInlineSchema(MetaParser):
    """Schema for 'show controllers power inline'"""

    schema = {
        Optional('poe_controller_registers'): str,
        Optional('poe_firmware_logs'): str,
    }

# =============================================
# Parser for 'show controllers power inline'
# =============================================
class ShowControllersPowerInline(ShowControllersPowerInlineSchema):
    """Parser for 'show controllers power inline'"""

    cli_command = 'show controllers power inline'

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        # Initialize return dictionary
        ret_dict = {}

        # Regular expressions for parsing
        # For PoE controller registers refer to /flash/poe_controller_regs_sw1*
        p1 = re.compile(r'^For PoE controller registers refer to (?P<poe_controller_registers>\S+)$')
        # For PoE firmware logs refer to /flash/poe_fw_logs_sw1*
        p2 = re.compile(r'^For PoE firmware logs refer to (?P<poe_firmware_logs>\S+)$')

        # Iterate over each line of the output
        for line in output.splitlines():
            line = line.strip()

            # Match PoE controller registers
            m = p1.match(line)
            if m:
                ret_dict['poe_controller_registers'] = m.group('poe_controller_registers')
                continue

            # Match PoE firmware logs
            m = p2.match(line)
            if m:
                ret_dict['poe_firmware_logs'] = m.group('poe_firmware_logs')
                continue

        # Return the parsed dictionary
        return ret_dict
