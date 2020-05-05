#!/bin/env python
import unittest
from unittest.mock import Mock
from pyats.topology import Device

from genie.metaparser.util.exceptions import SchemaEmptyParserError,\
                                       SchemaMissingKeyError
from genie.libs.parser.iosxe.show_lldp import ShowLldp, ShowLldpEntry, \
                                   ShowLldpNeighborsDetail, \
                                   ShowLldpTraffic, \
                                   ShowLldpInterface, \
                                   ShowLldpNeighbors


class test_show_lldp(unittest.TestCase):
    dev1 = Device(name='empty')
    dev_c3850 = Device(name='c3850')
    empty_output = {'execute.return_value': '      '}

    golden_parsed_output = {
        "hello_timer": 30,
        "enabled": True,
        "hold_timer": 120,
        "status": "active",
        "reinit_timer": 2
    }

    golden_output = {'execute.return_value': '''\
        Global LLDP Information:
          Status: ACTIVE
          LLDP advertisements are sent every 30 seconds
          LLDP hold time advertised is 120 seconds
          LLDP interface reinitialisation delay is 2 seconds
    '''
    }

    def test_empty(self):
        self.dev1 = Mock(**self.empty_output)
        obj = ShowLldp(device=self.dev1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden(self):
        self.maxDiff = None
        self.dev_c3850 = Mock(**self.golden_output)
        obj = ShowLldp(device=self.dev_c3850)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output)


