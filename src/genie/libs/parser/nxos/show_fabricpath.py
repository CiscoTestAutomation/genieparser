from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Or, Optional

# ==============================
# Schema for 'show fabricpath isis adjacency'
# ==============================
class ShowFabricpathIsisAdjacencySchema(MetaParser):

    ''' Schema for "show fabricpath isis adjacency" '''

# These are the key-value pairs to add to the parsed dictionary

    schema = {
        Any():
            {'adj-hold-time-out': str,
            'adj-intf-name-out': str,
            'adj-sys-name-out': str,
             'adj-state-out':str}
    }

# Python (this imports the Python re module for RegEx)
import re

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

        p1 = re.compile(r'Sessions +for +VRF +(?P<vrf>(\S+)),'
                        ' +total: +(?P<total>(\d+)),'
                        ' +established: +(?P<established>(\d+))$')


        # Defines the regex for the next line of device output, which is:
        # System ID       SNPA            Level  State  Hold Time  Interface
        # Switch-A           N/A             1      UP     00:00:28   port-channel1

        p1 = re.compile(r'(?P<peer>(\S+)) + (?P<snpa>(\S+)) + (?P<level>(\d+)) +(?P<state>(UP|DOWN)) + (?P<time>(\S+)) + (?P<interface>(\S+))$')

        # Defines the "for" loop, to pattern match each line of output

        for line in out.splitlines():
            line = line.strip()

            # Processes the matched patterns for the second line of output
            m = p1.match(line)
            if m:
                group = m.groupdict()
                peer = group['peer']
                peer_dict = {peer:{'adj-hold-time-out':'', 'adj-intf-name-out':'','adj-state-out':'','adj-sys-name-out':''}}
                peer_dict[peer]['adj-intf-name-out'] = group['interface']
                peer_dict[peer]['adj-hold-time-out'] = group['time']
                peer_dict[peer]['adj-state-out'] = group['state']
                peer_dict[peer]['adj-sys-name-out'] = group['peer']
                parsed_dict.update(peer_dict)
                continue

        return parsed_dict