# Python
import unittest
from unittest.mock import Mock

# ATS
from pyats.topology import Device
from pyats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError, \
    SchemaMissingKeyError

# iosxe show_lisp
from genie.libs.parser.nxos.show_lldp import ShowLldpAll, ShowLldpTimers, \
    ShowLldpTlvSelect, ShowLldpNeighborsDetail, ShowLldpTraffic

# =================================
# Unit test for 'show lldp all'
# =================================
class TestShowLldpAll(unittest.TestCase):
    '''unit test for "show lldp all'''
    device = Device(name='aDevice')

    empty_output = {'execute.return_value': ''}

    golden_parsed_output = {
        'interfaces': {
            'Ethernet1/64':
                {'enabled': True,
                 'tx': True,
                 'rx': True,
                 'dcbx': True
                 },
            'mgmt0':
                {'enabled': True,
                 'tx': True,
                 'rx': True,
                 'dcbx': False
                 }
        }
    }

    golden_output = {'execute.return_value': '''
    Interface Information: Eth1/64 Enable (tx/rx/dcbx): Y/Y/Y
    Interface Information: mgmt0 Enable (tx/rx/dcbx): Y/Y/N
    '''
                     }

    def test_empty(self):
        self.maxDiff = None
        self.device = Mock(**self.empty_output)
        obj = ShowLldpAll(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output)
        obj = ShowLldpAll(device=self.device)
        parsed_output = obj.parse()

        self.assertEqual(parsed_output, self.golden_parsed_output)


# =================================
# Unit test for 'show lldp timers'
# =================================
class TestShowLldpTimers(unittest.TestCase):
    '''unit test for show lldp timers'''
    empty_output = {'execute.return_value': ''}
    golden_parsed_output = {
        'hold_timer': 120,
        'reinit_timer': 2,
        'hello_timer': 30
    }
    golden_output = {'execute.return_value':
                         '''
                         LLDP Timers:

                             Holdtime in seconds: 120
                             Reinit-time in seconds: 2
                             Transmit interval in seconds: 30
                         '''
                     }

    golden_output_1 = {'execute.return_value': '''
        show lldp timers

        LLDP Timers:

            Holdtime in seconds: 120
            Reinit-time in seconds: 2
            Transmit interval in seconds: 30
            Transmit delay in seconds: 2
            Hold multiplier in seconds: 4
            Notification interval in seconds: 5
    '''
    }

    golden_parsed_output_1 = {
        'hello_timer': 30,
        'hold_multiplier': 4,
        'hold_timer': 120,
        'notification_interval': 5,
        'reinit_timer': 2,
        'transmit_delay': 2
    }

    def test_empty(self):
        self.maxDiff = None
        self.device = Mock(**self.empty_output)
        obj = ShowLldpTimers(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output)
        obj = ShowLldpTimers(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)

    def test_golden_1(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_1)
        obj = ShowLldpTimers(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_1)

