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
        'internal_vlan': {
            Any(): {
                        'usage': str,
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
                internal_vlan_dict = parsed_dict.setdefault('internal_vlan', {})
                usage = m.groupdict()['Usage']
                vlan = m.groupdict()['VLAN']
                vlan_dict = internal_vlan_dict[vlan].set_default(vlan, {})
                vlan_dict['usage'] = usage
                continue
        return parsed_dict
