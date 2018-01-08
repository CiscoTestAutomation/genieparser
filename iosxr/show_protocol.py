''' show_protocol.py

IOSXR parsers for the following show commands:
    * show protocols afi-all all
'''

# Python
import re
import xmltodict
from netaddr import IPAddress

# Metaparser
from metaparser import MetaParser
from metaparser.util.schemaengine import Schema, Any, Or, Optional
from parser.utils.common import Common


# =======================================
# Schema for 'show protocols afi-all all'
# =======================================
class ShowProtocolsAfiAllAllSchema(MetaParser):

    schema = {
        'protocols': 
            {Any(): 
                {'vrf': 
                    {Any(): 
                        {'address_family': 
                            {Any(): 
                                {'instance': 
                                    {Any():
                                        {'preference': 
                                            {'single_value': 
                                                {'all': int,
                                                },
                                            },
                                        'router_id': str,
                                        'nsf': bool,
                                        Optional('redistribution'): 
                                            {'bgp': 
                                                {'bgp_id': int,
                                                'metric': int,
                                                'metric_type': str,
                                                'nssa_only': bool,
                                                'route_map': str,
                                                'subnets': bool,
                                                'tag': int,
                                                'lsa_type_summary': bool,
                                                'preserve_med': bool,
                                                },
                                            },
                                        },
                                    },
                                },
                            },
                        },
                    },
                },
            },
        }


# =======================================
# Parser for 'show protocols afi-all all'
# =======================================
class ShowProtocolsAfiAllAll(ShowProtocolsAfiAllAllSchema):

     ''' Parser for "show protocols afi-all all" '''
     def cli(self):

        # Execute command on device
        out = self.device.execute('show protocols afi-all all')

        # Init vars
        ret_dict = {}

        for line in out.splitlines():
            line = line.strip()

            # Routing Protocol OSPF 1
            p1 = re.compile(r'^Routing +Protocol +OSPF +(?P<pid>(\d+))$')
            m = p1.match(line)
            if m:
                instance = str(m.groupdict()['pid'])
                if 'protocols' not in ret_dict:
                    ret_dict['protocols'] = {}
                if 'ospf' not in ret_dict['protocols']:
                    ret_dict['protocols']['ospf'] = {}
                if 'vrf' not in ret_dict['protocols']['ospf']:
                    ret_dict['protocols']['ospf']['vrf'] = {}
                if 'default' not in ret_dict['protocols']['ospf']['vrf']:
                    ret_dict['protocols']['ospf']['vrf']['default'] = {}
                if 'address_family' not in ret_dict['protocols']['ospf']['vrf']\
                        ['default']:
                    ret_dict['protocols']['ospf']['vrf']['default']\
                        ['address_family'] = {}
                if 'ipv4' not in ret_dict['protocols']['ospf']['vrf']['default']\
                        ['address_family']:
                    ret_dict['protocols']['ospf']['vrf']['default']\
                        ['address_family']['ipv4'] = {}
                if 'instance' not in ret_dict['protocols']['ospf']['vrf']\
                        ['default']['address_family']['ipv4']:
                    ret_dict['protocols']['ospf']['vrf']['default']\
                        ['address_family']['ipv4']['instance'] = {}
                if instance not in ret_dict['protocols']['ospf']['vrf']\
                        ['default']['address_family']['ipv4']['instance']:
                    ret_dict['protocols']['ospf']['vrf']['default']\
                        ['address_family']['ipv4']['instance'][instance] = {}
                # Set ospf_dict
                ospf_dict = ret_dict['protocols']['ospf']['vrf']['default']\
                        ['address_family']['ipv4']['instance'][instance]
                continue

            # Router Id: 3.3.3.3
            p2 = re.compile(r'^Router +Id: +(?P<router_id>(\S+))$')
            m = p2.match(line)
            if m:
                ospf_dict['router_id'] = str(m.groupdict()['router_id'])
                continue

            # Distance: 110
            p3 = re.compile(r'^Distance: +(?P<distance>(\d+))$')
            m = p3.match(line)
            if m:
                if 'preference' not in ospf_dict:
                    ospf_dict['preference'] = {}
                if 'single_value' not in ospf_dict['preference']:
                    ospf_dict['preference']['single_value'] = {}
                ospf_dict['preference']['single_value']['all'] = \
                    int(m.groupdict()['distance'])
                continue

            # Non-Stop Forwarding: Disabled
            p4 = re.compile(r'^Non-Stop +Forwarding: +(?P<nsf>(Disabled|Enabled))$')
            m = p4.match(line)
            if m:
                if 'Disabled' in m.groupdict()['nsf']:
                    ospf_dict['nsf'] = False
                else:
                    ospf_dict['nsf'] = True
                    continue

            # Redistribution:
            # None
            # Area 0
            # MPLS/TE enabled
            # Loopback0
            # GigabitEthernet0/0/0/0
            # GigabitEthernet0/0/0/2


            # Routing Protocol "BGP 100"
            # Non-stop routing is enabled
            # Graceful restart is not enabled
            # Current BGP NSR state - Active Ready
            # BGP NSR state not ready: Wait for standby ready msg

            # Address Family VPNv4 Unicast:
            # Distance: external 20 internal 200 local 200
            # Routing Information Sources:
            # Neighbor      State/Last update received  NSR-State  GR-Enabled
            # 4.4.4.4       08:05:59                    None       No

            # Address Family VPNv6 Unicast:
            # Distance: external 20 internal 200 local 200
            # Routing Information Sources:
            # Neighbor      State/Last update received  NSR-State  GR-Enabled
            # 4.4.4.4       08:05:59                    None       No

        return ret_dict
