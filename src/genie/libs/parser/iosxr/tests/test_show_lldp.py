# Python
import unittest
from unittest.mock import Mock

# ATS
from pyats.topology import Device
from pyats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError, \
    SchemaMissingKeyError

# iosxr show_ospf
from genie.libs.parser.iosxr.show_lldp import ShowLldp, \
    ShowLldpEntry, \
    ShowLldpNeighborsDetail, \
    ShowLldpTraffic, \
    ShowLldpInterface


class test_show_lldp(unittest.TestCase):
    dev = Device(name='d')
    empty_output = {'execute.return_value': ''}
    golden_parsed_output = {
        "hello_timer": 30,
        "enabled": True,
        "hold_timer": 120,
        "status": "active",
        "reinit_delay": 2
    }
    golden_output = {'execute.return_value': '''\

    Mon Mar 19 18:23:08.490 UTC
    Global LLDP information:
            Status: ACTIVE
            LLDP advertisements are sent every 30 seconds
            LLDP hold time advertised is 120 seconds
            LLDP interface reinitialisation delay is 2 seconds
    '''}

    def test_empty(self):
        self.dev = Mock(**self.empty_output)
        obj = ShowLldp(device=self.dev)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden(self):
        self.maxDiff = None
        self.dev = Mock(**self.golden_output)
        obj = ShowLldp(device=self.dev)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


