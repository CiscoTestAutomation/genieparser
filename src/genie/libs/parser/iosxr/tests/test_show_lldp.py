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
        self.assertEqual(parsed_output,self.golden_parsed_output)

class test_show_lldp_entry(unittest.TestCase):
    dev1 = Device(name='empty')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output = {
        'interfaces': {
            'GigabitEthernet0/0/0/0': {
                'port_id': {
                    'GigabitEthernet2': {
                        'neighbors': {
                            'R1_csr1000v.openstacklocal': {
                                'chassis_id': '001e.49f7.2c00',
                                'port_description': 'GigabitEthernet2',
                                'system_name': 'R1_csr1000v.openstacklocal',
                                'neighbor_id': 'R1_csr1000v.openstacklocal',
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
                            'R3_n9kv': {
                                'chassis_id': '5e00.8002.0009',
                                'port_description': 'Ethernet1/2',
                                'system_name': 'R3_n9kv',
                                'neighbor_id': 'R3_n9kv',
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
        System Name: R1_csr1000v.openstacklocal

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
        System Name: R3_n9kv

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
        System Name: tor1-55A1.qa-site1
        
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
        Port Description: to tor-3 hun 0/0/1/1 via novi2.dev 29-30 
        System Name: spine2-tatooine.net.bell.ca
        
        System Description: 
         7.0.1, NCS-5500
        
        Time remaining: 97 seconds
        Hold Time: 120 seconds
        System Capabilities: R
        Enabled Capabilities: R
        Management Addresses:
          IPv4 address: 172.18.0.7
        
        Peer MAC Address: 00:8a:96:0b:20:08
        
        
        ------------------------------------------------
        Local Interface: HundredGigE0/0/1/0
        Chassis id: 008a.960b.0c81
        Port id: HundredGigE0/0/0/2
        Port Description: to tor-3 hun 0/0/1/0 via novi2.dev 31-32 
        System Name: spine1-tatooine.net.bell.ca
        
        System Description: 
         7.0.1, NCS-5500
        
        Time remaining: 117 seconds
        Hold Time: 120 seconds
        System Capabilities: R
        Enabled Capabilities: R
        Management Addresses:
          IPv4 address: 172.18.0.5
        
        Peer MAC Address: 00:8a:96:0b:08:08
        
        
        Total entries displayed: 3
    '''}

    expected_output = {
        'interfaces': {
            'HundredGigE0/0/1/0': {
                'port_id': {
                    'HundredGigE0/0/0/2': {
                        'neighbors': {
                            'spine1-tatooine.net.bell.ca': {
                                'capabilities': {
                                    'router': {
                                        'enabled': True,
                                        'system': True,
                                    },
                                },
                                'chassis_id': '008a.960b.0c81',
                                'hold_time': 120,
                                'management_address': '172.18.0.5',
                                'neighbor_id': 'spine1-tatooine.net.bell.ca',
                                'port_description': 'to tor-3 hun 0/0/1/0 via novi2.dev 31-32',
                                'system_description': '',
                                'system_name': 'spine1-tatooine.net.bell.ca',
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
                            'spine2-tatooine.net.bell.ca': {
                                'capabilities': {
                                    'router': {
                                        'enabled': True,
                                        'system': True,
                                    },
                                },
                                'chassis_id': '008a.960b.2481',
                                'hold_time': 120,
                                'management_address': '172.18.0.7',
                                'neighbor_id': 'spine2-tatooine.net.bell.ca',
                                'port_description': 'to tor-3 hun 0/0/1/1 via novi2.dev 29-30',
                                'system_description': '',
                                'system_name': 'spine2-tatooine.net.bell.ca',
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
                            'tor1-55A1.qa-site1': {
                                'capabilities': {
                                    'router': {
                                        'enabled': True,
                                        'system': True,
                                    },
                                },
                                'chassis_id': '00bc.6017.68d9',
                                'hold_time': 120,
                                'management_address': '10.10.10.2',
                                'neighbor_id': 'tor1-55A1.qa-site1',
                                'port_description': 'not advertised',
                                'system_description': '',
                                'system_name': 'tor1-55A1.qa-site1',
                                'time_remaining': 100,
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
        self.assertEqual(parsed_output,self.golden_parsed_output)

    def test(self):
        self.maxDiff = None
        self.dev1 = Mock(**self.device_output)
        obj = ShowLldpEntry(device=self.dev1)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.expected_output)

class test_show_lldp_neighbor_detail(unittest.TestCase):
    dev = Device(name='empty')
    empty_output = {'execute.return_value': '      '}
    golden_parsed_output = {
        'interfaces': {
            'GigabitEthernet0/0/0/0': {
                'port_id': {
                    'GigabitEthernet2': {
                        'neighbors': {
                            'R1_csr1000v.openstacklocal': {
                                'chassis_id': '001e.49f7.2c00',
                                'port_description': 'GigabitEthernet2',
                                'system_name': 'R1_csr1000v.openstacklocal',
                                'neighbor_id': 'R1_csr1000v.openstacklocal',
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
                            'R3_n9kv': {
                                'chassis_id': '5e00.8002.0009',
                                'port_description': 'Ethernet1/2',
                                'system_name': 'R3_n9kv',
                                'neighbor_id': 'R3_n9kv',
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
    System Name: R1_csr1000v.openstacklocal

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
    System Name: R3_n9kv

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
        System Name: asr9k-5

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
        System Name: asr9k-5

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
                            'asr9k-5': {
                                'chassis_id': '0026.9815.c3e6',
                                'port_description': 'GigabitEthernet0/0/0/8',
                                'system_name': 'asr9k-5',
                                'neighbor_id': 'asr9k-5',
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
                            'asr9k-5': {
                                'chassis_id': '0026.9815.c3e6',
                                'port_description': 'GigabitEthernet0/0/0/8.1',
                                'system_name': 'asr9k-5',
                                'neighbor_id': 'asr9k-5',
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
        System Name: tor1-55A1.qa-site1
        
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
        Port Description: to tor-3 hun 0/0/1/1 via novi2.dev 29-30 
        System Name: spine2-tatooine.net.bell.ca
        
        System Description: 
         7.0.1, NCS-5500
        
        Time remaining: 96 seconds
        Hold Time: 120 seconds
        System Capabilities: R
        Enabled Capabilities: R
        Management Addresses:
          IPv4 address: 172.18.0.7
        
        Peer MAC Address: 00:8a:96:0b:20:08
        
        
        ------------------------------------------------
        Local Interface: HundredGigE0/0/1/0
        Chassis id: 008a.960b.0c81
        Port id: HundredGigE0/0/0/2
        Port Description: to tor-3 hun 0/0/1/0 via novi2.dev 31-32 
        System Name: spine1-tatooine.net.bell.ca
        
        System Description: 
         7.0.1, NCS-5500
        
        Time remaining: 116 seconds
        Hold Time: 120 seconds
        System Capabilities: R
        Enabled Capabilities: R
        Management Addresses:
          IPv4 address: 172.18.0.5
        
        Peer MAC Address: 00:8a:96:0b:08:08
        
        
        Total entries displayed: 3
    '''}

    expected_output = {
        'interfaces': {
            'HundredGigE0/0/1/0': {
                'port_id': {
                    'HundredGigE0/0/0/2': {
                        'neighbors': {
                            'spine1-tatooine.net.bell.ca': {
                                'capabilities': {
                                    'router': {
                                        'enabled': True,
                                        'system': True,
                                    },
                                },
                                'chassis_id': '008a.960b.0c81',
                                'hold_time': 120,
                                'management_address': '172.18.0.5',
                                'neighbor_id': 'spine1-tatooine.net.bell.ca',
                                'port_description': 'to tor-3 hun 0/0/1/0 via novi2.dev 31-32',
                                'system_description': '',
                                'system_name': 'spine1-tatooine.net.bell.ca',
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
                            'spine2-tatooine.net.bell.ca': {
                                'capabilities': {
                                    'router': {
                                        'enabled': True,
                                        'system': True,
                                    },
                                },
                                'chassis_id': '008a.960b.2481',
                                'hold_time': 120,
                                'management_address': '172.18.0.7',
                                'neighbor_id': 'spine2-tatooine.net.bell.ca',
                                'port_description': 'to tor-3 hun 0/0/1/1 via novi2.dev 29-30',
                                'system_description': '',
                                'system_name': 'spine2-tatooine.net.bell.ca',
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
                            'tor1-55A1.qa-site1': {
                                'capabilities': {
                                    'router': {
                                        'enabled': True,
                                        'system': True,
                                    },
                                },
                                'chassis_id': '00bc.6017.68d9',
                                'hold_time': 120,
                                'management_address': '10.10.10.2',
                                'neighbor_id': 'tor1-55A1.qa-site1',
                                'port_description': 'not advertised',
                                'system_description': '',
                                'system_name': 'tor1-55A1.qa-site1',
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
        self.assertEqual(parsed_output,self.golden_parsed_output)

    def test_golden_2(self):
        self.maxDiff = None
        self.dev = Mock(**self.golden_output_2)
        obj = ShowLldpNeighborsDetail(device=self.dev)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output_2)

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
        self.assertEqual(parsed_output,self.golden_parsed_output)

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
        self.assertEqual(parsed_output,self.golden_parsed_output)

if __name__ == '__main__':
    unittest.main()