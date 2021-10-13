"""
IOSXE C9300 parsers for the following show commands:
    * show controllers ethernet-controllers {interface} phy detail
"""
# Python
import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any


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
                 'hex_bit_value': str,
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

    def cli(self, interface='', output=None):
        if output is None:
            out = self.device.execute(self.cli_command.format(interface=interface))
        else:
            out = output

        parsed_dict = {}
        registers_dict = {}
        reg_index = 0  # Registers ID could be the same, hence abstraction iterator is needed

        # --------------------------------------------------------------
        # Regex patterns
        # --------------------------------------------------------------
        # Gi1/0/1 (if_id: 75)
        int_reg = re.compile(r'(?P<interface_name>[a-zA-Z]+\d+(?:\/\d+)+)\s\(if_id\:\s(?P<if_id>\d+)\)')

        #  0000 : 1140                  Control Register :  0001 0001 0100 0000
        #  0001 : 796d                    Control STATUS :  0111 1001 0110 1101
        registers_reg = re.compile(
            r'(?P<register_number>\S{4})\s\:\s(?P<hex_bit_value>\S{4})\s+(?P<register_name>.*)\s\:\s+(?P<bits>.*)')

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
                registers_dict[str(reg_index)] = {'register_number': group['register_number'],
                                                  'hex_bit_value': group['hex_bit_value'],
                                                  'register_name': group['register_name'],
                                                  'bits': group['bits'].replace(' ', '')}
                reg_index += 1
                continue
            parsed_dict['registers'] = registers_dict
        return parsed_dict
