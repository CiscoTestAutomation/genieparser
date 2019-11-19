import unittest
from unittest.mock import Mock
# ATS
from ats.topology import Device

from genie.metaparser.util.exceptions import SchemaEmptyParserError, \
                                       SchemaMissingKeyError

from genie.libs.parser.iosxe.show_routing import ShowIpRoute,\
                                                 ShowIpRouteWord,\
                                                 ShowIpv6RouteUpdated,\
                                                 ShowIpCef,\
                                                 ShowIpv6Cef,\
                                                 ShowIpCefDetail,\
                                                 ShowIpRouteSummary, \
                                                 ShowIpv6Route, \
                                                 ShowIpv6RouteWord, \
                                                 ShowIpCefInternal


# ============================================
# unit test for 'show ip route'
# =============================================
class TestShowIpRoute(unittest.TestCase):
    """
       unit test for show ip route
    """
    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}
 
    golden_output_1 = {'execute.return_value': '''
        R1_iosv#show ip route
        Codes: L - local, C - connected, S - static, R - RIP, M - mobile, B - BGP
               D - EIGRP, EX - EIGRP external, O - OSPF, IA - OSPF inter area
               N1 - OSPF NSSA external type 1, N2 - OSPF NSSA external type 2
               E1 - OSPF external type 1, E2 - OSPF external type 2
               i - IS-IS, su - IS-IS summary, L1 - IS-IS level-1, L2 - IS-IS level-2
               ia - IS-IS inter area, * - candidate default, U - per-user static route
               o - ODR, P - periodic downloaded static route, H - NHRP, l - LISP
               a - application route
               + - replicated route, % - next hop override

        Gateway of last resort is not set

              10.1.0.0/32 is subnetted, 1 subnets
        C        10.4.1.1 is directly connected, Loopback0
              10.4.0.0/32 is subnetted, 1 subnets
        S        10.16.2.2 [1/0] via 10.186.2.2, GigabitEthernet0/1
                         [1/0] via 10.1.2.2, GigabitEthernet0/0
              10.9.0.0/32 is subnetted, 1 subnets
        S        10.36.3.3 is directly connected, GigabitEthernet0/3
                         is directly connected, GigabitEthernet0/2
              10.0.0.0/8 is variably subnetted, 5 subnets, 2 masks
        C        10.1.2.0/24 is directly connected, GigabitEthernet0/0
        L        10.1.2.1/32 is directly connected, GigabitEthernet0/0
        C        10.1.3.0/24 is directly connected, GigabitEthernet0/2
        L        10.1.3.1/32 is directly connected, GigabitEthernet0/2
        O        10.2.3.0/24 [110/2] via 10.186.2.2, 06:46:59, GigabitEthernet0/1
                             [110/2] via 10.1.2.2, 06:46:59, GigabitEthernet0/0
               10.229.0.0/32 is subnetted, 1 subnets
        i L1     10.151.22.22 [115/20] via 10.186.2.2, 06:47:04, GigabitEthernet0/1
                         [115/20] via 10.1.2.2, 06:47:04, GigabitEthernet0/0
              10.4.0.0/32 is subnetted, 1 subnets
        B        10.16.32.32 [200/0] via 10.66.12.12, 1d00h
        '''}

    golden_parsed_output_1 = {
        'vrf':{
            'default':{
                'address_family': {
                    'ipv4': {
                        'routes': {
                            '10.4.1.1/32': {
                                'route': '10.4.1.1/32',
                                'active': True,
                                'source_protocol_codes': 'C',
                                'source_protocol':'connected',
                                'next_hop': {
                                    'outgoing_interface': {
                                        'Loopback0': {
                                            'outgoing_interface': 'Loopback0',
                                        },
                                    },
                                },
                            },
                            '10.16.2.2/32': {
                                'route': '10.16.2.2/32',
                                'active': True,
                                'route_preference': 1,
                                'metric': 0,
                                'source_protocol_codes': 'S',
                                'source_protocol': 'static',
                                'next_hop': {
                                    'next_hop_list': {
                                        1: {
                                            'index': 1,
                                            'next_hop': '10.186.2.2',
                                            'outgoing_interface': 'GigabitEthernet0/1',
                                        },
                                        2: {
                                            'index': 2,
                                            'next_hop': '10.1.2.2',
                                            'outgoing_interface': 'GigabitEthernet0/0',
                                        },
                                    },
                                },
                            },
                            '10.36.3.3/32': {
                                'route': '10.36.3.3/32',
                                'active': True,
                                'source_protocol_codes': 'S',
                                'source_protocol': 'static',
                                'next_hop': {
                                    'outgoing_interface': {
                                        'GigabitEthernet0/3': {
                                            'outgoing_interface': 'GigabitEthernet0/3',
                                        },
                                        'GigabitEthernet0/2': {
                                            'outgoing_interface': 'GigabitEthernet0/2',
                                        },
                                    },
                                },
                            },
                            '10.1.2.0/24': {
                                'route': '10.1.2.0/24',
                                'active': True,
                                'source_protocol_codes': 'C',
                                'source_protocol': 'connected',
                                'next_hop': {
                                    'outgoing_interface': {
                                        'GigabitEthernet0/0': {
                                            'outgoing_interface': 'GigabitEthernet0/0',
                                        },
                                    },

                                },
                            },
                            '10.1.2.1/32': {
                                'route': '10.1.2.1/32',
                                'active': True,
                                'source_protocol_codes': 'L',
                                'source_protocol': 'local',
                                'next_hop': {
                                    'outgoing_interface': {
                                        'GigabitEthernet0/0': {
                                            'outgoing_interface': 'GigabitEthernet0/0',
                                        },
                                    },

                                },
                            },
                            '10.1.3.0/24': {
                                'route': '10.1.3.0/24',
                                'active': True,
                                'source_protocol_codes': 'C',
                                'source_protocol': 'connected',
                                'next_hop': {
                                    'outgoing_interface': {
                                        'GigabitEthernet0/2': {
                                            'outgoing_interface': 'GigabitEthernet0/2',
                                        },
                                    },
                                },
                            },
                            '10.1.3.1/32': {
                                'route': '10.1.3.1/32',
                                'active': True,
                                'source_protocol_codes': 'L',
                                'source_protocol': 'local',
                                'next_hop': {
                                    'outgoing_interface': {
                                        'GigabitEthernet0/2': {
                                            'outgoing_interface': 'GigabitEthernet0/2',
                                        },
                                    },
                                },
                            },
                            '10.2.3.0/24': {
                                'route': '10.2.3.0/24',
                                'active': True,
                                'route_preference': 110,
                                'metric': 2,
                                'source_protocol_codes': 'O',
                                'source_protocol': 'ospf',
                                'next_hop': {
                                    'next_hop_list': {
                                        1: {
                                            'index': 1,
                                            'next_hop': '10.186.2.2',
                                            'updated': '06:46:59',
                                            'outgoing_interface': 'GigabitEthernet0/1',
                                        },
                                        2: {
                                            'index': 2,
                                            'next_hop': '10.1.2.2',
                                            'updated': '06:46:59',
                                            'outgoing_interface': 'GigabitEthernet0/0',
                                        },
                                    },
                                },
                            },
                            '10.151.22.22/32': {
                                'route': '10.151.22.22/32',
                                'active': True,
                                'route_preference': 115,
                                'metric': 20,
                                'source_protocol_codes': 'i L1',
                                'source_protocol': 'isis',
                                'next_hop': {
                                    'next_hop_list': {
                                        1: {
                                            'index': 1,
                                            'next_hop': '10.186.2.2',
                                            'updated': '06:47:04',
                                            'outgoing_interface': 'GigabitEthernet0/1',
                                        },
                                        2: {
                                            'index': 2,
                                            'next_hop': '10.1.2.2',
                                            'updated': '06:47:04',
                                            'outgoing_interface': 'GigabitEthernet0/0',
                                        },
                                    },
                                },
                            },
                            '10.16.32.32/32': {
                                'route': '10.16.32.32/32',
                                'active': True,
                                'route_preference': 200,
                                'metric': 0,
                                'source_protocol_codes': 'B',
                                'source_protocol': 'bgp',
                                'next_hop': {
                                    'next_hop_list': {
                                        1: {
                                            'index': 1,
                                            'next_hop': '10.66.12.12',
                                            'updated': '1d00h',
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

    golden_output_2_with_vrf = {'execute.return_value':'''
        PE1#sh ip route vrf VRF1
        Routing Table: VRF1
        Codes: L - local, C - connected, S - static, R - RIP, M - mobile, B - BGP
               D - EIGRP, EX - EIGRP external, O - OSPF, IA - OSPF inter area
               N1 - OSPF NSSA external type 1, N2 - OSPF NSSA external type 2
               E1 - OSPF external type 1, E2 - OSPF external type 2
               i - IS-IS, su - IS-IS summary, L1 - IS-IS level-1, L2 - IS-IS level-2
               ia - IS-IS inter area, * - candidate default, U - per-user static route
               o - ODR, P - periodic downloaded static route, H - NHRP, l - LISP
               a - application route
               + - replicated route, % - next hop override, p - overrides from PfR

        Gateway of last resort is not set

              10.0.0.0/24 is subnetted, 50 subnets
        O        10.0.0.0 [110/1] via 10.81.1.2, 01:02:20, GigabitEthernet0/0/2.100
        O        10.0.1.0 [110/1] via 10.81.1.2, 01:02:20, GigabitEthernet0/0/2.100
        O        10.0.2.0 [110/1] via 10.81.1.2, 01:02:20, GigabitEthernet0/0/2.100
              10.145.0.0/24 is subnetted, 50 subnets
        B        10.145.0.0 [200/1] via 192.168.51.1, 01:01:10
        B        10.145.1.0 [200/1] via 192.168.51.1, 01:01:10
        B        10.145.2.0 [200/1] via 192.168.51.1, 01:01:10
              10.81.0.0/8 is variably subnetted, 2 subnets, 2 masks
        C        10.81.1.0/24 is directly connected, GigabitEthernet0/0/2.100
        L        10.81.1.1/32 is directly connected, GigabitEthernet0/0/2.100
        B     192.168.4.0/24 [200/0] via 192.168.51.1, 01:01:10
        '''}

    golden_parsed_output_2_with_vrf = {
        'vrf': {
            'VRF1': {
                'address_family': {
                    'ipv4': {
                        'routes': {
                            '10.0.0.0/24': {
                                'route': '10.0.0.0/24',
                                'active': True,
                                'route_preference': 110,
                                'metric': 1,
                                'source_protocol_codes': 'O',
                                'source_protocol': 'ospf',
                                'next_hop': {
                                    'next_hop_list': {
                                        1: {
                                            'index': 1,
                                            'next_hop': '10.81.1.2',
                                            'updated': '01:02:20',
                                            'outgoing_interface': 'GigabitEthernet0/0/2.100',
                                        },
                                    },
                                },
                            },
                            '10.0.1.0/24': {
                                'route': '10.0.1.0/24',
                                'active': True,
                                'route_preference': 110,
                                'metric': 1,
                                'source_protocol_codes': 'O',
                                'source_protocol': 'ospf',
                                'next_hop': {
                                    'next_hop_list': {
                                        1: {
                                            'index': 1,
                                            'next_hop': '10.81.1.2',
                                            'updated': '01:02:20',
                                            'outgoing_interface': 'GigabitEthernet0/0/2.100',
                                        },
                                    },
                                },
                            },
                            '10.0.2.0/24': {
                                'route': '10.0.2.0/24',
                                'active': True,
                                'route_preference': 110,
                                'metric': 1,
                                'source_protocol_codes': 'O',
                                'source_protocol': 'ospf',
                                'next_hop': {
                                    'next_hop_list': {
                                        1: {
                                            'index': 1,
                                            'next_hop': '10.81.1.2',
                                            'updated': '01:02:20',
                                            'outgoing_interface': 'GigabitEthernet0/0/2.100',
                                        },
                                    },
                                },
                            },
                            '10.145.0.0/24': {
                                'route': '10.145.0.0/24',
                                'active': True,
                                'route_preference': 200,
                                'metric': 1,
                                'source_protocol_codes': 'B',
                                'source_protocol': 'bgp',
                                'next_hop': {
                                    'next_hop_list': {
                                        1: {
                                            'index': 1,
                                            'next_hop': '192.168.51.1',
                                            'updated': '01:01:10',
                                        },
                                    },
                                },
                            },
                            '10.145.1.0/24': {
                                'route': '10.145.1.0/24',
                                'active': True,
                                'route_preference': 200,
                                'metric': 1,
                                'source_protocol_codes': 'B',
                                'source_protocol': 'bgp',
                                'next_hop': {
                                    'next_hop_list': {
                                        1: {
                                            'index': 1,
                                            'next_hop': '192.168.51.1',
                                            'updated': '01:01:10',
                                        },
                                    },
                                },
                            },
                            '10.145.2.0/24': {
                                'route': '10.145.2.0/24',
                                'active': True,
                                'route_preference': 200,
                                'metric': 1,
                                'source_protocol_codes': 'B',
                                'source_protocol': 'bgp',
                                'next_hop': {
                                    'next_hop_list': {
                                        1: {
                                            'index': 1,
                                            'next_hop': '192.168.51.1',
                                            'updated': '01:01:10',
                                        },
                                    },
                                },
                            },
                            '10.81.1.0/24': {
                                'route': '10.81.1.0/24',
                                'active': True,
                                'source_protocol_codes': 'C',
                                'source_protocol': 'connected',
                                'next_hop': {
                                    'outgoing_interface': {
                                        'GigabitEthernet0/0/2.100': {
                                            'outgoing_interface': 'GigabitEthernet0/0/2.100',
                                        },
                                    },
                                },
                            },
                            '10.81.1.1/32': {
                                'route': '10.81.1.1/32',
                                'active': True,
                                'source_protocol_codes': 'L',
                                'source_protocol': 'local',
                                'next_hop': {
                                    'outgoing_interface': {
                                        'GigabitEthernet0/0/2.100': {
                                            'outgoing_interface': 'GigabitEthernet0/0/2.100',
                                        },
                                    },
                                },
                            },
                            '192.168.4.0/24': {
                                'route': '192.168.4.0/24',
                                'active': True,
                                'route_preference':200,
                                'metric':0,
                                'source_protocol_codes': 'B',
                                'source_protocol': 'bgp',
                                'next_hop': {
                                    'next_hop_list': {
                                        1: {
                                            'index': 1,
                                            'next_hop': '192.168.51.1',
                                            'updated': '01:01:10'},
                                        },
                                    },
                                },
                            },
                        },
                    },
                },
            },
        }

    golden_parsed_output3 = {
        'vrf': 
            {
            'OOB_Mgmt': 
                {
                'address_family': 
                    {
                    'ipv4': 
                        {
                        'routes': 
                            {
                            '0.0.0.0/0': 
                                { 
                                'active': True,
                                'metric': 0,
                                'next_hop': 
                                    {
                                    'next_hop_list': 
                                        {
                                        1: {
                                            'index': 1,
                                            'next_hop': '10.50.15.1'
                                           }
                                        }
                                    },
                                    'route': '0.0.0.0/0',
                                    'route_preference': 1,
                                    'source_protocol': 'static',
                                    'source_protocol_codes': 'S*'
                                },
                            '10.50.15.0/25': 
                                {
                                'active': True,
                                'next_hop': 
                                    {
                                    'outgoing_interface': 
                                        {
                                        'FastEthernet0/0': 
                                            {
                                            'outgoing_interface': 'FastEthernet0/0'
                                            }
                                        }
                                    },
                                'route': '10.50.15.0/25',
                                'source_protocol': 'connected',
                                'source_protocol_codes': 'C'
                                },
                            '10.50.15.12/32': 
                                {
                                'active': True,
                                'next_hop': 
                                    {
                                    'outgoing_interface': 
                                        {
                                        'FastEthernet0/0': 
                                            {
                                            'outgoing_interface': 'FastEthernet0/0'
                                            }
                                        }
                                    },
                                'route': '10.50.15.12/32',
                                'source_protocol': 'local',
                                'source_protocol_codes': 'L'
                                }
                            }
                        }
                    }
                }
            }
        }

    golden_output3 = {'execute.return_value': '''
        Router#show ip route vrf OOB_Mgmt

        Routing Table: OOB_Mgmt
        Codes: L - local, C - connected, S - static, R - RIP, M - mobile, B - BGP
               D - EIGRP, EX - EIGRP external, O - OSPF, IA - OSPF inter area 
               N1 - OSPF NSSA external type 1, N2 - OSPF NSSA external type 2
               E1 - OSPF external type 1, E2 - OSPF external type 2
               i - IS-IS, su - IS-IS summary, L1 - IS-IS level-1, L2 - IS-IS level-2
               ia - IS-IS inter area, * - candidate default, U - per-user static route
               o - ODR, P - periodic downloaded static route, H - NHRP, l - LISP
               a - application route
               + - replicated route, % - next hop override, p - overrides from PfR

        Gateway of last resort is 10.50.15.1 to network 0.0.0.0

        S*    0.0.0.0/0 [1/0] via 10.50.15.1
              10.0.0.0/8 is variably subnetted, 2 subnets, 2 masks
        C        10.50.15.0/25 is directly connected, FastEthernet0/0
        L        10.50.15.12/32 is directly connected, FastEthernet0/0
        '''}

    golden_parsed_output4 = {
        'vrf': 
            {'default': 
                {'address_family': 
                    {'ipv4': 
                        {'routes': 
                            {'0.0.0.0/0': 
                                {'active': True,
                                'metric': 100,
                                'next_hop': 
                                    {'next_hop_list': 
                                        {1: 
                                            {'index': 1,
                                            'next_hop': '10.12.7.37',
                                            'outgoing_interface': 'Vlan101',
                                            'updated': '3w6d'},
                                        2: 
                                            {'index': 2,
                                            'next_hop': '10.12.7.33',
                                            'outgoing_interface': 'Vlan100',
                                            'updated': '3w6d'}}},
                                    'route': '0.0.0.0/0',
                                    'route_preference': 115,
                                    'source_protocol': 'isis',
                                    'source_protocol_codes': 'i*L1'},
                            '10.12.6.1/32': 
                                {'active': True,
                                'metric': 200,
                                'next_hop': 
                                    {'next_hop_list': 
                                        {1: 
                                            {'index': 1,
                                            'next_hop': '10.12.7.33',
                                            'outgoing_interface': 'Vlan100',
                                            'updated': '1w1d'}}},
                                'route': '10.12.6.1/32',
                                'route_preference': 115,
                                'source_protocol': 'isis',
                                'source_protocol_codes': 'i ia'},
                            '10.12.6.10/32': 
                                {'active': True,
                                'metric': 200,
                                'next_hop': 
                                    {'next_hop_list': 
                                        {1: 
                                            {'index': 1,
                                            'next_hop': '10.12.7.33',
                                            'outgoing_interface': 'Vlan100',
                                            'updated': '2w1d'}}},
                                    'route': '10.12.6.10/32',
                                    'route_preference': 115,
                                    'source_protocol': 'isis',
                                    'source_protocol_codes': 'i ia'},
                            '10.12.6.13/32': 
                                {'active': True,
                                'metric': 250,
                                'next_hop': 
                                    {'next_hop_list': 
                                        {1: 
                                            {'index': 1,
                                            'next_hop': '10.12.7.33',
                                            'outgoing_interface': 'Vlan100',
                                            'updated': '2w1d'}}},
                                'route': '10.12.6.13/32',
                                'route_preference': 115,
                                'source_protocol': 'isis',
                                'source_protocol_codes': 'i ia'},
                            '10.12.6.14/32': 
                                {'active': True,
                                'metric': 300,
                                'next_hop': 
                                    {'next_hop_list': 
                                        {1: 
                                            {'index': 1,
                                            'next_hop': '10.12.7.37',
                                            'outgoing_interface': 'Vlan101',
                                            'updated': '2w1d'},
                                        2: 
                                            {'index': 2,
                                            'next_hop': '10.12.7.33',
                                            'outgoing_interface': 'Vlan100',
                                            'updated': '2w1d'}}},
                                'route': '10.12.6.14/32',
                                'route_preference': 115,
                                'source_protocol': 'isis',
                                'source_protocol_codes': 'i ia'},
                            '10.12.6.15/32': 
                                {'active': True,
                                'metric': 250,
                                'next_hop': 
                                    {'next_hop_list': 
                                        {1: 
                                            {'index': 1,
                                            'next_hop': '10.12.7.37',
                                            'outgoing_interface': 'Vlan101',
                                            'updated': '2w1d'}}},
                                'route': '10.12.6.15/32',
                                'route_preference': 115,
                                'source_protocol': 'isis',
                                'source_protocol_codes': 'i ia'},
                            '10.12.6.2/32': 
                                {'active': True,
                                'metric': 100,
                                'next_hop': 
                                    {'next_hop_list': 
                                        {1: 
                                            {'index': 1,
                                            'next_hop': '10.12.7.33',
                                            'outgoing_interface': 'Vlan100',
                                            'updated': '6w0d'}}},
                                'route': '10.12.6.2/32',
                                'route_preference': 115,
                                'source_protocol': 'isis',
                                'source_protocol_codes': 'i L1'},
                            '10.12.6.3/32': 
                                {'active': True,
                                'metric': 100,
                                'next_hop': 
                                    {'next_hop_list': 
                                        {1: 
                                            {'index': 1,
                                            'next_hop': '10.12.7.37',
                                            'outgoing_interface': 'Vlan101',
                                            'updated': '3w6d'}}},
                                'route': '10.12.6.3/32',
                                'route_preference': 115,
                                'source_protocol': 'isis',
                                'source_protocol_codes': 'i L1'},
                            '10.12.6.4/32': 
                                {'active': True,
                                'metric': 50,
                                'next_hop': 
                                    {'next_hop_list': 
                                        {1: 
                                            {'index': 1,
                                            'next_hop': '10.12.7.33',
                                            'outgoing_interface': 'Vlan100',
                                            'updated': '6w0d'}}},
                                'route': '10.12.6.4/32',
                                'route_preference': 115,
                                'source_protocol': 'isis',
                                'source_protocol_codes': 'i L1'},
                            '10.12.6.7/32': 
                                {'active': True,
                                'metric': 50,
                                'next_hop': 
                                    {'next_hop_list': 
                                        {1: 
                                            {'index': 1,
                                            'next_hop': '10.12.7.37',
                                            'outgoing_interface': 'Vlan101',
                                            'updated': '3w6d'}}},
                                'route': '10.12.6.7/32',
                                'route_preference': 115,
                                'source_protocol': 'isis',
                                'source_protocol_codes': 'i L1'},
                            '10.12.6.9/32': 
                                {'active': True,
                                'next_hop': 
                                    {'outgoing_interface': 
                                        {'Loopback0': 
                                            {'outgoing_interface': 'Loopback0'}}},
                                'route': '10.12.6.9/32',
                                'source_protocol': 'connected',
                                'source_protocol_codes': 'C'},
                            '10.12.7.32/30': 
                                {'active': True,
                                'next_hop': 
                                    {'outgoing_interface': 
                                        {'Vlan100': 
                                            {'outgoing_interface': 'Vlan100'}}},
                                'route': '10.12.7.32/30',
                                'source_protocol': 'connected',
                                'source_protocol_codes': 'C'},
                            '10.12.7.34/32': 
                                {'active': True,
                                'next_hop': 
                                    {'outgoing_interface': 
                                        {'Vlan100': 
                                            {'outgoing_interface': 'Vlan100'}}},
                                'route': '10.12.7.34/32',
                                'source_protocol': 'local',
                                'source_protocol_codes': 'L'},
                            '10.12.7.36/30': 
                                {'active': True,
                                'next_hop': 
                                    {'outgoing_interface': 
                                        {'Vlan101': 
                                            {'outgoing_interface': 'Vlan101'}}},
                                'route': '10.12.7.36/30',
                                'source_protocol': 'connected',
                                'source_protocol_codes': 'C'},
                            '10.12.7.38/32': 
                                {'active': True,
                                'next_hop': 
                                    {'outgoing_interface': 
                                        {'Vlan101': 
                                            {'outgoing_interface': 'Vlan101'}}},
                                'route': '10.12.7.38/32',
                                'source_protocol': 'local',
                                'source_protocol_codes': 'L'}}}}}}}

    golden_output4 = {'execute.return_value': '''
        Router#show ip route
        Codes: L - local, C - connected, S - static, R - RIP, M - mobile, B - BGP
               D - EIGRP, EX - EIGRP external, O - OSPF, IA - OSPF inter area 
               N1 - OSPF NSSA external type 1, N2 - OSPF NSSA external type 2
               E1 - OSPF external type 1, E2 - OSPF external type 2
               i - IS-IS, su - IS-IS summary, L1 - IS-IS level-1, L2 - IS-IS level-2
               ia - IS-IS inter area, * - candidate default, U - per-user static route
               o - ODR, P - periodic downloaded static route, H - NHRP, l - LISP
               a - application route
               + - replicated route, % - next hop override, p - overrides from PfR

        Gateway of last resort is 10.12.7.37 to network 0.0.0.0

        i*L1  0.0.0.0/0 [115/100] via 10.12.7.37, 3w6d, Vlan101
                        [115/100] via 10.12.7.33, 3w6d, Vlan100
              10.0.0.0/8 is variably subnetted, 14 subnets, 2 masks
        i ia     10.12.6.1/32 [115/200] via 10.12.7.33, 1w1d, Vlan100
        i L1     10.12.6.2/32 [115/100] via 10.12.7.33, 6w0d, Vlan100
        i L1     10.12.6.3/32 [115/100] via 10.12.7.37, 3w6d, Vlan101
        i L1     10.12.6.4/32 [115/50] via 10.12.7.33, 6w0d, Vlan100
        i L1     10.12.6.7/32 [115/50] via 10.12.7.37, 3w6d, Vlan101
        C        10.12.6.9/32 is directly connected, Loopback0
        i ia     10.12.6.10/32 [115/200] via 10.12.7.33, 2w1d, Vlan100
        i ia     10.12.6.13/32 [115/250] via 10.12.7.33, 2w1d, Vlan100
        i ia     10.12.6.14/32 [115/300] via 10.12.7.37, 2w1d, Vlan101
                                [115/300] via 10.12.7.33, 2w1d, Vlan100
        i ia     10.12.6.15/32 [115/250] via 10.12.7.37, 2w1d, Vlan101
        C        10.12.7.32/30 is directly connected, Vlan100
        L        10.12.7.34/32 is directly connected, Vlan100
        C        10.12.7.36/30 is directly connected, Vlan101
        L        10.12.7.38/32 is directly connected, Vlan101
        '''}

    golden_parsed_output5 = {
        "vrf": {
            "default": {
                "address_family": {
                    "ipv4": {
                        "routes": {
                            "10.1.1.0/24": {
                                "active": True,
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "10.4.1.1",
                                            "updated": "01:40:40"
                                        }
                                    }
                                },
                                "source_protocol": "bgp",
                                "metric": 2219,
                                "route_preference": 200,
                                "source_protocol_codes": "B",
                                "route": "10.1.1.0/24"
                            }
                        }
                    }
                }
            }
        }
    }

    golden_output5 = {'execute.return_value': '''
          R1#show ip route bgp
          IPv6 Routing Table - default - 5 entries
          Codes: C - Connected, L - Local, S - Static, U - Per-user Static route
                 B - BGP, R - RIP, H - NHRP, I1 - ISIS L1
                 I2 - ISIS L2, IA - ISIS interarea, IS - ISIS summary, D - EIGRP
                 EX - EIGRP external, ND - ND Default, NDp - ND Prefix, DCE - Destination
                 NDr - Redirect, RL - RPL, O - OSPF Intra, OI - OSPF Inter
                 OE1 - OSPF ext 1, OE2 - OSPF ext 2, ON1 - OSPF NSSA ext 1
                 ON2 - OSPF NSSA ext 2, la - LISP alt, lr - LISP site-registrations
                 ld - LISP dyn-eid, a - Application
                10.225.0.0/24 is subnetted, 5 subnets
          B        10.1.1.0 [200/2219] via 10.4.1.1, 01:40:40
          '''}

    golden_parsed_output6 = {
        "vrf": {
            "default": {
                "address_family": {
                    "ipv6": {
                        "routes": {
                            "2001:2:2:2::2/128": {
                                "active": True,
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "2001:DB8:1:1::2"
                                        }
                                    }
                                },
                                "source_protocol": "local_connected",
                                "metric": 0,
                                "route_preference": 200,
                                "source_protocol_codes": "LC",
                                "route": "2001:2:2:2::2/128"
                            },
                            "2001:db8:cdc9:1b9::/64": {
                                "active": True,
                                "metric": 2219,
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "10.4.1.1",
                                            "vrf": "default"
                                        }
                                    }
                                },
                                "route": "2001:db8:cdc9:1b9::/64",
                                "route_preference": 200,
                                "source_protocol": "bgp",
                                "source_protocol_codes": "B"
                            }
                        }
                    }
                }
            }
        }
    }

    golden_output6 = {'execute.return_value': '''
          R1#show ipv6 route bgp
          IPv6 Routing Table - default - 5 entries
          Codes: C - Connected, L - Local, S - Static, U - Per-user Static route
                 B - BGP, R - RIP, H - NHRP, I1 - ISIS L1
                 I2 - ISIS L2, IA - ISIS interarea, IS - ISIS summary, D - EIGRP
                 EX - EIGRP external, ND - ND Default, NDp - ND Prefix, DCE - Destination
                 NDr - Redirect, RL - RPL, O - OSPF Intra, OI - OSPF Inter
                 OE1 - OSPF ext 1, OE2 - OSPF ext 2, ON1 - OSPF NSSA ext 1
                 ON2 - OSPF NSSA ext 2, la - LISP alt, lr - LISP site-registrations
                 ld - LISP dyn-eid, a - Application
        LC   2001:2:2:2::2/128 [200/0]
               via 2001:DB8:1:1::2
          B   2001:db8:cdc9:1b9::/64 [200/2219]
            via 10.4.1.1%default, indirectly connected
    '''}

    golden_parsed_output7 = {
        "vrf": {
            "default": {
                "address_family": {
                    "ipv6": {
                        "routes": {
                            "FF00::/8": {
                                "route": "FF00::/8",
                                "active": True,
                                "metric": 0,
                                "route_preference": 0,
                                "source_protocol_codes": "L",
                                "source_protocol": "local",
                                "next_hop": {
                                    "outgoing_interface": {
                                        "Null0": {
                                            "outgoing_interface": "Null0"
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }

    golden_output7 = {'execute.return_value': '''
        CE1#show ipv6 route
        IPv6 Routing Table - default - 1 entries
        Codes: C - Connected, L - Local, S - Static, U - Per-user Static route
            B - BGP, R - RIP, H - NHRP, I1 - ISIS L1
            I2 - ISIS L2, IA - ISIS interarea, IS - ISIS summary, D - EIGRP
            EX - EIGRP external, O - OSPF Intra, OI - OSPF Inter, OE1 - OSPF ext 1
            OE2 - OSPF ext 2, ON1 - OSPF NSSA ext 1, ON2 - OSPF NSSA ext 2
            ls - LISP site, ld - LISP dyn-EID, a - Application
        L   FF00::/8 [0/0]
            via Null0, receive
    '''}

    def test_empty_1(self):
        self.device = Mock(**self.empty_output)
        obj = ShowIpRoute(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_show_ip_route_1(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_1)
        obj = ShowIpRoute(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output_1)

    def test_show_ip_route_2_with_vrf(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_2_with_vrf)
        obj = ShowIpRoute(device=self.device)
        parsed_output = obj.parse(vrf='VRF1')
        self.assertEqual(parsed_output, self.golden_parsed_output_2_with_vrf)

    def test_show_ip_route3(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output3)
        obj = ShowIpRoute(device=self.device)
        parsed_output = obj.parse(vrf='OOB_Mgmt')
        self.assertEqual(parsed_output, self.golden_parsed_output3)

    def test_show_ip_route4(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output4)
        obj = ShowIpRoute(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output4)

    def test_golden5(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output5)
        route_map_obj = ShowIpRoute(device=self.device)
        parsed_output = route_map_obj.parse(protocol='bgp')
        self.assertEqual(parsed_output, self.golden_parsed_output5)

    def test_golden6(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output6)
        route_map_obj = ShowIpv6Route(device=self.device)
        parsed_output = route_map_obj.parse()
        self.assertDictEqual(parsed_output, self.golden_parsed_output6)

    def test_golden7(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output7)
        route_map_obj = ShowIpv6Route(device=self.device)
        parsed_output = route_map_obj.parse()
        self.assertDictEqual(parsed_output, self.golden_parsed_output7)


###################################################
# unit test for show ipv6 route updated
####################################################
class TestShowIpv6RouteUpdated(unittest.TestCase):
    """
    unit test for show ipv6 route updated
    """
    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}
    golden_output_1 = {'execute.return_value': '''
    R1_iosv#show ipv6 route updated
    IPv6 Routing Table - default - 23 entries
    Codes: C - Connected, L - Local, S - Static, U - Per-user Static route
           B - BGP, HA - Home Agent, MR - Mobile Router, R - RIP
           H - NHRP, I1 - ISIS L1, I2 - ISIS L2, IA - ISIS interarea
           IS - ISIS summary, D - EIGRP, EX - EIGRP external, NM - NEMO
           ND - ND Default, NDp - ND Prefix, DCE - Destination, NDr - Redirect
           O - OSPF Intra, OI - OSPF Inter, OE1 - OSPF ext 1, OE2 - OSPF ext 2
           ON1 - OSPF NSSA ext 1, ON2 - OSPF NSSA ext 2, la - LISP alt
           lr - LISP site-registrations, ld - LISP dyn-eid, a - Application
    LC  2001:1:1:1::1/128 [0/0]
         via Loopback0, receive
          Last updated 22:55:51 04 December 2017
    S   2001:2:2:2::2/128 [1/0]
         via 2001:10:1:2::2, GigabitEthernet0/0
          Last updated 22:57:07 04 December 2017
         via 2001:20:1:2::2, GigabitEthernet0/1
          Last updated 22:57:23 04 December 2017
    S   2001:3:3:3::3/128 [1/0]
         via GigabitEthernet0/2, directly connected
          Last updated 22:57:34 04 December 2017
         via GigabitEthernet0/3, directly connected
          Last updated 22:57:43 04 December 2017
    B   2001:db8:400:1::/64 [200/1]
        via 192.168.51.1%default, indirectly connected
        Last updated 09:43:27 06 December 2017
    '''}
    golden_parsed_output_1 = {
        'ipv6_unicast_routing_enabled': True,
        'vrf':{
            'default':{
                'address_family': {
                    'ipv6': {
                        'routes': {
                            '2001:1:1:1::1/128': {
                                'route': '2001:1:1:1::1/128',
                                'active': True,
                                'source_protocol_codes': 'LC',
                                'source_protocol': 'local',
                                'route_preference': 0,
                                'metric': 0,
                                'next_hop': {
                                    'outgoing_interface': {
                                        'Loopback0': {
                                            'outgoing_interface': 'Loopback0',
                                            'updated': '22:55:51 04 December 2017',
                                        },
                                    },
                                },
                            },
                            '2001:2:2:2::2/128': {
                                'route': '2001:2:2:2::2/128',
                                'active': True,
                                'route_preference': 1,
                                'metric': 0,
                                'source_protocol_codes': 'S',
                                'source_protocol': 'static',
                                'next_hop': {
                                    'next_hop_list': {
                                        1: {
                                            'index': 1,
                                            'next_hop': '2001:10:1:2::2',
                                            'outgoing_interface': 'GigabitEthernet0/0',
                                            'updated': '22:57:07 04 December 2017',
                                        },
                                        2: {
                                            'index': 2,
                                            'next_hop': '2001:20:1:2::2',
                                            'outgoing_interface': 'GigabitEthernet0/1',
                                            'updated': '22:57:23 04 December 2017',
                                        },
                                    },
                                },
                            },
                            '2001:3:3:3::3/128': {
                                'route': '2001:3:3:3::3/128',
                                'active': True,
                                'route_preference': 1,
                                'metric': 0,
                                'source_protocol_codes': 'S',
                                'source_protocol': 'static',
                                'next_hop': {
                                    'outgoing_interface': {
                                        'GigabitEthernet0/2':{
                                            'outgoing_interface': 'GigabitEthernet0/2',
                                            'updated': '22:57:34 04 December 2017',
                                            },
                                        'GigabitEthernet0/3': {
                                            'outgoing_interface': 'GigabitEthernet0/3',
                                            'updated': '22:57:43 04 December 2017',
                                        },
                                    },
                                },
                            },
                            '2001:db8:400:1::/64': {
                                'route': '2001:db8:400:1::/64',
                                'active': True,
                                'route_preference': 200,
                                'metric': 1,
                                'source_protocol_codes': 'B',
                                'source_protocol': 'bgp',
                                'next_hop': {
                                    'next_hop_list': {
                                        1: {
                                            'index': 1,
                                            'next_hop': '192.168.51.1',
                                            'updated': '09:43:27 06 December 2017',
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

    golden_output_2 = {'execute.return_value': '''
    IPv6 Routing Table - VRF1 - 104 entries
    Codes: C - Connected, L - Local, S - Static, U - Per-user Static route
           B - BGP, R - RIP, H - NHRP, I1 - ISIS L1
           I2 - ISIS L2, IA - ISIS interarea, IS - ISIS summary, D - EIGRP
           EX - EIGRP external, ND - ND Default, NDp - ND Prefix, DCE - Destination
           NDr - Redirect, O - OSPF Intra, OI - OSPF Inter, OE1 - OSPF ext 1
           OE2 - OSPF ext 2, ON1 - OSPF NSSA ext 1, ON2 - OSPF NSSA ext 2
           la - LISP alt, lr - LISP site-registrations, ld - LISP dyn-eid
           a - Application
    O   2001:db8:100::/64 [110/1]
         via FE80::211:1FF:FE00:1, GigabitEthernet0/0/2.100
          Last updated 09:42:39 06 December 2017
    O   2001:db8:100:1::/64 [110/1]
         via FE80::211:1FF:FE00:1, GigabitEthernet0/0/2.100
          Last updated 09:42:39 06 December 2017
    O   2001:db8:100:4::/64 [110/1]
         via FE80::211:1FF:FE00:1, GigabitEthernet0/0/2.100
          Last updated 09:42:39 06 December 2017

       '''}
    golden_parsed_output_2 = {
        'ipv6_unicast_routing_enabled': True,
        'vrf': {
            'VRF1': {
                'address_family': {
                    'ipv6': {
                        'routes': {
                            '2001:db8:100::/64': {
                                'route': '2001:db8:100::/64',
                                'active': True,
                                'source_protocol_codes': 'O',
                                'source_protocol': 'ospf',
                                'route_preference': 110,
                                'metric': 1,
                                'next_hop': {
                                    'next_hop_list': {
                                        1: {
                                            'index': 1,
                                            'next_hop': 'FE80::211:1FF:FE00:1',
                                            'outgoing_interface': 'GigabitEthernet0/0/2.100',
                                            'updated': '09:42:39 06 December 2017',
                                        },
                                    },
                                },
                            },
                            '2001:db8:100:1::/64': {
                                'route': '2001:db8:100:1::/64',
                                'active': True,
                                'source_protocol_codes': 'O',
                                'source_protocol': 'ospf',
                                'route_preference': 110,
                                'metric': 1,
                                'next_hop': {
                                    'next_hop_list': {
                                        1: {
                                            'index': 1,
                                            'next_hop': 'FE80::211:1FF:FE00:1',
                                            'outgoing_interface': 'GigabitEthernet0/0/2.100',
                                            'updated': '09:42:39 06 December 2017',
                                        },
                                    },
                                },
                            },
                            '2001:db8:100:4::/64': {
                                'route': '2001:db8:100:4::/64',
                                'active': True,
                                'source_protocol_codes': 'O',
                                'source_protocol': 'ospf',
                                'route_preference': 110,
                                'metric': 1,
                                'next_hop': {
                                    'next_hop_list': {
                                        1: {
                                            'index': 1,
                                            'next_hop': 'FE80::211:1FF:FE00:1',
                                            'outgoing_interface': 'GigabitEthernet0/0/2.100',
                                            'updated': '09:42:39 06 December 2017',
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

    def test_empty_1(self):
        self.device = Mock(**self.empty_output)
        obj = ShowIpv6RouteUpdated(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_show_ipv6_route_1(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_1)
        obj = ShowIpv6RouteUpdated(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output_1)

    def test_show_ipv6_route_2(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_2)
        obj = ShowIpv6RouteUpdated(device=self.device)
        parsed_output = obj.parse(vrf='VRF1')
        self.assertEqual(parsed_output,self.golden_parsed_output_2)


###################################################
# unit test for show ip route <WROD>
####################################################
class TestShowIpRouteWord(unittest.TestCase):
    """unit test for show ip route <WORD>"""

    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_output_with_route = {'execute.return_value': '''
        show ip route 192.168.154.0
        Routing entry for 192.168.154.0/24
          Known via "eigrp 1", distance 130, metric 10880, type internal
          Redistributing via eigrp 1
          Last update from 192.168.151.2 on Vlan101, 2w3d ago
          Routing Descriptor Blocks:
          * 192.168.151.2, from 192.168.151.2, 2w3d ago, via Vlan101
              Route metric is 10880, traffic share count is 1
    '''}

    golden_parsed_output_with_route = {
        "entry": {
            "192.168.154.0/24": {
               "mask": "24",
               "type": "internal",
               "known_via": "eigrp 1",
               "ip": "192.168.154.0",
               "redist_via": "eigrp",
               "distance": "130",
               "metric": "10880",
               "redist_via_tag": "1",
               "update": {
                    "age": "2w3d",
                    "interface": "Vlan101",
                    "from": "192.168.151.2"
               },
               "paths": {
                    1: {
                         "age": "2w3d",
                         "interface": "Vlan101",
                         "from": "192.168.151.2",
                         "metric": "10880",
                         "share_count": "1",
                         "nexthop": "192.168.151.2",
                         "prefer_non_rib_labels": False,
                         "merge_labels": False
                    }
                }
            }
        },
        "total_prefixes": 1
    }

    golden_output_2 = {'execute.return_value': '''
        PE1#show ip route 10.16.2.2
        Routing entry for 10.16.2.2/32
          Known via "ospf 1024", distance 95, metric 4, type intra area
          Last update from 192.168.0.3 on GigabitEthernet2, 00:00:14 ago
         SR Incoming Label: 52610
          Routing Descriptor Blocks:
          * 192.168.0.1, from 10.16.2.2, 00:00:14 ago, via GigabitEthernet4, merge-labels
              Route metric is 5, traffic share count is 1
              MPLS label: 52610
              MPLS Flags: NSF
              Repair Path: 192.168.0.2, via GigabitEthernet3
            192.168.0.2, from 10.16.2.2, 00:00:14 ago, via GigabitEthernet3, prefer-non-rib-labels, merge-labels
              Route metric is 3, traffic share count is 5
              MPLS label: 52610
              MPLS Flags: NSF
              Repair Path: 192.168.0.4, via GigabitEthernet1
            192.168.0.3, from 10.16.2.2, 00:00:14 ago, via GigabitEthernet2, prefer-non-rib-labels, merge-labels
              Route metric is 1, traffic share count is 2
              MPLS label: 52610
              MPLS Flags: NSF
              Repair Path: 192.168.0.1, via GigabitEthernet4
            192.168.0.4, from 10.16.2.2, 00:00:14 ago, via GigabitEthernet1, prefer-non-rib-labels, merge-labels
              Route metric is 2, traffic share count is 1
              MPLS label: 52610
              MPLS Flags: NSF
              Repair Path: 192.168.0.3, via GigabitEthernet2
    '''}

    golden_parsed_output_2 = {
        'entry': {
            '10.16.2.2/32': {
                'ip': '10.16.2.2',
                'mask': '32',
                'known_via': 'ospf 1024',
                'distance': '95',
                'metric': '4',
                'type': 'intra area',
                'update': {
                    'from': '192.168.0.3',
                    'interface': 'GigabitEthernet2',
                    'age': '00:00:14'
                },
                'sr_incoming_label': '52610',
                'paths': {
                    1: {
                        'nexthop': '192.168.0.1',
                        'from': '10.16.2.2',
                        'age': '00:00:14',
                        'interface': 'GigabitEthernet4',
                        'prefer_non_rib_labels': False,
                        'merge_labels': True,
                        'metric': '5',
                        'share_count': '1',
                        'mpls_label': '52610',
                        'mpls_flags': 'NSF',
                        'repair_path': {
                            'repair_path': '192.168.0.2',
                            'via': 'GigabitEthernet3'
                        }
                    },
                    2: {
                        'nexthop': '192.168.0.2',
                        'from': '10.16.2.2',
                        'age': '00:00:14',
                        'interface': 'GigabitEthernet3',
                        'prefer_non_rib_labels': True,
                        'merge_labels': True,
                        'metric': '3',
                        'share_count': '5',
                        'mpls_label': '52610',
                        'mpls_flags': 'NSF',
                        'repair_path': {
                            'repair_path': '192.168.0.4',
                            'via': 'GigabitEthernet1'
                        }
                    },
                    3: {
                        'nexthop': '192.168.0.3',
                        'from': '10.16.2.2',
                        'age': '00:00:14',
                        'interface': 'GigabitEthernet2',
                        'prefer_non_rib_labels': True,
                        'merge_labels': True,
                        'metric': '1',
                        'share_count': '2',
                        'mpls_label': '52610',
                        'mpls_flags': 'NSF',
                        'repair_path': {
                            'repair_path': '192.168.0.1',
                            'via': 'GigabitEthernet4'
                        }
                    },
                    4: {
                        'nexthop': '192.168.0.4',
                        'from': '10.16.2.2',
                        'age': '00:00:14',
                        'interface': 'GigabitEthernet1',
                        'prefer_non_rib_labels': True,
                        'merge_labels': True,
                        'metric': '2',
                        'share_count': '1',
                        'mpls_label': '52610',
                        'mpls_flags': 'NSF',
                        'repair_path': {
                            'repair_path': '192.168.0.3',
                            'via': 'GigabitEthernet2'
                        }
                    }
                }
            }
        },
        'total_prefixes': 4
    }

    golden_output_3 = {'execute.return_value': '''\
        Routing entry for 0.0.0.0/0, supernet
            Known via "bgp 65161", distance 20, metric 0, candidate default path
            Tag 65161, type external
            Redistributing via ospf 1
            Last update from 10.101.146.10 2d07h ago
            Routing Descriptor Blocks:
            * 10.101.146.10, from 10.101.146.10, 2d07h ago
                Route metric is 0, traffic share count is 1
                AS Hops 9
                Route tag 65161
                MPLS label: none 
    '''
    }

    golden_parsed_output_3 = {
        'entry': {
            '0.0.0.0/0': {
                'distance': '20',
                'ip': '0.0.0.0',
                'known_via': 'bgp 65161',
                'mask': '0',
                'metric': '0',
                'net': 'supernet',
                'paths': {
                    1: {
                        'age': '2d07h',
                        'as_hops': '9',
                        'from': '10.101.146.10',
                        'merge_labels': False,
                        'metric': '0',
                        'mpls_label': 'none',
                        'nexthop': '10.101.146.10',
                        'prefer_non_rib_labels': False,
                        'route_tag': '65161',
                        'share_count': '1'
                    }
                },
                'redist_via': 'ospf',
                'redist_via_tag': '1',
                'tag_name': '65161',
                'tag_type': 'external',
                'type': 'default path',
                'update': {
                    'age': '2d07h', 
                    'from': '10.101.146.10'
                }
            }
        },
        'total_prefixes': 1
    }

    golden_output_4 = {'execute.return_value': '''\
        lab-asr-1002# show ip route vrf Mgmt-intf 0.0.0.0
        
        Routing Table: Mgmt-intf
        Routing entry for 0.0.0.0/0, supernet
        Known via "static", distance 1, metric 0, candidate default path
        Routing Descriptor Blocks:
        * 10.255.207.129
            Route metric is 0, traffic share count is 1
    '''
    }

    golden_parsed_output_4 = {
        'entry': {
            '0.0.0.0/0': {
                'distance': '1',
                'ip': '0.0.0.0',
                'known_via': 'static',
                'mask': '0',
                'metric': '0',
                'net': 'supernet',
                'paths': {
                    1: {
                        'merge_labels': False,
                        'metric': '0',
                        'nexthop': '10.255.207.129',
                        'prefer_non_rib_labels': False,
                        'share_count': '1'
                    }
                },
                'type': 'default path'
            }
        },
        'total_prefixes': 1
    }

    golden_output_5 = {'execute.return_value': '''
        GENIE#show ip route 192.168.4.10
        Routing entry for 192.168.4.0/25
        Known via "static", distance 1, metric 0
        Tag 113
        Redistributing via eigrp 10
        Advertised by eigrp 10 route-map GENIE_INTO_EIGRP
        Routing Descriptor Blocks:
        * 10.1.11.9
            Route metric is 0, traffic share count is 1
            Route tag 113
    '''
    }

    golden_parsed_output_5 = {
        'entry': {
            '192.168.4.0/25': {
                'distance': '1',
                'advertised_by': 'eigrp 10 route-map GENIE_INTO_EIGRP',
                'ip': '192.168.4.0',
                'known_via': 'static',
                'mask': '25',
                'metric': '0',
                'paths': {
                    1: {
                        'merge_labels': False,
                        'metric': '0',
                        'nexthop': '10.1.11.9',
                        'prefer_non_rib_labels': False,
                        'route_tag': '113',
                        'share_count': '1'
                    }
                },
                'redist_via': 'eigrp',
                'redist_via_tag': '10'
            }
        },
        'total_prefixes': 1
    }

    golden_output_6 = {'execute.return_value': '''
        show ip route 10.13.115.1
        Routing entry for 10.13.115.1/32
        Known via "connected", distance 0, metric 0 (connected)
        Routing Descriptor Blocks:
        * directly connected, via GigabitEthernet3.115
            Route metric is 0, traffic share count is 1
    '''}

    golden_parsed_output_6 = {
        'entry': {
            '10.13.115.1/32': {
                'ip': '10.13.115.1',
                'mask': '32',
                'known_via': 'connected',
                'distance': '0',
                'metric': '0',
                'paths': {
                    1: {
                        'interface': 'GigabitEthernet3.115',
                        'metric': '0',
                        'share_count': '1',
                    },
                },
            },
        },
        'total_prefixes': 1,
    }

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowIpRouteWord(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse(route='192.168.154.0')

    def test_golden(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_with_route)
        obj = ShowIpRouteWord(device=self.device)
        parsed_output = obj.parse(route='192.168.154.0')
        self.assertEqual(parsed_output,self.golden_parsed_output_with_route)

    def test_golden2(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_with_route)
        obj = ShowIpRouteWord(device=self.device)
        parsed_output = obj.parse(route='192.168.154.0')
        self.assertEqual(parsed_output,self.golden_parsed_output_with_route)

    def test_golden_2(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_2)
        obj = ShowIpRouteWord(device=self.device)
        parsed_output = obj.parse(route='192.168.154.0')
        self.assertEqual(parsed_output, self.golden_parsed_output_2)

    def test_golden_3(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_3)
        obj = ShowIpRouteWord(device=self.device)
        parsed_output = obj.parse(route='0.0.0.0')
        self.assertEqual(parsed_output, self.golden_parsed_output_3)

    def test_golden_4(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_4)
        obj = ShowIpRouteWord(device=self.device)
        parsed_output = obj.parse(route='0.0.0.0')
        self.assertEqual(parsed_output, self.golden_parsed_output_4)

    def test_golden_customer(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_5)
        obj = ShowIpRouteWord(device=self.device)
        parsed_output = obj.parse(route='192.168.4.10')
        self.assertEqual(parsed_output, self.golden_parsed_output_5)
    
    def test_golden_customer(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_6)
        obj = ShowIpRouteWord(device=self.device)
        parsed_output = obj.parse(route='10.13.115.1')
        self.assertEqual(parsed_output, self.golden_parsed_output_6)
        
###################################################
# unit test for show ipv6 route <WROD>
####################################################
class TestShowIpv6RouteWord(unittest.TestCase):
    """unit test for show ipv6 route <WORD>"""

    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output_with_route = {
    	"total_prefixes": 1,
		"entry": {
		    "2001:db8:400:4::4:1/128": {
		       "ip": "2001:db8:400:4::4:1",
		       "type": "level-2",
		       "distance": "115",
		       "metric": "20",
		       "known_via": "isis",
		       "mask": "128",
		       "paths": {
		            1: {
		                 "age": "2w4d",
		                 "fwd_intf": "Vlan202",
		                 "from": "FE80::EEBD:1DFF:FE09:56C2",
		                 "fwd_ip": "FE80::EEBD:1DFF:FE09:56C2"
		            }
		       },
		       "share_count": "0",
		       "route_count": "1/1"
		    }
		}
    }

    golden_output_with_ipv6_route = {'execute.return_value': '''
        Routing entry for 2001:db8:400:4::4:1/128
		  Known via "isis", distance 115, metric 20, type level-2
		  Route count is 1/1, share count 0
		  Routing paths:
		    FE80::EEBD:1DFF:FE09:56C2, Vlan202
		      From FE80::EEBD:1DFF:FE09:56C2
		      Last updated 2w4d ago

    '''}

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowIpv6RouteWord(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse(route='2001:db8:400:4::4:1')

    def test_golden(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_with_ipv6_route)
        obj = ShowIpv6RouteWord(device=self.device)
        parsed_output = obj.parse(route='2001:db8:400:4::4:1')
        self.assertEqual(parsed_output,self.golden_parsed_output_with_route)

###################################################
# unit test for show ip cef <prefix>
####################################################
class TestShowIpCef(unittest.TestCase):
    """unit test for show ip cef <ip>
                     show ip cef"""

    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_output_1 = {'execute.return_value': '''\
        R1#sh ip cef
        10.2.3.0/24
          nexthop 10.1.2.2 GigabitEthernet2.100
          next_hop 10.1.3.3 GigabitEthernet3.100
           '''}

    golden_parsed_output_1 = {
        "vrf": {
            "default": {
                "address_family": {
                    "ipv4": {
                        "prefix": {
                            "10.2.3.0/24": {
                                "nexthop": {
                                    "10.1.2.2": {
                                        "outgoing_interface": {
                                            "GigabitEthernet2.100": {}
                                        }
                                    },
                                    "10.1.3.3": {
                                        "outgoing_interface": {
                                            "GigabitEthernet3.100": {}
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }

    golden_output_1 = {'execute.return_value': '''\
    R1#sh ip cef 10.2.3.1
    10.2.3.0/24
      nexthop 10.1.2.2 GigabitEthernet2.100
      nexthop 10.1.3.3 GigabitEthernet3.100
       '''}
    golden_parsed_output_2 = {
        "vrf": {
            "default": {
                "address_family": {
                    "ipv4": {
                        "prefix": {
                            "10.169.197.104/30": {
                                "nexthop": {
                                    "10.169.197.93": {
                                        "outgoing_interface": {
                                            "TenGigabitEthernet0/2/0": {
                                                "local_label": 2043,
                                                "outgoing_label": ['22']
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }

    golden_output_2 = {'execute.return_value': '''\
    PE1#show ip cef 10.169.197.104
    Load for five secs: 2%/0%; one minute: 5%; five minutes: 4%
    Time source is NTP, 17:33:18.269 EST Fri Apr 5 2019
    10.169.197.104/30
             nexthop 10.169.197.93 TenGigabitEthernet0/2/0 label 22-(local:2043)

          '''}
    golden_parsed_output_3 = {
        "vrf": {
            "default": {
                "address_family": {
                    "ipv4": {
                        "prefix": {
                            "192.168.4.1/32": {
                                "nexthop": {
                                    "attached": {
                                        "outgoing_interface": {
                                            "GigabitEthernet3.100": {}
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }

    golden_output_3 = {'execute.return_value': '''\
    R1#sh ip cef 192.168.4.1
    192.168.4.1/32
        attached to GigabitEthernet3.100
          '''}
    golden_parsed_output_4 = {
        "vrf": {
            "default": {
                "address_family": {
                    "ipv4": {
                        "prefix": {
                            "0.0.0.0/0": {
                                "nexthop": {
                                    "10.1.2.1": {
                                        "outgoing_interface": {
                                            "GigabitEthernet2.100": {}
                                        }
                                    }
                                }
                            },
                            "0.0.0.0/8": {
                                "nexthop": {
                                    "drop": {}
                                }
                            },
                            "0.0.0.0/32": {
                                "nexthop": {
                                    "receive": {}
                                }
                            },
                            "10.1.2.0/24": {
                                "nexthop": {
                                    "attached": {
                                        "outgoing_interface": {
                                            "GigabitEthernet2.100": {}
                                        }
                                    }
                                }
                            },
                            "10.1.2.0/32": {
                                "nexthop": {
                                    "receive": {
                                        "outgoing_interface": {
                                            "GigabitEthernet2.100": {}
                                        }
                                    }
                                }
                            },
                            "10.1.2.1/32": {
                                "nexthop": {
                                    "attached": {
                                        "outgoing_interface": {
                                            "GigabitEthernet2.100": {}
                                        }
                                    }
                                }
                            },
                            "10.1.2.2/32": {
                                "nexthop": {
                                    "receive": {
                                        "outgoing_interface": {
                                            "GigabitEthernet2.100": {}
                                        }
                                    }
                                }
                            },
                            "10.1.2.255/32": {
                                "nexthop": {
                                    "receive": {
                                        "outgoing_interface": {
                                            "GigabitEthernet2.100": {}
                                        }
                                    }
                                }
                            },
                            "10.1.3.0/24": {
                                "nexthop": {
                                    "10.1.2.1": {
                                        "outgoing_interface": {
                                            "GigabitEthernet2.100": {}
                                        }
                                    },
                                    "10.2.3.3": {
                                        "outgoing_interface": {
                                            "GigabitEthernet3.100": {}
                                        }
                                    }
                                }
                            },
                            "10.2.3.0/24": {
                                "nexthop": {
                                    "attached": {
                                        "outgoing_interface": {
                                            "GigabitEthernet3.100": {}
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }
    golden_output_4 = {'execute.return_value': '''\
    R2#show ip cef
    Prefix               Next Hop             Interface
    0.0.0.0/0            10.1.2.1             GigabitEthernet2.100
    0.0.0.0/8            drop
    0.0.0.0/32           receive
    10.1.2.0/24          attached             GigabitEthernet2.100
    10.1.2.0/32          receive              GigabitEthernet2.100
    10.1.2.1/32          attached             GigabitEthernet2.100
    10.1.2.2/32          receive              GigabitEthernet2.100
    10.1.2.255/32        receive              GigabitEthernet2.100
    10.1.3.0/24          10.1.2.1             GigabitEthernet2.100
                         10.2.3.3             GigabitEthernet3.100
    10.2.3.0/24          attached             GigabitEthernet3.100

              '''}

    golden_parsed_output_5 = {
        "vrf": {
            "default": {
                "address_family": {
                    "ipv4": {
                        "prefix": {
                            "10.151.22.22/32": {
                                "epoch": 2,
                                "sr_local_label_info": "global/16022 [0x1B]",
                                "nexthop": {
                                    "10.0.0.9": {
                                        "outgoing_interface": {
                                            "GigabitEthernet3": {
                                                "local_label": 16022,
                                                "outgoing_label": ["16022"],
                                                "outgoing_label_backup": "implicit-null",
                                                "repair": "attached-nexthop 10.0.0.13 GigabitEthernet4"
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }

    golden_output_5 = {'execute.return_value': '''
    PE1#show ip cef 10.151.22.22 detail
    10.151.22.22/32, epoch 2
      sr local label info: global/16022 [0x1B]
      nexthop 10.0.0.9 GigabitEthernet3 label [16022|implicit-null]-(local:16022)
        repair: attached-nexthop 10.0.0.13 GigabitEthernet4
      nexthop 10.0.0.13 GigabitEthernet4, repair

    '''}

    golden_parsed_output_6 = {
        'vrf': {
            'default': {
                'address_family': {
                    'ipv4': {
                        'prefix': {
                            '10.169.196.241/32': {
                                'nexthop': {
                                    '10.19.198.25': {
                                        'outgoing_interface': {
                                            'GigabitEthernet0/1/6': {
                                                'local_label': 17063,
                                                'outgoing_label': ['16063'],
                                                'outgoing_label_info': 'elc',
                                            },
                                        },
                                    },
                                    '10.19.198.26': {
                                        'outgoing_interface': {
                                            'GigabitEthernet0/1/7': {
                                                'local_label': 17063,
                                                'outgoing_label': ['16063'],
                                                'outgoing_label_backup': '16063',
                                                'repair': 'attached-nexthop 10.19.198.29 GigabitEthernet0/1/8',
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

    golden_output_6 = {'execute.return_value': '''
    show ip cef 10.169.196.241
    10.169.196.241/32
        nexthop 10.19.198.25 GigabitEthernet0/1/6 label 16063(elc)-(local:17063)
        nexthop 10.19.198.26 GigabitEthernet0/1/7 label [16063|16063]-(local:17063)
            repair: attached-nexthop 10.19.198.29 GigabitEthernet0/1/8
    '''}

    golden_parsed_output_7 = {
        'vrf': {
            'default': {
                'address_family': {
                    'ipv4': {
                        'prefix': {
                            '0.0.0.0/0': {
                                'epoch': 3,
                                'flags': ['default route handler', 'default route'],
                                'nexthop': {'no route': {}},
                            }
                        }
                    }
                }
            }
        }
    }

    golden_output_7 = {'execute.return_value': '''
        show ip cef 10.169.196.241 detail
        0.0.0.0/0, epoch 3, flags [default route handler, default route]
        no route
    '''}

    golden_parsed_output_8 = {
        'vrf': {
            'default': {
                'address_family': {
                    'ipv4': {
                        'prefix': {
                            '10.169.196.241/32': {
                                'nexthop': {
                                    '10.0.0.10': {
                                        'outgoing_interface': {
                                            'GigabitEthernet3': {
                                                'local_label': 16022,
                                                'outgoing_label': ['16022'],
                                                'outgoing_label_backup': '16002',
                                                'outgoing_label_info': 'elc',
                                            },
                                        },
                                    }
                                },
                            },
                        },
                    },
                },
            },
        },
    }

    golden_output_8 = {'execute.return_value': '''
        show ip cef 10.169.196.241
        10.169.196.241/32
            nexthop 10.0.0.10 GigabitEthernet3 label [16022|16002](elc)-(local:16022)
        '''}

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowIpCef(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden_1(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_1)
        obj = ShowIpCef(device=self.device)
        parsed_output = obj.parse(prefix='10.2.3.1')
        self.assertEqual(parsed_output,self.golden_parsed_output_1)

    def test_golden_2(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_2)
        obj = ShowIpCef(device=self.device)
        parsed_output = obj.parse(prefix='10.169.197.104')
        self.assertEqual(parsed_output,self.golden_parsed_output_2)

    def test_golden_3(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_3)
        obj = ShowIpCef(device=self.device)
        parsed_output = obj.parse(prefix='192.168.4.1')
        self.assertEqual(parsed_output, self.golden_parsed_output_3)

    def test_golden_4(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_4)
        obj = ShowIpCef(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_4)

    def test_golden_5(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_5)
        obj = ShowIpCef(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_5)

    def test_golden_6(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_6)
        obj = ShowIpCef(device=self.device)
        parsed_output = obj.parse(prefix='10.169.196.241')
        self.assertEqual(parsed_output, self.golden_parsed_output_6)

    def test_golden_7(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_7)
        obj = ShowIpCef(device=self.device)
        parsed_output = obj.parse(prefix='10.169.196.241')
        self.assertEqual(parsed_output, self.golden_parsed_output_7)

    def test_golden_8(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_8)
        obj = ShowIpCef(device=self.device)
        parsed_output = obj.parse(prefix='10.169.196.241')
        self.assertEqual(parsed_output, self.golden_parsed_output_8)


###################################################
# unit test for show ipv6 cef <prefix>
####################################################
class TestShowIpv6Cef(unittest.TestCase):

    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}


    golden_output_1 = {'execute.return_value':'''
    R2#show ipv6 cef
    ::/0
      no route
    ::/127
      discard
    2001:DB8:1:2::/64
      attached to GigabitEthernet2.100
    2001:DB8:1:2::1/128
      nexthop 2001:DB8:1:2::1 GigabitEthernet2.100
    2001:DB8:1:2::2/128
      receive for GigabitEthernet2.100
    2001:DB8:1:3::/64
      nexthop FE80::F816:3EFF:FE86:1D6D GigabitEthernet2.100
      nexthop FE80::F816:3EFF:FEF3:7B32 GigabitEthernet3.100
    2001:DB8:2:3::/64
      attached to GigabitEthernet3.100
    2001:DB8:64::4:5:0/112
      nexthop 10.2.3.3 FastEthernet1/0/0 label 17 21
    '''}

    golden_parsed_output_1 = {
        "vrf": {
            "default": {
                "address_family": {
                    "ipv6": {
                        "prefix": {
                            "::/0": {
                                "nexthop": {
                                    "no route": {}
                                }
                            },
                            "::/127": {
                                "nexthop": {
                                    "discard": {}
                                }
                            },
                            "2001:DB8:1:2::/64": {
                                "nexthop": {
                                    "attached": {
                                        "outgoing_interface": {
                                            "GigabitEthernet2.100": {}
                                        }
                                    }
                                }
                            },
                            "2001:DB8:1:2::1/128": {
                                "nexthop": {
                                    "2001:DB8:1:2::1": {
                                        "outgoing_interface": {
                                            "GigabitEthernet2.100": {}
                                        }
                                    }
                                }
                            },
                            "2001:DB8:1:2::2/128": {
                                "nexthop": {
                                    "receive": {
                                        "outgoing_interface": {
                                            "GigabitEthernet2.100": {}
                                        }
                                    }
                                }
                            },
                            "2001:DB8:1:3::/64": {
                                "nexthop": {
                                    "FE80::F816:3EFF:FE86:1D6D": {
                                        "outgoing_interface": {
                                            "GigabitEthernet2.100": {}
                                        }
                                    },
                                    "FE80::F816:3EFF:FEF3:7B32": {
                                        "outgoing_interface": {
                                            "GigabitEthernet3.100": {}
                                        }
                                    }
                                }
                            },
                            "2001:DB8:2:3::/64": {
                                "nexthop": {
                                    "attached": {
                                        "outgoing_interface": {
                                            "GigabitEthernet3.100": {}
                                        }
                                    }
                                }
                            },
                            '2001:DB8:64::4:5:0/112': {
                                'nexthop': {
                                    '10.2.3.3': {
                                        'outgoing_interface': {
                                            'FastEthernet1/0/0': {
                                                'outgoing_label': ['17','21']
                                                }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowIpv6Cef(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden_1(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_1)
        obj = ShowIpv6Cef(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output_1)


# ==========================================
# Unittest for 'show ip cef <prefix> detail'
# ==========================================
class TestShowIpCefDetail(unittest.TestCase):
    '''Unittest for:
        * 'show ip cef <prefix> detail'
    '''

    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_output_1 = {'execute.return_value': '''
        PE1#show ip cef 10.16.2.2 detail
        10.16.2.2/32, epoch 2, per-destination sharing
          sr local label info: global/16002 [0x1B]
          nexthop 10.0.0.5 GigabitEthernet2 label [16002|16002]-(local:16002)
            repair: attached-nexthop 10.0.0.9 GigabitEthernet3
          nexthop 10.0.0.9 GigabitEthernet3 label [16002|16002]-(local:16002)
            repair: attached-nexthop 10.0.0.25 GigabitEthernet5
          nexthop 10.0.0.13 GigabitEthernet4 label [16002|16002]-(local:16002)
            repair: attached-nexthop 10.0.0.5 GigabitEthernet2
          nexthop 10.0.0.25 GigabitEthernet5 label [16002|16002]-(local:16002)
            repair: attached-nexthop 10.0.0.13 GigabitEthernet4
        PE1# 
        '''}

    golden_parsed_output_1 = {
        'vrf': 
            {'default': 
                {'address_family': 
                    {'ipv4': 
                        {'prefix': 
                            {'10.16.2.2/32': 
                                {'epoch': 2,
                                'nexthop': 
                                    {'10.0.0.13': 
                                        {'outgoing_interface': 
                                            {'GigabitEthernet4': 
                                                {'local_label': 16002,
                                                'outgoing_label': ['16002'],
                                                'outgoing_label_backup': "16002",
                                                'repair': 'attached-nexthop 10.0.0.5 GigabitEthernet2'}}},
                                    '10.0.0.25': 
                                        {'outgoing_interface': 
                                            {'GigabitEthernet5': 
                                                {'local_label': 16002,
                                                'outgoing_label': ['16002'],
                                                'outgoing_label_backup': "16002",
                                                'repair': 'attached-nexthop 10.0.0.13 GigabitEthernet4'}}},
                                    '10.0.0.5': 
                                        {'outgoing_interface': 
                                            {'GigabitEthernet2': 
                                                {'local_label': 16002,
                                                'outgoing_label': ['16002'],
                                                'outgoing_label_backup': "16002",
                                                'repair': 'attached-nexthop 10.0.0.9 GigabitEthernet3'}}},
                                    '10.0.0.9': 
                                        {'outgoing_interface': 
                                            {'GigabitEthernet3': 
                                                {'local_label': 16002,
                                                'outgoing_label': ['16002'],
                                                'outgoing_label_backup': "16002",
                                                'repair': 'attached-nexthop 10.0.0.25 GigabitEthernet5'}}}},
                            'per_destination_sharing': True,
                            'sr_local_label_info': 'global/16002 [0x1B]'}}}}}}}

    def test_empty(self):
        self.device1 = Mock(**self.empty_output)
        obj = ShowIpCefDetail(device=self.device1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse(prefix='10.16.2.2')

    def test_golden1(self):
        self.device = Mock(**self.golden_output_1)
        obj = ShowIpCefDetail(device=self.device)
        parsed_output = obj.parse(prefix='10.16.2.2')
        self.assertEqual(parsed_output, self.golden_parsed_output_1)


###################################################
# unit test for show ip route summary
####################################################
class TestShowIpRouteSummary(unittest.TestCase):
    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_output_1 = {'execute.return_value':'''
IP routing table name is VRF1 (0x2)
IP routing table maximum-paths is 32
Route Source    Networks    Subnets     Replicates  Overhead    Memory (bytes)
application     0           0           0           0           0
connected       0           17          0           1632        5168
static          0           0           0           0           0
ospf 2          0           1           0           96          308
  Intra-area: 1 Inter-area: 0 External-1: 0 External-2: 0
  NSSA External-1: 0 NSSA External-2: 0
isis test1      0           1           0           96          304
  Level 1: 1 Level 2: 0 Inter-area: 0
eigrp 100       0           3           0           672         912
rip             0           1           0           192         304
bgp 65000       0           0           0           0           0
  External: 0 Internal: 0 Local: 0
internal        4                                               2936
Total           4           23          0           2688        9932
    '''}
    golden_parsed_output_1 = {
        'vrf': {
            'VRF1': {
                'vrf_id': '0x2',
                'maximum_paths': 32,
                'total_route_source': {
                    'networks': 4,
                    'subnets': 23,
                    'replicates': 0,
                    'overhead': 2688,
                    'memory_bytes': 9932,
                },
                'route_source': {
                    'connected': {
                        'networks': 0,
                        'subnets': 17,
                        'replicates': 0,
                        'overhead': 1632,
                        'memory_bytes': 5168,
                    },
                    'static': {
                        'networks': 0,
                        'subnets': 0,
                        'replicates': 0,
                        'overhead': 0,
                        'memory_bytes': 0,
                    },
                    'internal': {
                        'networks': 4,
                        'memory_bytes': 2936,
                    },
                    'application': {
                        'networks': 0,
                        'subnets': 0,
                        'replicates': 0,
                        'overhead': 0,
                        'memory_bytes': 0,
                    },
                    'ospf': {

                        '2': {
                            'networks': 0,
                            'subnets': 1,
                            'replicates': 0,
                            'overhead': 96,
                            'memory_bytes': 308,
                            'intra_area': 1,
                            'inter_area': 0,
                            'external_1': 0,
                            'external_2': 0,
                            'nssa_external_1': 0,
                            'nssa_external_2': 0,
                        }

                    },
                    'isis': {

                        'test1': {
                            'networks': 0,
                            'subnets': 1,
                            'replicates': 0,
                            'overhead': 96,
                            'memory_bytes': 304,
                            'level_1': 1,
                            'level_2': 0,
                            'inter_area': 0,
                        }},
                    'eigrp': {

                        '100': {
                            'networks': 0,
                            'subnets': 3,
                            'replicates': 0,
                            'overhead': 672,
                            'memory_bytes': 912,
                        }},
                    'rip': {
                        'networks': 0,
                        'subnets': 1,
                        'replicates': 0,
                        'overhead': 192,
                        'memory_bytes': 304,
                    },
                    'bgp': {

                        '65000': {
                            'networks': 0,
                            'subnets': 0,
                            'replicates': 0,
                            'overhead': 0,
                            'memory_bytes': 0,
                            'external': 0,
                            'internal': 0,
                            'local': 0,
                        }},

                }
            }
        }
    }

    golden_output_2 = {'execute.return_value':'''
        #show ip route vrf VRF-1 summary
        IP routing table name is VRF-1 (0x27)
        IP routing table maximum-paths is 32
        Route Source    Networks    Subnets     Replicates  Overhead    Memory (bytes)
        application     0           0           0           0           0
        connected       0           2           0           192         624
        static          0           0           0           0           0
        bgp 65000        1           0           0           96          312
          External: 0 Internal: 1 Local: 0
        internal        1                                               712
        Total           2           2           0           288         1648
    '''}

    golden_parsed_output_2 = {
        'vrf': {
            'VRF-1': {
                'maximum_paths': 32,
                'route_source': {
                    'application': {
                        'memory_bytes': 0,
                        'networks': 0,
                        'overhead': 0,
                        'replicates': 0,
                        'subnets': 0},
                    'bgp': {
                        '65000': {
                            'external': 0,
                            'internal': 1,
                            'local': 0,
                            'memory_bytes': 312,
                            'networks': 1,
                            'overhead': 96,
                            'replicates': 0,
                            'subnets': 0}},
                    'connected': {
                        'memory_bytes': 624,
                        'networks': 0,
                        'overhead': 192,
                        'replicates': 0,
                        'subnets': 2},
                    'internal': {
                        'memory_bytes': 712,
                        'networks': 1},
                    'static': {
                        'memory_bytes': 0,
                        'networks': 0,
                        'overhead': 0,
                        'replicates': 0,
                        'subnets': 0}},
                'total_route_source': {
                        'memory_bytes': 1648,
                        'networks': 2,
                        'overhead': 288,
                        'replicates': 0,
                        'subnets': 2},
                'vrf_id': '0x27'}}}

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowIpRouteSummary(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden_1(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_1)
        obj = ShowIpRouteSummary(device=self.device)
        parsed_output = obj.parse(vrf='VRF1')
        self.assertEqual(parsed_output, self.golden_parsed_output_1)

    def test_golden_2(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_2)
        obj = ShowIpRouteSummary(device=self.device)
        parsed_output = obj.parse(vrf='VRF-1')
        self.assertEqual(parsed_output, self.golden_parsed_output_2)


# ==========================================
# Unittest for 'show ip cef internal'
# ==========================================
class TestShowIpCefInternal(unittest.TestCase):
    '''Unittest for:
        * 'show ip cef <prefix> internal'
        * 'show ip cef internal'
        * 'show ip cef vrf {vrf} {prefix} internal'
    '''

    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_output_1 = {'execute.return_value': '''
    device_name01#show ip cef 10.19.198.239 internal 
Load for five secs: 0%/0%; one minute: 0%; five minutes: 0%
Time source is NTP, 16:01:30.164 UTC Mon Nov 4 2019

10.19.198.239/32, epoch 2, RIB[I], refcnt 7, per-destination sharing
  sources: RIB, RR, LTE 
  feature space:
    IPRM: 0x00028000
    Broker: linked, distributed at 1st priority
    LFD: 10.19.198.239/32 2 local labels
    dflt local label info: global/28 [0x3]
    sr local label info: global/16073 [0x1B]
        contains path extension list
        dflt disposition chain 0x7F0FF19606C0
          label 51885
          FRR Primary
            <primary: TAG adj out of GigabitEthernet0/1/6, addr 10.169.196.213>
        dflt label switch chain 0x7F0FF19606C0
          label 51885
          FRR Primary
            <primary: TAG adj out of GigabitEthernet0/1/6, addr 10.169.196.213>
        sr disposition chain 0x7F0FF1960590
          label 16073
          FRR Primary
            <primary: TAG adj out of GigabitEthernet0/1/6, addr 10.169.196.213>
        sr label switch chain 0x7F0FF1960590
          label 16073
          FRR Primary
            <primary: TAG adj out of GigabitEthernet0/1/6, addr 10.169.196.213>
  subblocks:
    1 RR source [non-eos indirection, heavily shared]
      non-eos chain loadinfo 7F0FF16E6F38, per-session, flags 0111, 8 locks
  ifnums:
    GigabitEthernet0/1/6(15): 10.169.196.213
    MPLS-SR-Tunnel1(29)
  path list 7F0FEC884768, 19 locks, per-destination, flags 0x4D [shble, hvsh, rif, hwcn]
    path 7F0FF11E0AE0, share 1/1, type attached nexthop, for IPv4, flags [has-rpr]
      MPLS short path extensions: [rib | prfmfi | lblmrg | srlbl] MOI flags = 0x2020 label 51885
      nexthop 10.169.196.213 GigabitEthernet0/1/6 label [51885|16073]-(local:28), IP adj out of GigabitEthernet0/1/6, addr 10.169.196.213 7F0FF08D4900
  output chain:
    label [51885|16073]-(local:28)
    FRR Primary (0x80007F0FF094DD88)
      <primary: TAG adj out of GigabitEthernet0/1/6, addr 10.169.196.213 7F0FF08D46D0>
      <repair:  TAG midchain out of MPLS-SR-Tunnel1 7F0FF0AFAC68
                label 98
                TAG adj out of GigabitEthernet0/1/7, addr 10.169.196.217 7F0FF0AFB2F8>
    '''}

    golden_parsed_output_1 = {
    'vrf': {
        'default': {
            'address_family': {
                'ipv4': {
                    'prefix': {
                        '10.19.198.239/32': {
                            'epoch': 2,
                            'feature_space': {
                                'broker': {
                                    'distribution_priority': 1,
                                },
                                'iprm': '0x00028000',
                                'lfd': {
                                    '10.19.198.239/32': {
                                        'local_labels': 2,
                                    },
                                },
                                'local_label_info': {
                                    'dflt': 'global/28 [0x3]',
                                    'sr': 'global/16073 [0x1B]',
                                },
                                'path_extension_list': {
                                    'dflt': {
                                        'disposition_chain': {
                                            '0x7F0FF19606C0': {
                                                'frr': {
                                                    'primary': {
                                                        'primary': {
                                                            'tag_adj': {
                                                                'GigabitEthernet0/1/6': {
                                                                    'addr': '10.169.196.213',
                                                                },
                                                            },
                                                        },
                                                    },
                                                },
                                                'label': 51885,
                                            },
                                        },
                                        'label_switch_chain': {
                                            '0x7F0FF19606C0': {
                                                'frr': {
                                                    'primary': {
                                                        'primary': {
                                                            'tag_adj': {
                                                                'GigabitEthernet0/1/6': {
                                                                    'addr': '10.169.196.213',
                                                                },
                                                            },
                                                        },
                                                    },
                                                },
                                                'label': 51885,
                                            },
                                        },
                                    },
                                    'sr': {
                                        'disposition_chain': {
                                            '0x7F0FF1960590': {
                                                'frr': {
                                                    'primary': {
                                                        'primary': {
                                                            'tag_adj': {
                                                                'GigabitEthernet0/1/6': {
                                                                    'addr': '10.169.196.213',
                                                                },
                                                            },
                                                        },
                                                    },
                                                },
                                                'label': 16073,
                                            },
                                        },
                                        'label_switch_chain': {
                                            '0x7F0FF1960590': {
                                                'frr': {
                                                    'primary': {
                                                        'primary': {
                                                            'tag_adj': {
                                                                'GigabitEthernet0/1/6': {
                                                                    'addr': '10.169.196.213',
                                                                },
                                                            },
                                                        },
                                                    },
                                                },
                                                'label': 16073,
                                            },
                                        },
                                    },
                                },
                            },
                            'ifnums': {
                                'GigabitEthernet0/1/6': {
                                    'address': '10.169.196.213',
                                    'ifnum': 15,
                                },
                                'MPLS-SR-Tunnel1': {
                                    'ifnum': 29,
                                },
                            },
                            'output_chain': {
                                'frr': {
                                    'primary': {
                                        'info': '0x80007F0FF094DD88',
                                        'primary': {
                                            'tag_adj': {
                                                'GigabitEthernet0/1/6': {
                                                    'addr': '10.169.196.213',
                                                    'addr_info': '7F0FF08D46D0',
                                                },
                                            },
                                        },
                                        'repair': {
                                            'tag_midchain': {
                                                'MPLS-SR-Tunnel1': {
                                                    'label': ['98'],
                                                    'tag_adj': {
                                                        'GigabitEthernet0/1/7': {
                                                            'addr': '10.169.196.217',
                                                            'addr_info': '7F0FF0AFB2F8',
                                                        },
                                                    },
                                                    'tag_midchain_info': '7F0FF0AFAC68',
                                                },
                                            },
                                        },
                                    },
                                },
                                'label': ['[51885|16073]-(local:28)'],
                            },
                            'path_list': {
                                '7F0FEC884768': {
                                    'flags': '0x4D [shble, hvsh, rif, hwcn]',
                                    'locks': 19,
                                    'path': {
                                        '7F0FF11E0AE0': {
                                            'flags': '[has-rpr]',
                                            'for': 'IPv4',
                                            'nexthop': {
                                                '10.169.196.213': {
                                                    'outgoing_interface': {
                                                        'GigabitEthernet0/1/6': {
                                                            'ip_adj': {
                                                                'GigabitEthernet0/1/6': {
                                                                    'addr': '10.169.196.213',
                                                                    'addr_info': '7F0FF08D4900',
                                                                },
                                                            },
                                                            'local_label': 28,
                                                            'outgoing_label': ['51885'],
                                                            'outgoing_label_backup': '16073',
                                                        },
                                                    },
                                                },
                                            },
                                            'share': '1/1',
                                            'type': 'attached nexthop',
                                        },
                                    },
                                    'sharing': 'per-destination',
                                },
                            },
                            'refcnt': 7,
                            'rib': '[I]',
                            'sharing': 'per-destination',
                            'sources': ['RIB,', 'RR,', 'LTE'],
                            'subblocks': {
                                1: {
                                    'non_eos_chain_loadinfo': '7F0FF16E6F38',
                                    'per-session': True,
                                    'flags': '0111',
                                    'locks': 8,
                                    'rr_source': ['non-eos indirection', 'heavily shared']
                                },
                            },
                        },
                    },
                },
            },
        },
    },
}

    golden_output_2 = {'execute.return_value': '''
    device_name02#show ip cef 10.100.5.5 internal
Load for five secs: 0%/0%; one minute: 0%; five minutes: 1%
Time source is NTP, 01:05:14.418 EST Tue Nov 5 2019

10.100.5.5/32, epoch 3, RIB[I], refcnt 6, per-destination sharing
  sources: RIB, LTE 
  feature space:
    IPRM: 0x00028000
    Broker: linked, distributed at 4th priority
    LFD: 10.100.5.5/32 2 local labels
    dflt local label info: global/25 [0x23]
    sr local label info: global/17000 [0x1B]
        contains path extension list
        dflt disposition chain 0x7F2B22651570
          label 63300
          FRR Primary
            <primary: TAG adj out of GigabitEthernet0/1/6, addr 10.19.198.25>
        dflt label switch chain 0x7F2B22651570
          label 63300
          FRR Primary
            <primary: TAG adj out of GigabitEthernet0/1/6, addr 10.19.198.25>
        sr disposition chain 0x7F2B22651440
          label 17000
          FRR Primary
            <primary: TAG adj out of GigabitEthernet0/1/6, addr 10.19.198.25>
        sr label switch chain 0x7F2B22651440
          label 17000
          FRR Primary
            <primary: TAG adj out of GigabitEthernet0/1/6, addr 10.19.198.25>
  ifnums:
    GigabitEthernet0/1/6(15): 10.19.198.25
    GigabitEthernet0/1/7(16): 10.19.198.29
  path list 7F2B22A8B0A0, 477 locks, per-destination, flags 0x4D [shble, hvsh, rif, hwcn]
    path 7F2B22A6C220, share 1/1, type attached nexthop, for IPv4, flags [has-rpr]
      MPLS short path extensions: [rib | prfmfi | lblmrg | srlbl] MOI flags = 0x420 label 63300
      nexthop 10.19.198.25 GigabitEthernet0/1/6 label [63300|68544](elc)-(local:25), IP adj out of GigabitEthernet0/1/6, addr 10.19.198.25 7F2B21B247D8
        repair: attached-nexthop 10.19.198.29 GigabitEthernet0/1/7 (7F2B22A6C3C0)
    path 7F2B22A6C3C0, share 1/1, type attached nexthop, for IPv4, flags [rpr, rpr-only]
      MPLS short path extensions: [rib | prfmfi | lblmrg | srlbl] MOI flags = 0x1 label 17000
      nexthop 10.19.198.29 GigabitEthernet0/1/7 label 17000-(local:17000), repair, IP adj out of GigabitEthernet0/1/7, addr 10.19.198.29 7F2B21B24378
  output chain:
    label [63300|68544](elc)-(local:25)
    FRR Primary (0x80007F2B146ED518)
      <primary: TAG adj out of GigabitEthernet0/1/6, addr 10.19.198.25 7F2B21B245A8>
      <repair:  TAG adj out of GigabitEthernet0/1/7, addr 10.19.198.29 7F2B21B24148>'''}

    golden_parsed_output_2 = {
    'vrf': {
        'default': {
            'address_family': {
                'ipv4': {
                    'prefix': {
                        '10.100.5.5/32': {
                            'epoch': 3,
                            'feature_space': {
                                'broker': {
                                    'distribution_priority': 4,
                                },
                                'iprm': '0x00028000',
                                'lfd': {
                                    '10.100.5.5/32': {
                                        'local_labels': 2,
                                    },
                                },
                                'local_label_info': {
                                    'dflt': 'global/25 [0x23]',
                                    'sr': 'global/17000 [0x1B]',
                                },
                                'path_extension_list': {
                                    'dflt': {
                                        'disposition_chain': {
                                            '0x7F2B22651570': {
                                                'frr': {
                                                    'primary': {
                                                        'primary': {
                                                            'tag_adj': {
                                                                'GigabitEthernet0/1/6': {
                                                                    'addr': '10.19.198.25',
                                                                },
                                                            },
                                                        },
                                                    },
                                                },
                                                'label': 63300,
                                            },
                                        },
                                        'label_switch_chain': {
                                            '0x7F2B22651570': {
                                                'frr': {
                                                    'primary': {
                                                        'primary': {
                                                            'tag_adj': {
                                                                'GigabitEthernet0/1/6': {
                                                                    'addr': '10.19.198.25',
                                                                },
                                                            },
                                                        },
                                                    },
                                                },
                                                'label': 63300,
                                            },
                                        },
                                    },
                                    'sr': {
                                        'disposition_chain': {
                                            '0x7F2B22651440': {
                                                'frr': {
                                                    'primary': {
                                                        'primary': {
                                                            'tag_adj': {
                                                                'GigabitEthernet0/1/6': {
                                                                    'addr': '10.19.198.25',
                                                                },
                                                            },
                                                        },
                                                    },
                                                },
                                                'label': 17000,
                                            },
                                        },
                                        'label_switch_chain': {
                                            '0x7F2B22651440': {
                                                'frr': {
                                                    'primary': {
                                                        'primary': {
                                                            'tag_adj': {
                                                                'GigabitEthernet0/1/6': {
                                                                    'addr': '10.19.198.25',
                                                                },
                                                            },
                                                        },
                                                    },
                                                },
                                                'label': 17000,
                                            },
                                        },
                                    },
                                },
                            },
                            'ifnums': {
                                'GigabitEthernet0/1/6': {
                                    'address': '10.19.198.25',
                                    'ifnum': 15,
                                },
                                'GigabitEthernet0/1/7': {
                                    'address': '10.19.198.29',
                                    'ifnum': 16,
                                },
                            },
                            'output_chain': {
                                'frr': {
                                    'primary': {
                                        'info': '0x80007F2B146ED518',
                                        'primary': {
                                            'tag_adj': {
                                                'GigabitEthernet0/1/6': {
                                                    'addr': '10.19.198.25',
                                                    'addr_info': '7F2B21B245A8',
                                                },
                                            },
                                        },
                                        'repair': {
                                            'tag_adj': {
                                                'GigabitEthernet0/1/7': {
                                                    'addr': '10.19.198.29',
                                                    'addr_info': '7F2B21B24148',
                                                },
                                            },
                                        },
                                    },
                                },
                                'label': ['[63300|68544](elc)-(local:25)'],
                            },
                            'path_list': {
                                '7F2B22A8B0A0': {
                                    'flags': '0x4D [shble, hvsh, rif, hwcn]',
                                    'locks': 477,
                                    'path': {
                                        '7F2B22A6C220': {
                                            'flags': '[has-rpr]',
                                            'for': 'IPv4',
                                            'nexthop': {
                                                '10.19.198.25': {
                                                    'outgoing_interface': {
                                                        'GigabitEthernet0/1/6': {
                                                            'ip_adj': {
                                                                'GigabitEthernet0/1/6': {
                                                                    'addr': '10.19.198.25',
                                                                    'addr_info': '7F2B21B247D8',
                                                                },
                                                            },
                                                            'local_label': 25,
                                                            'outgoing_label': ['63300'],
                                                            'outgoing_label_backup': '68544',
                                                            'outgoing_label_info': 'elc',
                                                        },
                                                    },
                                                },
                                            },
                                            'share': '1/1',
                                            'type': 'attached nexthop',
                                        },
                                        '7F2B22A6C3C0': {
                                            'flags': '[rpr,',
                                            'for': 'IPv4',
                                            'nexthop': {
                                                '10.19.198.29': {
                                                    'outgoing_interface': {
                                                        'GigabitEthernet0/1/7': {
                                                            'local_label': 17000,
                                                            'outgoing_label': ['17000'],
                                                        },
                                                    },
                                                },
                                            },
                                            'share': '1/1',
                                            'type': 'attached nexthop',
                                        },
                                    },
                                    'sharing': 'per-destination',
                                },
                            },
                            'refcnt': 6,
                            'rib': '[I]',
                            'sharing': 'per-destination',
                            'sources': ['RIB,', 'LTE'],
                        },
                    },
                },
            },
        },
    },
}

    golden_output_3 = {'execute.return_value': '''
                device_name03#show ip cef vrf MG501 10.55.50.1 internal
            Load for five secs: 0%/0%; one minute: 0%; five minutes: 0%
            Time source is NTP, 11:56:14.594 UTC Tue Nov 5 2019

            10.55.50.1/32, epoch 0, flags [rlbls], RIB[B], refcnt 6, per-destination sharing
            sources: RIB
            feature space:
                IPRM: 0x00018000
                Broker: linked, distributed at 3rd priority
                LFD: 10.55.50.1/32 0 local labels
                    contains path extension list
            ifnums: (none)
            path list 7F4F8A142848, 3 locks, per-destination, flags 0x249 [shble, rif, hwcn, bgp]
                path 7F4F89512770, share 1/1, type recursive, for IPv4, flags [must-be-lbld]
                MPLS short path extensions: [rib] MOI flags = 0x0 label 262
                recursive via 15010[Binding-Sid Label:Default] label 262, fib 7F4F89318CD0, 1 terminal fib, bslbl:Default:15010
                path list 7F4F8A1428E8, 3 locks, per-destination, flags 0x249 [shble, rif, hwcn, bgp]
                    path 7F4F89512430, share 1/1, type attached prefix, for Binding-Sid Label
                        MPLS short path extensions: [rib | lblmrg | srlbl] MOI flags = 0x0 label implicit-null
                        attached to Tunnel65537, TAG midchain out of Tunnel65537 7F4F881C0718
            output chain:
                label 262
                label implicit-null
                TAG midchain out of Tunnel65537 7F4F881C0718    
                label [16073|16073]
                label [90|90]
                label [95|95]
                label [90|90]
                FRR Primary (0x80007F4F894B79F0)
                <primary: TAG adj out of GigabitEthernet0/1/6, addr 10.169.196.213 7F4F881C1898>
                <repair:  label 16061
                            TAG adj out of GigabitEthernet0/1/7, addr 10.169.196.217 7F4F881C1CF8>
            sr_ve-laasr01#'''}
    golden_parsed_output_3 = {
    'vrf': {
        'default': {
            'address_family': {
                'ipv4': {
                    'prefix': {
                        '10.55.50.1/32': {
                            'epoch': 0,
                            'feature_space': {
                                'broker': {
                                    'distribution_priority': 3,
                                },
                                'iprm': '0x00018000',
                                'lfd': {
                                    '10.55.50.1/32': {
                                        'local_labels': 0,
                                    },
                                },
                            },
                            'flags': ['rlbls'],
                            'output_chain': {
                                'label': ['262', 'implicit-null'],
                                'tag_midchain': {
                                    'Tunnel65537': {
                                        'frr': {
                                            'primary': {
                                                'info': '0x80007F4F894B79F0',
                                                'primary': {
                                                    'tag_adj': {
                                                        'GigabitEthernet0/1/6': {
                                                            'addr': '10.169.196.213',
                                                            'addr_info': '7F4F881C1898',
                                                        },
                                                    },
                                                },
                                                'repair': {
                                                    'label': ['16061'],
                                                    'tag_adj': {
                                                        'GigabitEthernet0/1/7': {
                                                            'addr': '10.169.196.217',
                                                            'addr_info': '7F4F881C1CF8',
                                                        },
                                                    },
                                                },
                                            },
                                        },
                                        'label': ['[16073|16073]', '[90|90]', '[95|95]', '[90|90]'],
                                        'tag_midchain_info': '7F4F881C0718',
                                    },
                                },
                            },
                            'path_list': {
                                '7F4F8A142848': {
                                    'flags': '0x249 [shble, rif, hwcn, bgp]',
                                    'locks': 3,
                                    'path': {
                                        '7F4F89512770': {
                                            'flags': '[must-be-lbld]',
                                            'for': 'IPv4',
                                            'share': '1/1',
                                            'type': 'recursive',
                                        },
                                    },
                                    'sharing': 'per-destination',
                                },
                                '7F4F8A1428E8': {
                                    'flags': '0x249 [shble, rif, hwcn, bgp]',
                                    'locks': 3,
                                    'path': {
                                        '7F4F89512430': {
                                            'for': 'Binding-Sid Label',
                                            'share': '1/1',
                                            'type': 'attached prefix',
                                        },
                                    },
                                    'sharing': 'per-destination',
                                },
                            },
                            'refcnt': 6,
                            'rib': '[B]',
                            'sharing': 'per-destination',
                            'sources': ['RIB'],
                        },
                    },
                },
            },
        },
    },
}

    def test_empty(self):
        self.device1 = Mock(**self.empty_output)
        obj = ShowIpCefInternal(device=self.device1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden1(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_1)
        obj = ShowIpCefInternal(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_1)

    def test_golden2(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_2)
        obj = ShowIpCefInternal(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_2)

    def test_golden3(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_3)
        obj = ShowIpCefInternal(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_3)


if __name__ == '__main__':
    unittest.main()