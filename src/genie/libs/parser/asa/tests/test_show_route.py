import unittest
from unittest.mock import Mock

from ats.topology import Device

from genie.metaparser.util.exceptions import SchemaEmptyParserError

from genie.libs.parser.asa.show_route import ShowRoute

# ============================================
# unit test for 'show route'
# =============================================
class test_show_route(unittest.TestCase):
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
                                            'next_hop': '20.20.2.2',
                                            'outgoing_interface': 'outside'
                                        },
                                        2: {
                                            'index': 2,
                                            'next_hop': '20.20.2.2',
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
                                            'next_hop': '20.20.2.2',
                                            'outgoing_interface': 'outside'
                                        },
                                        2: {
                                            'index': 2,
                                            'next_hop': '20.20.2.2',
                                            'outgoing_interface': 'pod1001'
                                        },
                                        3: {
                                            'index': 3,
                                            'next_hop': '20.20.2.2',
                                            'outgoing_interface': 'pod1002'
                                        }
                                    }
                                }
                            },
                            '10.10.1.1': {
                                'active': True,
                                'route': '10.10.1.1',
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
                            '10.10.1.1': {
                                'active': True,
                                'route': '10.10.1.1',
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
                            '10.10.1.1': {
                                'active': True,
                                'route': '10.10.1.1',
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
                            '10.10.1.1': {            
                                'active': True,
                                'route': '10.10.1.1',
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
                            '10.10.1.1': {
                                'active': True,
                                'route': '10.10.1.1',
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
                            '10.10.1.1.255': {
                                'active': True,
                                'route': '10.10.1.1.255',
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
         
        Codes: L - local, C - connected, S - static, R - RIP, M - mobile, B - BGP
               D - EIGRP, EX - EIGRP external, O - OSPF, IA - OSPF inter area
               N1 - OSPF NSSA external type 1, N2 - OSPF NSSA external type 2
               E1 - OSPF external type 1, E2 - OSPF external type 2, V - VPN
               i - IS-IS, su - IS-IS summary, L1 - IS-IS level-1, L2 - IS-IS level-2
               ia - IS-IS, * - candidate default, U - per-user static route
               o - ODR, P - periodic downloaded static route, + - replicated route
         
        Gateway of last resort is 20.20.2.2 to network 0.0.0.0
        

        S* 10.10.1.1 0.0.0.0 via 20.20.2.2, outside
                           via 20.20.2.2, pod1000
        S 10.10.1.1 0.0.0.0 [10/5] via 20.20.2.2, outside
                                via 20.20.2.2, pod1001
                                via 20.20.2.2, pod1002
        C 10.10.1.1 255.255.0.0 is directly connected, _internal_loopback
        C 10.10.1.1 255.255.254.0 is directly connected, outside
        L 10.10.1.1 255.255.255.255 is directly connected, pod2000
                                        is directly connected, pod2002
        V        10.10.1.1 255.255.255.255
                                connected by VPN (advertised), admin
        L        10.10.1.1 255.255.255.255 is directly connected, pod2500
        C        10.10.1.1.255 255.255.255.0 
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