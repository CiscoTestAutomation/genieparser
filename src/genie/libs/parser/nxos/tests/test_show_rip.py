# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError, \
    SchemaMissingKeyError

from genie.libs.parser.nxos.show_rip import ShowIpRipVrfAll, \
    ShowIpRipRouteVrfAll, ShowIpRipInterfaceVrfAll, ShowIpv6RipVrfAll, \
    ShowIpv6RipRouteVrfAll, ShowIpv6InterfaceVrfAll


# ==================================================
#  Unit test for:
#    * 'show ip rip vrf all'
#    * 'show ip rip route vrf all'
#    * 'show ip rip interface vrf all'
#    * 'show ipv6 rip vrf all'
#    * 'show ipv6 rip route vrf all'
#    * 'show ipv6 interface vrf all'
# ==================================================

class test_show_ip_rip_vrf_all(unittest.TestCase):
    '''Unit test for 'show ip rip vrf all' '''

    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output1 = {
        'vrf': {
            'isolate_mode': False,
            'mmode': 'Initialized',
            'VRF1': {
                'address_family': {
                    'ipv4': {
                        'instance': {
                            'rip-1': {
                                'default_metric': 1,
                                'distance': 120,
                                'interfaces': {
                                    'Ethernet1/1.200': {
                                        },
                                    'Ethernet1/2.200': {
                                        },
                                    },
                                'max_path': 16,
                                'multicast_group': '224.0.0.9',
                                'port': 520,
                                'redistribute': {
                                    'direct': {
                                        'route_policy': 'ALL',
                                        },
                                    'static': {
                                        'route_policy': 'metric15',
                                        },
                                    },
                                'state': 'up and running',
                                'timers': {
                                    'expire_time': 180,
                                    'flush_time': 120,
                                    'update_interval': 30,
                                    },
                                },
                            },
                        },
                    },
                },
            'default': {
                'address_family': {
                    'ipv4': {
                        'instance': {
                            'rip-1': {
                                'default_metric': 3,
                                'distance': 120,
                                'interfaces': {
                                    'Ethernet1/1.100': {
                                        },
                                    'Ethernet1/2.100': {
                                        },
                                    },
                                'max_path': 16,
                                'multicast_group': '224.0.0.9',
                                'port': 520,
                                'redistribute': {
                                    'direct': {
                                        'route_policy': 'ALL',
                                        },
                                    'static': {
                                        'route_policy': 'ALL',
                                        },
                                    },
                                'state': 'up and running',
                                'timers': {
                                    'expire_time': 21,
                                    'flush_time': 23,
                                    'update_interval': 10,
                                    },
                                },
                            },
                        },
                    },
                },
            },
        }

    golden_output1 = {'execute.return_value': '''
        RIP Isolate Mode: No
        MMODE: Initialized
        Process Name "rip-1" VRF "default"
        RIP port 520, multicast-group 224.0.0.9
        Admin-distance: 120 
        Updates every 10 sec, expire in 21 sec
        Collect garbage in 23 sec
        Default-metric: 3
        Max-paths: 16
        Process is up and running
          Interfaces supported by ipv4 RIP :
            Ethernet1/1.100
            Ethernet1/2.100
          Redistributing :
            direct          policy ALL
            static          policy ALL
        Process Name "rip-1" VRF "VRF1"
        RIP port 520, multicast-group 224.0.0.9
        Admin-distance: 120 
        Updates every 30 sec, expire in 180 sec
        Collect garbage in 120 sec
        Default-metric: 1
        Max-paths: 16
        Process is up and running
          Interfaces supported by ipv4 RIP :
            Ethernet1/1.200
            Ethernet1/2.200
          Redistributing :
            direct          policy ALL
            static          policy metric15
        '''}

    def test_show_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowIpRipVrfAll(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_show_golden1(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output1)
        obj = ShowIpRipVrfAll(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output1)


class test_show_ip_rip_route_vrf_all(unittest.TestCase):
    '''Unit test for 'show ip rip vrf all' '''

    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output1 = {
        'vrf': {
            'VRF1': {
                'address_family': {
                    'ipv4': {
                        'instance': {
                            'rip-1': {
                                'routes': {
                                    '10.1.2.0/24': {
                                        'index': {
                                            1: {
                                                'interface': 'Ethernet1/1.200',
                                                'metric': 1,
                                                'next_hop': '10.1.2.1',
                                                'route_type': 'connected',
                                                'tag': 0,
                                                },
                                            },
                                        },
                                    '10.1.3.0/24': {
                                        'index': {
                                            1: {
                                                'interface': 'Ethernet1/2.200',
                                                'metric': 1,
                                                'next_hop': '10.1.3.1',
                                                'route_type': 'connected',
                                                'tag': 0,
                                                },
                                            },
                                        },
                                    '10.2.3.0/24': {
                                        'index': {
                                            1: {
                                                'expire_time': '00:02:52',
                                                'interface': 'Ethernet1/1.200',
                                                'metric': 2,
                                                'next_hop': '10.1.2.2',
                                                'tag': 0,
                                                },
                                            },
                                        },
                                    '172.16.11.0/24': {
                                        'index': {
                                            1: {
                                                'interface': 'None',
                                                'metric': 15,
                                                'next_hop': '0.0.0.0',
                                                'redistributed': True,
                                                'tag': 0,
                                                },
                                            },
                                        },
                                    '192.168.2.2/32': {
                                        'index': {
                                            1: {
                                                'expire_time': '00:02:52',
                                                'interface': 'Ethernet1/1.200',
                                                'metric': 2,
                                                'next_hop': '10.1.2.2',
                                                'tag': 0,
                                                },
                                            },
                                        },
                                    '192.168.3.3/32': {
                                        'index': {
                                            1: {
                                                'expire_time': '00:02:52',
                                                'interface': 'Ethernet1/1.200',
                                                'metric': 3,
                                                'next_hop': '10.1.2.2',
                                                'tag': 0,
                                                },
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
                    'ipv4': {
                        'instance': {
                            'rip-1': {
                                'routes': {
                                    '10.1.2.0/24': {
                                        'index': {
                                            1: {
                                                'interface': 'Ethernet1/1.100',
                                                'metric': 1,
                                                'next_hop': '10.1.2.1',
                                                'route_type': 'connected',
                                                'tag': 0,
                                                },
                                            },
                                        },
                                    '10.1.3.0/24': {
                                        'index': {
                                            1: {
                                                'interface': 'Ethernet1/2.100',
                                                'metric': 1,
                                                'next_hop': '10.1.3.1',
                                                'route_type': 'connected',
                                                'tag': 0,
                                                },
                                            2: {
                                                'expire_time': '00:00:05',
                                                'interface': 'Ethernet1/1.100',
                                                'metric': 3,
                                                'next_hop': '10.1.2.2',
                                                'tag': 0,
                                                },
                                            },
                                        },
                                    '10.2.3.0/24': {
                                        'index': {
                                            1: {
                                                'expire_time': '00:00:05',
                                                'interface': 'Ethernet1/1.100',
                                                'metric': 2,
                                                'next_hop': '10.1.2.2',
                                                'tag': 0,
                                                },
                                            },
                                        },
                                    '172.16.22.0/24': {
                                        'index': {
                                            1: {
                                                'expire_time': '00:00:05',
                                                'interface': 'Ethernet1/1.100',
                                                'metric': 2,
                                                'next_hop': '10.1.2.2',
                                                'tag': 0,
                                                },
                                            },
                                        },
                                    '172.16.33.0/24': {
                                        'index': {
                                            1: {
                                                'expire_time': '00:00:05',
                                                'interface': 'Ethernet1/1.100',
                                                'metric': 3,
                                                'next_hop': '10.1.2.2',
                                                'tag': 0,
                                                },
                                            },
                                        },
                                    '192.168.2.2/32': {
                                        'index': {
                                            1: {
                                                'expire_time': '00:00:05',
                                                'interface': 'Ethernet1/1.100',
                                                'metric': 2,
                                                'next_hop': '10.1.2.2',
                                                'tag': 0,
                                                },
                                            },
                                        },
                                    '192.168.3.3/32': {
                                        'index': {
                                            1: {
                                                'expire_time': '00:00:05',
                                                'interface': 'Ethernet1/1.100',
                                                'metric': 3,
                                                'next_hop': '10.1.2.2',
                                                'tag': 0,
                                                },
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

    golden_output1 = {'execute.return_value': '''
        Process Name "rip-1" VRF "default"
        RIP routing table 

        > - indicates best RIP route

        >10.1.2.0/24 next-hops 0
         via 10.1.2.1 Ethernet1/1.100, metric 1, tag 0, direct route

        >10.1.3.0/24 next-hops 1
         via 10.1.3.1 Ethernet1/2.100, metric 1, tag 0, direct route
         via 10.1.2.2 Ethernet1/1.100, metric 3, tag 0, timeout 00:00:05

        >10.2.3.0/24 next-hops 1
         via 10.1.2.2 Ethernet1/1.100, metric 2, tag 0, timeout 00:00:05

        >172.16.22.0/24 next-hops 1
         via 10.1.2.2 Ethernet1/1.100, metric 2, tag 0, timeout 00:00:05

        >172.16.33.0/24 next-hops 1
         via 10.1.2.2 Ethernet1/1.100, metric 3, tag 0, timeout 00:00:05

        >192.168.2.2/32 next-hops 1
         via 10.1.2.2 Ethernet1/1.100, metric 2, tag 0, timeout 00:00:05

        >192.168.3.3/32 next-hops 1
         via 10.1.2.2 Ethernet1/1.100, metric 3, tag 0, timeout 00:00:05

        Process Name "rip-1" VRF "VRF1"
        RIP routing table 

        > - indicates best RIP route

        >10.1.2.0/24 next-hops 0
         via 10.1.2.1 Ethernet1/1.200, metric 1, tag 0, direct route

        >10.1.3.0/24 next-hops 0
         via 10.1.3.1 Ethernet1/2.200, metric 1, tag 0, direct route

        >10.2.3.0/24 next-hops 1
         via 10.1.2.2 Ethernet1/1.200, metric 2, tag 0, timeout 00:02:52

        >172.16.11.0/24 next-hops 1
         via 0.0.0.0, metric 15, tag 0, redistributed route

        >192.168.2.2/32 next-hops 1
         via 10.1.2.2 Ethernet1/1.200, metric 2, tag 0, timeout 00:02:52

        >192.168.3.3/32 next-hops 1
         via 10.1.2.2 Ethernet1/1.200, metric 3, tag 0, timeout 00:02:52
        '''}

    def test_show_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowIpRipRouteVrfAll(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_show_golden1(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output1)
        obj = ShowIpRipRouteVrfAll(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output1)


class test_show_ip_rip_interface_vrf_all(unittest.TestCase):
    '''Unit test for 'show ip rip interface vrf all' '''

    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output1 = {
        'vrf': {
            'VRF1': {
                'address_family': {
                    'ipv4': {
                        'instance': {
                            'rip-1': {
                                'interfaces': {
                                    'Ethernet1/1.200': {
                                        'oper_status': 'up',
                                        'passive': True,
                                        'split_horizon': True,
                                        'states': {
                                            'admin_state': 'up',
                                            'link_state': 'up',
                                            'protocol_state': 'up',
                                            },
                                        'summary_address': {
                                            '10.1.2.1/24': {
                                                'metric': 1,
                                                },
                                            },
                                        },
                                    'Ethernet1/2.200': {
                                        'authentication': {
                                            'auth_key': {
                                                'crypto_algorithm': 'md5',
                                                },
                                            'auth_key_chain': {
                                                'key_chain': 'none',
                                                },
                                            },
                                        'oper_status': 'up',
                                        'passive': True,
                                        'split_horizon': True,
                                        'states': {
                                            'admin_state': 'up',
                                            'link_state': 'up',
                                            'protocol_state': 'up',
                                            },
                                        'summary_address': {
                                            '10.1.3.1/24': {
                                                'metric': 1,
                                                },
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
                    'ipv4': {
                        'instance': {
                            'rip-1': {
                                'interfaces': {
                                    'Ethernet1/1.100': {
                                        'oper_status': 'up',
                                        'passive': True,
                                        'split_horizon': True,
                                        'states': {
                                            'admin_state': 'up',
                                            'link_state': 'up',
                                            'protocol_state': 'up',
                                            },
                                        'summary_address': {
                                            '10.1.2.1/24': {
                                                'metric': 1,
                                                },
                                            },
                                        },
                                    'Ethernet1/2.100': {
                                        'authentication': {
                                            'auth_key': {
                                                'crypto_algorithm': 'none',
                                                },
                                            'auth_key_chain': {
                                                'key_chain': '1',
                                                },
                                            },
                                        'oper_status': 'up',
                                        'passive': True,
                                        'split_horizon': True,
                                        'states': {
                                            'admin_state': 'up',
                                            'link_state': 'up',
                                            'protocol_state': 'up',
                                            },
                                        'summary_address': {
                                            '10.1.3.1/24': {
                                                'metric': 1,
                                                },
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

    golden_output1 = {'execute.return_value': '''
        Process Name "rip-1" VRF "default"
        RIP-configured interface information
        
        Ethernet1/1.100, protocol-up/link-up/admin-up, RIP state : up
          address/mask 10.1.2.1/24, metric 1, split-horizon, passive (no outbound updates)
        Ethernet1/2.100, protocol-up/link-up/admin-up, RIP state : up
          address/mask 10.1.3.1/24, metric 1, split-horizon
          Authentication Mode: none  Keychain: 1
        
        Process Name "rip-1" VRF "VRF1"
        RIP-configured interface information
        
        Ethernet1/1.200, protocol-up/link-up/admin-up, RIP state : up
          address/mask 10.1.2.1/24, metric 1, split-horizon
        Ethernet1/2.200, protocol-up/link-up/admin-up, RIP state : up
          address/mask 10.1.3.1/24, metric 1, split-horizon
          Authentication Mode: md5  Keychain: none
        '''}

    def test_show_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowIpRipInterfaceVrfAll(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_show_golden1(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output1)
        obj = ShowIpRipInterfaceVrfAll(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output1)


class test_show_ipv6_rip_vrf_all(unittest.TestCase):
    '''Unit test for 'show ipv6 rip vrf all' '''

    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output1 = {
        'vrf': {
            'VRF1': {
                'address_family': {
                    'ipv6': {
                        'instance': {
                            'rip-1': {
                                'default_metric': 1,
                                'distance': 120,
                                'interfaces': {
                                    'Ethernet1/1.200': {
                                        },
                                    'Ethernet1/2.200': {
                                        },
                                    },
                                'max_path': 16,
                                'multicast_group': 'ff02::9',
                                'port': 521,
                                'redistribute': {
                                    'direct': {
                                        'route_policy': 'ALL6',
                                        },
                                    'static': {
                                        'route_policy': 'static-to-rip',
                                        },
                                    },
                                'state': 'up and running',
                                'timers': {
                                    'expire_time': 180,
                                    'flush_time': 120,
                                    'update_interval': 30,
                                    },
                                },
                            },
                        },
                    },
                },
            'default': {
                'address_family': {
                    'ipv6': {
                        'instance': {
                            'rip-1': {
                                'default_metric': 1,
                                'distance': 120,
                                'interfaces': {
                                    'Ethernet1/1.100': {
                                        },
                                    'Ethernet1/2.100': {
                                        },
                                    },
                                'max_path': 16,
                                'multicast_group': 'ff02::9',
                                'port': 521,
                                'redistribute': {
                                    'static': {
                                        'route_policy': 'metric3_v6',
                                        },
                                    },
                                'state': 'up and running',
                                'timers': {
                                    'expire_time': 180,
                                    'flush_time': 120,
                                    'update_interval': 30,
                                    },
                                },
                            },
                        },
                    },
                },
            'isolate_mode': False,
            'mmode': 'Initialized',
            },
        }

    golden_output1 = {'execute.return_value': '''
        R1# show ipv6 rip vrf all
        RIP Isolate Mode: No
        MMODE: Initialized
        Process Name "rip-1" VRF "default"
        RIP port 521, multicast-group ff02::9
        Admin-distance: 120 
        Updates every 30 sec, expire in 180 sec
        Collect garbage in 120 sec
        Default-metric: 1
        Max-paths: 16
        Process is up and running
          Interfaces supported by ipv6 RIP :
            Ethernet1/1.100
            Ethernet1/2.100
          Redistributing :
            static          policy metric3_v6
        Process Name "rip-1" VRF "VRF1"
        RIP port 521, multicast-group ff02::9
        Admin-distance: 120 
        Updates every 30 sec, expire in 180 sec
        Collect garbage in 120 sec
        Default-metric: 1
        Max-paths: 16
        Default-originate: 
        Process is up and running
          Interfaces supported by ipv6 RIP :
            Ethernet1/1.200
            Ethernet1/2.200
          Redistributing :
            direct          policy ALL6
            static          policy static-to-rip
        '''}

    def test_show_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowIpv6RipVrfAll(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_show_golden1(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output1)
        obj = ShowIpv6RipVrfAll(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output1)


class test_show_ipv6_rip_route_vrf_all(unittest.TestCase):
    '''Unit test for 'show ipv6 rip route vrf all' '''

    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output1 = {
        'vrf': {
            'VRF1': {
                'address_family': {
                    'ipv4': {
                        'instance': {
                            'rip-1': {
                                'routes': {
                                    '2001:db8:1113:1113::/64': {
                                        'index': {
                                            1: {
                                                'interface': 'None',
                                                'metric': 1,
                                                'next_hop': '0::',
                                                'redistributed': True,
                                                'tag': 5,
                                                },
                                            },
                                        },
                                    '2001:db8:1:2::/64': {
                                        'index': {
                                            1: {
                                                'interface': 'Ethernet1/1.200',
                                                'metric': 1,
                                                'next_hop': '2001:db8:1:2::1',
                                                'route_type': 'connected',
                                                'tag': 0,
                                                },
                                            2: {
                                                'interface': 'None',
                                                'metric': 1,
                                                'next_hop': '0::',
                                                'redistributed': True,
                                                'tag': 0,
                                                },
                                            },
                                        },
                                    '2001:db8:1:3::/64': {
                                        'index': {
                                            1: {
                                                'interface': 'Ethernet1/2.200',
                                                'metric': 1,
                                                'next_hop': '2001:db8:1:3::1',
                                                'route_type': 'connected',
                                                'tag': 0,
                                                },
                                            2: {
                                                'interface': 'None',
                                                'metric': 1,
                                                'next_hop': '0::',
                                                'redistributed': True,
                                                'tag': 0,
                                                },
                                            },
                                        },
                                    '2001:db8:2:3::/64': {
                                        'index': {
                                            1: {
                                                'expire_time': '00:02:46',
                                                'interface': 'Ethernet1/1.200',
                                                'metric': 2,
                                                'next_hop': 'fe80::5c00:ff:fe01:7',
                                                'tag': 0,
                                                },
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
                    'ipv4': {
                        'instance': {
                            'rip-1': {
                                'routes': {
                                    '2001:db8:1111:1111::/64': {
                                        'index': {
                                            1: {
                                                'interface': 'None',
                                                'metric': 3,
                                                'next_hop': '0::',
                                                'redistributed': True,
                                                'tag': 0,
                                                },
                                            },
                                        },
                                    '2001:db8:1112:1112::/64': {
                                        'index': {
                                            1: {
                                                'interface': 'None',
                                                'metric': 3,
                                                'next_hop': '0::',
                                                'redistributed': True,
                                                'tag': 0,
                                                },
                                            },
                                        },
                                    '2001:db8:1113:1113::/64': {
                                        'index': {
                                            1: {
                                                'interface': 'None',
                                                'metric': 3,
                                                'next_hop': '0::',
                                                'redistributed': True,
                                                'tag': 0,
                                                },
                                            },
                                        },
                                    '2001:db8:1:2::/64': {
                                        'index': {
                                            1: {
                                                'interface': 'Ethernet1/1.100',
                                                'metric': 1,
                                                'next_hop': '2001:db8:1:2::1',
                                                'route_type': 'connected',
                                                'tag': 0,
                                                },
                                            },
                                        },
                                    '2001:db8:1:3::/64': {
                                        'index': {
                                            1: {
                                                'interface': 'Ethernet1/2.100',
                                                'metric': 1,
                                                'next_hop': '2001:db8:1:3::1',
                                                'route_type': 'connected',
                                                'tag': 0,
                                                },
                                            },
                                        },
                                    '2001:db8:2222:2222::/64': {
                                        'index': {
                                            1: {
                                                'expire_time': '00:02:36',
                                                'interface': 'Ethernet1/2.100',
                                                'metric': 7,
                                                'next_hop': 'fe80::5c00:ff:fe02:7',
                                                'tag': 0,
                                                },
                                            },
                                        },
                                    '2001:db8:2223:2223::/64': {
                                        'index': {
                                            1: {
                                                'expire_time': '00:02:39',
                                                'interface': 'Ethernet1/1.100',
                                                'metric': 6,
                                                'next_hop': 'fe80::5c00:ff:fe01:7',
                                                'tag': 0,
                                                },
                                            },
                                        },
                                    '2001:db8:2:3::/64': {
                                        'index': {
                                            1: {
                                                'expire_time': '00:02:36',
                                                'interface': 'Ethernet1/2.100',
                                                'metric': 2,
                                                'next_hop': 'fe80::5c00:ff:fe02:7',
                                                'tag': 0,
                                                },
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

    golden_output1 = {'execute.return_value': '''
        R1# show ipv6 rip route vrf all
        Process Name "rip-1" VRF "default"
        RIP routing table 
        
        > - indicates best RIP route
        
        >2001:db8:1:2::/64 next-hops 0
         via 2001:db8:1:2::1 Ethernet1/1.100, metric 1, tag 0, direct route
        
        >2001:db8:1:3::/64 next-hops 0
         via 2001:db8:1:3::1 Ethernet1/2.100, metric 1, tag 0, direct route
        
        >2001:db8:2:3::/64 next-hops 1
         via fe80::5c00:ff:fe02:7 Ethernet1/2.100, metric 2, tag 0, timeout 00:02:36
        
        >2001:db8:1111:1111::/64 next-hops 1
         via 0::, metric 3, tag 0, redistributed route
        
        >2001:db8:1112:1112::/64 next-hops 1
         via 0::, metric 3, tag 0, redistributed route
        
        >2001:db8:1113:1113::/64 next-hops 1
         via 0::, metric 3, tag 0, redistributed route
        
        >2001:db8:2222:2222::/64 next-hops 1
         via fe80::5c00:ff:fe02:7 Ethernet1/2.100, metric 7, tag 0, timeout 00:02:36
        
        >2001:db8:2223:2223::/64 next-hops 1
         via fe80::5c00:ff:fe01:7 Ethernet1/1.100, metric 6, tag 0, timeout 00:02:39
        
        Process Name "rip-1" VRF "VRF1"
        RIP routing table 
        
        > - indicates best RIP route
        
        >2001:db8:1:2::/64 next-hops 1
         via 2001:db8:1:2::1 Ethernet1/1.200, metric 1, tag 0, direct route
         via 0::, metric 1, tag 0, redistributed route
        
        >2001:db8:1:3::/64 next-hops 1
         via 2001:db8:1:3::1 Ethernet1/2.200, metric 1, tag 0, direct route
         via 0::, metric 1, tag 0, redistributed route
        
        >2001:db8:2:3::/64 next-hops 1
         via fe80::5c00:ff:fe01:7 Ethernet1/1.200, metric 2, tag 0, timeout 00:02:46
        
        >2001:db8:1113:1113::/64 next-hops 1
         via 0::, metric 1, tag 5, redistributed route
        '''}

    def test_show_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowIpv6RipRouteVrfAll(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_show_golden1(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output1)
        obj = ShowIpv6RipRouteVrfAll(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output1)


class test_show_ipv6_interface_vrf_all(unittest.TestCase):
    '''Unit test for 'show ipv6 interface vrf all' '''

    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output1 = {
        'vrf': {
            'VRF1': {
                'address_family': {
                    'ipv6': {
                        'instance': {
                            'rip': {
                                'interfaces': {
                                    'Ethernet1/1.200': {
                                        'RP_traffic_statistics': {
                                            'multicast_bytes': '0/19712/14568',
                                            'multicast_packets': '0/162/157',
                                            'unicast_bytes': '0/990/792',
                                            'unicast_packets': '0/11/11',
                                            },
                                        'address': {
                                            '2001:db8:1:2::1/64': {
                                                'valid': True,
                                                },
                                            },
                                        'forwarding_feature': 'disabled',
                                        'interface_statistics_last_reset': 'never',
                                        'iod': 137,
                                        'link_local_address': {
                                            'fe80::5c00:ff:fe00:7': {
                                                'default': True,
                                                'valid': True,
                                                },
                                            },
                                        'load_sharing': 'none',
                                        'multicast_SG_entries_joined': ' none',
                                        'multicast_groups_locally_joined': ['ff02::9', 'ff02::2', 'ff02::1', 'ff02::1:ff00:1', 'ff02::1:ff00:7', 'ff02::1:ff00:0'],
                                        'multicast_routing': 'disabled',
                                        'report_link_local': 'disabled',
                                        'states': {
                                            'admin_state': 'up',
                                            'link_state': 'up',
                                            'protocol_state': 'up',
                                            },
                                        'subnet': '2001:db8:1:2::/64',
                                        'unicast_reverse_path_forwarding': 'none',
                                        'virtual_addresses_configured': 'none',
                                        },
                                    'Ethernet1/2.200': {
                                        'RP_traffic_statistics': {
                                            'unicast_bytes': '0/0/0',
                                            'unicast_packets': '0/0/0',
                                            'multicast_bytes': '0/23088/1040',                                                      
                                            'multicast_packets': '0/166/10',
                                            },
                                        'address': {
                                            '2001:db8:1:3::1/64': {
                                                'valid': True,
                                                },
                                            },
                                        'forwarding_feature': 'disabled',
                                        'interface_statistics_last_reset': 'never',
                                        'iod': 139,
                                        'link_local_address': {
                                            'fe80::5c00:ff:fe00:7': {
                                                'default': True,
                                                'valid': True,
                                                },
                                            },
                                        'load_sharing': 'none',
                                        'multicast_SG_entries_joined': ' none',
                                        'multicast_groups_locally_joined': ['ff02::9', 'ff02::2', 'ff02::1', 'ff02::1:ff00:1', 'ff02::1:ff00:7', 'ff02::1:ff00:0'],
                                        'multicast_routing': 'disabled',
                                        'report_link_local': 'disabled',
                                        'states': {
                                            'admin_state': 'up',
                                            'link_state': 'up',
                                            'protocol_state': 'up',
                                            },
                                        'subnet': '2001:db8:1:3::/64',
                                        'unicast_reverse_path_forwarding': 'none',
                                        'virtual_addresses_configured': 'none',
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
                        'instance': {
                            'rip': {
                                'interfaces': {
                                    'Ethernet1/1.100': {
                                        'RP_traffic_statistics': {
                                            'multicast_bytes': '0/27886/20164',
                                            'multicast_packets': '0/165/156',
                                            'unicast_bytes': '0/1080/852',
                                            'unicast_packets': '0/12/11',
                                            },
                                        'address': {
                                            '2001:db8:1:2::1/64': {
                                                'valid': True,
                                                },
                                            },
                                        'forwarding_feature': 'disabled',
                                        'interface_statistics_last_reset': 'never',
                                        'iod': 136,
                                        'link_local_address': {
                                            'fe80::5c00:ff:fe00:7': {
                                                'default': True,
                                                'valid': True,
                                                },
                                            },
                                        'load_sharing': 'none',
                                        'multicast_SG_entries_joined': ' none',
                                        'multicast_groups_locally_joined': ['ff02::9', 'ff02::2', 'ff02::1', 'ff02::1:ff00:1', 'ff02::1:ff00:7', 'ff02::1:ff00:0'],
                                        'multicast_routing': 'disabled',
                                        'report_link_local': 'disabled',
                                        'states': {
                                            'admin_state': 'up',
                                            'link_state': 'up',
                                            'protocol_state': 'up',
                                            },
                                        'subnet': '2001:db8:1:2::/64',
                                        'unicast_reverse_path_forwarding': 'none',
                                        'virtual_addresses_configured': 'none',
                                        },
                                    'Ethernet1/2.100': {
                                        'RP_traffic_statistics': {
                                            'multicast_bytes': '0/28774/20224',
                                            'multicast_packets': '0/165/156',
                                            'unicast_bytes': '0/540/360',
                                            'unicast_packets': '0/6/5',
                                            },
                                        'address': {
                                            '2001:db8:1:3::1/64': {
                                                'valid': True,
                                                },
                                            },
                                        'forwarding_feature': 'disabled',
                                        'interface_statistics_last_reset': 'never',
                                        'iod': 138,
                                        'link_local_address': {
                                            'fe80::5c00:ff:fe00:7': {
                                                'default': True,
                                                'valid': True,
                                                },
                                            },
                                        'load_sharing': 'none',
                                        'multicast_SG_entries_joined': ' none',
                                        'multicast_groups_locally_joined': ['ff02::9', 'ff02::2', 'ff02::1', 'ff02::1:ff00:1', 'ff02::1:ff00:7', 'ff02::1:ff00:0'],
                                        'multicast_routing': 'disabled',
                                        'report_link_local': 'disabled',
                                        'states': {
                                            'admin_state': 'up',
                                            'link_state': 'up',
                                            'protocol_state': 'up',
                                            },
                                        'subnet': '2001:db8:1:3::/64',
                                        'unicast_reverse_path_forwarding': 'none',
                                        'virtual_addresses_configured': 'none',
                                        },
                                    },
                                },
                            },
                        },
                    },
                },
            'management': {
                'address_family': {
                    'ipv6': {
                        'instance': {
                            'rip': {
                                },
                            },
                        },
                    },
                },
            },
        }

    golden_output1 = {'execute.return_value': '''
        R1# show ipv6 interface vrf all
        IPv6 Interface Status for VRF "default"
        Ethernet1/1.100, Interface status: protocol-up/link-up/admin-up, iod: 136
          IPv6 address: 
            2001:db8:1:2::1/64 [VALID]
          IPv6 subnet:  2001:db8:1:2::/64
          IPv6 link-local address: fe80::5c00:ff:fe00:7 (default) [VALID]
          IPv6 virtual addresses configured: none
          IPv6 multicast routing: disabled
          IPv6 report link local: disabled
          IPv6 Forwarding feature: disabled
          IPv6 multicast groups locally joined:   
              ff02::9  ff02::2  ff02::1  ff02::1:ff00:1   
              ff02::1:ff00:7  ff02::1:ff00:0  
          IPv6 multicast (S,G) entries joined: none
          IPv6 MTU: 1500 (using link MTU)
          IPv6 unicast reverse path forwarding: none
          IPv6 load sharing: none 
          IPv6 interface statistics last reset: never
          IPv6 interface RP-traffic statistics: (forwarded/originated/consumed)
            Unicast packets:      0/12/11
            Unicast bytes:        0/1080/852
            Multicast packets:    0/165/156
            Multicast bytes:      0/27886/20164
        Ethernet1/2.100, Interface status: protocol-up/link-up/admin-up, iod: 138
          IPv6 address: 
            2001:db8:1:3::1/64 [VALID]
          IPv6 subnet:  2001:db8:1:3::/64
          IPv6 link-local address: fe80::5c00:ff:fe00:7 (default) [VALID]
          IPv6 virtual addresses configured: none
          IPv6 multicast routing: disabled
          IPv6 report link local: disabled
          IPv6 Forwarding feature: disabled
          IPv6 multicast groups locally joined:   
              ff02::9  ff02::2  ff02::1  ff02::1:ff00:1   
              ff02::1:ff00:7  ff02::1:ff00:0  
          IPv6 multicast (S,G) entries joined: none
          IPv6 MTU: 1500 (using link MTU)
          IPv6 unicast reverse path forwarding: none
          IPv6 load sharing: none 
          IPv6 interface statistics last reset: never
          IPv6 interface RP-traffic statistics: (forwarded/originated/consumed)
            Unicast packets:      0/6/5
            Unicast bytes:        0/540/360
            Multicast packets:    0/165/156
            Multicast bytes:      0/28774/20224

        IPv6 Interface Status for VRF "management"

        IPv6 Interface Status for VRF "VRF1"
        Ethernet1/1.200, Interface status: protocol-up/link-up/admin-up, iod: 137
          IPv6 address: 
            2001:db8:1:2::1/64 [VALID]
          IPv6 subnet:  2001:db8:1:2::/64
          IPv6 link-local address: fe80::5c00:ff:fe00:7 (default) [VALID]
          IPv6 virtual addresses configured: none
          IPv6 multicast routing: disabled
          IPv6 report link local: disabled
          IPv6 Forwarding feature: disabled
          IPv6 multicast groups locally joined:   
              ff02::9  ff02::2  ff02::1  ff02::1:ff00:1   
              ff02::1:ff00:7  ff02::1:ff00:0  
          IPv6 multicast (S,G) entries joined: none
          IPv6 MTU: 1500 (using link MTU)
          IPv6 unicast reverse path forwarding: none
          IPv6 load sharing: none 
          IPv6 interface statistics last reset: never
          IPv6 interface RP-traffic statistics: (forwarded/originated/consumed)
            Unicast packets:      0/11/11
            Unicast bytes:        0/990/792
            Multicast packets:    0/162/157
            Multicast bytes:      0/19712/14568
        Ethernet1/2.200, Interface status: protocol-up/link-up/admin-up, iod: 139
          IPv6 address: 
            2001:db8:1:3::1/64 [VALID]
          IPv6 subnet:  2001:db8:1:3::/64
          IPv6 link-local address: fe80::5c00:ff:fe00:7 (default) [VALID]
          IPv6 virtual addresses configured: none
          IPv6 multicast routing: disabled
          IPv6 report link local: disabled
          IPv6 Forwarding feature: disabled
          IPv6 multicast groups locally joined:   
              ff02::9  ff02::2  ff02::1  ff02::1:ff00:1   
              ff02::1:ff00:7  ff02::1:ff00:0  
          IPv6 multicast (S,G) entries joined: none
          IPv6 MTU: 1500 (using link MTU)
          IPv6 unicast reverse path forwarding: none
          IPv6 load sharing: none 
          IPv6 interface statistics last reset: never
          IPv6 interface RP-traffic statistics: (forwarded/originated/consumed)
            Unicast packets:      0/0/0
            Unicast bytes:        0/0/0
            Multicast packets:    0/166/10
            Multicast bytes:      0/23088/1040
        '''}

    def test_show_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowIpv6InterfaceVrfAll(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_show_golden1(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output1)
        obj = ShowIpv6InterfaceVrfAll(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output1)


if __name__ == '__main__':
    unittest.main()
