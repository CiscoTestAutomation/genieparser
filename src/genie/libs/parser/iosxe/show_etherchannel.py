''' show_etherchannel.py

IOSXE parsers for the following show commands:
    * show etherchannel summary
'''

# Python
import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Optional


# ======================================
# Schema for 'show etherchannel summary'
# ======================================
class ShowEtherchannelSummarySchema(MetaParser):
    
    '''Schema for:
        * 'show etherchannel summary'
    '''

    schema = {
        'port_channel': 
            {Any(): 
                {'group': int,
                'protocol': str,
                'ports': str,
                },
            },
        }


# ======================================
# Parser for 'show etherchannel summary'
# ======================================
class ShowEtherchannelSummary(ShowEtherchannelSummarySchema):

    '''Parser for:
        * 'show etherchannel summary'
    '''

    cli_command = ['show etherchannel summary']

    def cli(self, output=None):

        if output is None:
            out = self.device.execute(self.cli_command[0])
        else:
            out = output

        # Init vars
        parsed_dict = {}
        acl_names = []

        # Group  Port-channel    Protocol    Ports
        # --------------------------------------------------------------------------------
        # 1      Po1(SU)         LACP        Gi1/0/2(P)  Gi1/0/3(P)
        p1 = re.compile(r'^(?P<group>(\d+)) +(?P<pch>(\S+))'
                         ' +(?P<protocol>([a-zA-Z]+))'
                         ' +(?P<ports>([a-zA-Z0-9\/\(\)\s]+))$')

        for line in out.splitlines():
            line = line.strip()

            m = p1.match(line)
            if m:
                group = m.groupdict()
                pch_dict = parsed_dict.setdefault('port_channel', {}).\
                                       setdefault(group['pch'], {})
                pch_dict['group'] = int(group['group'])
                pch_dict['protocol'] = group['protocol']
                pch_dict['ports'] = group['ports']
                continue

        return parsed_dict