class test_show_lldp_entry(unittest.TestCase):
    dev1 = Device(name='empty')
    dev_c3850 = Device(name='c3850')
    empty_output = {'execute.return_value': '      '}

    golden_parsed_output = {
        'interfaces': {
            'GigabitEthernet2/0/15': {
                'if_name': 'GigabitEthernet2/0/15',
                'port_id': {
                    'GigabitEthernet1/0/4': {
                        'neighbors': {
                            'R5': {
                                'neighbor_id': 'R5',
                                'chassis_id': '843d.c6ff.f1b8',
                                'port_id': 'GigabitEthernet1/0/4',
                                'port_description': 'GigabitEthernet1/0/4',
                                'system_description': 'Cisco IOS Software, C3750E Software (C3750E-UNIVERSALK9-M), Version 12.2(58)SE2, RELEASE SOFTWARE (fc1)\nTechnical Support: http://www.cisco.com/techsupport\nCopyright (c) 1986-2011 by Cisco Systems, Inc.\nCompiled Thu 21-Jul-11 01:23 by prod_rel_team',
                                'system_name': 'R5',
                                'time_remaining': 112,
                                'capabilities': {
                                    'mac_bridge': {
                                        'name': 'mac_bridge',
                                        'system': True,
                                        'enabled': True,
                                        },
                                    'router': {
                                        'name': 'router',
                                        'system': True,
                                        'enabled': True,
                                        },
                                    },
                                'management_address': '10.9.1.1',
                                'auto_negotiation': 'supported, enabled',
                                'physical_media_capabilities': ['1000baseT(FD)', '100base-TX(FD)', '100base-TX(HD)', '10base-T(FD)', '10base-T(HD)'],
                                'unit_type': 30,
                                'vlan_id': 1,
                                },
                            },
                        },
                    },
                },
            'GigabitEthernet1/0/16': {
                'if_name': 'GigabitEthernet1/0/16',
                'port_id': {
                    'GigabitEthernet1/0/2': {
                        'neighbors': {
                            'R5': {
                                'neighbor_id': 'R5',
                                'chassis_id': '843d.c6ff.f1b8',
                                'port_id': 'GigabitEthernet1/0/2',
                                'port_description': 'GigabitEthernet1/0/2',
                                'system_name': 'R5',
                                'system_description': 'Cisco IOS Software, C3750E Software (C3750E-UNIVERSALK9-M), Version 12.2(58)SE2, RELEASE SOFTWARE (fc1)\nTechnical Support: http://www.cisco.com/techsupport\nCopyright (c) 1986-2011 by Cisco Systems, Inc.\nCompiled Thu 21-Jul-11 01:23 by prod_rel_team',
                                'time_remaining': 111,
                                'capabilities': {
                                    'mac_bridge': {
                                        'name': 'mac_bridge',
                                        'system': True,
                                        'enabled': True,
                                        },
                                    'router': {
                                        'name': 'router',
                                        'system': True,
                                        'enabled': True,
                                        },
                                    },
                                'management_address': '10.9.1.1',
                                'auto_negotiation': 'supported, enabled',
                                'physical_media_capabilities': ['1000baseT(FD)', '100base-TX(FD)', '100base-TX(HD)', '10base-T(FD)', '10base-T(HD)'],
                                'unit_type': 30,
                                'vlan_id': 1,
                                },
                            },
                        },
                    },
                },
            'GigabitEthernet1/0/17': {
                'if_name': 'GigabitEthernet1/0/17',
                'port_id': {
                    'GigabitEthernet1/0/3': {
                        'neighbors': {
                            'R5': {
                                'neighbor_id': 'R5',
                                'chassis_id': '843d.c6ff.f1b8',
                                'port_id': 'GigabitEthernet1/0/3',
                                'port_description': 'GigabitEthernet1/0/3',
                                'system_description': 'Cisco IOS Software, C3750E Software (C3750E-UNIVERSALK9-M), Version 12.2(58)SE2, RELEASE SOFTWARE (fc1)\nTechnical Support: http://www.cisco.com/techsupport\nCopyright (c) 1986-2011 by Cisco Systems, Inc.\nCompiled Thu 21-Jul-11 01:23 by prod_rel_team',
                                'system_name': 'R5',
                                'time_remaining': 108,
                                'capabilities': {
                                    'mac_bridge': {
                                        'name': 'mac_bridge',
                                        'system': True,
                                        'enabled': True,
                                        },
                                    'router': {
                                        'name': 'router',
                                        'system': True,
                                        'enabled': True,
                                        },
                                    },
                                'management_address': '10.9.1.1',
                                'auto_negotiation': 'supported, enabled',
                                'physical_media_capabilities': ['1000baseT(FD)', '100base-TX(FD)', '100base-TX(HD)', '10base-T(FD)', '10base-T(HD)'],
                                'unit_type': 30,
                                'vlan_id': 1,
                                },
                            },
                        },
                    },
                },
            'GigabitEthernet1/0/15': {
                'if_name': 'GigabitEthernet1/0/15',
                'port_id': {
                    'GigabitEthernet1/0/1': {
                        'neighbors': {
                            'R5': {
                                'neighbor_id': 'R5',
                                'system_description': 'Cisco IOS Software, C3750E Software (C3750E-UNIVERSALK9-M), Version 12.2(58)SE2, RELEASE SOFTWARE (fc1)\nTechnical Support: http://www.cisco.com/techsupport\nCopyright (c) 1986-2011 by Cisco Systems, Inc.\nCompiled Thu 21-Jul-11 01:23 by prod_rel_team',
                                'chassis_id': '843d.c6ff.f1b8',
                                'port_id': 'GigabitEthernet1/0/1',
                                'port_description': 'GigabitEthernet1/0/1',
                                'system_name': 'R5',
                                'time_remaining': 108,
                                'capabilities': {
                                    'mac_bridge': {
                                        'name': 'mac_bridge',
                                        'system': True,
                                        'enabled': True,
                                        },
                                    'router': {
                                        'name': 'router',
                                        'system': True,
                                        'enabled': True,
                                        },
                                    },
                                'management_address': '10.9.1.1',
                                'auto_negotiation': 'supported, enabled',
                                'physical_media_capabilities': ['1000baseT(FD)', '100base-TX(FD)', '100base-TX(HD)', '10base-T(FD)', '10base-T(HD)'],
                                'unit_type': 30,
                                'vlan_id': 1,
                                },
                            },
                        },
                    },
                },
            },
        'total_entries': 4,
        }

    golden_output = {'execute.return_value': '''\
        Capability codes:
            (R) Router, (B) Bridge, (T) Telephone, (C) DOCSIS Cable Device
            (W) WLAN Access Point, (P) Repeater, (S) Station, (O) Other
        ------------------------------------------------
        Local Intf: Gi2/0/15
        Chassis id: 843d.c6ff.f1b8
        Port id: Gi1/0/4
        Port Description: GigabitEthernet1/0/4
        System Name: R5

        System Description: 
        Cisco IOS Software, C3750E Software (C3750E-UNIVERSALK9-M), Version 12.2(58)SE2, RELEASE SOFTWARE (fc1)
        Technical Support: http://www.cisco.com/techsupport
        Copyright (c) 1986-2011 by Cisco Systems, Inc.
        Compiled Thu 21-Jul-11 01:23 by prod_rel_team

        Time remaining: 112 seconds
        System Capabilities: B,R
        Enabled Capabilities: B,R
        Management Addresses:
            IP: 10.9.1.1
        Auto Negotiation - supported, enabled
        Physical media capabilities:
            1000baseT(FD)
            100base-TX(FD)
            100base-TX(HD)
            10base-T(FD)
            10base-T(HD)
        Media Attachment Unit type: 30
        Vlan ID: 1

        ------------------------------------------------
        Local Intf: Gi1/0/16
        Chassis id: 843d.c6ff.f1b8
        Port id: Gi1/0/2
        Port Description: GigabitEthernet1/0/2
        System Name: R5

        System Description: 
        Cisco IOS Software, C3750E Software (C3750E-UNIVERSALK9-M), Version 12.2(58)SE2, RELEASE SOFTWARE (fc1)
        Technical Support: http://www.cisco.com/techsupport
        Copyright (c) 1986-2011 by Cisco Systems, Inc.
        Compiled Thu 21-Jul-11 01:23 by prod_rel_team

        Time remaining: 111 seconds
        System Capabilities: B,R
        Enabled Capabilities: B,R
        Management Addresses:
            IP: 10.9.1.1
        Auto Negotiation - supported, enabled
        Physical media capabilities:
            1000baseT(FD)
            100base-TX(FD)
            100base-TX(HD)
            10base-T(FD)
            10base-T(HD)
        Media Attachment Unit type: 30
        Vlan ID: 1

        ------------------------------------------------
        Local Intf: Gi1/0/17
        Chassis id: 843d.c6ff.f1b8
        Port id: Gi1/0/3
        Port Description: GigabitEthernet1/0/3
        System Name: R5

        System Description: 
        Cisco IOS Software, C3750E Software (C3750E-UNIVERSALK9-M), Version 12.2(58)SE2, RELEASE SOFTWARE (fc1)
        Technical Support: http://www.cisco.com/techsupport
        Copyright (c) 1986-2011 by Cisco Systems, Inc.
        Compiled Thu 21-Jul-11 01:23 by prod_rel_team

        Time remaining: 108 seconds
        System Capabilities: B,R
        Enabled Capabilities: B,R
        Management Addresses:
            IP: 10.9.1.1
        Auto Negotiation - supported, enabled
        Physical media capabilities:
            1000baseT(FD)
            100base-TX(FD)
            100base-TX(HD)
            10base-T(FD)
            10base-T(HD)
        Media Attachment Unit type: 30
        Vlan ID: 1

        ------------------------------------------------
        Local Intf: Gi1/0/15
        Chassis id: 843d.c6ff.f1b8
        Port id: Gi1/0/1
        Port Description: GigabitEthernet1/0/1
        System Name: R5

        System Description: 
        Cisco IOS Software, C3750E Software (C3750E-UNIVERSALK9-M), Version 12.2(58)SE2, RELEASE SOFTWARE (fc1)
        Technical Support: http://www.cisco.com/techsupport
        Copyright (c) 1986-2011 by Cisco Systems, Inc.
        Compiled Thu 21-Jul-11 01:23 by prod_rel_team

        Time remaining: 108 seconds
        System Capabilities: B,R
        Enabled Capabilities: B,R
        Management Addresses:
            IP: 10.9.1.1
        Auto Negotiation - supported, enabled
        Physical media capabilities:
            1000baseT(FD)
            100base-TX(FD)
            100base-TX(HD)
            10base-T(FD)
            10base-T(HD)
        Media Attachment Unit type: 30
        Vlan ID: 1


        Total entries displayed: 4
    '''
    }

    golden_output_1 = {'execute.return_value': '''\
        show lldp entry *

        Capability codes:
            (R) Router, (B) Bridge, (T) Telephone, (C) DOCSIS Cable Device
            (W) WLAN Access Point, (P) Repeater, (S) Station, (O) Other
        ------------------------------------------------
        Local Intf: Gi1/0/13
        Chassis id: 00fe.4fff.5a16e
        Port id: Gi0/0
        Port Description: GigabitEthernet0/0
        System Name: C9300-genie-3

        System Description: 
        Cisco IOS Software [Fuji], Catalyst L3 Switch Software (CAT9K_IOSXE), Version 16.9.3s, RELEASE SOFTWARE (fc3)
        Technical Support: http://www.cisco.com/techsupport
        Copyright (c) 1986-2019 by Cisco Systems, Inc.
        Compiled Sun 02-Jun-19 06:34 by mcpre

        Time remaining: 93 seconds
        System Capabilities: B,R
        Enabled Capabilities: B,R
        Management Addresses:
            IP: 10.1.2.203
        Auto Negotiation - not supported
        Physical media capabilities - not advertised
        Media Attachment Unit type - not advertised
        Vlan ID: - not advertised

        ------------------------------------------------
        Local Intf: Gi1/0/11
        Chassis id: 4500.1eff.67de
        Port id: Gi0/0
        Port Description: GigabitEthernet0/0
        System Name: C9300-genie.lab

        System Description: 
        Cisco IOS Software [Fuji], Catalyst L3 Switch Software (CAT9K_IOSXE), Version 16.9.3, RELEASE SOFTWARE (fc2)
        Technical Support: http://www.cisco.com/techsupport
        Copyright (c) 1986-2019 by Cisco Systems, Inc.
        Compiled Wed 20-Mar-19 08:02 by mcpre

        Time remaining: 101 seconds
        System Capabilities: B,R
        Enabled Capabilities: B,R
        Management Addresses:
            IP: 10.1.23.23
        Auto Negotiation - not supported
        Physical media capabilities - not advertised
        Media Attachment Unit type - not advertised
        Vlan ID: - not advertised

        ------------------------------------------------
        Local Intf: Te1/1/3
        Chassis id: 5a3e.70ff.57b2
        Port id: 5169.53ff.005b
        Port Description - not advertised
        System Name - not advertised
        System Description - not advertised

        Time remaining: 97 seconds
        System Capabilities - not advertised
        Enabled Capabilities - not advertised
        Management Addresses - not advertised
        Auto Negotiation - not supported
        Physical media capabilities - not advertised
        Media Attachment Unit type - not advertised
        Vlan ID: - not advertised

        ------------------------------------------------
        Local Intf: Gi1/0/10
        Chassis id: 8dc3.41ff.2988
        Port id: Gi0/0
        Port Description: GigabitEthernet0/0
        System Name: C9300-Edge.genie

        System Description: 
        Cisco IOS Software [Fuji], Catalyst L3 Switch Software (CAT9K_IOSXE), Version 16.9.3s, RELEASE SOFTWARE (fc3)
        Technical Support: http://www.cisco.com/techsupport
        Copyright (c) 1986-2019 by Cisco Systems, Inc.
        Compiled Sun 02-Jun-19 06:34 by mcpre

        Time remaining: 92 seconds
        System Capabilities: B,R
        Enabled Capabilities: B,R
        Management Addresses:
            IP: 10.1.23.102
        Auto Negotiation - not supported
        Physical media capabilities - not advertised
        Media Attachment Unit type - not advertised
        Vlan ID: - not advertised


        Total entries displayed: 4
    '''
    }

    golden_parsed_output_1 = {
        'interfaces': {
            'GigabitEthernet1/0/10': {
                'if_name': 'GigabitEthernet1/0/10',
                'port_id': {
                    'GigabitEthernet0/0': {
                        'neighbors': {
                            'C9300-Edge.genie': {
                                'auto_negotiation': 'not supported',
                                'capabilities': {
                                'mac_bridge': {
                                    'enabled': True,
                                    'name': 'mac_bridge',
                                    'system': True
                                    },
                                'router': {
                                    'enabled': True,
                                    'name': 'router',
                                    'system': True
                                    }
                                },
                            'chassis_id': '8dc3.41ff.2988',
                            'management_address': '10.1.23.102',
                            'neighbor_id': 'C9300-Edge.genie',
                            'port_description': 'GigabitEthernet0/0',
                            'port_id': 'GigabitEthernet0/0',
                            'system_description': 'Cisco IOS Software [Fuji], Catalyst L3 Switch Software (CAT9K_IOSXE), Version 16.9.3s, RELEASE SOFTWARE (fc3)\nTechnical Support: http://www.cisco.com/techsupport\nCopyright (c) 1986-2019 by Cisco Systems, Inc.\nCompiled Sun 02-Jun-19 06:34 by mcpre',
                            'system_name': 'C9300-Edge.genie',
                            'time_remaining': 92
                            }
                        }
                    }
                },
            },
            'GigabitEthernet1/0/11': {
                'if_name': 'GigabitEthernet1/0/11',
                'port_id': {
                    'GigabitEthernet0/0': {
                        'neighbors': {
                            'C9300-genie.lab': {
                                'auto_negotiation': 'not supported',
                                'capabilities': {
                                    'mac_bridge': {
                                        'enabled': True,
                                        'name': 'mac_bridge',
                                        'system': True
                                        },
                                    'router': {
                                        'enabled': True,
                                        'name': 'router',
                                        'system': True
                                        }
                                    },
                                'chassis_id': '4500.1eff.67de',
                                'management_address': '10.1.23.23',
                                'neighbor_id': 'C9300-genie.lab',
                                'port_description': 'GigabitEthernet0/0',
                                'port_id': 'GigabitEthernet0/0',
                                'system_description': 'Cisco IOS Software [Fuji], Catalyst L3 Switch Software (CAT9K_IOSXE), Version '
                                                    '16.9.3, RELEASE SOFTWARE (fc2)\nTechnical Support: http://www.cisco.com/techsupport\n'
                                                    'Copyright (c) 1986-2019 by Cisco Systems, Inc.\nCompiled Wed 20-Mar-19 08:02 by mcpre',
                                'system_name': 'C9300-genie.lab',
                                'time_remaining': 101,
                                },
                            },
                        },
                    },
                },
            'GigabitEthernet1/0/13': {
                'if_name': 'GigabitEthernet1/0/13',
                'port_id': {
                    'GigabitEthernet0/0': {
                        'neighbors': {
                            'C9300-genie-3': {
                            'auto_negotiation': 'not supported',
                            'capabilities': {
                                'mac_bridge': {
                                    'enabled': True,
                                    'name': 'mac_bridge',
                                    'system': True
                                    },
                                'router': {
                                    'enabled': True,
                                    'name': 'router',
                                    'system': True
                                    }
                                },
                            'chassis_id': '00fe.4fff.5a16e',
                            'management_address': '10.1.2.203',
                            'neighbor_id': 'C9300-genie-3',
                            'port_description': 'GigabitEthernet0/0',
                            'port_id': 'GigabitEthernet0/0',
                            'system_description': 'Cisco IOS Software [Fuji], Catalyst L3 Switch Software (CAT9K_IOSXE), Version '
                                                '16.9.3s, RELEASE SOFTWARE (fc3)\nTechnical Support: http://www.cisco.com/techsupport\n'
                                                'Copyright (c) 1986-2019 by Cisco Systems, Inc.\n'
                                                'Compiled Sun 02-Jun-19 06:34 by mcpre',
                            'system_name': 'C9300-genie-3',
                            'time_remaining': 93,
                            },
                        },
                    },
                },
            },
        'TenGigabitEthernet1/1/3': {
            'if_name': 'TenGigabitEthernet1/1/3',
            'port_id': {
                '5169.53ff.005b': {
                    'neighbors': {
                        'not advertised': {
                            'auto_negotiation': 'not supported',
                            'chassis_id': '5a3e.70ff.57b2',
                            'neighbor_id': 'not advertised',
                            'port_id': '5169.53ff.005b',
                            'system_name': 'not advertised',
                            'time_remaining': 97,
                            'management_address': 'not advertised',
                            },
                        },
                    },
                },
            },
        },
        'total_entries': 4
    }

    golden_output_2 = {'execute.return_value': '''
        ------------------------------------------------
        Chassis id: 10.10.191.112
        Port id: 7018.deff.50a4
        Port Description: IP Phone
        System Name - not advertised
        
        System Description:
        IP Phone, Firmware:90234AP
        
        Time remaining: 170 seconds
        System Capabilities: B,T
        Enabled Capabilities: B,T
        Management Addresses - not advertised
        Auto Negotiation - supported, enabled
        Physical media capabilities:
            100base-TX(FD)
            100base-TX(HD)
            10base-T(FD)
            10base-T(HD)
        Media Attachment Unit type: 16
        Vlan ID: - not advertised
        
        MED Information:
        
            MED Codes:
                  (NP) Network Policy, (LI) Location Identification
                  (PS) Power Source Entity, (PD) Power Device
                  (IN) Inventory
        
            F/W revision: 90234AP
            Manufacturer: Phone-05
            Model: 1220 IP Deskphone
            Capabilities: NP, LI, PD, IN
            Device type: Endpoint Class III
            Network Policy(Voice): VLAN 210, tagged, Layer-2 priority: 5, DSCP: 46
            Network Policy(Voice Signal): VLAN 210, tagged, Layer-2 priority: 0, DSCP: 0
            PD device, Power source: Unknown, Power Priority: High, Wattage: 6.0
            Location - not advertised
        
        ------------------------------------------------
        Chassis id: 10.10.191.104
        Port id: 7018.deff.584d
        Port Description: IP Phone
        System Name - not advertised
        
        System Description:
        IP Phone, Firmware:90234AP
        
        Time remaining: 165 seconds
        System Capabilities: B,T
        Enabled Capabilities: B,T
        Management Addresses - not advertised
        Auto Negotiation - supported, enabled
        Physical media capabilities:
            100base-TX(FD)
            100base-TX(HD)
            10base-T(FD)
            10base-T(HD)
        Media Attachment Unit type: 16
        Vlan ID: - not advertised
        
        MED Information:
        
            MED Codes:
                  (NP) Network Policy, (LI) Location Identification
                  (PS) Power Source Entity, (PD) Power Device
                  (IN) Inventory
        
            F/W revision: 90234AP
            Manufacturer: Phone-05
            Model: 1220 IP Deskphone
            Capabilities: NP, LI, PD, IN
            Device type: Endpoint Class III
            Network Policy(Voice): VLAN 210, tagged, Layer-2 priority: 5, DSCP: 46
            Network Policy(Voice Signal): VLAN 210, tagged, Layer-2 priority: 0, DSCP: 0
            PD device, Power source: Unknown, Power Priority: High, Wattage: 6.0
            Location - not advertised
        
        ------------------------------------------------
        Chassis id: 10.10.191.93
        Port id: fca8.41ff.f37c
        Port Description: IP Phone
        System Name - not advertised
        
        System Description:
        IP Phone, Firmware:90234AP
        
        Time remaining: 158 seconds
        System Capabilities: B,T
        Enabled Capabilities: B,T
        Management Addresses - not advertised
        Auto Negotiation - supported, enabled
        Physical media capabilities:
            100base-TX(FD)
            100base-TX(HD)
            10base-T(FD)
            10base-T(HD)
        Media Attachment Unit type: 16
        Vlan ID: - not advertised
        
        MED Information:
        
            MED Codes:
                  (NP) Network Policy, (LI) Location Identification
                  (PS) Power Source Entity, (PD) Power Device
                  (IN) Inventory
        
            F/W revision: 90234AP
            Manufacturer: Phone-05
            Model: 1220 IP Deskphone
            Capabilities: NP, LI, PD, IN
            Device type: Endpoint Class III
            Network Policy(Voice): VLAN 210, tagged, Layer-2 priority: 5, DSCP: 46
            Network Policy(Voice Signal): VLAN 210, tagged, Layer-2 priority: 0, DSCP: 0
            PD device, Power source: Unknown, Power Priority: High, Wattage: 6.0
            Location - not advertised
        
        ------------------------------------------------
        Chassis id: 10.10.191.91
        Port id: 7052.c5ff.4647
        Port Description: IP Phone
        System Name - not advertised
        
        System Description:
        IP Phone, Firmware:90234AP
        
        Time remaining: 151 seconds
        System Capabilities: B,T
        Enabled Capabilities: B,T
        Management Addresses - not advertised
        Auto Negotiation - supported, enabled
        Physical media capabilities:
            100base-TX(FD)
            100base-TX(HD)
            10base-T(FD)
            10base-T(HD)
        Media Attachment Unit type: 16
        Vlan ID: - not advertised
        
        MED Information:
        
            MED Codes:
                  (NP) Network Policy, (LI) Location Identification
                  (PS) Power Source Entity, (PD) Power Device
                  (IN) Inventory
        
            F/W revision: 90234AP
            Manufacturer: Phone-05
            Model: 1220 IP Deskphone
            Capabilities: NP, LI, PD, IN
            Device type: Endpoint Class III
            Network Policy(Voice): VLAN 210, tagged, Layer-2 priority: 5, DSCP: 46
            Network Policy(Voice Signal): VLAN 210, tagged, Layer-2 priority: 0, DSCP: 0
            PD device, Power source: Unknown, Power Priority: High, Wattage: 6.0
            Location - not advertised
        
        ------------------------------------------------
        Chassis id: 00ff.c8ff.3b7f
        Port id: Gi0/0/0
        Port Description: -X- router
        System Name: router
        
        System Description:
        Cisco IOS Software, ASR920 Software (PPC_LINUX_IOSD-UNIVERSALK9_NPE-M), Version 15.6(2)SP4, RELEASE SOFTWARE (fc4)
        Technical Support: http://www.cisco.com/techsupport
        Copyright (c) 1986-2018 by Cisco Systems, Inc.
        Compiled Mon 19-Mar-18 22:59 by mcpre
        
        Time remaining: 90 seconds
        System Capabilities: B,R
        Enabled Capabilities: R
        Management Addresses:
            IP: 10.10.4.30
        Auto Negotiation - not supported
        Physical media capabilities - not advertised
        Media Attachment Unit type - not advertised
        Vlan ID: - not advertised
        
        ------------------------------------------------
        Chassis id: 10.10.191.107
        Port id: 7018.deff.572d
        Port Description: IP Phone
        System Name - not advertised
        
        System Description:
        IP Phone, Firmware:90234AP
        
        Time remaining: 154 seconds
        System Capabilities: B,T
        Enabled Capabilities: B,T
        Management Addresses - not advertised
        Auto Negotiation - supported, enabled
        Physical media capabilities:
            100base-TX(FD)
            100base-TX(HD)
            10base-T(FD)
            10base-T(HD)
        Media Attachment Unit type: 16
        Vlan ID: - not advertised
        
        MED Information:
        
            MED Codes:
                  (NP) Network Policy, (LI) Location Identification
                  (PS) Power Source Entity, (PD) Power Device
                  (IN) Inventory
        
            F/W revision: 90234AP
            Manufacturer: Phone-05
            Model: 1220 IP Deskphone
            Capabilities: NP, LI, PD, IN
            Device type: Endpoint Class III
            Network Policy(Voice): VLAN 210, tagged, Layer-2 priority: 5, DSCP: 46
            Network Policy(Voice Signal): VLAN 210, tagged, Layer-2 priority: 0, DSCP: 0
            PD device, Power source: Unknown, Power Priority: High, Wattage: 6.0
            Location - not advertised
        
        ------------------------------------------------
        Chassis id: d89e.f3ff.58fe
        Port id: d89e.f3ff.58fe
        Port Description - not advertised
        System Name - not advertised
        System Description - not advertised
        
        Time remaining: 2845 seconds
        System Capabilities - not advertised
        Enabled Capabilities - not advertised
        Management Addresses - not advertised
        Auto Negotiation - supported, enabled
        Physical media capabilities:
            1000baseT(FD)
        Media Attachment Unit type - not advertised
        Vlan ID: - not advertised
        
        MED Information:
        
            MED Codes:
                  (NP) Network Policy, (LI) Location Identification
                  (PS) Power Source Entity, (PD) Power Device
                  (IN) Inventory
        
            Inventory information - not advertised
            Capabilities:
            Device type: Endpoint Class I
            Network Policies - not advertised
            Power requirements - not advertised
            Location - not advertised
        
        ------------------------------------------------
        Chassis id: 6400.6aff.7d09
        Port id: 6400.6aff.7d09
        Port Description - not advertised
        System Name - not advertised
        System Description - not advertised
        
        Time remaining: 3500 seconds
        System Capabilities - not advertised
        Enabled Capabilities - not advertised
        Management Addresses - not advertised
        Auto Negotiation - supported, enabled
        Physical media capabilities:
            1000baseT(FD)
        Media Attachment Unit type - not advertised
        Vlan ID: - not advertised
        
        MED Information:
        
            MED Codes:
                  (NP) Network Policy, (LI) Location Identification
                  (PS) Power Source Entity, (PD) Power Device
                  (IN) Inventory
        
            Inventory information - not advertised
            Capabilities:
            Device type: Endpoint Class I
            Network Policies - not advertised
            Power requirements - not advertised
            Location - not advertised
                
        Total entries displayed: 8
        '''}

    golden_parsed_output_2 = {
    'interfaces': {
        'N/A': {
            'if_name': 'N/A',
            'port_id': {
                '6400.6aff.7d09': {
                    'neighbors': {
                        'not advertised': {
                            'auto_negotiation': 'supported, enabled',
                            'chassis_id': '6400.6aff.7d09',
                            'management_address': 'not advertised',
                            'neighbor_id': 'not advertised',
                            'physical_media_capabilities': ['1000baseT(FD)'],
                            'port_id': '6400.6aff.7d09',
                            'system_name': 'not advertised',
                            'time_remaining': 3500,
                        },
                    },
                },
                '7018.deff.50a4': {
                    'neighbors': {
                        'not advertised': {
                            'auto_negotiation': 'supported, enabled',
                            'capabilities': {
                                'mac_bridge': {
                                    'enabled': True,
                                    'name': 'mac_bridge',
                                    'system': True,
                                },
                                'telephone': {
                                    'enabled': True,
                                    'name': 'telephone',
                                    'system': True,
                                },
                            },
                            'chassis_id': '10.10.191.112',
                            'management_address': 'not advertised',
                            'neighbor_id': 'not advertised',
                            'physical_media_capabilities': ['100base-TX(FD)', '100base-TX(HD)', '10base-T(FD)', '10base-T(HD)'],
                            'port_description': 'IP Phone',
                            'port_id': '7018.deff.50a4',
                            'system_description': 'IP Phone, Firmware:90234AP',
                            'system_name': 'not advertised',
                            'time_remaining': 170,
                            'unit_type': 16,
                        },
                    },
                },
                '7018.deff.572d': {
                    'neighbors': {
                        'not advertised': {
                            'auto_negotiation': 'supported, enabled',
                            'capabilities': {
                                'mac_bridge': {
                                    'enabled': True,
                                    'name': 'mac_bridge',
                                    'system': True,
                                },
                                'telephone': {
                                    'enabled': True,
                                    'name': 'telephone',
                                    'system': True,
                                },
                            },
                            'chassis_id': '10.10.191.107',
                            'management_address': 'not advertised',
                            'neighbor_id': 'not advertised',
                            'physical_media_capabilities': ['100base-TX(FD)', '100base-TX(HD)', '10base-T(FD)', '10base-T(HD)'],
                            'port_description': 'IP Phone',
                            'port_id': '7018.deff.572d',
                            'system_description': 'IP Phone, Firmware:90234AP',
                            'system_name': 'not advertised',
                            'time_remaining': 154,
                            'unit_type': 16,
                        },
                    },
                },
                '7018.deff.584d': {
                    'neighbors': {
                        'not advertised': {
                            'auto_negotiation': 'supported, enabled',
                            'capabilities': {
                                'mac_bridge': {
                                    'enabled': True,
                                    'name': 'mac_bridge',
                                    'system': True,
                                },
                                'telephone': {
                                    'enabled': True,
                                    'name': 'telephone',
                                    'system': True,
                                },
                            },
                            'chassis_id': '10.10.191.104',
                            'management_address': 'not advertised',
                            'neighbor_id': 'not advertised',
                            'physical_media_capabilities': ['100base-TX(FD)', '100base-TX(HD)', '10base-T(FD)', '10base-T(HD)'],
                            'port_description': 'IP Phone',
                            'port_id': '7018.deff.584d',
                            'system_description': 'IP Phone, Firmware:90234AP',
                            'system_name': 'not advertised',
                            'time_remaining': 165,
                            'unit_type': 16,
                        },
                    },
                },
                '7052.c5ff.4647': {
                    'neighbors': {
                        'not advertised': {
                            'auto_negotiation': 'supported, enabled',
                            'capabilities': {
                                'mac_bridge': {
                                    'enabled': True,
                                    'name': 'mac_bridge',
                                    'system': True,
                                },
                                'telephone': {
                                    'enabled': True,
                                    'name': 'telephone',
                                    'system': True,
                                },
                            },
                            'chassis_id': '10.10.191.91',
                            'management_address': 'not advertised',
                            'neighbor_id': 'not advertised',
                            'physical_media_capabilities': ['100base-TX(FD)', '100base-TX(HD)', '10base-T(FD)', '10base-T(HD)'],
                            'port_description': 'IP Phone',
                            'port_id': '7052.c5ff.4647',
                            'system_description': 'IP Phone, Firmware:90234AP',
                            'system_name': 'not advertised',
                            'time_remaining': 151,
                            'unit_type': 16,
                        },
                    },
                },
                'D89e.f3ff.58fe': {
                    'neighbors': {
                        'not advertised': {
                            'auto_negotiation': 'supported, enabled',
                            'chassis_id': 'd89e.f3ff.58fe',
                            'management_address': 'not advertised',
                            'neighbor_id': 'not advertised',
                            'physical_media_capabilities': ['1000baseT(FD)'],
                            'port_id': 'D89e.f3ff.58fe',
                            'system_name': 'not advertised',
                            'time_remaining': 2845,
                        },
                    },
                },
                'Fca8.41ff.f37c': {
                    'neighbors': {
                        'not advertised': {
                            'auto_negotiation': 'supported, enabled',
                            'capabilities': {
                                'mac_bridge': {
                                    'enabled': True,
                                    'name': 'mac_bridge',
                                    'system': True,
                                },
                                'telephone': {
                                    'enabled': True,
                                    'name': 'telephone',
                                    'system': True,
                                },
                            },
                            'chassis_id': '10.10.191.93',
                            'management_address': 'not advertised',
                            'neighbor_id': 'not advertised',
                            'physical_media_capabilities': ['100base-TX(FD)', '100base-TX(HD)', '10base-T(FD)', '10base-T(HD)'],
                            'port_description': 'IP Phone',
                            'port_id': 'Fca8.41ff.f37c',
                            'system_description': 'IP Phone, Firmware:90234AP',
                            'system_name': 'not advertised',
                            'time_remaining': 158,
                            'unit_type': 16,
                        },
                    },
                },
                'GigabitEthernet0/0/0': {
                    'neighbors': {
                        'router': {
                            'auto_negotiation': 'not supported',
                            'capabilities': {
                                'mac_bridge': {
                                    'name': 'mac_bridge',
                                    'system': True,
                                },
                                'router': {
                                    'enabled': True,
                                    'name': 'router',
                                    'system': True,
                                },
                            },
                            'chassis_id': '00ff.c8ff.3b7f',
                            'management_address': '10.10.4.30',
                            'neighbor_id': 'router',
                            'port_description': '-X- router',
                            'port_id': 'GigabitEthernet0/0/0',
                            'system_description': 'Cisco IOS Software, ASR920 Software (PPC_LINUX_IOSD-UNIVERSALK9_NPE-M), Version 15.6(2)SP4, RELEASE SOFTWARE (fc4)\nTechnical Support: http://www.cisco.com/techsupport\nCopyright (c) 1986-2018 by Cisco Systems, Inc.\nCompiled Mon 19-Mar-18 22:59 by mcpre',
                            'system_name': 'router',
                            'time_remaining': 90,
                        },
                    },
                },
            },
        },
    },
    'med_information': {
        'capabilities': ['NP', 'LI', 'PD', 'IN'],
        'device_type': 'Endpoint Class I',
        'f/w_revision': '90234AP',
        'location': 'not advertised',
        'manufacturer': 'Phone-05',
        'model': '1220 IP Deskphone',
        'network_policy': {
            'voice': {
                'dscp': 46,
                'layer_2_priority': 5,
                'tagged': True,
                'vlan': 210,
            },
            'voice_signal': {
                'dscp': 0,
                'layer_2_priority': 0,
                'tagged': True,
                'vlan': 210,
            },
        },
        'power_priority': 'High',
        'power_source': 'Unknown',
        'wattage': 6.0,
    },
    'total_entries': 8,
}

    def test_empty(self):
        self.dev1 = Mock(**self.empty_output)
        obj = ShowLldpEntry(device=self.dev1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse(entry='GigabitEthernet1/0/19')

    def test_golden(self):
        self.maxDiff = None
        self.dev_c3850 = Mock(**self.golden_output)
        obj = ShowLldpEntry(device=self.dev_c3850)
        parsed_output = obj.parse(entry='*')
        self.assertEqual(parsed_output, self.golden_parsed_output)

    def test_golden_1(self):
        self.maxDiff = None
        self.dev_c3850 = Mock(**self.golden_output_1)
        obj = ShowLldpEntry(device=self.dev_c3850)
        parsed_output = obj.parse(entry='*')
        self.assertEqual(parsed_output, self.golden_parsed_output_1)

    def test_golden_2(self):
        self.maxDiff = None
        self.dev_c3850 = Mock(**self.golden_output_2)
        obj = ShowLldpEntry(device=self.dev_c3850)
        parsed_output = obj.parse(entry='*')
        self.assertEqual(parsed_output, self.golden_parsed_output_2)


class test_show_lldp_neighbor_detail(unittest.TestCase):
    dev1 = Device(name='empty')
    dev_c3850 = Device(name='c3850')
    empty_output = {'execute.return_value': '      '}

    golden_parsed_output = {
        'interfaces': {
            'GigabitEthernet2/0/15': {
                'if_name': 'GigabitEthernet2/0/15',
                'port_id': {
                    'GigabitEthernet1/0/4': {
                        'neighbors': {
                            'R5': {
                                'neighbor_id': 'R5',
                                'chassis_id': '843d.c6ff.f1b8',
                                'port_id': 'GigabitEthernet1/0/4',
                                'port_description': 'GigabitEthernet1/0/4',
                                'system_description': 'Cisco IOS Software, C3750E Software (C3750E-UNIVERSALK9-M), Version 12.2(58)SE2, RELEASE SOFTWARE (fc1)\nTechnical Support: http://www.cisco.com/techsupport\nCopyright (c) 1986-2011 by Cisco Systems, Inc.\nCompiled Thu 21-Jul-11 01:23 by prod_rel_team',
                                'system_name': 'R5',
                                'time_remaining': 101,
                                'capabilities': {
                                    'mac_bridge': {
                                        'name': 'mac_bridge',
                                        'system': True,
                                        'enabled': True,
                                        },
                                    'router': {
                                        'name': 'router',
                                        'system': True,
                                        'enabled': True,
                                        },
                                    },
                                'management_address': '10.9.1.1',
                                'auto_negotiation': 'supported, enabled',
                                'physical_media_capabilities': ['1000baseT(FD)', '100base-TX(FD)', '100base-TX(HD)', '10base-T(FD)', '10base-T(HD)'],
                                'unit_type': 30,
                                'vlan_id': 1,
                                },
                            },
                        },
                    },
                },
            'GigabitEthernet1/0/16': {
                'if_name': 'GigabitEthernet1/0/16',
                'port_id': {
                    'GigabitEthernet1/0/2': {
                        'neighbors': {
                            'R5': {
                                'neighbor_id': 'R5',
                                'chassis_id': '843d.c6ff.f1b8',
                                'port_id': 'GigabitEthernet1/0/2',
                                'port_description': 'GigabitEthernet1/0/2',
                                'system_description': 'Cisco IOS Software, C3750E Software (C3750E-UNIVERSALK9-M), Version 12.2(58)SE2, RELEASE SOFTWARE (fc1)\nTechnical Support: http://www.cisco.com/techsupport\nCopyright (c) 1986-2011 by Cisco Systems, Inc.\nCompiled Thu 21-Jul-11 01:23 by prod_rel_team',
                                'system_name': 'R5',
                                'time_remaining': 99,
                                'capabilities': {
                                    'mac_bridge': {
                                        'name': 'mac_bridge',
                                        'system': True,
                                        'enabled': True,
                                        },
                                    'router': {
                                        'name': 'router',
                                        'system': True,
                                        'enabled': True,
                                        },
                                    },
                                'management_address': '10.9.1.1',
                                'auto_negotiation': 'supported, enabled',
                                'physical_media_capabilities': ['1000baseT(FD)', '100base-TX(FD)', '100base-TX(HD)', '10base-T(FD)', '10base-T(HD)'],
                                'unit_type': 30,
                                'vlan_id': 1,
                                },
                            },
                        },
                    },
                },
            'GigabitEthernet1/0/17': {
                'if_name': 'GigabitEthernet1/0/17',
                'port_id': {
                    'GigabitEthernet1/0/3': {
                        'neighbors': {
                            'R5': {
                                'neighbor_id': 'R5',
                                'chassis_id': '843d.c6ff.f1b8',
                                'port_id': 'GigabitEthernet1/0/3',
                                'port_description': 'GigabitEthernet1/0/3',
                                'system_name': 'R5',
                                'system_description': 'Cisco IOS Software, C3750E Software (C3750E-UNIVERSALK9-M), Version 12.2(58)SE2, RELEASE SOFTWARE (fc1)\nTechnical Support: http://www.cisco.com/techsupport\nCopyright (c) 1986-2011 by Cisco Systems, Inc.\nCompiled Thu 21-Jul-11 01:23 by prod_rel_team',
                                'time_remaining': 94,
                                'capabilities': {
                                    'mac_bridge': {
                                        'name': 'mac_bridge',
                                        'system': True,
                                        'enabled': True,
                                        },
                                    'router': {
                                        'name': 'router',
                                        'system': True,
                                        'enabled': True,
                                        },
                                    },
                                'management_address': '10.9.1.1',
                                'auto_negotiation': 'supported, enabled',
                                'physical_media_capabilities': ['1000baseT(FD)', '100base-TX(FD)', '100base-TX(HD)', '10base-T(FD)', '10base-T(HD)'],
                                'unit_type': 30,
                                'vlan_id': 1,
                                },
                            },
                        },
                    },
                },
            'GigabitEthernet1/0/15': {
                'if_name': 'GigabitEthernet1/0/15',
                'port_id': {
                    'GigabitEthernet1/0/1': {
                        'neighbors': {
                            'R5': {
                                'neighbor_id': 'R5',
                                'chassis_id': '843d.c6ff.f1b8',
                                'port_id': 'GigabitEthernet1/0/1',
                                'port_description': 'GigabitEthernet1/0/1',
                                'system_name': 'R5',
                                'system_description': 'Cisco IOS Software, C3750E Software (C3750E-UNIVERSALK9-M), Version 12.2(58)SE2, RELEASE SOFTWARE (fc1)\nTechnical Support: http://www.cisco.com/techsupport\nCopyright (c) 1986-2011 by Cisco Systems, Inc.\nCompiled Thu 21-Jul-11 01:23 by prod_rel_team',
                                'time_remaining': 98,
                                'capabilities': {
                                    'mac_bridge': {
                                        'name': 'mac_bridge',
                                        'system': True,
                                        'enabled': True,
                                        },
                                    'router': {
                                        'name': 'router',
                                        'system': True,
                                        'enabled': True,
                                        },
                                    },
                                'management_address': '10.9.1.1',
                                'auto_negotiation': 'supported, enabled',
                                'physical_media_capabilities': ['1000baseT(FD)', '100base-TX(FD)', '100base-TX(HD)', '10base-T(FD)', '10base-T(HD)'],
                                'unit_type': 30,
                                'vlan_id': 1,
                                },
                            },
                        },
                    },
                },
            },
        'total_entries': 4,
        }

    golden_output = {'execute.return_value': '''\
        ------------------------------------------------
        Local Intf: Gi2/0/15
        Chassis id: 843d.c6ff.f1b8
        Port id: Gi1/0/4
        Port Description: GigabitEthernet1/0/4
        System Name: R5

        System Description: 
        Cisco IOS Software, C3750E Software (C3750E-UNIVERSALK9-M), Version 12.2(58)SE2, RELEASE SOFTWARE (fc1)
        Technical Support: http://www.cisco.com/techsupport
        Copyright (c) 1986-2011 by Cisco Systems, Inc.
        Compiled Thu 21-Jul-11 01:23 by prod_rel_team

        Time remaining: 101 seconds
        System Capabilities: B,R
        Enabled Capabilities: B,R
        Management Addresses:
            IP: 10.9.1.1
        Auto Negotiation - supported, enabled
        Physical media capabilities:
            1000baseT(FD)
            100base-TX(FD)
            100base-TX(HD)
            10base-T(FD)
            10base-T(HD)
        Media Attachment Unit type: 30
        Vlan ID: 1

        ------------------------------------------------
        Local Intf: Gi1/0/16
        Chassis id: 843d.c6ff.f1b8
        Port id: Gi1/0/2
        Port Description: GigabitEthernet1/0/2
        System Name: R5

        System Description: 
        Cisco IOS Software, C3750E Software (C3750E-UNIVERSALK9-M), Version 12.2(58)SE2, RELEASE SOFTWARE (fc1)
        Technical Support: http://www.cisco.com/techsupport
        Copyright (c) 1986-2011 by Cisco Systems, Inc.
        Compiled Thu 21-Jul-11 01:23 by prod_rel_team

        Time remaining: 99 seconds
        System Capabilities: B,R
        Enabled Capabilities: B,R
        Management Addresses:
            IP: 10.9.1.1
        Auto Negotiation - supported, enabled
        Physical media capabilities:
            1000baseT(FD)
            100base-TX(FD)
            100base-TX(HD)
            10base-T(FD)
            10base-T(HD)
        Media Attachment Unit type: 30
        Vlan ID: 1

        ------------------------------------------------
        Local Intf: Gi1/0/17
        Chassis id: 843d.c6ff.f1b8
        Port id: Gi1/0/3
        Port Description: GigabitEthernet1/0/3
        System Name: R5

        System Description: 
        Cisco IOS Software, C3750E Software (C3750E-UNIVERSALK9-M), Version 12.2(58)SE2, RELEASE SOFTWARE (fc1)
        Technical Support: http://www.cisco.com/techsupport
        Copyright (c) 1986-2011 by Cisco Systems, Inc.
        Compiled Thu 21-Jul-11 01:23 by prod_rel_team

        Time remaining: 94 seconds
        System Capabilities: B,R
        Enabled Capabilities: B,R
        Management Addresses:
            IP: 10.9.1.1
        Auto Negotiation - supported, enabled
        Physical media capabilities:
            1000baseT(FD)
            100base-TX(FD)
            100base-TX(HD)
            10base-T(FD)
            10base-T(HD)
        Media Attachment Unit type: 30
        Vlan ID: 1

        ------------------------------------------------
        Local Intf: Gi1/0/15
        Chassis id: 843d.c6ff.f1b8
        Port id: Gi1/0/1
        Port Description: GigabitEthernet1/0/1
        System Name: R5

        System Description: 
        Cisco IOS Software, C3750E Software (C3750E-UNIVERSALK9-M), Version 12.2(58)SE2, RELEASE SOFTWARE (fc1)
        Technical Support: http://www.cisco.com/techsupport
        Copyright (c) 1986-2011 by Cisco Systems, Inc.
        Compiled Thu 21-Jul-11 01:23 by prod_rel_team

        Time remaining: 98 seconds
        System Capabilities: B,R
        Enabled Capabilities: B,R
        Management Addresses:
            IP: 10.9.1.1
        Auto Negotiation - supported, enabled
        Physical media capabilities:
            1000baseT(FD)
            100base-TX(FD)
            100base-TX(HD)
            10base-T(FD)
            10base-T(HD)
        Media Attachment Unit type: 30
        Vlan ID: 1


        Total entries displayed: 4
    '''
    }

    golden_output_2 = {'execute.return_value': '''
    Local Intf: Gi0/1/7
    Chassis id: 10.10.0.1
    Port id: C8F9F9D61BC2:P1
    Port Description: SW PORT
    System Name: SEPC8F9F9D61BC2
    
    System Description:
    Cisco IP Phone 7962G,V12, SCCP42.9-3-1ES27S
    
    Time remaining: 127 seconds
    System Capabilities: B,T
    Enabled Capabilities: B,T
    Management Addresses:
        IP: 10.10.0.1
    Auto Negotiation - supported, enabled
    Physical media capabilities:
        1000baseT(HD)
        1000baseX(FD)
        Symm, Asym Pause(FD)
        Symm Pause(FD)
    Media Attachment Unit type: 16
    Vlan ID: - not advertised
    
    MED Information:
    
        MED Codes:
    
            (NP) Network Policy, (LI) Location Identification
            (PS) Power Source Entity, (PD) Power Device
            (IN) Inventory
            
        H/W revision: 12
        F/W revision: tnp62.8-3-1-21a.bin
        S/W revision: SCCP42.9-3-1ES27S
        Serial number: FCH1610A5S5
        Manufacturer: Cisco Systems, Inc.
        Model: CP-7962G
        Capabilities: NP, PD, IN
        Device type: Endpoint Class III
        Network Policy(Voice): VLAN 10, tagged, Layer-2 priority: 5, DSCP: 46
        Network Policy(Voice Signal): VLAN 10, tagged, Layer-2 priority: 4, DSCP: 32
        PD device, Power source: Unknown, Power Priority: Unknown, Wattage: 6.3
        Location - not advertised
        
    Total entries displayed: 1
    '''}

    golden_parsed_output_2 = {
    'interfaces': {
        'GigabitEthernet0/1/7': {
            'if_name': 'GigabitEthernet0/1/7',
            'port_id': {
                'C8F9F9D61BC2:P1': {
                    'neighbors': {
                        'SEPC8F9F9D61BC2': {
                            'auto_negotiation': 'supported, enabled',
                            'capabilities': {
                                'mac_bridge': {
                                    'enabled': True,
                                    'name': 'mac_bridge',
                                    'system': True,
                                },
                                'telephone': {
                                    'enabled': True,
                                    'name': 'telephone',
                                    'system': True,
                                },
                            },
                            'chassis_id': '10.10.0.1',
                            'management_address': '10.10.0.1',
                            'neighbor_id': 'SEPC8F9F9D61BC2',
                            'physical_media_capabilities': ['1000baseT(HD)', '1000baseX(FD)', 'Symm, Asym Pause(FD)', 'Symm Pause(FD)'],
                            'port_description': 'SW PORT',
                            'port_id': 'C8F9F9D61BC2:P1',
                            'system_description': 'Cisco IP Phone 7962G,V12, SCCP42.9-3-1ES27S\n',
                            'system_name': 'SEPC8F9F9D61BC2',
                            'time_remaining': 127,
                            'unit_type': 16,
                            
                        },
                    },
                },
            },
        },
    },
    'med_information': {
        'capabilities': ['NP', 'PD', 'IN'],
        'device_type': 'PD device',
        'f/w_revision': 'tnp62.8-3-1-21a.bin',
        's/w_revision': 'SCCP42.9-3-1ES27S',
        'h/w_revision': '12',
        'location': 'not advertised',
        'manufacturer': 'Cisco Systems, Inc.',
        'model': 'CP-7962G',
        'network_policy': {
            'voice': {
                'dscp': 46,
                'layer_2_priority': 5,
                'tagged': True,
                'vlan': 10,
            },
            'voice_signal': {
                'dscp': 32,
                'layer_2_priority': 4,
                'tagged': True,
                'vlan': 10,
            },
        },
        'power_priority': 'Unknown',
        'power_source': 'Unknown',
        'serial_number': 'FCH1610A5S5',
        'wattage': 6.3,
    },
    'total_entries': 1,
}

    golden_output_3 = {'execute.return_value': '''     
        ------------------------------------------------
        Local Intf: Gi1/0/32
        Chassis id: FE80::EC22:9A75:BBC7:71AF
        Port id: 222
        Port Description: Description
        System Name - not advertised
        
        System Description: 
        {"SN":"SN-NR","Owner":"OWNER"}
        
        Time remaining: 92 seconds
        System Capabilities - not advertised
        Enabled Capabilities - not advertised
        Management Addresses:
            IPV6: 0000:0000:0000:0000:0000:ffff:7f00:0001
        Auto Negotiation - not supported
        Physical media capabilities - not advertised
        Media Attachment Unit type - not advertised
        Vlan ID: - not advertised
        
        
        Total entries displayed: 1
    '''}

    golden_parsed_output_3 = {
        'interfaces': {
            'GigabitEthernet1/0/32': {
                'if_name': 'GigabitEthernet1/0/32',
                'port_id': {
                    '222': {
                        'neighbors': {
                            'not advertised': {
                                'neighbor_id': 'not advertised',
                                'chassis_id': 'FE80::EC22:9A75:BBC7:71AF',
                                'port_id': '222',
                                'port_description': 'Description',
                                'system_name': 'not advertised',
                                'system_description': '{"SN":"SN-NR","Owner":"OWNER"}',
                                'time_remaining': 92,
                                'management_address': '0000:0000:0000:0000:0000:ffff:7f00:0001',
                                'auto_negotiation': 'not supported'
                            },
                        },
                    },
                },
            },
        },
        'total_entries': 1,
    }

    golden_output_4 = {'execute.return_value': '''     
        ------------------------------------------------
        Local Intf: Gi1/0/17
        Chassis id: 127.0.0.2
        Port id: c81f.7777.6666
        Port Description - not advertised
        System Name: TestName
        System Description - not advertised
        
        Time remaining: 104 seconds
        System Capabilities: B,T
        Enabled Capabilities: B,T
        Management Addresses:
            IP: 127.0.0.2
            OID:
                1.3.6.1.4.1.6889.1.69.2.0.
        Auto Negotiation - not supported
        Physical media capabilities - not advertised
        Media Attachment Unit type: 30
        Vlan ID: - not advertised
        
        MED Information:
        
            MED Codes:
                  (NP) Network Policy, (LI) Location Identification
                  (PS) Power Source Entity, (PD) Power Device
                  (IN) Inventory
        
            H/W revision: 9611GD02C
            S/W revision: 6.6604
            Serial number: 12389WET87
            Manufacturer: Avaya
            Model: 9611
            Capabilities: NP, PD, IN
            Device type: Endpoint Class III
            Network Policy(Voice): VLAN 66, tagged, Layer-2 priority: 5, DSCP: 46
            Power requirements - not advertised
            Location - not advertised
        
        
        Total entries displayed: 1
        '''}

    golden_parsed_output_4 = {
      'interfaces': {
        'GigabitEthernet1/0/17': {
          'if_name': 'GigabitEthernet1/0/17',
          'port_id': {
            'C81f.7777.6666': {
              'neighbors': {
                'TestName': {
                  'neighbor_id': 'TestName',
                  'chassis_id': '127.0.0.2',
                  'port_id': 'C81f.7777.6666',
                  'system_name': 'TestName',
                  'time_remaining': 104,
                  'capabilities': {
                    'mac_bridge': {
                      'name': 'mac_bridge',
                      'system': True,
                      'enabled': True
                    },
                    'telephone': {
                      'name': 'telephone',
                      'system': True,
                      'enabled': True
                    }
                  },
                  'management_address': '127.0.0.2',
                  'auto_negotiation': 'not supported',
                  'unit_type': 30
                }
              }
            }
          }
        }
      },
      'med_information': {
        'h/w_revision': '9611GD02C',
        's/w_revision': '6.6604',
        'serial_number': '12389WET87',
        'manufacturer': 'Avaya',
        'model': '9611',
        'capabilities': [
          'NP',
          'PD',
          'IN'
        ],
        'device_type': 'Endpoint Class III',
        'network_policy': {
          'voice': {
            'tagged': True,
            'layer_2_priority': 5,
            'dscp': 46,
            'vlan': 66
          }
        },
        'location': 'not advertised'
      },
      'total_entries': 1
    }

    golden_output_5 = {'execute.return_value': '''     
        ------------------------------------------------
        Local Intf: Gi1/0/19
        Chassis id: 6400.3333.1111
        Port id: 6400.3333.1111
        Port Description - not advertised
        System Name - not advertised
        System Description - not advertised
        
        Time remaining: 3284 seconds
        System Capabilities - not advertised
        Enabled Capabilities - not advertised
        Management Addresses - not advertised
        Auto Negotiation - supported, enabled
        Physical media capabilities:
            1000baseT(FD)
        Media Attachment Unit type - not advertised
        Vlan ID: - not advertised
        
        MED Information:
        
            MED Codes:
                  (NP) Network Policy, (LI) Location Identification
                  (PS) Power Source Entity, (PD) Power Device
                  (IN) Inventory
        
            Inventory information - not advertised
            Capabilities: 
            Device type: Endpoint Class I
            Network Policies - not advertised
            Power requirements - not advertised
            Location - not advertised
        
        
        Total entries displayed: 1
        '''}

    golden_parsed_output_5 = {
        'interfaces': {
            'GigabitEthernet1/0/19': {
                'if_name': 'GigabitEthernet1/0/19',
                'port_id': {
                    '6400.3333.1111': {
                        'neighbors': {
                            'not advertised': {
                                'neighbor_id': 'not advertised',
                                'chassis_id': '6400.3333.1111',
                                'port_id': '6400.3333.1111',
                                'system_name': 'not advertised',
                                'time_remaining': 3284,
                                'management_address': 'not advertised',
                                'auto_negotiation': 'supported, enabled',
                                'physical_media_capabilities': [
                                    '1000baseT(FD)'
                                ]
                            }
                        }
                    }
                }
            }
        },
        'med_information': {
            'device_type': 'Endpoint Class I',
            'location': 'not advertised'
        },
        'total_entries': 1
    }

    def test_empty(self):
        self.dev1 = Mock(**self.empty_output)
        obj = ShowLldpNeighborsDetail(device=self.dev1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden(self):
        self.maxDiff = None
        self.dev_c3850 = Mock(**self.golden_output)
        obj = ShowLldpNeighborsDetail(device=self.dev_c3850)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output)

    def test_golden_2(self):
        self.maxDiff = None
        self.dev_c3850 = Mock(**self.golden_output_2)
        obj = ShowLldpNeighborsDetail(device=self.dev_c3850)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output_2)

    def test_golden_3(self):
        self.maxDiff = None
        self.dev_c3850 = Mock(**self.golden_output_3)
        obj = ShowLldpNeighborsDetail(device=self.dev_c3850)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_3)

    def test_golden_4(self):
        self.maxDiff = None
        self.dev_c3850 = Mock(**self.golden_output_4)
        obj = ShowLldpNeighborsDetail(device=self.dev_c3850)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_4)

    def test_golden_5(self):
        self.maxDiff = None
        self.dev_c3850 = Mock(**self.golden_output_5)
        obj = ShowLldpNeighborsDetail(device=self.dev_c3850)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_5)