# =================================
# Unit test for 'show lldp tlv-select'
# =================================
class TestShowLldpTlvSelect(unittest.TestCase):
    '''unit test for show lldp tlv-select'''
    empty_output = {'execute.return_value': ''}
    golden_parsed_output = {
        'suppress_tlv_advertisement': {
            'port_description': False,
            'system_name': False,
            'system_description': False,
            'system_capabilities': False,
            'management_address_v4': False,
            'management_address_v6': False,
            'power_management': False,
            'port_vlan': False,
            'dcbxp': False
        }
    }
    golden_output = {'execute.return_value': '''
           management-address-v4
           management-address-v6
           port-description
           port-vlan
           power-management
           system-capabilities
           system-description
           system-name
           dcbxp
        '''}

    def test_empty(self):
        self.maxDiff = None
        self.device = Mock(**self.empty_output)
        obj = ShowLldpTlvSelect(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output)
        obj = ShowLldpTlvSelect(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


# =================================
# Unit test for 'show lldp neighbors detail'
# =================================
class TestShowLldpNeighborsDetail(unittest.TestCase):
    '''unit test for show lldp neighbors detail'''
    empty_output = {'execute.return_value': ''}

    golden_parsed_output = {
        'total_entries': 2,
        'interfaces': {
            'Ethernet1/1': {
                'port_id': {
                    'GigabitEthernet3': {
                        'neighbors': {
                            'R1_csr1000v.openstacklocal': {
                                'chassis_id': '001e.49ff.24f7',
                                'port_description': 'GigabitEthernet3',
                                'system_name': 'R1_csr1000v.openstacklocal',
                                'system_description': 'Cisco IOS Software [Everest], '
                                                      'Virtual XE Software ('
                                                      'X86_64_LINUX_IOSD-UNIVERSALK9-M), Version 16.6.1, RELEASE SOFTWARE (fc2)\nTechnical Support: http://www.cisco.com/techsupport\nCopyright (c) 1986-2017 by Cisco Systems, Inc.\nCompiled Sat 22-Jul-17 05:51 by',
                                'time_remaining': 114,
                                'capabilities': {
                                    'bridge': {
                                        'name': 'bridge',
                                        'system': True,
                                    },
                                    'router': {
                                        'name': 'router',
                                        'system': True,
                                        'enabled': True
                                    }
                                },
                                'management_address_v4': '10.1.3.1',
                                'management_address_v6': 'not advertised',
                                'vlan_id': 'not advertised'
                            }
                        }
                    }
                }
            },
            'Ethernet1/2': {
                'port_id': {
                    'GigabitEthernet0/0/0/1': {
                        'neighbors': {
                            'R2_xrv9000': {
                                'chassis_id': '000d.bdff.4f04',
                                'system_name': 'R2_xrv9000',
                                'system_description': '6.2.2, IOS-XRv 9000',
                                'time_remaining': 95,
                                'capabilities': {
                                    'router': {
                                        'name': 'router',
                                        'system': True,
                                        'enabled': True
                                    }
                                },
                                'management_address_v4': '10.2.3.2',
                                'management_address_v6': 'not advertised',
                                'vlan_id': 'not advertised'
                            }
                        }
                    }
                }
            }
        }
    }
    golden_output = {'execute.return_value': '''
            Capability codes:
              (R) Router, (B) Bridge, (T) Telephone, (C) DOCSIS Cable Device
              (W) WLAN Access Point, (P) Repeater, (S) Station, (O) Other
            Device ID            Local Intf      Hold-time  Capability  Port ID  

            Chassis id: 001e.49ff.24f7
            Port id: Gi3
            Local Port id: Eth1/1
            Port Description: GigabitEthernet3
            System Name: R1_csr1000v.openstacklocal
            System Description: Cisco IOS Software [Everest], Virtual XE Software (X86_64_LINUX_IOSD-UNIVERSALK9-M), Version 16.6.1, RELEASE SOFTWARE (fc2)
            Technical Support: http://www.cisco.com/techsupport
            Copyright (c) 1986-2017 by Cisco Systems, Inc.
            Compiled Sat 22-Jul-17 05:51 by 
            Time remaining: 114 seconds
            System Capabilities: B, R
            Enabled Capabilities: R
            Management Address: 10.1.3.1
            Management Address IPV6: not advertised
            Vlan ID: not advertised


            Chassis id: 000d.bdff.4f04
            Port id: Gi0/0/0/1
            Local Port id: Eth1/2
            Port Description: null
            System Name: R2_xrv9000
            System Description: 6.2.2, IOS-XRv 9000
            Time remaining: 95 seconds
            System Capabilities: R
            Enabled Capabilities: R
            Management Address: 10.2.3.2
            Management Address IPV6: not advertised
            Vlan ID: not advertised

            Total entries displayed: 2
        '''}

    golden_output_customer = {'execute.return_value': '''
        show lldp neighbors detail

        Capability codes:
        (R) Router, (B) Bridge, (T) Telephone, (C) DOCSIS Cable Device
        (W) WLAN Access Point, (P) Repeater, (S) Station, (O) Other
        Device ID            Local Intf      Hold-time  Capability  Port ID  

        Chassis id: 3935-5A43-4A37-39373638-35303036574C
        Port id: PCI-E Slot 1, Port 2
        Local Port id: Eth1/14
        Port Description: ConnectX-4 Lx, 25G/10G/1G SFP
        System Name: null
        System Description: ProLiant DL360 Gen10
        Time remaining: 40 seconds
        System Capabilities: not advertised
        Enabled Capabilities: not advertised
        Management Address: 98f2.b3ff.07f4
        Management Address IPV6: not advertised
        Vlan ID: not advertised


        Chassis id: e0cb.bcff.4290
        Port id: 0
        Local Port id: Eth1/38
        Port Description: internet port 0
        System Name: VPN-1
        System Description: Meraki MX450 Cloud Managed Security Appliance
        Time remaining: 101 seconds
        System Capabilities: R
        Enabled Capabilities: R
        Management Address: not advertised
        Management Address IPV6: not advertised
        Vlan ID: not advertised


        Chassis id: e0cb.bcff.7bab
        Port id: 1
        Local Port id: Eth1/40
        Port Description: internet port 1
        System Name: MX-L0
        System Description: Meraki MX450 Cloud Managed Security Appliance
        Time remaining: 90 seconds
        System Capabilities: R
        Enabled Capabilities: R
        Management Address: not advertised
        Management Address IPV6: not advertised
        Vlan ID: not advertised


        Chassis id: 7018.a7ff.7d64
        Port id: Te2/0/2
        Local Port id: Eth1/42
        Port Description: - NX1-2 (Eth1/43) -
        System Name: CAT2960-CED1
        System Description: Cisco IOS Software, C2960X Software (C2960X-UNIVERSALK9-M), Version 15.2(4)E7, RELEASE SOFTWARE (fc2)
        Technical Support: http://www.cisco.com/techsupport
        Copyright (c) 1986-2018 by Cisco Systems, Inc.
        Compiled Tue 18-Sep-18 13:07 by prod_rel_team
        Time remaining: 93 seconds
        System Capabilities: B, R
        Enabled Capabilities: B
        Management Address: 10.22.134.6
        Management Address IPV6: not advertised
        Vlan ID: 1


        Chassis id: 7018.a7ff.7d64
        Port id: Te1/0/1
        Local Port id: Eth1/43
        Port Description: - NX1-1 (Eth1/42) -
        System Name: RCAT2960
        System Description: Cisco IOS Software, C2960X Software (C2960X-UNIVERSALK9-M), Version 15.2(4)E7, RELEASE SOFTWARE (fc2)
        Technical Support: http://www.cisco.com/techsupport
        Copyright (c) 1986-2018 by Cisco Systems, Inc.
        Compiled Tue 18-Sep-18 13:07 by prod_rel_team
        Time remaining: 109 seconds
        System Capabilities: B, R
        Enabled Capabilities: B
        Management Address: 10.22.134.6
        Management Address IPV6: not advertised
        Vlan ID: not advertised


        Chassis id: 70ea.1aff.b6f6
        Port id: Ethernet1/46
        Local Port id: Eth1/46
        Port Description: - NX1-1 (eth1/46) - vPC Peer Keepalive link
        System Name: NX1-2
        System Description: Cisco Nexus Operating System (NX-OS) Software 9.2(3)
        TAC support: http://www.cisco.com/tac
        Copyright (c) 2002-2019, Cisco Systems, Inc. All rights reserved.
        Time remaining: 116 seconds
        System Capabilities: B, R
        Enabled Capabilities: B, R
        Management Address: 70ea.1aff.b6f6
        Management Address IPV6: not advertised
        Vlan ID: not advertised


        Chassis id: 70ea.1aff.854d
        Port id: Ethernet1/54
        Local Port id: Eth1/54
        Port Description: - NX1 -
        System Name: NX2-2
        System Description: Cisco Nexus Operating System (NX-OS) Software 9.2(3)
        TAC support: http://www.cisco.com/tac
        Copyright (c) 2002-2019, Cisco Systems, Inc. All rights reserved.
        Time remaining: 116 seconds
        System Capabilities: B, R
        Enabled Capabilities: B, R
        Management Address: 70ea.1aff.854d
        Management Address IPV6: not advertised
        Vlan ID: 1

        Total entries displayed: 22
    
    '''
    }

    golden_parsed_output_customer = {
        'interfaces': {
                'Ethernet1/14': {
                    'port_id': {
                        'PCI-ESlot1,Port2': {
                            'neighbors': {
                                'null': {
                                    'chassis_id': '3935-5A43-4A37-39373638-35303036574C',
                                    'enabled_capabilities': 'not advertised',
                                    'management_address_v4': '98f2.b3ff.07f4',
                                    'management_address_v6': 'not advertised',
                                    'port_description': 'ConnectX-4 Lx, 25G/10G/1G SFP',
                                    'system_capabilities': 'not advertised',
                                    'system_description': 'ProLiant DL360 Gen10',
                                    'system_name': 'null',
                                    'time_remaining': 40,
                                    'vlan_id': 'not advertised'
                                }
                            }
                        }
                    }
                },
                'Ethernet1/38': {
                    'port_id': {
                        '0': {
                            'neighbors': {
                                'VPN-1': {
                                    'capabilities': {
                                        'router': {
                                            'enabled': True,
                                            'name': 'router',
                                            'system': True
                                        }
                                    },
                                    'chassis_id': 'e0cb.bcff.4290',
                                    'management_address_v4': 'not advertised',
                                    'management_address_v6': 'not advertised',
                                    'port_description': 'internet port 0',
                                    'system_description': 'Meraki MX450 '
                                    'Cloud Managed Security Appliance',
                                    'system_name': 'VPN-1',
                                    'time_remaining': 101,
                                    'vlan_id': 'not advertised'
                                }
                            }
                        }
                    }
                },
                'Ethernet1/40': {
                    'port_id': {
                        '1': {
                            'neighbors': {
                                'MX-L0': {
                                    'capabilities': {
                                        'router': {
                                            'enabled': True,
                                            'name': 'router',
                                            'system': True
                                        }
                                    },
                                    'chassis_id': 'e0cb.bcff.7bab',
                                    'management_address_v4': 'not advertised',
                                    'management_address_v6': 'not advertised',
                                    'port_description': 'internet port 1',
                                    'system_description': 'Meraki MX450 Cloud '
                                    'Managed Security Appliance',
                                    'system_name': 'MX-L0',
                                    'time_remaining': 90,
                                    'vlan_id': 'not advertised'
                                }
                            }
                        }
                    }
                },
                'Ethernet1/42': {
                    'port_id': {
                        'TenGigabitEthernet2/0/2': {
                            'neighbors': {
                                'CAT2960-CED1': {
                                    'capabilities': {
                                        'bridge': {
                                            'enabled': True,
                                            'name': 'bridge',
                                            'system': True
                                        },
                                        'router': {
                                            'name': 'router',
                                            'system': True
                                        }
                                    },
                                    'chassis_id': '7018.a7ff.7d64',
                                    'management_address_v4': '10.22.134.6',
                                    'management_address_v6': 'not advertised',
                                    'port_description': '- NX1-2 (Eth1/43) -',
                                    'system_description': 'Cisco IOS Software, '
                                    'C2960X Software (C2960X-UNIVERSALK9-M), '
                                    'Version 15.2(4)E7, RELEASE SOFTWARE '
                                    '(fc2)\n'
                                    'Technical Support: '
                                    'http://www.cisco.com/techsupport\n'
                                    'Copyright (c) 1986-2018 by Cisco '
                                    'Systems, Inc.\n'
                                    'Compiled Tue 18-Sep-18 13:07 by '
                                    'prod_rel_team',
                                    'system_name': 'CAT2960-CED1',
                                    'time_remaining': 93,
                                    'vlan_id': '1'
                                }
                            }
                        }
                    }
                },
                'Ethernet1/43': {
                    'port_id': {
                        'TenGigabitEthernet1/0/1': {
                            'neighbors': {
                                'RCAT2960': {
                                    'capabilities': {
                                        'bridge': {
                                            'enabled': True,
                                            'name': 'bridge',
                                            'system': True
                                        },
                                        'router': {
                                            'name': 'router',
                                            'system': True
                                        }
                                    },
                                    'chassis_id': '7018.a7ff.7d64',
                                    'management_address_v4': '10.22.134.6',
                                    'management_address_v6': 'not advertised',
                                    'port_description': '- NX1-1 (Eth1/42) -',
                                    'system_description': 'Cisco IOS Software, '
                                    'C2960X Software (C2960X-UNIVERSALK9-M), '
                                    'Version 15.2(4)E7, RELEASE SOFTWARE '
                                    '(fc2)\n'
                                    'Technical Support: '
                                    'http://www.cisco.com/techsupport\n'
                                    'Copyright (c) 1986-2018 by Cisco Systems, '
                                    'Inc.\n'
                                    'Compiled Tue 18-Sep-18 13:07 by prod_rel_team',
                                    'system_name': 'RCAT2960',
                                    'time_remaining': 109,
                                    'vlan_id': 'not advertised'
                                }
                            }
                        }
                    }
                },
                'Ethernet1/46': {
                    'port_id': {
                        'Ethernet1/46': {
                            'neighbors': {
                                'NX1-2': {
                                    'capabilities': {
                                        'bridge': {
                                            'enabled': True,
                                            'name': 'bridge',
                                            'system': True
                                        },
                                        'router': {
                                            'enabled': True,
                                            'name': 'router',
                                            'system': True
                                        }
                                    },
                                    'chassis_id': '70ea.1aff.b6f6',
                                    'management_address_v4': '70ea.1aff.b6f6',
                                    'management_address_v6': 'not advertised',
                                    'port_description': '- NX1-1 (eth1/46) - '
                                    'vPC Peer Keepalive link',
                                    'system_description': 'Cisco Nexus Operating '
                                    'System (NX-OS) Software 9.2(3)\n'
                                    'TAC support: '
                                    'http://www.cisco.com/tac\n'
                                    'Copyright (c) 2002-2019, Cisco Systems, '
                                    'Inc. All rights reserved.\n',
                                    'system_name': 'NX1-2',
                                    'time_remaining': 116,
                                    'vlan_id': 'not advertised'
                                }
                            }
                        }
                    }
                },
                'Ethernet1/54': {
                    'port_id': {
                        'Ethernet1/54': {
                            'neighbors': {
                                'NX2-2': {
                                    'capabilities': {
                                        'bridge': {
                                            'enabled': True,
                                            'name': 'bridge',
                                            'system': True
                                        },
                                        'router': {
                                            'enabled': True,
                                            'name': 'router',
                                            'system': True
                                        }
                                    },
                                    'chassis_id': '70ea.1aff.854d',
                                    'management_address_v4': '70ea.1aff.854d',
                                    'management_address_v6': 'not advertised',
                                    'port_description': '- NX1 -',
                                    'system_description': 'Cisco Nexus Operating '
                                    'System (NX-OS) Software 9.2(3)\n'
                                    'TAC support: '
                                    'http://www.cisco.com/tac\n'
                                    'Copyright (c) 2002-2019, '
                                    'Cisco Systems, Inc. '
                                    'All rights reserved.\n',
                                    'system_name': 'NX2-2',
                                    'time_remaining': 116,
                                    'vlan_id': '1'
                                }
                            }
                        }
                    }
                }
            },
            'total_entries': 22
        }

    device_output_1 = {'execute.return_value': '''
              show lldp neighbors detail
              Capability codes:
              (R) Router, (B) Bridge, (T) Telephone, (C) DOCSIS Cable Device
              (W) WLAN Access Point, (P) Repeater, (S) Station, (O) Other
              Device ID            Local Intf      Hold-time  Capability  Port ID  
              Chassis id: 547f.eeff.9526
              Port id: mgmt:0
              Local Port id: mgmt0
              Port Description: mgmt0
              System Name: System1
              System Description: Cisco NX-OS n5000, Software (n5000-uk9), Version 7.3(2)N1(1), RELEASE SOFTWARE Copyright (c) 2002-2012, 2016-2017 by Cisco Systems, Inc. Compiled 5/12/2017 23:00:00
              Time remaining: 116 seconds
              System Capabilities: B
              Enabled Capabilities: B
              Management Address: 10.0.0.7
              Vlan ID: not advertised
              Total entries displayed: 1            
              '''}

    expected_parsed_output_1 = {
        'interfaces': {
            'mgmt0': {
                'port_id': {
                    'mgmt0': {
                        'neighbors': {
                            'System1': {
                                'chassis_id': '547f.eeff.9526',
                                'port_description': 'mgmt0',
                                'system_name': 'System1',
                                'system_description': 'Cisco NX-OS n5000, Software (n5000-uk9), Version 7.3(2)N1(1), RELEASE SOFTWARE Copyright (c) 2002-2012, 2016-2017 by Cisco Systems, Inc. Compiled 5/12/2017 23:00:00',
                                'time_remaining': 116,
                                'capabilities': {
                                    'bridge': {
                                        'name': 'bridge',
                                        'system': True,
                                        'enabled': True
                                    }
                                },
                                'management_address_v4': '10.0.0.7',
                                'vlan_id': 'not advertised'
                            }
                        }
                    }
                }
            }
        },
        'total_entries': 1
    }


    def test_empty(self):
        self.maxDiff = None
        self.device = Mock(**self.empty_output)
        obj = ShowLldpNeighborsDetail(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output)
        obj = ShowLldpNeighborsDetail(device=self.device)
        parsed_output = obj.parse()
        self.assertDictEqual(parsed_output, self.golden_parsed_output)

    def test_golden_customer(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_customer)
        obj = ShowLldpNeighborsDetail(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_customer)

    def test_show_lldp_neighbors_detail_missing_ipv6(self):
        self.maxDiff = None
        self.device = Mock(**self.device_output_1)
        obj = ShowLldpNeighborsDetail(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.expected_parsed_output_1)

# =================================
# Unit test for 'show lldp traffic'
# =================================
class TestShowLldpTraffic(unittest.TestCase):
    '''unit test for show lldp traffic'''
    empty_output = {'execute.return_value': ''}
    golden_parsed_output = {
        'counters': {
            "total_frames_received": 209,
            "total_frames_transmitted": 349,
            "total_frames_received_in_error": 0,
            "total_frames_discarded": 0,
            'total_unrecognized_tlvs': 0,
            'total_entries_aged': 0
        }
    }
    golden_output = {'execute.return_value': '''
        LLDP traffic statistics:

            Total frames transmitted: 349
            Total entries aged: 0
            Total frames received: 209
            Total frames received in error: 0
            Total frames discarded: 0
            Total unrecognized TLVs: 0
    '''
    }
    
    golden_output_1 = {'execute.return_value': '''
        LLDP traffic statistics: 

            Total frames transmitted: 530516
            Total entries aged: 0
            Total frames received: 496131
            Total frames received in error: 0
            Total frames discarded: 0
            Total unrecognized TLVs: 0
            Total flap count: 1
    '''
    }

    golden_parsed_output_1 = {
        'counters': {
            'total_entries_aged': 0,
            'total_flap_count': 1,
            'total_frames_discarded': 0,
            'total_frames_received': 496131,
            'total_frames_received_in_error': 0,
            'total_frames_transmitted': 530516,
            'total_unrecognized_tlvs': 0
        }
    }

    def test_empty(self):
        self.maxDiff = None
        self.device = Mock(**self.empty_output)
        obj = ShowLldpTraffic(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output)
        obj = ShowLldpTraffic(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)

    def test_golden_1(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_1)
        obj = ShowLldpTraffic(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_1)

if __name__ == '__main__':
    unittest.main()
