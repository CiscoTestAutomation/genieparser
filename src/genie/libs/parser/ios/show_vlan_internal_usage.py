'''
Author: Mehdi Cherifi
Twitter: https://twitter.com/LocketKeepsake
Github: https://github.com/cherifimehdi

'''
import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any


# ====================================================
#  Schema for 'show vlan internal usage' command
# ====================================================
class ShowVlanInternalUsageSchema(MetaParser):
    """Schema for:
        show vlan internal usage"""

    schema = {
        'Internal Vlan': {
            Any(): {
                        'Usage': str,
            },
        }
    }

# =================================================
# Parser for 'show vlan internal usage' command
# =================================================
class ShowVlanInternalUsage(ShowVlanInternalUsageSchema):

    cli_command = 'show vlan internal usage'

    def cli(self, output=None):

        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output


    #VLAN Usage
    #---- --------------------
    #1006 GigabitEthernet0/0
    #1007 GigabitEthernet0/1
    #1008 GigabitEthernet0/2

        # pattern to capture 'VLAN' and 'Usage'
        p0 = re.compile(r'^(?P<VLAN>[0-9]+)\s+(?P<Usage>.+)$')
        parsed_dict = {}

        for line in out.splitlines():
            line = line.strip()

            m = p0.match(line)
            if m:
                internal_vlan_dict=parsed_dict.setdefault('Internal Vlan', {})
                Usage=m.groupdict()['Usage']
                VLAN=m.groupdict()['VLAN']
                internal_vlan_dict[VLAN] = {}
                internal_vlan_dict[VLAN]['Usage']=Usage
                continue
        return parsed_dict
