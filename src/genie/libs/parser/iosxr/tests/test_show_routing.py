import unittest

from unittest.mock import Mock

# ATS
from pyats.topology import Device

from genie.metaparser.util.exceptions import SchemaEmptyParserError, \
    SchemaMissingKeyError

from genie.libs.parser.iosxr.show_routing import (ShowRouteIpv4,
                                                  ShowRouteIpv6)


# ============================================
# unit test for 'show route ipv4'
# =============================================
class TestShowRouteIpv4(unittest.TestCase):
    """
       unit test for show route ipv4
    """
    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    # show route ipv4
    golden_output_1 = {'execute.return_value': '''

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
        'vrf': {
            'default': {
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
                'last_resort': {
                    'gateway': 'not set'
                },
            },
        },
    }

    # show route ipv4
    golden_output_2 = {'execute.return_value': '''

        Fri Sep 27 17:00:03.303 EDT

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

        i L2 10.4.1.32/32 [115/100030] via 10.16.2.3, 1d06h, HundredGigE0/0/1/1 (!)
                             [115/100020] via 10.16.2.1, 1d06h, Bundle-Ether1
        i L2 10.4.1.33/32 [115/100030] via 10.16.2.3, 1d06h, HundredGigE0/0/1/1 (!)
                             [115/100020] via 10.16.2.1, 1d06h, Bundle-Ether1
        i L2 10.4.1.34/32 [115/100030] via 10.16.2.3, 1d06h, HundredGigE0/0/1/1 (!)
                             [115/100020] via 10.16.2.1, 1d06h, Bundle-Ether1
    '''
                       }
    golden_parsed_output_2 = {
        "vrf": {
            "default": {
                "address_family": {
                    "ipv4": {
                        "routes": {
                            "10.4.1.32/32": {
                                "route": "10.4.1.32/32",
                                "active": True,
                                "metric": 100020,
                                "route_preference": 115,
                                "source_protocol_codes": "i L2 (!)",
                                "source_protocol": "isis",
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "10.16.2.3",
                                            "updated": "1d06h",
                                            "outgoing_interface": "HundredGigE0/0/1/1"
                                        },
                                        2: {
                                            "index": 2,
                                            "next_hop": "10.16.2.1",
                                            "updated": "1d06h",
                                            "outgoing_interface": "Bundle-Ether1"
                                        }
                                    }
                                }
                            },
                            "10.4.1.33/32": {
                                "route": "10.4.1.33/32",
                                "active": True,
                                "metric": 100020,
                                "route_preference": 115,
                                "source_protocol_codes": "i L2 (!)",
                                "source_protocol": "isis",
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "10.16.2.3",
                                            "updated": "1d06h",
                                            "outgoing_interface": "HundredGigE0/0/1/1"
                                        },
                                        2: {
                                            "index": 2,
                                            "next_hop": "10.16.2.1",
                                            "updated": "1d06h",
                                            "outgoing_interface": "Bundle-Ether1"
                                        }
                                    }
                                }
                            },
                            "10.4.1.34/32": {
                                "route": "10.4.1.34/32",
                                "active": True,
                                "metric": 100020,
                                "route_preference": 115,
                                "source_protocol_codes": "i L2 (!)",
                                "source_protocol": "isis",
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "10.16.2.3",
                                            "updated": "1d06h",
                                            "outgoing_interface": "HundredGigE0/0/1/1"
                                        },
                                        2: {
                                            "index": 2,
                                            "next_hop": "10.16.2.1",
                                            "updated": "1d06h",
                                            "outgoing_interface": "Bundle-Ether1"
                                        }
                                    }
                                }
                            }
                        }
                    }
                },
                'last_resort': {
                    'gateway': 'not set'
                },
            }
        }
    }

    # show route vrf all ipv4
    golden_output_2_with_vrf = {'execute.return_value': '''

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
                'last_resort': {
                    'gateway': 'not set'
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
                'last_resort': {
                    'gateway': 'not set'
                },
            },
        },
    }

    # show route vrf VRF1 ipv4
    golden_output_3_with_vrf = {'execute.return_value': '''
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

        Gateway of last resort is 192.168.1.1 to network 0.0.0.0

        B*   0.0.0.0/0 [200/0] via 192.168.4.4 (nexthop in vrf default), 08:11:19
        B    192.168.1.2/18 [200/0] via 192.168.4.5 (nexthop in vrf default), 1w5d
        B    192.168.1.3/27 [20/0] via 192.168.4.6, 5d13h
        L    192.168.1.4/32 is directly connected, 36w5d, GigabitEthernet0/0/1/8
        C    192.168.1.5/29 is directly connected, 36w5d, BVI3001
        L    192.168.1.6/32 [0/0] via 192.168.4.7, 36w5d, BVI3001
        L    192.168.1.7/32 is directly connected, 36w5d, BVI3001
    '''}

    golden_parsed_output_3_with_vrf = {
        'vrf': {
            'VRF1': {
                'address_family': {
                    'ipv4': {
                        'routes': {
                            '0.0.0.0/0': {
                                'route': '0.0.0.0/0',
                                'active': True,
                                'route_preference': 200,
                                'metric': 0,
                                'source_protocol': 'bgp',
                                'source_protocol_codes': 'B*',
                                'next_hop': {
                                    'next_hop_list': {
                                        1: {
                                            'index': 1,
                                            'next_hop': '192.168.4.4',
                                            'updated': '08:11:19',
                                        },
                                    },
                                },
                            },
                            '192.168.1.2/18': {
                                'route': '192.168.1.2/18',
                                'active': True,
                                'route_preference': 200,
                                'metric': 0,
                                'source_protocol': 'bgp',
                                'source_protocol_codes': 'B',
                                'next_hop': {
                                    'next_hop_list': {
                                        1: {
                                            'index': 1,
                                            'next_hop': '192.168.4.5',
                                            'updated': '1w5d',
                                        },
                                    },
                                },
                            },
                            '192.168.1.3/27': {
                                'route': '192.168.1.3/27',
                                'active': True,
                                'route_preference': 20,
                                'metric': 0,
                                'source_protocol': 'bgp',
                                'source_protocol_codes': 'B',
                                'next_hop': {
                                    'next_hop_list': {
                                        1: {
                                            'index': 1,
                                            'next_hop': '192.168.4.6',
                                            'updated': '5d13h',
                                        },
                                    },
                                },
                            },
                            '192.168.1.4/32': {
                                'route': '192.168.1.4/32',
                                'active': True,
                                'source_protocol': 'local',
                                'source_protocol_codes': 'L',
                                'next_hop': {
                                    'outgoing_interface': {
                                        'GigabitEthernet0/0/1/8': {
                                            'outgoing_interface': 'GigabitEthernet0/0/1/8',
                                            'updated': '36w5d',
                                        },
                                    },
                                },
                            },
                            '192.168.1.5/29': {
                                'route': '192.168.1.5/29',
                                'active': True,
                                'source_protocol': 'connected',
                                'source_protocol_codes': 'C',
                                'next_hop': {
                                    'outgoing_interface': {
                                        'BVI3001': {
                                            'outgoing_interface': 'BVI3001',
                                            'updated': '36w5d',
                                        },
                                    },
                                },
                            },
                            '192.168.1.6/32': {
                                'route': '192.168.1.6/32',
                                'active': True,
                                'route_preference': 0,
                                'metric': 0,
                                'source_protocol': 'local',
                                'source_protocol_codes': 'L',
                                'next_hop': {
                                    'next_hop_list': {
                                        1: {
                                            'index': 1,
                                            'next_hop': '192.168.4.7',
                                            'outgoing_interface': 'BVI3001',
                                            'updated': '36w5d',
                                        },
                                    },
                                },
                            },
                            '192.168.1.7/32': {
                                'route': '192.168.1.7/32',
                                'active': True,
                                'source_protocol': 'local',
                                'source_protocol_codes': 'L',
                                'next_hop': {
                                    'outgoing_interface': {
                                        'BVI3001': {
                                            'outgoing_interface': 'BVI3001',
                                            'updated': '36w5d',
                                        },
                                    },
                                },
                            },
                        },
                    },
                },
                'last_resort': {
                    'gateway': '192.168.1.1',
                    'to_network': '0.0.0.0'
                },
            },
        },
    }

    device_output = {'execute.return_value': '''
        Codes: C - connected, S - static, R - RIP, B - BGP, (>) - Diversion path
        D - EIGRP, EX - EIGRP external, O - OSPF, IA - OSPF inter area
        N1 - OSPF NSSA external type 1, N2 - OSPF NSSA external type 2
        E1 - OSPF external type 1, E2 - OSPF external type 2, E - EGP
        i - ISIS, L1 - IS-IS level-1, L2 - IS-IS level-2
        ia - IS-IS inter area, su - IS-IS summary null, * - candidate default
        U - per-user static route, o - ODR, L - local, G  - DAGR, l - LISP
        A - access/subscriber, a - Application route
        M - mobile route, r - RPL, t - Traffic Engineering, (!) - FRR Backup path

        Gateway of last resort is 172.16.0.88 to network 0.0.0.0

        O*E2 0.0.0.0/0 [110/1] via 172.16.0.88, 3d00h, Bundle-Ether1
                    [110/1] via 172.16.0.96, 3d00h, Bundle-Ether2
        L    10.4.1.1/32 is directly connected, 5w6d, Loopback100
        O    10.1.1.0/24 [110/66036] via 172.16.0.88, 2d23h, Bundle-Ether1
                        [110/66036] via 172.16.0.96, 2d23h, Bundle-Ether2
        O E2 10.10.10.21/32 [110/1] via 172.16.0.88, 3d04h, Bundle-Ether1
        L    10.10.10.255/32 is directly connected, 5w6d, Loopback2112
    '''}

    expected_output = {
        'vrf': {
            'default': {
                'address_family': {
                    'ipv4': {
                        'routes': {
                            '0.0.0.0/0': {
                                'active': True,
                                'metric': 1,
                                'next_hop': {
                                    'next_hop_list': {
                                        1: {
                                            'index': 1,
                                            'next_hop': '172.16.0.88',
                                            'outgoing_interface': 'Bundle-Ether1',
                                            'updated': '3d00h',
                                        },
                                        2: {
                                            'index': 2,
                                            'next_hop': '172.16.0.96',
                                            'outgoing_interface': 'Bundle-Ether2',
                                            'updated': '3d00h',
                                        },
                                    },
                                },
                                'route': '0.0.0.0/0',
                                'route_preference': 110,
                                'source_protocol': 'ospf',
                                'source_protocol_codes': 'O* E2',
                            },
                            '10.4.1.1/32': {
                                'active': True,
                                'next_hop': {
                                    'outgoing_interface': {
                                        'Loopback100': {
                                            'outgoing_interface': 'Loopback100',
                                            'updated': '5w6d',
                                        },
                                    },
                                },
                                'route': '10.4.1.1/32',
                                'source_protocol': 'local',
                                'source_protocol_codes': 'L',
                            },
                            '10.1.1.0/24': {
                                'active': True,
                                'metric': 66036,
                                'next_hop': {
                                    'next_hop_list': {
                                        1: {
                                            'index': 1,
                                            'next_hop': '172.16.0.88',
                                            'outgoing_interface': 'Bundle-Ether1',
                                            'updated': '2d23h',
                                        },
                                        2: {
                                            'index': 2,
                                            'next_hop': '172.16.0.96',
                                            'outgoing_interface': 'Bundle-Ether2',
                                            'updated': '2d23h',
                                        },
                                    },
                                },
                                'route': '10.1.1.0/24',
                                'route_preference': 110,
                                'source_protocol': 'ospf',
                                'source_protocol_codes': 'O',
                            },
                            '10.10.10.21/32': {
                                'active': True,
                                'metric': 1,
                                'next_hop': {
                                    'next_hop_list': {
                                        1: {
                                            'index': 1,
                                            'next_hop': '172.16.0.88',
                                            'outgoing_interface': 'Bundle-Ether1',
                                            'updated': '3d04h',
                                        },
                                    },
                                },
                                'route': '10.10.10.21/32',
                                'route_preference': 110,
                                'source_protocol': 'ospf',
                                'source_protocol_codes': 'O E2',
                            },
                            '10.10.10.255/32': {
                                'active': True,
                                'next_hop': {
                                    'outgoing_interface': {
                                        'Loopback2112': {
                                            'outgoing_interface': 'Loopback2112',
                                            'updated': '5w6d',
                                        },
                                    },
                                },
                                'route': '10.10.10.255/32',
                                'source_protocol': 'local',
                                'source_protocol_codes': 'L',
                            },
                        },
                    },
                },
                'last_resort': {
                    'gateway': '172.16.0.88',
                    'to_network': '0.0.0.0'
                },
            },
        },
    }

    # show route ipv4 10.23.90.0/24
    golden_output_5 = {'execute.return_value': '''
        Tue Oct 29 21:03:37.089 UTC

        Routing entry for 10.23.90.0/24
        Known via "connected", distance 0, metric 0 (connected)
        Installed Oct  4 15:47:45.390 for 3w4d
        Routing Descriptor Blocks
            directly connected, via GigabitEthernet0/0/0/1.90
            Route metric is 0
        Redist Advertisers:
            eigrp/100 (protoid=5, clientid=22)
    '''}

    golden_parsed_output_5 = {
        'vrf': {
            'default': {
                'address_family': {
                    'ipv4': {
                        'routes': {
                            '10.23.90.0/24': {
                                'route': '10.23.90.0/24',
                                'ip': '10.23.90.0',
                                'mask': '24',
                                'active': True,
                                'known_via': 'connected',
                                'metric': 0,
                                'distance': 0,
                                'installed': {
                                    'date': 'Oct  4 15:47:45.390',
                                    'for': '3w4d',
                                },
                                'next_hop': {
                                    'outgoing_interface': {
                                        'GigabitEthernet0/0/0/1.90': {
                                            'outgoing_interface': 'GigabitEthernet0/0/0/1.90',
                                            'metric': 0,
                                        },
                                    },
                                },
                                'redist_advertisers': {
                                    'eigrp/100': {
                                        'protoid': 5,
                                        'clientid': 22,
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
        Tue Oct 29 21:29:10.924 UTC

        O    10.13.110.0/24 [110/2] via 10.12.110.1, 5d23h, GigabitEthernet0/0/0/0.110
    '''}

    golden_parsed_output_6 = {
        'vrf': {
            'default': {
                'address_family': {
                    'ipv4': {
                        'routes': {
                            '10.13.110.0/24': {
                                'route': '10.13.110.0/24',
                                'active': True,
                                'metric': 2,
                                'route_preference': 110,
                                'source_protocol_codes': 'O',
                                'source_protocol': 'ospf',
                                'next_hop': {
                                    'next_hop_list': {
                                        1: {
                                            'index': 1,
                                            'next_hop': '10.12.110.1',
                                            'updated': '5d23h',
                                            'outgoing_interface': 'GigabitEthernet0/0/0/0.110',
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

    # show route vrf VRF1 ipv4 local
    golden_output_7 = {'execute.return_value': '''
        Tue Oct 29 21:32:17.082 UTC

        L    10.16.2.2/32 is directly connected, 3w4d, Loopback300
        L    10.12.90.2/32 is directly connected, 3w4d, GigabitEthernet0/0/0/0.390
        L    10.12.110.2/32 is directly connected, 3w4d, GigabitEthernet0/0/0/0.410
        L    10.12.115.2/32 is directly connected, 3w4d, GigabitEthernet0/0/0/0.415
        L    10.12.120.2/32 is directly connected, 3w4d, GigabitEthernet0/0/0/0.420
        L    10.23.90.2/32 is directly connected, 3w4d, GigabitEthernet0/0/0/1.390
        L    10.23.110.2/32 is directly connected, 3w4d, GigabitEthernet0/0/0/1.410
        L    10.23.115.2/32 is directly connected, 3w4d, GigabitEthernet0/0/0/1.415
        L    10.23.120.2/32 is directly connected, 3w4d, GigabitEthernet0/0/0/1.420
    '''}

    golden_parsed_output_7 = {
        'vrf': {
            'VRF1': {
                'address_family': {
                    'ipv4': {
                        'routes': {
                            '10.16.2.2/32': {
                                'route': '10.16.2.2/32',
                                'active': True,
                                'source_protocol_codes': 'L',
                                'source_protocol': 'local',
                                'next_hop': {
                                    'outgoing_interface': {
                                        'Loopback300': {
                                            'outgoing_interface': 'Loopback300',
                                            'updated': '3w4d',
                                        },
                                    },
                                },
                            },
                            '10.12.90.2/32': {
                                'route': '10.12.90.2/32',
                                'active': True,
                                'source_protocol_codes': 'L',
                                'source_protocol': 'local',
                                'next_hop': {
                                    'outgoing_interface': {
                                        'GigabitEthernet0/0/0/0.390': {
                                            'outgoing_interface': 'GigabitEthernet0/0/0/0.390',
                                            'updated': '3w4d',
                                        },
                                    },
                                },
                            },
                            '10.12.110.2/32': {
                                'route': '10.12.110.2/32',
                                'active': True,
                                'source_protocol_codes': 'L',
                                'source_protocol': 'local',
                                'next_hop': {
                                    'outgoing_interface': {
                                        'GigabitEthernet0/0/0/0.410': {
                                            'outgoing_interface': 'GigabitEthernet0/0/0/0.410',
                                            'updated': '3w4d',
                                        },
                                    },
                                },
                            },
                            '10.12.115.2/32': {
                                'route': '10.12.115.2/32',
                                'active': True,
                                'source_protocol_codes': 'L',
                                'source_protocol': 'local',
                                'next_hop': {
                                    'outgoing_interface': {
                                        'GigabitEthernet0/0/0/0.415': {
                                            'outgoing_interface': 'GigabitEthernet0/0/0/0.415',
                                            'updated': '3w4d',
                                        },
                                    },
                                },
                            },
                            '10.12.120.2/32': {
                                'route': '10.12.120.2/32',
                                'active': True,
                                'source_protocol_codes': 'L',
                                'source_protocol': 'local',
                                'next_hop': {
                                    'outgoing_interface': {
                                        'GigabitEthernet0/0/0/0.420': {
                                            'outgoing_interface': 'GigabitEthernet0/0/0/0.420',
                                            'updated': '3w4d',
                                        },
                                    },
                                },
                            },
                            '10.23.90.2/32': {
                                'route': '10.23.90.2/32',
                                'active': True,
                                'source_protocol_codes': 'L',
                                'source_protocol': 'local',
                                'next_hop': {
                                    'outgoing_interface': {
                                        'GigabitEthernet0/0/0/1.390': {
                                            'outgoing_interface': 'GigabitEthernet0/0/0/1.390',
                                            'updated': '3w4d',
                                        },
                                    },
                                },
                            },
                            '10.23.110.2/32': {
                                'route': '10.23.110.2/32',
                                'active': True,
                                'source_protocol_codes': 'L',
                                'source_protocol': 'local',
                                'next_hop': {
                                    'outgoing_interface': {
                                        'GigabitEthernet0/0/0/1.410': {
                                            'outgoing_interface': 'GigabitEthernet0/0/0/1.410',
                                            'updated': '3w4d',
                                        },
                                    },
                                },
                            },
                            '10.23.115.2/32': {
                                'route': '10.23.115.2/32',
                                'active': True,
                                'source_protocol_codes': 'L',
                                'source_protocol': 'local',
                                'next_hop': {
                                    'outgoing_interface': {
                                        'GigabitEthernet0/0/0/1.415': {
                                            'outgoing_interface': 'GigabitEthernet0/0/0/1.415',
                                            'updated': '3w4d',
                                        },
                                    },
                                },
                            },
                            '10.23.120.2/32': {
                                'route': '10.23.120.2/32',
                                'active': True,
                                'source_protocol_codes': 'L',
                                'source_protocol': 'local',
                                'next_hop': {
                                    'outgoing_interface': {
                                        'GigabitEthernet0/0/0/1.420': {
                                            'outgoing_interface': 'GigabitEthernet0/0/0/1.420',
                                            'updated': '3w4d',
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

    # show route vrf VRF1 ipv4 10.23.120.2/32
    golden_output_8 = {'execute.return_value': '''
        Tue Oct 29 21:45:11.042 UTC

        Routing entry for 10.23.120.2/32
        Known via "local", distance 0, metric 0 (connected)
        Installed Oct  4 15:47:45.368 for 3w4d
        Routing Descriptor Blocks
            directly connected, via GigabitEthernet0/0/0/1.420
            Route metric is 0
        No advertising protos.
    '''}

    golden_parsed_output_8 = {
        'vrf': {
            'VRF1': {
                'address_family': {
                    'ipv4': {
                        'routes': {
                            '10.23.120.2/32': {
                                'route': '10.23.120.2/32',
                                'ip': '10.23.120.2',
                                'mask': '32',
                                'active': True,
                                'known_via': 'local',
                                'metric': 0,
                                'distance': 0,
                                'installed': {
                                    'date': 'Oct  4 15:47:45.368',
                                    'for': '3w4d',
                                },
                                'next_hop': {
                                    'outgoing_interface': {
                                        'GigabitEthernet0/0/0/1.420': {
                                            'outgoing_interface': 'GigabitEthernet0/0/0/1.420',
                                            'metric': 0,
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

    golden_output_9 = {'execute.return_value': '''
        10.64.219.128, 2d04h
        B    172.16.55.0/22 [200/0] via 10.154.219.128, 1w3d
        B    172.16.21.0/22 [200/0] via 10.154.219.128, 1w3d
        B    172.16.16.0/24 [200/0] via 10.154.219.128, 1w3d
    '''}

    golden_parsed_output_9 = {
        'vrf': {
            'default': {
                'address_family': {
                    'ipv4': {
                        'routes': {
                            '172.16.55.0/22': {
                                'active': True,
                                'metric': 0,
                                'next_hop': {
                                    'next_hop_list': {
                                        1: {
                                            'index': 1,
                                            'next_hop': '10.154.219.128',
                                            'updated': '1w3d',
                                        },
                                    },
                                },
                                'route': '172.16.55.0/22',
                                'route_preference': 200,
                                'source_protocol': 'bgp',
                                'source_protocol_codes': 'B',
                            },
                            '172.16.21.0/22': {
                                'active': True,
                                'metric': 0,
                                'next_hop': {
                                    'next_hop_list': {
                                        1: {
                                            'index': 1,
                                            'next_hop': '10.154.219.128',
                                            'updated': '1w3d',
                                        },
                                    },
                                },
                                'route': '172.16.21.0/22',
                                'route_preference': 200,
                                'source_protocol': 'bgp',
                                'source_protocol_codes': 'B',
                            },
                            '172.16.16.0/24': {
                                'active': True,
                                'metric': 0,
                                'next_hop': {
                                    'next_hop_list': {
                                        1: {
                                            'index': 1,
                                            'next_hop': '10.154.219.128',
                                            'updated': '1w3d',
                                        },
                                    },
                                },
                                'route': '172.16.16.0/24',
                                'route_preference': 200,
                                'source_protocol': 'bgp',
                                'source_protocol_codes': 'B',
                            },
                        },
                    },
                },
            },
        },
    }

    # show route vrf qattwd ipv4 0.0.0.0/0
    golden_output_10 = {'execute.return_value': '''                                                                             
        Routing entry for 0.0.0.0/0                                                             
        Known via "bgp 65001", distance 200, metric 10, candidate default path                
        Tag 10584, type internal                                                              
        Installed Nov 20 07:00:25.367 for 7w5d                                                 
        Routing Descriptor Blocks                                                             
            172.23.6.96, from 172.23.15.196                                                     
            Nexthop in Vrf: "default", Table: "default", IPv4 Unicast, Table Id: 0xe0000000   
            Route metric is 10                                                                
        No advertising protos.
    '''
    }

    golden_parsed_output_10 = {
        'vrf': {
            'qattwd': {
                'address_family': {
                    'ipv4': {
                        'routes': {
                            '0.0.0.0/0': {
                                'active': True,
                                'distance': 200,
                                'installed': {
                                    'date': 'Nov 20 07:00:25.367',
                                    'for': '7w5d'
                                },
                                'ip': '0.0.0.0',
                                'known_via': 'bgp '
                                '65001',
                                'mask': '0',
                                'metric': 10,
                                'next_hop': {
                                    'next_hop_list': {
                                        1: {
                                            'from': '172.23.15.196',
                                            'index': 1,
                                            'address_family': 'IPv4 Unicast',
                                            'metric': 10,
                                            'next_hop': '172.23.6.96',
                                            'nexthop_in_vrf': 'default',
                                            'table': 'default',
                                            'table_id': '0xe0000000'
                                        }
                                    }
                                },
                                'route': '0.0.0.0/0',
                                'tag': '10584',
                                'type': 'internal'
                            }
                        }
                    }
                }
            }
        }
    }

    # sh route vrf L:192
    golden_output_11 = {'execute.return_value': '''
        Thu Feb 6 00:29:44.865 UTC
        
        Codes: C - connected, S - static, R - RIP, B - BGP, (>) - Diversion path
        D - EIGRP, EX - EIGRP external, O - OSPF, IA - OSPF inter area
        N1 - OSPF NSSA external type 1, N2 - OSPF NSSA external type 2
        E1 - OSPF external type 1, E2 - OSPF external type 2, E - EGP
        i - ISIS, L1 - IS-IS level-1, L2 - IS-IS level-2
        ia - IS-IS inter area, su - IS-IS summary null, * - candidate default
        U - per-user static route, o - ODR, L - local, G - DAGR, l - LISP
        A - access/subscriber, a - Application route
        M - mobile route, r - RPL, t - Traffic Engineering, (!) - FRR Backup path
        
        Gateway of last resort is not set

        S 10.2.2.2/32 is directly connected, 00:06:36, Null0
    '''}

    golden_parsed_output_11 = {
        'vrf': {
            'L:192': {
                'address_family': {
                    'ipv4': {
                        'routes': {
                            '10.2.2.2/32': {
                                'active': True,
                                'next_hop': {
                                    'outgoing_interface': {
                                        'Null0': {
                                            'outgoing_interface': 'Null0',
                                            'updated': '00:06:36',
                                        },
                                    },
                                },
                                'route': '10.2.2.2/32',
                                'source_protocol': 'static',
                                'source_protocol_codes': 'S',
                            },
                        },
                    },
                },
                'last_resort': {
                    'gateway': 'not set'
                },
            },
        },
    }

    # show route vrf HIPTV ipv4 172.25.254.37/32
    golden_output_12 = {'execute.return_value': '''
    Wed Apr 22 16:38:25.274 EDT
    
    Routing entry for 172.25.254.37/32
    Known via "bgp 7992", distance 20, metric 0
    Tag 65525, type external
    Installed Feb 6 13:12:22.999 for 10w6d
    Routing Descriptor Blocks
    172.25.253.121, from 172.25.253.121, BGP external
    Route metric is 0
    No advertising protos.
    '''}

    golden_parsed_output_12 = {
        'vrf': {
            'HIPTV': {
                'address_family': {
                    'ipv4': {
                        'routes': {
                            '172.25.254.37/32': {
                                'known_via': 'bgp 7992',
                                'ip': '172.25.254.37',
                                'metric': 0,
                                'installed': {
                                    'date': 'Feb 6 13:12:22.999',
                                    'for': '10w6d',
                                },
                                'next_hop': {
                                    'next_hop_list': {
                                        1: {
                                            'index': 1,
                                            'metric': 0,
                                            'next_hop': '172.25.253.121',
                                            'from': '172.25.253.121',
                                        },
                                    },
                                },
                                'active': True,
                                'distance': 20,
                                'route': '172.25.254.37/32',
                                'mask': '32',
                                'tag': '65525',
                                'type': 'external',
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
        self.assertEqual(parsed_output, self.golden_parsed_output_1)

    def test_show_route_ipv4_2(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_2)
        obj = ShowRouteIpv4(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_2)

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
        parsed_output = obj.parse(vrf='VRF1')
        self.assertEqual(parsed_output, self.golden_parsed_output_3_with_vrf)

    def test_show_route_ipv4_4(self):
        self.maxDiff = None
        self.device = Mock(**self.device_output)
        obj = ShowRouteIpv4(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.expected_output)
    
    def test_show_route_5(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_5)
        obj = ShowRouteIpv4(device=self.device)
        parsed_output = obj.parse(route='10.23.90.0/24')
        self.assertEqual(parsed_output, self.golden_parsed_output_5)
    
    def test_show_route_6(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_6)
        obj = ShowRouteIpv4(device=self.device)
        parsed_output = obj.parse(protocol='ospf')
        self.assertEqual(parsed_output, self.golden_parsed_output_6)
    
    def test_show_route_7(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_7)
        obj = ShowRouteIpv4(device=self.device)
        parsed_output = obj.parse(protocol='local', vrf='VRF1')
        self.assertEqual(parsed_output, self.golden_parsed_output_7)

    def test_show_route_8(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_8)
        obj = ShowRouteIpv4(device=self.device)
        parsed_output = obj.parse(route='10.23.120.2/32', vrf='VRF1')
        self.assertEqual(parsed_output, self.golden_parsed_output_8)

    def test_show_route_9(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_9)
        obj = ShowRouteIpv4(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_9)

    def test_show_route_10(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_10)
        obj = ShowRouteIpv4(device=self.device)
        parsed_output = obj.parse(route='0.0.0.0/0', vrf='qattwd')
        self.assertEqual(parsed_output, self.golden_parsed_output_10)

    def test_show_route_11(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_11)
        obj = ShowRouteIpv4(device=self.device)
        parsed_output = obj.parse(vrf='L:192')
        self.assertEqual(parsed_output, self.golden_parsed_output_11)

    def test_show_route_12(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_12)
        obj = ShowRouteIpv4(device=self.device)
        parsed_output = obj.parse(vrf='HIPTV', route='172.25.254.37/32')
        self.assertEqual(parsed_output, self.golden_parsed_output_12)


# ============================================
# unit test for 'show route ipv6'
# =============================================
class TestShowRouteIpv6(unittest.TestCase):
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
        'vrf': {
            'default': {
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
                'last_resort': {
                    'gateway': 'not set'
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

        O E2 2001:db8:121::/64
            [110/0] via fe80::200:ff:fe33:3a83, 20:03:53, GigabitEthernet0/0/0/0.501
        O E2 2001:db8:121:51::/64
            [110/0] via fe80::200:ff:fe33:3a83, 20:03:53, GigabitEthernet0/0/0/0.501
        L    2001:db8:400:1::1/128 is directly connected,
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

        B    2001:db8:144::/64
            [20/0] via fe80::200:ff:fe33:3a84, 19:39:47, GigabitEthernet0/0/0/0.502
        B    2001:db8:144:1::/64
            [20/0] via fe80::200:ff:fe33:3a84, 19:39:47, GigabitEthernet0/0/0/0.502
        B    2001:db8:144:51::/64
            [20/0] via fe80::200:ff:fe33:3a84, 19:39:47, GigabitEthernet0/0/0/0.502
        L    2001:db8:400:4::1/128 is directly connected,
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
        L    2001:db8:400:9::1/128 is directly connected,
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
                            '2001:db8:121::/64': {
                                'route': '2001:db8:121::/64',
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
                            '2001:db8:121:51::/64': {
                                'route': '2001:db8:121:51::/64',
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
                            '2001:db8:400:1::1/128': {
                                'route': '2001:db8:400:1::1/128',
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
                'last_resort': {
                    'gateway': 'not set'
                },
            },
            'VRF502': {
                'address_family': {
                    'ipv6': {
                        'routes': {
                            '2001:db8:144::/64': {
                                'route': '2001:db8:144::/64',
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
                            '2001:db8:144:1::/64': {
                                'route': '2001:db8:144:1::/64',
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
                            '2001:db8:144:51::/64': {
                                'route': '2001:db8:144:51::/64',
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
                            '2001:db8:400:4::1/128': {
                                'route': '2001:db8:400:4::1/128',
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
                'last_resort': {
                    'gateway': 'not set'
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
                            '2001:db8:400:9::1/128': {
                                'route': '2001:db8:400:9::1/128',
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
                'last_resort': {
                    'gateway': 'not set'
                },
            },
        },
    }

    golden_output_4 = {'execute.return_value': '''
        #show route vrf VRF1 ipv6
        Tue Oct 29 22:01:28.796 UTC

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

        D    2001:1:1:1::1/128
            [90/10880] via fe80::f816:3eff:fe76:b56d, 5d23h, GigabitEthernet0/0/0/0.390
        L    2001:2:2:2::2/128 is directly connected,
            3w4d, Loopback300
        D    2001:3:3:3::3/128
            [90/2570240] via fe80::5c00:80ff:fe02:7, 3w4d, GigabitEthernet0/0/0/1.390
        C    2001:10:12:90::/64 is directly connected,
            3w4d, GigabitEthernet0/0/0/0.390
        L    2001:10:12:90::2/128 is directly connected,
            3w4d, GigabitEthernet0/0/0/0.390
        C    2001:10:12:110::/64 is directly connected,
            3w4d, GigabitEthernet0/0/0/0.410
        L    2001:10:12:110::2/128 is directly connected,
            3w4d, GigabitEthernet0/0/0/0.410
        C    2001:10:12:115::/64 is directly connected,
            3w4d, GigabitEthernet0/0/0/0.415
        L    2001:10:12:115::2/128 is directly connected,
            3w4d, GigabitEthernet0/0/0/0.415
        C    2001:10:12:120::/64 is directly connected,
            3w4d, GigabitEthernet0/0/0/0.420
        L    2001:10:12:120::2/128 is directly connected,
            3w4d, GigabitEthernet0/0/0/0.420
        D    2001:10:13:90::/64
            [90/15360] via fe80::f816:3eff:fe76:b56d, 5d23h, GigabitEthernet0/0/0/0.390
        D    2001:10:13:110::/64
            [90/15360] via fe80::f816:3eff:fe76:b56d, 5d23h, GigabitEthernet0/0/0/0.390
        D    2001:10:13:115::/64
            [90/15360] via fe80::f816:3eff:fe76:b56d, 5d23h, GigabitEthernet0/0/0/0.390
        D    2001:10:13:120::/64
            [90/15360] via fe80::f816:3eff:fe76:b56d, 5d23h, GigabitEthernet0/0/0/0.390
        C    2001:10:23:90::/64 is directly connected,
            3w4d, GigabitEthernet0/0/0/1.390
        L    2001:10:23:90::2/128 is directly connected,
            3w4d, GigabitEthernet0/0/0/1.390
        C    2001:10:23:110::/64 is directly connected,
            3w4d, GigabitEthernet0/0/0/1.410
        L    2001:10:23:110::2/128 is directly connected,
            3w4d, GigabitEthernet0/0/0/1.410
        C    2001:10:23:115::/64 is directly connected,
            3w4d, GigabitEthernet0/0/0/1.415
        L    2001:10:23:115::2/128 is directly connected,
            3w4d, GigabitEthernet0/0/0/1.415
        C    2001:10:23:120::/64 is directly connected,
            3w4d, GigabitEthernet0/0/0/1.420
        L    2001:10:23:120::2/128 is directly connected,
            3w4d, GigabitEthernet0/0/0/1.420
    '''}

    golden_parsed_output_4 = {
        'vrf': {
            'VRF1': {
                'address_family': {
                    'ipv6': {
                        'routes': {
                            '2001:1:1:1::1/128': {
                                'route': '2001:1:1:1::1/128',
                                'active': True,
                                'source_protocol_codes': 'D',
                                'source_protocol': 'eigrp',
                                'metric': 10880,
                                'route_preference': 90,
                                'next_hop': {
                                    'next_hop_list': {
                                        1: {
                                            'index': 1,
                                            'next_hop': 'fe80::f816:3eff:fe76:b56d',
                                            'outgoing_interface': 'GigabitEthernet0/0/0/0.390',
                                            'updated': '5d23h',
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
                                        'Loopback300': {
                                            'outgoing_interface': 'Loopback300',
                                            'updated': '3w4d',
                                        },
                                    },
                                },
                            },
                            '2001:3:3:3::3/128': {
                                'route': '2001:3:3:3::3/128',
                                'active': True,
                                'source_protocol_codes': 'D',
                                'source_protocol': 'eigrp',
                                'metric': 2570240,
                                'route_preference': 90,
                                'next_hop': {
                                    'next_hop_list': {
                                        1: {
                                            'index': 1,
                                            'next_hop': 'fe80::5c00:80ff:fe02:7',
                                            'outgoing_interface': 'GigabitEthernet0/0/0/1.390',
                                            'updated': '3w4d',
                                        },
                                    },
                                },
                            },
                            '2001:10:12:90::/64': {
                                'route': '2001:10:12:90::/64',
                                'active': True,
                                'source_protocol_codes': 'C',
                                'source_protocol': 'connected',
                                'next_hop': {
                                    'outgoing_interface': {
                                        'GigabitEthernet0/0/0/0.390': {
                                            'outgoing_interface': 'GigabitEthernet0/0/0/0.390',
                                            'updated': '3w4d',
                                        },
                                    },
                                },
                            },
                            '2001:10:12:90::2/128': {
                                'route': '2001:10:12:90::2/128',
                                'active': True,
                                'source_protocol_codes': 'L',
                                'source_protocol': 'local',
                                'next_hop': {
                                    'outgoing_interface': {
                                        'GigabitEthernet0/0/0/0.390': {
                                            'outgoing_interface': 'GigabitEthernet0/0/0/0.390',
                                            'updated': '3w4d',
                                        },
                                    },
                                },
                            },
                            '2001:10:12:110::/64': {
                                'route': '2001:10:12:110::/64',
                                'active': True,
                                'source_protocol_codes': 'C',
                                'source_protocol': 'connected',
                                'next_hop': {
                                    'outgoing_interface': {
                                        'GigabitEthernet0/0/0/0.410': {
                                            'outgoing_interface': 'GigabitEthernet0/0/0/0.410',
                                            'updated': '3w4d',
                                        },
                                    },
                                },
                            },
                            '2001:10:12:110::2/128': {
                                'route': '2001:10:12:110::2/128',
                                'active': True,
                                'source_protocol_codes': 'L',
                                'source_protocol': 'local',
                                'next_hop': {
                                    'outgoing_interface': {
                                        'GigabitEthernet0/0/0/0.410': {
                                            'outgoing_interface': 'GigabitEthernet0/0/0/0.410',
                                            'updated': '3w4d',
                                        },
                                    },
                                },
                            },
                            '2001:10:12:115::/64': {
                                'route': '2001:10:12:115::/64',
                                'active': True,
                                'source_protocol_codes': 'C',
                                'source_protocol': 'connected',
                                'next_hop': {
                                    'outgoing_interface': {
                                        'GigabitEthernet0/0/0/0.415': {
                                            'outgoing_interface': 'GigabitEthernet0/0/0/0.415',
                                            'updated': '3w4d',
                                        },
                                    },
                                },
                            },
                            '2001:10:12:115::2/128': {
                                'route': '2001:10:12:115::2/128',
                                'active': True,
                                'source_protocol_codes': 'L',
                                'source_protocol': 'local',
                                'next_hop': {
                                    'outgoing_interface': {
                                        'GigabitEthernet0/0/0/0.415': {
                                            'outgoing_interface': 'GigabitEthernet0/0/0/0.415',
                                            'updated': '3w4d',
                                        },
                                    },
                                },
                            },
                            '2001:10:12:120::/64': {
                                'route': '2001:10:12:120::/64',
                                'active': True,
                                'source_protocol_codes': 'C',
                                'source_protocol': 'connected',
                                'next_hop': {
                                    'outgoing_interface': {
                                        'GigabitEthernet0/0/0/0.420': {
                                            'outgoing_interface': 'GigabitEthernet0/0/0/0.420',
                                            'updated': '3w4d',
                                        },
                                    },
                                },
                            },
                            '2001:10:12:120::2/128': {
                                'route': '2001:10:12:120::2/128',
                                'active': True,
                                'source_protocol_codes': 'L',
                                'source_protocol': 'local',
                                'next_hop': {
                                    'outgoing_interface': {
                                        'GigabitEthernet0/0/0/0.420': {
                                            'outgoing_interface': 'GigabitEthernet0/0/0/0.420',
                                            'updated': '3w4d',
                                        },
                                    },
                                },
                            },
                            '2001:10:13:90::/64': {
                                'route': '2001:10:13:90::/64',
                                'active': True,
                                'source_protocol_codes': 'D',
                                'source_protocol': 'eigrp',
                                'metric': 15360,
                                'route_preference': 90,
                                'next_hop': {
                                    'next_hop_list': {
                                        1: {
                                            'index': 1,
                                            'next_hop': 'fe80::f816:3eff:fe76:b56d',
                                            'outgoing_interface': 'GigabitEthernet0/0/0/0.390',
                                            'updated': '5d23h',
                                        },
                                    },
                                },
                            },
                            '2001:10:13:110::/64': {
                                'route': '2001:10:13:110::/64',
                                'active': True,
                                'source_protocol_codes': 'D',
                                'source_protocol': 'eigrp',
                                'metric': 15360,
                                'route_preference': 90,
                                'next_hop': {
                                    'next_hop_list': {
                                        1: {
                                            'index': 1,
                                            'next_hop': 'fe80::f816:3eff:fe76:b56d',
                                            'outgoing_interface': 'GigabitEthernet0/0/0/0.390',
                                            'updated': '5d23h',
                                        },
                                    },
                                },
                            },
                            '2001:10:13:115::/64': {
                                'route': '2001:10:13:115::/64',
                                'active': True,
                                'source_protocol_codes': 'D',
                                'source_protocol': 'eigrp',
                                'metric': 15360,
                                'route_preference': 90,
                                'next_hop': {
                                    'next_hop_list': {
                                        1: {
                                            'index': 1,
                                            'next_hop': 'fe80::f816:3eff:fe76:b56d',
                                            'outgoing_interface': 'GigabitEthernet0/0/0/0.390',
                                            'updated': '5d23h',
                                        },
                                    },
                                },
                            },
                            '2001:10:13:120::/64': {
                                'route': '2001:10:13:120::/64',
                                'active': True,
                                'source_protocol_codes': 'D',
                                'source_protocol': 'eigrp',
                                'metric': 15360,
                                'route_preference': 90,
                                'next_hop': {
                                    'next_hop_list': {
                                        1: {
                                            'index': 1,
                                            'next_hop': 'fe80::f816:3eff:fe76:b56d',
                                            'outgoing_interface': 'GigabitEthernet0/0/0/0.390',
                                            'updated': '5d23h',
                                        },
                                    },
                                },
                            },
                            '2001:10:23:90::/64': {
                                'route': '2001:10:23:90::/64',
                                'active': True,
                                'source_protocol_codes': 'C',
                                'source_protocol': 'connected',
                                'next_hop': {
                                    'outgoing_interface': {
                                        'GigabitEthernet0/0/0/1.390': {
                                            'outgoing_interface': 'GigabitEthernet0/0/0/1.390',
                                            'updated': '3w4d',
                                        },
                                    },
                                },
                            },
                            '2001:10:23:90::2/128': {
                                'route': '2001:10:23:90::2/128',
                                'active': True,
                                'source_protocol_codes': 'L',
                                'source_protocol': 'local',
                                'next_hop': {
                                    'outgoing_interface': {
                                        'GigabitEthernet0/0/0/1.390': {
                                            'outgoing_interface': 'GigabitEthernet0/0/0/1.390',
                                            'updated': '3w4d',
                                        },
                                    },
                                },
                            },
                            '2001:10:23:110::/64': {
                                'route': '2001:10:23:110::/64',
                                'active': True,
                                'source_protocol_codes': 'C',
                                'source_protocol': 'connected',
                                'next_hop': {
                                    'outgoing_interface': {
                                        'GigabitEthernet0/0/0/1.410': {
                                            'outgoing_interface': 'GigabitEthernet0/0/0/1.410',
                                            'updated': '3w4d',
                                        },
                                    },
                                },
                            },
                            '2001:10:23:110::2/128': {
                                'route': '2001:10:23:110::2/128',
                                'active': True,
                                'source_protocol_codes': 'L',
                                'source_protocol': 'local',
                                'next_hop': {
                                    'outgoing_interface': {
                                        'GigabitEthernet0/0/0/1.410': {
                                            'outgoing_interface': 'GigabitEthernet0/0/0/1.410',
                                            'updated': '3w4d',
                                        },
                                    },
                                },
                            },
                            '2001:10:23:115::/64': {
                                'route': '2001:10:23:115::/64',
                                'active': True,
                                'source_protocol_codes': 'C',
                                'source_protocol': 'connected',
                                'next_hop': {
                                    'outgoing_interface': {
                                        'GigabitEthernet0/0/0/1.415': {
                                            'outgoing_interface': 'GigabitEthernet0/0/0/1.415',
                                            'updated': '3w4d',
                                        },
                                    },
                                },
                            },
                            '2001:10:23:115::2/128': {
                                'route': '2001:10:23:115::2/128',
                                'active': True,
                                'source_protocol_codes': 'L',
                                'source_protocol': 'local',
                                'next_hop': {
                                    'outgoing_interface': {
                                        'GigabitEthernet0/0/0/1.415': {
                                            'outgoing_interface': 'GigabitEthernet0/0/0/1.415',
                                            'updated': '3w4d',
                                        },
                                    },
                                },
                            },
                            '2001:10:23:120::/64': {
                                'route': '2001:10:23:120::/64',
                                'active': True,
                                'source_protocol_codes': 'C',
                                'source_protocol': 'connected',
                                'next_hop': {
                                    'outgoing_interface': {
                                        'GigabitEthernet0/0/0/1.420': {
                                            'outgoing_interface': 'GigabitEthernet0/0/0/1.420',
                                            'updated': '3w4d',
                                        },
                                    },
                                },
                            },
                            '2001:10:23:120::2/128': {
                                'route': '2001:10:23:120::2/128',
                                'active': True,
                                'source_protocol_codes': 'L',
                                'source_protocol': 'local',
                                'next_hop': {
                                    'outgoing_interface': {
                                        'GigabitEthernet0/0/0/1.420': {
                                            'outgoing_interface': 'GigabitEthernet0/0/0/1.420',
                                            'updated': '3w4d',
                                        },
                                    },
                                },
                            },
                        },
                    },
                },
                'last_resort': {
                    'gateway': 'not set'
                },
            },
        },
    }

    golden_output_5 = {'execute.return_value': '''
        show route ipv6 2001:10:23:120::2/128
        Tue Oct 29 22:14:01.797 UTC

        Routing entry for 2001:10:23:120::2/128
        Known via "local", distance 0, metric 0 (connected)
        Installed Oct  4 15:47:46.727 for 3w4d
        Routing Descriptor Blocks
            directly connected, via GigabitEthernet0/0/0/1.120
            Route metric is 0
        No advertising protos.
    '''}

    golden_parsed_output_5 = {
        'vrf': {
            'default': {
                'address_family': {
                    'ipv6': {
                        'routes': {
                            '2001:10:23:120::2/128': {
                                'route': '2001:10:23:120::2/128',
                                'ip': '2001:10:23:120::2',
                                'mask': '128',
                                'active': True,
                                'known_via': 'local',
                                'metric': 0,
                                'distance': 0,
                                'installed': {
                                    'date': 'Oct  4 15:47:46.727',
                                    'for': '3w4d',
                                },
                                'next_hop': {
                                    'outgoing_interface': {
                                        'GigabitEthernet0/0/0/1.120': {
                                            'outgoing_interface': 'GigabitEthernet0/0/0/1.120',
                                            'metric': 0,
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
        show route ipv6 local
        Tue Oct 29 22:16:33.287 UTC

        L    2001:2:2:2::2/128 is directly connected,
            3w4d, Loopback0
        L    2001:10:12:90::2/128 is directly connected,
            3w4d, GigabitEthernet0/0/0/0.90
        L    2001:10:12:110::2/128 is directly connected,
            3w4d, GigabitEthernet0/0/0/0.110
        L    2001:10:12:115::2/128 is directly connected,
            3w4d, GigabitEthernet0/0/0/0.115
        L    2001:10:12:120::2/128 is directly connected,
            3w4d, GigabitEthernet0/0/0/0.120
        L    2001:10:23:90::2/128 is directly connected,
            3w4d, GigabitEthernet0/0/0/1.90
        L    2001:10:23:110::2/128 is directly connected,
            3w4d, GigabitEthernet0/0/0/1.110
        L    2001:10:23:115::2/128 is directly connected,
            3w4d, GigabitEthernet0/0/0/1.115
        L    2001:10:23:120::2/128 is directly connected,
            3w4d, GigabitEthernet0/0/0/1.120
    '''}

    golden_parsed_output_6 = {
        'vrf': {
            'default': {
                'address_family': {
                    'ipv6': {
                        'routes': {
                            '2001:2:2:2::2/128': {
                                'route': '2001:2:2:2::2/128',
                                'active': True,
                                'source_protocol_codes': 'L',
                                'source_protocol': 'local',
                                'next_hop': {
                                    'outgoing_interface': {
                                        'Loopback0': {
                                            'outgoing_interface': 'Loopback0',
                                            'updated': '3w4d',
                                        },
                                    },
                                },
                            },
                            '2001:10:12:90::2/128': {
                                'route': '2001:10:12:90::2/128',
                                'active': True,
                                'source_protocol_codes': 'L',
                                'source_protocol': 'local',
                                'next_hop': {
                                    'outgoing_interface': {
                                        'GigabitEthernet0/0/0/0.90': {
                                            'outgoing_interface': 'GigabitEthernet0/0/0/0.90',
                                            'updated': '3w4d',
                                        },
                                    },
                                },
                            },
                            '2001:10:12:110::2/128': {
                                'route': '2001:10:12:110::2/128',
                                'active': True,
                                'source_protocol_codes': 'L',
                                'source_protocol': 'local',
                                'next_hop': {
                                    'outgoing_interface': {
                                        'GigabitEthernet0/0/0/0.110': {
                                            'outgoing_interface': 'GigabitEthernet0/0/0/0.110',
                                            'updated': '3w4d',
                                        },
                                    },
                                },
                            },
                            '2001:10:12:115::2/128': {
                                'route': '2001:10:12:115::2/128',
                                'active': True,
                                'source_protocol_codes': 'L',
                                'source_protocol': 'local',
                                'next_hop': {
                                    'outgoing_interface': {
                                        'GigabitEthernet0/0/0/0.115': {
                                            'outgoing_interface': 'GigabitEthernet0/0/0/0.115',
                                            'updated': '3w4d',
                                        },
                                    },
                                },
                            },
                            '2001:10:12:120::2/128': {
                                'route': '2001:10:12:120::2/128',
                                'active': True,
                                'source_protocol_codes': 'L',
                                'source_protocol': 'local',
                                'next_hop': {
                                    'outgoing_interface': {
                                        'GigabitEthernet0/0/0/0.120': {
                                            'outgoing_interface': 'GigabitEthernet0/0/0/0.120',
                                            'updated': '3w4d',
                                        },
                                    },
                                },
                            },
                            '2001:10:23:90::2/128': {
                                'route': '2001:10:23:90::2/128',
                                'active': True,
                                'source_protocol_codes': 'L',
                                'source_protocol': 'local',
                                'next_hop': {
                                    'outgoing_interface': {
                                        'GigabitEthernet0/0/0/1.90': {
                                            'outgoing_interface': 'GigabitEthernet0/0/0/1.90',
                                            'updated': '3w4d',
                                        },
                                    },
                                },
                            },
                            '2001:10:23:110::2/128': {
                                'route': '2001:10:23:110::2/128',
                                'active': True,
                                'source_protocol_codes': 'L',
                                'source_protocol': 'local',
                                'next_hop': {
                                    'outgoing_interface': {
                                        'GigabitEthernet0/0/0/1.110': {
                                            'outgoing_interface': 'GigabitEthernet0/0/0/1.110',
                                            'updated': '3w4d',
                                        },
                                    },
                                },
                            },
                            '2001:10:23:115::2/128': {
                                'route': '2001:10:23:115::2/128',
                                'active': True,
                                'source_protocol_codes': 'L',
                                'source_protocol': 'local',
                                'next_hop': {
                                    'outgoing_interface': {
                                        'GigabitEthernet0/0/0/1.115': {
                                            'outgoing_interface': 'GigabitEthernet0/0/0/1.115',
                                            'updated': '3w4d',
                                        },
                                    },
                                },
                            },
                            '2001:10:23:120::2/128': {
                                'route': '2001:10:23:120::2/128',
                                'active': True,
                                'source_protocol_codes': 'L',
                                'source_protocol': 'local',
                                'next_hop': {
                                    'outgoing_interface': {
                                        'GigabitEthernet0/0/0/1.120': {
                                            'outgoing_interface': 'GigabitEthernet0/0/0/1.120',
                                            'updated': '3w4d',
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

    golden_output_7 = {'execute.return_value': '''
        show route vrf VRF1 ipv6 2001:1:1:1::1
        Tue Oct 29 19:31:30.848 UTC

        Routing entry for 2001:1:1:1::1/128
        Known via "eigrp 100", distance 90, metric 10880, type internal
        Installed Oct 23 22:09:38.380 for 5d21h
        Routing Descriptor Blocks
            fe80::f816:3eff:fe76:b56d, from fe80::f816:3eff:fe76:b56d, via GigabitEthernet0/0/0/0.390
            Route metric is 10880
        No advertising protos.
    '''}

    golden_parsed_output_7 = {
        'vrf': {
            'VRF1': {
                'address_family': {
                    'ipv6': {
                        'routes': {
                            '2001:1:1:1::1/128': {
                                'route': '2001:1:1:1::1/128',
                                'ip': '2001:1:1:1::1',
                                'mask': '128',
                                'active': True,
                                'known_via': 'eigrp 100',
                                'metric': 10880,
                                'distance': 90,
                                'type': 'internal',
                                'installed': {
                                    'date': 'Oct 23 22:09:38.380',
                                    'for': '5d21h',
                                },
                                'next_hop': {
                                    'next_hop_list': {
                                        1: {
                                            'index': 1,
                                            'outgoing_interface': 'GigabitEthernet0/0/0/0.390',
                                            'from': 'fe80::f816:3eff:fe76:b56d',
                                            'next_hop': 'fe80::f816:3eff:fe76:b56d',
                                            'metric': 10880,
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

    golden_output8 = {'execute.return_value': '''
        RP/0/RSP0/CPU0:ASR-01#
        [2020-01-21 03:11:17,780] +++ ASR-01: executing command 'show route ipv6' +++
        show route ipv6

        Tue Jan 21 03:11:17.836 UTC

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

        L    ::ffff:127.0.0.0/104 
            [0/0] via ::, 00:03:29
        L    2001:db8:4:4::1/128 is directly connected,
            00:05:52, Loopback60
        C    2001:0:10:204:0:30::/126 is directly connected,
            00:05:36, Bundle-Ether10
        L    2001:0:10:204:0:30:0:2/128 is directly connected,
            00:05:36, Bundle-Ether10
        i L2 2001:0:10:204:0:33::/126 
            [115/20] via fe80::21c:73ff:fed7:2ead, 00:01:58, Bundle-Ether10
            [115/20] via fe80::226:88ff:fe55:6f17, 00:01:58, TenGigE0/0/0/1
        i L2 2001:db8:1b7f:8e5c::8/128 
            [115/10] via fe80::226:88ff:fe55:6f17, 00:01:58, TenGigE0/0/0/1
        C    fc00:a0:1::/64 is directly connected,
            00:05:52, TenGigE0/0/0/0
        L    fc00:a0:1::2/128 is directly connected,
            00:05:52, TenGigE0/0/0/0
        i L2 fc00:a0:1:216::1/128 
            [115/20] via fe80::21c:73ff:fed7:2ead, 00:05:23, Bundle-Ether10
        C    fc00:a0:5::/64 is directly connected,
            00:02:10, TenGigE0/0/0/1
        L    fc00:a0:5::2/128 is directly connected,
            00:02:10, TenGigE0/0/0/1
        RP/0/RSP0/CPU0:ASR-01#    
    
    '''
    }

    golden_parsed_output8 = {
        'vrf': {
            'default': {
                'address_family': {
                    'ipv6': {
                        'routes': {
                            '2001:0:10:204:0:30:0:2/128': {
                                'active': True,
                                'next_hop': {
                                    'outgoing_interface': {
                                        'Bundle-Ether10': {
                                            'outgoing_interface': 'Bundle-Ether10',
                                            'updated': '00:05:36'
                                        }
                                    }
                                },
                                'route': '2001:0:10:204:0:30:0:2/128',
                                'source_protocol': 'local',
                                'source_protocol_codes': 'L'
                            },
                            '2001:0:10:204:0:30::/126': {
                                'active': True,
                                'next_hop': {
                                    'outgoing_interface': {
                                        'Bundle-Ether10': {
                                            'outgoing_interface': 'Bundle-Ether10',
                                            'updated': '00:05:36'
                                        }
                                    }
                                },
                                'route': '2001:0:10:204:0:30::/126',
                                'source_protocol': 'connected',
                                'source_protocol_codes': 'C'
                            },
                            '2001:0:10:204:0:33::/126': {
                                'active': True,
                                'metric': 20,
                                'next_hop': {
                                    'next_hop_list': {
                                        1: {
                                            'index': 1,
                                            'next_hop': 'fe80::21c:73ff:fed7:2ead',
                                            'outgoing_interface': 'Bundle-Ether10',
                                            'updated': '00:01:58'
                                        },
                                        2: {
                                            'index': 2,
                                            'next_hop': 'fe80::226:88ff:fe55:6f17',
                                            'outgoing_interface': 'TenGigE0/0/0/1',
                                            'updated': '00:01:58'
                                        }
                                    }
                                },
                                'route': '2001:0:10:204:0:33::/126',
                                'route_preference': 115,
                                'source_protocol': 'isis',
                                'source_protocol_codes': 'i L2'
                            },
                            '2001:db8:1b7f:8e5c::8/128': {
                                'active': True,
                                'metric': 10,
                                'next_hop': {
                                    'next_hop_list': {
                                        1: {
                                            'index': 1,
                                            'next_hop': 'fe80::226:88ff:fe55:6f17',
                                            'outgoing_interface': 'TenGigE0/0/0/1',
                                            'updated': '00:01:58'
                                        }
                                    }
                                },
                                'route': '2001:db8:1b7f:8e5c::8/128',
                                'route_preference': 115,
                                'source_protocol': 'isis',
                                'source_protocol_codes': 'i L2'
                            },
                            '2001:db8:4:4::1/128': {
                                'active': True,
                                'next_hop': {
                                    'outgoing_interface': {
                                        'Loopback60': {
                                            'outgoing_interface': 'Loopback60',
                                            'updated': '00:05:52'
                                        }
                                    }
                                },
                                'route': '2001:db8:4:4::1/128',
                                'source_protocol': 'local',
                                'source_protocol_codes': 'L'
                            },
                            '::ffff:127.0.0.0/104': {
                                'active': True,
                                'metric': 0,
                                'next_hop': {
                                    'next_hop_list': {
                                        1: {
                                            'index': 1,
                                            'next_hop': '::',
                                            'updated': '00:03:29'
                                        }
                                    }
                                },
                                'route': '::ffff:127.0.0.0/104',
                                'route_preference': 0,
                                'source_protocol': 'local',
                                'source_protocol_codes': 'L'
                            },
                            'fc00:a0:1:216::1/128': {
                                'active': True,
                                'metric': 20,
                                'next_hop': {
                                    'next_hop_list': {
                                        1: {
                                            'index': 1,
                                            'next_hop': 'fe80::21c:73ff:fed7:2ead',
                                            'outgoing_interface': 'Bundle-Ether10',
                                            'updated': '00:05:23'
                                        }
                                    }
                                },
                                'route': 'fc00:a0:1:216::1/128',
                                'route_preference': 115,
                                'source_protocol': 'isis',
                                'source_protocol_codes': 'i L2'
                            },
                            'fc00:a0:1::/64': {
                                'active': True,
                                'next_hop': {
                                    'outgoing_interface': {
                                        'TenGigE0/0/0/0': {
                                            'outgoing_interface': 'TenGigE0/0/0/0',
                                            'updated': '00:05:52'
                                        }
                                    }
                                },
                                'route': 'fc00:a0:1::/64',
                                'source_protocol': 'connected',
                                'source_protocol_codes': 'C'
                            },
                            'fc00:a0:1::2/128': {
                                'active': True,
                                'next_hop': {
                                    'outgoing_interface': {
                                        'TenGigE0/0/0/0': {
                                            'outgoing_interface': 'TenGigE0/0/0/0',
                                            'updated': '00:05:52'
                                        }
                                    }
                                },
                                'route': 'fc00:a0:1::2/128',
                                'source_protocol': 'local',
                                'source_protocol_codes': 'L'
                            },
                            'fc00:a0:5::/64': {
                                'active': True,
                                'next_hop': {
                                    'outgoing_interface': {
                                        'TenGigE0/0/0/1': {
                                            'outgoing_interface': 'TenGigE0/0/0/1',
                                            'updated': '00:02:10'
                                        }
                                    }
                                },
                                'route': 'fc00:a0:5::/64',
                                'source_protocol': 'connected',
                                'source_protocol_codes': 'C'
                            },
                            'fc00:a0:5::2/128': {
                                'active': True,
                                'next_hop': {
                                    'outgoing_interface': {
                                        'TenGigE0/0/0/1': {
                                            'outgoing_interface': 'TenGigE0/0/0/1',
                                            'updated': '00:02:10'
                                        }
                                    }
                                },
                                'route': 'fc00:a0:5::2/128',
                                'source_protocol': 'local',
                                'source_protocol_codes': 'L'
                            }
                        }
                    }
                },
                'last_resort': {
                    'gateway': 'not set'
                },
            },
        }
    }

    golden_output9 = {'execute.return_value': '''
        Codes: C - connected, S - static, R - RIP, B - BGP, (>) - Diversion path
            D - EIGRP, EX - EIGRP external, O - OSPF, IA - OSPF inter area
            N1 - OSPF NSSA external type 1, N2 - OSPF NSSA external type 2
            E1 - OSPF external type 1, E2 - OSPF external type 2, E - EGP
            i - ISIS, L1 - IS-IS level-1, L2 - IS-IS level-2
            ia - IS-IS inter area, su - IS-IS summary null, * - candidate default
            U - per-user static route, o - ODR, L - local, G  - DAGR, l - LISP
            A - access/subscriber, a - Application route
            M - mobile route, r - RPL, t - Traffic Engineering, (!) - FRR Backup path

        Gateway of last resort is fe80::10ff:fe04:209e to network ::

        a*   ::/0
        [2/0] via fe80::10ff:fe04:209e, 00:08:31, MgmtEth0/RP0/CPU0/0
        O    2001:db8:1234::8/128
        [110/1] via fe80::5054:ff:fef2:a625, 00:03:00, GigabitEthernet0/0/0/1
        O    2001:db8:1579::8/128
        [110/1] via fe80::5054:ff:fef2:a625, 00:03:00, GigabitEthernet0/0/0/1
        O    2001:db8:1981::8/128
        [110/1] via fe80::5054:ff:fef2:a625, 00:03:00, GigabitEthernet0/0/0/1
        O    2001:db8:2222::8/128
        [110/1] via fe80::5054:ff:fef2:a625, 00:03:00, GigabitEthernet0/0/0/1
        O    2001:db8:3456::8/128
        [110/1] via fe80::5054:ff:fef2:a625, 00:03:00, GigabitEthernet0/0/0/1
        O    2001:db8:4021::8/128
        [110/1] via fe80::5054:ff:fef2:a625, 00:03:00, GigabitEthernet0/0/0/1
        O    2001:db8:5354::8/128
        [110/1] via fe80::5054:ff:fef2:a625, 00:03:00, GigabitEthernet0/0/0/1
        O    2001:db8:5555::8/128
        [110/1] via fe80::5054:ff:fef2:a625, 00:03:00, GigabitEthernet0/0/0/1
        O    2001:db8:6666::8/128
        [110/1] via fe80::5054:ff:fef2:a625, 00:03:00, GigabitEthernet0/0/0/1
        O    2001:db8:7654::8/128
        [110/1] via fe80::5054:ff:fef2:a625, 00:03:00, GigabitEthernet0/0/0/1
        O    2001:db8:7777::8/128
        [110/1] via fe80::5054:ff:fef2:a625, 00:03:00, GigabitEthernet0/0/0/1
        O    2001:db8:9843::8/128
        [110/1] via fe80::5054:ff:fef2:a625, 00:03:00, GigabitEthernet0/0/0/1
        C    2001:db8:abcd::/64 is directly connected,
        00:07:43, GigabitEthernet0/0/0/1
        L    2001:db8:abcd::1/128 is directly connected,
        00:07:43, GigabitEthernet0/0/0/1
        C    2001:db8:50e0:7b33::/64 is directly connected,
        00:08:31, MgmtEth0/RP0/CPU0/0
        L    2001:db8:50e0:7b33:5054:ff:fe43:e2ee/128 is directly connected,
        00:08:31, MgmtEth0/RP0/CPU0/0   
    '''
    }

    golden_parsed_output9 = {
        'vrf': {
            'default': {
                'address_family': {
                    'ipv6': {
                        'routes': {
                            '2001:db8:1234::8/128': {
                                'active': True,
                                'metric': 1,
                                'next_hop': {
                                    'next_hop_list': {
                                        1: {
                                            'index': 1,
                                            'next_hop': 'fe80::5054:ff:fef2:a625',
                                            'outgoing_interface': 'GigabitEthernet0/0/0/1',
                                            'updated': '00:03:00'
                                        }
                                    }
                                },
                                'route': '2001:db8:1234::8/128',
                                'route_preference': 110,
                                'source_protocol': 'ospf',
                                'source_protocol_codes': 'O'
                            },
                            '2001:db8:1579::8/128': {
                                'active': True,
                                'metric': 1,
                                'next_hop': {
                                    'next_hop_list': {
                                        1: {
                                            'index': 1,
                                            'next_hop': 'fe80::5054:ff:fef2:a625',
                                            'outgoing_interface': 'GigabitEthernet0/0/0/1',
                                            'updated': '00:03:00'
                                        }
                                    }
                                },
                                'route': '2001:db8:1579::8/128',
                                'route_preference': 110,
                                'source_protocol': 'ospf',
                                'source_protocol_codes': 'O'
                            },
                            '2001:db8:1981::8/128': {
                                'active': True,
                                'metric': 1,
                                'next_hop': {
                                    'next_hop_list': {
                                        1: {
                                            'index': 1,
                                            'next_hop': 'fe80::5054:ff:fef2:a625',
                                            'outgoing_interface': 'GigabitEthernet0/0/0/1',
                                            'updated': '00:03:00'
                                        }
                                    }
                                },
                                'route': '2001:db8:1981::8/128',
                                'route_preference': 110,
                                'source_protocol': 'ospf',
                                'source_protocol_codes': 'O'
                            },
                            '2001:db8:2222::8/128': {
                                'active': True,
                                'metric': 1,
                                'next_hop': {
                                    'next_hop_list': {
                                        1: {
                                            'index': 1,
                                            'next_hop': 'fe80::5054:ff:fef2:a625',
                                            'outgoing_interface': 'GigabitEthernet0/0/0/1',
                                            'updated': '00:03:00'
                                        }
                                    }
                                },
                                'route': '2001:db8:2222::8/128',
                                'route_preference': 110,
                                'source_protocol': 'ospf',
                                'source_protocol_codes': 'O'
                            },
                            '2001:db8:3456::8/128': {
                                'active': True,
                                'metric': 1,
                                'next_hop': {
                                    'next_hop_list': {
                                        1: {
                                            'index': 1,
                                            'next_hop': 'fe80::5054:ff:fef2:a625',
                                            'outgoing_interface': 'GigabitEthernet0/0/0/1',
                                            'updated': '00:03:00'
                                        }
                                    }
                                },
                                'route': '2001:db8:3456::8/128',
                                'route_preference': 110,
                                'source_protocol': 'ospf',
                                'source_protocol_codes': 'O'
                            },
                            '2001:db8:4021::8/128': {
                                'active': True,
                                'metric': 1,
                                'next_hop': {
                                    'next_hop_list': {
                                        1: {
                                            'index': 1,
                                            'next_hop': 'fe80::5054:ff:fef2:a625',
                                            'outgoing_interface': 'GigabitEthernet0/0/0/1',
                                            'updated': '00:03:00'
                                        }
                                    }
                                },
                                'route': '2001:db8:4021::8/128',
                                'route_preference': 110,
                                'source_protocol': 'ospf',
                                'source_protocol_codes': 'O'
                            },
                            '2001:db8:5354::8/128': {
                                'active': True,
                                'metric': 1,
                                'next_hop': {
                                    'next_hop_list': {
                                        1: {
                                            'index': 1,
                                            'next_hop': 'fe80::5054:ff:fef2:a625',
                                            'outgoing_interface': 'GigabitEthernet0/0/0/1',
                                            'updated': '00:03:00'
                                        }
                                    }
                                },
                                'route': '2001:db8:5354::8/128',
                                'route_preference': 110,
                                'source_protocol': 'ospf',
                                'source_protocol_codes': 'O'
                            },
                            '2001:db8:5555::8/128': {
                                'active': True,
                                'metric': 1,
                                'next_hop': {
                                    'next_hop_list': {
                                        1: {
                                            'index': 1,
                                            'next_hop': 'fe80::5054:ff:fef2:a625',
                                            'outgoing_interface': 'GigabitEthernet0/0/0/1',
                                            'updated': '00:03:00'
                                        }
                                    }
                                },
                                'route': '2001:db8:5555::8/128',
                                'route_preference': 110,
                                'source_protocol': 'ospf',
                                'source_protocol_codes': 'O'
                            },
                            '2001:db8:6666::8/128': {
                                'active': True,
                                'metric': 1,
                                'next_hop': {
                                    'next_hop_list': {
                                        1: {
                                            'index': 1,
                                            'next_hop': 'fe80::5054:ff:fef2:a625',
                                            'outgoing_interface': 'GigabitEthernet0/0/0/1',
                                            'updated': '00:03:00'
                                        }
                                    }
                                },
                                'route': '2001:db8:6666::8/128',
                                'route_preference': 110,
                                'source_protocol': 'ospf',
                                'source_protocol_codes': 'O'
                            },
                            '2001:db8:7654::8/128': {
                                'active': True,
                                'metric': 1,
                                'next_hop': {
                                    'next_hop_list': {
                                        1: {
                                            'index': 1,
                                            'next_hop': 'fe80::5054:ff:fef2:a625',
                                            'outgoing_interface': 'GigabitEthernet0/0/0/1',
                                            'updated': '00:03:00'
                                        }
                                    }
                                },
                                'route': '2001:db8:7654::8/128',
                                'route_preference': 110,
                                'source_protocol': 'ospf',
                                'source_protocol_codes': 'O'
                            },
                            '2001:db8:7777::8/128': {
                                'active': True,
                                'metric': 1,
                                'next_hop': {
                                    'next_hop_list': {
                                        1: {
                                            'index': 1,
                                            'next_hop': 'fe80::5054:ff:fef2:a625',
                                            'outgoing_interface': 'GigabitEthernet0/0/0/1',
                                            'updated': '00:03:00'
                                        }
                                    }
                                },
                                'route': '2001:db8:7777::8/128',
                                'route_preference': 110,
                                'source_protocol': 'ospf',
                                'source_protocol_codes': 'O'
                            },
                            '2001:db8:9843::8/128': {
                                'active': True,
                                'metric': 1,
                                'next_hop': {
                                    'next_hop_list': {
                                        1: {
                                            'index': 1,
                                            'next_hop': 'fe80::5054:ff:fef2:a625',
                                            'outgoing_interface': 'GigabitEthernet0/0/0/1',
                                            'updated': '00:03:00'
                                        }
                                    }
                                },
                                'route': '2001:db8:9843::8/128',
                                'route_preference': 110,
                                'source_protocol': 'ospf',
                                'source_protocol_codes': 'O'
                            },
                            '2001:db8:abcd::/64': {
                                'active': True,
                                'next_hop': {
                                    'outgoing_interface': {
                                        'GigabitEthernet0/0/0/1': {
                                            'outgoing_interface': 'GigabitEthernet0/0/0/1',
                                            'updated': '00:07:43'
                                        }
                                    }
                                },
                                'route': '2001:db8:abcd::/64',
                                'source_protocol': 'connected',
                                'source_protocol_codes': 'C'
                            },
                            '2001:db8:abcd::1/128': {
                                'active': True,
                                'next_hop': {
                                    'outgoing_interface': {
                                        'GigabitEthernet0/0/0/1': {
                                            'outgoing_interface': 'GigabitEthernet0/0/0/1',
                                            'updated': '00:07:43'
                                        }
                                    }
                                },
                                'route': '2001:db8:abcd::1/128',
                                'source_protocol': 'local',
                                'source_protocol_codes': 'L'
                            },
                            '2001:db8:50e0:7b33:5054:ff:fe43:e2ee/128': {
                                'active': True,
                                'next_hop': {
                                    'outgoing_interface': {
                                        'MgmtEth0/RP0/CPU0/0': {
                                            'outgoing_interface': 'MgmtEth0/RP0/CPU0/0',
                                            'updated': '00:08:31'
                                        }
                                    }
                                },
                                'route': '2001:db8:50e0:7b33:5054:ff:fe43:e2ee/128',
                                'source_protocol': 'local',
                                'source_protocol_codes': 'L'
                            },
                            '2001:db8:50e0:7b33::/64': {
                                'active': True,
                                'next_hop': {
                                    'outgoing_interface': {
                                        'MgmtEth0/RP0/CPU0/0': {
                                            'outgoing_interface': 'MgmtEth0/RP0/CPU0/0',
                                            'updated': '00:08:31'
                                        }
                                    }
                                },
                                'route': '2001:db8:50e0:7b33::/64',
                                'source_protocol': 'connected',
                                'source_protocol_codes': 'C'
                            },
                            '::/0': {
                                'active': True,
                                'metric': 0,
                                'next_hop': {
                                    'next_hop_list': {
                                        1: {
                                            'index': 1,
                                            'next_hop': 'fe80::10ff:fe04:209e',
                                            'outgoing_interface': 'MgmtEth0/RP0/CPU0/0',
                                            'updated': '00:08:31'
                                        }
                                    }
                                },
                                'route': '::/0',
                                'route_preference': 2,
                                'source_protocol': 'application route',
                                'source_protocol_codes': 'a*'
                            }
                        }
                    },
                },
                'last_resort': {
                    'gateway': 'fe80::10ff:fe04:209e',
                    'to_network': '::'
                },
            },
        }
    }

    golden_output_10 = {'execute.return_value': '''
        RP/0/RSP1/CPU0:ASR-01#show route ipv6
        Wed Sep  9 16:23:10.848 UTC
        
        Codes: C - connected, S - static, R - RIP, B - BGP, (>) - Diversion path
            D - EIGRP, EX - EIGRP external, O - OSPF, IA - OSPF inter area
            N1 - OSPF NSSA external type 1, N2 - OSPF NSSA external type 2
            E1 - OSPF external type 1, E2 - OSPF external type 2, E - EGP
            i - ISIS, L1 - IS-IS level-1, L2 - IS-IS level-2
            ia - IS-IS inter area, su - IS-IS summary null, * - candidate default
            U - per-user static route, o - ODR, L - local, G  - DAGR, l - LISP
            A - access/subscriber, a - Application route
            M - mobile route, r - RPL, (!) - FRR Backup path
        
        Gateway of last resort is fe80::226:88ff:fe55:6f17 to network ::
        
        i*L2 ::/0 
            [115/11] via fe80::226:88ff:fe55:6f17, 00:00:10, TenGigE0/0/0/1
        L    2001:db8:4:4::1/128 is directly connected,
            00:54:19, Loopback60
        C    2001:0:10:204:0:30::/126 is directly connected,
            00:54:06, Bundle-Ether10
        L    2001:0:10:204:0:30:0:2/128 is directly connected,
            00:54:06, Bundle-Ether10
        i L2 2001:0:10:204:0:33::/126 
            [115/11] via fe80::226:88ff:fe55:6f17, 00:53:18, TenGigE0/0/0/1
        i L2 2001:db8:1b7f:8e5c::8/128 
            [115/11] via fe80::226:88ff:fe55:6f17, 00:53:18, TenGigE0/0/0/1
        C    fc00:a0:1::/64 is directly connected,
            00:54:18, TenGigE0/0/0/0
        L    fc00:a0:1::2/128 is directly connected,
            00:54:18, TenGigE0/0/0/0
        i L2 fc00:a0:1:216::1/128 
            [115/20] via fe80::464c:a8ff:fe96:a25f, 00:53:55, Bundle-Ether10
        i L2 fc00:a0:2::/64 
            [115/11] via fe80::226:88ff:fe55:6f17, 00:53:18, TenGigE0/0/0/1
        C    fc00:a0:5::/64 is directly connected,
            00:54:18, TenGigE0/0/0/1
        L    fc00:a0:5::2/128 is directly connected,
            00:54:18, TenGigE0/0/0/1
        RP/0/RSP1/CPU0:ASR-01#
    '''
    }
    
    golden_parsed_output_10 = {
        'vrf': {
            'default': {
                'address_family': {
                    'ipv6': {
                        'routes': {
                            '2001:0:10:204:0:30:0:2/128': {
                                'active': True,
                                'next_hop': {
                                    'outgoing_interface': {
                                        'Bundle-Ether10': {
                                            'outgoing_interface': 'Bundle-Ether10',
                                            'updated': '00:54:06'
                                        }
                                    }
                                },
                                'route': '2001:0:10:204:0:30:0:2/128',
                                'source_protocol': 'local',
                                'source_protocol_codes': 'L'
                            },
                            '2001:0:10:204:0:30::/126': {
                                'active': True,
                                'next_hop': {
                                    'outgoing_interface': {
                                        'Bundle-Ether10': {
                                            'outgoing_interface': 'Bundle-Ether10',
                                            'updated': '00:54:06'
                                        }
                                    }
                                },
                                'route': '2001:0:10:204:0:30::/126',
                                'source_protocol': 'connected',
                                'source_protocol_codes': 'C'
                            },
                            '2001:0:10:204:0:33::/126': {
                                'active': True,
                                'metric': 11,
                                'next_hop': {
                                    'next_hop_list': {
                                        1: {
                                            'index': 1,
                                            'next_hop': 'fe80::226:88ff:fe55:6f17',
                                            'outgoing_interface': 'TenGigE0/0/0/1',
                                            'updated': '00:53:18'
                                        }
                                    }
                                },
                                'route': '2001:0:10:204:0:33::/126',
                                'route_preference': 115,
                                'source_protocol': 'isis',
                                'source_protocol_codes': 'i '
                                                        'L2'
                        },
                        '2001:db8:1b7f:8e5c::8/128': {
                            'active': True,
                            'metric': 11,
                            'next_hop': {
                                'next_hop_list': {
                                    1: {
                                        'index': 1,
                                        'next_hop': 'fe80::226:88ff:fe55:6f17',
                                        'outgoing_interface': 'TenGigE0/0/0/1',
                                        'updated': '00:53:18'
                                    }
                                }
                            },
                            'route': '2001:db8:1b7f:8e5c::8/128',
                            'route_preference': 115,
                            'source_protocol': 'isis',
                            'source_protocol_codes': 'i '
                                                    'L2'
                        },
                        '2001:db8:4:4::1/128': {
                            'active': True,
                            'next_hop': {
                                'outgoing_interface': {
                                    'Loopback60': {
                                        'outgoing_interface': 'Loopback60',
                                        'updated': '00:54:19'
                                    }
                                }
                            },
                            'route': '2001:db8:4:4::1/128',
                            'source_protocol': 'local',
                            'source_protocol_codes': 'L'
                        },
                        '::/0': {
                            'active': True,
                            'metric': 11,
                            'next_hop': {
                                'next_hop_list': {
                                    1: {
                                        'index': 1,
                                        'next_hop': 'fe80::226:88ff:fe55:6f17',
                                        'outgoing_interface': 'TenGigE0/0/0/1',
                                        'updated': '00:00:10'
                                    }
                                }
                            },
                            'route': '::/0',
                            'route_preference': 115,
                            'source_protocol': 'isis',
                            'source_protocol_codes': 'i* '
                                                    'L2'
                        },
                        'fc00:a0:1:216::1/128': {
                            'active': True,
                            'metric': 20,
                            'next_hop': {
                                'next_hop_list': {
                                    1: {
                                        'index': 1,
                                        'next_hop': 'fe80::464c:a8ff:fe96:a25f',
                                        'outgoing_interface': 'Bundle-Ether10',
                                        'updated': '00:53:55'
                                    }
                                }
                            },
                            'route': 'fc00:a0:1:216::1/128',
                            'route_preference': 115,
                            'source_protocol': 'isis',
                            'source_protocol_codes': 'i '
                                                    'L2'
                        },
                        'fc00:a0:1::/64': {
                            'active': True,
                            'next_hop': {
                                'outgoing_interface': {
                                    'TenGigE0/0/0/0': {
                                        'outgoing_interface': 'TenGigE0/0/0/0',
                                        'updated': '00:54:18'
                                    }
                                }
                            },
                            'route': 'fc00:a0:1::/64',
                            'source_protocol': 'connected',
                            'source_protocol_codes': 'C'
                        },
                        'fc00:a0:1::2/128': {
                            'active': True,
                            'next_hop': {
                                'outgoing_interface': {
                                    'TenGigE0/0/0/0': {
                                        'outgoing_interface': 'TenGigE0/0/0/0',
                                        'updated': '00:54:18'
                                    }
                                }
                            },
                            'route': 'fc00:a0:1::2/128',
                            'source_protocol': 'local',
                            'source_protocol_codes': 'L'
                        },
                        'fc00:a0:2::/64': {
                            'active': True,
                            'metric': 11,
                            'next_hop': {
                                'next_hop_list': {
                                    1: {
                                        'index': 1,
                                        'next_hop': 'fe80::226:88ff:fe55:6f17',
                                        'outgoing_interface': 'TenGigE0/0/0/1',
                                        'updated': '00:53:18'
                                    }
                                }
                            },
                            'route': 'fc00:a0:2::/64',
                            'route_preference': 115,
                            'source_protocol': 'isis',
                            'source_protocol_codes': 'i '
                                                    'L2'
                        },
                        'fc00:a0:5::/64': {
                            'active': True,
                            'next_hop': {
                                'outgoing_interface': {
                                    'TenGigE0/0/0/1': {
                                        'outgoing_interface': 'TenGigE0/0/0/1',
                                        'updated': '00:54:18'
                                    }
                                }
                            },
                            'route': 'fc00:a0:5::/64',
                            'source_protocol': 'connected',
                            'source_protocol_codes': 'C'
                        },
                        'fc00:a0:5::2/128': {
                            'active': True,
                            'next_hop': {
                                'outgoing_interface': {
                                    'TenGigE0/0/0/1': {
                                        'outgoing_interface': 'TenGigE0/0/0/1',
                                        'updated': '00:54:18'
                                    }
                                }
                            },
                            'route': 'fc00:a0:5::2/128',
                            'source_protocol': 'local',
                            'source_protocol_codes': 'L'
                        }
                    }
                }
            },
            'last_resort': {
                'gateway': 'fe80::226:88ff:fe55:6f17',
                'to_network': '::'
                }
            }
        }
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
        self.assertEqual(parsed_output, self.golden_parsed_output_1)

    def test_show_route_ipv6_2(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_2)
        obj = ShowRouteIpv6(device=self.device)
        parsed_output = obj.parse(vrf='all')
        self.assertEqual(parsed_output, self.golden_parsed_output_2)
    
    def test_show_route_4(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_4)
        obj = ShowRouteIpv6(device=self.device)
        parsed_output = obj.parse(vrf='VRF1')
        self.assertEqual(parsed_output, self.golden_parsed_output_4)

    def test_show_route_5(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_5)
        obj = ShowRouteIpv6(device=self.device)
        parsed_output = obj.parse(route='2001:10:23:120::2/128')

        self.assertEqual(parsed_output, self.golden_parsed_output_5)

    def test_show_route_6(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_6)
        obj = ShowRouteIpv6(device=self.device)
        parsed_output = obj.parse(protocol='local')
        self.assertEqual(parsed_output, self.golden_parsed_output_6)
    
    def test_show_route_7(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_7)
        obj = ShowRouteIpv6(device=self.device)
        parsed_output = obj.parse(vrf='VRF1', route='2001:1:1:1::1')
        self.assertEqual(parsed_output, self.golden_parsed_output_7)

    def test_show_route_ipv6_3(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output8)
        obj = ShowRouteIpv6(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output8)

    def test_show_route_ipv6_4(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output9)
        obj = ShowRouteIpv6(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output9)

    def test_show_route_ipv6_10(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_10)
        obj = ShowRouteIpv6(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_10)

if __name__ == '__main__':
    unittest.main()
