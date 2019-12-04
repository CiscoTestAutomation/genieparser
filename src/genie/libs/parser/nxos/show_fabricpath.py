# Python (this imports the Python re module for RegEx)
import re
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Or, Optional
from genie.libs.parser.utils.common import Common

# ==============================
# Schema for 'show fabricpath isis adjacency'
# ==============================
class ShowFabricpathIsisAdjacencySchema(MetaParser):

    ''' Schema for "show fabricpath isis adjacency" '''

# These are the key-value pairs to add to the parsed dictionary

    # schema = {
    #     Any():
    #         {'adj-hold-time-out': str,
    #         'adj-intf-name-out': str,
    #         'adj-sys-name-out': str,
    #          'adj-state-out':str}
    # }
    schema = {
        'domain': {
            Any(): {
                Optional('interfaces'): {
                    Any(): {
                        'system_id': str,
                        'snpa': str,
                        'level': int,
                        'state': str,
                        'hold_time': str,
                    }
                }
            }
        }
    }



# ==============================
# Parser for 'show fabricpath isis adjacency'
# ==============================

# The parser class inherits from the schema class
class ShowFabricpathIsisAdjacency(ShowFabricpathIsisAdjacencySchema):

    ''' Parser for "show fabricpath isis adjacency"'''

    cli_command = 'show fabricpath isis adjacency'

    # Defines a function to run the cli_command
    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        # Initializes the Python dictionary variable
        parsed_dict = {}

        # Defines the regex for the first line of device output, which is:
        # Sessions for VRF default, total: 3, established: 3

        p1 = re.compile(r'Fabricpath IS-IS domain: +(?P<domain>(\S+)) +Fabricpath IS-IS adjacency database:$')

        # Defines the regex for the next line of device output, which is:
        # System ID       SNPA            Level  State  Hold Time  Interface
        # Switch-A           N/A             1      UP     00:00:28   port-channel1

        p2 = re.compile(
            r'(?P<system_id>(\S+)) + (?P<snpa>(\S+)) + (?P<level>(\d+)) +(?P<state>(UP|DOWN)) + (?P<hold_time>(\S+)) + (?P<interface>(\S+))$')

        for line in out.splitlines():
            line = line.strip()

            # IS-IS Process: test VRF: default
            m = p1.match(line)
            if m:
                group = m.groupdict()
                domain = group['domain']
                intf_dict = parsed_dict.setdefault('domain', {}). \
                    setdefault(domain, {})


            m = p2.match(line)
            if m:
                group = m.groupdict()
                system_id = group['system_id']
                snpa = group['snpa']
                level = int(group['level'])
                state = group['state']
                hold_time = group['hold_time']
                interface = Common.convert_intf_name(group['interface'])
                level_dict = intf_dict.setdefault('interfaces', {}).setdefault(interface, {})
                level_dict.update({'system_id': system_id})
                level_dict.update({'snpa': snpa})
                level_dict.update({'level': level})
                level_dict.update({'state': state})
                level_dict.update({'hold_time': hold_time})


        return parsed_dict