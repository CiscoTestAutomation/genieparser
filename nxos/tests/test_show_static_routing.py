import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device

from metaparser.util.exceptions import SchemaEmptyParserError, \
                                       SchemaMissingKeyError

from parser.nxos.show_static_routing import ShowIpStaticRoute

# ============================================
# unit test for 'show ip static-route'
# =============================================
class test_show_ip_static_route(unittest.TestCase):
    '''
       unit test for show ip static-route
    '''
    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}
    golden_output_1 = {'execute.return_value': '''
    R3_nxosv# show ip static-route vrf all

    Static-route for VRF "default"(1)
    IPv4 Unicast Static Routes:
      1.1.1.1/32, configured nh: 10.1.3.1/32 Ethernet1/2
        (installed in urib)
      1.1.1.1/32, configured nh: 20.1.3.1/32 Ethernet1/3
        (installed in urib)
      2.2.2.2/32, configured nh: 10.2.3.2/32 Ethernet1/4
        (installed in urib)
      2.2.2.2/32, configured nh: 20.2.3.2/32 Ethernet1/1
        (installed in urib)


    Static-route for VRF "VRF1"(3)
    IPv4 Unicast Static Routes:
      1.1.1.1/32, configured nh: 0.0.0.0/32 Null0
        (installed in urib)
      1.1.1.1/32, configured nh: 10.1.3.1/32 Ethernet1/2
        (not installed in urib)
      2.2.2.2/32, configured nh: 20.2.3.2/32
        (not installed in urib)
        rnh(installed in urib)
      2.2.2.2/32, configured nh: 20.2.3.2/32 Ethernet1/1
        (not installed in urib)
      2.2.2.2/32, configured nh: 50.2.3.2/32
        (not installed in urib)
        rnh(installed in urib)
    '''
}
    golden_parsed_output_1 = {
        'vrfs':{
            'default':{
                'address_family': {
                    'ipv4': {
                        'routes': {
                            '1.1.1.1/32': {
                                'route': '1.1.1.1/32',
                                'next_hop': {
                                    'next_hop_list': {
                                         1: {
                                             'index': 1,
                                             'active': True,
                                             'next_hop': '10.1.3.1/32',
                                             'outgoing_interface': 'Ethernet1/2',
                                         },
                                        2: {
                                            'index': 2,
                                            'active': True,
                                            'next_hop': '20.1.3.1/32',
                                            'outgoing_interface': 'Ethernet1/3',
                                        },
                                    },
                                },
                            },
                            '2.2.2.2/32': {
                                'route': '2.2.2.2/32',
                                'next_hop': {
                                    'next_hop_list': {
                                        1: {
                                            'index': 1,
                                            'active': True,
                                            'next_hop': '10.2.3.2/32',
                                            'outgoing_interface': 'Ethernet1/4',
                                        },
                                        2: {
                                            'index': 2,
                                            'active': True,
                                            'next_hop': '20.2.3.2/32',
                                            'outgoing_interface': 'Ethernet1/1',
                                        },
                                    },
                                },
                            },
                        },
                    },

                },
            },
            'VRF1': {
                'address_family': {
                    'ipv4': {
                        'routes': {
                            '1.1.1.1/32': {
                                'route': '1.1.1.1/32',
                                'next_hop': {
                                    'next_hop_list': {
                                        1: {
                                            'index': 1,
                                            'active': True,
                                            'next_hop': '0.0.0.0/32',
                                            'outgoing_interface': 'Null0',
                                        },
                                        2: {
                                            'index': 2,
                                            'active': False,
                                            'next_hop': '10.1.3.1/32',
                                            'outgoing_interface': 'Ethernet1/2',
                                        },
                                    },
                                },
                            },
                            '2.2.2.2/32': {
                                'route': '2.2.2.2/32',
                                'next_hop': {
                                    'next_hop_list': {
                                        1: {
                                            'index': 1,
                                            'active': False,
                                            'rnh_active': True,
                                            'next_hop': '20.2.3.2/32',
                                        },
                                        2: {
                                            'index': 2,
                                            'active': False,
                                            'next_hop': '20.2.3.2/32',
                                            'outgoing_interface': 'Ethernet1/1',
                                        },
                                        3: {
                                            'index': 3,
                                            'active': False,
                                            'rnh_active': True,
                                            'next_hop': '50.2.3.2/32',
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
        R3_nxosv# show ip static-route

        Static-route for VRF "default"(1)
        IPv4 Unicast Static Routes:
          1.1.1.1/32, configured nh: 10.1.3.1/32 Ethernet1/2
            (installed in urib)
          2.2.2.2/32, configured nh: 10.2.3.2/32 Ethernet1/4
            (installed in urib)
          2.2.2.2/32, configured nh: 20.2.3.2/32 Ethernet1/1
            (installed in urib)
            '''}

    golden_parsed_output_2 = {
        'vrfs': {
            'default': {
                'address_family': {
                    'ipv4': {
                        'routes': {
                            '1.1.1.1/32': {
                                'route': '1.1.1.1/32',
                                'next_hop': {
                                    'next_hop_list': {
                                        1: {
                                            'index': 1,
                                            'active': True,
                                            'next_hop': '10.1.3.1/32',
                                            'outgoing_interface': 'Ethernet1/2',
                                        },
                                    },
                                },
                            },
                            '2.2.2.2/32': {
                                'route': '2.2.2.2/32',
                                'next_hop': {
                                    'next_hop_list': {
                                        1: {
                                            'index': 1,
                                            'active': True,
                                            'next_hop': '10.2.3.2/32',
                                            'outgoing_interface': 'Ethernet1/4',
                                        },
                                        2: {
                                            'index': 2,
                                            'active': True,
                                            'next_hop': '20.2.3.2/32',
                                            'outgoing_interface': 'Ethernet1/1',
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
        parsed_output = obj.parse(vrf='all')
        self.assertEqual(parsed_output,self.golden_parsed_output_1)

    def test_show_ip_static_route_2(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_2)
        obj = ShowIpStaticRoute(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output_2)
if __name__ == '__main__':
    unittest.main()