class TestShowLldpEntry(unittest.TestCase):
    dev1 = Device(name='empty')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output = {
        'interfaces': {
            'GigabitEthernet0/0/0/0': {
                'port_id': {
                    'GigabitEthernet2': {
                        'neighbors': {
                            'Ge_nie1000v.openstacklocal': {
                                'chassis_id': '001e.49ff.24f7',
                                'port_description': 'GigabitEthernet2',
                                'system_name': 'Ge_nie1000v.openstacklocal',
                                'neighbor_id': 'Ge_nie1000v.openstacklocal',
                                'system_description': 'Cisco IOS Software [Everest], Virtual XE Software (X86_64_LINUX_IOSD-UNIVERSALK9-M), Version 16.6.1, RELEASE SOFTWARE (fc2)\nTechnical Support: http://www.cisco.com/techsupport\nCopyright (c) 1986-2017 by Cisco Systems, Inc.\nCompiled Sat 22-Jul-17 05:51 by',
                                'time_remaining': 117,
                                'hold_time': 120,
                                'capabilities': {
                                    'bridge': {
                                        'system': True,
                                    },
                                    'router': {
                                        'system': True,
                                        'enabled': True,
                                    },
                                },
                                'management_address': '10.1.2.1',
                            },
                        },
                    },
                },
            },
            'GigabitEthernet0/0/0/1': {
                'port_id': {
                    'Ethernet1/2': {
                        'neighbors': {
                            'G1_n9ie': {
                                'chassis_id': '5e00.80ff.020b',
                                'port_description': 'Ethernet1/2',
                                'system_name': 'G1_n9ie',
                                'neighbor_id': 'G1_n9ie',
                                'system_description': 'Cisco Nexus Operating System (NX-OS) Software 7.0(3)I7(1)\nTAC support: http://www.cisco.com/tac\nCopyright (c) 2002-2017, Cisco Systems, Inc. All rights reserved.\n',
                                'time_remaining': 103,
                                'hold_time': 120,
                                'capabilities': {
                                    'bridge': {
                                        'system': True,
                                        'enabled': True,
                                    },
                                    'router': {
                                        'system': True,
                                        'enabled': True,
                                    },
                                },
                            },
                        },
                    },
                },
            },
        },
        'total_entries': 2,
    }

    golden_output = {'execute.return_value': '''\
        Mon Mar 19 18:23:32.251 UTC
        Capability codes:
                (R) Router, (B) Bridge, (T) Telephone, (C) DOCSIS Cable Device
                (W) WLAN Access Point, (P) Repeater, (S) Station, (O) Other

        ------------------------------------------------
        Local Interface: GigabitEthernet0/0/0/0
        Chassis id: 001e.49ff.24f7
        Port id: Gi2
        Port Description: GigabitEthernet2
        System Name: Ge_nie1000v.openstacklocal

        System Description:
        Cisco IOS Software [Everest], Virtual XE Software (X86_64_LINUX_IOSD-UNIVERSALK9-M), Version 16.6.1, RELEASE SOFTWARE (fc2)
        Technical Support: http://www.cisco.com/techsupport
        Copyright (c) 1986-2017 by Cisco Systems, Inc.
        Compiled Sat 22-Jul-17 05:51 by

        Time remaining: 117 seconds
        Hold Time: 120 seconds
        System Capabilities: B,R
        Enabled Capabilities: R
        Management Addresses:
         IPv4 address: 10.1.2.1



        ------------------------------------------------
        Local Interface: GigabitEthernet0/0/0/1
        Chassis id: 5e00.80ff.020b
        Port id: Ethernet1/2
        Port Description: Ethernet1/2
        System Name: G1_n9ie

        System Description:
        Cisco Nexus Operating System (NX-OS) Software 7.0(3)I7(1)
        TAC support: http://www.cisco.com/tac
        Copyright (c) 2002-2017, Cisco Systems, Inc. All rights reserved.

        Time remaining: 103 seconds
        Hold Time: 120 seconds
        System Capabilities: B,R
        Enabled Capabilities: B,R
        Management Addresses - not advertised


        Total entries displayed: 2

     '''}

    device_output = {'execute.return_value': '''
            Mon Oct 21 18:41:43.442 EDT
        Capability codes:
            (R) Router, (B) Bridge, (T) Telephone, (C) DOCSIS Cable Device
            (W) WLAN Access Point, (P) Repeater, (S) Station, (O) Other

        ------------------------------------------------
        Local Interface: TenGigE0/0/0/41
        Chassis id: 00bc.60ff.7ff0
        Port id: TenGigE0/0/0/0/0
        Port Description - not advertised
        System Name: genie1-ggN1.ie-genie1

        System Description: 
         6.5.3, NCS-5500

        Time remaining: 100 seconds
        Hold Time: 120 seconds
        System Capabilities: R
        Enabled Capabilities: R
        Management Addresses:
          IPv4 address: 10.10.10.2

        Peer MAC Address: 00:bc:60:ff:7f:17


        ------------------------------------------------
        Local Interface: HundredGigE0/0/1/1
        Chassis id: 008a.96ff.2f8c
        Port id: HundredGigE0/0/0/2
        Port Description: to gen-8 nie  0/0/1/1 via gee1.dev 29-30 
        System Name: system2

        System Description: 
         7.0.1, NCS-5500

        Time remaining: 97 seconds
        Hold Time: 120 seconds
        System Capabilities: R
        Enabled Capabilities: R
        Management Addresses:
          IPv4 address: 10.10.10.10

        Peer MAC Address: 00:8a:96:ff:2b:13


        ------------------------------------------------
        Local Interface: HundredGigE0/0/1/0
        Chassis id: 008a.96ff.178c
        Port id: HundredGigE0/0/0/2
        Port Description: to gen-8 nie  0/0/1/0 via gee1.dev 31-32 
        System Name: system1

        System Description: 
         7.0.1, NCS-5500

        Time remaining: 117 seconds
        Hold Time: 120 seconds
        System Capabilities: R
        Enabled Capabilities: R
        Management Addresses:
          IPv4 address: 10.10.10.11

        Peer MAC Address: 00:8a:96:ff:13:13


        Total entries displayed: 3
    '''}

    expected_output = {
        'interfaces': {
            'HundredGigE0/0/1/0': {
                'port_id': {
                    'HundredGigE0/0/0/2': {
                        'neighbors': {
                            'system1': {
                                'capabilities': {
                                    'router': {
                                        'enabled': True,
                                        'system': True,
                                    },
                                },
                                'peer_mac': '00:8a:96:ff:13:13',
                                'chassis_id': '008a.96ff.178c',
                                'hold_time': 120,
                                'management_address': '10.10.10.11',
                                'neighbor_id': 'system1',
                                'port_description': 'to gen-8 nie  0/0/1/0 via gee1.dev 31-32',
                                'system_description': '',
                                'system_name': 'system1',
                                'time_remaining': 117,
                            },
                        },
                    },
                },
            },
            'HundredGigE0/0/1/1': {
                'port_id': {
                    'HundredGigE0/0/0/2': {
                        'neighbors': {
                            'system2': {
                                'capabilities': {
                                    'router': {
                                        'enabled': True,
                                        'system': True,
                                    },
                                },
                                'peer_mac': '00:8a:96:ff:2b:13',
                                'chassis_id': '008a.96ff.2f8c',
                                'hold_time': 120,
                                'management_address': '10.10.10.10',
                                'neighbor_id': 'system2',
                                'port_description': 'to gen-8 nie  0/0/1/1 via gee1.dev 29-30',
                                'system_description': '',
                                'system_name': 'system2',
                                'time_remaining': 97,
                            },
                        },
                    },
                },
            },
            'TenGigE0/0/0/41': {
                'port_id': {
                    'TenGigE0/0/0/0/0': {
                        'neighbors': {
                            'genie1-ggN1.ie-genie1': {
                                'capabilities': {
                                    'router': {
                                        'enabled': True,
                                        'system': True,
                                    },
                                },
                                'peer_mac': '00:bc:60:ff:7f:17',
                                'chassis_id': '00bc.60ff.7ff0',
                                'hold_time': 120,
                                'management_address': '10.10.10.2',
                                'neighbor_id': 'genie1-ggN1.ie-genie1',
                                'port_description': 'not advertised',
                                'system_description': '',
                                'system_name': 'genie1-ggN1.ie-genie1',
                                'time_remaining': 100,
                            },
                        },
                    },
                },
            },
        },
        'total_entries': 3,
    }

    device_output2 = {'execute.return_value': '''
        Local Interface: TenGigE0/1/0/0
    Parent Interface: Bundle-Ether1
    Chassis id: ccd8.c1ff.49dc
    Port id: Bundle-Ether2
    Port Description: 10G to ge1-genie port Ge1/1/1/1:GG1 
    System Name: geni5-genie

    System Description: 
    Cisco IOS XR Software, Version 6.5.3[Default]
    Copyright (c) 2019 by Cisco Systems, Inc., ASR9K Series

    Time remaining: 99 seconds
    Hold Time: 120 seconds
    System Capabilities: R
    Enabled Capabilities: R
    Management Addresses:
      IPv4 address: 10.10.10.12

    Peer MAC Address: cc:d8:c1:ff:49:df

        Local Interface: TenGigE0/5/0/5
    Chassis id: c471.feff.70c3
    Port id: Te0/1/0/3
    Port Description: 10G link to genie1-genie port TEN 0/5/0/5 in BE 43 (with port 0/4/0/3)
    System Name: system3

    System Description: 
    Cisco IOS XR Software, Version 6.4.2[Default]
    Copyright (c) 2019 by Cisco Systems, Inc., CRS

    Time remaining: 108 seconds
    Hold Time: 120 seconds
    System Capabilities: R
    Enabled Capabilities: R
    Management Addresses:
      IPv4 address: 10.10.10.13

    Peer MAC Address: c4:71:fe:ff:73:3d

        Local Interface: TenGigE0/5/0/6
    Chassis id: 8426.2bff.e85a
    Port id: 1611153480
    Port Description: 2/1/9, 10-Gig Ethernet, "10G interface to genie1-genie port 0/5/0/6-DO NOT SHUT or REMOVE..Mitch"
    System Name: GENIE02GEN2

    System Description: 
    TiMOS-C-16.0.R7 cpm/hops64 Nokia 7950 XRS Copyright (c) 2000-2019 Nokia.
    All rights reserved. All use subject to applicable license agreements.
    Built on Wed Apr 10 16:45:38 PDT 2019 by builder in /builds/c/160B/R7/panos/main


    Time remaining: 105 seconds
    Hold Time: 121 seconds
    System Capabilities: B,R
    Enabled Capabilities: B,R
    Management Addresses:
      IPv4 address: 10.10.10.14

    Peer MAC Address: a0:f3:e4:ff:19:d4
    
    Local Interface: TenGigE0/5/0/8
    Chassis id: 8426.2bff.e85a
    Port id: 8426.2bff.e85a
    Port Description - not advertised
    System Name - not advertised
    System Description - not advertised
    
    Time remaining: 74 seconds
    Hold Time: 14 seconds
    System Capabilities: N/A
    Enabled Capabilities: N/A
    Management Addresses - not advertised
    Peer MAC Address: c4:71:fe:ff:73:3d

    Total entries displayed: 4
    '''}
    expected_output2 = {
        'interfaces': {
            'TenGigE0/1/0/0': {
                'port_id': {
                    'Bundle-Ether2': {
                        'neighbors': {
                            'geni5-genie': {
                                'chassis_id': 'ccd8.c1ff.49dc',
                                'port_description': '10G to ge1-genie port Ge1/1/1/1:GG1',
                                'system_name': 'geni5-genie',
                                'neighbor_id': 'geni5-genie',
                                'system_description': 'Cisco IOS XR Software, Version 6.5.3[Default]\nCopyright (c) 2019 by Cisco Systems, Inc., ASR9K Series\n',
                                'time_remaining': 99,
                                'hold_time': 120,
                                'capabilities': {
                                    'router': {
                                        'system': True,
                                        'enabled': True
                                    }
                                },
                                'management_address': '10.10.10.12',
                                'peer_mac': 'cc:d8:c1:ff:49:df'
                            }
                        }
                    }
                }
            },
            'TenGigE0/5/0/5': {
                'port_id': {
                    'TenGigabitEthernet0/1/0/3': {
                        'neighbors': {
                            'system3': {
                                'chassis_id': 'c471.feff.70c3',
                                'port_description': '10G link to genie1-genie port TEN 0/5/0/5 in BE 43 (with port 0/4/0/3)',
                                'system_name': 'system3',
                                'neighbor_id': 'system3',
                                'system_description': 'Cisco IOS XR Software, Version 6.4.2[Default]\nCopyright (c) 2019 by Cisco Systems, Inc., CRS\n',
                                'time_remaining': 108,
                                'hold_time': 120,
                                'capabilities': {
                                    'router': {
                                        'system': True,
                                        'enabled': True
                                    }
                                },
                                'management_address': '10.10.10.13',
                                'peer_mac': 'c4:71:fe:ff:73:3d'
                            }
                        }
                    }
                }
            },
            'TenGigE0/5/0/6': {
                'port_id': {
                    '1611153480': {
                        'neighbors': {
                            'GENIE02GEN2': {
                                'chassis_id': '8426.2bff.e85a',
                                'port_description': '2/1/9, 10-Gig Ethernet, "10G interface to genie1-genie port 0/5/0/6-DO NOT SHUT or REMOVE..Mitch"',
                                'system_name': 'GENIE02GEN2',
                                'neighbor_id': 'GENIE02GEN2',
                                'system_description': '',
                                'time_remaining': 105,
                                'hold_time': 121,
                                'capabilities': {
                                    'bridge': {
                                        'system': True,
                                        'enabled': True
                                    },
                                    'router': {
                                        'system': True,
                                        'enabled': True
                                    }
                                },
                                'management_address': '10.10.10.14',
                                'peer_mac': 'a0:f3:e4:ff:19:d4'
                            }
                        }
                    }
                }
            },
            'TenGigE0/5/0/8': {
                'port_id': {
                    '8426.2bff.e85a': {
                        'neighbors': {
                            'c4:71:fe:ff:73:3d': {
                                'chassis_id': '8426.2bff.e85a',
                                'port_description': 'not advertised',
                                'time_remaining': 74,
                                'hold_time': 14,
                                'peer_mac': 'c4:71:fe:ff:73:3d'
                            }
                        }
                    }
                }
            }
        },
        'total_entries': 4
    }

    def test_empty(self):
        self.dev1 = Mock(**self.empty_output)
        obj = ShowLldpEntry(device=self.dev1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden(self):
        self.maxDiff = None
        self.dev1 = Mock(**self.golden_output)
        obj = ShowLldpEntry(device=self.dev1)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)

    def test(self):
        self.maxDiff = None
        self.dev1 = Mock(**self.device_output)
        obj = ShowLldpEntry(device=self.dev1)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.expected_output)

    def test2(self):
        self.maxDiff = None
        self.dev1 = Mock(**self.device_output2)
        obj = ShowLldpEntry(device=self.dev1)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.expected_output2)


