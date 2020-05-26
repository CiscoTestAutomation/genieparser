import unittest
from unittest.mock import Mock

# ATS
from pyats.topology import Device

from genie.metaparser.util.exceptions import SchemaEmptyParserError, \
    SchemaMissingKeyError

from genie.libs.parser.asa.show_route import ShowRoute


# ============================================
# unit test for 'show route'
# =============================================


class test_show_ip_route(unittest.TestCase):
    '''
       unit test for show route
    '''

    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}
    golden_parsed_output = {
        'vrf': {
            'default': {
                'address_family': {
                    'ipv4': {
                        'routes': {
                            '0.0.0.0/0': {
                                'active': True,
                                'candidate_default': True,
                                'next_hop': {
                                    'next_hop_list': {
                                        1: {
                                            'index': 1,
                                            'next_hop': '10.16.251.1',
                                            'outgoing_interface_name': 'outside',
                                        },
                                        2: {
                                            'index': 2,
                                            'next_hop': '10.16.251.2',
                                            'outgoing_interface_name': 'pod1000',
                                        },
                                    },
                                },
                                'route': '0.0.0.0/0',
                                'route_preference': 10,
                                'source_protocol': 'static',
                                'source_protocol_codes': 'S',
                            },
                            '0.0.0.1/0': {
                                'active': True,
                                'candidate_default': False,
                                'metric': 5,
                                'next_hop': {
                                    'next_hop_list': {
                                        1: {
                                            'index': 1,
                                            'next_hop': '10.16.255.1',
                                            'outgoing_interface_name': 'outside',
                                        },
                                        2: {
                                            'index': 2,
                                            'next_hop': '10.16.255.2',
                                            'outgoing_interface_name': 'pod1001',
                                        },
                                        3: {
                                            'index': 3,
                                            'next_hop': '10.16.255.3',
                                            'outgoing_interface_name': 'pod1002',
                                        },
                                    },
                                },
                                'route': '0.0.0.1/0',
                                'route_preference': 10,
                                'source_protocol': 'static',
                                'source_protocol_codes': 'S',
                            },
                            '10.0.0.0/24': {
                                'active': True,
                                'candidate_default': False,
                                'date': '0:19:52',
                                'metric': 30720,
                                'next_hop': {
                                    'outgoing_interface_name': {
                                        'inside': {
                                            'outgoing_interface_name': 'inside',
                                        },
                                    },
                                },
                                'route': '10.0.0.0/24',
                                'route_preference': 90,
                                'source_protocol': 'eigrp',
                                'source_protocol_codes': 'D',
                            },
                            '10.10.1.1/16': {
                                'active': True,
                                'candidate_default': False,
                                'next_hop': {
                                    'outgoing_interface_name': {
                                        '_internal_loopback': {
                                            'outgoing_interface_name': '_internal_loopback',
                                        },
                                    },
                                },
                                'route': '10.10.1.1/16',
                                'source_protocol': 'connected',
                                'source_protocol_codes': 'C',
                            },
                            '10.10.1.2/23': {
                                'active': True,
                                'candidate_default': False,
                                'next_hop': {
                                    'outgoing_interface_name': {
                                        'outside': {
                                            'outgoing_interface_name': 'outside',
                                        },
                                    },
                                },
                                'route': '10.10.1.2/23',
                                'source_protocol': 'connected',
                                'source_protocol_codes': 'C',
                            },
                            '10.10.1.3/32': {
                                'active': True,
                                'candidate_default': False,
                                'next_hop': {
                                    'outgoing_interface_name': {
                                        'pod2002': {
                                            'outgoing_interface_name': 'pod2002',
                                        },
                                    },
                                },
                                'route': '10.10.1.3/32',
                                'source_protocol': 'local',
                                'source_protocol_codes': 'L',
                            },
                            '10.10.1.4/32': {
                                'active': True,
                                'candidate_default': False,
                                'next_hop': {
                                    'outgoing_interface_name': {
                                        'admin': {
                                            'outgoing_interface_name': 'admin',
                                        },
                                    },
                                },
                                'route': '10.10.1.4/32',
                                'source_protocol': 'vpn',
                                'source_protocol_codes': 'V',
                            },
                            '10.10.1.5/32': {
                                'active': True,
                                'candidate_default': False,
                                'next_hop': {
                                    'outgoing_interface_name': {
                                        'pod2500': {
                                            'outgoing_interface_name': 'pod2500',
                                        },
                                    },
                                },
                                'route': '10.10.1.5/32',
                                'source_protocol': 'local',
                                'source_protocol_codes': 'L',
                            },
                            '10.10.1.6/24': {
                                'active': True,
                                'candidate_default': False,
                                'next_hop': {
                                    'outgoing_interface_name': {
                                        'pod3000': {
                                            'outgoing_interface_name': 'pod3000',
                                        },
                                    },
                                },
                                'route': '10.10.1.6/24',
                                'source_protocol': 'connected',
                                'source_protocol_codes': 'C',
                            },
                            '10.121.65.0/24': {
                                'active': True,
                                'candidate_default': False,
                                'date': '7w0d',
                                'metric': 20,
                                'next_hop': {
                                    'next_hop_list': {
                                        1: {
                                            'index': 1,
                                            'next_hop': '10.121.64.35',
                                            'outgoing_interface_name': 'inside',
                                        },
                                        2: {
                                            'index': 2,
                                            'next_hop': '10.121.64.34',
                                            'outgoing_interface_name': 'inside',
                                        },
                                    },
                                },
                                'route': '10.121.65.0/24',
                                'route_preference': 110,
                                'source_protocol': 'ospf',
                                'source_protocol_codes': 'O',
                            },
                            '10.121.67.0/24': {
                                'active': True,
                                'candidate_default': False,
                                'date': '2w1d',
                                'metric': 345856,
                                'next_hop': {
                                    'next_hop_list': {
                                        1: {
                                            'index': 1,
                                            'next_hop': '10.9.193.99',
                                            'outgoing_interface_name': 'esavpn',
                                        },
                                        2: {
                                            'index': 2,
                                            'next_hop': '10.9.193.98',
                                            'outgoing_interface_name': 'esavpn',
                                        },
                                    },
                                },
                                'route': '10.121.67.0/24',
                                'route_preference': 170,
                                'source_protocol': 'eigrp',
                                'source_protocol_codes': 'EX',
                            },
                            '10.121.68.0/24': {
                                'active': True,
                                'candidate_default': False,
                                'date': '2w1d',
                                'metric': 345856,
                                'next_hop': {
                                    'next_hop_list': {
                                        1: {
                                            'index': 1,
                                            'next_hop': '10.9.193.99',
                                            'outgoing_interface_name': 'esavpn',
                                        },
                                        2: {
                                            'index': 2,
                                            'next_hop': '10.9.193.98',
                                            'outgoing_interface_name': 'esavpn',
                                        },
                                    },
                                },
                                'route': '10.121.68.0/24',
                                'route_preference': 170,
                                'source_protocol': 'eigrp',
                                'source_protocol_codes': 'EX',
                            },
                            '10.121.69.0/24': {
                                'active': True,
                                'candidate_default': False,
                                'date': '7w0d',
                                'metric': 20,
                                'next_hop': {
                                    'next_hop_list': {
                                        1: {
                                            'index': 1,
                                            'next_hop': '10.121.64.35',
                                            'outgoing_interface_name': 'inside',
                                        },
                                        2: {
                                            'index': 2,
                                            'next_hop': '10.121.64.34',
                                            'outgoing_interface_name': 'inside',
                                        },
                                    },
                                },
                                'route': '10.121.69.0/24',
                                'route_preference': 110,
                                'source_protocol': 'ospf',
                                'source_protocol_codes': 'O',
                            },
                            '10.121.70.0/24': {
                                'active': True,
                                'candidate_default': False,
                                'date': '2w1d',
                                'metric': 345856,
                                'next_hop': {
                                    'next_hop_list': {
                                        1: {
                                            'index': 1,
                                            'next_hop': '10.9.193.99',
                                            'outgoing_interface_name': 'esavpn',
                                        },
                                        2: {
                                            'index': 2,
                                            'next_hop': '10.9.193.98',
                                            'outgoing_interface_name': 'esavpn',
                                        },
                                    },
                                },
                                'route': '10.121.70.0/24',
                                'route_preference': 170,
                                'source_protocol': 'eigrp',
                                'source_protocol_codes': 'EX',
                            },
                            '10.121.71.0/24': {
                                'active': True,
                                'candidate_default': False,
                                'date': '2w1d',
                                'metric': 345856,
                                'next_hop': {
                                    'next_hop_list': {
                                        1: {
                                            'index': 1,
                                            'next_hop': '10.9.193.99',
                                            'outgoing_interface_name': 'esavpn',
                                        },
                                        2: {
                                            'index': 2,
                                            'next_hop': '10.9.193.98',
                                            'outgoing_interface_name': 'esavpn',
                                        },
                                    },
                                },
                                'route': '10.121.71.0/24',
                                'route_preference': 170,
                                'source_protocol': 'eigrp',
                                'source_protocol_codes': 'EX',
                            },
                            '10.122.3.0/24': {
                                'active': True,
                                'candidate_default': False,
                                'date': '7w0d',
                                'metric': 0,
                                'next_hop': {
                                    'next_hop_list': {
                                        1: {
                                            'index': 1,
                                            'next_hop': '172.25.141.2',
                                        },
                                    },
                                },
                                'route': '10.122.3.0/24',
                                'route_preference': 20,
                                'source_protocol': 'bgp',
                                'source_protocol_codes': 'B',
                            },
                            '10.20.2.64/26': {
                                'active': True,
                                'candidate_default': False,
                                'date': '2d03h',
                                'metric': 1,
                                'next_hop': {
                                    'next_hop_list': {
                                        1: {
                                            'index': 1,
                                            'next_hop': '10.19.1.1',
                                            'outgoing_interface_name': 'wan2',
                                        },
                                    },
                                },
                                'route': '10.20.2.64/26',
                                'route_preference': 110,
                                'source_protocol': 'ospf',
                                'source_protocol_codes': 'E2',
                            },
                            '10.20.58.64/26': {
                                'active': True,
                                'candidate_default': False,
                                'date': '3w6d',
                                'metric': 11,
                                'next_hop': {
                                    'next_hop_list': {
                                        1: {
                                            'index': 1,
                                            'next_hop': '172.20.192.3',
                                            'outgoing_interface_name': 'wan1',
                                        },
                                    },
                                },
                                'route': '10.20.58.64/26',
                                'route_preference': 110,
                                'source_protocol': 'ospf',
                                'source_protocol_codes': 'E2',
                            },
                            '10.30.79.64/26': {
                                'active': True,
                                'candidate_default': False,
                                'date': '1w1d',
                                'metric': 11,
                                'next_hop': {
                                    'next_hop_list': {
                                        1: {
                                            'index': 1,
                                            'next_hop': '10.20.192.3',
                                            'outgoing_interface_name': 'wan3',
                                        },
                                        2: {
                                            'index': 2,
                                            'next_hop': '10.20.192.4',
                                            'outgoing_interface_name': 'wan4',
                                        },
                                    },
                                },
                                'route': '10.30.79.64/26',
                                'route_preference': 110,
                                'source_protocol': 'ospf',
                                'source_protocol_codes': 'E2',
                            },
                            '30.20.8.0/23': {
                                'active': True,
                                'candidate_default': False,
                                'date': '7w0d',
                                'metric': 20,
                                'next_hop': {
                                    'next_hop_list': {
                                        1: {
                                            'index': 1,
                                            'next_hop': '172.20.1.1',
                                            'outgoing_interface_name': 'wan5',
                                        },
                                    },
                                },
                                'route': '30.20.8.0/23',
                                'route_preference': 110,
                                'source_protocol': 'ospf',
                                'source_protocol_codes': 'O',
                            },
                        },
                    },
                },
            },
        },
    }

    golden_output = {'execute.return_value': """ciscoasa/admin(config)# show route

            Codes: L - Local, C - connected, S - static, I - IGRP, R - RIP, M - mobile, B - BGP
            D - EIGRP, E - EGP, EX - EIGRP external, O - OSPF, I - IGRP, IA - OSPF inter area
            N1 - OSPF NSSA external type 1, N2 - OSPF NSSA external type 2
            E1 - OSPF external type 1, E2 - OSPF external type 2, E - EGP
            i - IS-IS, L1 - IS-IS level-1, L2 - IS-IS level-2, ia - IS-IS inter area
            * - candidate default, su - IS-IS summary, U - per-user static route, o - ODR
            P - periodic downloaded static route, + - replicated route

            Gateway of last resort is 10.16.251.1 to network 0.0.0.0


            S* 0.0.0.0 0.0.0.0 [10] via 10.16.251.1, outside
                               via 10.16.251.2, pod1000
            S 0.0.0.1 0.0.0.0 [10/5] via 10.16.255.1, outside
                                    via 10.16.255.2, pod1001
                                    via 10.16.255.3, pod1002
            C 10.10.1.1 255.255.0.0 is directly connected, _internal_loopback
            C 10.10.1.2 255.255.254.0 is directly connected, outside
            B 10.122.3.0 255.255.255.0 [20/0] via 172.25.141.2, 7w0d
            L 10.10.1.3 255.255.255.255 is directly connected, pod2000
                                            is directly connected, pod2002
            V        10.10.1.4 255.255.255.255
                                    connected by VPN (advertised), admin
            L        10.10.1.5 255.255.255.255 is directly connected, pod2500
            C        10.10.1.6 255.255.255.0
                                    is directly connected, pod3000
            O E2     10.20.58.64 255.255.255.192
                       [110/11] via 172.20.192.3, 3w6d, wan1
            O E2     10.20.2.64 255.255.255.192 [110/1] via 10.19.1.1, 2d03h, wan2
            O E2     10.30.79.64 255.255.255.192
                       [110/11] via 10.20.192.3, 1w1d, wan3
                       [110/11] via 10.20.192.4, 1w1d, wan4
            O    30.20.8.0 255.255.254.0 [110/20] via 172.20.1.1, 7w0d, wan5
            D    10.0.0.0 255.255.255.0 [90/30720] via 192.168.1.1, 0:19:52, inside
           O        10.121.65.0 255.255.255.0 [110/20] via 10.121.64.35, 7w0d, inside
                                              [110/20] via 10.121.64.34, 7w0d, inside
           D EX     10.121.67.0 255.255.255.0 [170/345856] via 10.9.193.99, 2w1d, esavpn
                                              [170/345856] via 10.9.193.98, 2w1d, esavpn
           D EX     10.121.68.0 255.255.255.0 [170/345856] via 10.9.193.99, 2w1d, esavpn
                                              [170/345856] via 10.9.193.98, 2w1d, esavpn
           O        10.121.69.0 255.255.255.0 [110/20] via 10.121.64.35, 7w0d, inside
                                              [110/20] via 10.121.64.34, 7w0d, inside
           D EX     10.121.70.0 255.255.255.0 [170/345856] via 10.9.193.99, 2w1d, esavpn
                                              [170/345856] via 10.9.193.98, 2w1d, esavpn
           D EX     10.121.71.0 255.255.255.0 [170/345856] via 10.9.193.99, 2w1d, esavpn
                                              [170/345856] via 10.9.193.98, 2w1d, esavpn            
                """}

    golden_output_2 = {'execute.return_value': '''

       O        10.121.65.0 255.255.255.0 [110/20] via 10.121.64.35, 7w0d, inside
                                          [110/20] via 10.121.64.34, 7w0d, inside
       D EX     10.121.67.0 255.255.255.0 [170/345856] via 10.9.193.99, 2w1d, esavpn
                                          [170/345856] via 10.9.193.98, 2w1d, esavpn
       D EX     10.121.68.0 255.255.255.0 [170/345856] via 10.9.193.99, 2w1d, esavpn
                                          [170/345856] via 10.9.193.98, 2w1d, esavpn
       O        10.121.69.0 255.255.255.0 [110/20] via 10.121.64.35, 7w0d, inside
                                          [110/20] via 10.121.64.34, 7w0d, inside
       D EX     10.121.70.0 255.255.255.0 [170/345856] via 10.9.193.99, 2w1d, esavpn
                                          [170/345856] via 10.9.193.98, 2w1d, esavpn
       D EX     10.121.71.0 255.255.255.0 [170/345856] via 10.9.193.99, 2w1d, esavpn
                                          [170/345856] via 10.9.193.98, 2w1d, esavpn
       '''}

    golden_parsed_output_2 = {
        'vrf': {
            'default': {
                'address_family': {
                    'ipv4': {
                        'routes': {
                            '10.121.65.0/24': {
                                'active': True,
                                'candidate_default': False,
                                'date': '7w0d',
                                'metric': 20,
                                'next_hop': {
                                    'next_hop_list': {
                                        1: {
                                            'index': 1,
                                            'next_hop': '10.121.64.35',
                                            'outgoing_interface_name': 'inside',
                                        },
                                        2: {
                                            'index': 2,
                                            'next_hop': '10.121.64.34',
                                            'outgoing_interface_name': 'inside',
                                        },
                                    },
                                },
                                'route': '10.121.65.0/24',
                                'route_preference': 110,
                                'source_protocol': 'ospf',
                                'source_protocol_codes': 'O',
                            },
                            '10.121.67.0/24': {
                                'active': True,
                                'candidate_default': False,
                                'date': '2w1d',
                                'metric': 345856,
                                'next_hop': {
                                    'next_hop_list': {
                                        1: {
                                            'index': 1,
                                            'next_hop': '10.9.193.99',
                                            'outgoing_interface_name': 'esavpn',
                                        },
                                        2: {
                                            'index': 2,
                                            'next_hop': '10.9.193.98',
                                            'outgoing_interface_name': 'esavpn',
                                        },
                                    },
                                },
                                'route': '10.121.67.0/24',
                                'route_preference': 170,
                                'source_protocol': 'eigrp',
                                'source_protocol_codes': 'EX',
                            },
                            '10.121.68.0/24': {
                                'active': True,
                                'candidate_default': False,
                                'date': '2w1d',
                                'metric': 345856,
                                'next_hop': {
                                    'next_hop_list': {
                                        1: {
                                            'index': 1,
                                            'next_hop': '10.9.193.99',
                                            'outgoing_interface_name': 'esavpn',
                                        },
                                        2: {
                                            'index': 2,
                                            'next_hop': '10.9.193.98',
                                            'outgoing_interface_name': 'esavpn',
                                        },
                                    },
                                },
                                'route': '10.121.68.0/24',
                                'route_preference': 170,
                                'source_protocol': 'eigrp',
                                'source_protocol_codes': 'EX',
                            },
                            '10.121.69.0/24': {
                                'active': True,
                                'candidate_default': False,
                                'date': '7w0d',
                                'metric': 20,
                                'next_hop': {
                                    'next_hop_list': {
                                        1: {
                                            'index': 1,
                                            'next_hop': '10.121.64.35',
                                            'outgoing_interface_name': 'inside',
                                        },
                                        2: {
                                            'index': 2,
                                            'next_hop': '10.121.64.34',
                                            'outgoing_interface_name': 'inside',
                                        },
                                    },
                                },
                                'route': '10.121.69.0/24',
                                'route_preference': 110,
                                'source_protocol': 'ospf',
                                'source_protocol_codes': 'O',
                            },
                            '10.121.70.0/24': {
                                'active': True,
                                'candidate_default': False,
                                'date': '2w1d',
                                'metric': 345856,
                                'next_hop': {
                                    'next_hop_list': {
                                        1: {
                                            'index': 1,
                                            'next_hop': '10.9.193.99',
                                            'outgoing_interface_name': 'esavpn',
                                        },
                                        2: {
                                            'index': 2,
                                            'next_hop': '10.9.193.98',
                                            'outgoing_interface_name': 'esavpn',
                                        },
                                    },
                                },
                                'route': '10.121.70.0/24',
                                'route_preference': 170,
                                'source_protocol': 'eigrp',
                                'source_protocol_codes': 'EX',
                            },
                            '10.121.71.0/24': {
                                'active': True,
                                'candidate_default': False,
                                'date': '2w1d',
                                'metric': 345856,
                                'next_hop': {
                                    'next_hop_list': {
                                        1: {
                                            'index': 1,
                                            'next_hop': '10.9.193.99',
                                            'outgoing_interface_name': 'esavpn',
                                        },
                                        2: {
                                            'index': 2,
                                            'next_hop': '10.9.193.98',
                                            'outgoing_interface_name': 'esavpn',
                                        },
                                    },
                                },
                                'route': '10.121.71.0/24',
                                'route_preference': 170,
                                'source_protocol': 'eigrp',
                                'source_protocol_codes': 'EX',
                            },
                        },
                    },
                },
            },
        },
    }

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowRoute(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output)
        route_obj = ShowRoute(device=self.device)
        parsed_output = route_obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)

    def test_golden_2(self):
        self.device = Mock(**self.golden_output_2)
        route_obj = ShowRoute(device=self.device)
        parsed_output = route_obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_2)


if __name__ == '__main__':
    unittest.main()
