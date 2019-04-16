# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device

# Metaparset
from genie.metaparser.util.exceptions import SchemaEmptyParserError, \
                                       SchemaMissingKeyError

# Parser
from genie.libs.parser.iosxe.show_rip import ShowIpRipDatabase,\
                                             ShowIpv6RipDatabase,\
                                             ShowIpv6Rip

# ============================================
# Parser for 'show ip rip database'
# Parser for 'show ip rip database vrf {vrf}'
# ============================================
class test_show_ip_rip_database(unittest.TestCase):
    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output = {
        'vrf': {
            'default': {
                'address_family': {
                    'ipv4': {
                        'instance': {
                            'rip': {
                                'routes': {
                                    '0.0.0.0/0': {
                                        'index': {
                                            1: {
                                                'summary_type': 'auto-summary',
                                            },
                                            2:{
                                                'redistributed': True,
                                                'next_hop': '172.16.1.254',
                                                'from': '0.0.0.0',
                                                'metric': 3,
                                            },
                                            3: {
                                                'redistributed': True,
                                                'next_hop': '172.16.1.254',
                                                'from': '0.0.0.0',
                                                'metric': 3,
                                            },
                                        }
                                    },
                                    '10.0.0.0/8': {
                                        'index': {
                                            1: {
                                                'summary_type': 'auto-summary'
                                            },
                                        }
                                    },
                                    '10.1.2.0/24': {
                                        'index': {
                                            1: {
                                                'route_type': 'connected',
                                                'interface': 'GigabitEthernet2.100',
                                            },
                                        }
                                    },
                                    '10.1.3.0/24': {
                                        'index': {
                                            1: {
                                                'route_type': 'connected',
                                                'interface': 'GigabitEthernet3.100',
                                            },
                                        }
                                    },
                                    '10.2.3.0/24': {
                                        'index': {
                                            1: {
                                                'next_hop': '10.1.3.3',
                                                'expire_time': '00:00:05',
                                                'interface': 'GigabitEthernet3.100',
                                                'metric': 1,
                                            },
                                            2: {
                                                'next_hop': '10.1.2.2',
                                                'expire_time': '00:00:21',
                                                'interface': 'GigabitEthernet2.100',
                                                'metric': 1,
                                            },
                                        }
                                    },
                                    '172.16.0.0/16': {
                                        'index': {
                                            1: {
                                                'summary_type': 'auto-summary'
                                            },
                                        }
                                    },
                                    '172.16.0.0/17': {
                                        'index': {
                                            1: {
                                                'summary_type': 'int-summary'
                                            },
                                            2: {
                                                'next_hop': '10.1.2.2',
                                                'expire_time': '00:00:00',
                                                'interface': 'GigabitEthernet2.100',
                                                'metric': 4,
                                            },
                                        }
                                    },
                                },
                            },
                        },
                    },
                },
            },
        },
    }

    golden_output = {'execute.return_value': '''\
R1#show ip rip database
0.0.0.0/0    auto-summary
0.0.0.0/0    redistributed
    [3] via 172.16.1.254, from 0.0.0.0,
    [3] via 172.16.1.254, from 0.0.0.0,
10.0.0.0/8    auto-summary
10.1.2.0/24    directly connected, GigabitEthernet2.100
10.1.3.0/24    directly connected, GigabitEthernet3.100
10.2.3.0/24
    [1] via 10.1.3.3, 00:00:05, GigabitEthernet3.100
    [1] via 10.1.2.2, 00:00:21, GigabitEthernet2.100
172.16.0.0/16    auto-summary
172.16.0.0/17    int-summary
172.16.0.0/17
    [4] via 10.1.2.2, 00:00:00, GigabitEthernet2.100

    '''}

    golden_parsed_output_2 = {
        'vrf': {
            'VRF1': {
                'address_family': {
                    'ipv4': {
                        'instance': {
                            'rip': {
                                'routes': {
                                    '10.0.0.0/8': {
                                        'index': {
                                            1: {
                                                'summary_type': 'auto-summary'
                                            },
                                        }
                                    },
                                    '10.1.2.0/24': {
                                        'index': {
                                            1: {
                                                'route_type': 'connected',
                                                'interface': 'GigabitEthernet2.200',
                                            },
                                        }
                                    },
                                    '10.1.3.0/24': {
                                        'index': {
                                            1: {
                                                'route_type': 'connected',
                                                'interface': 'GigabitEthernet3.200',
                                            },
                                        }
                                    },
                                    '10.2.3.0/24': {
                                        'index': {
                                            1: {
                                                'next_hop': '10.1.2.2',
                                                'expire_time': '00:00:08',
                                                'interface': 'GigabitEthernet2.200',
                                                'metric': 1,
                                            },
                                        }
                                    },
                                    '172.16.0.0/16': {
                                        'index': {
                                            1: {
                                                'summary_type': 'auto-summary'
                                            },
                                        }
                                    },
                                    '172.16.11.0/24': {
                                        'index': {
                                            1: {
                                                'redistributed': True,
                                                'metric': 15,
                                                'next_hop': '0.0.0.0',
                                            },
                                        }
                                    },
                                    '172.16.22.0/24': {
                                        'index': {
                                            1: {
                                                'expire_time': '00:00:08',
                                                'interface': 'GigabitEthernet2.200',
                                                'metric': 15,
                                                'next_hop': '10.1.2.2',
                                            },
                                        }
                                    },
                                    '192.168.1.0/24': {
                                        'index': {
                                            1: {
                                                'summary_type': 'auto-summary',
                                            },
                                        }
                                    },
                                    '192.168.1.1/32': {
                                        'index': {
                                            1: {
                                                'redistributed': True,
                                                'metric': 1,
                                                'next_hop': '0.0.0.0',
                                            },
                                        }
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
R1#show ip rip database vrf VRF1
10.0.0.0/8    auto-summary
10.1.2.0/24    directly connected, GigabitEthernet2.200
10.1.3.0/24    directly connected, GigabitEthernet3.200
10.2.3.0/24
    [1] via 10.1.2.2, 00:00:08, GigabitEthernet2.200
172.16.0.0/16    auto-summary
172.16.11.0/24    redistributed
    [15] via 0.0.0.0,
172.16.22.0/24
    [15] via 10.1.2.2, 00:00:08, GigabitEthernet2.200
192.168.1.0/24    auto-summary
192.168.1.1/32    redistributed
    [1] via 0.0.0.0,
'''}

    def test_empty(self):
        self.device1 = Mock(**self.empty_output)
        obj = ShowIpRipDatabase(device=self.device1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden_vrf_default(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output)
        obj = ShowIpRipDatabase(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)

    def test_golden_vrf_vrf1(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_2)
        obj = ShowIpRipDatabase(device=self.device)
        parsed_output = obj.parse(vrf="VRF1")
        self.assertEqual(parsed_output, self.golden_parsed_output_2)

# ============================================
# Parser for 'show ipv6 rip database'
# Parser for 'show ipv6 rip vrf {vrf} database'
# ============================================
class test_show_ipv6_rip_database(unittest.TestCase):
    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output = {
        'vrf': {
            'default': {
                'address_family': {
                    'ipv6': {
                        'routes': {
                            '2001:DB8:1:3::/64': {
                                'index': {
                                    1: {
                                        'metric': 2,
                                        'interface': 'GigabitEthernet3.100',
                                        'next_hop': 'FE80::F816:3EFF:FEFF:1E3D',
                                        'expire_time': '179'
                                    },

                                }
                            },
                            '2001:DB8:2:3::/64': {
                                'index': {
                                    1: {
                                        'metric': 2,
                                        'installed': True,
                                        'interface': 'GigabitEthernet3.100',
                                        'next_hop': 'FE80::F816:3EFF:FEFF:1E3D',
                                        'expire_time': '179'
                                    },

                                }
                            },
                            '2001:DB8:2222:2222::/64': {
                                'index': {
                                    1: {
                                        'metric': 7,
                                        'installed': True,
                                        'interface': 'GigabitEthernet3.100',
                                        'next_hop': 'FE80::F816:3EFF:FEFF:1E3D',
                                        'expire_time': '179'
                                    },

                                }
                            },
                            '2001:DB8:2223:2223::/64': {
                                'index': {
                                    1: {
                                        'metric': 6,
                                        'installed': True,
                                        'interface': 'GigabitEthernet2.100',
                                        'next_hop': 'FE80::F816:3EFF:FE7B:437',
                                        'expire_time': '173'
                                    },

                                }
                            },
                        }
                    },
                },
            },
        },
    }

    golden_output = {'execute.return_value': '''\
R1#show ipv6 rip database
RIP VRF "Default VRF", local RIB
 2001:DB8:1:3::/64, metric 2
     GigabitEthernet3.100/FE80::F816:3EFF:FEFF:1E3D, expires in 179 secs
 2001:DB8:2:3::/64, metric 2, installed
     GigabitEthernet3.100/FE80::F816:3EFF:FEFF:1E3D, expires in 179 secs
 2001:DB8:2222:2222::/64, metric 7, installed
     GigabitEthernet3.100/FE80::F816:3EFF:FEFF:1E3D, expires in 179 secs
 2001:DB8:2223:2223::/64, metric 6, installed
     GigabitEthernet2.100/FE80::F816:3EFF:FE7B:437, expires in 173 secs
    '''}

    golden_parsed_output_2 = {
        'vrf': {
            'VRF1': {
                'address_family': {
                    'ipv6': {
                        'routes': {
                            '2001:DB8:1:2::/64': {
                                'index': {
                                    1: {
                                        'metric': 2,
                                        'interface': 'GigabitEthernet2.200',
                                        'next_hop': 'FE80::F816:3EFF:FE7B:437',
                                        'expire_time': '166'
                                    },
                                }
                            },
                            '2001:DB8:1:3::/64': {
                                'index': {
                                    1: {
                                        'metric': 2,
                                        'interface': 'GigabitEthernet3.200',
                                        'next_hop': 'FE80::F816:3EFF:FEFF:1E3D',
                                        'expire_time': '169'
                                    },
                                }
                            },
                            '2001:DB8:2:3::/64': {
                                'index': {
                                    1: {
                                        'metric': 2,
                                        'installed': True,
                                        'interface': 'GigabitEthernet3.200',
                                        'next_hop': 'FE80::F816:3EFF:FEFF:1E3D',
                                        'expire_time': '169'
                                    },
                                    2: {
                                        'metric': 2,
                                        'installed': True,
                                        'interface': 'GigabitEthernet2.200',
                                        'next_hop': 'FE80::F816:3EFF:FE7B:437',
                                        'expire_time': '166'
                                    },
                                }
                            },
                        },
                    },
                },
            },
        },
    }
    golden_output_2 = {'execute.return_value': '''\
R1#show ipv6 rip vrf VRF1 database
RIP VRF "VRF1", local RIB
 2001:DB8:1:2::/64, metric 2
     GigabitEthernet2.200/FE80::F816:3EFF:FE7B:437, expires in 166 secs
 2001:DB8:1:3::/64, metric 2
     GigabitEthernet3.200/FE80::F816:3EFF:FEFF:1E3D, expires in 169 secs
 2001:DB8:2:3::/64, metric 2, installed
     GigabitEthernet3.200/FE80::F816:3EFF:FEFF:1E3D, expires in 169 secs
     GigabitEthernet2.200/FE80::F816:3EFF:FE7B:437, expires in 166 secs
'''}

    def test_empty(self):
        self.device1 = Mock(**self.empty_output)
        obj = ShowIpv6RipDatabase(device=self.device1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden_vrf_default(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output)
        obj = ShowIpv6RipDatabase(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)

    def test_golden_vrf_vrf1(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_2)
        obj = ShowIpv6RipDatabase(device=self.device)
        parsed_output = obj.parse(vrf="VRF1")
        self.assertEqual(parsed_output, self.golden_parsed_output_2)

# ============================================
# Parser for 'show ipv6 rip'
# Parser for 'show ipv6 rip vrf {vrf}'
# ============================================
class test_show_ipv6_rip(unittest.TestCase):
    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output = {
        'vrf': {
            'default': {
                'address_family': {
                    'ipv6': {
                        'port': 521,
                        'multicast_group': 'FF02::9',
                        'pid': 635,
                        'distance': 120,
                        'maximum_paths': 16,
                        'split_horizon': True,
                        'poison_reverse': False,
                        'originate_default_route': {
                            'enabled': False,
                        },
                        'timers': {
                            'flush_interval': 120,
                            'holddown_interval': 0,
                            'update_interval': 30,
                            'expire_time': 180,
                        },
                        'redistribute': {
                            'static': {
                                'metric': 3,
                            },
                        },
                        'interfaces': {
                           'GigabitEthernet3.100': {},
                           'GigabitEthernet2.100': {},
                        },
                        'statistics': {
                            'periodic_updates': 399,
                            'delayed_events': 0,
                            'trigger_updates': 8,
                            'full_advertisement': 0,
                        },
                    },
                },
            },
        },
    }

    golden_output = {'execute.return_value': '''\
    R1#show ipv6 rip
RIP VRF "Default VRF", port 521, multicast-group FF02::9, pid 635
     Administrative distance is 120. Maximum paths is 16
     Updates every 30 seconds, expire after 180
     Holddown lasts 0 seconds, garbage collect after 120
     Split horizon is on; poison reverse is off
     Default routes are not generated
     Periodic updates 399, trigger updates 8
     Full Advertisement 0, Delayed Events 0
  Interfaces:
    GigabitEthernet3.100
    GigabitEthernet2.100
  Redistribution:
    Redistributing protocol static with metric 3
    '''}

    golden_parsed_output_2 = {
        'vrf': {
            'VRF1': {
                'address_family': {
                    'ipv6': {
                        'port': 521,
                        'multicast_group': 'FF02::9',
                        'pid': 635,
                        'distance': 120,
                        'maximum_paths': 16,
                        'split_horizon': True,
                        'poison_reverse': False,
                        'originate_default_route': {
                            'enabled': True,
                        },
                        'timers': {
                            'flush_interval': 120,
                            'holddown_interval': 0,
                            'update_interval': 30,
                            'expire_time': 180,
                        },
                        'redistribute': {
                            'static': {
                                'route_policy': 'static-to-rip',
                            },
                            'connected':{},
                        },
                        'interfaces': {
                            'GigabitEthernet3.200': {},
                            'GigabitEthernet2.200': {},
                        },
                        'statistics': {
                            'periodic_updates': 390,
                            'delayed_events': 0,
                            'trigger_updates': 3,
                            'full_advertisement': 0,
                        },
                    },
                },
            },
        },

    }
    golden_output_2 = {'execute.return_value': '''
    R1#show ipv6 rip vrf VRF1
RIP VRF "VRF1", port 521, multicast-group FF02::9, pid 635
     Administrative distance is 120. Maximum paths is 16
     Updates every 30 seconds, expire after 180
     Holddown lasts 0 seconds, garbage collect after 120
     Split horizon is on; poison reverse is off
     Default routes are generated
     Periodic updates 390, trigger updates 3
     Full Advertisement 0, Delayed Events 0
  Interfaces:
    GigabitEthernet3.200
    GigabitEthernet2.200
  Redistribution:
    Redistributing protocol connected with transparent metric
    Redistributing protocol static with transparent metric route-map static-to-rip
'''}

    golden_parsed_output_3 = {
        'vrf': {
            'VRF1': {
                'address_family': {
                    'ipv6': {
                        'port': 521,
                        'multicast_group': 'FF02::9',
                        'pid': 635,
                        'distance': 120,
                        'maximum_paths': 16,
                        'split_horizon': True,
                        'poison_reverse': False,
                        'originate_default_route': {
                            'enabled': True,
                        },
                        'timers': {
                            'flush_interval': 120,
                            'holddown_interval': 0,
                            'update_interval': 30,
                            'expire_time': 180,
                        },
                        'interfaces': {
                            'GigabitEthernet3.200': {},
                            'GigabitEthernet2.200': {},
                        },
                        'statistics': {
                            'periodic_updates': 390,
                            'delayed_events': 0,
                            'trigger_updates': 3,
                            'full_advertisement': 0,
                        },
                    },
                },
            },
        },

    }
    golden_output_3 = {'execute.return_value': '''
        R1#show ipv6 rip vrf VRF1
    RIP VRF "VRF1", port 521, multicast-group FF02::9, pid 635
         Administrative distance is 120. Maximum paths is 16
         Updates every 30 seconds, expire after 180
         Holddown lasts 0 seconds, garbage collect after 120
         Split horizon is on; poison reverse is off
         Default routes are generated
         Periodic updates 390, trigger updates 3
         Full Advertisement 0, Delayed Events 0
      Interfaces:
        GigabitEthernet3.200
        GigabitEthernet2.200
      Redistribution:
        None
    '''}
    def test_empty(self):
        self.device1 = Mock(**self.empty_output)
        obj = ShowIpv6Rip(device=self.device1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden_vrf_default(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output)
        obj = ShowIpv6Rip(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)

    def test_golden_vrf_vrf1(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_2)
        obj = ShowIpv6Rip(device=self.device)
        parsed_output = obj.parse(vrf="VRF1")
        self.assertEqual(parsed_output, self.golden_parsed_output_2)

    def test_golden_vrf_vrf1_non_distribution(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_3)
        obj = ShowIpv6Rip(device=self.device)
        parsed_output = obj.parse(vrf="VRF1")
        self.assertEqual(parsed_output, self.golden_parsed_output_3)
if __name__ == '__main__':
    unittest.main()