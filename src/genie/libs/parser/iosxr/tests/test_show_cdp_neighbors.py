import unittest
from unittest.mock import Mock

from pyats.topology import Device

from genie.metaparser.util.exceptions import SchemaEmptyParserError

from genie.libs.parser.iosxr.show_cdp import ShowCdpNeighbors


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


if __name__ == '__main__':
    unittest.main()