class TestShowLldpNeighborDetail(unittest.TestCase):
    dev = Device(name='empty')
    empty_output = {'execute.return_value': '      '}
    golden_parsed_output = {
        'interfaces': {
            'GigabitEthernet0/0/0/0': {
                'port_id': {
                    'GigabitEthernet2': {
                        'neighbors': {
                            'Ge_nie1000v.openstacklocal': {
                                'chassis_id': '001e.49ff.24f7',
                                'port_description': 'GigabitEthernet2',
                                'system_name': 'Ge_nie1000v.openstacklocal',
                                'neighbor_id': 'Ge_nie1000v.openstacklocal',
                                'system_description': 'Cisco IOS Software [Everest], Virtual XE Software (X86_64_LINUX_IOSD-UNIVERSALK9-M), Version 16.6.1, RELEASE SOFTWARE (fc2)\nTechnical Support: http://www.cisco.com/techsupport\nCopyright (c) 1986-2017 by Cisco Systems, Inc.\nCompiled Sat 22-Jul-17 05:51 by',
                                'time_remaining': 90,
                                'hold_time': 120,
                                'capabilities': {
                                    'bridge': {
                                        'system': True,
                                    },
                                    'router': {
                                        'system': True,
                                        'enabled': True,
                                    },
                                },
                                'management_address': '10.1.2.1',
                            },
                        },
                    },
                },
            },
            'GigabitEthernet0/0/0/1': {
                'port_id': {
                    'Ethernet1/2': {
                        'neighbors': {
                            'G1_n9ie': {
                                'chassis_id': '5e00.80ff.020b',
                                'port_description': 'Ethernet1/2',
                                'system_name': 'G1_n9ie',
                                'neighbor_id': 'G1_n9ie',
                                'system_description': 'Cisco Nexus Operating System (NX-OS) Software 7.0(3)I7(1)\nTAC support: http://www.cisco.com/tac\nCopyright (c) 2002-2017, Cisco Systems, Inc. All rights reserved.\n',
                                'time_remaining': 106,
                                'hold_time': 120,
                                'capabilities': {
                                    'bridge': {
                                        'system': True,
                                        'enabled': True,
                                    },
                                    'router': {
                                        'system': True,
                                        'enabled': True,
                                    },
                                },
                            },
                        },
                    },
                },
            },
        },
        'total_entries': 2,
    }

    golden_output = {'execute.return_value': '''\
        Mon Mar 19 18:24:29.512 UTC
        Capability codes:
                (R) Router, (B) Bridge, (T) Telephone, (C) DOCSIS Cable Device
                (W) WLAN Access Point, (P) Repeater, (S) Station, (O) Other

        ------------------------------------------------
        Local Interface: GigabitEthernet0/0/0/0
        Chassis id: 001e.49ff.24f7
        Port id: Gi2
        Port Description: GigabitEthernet2
        System Name: Ge_nie1000v.openstacklocal

        System Description:
        Cisco IOS Software [Everest], Virtual XE Software (X86_64_LINUX_IOSD-UNIVERSALK9-M), Version 16.6.1, RELEASE SOFTWARE (fc2)
        Technical Support: http://www.cisco.com/techsupport
        Copyright (c) 1986-2017 by Cisco Systems, Inc.
        Compiled Sat 22-Jul-17 05:51 by

        Time remaining: 90 seconds
        Hold Time: 120 seconds
        System Capabilities: B,R
        Enabled Capabilities: R
        Management Addresses:
        IPv4 address: 10.1.2.1



        ------------------------------------------------
        Local Interface: GigabitEthernet0/0/0/1
        Chassis id: 5e00.80ff.020b
        Port id: Ethernet1/2
        Port Description: Ethernet1/2
        System Name: G1_n9ie

        System Description:
        Cisco Nexus Operating System (NX-OS) Software 7.0(3)I7(1)
        TAC support: http://www.cisco.com/tac
        Copyright (c) 2002-2017, Cisco Systems, Inc. All rights reserved.

        Time remaining: 106 seconds
        Hold Time: 120 seconds
        System Capabilities: B,R
        Enabled Capabilities: B,R
        Management Addresses - not advertised


        Total entries displayed: 2
    '''}

    golden_output_2 = {'execute.return_value': '''
        Local Interface: GigabitEthernet0/0/0/8
        Chassis id: 0026.98ff.d8fb
        Port id: Gi0/0/0/8
        Port Description: GigabitEthernet0/0/0/8
        System Name: gee1a-2

        System Description: 
        Cisco IOS XR Software, Version 4.1.0.32I[Default]
        Copyright (c) 2011 by Cisco Systems, Inc.

        Time remaining: 102 seconds
        Hold Time: 120 seconds
        System Capabilities: R
        Enabled Capabilities: R
        Management Addresses:
          IPv4 address: 10.5.173.110



        ------------------------------------------------
        Local Interface: GigabitEthernet0/0/0/8
        Chassis id: 0026.98ff.d8fb
        Port id: Gi0/0/0/8.1
        Port Description: GigabitEthernet0/0/0/8.1
        System Name: gee1a-2

        System Description: 
        Cisco IOS XR Software, Version 4.1.0.32I[Default]
        Copyright (c) 2011 by Cisco Systems, Inc.

        Time remaining: 96 seconds
        Hold Time: 120 seconds
        System Capabilities: R
        Enabled Capabilities: R
        Management Addresses:
          IPv4 address: 10.5.173.110



        Total entries displayed: 2
    '''
                       }
    golden_parsed_output_2 = {
        'interfaces': {
            'GigabitEthernet0/0/0/8': {
                'port_id': {
                    'GigabitEthernet0/0/0/8': {
                        'neighbors': {
                            'gee1a-2': {
                                'chassis_id': '0026.98ff.d8fb',
                                'port_description': 'GigabitEthernet0/0/0/8',
                                'system_name': 'gee1a-2',
                                'neighbor_id': 'gee1a-2',
                                'system_description': 'Cisco IOS XR Software, Version 4.1.0.32I[Default]\nCopyright (c) 2011 by Cisco Systems, Inc.\n',
                                'time_remaining': 102,
                                'hold_time': 120,
                                'capabilities': {
                                    'router': {
                                        'system': True,
                                        'enabled': True,
                                    },
                                },
                                'management_address': '10.5.173.110',
                            },
                        },
                    },
                    'GigabitEthernet0/0/0/8.1': {
                        'neighbors': {
                            'gee1a-2': {
                                'chassis_id': '0026.98ff.d8fb',
                                'port_description': 'GigabitEthernet0/0/0/8.1',
                                'system_name': 'gee1a-2',
                                'neighbor_id': 'gee1a-2',
                                'system_description': 'Cisco IOS XR Software, Version 4.1.0.32I[Default]\nCopyright (c) 2011 by Cisco Systems, Inc.\n',
                                'time_remaining': 96,
                                'hold_time': 120,
                                'capabilities': {
                                    'router': {
                                        'system': True,
                                        'enabled': True,
                                    },
                                },
                                'management_address': '10.5.173.110',
                            },
                        },
                    },
                },
            },
        },
        'total_entries': 2,
    }

    device_output = {'execute.return_value': '''
            Capability codes:
            (R) Router, (B) Bridge, (T) Telephone, (C) DOCSIS Cable Device
            (W) WLAN Access Point, (P) Repeater, (S) Station, (O) Other

        ------------------------------------------------
        Local Interface: TenGigE0/0/0/41
        Chassis id: 00bc.60ff.7ff0
        Port id: TenGigE0/0/0/0/0
        Port Description - not advertised
        System Name: genie1-ggN1.ie-genie1

        System Description: 
         6.5.3, NCS-5500

        Time remaining: 99 seconds
        Hold Time: 120 seconds
        System Capabilities: R
        Enabled Capabilities: R
        Management Addresses:
          IPv4 address: 10.10.10.2

        Peer MAC Address: 00:bc:60:ff:7f:17


        ------------------------------------------------
        Local Interface: HundredGigE0/0/1/1
        Chassis id: 008a.96ff.2f8c
        Port id: HundredGigE0/0/0/2
        Port Description: to gen-8 nie  0/0/1/1 via gee1.dev 29-30 
        System Name: system2

        System Description: 
         7.0.1, NCS-5500

        Time remaining: 96 seconds
        Hold Time: 120 seconds
        System Capabilities: R
        Enabled Capabilities: R
        Management Addresses:
          IPv4 address: 10.10.10.10

        Peer MAC Address: 00:8a:96:ff:2b:13


        ------------------------------------------------
        Local Interface: HundredGigE0/0/1/0
        Chassis id: 008a.96ff.178c
        Port id: HundredGigE0/0/0/2
        Port Description: to gen-8 nie  0/0/1/0 via gee1.dev 31-32 
        System Name: system1

        System Description: 
         7.0.1, NCS-5500

        Time remaining: 116 seconds
        Hold Time: 120 seconds
        System Capabilities: R
        Enabled Capabilities: R
        Management Addresses:
          IPv4 address: 10.10.10.11

        Peer MAC Address: 00:8a:96:ff:13:13


        Total entries displayed: 3
    '''}

    expected_output = {
        'interfaces': {
            'HundredGigE0/0/1/0': {
                'port_id': {
                    'HundredGigE0/0/0/2': {
                        'neighbors': {
                            'system1': {
                                'capabilities': {
                                    'router': {
                                        'enabled': True,
                                        'system': True,
                                    },
                                },
                                'peer_mac': '00:8a:96:ff:13:13',
                                'chassis_id': '008a.96ff.178c',
                                'hold_time': 120,
                                'management_address': '10.10.10.11',
                                'neighbor_id': 'system1',
                                'port_description': 'to gen-8 nie  0/0/1/0 via gee1.dev 31-32',
                                'system_description': '',
                                'system_name': 'system1',
                                'time_remaining': 116,
                            },
                        },
                    },
                },
            },
            'HundredGigE0/0/1/1': {
                'port_id': {
                    'HundredGigE0/0/0/2': {
                        'neighbors': {
                            'system2': {
                                'capabilities': {
                                    'router': {
                                        'enabled': True,
                                        'system': True,
                                    },
                                },
                                'peer_mac': '00:8a:96:ff:2b:13',
                                'chassis_id': '008a.96ff.2f8c',
                                'hold_time': 120,
                                'management_address': '10.10.10.10',
                                'neighbor_id': 'system2',
                                'port_description': 'to gen-8 nie  0/0/1/1 via gee1.dev 29-30',
                                'system_description': '',
                                'system_name': 'system2',
                                'time_remaining': 96,
                            },
                        },
                    },
                },
            },
            'TenGigE0/0/0/41': {
                'port_id': {
                    'TenGigE0/0/0/0/0': {
                        'neighbors': {
                            'genie1-ggN1.ie-genie1': {
                                'capabilities': {
                                    'router': {
                                        'enabled': True,
                                        'system': True,
                                    },
                                },
                                'peer_mac': '00:bc:60:ff:7f:17',
                                'chassis_id': '00bc.60ff.7ff0',
                                'hold_time': 120,
                                'management_address': '10.10.10.2',
                                'neighbor_id': 'genie1-ggN1.ie-genie1',
                                'port_description': 'not advertised',
                                'system_description': '',
                                'system_name': 'genie1-ggN1.ie-genie1',
                                'time_remaining': 99,
                            },
                        },
                    },
                },
            },
        },
        'total_entries': 3,
    }

    golden_output_4 = {'execute.return_value': '''
        show lldp neighbors detail

        
        
        Thu Apr 30 16:14:06.186 UTC
        
        Capability codes:
        
            (R) Router, (B) Bridge, (T) Telephone, (C) DOCSIS Cable Device
        
            (W) WLAN Access Point, (P) Repeater, (S) Station, (O) Other
        
        
        
        ------------------------------------------------
        
        Local Interface: TenGigE0/0/0/1
        
        Chassis id: 0026.88ff.c416
        
        Port id: 655
        
        Port Description: PHY|BW|L3|CORE|type:CRAN-P2P|rhost:ASR-01|rport:TenGigE0/0/0/1
        
        System Name: MX480-01.comcast.net
        
        
        
        System Description:
        
        Juniper Networks, Inc. mx480 internet router, kernel JUNOS 18.4R2.7, Build date: 2019-06-27 10:00:44 UTC Copyright (c) 1996-2019 Juniper Networks, Inc.
        
        
        
        Time remaining: 98 seconds
        
        Hold Time: 120 seconds
        
        System Capabilities: B,R
        
        Enabled Capabilities: B,R
        
        Management Addresses:
        
        IPv4 address: 10.253.47.140
        
        
        
        
        
        
        
        ------------------------------------------------
        
        Local Interface: TenGigE0/2/0/1
        
        Parent Interface: Bundle-Ether10
        
        Chassis id: 444c.a8ff.39f5
        
        Port id: Ethernet1/4
        
        Port Description: PHY|BW|AGG-MEMBER|CORE|type:CRAN-P2P|rhost:ASR-01|rport:TenGigE0/2/0/1|lagg:Port-Channel10|ragg:Bundle-Ether10
        
        System Name: 7280CR2A-01.comcast.net
        
        
        
        System Description:
        
        Arista Networks EOS version 4.21.6F running on an Arista Networks DCS-7280CR-48
        
        
        
        Time remaining: 97 seconds
        
        Hold Time: 120 seconds
        
        System Capabilities: B,R
        
        Enabled Capabilities: B,R
        
        Management Addresses:
        
        IPv4 address: 10.252.26.104
        
        
        
        
        
        
        
        ------------------------------------------------
        
        Local Interface: TenGigE0/2/0/11
        
        Chassis id: 6c41.0eff.3712
        
        Port id: Te0/0/0/0
        
        Port Description: PHY|BW|L3|CORE|type:CRAN-P2P|rhost:ASR-01|rport:te0/2/0/11
        
        System Name: ASR9904.netlabs.nj.ula.comcast.net
        
        
        
        System Description:
        
        Cisco IOS XR Software, Version 6.1.4[Default]
        
        Copyright (c) 2017 by Cisco Systems, Inc., ASR9K Series
        
        
        
        Time remaining: 116 seconds
        
        Hold Time: 120 seconds
        
        System Capabilities: R
        
        Enabled Capabilities: R
        
        Management Addresses:
        
        IPv4 address: 10.253.47.122
        
        IPv6 address: 2001:db8:fbd1:8e5c::4
        
        
        
        
        
        
        
        ------------------------------------------------
        
        Local Interface: TenGigE0/2/0/23
        
        Chassis id: 7c31.0eff.203f
        
        Port id: TenGigE0/0/0/4
        
        Port Description: ASR-01 T0/2/0/23
        
        System Name: NCS5501
        
        
        
        System Description:
        
        6.5.2, NCS-5500
        
        
        
        Time remaining: 114 seconds
        
        Hold Time: 120 seconds
        
        System Capabilities: R
        
        Enabled Capabilities: R
        
        Management Addresses:
        
        IPv4 address: 10.253.47.30
        
        
        
        
        
        
        
        Total entries displayed: 4
    '''}

    golden_parsed_output_4 = {
        'interfaces': {
            'TenGigE0/0/0/1': {
                'port_id': {
                    '655': {
                        'neighbors': {
                            'MX480-01.comcast.net': {
                                'capabilities': {
                                    'bridge': {
                                        'enabled': True,
                                        'system': True,
                                    },
                                    'router': {
                                        'enabled': True,
                                        'system': True,
                                    },
                                },
                                'chassis_id': '0026.88ff.c416',
                                'hold_time': 120,
                                'management_address': '10.253.47.140',
                                'neighbor_id': 'MX480-01.comcast.net',
                                'port_description': 'PHY|BW|L3|CORE|type:CRAN-P2P|rhost:ASR-01|rport:TenGigE0/0/0/1',
                                'system_description': '',
                                'system_name': 'MX480-01.comcast.net',
                                'time_remaining': 98,
                            },
                        },
                    },
                },
            },
            'TenGigE0/2/0/1': {
                'port_id': {
                    'Ethernet1/4': {
                        'neighbors': {
                            '7280CR2A-01.comcast.net': {
                                'capabilities': {
                                    'bridge': {
                                        'enabled': True,
                                        'system': True,
                                    },
                                    'router': {
                                        'enabled': True,
                                        'system': True,
                                    },
                                },
                                'chassis_id': '444c.a8ff.39f5',
                                'hold_time': 120,
                                'management_address': '10.252.26.104',
                                'neighbor_id': '7280CR2A-01.comcast.net',
                                'port_description': 'PHY|BW|AGG-MEMBER|CORE|type:CRAN-P2P|rhost:ASR-01|rport:TenGigE0/2/0/1|lagg:Port-Channel10|ragg:Bundle-Ether10',
                                'system_description': '',
                                'system_name': '7280CR2A-01.comcast.net',
                                'time_remaining': 97,
                            },
                        },
                    },
                },
            },
            'TenGigE0/2/0/11': {
                'port_id': {
                    'TenGigabitEthernet0/0/0/0': {
                        'neighbors': {
                            'ASR9904.netlabs.nj.ula.comcast.net': {
                                'capabilities': {
                                    'router': {
                                        'enabled': True,
                                        'system': True,
                                    },
                                },
                                'chassis_id': '6c41.0eff.3712',
                                'hold_time': 120,
                                'management_address': '10.253.47.122',
                                'neighbor_id': 'ASR9904.netlabs.nj.ula.comcast.net',
                                'port_description': 'PHY|BW|L3|CORE|type:CRAN-P2P|rhost:ASR-01|rport:te0/2/0/11',
                                'system_description': 'Cisco IOS XR Software, Version 6.1.4[Default]\nCopyright (c) 2017 by Cisco Systems, Inc., ASR9K Series\n',
                                'system_name': 'ASR9904.netlabs.nj.ula.comcast.net',
                                'time_remaining': 116,
                            },
                        },
                    },
                },
            },
            'TenGigE0/2/0/23': {
                'port_id': {
                    'TenGigE0/0/0/4': {
                        'neighbors': {
                            'NCS5501': {
                                'capabilities': {
                                    'router': {
                                        'enabled': True,
                                        'system': True,
                                    },
                                },
                                'chassis_id': '7c31.0eff.203f',
                                'hold_time': 120,
                                'management_address': '10.253.47.30',
                                'neighbor_id': 'NCS5501',
                                'port_description': 'ASR-01 T0/2/0/23',
                                'system_description': '',
                                'system_name': 'NCS5501',
                                'time_remaining': 114,
                            },
                        },
                    },
                },
            },
        },
        'total_entries': 4,
    }

    golden_output_5 = {'execute.return_value': '''
        #show lldp neighbors detail TenGigE0/0/0/28/0
        Tue Oct  6 13:56:33.804 UTC
        Capability codes:
                (R) Router, (B) Bridge, (T) Telephone, (C) DOCSIS Cable Device
                (W) WLAN Access Point, (P) Repeater, (S) Station, (O) Other

        ------------------------------------------------
        Local Interface: TenGigE0/0/0/28/0
        Chassis id: 6464.9bff.6e31
        Port id: xe-0/1/2
        Port Description: port description
        System Name: switch1

        System Description:
        Juniper Networks, Inc. ex4200-48t , version 12.3R9.4 Build date: 2015-02-12 12:01:56 UTC

        Time remaining: 108 seconds
        Hold Time: 120 seconds
        System Capabilities: B,R
        Enabled Capabilities: B,R
        Management Addresses - not advertised
        Peer MAC Address: 64:64:9b:ff:6e:66


        Total entries displayed: 1
    '''}
    golden_parsed_output_5 = {
        'interfaces': {
            'TenGigE0/0/0/28/0': {
                'port_id': {
                    'xe-0/1/2': {
                        'neighbors': {
                            'switch1': {
                                'capabilities': {
                                    'bridge': {
                                        'enabled': True,
                                        'system': True,
                                    },
                                    'router': {
                                        'enabled': True,
                                        'system': True,
                                    },
                                },
                                'chassis_id': '6464.9bff.6e31',
                                'hold_time': 120,
                                'neighbor_id': 'switch1',
                                'peer_mac': '64:64:9b:ff:6e:66',
                                'port_description': 'port description',
                                'system_description': '',
                                'system_name': 'switch1',
                                'time_remaining': 108,
                            },
                        },
                    },
                },
            },
        },
        'total_entries': 1,
    }

    def test_empty(self):
        self.dev = Mock(**self.empty_output)
        obj = ShowLldpNeighborsDetail(device=self.dev)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden(self):
        self.maxDiff = None
        self.dev = Mock(**self.golden_output)
        obj = ShowLldpNeighborsDetail(device=self.dev)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)

    def test_golden_2(self):
        self.maxDiff = None
        self.dev = Mock(**self.golden_output_2)
        obj = ShowLldpNeighborsDetail(device=self.dev)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_2)

    def test_golden_3(self):
        self.maxDiff = None
        self.dev1 = Mock(**self.device_output)
        obj = ShowLldpNeighborsDetail(device=self.dev1)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.expected_output)

    def test_golden_4(self):
        self.maxDiff = None
        self.dev1 = Mock(**self.golden_output_4)
        obj = ShowLldpNeighborsDetail(device=self.dev1)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_4)

    def test_golden_5(self):
        self.maxDiff = None
        self.dev1 = Mock(**self.golden_output_5)
        obj = ShowLldpNeighborsDetail(device=self.dev1)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_5)


