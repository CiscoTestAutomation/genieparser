import unittest
from unittest.mock import Mock

from ats.topology import Device

from genie.metaparser.util.exceptions import SchemaEmptyParserError

from genie.libs.parser.nxos.show_cdp import ShowCdpNeighbors, ShowCdpNeighborsDetail


class test_show_cdp_neighbors(unittest.TestCase):

    device = Device(name='aDevice')    

    expected_parsed_output_1 = {
        'cdp': {
            'index': {
                1: {
                    'capability': 'S I',
                    'device_id': 'C2950-1',
                    'hold_time': 148,
                    'local_interface': 'Fas 0/0',
                    'platform': 'WS-C2950T-Fas',
                    'port_id': '0/15'},
               2: {
                    'capability': 'T S',
                    'device_id': 'RX-SWV.cisco.com',
                    'hold_time': 167,
                    'local_interface': 'Fas 0/1',
                    'platform': 'WS-C3524-XFas',
                    'port_id': '0/13'},
                3: {
                    'capability': 'R',
                    'device_id': 'device2',
                    'hold_time': 152,
                    'local_interface': 'Eth 0',
                    'platform': 'AS5200',
                    'port_id': 'Eth 0'},
                4: {
                    'capability': 'R',
                    'device_id': 'device3',
                    'hold_time': 144,
                    'local_interface': 'Eth 0',
                    'platform': '3640',
                    'port_id': 'Eth0/0'},
                5: {
                    'capability': '',
                    'device_id': 'device4',
                    'hold_time': 141,
                    'local_interface': 'Eth 0',
                    'platform': 'RP1',
                    'port_id': 'Eth 0/0'}
                }
            }
        }

    expected_parsed_output_2 = {
        'cdp': {
            'index': {
                1: {
                    'capability': 'R B',
                    'device_id': 'R5.cisco.com',
                    'hold_time': 125,
                    'local_interface': 'Gig 0/0',
                    'platform': '',
                    'port_id': 'Gig 0/0'},
                2: {
                    'capability': 'R B',
                    'device_id': 'R8.cisco.com',
                    'hold_time': 148,
                    'local_interface': 'Gig 0/0',
                    'platform': '',
                    'port_id': 'Gig 0/0'},
                3: {
                    'capability': 'R B',
                    'device_id': 'R9.cisco.com',
                    'hold_time': 156,
                    'local_interface': 'Gig 0/0',
                    'platform': '',
                    'port_id': 'Gig 0/0'},
                4: {
                    'capability': 'R S I',
                    'device_id': 'device6',
                    'hold_time': 157,
                    'local_interface': 'Gig 0',
                    'platform': 'C887VA-W-',
                    'port_id': 'WGi 0'}
                }
            }
        }


    expected_parsed_empty_output = {
        'cdp': {}
    }

    empty_device_output = {'execute.return_value': '''
        Device# show cdp neighbors

        Capability Codes: R - Router, T - Trans Bridge, B - Source Route Bridge
                        S - Switch, H - Host, I - IGMP, r - Repeater

        Device ID        Local Interfce     Holdtme    Capability  Platform  ''
        Port ID
      '''}

    device_output_1 = {'execute.return_value': '''
        Device# show cdp neighbors

        Capability Codes: R - Router, T - Trans Bridge, B - Source Route Bridge
                        S - Switch, H - Host, I - IGMP, r - Repeater

        Device ID        Local Interfce     Holdtme    Capability  ''
        Platform  Port ID

        C2950-1          Fas 0/0            148         S I       WS-C2950T-Fas 0/15
        RX-SWV.cisco.com Fas 0/1            167         T S       WS-C3524-XFas 0/13    
        device2      Eth 0          152      R           AS5200    Eth 0
        device3      Eth 0          144      R           3640      Eth0/0
        device4      Eth 0          141                  RP1      Eth 0/0        
    '''}

    device_output_2 = {'execute.return_value': '''
        Device# show cdp neighbors

        Capability Codes: R - Router, T - Trans Bridge, B - Source Route Bridge
                        S - Switch, H - Host, I - IGMP, r - Repeater

        Device ID        Local Interfce     Holdtme    Capability  ''
        Platform  Port ID
 
        R5.cisco.com     Gig 0/0           125              R B             Gig 0/0
        R8.cisco.com     Gig 0/0           148              R B             Gig 0/0
        R9.cisco.com     Gig 0/0           156              R B             Gig 0/0
        device6    Gig 0          157      R S I       C887VA-W- WGi 0
    
    '''}


    device_output_3 = {'execute.return_value': '''
        Device# show cdp neighbors

        Capability Codes: R - Router, T - Trans Bridge, B - Source Route Bridge
                        S - Switch, H - Host, I - IGMP, r - Repeater

        Device ID        Local Interfce     Holdtme    Capability  ''
        Platform  Port ID
        
        device4      Eth 0          141                  RP1      Eth 0/0
        device5      Eth 0            164                  7206      Eth 1/0
        R6(9P57K4EJ8CA)  Gig 0/0           137             R S C  N9K-9000v mgmt0
        R7(9QBDKB58F76)  Gig 0/0           130             R S C  N9K-9000v mgmt0
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

    def test_show_cdp_neighbors_empty_output(self):
        self.maxDiff = None
        self.device = Mock(**self.empty_device_output)
        obj = ShowCdpNeighbors(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.expected_parsed_empty_output)


class test_show_cdp_neighbors_detail(unittest.TestCase):
    device = Device(name='aDevice')


    expected_parsed_output_empty = {
        'total_entries_displayed': 0
    }

    expected_parsed_output_1 = {
        'index': {
            1: {'capabilities': 'Switch IGMP Filtering',
                'device_id': 'savbu-qa-dist-120',
                'duplex_mode': 'full',
                'hold_time': 128,
                'interface_addresses': {
                    '192.168.0.82': {}},
                'local_interface': 'mgmt0',
                'management_addresses': {
                    '192.168.0.82': {}},
                'native_vlan': '16',
                'physical_location': '',
                'platform': 'cisco WS-C3750E-24TD',
                'port_id': 'GigabitEthernet1',
                'software_version': 'Cisco IOS Software, C3750E Software '
                                    '(C3750E-UNIVERSAL-M), Version 12.2(35)SE5, '
                                    'RELEASE SOFTWARE (fc1)',
                'system_name': '',
                'vtp_mng_domain': ''}},
        'total_entries_displayed': 1}

    expected_parsed_output_2 = {
        'index': {
            1: {'capabilities': 'Switch IGMP Filtering Supports-STP-Disput',
                'device_id': 'swor96(SSI13110AAQ)',
                'duplex_mode': 'full',
                'hold_time': 175,
                'interface_addresses': {
                    '192.168.0.1': {}},
                'local_interface': 'Ethernet1/17',
                'management_addresses': {
                    '192.168.0.96': {}},
                'native_vlan': '1',
                'physical_location': 'snmplocation',
                'platform': 'N5K-C5010P-BF',
                'port_id': 'Ethernet1',
                'software_version': 'Cisco Nexus Operating System (NX-OS) '
                                   'Software, Version 5.0(3)N2(1)',
               'system_name': 'swor96',
               'vtp_mng_domain': ''}},
        'total_entries_displayed': 1
    }

    expected_parsed_output_3 = {
        'index': {
            1: {'capabilities': 'Switch IGMP Filtering Supports-STP-Disput',
                'device_id': 'swor96(SSI13110AAQ)',
                'duplex_mode': 'full',
                'hold_time': 175,
                'interface_addresses': {'192.168.0.1': {}},
                'local_interface': 'Ethernet1/18',
                'management_addresses': {'192.168.0.96': {}},
                'native_vlan': '1',
                'physical_location': 'snmplocation',
                'platform': 'N5K-C5010P-BF',
                'port_id': 'Ethernet1',
                'software_version': 'Cisco Nexus Operating System (NX-OS) '
                                    'Software, Version 5.0(3)N2(1)',
                'system_name': 'swor96',
                'vtp_mng_domain': ''}},
        'total_entries_displayed': 1
    }

    expected_parsed_output_4 = {
        'index': {
            1: {'capabilities': 'Switch IGMP Filtering Supports-STP-Dispute',
                'device_id': 'swor95(SSI13110AAS)',
                'duplex_mode': 'full',
                'hold_time': 121,
                'interface_addresses': {'192.168.0.95': {}},
                'local_interface': 'Ethernet1/29',
                'management_addresses': {'192.168.0.95': {}},
                'native_vlan': '1',
                'physical_location': 'snmplocation',
                'platform': 'N5K-C5010P-BF',
                'port_id': 'Ethernet1',
                'software_version': 'Cisco Nexus Operating System (NX-OS) '
                                    'Software, Version 5.0(3)N2(1)',
                'system_name': 'swor95',
                'vtp_mng_domain': ''}},
        'total_entries_displayed': 1}

    expected_parsed_output_5 = {
        'index': {
            1: {'capabilities': 'Switch IGMP Filtering Supports-STP-Dispute',
                'device_id': 'swor95(SSI13110AAS)',
                'duplex_mode': 'full',
                'hold_time': 121,
                'interface_addresses': {
                    '192.168.0.95': {},
                    '192.168.0.96': {},
                    '192.168.0.97': {},
                    '4000::BC:0:C0A8B:BC06': {
                        'type': 'global unicats'},
                    '5000::CB:0:C0B8B:BCC6': {
                        'type': 'link-local'}},
                'local_interface': 'Ethernet1/29',
                'management_addresses': {
                    '192.168.0.95': {},
                    '192.168.0.96': {},
                    '192.168.0.97': {},
                    '4000::BC:0:C0A8B:BC06': {
                        'type': 'global unicats'},
                    '5000::CB:0:C0B8B:BCC6': {
                        'type': 'link-local'}},
                'native_vlan': '1',
                'physical_location': 'snmplocation',
                'platform': 'N5K-C5010P-BF',
                'port_id': 'Ethernet1',
                'software_version': 'Cisco Nexus Operating System (NX-OS) '
                                    'Software, Version 5.0(3)N2(1)',
                'system_name': 'swor95',
                'vtp_mng_domain': ''}},
        'total_entries_displayed': 1
    }

    device_output_empty = {'execute.return_value': """
    """}


    device_output_1 = {'execute.return_value': """
        Device ID:savbu-qa-dist-120
        System Name:
        Interface address(es):
        IPv4 Address: 192.168.0.82
        Platform: cisco WS-C3750E-24TD, Capabilities: Switch IGMP Filtering
        Interface: mgmt0, Port ID (outgoing port): GigabitEthernet1/0/13
        Holdtime: 128 sec

        Version:
        Cisco IOS Software, C3750E Software (C3750E-UNIVERSAL-M), Version 12.2(35)SE5, RELEASE SOFTWARE (fc1)
        Copyright (c) 1986-2007 by Cisco Systems, Inc.
        Compiled Thu 19-Jul-07 16:17 by nachen

        Advertisement Version: 2
        Native VLAN: 16
        VTP Management Domain:
        Duplex: full
        Mgmt address(es):
        IPv4 Address: 192.168.0.82

    """}

    device_output_2 = {'execute.return_value': """
        Device ID:swor96(SSI13110AAQ)
        System Name:swor96
        Interface address(es):
        IPv4 Address: 192.168.0.1
        Platform: N5K-C5010P-BF, Capabilities: Switch IGMP Filtering Supports-STP-Disput
        e
        Interface: Ethernet1/17, Port ID (outgoing port): Ethernet1/19
        Holdtime: 175 sec

        Version:
        Cisco Nexus Operating System (NX-OS) Software, Version 5.0(3)N2(1)

        Advertisement Version: 2
        Native VLAN: 1
        Duplex: full
        Physical Location: snmplocation
        Mgmt address(es):
        IPv4 Address: 192.168.0.96
    """}
 
    device_output_3 = {'execute.return_value': """
        Device ID:swor96(SSI13110AAQ)
        System Name:swor96
        Interface address(es):
        IPv4 Address: 192.168.0.1
        Platform: N5K-C5010P-BF, Capabilities: Switch IGMP Filtering Supports-STP-Disput
        e
        Interface: Ethernet1/18, Port ID (outgoing port): Ethernet1/20
        Holdtime: 175 sec

        Version:
        Cisco Nexus Operating System (NX-OS) Software, Version 5.0(3)N2(1)

        Advertisement Version: 2
        Native VLAN: 1
        Duplex: full
        Physical Location: snmplocation
        Mgmt address(es):
        IPv4 Address: 192.168.0.96
    """}
 
    device_output_4 = {'execute.return_value': """
        Device ID:swor95(SSI13110AAS)
        System Name:swor95
        Interface address(es):
        IPv4 Address: 192.168.0.95
        Platform: N5K-C5010P-BF, Capabilities: Switch IGMP Filtering Supports-STP-Dispute
        Interface: Ethernet1/29, Port ID (outgoing port): Ethernet1/19
        Holdtime: 121 sec

        Version:
        Cisco Nexus Operating System (NX-OS) Software, Version 5.0(3)N2(1)

        Advertisement Version: 2
        Native VLAN: 1
        Duplex: full
        Physical Location: snmplocation
        Mgmt address(es):
        IPv4 Address: 192.168.0.95 
    """}

    device_output_5 = {'execute.return_value': """
        Device ID:swor95(SSI13110AAS)
        System Name:swor95
        Interface address(es):
        IPv4 Address: 192.168.0.95
        IPv6 Address: 4000::BC:0:C0A8B:BC06 (global unicats)
        IPv6 Address: 5000::CB:0:C0B8B:BCC6 (link-local)
        IPv4 Address: 192.168.0.96
        IPv4 Address: 192.168.0.97
        Platform: N5K-C5010P-BF, Capabilities: Switch IGMP Filtering Supports-STP-Dispute
        Interface: Ethernet1/29, Port ID (outgoing port): Ethernet1/19
        Holdtime: 121 sec

        Version:
        Cisco Nexus Operating System (NX-OS) Software, Version 5.0(3)N2(1)

        Advertisement Version: 2
        Native VLAN: 1
        Duplex: full
        Physical Location: snmplocation
        Mgmt address(es):
        IPv4 Address: 192.168.0.95
        IPv6 Address: 4000::BC:0:C0A8B:BC06 (global unicats)
        IPv6 Address: 5000::CB:0:C0B8B:BCC6 (link-local)
        IPv4 Address: 192.168.0.96
        IPv4 Address: 192.168.0.97
    """}

    def test_show_cdp_neighbors_detail_1(self):
        self.maxDiff = None
        self.device = Mock(**self.device_output_1)
        obj = ShowCdpNeighborsDetail(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.expected_parsed_output_1)

    def test_show_cdp_neighbors_detail_2(self ):
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

    def test_show_cdp_neighbors_detail_4(self):
        self.maxDiff = None
        self.device = Mock(**self.device_output_4)
        obj = ShowCdpNeighborsDetail(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.expected_parsed_output_4)

    def test_show_cdp_neighbors_detail_5(self):
        self.maxDiff = None
        self.device = Mock(**self.device_output_5)
        obj = ShowCdpNeighborsDetail(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.expected_parsed_output_5)

    def test_show_cdp_neighbors_detail_empty(self):
        self.maxDiff = None
        self.device = Mock(**self.device_output_empty)
        obj = ShowCdpNeighborsDetail(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.expected_parsed_output_empty)

if __name__ == '__main__':
    unittest.main()