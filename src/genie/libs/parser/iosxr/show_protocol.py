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
                                            Optional('ospf'): 
                                                {'ospf_id': int,
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
                                            Optional('ospf'): 
                                                {'ospf_id': int,
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
                        Optional('sourced_networks'): list,
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
    exclude = ['last_update', 'current_state']

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
            p1 = re.compile(r'^Routing +Protocol +(?P<pro>OSPF|OSPFv3) +(?P<pid>\S+)$')
            m = p1.match(line)
            if m:
                instance = str(m.groupdict()['pid'])
                pro = m.groupdict()['pro'].lower()
                # Set ospf_dict
                ospf_dict = ret_dict.setdefault('protocols', {}).setdefault(pro, {}) \
                            .setdefault('vrf', {}).setdefault('default', {}) \
                            .setdefault('address_family', {}).setdefault('ipv4', {}) \
                            .setdefault('instance', {}).setdefault(instance, {})
                continue

            # Router Id: 10.36.3.3
            p2 = re.compile(r'^Router +Id: +(?P<router_id>\S+)$')
            m = p2.match(line)
            if m:
                ospf_dict['router_id'] = str(m.groupdict()['router_id'])
                continue

            # Distance: 110
            p3_1 = re.compile(r'^Distance: +(?P<distance>\d+)$')
            m = p3_1.match(line)
            if m:
                try:
                    ospf_dict
                except Exception:
                    continue
                
                sub_dict = ospf_dict.setdefault('preference', {}) \
                                    .setdefault('single_value', {})
                sub_dict['all'] = int(m.groupdict()['distance'])
                continue

            # Distance: IntraArea 112 InterArea 113 External/NSSA 114
            p3_2 = re.compile(r'^Distance: +IntraArea +(?P<intra>\d+)'
                               ' +InterArea +(?P<inter>\d+) +External\/NSSA'
                               ' +(?P<external>\d+)$')
            m = p3_2.match(line)
            if m:
                sub_dict = ospf_dict.setdefault('preference', {}) \
                                    .setdefault('multi_values', {}) \
                                    .setdefault('granularity', {}) \
                                    .setdefault('detail', {})
                sub_dict['intra_area'] = int(m.groupdict()['intra'])
                sub_dict['inter_area'] = int(m.groupdict()['inter'])
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
                               ' +(?P<metric>\d+))?$')
            m = p14.match(line)
            if m:
                the_type = str(m.groupdict()['type'])
                sub_dict = ospf_dict.setdefault('redistribution', {}).setdefault(the_type, {})
                sub_dict['enabled'] = True
                if m.groupdict()['metric']:
                    sub_dict['metric'] = int(m.groupdict()['metric'])
                continue

            # Redistribution:
            #   bgp 100 with metric 111
            #   isis 10 with metric 3333
            #   ospf 99
            p15 = re.compile(r'^(?!Area)(?P<prot>\w+) +(?P<pid>\d+)(?: +with'
                               ' +metric +(?P<metric>\d+))?$')
            m = p15.match(line)
            if m:
                group = m.groupdict()
                prot = group['prot'].lower()
                sub_dict = ospf_dict.setdefault('redistribution', {}).setdefault(prot, {})
                if prot == 'isis':
                    sub_dict['isis_pid'] = str(group['pid'])
                else:
                    sub_dict[prot + '_id'] = int(group['pid'])
                if m.groupdict()['metric']:
                    sub_dict['metric'] = int(group['metric'])
                continue

            # Area 0
            p5 = re.compile(r'^Area +(?P<area>\S+)$')
            m = p5.match(line)
            if m:
                area = str(IPAddress(m.groupdict()['area']))
                area_interfaces = []
                area_dict = ospf_dict.setdefault('areas', {}).setdefault(area, {})
                area_dict['interfaces'] = area_interfaces
                continue

            # MPLS/TE enabled
            p6 = re.compile(r'^MPLS\/TE +(?P<te>(enabled|disabled))$')
            m = p6.match(line)
            if m:
                sub_dict = area_dict.setdefault('mpls', {}).setdefault('te', {})
                if 'enabled' in m.groupdict()['te']:
                    sub_dict['enable'] = True
                else:
                    sub_dict['enable'] = False
                continue

            # Loopback0
            # GigabitEthernet0/0/0/0
            # GigabitEthernet0/0/0/2
            # TenGigabitEthernet0/0/0/2
            p6 = re.compile(r'^(?P<intf>(Lo|Gi|Te|Bu)[\w\/\.\-]+)$')
            m = p6.match(line)
            if m:
                area_interfaces.append(m.groupdict()['intf'])
                continue

            # Routing Protocol "BGP 100"
            p8 = re.compile(r'^Routing +Protocol +\"BGP +(?P<bgp_pid>\d+)\"$')
            m = p8.match(line)
            if m:
                # Set sub_dict
                bgp_dict = ret_dict.setdefault('protocols', {}).setdefault('bgp', {})
                bgp_dict['bgp_pid'] = int(m.groupdict()['bgp_pid'])
                continue

            # Non-stop routing is enabled
            p8 = re.compile(r'^Non-stop +routing +is +(?P<nsr>(enabled|disabled))$')
            m = p8.match(line)
            if m:
                nsr_dict = bgp_dict.setdefault('nsr', {})
                if 'enabled' in m.groupdict()['nsr']:
                    nsr_dict['enable'] = True
                else:
                    nsr_dict['enable'] = False
                continue

            # Graceful restart is not enabled
            p9 = re.compile(r'^Graceful restart is not +enabled$')
            m = p9.match(line)
            if m:
                sub_dict = bgp_dict.setdefault('graceful_restart', {})
                sub_dict['enable'] = False
                continue

            # Current BGP NSR state - Active Ready
            p10 = re.compile(r'^Current +BGP +NSR +state +\-'
                              ' +(?P<state>([\w\s]+))$')
            m = p10.match(line)
            if m:
                nsr_dict = bgp_dict.setdefault('nsr', {})
                
                nsr_dict['current_state'] = m.groupdict()['state'].lower()
                continue

            # Address Family VPNv4 Unicast:
            # Address Family VPNv6 Unicast:
            p11 = re.compile(r'^Address +Family +(?P<af>[\w\s\-]+):$')
            m = p11.match(line)
            if m:
                af = m.groupdict()['af'].lower()
                af_dict = bgp_dict.setdefault('address_family', {}).setdefault(af, {})
                continue

            # Distance: external 20 internal 200 local 200
            p12 = re.compile(r'^Distance: +external +(?P<external>\d+) +internal'
                              ' +(?P<internal>\d+) +local +(?P<local>\d+)$')
            m = p12.match(line)
            if m:
                group = m.groupdict()
                dist_dict = af_dict.setdefault('distance', {})
                dist_dict.update({k: int(v) for k, v in group.items()})
                continue

            # Sourced Networks:
            p_sn = re.compile(r'(?i)^Sourced +Networks:$')
            m = p_sn.match(line)
            if m:
                src_networks = []
                sn_dict = af_dict.setdefault('sourced_networks', src_networks)
                continue

            # 10.10.10.0/30
            # 2001:db8:7000:8::/64
            p_sn2 = re.compile(r'^(?P<src>[\d\.\:\/]+)$')
            m = p_sn2.match(line)
            if m:
                try:
                    src_networks.append(m.groupdict()['src'])
                except Exception:
                    continue
                    
                continue

            # Neighbor      State/Last update received  NSR-State  GR-Enabled
            # 10.64.4.4       08:05:59                    None       No
            # 10.64.4.4       08:05:59                    None       No
            # 172.25.12.17    1w0d                        None       Yes
            # 2001:db8:7000:13::1   1w0d                 None       Yes
            p13 = re.compile(r'^(?P<nbr>[\d\:\.]+) +(?P<last_update>[\w\:]+)'
                              ' +(?P<nsr_state>\S+) +(?P<gr_enable>No|Yes)$')
            m = p13.match(line)
            if m:
                group = m.groupdict()
                nbr = group.pop('nbr')
                nbr_dict = af_dict.setdefault('neighbors', {}).setdefault(nbr, {})
                nbr_dict.update({k:v for k, v in group.items()})
                continue

        return ret_dict


class ShowProtocolsSchema(MetaParser):
    """Schema for show protocols {protocol}"""
    schema = {
        'protocols': {
            Optional('ospf'): {
                'vrf': {
                    Any(): {
                        'address_family': {
                            Any(): {
                                'instance': {
                                    Any(): {
                                        Optional('preference'): {
                                            Optional('single_value'): {
                                                'all': int
                                            },
                                            Optional('multi_values'): {
                                                'granularity': {
                                                    'detail': {
                                                        'intra_area': int,
                                                        'inter_area': int,
                                                    },
                                                },
                                                'external': int,
                                                },
                                            },
                                        'router_id': str,
                                        Optional('nsf'): bool,
                                        Optional('redistribution'): {
                                            Optional('connected'): {
                                                'enabled': bool,
                                                Optional('metric'): int},
                                            Optional('static'): {
                                                'enabled': bool,
                                                Optional('metric'): int
                                            },
                                            Optional('bgp'): {
                                                'bgp_id': int,
                                                Optional('metric'): int
                                            },
                                            Optional('ospf'): {
                                                'ospf_id': int,
                                                Optional('metric'): int
                                            },
                                            Optional('isis'): {
                                                'isis_id': int,
                                                Optional('metric'): int
                                            }
                                        },
                                        Optional('areas'): {
                                            Any(): {
                                                'interfaces': list,
                                                Optional('mpls'): {
                                                    Optional('te'): {
                                                        Optional('enabled'): bool
                                                    }
                                                }
                                            }
                                        },
                                    },
                                },
                            },
                        },
                    },
                },
            },
            Optional('ospfv3'): {
                'vrf': {
                    Any(): {
                        'address_family': {
                            Any(): {
                                'instance': {
                                    Any(): {
                                        Optional('preference'): {
                                            Optional('single_value'): {
                                                'all': int
                                            },
                                            Optional('multi_values'): {
                                                'granularity': {
                                                    'detail': {
                                                        'intra_area': int,
                                                        'inter_area': int,
                                                    },
                                                },
                                                'external': int,
                                            },
                                        },
                                        'router_id': str,
                                        Optional('nsf'): bool,
                                        Optional('redistribution'): {
                                            Optional('connected'): {
                                                'enabled': bool,
                                                Optional('metric'): int
                                            },
                                            Optional('static'): {
                                                'enabled': bool,
                                                Optional('metric'): int
                                            },
                                            Optional('bgp'): {
                                                'bgp_id': int,
                                                Optional('metric'): int
                                            },
                                            Optional('ospf'): {
                                                'ospf_id': int,
                                                Optional('metric'): int
                                            },
                                            Optional('isis'): {
                                                'isis_id': int,
                                                Optional('metric'): int
                                            }
                                        },
                                        Optional('areas'): {
                                            Any(): {
                                                'interfaces': list,
                                                Optional('mpls'): {
                                                    Optional('te'): {
                                                        Optional('enabled'): bool
                                                    }
                                                }
                                            }
                                        },
                                    },
                                },
                            },
                        },
                    },
                },
            },
            Optional('bgp'): {
                'bgp_pid': int,
                Optional('nsr'): {
                    'enabled': bool,
                    'current_state': str
                },
                Optional('graceful_restart'): {
                    'enable': bool
                },
                Optional('address_family'): {
                    Any(): {
                        Optional('distance'): {
                            Optional('external'): int,
                            Optional('internal'): int,
                            Optional('local'): int,
                        },
                        Optional('sourced_networks'): list,
                        Optional('neighbors'): {
                            Any(): {
                                'last_update': str,
                                Optional('gr_enable'): str,
                                Optional('nsr_state'): str,
                            },
                        },
                    },
                },
            },
        },
    }


class ShowProtocols(ShowProtocolsSchema):
    """Parser for show protocols {protocol}"""
    cli_command = 'show protocols {protocol}'

    def cli(self, protocol="", output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        result_dict = {}

        # Routing Protocol OSPF mpls1
        p1 = re.compile(r'^Routing +Protocol +(?P<protocol>(OSPF(v3)?))'
                        ' +(?P<pid>\S+)$')

        # Router Id: 10.94.1.1
        p2 = re.compile(r'^Router +Id: +(?P<router_id>\S+)$')

        # Distance: 110
        p3 = re.compile(r'^Distance: +(?P<distance>\d+)$')

        # Distance: IntraArea 112 InterArea 113 External/NSSA 114
        p4 = re.compile(r'^Distance: +IntraArea +(?P<intra>\d+)'
                        ' +InterArea +(?P<inter>\d+) +External\/NSSA'
                        ' +(?P<external>\d+)$')

        # Non-Stop Forwarding: Enabled
        # Non-Stop Forwarding: Disabled
        p5 = re.compile(r'^Non-Stop +Forwarding:'
                        ' +(?P<nsf>(Disabled|Enabled))$')

        # Redistribution:
        #   connected
        #   connected with metric 10
        #   static
        #   static with metric 100
        p6 = re.compile(r'^(?P<type>(connected|static))(?: +with +metric'
                        ' +(?P<metric>\d+))?$')

        # Redistribution:
        #   bgp 100 with metric 111
        #   isis 10 with metric 3333
        p7 = re.compile(r'^(?!Area)(?P<prot>\w+) +(?P<pid>\d+)(?: +with'
                        ' +metric +(?P<metric>\d+))?$')

        # Area 0
        p8 = re.compile(r'^Area +(?P<area>\S+)$')

        #   MPLS/TE enabled
        p9 = re.compile(r'^MPLS\/TE +(?P<mpls_te>(enabled|disabled))$')

        #   Loopback0
        #   GigabitEthernet0/0/0/0
        #   GigabitEthernet0/0/0/1
        p10 = re.compile(r'^(?P<interface>(Loopback|(Ten)?GigabitEthernet)'
                        '[\d\/]+)$')

        # Routing Protocol "BGP 40"
        p11 = re.compile(r'^Routing +Protocol +\"BGP +(?P<bgp_pid>\d+)\"$')

        # Non-stop routing is enabled
        p12 = re.compile(r'^Non-stop +routing +is +'
                         '(?P<nsr>(enabled|disabled))$')

        # Graceful restart is enabled
        p13 = re.compile(r'^Graceful restart is not +enabled$')

        # Current BGP NSR state - TCP Initial Sync
        p14 = re.compile(r'^Current +BGP +NSR +state +\-'
                         ' +(?P<state>([\w\s]+))$')

        # Address Family IPv4 Unicast:
        # Address Family VPNv6 Unicast:
        p15 = re.compile(r'^Address +Family +(?P<af>[\w\s\-]+):$')

        # Distance: external 20 internal 200 local 200
        p16 = re.compile(r'^Distance: +external +(?P<external>\d+) +internal'
                         ' +(?P<internal>\d+) +local +(?P<local>\d+)$')

        # Sourced Networks:
        p17 = re.compile(r'^Sourced +Networks:$')

        # 10.100.0.0/16 backdoor
        # 10.100.1.0/24
        p18 = re.compile(r'^(?P<src>[\d\.\:\/]+ *(backdoor)?)$')

        # Neighbor          State/Last update received
        # 10.5.0.2          Idle
        # Neighbor      State/Last update received  NSR-State  GR-Enabled
        # 10.64.4.4       08:05:59                    None       No
        p19 = re.compile(r'^(?P<nbr>[\d\:\.]+) +(?P<last_update>[\w\:]+)'
                         '( +(?P<nsr_state>\S+) +(?P<gr_enable>No|Yes))?$')

        for line in out.splitlines():
            line = line.strip()

            # Routing Protocol OSPF mpls1
            m = p1.match(line)
            if m:
                group = m.groupdict()
                instance = group['pid']
                protocol = group['protocol'].lower()
                prot_dict = result_dict.setdefault('protocols', {})\
                                       .setdefault(protocol, {})\
                                       .setdefault('vrf', {})\
                                       .setdefault('default', {})\
                                       .setdefault('address_family', {})\
                                       .setdefault('ipv4', {})\
                                       .setdefault('instance', {})\
                                       .setdefault(instance, {})
                continue

            # Router Id: 10.94.1.1
            m = p2.match(line)
            if m:
                group = m.groupdict()
                prot_dict['router_id'] = group['router_id']
                continue

            # Distance: 110
            m = p3.match(line)
            if m:
                group = m.groupdict()
                sub_dict = prot_dict.setdefault('preference', {})\
                                    .setdefault('single_value', {})

                sub_dict.update({
                    'all': int(group['distance'])
                })

                continue

            # Distance: IntraArea 112 InterArea 113 External/NSSA 114
            m = p4.match(line)
            if m:
                group = m.groupdict()
                multi_values_dict = prot_dict.setdefault('preference', {})\
                                             .setdefault('multi_values', {})

                sub_dict = multi_values_dict.setdefault('granularity', {})\
                                            .setdefault('detail', {})

                sub_dict.update({
                    'intra_area': int(group['intra']),
                    'inter_area': int(group['inter'])
                })

                multi_values_dict.update({
                    'external': int(group['external'])
                })

                continue

            # Non-Stop Forwarding: Enabled
            # Non-Stop Forwarding: Disabled
            m = p5.match(line)
            if m:
                group = m.groupdict()
                if group['nsf'] == 'Enabled':
                    prot_dict['nsf'] = True
                else:
                    prot_dict['nsf'] = False

                continue

            # Redistribution:
            #   connected
            #   connected with metric 10
            #   static
            #   static with metric 100
            m = p6.match(line)
            if m:
                group = m.groupdict()
                redistrib_dict = prot_dict.setdefault('redistribution', {})
                redist = {
                    'enabled': True
                }

                if group['metric']:
                    redist['metric'] = int(group['metric'])

                redistrib_dict.update({group['type']: redist})

            # Redistribution:
            #   bgp 100 with metric 111
            #   isis 10 with metric 3333
            m = p7.match(line)
            if m:
                group = m.groupdict()
                prot = group['prot'].lower()
                redistrib_dict = prot_dict.setdefault('redistribution', {})\
                                          .setdefault(prot, {})

                redistrib_dict[prot + '_id'] = int(group['pid'])

                if m.groupdict()['metric']:
                    redistrib_dict['metric'] = int(group['metric'])
                continue

            # Area 0
            m = p8.match(line)
            if m:
                group = m.groupdict()
                areas_dict = prot_dict.setdefault('areas', {})
                area_dict = areas_dict.setdefault(group['area'], {})
                area_dict['interfaces'] = []
                continue

            # MPLS/TE enabled
            m = p9.match(line)
            if m:
                group = m.groupdict()
                mpls_dict = area_dict.setdefault('mpls', {})\
                                     .setdefault('te', {})

                if group['mpls_te'] == 'enabled':
                    mpls_dict['enabled'] = True
                else:
                    mpls_dict['enabled'] = False

                continue

            #   Loopback0
            #   GigabitEthernet0/0/0/0
            #   GigabitEthernet0/0/0/1
            m = p10.match(line)
            if m:
                group = m.groupdict()
                area_dict['interfaces'].append(group['interface'])
                continue

            # Routing Protocol "BGP 40"
            m = p11.match(line)
            if m:
                group = m.groupdict()
                prot_dict = result_dict.setdefault('protocols', {})\
                                       .setdefault('bgp', {})
                prot_dict['bgp_pid'] = int(group['bgp_pid'])
                continue

            # Non-stop routing is enabled
            m = p12.match(line)
            if m:
                group = m.groupdict()
                nsr_dict = prot_dict.setdefault('nsr', {})
                if group['nsr'] == 'enabled':
                    nsr_dict['enabled'] = True
                else:
                    nsr_dict['enabled'] = False
                continue

            # Graceful restart is not enabled
            m = p13.match(line)
            if m:
                gr_dict = prot_dict.setdefault('graceful_restart', {})
                gr_dict['enable'] = False
                continue

            # Current BGP NSR state - Active Ready
            m = p14.match(line)
            if m:
                group = m.groupdict()
                nsr_dict = prot_dict.setdefault('nsr', {})

                nsr_dict['current_state'] = group['state'].lower()
                continue

            # Address Family VPNv6 Unicast:
            m = p15.match(line)
            if m:
                group = m.groupdict()
                af_dict = prot_dict.setdefault('address_family', {})\
                                   .setdefault(group['af'], {})

                continue

            # Distance: external 20 internal 200 local 200
            m = p16.match(line)
            if m:
                group = m.groupdict()
                dist_dict = af_dict.setdefault('distance', {})
                dist_dict.update({k: int(v) for k, v in group.items()})
                continue

            # Sourced Networks:
            m = p17.match(line)
            if m:
                sn_dict = af_dict.setdefault('sourced_networks', [])
                continue

            # 10.100.0.0/16 backdoor
            # 10.100.1.0/24
            m = p18.match(line)
            if m:
                group = m.groupdict()
                sn_dict.append(group['src'])
                continue

            # Neighbor          State/Last update received
            # 10.5.0.2          Idle
            # Neighbor      State/Last update received  NSR-State  GR-Enabled
            # 10.64.4.4       08:05:59                    None       No
            m = p19.match(line)
            if m:
                group = m.groupdict()
                neighbor = group['nbr']
                neighbors_dict = af_dict.setdefault('neighbors', {})\
                                        .setdefault(neighbor, {})

                neighbors_dict['last_update'] = group['last_update']

                if group['nsr_state']:
                    neighbors_dict['nsr_state'] = group['nsr_state']

                if group['gr_enable']:
                    neighbors_dict['gr_enable'] = group['gr_enable']
                continue

        return result_dict
