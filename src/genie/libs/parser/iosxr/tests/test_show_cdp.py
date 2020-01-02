import unittest
from unittest.mock import Mock

from pyats.topology import Device

from genie.metaparser.util.exceptions import SchemaEmptyParserError

from genie.libs.parser.iosxr.show_cdp import ShowCdpNeighbors, ShowCdpNeighborsDetail


class TestShowCdpNeighbors(unittest.TestCase):

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
                    'capability': 'R I',
                    'device_id': 'R1_xe.cisco.com',
                    'hold_time': 135,
                    'local_interface': 'GigabitEthernet0/0/0/0',
                    'platform': 'CSR1000V',
                    'port_id': 'GigabitEthernet2'},
                2: {
                    'capability': 'R S I',
                    'device_id': 'R3_nx.cisco.com',
                    'hold_time': 163,
                    'local_interface': 'GigabitEthernet0/0/0/5',
                    'platform': 'N9K-9000v',
                    'port_id': 'Ethernet1/4'},
                3: {
                    'capability': 'R S I',
                    'device_id': 'R3_nx.cisco.com',
                    'hold_time': 163,
                    'local_interface': 'GigabitEthernet0/0/0/4',
                    'platform': 'N9K-9000v',
                    'port_id': 'Ethernet1/3'},
                4: {
                    'capability': 'R I',
                    'device_id': 'R1_xe.cisco.com',
                    'hold_time': 161,
                    'local_interface': 'GigabitEthernet0/0/0/3',
                    'platform': 'CSR1000V',
                    'port_id': 'GigabitEthernet5'},
                5: {
                    'capability': 'R I',
                    'device_id': 'R1_xe.cisco.com',
                    'hold_time': 177,
                    'local_interface': 'GigabitEthernet0/0/0/2',
                    'platform': 'CSR1000V',
                    'port_id': 'GigabitEthernet4'},
                6: {
                    'capability': 'R S',
                    'device_id': 'R3_nx.cisco.com',
                    'hold_time': 151,
                    'local_interface': 'GigabitEthernet0/0/0/1',
                    'platform': 'N9K-9000v',
                    'port_id': 'Ethernet1/1'},
            }
        }
    }

    device_output_1 = {'execute.return_value': '''
        Device# show cdp neighbors

        Capability Codes: R - Router, T - Trans Bridge, B - Source Route Bridge
                        S - Switch, H - Host, I - IGMP, r - Repeater

        Device ID       Local Intrfce    Holdtme Capability Platform  Port ID
        R1_xe.cisco.com Gi0/0/0/0        135     R I        CSR1000V  Gi2
        R3_nx.cisco.com Gi0/0/0/5        163     R S I      N9K-9000v Et1/4
        R3_nx.cisco.com Gi0/0/0/4        163     R S I      N9K-9000v Et1/3
        R1_xe.cisco.com Gi0/0/0/3        161     R I        CSR1000V  Gi5
        R1_xe.cisco.com Gi0/0/0/2        177     R I        CSR1000V  Gi4
        R3_nx.cisco.com Gi0/0/0/1        151     R S        N9K-9000v Et1/1
    '''}

    @classmethod
    def setUpClass(cls):
        cls.maxDiff = None

    def test_show_cdp_neighbors_1(self):

        self.device = Mock(**self.device_output_1)
        obj = ShowCdpNeighbors(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.expected_parsed_output_1)

    def test_show_cdp_neighbors_empty_output(self):

        self.device = Mock(**self.empty_device_output)
        obj = ShowCdpNeighbors(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()


class TestShowCdpNeighborsDetail(unittest.TestCase):

    device = Device(name='aDevice')

    expected_parsed_output_1 = {
        'index': {
            1: {'capabilities': 'Router Switch IGMP',
                'device_id': 'R3_nx.cisco.com(972ZZK4REQK)',
                'duplex_mode': 'full',
                'hold_time': 138,
                'entry_addresses': {
                    '172.16.1.53': {}},
                'native_vlan': '1',
                'platform': 'N9K-9000v',
                'local_interface': 'GigabitEthernet0/0/0/5',
                'port_id': 'Ethernet1/4',
                'software_version': 'Cisco Nexus Operating System (NX-OS) Software, Version 9.2(1)',
                'system_name': 'R3_nx',
                'advertisement_ver': 2,
                }},
        'total_entries_displayed': 1}

    device_output_1 = {'execute.return_value': """
        Device# show cdp neighbors detail

        Device ID: R3_nx.cisco.com(972ZZK4REQK)
        SysName : R3_nx
        Entry address(es):
          IPv4 address: 172.16.1.53
        Platform: N9K-9000v,  Capabilities: Router Switch IGMP
        Interface: GigabitEthernet0/0/0/5
        Port ID (outgoing port): Ethernet1/4
        Holdtime : 138 sec

        Version :
        Cisco Nexus Operating System (NX-OS) Software, Version 9.2(1)

        advertisement version: 2
        Native VLAN: 1
        Duplex: full


    """}

    def test_show_cdp_neighbors_detail_1(self):
        self.maxDiff = None
        self.device = Mock(**self.device_output_1)
        obj = ShowCdpNeighborsDetail(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.expected_parsed_output_1)


if __name__ == '__main__':
    unittest.main()
