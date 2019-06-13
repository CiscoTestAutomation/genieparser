import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device

from genie.metaparser.util.exceptions import SchemaEmptyParserError, \
                                       SchemaMissingKeyError

from genie.libs.parser.asa.show_route import ShowRoute

# ============================================
# unit test for 'show ip route'
# =============================================
class test_show_ip_route(unittest.TestCase):
    '''
       unit test for show ip route
    '''
    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}
 
    golden_parsed_output = {
        'vrf': {
            'default': {
                'address_family': {
                    'ipv4': {
                        'routes': {
                            '0.0.0.0': {
                                'active': True,
                                'route': '0.0.0.0',
                                'mac_address': '0.0.0.0',
                                'source_protocol_codes': 'S*',
                                'source_protocol': 'static',
                                'next_hop': {
                                    'next_hop_list': {
                                        1: {
                                            'index': 1,
                                            'next_hop': '10.16.251.1',
                                            'outgoing_interface': 'outside'
                                        },
                                        2: {
                                            'index': 2,
                                            'next_hop': '10.16.251.2',
                                            'outgoing_interface': 'pod1000'
                                        }
                                    }
                                }
                            },
                            '0.0.0.1': {
                                'active': True,
                                'route': '0.0.0.1',
                                'mac_address': '0.0.0.0',
                                'source_protocol_codes': 'S',
                                'source_protocol': 'static',
                                'route_preference': 10,
                                'metric': 5,
                                'next_hop': {
                                    'next_hop_list': {
                                        1: {
                                            'index': 1,
                                            'next_hop': '10.16.255.1',
                                            'outgoing_interface': 'outside'
                                        },
                                        2: {
                                            'index': 2,
                                            'next_hop': '10.16.255.2',
                                            'outgoing_interface': 'pod1001'
                                        },
                                        3: {
                                            'index': 3,
                                            'next_hop': '10.16.255.3',
                                            'outgoing_interface': 'pod1002'
                                        }
                                    }
                                }
                            },
                            '127.1.0.0': {
                                'active': True,
                                'route': '127.1.0.0',
                                'mac_address': '255.255.0.0',
                                'source_protocol_codes': 'C',
                                'source_protocol': 'connected',
                                'next_hop': {
                                    'outgoing_interface': {
                                        '_internal_loopback': {
                                            'outgoing_interface': '_internal_loopback'
                                        }
                                    }
                                }
                            },
                            '10.86.168.0': {
                                'active': True,
                                'route': '10.86.168.0',
                                'mac_address': '255.255.254.0',
                                'source_protocol_codes': 'C',
                                'source_protocol': 'connected',
                                'next_hop': {
                                    'outgoing_interface': {
                                        'outside': {
                                            'outgoing_interface': 'outside'
                                        }
                                    }
                                }
                            },
                            '192.16.168.251': {
                                'active': True,
                                'route': '192.16.168.251',
                                'mac_address': '255.255.255.255',
                                'source_protocol_codes': 'L',
                                'source_protocol': 'local',
                                'next_hop': {
                                    'outgoing_interface': {
                                        'pod2000': {
                                            'outgoing_interface': 'pod2000'
                                        },
                                        'pod2002': {
                                            'outgoing_interface': 'pod2002'
                                        }
                                    }
                                }
                            },
                            '192.168.0.1': {            
                                'active': True,
                                'route': '192.168.0.1',
                                'mac_address': '255.255.255.255',
                                'source_protocol_codes': 'V',
                                'source_protocol': 'vpn',
                                'next_hop': {
                                    'outgoing_interface': {
                                        'admin': {
                                            'outgoing_interface': 'admin'
                                        }
                                    }
                                }
                            },
                            '172.10.16.251': {
                                'active': True,
                                'route': '172.10.16.251',
                                'mac_address': '255.255.255.255',
                                'source_protocol_codes': 'L',
                                'source_protocol': 'local',
                                'next_hop': {
                                    'outgoing_interface': {
                                        'pod2500': {
                                            'outgoing_interface': 'pod2500'
                                        }
                                    }
                                }
                            },
                            '172.10.16.255': {
                                'active': True,
                                'route': '172.10.16.255',
                                'mac_address': '255.255.255.0',
                                'source_protocol_codes': 'C',
                                'source_protocol': 'connected',
                                'next_hop': {
                                    'outgoing_interface': {
                                        'pod3000': {
                                            'outgoing_interface': 'pod3000'
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

    golden_output = {'execute.return_value': '''
        ciscoasa/admin(config)# show route
         
        Codes: L - Local, C - connected, S - static, I - IGRP, R - RIP, M - mobile, B - BGP
        D - EIGRP, E - EGP, EX - EIGRP external, O - OSPF, I - IGRP, IA - OSPF inter area
        N1 - OSPF NSSA external type 1, N2 - OSPF NSSA external type 2
        E1 - OSPF external type 1, E2 - OSPF external type 2, E - EGP
        i - IS-IS, L1 - IS-IS level-1, L2 - IS-IS level-2, ia - IS-IS inter area
        * - candidate default, su - IS-IS summary, U - per-user static route, o - ODR
        P - periodic downloaded static route, + - replicated route
         
        Gateway of last resort is 10.16.251.1 to network 0.0.0.0
        

        S* 0.0.0.0 0.0.0.0 via 10.16.251.1, outside
                           via 10.16.251.2, pod1000
        S 0.0.0.1 0.0.0.0 [10/5] via 10.16.255.1, outside
                                via 10.16.255.2, pod1001
                                via 10.16.255.3, pod1002
        C 127.1.0.0 255.255.0.0 is directly connected, _internal_loopback
        C 10.86.168.0 255.255.254.0 is directly connected, outside
        L 192.16.168.251 255.255.255.255 is directly connected, pod2000
                                        is directly connected, pod2002
        V        192.168.0.1 255.255.255.255
                                connected by VPN (advertised), admin
        L        172.10.16.251 255.255.255.255 is directly connected, pod2500
        C        172.10.16.255 255.255.255.0 
                                is directly connected, pod3000
          '''}

    def test_empty_1(self):
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

if __name__ == '__main__':
    unittest.main()