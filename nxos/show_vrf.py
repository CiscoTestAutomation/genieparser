''' show_bgp.py

NXOS parsers for the following show commands:
    * 'show vrf'
'''

# Python
import re
import xmltodict

# Metaparser
from metaparser import MetaParser
from metaparser.util.schemaengine import Schema, Any, Optional, Or, And,\
                                         Default, Use


# =====================
# Parser for 'show vrf'
# =====================

class ShowVrfSchema(MetaParser):
    
    '''Schema for show vrf'''

    schema = {
        'vrfs':
            {Any():
                {'vrf_id': int,
                 'vrf_state': str,
                 'reason': str,},
            },
        }

class ShowVrf(ShowVrfSchema):
    
    '''Parser for show vrf'''

    def cli(self):
        cmd = 'show vrf'
        out = self.device.execute(cmd)
        
        # Init vars
        vrf_dict = {}

        for line in out.splitlines():
            line = line.rstrip()

            # VRF2                                    4 Up      --
            # default                                 1 Up      --
            p1 = re.compile(r'^\s*(?P<vrf_name>(\S+)) +(?P<vrf_id>[0-9]+)'
                             ' +(?P<vrf_state>(Up|Down)) +(?P<reason>(\S+))$')
            m = p1.match(line)
            if m:
                if 'vrfs' not in vrf_dict:
                    vrf_dict['vrfs'] = {}
                vrf_name = str(m.groupdict()['vrf_name'])
                if vrf_name not in vrf_dict['vrfs']:
                    vrf_dict['vrfs'][vrf_name] = {}
                vrf_dict['vrfs'][vrf_name]['vrf_id'] = \
                    int(m.groupdict()['vrf_id'])
                vrf_dict['vrfs'][vrf_name]['vrf_state'] = \
                    str(m.groupdict()['vrf_state'])
                vrf_dict['vrfs'][vrf_name]['reason'] = \
                    str(m.groupdict()['reason'])
                continue

        return vrf_dict

# vim: ft=python et sw=4
