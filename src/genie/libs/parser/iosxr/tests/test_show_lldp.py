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
                'neighbors': {
                    'R1_csr1000v.openstacklocal': {
                        'chassis_id': '001e.49f7.2c00',
                        'port_id': 'GigabitEthernet2',
                        'port_description': 'GigabitEthernet2',
                        'system_name': 'R1_csr1000v.openstacklocal',
                        'system_description': 'Cisco IOS Software [Everest], Virtual XE Software (X86_64_LINUX_IOSD-UNIVERSALK9-M), Version 16.6.1, RELEASE SOFTWARE (fc2)\nTechnical Support: http://www.cisco.com/techsupport\nCopyright (c) 1986-2017 by Cisco Systems, Inc.\nCompiled Sat 22-Jul-17 05:51 by',
                        'time_remaining': 117,
                        'neighbor_id': 'R1_csr1000v.openstacklocal',
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
            'GigabitEthernet0/0/0/1': {
                'neighbors': {
                    'R3_n9kv': {
                        'chassis_id': '5e00.8002.0009',
                        'port_id': 'Ethernet1/2',
                        'port_description': 'Ethernet1/2',
                        'system_name': 'R3_n9kv',
                        'system_description': 'Cisco Nexus Operating System (NX-OS) Software 7.0(3)I7(1)\nTAC support: http://www.cisco.com/tac\nCopyright (c) 2002-2017, Cisco Systems, Inc. All rights reserved.\n',
                        'time_remaining': 103,
                        'neighbor_id': 'R3_n9kv',
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

class test_show_lldp_neighbor_detail(unittest.TestCase):
    dev = Device(name='empty')
    empty_output = {'execute.return_value': '      '}
    golden_parsed_output = {
        'interfaces': {
            'GigabitEthernet0/0/0/0': {
                'neighbors': {
                    'R1_csr1000v.openstacklocal': {
                        'chassis_id': '001e.49f7.2c00',
                        'port_id': 'GigabitEthernet2',
                        'port_description': 'GigabitEthernet2',
                        'system_name': 'R1_csr1000v.openstacklocal',
                        'system_description': 'Cisco IOS Software [Everest], Virtual XE Software (X86_64_LINUX_IOSD-UNIVERSALK9-M), Version 16.6.1, RELEASE SOFTWARE (fc2)\nTechnical Support: http://www.cisco.com/techsupport\nCopyright (c) 1986-2017 by Cisco Systems, Inc.\nCompiled Sat 22-Jul-17 05:51 by',
                        'time_remaining': 90,
                        'neighbor_id': 'R1_csr1000v.openstacklocal',
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
            'GigabitEthernet0/0/0/1': {
                'neighbors': {
                    'R3_n9kv': {
                        'chassis_id': '5e00.8002.0009',
                        'port_id': 'Ethernet1/2',
                        'port_description': 'Ethernet1/2',
                        'system_name': 'R3_n9kv',
                        'system_description': 'Cisco Nexus Operating System (NX-OS) Software 7.0(3)I7(1)\nTAC support: http://www.cisco.com/tac\nCopyright (c) 2002-2017, Cisco Systems, Inc. All rights reserved.\n',
                        'time_remaining': 106,
                        'neighbor_id': 'R3_n9kv',
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