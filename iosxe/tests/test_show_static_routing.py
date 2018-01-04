import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device

from metaparser.util.exceptions import SchemaEmptyParserError, \
                                       SchemaMissingKeyError

from parser.iosxe.show_static_routing import ShowIpStaticRoute

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
M  10.1.1.0/24 [1/0] via GigabitEthernet2.2 4.0.0.2 [A]
M              [3/0] via GigabitEthernet1 192.168.1.1 [N]
M  20.1.1.0/24 [3/0] via GigabitEthernet1 192.168.1.1 [A]

    '''
}
    golden_parsed_output_1 = {
        'vrfs':{
            'default':{
                'address_family': {
                    'ipv4': {
                        'routes': {
                            '10.1.1.0/255.255.255.0': {
                                'route': '10.1.1.0/255.255.255.0',
                                'next_hop': {
                                    'next_hop_list': {
                                         1: {
                                             'index': 1,
                                             'active': True,
                                             'next_hop': '4.0.0.2',
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
                            '20.1.1.0/255.255.255.0': {
                                'route': '20.1.1.0/255.255.255.0',
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
    M  2.2.2.2/32 [1/0] via GigabitEthernet0/0 10.1.2.2 [A]
    M             [2/0] via GigabitEthernet0/1 20.1.2.2 [N]
    M             [3/0] via 20.1.2.2 [N]
    M  3.3.3.3/32 [1/0] via GigabitEthernet0/2 [A]
    M             [1/0] via GigabitEthernet0/3 [A]
    '''
    }
    golden_parsed_output_2 = {
        'vrfs': {
            'VRF1': {
                'address_family': {
                    'ipv4': {
                        'routes': {
                            '2.2.2.2/255.255.255.255': {
                                'route': '2.2.2.2/255.255.255.255',
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
                                            'next_hop': '20.1.2.2',
                                            'outgoing_interface': 'GigabitEthernet0/1',
                                            'preference': 2,
                                        },
                                        3: {
                                            'index': 3,
                                            'active': False,
                                            'next_hop': '20.1.2.2',
                                            'preference': 3,
                                        },
                                    },
                                },
                            },
                            '3.3.3.3/255.255.255.255': {
                                'route': '3.3.3.3/255.255.255.255',
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

if __name__ == '__main__':
    unittest.main()