# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device

# Metaparset
from genie.metaparser.util.exceptions import SchemaEmptyParserError, \
                                       SchemaMissingKeyError

# Parser
from genie.libs.parser.iosxe.show_rip import ShowIpProtocols,\
                                             ShowIpv6Protocols,\
                                             ShowIpRipDatabase,\
                                             ShowIpv6RipDatabase,\
                                             ShowIpv6Rip


# ============================================
# Parser for 'show ip protocols | sec rip'
# Parser for 'show ip protocols vrf {vrf} | sec rip'
# ============================================
class test_show_ip_protocols(unittest.TestCase):
    
    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}
    
    golden_parsed_output = {
        'vrf': {
            'default': {
                'address_family': {
                    'ipv4': {
                        'instance': {
                            'rip': {
                                'distance': 120,
                                'maximum_paths': 4,
                                'output_delay': 50,
                                'redistribute': {
                                    'connected': {},
                                    'static': {},
                                    'rip': {},
                                },
                                'timers': {
                                    'update_interval': 10,
                                    'invalid_interval': 21,
                                    'holddown_interval': 22,
                                    'flush_interval': 23,
                                },
                                'interfaces': {
                                    'GigabitEthernet3.100': {
                                        'summary_address': {
                                            '172.16.0.0/17': {},
                                        },
                                        'passive': 'GigabitEthernet2.100',
                                        'send': 2,
                                        'receive': 2,
                                        'triggered_rip': 'no',
                                        'key_chain': '1',
                                    },
                                },
                                'neighbors': {
                                    '10.1.3.3': {
                                        'last_update': '00:00:00',
                                    },
                                    '10.1.2.2': {
                                        'last_update': '00:00:04',
                                    },
                                },
                            },
                        },
                    },
                },
            },
        }
    }
    golden_output = {'execute.return_value': '''\
R1#show ip protocols | sec rip
Routing Protocol is "rip"
  Output delay 50 milliseconds between packets
  Outgoing update filter list for all interfaces is not set
  Incoming update filter list for all interfaces is not set
  Incoming routes will have 10 added to metric if on list 21
  Sending updates every 10 seconds, next due in 8 seconds
  Invalid after 21 seconds, hold down 22, flushed after 23
  Default redistribution metric is 3
  Redistributing: connected, static, rip
  Neighbor(s):
    10.1.2.2
  Default version control: send version 2, receive version 2
    Interface                           Send  Recv  Triggered RIP  Key-chain
    GigabitEthernet3.100                2     2          No        1
  Automatic network summarization is not in effect
  Address Summarization:
    172.16.0.0/17 for GigabitEthernet3.100
  Maximum path: 4
  Routing for Networks:
    10.0.0.0
  Passive Interface(s):
    GigabitEthernet2.100
  Routing Information Sources:
    Gateway         Distance      Last Update
    10.1.3.3             120      00:00:00
    10.1.2.2             120      00:00:04
  Distance: (default is 120)

    '''}

    golden_parsed_output_2 = {
        'vrf': {
            'VRF1': {
                'address_family': {
                    'ipv4': {
                        'instance': {
                            'rip': {
                                'distance': 120,
                                'maximum_paths': 4,
                                'output_delay': 50,
                                'redistribute': {
                                    'connected': {},
                                    'static': {},
                                    'rip': {},
                                },
                                'timers': {
                                    'update_interval': 30,
                                    'invalid_interval': 180,
                                    'holddown_interval': 180,
                                    'flush_interval': 240,
                                },
                                'interfaces': {
                                    'GigabitEthernet2.200': {
                                        'send': 2,
                                        'receive': 2,
                                        'triggered_rip': 'no',
                                        'key_chain': 'none',
                                    },
                                    'GigabitEthernet3.200': {
                                        'send': 2,
                                        'receive': 2,
                                        'triggered_rip': 'no',
                                        'key_chain': 'none',
                                    },
                                },
                                'neighbors': {
                                    '10.1.3.3': {
                                        'last_update': '20:33:00',
                                    },
                                    '10.1.2.2': {
                                        'last_update': '00:00:21',
                                    },
                                },
                            },
                        },
                    },
                },
            },
        }
    }
    golden_output_2 = {'execute.return_value':'''
R1#show ip protocols vrf VRF1 | sec rip
Routing Protocol is "rip"
  Output delay 50 milliseconds between packets
  Outgoing update filter list for all interfaces is not set
  Incoming update filter list for all interfaces is not set
  Sending updates every 30 seconds, next due in 2 seconds
  Invalid after 180 seconds, hold down 180, flushed after 240
  Redistributing: connected, static, rip
  Default version control: send version 2, receive version 2
    Interface                           Send  Recv  Triggered RIP  Key-chain
    GigabitEthernet2.200                2     2          No        none
    GigabitEthernet3.200                2     2          No        none
  Maximum path: 4
  Routing for Networks:
     10.0.0.0
    10.0.0.0
  Routing Information Sources:
    Gateway         Distance      Last Update
    10.1.3.3             120      20:33:00
    10.1.2.2             120      00:00:21
  Distance: (default is 120)
'''}
    def test_empty(self):
        self.device1 = Mock(**self.empty_output)
        obj = ShowIpProtocols(device=self.device1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden_vrf_default(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output)
        obj = ShowIpProtocols(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output)

    def test_golden_vrf_vrf1(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_2)
        obj = ShowIpProtocols(device=self.device)
        parsed_output = obj.parse(vrf="VRF1")
        self.assertEqual(parsed_output,self.golden_parsed_output_2)

# ============================================
# Parser for 'show ipv6 protocols | sec rip'
# Parser for 'show ipv6 protocols vrf {vrf} | sec rip'
# ============================================
class test_show_ipv6_protocols(unittest.TestCase):
    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output = {
        'vrf': {
            'default': {
                'address_family': {
                    'ipv6': {
                        'instance': {
                            'rip ripng': {
                                'redistribute': {
                                    'static': {
                                        'metric': 3,
                                    },
                                },
                                'interfaces': {
                                   'GigabitEthernet3.100': {},
                                   'GigabitEthernet2.100': {},
                                    },
                                },
                            },
                        },
                    },
                },
            },
        }

    golden_output = {'execute.return_value': '''\
R1#show ipv6 protocols | sec rip
IPv6 Routing Protocol is "rip ripng"
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
                        'instance': {
                            'rip ripng': {
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
                            },
                        },
                    },
                },
            },
        },

    }
    golden_output_2 = {'execute.return_value': '''
R1#show ipv6 protocols vrf VRF1 | sec rip
IPv6 Routing Protocol is "rip ripng"
  Interfaces:
    GigabitEthernet3.200
    GigabitEthernet2.200
  Redistribution:
    Redistributing protocol connected with transparent metric
    Redistributing protocol static with transparent metric route-map static-to-rip
'''}

    def test_empty(self):
        self.device1 = Mock(**self.empty_output)
        obj = ShowIpv6Protocols(device=self.device1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden_vrf_default(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output)
        obj = ShowIpv6Protocols(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)

    def test_golden_vrf_vrf1(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_2)
        obj = ShowIpv6Protocols(device=self.device)
        parsed_output = obj.parse(vrf="VRF1")
        self.assertEqual(parsed_output, self.golden_parsed_output_2)

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
                                        'route_type': 'installed',
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
                                        'route_type': 'installed',
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
                                        'route_type': 'installed',
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
                                        'route_type': 'installed',
                                        'interface': 'GigabitEthernet3.200',
                                        'next_hop': 'FE80::F816:3EFF:FEFF:1E3D',
                                        'expire_time': '169'
                                    },
                                    2: {
                                        'metric': 2,
                                        'route_type': 'installed',
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
        obj = ShowIpRipDatabase(device=self.device1)
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
                           'GigabitEthernet3.100': {
                               'split_horizon': True,
                               'poison_reverse': False,
                               'timers': {
                                   'update_interval': 399,
                                   'holddown_interval': 0,
                                   'trigger_interval': 8,
                                   'full_advertisement': 0,
                               },
                           },
                           'GigabitEthernet2.100': {
                               'split_horizon': True,
                               'poison_reverse': False,
                               'timers': {
                                   'update_interval': 399,
                                   'holddown_interval': 0,
                                   'trigger_interval': 8,
                                   'full_advertisement': 0,
                               },
                           },
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
                            'GigabitEthernet3.200': {
                                'split_horizon': True,
                                'poison_reverse': False,
                                'timers': {
                                    'update_interval': 390,
                                    'holddown_interval': 0,
                                    'trigger_interval': 3,
                                    'full_advertisement': 0,
                                },
                            },
                            'GigabitEthernet2.200': {
                                'split_horizon': True,
                                'poison_reverse': False,
                                'timers':{
                                    'update_interval': 390,
                                    'holddown_interval': 0,
                                    'trigger_interval': 3,
                                    'full_advertisement': 0,
                                },
                            },
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

if __name__ == '__main__':
    unittest.main()