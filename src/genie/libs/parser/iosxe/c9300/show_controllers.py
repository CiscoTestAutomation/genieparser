"""
IOSXE C9300 parsers for the following show commands:
    * show controllers ethernet-controllers {interface} phy detail
"""
# Python
import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Or, Optional


# ============================
#  Schema for 'show controllers ethernet-controllers {interface} phy detail'
# ============================

class ShowControllersSchema(MetaParser):

    """ Schema for:
        * show controllers ethernet-controllers {interface} phy detail
    """
    schema = {
        'interface_name': str,
        'if_id': str,
        'phy_registers': {
            Any():
                {'register_number': str,
                 'ieee_register_number': str,
                 'register_name': str,
                 'bits': str
                }
            }
        }


# ============================
#  Parser for 'show controllers ethernet-controllers {interface} phy detail'
# ============================
class ShowControllers(ShowControllersSchema):
    """
    Parser for :
        * show controllers ethernet-controllers {interface} phy detail
    """

    cli_command = 'show controllers ethernet-controllers {interface} phy detail'

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        parsed_dict = {}
        reg_index = 0  # Registers ID could be the same, hence abstraction iterator is needed

        # --------------------------------------------------------------
        # Regex patterns
        # --------------------------------------------------------------
        # Gi1/0/1 (if_id: 75)
        int_reg = re.compile(r'(?P<interface_name>[a-zA-Z]+\d+(?:\/\d+)+)\s\(if_id\:\s(?P<if_id>\d+)\)')

        #  0000 : 1140                  Control Register :  0001 0001 0100 0000
        #  0001 : 796d                    Control STATUS :  0111 1001 0110 1101
        registers_reg = re.compile(
            r'(?P<register_number>\S{4})\s\:\s(?P<ieee_register_number>\S{4})\s+(?P<register_name>.*)\s\:\s+(?P<bits>.*)')

        # --------------------------------------------------------------
        # Build the parsed output
        # --------------------------------------------------------------
        for line in out.splitlines():
            line = line.strip()

            # Gi1/0/1 (if_id: 75)
            int_name = int_reg.match(line)
            if int_name:
                group = int_name.groupdict()
                for key in group.keys():
                    if group[key]:
                        parsed_dict[key] = group[key]
                continue

            #  0000 : 1140                  Control Register :  0001 0001 0100 0000
            #  0001 : 796d                    Control STATUS :  0111 1001 0110 1101
            register_line = registers_reg.match(line)
            if register_line:
                group = register_line.groupdict()
                parsed_dict['registers'][reg_index] = {'register_number': group['register_number'],
                                            'ieee_register_number': group['ieee_register_number'],
                                            'register_name': group['register_name'],
                                            'bits': group['bits'].replace(' ', '')}
                reg_index += 1
        return parsed_dict
