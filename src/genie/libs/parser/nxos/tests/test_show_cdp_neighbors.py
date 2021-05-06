import unittest

from unittest.mock import Mock

from pyats.topology import Device

from genie.metaparser.util.exceptions import SchemaEmptyParserError

from genie.libs.parser.nxos.show_cdp import ShowCdpNeighbors


class TestShowCdpNeighbors(unittest.TestCase):

    device = Device(name='Device')

    empty_device_output = {'execute.return_value': '''
        Device# show cdp neighbors
        Capability Codes: R - Router, T - Trans-Bridge, B - Source-Route-Bridge
                          S - Switch, H - Host, I - IGMP, r - Repeater,
                          V - VoIP-Phone, D - Remotely-Managed-Device,
                          s - Supports-STP-Dispute
        
        Device-ID          Local Intrfce  Hldtme Capability  Platform      Port ID
      '''}

    expected_parsed_output_1 = {
        'cdp': {'index': {1: {'capability': 'S I',
                              'device_id': 'sw-ff09',
                              'hold_time': 147,
                              'local_interface': 'mgmt0',
                              'platform': 'WS-C3560X-48',
                              'port_id': 'GigabitEthernet0/7'},
                          2: {'capability': 'R S s',
                              'device_id': 'duvel',
                              'hold_time': 138,
                              'local_interface': 'Ethernet1/5',
                              'platform': 'N9K-C9364D-GX',
                              'port_id': 'Ethernet1/35'},
                          3: {'capability': 'R S s',
                              'device_id': 'duvel(FDO243107WE)',
                              'hold_time': 138,
                              'local_interface': 'Ethernet1/6',
                              'platform': 'N9K-C9364D-GX',
                              'port_id': 'Ethernet1/36'},
                          4: {'capability': 'R S H',
                              'device_id': 'shkothap-lnx',
                              'hold_time': 119,
                              'local_interface': 'Ethernet1/1/1',
                              'platform': 'Linux',
                              'port_id': 'Enp2s0'},
                          5: {'capability': 'R S H',
                              'device_id': 'shkothap-lnx.cisco.com',
                              'hold_time': 119,
                              'local_interface': 'Ethernet1/1/2',
                              'platform': 'Linux',
                              'port_id': 'Enp2s1'},
                          6: {'capability': 'R S s',
                              'device_id': 'ironcity',
                              'hold_time': 177,
                              'local_interface': 'Ethernet1/30/1',
                              'platform': 'N3K-C34200YC-',
                              'port_id': 'Ethernet1/31'},
                          7: {'capability': 'R S s',
                              'device_id': 'ironcity(FOC23223HC5)',
                              'hold_time': 177,
                              'local_interface': 'Ethernet1/30/2',
                              'platform': 'N3K-C34200YC-',
                              'port_id': 'Ethernet1/32'},
                          8: {'capability': 'S',
                               'device_id': '1111-2222-3333',
                               'hold_time': 130,
                               'local_interface': 'Ethernet1/3',
                               'platform': 'HPE 2200AF-48',
                               'port_id': 'TenGigabitEthernet1/0/10'},
                           9: {'capability': 'S',
                               'device_id': '4444-5555-6666',
                               'hold_time': 125,
                               'local_interface': 'Ethernet1/5',
                               'platform': 'HPE 2200AF-48 B',
                               'port_id': 'TenGigabitEthernet2/0/20'}

                         }
               }
    }

    device_output_1 = {'execute.return_value': '''
        Device# show cdp neighbors
        Capability Codes: R - Router, T - Trans-Bridge, B - Source-Route-Bridge
                          S - Switch, H - Host, I - IGMP, r - Repeater,
                          V - VoIP-Phone, D - Remotely-Managed-Device,
                          s - Supports-STP-Dispute
        
        Device-ID          Local Intrfce  Hldtme Capability  Platform      Port ID
        sw-ff09             mgmt0          147    S I       WS-C3560X-48  Gig0/7        
        duvel               Eth1/5         138    R S s     N9K-C9364D-GX Eth1/35       
        duvel(FDO243107WE)
                            Eth1/6         138    R S s     N9K-C9364D-GX Eth1/36       
        shkothap-lnx        Eth1/1/1       119    R S H     Linux         enp2s0
        shkothap-lnx.cisco.com
                            Eth1/1/2       119    R S H     Linux         enp2s1
        ironcity            Eth1/30/1      177    R S s     N3K-C34200YC- Eth1/31       
        ironcity(FOC23223HC5)
                            Eth1/30/2      177    R S s     N3K-C34200YC- Eth1/32       
        1111-2222-3333      Eth1/3         130    S         HPE 2200AF-48
                                                               Ten-GigabitEthernet1/0/10
        4444-5555-6666      Eth1/5         125    S         HPE 2200AF-48 B
                                                               Ten-GigabitEthernet2/0/20

Total entries displayed: 9
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
