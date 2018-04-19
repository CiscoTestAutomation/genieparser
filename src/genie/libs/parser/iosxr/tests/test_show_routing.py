import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device

from metaparser.util.exceptions import SchemaEmptyParserError, \
                                       SchemaMissingKeyError

from parser.iosxr.show_routing import ShowRouteIpv4, ShowRouteIpv6

# ============================================
# unit test for 'show route ipv4'
# =============================================
class test_show_route_ipv4(unittest.TestCase):
    """
       unit test for show route ipv4
    """
    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}
    golden_output_1 = {'execute.return_value': '''
    RP/0/0/CPU0:R2_xrv#show route ipv4
    Wed Dec  6 15:18:18.928 UTC

    Codes: C - connected, S - static, R - RIP, B - BGP, (>) - Diversion path
           D - EIGRP, EX - EIGRP external, O - OSPF, IA - OSPF inter area
           N1 - OSPF NSSA external type 1, N2 - OSPF NSSA external type 2
           E1 - OSPF external type 1, E2 - OSPF external type 2, E - EGP
           i - ISIS, L1 - IS-IS level-1, L2 - IS-IS level-2
           ia - IS-IS inter area, su - IS-IS summary null, * - candidate default
           U - per-user static route, o - ODR, L - local, G  - DAGR, l - LISP
           A - access/subscriber, a - Application route
           M - mobile route, r - RPL, (!) - FRR Backup path

    Gateway of last resort is not set

    S    1.1.1.1/32 is directly connected, 01:51:13, GigabitEthernet0/0/0/0
                    is directly connected, 01:51:13, GigabitEthernet0/0/0/3
    L    2.2.2.2/32 is directly connected, 01:51:14, Loopback0
    S    3.3.3.3/32 [1/0] via 10.2.3.3, 01:51:13, GigabitEthernet0/0/0/1
                    [1/0] via 20.2.3.3, 01:51:13, GigabitEthernet0/0/0/2
    C    10.1.2.0/24 is directly connected, 01:51:13, GigabitEthernet0/0/0/3
    i L1 21.21.21.21/32 [115/20] via 20.1.2.1, 01:50:50, GigabitEthernet0/0/0/0
                        [115/20] via 10.1.2.1, 01:50:50, GigabitEthernet0/0/0/3
    B    31.31.31.31/32 [200/0] via 11.11.11.11, 00:55:14
    L    32.32.32.32/32 is directly connected, 01:51:14, Loopback3
    B    33.33.33.33/32 [200/0] via 13.13.13.13, 00:52:31
    '''
}
    golden_parsed_output_1 = {
        'vrf':{
            'default':{
                'address_family': {
                    'ipv4': {
                        'routes': {
                            '1.1.1.1/32': {
                                'route': '1.1.1.1/32',
                                'active': True,
                                'source_protocol_codes': 'S',
                                'source_protocol': 'static',
                                'next_hop': {
                                    'outgoing_interface': {
                                        'GigabitEthernet0/0/0/0': {
                                            'outgoing_interface': 'GigabitEthernet0/0/0/0',
                                            'updated': '01:51:13'
                                        },
                                        'GigabitEthernet0/0/0/3': {
                                            'outgoing_interface': 'GigabitEthernet0/0/0/3',
                                            'updated': '01:51:13'
                                        },
                                    },
                                },
                            },
                            '2.2.2.2/32': {
                                'route': '2.2.2.2/32',
                                'active': True,
                                'source_protocol_codes': 'L',
                                'source_protocol': 'local',
                                'next_hop': {
                                    'outgoing_interface': {
                                        'Loopback0': {
                                            'outgoing_interface': 'Loopback0',
                                            'updated': '01:51:14'
                                        },
                                    },
                                },
                            },
                            '3.3.3.3/32': {
                                'route': '3.3.3.3/32',
                                'active': True,
                                'route_preference': 1,
                                'metric': 0,
                                'source_protocol_codes': 'S',
                                'source_protocol': 'static',
                                'next_hop': {
                                    'next_hop_list': {
                                        1: {
                                            'index': 1,
                                            'next_hop': '10.2.3.3',
                                            'outgoing_interface': 'GigabitEthernet0/0/0/1',
                                            'updated': '01:51:13'
                                        },
                                        2: {
                                            'index': 2,
                                            'next_hop': '20.2.3.3',
                                            'outgoing_interface': 'GigabitEthernet0/0/0/2',
                                            'updated': '01:51:13'
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
                                        'GigabitEthernet0/0/0/3': {
                                            'outgoing_interface': 'GigabitEthernet0/0/0/3',
                                            'updated': '01:51:13'
                                        },
                                    },
                                },
                            },
                            '21.21.21.21/32': {
                                'route': '21.21.21.21/32',
                                'active': True,
                                'route_preference': 115,
                                'metric': 20,
                                'source_protocol_codes': 'i L1',
                                'source_protocol': 'isis',
                                'next_hop': {
                                    'next_hop_list': {
                                        1: {
                                            'index': 1,
                                            'next_hop': '20.1.2.1',
                                            'outgoing_interface': 'GigabitEthernet0/0/0/0',
                                            'updated': '01:50:50'
                                        },
                                        2: {
                                            'index': 2,
                                            'next_hop': '10.1.2.1',
                                            'outgoing_interface': 'GigabitEthernet0/0/0/3',
                                            'updated': '01:50:50'
                                        },
                                    },
                                },

                        },
                            '31.31.31.31/32': {
                                'route': '31.31.31.31/32',
                                'active': True,
                                'route_preference': 200,
                                'metric': 0,
                                'source_protocol_codes': 'B',
                                'source_protocol': 'bgp',
                                'next_hop': {
                                    'next_hop_list': {
                                        1: {
                                            'index': 1,
                                            'next_hop': '11.11.11.11',
                                            'updated': '00:55:14'
                                        },
                                    },
                                },

                            },
                            '32.32.32.32/32': {
                                'route': '32.32.32.32/32',
                                'active': True,
                                'source_protocol_codes': 'L',
                                'source_protocol': 'local',
                                'next_hop': {
                                    'outgoing_interface': {
                                        'Loopback3': {
                                            'outgoing_interface': 'Loopback3',
                                            'updated': '01:51:14'
                                        },
                                    },
                                },
                            },
                            '33.33.33.33/32': {
                                'route': '33.33.33.33/32',
                                'active': True,
                                'route_preference': 200,
                                'metric': 0,
                                'source_protocol_codes': 'B',
                                'source_protocol': 'bgp',
                                'next_hop': {
                                    'next_hop_list': {
                                        1: {
                                            'index': 1,
                                            'next_hop': '13.13.13.13',
                                            'updated': '00:52:31'
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
    RP/0/RP0/CPU0:PE1#show route vrf all ipv4

    VRF: VRF501


    Codes: C - connected, S - static, R - RIP, B - BGP, (>) - Diversion path
           D - EIGRP, EX - EIGRP external, O - OSPF, IA - OSPF inter area
           N1 - OSPF NSSA external type 1, N2 - OSPF NSSA external type 2
           E1 - OSPF external type 1, E2 - OSPF external type 2, E - EGP
           i - ISIS, L1 - IS-IS level-1, L2 - IS-IS level-2
           ia - IS-IS inter area, su - IS-IS summary null, * - candidate default
           U - per-user static route, o - ODR, L - local, G  - DAGR, l - LISP
           A - access/subscriber, a - Application route
           M - mobile route, r - RPL, t - Traffic Engineering, (!) - FRR Backup path

    Gateway of last resort is not set

    L    200.1.0.1/32 is directly connected, 1d22h, Loopback501
    C    201.1.0.0/24 is directly connected, 20:03:59, GigabitEthernet0/0/0/0.501
    L    201.1.0.1/32 is directly connected, 20:03:59, GigabitEthernet0/0/0/0.501

    VRF: VRF502


    Codes: C - connected, S - static, R - RIP, B - BGP, (>) - Diversion path
           D - EIGRP, EX - EIGRP external, O - OSPF, IA - OSPF inter area
           N1 - OSPF NSSA external type 1, N2 - OSPF NSSA external type 2
           E1 - OSPF external type 1, E2 - OSPF external type 2, E - EGP
           i - ISIS, L1 - IS-IS level-1, L2 - IS-IS level-2
           ia - IS-IS inter area, su - IS-IS summary null, * - candidate default
           U - per-user static route, o - ODR, L - local, G  - DAGR, l - LISP
           A - access/subscriber, a - Application route
           M - mobile route, r - RPL, t - Traffic Engineering, (!) - FRR Backup path

    Gateway of last resort is not set

    B    12.0.0.0/24 [20/0] via 201.2.0.2, 19:38:48
    B    12.0.1.0/24 [20/0] via 201.2.0.2, 19:38:48
    B    12.0.2.0/24 [20/0] via 201.2.0.2, 19:38:48
    L    200.2.0.1/32 is directly connected, 1d22h, Loopback502
    C    201.2.0.0/24 is directly connected, 20:03:59, GigabitEthernet0/0/0/0.502
    L    201.2.0.1/32 is directly connected, 20:03:59, GigabitEthernet0/0/0/0.502


    VRF: VRF505


    % No matching routes found
    '''}
    golden_parsed_output_2_with_vrf = {
        'vrf': {
            'VRF501': {
                'address_family': {
                    'ipv4': {
                        'routes': {
                            '200.1.0.1/32': {
                                'route': '200.1.0.1/32',
                                'active': True,
                                'source_protocol_codes': 'L',
                                'source_protocol': 'local',
                                'next_hop': {
                                    'outgoing_interface': {
                                        'Loopback501': {
                                            'outgoing_interface': 'Loopback501',
                                            'updated': '1d22h'
                                        },
                                    },
                                },
                            },
                            '201.1.0.0/24': {
                                'route': '201.1.0.0/24',
                                'active': True,
                                'source_protocol_codes': 'C',
                                'source_protocol': 'connected',
                                'next_hop': {
                                    'outgoing_interface': {
                                        'GigabitEthernet0/0/0/0.501': {
                                            'outgoing_interface': 'GigabitEthernet0/0/0/0.501',
                                            'updated': '20:03:59'
                                        },
                                    },
                                },
                            },
                            '201.1.0.1/32': {
                                'route': '201.1.0.1/32',
                                'active': True,
                                'source_protocol_codes': 'L',
                                'source_protocol': 'local',
                                'next_hop': {
                                    'outgoing_interface': {
                                        'GigabitEthernet0/0/0/0.501': {
                                            'outgoing_interface': 'GigabitEthernet0/0/0/0.501',
                                            'updated': '20:03:59'
                                        },
                                    },
                                },
                            },
                        },
                    },
                },
            },
            'VRF502': {
                'address_family': {
                    'ipv4': {
                        'routes': {
                            '12.0.0.0/24': {
                                'route': '12.0.0.0/24',
                                'active': True,
                                'source_protocol_codes': 'B',
                                'source_protocol': 'bgp',
                                'route_preference': 20,
                                'metric': 0,
                                'next_hop': {
                                    'next_hop_list': {
                                        1: {
                                            'index': 1,
                                            'next_hop': '201.2.0.2',
                                            'updated': '19:38:48'
                                        },
                                    },
                                },
                            },
                            '12.0.1.0/24': {
                                'route': '12.0.1.0/24',
                                'active': True,
                                'source_protocol_codes': 'B',
                                'source_protocol': 'bgp',
                                'route_preference': 20,
                                'metric': 0,
                                'next_hop': {
                                    'next_hop_list': {
                                        1: {
                                            'index': 1,
                                            'next_hop': '201.2.0.2',
                                            'updated': '19:38:48'
                                        },
                                    },
                                },
                            },
                            '12.0.2.0/24': {
                                'route': '12.0.2.0/24',
                                'active': True,
                                'source_protocol_codes': 'B',
                                'source_protocol': 'bgp',
                                'route_preference': 20,
                                'metric': 0,
                                'next_hop': {
                                    'next_hop_list': {
                                        1: {
                                            'index': 1,
                                            'next_hop': '201.2.0.2',
                                            'updated': '19:38:48'
                                        },
                                    },
                                },
                            },
                            '200.2.0.1/32': {
                                'route': '200.2.0.1/32',
                                'active': True,
                                'source_protocol_codes': 'L',
                                'source_protocol': 'local',
                                'next_hop': {
                                    'outgoing_interface': {
                                        'Loopback502': {
                                            'outgoing_interface': 'Loopback502',
                                            'updated': '1d22h'
                                        },
                                    },
                                },
                            },
                            '201.2.0.0/24': {
                                'route': '201.2.0.0/24',
                                'active': True,
                                'source_protocol_codes': 'C',
                                'source_protocol': 'connected',
                                'next_hop': {
                                    'outgoing_interface': {
                                        'GigabitEthernet0/0/0/0.502': {
                                            'outgoing_interface': 'GigabitEthernet0/0/0/0.502',
                                            'updated': '20:03:59'
                                        },
                                    },
                                },
                            },
                            '201.2.0.1/32': {
                                'route': '201.2.0.1/32',
                                'active': True,
                                'source_protocol_codes': 'L',
                                'source_protocol': 'local',
                                'next_hop': {
                                    'outgoing_interface': {
                                        'GigabitEthernet0/0/0/0.502': {
                                            'outgoing_interface': 'GigabitEthernet0/0/0/0.502',
                                            'updated': '20:03:59'
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
        obj = ShowRouteIpv4(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_show_route_ipv4_1(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_1)
        obj = ShowRouteIpv4(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output_1)


    def test_show_route_ipv4_2_with_vrf(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_2_with_vrf)
        obj = ShowRouteIpv4(device=self.device)
        parsed_output = obj.parse(vrf='all')
        self.assertEqual(parsed_output, self.golden_parsed_output_2_with_vrf)


# ============================================
# unit test for 'show route ipv6'
# =============================================
class test_show_route_ipv6(unittest.TestCase):
    """
       unit test for show route ipv6
    """
    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}
    golden_output_1 = {'execute.return_value': '''
    RP/0/0/CPU0:R2_xrv#show route ipv6
Wed Dec  6 15:19:28.823 UTC

Codes: C - connected, S - static, R - RIP, B - BGP, (>) - Diversion path
       D - EIGRP, EX - EIGRP external, O - OSPF, IA - OSPF inter area
       N1 - OSPF NSSA external type 1, N2 - OSPF NSSA external type 2
       E1 - OSPF external type 1, E2 - OSPF external type 2, E - EGP
       i - ISIS, L1 - IS-IS level-1, L2 - IS-IS level-2
       ia - IS-IS inter area, su - IS-IS summary null, * - candidate default
       U - per-user static route, o - ODR, L - local, G  - DAGR, l - LISP
       A - access/subscriber, a - Application route
       M - mobile route, r - RPL, (!) - FRR Backup path

Gateway of last resort is not set

S    2001:1:1:1::1/128
      [1/0] via 2001:20:1:2::1, 01:52:23, GigabitEthernet0/0/0/0
      [1/0] via 2001:10:1:2::1, 01:52:23, GigabitEthernet0/0/0/3
L    2001:2:2:2::2/128 is directly connected,
      01:52:24, Loopback0
S    2001:3:3:3::3/128
      [1/0] via 2001:10:2:3::3, 01:52:23, GigabitEthernet0/0/0/1
      [1/0] via 2001:20:2:3::3, 01:52:23, GigabitEthernet0/0/0/2
i L1 2001:21:21:21::21/128
      [115/20] via fe80::5054:ff:fe54:6569, 00:56:34, GigabitEthernet0/0/0/0
      [115/20] via fe80::5054:ff:fea5:829 (nexthop in vrf default), 00:56:34, GigabitEthernet0/0/0/3
L    2001:32:32:32::32/128 is directly connected,
      01:52:24, Loopback3
B    2001:33:33:33::33/128
      [200/0] via 2001:13:13:13::13, 00:53:22

    '''
}
    golden_parsed_output_1 = {
        'vrf':{
            'default':{
                'address_family': {
                    'ipv6': {
                        'routes': {
                            '2001:1:1:1::1/128': {
                                'route': '2001:1:1:1::1/128',
                                'active': True,
                                'source_protocol_codes': 'S',
                                'source_protocol': 'static',
                                'route_preference': 1,
                                'metric': 0,
                                'next_hop': {
                                    'next_hop_list': {
                                        1: {
                                            'index': 1,
                                            'next_hop': '2001:20:1:2::1',
                                            'outgoing_interface': 'GigabitEthernet0/0/0/0',
                                            'updated': '01:52:23'
                                        },
                                        2: {
                                            'index': 2,
                                            'next_hop': '2001:10:1:2::1',
                                            'outgoing_interface': 'GigabitEthernet0/0/0/3',
                                            'updated': '01:52:23'
                                        },

                                    },
                                },
                            },
                            '2001:2:2:2::2/128': {
                                'route': '2001:2:2:2::2/128',
                                'active': True,
                                'source_protocol_codes': 'L',
                                'source_protocol': 'local',
                                'next_hop': {
                                    'outgoing_interface': {
                                        'Loopback0': {
                                            'outgoing_interface': 'Loopback0',
                                            'updated': '01:52:24'
                                        },
                                    },
                                },
                            },
                            '2001:3:3:3::3/128': {
                                'route': '2001:3:3:3::3/128',
                                'active': True,
                                'source_protocol_codes': 'S',
                                'source_protocol': 'static',
                                'route_preference': 1,
                                'metric': 0,
                                'next_hop': {
                                    'next_hop_list': {
                                        1: {
                                            'index': 1,
                                            'next_hop': '2001:10:2:3::3',
                                            'outgoing_interface': 'GigabitEthernet0/0/0/1',
                                            'updated': '01:52:23'
                                        },
                                        2: {
                                            'index': 2,
                                            'next_hop': '2001:20:2:3::3',
                                            'outgoing_interface': 'GigabitEthernet0/0/0/2',
                                            'updated': '01:52:23'
                                        },

                                    },
                                },
                            },
                            '2001:21:21:21::21/128': {
                                'route': '2001:21:21:21::21/128',
                                'active': True,
                                'source_protocol_codes': 'i L1',
                                'source_protocol': 'isis',
                                'route_preference': 115,
                                'metric': 20,
                                'next_hop': {
                                    'next_hop_list': {
                                        1: {
                                            'index': 1,
                                            'next_hop': 'fe80::5054:ff:fe54:6569',
                                            'outgoing_interface': 'GigabitEthernet0/0/0/0',
                                            'updated': '00:56:34'
                                        },
                                        2: {
                                            'index': 2,
                                            'next_hop': 'fe80::5054:ff:fea5:829',
                                            'outgoing_interface': 'GigabitEthernet0/0/0/3',
                                            'updated': '00:56:34'
                                        },

                                    },
                                },
                            },
                            '2001:32:32:32::32/128': {
                                'route': '2001:32:32:32::32/128',
                                'active': True,
                                'source_protocol_codes': 'L',
                                'source_protocol': 'local',
                                'next_hop': {
                                    'outgoing_interface': {
                                        'Loopback3': {
                                            'outgoing_interface': 'Loopback3',
                                            'updated': '01:52:24'
                                        },
                                    },
                                },
                            },
                            '2001:33:33:33::33/128': {
                                'route': '2001:33:33:33::33/128',
                                'active': True,
                                'route_preference': 200,
                                'metric': 0,
                                'source_protocol_codes': 'B',
                                'source_protocol': 'bgp',
                                'next_hop': {
                                    'next_hop_list': {
                                        1: {
                                            'index': 1,
                                            'next_hop': '2001:13:13:13::13',
                                            'updated': '00:53:22'
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
RP/0/RP0/CPU0:PE1#show route vrf all ipv6

VRF: VRF501

Codes: C - connected, S - static, R - RIP, B - BGP, (>) - Diversion path
       D - EIGRP, EX - EIGRP external, O - OSPF, IA - OSPF inter area
       N1 - OSPF NSSA external type 1, N2 - OSPF NSSA external type 2
       E1 - OSPF external type 1, E2 - OSPF external type 2, E - EGP
       i - ISIS, L1 - IS-IS level-1, L2 - IS-IS level-2
       ia - IS-IS inter area, su - IS-IS summary null, * - candidate default
       U - per-user static route, o - ODR, L - local, G  - DAGR, l - LISP
       A - access/subscriber, a - Application route
       M - mobile route, r - RPL, t - Traffic Engineering, (!) - FRR Backup path

Gateway of last resort is not set

O E2 11::/64
      [110/0] via fe80::200:ff:fe33:3a83, 20:03:53, GigabitEthernet0/0/0/0.501
O E2 11:0:0:9::/64
      [110/0] via fe80::200:ff:fe33:3a83, 20:03:53, GigabitEthernet0/0/0/0.501
L    2000:1::1/128 is directly connected,
      1d22h, Loopback501
C    2001:1::/112 is directly connected,
      20:04:59, GigabitEthernet0/0/0/0.501
L    2001:1::1/128 is directly connected,
      20:04:59, GigabitEthernet0/0/0/0.501

VRF: VRF502


Codes: C - connected, S - static, R - RIP, B - BGP, (>) - Diversion path
       D - EIGRP, EX - EIGRP external, O - OSPF, IA - OSPF inter area
       N1 - OSPF NSSA external type 1, N2 - OSPF NSSA external type 2
       E1 - OSPF external type 1, E2 - OSPF external type 2, E - EGP
       i - ISIS, L1 - IS-IS level-1, L2 - IS-IS level-2
       ia - IS-IS inter area, su - IS-IS summary null, * - candidate default
       U - per-user static route, o - ODR, L - local, G  - DAGR, l - LISP
       A - access/subscriber, a - Application route
       M - mobile route, r - RPL, t - Traffic Engineering, (!) - FRR Backup path

Gateway of last resort is not set

B    12::/64
      [20/0] via fe80::200:ff:fe33:3a84, 19:39:47, GigabitEthernet0/0/0/0.502
B    12:0:0:1::/64
      [20/0] via fe80::200:ff:fe33:3a84, 19:39:47, GigabitEthernet0/0/0/0.502
B    12:0:0:9::/64
      [20/0] via fe80::200:ff:fe33:3a84, 19:39:47, GigabitEthernet0/0/0/0.502
L    2000:2::1/128 is directly connected,
      1d22h, Loopback502
C    2001:2::/112 is directly connected,
      20:05:00, GigabitEthernet0/0/0/0.502
L    2001:2::1/128 is directly connected,
      20:05:00, GigabitEthernet0/0/0/0.502

VRF: VRF503


Codes: C - connected, S - static, R - RIP, B - BGP, (>) - Diversion path
       D - EIGRP, EX - EIGRP external, O - OSPF, IA - OSPF inter area
       N1 - OSPF NSSA external type 1, N2 - OSPF NSSA external type 2
       E1 - OSPF external type 1, E2 - OSPF external type 2, E - EGP
       i - ISIS, L1 - IS-IS level-1, L2 - IS-IS level-2
       ia - IS-IS inter area, su - IS-IS summary null, * - candidate default
       U - per-user static route, o - ODR, L - local, G  - DAGR, l - LISP
       A - access/subscriber, a - Application route
       M - mobile route, r - RPL, t - Traffic Engineering, (!) - FRR Backup path

Gateway of last resort is not set

S    100::1/128
      [1/0] via 2001:3::2, 20:05:00
L    2000:3::1/128 is directly connected,
      1d22h, Loopback503
C    2001:3::/112 is directly connected,
      20:05:00, GigabitEthernet0/0/0/0.503
L    2001:3::1/128 is directly connected,
      20:05:00, GigabitEthernet0/0/0/0.503

VRF: VRF505


% No matching routes found
    '''}
    golden_parsed_output_2 = {
        'vrf': {
            'VRF501': {
                'address_family': {
                    'ipv6': {
                        'routes': {
                            '11::/64': {
                                'route': '11::/64',
                                'active': True,
                                'source_protocol_codes': 'O E2',
                                'source_protocol': 'ospf',
                                'route_preference': 110,
                                'metric': 0,
                                'next_hop': {
                                    'next_hop_list': {
                                        1: {
                                            'index': 1,
                                            'next_hop': 'fe80::200:ff:fe33:3a83',
                                            'outgoing_interface': 'GigabitEthernet0/0/0/0.501',
                                            'updated': '20:03:53'
                                        },

                                    },
                                },
                            },
                            '11:0:0:9::/64': {
                                'route': '11:0:0:9::/64',
                                'active': True,
                                'source_protocol_codes': 'O E2',
                                'source_protocol': 'ospf',
                                'route_preference': 110,
                                'metric': 0,
                                'next_hop': {
                                    'next_hop_list': {
                                        1: {
                                            'index': 1,
                                            'next_hop': 'fe80::200:ff:fe33:3a83',
                                            'outgoing_interface': 'GigabitEthernet0/0/0/0.501',
                                            'updated': '20:03:53'
                                        },

                                    },
                                },
                            },
                            '2000:1::1/128': {
                                'route': '2000:1::1/128',
                                'active': True,
                                'source_protocol_codes': 'L',
                                'source_protocol': 'local',
                                'next_hop': {
                                    'outgoing_interface': {
                                        'Loopback501': {
                                            'outgoing_interface': 'Loopback501',
                                            'updated': '1d22h'
                                        },
                                    },
                                },
                            },
                            '2001:1::/112': {
                                'route': '2001:1::/112',
                                'active': True,
                                'source_protocol_codes': 'C',
                                'source_protocol': 'connected',
                                'next_hop': {
                                    'outgoing_interface': {
                                        'GigabitEthernet0/0/0/0.501': {
                                            'outgoing_interface': 'GigabitEthernet0/0/0/0.501',
                                            'updated': '20:04:59'
                                        },
                                    },
                                },
                            },
                            '2001:1::1/128': {
                                'route': '2001:1::1/128',
                                'active': True,
                                'source_protocol_codes': 'L',
                                'source_protocol': 'local',
                                'next_hop': {
                                    'outgoing_interface': {
                                        'GigabitEthernet0/0/0/0.501': {
                                            'outgoing_interface': 'GigabitEthernet0/0/0/0.501',
                                            'updated': '20:04:59'
                                        },
                                    },
                                },
                            },

                        },
                    },
                },
            },
            'VRF502': {
                'address_family': {
                    'ipv6': {
                        'routes': {
                            '12::/64': {
                                'route': '12::/64',
                                'active': True,
                                'source_protocol_codes': 'B',
                                'source_protocol': 'bgp',
                                'route_preference': 20,
                                'metric': 0,
                                'next_hop': {
                                    'next_hop_list': {
                                        1: {
                                            'index': 1,
                                            'next_hop': 'fe80::200:ff:fe33:3a84',
                                            'outgoing_interface': 'GigabitEthernet0/0/0/0.502',
                                            'updated': '19:39:47'
                                        },

                                    },
                                },
                            },
                            '12:0:0:1::/64': {
                                'route': '12:0:0:1::/64',
                                'active': True,
                                'source_protocol_codes': 'B',
                                'source_protocol': 'bgp',
                                'route_preference': 20,
                                'metric': 0,
                                'next_hop': {
                                    'next_hop_list': {
                                        1: {
                                            'index': 1,
                                            'next_hop': 'fe80::200:ff:fe33:3a84',
                                            'outgoing_interface': 'GigabitEthernet0/0/0/0.502',
                                            'updated': '19:39:47'
                                        },

                                    },
                                },
                            },
                            '12:0:0:9::/64': {
                                'route': '12:0:0:9::/64',
                                'active': True,
                                'source_protocol_codes': 'B',
                                'source_protocol': 'bgp',
                                'route_preference': 20,
                                'metric': 0,
                                'next_hop': {
                                    'next_hop_list': {
                                        1: {
                                            'index': 1,
                                            'next_hop': 'fe80::200:ff:fe33:3a84',
                                            'outgoing_interface': 'GigabitEthernet0/0/0/0.502',
                                            'updated': '19:39:47'
                                        },

                                    },
                                },
                            },
                            '2000:2::1/128': {
                                'route': '2000:2::1/128',
                                'active': True,
                                'source_protocol_codes': 'L',
                                'source_protocol': 'local',
                                'next_hop': {
                                    'outgoing_interface': {
                                        'Loopback502': {
                                            'outgoing_interface': 'Loopback502',
                                            'updated': '1d22h'
                                        },
                                    },
                                },
                            },
                            '2001:2::/112': {
                                'route': '2001:2::/112',
                                'active': True,
                                'source_protocol_codes': 'C',
                                'source_protocol': 'connected',
                                'next_hop': {
                                    'outgoing_interface': {
                                        'GigabitEthernet0/0/0/0.502': {
                                            'outgoing_interface': 'GigabitEthernet0/0/0/0.502',
                                            'updated': '20:05:00'
                                        },
                                    },
                                },
                            },
                            '2001:2::1/128': {
                                'route': '2001:2::1/128',
                                'active': True,
                                'source_protocol_codes': 'L',
                                'source_protocol': 'local',
                                'next_hop': {
                                    'outgoing_interface': {
                                        'GigabitEthernet0/0/0/0.502': {
                                            'outgoing_interface': 'GigabitEthernet0/0/0/0.502',
                                            'updated': '20:05:00'
                                        },
                                    },
                                },
                            },

                        },
                    },
                },
            },
            'VRF503': {
                'address_family': {
                    'ipv6': {
                        'routes': {
                            '100::1/128': {
                                'route': '100::1/128',
                                'active': True,
                                'source_protocol_codes': 'S',
                                'source_protocol': 'static',
                                'route_preference': 1,
                                'metric': 0,
                                'next_hop': {
                                    'next_hop_list': {
                                        1: {
                                            'index': 1,
                                            'next_hop': '2001:3::2',
                                            'updated': '20:05:00'
                                        },

                                    },
                                },
                            },
                            '2000:3::1/128': {
                                'route': '2000:3::1/128',
                                'active': True,
                                'source_protocol_codes': 'L',
                                'source_protocol': 'local',
                                'next_hop': {
                                    'outgoing_interface': {
                                        'Loopback503': {
                                            'outgoing_interface': 'Loopback503',
                                            'updated': '1d22h'
                                        },
                                    },
                                },
                            },
                            '2001:3::/112': {
                                'route': '2001:3::/112',
                                'active': True,
                                'source_protocol_codes': 'C',
                                'source_protocol': 'connected',
                                'next_hop': {
                                    'outgoing_interface': {
                                        'GigabitEthernet0/0/0/0.503': {
                                            'outgoing_interface': 'GigabitEthernet0/0/0/0.503',
                                            'updated': '20:05:00'
                                        },
                                    },
                                },
                            },
                            '2001:3::1/128': {
                                'route': '2001:3::1/128',
                                'active': True,
                                'source_protocol_codes': 'L',
                                'source_protocol': 'local',
                                'next_hop': {
                                    'outgoing_interface': {
                                        'GigabitEthernet0/0/0/0.503': {
                                            'outgoing_interface': 'GigabitEthernet0/0/0/0.503',
                                            'updated': '20:05:00'
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
        obj = ShowRouteIpv6(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_show_route_ipv6_1(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_1)
        obj = ShowRouteIpv6(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output_1)


    def test_show_route_ipv6_2(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_2)
        obj = ShowRouteIpv6(device=self.device)
        parsed_output = obj.parse(vrf='all')
        self.assertEqual(parsed_output,self.golden_parsed_output_2)

if __name__ == '__main__':
    unittest.main()