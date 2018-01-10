import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device

from metaparser.util.exceptions import SchemaEmptyParserError, \
                                       SchemaMissingKeyError

from parser.iosxr.show_static_routing import ShowStaticTopologyDetail

# ============================================
# unit test for 'show ip static route'
# =============================================
class test_show_static_topology_detail(unittest.TestCase):
    '''
       unit test for show static topology detail
    '''
    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}
    golden_output_1 = {'execute.return_value': '''
    RP/0/0/CPU0:R2_xrv#show static vrf all ipv4 topology detail
    Thu Dec  7 22:09:55.169 UTC

    VRF: default Table Id: 0xe0000000 AFI: IPv4 SAFI: Unicast
      Last path event occured at Dec  7 21:52:00.853
    Prefix/Len          Interface                Nexthop             Object              Explicit-path       Metrics
    1.1.1.1/32          GigabitEthernet0_0_0_3   None                None                None                [0/4096/1/0/1]
      Path is installed into RIB at Dec  7 21:52:00.853
      Path version: 1, Path status: 0x21
      Path has best tag: 0
                        GigabitEthernet0_0_0_0   None                None                None                [0/4096/1/0/1]
      Path is installed into RIB at Dec  7 21:52:00.733
      Path version: 1, Path status: 0x21
      Path has best tag: 0

    3.3.3.3/32          GigabitEthernet0_0_0_2   20.2.3.3            None                None                [0/0/1/0/1]
      Path is installed into RIB at Dec  7 21:52:00.843
      Path version: 1, Path status: 0xa1
      Path has best tag: 0
      Path contains both next-hop and outbound interface.
                        None                     20.2.3.3            None                None                [0/0/3/0/1]
      Path is configured at Dec  7 21:47:43.624
      Path version: 0, Path status: 0x0
                        GigabitEthernet0_0_0_1   10.2.3.3            1                   None                [7/0/17/0/1]
      Path is configured at Dec  7 21:47:43.624
      Path version: 0, Path status: 0x80
      Path contains both next-hop and outbound interface.

    '''
}
    golden_parsed_output_1 = {
        'vrfs':{
            'default':{
                'address_family': {
                    'ipv4': {
                        'table_id': '0xe0000000',
                        'safi': 'unicast',
                        'routes': {
                            '1.1.1.1/32': {
                                'route': '1.1.1.1/32',
                                'next_hop': {
                                    'outgoing_interface': {
                                        'GigabitEthernet0/0/0/3': {
                                            'active': True,
                                            'outgoing_interface': 'GigabitEthernet0/0/0/3',
                                            'install_date': 'Dec  7 21:52:00.853',
                                            'metrics': 1,
                                            'preference': 1,
                                            'path_version': 1,
                                            'path_status': '0x21',
                                            'tag':0,
                                        },
                                        'GigabitEthernet0/0/0/0': {
                                            'active': True,
                                            'outgoing_interface': 'GigabitEthernet0/0/0/0',
                                            'install_date': 'Dec  7 21:52:00.733',
                                            'metrics': 1,
                                            'preference': 1,
                                            'path_version': 1,
                                            'path_status': '0x21',
                                            'tag': 0,
                                        },
                                    },
                                },
                            },
                            '3.3.3.3/32': {
                                'route': '3.3.3.3/32',
                                'next_hop': {
                                    'next_hop_list': {
                                        1: {
                                            'index': 1,
                                            'active': True,
                                            'next_hop': '20.2.3.3',
                                            'outgoing_interface': 'GigabitEthernet0/0/0/2',
                                            'install_date': 'Dec  7 21:52:00.843',
                                            'metrics': 1,
                                            'preference': 1,
                                            'path_version': 1,
                                            'path_status': '0xa1',
                                            'tag': 0,

                                        },
                                        2: {
                                            'index': 2,
                                            'active': False,
                                            'next_hop': '20.2.3.3',
                                            'configure_date': 'Dec  7 21:47:43.624',
                                            'metrics': 1,
                                            'preference': 3,
                                            'path_version': 0,
                                            'path_status': '0x0',

                                        },
                                        3: {
                                            'index': 3,
                                            'active': False,
                                            'next_hop': '10.2.3.3',
                                            'outgoing_interface': 'GigabitEthernet0/0/0/1',
                                            'configure_date': 'Dec  7 21:47:43.624',
                                            'metrics': 1,
                                            'preference': 17,
                                            'path_version': 0,
                                            'track': 1,
                                            'path_status': '0x80',

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

    golden_output_vrf_af = {'execute.return_value': '''
    RP/0/0/CPU0:R2_xrv#show static vrf all ipv6 topology detail
    Thu Dec  7 22:10:18.618 UTC


    VRF: default Table Id: 0xe0800000 AFI: IPv6 SAFI: Unicast
      Last path event occured at Dec  7 21:52:00.843
    Prefix/Len          Interface                Nexthop             Object              Explicit-path       Metrics
    2001:1:1:1::1/128   GigabitEthernet0_0_0_3   2001:10:1:2::1      None                None                [0/0/1/0/1]
      Path is installed into RIB at Dec  7 21:52:00.843
      Path version: 1, Path status: 0xa1
      Path has best tag: 0
      Path contains both next-hop and outbound interface.
                        GigabitEthernet0_0_0_0   2001:20:1:2::1      None                None                [0/0/1/0/1]
      Path is installed into RIB at Dec  7 21:52:00.733
      Path version: 1, Path status: 0xa1
      Path has best tag: 0
      Path contains both next-hop and outbound interface.

    2001:3:3:3::3/128   GigabitEthernet0_0_0_2   2001:20:2:3::3      None                None                [0/0/1/0/1]
      Path is installed into RIB at Dec  7 21:52:00.763
      Path version: 1, Path status: 0xa1
      Path has best tag: 0
      Path contains both next-hop and outbound interface.
                        GigabitEthernet0_0_0_1   2001:10:2:3::3      None                None                [0/0/1/0/1]
      Path is installed into RIB at Dec  7 21:52:00.753
      Path version: 1, Path status: 0xa1
      Path has best tag: 0
      Path contains both next-hop and outbound interface.
                        None                     2001:20:2:3::3      None                None                [0/0/3/0/1]
      Path is configured at Dec  7 21:47:43.624
      Path version: 0, Path status: 0x0


    VRF: VRF1 Table Id: 0xe0800010 AFI: IPv6 SAFI: Unicast
      Last path event occured at Dec  7 21:51:47.424
    Prefix/Len          Interface                Nexthop             Object              Explicit-path       Metrics
    2001:1:1:1::1/128   Null0                    None                None                None                [0/4096/99/0/1234]
      Path is installed into RIB at Dec  7 21:51:47.424
      Path version: 1, Path status: 0x21
      Path has best tag: 0

    2001:2:2:2::2/128   Null0                    None                None                None                [0/4096/101/0/3456]
      Path is installed into RIB at Dec  7 21:51:47.424
      Path version: 1, Path status: 0x21
      Path has best tag: 0

    '''
    }
    golden_parsed_output_vrf_af = {
        'vrfs': {
            'VRF1': {
                'address_family': {
                    'ipv6': {
                        'table_id': '0xe0800010',
                        'safi': 'unicast',
                        'routes': {
                            '2001:1:1:1::1/128': {
                                'route': '2001:1:1:1::1/128',
                                'next_hop': {
                                    'outgoing_interface': {
                                        'Null0': {
                                            'active': True,
                                            'outgoing_interface': 'Null0',
                                            'install_date': 'Dec  7 21:51:47.424',
                                            'metrics': 1234,
                                            'preference': 99,
                                            'path_version': 1,
                                            'path_status': '0x21',
                                            'tag': 0,
                                        },
                                    },
                                },
                            },
                            '2001:2:2:2::2/128': {
                                'route': '2001:2:2:2::2/128',
                                'next_hop': {
                                    'outgoing_interface': {
                                        'Null0': {
                                            'active': True,
                                            'outgoing_interface': 'Null0',
                                            'install_date': 'Dec  7 21:51:47.424',
                                            'metrics': 3456,
                                            'preference': 101,
                                            'path_version': 1,
                                            'path_status': '0x21',
                                            'tag': 0,
                                        },
                                    },
                                },
                            },
                        },
                    },
                },
            },
            'default': {
                'address_family': {
                    'ipv6': {
                        'table_id': '0xe0800000',
                        'safi': 'unicast',
                        'routes': {
                            '2001:1:1:1::1/128': {
                                'route': '2001:1:1:1::1/128',
                                'next_hop': {
                                    'next_hop_list': {
                                        1: {
                                            'index': 1,
                                            'active': True,
                                            'next_hop': '2001:10:1:2::1',
                                            'outgoing_interface': 'GigabitEthernet0/0/0/3',
                                            'install_date': 'Dec  7 21:52:00.843',
                                            'metrics': 1,
                                            'preference': 1,
                                            'path_version': 1,
                                            'path_status': '0xa1',
                                            'tag': 0,
                                        },
                                        2: {
                                            'index': 2,
                                            'active': True,
                                            'next_hop': '2001:20:1:2::1',
                                            'outgoing_interface': 'GigabitEthernet0/0/0/0',
                                            'install_date': 'Dec  7 21:52:00.733',
                                            'metrics': 1,
                                            'preference': 1,
                                            'path_version': 1,
                                            'path_status': '0xa1',
                                            'tag': 0,
                                        },
                                    },
                                },
                            },
                            '2001:3:3:3::3/128': {
                                'route': '2001:3:3:3::3/128',
                                'next_hop': {
                                    'next_hop_list': {
                                        1: {
                                            'index': 1,
                                            'active': True,
                                            'next_hop': '2001:20:2:3::3',
                                            'outgoing_interface': 'GigabitEthernet0/0/0/2',
                                            'install_date': 'Dec  7 21:52:00.763',
                                            'metrics': 1,
                                            'preference': 1,
                                            'path_version': 1,
                                            'path_status': '0xa1',
                                            'tag': 0,
                                        },
                                        2: {
                                            'index': 2,
                                            'active': True,
                                            'next_hop': '2001:10:2:3::3',
                                            'outgoing_interface': 'GigabitEthernet0/0/0/1',
                                            'install_date': 'Dec  7 21:52:00.753',
                                            'metrics': 1,
                                            'preference': 1,
                                            'path_version': 1,
                                            'path_status': '0xa1',
                                            'tag': 0,
                                        },
                                        3: {
                                            'index': 3,
                                            'active': False,
                                            'next_hop': '2001:20:2:3::3',
                                            'configure_date': 'Dec  7 21:47:43.624',
                                            'metrics': 1,
                                            'preference': 3,
                                            'path_version': 0,
                                            'path_status': '0x0',
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
        obj = ShowStaticTopologyDetail(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_show_ip_static_route_1(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_1)
        obj = ShowStaticTopologyDetail(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output_1)

    def test_show_ip_static_route_2(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_vrf_af)
        obj = ShowStaticTopologyDetail(device=self.device)
        parsed_output = obj.parse(vrf='all',af='ipv6')
        self.assertEqual(parsed_output,self.golden_parsed_output_vrf_af)


if __name__ == '__main__':
    unittest.main()