"""show_dampening.py

NXOS parsers for the following show commands:
    * show dampening interface
"""

# Python
import re

# Metaparser
from genie.metaparser import MetaParser


# ==================================================
# Schema for 'show dampening interface'
# ==================================================
class ShowDampeningInterfaceSchema(MetaParser):
    """Schema for show dampening interface"""

    schema = {
        'number_of_interfaces_configured_with_dampening': int,
        'number_of_interfaces_in_suppressed_state': int,
    }


# ==================================================
# Parser for 'show dampening interface'
# ==================================================
class ShowDampeningInterface(ShowDampeningInterfaceSchema):
    """Parser for show dampening interface"""

    cli_command = 'show dampening interface'

    def cli(self, command, output=None):
        if output is None:
            output = self.device.execute(command)

        ret_dict = {}

        # number of interfaces configured with dampening = 2
        p1 = re.compile(r'^number +of +interfaces +configured +with +dampening *= *(?P<number_of_interfaces_configured_with_dampening>\d+)$')

        # number of interfaces in suppressed state = 0
        p2 = re.compile(r'^number +of +interfaces +in +suppressed +state *= *(?P<number_of_interfaces_in_suppressed_state>\d+)$')

        for line in output.splitlines():
            line = line.strip()
            if not line:
                continue

            # number of interfaces configured with dampening = 2
            m = p1.match(line)
            if m:
                groups = m.groupdict()
                ret_dict.update({
                    'number_of_interfaces_configured_with_dampening': int(
                        groups[
                            'number_of_interfaces_configured_with_dampening'
                        ])
                })
                continue

            # number of interfaces in suppressed state = 0
            m = p2.match(line)
            if m:
                groups = m.groupdict()
                ret_dict.update({
                    'number_of_interfaces_in_suppressed_state': int(
                        groups[
                            'number_of_interfaces_in_suppressed_state'
                        ])
                })
                continue

        return ret_dict
