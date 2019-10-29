# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

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
                                'chassis_id': '001e.49f7.2c00',
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
                                'chassis_id': '5e00.8002.0009',
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
        Chassis id: 001e.49f7.2c00
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
        Chassis id: 5e00.8002.0009
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
        Chassis id: 00bc.6017.68d9
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

        Peer MAC Address: 00:bc:60:17:68:00


        ------------------------------------------------
        Local Interface: HundredGigE0/0/1/1
        Chassis id: 008a.960b.2481
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

        Peer MAC Address: 00:8a:96:0b:20:08


        ------------------------------------------------
        Local Interface: HundredGigE0/0/1/0
        Chassis id: 008a.960b.0c81
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

        Peer MAC Address: 00:8a:96:0b:08:08


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
                                'chassis_id': '008a.960b.0c81',
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
                                'chassis_id': '008a.960b.2481',
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
                                'chassis_id': '00bc.6017.68d9',
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
    Chassis id: ccd8.c1cb.7d11
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

    Peer MAC Address: cc:d8:c1:cb:7d:14

        Local Interface: TenGigE0/5/0/5
    Chassis id: c471.fec3.ac00
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

    Peer MAC Address: c4:71:fe:c3:af:79

        Local Interface: TenGigE0/5/0/6
    Chassis id: 8426.2bbc.2c9d
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

    Peer MAC Address: a0:f3:e4:c6:52:0e

    Total entries displayed: 3
    '''}
    expected_output2 = {
        'interfaces': {
            'TenGigE0/1/0/0': {
                'port_id': {
                    'Bundle-Ether2': {
                        'neighbors': {
                            'geni5-genie': {
                                'capabilities': {
                                    'router': {
                                        'enabled': True,
                                        'system': True,
                                    },
                                },
                                'chassis_id': 'ccd8.c1cb.7d11',
                                'hold_time': 120,
                                'management_address': '10.10.10.12',
                                'neighbor_id': 'geni5-genie',
                                'port_description': '10G to ge1-genie port Ge1/1/1/1:GG1',
                                'system_description': 'Cisco IOS XR Software, Version 6.5.3[Default]\nCopyright (c) 2019 by Cisco Systems, Inc., ASR9K Series\n',
                                'system_name': 'geni5-genie',
                                'time_remaining': 99,
                            },
                        },
                    },
                },
            },
            'TenGigE0/5/0/5': {
                'port_id': {
                    'TenGigabitEthernet0/1/0/3': {
                        'neighbors': {
                            'system3': {
                                'capabilities': {
                                    'router': {
                                        'enabled': True,
                                        'system': True,
                                    },
                                },
                                'chassis_id': 'c471.fec3.ac00',
                                'hold_time': 120,
                                'management_address': '10.10.10.13',
                                'neighbor_id': 'system3',
                                'port_description': '10G link to genie1-genie port TEN 0/5/0/5 in BE 43 (with port 0/4/0/3)',
                                'system_description': 'Cisco IOS XR Software, Version 6.4.2[Default]\nCopyright (c) 2019 by Cisco Systems, Inc., CRS\n',
                                'system_name': 'system3',
                                'time_remaining': 108,
                            },
                        },
                    },
                },
            },
            'TenGigE0/5/0/6': {
                'port_id': {
                    '1611153480': {
                        'neighbors': {
                            'GENIE02GEN2': {
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
                                'chassis_id': '8426.2bbc.2c9d',
                                'hold_time': 121,
                                'management_address': '10.10.10.14',
                                'neighbor_id': 'GENIE02GEN2',
                                'port_description': '2/1/9, 10-Gig Ethernet, "10G interface to genie1-genie port 0/5/0/6-DO NOT SHUT or REMOVE..Mitch"',
                                'system_description': '',
                                'system_name': 'GENIE02GEN2',
                                'time_remaining': 105,
                            },
                        },
                    },
                },
            },
        },
        'total_entries': 3,
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
                                'chassis_id': '001e.49f7.2c00',
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
                                'chassis_id': '5e00.8002.0009',
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
    Chassis id: 001e.49f7.2c00
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
    Chassis id: 5e00.8002.0009
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
        Chassis id: 0026.9815.c3e6
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
        Chassis id: 0026.9815.c3e6
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
                                'chassis_id': '0026.9815.c3e6',
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
                                'chassis_id': '0026.9815.c3e6',
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
        Chassis id: 00bc.6017.68d9
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

        Peer MAC Address: 00:bc:60:17:68:00


        ------------------------------------------------
        Local Interface: HundredGigE0/0/1/1
        Chassis id: 008a.960b.2481
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

        Peer MAC Address: 00:8a:96:0b:20:08


        ------------------------------------------------
        Local Interface: HundredGigE0/0/1/0
        Chassis id: 008a.960b.0c81
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

        Peer MAC Address: 00:8a:96:0b:08:08


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
                                'chassis_id': '008a.960b.0c81',
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
                                'chassis_id': '008a.960b.2481',
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
                                'chassis_id': '00bc.6017.68d9',
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

    def test(self):
        self.maxDiff = None
        self.dev1 = Mock(**self.device_output)
        obj = ShowLldpNeighborsDetail(device=self.dev1)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.expected_output)


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