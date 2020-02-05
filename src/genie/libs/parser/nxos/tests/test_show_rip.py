# Python
import unittest
from unittest.mock import Mock

# ATS
from pyats.topology import Device
from pyats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError, \
    SchemaMissingKeyError

from genie.libs.parser.nxos.show_rip import ShowIpRipVrfAll, \
    ShowIpRipRouteVrfAll, ShowIpRipInterfaceVrfAll, ShowIpv6RipVrfAll, \
    ShowIpv6RipRouteVrfAll


# ==================================================
#  Unit test for:
#     * show ip rip
#     * show ip rip vrf <vrf>
#     * show ip rip vrf all
#
#     * show ipv6 rip
#     * show ipv6 rip vrf <vrf>
#     * show ipv6 rip vrf all
#
#     * show ip rip route
#     * show ip rip route vrf <vrf>
#     * show ip rip route vrf all
#
#     * show ipv6 rip route
#     * show ipv6 rip route vrf {vrf}
#     * show ipv6 rip route vrf all
#
#     * show ip rip interface
#     * show ip rip interface vrf {vrf}
#     * show ip rip interface vrf all
# ==================================================

class test_show_ip_rip_vrf_all(unittest.TestCase):
    """Unit test for:
        * show ip rip
        * show ip rip vrf <vrf>
        * show ip rip vrf all"""

    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output1 = {
        'isolate_mode': False,
        'mmode': 'Initialized',
        'vrf': {
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
                                'maximum_paths': 16,
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
                                'process': 'up and running',
                                'timers': {
                                    'expire_in': 180,
                                    'collect_garbage': 120,
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
                                'maximum_paths': 16,
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
                                'process': 'up and running',
                                'timers': {
                                    'expire_in': 21,
                                    'collect_garbage': 23,
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
        # show ip rip vrf all
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

    golden_parsed_output2 = {
        'isolate_mode': False,
        'mmode': 'Initialized',
        'vrf': {
            'default': {
                'address_family': {
                    'ipv4': {
                        'instance': {
                            'rip-1': {
                                'default_metric': 1,
                                'distance': 120,
                                'interfaces': {
                                    'Ethernet1/1.120': {
                                        },
                                    'Ethernet1/2.120': {
                                        },
                                    'loopback0': {
                                        },
                                    },
                                'maximum_paths': 16,
                                'multicast_group': '224.0.0.9',
                                'port': 520,
                                'process': 'up and running',
                                'timers': {
                                    'collect_garbage': 120,
                                    'expire_in': 180,
                                    'update_interval': 30,
                                    },
                                },
                            },
                        },
                    },
                },
            },
        }

    golden_output2 = {'execute.return_value': '''
        # show ip rip vrf
        RIP Isolate Mode: No
        MMODE: Initialized
        Process Name "rip-1" VRF "default"
        RIP port 520, multicast-group 224.0.0.9
        Admin-distance: 120 
        Updates every 30 sec, expire in 180 sec
        Collect garbage in 120 sec
        Default-metric: 1
        Max-paths: 16
        Process is up and running
          Interfaces supported by ipv4 RIP :
            Ethernet1/1.120
            Ethernet1/2.120
            loopback0
        '''}

    golden_parsed_output3 = {
        'isolate_mode': False,
        'mmode': 'Initialized',
        'vrf': {
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
                                'maximum_paths': 16,
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
                                'process': 'up and running',
                                'timers': {
                                    'expire_in': 180,
                                    'collect_garbage': 120,
                                    'update_interval': 30,
                                    },
                                },
                            },
                        },
                    },
                },
            },
        }

    golden_output3 = {'execute.return_value': '''
        # show ip rip vrf VRF1
        RIP Isolate Mode: No
        MMODE: Initialized
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

    def test_show_empty1(self):
        self.device = Mock(**self.empty_output)
        obj = ShowIpRipVrfAll(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse(vrf='all')

    def test_show_empty2(self):
        self.device = Mock(**self.empty_output)
        obj = ShowIpRipVrfAll(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_show_empty3(self):
        self.device = Mock(**self.empty_output)
        obj = ShowIpRipVrfAll(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse(vrf='VRF1')

    def test_show_golden1(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output1)
        obj = ShowIpRipVrfAll(device=self.device)
        parsed_output = obj.parse(vrf='all')
        self.assertEqual(parsed_output, self.golden_parsed_output1)

    def test_show_golden2(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output2)
        obj = ShowIpRipVrfAll(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output2)

    def test_show_golden3(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output3)
        obj = ShowIpRipVrfAll(device=self.device)
        parsed_output = obj.parse(vrf='VRF1')
        self.assertEqual(parsed_output, self.golden_parsed_output3)


class test_show_ip_rip_route_vrf_all(unittest.TestCase):
    """Unit test for:
        * 'show ip rip'
        * 'show ip rip vrf <vrf>'
        * 'show ip rip vrf all'"""

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
                                        'best_route': True,
                                        'index': {
                                            1: {
                                                'interface': 'Ethernet1/1.200',
                                                'metric': 1,
                                                'next_hop': '10.1.2.1',
                                                'route_type': 'connected',
                                                'tag': 0,
                                                },
                                            },
                                        'next_hops': 0,
                                        },
                                    '10.1.3.0/24': {
                                        'best_route': True,
                                        'index': {
                                            1: {
                                                'interface': 'Ethernet1/2.200',
                                                'metric': 1,
                                                'next_hop': '10.1.3.1',
                                                'route_type': 'connected',
                                                'tag': 0,
                                                },
                                            },
                                        'next_hops': 0,
                                        },
                                    '10.2.3.0/24': {
                                        'best_route': True,
                                        'index': {
                                            1: {
                                                'expire_time': '00:02:52',
                                                'interface': 'Ethernet1/1.200',
                                                'metric': 2,
                                                'next_hop': '10.1.2.2',
                                                'tag': 0,
                                                },
                                            },
                                        'next_hops': 1,
                                        },
                                    '172.16.11.0/24': {
                                        'best_route': True,
                                        'index': {
                                            1: {
                                                'metric': 15,
                                                'next_hop': '0.0.0.0',
                                                'redistributed': True,
                                                'tag': 0,
                                                },
                                            },
                                        'next_hops': 1,
                                        },
                                    '192.168.2.2/32': {
                                        'best_route': True,
                                        'index': {
                                            1: {
                                                'expire_time': '00:02:52',
                                                'interface': 'Ethernet1/1.200',
                                                'metric': 2,
                                                'next_hop': '10.1.2.2',
                                                'tag': 0,
                                                },
                                            },
                                        'next_hops': 1,
                                        },
                                    '192.168.3.3/32': {
                                        'best_route': True,
                                        'index': {
                                            1: {
                                                'expire_time': '00:02:52',
                                                'interface': 'Ethernet1/1.200',
                                                'metric': 3,
                                                'next_hop': '10.1.2.2',
                                                'tag': 0,
                                                },
                                            },
                                        'next_hops': 1,
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
                                        'best_route': True,
                                        'index': {
                                            1: {
                                                'interface': 'Ethernet1/1.100',
                                                'metric': 1,
                                                'next_hop': '10.1.2.1',
                                                'route_type': 'connected',
                                                'tag': 0,
                                                },
                                            },
                                        'next_hops': 0,
                                        },
                                    '10.1.3.0/24': {
                                        'best_route': True,
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
                                        'next_hops': 1,
                                        },
                                    '10.2.3.0/24': {
                                        'best_route': True,
                                        'index': {
                                            1: {
                                                'expire_time': '00:00:05',
                                                'interface': 'Ethernet1/1.100',
                                                'metric': 2,
                                                'next_hop': '10.1.2.2',
                                                'tag': 0,
                                                },
                                            },
                                        'next_hops': 1,
                                        },
                                    '172.16.22.0/24': {
                                        'best_route': True,
                                        'index': {
                                            1: {
                                                'expire_time': '00:00:05',
                                                'interface': 'Ethernet1/1.100',
                                                'metric': 2,
                                                'next_hop': '10.1.2.2',
                                                'tag': 0,
                                                },
                                            },
                                        'next_hops': 1,
                                        },
                                    '172.16.33.0/24': {
                                        'best_route': True,
                                        'index': {
                                            1: {
                                                'expire_time': '00:00:05',
                                                'interface': 'Ethernet1/1.100',
                                                'metric': 3,
                                                'next_hop': '10.1.2.2',
                                                'tag': 0,
                                                },
                                            },
                                        'next_hops': 1,
                                        },
                                    '192.168.2.2/32': {
                                        'best_route': True,
                                        'index': {
                                            1: {
                                                'expire_time': '00:00:05',
                                                'interface': 'Ethernet1/1.100',
                                                'metric': 2,
                                                'next_hop': '10.1.2.2',
                                                'tag': 0,
                                                },
                                            },
                                        'next_hops': 1,
                                        },
                                    '192.168.3.3/32': {
                                        'best_route': True,
                                        'index': {
                                            1: {
                                                'expire_time': '00:00:05',
                                                'interface': 'Ethernet1/1.100',
                                                'metric': 3,
                                                'next_hop': '10.1.2.2',
                                                'tag': 0,
                                                },
                                            },
                                        'next_hops': 1,
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
        R1# show ip rip vrf all
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

    golden_parsed_output2 = {
        'vrf': {
            'default': {
                'address_family': {
                    'ipv4': {
                        'instance': {
                            'rip-1': {
                                'routes': {
                                    '10.1.0.0/8': {
                                        'best_route': True,
                                        'index': {
                                            1: {
                                                'expire_time': '00:02:33',
                                                'interface': 'Ethernet1/2.120',
                                                'metric': 2,
                                                'next_hop': '10.13.120.1',
                                                'tag': 0,
                                                },
                                            },
                                        'next_hops': 1,
                                        },
                                    '10.12.110.0/24': {
                                        'best_route': False,
                                        'index': {
                                            1: {
                                                'expire_time': '00:02:33',
                                                'interface': 'Ethernet1/2.120',
                                                'metric': 2,
                                                'next_hop': '10.13.120.1',
                                                'tag': 0,
                                                },
                                            },
                                        'next_hops': 1,
                                        },
                                    '10.12.115.0/24': {
                                        'best_route': False,
                                        'index': {
                                            1: {
                                                'expire_time': '00:02:33',
                                                'interface': 'Ethernet1/2.120',
                                                'metric': 2,
                                                'next_hop': '10.13.120.1',
                                                'tag': 0,
                                                },
                                            },
                                        'next_hops': 1,
                                        },
                                    '10.12.120.0/24': {
                                        'best_route': True,
                                        'index': {
                                            1: {
                                                'expire_time': '00:02:33',
                                                'interface': 'Ethernet1/2.120',
                                                'metric': 2,
                                                'next_hop': '10.13.120.1',
                                                'tag': 0,
                                                },
                                            },
                                        'next_hops': 1,
                                        },
                                    '10.12.90.0/24': {
                                        'best_route': False,
                                        'index': {
                                            1: {
                                                'expire_time': '00:02:33',
                                                'interface': 'Ethernet1/2.120',
                                                'metric': 2,
                                                'next_hop': '10.13.120.1',
                                                'tag': 0,
                                                },
                                            },
                                        'next_hops': 1,
                                        },
                                    '10.13.110.0/24': {
                                        'best_route': False,
                                        'index': {
                                            1: {
                                                'expire_time': '00:02:33',
                                                'interface': 'Ethernet1/2.120',
                                                'metric': 2,
                                                'next_hop': '10.13.120.1',
                                                'tag': 0,
                                                },
                                            },
                                        'next_hops': 1,
                                        },
                                    '10.13.115.0/24': {
                                        'best_route': False,
                                        'index': {
                                            1: {
                                                'expire_time': '00:02:33',
                                                'interface': 'Ethernet1/2.120',
                                                'metric': 2,
                                                'next_hop': '10.13.120.1',
                                                'tag': 0,
                                                },
                                            },
                                        'next_hops': 1,
                                        },
                                    '10.13.120.0/24': {
                                        'best_route': True,
                                        'index': {
                                            1: {
                                                'interface': 'Ethernet1/2.120',
                                                'metric': 1,
                                                'next_hop': '10.13.120.3',
                                                'route_type': 'connected',
                                                'tag': 0,
                                                },
                                            },
                                        'next_hops': 0,
                                        },
                                    '10.13.90.0/24': {
                                        'best_route': False,
                                        'index': {
                                            1: {
                                                'expire_time': '00:02:33',
                                                'interface': 'Ethernet1/2.120',
                                                'metric': 2,
                                                'next_hop': '10.13.120.1',
                                                'tag': 0,
                                                },
                                            },
                                        'next_hops': 1,
                                        },
                                    '10.23.120.0/24': {
                                        'best_route': True,
                                        'index': {
                                            1: {
                                                'interface': 'Ethernet1/1.120',
                                                'metric': 1,
                                                'next_hop': '10.23.120.3',
                                                'route_type': 'connected',
                                                'tag': 0,
                                                },
                                            },
                                        'next_hops': 0,
                                        },
                                    '10.36.3.3/32': {
                                        'best_route': True,
                                        'index': {
                                            1: {
                                                'interface': 'loopback0',
                                                'metric': 1,
                                                'next_hop': '10.36.3.3',
                                                'route_type': 'connected',
                                                'tag': 0,
                                                },
                                            },
                                        'next_hops': 0,
                                        },
                                    },
                                },
                            },
                        },
                    },
                },
            },
        }

    golden_output2 = {'execute.return_value': '''
        R3_nx# show ip rip route
        R3_nx# show ip rip route vrf default
        Process Name "rip-1" VRF "default"
        RIP routing table 
        
        > - indicates best RIP route
        
        >10.1.0.0/8 next-hops 1
         via 10.13.120.1 Ethernet1/2.120, metric 2, tag 0, timeout 00:02:33
        
        >10.36.3.3/32 next-hops 0
         via 10.36.3.3 loopback0, metric 1, tag 0, direct route
        
         10.12.90.0/24 next-hops 1
         via 10.13.120.1 Ethernet1/2.120, metric 2, tag 0, timeout 00:02:33
        
         10.12.110.0/24 next-hops 1
         via 10.13.120.1 Ethernet1/2.120, metric 2, tag 0, timeout 00:02:33
        
         10.12.115.0/24 next-hops 1
         via 10.13.120.1 Ethernet1/2.120, metric 2, tag 0, timeout 00:02:33
        
        >10.12.120.0/24 next-hops 1
         via 10.13.120.1 Ethernet1/2.120, metric 2, tag 0, timeout 00:02:33
        
         10.13.90.0/24 next-hops 1
         via 10.13.120.1 Ethernet1/2.120, metric 2, tag 0, timeout 00:02:33
        
         10.13.110.0/24 next-hops 1
         via 10.13.120.1 Ethernet1/2.120, metric 2, tag 0, timeout 00:02:33
        
         10.13.115.0/24 next-hops 1
         via 10.13.120.1 Ethernet1/2.120, metric 2, tag 0, timeout 00:02:33
        
        >10.13.120.0/24 next-hops 0
         via 10.13.120.3 Ethernet1/2.120, metric 1, tag 0, direct route
        
        >10.23.120.0/24 next-hops 0
         via 10.23.120.3 Ethernet1/1.120, metric 1, tag 0, direct route
    '''}

    def test_show_empty1(self):
        self.device = Mock(**self.empty_output)
        obj = ShowIpRipRouteVrfAll(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse(vrf='all')

    def test_show_golden1(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output1)
        obj = ShowIpRipRouteVrfAll(device=self.device)
        parsed_output = obj.parse(vrf='all')
        self.assertEqual(parsed_output, self.golden_parsed_output1)

    def test_show_empty2(self):
        self.device = Mock(**self.empty_output)
        obj = ShowIpRipRouteVrfAll(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_show_golden2(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output2)
        obj = ShowIpRipRouteVrfAll(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output2)

    def test_show_empty3(self):
        self.device = Mock(**self.empty_output)
        obj = ShowIpRipRouteVrfAll(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse(vrf='default')

    def test_show_golden3(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output2)
        obj = ShowIpRipRouteVrfAll(device=self.device)
        parsed_output = obj.parse(vrf='default')
        self.assertEqual(parsed_output, self.golden_parsed_output2)


class test_show_ip_rip_interface_vrf_all(unittest.TestCase):
    """Unit test for:
        * 'show ip rip interface'
        * 'show ip rip interface vrf {vrf}'
        * 'show ip rip interface vrf all' """

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
                                        'ipv4': {
                                            '10.1.2.1/24': {
                                                'ip': '10.1.2.1',
                                                'prefix_length': 24,
                                                },
                                            },
                                        'metric': 1,
                                        'oper_status': 'up',
                                        'split_horizon': True,
                                        'states': {
                                            'admin_state': 'up',
                                            'link_state': 'up',
                                            'protocol_state': 'up',
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
                                        'ipv4': {
                                            '10.1.3.1/24': {
                                                'ip': '10.1.3.1',
                                                'prefix_length': 24,
                                                },
                                            },
                                        'metric': 1,
                                        'oper_status': 'up',
                                        'split_horizon': True,
                                        'states': {
                                            'admin_state': 'up',
                                            'link_state': 'up',
                                            'protocol_state': 'up',
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
                                        'ipv4': {
                                            '10.1.2.1/24': {
                                                'ip': '10.1.2.1',
                                                'prefix_length': 24,
                                                },
                                            },
                                        'metric': 1,
                                        'oper_status': 'up',
                                        'passive': True,
                                        'split_horizon': True,
                                        'states': {
                                            'admin_state': 'up',
                                            'link_state': 'up',
                                            'protocol_state': 'up',
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
                                        'ipv4': {
                                            '10.1.3.1/24': {
                                                'ip': '10.1.3.1',
                                                'prefix_length': 24,
                                                },
                                            },
                                        'metric': 1,
                                        'oper_status': 'up',
                                        'split_horizon': True,
                                        'states': {
                                            'admin_state': 'up',
                                            'link_state': 'up',
                                            'protocol_state': 'up',
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
        R1# show ip rip interface vrf all
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

    golden_parsed_output2 = {
        'vrf': {
            'default': {
                'address_family': {
                    'ipv4': {
                        'instance': {
                            'rip-1': {
                                'interfaces': {
                                    'Ethernet1/1.120': {
                                        'ipv4': {
                                            '10.23.120.3/24': {
                                                'ip': '10.23.120.3',
                                                'prefix_length': 24,
                                                },
                                            },
                                        'metric': 1,
                                        'oper_status': 'up',
                                        'split_horizon': True,
                                        'states': {
                                            'admin_state': 'up',
                                            'link_state': 'up',
                                            'protocol_state': 'up',
                                            },
                                        },
                                    'Ethernet1/2.120': {
                                        'ipv4': {
                                            '10.13.120.3/24': {
                                                'ip': '10.13.120.3',
                                                'prefix_length': 24,
                                                },
                                            },
                                        'metric': 1,
                                        'oper_status': 'up',
                                        'split_horizon': True,
                                        'states': {
                                            'admin_state': 'up',
                                            'link_state': 'up',
                                            'protocol_state': 'up',
                                            },
                                        },
                                    'loopback0': {
                                        'ipv4': {
                                            '10.36.3.3/32': {
                                                'ip': '10.36.3.3',
                                                'prefix_length': 32,
                                                },
                                            },
                                        'metric': 1,
                                        'oper_status': 'up',
                                        'split_horizon': True,
                                        'states': {
                                            'admin_state': 'up',
                                            'link_state': 'up',
                                            'protocol_state': 'up',
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

    golden_output2 = {'execute.return_value': '''
    R3_nx# show ip rip interface
    R3_nx# show ip rip interface vrf default
    Process Name "rip-1" VRF "default"
    RIP-configured interface information
    
    Ethernet1/1.120, protocol-up/link-up/admin-up, RIP state : up
      address/mask 10.23.120.3/24, metric 1, split-horizon
    Ethernet1/2.120, protocol-up/link-up/admin-up, RIP state : up
      address/mask 10.13.120.3/24, metric 1, split-horizon
    loopback0, protocol-up/link-up/admin-up, RIP state : up
      address/mask 10.36.3.3/32, metric 1, split-horizon
            '''}

    def test_show_empty1(self):
        self.device = Mock(**self.empty_output)
        obj = ShowIpRipInterfaceVrfAll(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse(vrf='all')

    def test_show_empty2(self):
        self.device = Mock(**self.empty_output)
        obj = ShowIpRipInterfaceVrfAll(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_show_empty3(self):
        self.device = Mock(**self.empty_output)
        obj = ShowIpRipInterfaceVrfAll(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse(vrf='default')

    def test_show_golden1(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output1)
        obj = ShowIpRipInterfaceVrfAll(device=self.device)
        parsed_output = obj.parse(vrf='all')
        self.assertEqual(parsed_output, self.golden_parsed_output1)

    def test_show_golden2(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output2)
        obj = ShowIpRipInterfaceVrfAll(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output2)

    def test_show_golden3(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output2)
        obj = ShowIpRipInterfaceVrfAll(device=self.device)
        parsed_output = obj.parse(vrf='default')
        self.assertEqual(parsed_output, self.golden_parsed_output2)


class test_show_ipv6_rip_vrf_all(unittest.TestCase):
    """Unit test for:
        * 'show ipv6 rip'
        * 'show ipv6 rip vrf {vrf}'
        * 'show ipv6 rip vrf all' """

    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output1 = {
        'isolate_mode': False,
        'mmode': 'Initialized',
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
                                'maximum_paths': 16,
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
                                'process': 'up and running',
                                'timers': {
                                    'expire_in': 180,
                                    'collect_garbage': 120,
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
                                'maximum_paths': 16,
                                'multicast_group': 'ff02::9',
                                'port': 521,
                                'redistribute': {
                                    'static': {
                                        'route_policy': 'metric3_v6',
                                        },
                                    },
                                'process': 'up and running',
                                'timers': {
                                    'expire_in': 180,
                                    'collect_garbage': 120,
                                    'update_interval': 30,
                                    },
                                },
                            },
                        },
                    },
                },
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

    golden_parsed_output2 = {
        'isolate_mode': False,
        'mmode': 'Initialized',
        'vrf': {
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
                                'maximum_paths': 16,
                                'multicast_group': 'ff02::9',
                                'port': 521,
                                'redistribute': {
                                    'static': {
                                        'route_policy': 'metric3_v6',
                                        },
                                    },
                                'process': 'up and running',
                                'timers': {
                                    'expire_in': 180,
                                    'collect_garbage': 120,
                                    'update_interval': 30,
                                    },
                                },
                            },
                        },
                    },
                },
            },
        }

    golden_output2 = {'execute.return_value': '''
            R1# show ipv6 rip
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
            '''}

    def test_show_empty1(self):
        self.device = Mock(**self.empty_output)
        obj = ShowIpv6RipVrfAll(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse(vrf='all')

    def test_show_empty2(self):
        self.device = Mock(**self.empty_output)
        obj = ShowIpv6RipVrfAll(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_show_empty3(self):
        self.device = Mock(**self.empty_output)
        obj = ShowIpv6RipVrfAll(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse(vrf='default')

    def test_show_golden1(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output1)
        obj = ShowIpv6RipVrfAll(device=self.device)
        parsed_output = obj.parse(vrf='all')
        self.assertEqual(parsed_output, self.golden_parsed_output1)

    def test_show_golden2(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output2)
        obj = ShowIpv6RipVrfAll(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output2)

    def test_show_golden3(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output2)
        obj = ShowIpv6RipVrfAll(device=self.device)
        parsed_output = obj.parse(vrf='default')
        self.assertEqual(parsed_output, self.golden_parsed_output2)


class test_show_ipv6_rip_route_vrf_all(unittest.TestCase):
    """Unit test for:
        * 'show ipv6 rip route'
        * 'show ipv6 rip route vrf {vrf}'
        * 'show ipv6 rip route vrf all' """

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
                                        'best_route': True,
                                        'index': {
                                            1: {
                                                'metric': 1,
                                                'next_hop': '0::',
                                                'redistributed': True,
                                                'tag': 5,
                                                },
                                            },
                                        'next_hops': 1,
                                        },
                                    '2001:db8:1:2::/64': {
                                        'best_route': True,
                                        'index': {
                                            1: {
                                                'interface': 'Ethernet1/1.200',
                                                'metric': 1,
                                                'next_hop': '2001:db8:1:2::1',
                                                'route_type': 'connected',
                                                'tag': 0,
                                                },
                                            2: {
                                                'metric': 1,
                                                'next_hop': '0::',
                                                'redistributed': True,
                                                'tag': 0,
                                                },
                                            },
                                        'next_hops': 1,
                                        },
                                    '2001:db8:1:3::/64': {
                                        'best_route': True,
                                        'index': {
                                            1: {
                                                'interface': 'Ethernet1/2.200',
                                                'metric': 1,
                                                'next_hop': '2001:db8:1:3::1',
                                                'route_type': 'connected',
                                                'tag': 0,
                                                },
                                            2: {
                                                'metric': 1,
                                                'next_hop': '0::',
                                                'redistributed': True,
                                                'tag': 0,
                                                },
                                            },
                                        'next_hops': 1,
                                        },
                                    '2001:db8:2:3::/64': {
                                        'best_route': True,
                                        'index': {
                                            1: {
                                                'expire_time': '00:02:46',
                                                'interface': 'Ethernet1/1.200',
                                                'metric': 2,
                                                'next_hop': 'fe80::5c00:ff:fe01:7',
                                                'tag': 0,
                                                },
                                            },
                                        'next_hops': 1,
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
                                        'best_route': True,
                                        'index': {
                                            1: {
                                                'metric': 3,
                                                'next_hop': '0::',
                                                'redistributed': True,
                                                'tag': 0,
                                                },
                                            },
                                        'next_hops': 1,
                                        },
                                    '2001:db8:1112:1112::/64': {
                                        'best_route': True,
                                        'index': {
                                            1: {
                                                'metric': 3,
                                                'next_hop': '0::',
                                                'redistributed': True,
                                                'tag': 0,
                                                },
                                            },
                                        'next_hops': 1,
                                        },
                                    '2001:db8:1113:1113::/64': {
                                        'best_route': True,
                                        'index': {
                                            1: {
                                                'metric': 3,
                                                'next_hop': '0::',
                                                'redistributed': True,
                                                'tag': 0,
                                                },
                                            },
                                        'next_hops': 1,
                                        },
                                    '2001:db8:1:2::/64': {
                                        'best_route': True,
                                        'index': {
                                            1: {
                                                'interface': 'Ethernet1/1.100',
                                                'metric': 1,
                                                'next_hop': '2001:db8:1:2::1',
                                                'route_type': 'connected',
                                                'tag': 0,
                                                },
                                            },
                                        'next_hops': 0,
                                        },
                                    '2001:db8:1:3::/64': {
                                        'best_route': True,
                                        'index': {
                                            1: {
                                                'interface': 'Ethernet1/2.100',
                                                'metric': 1,
                                                'next_hop': '2001:db8:1:3::1',
                                                'route_type': 'connected',
                                                'tag': 0,
                                                },
                                            },
                                        'next_hops': 0,
                                        },
                                    '2001:db8:2222:2222::/64': {
                                        'best_route': True,
                                        'index': {
                                            1: {
                                                'expire_time': '00:02:36',
                                                'interface': 'Ethernet1/2.100',
                                                'metric': 7,
                                                'next_hop': 'fe80::5c00:ff:fe02:7',
                                                'tag': 0,
                                                },
                                            },
                                        'next_hops': 1,
                                        },
                                    '2001:db8:2223:2223::/64': {
                                        'best_route': True,
                                        'index': {
                                            1: {
                                                'expire_time': '00:02:39',
                                                'interface': 'Ethernet1/1.100',
                                                'metric': 6,
                                                'next_hop': 'fe80::5c00:ff:fe01:7',
                                                'tag': 0,
                                                },
                                            },
                                        'next_hops': 1,
                                        },
                                    '2001:db8:2:3::/64': {
                                        'best_route': True,
                                        'index': {
                                            1: {
                                                'expire_time': '00:02:36',
                                                'interface': 'Ethernet1/2.100',
                                                'metric': 2,
                                                'next_hop': 'fe80::5c00:ff:fe02:7',
                                                'tag': 0,
                                                },
                                            },
                                        'next_hops': 1,
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

    golden_parsed_output2 = {
        'vrf': {
            'default': {
                'address_family': {
                    'ipv4': {
                        'instance': {
                            'rip-1': {
                                'routes': {
                                    '2001:10:12:120::/64': {
                                        'best_route': False,
                                        'index': {
                                            1: {
                                                'expire_time': '00:02:58',
                                                'interface': 'Ethernet1/2.120',
                                                'metric': 2,
                                                'next_hop': 'fe80::f816:3eff:fe8f:fbd9',
                                                'tag': 0,
                                                },
                                            },
                                        'next_hops': 1,
                                        },
                                    '2001:10:13:120::/64': {
                                        'best_route': True,
                                        'index': {
                                            1: {
                                                'interface': 'Ethernet1/2.120',
                                                'metric': 1,
                                                'next_hop': '2001:10:13:120::3',
                                                'route_type': 'connected',
                                                'tag': 0,
                                                },
                                            },
                                        'next_hops': 0,
                                        },
                                    '2001:10:23:120::/64': {
                                        'best_route': True,
                                        'index': {
                                            1: {
                                                'interface': 'Ethernet1/1.120',
                                                'metric': 1,
                                                'next_hop': '2001:10:23:120::3',
                                                'route_type': 'connected',
                                                'tag': 0,
                                                },
                                            },
                                        'next_hops': 0,
                                        },
                                    '2001:1:1:1::1/128': {
                                        'best_route': False,
                                        'index': {
                                            1: {
                                                'expire_time': '00:02:58',
                                                'interface': 'Ethernet1/2.120',
                                                'metric': 2,
                                                'next_hop': 'fe80::f816:3eff:fe8f:fbd9',
                                                'tag': 0,
                                                },
                                            },
                                        'next_hops': 1,
                                        },
                                    '2001:3:3:3::3/128': {
                                        'best_route': True,
                                        'index': {
                                            1: {
                                                'interface': 'loopback0',
                                                'metric': 1,
                                                'next_hop': '2001:3:3:3::3',
                                                'route_type': 'connected',
                                                'tag': 0,
                                                },
                                            },
                                        'next_hops': 0,
                                        },
                                    },
                                },
                            },
                        },
                    },
                },
            },
        }

    golden_output2 = {'execute.return_value': '''
        R3_nx# show ipv6 rip route
        R3_nx# show ipv6 rip route vrf default
        Process Name "rip-1" VRF "default"
        RIP routing table 
        
        > - indicates best RIP route
        
         2001:1:1:1::1/128 next-hops 1
         via fe80::f816:3eff:fe8f:fbd9 Ethernet1/2.120, metric 2, tag 0, timeout 00:02:58
        
        >2001:3:3:3::3/128 next-hops 0
         via 2001:3:3:3::3 loopback0, metric 1, tag 0, direct route
        
         2001:10:12:120::/64 next-hops 1
         via fe80::f816:3eff:fe8f:fbd9 Ethernet1/2.120, metric 2, tag 0, timeout 00:02:58
        
        >2001:10:13:120::/64 next-hops 0
         via 2001:10:13:120::3 Ethernet1/2.120, metric 1, tag 0, direct route
        
        >2001:10:23:120::/64 next-hops 0
         via 2001:10:23:120::3 Ethernet1/1.120, metric 1, tag 0, direct route
    '''}

    def test_show_empty1(self):
        self.device = Mock(**self.empty_output)
        obj = ShowIpv6RipRouteVrfAll(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse(vrf='all')

    def test_show_empty2(self):
        self.device = Mock(**self.empty_output)
        obj = ShowIpv6RipRouteVrfAll(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_show_empty3(self):
        self.device = Mock(**self.empty_output)
        obj = ShowIpv6RipRouteVrfAll(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse(vrf='default')

    def test_show_golden1(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output1)
        obj = ShowIpv6RipRouteVrfAll(device=self.device)
        parsed_output = obj.parse(vrf='all')
        self.assertEqual(parsed_output, self.golden_parsed_output1)

    def test_show_golden2(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output2)
        obj = ShowIpv6RipRouteVrfAll(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output2)

    def test_show_golden3(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output2)
        obj = ShowIpv6RipRouteVrfAll(device=self.device)
        parsed_output = obj.parse(vrf='default')
        self.assertEqual(parsed_output, self.golden_parsed_output2)

if __name__ == '__main__':
    unittest.main()
