import unittest
from unittest.mock import Mock

# ATS
from pyats.topology import Device

from genie.metaparser.util.exceptions import SchemaEmptyParserError, \
                                       SchemaMissingKeyError

from genie.libs.parser.nxos.show_static_routing import ShowIpStaticRoute, \
                                            ShowIpv6StaticRoute

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
      10.4.1.1/32, configured nh: 10.1.3.1/32 Ethernet1/2
        (installed in urib)
      10.4.1.1/32, configured nh: 10.186.3.1/32 Ethernet1/3
        (installed in urib)
      10.16.2.2/32, configured nh: 10.2.3.2/32 Ethernet1/4
        (installed in urib)
      10.16.2.2/32, configured nh: 10.229.3.2/32 Ethernet1/1
        (installed in urib)


    Static-route for VRF "VRF1"(3)
    IPv4 Unicast Static Routes:
      10.4.1.1/32, configured nh: 0.0.0.0/32 Null0
        (installed in urib)
      10.4.1.1/32, configured nh: 10.1.3.1/32 Ethernet1/2
        (not installed in urib)
      10.16.2.2/32, configured nh: 10.229.3.2/32
        (not installed in urib)
        rnh(installed in urib)
      10.16.2.2/32, configured nh: 10.229.3.2/32 Ethernet1/1
        (not installed in urib)
      10.16.2.2/32, configured nh: 10.154.3.2/32
        (not installed in urib)
        rnh(installed in urib)
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
                                'next_hop': {
                                    'next_hop_list': {
                                         1: {
                                             'index': 1,
                                             'active': True,
                                             'next_hop': '10.1.3.1',
                                             'next_hop_netmask': '32',
                                             'outgoing_interface': 'Ethernet1/2',
                                         },
                                        2: {
                                            'index': 2,
                                            'active': True,
                                            'next_hop': '10.186.3.1',
                                            'next_hop_netmask': '32',
                                            'outgoing_interface': 'Ethernet1/3',
                                        },
                                    },
                                },
                            },
                            '10.16.2.2/32': {
                                'route': '10.16.2.2/32',
                                'next_hop': {
                                    'next_hop_list': {
                                        1: {
                                            'index': 1,
                                            'active': True,
                                            'next_hop': '10.2.3.2',
                                            'next_hop_netmask': '32',
                                            'outgoing_interface': 'Ethernet1/4',
                                        },
                                        2: {
                                            'index': 2,
                                            'active': True,
                                            'next_hop': '10.229.3.2',
                                            'next_hop_netmask': '32',
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
                            '10.4.1.1/32': {
                                'route': '10.4.1.1/32',
                                'next_hop': {
                                    'next_hop_list': {
                                        1: {
                                            'index': 1,
                                            'active': True,
                                            'next_hop': '0.0.0.0',
                                            'next_hop_netmask': '32',
                                            'outgoing_interface': 'Null0',
                                        },
                                        2: {
                                            'index': 2,
                                            'active': False,
                                            'next_hop': '10.1.3.1',
                                            'next_hop_netmask': '32',
                                            'outgoing_interface': 'Ethernet1/2',
                                        },
                                    },
                                },
                            },
                            '10.16.2.2/32': {
                                'route': '10.16.2.2/32',
                                'next_hop': {
                                    'next_hop_list': {
                                        1: {
                                            'index': 1,
                                            'active': False,
                                            'rnh_active': True,
                                            'next_hop': '10.229.3.2',
                                            'next_hop_netmask': '32',
                                        },
                                        2: {
                                            'index': 2,
                                            'active': False,
                                            'next_hop': '10.229.3.2',
                                            'next_hop_netmask': '32',
                                            'outgoing_interface': 'Ethernet1/1',
                                        },
                                        3: {
                                            'index': 3,
                                            'active': False,
                                            'rnh_active': True,
                                            'next_hop': '10.154.3.2',
                                            'next_hop_netmask': '32',
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
          10.4.1.1/32, configured nh: 10.1.3.1/32 Ethernet1/2
            (installed in urib)
          10.16.2.2/32, configured nh: 10.2.3.2/32 Ethernet1/4
            (installed in urib)
          10.16.2.2/32, configured nh: 10.229.3.2/32 Ethernet1/1
            (installed in urib)
            '''}

    golden_parsed_output_2 = {
        'vrf': {
            'default': {
                'address_family': {
                    'ipv4': {
                        'routes': {
                            '10.4.1.1/32': {
                                'route': '10.4.1.1/32',
                                'next_hop': {
                                    'next_hop_list': {
                                        1: {
                                            'index': 1,
                                            'active': True,
                                            'next_hop': '10.1.3.1',
                                            'next_hop_netmask': '32',
                                            'outgoing_interface': 'Ethernet1/2',
                                        },
                                    },
                                },
                            },
                            '10.16.2.2/32': {
                                'route': '10.16.2.2/32',
                                'next_hop': {
                                    'next_hop_list': {
                                        1: {
                                            'index': 1,
                                            'active': True,
                                            'next_hop': '10.2.3.2',
                                            'next_hop_netmask': '32',
                                            'outgoing_interface': 'Ethernet1/4',
                                        },
                                        2: {
                                            'index': 2,
                                            'active': True,
                                            'next_hop': '10.229.3.2',
                                            'next_hop_netmask': '32',
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

# ============================================
# unit test for 'show ipv6 static-route'
# =============================================
class test_show_ipv6_static_route(unittest.TestCase):
    '''
       unit test for show ipv6 static-route
    '''
    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}
    golden_output_ipv6_1 = {'execute.return_value': '''
    R3_nxosv# show ipv6 static-route
    IPv6 Configured Static Routes for VRF "default"(1)

    2001:1:1:1::1/128 -> 2001:10:1:3::1/128, preference: 1
      nh_vrf(default) reslv_tid 0
      real-next-hop: 2001:10:1:3::1, interface: Ethernet1/2
        rnh(not installed in u6rib)
        bfd_enabled no
    2001:1:1:1::1/128 -> 2001:20:1:3::1/128, preference: 1
      nh_vrf(default) reslv_tid 0
      real-next-hop: 2001:20:1:3::1, interface: Ethernet1/3
        rnh(not installed in u6rib)
        bfd_enabled no
    2001:2:2:2::2/128 -> 2001:10:2:3::2/128, preference: 1
      nh_vrf(default) reslv_tid 0
      real-next-hop: 2001:10:2:3::2, interface: Ethernet1/4
        rnh(not installed in u6rib)
        bfd_enabled no
    2001:2:2:2::2/128 -> 2001:20:2:3::2/128, preference: 1
      nh_vrf(default) reslv_tid 0
      real-next-hop: 2001:20:2:3::2, interface: Ethernet1/1
        rnh(not installed in u6rib)
        bfd_enabled no

    '''
}
    golden_parsed_output_ipv6_1 = {
        'vrf':{
            'default':{
                'address_family': {
                    'ipv6': {
                        'routes': {
                            '2001:1:1:1::1/128': {
                                'route': '2001:1:1:1::1/128',
                                'next_hop': {
                                    'next_hop_list': {
                                         1: {
                                             'index': 1,
                                             'next_hop_vrf': 'default',
                                             'rnh_active': False,
                                             'next_hop': '2001:10:1:3::1',
                                             'next_hop_netmask': '128',
                                             'outgoing_interface': 'Ethernet1/2',
                                             'bfd_enabled': False,
                                             'resolved_tid': 0,
                                             'preference': 1,
                                         },
                                         2: {
                                            'index': 2,
                                            'next_hop_vrf': 'default',
                                            'rnh_active': False,
                                            'next_hop': '2001:20:1:3::1',
                                            'next_hop_netmask': '128',
                                            'outgoing_interface': 'Ethernet1/3',
                                            'bfd_enabled': False,
                                            'resolved_tid': 0,
                                            'preference': 1,
                                         },
                                    },
                                },
                            },
                            '2001:2:2:2::2/128': {
                                'route': '2001:2:2:2::2/128',
                                'next_hop': {
                                    'next_hop_list': {
                                        1: {
                                            'index': 1,
                                            'next_hop_vrf': 'default',
                                            'rnh_active': False,
                                            'next_hop': '2001:10:2:3::2',
                                            'next_hop_netmask': '128',
                                            'outgoing_interface': 'Ethernet1/4',
                                            'bfd_enabled': False,
                                            'resolved_tid': 0,
                                            'preference': 1,
                                        },
                                        2: {
                                            'index': 2,
                                            'next_hop_vrf': 'default',
                                            'rnh_active': False,
                                            'next_hop': '2001:20:2:3::2',
                                            'next_hop_netmask': '128',
                                            'outgoing_interface': 'Ethernet1/1',
                                            'bfd_enabled': False,
                                            'resolved_tid': 0,
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

    golden_output_ipv6_2 = {'execute.return_value': '''
    R3_nxosv# show ipv6 static-route vrf all
    IPv6 Configured Static Routes for VRF "default"(1)

    2001:1:1:1::1/128 -> 2001:10:1:3::1/128, preference: 1
      nh_vrf(default) reslv_tid 0
      real-next-hop: 2001:10:1:3::1, interface: Ethernet1/2
        rnh(not installed in u6rib)
        bfd_enabled no
    2001:1:1:1::1/128 -> 2001:20:1:3::1/128, preference: 1
      nh_vrf(default) reslv_tid 0
      real-next-hop: 2001:20:1:3::1, interface: Ethernet1/3
        rnh(not installed in u6rib)
        bfd_enabled no
    2001:2:2:2::2/128 -> 2001:10:2:3::2/128, preference: 1
      nh_vrf(default) reslv_tid 0
      real-next-hop: 2001:10:2:3::2, interface: Ethernet1/4
        rnh(not installed in u6rib)
        bfd_enabled no
    2001:2:2:2::2/128 -> 2001:20:2:3::2/128, preference: 1
      nh_vrf(default) reslv_tid 0
      real-next-hop: 2001:20:2:3::2, interface: Ethernet1/1
        rnh(not installed in u6rib)
        bfd_enabled no

    IPv6 Configured Static Routes for VRF "management"(2)


    IPv6 Configured Static Routes for VRF "VRF1"(3)

    2001:1:1:1::1/128 -> Null0, preference: 1
      nh_vrf(VRF1) reslv_tid 80000003
      real-next-hop: 0::, interface: Null0
        rnh(not installed in u6rib)
        bfd_enabled no
    2001:2:2:2::2/128 -> Null0, preference: 2
      nh_vrf(VRF1) reslv_tid 80000003
      real-next-hop: 0::, interface: Null0
        rnh(not installed in u6rib)
        bfd_enabled no
    2001:1:1:1::1/128 -> 2001:10:1:3::1/128, preference: 1
      nh_vrf(VRF1) reslv_tid 0
      real-next-hop: 2001:10:1:3::1, interface: none
        rnh(not installed in u6rib)
        bfd_enabled no
    2001:1:1:1::1/128 -> 2001:20:1:3::1/128, preference: 1
      nh_vrf(VRF1) reslv_tid 0
      real-next-hop: 2001:20:1:3::1, interface: none
        rnh(not installed in u6rib)
        bfd_enabled no
    2001:2:2:2::2/128 -> 2001:10:2:3::2/128, preference: 1
      nh_vrf(VRF1) reslv_tid 0
      real-next-hop: 2001:10:2:3::2, interface: none
        rnh(not installed in u6rib)
        bfd_enabled no
    2001:2:2:2::2/128 -> 2001:20:2:3::2/128, preference: 1
      nh_vrf(VRF1) reslv_tid 0
      real-next-hop: 2001:20:2:3::2, interface: none
        rnh(not installed in u6rib)
        bfd_enabled no
    2001:2:2:2::2/128 -> 2001:20:2:3::2/128, preference: 3
      nh_vrf(VRF1) reslv_tid 0
      real-next-hop: 0::, interface: none
        rnh(installed in u6rib)
        bfd_enabled no
    2001:2:2:2::2/128 -> 2001:50:2:3::2/128, preference: 5
      nh_vrf(VRF1) reslv_tid 0
      real-next-hop: 0::, interface: none
        rnh(installed in u6rib)
        bfd_enabled no

    '''
  }

    golden_parsed_output_ipv6_2 = {
        'vrf': {
            'default': {
                'address_family': {
                    'ipv6': {
                        'routes': {
                            '2001:1:1:1::1/128': {
                                'route': '2001:1:1:1::1/128',
                                'next_hop': {
                                    'next_hop_list': {
                                        1: {
                                            'index': 1,
                                            'next_hop_vrf': 'default',
                                            'rnh_active': False,
                                            'next_hop': '2001:10:1:3::1',
                                            'next_hop_netmask': '128',
                                            'outgoing_interface': 'Ethernet1/2',
                                            'bfd_enabled': False,
                                            'resolved_tid': 0,
                                            'preference': 1,
                                        },
                                        2: {
                                            'index': 2,
                                            'next_hop_vrf': 'default',
                                            'rnh_active': False,
                                            'next_hop': '2001:20:1:3::1',
                                            'next_hop_netmask': '128',
                                            'outgoing_interface': 'Ethernet1/3',
                                            'bfd_enabled': False,
                                            'resolved_tid': 0,
                                            'preference': 1,
                                        },
                                    },
                                },
                            },
                            '2001:2:2:2::2/128': {
                                'route': '2001:2:2:2::2/128',
                                'next_hop': {
                                    'next_hop_list': {
                                        1: {
                                            'index': 1,
                                            'next_hop_vrf': 'default',
                                            'rnh_active': False,
                                            'next_hop': '2001:10:2:3::2',
                                            'next_hop_netmask': '128',
                                            'outgoing_interface': 'Ethernet1/4',
                                            'bfd_enabled': False,
                                            'resolved_tid': 0,
                                            'preference': 1,
                                        },
                                        2: {
                                            'index': 2,
                                            'next_hop_vrf': 'default',
                                            'rnh_active': False,
                                            'next_hop': '2001:20:2:3::2',
                                            'next_hop_netmask': '128',
                                            'outgoing_interface': 'Ethernet1/1',
                                            'bfd_enabled': False,
                                            'resolved_tid': 0,
                                            'preference': 1,
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
                    'ipv6': {
                        'routes': {
                            '2001:1:1:1::1/128': {
                                'route': '2001:1:1:1::1/128',
                                'next_hop': {
                                    'outgoing_interface': {
                                        'Null0': {
                                            'outgoing_interface': 'Null0',
                                            'preference': 1,
                                            'resolved_tid': 80000003,
                                            'bfd_enabled': False,
                                            'rnh_active': False,
                                            'next_hop_vrf': 'VRF1',
                                        },
                                    },
                                    'next_hop_list': {
                                        1: {
                                            'index': 1,
                                            'next_hop_vrf': 'VRF1',
                                            'rnh_active': False,
                                            'next_hop': '2001:10:1:3::1',
                                            'next_hop_netmask': '128',
                                            'bfd_enabled': False,
                                            'resolved_tid': 0,
                                            'preference': 1,
                                        },
                                        2: {
                                            'index': 2,
                                            'next_hop_vrf': 'VRF1',
                                            'rnh_active': False,
                                            'next_hop': '2001:20:1:3::1',
                                            'next_hop_netmask': '128',
                                            'bfd_enabled': False,
                                            'resolved_tid': 0,
                                            'preference': 1,
                                        },
                                    },
                                },
                            },
                            '2001:2:2:2::2/128': {
                                'route': '2001:2:2:2::2/128',
                                'next_hop': {
                                    'outgoing_interface': {
                                        'Null0': {
                                            'outgoing_interface': 'Null0',
                                            'preference': 2,
                                            'resolved_tid': 80000003,
                                            'bfd_enabled': False,
                                            'rnh_active': False,
                                            'next_hop_vrf': 'VRF1',
                                        },
                                    },
                                    'next_hop_list': {
                                        1: {
                                            'index': 1,
                                            'next_hop_vrf': 'VRF1',
                                            'rnh_active': False,
                                            'next_hop': '2001:10:2:3::2',
                                            'next_hop_netmask': '128',
                                            'bfd_enabled': False,
                                            'resolved_tid': 0,
                                            'preference': 1,
                                        },
                                        2: {
                                            'index': 2,
                                            'next_hop_vrf': 'VRF1',
                                            'rnh_active': False,
                                            'next_hop': '2001:20:2:3::2',
                                            'next_hop_netmask': '128',
                                            'bfd_enabled': False,
                                            'resolved_tid': 0,
                                            'preference': 1,
                                        },
                                        3: {
                                            'index': 3,
                                            'next_hop_vrf': 'VRF1',
                                            'rnh_active': True,
                                            'next_hop': '2001:20:2:3::2',
                                            'next_hop_netmask': '128',
                                            'bfd_enabled': False,
                                            'resolved_tid': 0,
                                            'preference': 3,
                                        },
                                        4: {
                                            'index': 4,
                                            'next_hop_vrf': 'VRF1',
                                            'rnh_active': True,
                                            'next_hop': '2001:50:2:3::2',
                                            'next_hop_netmask': '128',
                                            'bfd_enabled': False,
                                            'resolved_tid': 0,
                                            'preference': 5,
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
        self.device = Mock(**self.golden_output_ipv6_1)
        obj = ShowIpv6StaticRoute(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output_ipv6_1)


    def test_show_ip_static_route_2(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_ipv6_2)
        obj = ShowIpv6StaticRoute(device=self.device)
        parsed_output = obj.parse(vrf='all')
        self.assertEqual(parsed_output,self.golden_parsed_output_ipv6_2)

if __name__ == '__main__':
    unittest.main()