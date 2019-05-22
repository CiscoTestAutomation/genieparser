''' show_port_channel.py

NXOS parsers for the following show commands:
    * show port-channel summary
'''

# Python
import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Optional


# ======================================
# Schema for 'show port-channel summary'
# ======================================
class ShowPortChannelSummarySchema(MetaParser):
    
    '''Schema for:
        * 'show port-channel summary'
    '''

    schema = {
        'port_channel': 
            {Any(): 
                {'state': str,
                'group': int,
                'type': str,
                'protocol': str,
                'member': str,
                'ports': str,
                },
            },
        }


# ======================================
# Parser for 'show port-channel summary'
# ======================================
class ShowPortChannelSummary(ShowPortChannelSummarySchema):

    '''Parser for:
        * 'show port-channel summary'
    '''

    cli_command = ['show port-channel summary']

    def cli(self, output=None):

        if output is None:
            out = self.device.execute(self.cli_command[0])
        else:
            out = output

        # Init vars
        parsed_dict = {}
        acl_names = []

        # Group Port-       Type     Protocol  Member       Ports
        #       Channel
        # --------------------------------------------------------------------------------
        # 1     Po1(SU)     Eth      LACP      Eth3/1(P)    Eth3/2(P)
        p1 = re.compile(r'^(?P<group>(\d+)) +(?P<pch>([a-zA-Z0-9]+))\((?P<state>(\S+))\)'
                         ' +(?P<type>([a-zA-Z]+)) +(?P<protocol>([a-zA-Z]+))'
                         ' +(?P<member>(\S+)) +(?P<ports>(\S+))$')

        for line in out.splitlines():
            line = line.strip()

            m = p1.match(line)
            if m:
                group = m.groupdict()
                pch_dict = parsed_dict.setdefault('port_channel', {}).\
                                       setdefault(group['pch'], {})
                pch_dict['state'] = group['state']
                pch_dict['group'] = int(group['group'])
                pch_dict['type'] = group['type']
                pch_dict['protocol'] = group['protocol']
                pch_dict['member'] = group['member']
                pch_dict['ports'] = group['ports']
                continue

        return parsed_dict
