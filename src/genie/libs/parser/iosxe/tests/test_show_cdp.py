import unittest
from unittest.mock import Mock

from ats.topology import Device

from genie.metaparser.util.exceptions import SchemaEmptyParserError

from genie.libs.parser.iosxe.show_cdp import ShowCdpNeighbors, ShowCdpNeighborsDetail


class test_show_cdp_neighbors(unittest.TestCase):

    device = Device(name='aDevice')

    empty_device_output = {'execute.return_value': '''
        Device# show cdp neighbors

        Capability Codes: R - Router, T - Trans Bridge, B - Source Route Bridge
                        S - Switch, H - Host, I - IGMP, r - Repeater

        Device ID        Local Interfce     Holdtme    Capability  Platform  ''
        Port ID
      '''}

    expected_parsed_output_1 = {
        'cdp': {
            'index': {
                1: {
                    'capability': 'R B',
                    'device_id': 'R5.cisco.com',
                    'hold_time': 125,
                    'local_interface': 'GigabitEthernet0/0',
                    'platform': '',
                    'port_id': 'GigabitEthernet0/0'},
                2: {
                    'capability': 'T S',
                    'device_id': 'RX-SWV.cisco.com',
                    'hold_time': 167,
                    'local_interface': 'FastEthernet0/1',
                    'platform': 'WS-C3524-X',
                    'port_id': 'FastEthernet0/13'},
                3: {
                    'capability': 'S I',
                    'device_id': 'C2950-1',
                    'hold_time': 148,
                    'local_interface': 'FastEthernet0/0',
                    'platform': 'WS-C2950T-',
                    'port_id': 'FastEthernet0/15'}
                }
            }
        }

    device_output_1 = {'execute.return_value': '''
        Device# show cdp neighbors

        Capability Codes: R - Router, T - Trans Bridge, B - Source Route Bridge
                        S - Switch, H - Host, I - IGMP, r - Repeater

        Device ID        Local Interfce     Holdtme    Capability  Platform  ''
        Port ID

        R5.cisco.com     Gig 0/0           125              R B              Gig 0/0
        RX-SWV.cisco.com Fas 0/1            167         T S       WS-C3524-XFas 0/13
        C2950-1          Fas 0/0            148         S I       WS-C2950T-Fas 0/15
    '''}

    expected_parsed_output_2 = {
        'cdp': {
            'index': {
                1: {
                    'capability': 'R',
                    'device_id': 'device2',
                    'hold_time': 152,
                    'local_interface': 'Ethernet0',
                    'platform': 'AS5200',
                    'port_id': 'Ethernet0'},
                2: {
                    'capability': 'R',
                    'device_id': 'device3',
                    'hold_time': 144,
                    'local_interface': 'Ethernet0',
                    'platform': '3640',
                    'port_id': 'Ethernet0/0'},
                3: {
                    'capability': '',
                    'device_id': 'device4',
                    'hold_time': 141,
                    'local_interface': 'Ethernet0',
                    'platform': 'RP1',
                    'port_id': 'Ethernet0/0'}
                }
            }
        }

    device_output_2 = {'execute.return_value': '''
        Device# show cdp neighbors

        Capability Codes: R - Router, T - Trans Bridge, B - Source Route Bridge
                        S - Switch, H - Host, I - IGMP, r - Repeater

        Device ID        Local Interfce     Holdtme    Capability  Platform  ''
        Port ID

        device2      Eth 0          152      R           AS5200    Eth 0
        device3      Eth 0          144      R           3640      Eth0/0
        device4      Eth 0          141                  RP1      Eth 0/0
    '''}

    expected_parsed_output_3 = {
        'cdp': {
            'index': {
                1: {
                    'capability': 'R B',
                    'device_id': 'R8.cisco.com',
                    'hold_time': 148,
                    'local_interface': 'GigabitEthernet0/0',
                    'platform': '',
                    'port_id': 'GigabitEthernet0/0'},
                2: {
                    'capability': 'R B',
                    'device_id': 'R9.cisco.com',
                    'hold_time': 156,
                    'local_interface': 'GigabitEthernet0/0',
                    'platform': '',
                    'port_id': 'GigabitEthernet0/0'},
                3: {
                    'capability': 'R S I',
                    'device_id': 'device6',
                    'hold_time': 157,
                    'local_interface': 'GigabitEthernet0',
                    'platform': 'C887VA-W-W',
                    'port_id': 'GigabitEthernet0'}
                }
            }
        }

    device_output_3 = {'execute.return_value': '''
        Device# show cdp neighbors

        Capability Codes: R - Router, T - Trans Bridge, B - Source Route Bridge
                        S - Switch, H - Host, I - IGMP, r - Repeater

        Device ID        Local Interfce     Holdtme    Capability  Platform  ''
        Port ID

        R8.cisco.com     Gig 0/0           148              R B                     Gig 0/0
        R9.cisco.com     Gig 0/0           156              R B                     Gig 0/0
        device6          Gig 0             157              R S I       C887VA-W-W  Gi 0
    '''}

    expected_parsed_output_4 = {
        'cdp': {
            'index': {
                1: {
                    'capability': '',
                    'device_id': 'device4',
                    'hold_time': 141,
                    'local_interface': 'Ethernet0',
                    'platform': 'RP1',
                    'port_id': 'Ethernet0/0'},
                2: {
                    'capability': '',
                    'device_id': 'device5',
                    'hold_time': 164,
                    'local_interface': 'Ethernet0',
                    'platform': '7206',
                    'port_id': 'Ethernet1/0'}
                }
            }
        }

    device_output_4 = {'execute.return_value': '''
        Device# show cdp neighbors

        Capability Codes: R - Router, T - Trans Bridge, B - Source Route Bridge
                        S - Switch, H - Host, I - IGMP, r - Repeater

        Device ID        Local Interfce     Holdtme    Capability  Platform  ''
        Port ID

        device4      Eth 0          141                  RP1      Eth 0/0
        device5      Eth 0            164                  7206      Eth 1/0
    '''}

    expected_parsed_output_5 = {
        'cdp': {
            'index': {
                1: {
                    'capability': 'R S C',
                    'device_id': 'Device_With_A_Particularly_Long_Name',
                    'hold_time': 134,
                    'local_interface': 'GigabitEthernet1',
                    'platform': 'N9K-9000v',
                    'port_id': 'Ethernet0/0'}
            }
        }
    }

    device_output_5 = {'execute.return_value': '''
        Capability Codes: R - Router, T - Trans Bridge, B - Source Route Bridge
                      S - Switch, H - Host, I - IGMP, r - Repeater, P - Phone,
                      D - Remote, C - CVTA, M - Two-port Mac Relay

        Device ID        Local Intrfce     Holdtme    Capability  Platform  Port ID
        Device_With_A_Particularly_Long_Name
                         Gig 1             134             R S C  N9K-9000v Eth 0/0
    '''}

    def test_show_cdp_neighbors_1(self):
        self.maxDiff = None
        self.device = Mock(**self.device_output_1)
        obj = ShowCdpNeighbors(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.expected_parsed_output_1)

    def test_show_cdp_neighbors_2(self):
        self.maxDiff = None
        self.device = Mock(**self.device_output_2)
        obj = ShowCdpNeighbors(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.expected_parsed_output_2)

    def test_show_cdp_neighbors_3(self):
        self.maxDiff = None
        self.device = Mock(**self.device_output_3)
        obj = ShowCdpNeighbors(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.expected_parsed_output_3)

    def test_show_cdp_neighbors_4(self):
        self.maxDiff = None
        self.device = Mock(**self.device_output_4)
        obj = ShowCdpNeighbors(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.expected_parsed_output_4)

    def test_show_cdp_neighbors_5(self):
        self.maxDiff = None
        self.device = Mock(**self.device_output_5)
        obj = ShowCdpNeighbors(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.expected_parsed_output_5)

    def test_show_cdp_neighbors_empty_output(self):
        self.maxDiff = None
        self.device = Mock(**self.empty_device_output)
        obj = ShowCdpNeighbors(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()


class test_show_cdp_neighbors_detail(unittest.TestCase):
    device = Device(name='aDevice')

    expected_parsed_output_1 = {
        'total_entries_displayed': 3,
        'index': {
            1: {
                'advertisement_ver': 2,
                'capabilities': 'Router Switch CVTA phone port',
                'device_id': 'R6(9P57K4EJ8CA)',
                'duplex_mode': 'full',
                'entry_addresses': {'172.16.1.203': {}},
                'hold_time': 133,
                'local_interface': 'GigabitEthernet0/0',
                'management_addresses': {'172.16.1.203': {}},
                'native_vlan': '',
                'platform': 'N9K-9000v',
                'port_id': 'mgmt0',
                'software_version': 'Cisco Nexus Operating System (NX-OS) Software, Version 9.2(1)',
                'vtp_management_domain': ''},
            2: {
                'advertisement_ver': 2,
                'capabilities': 'Router Switch CVTA phone port',
                'device_id': 'R7(9QBDKB58F76)',
                'duplex_mode': 'full',
                'entry_addresses': {'172.16.1.204': {}},
                'hold_time': 126,
                'local_interface': 'GigabitEthernet0/0',
                'management_addresses': {'172.16.1.204': {}},
                'native_vlan': '',
                'platform': 'N9K-9000v',
                'port_id': 'mgmt0',
                'software_version': 'Cisco Nexus Operating System (NX-OS) Software, Version 9.2(1)',
                'vtp_management_domain': ''},
            3: {
                'advertisement_ver': 2,
                'capabilities': 'Router Source-Route-Bridge',
                'device_id': 'R5.cisco.com',
                'duplex_mode': '',
                'entry_addresses': {'172.16.1.202': {}},
                'hold_time': 177,
                'local_interface': 'GigabitEthernet0/0',
                'management_addresses': {'172.16.1.202': {}},
                'native_vlan': '',
                'platform': 'Cisco ',
                'port_id': 'GigabitEthernet0/0',
                'software_version': 'Cisco IOS Software, IOSv Software (VIOS-ADVENTERPRISEK9-M), Version 15.7(3)M3, RELEASE SOFTWARE (fc2)\n'
        							'Technical Support: http://www.cisco.com/techsupport\n'
        							'Copyright (c) 1986-2018 by Cisco Systems, Inc.\n'
        							'Compiled Wed 01-Aug-18 16:45 by prod_rel_team',
                'vtp_management_domain': ''},

            },
        }

    device_output_1 = {'execute.return_value': '''
        Device# show cdp neighbors detail
        Device ID: R6(9P57K4EJ8CA)
        Entry address(es):
          IP address: 172.16.1.203
        Platform: N9K-9000v,  Capabilities: Router Switch CVTA phone port
        Interface: GigabitEthernet0/0,  Port ID (outgoing port): mgmt0
        Holdtime : 133 sec

        Version :
        Cisco Nexus Operating System (NX-OS) Software, Version 9.2(1)

        advertisement version: 2
        Duplex: full
        Management address(es):
          IP address: 172.16.1.203

        -------------------------
        Device ID: R7(9QBDKB58F76)
        Entry address(es):
          IP address: 172.16.1.204
        Platform: N9K-9000v,  Capabilities: Router Switch CVTA phone port
        Interface: GigabitEthernet0/0,  Port ID (outgoing port): mgmt0
        Holdtime : 126 sec

        Version :
        Cisco Nexus Operating System (NX-OS) Software, Version 9.2(1)

        advertisement version: 2
        Duplex: full
        Management address(es):
          IP address: 172.16.1.204

        -------------------------
        Device ID: R5.cisco.com
        Entry address(es):
          IP address: 172.16.1.202
        Platform: Cisco ,  Capabilities: Router Source-Route-Bridge
        Interface: GigabitEthernet0/0,  Port ID (outgoing port): GigabitEthernet0/0
        Holdtime : 177 sec

        Version :
        Cisco IOS Software, IOSv Software (VIOS-ADVENTERPRISEK9-M), Version 15.7(3)M3, RELEASE SOFTWARE (fc2)
        Technical Support: http://www.cisco.com/techsupport
        Copyright (c) 1986-2018 by Cisco Systems, Inc.
        Compiled Wed 01-Aug-18 16:45 by prod_rel_team

        advertisement version: 2
        Management address(es):
          IP address: 172.16.1.202


        Total cdp entries displayed : 3
    '''}

    expected_parsed_output_2 = {
        'total_entries_displayed': 2,
        'index': {
                1: {
                    'advertisement_ver': 2,
                    'capabilities': 'Router Source-Route-Bridge',
                    'device_id': 'R8.cisco.com',
                    'duplex_mode': '',
                    'entry_addresses': {'172.16.1.205': {}},
                    'hold_time': 143,
                    'local_interface': 'GigabitEthernet0/0',
                    'management_addresses': {'172.16.1.205': {}},
                    'native_vlan': '',
                    'platform': 'Cisco ',
                    'port_id': 'GigabitEthernet0/0',
                    'software_version': 'Cisco IOS Software, IOSv Software (VIOS-ADVENTERPRISEK9-M), Version 15.7(3)M3, RELEASE SOFTWARE (fc2)\n'
        								'Technical Support: http://www.cisco.com/techsupport\n'
        								'Copyright (c) 1986-2018 by Cisco Systems, Inc.\n'
        								'Compiled Wed 01-Aug-18 16:45 by prod_rel_team',
                    'vtp_management_domain': ''},
                2: {
                    'advertisement_ver': 2,
                    'capabilities': 'Router Source-Route-Bridge',
                    'device_id': 'R9.cisco.com',
                    'duplex_mode': '',
                    'entry_addresses': {'172.16.1.206': {}},
                    'hold_time': 151,
                    'local_interface': 'GigabitEthernet0/0',
                    'management_addresses': {'172.16.1.206': {}},
                    'native_vlan': '',
                    'platform': 'Cisco ',
                    'port_id': 'GigabitEthernet0/0',
                     'software_version': 'Cisco IOS Software, IOSv Software (VIOS-ADVENTERPRISEK9-M), Version 15.7(3)M3, RELEASE SOFTWARE (fc2)\n'
        								 'Technical Support: http://www.cisco.com/techsupport\n'
        								 'Copyright (c) 1986-2018 by Cisco Systems, Inc.\n'
        								 'Compiled Wed 01-Aug-18 16:45 by prod_rel_team',
                    'vtp_management_domain': ''},
                },
        }

    device_output_2 = {'execute.return_value': '''
        Device# show cdp neighbors detail
        Device ID: R8.cisco.com
        Entry address(es):
          IP address: 172.16.1.205
        Platform: Cisco ,  Capabilities: Router Source-Route-Bridge
        Interface: GigabitEthernet0/0,  Port ID (outgoing port): GigabitEthernet0/0
        Holdtime : 143 sec

        Version :
        Cisco IOS Software, IOSv Software (VIOS-ADVENTERPRISEK9-M), Version 15.7(3)M3, RELEASE SOFTWARE (fc2)
        Technical Support: http://www.cisco.com/techsupport
        Copyright (c) 1986-2018 by Cisco Systems, Inc.
        Compiled Wed 01-Aug-18 16:45 by prod_rel_team

        advertisement version: 2
        Management address(es):
          IP address: 172.16.1.205

        -------------------------
        Device ID: R9.cisco.com
        Entry address(es):
          IP address: 172.16.1.206
        Platform: Cisco ,  Capabilities: Router Source-Route-Bridge
        Interface: GigabitEthernet0/0,  Port ID (outgoing port): GigabitEthernet0/0
        Holdtime : 151 sec

        Version :
        Cisco IOS Software, IOSv Software (VIOS-ADVENTERPRISEK9-M), Version 15.7(3)M3, RELEASE SOFTWARE (fc2)
        Technical Support: http://www.cisco.com/techsupport
        Copyright (c) 1986-2018 by Cisco Systems, Inc.
        Compiled Wed 01-Aug-18 16:45 by prod_rel_team

        advertisement version: 2
        Management address(es):
          IP address: 172.16.1.206

        Total cdp entries displayed : 2
    '''}

    expected_parsed_output_3 = {
        'total_entries_displayed': 1,
        'index': {
                1: {
                    'advertisement_ver': 2,
                    'capabilities': 'Router',
                    'device_id': 'device.cisco.com',
                    'duplex_mode': 'half',
                    'entry_addresses': {
                        '2001:DB8:1000:8A10::C0A8:BC06': {'type': 'global unicast'},
                        'FE80::203:E3FF:FE6A:BF81': {'type': 'link-local'},
                    },
                    'hold_time': 160,
                    'local_interface': 'Ethernet0/1',
                    'management_addresses': {},
                    'native_vlan': '42',
                    'platform': 'cisco 3640',
                    'port_id': 'Ethernet0/1',
                    'software_version': 'Cisco Internetwork Operating System Software IOS (tm) 3600 Software (C3640-A2IS-M), Version 12.2(25)SEB4, RELE)',
                    'vtp_management_domain': 'Accounting Group'},
                }
            }

    device_output_3 = {'execute.return_value': '''
        Device# show cdp neighbors detail
        Device ID: device.cisco.com
        Entry address(es):
            IPv6 address: FE80::203:E3FF:FE6A:BF81  (link-local)
            IPv6 address: 2001:DB8:1000:8A10::C0A8:BC06  (global unicast)
        Platform: cisco 3640,  Capabilities: Router
        Interface: Ethernet0/1,  Port ID (outgoing port): Ethernet0/1
        Holdtime : 160 sec
        Version :
        Cisco Internetwork Operating System Software IOS (tm) 3600 Software (C3640-A2IS-M), Version 12.2(25)SEB4, RELE)
        advertisement version: 2
        Duplex Mode: half
        Native VLAN: 42
        VTP Management Domain: ‘Accounting Group’

    '''}

    device_output_4_empty = {'execute.return_value': ''}

    expected_parsed_output_5 = {
        'total_entries_displayed': 2,
        'index': {
                1: {
                    'advertisement_ver': 2,
                    'capabilities': 'Router Switch-6506 IGMP',
                    'device_id': 'R8.cisco.com',
                    'duplex_mode': '',
                    'entry_addresses': {'172.16.1.205': {}},
                    'hold_time': 143,
                    'local_interface': 'GigabitEthernet1/0/3',
                    'management_addresses': {'172.16.1.205': {}},
                    'native_vlan': '',
                    'platform': 'cisco WS_C6506_E',
                    'port_id': 'GigabitEthernet1/0/3',
                    'software_version': 'Cisco IOS Software, IOSv Software (VIOS-ADVENTERPRISEK9-M), Version 15.7(3)M3, RELEASE SOFTWARE (fc2)\n'
                                        'Technical Support: http://www.cisco.com/techsupport\n'
                                        'Copyright (c) 1986-2018 by Cisco Systems, Inc.\n'
                                        'Compiled Wed 01-Aug-18 16:45 by prod_rel_team',
                    'vtp_management_domain': ''},
                2: {
                    'advertisement_ver': 2,
                    'capabilities': 'Router Switch_6506 IGMP',
                    'device_id': 'R9.cisco.com',
                    'duplex_mode': '',
                    'entry_addresses': {'172.16.1.206': {}},
                    'hold_time': 151,
                    'local_interface': 'GigabitEthernet1/2/5',
                    'management_addresses': {'172.16.1.206': {}},
                    'native_vlan': '',
                    'platform': 'cisco WS-C6506-E',
                    'port_id': 'GigabitEthernet1/2/5',
                     'software_version': 'Cisco IOS Software, IOSv Software (VIOS-ADVENTERPRISEK9-M), Version 15.7(3)M3, RELEASE SOFTWARE (fc2)\n'
                                         'Technical Support: http://www.cisco.com/techsupport\n'
                                         'Copyright (c) 1986-2018 by Cisco Systems, Inc.\n'
                                         'Compiled Wed 01-Aug-18 16:45 by prod_rel_team',
                    'vtp_management_domain': ''},
                },
        }

    device_output_5 = {'execute.return_value': '''
        Device# show cdp neighbors detail
        Device ID: R8.cisco.com
        Entry address(es):
          IP address: 172.16.1.205
        Platform: cisco WS_C6506_E,  Capabilities: Router Switch-6506 IGMP
        Interface: GigabitEthernet1/0/3,  Port ID (outgoing port): GigabitEthernet1/0/3
        Holdtime : 143 sec

        Version :
        Cisco IOS Software, IOSv Software (VIOS-ADVENTERPRISEK9-M), Version 15.7(3)M3, RELEASE SOFTWARE (fc2)
        Technical Support: http://www.cisco.com/techsupport
        Copyright (c) 1986-2018 by Cisco Systems, Inc.
        Compiled Wed 01-Aug-18 16:45 by prod_rel_team

        advertisement version: 2
        Management address(es):
          IP address: 172.16.1.205

        -------------------------
        Device ID: R9.cisco.com
        Entry address(es):
          IP address: 172.16.1.206
        Platform: cisco WS-C6506-E,  Capabilities: Router Switch_6506 IGMP
        Interface: GigabitEthernet1/2/5,  Port ID (outgoing port): GigabitEthernet1/2/5
        Holdtime : 151 sec

        Version :
        Cisco IOS Software, IOSv Software (VIOS-ADVENTERPRISEK9-M), Version 15.7(3)M3, RELEASE SOFTWARE (fc2)
        Technical Support: http://www.cisco.com/techsupport
        Copyright (c) 1986-2018 by Cisco Systems, Inc.
        Compiled Wed 01-Aug-18 16:45 by prod_rel_team

        advertisement version: 2
        Management address(es):
          IP address: 172.16.1.206

        Total cdp entries displayed : 2
    '''}

    def test_show_cdp_neighbors_detail_1(self):
        self.maxDiff = None
        self.device = Mock(**self.device_output_1)
        obj = ShowCdpNeighborsDetail(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.expected_parsed_output_1)

    def test_show_cdp_neighbors_detail_2(self):
        self.maxDiff = None
        self.device = Mock(**self.device_output_2)
        obj = ShowCdpNeighborsDetail(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.expected_parsed_output_2)

    def test_show_cdp_neighbors_detail_3(self):
        self.maxDiff = None
        self.device = Mock(**self.device_output_3)
        obj = ShowCdpNeighborsDetail(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.expected_parsed_output_3)

    def test_show_cdp_neighbors_detail_empty(self):
        self.maxDiff = None
        self.device = Mock(**self.device_output_4_empty)
        obj = ShowCdpNeighborsDetail(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_show_cdp_neighbors_detail_4(self):
        self.maxDiff = None
        self.device = Mock(**self.device_output_5)
        obj = ShowCdpNeighborsDetail(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.expected_parsed_output_5)

if __name__ == '__main__':
    unittest.main()
