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
                    'capability': 'R S I',
                    'device_id': 'switchB',
                    'hold_time': 177,
                    'local_interface': 'Ethernet2/3',
                    'platform': 'WS-C2960-24TC',
                    'port_id': 'Ethernet1/4'},
                2: {
                    'capability': 'R S I',
                    'device_id': 'switchA',
                    'hold_time': 120,
                    'local_interface': 'Ethernet1/4',
                    'platform': 'WS-C2960-24TC',
                    'port_id': 'Ethernet2/3'}
                    }
                }
            }

    device_output_1 = {'execute.return_value': '''
        switchA# show cdp neighbors
        Capability Codes: R - Router, T - Trans-Bridge, B - Source-Route-Bridge
            S - Switch, H - Host, I - IGMP, r - Repeater,
            V - VoIP-Phone, D - Remotely-Managed-Device,
            s - Supports-STP-Dispute
            Device ID              Local Intrfce   Hldtme  Capability  Platform      Port ID
            switchB                Ethernet2/3     177     R S I    WS-C2960-24TC Ethernet1/4
            switchA                Ethernet1/4     120     R S I    WS-C2960-24TC Ethernet2/3
    '''}

    expected_parsed_output_2 = {
        'cdp': {
            'index': {
                1: {
                    'capability': 'S I',
                    'device_id': 'Switch',
                    'hold_time': 163,
                    'local_interface': 'mgmt0',
                    'platform': 'WS-C2960-24TC',
                    'port_id': 'FastEthernet0/21'},
                2: {
                    'capability': 'R S I',
                    'device_id': 'swordfish-6k-2',
                    'hold_time': 149,
                    'local_interface': 'Ethernet3/2',
                    'platform': 'WS-C6506-E',
                    'port_id': 'GigabitEthernet1/38'}
                }
            }
        }

    device_output_2 = {'execute.return_value': '''
        switchA# show cdp neighbors
        Capability Codes:
                R - Router, T - Trans-Bridge, B - Source-Route-Bridge
                S - Switch, H - Host, I - IGMP, r - Repeater,
                V - VoIP-Phone, D - Remotely-Managed-Device,
                s - Supports-STP-Dispute
        Device ID              Local Intrfce   Hldtme  Capability  Platform      Port ID
        Switch mgmt0 163 S I WS-C2960-24TC Fas0/21
        swordfish-6k-2 Eth3/2 149 R S I WS-C6506-E Gig1/38
    '''}

    empty_device_output = {'execute.return_value': '''
        Device# show cdp neighbors
        Capability Codes:
                        R - Router, T - Trans-Bridge, B - Source-Route-Bridge
                        S - Switch, H - Host, I - IGMP, r - Repeater,
                        V - VoIP-Phone, D - Remotely-Managed-Device,
                        s - Supports-STP-Dispute
        Device ID              Local Intrfce   Hldtme  Capability  Platform      Port ID
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
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()


class test_show_cdp_neighbors_detail(unittest.TestCase):
    device = Device(name='aDevice')

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
                                   'RELEASE SOFTWARE (fc1)Copyright (c) '
                                   '1986-2007 by Cisco Systems, Inc.Compiled '
                                   'Thu 19-Jul-07 16:17 by nachen',
                'system_name': '',
                'advertisement_ver': 2,
                'vtp_management_domain': ''}},
        'total_entries_displayed': 1}

    device_output_1 = {'execute.return_value': """
        Device# show cdp neighbors detail

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
                'advertisement_ver': 2,
                'vtp_management_domain': ''}},
        'total_entries_displayed': 1
    }

    device_output_2 = {'execute.return_value': """
        Device# show cdp neighbors detail

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
                'advertisement_ver': 2,
                'vtp_management_domain': ''}},
        'total_entries_displayed': 1
    }

    device_output_3 = {'execute.return_value': """
        Device# show cdp neighbors detail

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
                'advertisement_ver': 2,
                'vtp_management_domain': ''}},
        'total_entries_displayed': 1}

    device_output_4 = {'execute.return_value': """
        Device# show cdp neighbors detail

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
                        'type': 'global unicast'},
                    '5000::CB:0:C0B8B:BCC6': {
                        'type': 'link-local'}},
                'local_interface': 'Ethernet1/29',
                'management_addresses': {
                    '192.168.0.95': {},
                    '192.168.0.96': {},
                    '192.168.0.97': {},
                    '4000::BC:0:C0A8B:BC06': {
                        'type': 'global unicast'},
                    '5000::CB:0:C0B8B:BCC6': {
                        'type': 'link-local'}},
                'native_vlan': '1',
                'physical_location': 'snmplocation',
                'platform': 'N5K-C5010P-BF',
                'port_id': 'Ethernet1',
                'software_version': 'Cisco Nexus Operating System (NX-OS) '
                                    'Software, Version 5.0(3)N2(1)',
                'system_name': 'swor95',
                'advertisement_ver': 2,
                'vtp_management_domain': ''}},
        'total_entries_displayed': 1
    }

    device_output_5 = {'execute.return_value': """
        Device# show cdp neighbors detail

        Device ID:swor95(SSI13110AAS)
        System Name:swor95
        Interface address(es):
        IPv4 Address: 192.168.0.95
        IPv6 Address: 4000::BC:0:C0A8B:BC06 (global unicast)
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
        IPv6 Address: 4000::BC:0:C0A8B:BC06 (global unicast)
        IPv6 Address: 5000::CB:0:C0B8B:BCC6 (link-local)
        IPv4 Address: 192.168.0.96
        IPv4 Address: 192.168.0.97
    """}

    device_output_empty = {'execute.return_value': """
    """}

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
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()


if __name__ == '__main__':
    unittest.main()