class test_show_lldp_traffic(unittest.TestCase):
    dev1 = Device(name='empty')
    dev_c3850 = Device(name='c3850')
    empty_output = {'execute.return_value': '      '}

    golden_parsed_output = {
        "frame_in": 13315,
        "frame_out": 20372,
        "frame_error_in": 0,
        "frame_discard": 14,
        "tlv_discard": 0,
        'tlv_unknown': 0,
        'entries_aged_out': 34
    }

    golden_output = {'execute.return_value': '''\
        LLDP traffic statistics:
          Total frames out: 20372
          Total entries aged: 34
          Total frames in: 13315
          Total frames received in error: 0
          Total frames discarded: 14
          Total TLVs discarded: 0
          Total TLVs unrecognized: 0
    '''
    }

    def test_empty(self):
        self.dev1 = Mock(**self.empty_output)
        obj = ShowLldpTraffic(device=self.dev1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden(self):
        self.maxDiff = None
        self.dev_c3850 = Mock(**self.golden_output)
        obj = ShowLldpTraffic(device=self.dev_c3850)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output)


class test_show_lldp_interface(unittest.TestCase):
    dev1 = Device(name='empty')
    dev_c3850 = Device(name='c3850')
    empty_output = {'execute.return_value': '      '}

    golden_parsed_output = {
        'interfaces': {
            'GigabitEthernet1/0/15': {
                'tx': 'enabled',
                'rx': 'enabled',
                'tx_state': 'idle',
                'rx_state': 'wait for frame',
            },
            'GigabitEthernet1/0/16': {
                'tx': 'enabled',
                'rx': 'enabled',
                'tx_state': 'idle',
                'rx_state': 'wait for frame',
            },
            'GigabitEthernet1/0/17': {
                'tx': 'enabled',
                'rx': 'enabled',
                'tx_state': 'idle',
                'rx_state': 'wait for frame',
            },
            'GigabitEthernet2/0/15': {
                'tx': 'enabled',
                'rx': 'enabled',
                'tx_state': 'idle',
                'rx_state': 'wait for frame',
            },
        }        
    }

    golden_output = {'execute.return_value': '''\
        GigabitEthernet1/0/15:
            Tx: enabled
            Rx: enabled
            Tx state: IDLE
            Rx state: WAIT FOR FRAME

        GigabitEthernet1/0/16:
            Tx: enabled
            Rx: enabled
            Tx state: IDLE
            Rx state: WAIT FOR FRAME

        GigabitEthernet1/0/17:
            Tx: enabled
            Rx: enabled
            Tx state: IDLE
            Rx state: WAIT FOR FRAME

        GigabitEthernet2/0/15:
            Tx: enabled
            Rx: enabled
            Tx state: IDLE
            Rx state: WAIT FOR FRAME
    '''
    }

    def test_empty(self):
        self.dev1 = Mock(**self.empty_output)
        obj = ShowLldpInterface(device=self.dev1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden(self):
        self.maxDiff = None
        self.dev_c3850 = Mock(**self.golden_output)
        obj = ShowLldpInterface(device=self.dev_c3850)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output)