class test_show_lldp_traffic(unittest.TestCase):
    dev = Device(name='empty')
    empty_output = {'execute.return_value': '      '}

    golden_parsed_output = {
        "counters": {
            "frame_in": 399,
            "frame_out": 588,
            "frame_error_in": 0,
            "frame_discard": 0,
            "tlv_discard": 119,
            'tlv_unknown': 119,
            'entries_aged_out': 0
        }
    }
    golden_output = {'execute.return_value': '''\
    RP/0/RP0/CPU0:R2_xrv9000#show lldp traffic 
    Mon Mar 19 18:24:54.528 UTC

    LLDP traffic statistics:
            Total frames out: 588
            Total entries aged: 0
            Total frames in: 399
            Total frames received in error: 0
            Total frames discarded: 0
            Total TLVs discarded: 119
            Total TLVs unrecognized: 119
    '''}

    def test_empty(self):
        self.dev = Mock(**self.empty_output)
        obj = ShowLldpTraffic(device=self.dev)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden(self):
        self.dev = Mock(**self.golden_output)
        obj = ShowLldpTraffic(device=self.dev)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


class test_show_lldp_interface(unittest.TestCase):
    dev = Device(name='device')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output = {
        'interfaces': {
            'GigabitEthernet0/0/0/0': {
                'tx': 'enabled',
                'rx': 'enabled',
                'tx_state': 'idle',
                'rx_state': 'wait for frame',
            },
            'GigabitEthernet0/0/0/1': {
                'tx': 'enabled',
                'rx': 'enabled',
                'tx_state': 'idle',
                'rx_state': 'wait for frame',
            },
        }
    }

    golden_output = {'execute.return_value': '''\
    GigabitEthernet0/0/0/0:
			Tx: enabled
			Rx: enabled
			Tx state: IDLE
			Rx state: WAIT FOR FRAME


    GigabitEthernet0/0/0/1:
			Tx: enabled
			Rx: enabled
			Tx state: IDLE
			Rx state: WAIT FOR FRAME
    '''}

    def test_empty(self):
        self.dev = Mock(**self.empty_output)
        obj = ShowLldpInterface(device=self.dev)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden(self):
        self.dev = Mock(**self.golden_output)
        obj = ShowLldpInterface(device=self.dev)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


if __name__ == '__main__':
    unittest.main()