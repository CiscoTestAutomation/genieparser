import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device

from genie.metaparser.util.exceptions import SchemaEmptyParserError, \
                                       SchemaMissingKeyError

from genie.libs.parser.iosxr.show_routing import ShowRouteIpv4, ShowRouteIpv6

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

    S    10.4.1.1/32 is directly connected, 01:51:13, GigabitEthernet0/0/0/0
                    is directly connected, 01:51:13, GigabitEthernet0/0/0/3
    L    10.16.2.2/32 is directly connected, 01:51:14, Loopback0
    S    10.36.3.3/32 [1/0] via 10.2.3.3, 01:51:13, GigabitEthernet0/0/0/1
                    [1/0] via 10.229.3.3, 01:51:13, GigabitEthernet0/0/0/2
    C    10.1.2.0/24 is directly connected, 01:51:13, GigabitEthernet0/0/0/3
    i L1 10.234.21.21/32 [115/20] via 10.186.2.1, 01:50:50, GigabitEthernet0/0/0/0
                        [115/20] via 10.1.2.1, 01:50:50, GigabitEthernet0/0/0/3
    B    10.19.31.31/32 [200/0] via 10.229.11.11, 00:55:14
    L    10.16.32.32/32 is directly connected, 01:51:14, Loopback3
    B    10.21.33.33/32 [200/0] via 10.166.13.13, 00:52:31
    '''
}
    golden_parsed_output_1 = {
        'vrf':{
            'default':{
                'address_family': {
                    'ipv4': {
                        'routes': {
                            '10.4.1.1/32': {
                                'route': '10.4.1.1/32',
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
                            '10.16.2.2/32': {
                                'route': '10.16.2.2/32',
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
                            '10.36.3.3/32': {
                                'route': '10.36.3.3/32',
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
                                            'next_hop': '10.229.3.3',
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
                            '10.234.21.21/32': {
                                'route': '10.234.21.21/32',
                                'active': True,
                                'route_preference': 115,
                                'metric': 20,
                                'source_protocol_codes': 'i L1',
                                'source_protocol': 'isis',
                                'next_hop': {
                                    'next_hop_list': {
                                        1: {
                                            'index': 1,
                                            'next_hop': '10.186.2.1',
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
                            '10.19.31.31/32': {
                                'route': '10.19.31.31/32',
                                'active': True,
                                'route_preference': 200,
                                'metric': 0,
                                'source_protocol_codes': 'B',
                                'source_protocol': 'bgp',
                                'next_hop': {
                                    'next_hop_list': {
                                        1: {
                                            'index': 1,
                                            'next_hop': '10.229.11.11',
                                            'updated': '00:55:14'
                                        },
                                    },
                                },

                            },
                            '10.16.32.32/32': {
                                'route': '10.16.32.32/32',
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
                            '10.21.33.33/32': {
                                'route': '10.21.33.33/32',
                                'active': True,
                                'route_preference': 200,
                                'metric': 0,
                                'source_protocol_codes': 'B',
                                'source_protocol': 'bgp',
                                'next_hop': {
                                    'next_hop_list': {
                                        1: {
                                            'index': 1,
                                            'next_hop': '10.166.13.13',
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

    L    192.168.111.1/32 is directly connected, 1d22h, Loopback501
    C    192.168.4.0/24 is directly connected, 20:03:59, GigabitEthernet0/0/0/0.501
    L    192.168.4.1/32 is directly connected, 20:03:59, GigabitEthernet0/0/0/0.501

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

    B    10.144.0.0/24 [20/0] via 192.168.154.2, 19:38:48
    B    10.144.1.0/24 [20/0] via 192.168.154.2, 19:38:48
    B    10.144.2.0/24 [20/0] via 192.168.154.2, 19:38:48
    L    192.168.4.1/32 is directly connected, 1d22h, Loopback502
    C    192.168.154.0/24 is directly connected, 20:03:59, GigabitEthernet0/0/0/0.502
    L    192.168.154.1/32 is directly connected, 20:03:59, GigabitEthernet0/0/0/0.502


    VRF: VRF505


    % No matching routes found
    '''}
    golden_parsed_output_2_with_vrf = {
        'vrf': {
            'VRF501': {
                'address_family': {
                    'ipv4': {
                        'routes': {
                            '192.168.111.1/32': {
                                'route': '192.168.111.1/32',
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
                            '192.168.4.0/24': {
                                'route': '192.168.4.0/24',
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
                            '192.168.4.1/32': {
                                'route': '192.168.4.1/32',
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
                            '10.144.0.0/24': {
                                'route': '10.144.0.0/24',
                                'active': True,
                                'source_protocol_codes': 'B',
                                'source_protocol': 'bgp',
                                'route_preference': 20,
                                'metric': 0,
                                'next_hop': {
                                    'next_hop_list': {
                                        1: {
                                            'index': 1,
                                            'next_hop': '192.168.154.2',
                                            'updated': '19:38:48'
                                        },
                                    },
                                },
                            },
                            '10.144.1.0/24': {
                                'route': '10.144.1.0/24',
                                'active': True,
                                'source_protocol_codes': 'B',
                                'source_protocol': 'bgp',
                                'route_preference': 20,
                                'metric': 0,
                                'next_hop': {
                                    'next_hop_list': {
                                        1: {
                                            'index': 1,
                                            'next_hop': '192.168.154.2',
                                            'updated': '19:38:48'
                                        },
                                    },
                                },
                            },
                            '10.144.2.0/24': {
                                'route': '10.144.2.0/24',
                                'active': True,
                                'source_protocol_codes': 'B',
                                'source_protocol': 'bgp',
                                'route_preference': 20,
                                'metric': 0,
                                'next_hop': {
                                    'next_hop_list': {
                                        1: {
                                            'index': 1,
                                            'next_hop': '192.168.154.2',
                                            'updated': '19:38:48'
                                        },
                                    },
                                },
                            },
                            '192.168.4.1/32': {
                                'route': '192.168.4.1/32',
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
                            '192.168.154.0/24': {
                                'route': '192.168.154.0/24',
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
                            '192.168.154.1/32': {
                                'route': '192.168.154.1/32',
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

    golden_output_3_with_vrf = {'execute.return_value':'''
        show route vrf gsn2 ipv4

        Thu Sep  5 14:14:08.981 UTC

        Codes: C - connected, S - static, R - RIP, B - BGP, (>) - Diversion path
               D - EIGRP, EX - EIGRP external, O - OSPF, IA - OSPF inter area
               N1 - OSPF NSSA external type 1, N2 - OSPF NSSA external type 2
               E1 - OSPF external type 1, E2 - OSPF external type 2, E - EGP
               i - ISIS, L1 - IS-IS level-1, L2 - IS-IS level-2
               ia - IS-IS inter area, su - IS-IS summary null, * - candidate default
               U - per-user static route, o - ODR, L - local, G  - DAGR, l - LISP
               A - access/subscriber, a - Application route
               M - mobile route, r - RPL, (!) - FRR Backup path

        Gateway of last resort is 172.23.6.198 to network 0.0.0.0

        B*   0.0.0.0/0 [200/0] via 172.23.6.198 (nexthop in vrf default), 08:11:19
        B    10.93.64.0/18 [200/0] via 172.23.36.198 (nexthop in vrf default), 1w5d
        B    10.93.128.0/18 [200/0] via 172.23.40.199 (nexthop in vrf default), 5w1d
        B    10.100.0.0/27 [200/0] via 172.23.6.198 (nexthop in vrf default), 5d13h
        B    10.100.1.0/27 [200/0] via 172.23.6.198 (nexthop in vrf default), 5d13h
        B    10.100.3.0/31 [200/0] via 172.23.6.198 (nexthop in vrf default), 27w5d
        B    10.100.3.2/31 [200/0] via 172.23.6.199 (nexthop in vrf default), 27w5d
        B    10.100.3.32/29 [200/0] via 172.23.6.198 (nexthop in vrf default), 5d13h
        B    10.100.3.96/31 [200/0] via 172.23.6.198 (nexthop in vrf default), 5d13h
        B    10.100.3.98/31 [200/0] via 172.23.6.198 (nexthop in vrf default), 5d13h
        B    10.100.3.104/31 [200/0] via 172.23.6.198 (nexthop in vrf default), 5d13h
        B    10.100.3.136/31 [200/0] via 172.23.6.198 (nexthop in vrf default), 5d13h
        B    10.100.3.138/31 [200/0] via 172.23.6.198 (nexthop in vrf default), 5d13h
        B    10.100.3.144/31 [200/0] via 172.23.6.198 (nexthop in vrf default), 5d13h
        B    10.100.3.146/31 [200/0] via 172.23.6.198 (nexthop in vrf default), 5d13h
        B    10.100.3.160/31 [200/0] via 172.23.6.198 (nexthop in vrf default), 5d13h
        B    10.100.3.162/31 [200/0] via 172.23.6.198 (nexthop in vrf default), 5d13h
        B    10.100.3.168/31 [200/0] via 172.23.6.198 (nexthop in vrf default), 5d13h
        B    10.100.3.170/31 [200/0] via 172.23.6.198 (nexthop in vrf default), 5d13h
        B    10.100.4.0/27 [200/0] via 172.23.8.199 (nexthop in vrf default), 5d14h
        B    10.100.7.0/31 [200/0] via 172.23.8.198 (nexthop in vrf default), 8w0d
        B    10.100.7.2/31 [200/0] via 172.23.8.199 (nexthop in vrf default), 13w5d
        B    10.100.7.32/29 [200/0] via 172.23.8.199 (nexthop in vrf default), 5d14h
        B    10.100.7.96/31 [200/0] via 172.23.8.199 (nexthop in vrf default), 5d14h
        B    10.100.7.98/31 [200/0] via 172.23.8.199 (nexthop in vrf default), 5d14h
        B    10.100.7.104/31 [200/0] via 172.23.8.199 (nexthop in vrf default), 5d14h
        B    10.100.7.136/31 [200/0] via 172.23.8.199 (nexthop in vrf default), 5d14h
        B    10.100.7.138/31 [200/0] via 172.23.8.199 (nexthop in vrf default), 5d14h
        B    10.100.7.160/31 [200/0] via 172.23.8.199 (nexthop in vrf default), 5d14h
        B    10.100.7.162/31 [200/0] via 172.23.8.199 (nexthop in vrf default), 5d14h
        B    10.100.8.0/27 [20/0] via 10.100.11.1, 5d13h
        B    10.100.9.0/27 [20/0] via 10.100.11.1, 5d13h
        C    10.100.11.0/31 is directly connected, 36w5d, GigabitEthernet0/0/1/8
        L    10.100.11.0/32 is directly connected, 36w5d, GigabitEthernet0/0/1/8
        B    10.100.11.2/31 [20/0] via 10.100.11.1, 27w5d
        C    10.100.11.16/29 is directly connected, 36w5d, BVI3001
        L    10.100.11.17/32 [0/0] via 10.100.11.17, 36w5d, BVI3001
        L    10.100.11.18/32 is directly connected, 36w5d, BVI3001
        B    10.100.11.96/31 [20/0] via 10.100.11.1, 5d13h
        B    10.100.11.98/31 [20/0] via 10.100.11.1, 5d13h
        B    10.100.11.104/31 [20/0] via 10.100.11.1, 5d13h
        B    10.100.32.0/27 [200/0] via 172.23.36.198 (nexthop in vrf default), 1w5d
        B    10.100.33.0/27 [200/0] via 172.23.36.198 (nexthop in vrf default), 1w5d
        B    10.100.33.32/28 [200/0] via 172.23.36.198 (nexthop in vrf default), 1w5d
        B    10.100.33.48/28 [200/0] via 172.23.36.198 (nexthop in vrf default), 1w5d
        B    10.100.35.0/31 [200/0] via 172.23.36.198 (nexthop in vrf default), 7w0d
        B    10.100.35.2/31 [200/0] via 172.23.36.199 (nexthop in vrf default), 14w5d
        B    10.100.35.16/29 [200/0] via 172.23.36.198 (nexthop in vrf default), 1w5d
        B    10.100.35.32/29 [200/0] via 172.23.36.198 (nexthop in vrf default), 1w5d
        B    10.100.35.96/31 [200/0] via 172.23.36.198 (nexthop in vrf default), 1w5d
        B    10.100.35.98/31 [200/0] via 172.23.36.198 (nexthop in vrf default), 1w5d
        B    10.100.35.104/31 [200/0] via 172.23.36.198 (nexthop in vrf default), 1w5d
        B    10.100.35.136/31 [200/0] via 172.23.36.198 (nexthop in vrf default), 1w5d
        B    10.100.35.138/31 [200/0] via 172.23.36.198 (nexthop in vrf default), 1w5d
        B    10.100.35.144/31 [200/0] via 172.23.36.198 (nexthop in vrf default), 1w5d
        B    10.100.35.146/31 [200/0] via 172.23.36.198 (nexthop in vrf default), 1w5d
        B    10.100.35.176/31 [200/0] via 172.23.36.198 (nexthop in vrf default), 1w5d
        B    10.100.35.178/31 [200/0] via 172.23.36.198 (nexthop in vrf default), 1w5d
        B    10.100.35.184/31 [200/0] via 172.23.36.198 (nexthop in vrf default), 1w5d
        B    10.100.35.186/31 [200/0] via 172.23.36.198 (nexthop in vrf default), 1w5d
        B    10.100.36.0/27 [200/0] via 172.23.40.199 (nexthop in vrf default), 5w1d
        B    10.100.37.0/27 [200/0] via 172.23.40.199 (nexthop in vrf default), 5w1d
        B    10.100.37.32/28 [200/0] via 172.23.40.199 (nexthop in vrf default), 5w1d
        B    10.100.37.48/28 [200/0] via 172.23.40.199 (nexthop in vrf default), 5w1d
        B    10.100.39.0/31 [200/0] via 172.23.40.198 (nexthop in vrf default), 15w4d
        B    10.100.39.2/31 [200/0] via 172.23.40.199 (nexthop in vrf default), 15w4d
        B    10.100.39.16/29 [200/0] via 172.23.40.199 (nexthop in vrf default), 5w1d
        B    10.100.39.32/29 [200/0] via 172.23.40.199 (nexthop in vrf default), 5w1d
        B    10.100.39.96/31 [200/0] via 172.23.40.199 (nexthop in vrf default), 5w1d
        B    10.100.39.98/31 [200/0] via 172.23.40.199 (nexthop in vrf default), 5w1d
        B    10.100.39.104/31 [200/0] via 172.23.40.199 (nexthop in vrf default), 5w1d
        B    10.100.39.136/31 [200/0] via 172.23.40.199 (nexthop in vrf default), 5w1d
        B    10.100.39.138/31 [200/0] via 172.23.40.199 (nexthop in vrf default), 5w1d
        B    10.100.39.176/31 [200/0] via 172.23.40.199 (nexthop in vrf default), 5w1d
        B    10.100.39.178/31 [200/0] via 172.23.40.199 (nexthop in vrf default), 5w1d
        B    10.100.66.0/27 [200/0] via 172.23.8.199 (nexthop in vrf default), 5d14h
        B    10.100.100.1/32 [200/0] via 172.23.36.198 (nexthop in vrf default), 1w5d
        B    10.100.100.100/32 [20/0] via 10.100.11.1, 5d13h
        B    10.100.160.0/22 [200/0] via 172.23.36.198 (nexthop in vrf default), 1w5d
        B    10.100.164.0/22 [200/0] via 172.23.40.199 (nexthop in vrf default), 5w1d
        B    10.101.194.0/23 [20/0] via 10.100.11.1, 31w5d
        B    10.101.196.0/23 [20/0] via 10.100.11.1, 31w5d
        B    10.103.64.0/23 [200/0] via 172.23.36.198 (nexthop in vrf default), 1w5d
        B    10.103.66.0/24 [200/0] via 172.23.36.198 (nexthop in vrf default), 1w5d
        B    10.103.68.0/24 [200/0] via 172.23.36.198 (nexthop in vrf default), 1w5d
        B    10.103.70.0/23 [200/0] via 172.23.36.198 (nexthop in vrf default), 1w0d
        B    10.103.72.0/24 [200/0] via 172.23.36.198 (nexthop in vrf default), 1w5d
        B    10.103.80.0/24 [200/0] via 172.23.36.198 (nexthop in vrf default), 1w5d
        B    10.103.128.0/24 [200/0] via 172.23.40.199 (nexthop in vrf default), 5w1d
        B    10.103.130.0/24 [200/0] via 172.23.40.199 (nexthop in vrf default), 5w1d
        B    10.103.132.0/24 [200/0] via 172.23.40.199 (nexthop in vrf default), 5w1d
        B    10.103.134.0/23 [200/0] via 172.23.40.199 (nexthop in vrf default), 5w1d
        B    10.103.144.0/24 [200/0] via 172.23.40.199 (nexthop in vrf default), 5w1d
        B    10.111.195.0/27 [20/0] via 10.100.11.1, 31w5d
        B    10.111.195.64/27 [20/0] via 10.100.11.1, 31w5d
        B    10.111.195.128/27 [20/0] via 10.100.11.1, 31w5d
        B    10.111.254.0/27 [20/0] via 10.100.11.1, 31w5d
        B    10.111.254.32/27 [20/0] via 10.100.11.1, 31w5d
        B    10.113.64.0/23 [200/0] via 172.23.36.198 (nexthop in vrf default), 1w5d
        B    10.113.66.0/24 [200/0] via 172.23.36.198 (nexthop in vrf default), 1w5d
        B    10.113.67.0/27 [200/0] via 172.23.36.198 (nexthop in vrf default), 1w5d
        B    10.113.67.64/27 [200/0] via 172.23.36.198 (nexthop in vrf default), 1w5d
        B    10.113.67.128/27 [200/0] via 172.23.36.198 (nexthop in vrf default), 1w5d
        B    10.113.72.0/23 [200/0] via 172.23.36.198 (nexthop in vrf default), 1w5d
        B    10.113.74.0/23 [200/0] via 172.23.36.198 (nexthop in vrf default), 1w5d
        B    10.113.84.0/23 [200/0] via 172.23.36.198 (nexthop in vrf default), 1w5d
        B    10.113.86.0/23 [200/0] via 172.23.36.198 (nexthop in vrf default), 1w5d
        B    10.113.88.0/23 [200/0] via 172.23.36.198 (nexthop in vrf default), 1w5d
        B    10.113.118.0/24 [200/0] via 172.23.36.198 (nexthop in vrf default), 1w5d
        B    10.113.120.0/24 [200/0] via 172.23.36.198 (nexthop in vrf default), 1w5d
        B    10.113.121.0/24 [200/0] via 172.23.36.198 (nexthop in vrf default), 1w5d
        B    10.113.122.0/24 [200/0] via 172.23.36.198 (nexthop in vrf default), 1w5d
        B    10.113.123.0/24 [200/0] via 172.23.36.198 (nexthop in vrf default), 1w5d
        B    10.113.126.0/27 [200/0] via 172.23.36.198 (nexthop in vrf default), 1w5d
        B    10.113.126.32/27 [200/0] via 172.23.36.198 (nexthop in vrf default), 1w5d
        B    10.113.126.64/27 [200/0] via 172.23.36.198 (nexthop in vrf default), 1w5d
        B    10.113.126.96/27 [200/0] via 172.23.36.198 (nexthop in vrf default), 1w5d
        B    10.113.128.0/23 [200/0] via 172.23.40.199 (nexthop in vrf default), 5w1d
        B    10.113.130.0/24 [200/0] via 172.23.40.199 (nexthop in vrf default), 5w1d
        B    10.113.131.0/27 [200/0] via 172.23.40.199 (nexthop in vrf default), 5w1d
        B    10.113.131.64/27 [200/0] via 172.23.40.199 (nexthop in vrf default), 5w1d
        B    10.113.131.128/27 [200/0] via 172.23.40.199 (nexthop in vrf default), 5w1d
        B    10.113.136.0/23 [200/0] via 172.23.40.199 (nexthop in vrf default), 5w1d
        B    10.113.138.0/23 [200/0] via 172.23.40.199 (nexthop in vrf default), 5w1d
        B    10.113.148.0/23 [200/0] via 172.23.40.199 (nexthop in vrf default), 5w1d
        B    10.113.182.0/24 [200/0] via 172.23.40.199 (nexthop in vrf default), 5w1d
        B    10.113.184.0/24 [200/0] via 172.23.40.199 (nexthop in vrf default), 5w1d
        B    10.113.185.0/24 [200/0] via 172.23.40.199 (nexthop in vrf default), 5w1d
        B    10.113.190.0/27 [200/0] via 172.23.40.199 (nexthop in vrf default), 5w1d
        B    10.113.190.32/27 [200/0] via 172.23.40.199 (nexthop in vrf default), 5w1d
        B    10.113.190.64/27 [200/0] via 172.23.40.199 (nexthop in vrf default), 5w1d
        B    10.113.190.96/27 [200/0] via 172.23.40.199 (nexthop in vrf default), 5w1d
        S    10.170.0.0/16 [1/0] via 10.100.11.20, 36w5d
        B    10.170.19.0/24 [200/0] via 172.23.6.198 (nexthop in vrf default), 5d13h
        B    10.170.22.0/24 [200/0] via 172.23.6.198 (nexthop in vrf default), 5d13h
        S    10.170.47.0/24 [1/0] via 10.100.11.20, 36w5d
        B    10.170.60.0/22 [200/0] via 172.23.6.198 (nexthop in vrf default), 5d13h
        B    10.170.136.0/23 [200/0] via 172.23.6.198 (nexthop in vrf default), 5d13h
        B    10.170.136.2/32 [200/0] via 172.23.6.198 (nexthop in vrf default), 5d13h
        B    10.170.136.3/32 [200/0] via 172.23.6.198 (nexthop in vrf default), 5d13h
        B    10.170.138.0/24 [200/0] via 172.23.6.198 (nexthop in vrf default), 5d13h
        B    10.170.138.2/32 [200/0] via 172.23.6.198 (nexthop in vrf default), 5d13h
        B    10.170.138.3/32 [200/0] via 172.23.6.198 (nexthop in vrf default), 5d13h
        B    10.170.139.0/24 [200/0] via 172.23.6.198 (nexthop in vrf default), 5d13h
        B    10.170.139.2/32 [200/0] via 172.23.6.198 (nexthop in vrf default), 5d13h
        B    10.170.139.3/32 [200/0] via 172.23.6.198 (nexthop in vrf default), 5d13h
        B    10.170.140.0/22 [200/0] via 172.23.6.198 (nexthop in vrf default), 5d13h
        B    10.170.140.2/32 [200/0] via 172.23.6.198 (nexthop in vrf default), 5d13h
        B    10.170.140.3/32 [200/0] via 172.23.6.198 (nexthop in vrf default), 5d13h
        B    10.170.142.2/32 [200/0] via 172.23.6.198 (nexthop in vrf default), 5d13h
        B    10.170.142.3/32 [200/0] via 172.23.6.198 (nexthop in vrf default), 5d13h
        B    10.170.143.2/32 [200/0] via 172.23.6.198 (nexthop in vrf default), 5d13h
        B    10.170.143.3/32 [200/0] via 172.23.6.198 (nexthop in vrf default), 5d13h
        B    10.170.150.0/24 [200/0] via 172.23.6.198 (nexthop in vrf default), 5d13h
        B    10.170.188.0/22 [200/0] via 172.23.8.199 (nexthop in vrf default), 5d14h
        B    10.172.44.0/24 [200/0] via 172.23.36.198 (nexthop in vrf default), 1w5d
        B    10.172.64.48/28 [200/0] via 172.23.36.198 (nexthop in vrf default), 1w5d
        B    10.172.64.114/31 [200/0] via 172.23.36.198 (nexthop in vrf default), 1w5d
        B    10.172.64.116/31 [200/0] via 172.23.36.198 (nexthop in vrf default), 1w5d
        B    10.172.64.120/30 [200/0] via 172.23.36.198 (nexthop in vrf default), 1w5d
        B    10.172.96.48/28 [200/0] via 172.23.36.198 (nexthop in vrf default), 1w5d
        B    10.172.97.0/24 [200/0] via 172.23.36.198 (nexthop in vrf default), 1w5d
        B    10.172.100.0/23 [200/0] via 172.23.36.198 (nexthop in vrf default), 1w5d
        B    10.172.102.0/23 [200/0] via 172.23.36.198 (nexthop in vrf default), 1w5d
        B    10.172.108.0/24 [200/0] via 172.23.36.198 (nexthop in vrf default), 1w5d
        B    10.172.110.0/27 [200/0] via 172.23.36.198 (nexthop in vrf default), 1w5d
        B    10.172.110.128/27 [200/0] via 172.23.36.198 (nexthop in vrf default), 1w5d
        B    10.172.112.0/22 [200/0] via 172.23.36.198 (nexthop in vrf default), 1w5d
        B    10.172.116.0/22 [200/0] via 172.23.36.198 (nexthop in vrf default), 1w5d
        B    10.172.128.48/28 [200/0] via 172.23.40.199 (nexthop in vrf default), 5w1d
        B    10.172.128.114/31 [200/0] via 172.23.40.199 (nexthop in vrf default), 5w1d
        B    10.172.128.116/31 [200/0] via 172.23.40.199 (nexthop in vrf default), 5w1d
        B    10.172.128.120/30 [200/0] via 172.23.40.199 (nexthop in vrf default), 5w1d
        B    10.172.131.0/24 [200/0] via 172.23.40.199 (nexthop in vrf default), 5w1d
        B    10.172.132.0/23 [200/0] via 172.23.40.199 (nexthop in vrf default), 5w1d
        B    10.172.160.0/20 [200/0] via 172.23.40.199 (nexthop in vrf default), 5w1d
        B    10.172.161.0/24 [200/0] via 172.23.40.199 (nexthop in vrf default), 5w1d
        B    10.172.166.0/23 [200/0] via 172.23.40.199 (nexthop in vrf default), 5w1d
        B    10.172.172.0/24 [200/0] via 172.23.40.199 (nexthop in vrf default), 5w1d
        B    10.172.174.0/27 [200/0] via 172.23.40.199 (nexthop in vrf default), 5w1d
        B    10.172.174.128/27 [200/0] via 172.23.40.199 (nexthop in vrf default), 5w1d
        B    10.172.180.0/22 [200/0] via 172.23.40.199 (nexthop in vrf default), 5w1d
        B    10.172.224.0/31 [200/0] via 172.23.36.198 (nexthop in vrf default), 1w5d
        B    10.172.224.2/31 [200/0] via 172.23.36.198 (nexthop in vrf default), 1w5d
        B    10.172.224.34/31 [200/0] via 172.23.36.198 (nexthop in vrf default), 1w5d
        B    10.172.224.36/31 [200/0] via 172.23.36.198 (nexthop in vrf default), 1w5d
        B    10.172.224.148/31 [200/0] via 172.23.36.198 (nexthop in vrf default), 1w5d
        B    10.172.224.150/31 [200/0] via 172.23.36.198 (nexthop in vrf default), 1w5d
        B    10.172.228.0/23 [200/0] via 172.23.36.198 (nexthop in vrf default), 1w5d
        B    10.172.230.0/24 [200/0] via 172.23.36.198 (nexthop in vrf default), 1w5d
        B    10.172.231.0/25 [200/0] via 172.23.36.198 (nexthop in vrf default), 1w5d
        B    10.172.231.128/27 [200/0] via 172.23.36.198 (nexthop in vrf default), 1w5d
        B    10.172.231.240/28 [200/0] via 172.23.36.198 (nexthop in vrf default), 1w5d
        B    10.172.236.0/23 [200/0] via 172.23.36.198 (nexthop in vrf default), 1w5d
        B    10.172.238.0/27 [200/0] via 172.23.36.198 (nexthop in vrf default), 1w5d
        B    10.172.238.64/26 [200/0] via 172.23.36.198 (nexthop in vrf default), 1w5d
        B    10.172.238.128/27 [200/0] via 172.23.36.198 (nexthop in vrf default), 1w5d
        B    10.172.239.128/28 [200/0] via 172.23.36.198 (nexthop in vrf default), 1w5d
        B    10.172.240.0/31 [200/0] via 172.23.36.198 (nexthop in vrf default), 1w5d
        B    10.172.240.2/31 [200/0] via 172.23.36.198 (nexthop in vrf default), 1w5d
        B    10.172.240.14/31 [200/0] via 172.23.36.198 (nexthop in vrf default), 1w5d
        B    10.172.240.64/27 [200/0] via 172.23.36.198 (nexthop in vrf default), 1w5d
        B    10.172.240.96/28 [200/0] via 172.23.36.198 (nexthop in vrf default), 1w5d
        B    10.172.240.128/26 [200/0] via 172.23.36.198 (nexthop in vrf default), 1w5d
        S    172.16.0.0/16 [1/0] via 10.100.11.20, 36w5d
        B    172.16.2.208/28 [200/0] via 172.23.6.198 (nexthop in vrf default), 5d13h
        B    172.16.3.0/24 [200/0] via 172.23.6.198 (nexthop in vrf default), 5d13h
        B    172.16.4.0/23 [200/0] via 172.23.6.198 (nexthop in vrf default), 5d13h
        B    172.16.7.0/24 [200/0] via 172.23.6.198 (nexthop in vrf default), 5d13h
        B    172.16.8.0/24 [200/0] via 172.23.6.198 (nexthop in vrf default), 5d13h
        B    172.16.10.0/23 [200/0] via 172.23.6.198 (nexthop in vrf default), 5d13h
        B    172.16.23.0/24 [200/0] via 172.23.6.198 (nexthop in vrf default), 5d13h
        B    172.16.24.0/24 [200/0] via 172.23.6.198 (nexthop in vrf default), 5d13h
        B    172.16.24.48/28 [200/0] via 172.23.6.198 (nexthop in vrf default), 5d13h
        B    172.16.25.0/24 [200/0] via 172.23.6.198 (nexthop in vrf default), 5d13h
        B    172.16.26.0/24 [200/0] via 172.23.6.198 (nexthop in vrf default), 5d13h
        B    172.16.27.0/24 [200/0] via 172.23.6.198 (nexthop in vrf default), 5d13h
        B    172.16.29.0/24 [200/0] via 172.23.6.198 (nexthop in vrf default), 5d13h
        S    172.16.47.0/24 [1/0] via 10.100.11.20, 36w5d
        B    172.16.50.0/24 [200/0] via 172.23.6.198 (nexthop in vrf default), 5d13h
        B    172.16.51.0/24 [200/0] via 172.23.6.198 (nexthop in vrf default), 5d13h
        B    172.16.52.0/24 [200/0] via 172.23.6.198 (nexthop in vrf default), 5d13h
        B    172.16.53.0/25 [200/0] via 172.23.6.198 (nexthop in vrf default), 5d13h
        B    172.16.60.0/22 [200/0] via 172.23.8.199 (nexthop in vrf default), 5d14h
        B    172.16.67.0/24 [200/0] via 172.23.8.199 (nexthop in vrf default), 5d14h
        B    172.16.68.0/23 [200/0] via 172.23.8.199 (nexthop in vrf default), 5d14h
        B    172.16.71.0/24 [200/0] via 172.23.8.199 (nexthop in vrf default), 5d14h
        B    172.16.72.0/24 [200/0] via 172.23.8.199 (nexthop in vrf default), 5d14h
        B    172.16.87.0/24 [200/0] via 172.23.8.199 (nexthop in vrf default), 5d14h
        B    172.16.88.0/24 [200/0] via 172.23.8.199 (nexthop in vrf default), 5d14h
        B    172.16.90.0/24 [200/0] via 172.23.8.199 (nexthop in vrf default), 5d14h
        B    172.16.92.0/24 [200/0] via 172.23.8.199 (nexthop in vrf default), 5d14h
        B    172.16.188.0/22 [200/0] via 172.23.6.198 (nexthop in vrf default), 5d13h
        B    172.16.224.0/24 [200/0] via 172.23.8.199 (nexthop in vrf default), 5d14h
        B    172.16.225.0/24 [200/0] via 172.23.8.199 (nexthop in vrf default), 5d14h
        B    172.16.226.0/24 [200/0] via 172.23.8.199 (nexthop in vrf default), 5d14h
        B    172.16.232.0/24 [200/0] via 172.23.6.198 (nexthop in vrf default), 5d13h
        B    172.16.233.0/24 [200/0] via 172.23.6.198 (nexthop in vrf default), 5d13h
        B    172.16.234.0/24 [200/0] via 172.23.6.198 (nexthop in vrf default), 5d13h
        B    172.16.240.0/24 [20/0] via 10.100.11.1, 5d13h
        B    172.16.241.0/24 [20/0] via 10.100.11.1, 5d13h
        B    172.16.242.0/24 [20/0] via 10.100.11.1, 5d13h
        B    172.16.247.0/24 [20/0] via 10.100.11.1, 5d13h
        B    172.16.250.16/28 [20/0] via 10.100.11.1, 5d13h
        B    172.16.250.128/28 [20/0] via 10.100.11.1, 5d13h
        B    172.16.250.244/30 [20/0] via 10.100.11.1, 5d13h
        B    172.16.250.248/29 [20/0] via 10.100.11.1, 5d13h
        B    172.18.3.0/24 [200/0] via 172.23.36.198 (nexthop in vrf default), 1w5d
        B    172.18.4.0/23 [200/0] via 172.23.36.198 (nexthop in vrf default), 1w5d
        B    172.18.6.0/23 [200/0] via 172.23.36.198 (nexthop in vrf default), 1w5d
        B    172.18.8.0/23 [200/0] via 172.23.36.198 (nexthop in vrf default), 1w5d
        B    172.18.10.0/23 [200/0] via 172.23.36.198 (nexthop in vrf default), 1w5d
        B    172.18.23.0/27 [200/0] via 172.23.36.198 (nexthop in vrf default), 1w5d
        B    172.18.33.0/24 [200/0] via 172.23.36.198 (nexthop in vrf default), 1w5d
        B    172.18.41.0/24 [200/0] via 172.23.40.199 (nexthop in vrf default), 5w1d
        B    172.18.48.48/28 [200/0] via 172.23.36.198 (nexthop in vrf default), 1w5d
        B    172.18.48.64/28 [200/0] via 172.23.36.198 (nexthop in vrf default), 1w5d
        B    172.18.48.120/30 [200/0] via 172.23.36.198 (nexthop in vrf default), 1w5d
        B    172.18.50.0/24 [200/0] via 172.23.36.198 (nexthop in vrf default), 1w5d
        B    172.18.105.0/24 [200/0] via 172.23.36.198 (nexthop in vrf default), 1w5d
        B    172.18.109.0/24 [200/0] via 172.23.36.198 (nexthop in vrf default), 1w5d
        B    172.18.160.0/20 [200/0] via 172.23.40.199 (nexthop in vrf default), 5w1d
        B    172.18.160.48/28 [200/0] via 172.23.40.199 (nexthop in vrf default), 5w1d
        B    172.18.161.0/24 [200/0] via 172.23.40.199 (nexthop in vrf default), 5w1d
        B    172.18.169.0/24 [200/0] via 172.23.40.199 (nexthop in vrf default), 5w1d
        B    172.18.169.224/28 [200/0] via 172.23.40.199 (nexthop in vrf default), 5w1d
        B    172.18.173.0/24 [200/0] via 172.23.40.199 (nexthop in vrf default), 5w1d
        B    172.18.224.0/24 [200/0] via 172.23.36.198 (nexthop in vrf default), 1w5d
        B    172.18.225.0/24 [200/0] via 172.23.36.198 (nexthop in vrf default), 1w5d
        B    172.18.226.0/24 [200/0] via 172.23.36.198 (nexthop in vrf default), 1w5d
        B    172.18.227.0/24 [200/0] via 172.23.36.198 (nexthop in vrf default), 1w5d
        B    172.18.232.0/24 [200/0] via 172.23.40.199 (nexthop in vrf default), 5w1d
        B    172.18.233.0/24 [200/0] via 172.23.40.199 (nexthop in vrf default), 5w1d
        B    172.18.234.0/24 [200/0] via 172.23.40.199 (nexthop in vrf default), 5w1d
        B    172.18.235.0/24 [200/0] via 172.23.40.199 (nexthop in vrf default), 5w1d
        B    172.18.252.0/30 [200/0] via 172.23.36.198 (nexthop in vrf default), 1w5d
        B    172.18.252.4/30 [200/0] via 172.23.36.198 (nexthop in vrf default), 1w5d
        B    172.18.252.16/28 [200/0] via 172.23.36.198 (nexthop in vrf default), 1w5d
        B    172.18.252.32/29 [200/0] via 172.23.36.198 (nexthop in vrf default), 1w5d
        B    172.18.252.48/28 [200/0] via 172.23.36.198 (nexthop in vrf default), 1w5d
        B    172.18.252.64/28 [200/0] via 172.23.36.198 (nexthop in vrf default), 1w5d
        B    172.18.252.80/28 [200/0] via 172.23.36.198 (nexthop in vrf default), 1w5d
        B    172.18.252.252/30 [200/0] via 172.23.36.198 (nexthop in vrf default), 1w5d
        B    172.18.253.0/30 [200/0] via 172.23.40.199 (nexthop in vrf default), 5w1d
        B    172.18.253.4/30 [200/0] via 172.23.40.199 (nexthop in vrf default), 5w1d
        B    172.18.253.16/28 [200/0] via 172.23.40.199 (nexthop in vrf default), 5w1d
        B    172.18.253.32/29 [200/0] via 172.23.40.199 (nexthop in vrf default), 5w1d
        B    172.18.253.48/28 [200/0] via 172.23.40.199 (nexthop in vrf default), 5w1d
        B    172.18.253.252/30 [200/0] via 172.23.40.199 (nexthop in vrf default), 5w1d
        B    172.22.36.128/27 [200/0] via 172.23.36.198 (nexthop in vrf default), 1w5d
        B    172.22.36.145/32 [200/0] via 172.23.36.198 (nexthop in vrf default), 1w5d
        B    172.22.36.146/32 [200/0] via 172.23.36.198 (nexthop in vrf default), 1w5d
        B    172.22.36.210/32 [200/0] via 172.23.36.198 (nexthop in vrf default), 1w5d
        B    172.22.36.211/32 [200/0] via 172.23.36.198 (nexthop in vrf default), 1w5d
        B    172.22.40.128/27 [200/0] via 172.23.40.199 (nexthop in vrf default), 5w1d
        B    172.22.40.145/32 [200/0] via 172.23.40.199 (nexthop in vrf default), 5w1d
        B    172.22.40.146/32 [200/0] via 172.23.40.199 (nexthop in vrf default), 5w1d
        B    172.22.40.210/32 [200/0] via 172.23.40.199 (nexthop in vrf default), 5w1d
        B    172.22.40.211/32 [200/0] via 172.23.40.199 (nexthop in vrf default), 5w1d
        B    172.22.46.0/25 [200/0] via 172.23.36.198 (nexthop in vrf default), 1w5d
        B    172.22.46.128/27 [200/0] via 172.23.36.198 (nexthop in vrf default), 1w5d
        B    172.22.46.191/32 [200/0] via 172.23.36.198 (nexthop in vrf default), 1w5d
        B    172.22.46.210/32 [200/0] via 172.23.36.198 (nexthop in vrf default), 1w5d
        B    172.22.46.211/32 [200/0] via 172.23.36.198 (nexthop in vrf default), 1w5d
        B    172.22.47.0/32 [200/0] via 172.23.36.198 (nexthop in vrf default), 1w5d
        B    172.22.47.1/32 [200/0] via 172.23.36.198 (nexthop in vrf default), 1w5d
        RP/0/RSP0/CPU0:USPW-CORE-PE-01#
    '''}

    golden_parsed_output_3_with_vrf = {
        "vrf": {
            "gsn2": {
                "address_family": {
                    "ipv4": {
                        "routes": {
                            "0.0.0.0/0": {
                                "route": "0.0.0.0/0",
                                "active": True,
                                "metric": 0,
                                "route_preference": 200,
                                "source_protocol_codes": "B*",
                                "source_protocol": "bgp",
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "172.23.6.198",
                                            "updated": "08:11:19",
                                        }
                                    }
                                },
                            },
                            "10.93.64.0/18": {
                                "route": "10.93.64.0/18",
                                "active": True,
                                "metric": 0,
                                "route_preference": 200,
                                "source_protocol_codes": "B",
                                "source_protocol": "bgp",
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "172.23.36.198",
                                            "updated": "1w5d",
                                        }
                                    }
                                },
                            },
                            "10.93.128.0/18": {
                                "route": "10.93.128.0/18",
                                "active": True,
                                "metric": 0,
                                "route_preference": 200,
                                "source_protocol_codes": "B",
                                "source_protocol": "bgp",
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "172.23.40.199",
                                            "updated": "5w1d",
                                        }
                                    }
                                },
                            },
                            "10.100.0.0/27": {
                                "route": "10.100.0.0/27",
                                "active": True,
                                "metric": 0,
                                "route_preference": 200,
                                "source_protocol_codes": "B",
                                "source_protocol": "bgp",
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "172.23.6.198",
                                            "updated": "5d13h",
                                        }
                                    }
                                },
                            },
                            "10.100.1.0/27": {
                                "route": "10.100.1.0/27",
                                "active": True,
                                "metric": 0,
                                "route_preference": 200,
                                "source_protocol_codes": "B",
                                "source_protocol": "bgp",
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "172.23.6.198",
                                            "updated": "5d13h",
                                        }
                                    }
                                },
                            },
                            "10.100.3.0/31": {
                                "route": "10.100.3.0/31",
                                "active": True,
                                "metric": 0,
                                "route_preference": 200,
                                "source_protocol_codes": "B",
                                "source_protocol": "bgp",
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "172.23.6.198",
                                            "updated": "27w5d",
                                        }
                                    }
                                },
                            },
                            "10.100.3.2/31": {
                                "route": "10.100.3.2/31",
                                "active": True,
                                "metric": 0,
                                "route_preference": 200,
                                "source_protocol_codes": "B",
                                "source_protocol": "bgp",
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "172.23.6.199",
                                            "updated": "27w5d",
                                        }
                                    }
                                },
                            },
                            "10.100.3.32/29": {
                                "route": "10.100.3.32/29",
                                "active": True,
                                "metric": 0,
                                "route_preference": 200,
                                "source_protocol_codes": "B",
                                "source_protocol": "bgp",
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "172.23.6.198",
                                            "updated": "5d13h",
                                        }
                                    }
                                },
                            },
                            "10.100.3.96/31": {
                                "route": "10.100.3.96/31",
                                "active": True,
                                "metric": 0,
                                "route_preference": 200,
                                "source_protocol_codes": "B",
                                "source_protocol": "bgp",
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "172.23.6.198",
                                            "updated": "5d13h",
                                        }
                                    }
                                },
                            },
                            "10.100.3.98/31": {
                                "route": "10.100.3.98/31",
                                "active": True,
                                "metric": 0,
                                "route_preference": 200,
                                "source_protocol_codes": "B",
                                "source_protocol": "bgp",
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "172.23.6.198",
                                            "updated": "5d13h",
                                        }
                                    }
                                },
                            },
                            "10.100.3.104/31": {
                                "route": "10.100.3.104/31",
                                "active": True,
                                "metric": 0,
                                "route_preference": 200,
                                "source_protocol_codes": "B",
                                "source_protocol": "bgp",
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "172.23.6.198",
                                            "updated": "5d13h",
                                        }
                                    }
                                },
                            },
                            "10.100.3.136/31": {
                                "route": "10.100.3.136/31",
                                "active": True,
                                "metric": 0,
                                "route_preference": 200,
                                "source_protocol_codes": "B",
                                "source_protocol": "bgp",
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "172.23.6.198",
                                            "updated": "5d13h",
                                        }
                                    }
                                },
                            },
                            "10.100.3.138/31": {
                                "route": "10.100.3.138/31",
                                "active": True,
                                "metric": 0,
                                "route_preference": 200,
                                "source_protocol_codes": "B",
                                "source_protocol": "bgp",
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "172.23.6.198",
                                            "updated": "5d13h",
                                        }
                                    }
                                },
                            },
                            "10.100.3.144/31": {
                                "route": "10.100.3.144/31",
                                "active": True,
                                "metric": 0,
                                "route_preference": 200,
                                "source_protocol_codes": "B",
                                "source_protocol": "bgp",
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "172.23.6.198",
                                            "updated": "5d13h",
                                        }
                                    }
                                },
                            },
                            "10.100.3.146/31": {
                                "route": "10.100.3.146/31",
                                "active": True,
                                "metric": 0,
                                "route_preference": 200,
                                "source_protocol_codes": "B",
                                "source_protocol": "bgp",
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "172.23.6.198",
                                            "updated": "5d13h",
                                        }
                                    }
                                },
                            },
                            "10.100.3.160/31": {
                                "route": "10.100.3.160/31",
                                "active": True,
                                "metric": 0,
                                "route_preference": 200,
                                "source_protocol_codes": "B",
                                "source_protocol": "bgp",
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "172.23.6.198",
                                            "updated": "5d13h",
                                        }
                                    }
                                },
                            },
                            "10.100.3.162/31": {
                                "route": "10.100.3.162/31",
                                "active": True,
                                "metric": 0,
                                "route_preference": 200,
                                "source_protocol_codes": "B",
                                "source_protocol": "bgp",
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "172.23.6.198",
                                            "updated": "5d13h",
                                        }
                                    }
                                },
                            },
                            "10.100.3.168/31": {
                                "route": "10.100.3.168/31",
                                "active": True,
                                "metric": 0,
                                "route_preference": 200,
                                "source_protocol_codes": "B",
                                "source_protocol": "bgp",
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "172.23.6.198",
                                            "updated": "5d13h",
                                        }
                                    }
                                },
                            },
                            "10.100.3.170/31": {
                                "route": "10.100.3.170/31",
                                "active": True,
                                "metric": 0,
                                "route_preference": 200,
                                "source_protocol_codes": "B",
                                "source_protocol": "bgp",
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "172.23.6.198",
                                            "updated": "5d13h",
                                        }
                                    }
                                },
                            },
                            "10.100.4.0/27": {
                                "route": "10.100.4.0/27",
                                "active": True,
                                "metric": 0,
                                "route_preference": 200,
                                "source_protocol_codes": "B",
                                "source_protocol": "bgp",
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "172.23.8.199",
                                            "updated": "5d14h",
                                        }
                                    }
                                },
                            },
                            "10.100.7.0/31": {
                                "route": "10.100.7.0/31",
                                "active": True,
                                "metric": 0,
                                "route_preference": 200,
                                "source_protocol_codes": "B",
                                "source_protocol": "bgp",
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "172.23.8.198",
                                            "updated": "8w0d",
                                        }
                                    }
                                },
                            },
                            "10.100.7.2/31": {
                                "route": "10.100.7.2/31",
                                "active": True,
                                "metric": 0,
                                "route_preference": 200,
                                "source_protocol_codes": "B",
                                "source_protocol": "bgp",
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "172.23.8.199",
                                            "updated": "13w5d",
                                        }
                                    }
                                },
                            },
                            "10.100.7.32/29": {
                                "route": "10.100.7.32/29",
                                "active": True,
                                "metric": 0,
                                "route_preference": 200,
                                "source_protocol_codes": "B",
                                "source_protocol": "bgp",
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "172.23.8.199",
                                            "updated": "5d14h",
                                        }
                                    }
                                },
                            },
                            "10.100.7.96/31": {
                                "route": "10.100.7.96/31",
                                "active": True,
                                "metric": 0,
                                "route_preference": 200,
                                "source_protocol_codes": "B",
                                "source_protocol": "bgp",
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "172.23.8.199",
                                            "updated": "5d14h",
                                        }
                                    }
                                },
                            },
                            "10.100.7.98/31": {
                                "route": "10.100.7.98/31",
                                "active": True,
                                "metric": 0,
                                "route_preference": 200,
                                "source_protocol_codes": "B",
                                "source_protocol": "bgp",
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "172.23.8.199",
                                            "updated": "5d14h",
                                        }
                                    }
                                },
                            },
                            "10.100.7.104/31": {
                                "route": "10.100.7.104/31",
                                "active": True,
                                "metric": 0,
                                "route_preference": 200,
                                "source_protocol_codes": "B",
                                "source_protocol": "bgp",
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "172.23.8.199",
                                            "updated": "5d14h",
                                        }
                                    }
                                },
                            },
                            "10.100.7.136/31": {
                                "route": "10.100.7.136/31",
                                "active": True,
                                "metric": 0,
                                "route_preference": 200,
                                "source_protocol_codes": "B",
                                "source_protocol": "bgp",
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "172.23.8.199",
                                            "updated": "5d14h",
                                        }
                                    }
                                },
                            },
                            "10.100.7.138/31": {
                                "route": "10.100.7.138/31",
                                "active": True,
                                "metric": 0,
                                "route_preference": 200,
                                "source_protocol_codes": "B",
                                "source_protocol": "bgp",
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "172.23.8.199",
                                            "updated": "5d14h",
                                        }
                                    }
                                },
                            },
                            "10.100.7.160/31": {
                                "route": "10.100.7.160/31",
                                "active": True,
                                "metric": 0,
                                "route_preference": 200,
                                "source_protocol_codes": "B",
                                "source_protocol": "bgp",
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "172.23.8.199",
                                            "updated": "5d14h",
                                        }
                                    }
                                },
                            },
                            "10.100.7.162/31": {
                                "route": "10.100.7.162/31",
                                "active": True,
                                "metric": 0,
                                "route_preference": 200,
                                "source_protocol_codes": "B",
                                "source_protocol": "bgp",
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "172.23.8.199",
                                            "updated": "5d14h",
                                        }
                                    }
                                },
                            },
                            "10.100.8.0/27": {
                                "route": "10.100.8.0/27",
                                "active": True,
                                "metric": 0,
                                "route_preference": 20,
                                "source_protocol_codes": "B",
                                "source_protocol": "bgp",
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "10.100.11.1",
                                            "updated": "5d13h",
                                        }
                                    }
                                },
                            },
                            "10.100.9.0/27": {
                                "route": "10.100.9.0/27",
                                "active": True,
                                "metric": 0,
                                "route_preference": 20,
                                "source_protocol_codes": "B",
                                "source_protocol": "bgp",
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "10.100.11.1",
                                            "updated": "5d13h",
                                        }
                                    }
                                },
                            },
                            "10.100.11.0/31": {
                                "route": "10.100.11.0/31",
                                "active": True,
                                "source_protocol_codes": "C",
                                "source_protocol": "connected",
                                "next_hop": {
                                    "outgoing_interface": {
                                        "GigabitEthernet0/0/1/8": {
                                            "outgoing_interface": "GigabitEthernet0/0/1/8",
                                            "updated": "36w5d",
                                        }
                                    }
                                },
                            },
                            "10.100.11.0/32": {
                                "route": "10.100.11.0/32",
                                "active": True,
                                "source_protocol_codes": "L",
                                "source_protocol": "local",
                                "next_hop": {
                                    "outgoing_interface": {
                                        "GigabitEthernet0/0/1/8": {
                                            "outgoing_interface": "GigabitEthernet0/0/1/8",
                                            "updated": "36w5d",
                                        }
                                    }
                                },
                            },
                            "10.100.11.2/31": {
                                "route": "10.100.11.2/31",
                                "active": True,
                                "metric": 0,
                                "route_preference": 20,
                                "source_protocol_codes": "B",
                                "source_protocol": "bgp",
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "10.100.11.1",
                                            "updated": "27w5d",
                                        }
                                    }
                                },
                            },
                            "10.100.11.16/29": {
                                "route": "10.100.11.16/29",
                                "active": True,
                                "source_protocol_codes": "C",
                                "source_protocol": "connected",
                                "next_hop": {
                                    "outgoing_interface": {
                                        "BVI3001": {
                                            "outgoing_interface": "BVI3001",
                                            "updated": "36w5d",
                                        }
                                    }
                                },
                            },
                            "10.100.11.17/32": {
                                "route": "10.100.11.17/32",
                                "active": True,
                                "metric": 0,
                                "source_protocol_codes": "L",
                                "source_protocol": "local",
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "10.100.11.17",
                                            "updated": "36w5d",
                                            "outgoing_interface": "BVI3001",
                                        }
                                    }
                                },
                            },
                            "10.100.11.18/32": {
                                "route": "10.100.11.18/32",
                                "active": True,
                                "source_protocol_codes": "L",
                                "source_protocol": "local",
                                "next_hop": {
                                    "outgoing_interface": {
                                        "BVI3001": {
                                            "outgoing_interface": "BVI3001",
                                            "updated": "36w5d",
                                        }
                                    }
                                },
                            },
                            "10.100.11.96/31": {
                                "route": "10.100.11.96/31",
                                "active": True,
                                "metric": 0,
                                "route_preference": 20,
                                "source_protocol_codes": "B",
                                "source_protocol": "bgp",
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "10.100.11.1",
                                            "updated": "5d13h",
                                        }
                                    }
                                },
                            },
                            "10.100.11.98/31": {
                                "route": "10.100.11.98/31",
                                "active": True,
                                "metric": 0,
                                "route_preference": 20,
                                "source_protocol_codes": "B",
                                "source_protocol": "bgp",
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "10.100.11.1",
                                            "updated": "5d13h",
                                        }
                                    }
                                },
                            },
                            "10.100.11.104/31": {
                                "route": "10.100.11.104/31",
                                "active": True,
                                "metric": 0,
                                "route_preference": 20,
                                "source_protocol_codes": "B",
                                "source_protocol": "bgp",
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "10.100.11.1",
                                            "updated": "5d13h",
                                        }
                                    }
                                },
                            },
                            "10.100.32.0/27": {
                                "route": "10.100.32.0/27",
                                "active": True,
                                "metric": 0,
                                "route_preference": 200,
                                "source_protocol_codes": "B",
                                "source_protocol": "bgp",
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "172.23.36.198",
                                            "updated": "1w5d",
                                        }
                                    }
                                },
                            },
                            "10.100.33.0/27": {
                                "route": "10.100.33.0/27",
                                "active": True,
                                "metric": 0,
                                "route_preference": 200,
                                "source_protocol_codes": "B",
                                "source_protocol": "bgp",
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "172.23.36.198",
                                            "updated": "1w5d",
                                        }
                                    }
                                },
                            },
                            "10.100.33.32/28": {
                                "route": "10.100.33.32/28",
                                "active": True,
                                "metric": 0,
                                "route_preference": 200,
                                "source_protocol_codes": "B",
                                "source_protocol": "bgp",
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "172.23.36.198",
                                            "updated": "1w5d",
                                        }
                                    }
                                },
                            },
                            "10.100.33.48/28": {
                                "route": "10.100.33.48/28",
                                "active": True,
                                "metric": 0,
                                "route_preference": 200,
                                "source_protocol_codes": "B",
                                "source_protocol": "bgp",
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "172.23.36.198",
                                            "updated": "1w5d",
                                        }
                                    }
                                },
                            },
                            "10.100.35.0/31": {
                                "route": "10.100.35.0/31",
                                "active": True,
                                "metric": 0,
                                "route_preference": 200,
                                "source_protocol_codes": "B",
                                "source_protocol": "bgp",
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "172.23.36.198",
                                            "updated": "7w0d",
                                        }
                                    }
                                },
                            },
                            "10.100.35.2/31": {
                                "route": "10.100.35.2/31",
                                "active": True,
                                "metric": 0,
                                "route_preference": 200,
                                "source_protocol_codes": "B",
                                "source_protocol": "bgp",
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "172.23.36.199",
                                            "updated": "14w5d",
                                        }
                                    }
                                },
                            },
                            "10.100.35.16/29": {
                                "route": "10.100.35.16/29",
                                "active": True,
                                "metric": 0,
                                "route_preference": 200,
                                "source_protocol_codes": "B",
                                "source_protocol": "bgp",
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "172.23.36.198",
                                            "updated": "1w5d",
                                        }
                                    }
                                },
                            },
                            "10.100.35.32/29": {
                                "route": "10.100.35.32/29",
                                "active": True,
                                "metric": 0,
                                "route_preference": 200,
                                "source_protocol_codes": "B",
                                "source_protocol": "bgp",
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "172.23.36.198",
                                            "updated": "1w5d",
                                        }
                                    }
                                },
                            },
                            "10.100.35.96/31": {
                                "route": "10.100.35.96/31",
                                "active": True,
                                "metric": 0,
                                "route_preference": 200,
                                "source_protocol_codes": "B",
                                "source_protocol": "bgp",
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "172.23.36.198",
                                            "updated": "1w5d",
                                        }
                                    }
                                },
                            },
                            "10.100.35.98/31": {
                                "route": "10.100.35.98/31",
                                "active": True,
                                "metric": 0,
                                "route_preference": 200,
                                "source_protocol_codes": "B",
                                "source_protocol": "bgp",
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "172.23.36.198",
                                            "updated": "1w5d",
                                        }
                                    }
                                },
                            },
                            "10.100.35.104/31": {
                                "route": "10.100.35.104/31",
                                "active": True,
                                "metric": 0,
                                "route_preference": 200,
                                "source_protocol_codes": "B",
                                "source_protocol": "bgp",
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "172.23.36.198",
                                            "updated": "1w5d",
                                        }
                                    }
                                },
                            },
                            "10.100.35.136/31": {
                                "route": "10.100.35.136/31",
                                "active": True,
                                "metric": 0,
                                "route_preference": 200,
                                "source_protocol_codes": "B",
                                "source_protocol": "bgp",
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "172.23.36.198",
                                            "updated": "1w5d",
                                        }
                                    }
                                },
                            },
                            "10.100.35.138/31": {
                                "route": "10.100.35.138/31",
                                "active": True,
                                "metric": 0,
                                "route_preference": 200,
                                "source_protocol_codes": "B",
                                "source_protocol": "bgp",
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "172.23.36.198",
                                            "updated": "1w5d",
                                        }
                                    }
                                },
                            },
                            "10.100.35.144/31": {
                                "route": "10.100.35.144/31",
                                "active": True,
                                "metric": 0,
                                "route_preference": 200,
                                "source_protocol_codes": "B",
                                "source_protocol": "bgp",
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "172.23.36.198",
                                            "updated": "1w5d",
                                        }
                                    }
                                },
                            },
                            "10.100.35.146/31": {
                                "route": "10.100.35.146/31",
                                "active": True,
                                "metric": 0,
                                "route_preference": 200,
                                "source_protocol_codes": "B",
                                "source_protocol": "bgp",
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "172.23.36.198",
                                            "updated": "1w5d",
                                        }
                                    }
                                },
                            },
                            "10.100.35.176/31": {
                                "route": "10.100.35.176/31",
                                "active": True,
                                "metric": 0,
                                "route_preference": 200,
                                "source_protocol_codes": "B",
                                "source_protocol": "bgp",
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "172.23.36.198",
                                            "updated": "1w5d",
                                        }
                                    }
                                },
                            },
                            "10.100.35.178/31": {
                                "route": "10.100.35.178/31",
                                "active": True,
                                "metric": 0,
                                "route_preference": 200,
                                "source_protocol_codes": "B",
                                "source_protocol": "bgp",
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "172.23.36.198",
                                            "updated": "1w5d",
                                        }
                                    }
                                },
                            },
                            "10.100.35.184/31": {
                                "route": "10.100.35.184/31",
                                "active": True,
                                "metric": 0,
                                "route_preference": 200,
                                "source_protocol_codes": "B",
                                "source_protocol": "bgp",
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "172.23.36.198",
                                            "updated": "1w5d",
                                        }
                                    }
                                },
                            },
                            "10.100.35.186/31": {
                                "route": "10.100.35.186/31",
                                "active": True,
                                "metric": 0,
                                "route_preference": 200,
                                "source_protocol_codes": "B",
                                "source_protocol": "bgp",
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "172.23.36.198",
                                            "updated": "1w5d",
                                        }
                                    }
                                },
                            },
                            "10.100.36.0/27": {
                                "route": "10.100.36.0/27",
                                "active": True,
                                "metric": 0,
                                "route_preference": 200,
                                "source_protocol_codes": "B",
                                "source_protocol": "bgp",
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "172.23.40.199",
                                            "updated": "5w1d",
                                        }
                                    }
                                },
                            },
                            "10.100.37.0/27": {
                                "route": "10.100.37.0/27",
                                "active": True,
                                "metric": 0,
                                "route_preference": 200,
                                "source_protocol_codes": "B",
                                "source_protocol": "bgp",
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "172.23.40.199",
                                            "updated": "5w1d",
                                        }
                                    }
                                },
                            },
                            "10.100.37.32/28": {
                                "route": "10.100.37.32/28",
                                "active": True,
                                "metric": 0,
                                "route_preference": 200,
                                "source_protocol_codes": "B",
                                "source_protocol": "bgp",
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "172.23.40.199",
                                            "updated": "5w1d",
                                        }
                                    }
                                },
                            },
                            "10.100.37.48/28": {
                                "route": "10.100.37.48/28",
                                "active": True,
                                "metric": 0,
                                "route_preference": 200,
                                "source_protocol_codes": "B",
                                "source_protocol": "bgp",
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "172.23.40.199",
                                            "updated": "5w1d",
                                        }
                                    }
                                },
                            },
                            "10.100.39.0/31": {
                                "route": "10.100.39.0/31",
                                "active": True,
                                "metric": 0,
                                "route_preference": 200,
                                "source_protocol_codes": "B",
                                "source_protocol": "bgp",
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "172.23.40.198",
                                            "updated": "15w4d",
                                        }
                                    }
                                },
                            },
                            "10.100.39.2/31": {
                                "route": "10.100.39.2/31",
                                "active": True,
                                "metric": 0,
                                "route_preference": 200,
                                "source_protocol_codes": "B",
                                "source_protocol": "bgp",
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "172.23.40.199",
                                            "updated": "15w4d",
                                        }
                                    }
                                },
                            },
                            "10.100.39.16/29": {
                                "route": "10.100.39.16/29",
                                "active": True,
                                "metric": 0,
                                "route_preference": 200,
                                "source_protocol_codes": "B",
                                "source_protocol": "bgp",
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "172.23.40.199",
                                            "updated": "5w1d",
                                        }
                                    }
                                },
                            },
                            "10.100.39.32/29": {
                                "route": "10.100.39.32/29",
                                "active": True,
                                "metric": 0,
                                "route_preference": 200,
                                "source_protocol_codes": "B",
                                "source_protocol": "bgp",
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "172.23.40.199",
                                            "updated": "5w1d",
                                        }
                                    }
                                },
                            },
                            "10.100.39.96/31": {
                                "route": "10.100.39.96/31",
                                "active": True,
                                "metric": 0,
                                "route_preference": 200,
                                "source_protocol_codes": "B",
                                "source_protocol": "bgp",
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "172.23.40.199",
                                            "updated": "5w1d",
                                        }
                                    }
                                },
                            },
                            "10.100.39.98/31": {
                                "route": "10.100.39.98/31",
                                "active": True,
                                "metric": 0,
                                "route_preference": 200,
                                "source_protocol_codes": "B",
                                "source_protocol": "bgp",
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "172.23.40.199",
                                            "updated": "5w1d",
                                        }
                                    }
                                },
                            },
                            "10.100.39.104/31": {
                                "route": "10.100.39.104/31",
                                "active": True,
                                "metric": 0,
                                "route_preference": 200,
                                "source_protocol_codes": "B",
                                "source_protocol": "bgp",
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "172.23.40.199",
                                            "updated": "5w1d",
                                        }
                                    }
                                },
                            },
                            "10.100.39.136/31": {
                                "route": "10.100.39.136/31",
                                "active": True,
                                "metric": 0,
                                "route_preference": 200,
                                "source_protocol_codes": "B",
                                "source_protocol": "bgp",
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "172.23.40.199",
                                            "updated": "5w1d",
                                        }
                                    }
                                },
                            },
                            "10.100.39.138/31": {
                                "route": "10.100.39.138/31",
                                "active": True,
                                "metric": 0,
                                "route_preference": 200,
                                "source_protocol_codes": "B",
                                "source_protocol": "bgp",
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "172.23.40.199",
                                            "updated": "5w1d",
                                        }
                                    }
                                },
                            },
                            "10.100.39.176/31": {
                                "route": "10.100.39.176/31",
                                "active": True,
                                "metric": 0,
                                "route_preference": 200,
                                "source_protocol_codes": "B",
                                "source_protocol": "bgp",
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "172.23.40.199",
                                            "updated": "5w1d",
                                        }
                                    }
                                },
                            },
                            "10.100.39.178/31": {
                                "route": "10.100.39.178/31",
                                "active": True,
                                "metric": 0,
                                "route_preference": 200,
                                "source_protocol_codes": "B",
                                "source_protocol": "bgp",
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "172.23.40.199",
                                            "updated": "5w1d",
                                        }
                                    }
                                },
                            },
                            "10.100.66.0/27": {
                                "route": "10.100.66.0/27",
                                "active": True,
                                "metric": 0,
                                "route_preference": 200,
                                "source_protocol_codes": "B",
                                "source_protocol": "bgp",
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "172.23.8.199",
                                            "updated": "5d14h",
                                        }
                                    }
                                },
                            },
                            "10.100.100.1/32": {
                                "route": "10.100.100.1/32",
                                "active": True,
                                "metric": 0,
                                "route_preference": 200,
                                "source_protocol_codes": "B",
                                "source_protocol": "bgp",
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "172.23.36.198",
                                            "updated": "1w5d",
                                        }
                                    }
                                },
                            },
                            "10.100.100.100/32": {
                                "route": "10.100.100.100/32",
                                "active": True,
                                "metric": 0,
                                "route_preference": 20,
                                "source_protocol_codes": "B",
                                "source_protocol": "bgp",
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "10.100.11.1",
                                            "updated": "5d13h",
                                        }
                                    }
                                },
                            },
                            "10.100.160.0/22": {
                                "route": "10.100.160.0/22",
                                "active": True,
                                "metric": 0,
                                "route_preference": 200,
                                "source_protocol_codes": "B",
                                "source_protocol": "bgp",
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "172.23.36.198",
                                            "updated": "1w5d",
                                        }
                                    }
                                },
                            },
                            "10.100.164.0/22": {
                                "route": "10.100.164.0/22",
                                "active": True,
                                "metric": 0,
                                "route_preference": 200,
                                "source_protocol_codes": "B",
                                "source_protocol": "bgp",
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "172.23.40.199",
                                            "updated": "5w1d",
                                        }
                                    }
                                },
                            },
                            "10.101.194.0/23": {
                                "route": "10.101.194.0/23",
                                "active": True,
                                "metric": 0,
                                "route_preference": 20,
                                "source_protocol_codes": "B",
                                "source_protocol": "bgp",
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "10.100.11.1",
                                            "updated": "31w5d",
                                        }
                                    }
                                },
                            },
                            "10.101.196.0/23": {
                                "route": "10.101.196.0/23",
                                "active": True,
                                "metric": 0,
                                "route_preference": 20,
                                "source_protocol_codes": "B",
                                "source_protocol": "bgp",
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "10.100.11.1",
                                            "updated": "31w5d",
                                        }
                                    }
                                },
                            },
                            "10.103.64.0/23": {
                                "route": "10.103.64.0/23",
                                "active": True,
                                "metric": 0,
                                "route_preference": 200,
                                "source_protocol_codes": "B",
                                "source_protocol": "bgp",
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "172.23.36.198",
                                            "updated": "1w5d",
                                        }
                                    }
                                },
                            },
                            "10.103.66.0/24": {
                                "route": "10.103.66.0/24",
                                "active": True,
                                "metric": 0,
                                "route_preference": 200,
                                "source_protocol_codes": "B",
                                "source_protocol": "bgp",
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "172.23.36.198",
                                            "updated": "1w5d",
                                        }
                                    }
                                },
                            },
                            "10.103.68.0/24": {
                                "route": "10.103.68.0/24",
                                "active": True,
                                "metric": 0,
                                "route_preference": 200,
                                "source_protocol_codes": "B",
                                "source_protocol": "bgp",
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "172.23.36.198",
                                            "updated": "1w5d",
                                        }
                                    }
                                },
                            },
                            "10.103.70.0/23": {
                                "route": "10.103.70.0/23",
                                "active": True,
                                "metric": 0,
                                "route_preference": 200,
                                "source_protocol_codes": "B",
                                "source_protocol": "bgp",
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "172.23.36.198",
                                            "updated": "1w0d",
                                        }
                                    }
                                },
                            },
                            "10.103.72.0/24": {
                                "route": "10.103.72.0/24",
                                "active": True,
                                "metric": 0,
                                "route_preference": 200,
                                "source_protocol_codes": "B",
                                "source_protocol": "bgp",
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "172.23.36.198",
                                            "updated": "1w5d",
                                        }
                                    }
                                },
                            },
                            "10.103.80.0/24": {
                                "route": "10.103.80.0/24",
                                "active": True,
                                "metric": 0,
                                "route_preference": 200,
                                "source_protocol_codes": "B",
                                "source_protocol": "bgp",
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "172.23.36.198",
                                            "updated": "1w5d",
                                        }
                                    }
                                },
                            },
                            "10.103.128.0/24": {
                                "route": "10.103.128.0/24",
                                "active": True,
                                "metric": 0,
                                "route_preference": 200,
                                "source_protocol_codes": "B",
                                "source_protocol": "bgp",
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "172.23.40.199",
                                            "updated": "5w1d",
                                        }
                                    }
                                },
                            },
                            "10.103.130.0/24": {
                                "route": "10.103.130.0/24",
                                "active": True,
                                "metric": 0,
                                "route_preference": 200,
                                "source_protocol_codes": "B",
                                "source_protocol": "bgp",
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "172.23.40.199",
                                            "updated": "5w1d",
                                        }
                                    }
                                },
                            },
                            "10.103.132.0/24": {
                                "route": "10.103.132.0/24",
                                "active": True,
                                "metric": 0,
                                "route_preference": 200,
                                "source_protocol_codes": "B",
                                "source_protocol": "bgp",
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "172.23.40.199",
                                            "updated": "5w1d",
                                        }
                                    }
                                },
                            },
                            "10.103.134.0/23": {
                                "route": "10.103.134.0/23",
                                "active": True,
                                "metric": 0,
                                "route_preference": 200,
                                "source_protocol_codes": "B",
                                "source_protocol": "bgp",
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "172.23.40.199",
                                            "updated": "5w1d",
                                        }
                                    }
                                },
                            },
                            "10.103.144.0/24": {
                                "route": "10.103.144.0/24",
                                "active": True,
                                "metric": 0,
                                "route_preference": 200,
                                "source_protocol_codes": "B",
                                "source_protocol": "bgp",
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "172.23.40.199",
                                            "updated": "5w1d",
                                        }
                                    }
                                },
                            },
                            "10.111.195.0/27": {
                                "route": "10.111.195.0/27",
                                "active": True,
                                "metric": 0,
                                "route_preference": 20,
                                "source_protocol_codes": "B",
                                "source_protocol": "bgp",
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "10.100.11.1",
                                            "updated": "31w5d",
                                        }
                                    }
                                },
                            },
                            "10.111.195.64/27": {
                                "route": "10.111.195.64/27",
                                "active": True,
                                "metric": 0,
                                "route_preference": 20,
                                "source_protocol_codes": "B",
                                "source_protocol": "bgp",
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "10.100.11.1",
                                            "updated": "31w5d",
                                        }
                                    }
                                },
                            },
                            "10.111.195.128/27": {
                                "route": "10.111.195.128/27",
                                "active": True,
                                "metric": 0,
                                "route_preference": 20,
                                "source_protocol_codes": "B",
                                "source_protocol": "bgp",
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "10.100.11.1",
                                            "updated": "31w5d",
                                        }
                                    }
                                },
                            },
                            "10.111.254.0/27": {
                                "route": "10.111.254.0/27",
                                "active": True,
                                "metric": 0,
                                "route_preference": 20,
                                "source_protocol_codes": "B",
                                "source_protocol": "bgp",
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "10.100.11.1",
                                            "updated": "31w5d",
                                        }
                                    }
                                },
                            },
                            "10.111.254.32/27": {
                                "route": "10.111.254.32/27",
                                "active": True,
                                "metric": 0,
                                "route_preference": 20,
                                "source_protocol_codes": "B",
                                "source_protocol": "bgp",
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "10.100.11.1",
                                            "updated": "31w5d",
                                        }
                                    }
                                },
                            },
                            "10.113.64.0/23": {
                                "route": "10.113.64.0/23",
                                "active": True,
                                "metric": 0,
                                "route_preference": 200,
                                "source_protocol_codes": "B",
                                "source_protocol": "bgp",
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "172.23.36.198",
                                            "updated": "1w5d",
                                        }
                                    }
                                },
                            },
                            "10.113.66.0/24": {
                                "route": "10.113.66.0/24",
                                "active": True,
                                "metric": 0,
                                "route_preference": 200,
                                "source_protocol_codes": "B",
                                "source_protocol": "bgp",
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "172.23.36.198",
                                            "updated": "1w5d",
                                        }
                                    }
                                },
                            },
                            "10.113.67.0/27": {
                                "route": "10.113.67.0/27",
                                "active": True,
                                "metric": 0,
                                "route_preference": 200,
                                "source_protocol_codes": "B",
                                "source_protocol": "bgp",
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "172.23.36.198",
                                            "updated": "1w5d",
                                        }
                                    }
                                },
                            },
                            "10.113.67.64/27": {
                                "route": "10.113.67.64/27",
                                "active": True,
                                "metric": 0,
                                "route_preference": 200,
                                "source_protocol_codes": "B",
                                "source_protocol": "bgp",
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "172.23.36.198",
                                            "updated": "1w5d",
                                        }
                                    }
                                },
                            },
                            "10.113.67.128/27": {
                                "route": "10.113.67.128/27",
                                "active": True,
                                "metric": 0,
                                "route_preference": 200,
                                "source_protocol_codes": "B",
                                "source_protocol": "bgp",
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "172.23.36.198",
                                            "updated": "1w5d",
                                        }
                                    }
                                },
                            },
                            "10.113.72.0/23": {
                                "route": "10.113.72.0/23",
                                "active": True,
                                "metric": 0,
                                "route_preference": 200,
                                "source_protocol_codes": "B",
                                "source_protocol": "bgp",
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "172.23.36.198",
                                            "updated": "1w5d",
                                        }
                                    }
                                },
                            },
                            "10.113.74.0/23": {
                                "route": "10.113.74.0/23",
                                "active": True,
                                "metric": 0,
                                "route_preference": 200,
                                "source_protocol_codes": "B",
                                "source_protocol": "bgp",
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "172.23.36.198",
                                            "updated": "1w5d",
                                        }
                                    }
                                },
                            },
                            "10.113.84.0/23": {
                                "route": "10.113.84.0/23",
                                "active": True,
                                "metric": 0,
                                "route_preference": 200,
                                "source_protocol_codes": "B",
                                "source_protocol": "bgp",
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "172.23.36.198",
                                            "updated": "1w5d",
                                        }
                                    }
                                },
                            },
                            "10.113.86.0/23": {
                                "route": "10.113.86.0/23",
                                "active": True,
                                "metric": 0,
                                "route_preference": 200,
                                "source_protocol_codes": "B",
                                "source_protocol": "bgp",
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "172.23.36.198",
                                            "updated": "1w5d",
                                        }
                                    }
                                },
                            },
                            "10.113.88.0/23": {
                                "route": "10.113.88.0/23",
                                "active": True,
                                "metric": 0,
                                "route_preference": 200,
                                "source_protocol_codes": "B",
                                "source_protocol": "bgp",
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "172.23.36.198",
                                            "updated": "1w5d",
                                        }
                                    }
                                },
                            },
                            "10.113.118.0/24": {
                                "route": "10.113.118.0/24",
                                "active": True,
                                "metric": 0,
                                "route_preference": 200,
                                "source_protocol_codes": "B",
                                "source_protocol": "bgp",
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "172.23.36.198",
                                            "updated": "1w5d",
                                        }
                                    }
                                },
                            },
                            "10.113.120.0/24": {
                                "route": "10.113.120.0/24",
                                "active": True,
                                "metric": 0,
                                "route_preference": 200,
                                "source_protocol_codes": "B",
                                "source_protocol": "bgp",
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "172.23.36.198",
                                            "updated": "1w5d",
                                        }
                                    }
                                },
                            },
                            "10.113.121.0/24": {
                                "route": "10.113.121.0/24",
                                "active": True,
                                "metric": 0,
                                "route_preference": 200,
                                "source_protocol_codes": "B",
                                "source_protocol": "bgp",
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "172.23.36.198",
                                            "updated": "1w5d",
                                        }
                                    }
                                },
                            },
                            "10.113.122.0/24": {
                                "route": "10.113.122.0/24",
                                "active": True,
                                "metric": 0,
                                "route_preference": 200,
                                "source_protocol_codes": "B",
                                "source_protocol": "bgp",
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "172.23.36.198",
                                            "updated": "1w5d",
                                        }
                                    }
                                },
                            },
                            "10.113.123.0/24": {
                                "route": "10.113.123.0/24",
                                "active": True,
                                "metric": 0,
                                "route_preference": 200,
                                "source_protocol_codes": "B",
                                "source_protocol": "bgp",
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "172.23.36.198",
                                            "updated": "1w5d",
                                        }
                                    }
                                },
                            },
                            "10.113.126.0/27": {
                                "route": "10.113.126.0/27",
                                "active": True,
                                "metric": 0,
                                "route_preference": 200,
                                "source_protocol_codes": "B",
                                "source_protocol": "bgp",
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "172.23.36.198",
                                            "updated": "1w5d",
                                        }
                                    }
                                },
                            },
                            "10.113.126.32/27": {
                                "route": "10.113.126.32/27",
                                "active": True,
                                "metric": 0,
                                "route_preference": 200,
                                "source_protocol_codes": "B",
                                "source_protocol": "bgp",
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "172.23.36.198",
                                            "updated": "1w5d",
                                        }
                                    }
                                },
                            },
                            "10.113.126.64/27": {
                                "route": "10.113.126.64/27",
                                "active": True,
                                "metric": 0,
                                "route_preference": 200,
                                "source_protocol_codes": "B",
                                "source_protocol": "bgp",
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "172.23.36.198",
                                            "updated": "1w5d",
                                        }
                                    }
                                },
                            },
                            "10.113.126.96/27": {
                                "route": "10.113.126.96/27",
                                "active": True,
                                "metric": 0,
                                "route_preference": 200,
                                "source_protocol_codes": "B",
                                "source_protocol": "bgp",
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "172.23.36.198",
                                            "updated": "1w5d",
                                        }
                                    }
                                },
                            },
                            "10.113.128.0/23": {
                                "route": "10.113.128.0/23",
                                "active": True,
                                "metric": 0,
                                "route_preference": 200,
                                "source_protocol_codes": "B",
                                "source_protocol": "bgp",
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "172.23.40.199",
                                            "updated": "5w1d",
                                        }
                                    }
                                },
                            },
                            "10.113.130.0/24": {
                                "route": "10.113.130.0/24",
                                "active": True,
                                "metric": 0,
                                "route_preference": 200,
                                "source_protocol_codes": "B",
                                "source_protocol": "bgp",
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "172.23.40.199",
                                            "updated": "5w1d",
                                        }
                                    }
                                },
                            },
                            "10.113.131.0/27": {
                                "route": "10.113.131.0/27",
                                "active": True,
                                "metric": 0,
                                "route_preference": 200,
                                "source_protocol_codes": "B",
                                "source_protocol": "bgp",
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "172.23.40.199",
                                            "updated": "5w1d",
                                        }
                                    }
                                },
                            },
                            "10.113.131.64/27": {
                                "route": "10.113.131.64/27",
                                "active": True,
                                "metric": 0,
                                "route_preference": 200,
                                "source_protocol_codes": "B",
                                "source_protocol": "bgp",
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "172.23.40.199",
                                            "updated": "5w1d",
                                        }
                                    }
                                },
                            },
                            "10.113.131.128/27": {
                                "route": "10.113.131.128/27",
                                "active": True,
                                "metric": 0,
                                "route_preference": 200,
                                "source_protocol_codes": "B",
                                "source_protocol": "bgp",
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "172.23.40.199",
                                            "updated": "5w1d",
                                        }
                                    }
                                },
                            },
                            "10.113.136.0/23": {
                                "route": "10.113.136.0/23",
                                "active": True,
                                "metric": 0,
                                "route_preference": 200,
                                "source_protocol_codes": "B",
                                "source_protocol": "bgp",
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "172.23.40.199",
                                            "updated": "5w1d",
                                        }
                                    }
                                },
                            },
                            "10.113.138.0/23": {
                                "route": "10.113.138.0/23",
                                "active": True,
                                "metric": 0,
                                "route_preference": 200,
                                "source_protocol_codes": "B",
                                "source_protocol": "bgp",
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "172.23.40.199",
                                            "updated": "5w1d",
                                        }
                                    }
                                },
                            },
                            "10.113.148.0/23": {
                                "route": "10.113.148.0/23",
                                "active": True,
                                "metric": 0,
                                "route_preference": 200,
                                "source_protocol_codes": "B",
                                "source_protocol": "bgp",
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "172.23.40.199",
                                            "updated": "5w1d",
                                        }
                                    }
                                },
                            },
                            "10.113.182.0/24": {
                                "route": "10.113.182.0/24",
                                "active": True,
                                "metric": 0,
                                "route_preference": 200,
                                "source_protocol_codes": "B",
                                "source_protocol": "bgp",
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "172.23.40.199",
                                            "updated": "5w1d",
                                        }
                                    }
                                },
                            },
                            "10.113.184.0/24": {
                                "route": "10.113.184.0/24",
                                "active": True,
                                "metric": 0,
                                "route_preference": 200,
                                "source_protocol_codes": "B",
                                "source_protocol": "bgp",
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "172.23.40.199",
                                            "updated": "5w1d",
                                        }
                                    }
                                },
                            },
                            "10.113.185.0/24": {
                                "route": "10.113.185.0/24",
                                "active": True,
                                "metric": 0,
                                "route_preference": 200,
                                "source_protocol_codes": "B",
                                "source_protocol": "bgp",
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "172.23.40.199",
                                            "updated": "5w1d",
                                        }
                                    }
                                },
                            },
                            "10.113.190.0/27": {
                                "route": "10.113.190.0/27",
                                "active": True,
                                "metric": 0,
                                "route_preference": 200,
                                "source_protocol_codes": "B",
                                "source_protocol": "bgp",
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "172.23.40.199",
                                            "updated": "5w1d",
                                        }
                                    }
                                },
                            },
                            "10.113.190.32/27": {
                                "route": "10.113.190.32/27",
                                "active": True,
                                "metric": 0,
                                "route_preference": 200,
                                "source_protocol_codes": "B",
                                "source_protocol": "bgp",
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "172.23.40.199",
                                            "updated": "5w1d",
                                        }
                                    }
                                },
                            },
                            "10.113.190.64/27": {
                                "route": "10.113.190.64/27",
                                "active": True,
                                "metric": 0,
                                "route_preference": 200,
                                "source_protocol_codes": "B",
                                "source_protocol": "bgp",
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "172.23.40.199",
                                            "updated": "5w1d",
                                        }
                                    }
                                },
                            },
                            "10.113.190.96/27": {
                                "route": "10.113.190.96/27",
                                "active": True,
                                "metric": 0,
                                "route_preference": 200,
                                "source_protocol_codes": "B",
                                "source_protocol": "bgp",
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "172.23.40.199",
                                            "updated": "5w1d",
                                        }
                                    }
                                },
                            },
                            "10.170.0.0/16": {
                                "route": "10.170.0.0/16",
                                "active": True,
                                "metric": 0,
                                "route_preference": 1,
                                "source_protocol_codes": "S",
                                "source_protocol": "static",
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "10.100.11.20",
                                            "updated": "36w5d",
                                        }
                                    }
                                },
                            },
                            "10.170.19.0/24": {
                                "route": "10.170.19.0/24",
                                "active": True,
                                "metric": 0,
                                "route_preference": 200,
                                "source_protocol_codes": "B",
                                "source_protocol": "bgp",
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "172.23.6.198",
                                            "updated": "5d13h",
                                        }
                                    }
                                },
                            },
                            "10.170.22.0/24": {
                                "route": "10.170.22.0/24",
                                "active": True,
                                "metric": 0,
                                "route_preference": 200,
                                "source_protocol_codes": "B",
                                "source_protocol": "bgp",
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "172.23.6.198",
                                            "updated": "5d13h",
                                        }
                                    }
                                },
                            },
                            "10.170.47.0/24": {
                                "route": "10.170.47.0/24",
                                "active": True,
                                "metric": 0,
                                "route_preference": 1,
                                "source_protocol_codes": "S",
                                "source_protocol": "static",
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "10.100.11.20",
                                            "updated": "36w5d",
                                        }
                                    }
                                },
                            },
                            "10.170.60.0/22": {
                                "route": "10.170.60.0/22",
                                "active": True,
                                "metric": 0,
                                "route_preference": 200,
                                "source_protocol_codes": "B",
                                "source_protocol": "bgp",
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "172.23.6.198",
                                            "updated": "5d13h",
                                        }
                                    }
                                },
                            },
                            "10.170.136.0/23": {
                                "route": "10.170.136.0/23",
                                "active": True,
                                "metric": 0,
                                "route_preference": 200,
                                "source_protocol_codes": "B",
                                "source_protocol": "bgp",
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "172.23.6.198",
                                            "updated": "5d13h",
                                        }
                                    }
                                },
                            },
                            "10.170.136.2/32": {
                                "route": "10.170.136.2/32",
                                "active": True,
                                "metric": 0,
                                "route_preference": 200,
                                "source_protocol_codes": "B",
                                "source_protocol": "bgp",
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "172.23.6.198",
                                            "updated": "5d13h",
                                        }
                                    }
                                },
                            },
                            "10.170.136.3/32": {
                                "route": "10.170.136.3/32",
                                "active": True,
                                "metric": 0,
                                "route_preference": 200,
                                "source_protocol_codes": "B",
                                "source_protocol": "bgp",
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "172.23.6.198",
                                            "updated": "5d13h",
                                        }
                                    }
                                },
                            },
                            "10.170.138.0/24": {
                                "route": "10.170.138.0/24",
                                "active": True,
                                "metric": 0,
                                "route_preference": 200,
                                "source_protocol_codes": "B",
                                "source_protocol": "bgp",
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "172.23.6.198",
                                            "updated": "5d13h",
                                        }
                                    }
                                },
                            },
                            "10.170.138.2/32": {
                                "route": "10.170.138.2/32",
                                "active": True,
                                "metric": 0,
                                "route_preference": 200,
                                "source_protocol_codes": "B",
                                "source_protocol": "bgp",
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "172.23.6.198",
                                            "updated": "5d13h",
                                        }
                                    }
                                },
                            },
                            "10.170.138.3/32": {
                                "route": "10.170.138.3/32",
                                "active": True,
                                "metric": 0,
                                "route_preference": 200,
                                "source_protocol_codes": "B",
                                "source_protocol": "bgp",
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "172.23.6.198",
                                            "updated": "5d13h",
                                        }
                                    }
                                },
                            },
                            "10.170.139.0/24": {
                                "route": "10.170.139.0/24",
                                "active": True,
                                "metric": 0,
                                "route_preference": 200,
                                "source_protocol_codes": "B",
                                "source_protocol": "bgp",
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "172.23.6.198",
                                            "updated": "5d13h",
                                        }
                                    }
                                },
                            },
                            "10.170.139.2/32": {
                                "route": "10.170.139.2/32",
                                "active": True,
                                "metric": 0,
                                "route_preference": 200,
                                "source_protocol_codes": "B",
                                "source_protocol": "bgp",
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "172.23.6.198",
                                            "updated": "5d13h",
                                        }
                                    }
                                },
                            },
                            "10.170.139.3/32": {
                                "route": "10.170.139.3/32",
                                "active": True,
                                "metric": 0,
                                "route_preference": 200,
                                "source_protocol_codes": "B",
                                "source_protocol": "bgp",
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "172.23.6.198",
                                            "updated": "5d13h",
                                        }
                                    }
                                },
                            },
                            "10.170.140.0/22": {
                                "route": "10.170.140.0/22",
                                "active": True,
                                "metric": 0,
                                "route_preference": 200,
                                "source_protocol_codes": "B",
                                "source_protocol": "bgp",
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "172.23.6.198",
                                            "updated": "5d13h",
                                        }
                                    }
                                },
                            },
                            "10.170.140.2/32": {
                                "route": "10.170.140.2/32",
                                "active": True,
                                "metric": 0,
                                "route_preference": 200,
                                "source_protocol_codes": "B",
                                "source_protocol": "bgp",
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "172.23.6.198",
                                            "updated": "5d13h",
                                        }
                                    }
                                },
                            },
                            "10.170.140.3/32": {
                                "route": "10.170.140.3/32",
                                "active": True,
                                "metric": 0,
                                "route_preference": 200,
                                "source_protocol_codes": "B",
                                "source_protocol": "bgp",
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "172.23.6.198",
                                            "updated": "5d13h",
                                        }
                                    }
                                },
                            },
                            "10.170.142.2/32": {
                                "route": "10.170.142.2/32",
                                "active": True,
                                "metric": 0,
                                "route_preference": 200,
                                "source_protocol_codes": "B",
                                "source_protocol": "bgp",
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "172.23.6.198",
                                            "updated": "5d13h",
                                        }
                                    }
                                },
                            },
                            "10.170.142.3/32": {
                                "route": "10.170.142.3/32",
                                "active": True,
                                "metric": 0,
                                "route_preference": 200,
                                "source_protocol_codes": "B",
                                "source_protocol": "bgp",
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "172.23.6.198",
                                            "updated": "5d13h",
                                        }
                                    }
                                },
                            },
                            "10.170.143.2/32": {
                                "route": "10.170.143.2/32",
                                "active": True,
                                "metric": 0,
                                "route_preference": 200,
                                "source_protocol_codes": "B",
                                "source_protocol": "bgp",
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "172.23.6.198",
                                            "updated": "5d13h",
                                        }
                                    }
                                },
                            },
                            "10.170.143.3/32": {
                                "route": "10.170.143.3/32",
                                "active": True,
                                "metric": 0,
                                "route_preference": 200,
                                "source_protocol_codes": "B",
                                "source_protocol": "bgp",
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "172.23.6.198",
                                            "updated": "5d13h",
                                        }
                                    }
                                },
                            },
                            "10.170.150.0/24": {
                                "route": "10.170.150.0/24",
                                "active": True,
                                "metric": 0,
                                "route_preference": 200,
                                "source_protocol_codes": "B",
                                "source_protocol": "bgp",
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "172.23.6.198",
                                            "updated": "5d13h",
                                        }
                                    }
                                },
                            },
                            "10.170.188.0/22": {
                                "route": "10.170.188.0/22",
                                "active": True,
                                "metric": 0,
                                "route_preference": 200,
                                "source_protocol_codes": "B",
                                "source_protocol": "bgp",
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "172.23.8.199",
                                            "updated": "5d14h",
                                        }
                                    }
                                },
                            },
                            "10.172.44.0/24": {
                                "route": "10.172.44.0/24",
                                "active": True,
                                "metric": 0,
                                "route_preference": 200,
                                "source_protocol_codes": "B",
                                "source_protocol": "bgp",
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "172.23.36.198",
                                            "updated": "1w5d",
                                        }
                                    }
                                },
                            },
                            "10.172.64.48/28": {
                                "route": "10.172.64.48/28",
                                "active": True,
                                "metric": 0,
                                "route_preference": 200,
                                "source_protocol_codes": "B",
                                "source_protocol": "bgp",
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "172.23.36.198",
                                            "updated": "1w5d",
                                        }
                                    }
                                },
                            },
                            "10.172.64.114/31": {
                                "route": "10.172.64.114/31",
                                "active": True,
                                "metric": 0,
                                "route_preference": 200,
                                "source_protocol_codes": "B",
                                "source_protocol": "bgp",
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "172.23.36.198",
                                            "updated": "1w5d",
                                        }
                                    }
                                },
                            },
                            "10.172.64.116/31": {
                                "route": "10.172.64.116/31",
                                "active": True,
                                "metric": 0,
                                "route_preference": 200,
                                "source_protocol_codes": "B",
                                "source_protocol": "bgp",
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "172.23.36.198",
                                            "updated": "1w5d",
                                        }
                                    }
                                },
                            },
                            "10.172.64.120/30": {
                                "route": "10.172.64.120/30",
                                "active": True,
                                "metric": 0,
                                "route_preference": 200,
                                "source_protocol_codes": "B",
                                "source_protocol": "bgp",
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "172.23.36.198",
                                            "updated": "1w5d",
                                        }
                                    }
                                },
                            },
                            "10.172.96.48/28": {
                                "route": "10.172.96.48/28",
                                "active": True,
                                "metric": 0,
                                "route_preference": 200,
                                "source_protocol_codes": "B",
                                "source_protocol": "bgp",
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "172.23.36.198",
                                            "updated": "1w5d",
                                        }
                                    }
                                },
                            },
                            "10.172.97.0/24": {
                                "route": "10.172.97.0/24",
                                "active": True,
                                "metric": 0,
                                "route_preference": 200,
                                "source_protocol_codes": "B",
                                "source_protocol": "bgp",
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "172.23.36.198",
                                            "updated": "1w5d",
                                        }
                                    }
                                },
                            },
                            "10.172.100.0/23": {
                                "route": "10.172.100.0/23",
                                "active": True,
                                "metric": 0,
                                "route_preference": 200,
                                "source_protocol_codes": "B",
                                "source_protocol": "bgp",
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "172.23.36.198",
                                            "updated": "1w5d",
                                        }
                                    }
                                },
                            },
                            "10.172.102.0/23": {
                                "route": "10.172.102.0/23",
                                "active": True,
                                "metric": 0,
                                "route_preference": 200,
                                "source_protocol_codes": "B",
                                "source_protocol": "bgp",
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "172.23.36.198",
                                            "updated": "1w5d",
                                        }
                                    }
                                },
                            },
                            "10.172.108.0/24": {
                                "route": "10.172.108.0/24",
                                "active": True,
                                "metric": 0,
                                "route_preference": 200,
                                "source_protocol_codes": "B",
                                "source_protocol": "bgp",
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "172.23.36.198",
                                            "updated": "1w5d",
                                        }
                                    }
                                },
                            },
                            "10.172.110.0/27": {
                                "route": "10.172.110.0/27",
                                "active": True,
                                "metric": 0,
                                "route_preference": 200,
                                "source_protocol_codes": "B",
                                "source_protocol": "bgp",
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "172.23.36.198",
                                            "updated": "1w5d",
                                        }
                                    }
                                },
                            },
                            "10.172.110.128/27": {
                                "route": "10.172.110.128/27",
                                "active": True,
                                "metric": 0,
                                "route_preference": 200,
                                "source_protocol_codes": "B",
                                "source_protocol": "bgp",
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "172.23.36.198",
                                            "updated": "1w5d",
                                        }
                                    }
                                },
                            },
                            "10.172.112.0/22": {
                                "route": "10.172.112.0/22",
                                "active": True,
                                "metric": 0,
                                "route_preference": 200,
                                "source_protocol_codes": "B",
                                "source_protocol": "bgp",
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "172.23.36.198",
                                            "updated": "1w5d",
                                        }
                                    }
                                },
                            },
                            "10.172.116.0/22": {
                                "route": "10.172.116.0/22",
                                "active": True,
                                "metric": 0,
                                "route_preference": 200,
                                "source_protocol_codes": "B",
                                "source_protocol": "bgp",
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "172.23.36.198",
                                            "updated": "1w5d",
                                        }
                                    }
                                },
                            },
                            "10.172.128.48/28": {
                                "route": "10.172.128.48/28",
                                "active": True,
                                "metric": 0,
                                "route_preference": 200,
                                "source_protocol_codes": "B",
                                "source_protocol": "bgp",
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "172.23.40.199",
                                            "updated": "5w1d",
                                        }
                                    }
                                },
                            },
                            "10.172.128.114/31": {
                                "route": "10.172.128.114/31",
                                "active": True,
                                "metric": 0,
                                "route_preference": 200,
                                "source_protocol_codes": "B",
                                "source_protocol": "bgp",
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "172.23.40.199",
                                            "updated": "5w1d",
                                        }
                                    }
                                },
                            },
                            "10.172.128.116/31": {
                                "route": "10.172.128.116/31",
                                "active": True,
                                "metric": 0,
                                "route_preference": 200,
                                "source_protocol_codes": "B",
                                "source_protocol": "bgp",
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "172.23.40.199",
                                            "updated": "5w1d",
                                        }
                                    }
                                },
                            },
                            "10.172.128.120/30": {
                                "route": "10.172.128.120/30",
                                "active": True,
                                "metric": 0,
                                "route_preference": 200,
                                "source_protocol_codes": "B",
                                "source_protocol": "bgp",
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "172.23.40.199",
                                            "updated": "5w1d",
                                        }
                                    }
                                },
                            },
                            "10.172.131.0/24": {
                                "route": "10.172.131.0/24",
                                "active": True,
                                "metric": 0,
                                "route_preference": 200,
                                "source_protocol_codes": "B",
                                "source_protocol": "bgp",
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "172.23.40.199",
                                            "updated": "5w1d",
                                        }
                                    }
                                },
                            },
                            "10.172.132.0/23": {
                                "route": "10.172.132.0/23",
                                "active": True,
                                "metric": 0,
                                "route_preference": 200,
                                "source_protocol_codes": "B",
                                "source_protocol": "bgp",
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "172.23.40.199",
                                            "updated": "5w1d",
                                        }
                                    }
                                },
                            },
                            "10.172.160.0/20": {
                                "route": "10.172.160.0/20",
                                "active": True,
                                "metric": 0,
                                "route_preference": 200,
                                "source_protocol_codes": "B",
                                "source_protocol": "bgp",
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "172.23.40.199",
                                            "updated": "5w1d",
                                        }
                                    }
                                },
                            },
                            "10.172.161.0/24": {
                                "route": "10.172.161.0/24",
                                "active": True,
                                "metric": 0,
                                "route_preference": 200,
                                "source_protocol_codes": "B",
                                "source_protocol": "bgp",
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "172.23.40.199",
                                            "updated": "5w1d",
                                        }
                                    }
                                },
                            },
                            "10.172.166.0/23": {
                                "route": "10.172.166.0/23",
                                "active": True,
                                "metric": 0,
                                "route_preference": 200,
                                "source_protocol_codes": "B",
                                "source_protocol": "bgp",
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "172.23.40.199",
                                            "updated": "5w1d",
                                        }
                                    }
                                },
                            },
                            "10.172.172.0/24": {
                                "route": "10.172.172.0/24",
                                "active": True,
                                "metric": 0,
                                "route_preference": 200,
                                "source_protocol_codes": "B",
                                "source_protocol": "bgp",
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "172.23.40.199",
                                            "updated": "5w1d",
                                        }
                                    }
                                },
                            },
                            "10.172.174.0/27": {
                                "route": "10.172.174.0/27",
                                "active": True,
                                "metric": 0,
                                "route_preference": 200,
                                "source_protocol_codes": "B",
                                "source_protocol": "bgp",
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "172.23.40.199",
                                            "updated": "5w1d",
                                        }
                                    }
                                },
                            },
                            "10.172.174.128/27": {
                                "route": "10.172.174.128/27",
                                "active": True,
                                "metric": 0,
                                "route_preference": 200,
                                "source_protocol_codes": "B",
                                "source_protocol": "bgp",
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "172.23.40.199",
                                            "updated": "5w1d",
                                        }
                                    }
                                },
                            },
                            "10.172.180.0/22": {
                                "route": "10.172.180.0/22",
                                "active": True,
                                "metric": 0,
                                "route_preference": 200,
                                "source_protocol_codes": "B",
                                "source_protocol": "bgp",
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "172.23.40.199",
                                            "updated": "5w1d",
                                        }
                                    }
                                },
                            },
                            "10.172.224.0/31": {
                                "route": "10.172.224.0/31",
                                "active": True,
                                "metric": 0,
                                "route_preference": 200,
                                "source_protocol_codes": "B",
                                "source_protocol": "bgp",
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "172.23.36.198",
                                            "updated": "1w5d",
                                        }
                                    }
                                },
                            },
                            "10.172.224.2/31": {
                                "route": "10.172.224.2/31",
                                "active": True,
                                "metric": 0,
                                "route_preference": 200,
                                "source_protocol_codes": "B",
                                "source_protocol": "bgp",
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "172.23.36.198",
                                            "updated": "1w5d",
                                        }
                                    }
                                },
                            },
                            "10.172.224.34/31": {
                                "route": "10.172.224.34/31",
                                "active": True,
                                "metric": 0,
                                "route_preference": 200,
                                "source_protocol_codes": "B",
                                "source_protocol": "bgp",
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "172.23.36.198",
                                            "updated": "1w5d",
                                        }
                                    }
                                },
                            },
                            "10.172.224.36/31": {
                                "route": "10.172.224.36/31",
                                "active": True,
                                "metric": 0,
                                "route_preference": 200,
                                "source_protocol_codes": "B",
                                "source_protocol": "bgp",
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "172.23.36.198",
                                            "updated": "1w5d",
                                        }
                                    }
                                },
                            },
                            "10.172.224.148/31": {
                                "route": "10.172.224.148/31",
                                "active": True,
                                "metric": 0,
                                "route_preference": 200,
                                "source_protocol_codes": "B",
                                "source_protocol": "bgp",
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "172.23.36.198",
                                            "updated": "1w5d",
                                        }
                                    }
                                },
                            },
                            "10.172.224.150/31": {
                                "route": "10.172.224.150/31",
                                "active": True,
                                "metric": 0,
                                "route_preference": 200,
                                "source_protocol_codes": "B",
                                "source_protocol": "bgp",
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "172.23.36.198",
                                            "updated": "1w5d",
                                        }
                                    }
                                },
                            },
                            "10.172.228.0/23": {
                                "route": "10.172.228.0/23",
                                "active": True,
                                "metric": 0,
                                "route_preference": 200,
                                "source_protocol_codes": "B",
                                "source_protocol": "bgp",
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "172.23.36.198",
                                            "updated": "1w5d",
                                        }
                                    }
                                },
                            },
                            "10.172.230.0/24": {
                                "route": "10.172.230.0/24",
                                "active": True,
                                "metric": 0,
                                "route_preference": 200,
                                "source_protocol_codes": "B",
                                "source_protocol": "bgp",
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "172.23.36.198",
                                            "updated": "1w5d",
                                        }
                                    }
                                },
                            },
                            "10.172.231.0/25": {
                                "route": "10.172.231.0/25",
                                "active": True,
                                "metric": 0,
                                "route_preference": 200,
                                "source_protocol_codes": "B",
                                "source_protocol": "bgp",
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "172.23.36.198",
                                            "updated": "1w5d",
                                        }
                                    }
                                },
                            },
                            "10.172.231.128/27": {
                                "route": "10.172.231.128/27",
                                "active": True,
                                "metric": 0,
                                "route_preference": 200,
                                "source_protocol_codes": "B",
                                "source_protocol": "bgp",
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "172.23.36.198",
                                            "updated": "1w5d",
                                        }
                                    }
                                },
                            },
                            "10.172.231.240/28": {
                                "route": "10.172.231.240/28",
                                "active": True,
                                "metric": 0,
                                "route_preference": 200,
                                "source_protocol_codes": "B",
                                "source_protocol": "bgp",
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "172.23.36.198",
                                            "updated": "1w5d",
                                        }
                                    }
                                },
                            },
                            "10.172.236.0/23": {
                                "route": "10.172.236.0/23",
                                "active": True,
                                "metric": 0,
                                "route_preference": 200,
                                "source_protocol_codes": "B",
                                "source_protocol": "bgp",
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "172.23.36.198",
                                            "updated": "1w5d",
                                        }
                                    }
                                },
                            },
                            "10.172.238.0/27": {
                                "route": "10.172.238.0/27",
                                "active": True,
                                "metric": 0,
                                "route_preference": 200,
                                "source_protocol_codes": "B",
                                "source_protocol": "bgp",
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "172.23.36.198",
                                            "updated": "1w5d",
                                        }
                                    }
                                },
                            },
                            "10.172.238.64/26": {
                                "route": "10.172.238.64/26",
                                "active": True,
                                "metric": 0,
                                "route_preference": 200,
                                "source_protocol_codes": "B",
                                "source_protocol": "bgp",
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "172.23.36.198",
                                            "updated": "1w5d",
                                        }
                                    }
                                },
                            },
                            "10.172.238.128/27": {
                                "route": "10.172.238.128/27",
                                "active": True,
                                "metric": 0,
                                "route_preference": 200,
                                "source_protocol_codes": "B",
                                "source_protocol": "bgp",
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "172.23.36.198",
                                            "updated": "1w5d",
                                        }
                                    }
                                },
                            },
                            "10.172.239.128/28": {
                                "route": "10.172.239.128/28",
                                "active": True,
                                "metric": 0,
                                "route_preference": 200,
                                "source_protocol_codes": "B",
                                "source_protocol": "bgp",
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "172.23.36.198",
                                            "updated": "1w5d",
                                        }
                                    }
                                },
                            },
                            "10.172.240.0/31": {
                                "route": "10.172.240.0/31",
                                "active": True,
                                "metric": 0,
                                "route_preference": 200,
                                "source_protocol_codes": "B",
                                "source_protocol": "bgp",
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "172.23.36.198",
                                            "updated": "1w5d",
                                        }
                                    }
                                },
                            },
                            "10.172.240.2/31": {
                                "route": "10.172.240.2/31",
                                "active": True,
                                "metric": 0,
                                "route_preference": 200,
                                "source_protocol_codes": "B",
                                "source_protocol": "bgp",
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "172.23.36.198",
                                            "updated": "1w5d",
                                        }
                                    }
                                },
                            },
                            "10.172.240.14/31": {
                                "route": "10.172.240.14/31",
                                "active": True,
                                "metric": 0,
                                "route_preference": 200,
                                "source_protocol_codes": "B",
                                "source_protocol": "bgp",
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "172.23.36.198",
                                            "updated": "1w5d",
                                        }
                                    }
                                },
                            },
                            "10.172.240.64/27": {
                                "route": "10.172.240.64/27",
                                "active": True,
                                "metric": 0,
                                "route_preference": 200,
                                "source_protocol_codes": "B",
                                "source_protocol": "bgp",
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "172.23.36.198",
                                            "updated": "1w5d",
                                        }
                                    }
                                },
                            },
                            "10.172.240.96/28": {
                                "route": "10.172.240.96/28",
                                "active": True,
                                "metric": 0,
                                "route_preference": 200,
                                "source_protocol_codes": "B",
                                "source_protocol": "bgp",
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "172.23.36.198",
                                            "updated": "1w5d",
                                        }
                                    }
                                },
                            },
                            "10.172.240.128/26": {
                                "route": "10.172.240.128/26",
                                "active": True,
                                "metric": 0,
                                "route_preference": 200,
                                "source_protocol_codes": "B",
                                "source_protocol": "bgp",
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "172.23.36.198",
                                            "updated": "1w5d",
                                        }
                                    }
                                },
                            },
                            "172.16.0.0/16": {
                                "route": "172.16.0.0/16",
                                "active": True,
                                "metric": 0,
                                "route_preference": 1,
                                "source_protocol_codes": "S",
                                "source_protocol": "static",
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "10.100.11.20",
                                            "updated": "36w5d",
                                        }
                                    }
                                },
                            },
                            "172.16.2.208/28": {
                                "route": "172.16.2.208/28",
                                "active": True,
                                "metric": 0,
                                "route_preference": 200,
                                "source_protocol_codes": "B",
                                "source_protocol": "bgp",
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "172.23.6.198",
                                            "updated": "5d13h",
                                        }
                                    }
                                },
                            },
                            "172.16.3.0/24": {
                                "route": "172.16.3.0/24",
                                "active": True,
                                "metric": 0,
                                "route_preference": 200,
                                "source_protocol_codes": "B",
                                "source_protocol": "bgp",
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "172.23.6.198",
                                            "updated": "5d13h",
                                        }
                                    }
                                },
                            },
                            "172.16.4.0/23": {
                                "route": "172.16.4.0/23",
                                "active": True,
                                "metric": 0,
                                "route_preference": 200,
                                "source_protocol_codes": "B",
                                "source_protocol": "bgp",
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "172.23.6.198",
                                            "updated": "5d13h",
                                        }
                                    }
                                },
                            },
                            "172.16.7.0/24": {
                                "route": "172.16.7.0/24",
                                "active": True,
                                "metric": 0,
                                "route_preference": 200,
                                "source_protocol_codes": "B",
                                "source_protocol": "bgp",
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "172.23.6.198",
                                            "updated": "5d13h",
                                        }
                                    }
                                },
                            },
                            "172.16.8.0/24": {
                                "route": "172.16.8.0/24",
                                "active": True,
                                "metric": 0,
                                "route_preference": 200,
                                "source_protocol_codes": "B",
                                "source_protocol": "bgp",
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "172.23.6.198",
                                            "updated": "5d13h",
                                        }
                                    }
                                },
                            },
                            "172.16.10.0/23": {
                                "route": "172.16.10.0/23",
                                "active": True,
                                "metric": 0,
                                "route_preference": 200,
                                "source_protocol_codes": "B",
                                "source_protocol": "bgp",
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "172.23.6.198",
                                            "updated": "5d13h",
                                        }
                                    }
                                },
                            },
                            "172.16.23.0/24": {
                                "route": "172.16.23.0/24",
                                "active": True,
                                "metric": 0,
                                "route_preference": 200,
                                "source_protocol_codes": "B",
                                "source_protocol": "bgp",
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "172.23.6.198",
                                            "updated": "5d13h",
                                        }
                                    }
                                },
                            },
                            "172.16.24.0/24": {
                                "route": "172.16.24.0/24",
                                "active": True,
                                "metric": 0,
                                "route_preference": 200,
                                "source_protocol_codes": "B",
                                "source_protocol": "bgp",
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "172.23.6.198",
                                            "updated": "5d13h",
                                        }
                                    }
                                },
                            },
                            "172.16.24.48/28": {
                                "route": "172.16.24.48/28",
                                "active": True,
                                "metric": 0,
                                "route_preference": 200,
                                "source_protocol_codes": "B",
                                "source_protocol": "bgp",
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "172.23.6.198",
                                            "updated": "5d13h",
                                        }
                                    }
                                },
                            },
                            "172.16.25.0/24": {
                                "route": "172.16.25.0/24",
                                "active": True,
                                "metric": 0,
                                "route_preference": 200,
                                "source_protocol_codes": "B",
                                "source_protocol": "bgp",
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "172.23.6.198",
                                            "updated": "5d13h",
                                        }
                                    }
                                },
                            },
                            "172.16.26.0/24": {
                                "route": "172.16.26.0/24",
                                "active": True,
                                "metric": 0,
                                "route_preference": 200,
                                "source_protocol_codes": "B",
                                "source_protocol": "bgp",
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "172.23.6.198",
                                            "updated": "5d13h",
                                        }
                                    }
                                },
                            },
                            "172.16.27.0/24": {
                                "route": "172.16.27.0/24",
                                "active": True,
                                "metric": 0,
                                "route_preference": 200,
                                "source_protocol_codes": "B",
                                "source_protocol": "bgp",
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "172.23.6.198",
                                            "updated": "5d13h",
                                        }
                                    }
                                },
                            },
                            "172.16.29.0/24": {
                                "route": "172.16.29.0/24",
                                "active": True,
                                "metric": 0,
                                "route_preference": 200,
                                "source_protocol_codes": "B",
                                "source_protocol": "bgp",
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "172.23.6.198",
                                            "updated": "5d13h",
                                        }
                                    }
                                },
                            },
                            "172.16.47.0/24": {
                                "route": "172.16.47.0/24",
                                "active": True,
                                "metric": 0,
                                "route_preference": 1,
                                "source_protocol_codes": "S",
                                "source_protocol": "static",
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "10.100.11.20",
                                            "updated": "36w5d",
                                        }
                                    }
                                },
                            },
                            "172.16.50.0/24": {
                                "route": "172.16.50.0/24",
                                "active": True,
                                "metric": 0,
                                "route_preference": 200,
                                "source_protocol_codes": "B",
                                "source_protocol": "bgp",
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "172.23.6.198",
                                            "updated": "5d13h",
                                        }
                                    }
                                },
                            },
                            "172.16.51.0/24": {
                                "route": "172.16.51.0/24",
                                "active": True,
                                "metric": 0,
                                "route_preference": 200,
                                "source_protocol_codes": "B",
                                "source_protocol": "bgp",
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "172.23.6.198",
                                            "updated": "5d13h",
                                        }
                                    }
                                },
                            },
                            "172.16.52.0/24": {
                                "route": "172.16.52.0/24",
                                "active": True,
                                "metric": 0,
                                "route_preference": 200,
                                "source_protocol_codes": "B",
                                "source_protocol": "bgp",
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "172.23.6.198",
                                            "updated": "5d13h",
                                        }
                                    }
                                },
                            },
                            "172.16.53.0/25": {
                                "route": "172.16.53.0/25",
                                "active": True,
                                "metric": 0,
                                "route_preference": 200,
                                "source_protocol_codes": "B",
                                "source_protocol": "bgp",
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "172.23.6.198",
                                            "updated": "5d13h",
                                        }
                                    }
                                },
                            },
                            "172.16.60.0/22": {
                                "route": "172.16.60.0/22",
                                "active": True,
                                "metric": 0,
                                "route_preference": 200,
                                "source_protocol_codes": "B",
                                "source_protocol": "bgp",
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "172.23.8.199",
                                            "updated": "5d14h",
                                        }
                                    }
                                },
                            },
                            "172.16.67.0/24": {
                                "route": "172.16.67.0/24",
                                "active": True,
                                "metric": 0,
                                "route_preference": 200,
                                "source_protocol_codes": "B",
                                "source_protocol": "bgp",
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "172.23.8.199",
                                            "updated": "5d14h",
                                        }
                                    }
                                },
                            },
                            "172.16.68.0/23": {
                                "route": "172.16.68.0/23",
                                "active": True,
                                "metric": 0,
                                "route_preference": 200,
                                "source_protocol_codes": "B",
                                "source_protocol": "bgp",
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "172.23.8.199",
                                            "updated": "5d14h",
                                        }
                                    }
                                },
                            },
                            "172.16.71.0/24": {
                                "route": "172.16.71.0/24",
                                "active": True,
                                "metric": 0,
                                "route_preference": 200,
                                "source_protocol_codes": "B",
                                "source_protocol": "bgp",
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "172.23.8.199",
                                            "updated": "5d14h",
                                        }
                                    }
                                },
                            },
                            "172.16.72.0/24": {
                                "route": "172.16.72.0/24",
                                "active": True,
                                "metric": 0,
                                "route_preference": 200,
                                "source_protocol_codes": "B",
                                "source_protocol": "bgp",
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "172.23.8.199",
                                            "updated": "5d14h",
                                        }
                                    }
                                },
                            },
                            "172.16.87.0/24": {
                                "route": "172.16.87.0/24",
                                "active": True,
                                "metric": 0,
                                "route_preference": 200,
                                "source_protocol_codes": "B",
                                "source_protocol": "bgp",
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "172.23.8.199",
                                            "updated": "5d14h",
                                        }
                                    }
                                },
                            },
                            "172.16.88.0/24": {
                                "route": "172.16.88.0/24",
                                "active": True,
                                "metric": 0,
                                "route_preference": 200,
                                "source_protocol_codes": "B",
                                "source_protocol": "bgp",
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "172.23.8.199",
                                            "updated": "5d14h",
                                        }
                                    }
                                },
                            },
                            "172.16.90.0/24": {
                                "route": "172.16.90.0/24",
                                "active": True,
                                "metric": 0,
                                "route_preference": 200,
                                "source_protocol_codes": "B",
                                "source_protocol": "bgp",
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "172.23.8.199",
                                            "updated": "5d14h",
                                        }
                                    }
                                },
                            },
                            "172.16.92.0/24": {
                                "route": "172.16.92.0/24",
                                "active": True,
                                "metric": 0,
                                "route_preference": 200,
                                "source_protocol_codes": "B",
                                "source_protocol": "bgp",
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "172.23.8.199",
                                            "updated": "5d14h",
                                        }
                                    }
                                },
                            },
                            "172.16.188.0/22": {
                                "route": "172.16.188.0/22",
                                "active": True,
                                "metric": 0,
                                "route_preference": 200,
                                "source_protocol_codes": "B",
                                "source_protocol": "bgp",
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "172.23.6.198",
                                            "updated": "5d13h",
                                        }
                                    }
                                },
                            },
                            "172.16.224.0/24": {
                                "route": "172.16.224.0/24",
                                "active": True,
                                "metric": 0,
                                "route_preference": 200,
                                "source_protocol_codes": "B",
                                "source_protocol": "bgp",
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "172.23.8.199",
                                            "updated": "5d14h",
                                        }
                                    }
                                },
                            },
                            "172.16.225.0/24": {
                                "route": "172.16.225.0/24",
                                "active": True,
                                "metric": 0,
                                "route_preference": 200,
                                "source_protocol_codes": "B",
                                "source_protocol": "bgp",
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "172.23.8.199",
                                            "updated": "5d14h",
                                        }
                                    }
                                },
                            },
                            "172.16.226.0/24": {
                                "route": "172.16.226.0/24",
                                "active": True,
                                "metric": 0,
                                "route_preference": 200,
                                "source_protocol_codes": "B",
                                "source_protocol": "bgp",
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "172.23.8.199",
                                            "updated": "5d14h",
                                        }
                                    }
                                },
                            },
                            "172.16.232.0/24": {
                                "route": "172.16.232.0/24",
                                "active": True,
                                "metric": 0,
                                "route_preference": 200,
                                "source_protocol_codes": "B",
                                "source_protocol": "bgp",
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "172.23.6.198",
                                            "updated": "5d13h",
                                        }
                                    }
                                },
                            },
                            "172.16.233.0/24": {
                                "route": "172.16.233.0/24",
                                "active": True,
                                "metric": 0,
                                "route_preference": 200,
                                "source_protocol_codes": "B",
                                "source_protocol": "bgp",
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "172.23.6.198",
                                            "updated": "5d13h",
                                        }
                                    }
                                },
                            },
                            "172.16.234.0/24": {
                                "route": "172.16.234.0/24",
                                "active": True,
                                "metric": 0,
                                "route_preference": 200,
                                "source_protocol_codes": "B",
                                "source_protocol": "bgp",
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "172.23.6.198",
                                            "updated": "5d13h",
                                        }
                                    }
                                },
                            },
                            "172.16.240.0/24": {
                                "route": "172.16.240.0/24",
                                "active": True,
                                "metric": 0,
                                "route_preference": 20,
                                "source_protocol_codes": "B",
                                "source_protocol": "bgp",
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "10.100.11.1",
                                            "updated": "5d13h",
                                        }
                                    }
                                },
                            },
                            "172.16.241.0/24": {
                                "route": "172.16.241.0/24",
                                "active": True,
                                "metric": 0,
                                "route_preference": 20,
                                "source_protocol_codes": "B",
                                "source_protocol": "bgp",
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "10.100.11.1",
                                            "updated": "5d13h",
                                        }
                                    }
                                },
                            },
                            "172.16.242.0/24": {
                                "route": "172.16.242.0/24",
                                "active": True,
                                "metric": 0,
                                "route_preference": 20,
                                "source_protocol_codes": "B",
                                "source_protocol": "bgp",
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "10.100.11.1",
                                            "updated": "5d13h",
                                        }
                                    }
                                },
                            },
                            "172.16.247.0/24": {
                                "route": "172.16.247.0/24",
                                "active": True,
                                "metric": 0,
                                "route_preference": 20,
                                "source_protocol_codes": "B",
                                "source_protocol": "bgp",
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "10.100.11.1",
                                            "updated": "5d13h",
                                        }
                                    }
                                },
                            },
                            "172.16.250.16/28": {
                                "route": "172.16.250.16/28",
                                "active": True,
                                "metric": 0,
                                "route_preference": 20,
                                "source_protocol_codes": "B",
                                "source_protocol": "bgp",
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "10.100.11.1",
                                            "updated": "5d13h",
                                        }
                                    }
                                },
                            },
                            "172.16.250.128/28": {
                                "route": "172.16.250.128/28",
                                "active": True,
                                "metric": 0,
                                "route_preference": 20,
                                "source_protocol_codes": "B",
                                "source_protocol": "bgp",
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "10.100.11.1",
                                            "updated": "5d13h",
                                        }
                                    }
                                },
                            },
                            "172.16.250.244/30": {
                                "route": "172.16.250.244/30",
                                "active": True,
                                "metric": 0,
                                "route_preference": 20,
                                "source_protocol_codes": "B",
                                "source_protocol": "bgp",
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "10.100.11.1",
                                            "updated": "5d13h",
                                        }
                                    }
                                },
                            },
                            "172.16.250.248/29": {
                                "route": "172.16.250.248/29",
                                "active": True,
                                "metric": 0,
                                "route_preference": 20,
                                "source_protocol_codes": "B",
                                "source_protocol": "bgp",
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "10.100.11.1",
                                            "updated": "5d13h",
                                        }
                                    }
                                },
                            },
                            "172.18.3.0/24": {
                                "route": "172.18.3.0/24",
                                "active": True,
                                "metric": 0,
                                "route_preference": 200,
                                "source_protocol_codes": "B",
                                "source_protocol": "bgp",
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "172.23.36.198",
                                            "updated": "1w5d",
                                        }
                                    }
                                },
                            },
                            "172.18.4.0/23": {
                                "route": "172.18.4.0/23",
                                "active": True,
                                "metric": 0,
                                "route_preference": 200,
                                "source_protocol_codes": "B",
                                "source_protocol": "bgp",
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "172.23.36.198",
                                            "updated": "1w5d",
                                        }
                                    }
                                },
                            },
                            "172.18.6.0/23": {
                                "route": "172.18.6.0/23",
                                "active": True,
                                "metric": 0,
                                "route_preference": 200,
                                "source_protocol_codes": "B",
                                "source_protocol": "bgp",
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "172.23.36.198",
                                            "updated": "1w5d",
                                        }
                                    }
                                },
                            },
                            "172.18.8.0/23": {
                                "route": "172.18.8.0/23",
                                "active": True,
                                "metric": 0,
                                "route_preference": 200,
                                "source_protocol_codes": "B",
                                "source_protocol": "bgp",
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "172.23.36.198",
                                            "updated": "1w5d",
                                        }
                                    }
                                },
                            },
                            "172.18.10.0/23": {
                                "route": "172.18.10.0/23",
                                "active": True,
                                "metric": 0,
                                "route_preference": 200,
                                "source_protocol_codes": "B",
                                "source_protocol": "bgp",
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "172.23.36.198",
                                            "updated": "1w5d",
                                        }
                                    }
                                },
                            },
                            "172.18.23.0/27": {
                                "route": "172.18.23.0/27",
                                "active": True,
                                "metric": 0,
                                "route_preference": 200,
                                "source_protocol_codes": "B",
                                "source_protocol": "bgp",
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "172.23.36.198",
                                            "updated": "1w5d",
                                        }
                                    }
                                },
                            },
                            "172.18.33.0/24": {
                                "route": "172.18.33.0/24",
                                "active": True,
                                "metric": 0,
                                "route_preference": 200,
                                "source_protocol_codes": "B",
                                "source_protocol": "bgp",
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "172.23.36.198",
                                            "updated": "1w5d",
                                        }
                                    }
                                },
                            },
                            "172.18.41.0/24": {
                                "route": "172.18.41.0/24",
                                "active": True,
                                "metric": 0,
                                "route_preference": 200,
                                "source_protocol_codes": "B",
                                "source_protocol": "bgp",
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "172.23.40.199",
                                            "updated": "5w1d",
                                        }
                                    }
                                },
                            },
                            "172.18.48.48/28": {
                                "route": "172.18.48.48/28",
                                "active": True,
                                "metric": 0,
                                "route_preference": 200,
                                "source_protocol_codes": "B",
                                "source_protocol": "bgp",
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "172.23.36.198",
                                            "updated": "1w5d",
                                        }
                                    }
                                },
                            },
                            "172.18.48.64/28": {
                                "route": "172.18.48.64/28",
                                "active": True,
                                "metric": 0,
                                "route_preference": 200,
                                "source_protocol_codes": "B",
                                "source_protocol": "bgp",
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "172.23.36.198",
                                            "updated": "1w5d",
                                        }
                                    }
                                },
                            },
                            "172.18.48.120/30": {
                                "route": "172.18.48.120/30",
                                "active": True,
                                "metric": 0,
                                "route_preference": 200,
                                "source_protocol_codes": "B",
                                "source_protocol": "bgp",
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "172.23.36.198",
                                            "updated": "1w5d",
                                        }
                                    }
                                },
                            },
                            "172.18.50.0/24": {
                                "route": "172.18.50.0/24",
                                "active": True,
                                "metric": 0,
                                "route_preference": 200,
                                "source_protocol_codes": "B",
                                "source_protocol": "bgp",
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "172.23.36.198",
                                            "updated": "1w5d",
                                        }
                                    }
                                },
                            },
                            "172.18.105.0/24": {
                                "route": "172.18.105.0/24",
                                "active": True,
                                "metric": 0,
                                "route_preference": 200,
                                "source_protocol_codes": "B",
                                "source_protocol": "bgp",
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "172.23.36.198",
                                            "updated": "1w5d",
                                        }
                                    }
                                },
                            },
                            "172.18.109.0/24": {
                                "route": "172.18.109.0/24",
                                "active": True,
                                "metric": 0,
                                "route_preference": 200,
                                "source_protocol_codes": "B",
                                "source_protocol": "bgp",
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "172.23.36.198",
                                            "updated": "1w5d",
                                        }
                                    }
                                },
                            },
                            "172.18.160.0/20": {
                                "route": "172.18.160.0/20",
                                "active": True,
                                "metric": 0,
                                "route_preference": 200,
                                "source_protocol_codes": "B",
                                "source_protocol": "bgp",
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "172.23.40.199",
                                            "updated": "5w1d",
                                        }
                                    }
                                },
                            },
                            "172.18.160.48/28": {
                                "route": "172.18.160.48/28",
                                "active": True,
                                "metric": 0,
                                "route_preference": 200,
                                "source_protocol_codes": "B",
                                "source_protocol": "bgp",
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "172.23.40.199",
                                            "updated": "5w1d",
                                        }
                                    }
                                },
                            },
                            "172.18.161.0/24": {
                                "route": "172.18.161.0/24",
                                "active": True,
                                "metric": 0,
                                "route_preference": 200,
                                "source_protocol_codes": "B",
                                "source_protocol": "bgp",
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "172.23.40.199",
                                            "updated": "5w1d",
                                        }
                                    }
                                },
                            },
                            "172.18.169.0/24": {
                                "route": "172.18.169.0/24",
                                "active": True,
                                "metric": 0,
                                "route_preference": 200,
                                "source_protocol_codes": "B",
                                "source_protocol": "bgp",
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "172.23.40.199",
                                            "updated": "5w1d",
                                        }
                                    }
                                },
                            },
                            "172.18.169.224/28": {
                                "route": "172.18.169.224/28",
                                "active": True,
                                "metric": 0,
                                "route_preference": 200,
                                "source_protocol_codes": "B",
                                "source_protocol": "bgp",
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "172.23.40.199",
                                            "updated": "5w1d",
                                        }
                                    }
                                },
                            },
                            "172.18.173.0/24": {
                                "route": "172.18.173.0/24",
                                "active": True,
                                "metric": 0,
                                "route_preference": 200,
                                "source_protocol_codes": "B",
                                "source_protocol": "bgp",
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "172.23.40.199",
                                            "updated": "5w1d",
                                        }
                                    }
                                },
                            },
                            "172.18.224.0/24": {
                                "route": "172.18.224.0/24",
                                "active": True,
                                "metric": 0,
                                "route_preference": 200,
                                "source_protocol_codes": "B",
                                "source_protocol": "bgp",
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "172.23.36.198",
                                            "updated": "1w5d",
                                        }
                                    }
                                },
                            },
                            "172.18.225.0/24": {
                                "route": "172.18.225.0/24",
                                "active": True,
                                "metric": 0,
                                "route_preference": 200,
                                "source_protocol_codes": "B",
                                "source_protocol": "bgp",
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "172.23.36.198",
                                            "updated": "1w5d",
                                        }
                                    }
                                },
                            },
                            "172.18.226.0/24": {
                                "route": "172.18.226.0/24",
                                "active": True,
                                "metric": 0,
                                "route_preference": 200,
                                "source_protocol_codes": "B",
                                "source_protocol": "bgp",
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "172.23.36.198",
                                            "updated": "1w5d",
                                        }
                                    }
                                },
                            },
                            "172.18.227.0/24": {
                                "route": "172.18.227.0/24",
                                "active": True,
                                "metric": 0,
                                "route_preference": 200,
                                "source_protocol_codes": "B",
                                "source_protocol": "bgp",
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "172.23.36.198",
                                            "updated": "1w5d",
                                        }
                                    }
                                },
                            },
                            "172.18.232.0/24": {
                                "route": "172.18.232.0/24",
                                "active": True,
                                "metric": 0,
                                "route_preference": 200,
                                "source_protocol_codes": "B",
                                "source_protocol": "bgp",
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "172.23.40.199",
                                            "updated": "5w1d",
                                        }
                                    }
                                },
                            },
                            "172.18.233.0/24": {
                                "route": "172.18.233.0/24",
                                "active": True,
                                "metric": 0,
                                "route_preference": 200,
                                "source_protocol_codes": "B",
                                "source_protocol": "bgp",
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "172.23.40.199",
                                            "updated": "5w1d",
                                        }
                                    }
                                },
                            },
                            "172.18.234.0/24": {
                                "route": "172.18.234.0/24",
                                "active": True,
                                "metric": 0,
                                "route_preference": 200,
                                "source_protocol_codes": "B",
                                "source_protocol": "bgp",
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "172.23.40.199",
                                            "updated": "5w1d",
                                        }
                                    }
                                },
                            },
                            "172.18.235.0/24": {
                                "route": "172.18.235.0/24",
                                "active": True,
                                "metric": 0,
                                "route_preference": 200,
                                "source_protocol_codes": "B",
                                "source_protocol": "bgp",
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "172.23.40.199",
                                            "updated": "5w1d",
                                        }
                                    }
                                },
                            },
                            "172.18.252.0/30": {
                                "route": "172.18.252.0/30",
                                "active": True,
                                "metric": 0,
                                "route_preference": 200,
                                "source_protocol_codes": "B",
                                "source_protocol": "bgp",
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "172.23.36.198",
                                            "updated": "1w5d",
                                        }
                                    }
                                },
                            },
                            "172.18.252.4/30": {
                                "route": "172.18.252.4/30",
                                "active": True,
                                "metric": 0,
                                "route_preference": 200,
                                "source_protocol_codes": "B",
                                "source_protocol": "bgp",
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "172.23.36.198",
                                            "updated": "1w5d",
                                        }
                                    }
                                },
                            },
                            "172.18.252.16/28": {
                                "route": "172.18.252.16/28",
                                "active": True,
                                "metric": 0,
                                "route_preference": 200,
                                "source_protocol_codes": "B",
                                "source_protocol": "bgp",
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "172.23.36.198",
                                            "updated": "1w5d",
                                        }
                                    }
                                },
                            },
                            "172.18.252.32/29": {
                                "route": "172.18.252.32/29",
                                "active": True,
                                "metric": 0,
                                "route_preference": 200,
                                "source_protocol_codes": "B",
                                "source_protocol": "bgp",
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "172.23.36.198",
                                            "updated": "1w5d",
                                        }
                                    }
                                },
                            },
                            "172.18.252.48/28": {
                                "route": "172.18.252.48/28",
                                "active": True,
                                "metric": 0,
                                "route_preference": 200,
                                "source_protocol_codes": "B",
                                "source_protocol": "bgp",
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "172.23.36.198",
                                            "updated": "1w5d",
                                        }
                                    }
                                },
                            },
                            "172.18.252.64/28": {
                                "route": "172.18.252.64/28",
                                "active": True,
                                "metric": 0,
                                "route_preference": 200,
                                "source_protocol_codes": "B",
                                "source_protocol": "bgp",
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "172.23.36.198",
                                            "updated": "1w5d",
                                        }
                                    }
                                },
                            },
                            "172.18.252.80/28": {
                                "route": "172.18.252.80/28",
                                "active": True,
                                "metric": 0,
                                "route_preference": 200,
                                "source_protocol_codes": "B",
                                "source_protocol": "bgp",
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "172.23.36.198",
                                            "updated": "1w5d",
                                        }
                                    }
                                },
                            },
                            "172.18.252.252/30": {
                                "route": "172.18.252.252/30",
                                "active": True,
                                "metric": 0,
                                "route_preference": 200,
                                "source_protocol_codes": "B",
                                "source_protocol": "bgp",
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "172.23.36.198",
                                            "updated": "1w5d",
                                        }
                                    }
                                },
                            },
                            "172.18.253.0/30": {
                                "route": "172.18.253.0/30",
                                "active": True,
                                "metric": 0,
                                "route_preference": 200,
                                "source_protocol_codes": "B",
                                "source_protocol": "bgp",
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "172.23.40.199",
                                            "updated": "5w1d",
                                        }
                                    }
                                },
                            },
                            "172.18.253.4/30": {
                                "route": "172.18.253.4/30",
                                "active": True,
                                "metric": 0,
                                "route_preference": 200,
                                "source_protocol_codes": "B",
                                "source_protocol": "bgp",
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "172.23.40.199",
                                            "updated": "5w1d",
                                        }
                                    }
                                },
                            },
                            "172.18.253.16/28": {
                                "route": "172.18.253.16/28",
                                "active": True,
                                "metric": 0,
                                "route_preference": 200,
                                "source_protocol_codes": "B",
                                "source_protocol": "bgp",
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "172.23.40.199",
                                            "updated": "5w1d",
                                        }
                                    }
                                },
                            },
                            "172.18.253.32/29": {
                                "route": "172.18.253.32/29",
                                "active": True,
                                "metric": 0,
                                "route_preference": 200,
                                "source_protocol_codes": "B",
                                "source_protocol": "bgp",
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "172.23.40.199",
                                            "updated": "5w1d",
                                        }
                                    }
                                },
                            },
                            "172.18.253.48/28": {
                                "route": "172.18.253.48/28",
                                "active": True,
                                "metric": 0,
                                "route_preference": 200,
                                "source_protocol_codes": "B",
                                "source_protocol": "bgp",
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "172.23.40.199",
                                            "updated": "5w1d",
                                        }
                                    }
                                },
                            },
                            "172.18.253.252/30": {
                                "route": "172.18.253.252/30",
                                "active": True,
                                "metric": 0,
                                "route_preference": 200,
                                "source_protocol_codes": "B",
                                "source_protocol": "bgp",
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "172.23.40.199",
                                            "updated": "5w1d",
                                        }
                                    }
                                },
                            },
                            "172.22.36.128/27": {
                                "route": "172.22.36.128/27",
                                "active": True,
                                "metric": 0,
                                "route_preference": 200,
                                "source_protocol_codes": "B",
                                "source_protocol": "bgp",
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "172.23.36.198",
                                            "updated": "1w5d",
                                        }
                                    }
                                },
                            },
                            "172.22.36.145/32": {
                                "route": "172.22.36.145/32",
                                "active": True,
                                "metric": 0,
                                "route_preference": 200,
                                "source_protocol_codes": "B",
                                "source_protocol": "bgp",
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "172.23.36.198",
                                            "updated": "1w5d",
                                        }
                                    }
                                },
                            },
                            "172.22.36.146/32": {
                                "route": "172.22.36.146/32",
                                "active": True,
                                "metric": 0,
                                "route_preference": 200,
                                "source_protocol_codes": "B",
                                "source_protocol": "bgp",
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "172.23.36.198",
                                            "updated": "1w5d",
                                        }
                                    }
                                },
                            },
                            "172.22.36.210/32": {
                                "route": "172.22.36.210/32",
                                "active": True,
                                "metric": 0,
                                "route_preference": 200,
                                "source_protocol_codes": "B",
                                "source_protocol": "bgp",
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "172.23.36.198",
                                            "updated": "1w5d",
                                        }
                                    }
                                },
                            },
                            "172.22.36.211/32": {
                                "route": "172.22.36.211/32",
                                "active": True,
                                "metric": 0,
                                "route_preference": 200,
                                "source_protocol_codes": "B",
                                "source_protocol": "bgp",
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "172.23.36.198",
                                            "updated": "1w5d",
                                        }
                                    }
                                },
                            },
                            "172.22.40.128/27": {
                                "route": "172.22.40.128/27",
                                "active": True,
                                "metric": 0,
                                "route_preference": 200,
                                "source_protocol_codes": "B",
                                "source_protocol": "bgp",
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "172.23.40.199",
                                            "updated": "5w1d",
                                        }
                                    }
                                },
                            },
                            "172.22.40.145/32": {
                                "route": "172.22.40.145/32",
                                "active": True,
                                "metric": 0,
                                "route_preference": 200,
                                "source_protocol_codes": "B",
                                "source_protocol": "bgp",
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "172.23.40.199",
                                            "updated": "5w1d",
                                        }
                                    }
                                },
                            },
                            "172.22.40.146/32": {
                                "route": "172.22.40.146/32",
                                "active": True,
                                "metric": 0,
                                "route_preference": 200,
                                "source_protocol_codes": "B",
                                "source_protocol": "bgp",
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "172.23.40.199",
                                            "updated": "5w1d",
                                        }
                                    }
                                },
                            },
                            "172.22.40.210/32": {
                                "route": "172.22.40.210/32",
                                "active": True,
                                "metric": 0,
                                "route_preference": 200,
                                "source_protocol_codes": "B",
                                "source_protocol": "bgp",
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "172.23.40.199",
                                            "updated": "5w1d",
                                        }
                                    }
                                },
                            },
                            "172.22.40.211/32": {
                                "route": "172.22.40.211/32",
                                "active": True,
                                "metric": 0,
                                "route_preference": 200,
                                "source_protocol_codes": "B",
                                "source_protocol": "bgp",
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "172.23.40.199",
                                            "updated": "5w1d",
                                        }
                                    }
                                },
                            },
                            "172.22.46.0/25": {
                                "route": "172.22.46.0/25",
                                "active": True,
                                "metric": 0,
                                "route_preference": 200,
                                "source_protocol_codes": "B",
                                "source_protocol": "bgp",
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "172.23.36.198",
                                            "updated": "1w5d",
                                        }
                                    }
                                },
                            },
                            "172.22.46.128/27": {
                                "route": "172.22.46.128/27",
                                "active": True,
                                "metric": 0,
                                "route_preference": 200,
                                "source_protocol_codes": "B",
                                "source_protocol": "bgp",
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "172.23.36.198",
                                            "updated": "1w5d",
                                        }
                                    }
                                },
                            },
                            "172.22.46.191/32": {
                                "route": "172.22.46.191/32",
                                "active": True,
                                "metric": 0,
                                "route_preference": 200,
                                "source_protocol_codes": "B",
                                "source_protocol": "bgp",
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "172.23.36.198",
                                            "updated": "1w5d",
                                        }
                                    }
                                },
                            },
                            "172.22.46.210/32": {
                                "route": "172.22.46.210/32",
                                "active": True,
                                "metric": 0,
                                "route_preference": 200,
                                "source_protocol_codes": "B",
                                "source_protocol": "bgp",
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "172.23.36.198",
                                            "updated": "1w5d",
                                        }
                                    }
                                },
                            },
                            "172.22.46.211/32": {
                                "route": "172.22.46.211/32",
                                "active": True,
                                "metric": 0,
                                "route_preference": 200,
                                "source_protocol_codes": "B",
                                "source_protocol": "bgp",
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "172.23.36.198",
                                            "updated": "1w5d",
                                        }
                                    }
                                },
                            },
                            "172.22.47.0/32": {
                                "route": "172.22.47.0/32",
                                "active": True,
                                "metric": 0,
                                "route_preference": 200,
                                "source_protocol_codes": "B",
                                "source_protocol": "bgp",
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "172.23.36.198",
                                            "updated": "1w5d",
                                        }
                                    }
                                },
                            },
                            "172.22.47.1/32": {
                                "route": "172.22.47.1/32",
                                "active": True,
                                "metric": 0,
                                "route_preference": 200,
                                "source_protocol_codes": "B",
                                "source_protocol": "bgp",
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "172.23.36.198",
                                            "updated": "1w5d",
                                        }
                                    }
                                },
                            },
                        }
                    }
                }
            }
        }
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


    def test_show_route_ipv4_3_with_vrf(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_3_with_vrf)
        obj = ShowRouteIpv4(device=self.device)
        parsed_output = obj.parse(vrf='gsn2')
        self.assertEqual(parsed_output, self.golden_parsed_output_3_with_vrf)


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