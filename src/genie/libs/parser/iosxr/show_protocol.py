''' show_protocol.py

IOSXR parsers for the following show commands:
    * show protocols afi-all all
'''

# Python
import re
import xmltodict
from netaddr import IPAddress

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Or, Optional
from genie.libs.parser.utils.common import Common


# =======================================
# Schema for 'show protocols afi-all all'
# =======================================
class ShowProtocolsAfiAllAllSchema(MetaParser):
    """Schema for show protocols afi-all all"""
    schema = {
        'protocols': 
            {Optional('ospf'): 
                {'vrf': 
                    {Any(): 
                        {'address_family': 
                            {Any(): 
                                {'instance': 
                                    {Any():
                                        {Optional('preference'): 
                                            {Optional('single_value'): 
                                                {'all': int},
                                            Optional('multi_values'): 
                                                {'granularity': 
                                                    {'detail': 
                                                        {'intra_area': int,
                                                        'inter_area': int,
                                                        },
                                                    },
                                                'external': int,
                                                },
                                            },
                                        'router_id': str,
                                        Optional('nsf'): bool,
                                        Optional('redistribution'): 
                                            {Optional('connected'): 
                                                {'enabled': bool,
                                                Optional('metric'): int},
                                            Optional('static'): 
                                                {'enabled': bool,
                                                Optional('metric'): int},
                                            Optional('bgp'): 
                                                {'bgp_id': int,
                                                Optional('metric'): int},
                                            Optional('isis'): 
                                                {'isis_pid': str,
                                                Optional('metric'): int}},
                                        Optional('areas'): 
                                            {Any(): 
                                                {'interfaces': list,
                                                Optional('mpls'): 
                                                    {Optional('te'): 
                                                        {Optional('enable'): bool}}}},
                                            },
                                        },
                                    },
                                },
                            },
                        },
                    },
            Optional('ospfv3'): 
                {'vrf': 
                    {Any(): 
                        {'address_family': 
                            {Any(): 
                                {'instance': 
                                    {Any():
                                        {Optional('preference'): 
                                            {Optional('single_value'): 
                                                {'all': int},
                                            Optional('multi_values'): 
                                                {'granularity': 
                                                    {'detail': 
                                                        {'intra_area': int,
                                                        'inter_area': int,
                                                        },
                                                    },
                                                'external': int,
                                                },
                                            },
                                        'router_id': str,
                                        Optional('nsf'): bool,
                                        Optional('redistribution'): 
                                            {Optional('connected'): 
                                                {'enabled': bool,
                                                Optional('metric'): int},
                                            Optional('static'): 
                                                {'enabled': bool,
                                                Optional('metric'): int},
                                            Optional('bgp'): 
                                                {'bgp_id': int,
                                                Optional('metric'): int},
                                            Optional('isis'): 
                                                {'isis_pid': str,
                                                Optional('metric'): int}},
                                        Optional('areas'): 
                                            {Any(): 
                                                {'interfaces': list,
                                                Optional('mpls'): 
                                                    {Optional('te'): 
                                                        {Optional('enable'): bool}}}},
                                            },
                                        },
                                    },
                                },
                            },
                        },
                    },
            Optional('bgp'): 
                {'bgp_pid': int,
                Optional('nsr'): 
                    {'enable': bool,
                    'current_state': str},
                Optional('graceful_restart'): 
                    {'enable': bool},
                Optional('address_family'): 
                    {Any(): 
                        {Optional('distance'): 
                            {Optional('external'): int,
                            Optional('internal'): int,
                            Optional('local'): int,
                            },
                        Optional('neighbors'): 
                            {Any(): 
                                {'last_update': str,
                                'gr_enable': str,
                                'nsr_state': str,
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
    """Parser for show protocols afi-all all"""

    cli_command = 'show protocols afi-all all'
    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output
        # Init vars
        ret_dict = {}

        for line in out.splitlines():
            line = line.strip()

            # Routing Protocol OSPF 1
            p1 = re.compile(r'^Routing +Protocol +(?P<pro>OSPF|OSPFv3) +(?P<pid>(\S+))$')
            m = p1.match(line)
            if m:
                instance = str(m.groupdict()['pid'])
                if 'protocols' not in ret_dict:
                    ret_dict['protocols'] = {}
                pro = m.groupdict()['pro'].lower()
                if pro not in ret_dict['protocols']:
                    ret_dict['protocols'][pro] = {}
                if 'vrf' not in ret_dict['protocols'][pro]:
                    ret_dict['protocols'][pro]['vrf'] = {}
                if 'default' not in ret_dict['protocols'][pro]['vrf']:
                    ret_dict['protocols'][pro]['vrf']['default'] = {}
                if 'address_family' not in ret_dict['protocols'][pro]['vrf']\
                        ['default']:
                    ret_dict['protocols'][pro]['vrf']['default']\
                        ['address_family'] = {}
                if 'ipv4' not in ret_dict['protocols'][pro]['vrf']['default']\
                        ['address_family']:
                    ret_dict['protocols'][pro]['vrf']['default']\
                        ['address_family']['ipv4'] = {}
                if 'instance' not in ret_dict['protocols'][pro]['vrf']\
                        ['default']['address_family']['ipv4']:
                    ret_dict['protocols'][pro]['vrf']['default']\
                        ['address_family']['ipv4']['instance'] = {}
                if instance not in ret_dict['protocols'][pro]['vrf']\
                        ['default']['address_family']['ipv4']['instance']:
                    ret_dict['protocols'][pro]['vrf']['default']\
                        ['address_family']['ipv4']['instance'][instance] = {}
                # Set ospf_dict
                ospf_dict = ret_dict['protocols'][pro]['vrf']['default']\
                        ['address_family']['ipv4']['instance'][instance]
                continue

            # Router Id: 10.36.3.3
            p2 = re.compile(r'^Router +Id: +(?P<router_id>(\S+))$')
            m = p2.match(line)
            if m:
                ospf_dict['router_id'] = str(m.groupdict()['router_id'])
                continue

            # Distance: 110
            p3_1 = re.compile(r'^Distance: +(?P<distance>(\d+))$')
            m = p3_1.match(line)
            if m:
                try:
                    ospf_dict
                except Exception:
                    continue
                if 'preference' not in ospf_dict:
                    ospf_dict['preference'] = {}
                if 'single_value' not in ospf_dict['preference']:
                    ospf_dict['preference']['single_value'] = {}
                ospf_dict['preference']['single_value']['all'] = \
                    int(m.groupdict()['distance'])
                continue

            # Distance: IntraArea 112 InterArea 113 External/NSSA 114
            p3_2 = re.compile(r'^Distance: +IntraArea +(?P<intra>(\d+))'
                               ' +InterArea +(?P<inter>(\d+)) +External\/NSSA'
                               ' +(?P<external>(\d+))$')
            m = p3_2.match(line)
            if m:
                if 'preference' not in ospf_dict:
                    ospf_dict['preference'] = {}
                if 'multi_values' not in ospf_dict['preference']:
                    ospf_dict['preference']['multi_values'] = {}
                if 'granularity' not in ospf_dict['preference']['multi_values']:
                    ospf_dict['preference']['multi_values']['granularity'] = {}
                if 'detail' not in ospf_dict['preference']['multi_values']\
                        ['granularity']:
                    ospf_dict['preference']['multi_values']['granularity']\
                        ['detail'] = {}
                ospf_dict['preference']['multi_values']['granularity']\
                        ['detail']['intra_area'] = int(m.groupdict()['intra'])
                ospf_dict['preference']['multi_values']['granularity']\
                        ['detail']['inter_area'] = int(m.groupdict()['inter'])
                ospf_dict['preference']['multi_values']['external'] = \
                    int(m.groupdict()['external'])
                continue

            # Non-Stop Forwarding: Disabled
            p4 = re.compile(r'^Non-Stop +Forwarding:'
                             ' +(?P<nsf>(Disabled|Enabled))$')
            m = p4.match(line)
            if m:
                if 'Disabled' in m.groupdict()['nsf']:
                    ospf_dict['nsf'] = False
                else:
                    ospf_dict['nsf'] = True
                    continue

            # Redistribution:
            #   connected
            #   connected with metric 10
            #   static
            #   static with metric 10
            p14 = re.compile(r'^(?P<type>(connected|static))(?: +with +metric'
                               ' +(?P<metric>(\d+)))?$')
            m = p14.match(line)
            if m:
                the_type = str(m.groupdict()['type'])
                if 'redistribution' not in ospf_dict:
                    ospf_dict['redistribution'] = {}
                if the_type not in ospf_dict['redistribution']:
                    ospf_dict['redistribution'][the_type] = {}
                ospf_dict['redistribution'][the_type]['enabled'] = True
                if m.groupdict()['metric']:
                    ospf_dict['redistribution'][the_type]['metric'] = \
                        int(m.groupdict()['metric'])
                    continue

            # Redistribution:
            #   bgp 100 with metric 111
            #   isis 10 with metric 3333
            p15 = re.compile(r'^(?P<prot>(bgp|isis)) +(?P<pid>(\d+))(?: +with'
                               ' +metric +(?P<metric>(\d+)))?$')
            m = p15.match(line)
            if m:
                prot = str(m.groupdict()['prot'])
                if prot not in ospf_dict['redistribution']:
                    ospf_dict['redistribution'][prot] = {}
                if prot == 'bgp':
                    ospf_dict['redistribution'][prot]['bgp_id'] = \
                        int(m.groupdict()['pid'])
                else:
                    ospf_dict['redistribution'][prot]['isis_pid'] = \
                        str(m.groupdict()['pid'])
                if m.groupdict()['metric']:
                    ospf_dict['redistribution'][prot]['metric'] = \
                        int(m.groupdict()['metric'])
                continue

            # Area 0
            p5 = re.compile(r'^Area +(?P<area>(\S+))$')
            m = p5.match(line)
            if m:
                area = str(IPAddress(str(m.groupdict()['area'])))
                area_interfaces = []
                if 'areas' not in ospf_dict:
                    ospf_dict['areas'] = {}
                if area not in ospf_dict['areas']:
                    ospf_dict['areas'][area] = {}
                ospf_dict['areas'][area]['interfaces'] = area_interfaces
                continue

            # MPLS/TE enabled
            p6 = re.compile(r'^MPLS\/TE +(?P<te>(enabled|disabled))$')
            m = p6.match(line)
            if m:
                if 'mpls' not in ospf_dict['areas'][area]:
                    ospf_dict['areas'][area]['mpls'] = {}
                if 'te' not in ospf_dict['areas'][area]['mpls']:
                    ospf_dict['areas'][area]['mpls']['te'] = {}
                if 'enabled' in m.groupdict()['te']:
                    ospf_dict['areas'][area]['mpls']['te']['enable'] = True
                else:
                    ospf_dict['areas'][area]['mpls']['te']['enable'] = False
                    continue

            # Loopback0
            # GigabitEthernet0/0/0/0
            # GigabitEthernet0/0/0/2
            p6 = re.compile(r'^(?P<intf>(Lo|Gi)[\w\/\.\-]+)$')
            m = p6.match(line)
            if m:
                area_interfaces.append(str(m.groupdict()['intf']))
                ospf_dict['areas'][area]['interfaces'] = area_interfaces
                continue

            # Routing Protocol "BGP 100"
            p8 = re.compile(r'^Routing +Protocol +\"BGP +(?P<bgp_pid>(\d+))\"$')
            m = p8.match(line)
            if m:
                if 'protocols' not in ret_dict:
                    ret_dict['protocols'] = {}
                if 'bgp' not in ret_dict['protocols']:
                    ret_dict['protocols']['bgp'] = {}

                # Set sub_dict
                bgp_dict = ret_dict['protocols']['bgp']
                bgp_dict['bgp_pid'] = int(m.groupdict()['bgp_pid'])
                continue

            # Non-stop routing is enabled
            p8 = re.compile(r'^Non-stop +routing +is'
                             ' +(?P<nsr>(enabled|disabled))$')
            m = p8.match(line)
            if m:
                if 'nsr' not in bgp_dict:
                    bgp_dict['nsr'] = {}
                if 'enabled' in m.groupdict()['nsr']:
                    bgp_dict['nsr']['enable'] = True
                else:
                    bgp_dict['nsr']['enable'] = False
                    continue

            # Graceful restart is not enabled
            p9 = re.compile(r'^Graceful restart is not +enabled$')
            m = p9.match(line)
            if m:
                if 'graceful_restart' not in bgp_dict:
                    bgp_dict['graceful_restart'] = {}
                bgp_dict['graceful_restart']['enable'] = False
                continue

            # Current BGP NSR state - Active Ready
            p10 = re.compile(r'^Current +BGP +NSR +state +\-'
                              ' +(?P<state>([a-zA-Z\s]+))$')
            m = p10.match(line)
            if m:
                if 'nsr' not in bgp_dict:
                    bgp_dict['nsr'] = {}
                bgp_dict['nsr']['current_state'] = \
                    str(m.groupdict()['state']).lower()
                continue

            # Address Family VPNv4 Unicast:
            # Address Family VPNv6 Unicast:
            p11 = re.compile(r'^Address +Family +(?P<af>([a-zA-Z0-9\s]+)):$')
            m = p11.match(line)
            if m:
                af = str(m.groupdict()['af']).lower()
                if 'address_family' not in bgp_dict:
                    bgp_dict['address_family'] = {}
                if af not in bgp_dict['address_family']:
                    bgp_dict['address_family'][af] = {}
                    continue

            # Distance: external 20 internal 200 local 200
            p12 = re.compile(r'^Distance: +external +(?P<ext>(\d+)) +internal'
                              ' +(?P<int>(\d+)) +local +(?P<local>(\d+))$')
            m = p12.match(line)
            if m:
                if 'distance' not in bgp_dict['address_family'][af]:
                    bgp_dict['address_family'][af]['distance'] = {}
                bgp_dict['address_family'][af]['distance']['external'] = \
                    int(m.groupdict()['ext'])
                bgp_dict['address_family'][af]['distance']['internal'] = \
                    int(m.groupdict()['int'])
                bgp_dict['address_family'][af]['distance']['local'] = \
                    int(m.groupdict()['local'])
                continue

            # Neighbor      State/Last update received  NSR-State  GR-Enabled
            # 10.64.4.4       08:05:59                    None       No
            # 10.64.4.4       08:05:59                    None       No
            p13 = re.compile(r'^(?P<nbr>([0-9\.]+)) +(?P<last_update>([0-9\:]+))'
                              ' +(?P<nsr_state>(\S+)) +(?P<gr_en>(No|Yes))$')
            m = p13.match(line)
            if m:
                nbr = str(m.groupdict()['nbr'])
                if 'neighbors' not in bgp_dict['address_family'][af]:
                    bgp_dict['address_family'][af]['neighbors'] = {}
                if nbr not in bgp_dict['address_family'][af]['neighbors']:
                    bgp_dict['address_family'][af]['neighbors'][nbr] = {}
                bgp_dict['address_family'][af]['neighbors'][nbr]['last_update'] = \
                    str(m.groupdict()['last_update'])
                bgp_dict['address_family'][af]['neighbors'][nbr]['nsr_state'] = \
                    str(m.groupdict()['nsr_state'])
                bgp_dict['address_family'][af]['neighbors'][nbr]['gr_enable'] = \
                    str(m.groupdict()['gr_en'])
                continue

        return ret_dict
