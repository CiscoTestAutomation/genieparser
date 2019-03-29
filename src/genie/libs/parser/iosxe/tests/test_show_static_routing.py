import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device

from genie.metaparser.util.exceptions import SchemaEmptyParserError, \
                                       SchemaMissingKeyError

from genie.libs.parser.iosxe.show_static_routing import ShowIpStaticRoute, \
                                             ShowIpv6StaticDetail

# ============================================
# unit test for 'show ip static route'
# =============================================
class test_show_ip_static_route(unittest.TestCase):
    '''
       unit test for show ip static route
    '''
    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}
    golden_output_1 = {'execute.return_value': '''
Codes: M - Manual static, A - AAA download, N - IP NAT, D - DHCP,
   G - GPRS, V - Crypto VPN, C - CASA, P - Channel interface processor,
   B - BootP, S - Service selection gateway
   DN - Default Network, T - Tracking object
   L - TL1, E - OER, I - iEdge
   D1 - Dot1x Vlan Network, K - MWAM Route
   PP - PPP default route, MR - MRIPv6, SS - SSLVPN
   H - IPe Host, ID - IPe Domain Broadcast
   U - User GPRS, TE - MPLS Traffic-eng, LI - LIIN
   IR - ICMP Redirect
Codes in []: A - active, N - non-active, B - BFD-tracked, D - Not Tracked, P - permanent
Static local RIB for default
M  10.1.1.0/24 [1/0] via GigabitEthernet2.2 10.16.0.2 [A]
M              [3/0] via GigabitEthernet1 192.168.1.1 [N]
M  10.186.1.0/24 [3/0] via GigabitEthernet1 192.168.1.1 [A]

    '''
}
    golden_parsed_output_1 = {
        'vrf':{
            'default':{
                'address_family': {
                    'ipv4': {
                        'routes': {
                            '10.1.1.0/24': {
                                'route': '10.1.1.0/24',
                                'next_hop': {
                                    'next_hop_list': {
                                         1: {
                                             'index': 1,
                                             'active': True,
                                             'next_hop': '10.16.0.2',
                                             'outgoing_interface': 'GigabitEthernet2.2',
                                             'preference': 1,
                                         },
                                        2: {
                                            'index': 2,
                                            'active': False,
                                            'next_hop': '192.168.1.1',
                                            'outgoing_interface': 'GigabitEthernet1',
                                            'preference': 3,
                                        },
                                    },
                                },
                            },
                            '10.186.1.0/24': {
                                'route': '10.186.1.0/24',
                                'next_hop': {
                                    'next_hop_list': {
                                        1: {
                                            'index': 1,
                                            'active': True,
                                            'next_hop': '192.168.1.1',
                                            'outgoing_interface': 'GigabitEthernet1',
                                            'preference': 3,
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
    Codes: M - Manual static, A - AAA download, N - IP NAT, D - DHCP,
       G - GPRS, V - Crypto VPN, C - CASA, P - Channel interface processor,
       B - BootP, S - Service selection gateway
       DN - Default Network, T - Tracking object
       L - TL1, E - OER, I - iEdge
       D1 - Dot1x Vlan Network, K - MWAM Route
       PP - PPP default route, MR - MRIPv6, SS - SSLVPN
       H - IPe Host, ID - IPe Domain Broadcast
       U - User GPRS, TE - MPLS Traffic-eng, LI - LIIN
       IR - ICMP Redirect
    Codes in []: A - active, N - non-active, B - BFD-tracked, D - Not Tracked, P - permanent
    Static local RIB for VRF1
    M  10.16.2.2/32 [1/0] via GigabitEthernet0/0 10.1.2.2 [A]
    M             [2/0] via GigabitEthernet0/1 10.186.2.2 [N]
    M             [3/0] via 10.186.2.2 [N]
    M  10.36.3.3/32 [1/0] via GigabitEthernet0/2 [A]
    M             [1/0] via GigabitEthernet0/3 [A]
    '''
    }
    golden_parsed_output_2 = {
        'vrf': {
            'VRF1': {
                'address_family': {
                    'ipv4': {
                        'routes': {
                            '10.16.2.2/32': {
                                'route': '10.16.2.2/32',
                                'next_hop': {
                                    'next_hop_list': {
                                        1: {
                                            'index': 1,
                                            'active': True,
                                            'next_hop': '10.1.2.2',
                                            'outgoing_interface': 'GigabitEthernet0/0',
                                            'preference': 1,
                                        },
                                        2: {
                                            'index': 2,
                                            'active': False,
                                            'next_hop': '10.186.2.2',
                                            'outgoing_interface': 'GigabitEthernet0/1',
                                            'preference': 2,
                                        },
                                        3: {
                                            'index': 3,
                                            'active': False,
                                            'next_hop': '10.186.2.2',
                                            'preference': 3,
                                        },
                                    },
                                },
                            },
                            '10.36.3.3/32': {
                                'route': '10.36.3.3/32',
                                'next_hop': {
                                    'outgoing_interface': {
                                        'GigabitEthernet0/2': {
                                            'active': True,
                                            'outgoing_interface': 'GigabitEthernet0/2',
                                            'preference': 1,
                                        },
                                        'GigabitEthernet0/3': {
                                            'active': True,
                                            'outgoing_interface': 'GigabitEthernet0/3',
                                            'preference': 1,
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
        obj = ShowIpStaticRoute(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()


    def test_show_ip_static_route_1(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_1)
        obj = ShowIpStaticRoute(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output_1)

    def test_show_ip_static_route_2(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_2)
        obj = ShowIpStaticRoute(device=self.device)
        parsed_output = obj.parse(vrf='VRF1')
        self.assertEqual(parsed_output, self.golden_parsed_output_2)

# ============================================
# unit test for 'show ipv6 static detail'
# =============================================
class test_show_ipv6_static_detail(unittest.TestCase):
    '''
       unit test for show ipv6 static detail
    '''
    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}
    golden_output_detail_1 = {'execute.return_value': '''
R1_iosv#show ipv6 static detail
IPv6 Static routes Table - default
Codes: * - installed in RIB, u/m - Unicast/Multicast only
       U - Per-user Static route
       N - ND Static route
       M - MIP Static route
       P - DHCP-PD Static route
       R - RHI Static route
    2001:2:2:2::2/128 via 2001:10:1:2::2, distance 3
     Resolves to 1 paths (max depth 1)
     via GigabitEthernet0/0
*   2001:2:2:2::2/128 via 2001:20:1:2::2, GigabitEthernet0/1, distance 1
    2001:2:2:2::2/128 via 2001:10:1:2::2, GigabitEthernet0/0, distance 11, tag 100
     Rejected by routing table
     Tracked object 1 is Up
*   2001:3:3:3::3/128 via GigabitEthernet0/3, distance 1
*   2001:3:3:3::3/128 via GigabitEthernet0/2, distance 1
    '''
}
    golden_parsed_output_detail_1 = {
        'vrf':{
            'default':{
                'address_family': {
                    'ipv6': {
                        'routes': {
                            '2001:2:2:2::2/128': {
                                'route': '2001:2:2:2::2/128',
                                'next_hop': {
                                    'next_hop_list': {
                                         1: {
                                             'index': 1,
                                             'active': False,
                                             'next_hop': '2001:10:1:2::2',
                                             'resolved_outgoing_interface': 'GigabitEthernet0/0',
                                             'resolved_paths_number': 1,
                                             'max_depth': 1,
                                             'preference': 3,
                                         },
                                        2: {
                                            'index': 2,
                                            'next_hop': '2001:20:1:2::2',
                                            'active': True,
                                            'outgoing_interface': 'GigabitEthernet0/1',
                                            'preference': 1,
                                        },
                                        3: {
                                            'index': 3,
                                            'active': False,
                                            'next_hop': '2001:10:1:2::2',
                                            'outgoing_interface': 'GigabitEthernet0/0',
                                            'rejected_by':'routing table',
                                            'preference': 11,
                                            'tag': 100,
                                            'track': 1,
                                            'track_state': 'up',
                                        },
                                    },
                                },
                            },
                            '2001:3:3:3::3/128': {
                                'route': '2001:3:3:3::3/128',
                                'next_hop': {
                                    'outgoing_interface': {
                                        'GigabitEthernet0/3': {
                                            'outgoing_interface': 'GigabitEthernet0/3',
                                            'active': True,
                                            'preference': 1,
                                        },
                                        'GigabitEthernet0/2': {
                                            'outgoing_interface': 'GigabitEthernet0/2',
                                            'active': True,
                                            'preference': 1,
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


    golden_output_detail_2 = {'execute.return_value':'''
    R1_iosv#show ipv6 static vrf VRF1 detail
    IPv6 Static routes Table - VRF1
    Codes: * - installed in RIB, u/m - Unicast/Multicast only
           U - Per-user Static route
           N - ND Static route
           M - MIP Static route
           P - DHCP-PD Static route
           R - RHI Static route
    *   2001:2:2:2::2/128 via Null0, distance 2
    *   2001:3:3:3::3/128 via Null0, distance 3
    '''
    }
    golden_parsed_output_detail_2 = {
        'vrf': {
            'VRF1': {
                'address_family': {
                    'ipv6': {
                        'routes': {
                            '2001:2:2:2::2/128': {
                                'route': '2001:2:2:2::2/128',
                                'next_hop': {
                                    'outgoing_interface': {
                                        'Null0': {
                                            'outgoing_interface': 'Null0',
                                            'active': True,
                                            'preference': 2,
                                        },
                                    },
                                },
                            },
                            '2001:3:3:3::3/128': {
                                'route': '2001:3:3:3::3/128',
                                'next_hop': {
                                    'outgoing_interface': {
                                        'Null0': {
                                            'outgoing_interface': 'Null0',
                                            'active': True,
                                            'preference': 3,
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

    def test_empty_detail_1(self):
        self.device = Mock(**self.empty_output)
        obj = ShowIpv6StaticDetail(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()


    def test_show_ip_static_detail_1(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_detail_1)
        obj = ShowIpv6StaticDetail(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output_detail_1)

    def test_show_ip_static_route_2(self):
         self.maxDiff = None
         self.device = Mock(**self.golden_output_detail_2)
         obj = ShowIpv6StaticDetail(device=self.device)
         parsed_output = obj.parse(vrf='VRF1')
         self.assertEqual(parsed_output, self.golden_parsed_output_detail_2)

if __name__ == '__main__':
    unittest.main()