class test_show_lldp_neighbors(unittest.TestCase):
    dev1 = Device(name='empty')
    dev_c3850 = Device(name='c3850')
    empty_output = {'execute.return_value': '      '}

    # show lldp neighbors
    golden_output = {'execute.return_value': '''
        Capability codes:
            (R) Router, (B) Bridge, (T) Telephone, (C) DOCSIS Cable Device
            (W) WLAN Access Point, (P) Repeater, (S) Station, (O) Other
        
        Device ID           Local Intf     Hold-time  Capability      Port ID
        10.10.191.112       Gi1/0/44       171        B,T             7038.eeff.50a4
        10.10.191.104       Gi1/0/16       166        B,T             7038.eeff.584d
        10.10.191.93        Gi1/0/31       159        B,T             fca8.41ff.f37c
        10.10.191.91        Gi1/0/33       152        B,T             7052.c5ff.4647
        router               Gi1/0/52       117        R               Gi0/0/0
        10.10.191.107       Gi1/0/14       155        B,T             7038.eeff.572d
        d89e.f3ff.58fe      Gi1/0/33       3070                       d89e.f3ff.58fe
        6400.6aff.7d09      Gi1/0/16       2781                       6400.6aff.7d09
        
        Total entries displayed: 8
        
        switch#
        '''}

    golden_parsed_output = {
        'interfaces': {
            'GigabitEthernet1/0/14': {
                'port_id': {
                    '7038.eeff.572d': {
                        'neighbors': {
                            '10.10.191.107': {
                                'capabilities': ['B', 'T'],
                                'hold_time': 155,
                            },
                        },
                    },
                },
            },
            'GigabitEthernet1/0/16': {
                'port_id': {
                    '6400.6aff.7d09': {
                        'neighbors': {
                            '6400.6aff.7d09': {
                                'hold_time': 2781,
                            },
                        },
                    },
                    '7038.eeff.584d': {
                        'neighbors': {
                            '10.10.191.104': {
                                'capabilities': ['B', 'T'],
                                'hold_time': 166,
                            },
                        },
                    },
                },
            },
            'GigabitEthernet1/0/31': {
                'port_id': {
                    'fca8.41ff.f37c': {
                        'neighbors': {
                            '10.10.191.93': {
                                'capabilities': ['B', 'T'],
                                'hold_time': 159,
                            },
                        },
                    },
                },
            },
            'GigabitEthernet1/0/33': {
                'port_id': {
                    '7052.c5ff.4647': {
                        'neighbors': {
                            '10.10.191.91': {
                                'capabilities': ['B', 'T'],
                                'hold_time': 152,
                            },
                        },
                    },
                    'd89e.f3ff.58fe': {
                        'neighbors': {
                            'd89e.f3ff.58fe': {
                                'hold_time': 3070,
                            },
                        },
                    },
                },
            },
            'GigabitEthernet1/0/44': {
                'port_id': {
                    '7038.eeff.50a4': {
                        'neighbors': {
                            '10.10.191.112': {
                                'capabilities': ['B', 'T'],
                                'hold_time': 171,
                            },
                        },
                    },
                },
            },
            'GigabitEthernet1/0/52': {
                'port_id': {
                    'Gi0/0/0': {
                        'neighbors': {
                            'router': {
                                'capabilities': ['R'],
                                'hold_time': 117,
                            },
                        },
                    },
                },
            },
        },
        'total_entries': 8,
    }

    def test_empty(self):
        self.dev1 = Mock(**self.empty_output)
        obj = ShowLldpNeighbors(device=self.dev1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden(self):
        self.maxDiff = None
        self.dev_c3850 = Mock(**self.golden_output)
        obj = ShowLldpNeighbors(device=self.dev_c3850)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output)

if __name__ == '__main__':
    unittest.main()

