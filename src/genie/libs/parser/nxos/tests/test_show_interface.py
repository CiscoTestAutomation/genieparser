# Python
import unittest
from unittest.mock import Mock

from pyats.topology import Device

# Genie
from genie.metaparser.util.exceptions import SchemaEmptyParserError, SchemaMissingKeyError

from genie.libs.parser.nxos.show_interface import (ShowInterface,
                                                   ShowVrfAllInterface,
                                                   ShowInterfaceSwitchport,
                                                   ShowIpv6InterfaceVrfAll,
                                                   ShowIpInterfaceVrfAll,
                                                   ShowIpInterfaceBrief,
                                                   ShowIpInterfaceBriefPipeVlan,
                                                   ShowInterfaceBrief,
                                                   ShowRunningConfigInterface,
                                                   ShowNveInterface,
                                                   ShowIpInterfaceBriefVrfAll,
                                                   ShowInterfaceDescription,
                                                   ShowInterfaceStatus,
                                                   ShowInterfaceCapabilities,
                                                   ShowInterfaceTransceiver,
                                                   ShowInterfaceTransceiverDetails,
                                                   ShowInterfaceFec,
                                                   ShowInterfaceHardwareMap)


# #############################################################################
# # Unittest For Show Vrf All Interface
# #############################################################################

class TestShowVrfAllInterface(unittest.TestCase):
    device = Device(name='aDevice')
    device0 = Device(name='bDevice')
    empty_output = {'execute.return_value': ''}
    golden_parsed_output = {
        'Ethernet2/1': {'site_of_origin': '--', 'vrf': 'VRF1', 'vrf_id': 3},
        'Ethernet2/1.10': {'site_of_origin': '--', 'vrf': 'default', 'vrf_id': 1},
        'Ethernet2/1.20': {'site_of_origin': '--', 'vrf': 'default', 'vrf_id': 1},
        'Ethernet2/10': {'site_of_origin': '--', 'vrf': 'default', 'vrf_id': 1},
        'Ethernet2/11': {'site_of_origin': '--', 'vrf': 'default', 'vrf_id': 1},
        'Ethernet2/12': {'site_of_origin': '--', 'vrf': 'default', 'vrf_id': 1},
        'Ethernet2/13': {'site_of_origin': '--', 'vrf': 'default', 'vrf_id': 1},
        'Ethernet2/14': {'site_of_origin': '--', 'vrf': 'default', 'vrf_id': 1},
        'Ethernet2/15': {'site_of_origin': '--', 'vrf': 'default', 'vrf_id': 1},
        'Ethernet2/16': {'site_of_origin': '--', 'vrf': 'default', 'vrf_id': 1},
        'Ethernet2/17': {'site_of_origin': '--', 'vrf': 'default', 'vrf_id': 1},
        'Ethernet2/18': {'site_of_origin': '--', 'vrf': 'default', 'vrf_id': 1},
        'Ethernet2/19': {'site_of_origin': '--', 'vrf': 'default', 'vrf_id': 1},
        'Ethernet2/20': {'site_of_origin': '--', 'vrf': 'default', 'vrf_id': 1},
        'Ethernet2/21': {'site_of_origin': '--', 'vrf': 'default', 'vrf_id': 1},
        'Ethernet2/22': {'site_of_origin': '--', 'vrf': 'default', 'vrf_id': 1},
        'Ethernet2/23': {'site_of_origin': '--', 'vrf': 'default', 'vrf_id': 1},
        'Ethernet2/24': {'site_of_origin': '--', 'vrf': 'default', 'vrf_id': 1},
        'Ethernet2/25': {'site_of_origin': '--', 'vrf': 'default', 'vrf_id': 1},
        'Ethernet2/26': {'site_of_origin': '--', 'vrf': 'default', 'vrf_id': 1},
        'Ethernet2/27': {'site_of_origin': '--', 'vrf': 'default', 'vrf_id': 1},
        'Ethernet2/28': {'site_of_origin': '--', 'vrf': 'default', 'vrf_id': 1},
        'Ethernet2/29': {'site_of_origin': '--', 'vrf': 'default', 'vrf_id': 1},
        'Ethernet2/30': {'site_of_origin': '--', 'vrf': 'default', 'vrf_id': 1},
        'Ethernet2/31': {'site_of_origin': '--', 'vrf': 'default', 'vrf_id': 1},
        'Ethernet2/32': {'site_of_origin': '--', 'vrf': 'default', 'vrf_id': 1},
        'Ethernet2/33': {'site_of_origin': '--', 'vrf': 'default', 'vrf_id': 1},
        'Ethernet2/34': {'site_of_origin': '--', 'vrf': 'default', 'vrf_id': 1},
        'Ethernet2/35': {'site_of_origin': '--', 'vrf': 'default', 'vrf_id': 1},
        'Ethernet2/36': {'site_of_origin': '--', 'vrf': 'default', 'vrf_id': 1},
        'Ethernet2/37': {'site_of_origin': '--', 'vrf': 'default', 'vrf_id': 1},
        'Ethernet2/38': {'site_of_origin': '--', 'vrf': 'default', 'vrf_id': 1},
        'Ethernet2/39': {'site_of_origin': '--', 'vrf': 'default', 'vrf_id': 1},
        'Ethernet2/4': {'site_of_origin': '--', 'vrf': 'default', 'vrf_id': 1},
        'Ethernet2/40': {'site_of_origin': '--', 'vrf': 'default', 'vrf_id': 1},
        'Ethernet2/41': {'site_of_origin': '--', 'vrf': 'default', 'vrf_id': 1},
        'Ethernet2/42': {'site_of_origin': '--', 'vrf': 'default', 'vrf_id': 1},
        'Ethernet2/43': {'site_of_origin': '--', 'vrf': 'default', 'vrf_id': 1},
        'Ethernet2/44': {'site_of_origin': '--', 'vrf': 'default', 'vrf_id': 1},
        'Ethernet2/45': {'site_of_origin': '--', 'vrf': 'default', 'vrf_id': 1},
        'Ethernet2/46': {'site_of_origin': '--', 'vrf': 'default', 'vrf_id': 1},
        'Ethernet2/47': {'site_of_origin': '--', 'vrf': 'default', 'vrf_id': 1},
        'Ethernet2/48': {'site_of_origin': '--', 'vrf': 'default', 'vrf_id': 1},
        'Ethernet2/5': {'site_of_origin': '--', 'vrf': 'default', 'vrf_id': 1},
        'Ethernet2/6': {'site_of_origin': '--', 'vrf': 'default', 'vrf_id': 1},
        'Ethernet2/7': {'site_of_origin': '--', 'vrf': 'default', 'vrf_id': 1},
        'Ethernet2/8': {'site_of_origin': '--', 'vrf': 'default', 'vrf_id': 1},
        'Ethernet2/9': {'site_of_origin': '--', 'vrf': 'default', 'vrf_id': 1},
        'Ethernet3/1': {'site_of_origin': '--', 'vrf': 'default', 'vrf_id': 1},
        'Ethernet3/10': {'site_of_origin': '--', 'vrf': 'default', 'vrf_id': 1},
        'Ethernet3/11': {'site_of_origin': '--', 'vrf': 'default', 'vrf_id': 1},
        'Ethernet3/12': {'site_of_origin': '--', 'vrf': 'default', 'vrf_id': 1},
        'Ethernet3/13': {'site_of_origin': '--', 'vrf': 'default', 'vrf_id': 1},
        'Ethernet3/14': {'site_of_origin': '--', 'vrf': 'default', 'vrf_id': 1},
        'Ethernet3/15': {'site_of_origin': '--', 'vrf': 'default', 'vrf_id': 1},
        'Ethernet3/16': {'site_of_origin': '--', 'vrf': 'default', 'vrf_id': 1},
        'Ethernet3/17': {'site_of_origin': '--', 'vrf': 'default', 'vrf_id': 1},
        'Ethernet3/18': {'site_of_origin': '--', 'vrf': 'default', 'vrf_id': 1},
        'Ethernet3/19': {'site_of_origin': '--', 'vrf': 'default', 'vrf_id': 1},
        'Ethernet3/2': {'site_of_origin': '--', 'vrf': 'default', 'vrf_id': 1},
        'Ethernet3/20': {'site_of_origin': '--', 'vrf': 'default', 'vrf_id': 1},
        'Ethernet3/21': {'site_of_origin': '--', 'vrf': 'default', 'vrf_id': 1},
        'Ethernet3/22': {'site_of_origin': '--', 'vrf': 'default', 'vrf_id': 1},
        'Ethernet3/23': {'site_of_origin': '--', 'vrf': 'default', 'vrf_id': 1},
        'Ethernet3/24': {'site_of_origin': '--', 'vrf': 'default', 'vrf_id': 1},
        'Ethernet3/25': {'site_of_origin': '--', 'vrf': 'default', 'vrf_id': 1},
        'Ethernet3/26': {'site_of_origin': '--', 'vrf': 'default', 'vrf_id': 1},
        'Ethernet3/27': {'site_of_origin': '--', 'vrf': 'default', 'vrf_id': 1},
        'Ethernet3/28': {'site_of_origin': '--', 'vrf': 'default', 'vrf_id': 1},
        'Ethernet3/29': {'site_of_origin': '--', 'vrf': 'default', 'vrf_id': 1},
        'Ethernet3/3': {'site_of_origin': '--', 'vrf': 'default', 'vrf_id': 1},
        'Ethernet3/30': {'site_of_origin': '--', 'vrf': 'default', 'vrf_id': 1},
        'Ethernet3/31': {'site_of_origin': '--', 'vrf': 'default', 'vrf_id': 1},
        'Ethernet3/32': {'site_of_origin': '--', 'vrf': 'default', 'vrf_id': 1},
        'Ethernet3/33': {'site_of_origin': '--', 'vrf': 'default', 'vrf_id': 1},
        'Ethernet3/34': {'site_of_origin': '--', 'vrf': 'default', 'vrf_id': 1},
        'Ethernet3/35': {'site_of_origin': '--', 'vrf': 'default', 'vrf_id': 1},
        'Ethernet3/36': {'site_of_origin': '--', 'vrf': 'default', 'vrf_id': 1},
        'Ethernet3/37': {'site_of_origin': '--', 'vrf': 'default', 'vrf_id': 1},
        'Ethernet3/38': {'site_of_origin': '--', 'vrf': 'default', 'vrf_id': 1},
        'Ethernet3/39': {'site_of_origin': '--', 'vrf': 'default', 'vrf_id': 1},
        'Ethernet3/4': {'site_of_origin': '--', 'vrf': 'default', 'vrf_id': 1},
        'Ethernet3/40': {'site_of_origin': '--', 'vrf': 'default', 'vrf_id': 1},
        'Ethernet3/41': {'site_of_origin': '--', 'vrf': 'default', 'vrf_id': 1},
        'Ethernet3/42': {'site_of_origin': '--', 'vrf': 'default', 'vrf_id': 1},
        'Ethernet3/43': {'site_of_origin': '--', 'vrf': 'default', 'vrf_id': 1},
        'Ethernet3/44': {'site_of_origin': '--', 'vrf': 'default', 'vrf_id': 1},
        'Ethernet3/45': {'site_of_origin': '--', 'vrf': 'default', 'vrf_id': 1},
        'Ethernet3/46': {'site_of_origin': '--', 'vrf': 'default', 'vrf_id': 1},
        'Ethernet3/47': {'site_of_origin': '--', 'vrf': 'default', 'vrf_id': 1},
        'Ethernet3/48': {'site_of_origin': '--', 'vrf': 'default', 'vrf_id': 1},
        'Ethernet3/5': {'site_of_origin': '--', 'vrf': 'default', 'vrf_id': 1},
        'Ethernet3/6': {'site_of_origin': '--', 'vrf': 'default', 'vrf_id': 1},
        'Ethernet3/7': {'site_of_origin': '--', 'vrf': 'default', 'vrf_id': 1},
        'Ethernet3/8': {'site_of_origin': '--', 'vrf': 'default', 'vrf_id': 1},
        'Ethernet3/9': {'site_of_origin': '--', 'vrf': 'default', 'vrf_id': 1},
        'Ethernet4/1': {'site_of_origin': '--', 'vrf': 'default', 'vrf_id': 1},
        'Ethernet4/10': {'site_of_origin': '--', 'vrf': 'default', 'vrf_id': 1},
        'Ethernet4/11': {'site_of_origin': '--', 'vrf': 'default', 'vrf_id': 1},
        'Ethernet4/12': {'site_of_origin': '--', 'vrf': 'default', 'vrf_id': 1},
        'Ethernet4/13': {'site_of_origin': '--', 'vrf': 'default', 'vrf_id': 1},
        'Ethernet4/14': {'site_of_origin': '--', 'vrf': 'default', 'vrf_id': 1},
        'Ethernet4/15': {'site_of_origin': '--', 'vrf': 'default', 'vrf_id': 1},
        'Ethernet4/16': {'site_of_origin': '--', 'vrf': 'default', 'vrf_id': 1},
        'Ethernet4/17': {'site_of_origin': '--', 'vrf': 'default', 'vrf_id': 1},
        'Ethernet4/18': {'site_of_origin': '--', 'vrf': 'default', 'vrf_id': 1},
        'Ethernet4/19': {'site_of_origin': '--', 'vrf': 'default', 'vrf_id': 1},
        'Ethernet4/2': {'site_of_origin': '--', 'vrf': 'default', 'vrf_id': 1},
        'Ethernet4/20': {'site_of_origin': '--', 'vrf': 'default', 'vrf_id': 1},
        'Ethernet4/21': {'site_of_origin': '--', 'vrf': 'default', 'vrf_id': 1},
        'Ethernet4/22': {'site_of_origin': '--', 'vrf': 'default', 'vrf_id': 1},
        'Ethernet4/23': {'site_of_origin': '--', 'vrf': 'default', 'vrf_id': 1},
        'Ethernet4/24': {'site_of_origin': '--', 'vrf': 'default', 'vrf_id': 1},
        'Ethernet4/25': {'site_of_origin': '--', 'vrf': 'default', 'vrf_id': 1},
        'Ethernet4/26': {'site_of_origin': '--', 'vrf': 'default', 'vrf_id': 1},
        'Ethernet4/27': {'site_of_origin': '--', 'vrf': 'default', 'vrf_id': 1},
        'Ethernet4/28': {'site_of_origin': '--', 'vrf': 'default', 'vrf_id': 1},
        'Ethernet4/29': {'site_of_origin': '--', 'vrf': 'default', 'vrf_id': 1},
        'Ethernet4/3': {'site_of_origin': '--', 'vrf': 'default', 'vrf_id': 1},
        'Ethernet4/30': {'site_of_origin': '--', 'vrf': 'default', 'vrf_id': 1},
        'Ethernet4/31': {'site_of_origin': '--', 'vrf': 'default', 'vrf_id': 1},
        'Ethernet4/32': {'site_of_origin': '--', 'vrf': 'default', 'vrf_id': 1},
        'Ethernet4/33': {'site_of_origin': '--', 'vrf': 'default', 'vrf_id': 1},
        'Ethernet4/34': {'site_of_origin': '--', 'vrf': 'default', 'vrf_id': 1},
        'Ethernet4/35': {'site_of_origin': '--', 'vrf': 'default', 'vrf_id': 1},
        'Ethernet4/36': {'site_of_origin': '--', 'vrf': 'default', 'vrf_id': 1},
        'Ethernet4/37': {'site_of_origin': '--', 'vrf': 'default', 'vrf_id': 1},
        'Ethernet4/38': {'site_of_origin': '--', 'vrf': 'default', 'vrf_id': 1},
        'Ethernet4/39': {'site_of_origin': '--', 'vrf': 'default', 'vrf_id': 1},
        'Ethernet4/4': {'site_of_origin': '--', 'vrf': 'default', 'vrf_id': 1},
        'Ethernet4/40': {'site_of_origin': '--', 'vrf': 'default', 'vrf_id': 1},
        'Ethernet4/41': {'site_of_origin': '--', 'vrf': 'default', 'vrf_id': 1},
        'Ethernet4/42': {'site_of_origin': '--', 'vrf': 'default', 'vrf_id': 1},
        'Ethernet4/43': {'site_of_origin': '--', 'vrf': 'default', 'vrf_id': 1},
        'Ethernet4/44': {'site_of_origin': '--', 'vrf': 'default', 'vrf_id': 1},
        'Ethernet4/45': {'site_of_origin': '--', 'vrf': 'default', 'vrf_id': 1},
        'Ethernet4/46': {'site_of_origin': '--', 'vrf': 'default', 'vrf_id': 1},
        'Ethernet4/47': {'site_of_origin': '--', 'vrf': 'default', 'vrf_id': 1},
        'Ethernet4/48': {'site_of_origin': '--', 'vrf': 'default', 'vrf_id': 1},
        'Ethernet4/5': {'site_of_origin': '--', 'vrf': 'default', 'vrf_id': 1},
        'Ethernet4/6': {'site_of_origin': '--', 'vrf': 'default', 'vrf_id': 1},
        'Ethernet4/7': {'site_of_origin': '--', 'vrf': 'default', 'vrf_id': 1},
        'Ethernet4/8': {'site_of_origin': '--', 'vrf': 'default', 'vrf_id': 1},
        'Ethernet4/9': {'site_of_origin': '--', 'vrf': 'default', 'vrf_id': 1},
        'Null0': {'site_of_origin': '--', 'vrf': 'default', 'vrf_id': 1},
        'mgmt0': {'site_of_origin': '--', 'vrf': 'management', 'vrf_id': 2}}

    golden_output = {'execute.return_value': '''

    Interface                 VRF-Name                        VRF-ID  Site-of-Origin
    Ethernet2/1               VRF1                                 3  --
    Null0                     default                              1  --
    Ethernet2/1.10            default                              1  --
    Ethernet2/1.20            default                              1  --
    Ethernet2/4               default                              1  --
    Ethernet2/5               default                              1  --
    Ethernet2/6               default                              1  --
    Ethernet2/7               default                              1  --
    Ethernet2/8               default                              1  --
    Ethernet2/9               default                              1  --
    Ethernet2/10              default                              1  --
    Ethernet2/11              default                              1  --
    Ethernet2/12              default                              1  --
    Ethernet2/13              default                              1  --
    Ethernet2/14              default                              1  --
    Ethernet2/15              default                              1  --
    Ethernet2/16              default                              1  --
    Ethernet2/17              default                              1  --
    Ethernet2/18              default                              1  --
    Ethernet2/19              default                              1  --
    Ethernet2/20              default                              1  --
    Ethernet2/21              default                              1  --
    Ethernet2/22              default                              1  --
    Ethernet2/23              default                              1  --
    Ethernet2/24              default                              1  --
    Ethernet2/25              default                              1  --
    Ethernet2/26              default                              1  --
    Ethernet2/27              default                              1  --
    Ethernet2/28              default                              1  --
    Ethernet2/29              default                              1  --
    Ethernet2/30              default                              1  --
    Ethernet2/31              default                              1  --
    Ethernet2/32              default                              1  --
    Ethernet2/33              default                              1  --
    Ethernet2/34              default                              1  --
    Ethernet2/35              default                              1  --
    Ethernet2/36              default                              1  --
    Ethernet2/37              default                              1  --
    Ethernet2/38              default                              1  --
    Ethernet2/39              default                              1  --
    Ethernet2/40              default                              1  --
    Ethernet2/41              default                              1  --
    Ethernet2/42              default                              1  --
    Ethernet2/43              default                              1  --
    Ethernet2/44              default                              1  --
    Ethernet2/45              default                              1  --
    Ethernet2/46              default                              1  --
    Ethernet2/47              default                              1  --
    Ethernet2/48              default                              1  --
    Ethernet3/1               default                              1  --
    Ethernet3/2               default                              1  --
    Ethernet3/3               default                              1  --
    Ethernet3/4               default                              1  --
    Ethernet3/5               default                              1  --
    Ethernet3/6               default                              1  --
    Ethernet3/7               default                              1  --
    Ethernet3/8               default                              1  --
    Ethernet3/9               default                              1  --
    Ethernet3/10              default                              1  --
    Ethernet3/11              default                              1  --
    Ethernet3/12              default                              1  --
    Ethernet3/13              default                              1  --
    Ethernet3/14              default                              1  --
    Ethernet3/15              default                              1  --
    Ethernet3/16              default                              1  --
    Ethernet3/17              default                              1  --
    Ethernet3/18              default                              1  --
    Ethernet3/19              default                              1  --
    Ethernet3/20              default                              1  --
    Ethernet3/21              default                              1  --
    Ethernet3/22              default                              1  --
    Ethernet3/23              default                              1  --
    Ethernet3/24              default                              1  --
    Ethernet3/25              default                              1  --
    Ethernet3/26              default                              1  --
    Ethernet3/27              default                              1  --
    Ethernet3/28              default                              1  --
    Ethernet3/29              default                              1  --
    Ethernet3/30              default                              1  --
    Ethernet3/31              default                              1  --
    Ethernet3/32              default                              1  --
    Ethernet3/33              default                              1  --
    Ethernet3/34              default                              1  --
    Ethernet3/35              default                              1  --
    Ethernet3/36              default                              1  --
    Ethernet3/37              default                              1  --
    Ethernet3/38              default                              1  --
    Ethernet3/39              default                              1  --
    Ethernet3/40              default                              1  --
    Ethernet3/41              default                              1  --
    Ethernet3/42              default                              1  --
    Ethernet3/43              default                              1  --
    Ethernet3/44              default                              1  --
    Ethernet3/45              default                              1  --
    Ethernet3/46              default                              1  --
    Ethernet3/47              default                              1  --
    Ethernet3/48              default                              1  --
    Ethernet4/1               default                              1  --
    Ethernet4/2               default                              1  --
    Ethernet4/3               default                              1  --
    Ethernet4/4               default                              1  --
    Ethernet4/5               default                              1  --
    Ethernet4/6               default                              1  --
    Ethernet4/7               default                              1  --
    Ethernet4/8               default                              1  --
    Ethernet4/9               default                              1  --
    Ethernet4/10              default                              1  --
    Ethernet4/11              default                              1  --
    Ethernet4/12              default                              1  --
    Ethernet4/13              default                              1  --
    Ethernet4/14              default                              1  --
    Ethernet4/15              default                              1  --
    Ethernet4/16              default                              1  --
    Ethernet4/17              default                              1  --
    Ethernet4/18              default                              1  --
    Ethernet4/19              default                              1  --
    Ethernet4/20              default                              1  --
    Ethernet4/21              default                              1  --
    Ethernet4/22              default                              1  --
    Ethernet4/23              default                              1  --
    Ethernet4/24              default                              1  --
    Ethernet4/25              default                              1  --
    Ethernet4/26              default                              1  --
    Ethernet4/27              default                              1  --
    Ethernet4/28              default                              1  --
    Ethernet4/29              default                              1  --
    Ethernet4/30              default                              1  --
    Ethernet4/31              default                              1  --
    Ethernet4/32              default                              1  --
    Ethernet4/33              default                              1  --
    Ethernet4/34              default                              1  --
    Ethernet4/35              default                              1  --
    Ethernet4/36              default                              1  --
    Ethernet4/37              default                              1  --
    Ethernet4/38              default                              1  --
    Ethernet4/39              default                              1  --
    Ethernet4/40              default                              1  --
    Ethernet4/41              default                              1  --
    Ethernet4/42              default                              1  --
    Ethernet4/43              default                              1  --
    Ethernet4/44              default                              1  --
    Ethernet4/45              default                              1  --
    Ethernet4/46              default                              1  --
    Ethernet4/47              default                              1  --
    Ethernet4/48              default                              1  --
    mgmt0                     management                           2  --

        '''}
    golden_parsed_output_custom = {
        'Ethernet2/1': {'site_of_origin': '--', 'vrf': 'VRF1', 'vrf_id': 3}
    }
    golden_output_custom = {'execute.return_value': '''
     Interface                 VRF-Name                        VRF-ID  Site-of-Origin
    Ethernet2/1               VRF1                                 3  --
    '''}

    def test_empty(self):
        self.device1 = Mock(**self.empty_output)
        vrf_all_interface_obj = ShowVrfAllInterface(device=self.device1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = vrf_all_interface_obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        vrf_all_interface_obj = ShowVrfAllInterface(device=self.device)
        parsed_output = vrf_all_interface_obj.parse()
        self.maxDiff = None
        self.assertEqual(parsed_output, self.golden_parsed_output)

    def test_golden_custom(self):
        self.device = Mock(**self.golden_output_custom)
        vrf_all_interface_obj = ShowVrfAllInterface(device=self.device)
        parsed_output = vrf_all_interface_obj.parse(vrf='VRF1', interface='Ethernet2/1')
        self.maxDiff = None
        self.assertEqual(parsed_output, self.golden_parsed_output_custom)


# #############################################################################
# # Unittest For Show Interface Switchport
# #############################################################################


class TestShowInterfaceSwitchport(unittest.TestCase):
    device = Device(name='aDevice')
    device0 = Device(name='bDevice')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output_1 = {
        'Ethernet2/2':
            {'access_vlan': 1,
             'access_vlan_mode': 'default',
             'admin_priv_vlan_primary_host_assoc': 'none',
             'admin_priv_vlan_primary_mapping': 'none',
             'admin_priv_vlan_secondary_host_assoc': 'none',
             'admin_priv_vlan_secondary_mapping': 'none',
             'admin_priv_vlan_trunk_encapsulation': 'dot1q',
             'admin_priv_vlan_trunk_native_vlan': 'none',
             'admin_priv_vlan_trunk_normal_vlans': 'none',
             'admin_priv_vlan_trunk_private_vlans': 'none',
             'native_vlan': 1,
             'native_vlan_mode': 'default',
             'operational_private_vlan': 'none',
             'switchport_mode': 'trunk',
             'switchport_monitor': 'Not enabled',
             'switchport_status': 'enabled',
             'switchport_enable': True,
             'trunk_vlans': '100,300'},
        'Ethernet2/3':
            {'access_vlan': 100,
             'access_vlan_mode': 'Vlan not created',
             'admin_priv_vlan_primary_host_assoc': 'none',
             'admin_priv_vlan_primary_mapping': 'none',
             'admin_priv_vlan_secondary_host_assoc': 'none',
             'admin_priv_vlan_secondary_mapping': 'none',
             'admin_priv_vlan_trunk_encapsulation': 'dot1q',
             'admin_priv_vlan_trunk_native_vlan': 'none',
             'admin_priv_vlan_trunk_normal_vlans': 'none',
             'admin_priv_vlan_trunk_private_vlans': 'none',
             'native_vlan': 1,
             'native_vlan_mode': 'default',
             'operational_private_vlan': 'none',
             'switchport_mode': 'access',
             'switchport_monitor': 'Not enabled',
             'switchport_status': 'enabled',
             'switchport_enable': True,
             'trunk_vlans': '1-4094'}}

    golden_output_1 = {'execute.return_value': '''
        Name: Ethernet2/2
          Switchport: Enabled
          Switchport Monitor: Not enabled
          Operational Mode: trunk
          Access Mode VLAN: 1 (default)
          Trunking Native Mode VLAN: 1 (default)
          Trunking VLANs Allowed: 100,300
          Administrative private-vlan primary host-association: none
          Administrative private-vlan secondary host-association: none
          Administrative private-vlan primary mapping: none
          Administrative private-vlan secondary mapping: none
          Administrative private-vlan trunk native VLAN: none
          Administrative private-vlan trunk encapsulation: dot1q
          Administrative private-vlan trunk normal VLANs: none
          Administrative private-vlan trunk private VLANs: none
          Operational private-vlan: none
        Name: Ethernet2/3
          Switchport: Enabled
          Switchport Monitor: Not enabled
          Operational Mode: access
          Access Mode VLAN: 100 (Vlan not created)
          Trunking Native Mode VLAN: 1 (default)
          Trunking VLANs Allowed: 1-4094
          Administrative private-vlan primary host-association: none
          Administrative private-vlan secondary host-association: none
          Administrative private-vlan primary mapping: none
          Administrative private-vlan secondary mapping: none
          Administrative private-vlan trunk native VLAN: none
          Administrative private-vlan trunk encapsulation: dot1q
          Administrative private-vlan trunk normal VLANs: none
          Administrative private-vlan trunk private VLANs: none
          Operational private-vlan: none
      '''}

    golden_parsed_output_2 = {
        'port-channel662':
            {'access_vlan': 1,
             'access_vlan_mode': 'default',
             'admin_priv_vlan_primary_host_assoc': 'none',
             'admin_priv_vlan_primary_mapping': 'none',
             'admin_priv_vlan_secondary_host_assoc': 'none',
             'admin_priv_vlan_secondary_mapping': 'none',
             'admin_priv_vlan_trunk_encapsulation': 'dot1q',
             'admin_priv_vlan_trunk_native_vlan': 'none',
             'admin_priv_vlan_trunk_normal_vlans': 'none',
             'admin_priv_vlan_trunk_private_vlans': 'none',
             'native_vlan': 3967,
             'native_vlan_mode': 'Vlan not created',
             'operational_private_vlan': 'none',
             'switchport_enable': True,
             'switchport_mode': 'trunk',
             'switchport_monitor': 'Not enabled',
             'switchport_status': 'enabled',
             'trunk_vlans': '2600-26507,2610,2620,2630,2640,2690,2698-2699'}}

    golden_output_2 = {'execute.return_value': '''
        Name: port-channel662
          Switchport: Enabled
          Switchport Monitor: Not enabled
          Operational Mode: trunk
          Access Mode VLAN: 1 (default)
          Trunking Native Mode VLAN: 3967 (Vlan not created)
          Trunking VLANs Allowed: 2600-26507,2610,2620,2630,2640,2690,2698-2699
          FabricPath Topology List Allowed: 0
          Administrative private-vlan primary host-association: none
          Administrative private-vlan secondary host-association: none
          Administrative private-vlan primary mapping: none
          Administrative private-vlan secondary mapping: none
          Administrative private-vlan trunk native VLAN: none
          Administrative private-vlan trunk encapsulation: dot1q
          Administrative private-vlan trunk normal VLANs: none
          Administrative private-vlan trunk private VLANs: none
          Operational private-vlan: none
        '''}
    golden_parsed_output_custom = {
        'Ethernet2/2':
            {'access_vlan': 1,
             'access_vlan_mode': 'default',
             'admin_priv_vlan_primary_host_assoc': 'none',
             'admin_priv_vlan_primary_mapping': 'none',
             'admin_priv_vlan_secondary_host_assoc': 'none',
             'admin_priv_vlan_secondary_mapping': 'none',
             'admin_priv_vlan_trunk_encapsulation': 'dot1q',
             'admin_priv_vlan_trunk_native_vlan': 'none',
             'admin_priv_vlan_trunk_normal_vlans': 'none',
             'admin_priv_vlan_trunk_private_vlans': 'none',
             'native_vlan': 1,
             'native_vlan_mode': 'default',
             'operational_private_vlan': 'none',
             'switchport_mode': 'trunk',
             'switchport_monitor': 'Not enabled',
             'switchport_status': 'enabled',
             'switchport_enable': True,
             'trunk_vlans': '100,300'},
    }
    golden_output_custom = {'execute.return_value': '''
            Name: Ethernet2/2
              Switchport: Enabled
              Switchport Monitor: Not enabled
              Operational Mode: trunk
              Access Mode VLAN: 1 (default)
              Trunking Native Mode VLAN: 1 (default)
              Trunking VLANs Allowed: 100,300
              Administrative private-vlan primary host-association: none
              Administrative private-vlan secondary host-association: none
              Administrative private-vlan primary mapping: none
              Administrative private-vlan secondary mapping: none
              Administrative private-vlan trunk native VLAN: none
              Administrative private-vlan trunk encapsulation: dot1q
              Administrative private-vlan trunk normal VLANs: none
              Administrative private-vlan trunk private VLANs: none
              Operational private-vlan: none
              '''}
    golden_parsed_output_disabled = {
        'Ethernet1/1': {
            'switchport_status': 'disabled',
            'switchport_enable': False,
        }
    }
    golden_output_disabled = {'execute.return_value': '''
    Name: Ethernet1/1
        Switchport: Disabled
    '''}

    def test_empty(self):
        self.device1 = Mock(**self.empty_output)
        interface_switchport_obj = ShowInterfaceSwitchport(device=self.device1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = interface_switchport_obj.parse()

    def test_golden_1(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_1)
        interface_switchport_obj = ShowInterfaceSwitchport(device=self.device)
        parsed_output = interface_switchport_obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_1)

    def test_golden_2(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_2)
        interface_switchport_obj = ShowInterfaceSwitchport(device=self.device)
        parsed_output = interface_switchport_obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_2)

    def test_golden_custom(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_custom)
        interface_switchport_obj = ShowInterfaceSwitchport(device=self.device)
        parsed_output = interface_switchport_obj.parse(interface='Ethernet2/2')
        self.assertEqual(parsed_output, self.golden_parsed_output_custom)

    def test_golden_disabled(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_disabled)
        interface_switchport_obj = ShowInterfaceSwitchport(device=self.device)
        parsed_output = interface_switchport_obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_disabled)


class TestShowIpInterfaceBrief(unittest.TestCase):
    device = Device(name='aDevice')
    device1 = Device(name='bDevice')
    empty_output = {'execute.return_value': ''}
    golden_parsed_output = {'interface':
                                {'Eth5/48.106':
                                     {'interface_status': 'protocol-down/link-down/admin-up',
                                      'ip_address': '10.81.6.1'},
                                 'Lo3':
                                     {'interface_status': 'protocol-up/link-up/admin-up',
                                      'ip_address': '192.168.205.1'},
                                 'Po1.102':
                                     {'interface_status': 'protocol-up/link-up/admin-up', 'ip_address': '192.168.70.2'},
                                 'Lo11':
                                     {'interface_status': 'protocol-up/link-up/admin-up',
                                      'ip_address': '192.168.151.1'},
                                 'Vlan23':
                                     {'vlan_id':
                                          {'23':
                                               {'interface_status': 'protocol-up/link-up/admin-up',
                                                'ip_address': '192.168.186.1'}}},
                                 'Eth5/48.101':
                                     {'interface_status': 'protocol-down/link-down/admin-up',
                                      'ip_address': '10.81.1.1'},
                                 'Eth5/48.102':
                                     {'interface_status': 'protocol-down/link-down/admin-up',
                                      'ip_address': '10.81.2.1'},
                                 'Eth5/48.105':
                                     {'interface_status': 'protocol-down/link-down/admin-up',
                                      'ip_address': '10.81.5.1'},
                                 'Lo2':
                                     {'interface_status': 'protocol-up/link-up/admin-up', 'ip_address': '192.168.51.1'},
                                 'Lo1':
                                     {'interface_status': 'protocol-up/link-up/admin-up',
                                      'ip_address': '192.168.154.1'},
                                 'Eth6/22':
                                     {'interface_status': 'protocol-up/link-up/admin-up',
                                      'ip_address': '192.168.145.1'},
                                 'Po1.101':
                                     {'interface_status': 'protocol-up/link-up/admin-up',
                                      'ip_address': '192.168.151.2'},
                                 'Lo10':
                                     {'interface_status': 'protocol-up/link-up/admin-up', 'ip_address': '192.168.64.1'},
                                 'Po1.103':
                                     {'interface_status': 'protocol-up/link-up/admin-up',
                                      'ip_address': '192.168.246.2'},
                                 'Eth5/48.100':
                                     {'interface_status': 'protocol-down/link-down/admin-up',
                                      'ip_address': '10.81.0.1'},
                                 'Po2.107':
                                     {'interface_status': 'protocol-up/link-up/admin-up', 'ip_address': '192.168.66.1'},
                                 'Eth5/48.103':
                                     {'interface_status': 'protocol-down/link-down/admin-up',
                                      'ip_address': '10.81.3.1'},
                                 'tunnel-te12':
                                     {'interface_status': 'protocol-up/link-up/admin-up',
                                      'ip_address': 'unnumbered(loopback0)'},
                                 'Eth5/48.110':
                                     {'interface_status': 'protocol-down/link-down/admin-up',
                                      'ip_address': '10.81.10.1'},
                                 'Po2.103':
                                     {'interface_status': 'protocol-up/link-up/admin-up', 'ip_address': '192.168.19.1'},
                                 'Lo0':
                                     {'interface_status': 'protocol-up/link-up/admin-up', 'ip_address': '192.168.4.1'},
                                 'Po2.101':
                                     {'interface_status': 'protocol-up/link-up/admin-up',
                                      'ip_address': '192.168.135.1'},
                                 'Po2.100':
                                     {'interface_status': 'protocol-up/link-up/admin-up',
                                      'ip_address': '192.168.196.1'},
                                 'tunnel-te11':
                                     {'interface_status': 'protocol-up/link-up/admin-up',
                                      'ip_address': 'unnumbered(loopback0)'},
                                 'Po2.102':
                                     {'interface_status': 'protocol-up/link-up/admin-up', 'ip_address': '192.168.76.1'},
                                 'Eth5/48.104':
                                     {'interface_status': 'protocol-down/link-down/admin-up', 'ip_address': '10.81.4.1'}
                                 }
                            }

    golden_output = {'execute.return_value': '''
 IP Interface Status for VRF "default"(1)
 Interface            IP Address      Interface Status
 Vlan23               192.168.186.1     protocol-up/link-up/admin-up
 Lo0                  192.168.4.1       protocol-up/link-up/admin-up
 Lo1                  192.168.154.1       protocol-up/link-up/admin-up
 Lo2                  192.168.51.1       protocol-up/link-up/admin-up
 Lo3                  192.168.205.1       protocol-up/link-up/admin-up
 Lo10                 192.168.64.1      protocol-up/link-up/admin-up
 Lo11                 192.168.151.1      protocol-up/link-up/admin-up
 Po2.100              192.168.196.1      protocol-up/link-up/admin-up
 Po1.101              192.168.151.2      protocol-up/link-up/admin-up
 Po2.101              192.168.135.1      protocol-up/link-up/admin-up
 Po1.102              192.168.70.2      protocol-up/link-up/admin-up
 Po2.102              192.168.76.1      protocol-up/link-up/admin-up
 Po1.103              192.168.246.2      protocol-up/link-up/admin-up
 Po2.103              192.168.19.1      protocol-up/link-up/admin-up
 Po2.107              192.168.66.1      protocol-up/link-up/admin-up
 Eth5/48.100          10.81.0.1       protocol-down/link-down/admin-up
 Eth5/48.101          10.81.1.1       protocol-down/link-down/admin-up
 Eth5/48.102          10.81.2.1       protocol-down/link-down/admin-up
 Eth5/48.103          10.81.3.1       protocol-down/link-down/admin-up
 Eth5/48.104          10.81.4.1       protocol-down/link-down/admin-up
 Eth5/48.105          10.81.5.1       protocol-down/link-down/admin-up
 Eth5/48.106          10.81.6.1       protocol-down/link-down/admin-up
 Eth5/48.110          10.81.10.1      protocol-down/link-down/admin-up
 Eth6/22              192.168.145.1     protocol-up/link-up/admin-up
 tunnel-te11          unnumbered      protocol-up/link-up/admin-up
                      (loopback0)
 tunnel-te12          unnumbered      protocol-up/link-up/admin-up
                      (loopback0)

'''}

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        intf_obj = ShowIpInterfaceBrief(device=self.device)
        parsed_output = intf_obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)

    def test_empty(self):
        self.device1 = Mock(**self.empty_output)
        intf_obj = ShowIpInterfaceBrief(device=self.device1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = intf_obj.parse()


class TestShowIpInterfaceBriefPipeVlan(unittest.TestCase):
    device = Device(name='aDevice')
    device1 = Device(name='bDevice')
    empty_output = {'execute.return_value': ''}
    golden_parsed_output = {'interface':
                                {'Vlan98':
                                     {'vlan_id':
                                          {'98':
                                               {'interface_status': 'protocol-down/link-down/admin-up',
                                                'ip_address': '192.168.234.1'}
                                           }
                                      }
                                 }
                            }

    golden_output = {'execute.return_value': '''
 Vlan98               192.168.234.1      protocol-down/link-down/admin-up
'''}

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        intf_obj = ShowIpInterfaceBriefPipeVlan(device=self.device)
        parsed_output = intf_obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)

    def test_empty(self):
        self.device1 = Mock(**self.empty_output)
        intf_obj = ShowIpInterfaceBriefPipeVlan(device=self.device1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = intf_obj.parse()


# ====================================
# Unit test for 'show interface brief'
# ====================================


class TestShowInterfaceBrief(unittest.TestCase):
    device = Device(name='aDevice')
    device1 = Device(name='bDevice')
    maxDiff = None

    empty_output = {'execute.return_value': ''}

    golden_parsed_output = {'interface':
                                {'ethernet':
                                     {'Ethernet1/1': {'mode': 'routed',
                                                      'port_ch': '--',
                                                      'reason': 'none',
                                                      'speed': '1000(D)',
                                                      'status': 'up',
                                                      'type': 'eth',
                                                      'vlan': '--'},
                                      'Ethernet1/3': {'mode': 'access',
                                                      'port_ch': '--',
                                                      'reason': 'Administratively '
                                                                'down',
                                                      'speed': 'auto(D)',
                                                      'status': 'down',
                                                      'type': 'eth',
                                                      'vlan': '1'},
                                      'Ethernet1/6': {'mode': 'access',
                                                      'port_ch': '--',
                                                      'reason': 'Link not '
                                                                'connected',
                                                      'speed': 'auto(D)',
                                                      'status': 'down',
                                                      'type': 'eth',
                                                      'vlan': '1'}},
                                 'loopback':
                                     {'Loopback0':
                                          {'description': '--',
                                           'status': 'up'}},
                                 'port':
                                     {'mgmt0':
                                          {'ip_address': '172.25.143.76',
                                           'mtu': 1500,
                                           'speed': '1000',
                                           'status': 'up',
                                           'vrf': '--'}},
                                 'port_channel':
                                     {'Port-channel8':
                                          {'mode': 'access',
                                           'protocol': 'none',
                                           'reason': 'No operational '
                                                     'members',
                                           'speed': 'auto(I)',
                                           'status': 'down',
                                           'type': 'eth',
                                           'vlan': '1'}}}}

    golden_output = {'execute.return_value': '''
        pinxdt-n9kv-3 # show interface brief

        --------------------------------------------------------------------------------
        Port   VRF          Status IP Address                              Speed    MTU
        --------------------------------------------------------------------------------
        mgmt0  --           up     172.25.143.76                           1000     1500

        --------------------------------------------------------------------------------
        Ethernet      VLAN    Type Mode   Status  Reason                   Speed     Port
        Interface                                                                    Ch #
        --------------------------------------------------------------------------------
        Eth1/1        --      eth  routed up      none                       1000(D) --
        Eth1/3        1       eth  access down    Administratively down      auto(D) --
        Eth1/6        1       eth  access down    Link not connected         auto(D) --


        --------------------------------------------------------------------------------
        Port-channel VLAN    Type Mode   Status  Reason                    Speed   Protocol
        Interface
        --------------------------------------------------------------------------------
        Po8          1       eth  access down    No operational members      auto(I)  none

        --------------------------------------------------------------------------------
        Interface     Status     Description
        --------------------------------------------------------------------------------
        Lo0           up         --

        '''}

    golden_output2 = {'execute.return_value': '''
        show interface Ethernet1/1 brief

        --------------------------------------------------------------------------------
        Ethernet        VLAN  Type Mode   Status  Reason                   Speed     Port
        Interface                                                                    Ch #
        --------------------------------------------------------------------------------
        Eth1/1          --    eth  routed up      none                       1000(D) --
                '''}

    golden_parsed_output2 = {
        'interface':
            {'ethernet':
                 {'Ethernet1/1':
                      {'mode': 'routed',
                       'port_ch': '--',
                       'reason': 'none',
                       'speed': '1000(D)',
                       'status': 'up',
                       'type': 'eth',
                       'vlan': '--'}}}}

    golden_output3 = {'execute.return_value': '''

        --------------------------------------------------------------------------------

        Port   VRF          Status IP Address                              Speed    MTU

        --------------------------------------------------------------------------------

        mgmt0  --           up     172.31.150.153                          1000    1500

        --------------------------------------------------------------------------------

        Ethernet        VLAN    Type Mode   Status  Reason                 Speed     Port

        Interface                                                                    Ch #

        --------------------------------------------------------------------------------

        Eth1/1          --      eth  routed down    Administratively down    auto(D) --

        Eth1/4          --      eth  routed down    Administratively down    auto(D) --

        Eth1/4.1        110     eth  routed down    Administratively down    auto(D) --

        Eth1/4.2        112     eth  routed down    Administratively down    auto(D) --

        Eth1/4.3        114     eth  routed down    Administratively down    auto(D) --

        Eth1/9          --      eth  routed down    XCVR not inserted        auto(D) --

        Eth1/10         --      eth  routed up      none                      10G(D) --

        Eth1/10.1       --      eth  routed down    Configuration Incomplet  auto(D) --

        Eth1/11         --      eth  routed down    Administratively down    auto(D) --

        -------------------------------------------------------------------------------

        Interface Secondary VLAN(Type)                    Status Reason

        -------------------------------------------------------------------------------

        Vlan1     --                                      down   Administratively down
    '''}

    golden_parsed_output3 = {
        'interface': {
            'ethernet': {
                'Ethernet1/1': {
                    'mode': 'routed',
                    'port_ch': '--',
                    'reason': 'Administratively down',
                    'speed': 'auto(D)',
                    'status': 'down',
                    'type': 'eth',
                    'vlan': '--',
                },
                'Ethernet1/10': {
                    'mode': 'routed',
                    'port_ch': '--',
                    'reason': 'none',
                    'speed': '10G(D)',
                    'status': 'up',
                    'type': 'eth',
                    'vlan': '--',
                },
                'Ethernet1/10.1': {
                    'mode': 'routed',
                    'port_ch': '--',
                    'reason': 'Configuration Incomplet',
                    'speed': 'auto(D)',
                    'status': 'down',
                    'type': 'eth',
                    'vlan': '--',
                },
                'Ethernet1/11': {
                    'mode': 'routed',
                    'port_ch': '--',
                    'reason': 'Administratively down',
                    'speed': 'auto(D)',
                    'status': 'down',
                    'type': 'eth',
                    'vlan': '--',
                },
                'Ethernet1/4': {
                    'mode': 'routed',
                    'port_ch': '--',
                    'reason': 'Administratively down',
                    'speed': 'auto(D)',
                    'status': 'down',
                    'type': 'eth',
                    'vlan': '--',
                },
                'Ethernet1/4.1': {
                    'mode': 'routed',
                    'port_ch': '--',
                    'reason': 'Administratively down',
                    'speed': 'auto(D)',
                    'status': 'down',
                    'type': 'eth',
                    'vlan': '110',
                },
                'Ethernet1/4.2': {
                    'mode': 'routed',
                    'port_ch': '--',
                    'reason': 'Administratively down',
                    'speed': 'auto(D)',
                    'status': 'down',
                    'type': 'eth',
                    'vlan': '112',
                },
                'Ethernet1/4.3': {
                    'mode': 'routed',
                    'port_ch': '--',
                    'reason': 'Administratively down',
                    'speed': 'auto(D)',
                    'status': 'down',
                    'type': 'eth',
                    'vlan': '114',
                },
                'Ethernet1/9': {
                    'mode': 'routed',
                    'port_ch': '--',
                    'reason': 'XCVR not inserted',
                    'speed': 'auto(D)',
                    'status': 'down',
                    'type': 'eth',
                    'vlan': '--',
                },
            },
            'port': {
                'mgmt0': {
                    'ip_address': '172.31.150.153',
                    'mtu': 1500,
                    'speed': '1000',
                    'status': 'up',
                    'vrf': '--',
                },
            },
            'vlan': {
                'Vlan1': {
                    'reason': 'Administratively down',
                    'status': 'down',
                    'type': '--',
                },
            },
        },
    }

    golden_output4 = {'execute.return_value': '''
        --------------------------------------------------------------------------------

        Port   VRF          Status IP Address                              Speed    MTU

        --------------------------------------------------------------------------------

        mgmt0  --           up     172.28.249.175                          1000    1500

        --------------------------------------------------------------------------------

        Ethernet        VLAN    Type Mode   Status  Reason                 Speed     Port

        Interface                                                                    Ch #

        --------------------------------------------------------------------------------

        Eth1/1          --      eth  routed down    XCVR not inserted        auto(D) --

        Eth1/2          --      eth  routed down    XCVR not inserted        auto(D) --

        Eth1/3          --      eth  routed down    XCVR not inserted        auto(D) --

        Eth1/4          --      eth  routed down    XCVR not inserted        auto(D) --

        Eth1/5          --      eth  routed down    XCVR not inserted        auto(D) --

        Eth1/6          --      eth  routed down    XCVR not inserted        auto(D) --


        ------------------------------------------------------------------------------------------

        Port-channel VLAN    Type Mode   Status  Reason                              Speed   Protocol

        Interface

        ------------------------------------------------------------------------------------------

        Po10         --      eth  routed up      none                                 a-40G(D)  lacp

        Po10.1       2       eth  routed up      none                                 a-40G(D)    --

        Po10.2       3       eth  routed up      none                                 a-40G(D)    --

        Po10.3       4       eth  routed up      none                                 a-40G(D)    --

    '''}

    golden_parsed_output4 = {
        'interface': {
            'ethernet': {
                'Ethernet1/1': {
                    'mode': 'routed',
                    'port_ch': '--',
                    'reason': 'XCVR not inserted',
                    'speed': 'auto(D)',
                    'status': 'down',
                    'type': 'eth',
                    'vlan': '--',
                },
                'Ethernet1/2': {
                    'mode': 'routed',
                    'port_ch': '--',
                    'reason': 'XCVR not inserted',
                    'speed': 'auto(D)',
                    'status': 'down',
                    'type': 'eth',
                    'vlan': '--',
                },
                'Ethernet1/3': {
                    'mode': 'routed',
                    'port_ch': '--',
                    'reason': 'XCVR not inserted',
                    'speed': 'auto(D)',
                    'status': 'down',
                    'type': 'eth',
                    'vlan': '--',
                },
                'Ethernet1/4': {
                    'mode': 'routed',
                    'port_ch': '--',
                    'reason': 'XCVR not inserted',
                    'speed': 'auto(D)',
                    'status': 'down',
                    'type': 'eth',
                    'vlan': '--',
                },
                'Ethernet1/5': {
                    'mode': 'routed',
                    'port_ch': '--',
                    'reason': 'XCVR not inserted',
                    'speed': 'auto(D)',
                    'status': 'down',
                    'type': 'eth',
                    'vlan': '--',
                },
                'Ethernet1/6': {
                    'mode': 'routed',
                    'port_ch': '--',
                    'reason': 'XCVR not inserted',
                    'speed': 'auto(D)',
                    'status': 'down',
                    'type': 'eth',
                    'vlan': '--',
                },
            },
            'port': {
                'mgmt0': {
                    'ip_address': '172.28.249.175',
                    'mtu': 1500,
                    'speed': '1000',
                    'status': 'up',
                    'vrf': '--',
                },
            },
            'port_channel': {
                'Port-channel10': {
                    'mode': 'routed',
                    'protocol': 'lacp',
                    'reason': 'none',
                    'speed': 'a-40G(D)',
                    'status': 'up',
                    'type': 'eth',
                    'vlan': '--',
                },
                'Port-channel10.1': {
                    'mode': 'routed',
                    'protocol': '--',
                    'reason': 'none',
                    'speed': 'a-40G(D)',
                    'status': 'up',
                    'type': 'eth',
                    'vlan': '2',
                },
                'Port-channel10.2': {
                    'mode': 'routed',
                    'protocol': '--',
                    'reason': 'none',
                    'speed': 'a-40G(D)',
                    'status': 'up',
                    'type': 'eth',
                    'vlan': '3',
                },
                'Port-channel10.3': {
                    'mode': 'routed',
                    'protocol': '--',
                    'reason': 'none',
                    'speed': 'a-40G(D)',
                    'status': 'up',
                    'type': 'eth',
                    'vlan': '4',
                },
            },
        },
    }

    golden_output5 = {'execute.return_value': '''
     ------------------------------------------------------------------------------------------
    Port-channel VLAN    Type Mode   Status  Reason                              Speed   Protocol
    Interface
    ------------------------------------------------------------------------------------------
    Po403.1      1    eth  routed down    Administratively down                 auto(D)    --
    '''}

    golden_parsed_output5 = {
        'interface': {
            'port_channel': {
                'Port-channel403.1': {
                    'mode': 'routed',
                    'protocol': '--',
                    'reason': 'Administratively down',
                    'speed': 'auto(D)',
                    'status': 'down',
                    'type': 'eth',
                    'vlan': '1',
                }
            },
        },
    }

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        intf_obj = ShowInterfaceBrief(device=self.device)
        parsed_output = intf_obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)

    def test_golden2(self):
        self.device = Mock(**self.golden_output2)
        intf_obj = ShowInterfaceBrief(device=self.device)
        parsed_output = intf_obj.parse(interface="Ethernet1/1")
        self.assertEqual(parsed_output, self.golden_parsed_output2)

    def test_golden3(self):
        self.device = Mock(**self.golden_output3)
        intf_obj = ShowInterfaceBrief(device=self.device)
        parsed_output = intf_obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output3)

    def test_empty(self):
        self.device1 = Mock(**self.empty_output)
        intf_obj = ShowInterfaceBrief(device=self.device1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = intf_obj.parse()

    def test_golden4(self):
        self.device = Mock(**self.golden_output4)
        intf_obj = ShowInterfaceBrief(device=self.device)
        parsed_output = intf_obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output4)

    def test_golden5(self):
        self.device = Mock(**self.golden_output5)
        intf_obj = ShowInterfaceBrief(device=self.device)
        parsed_output = intf_obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output5)


class TestShowRunInterface(unittest.TestCase):
    device = Device(name='aDevice')
    device1 = Device(name='bDevice')

    empty_output = {'execute.return_value': ''}

    golden_parsed_output = {'interface':
                                {'nve1':
                                     {'host_reachability_protocol': 'bgp',
                                      'member_vni':
                                          {'8100': {'mcast_group': '225.0.1.11'},
                                           '8101': {'mcast_group': '225.0.1.12'},
                                           '8103': {'mcast_group': '225.0.1.13'},
                                           '8105': {'mcast_group': '225.0.1.16'},
                                           '8106': {'mcast_group': '225.0.1.17'},
                                           '8107': {'mcast_group': '225.0.1.18'},
                                           '8108': {'mcast_group': '225.0.1.19'},
                                           '8109': {'mcast_group': '225.0.1.20'},
                                           '8110': {'mcast_group': '225.0.1.21'},
                                           '8111': {'mcast_group': '225.0.1.22'},
                                           '8112': {'mcast_group': '225.0.1.23'},
                                           '8113': {'mcast_group': '225.0.1.24'},
                                           '8114': {'mcast_group': '225.0.1.25'},
                                           '9100': {'associate_vrf': True},
                                           '9105': {'associate_vrf': True},
                                           '9106': {'associate_vrf': True},
                                           '9107': {'associate_vrf': True},
                                           '9108': {'associate_vrf': True},
                                           '9109': {'associate_vrf': True}
                                           },
                                      'shutdown': False,
                                      'source_interface': 'loopback1'}
                                 }
                            }

    golden_output = {'execute.return_value': '''
        N95_1# show running-config  interface nve 1

        !Command: show running-config interface nve1
        !Time: Mon May 28 16:02:43 2018

        version 7.0(3)I7(1)

        interface nve1
          no shutdown
          host-reachability protocol bgp
          source-interface loopback1
          member vni 8100
            mcast-group 225.0.1.11
          member vni 8101
            mcast-group 225.0.1.12
          member vni 8103
            mcast-group 225.0.1.13
          member vni 8105
            mcast-group 225.0.1.16
          member vni 8106
            mcast-group 225.0.1.17
          member vni 8107
            mcast-group 225.0.1.18
          member vni 8108
            mcast-group 225.0.1.19
          member vni 8109
            mcast-group 225.0.1.20
          member vni 8110
            mcast-group 225.0.1.21
          member vni 8111
            mcast-group 225.0.1.22
          member vni 8112
            mcast-group 225.0.1.23
          member vni 8113
            mcast-group 225.0.1.24
          member vni 8114
            mcast-group 225.0.1.25
          member vni 9100 associate-vrf
          member vni 9105 associate-vrf
          member vni 9106 associate-vrf
          member vni 9107 associate-vrf
          member vni 9108 associate-vrf
          member vni 9109 associate-vrf

    '''}

    golden_parsed_output_1 = {
        'interface': {
            'nve1': {
                'host_reachability_protocol': 'bgp',
                'member_vni': {'2000002': {'mcast_group': '227.1.1.1',
                                           'suppress_arp': True},
                               '2000003': {'mcast_group': '227.1.1.1',
                                           'suppress_arp': True},
                               '2000004': {'mcast_group': '227.1.1.1',
                                           'suppress_arp': True},
                               '2000005': {'mcast_group': '227.1.1.1',
                                           'suppress_arp': True},
                               '2000006': {'mcast_group': '227.1.1.1',
                                           'suppress_arp': True},
                               '2000007': {'mcast_group': '227.1.1.1',
                                           'suppress_arp': True},
                               '2000008': {'mcast_group': '227.1.1.1',
                                           'suppress_arp': True},
                               '2000009': {'mcast_group': '227.1.1.1',
                                           'suppress_arp': True},
                               '2000010': {'mcast_group': '227.1.1.1',
                                           'suppress_arp': True},
                               '3003002': {'associate_vrf': True},
                               '3003003': {'associate_vrf': True},
                               '3003004': {'associate_vrf': True},
                               '3003005': {'associate_vrf': True},
                               '3003006': {'associate_vrf': True},
                               '3003007': {'associate_vrf': True},
                               '3003008': {'associate_vrf': True},
                               '3003009': {'associate_vrf': True},
                               '3003010': {'associate_vrf': True}},
                'shutdown': False,
                'source_interface': 'loopback0'}}}

    golden_output_1 = {'execute.return_value': '''
        CH-P2-TOR-1# sh run int nve 1

        !Command: show running-config interface nve1
        !Time: Wed May 30 07:34:20 2018

        version 7.0(3)I7(4)

        interface nve1
          no shutdown
          host-reachability protocol bgp
          source-interface loopback0
          member vni 2000002-2000010
            suppress-arp
            mcast-group 227.1.1.1
          member vni 3003002-3003010 associate-vrf
    '''}

    golden_parsed_output_2 = {
        'interface': {
            'Ethernet1/1': {
                'description': '*** Peer Link ***',
                'switchport': True,
                'switchport_mode': 'trunk',
                'trunk_vlans': '1-99,101-199,201-1399,1401-4094',
                'trunk_native_vlan': '330',
                'port_channel': {
                    'port_channel_mode': 'active',
                    'port_channel_int': '1',
                },
                'shutdown': False,
            },
        },
    }

    golden_output_2 = {'execute.return_value': '''
      !Command: show running-config interface Ethernet1/1
        !Running configuration last done at: Sun Aug 18 23:22:42 2019
        !Time: Tue Sep  3 23:25:59 2019

        version 7.0(3)I7(6) Bios:version 08.35

        interface Ethernet1/1
          description *** Peer Link ***
          switchport
          switchport mode trunk
          switchport trunk native vlan 330
          switchport trunk allowed vlan 1-99,101-199,201-1399,1401-4094
          channel-group 1 mode active
          no shutdown
    '''
                       }

    # show running-config interface Eth1/4
    golden_output_3 = {'execute.return_value': '''
    !Time: ...
    version ...
    interface Ethernet1/4
     description DeviceA-description
     switchport access vlan x
     speed 1000
     duplex full
    '''}

    golden_parsed_output_3 = {
        'interface': {
            'Ethernet1/4': {
                'duplex': 'full',
                'access_vlan': 'x',
                'switchport_mode': 'access',
                'speed': 1000,
                'description': 'DeviceA-description',
            },
        },
    }

    golden_output_4 = {'execute.return_value': '''
    interface port-channel5
      description Port Channel Config Tst
      switchport mode trunk
      switchport trunk native vlan 2253
      switchport trunk allowed vlan 2253
      speed 10000
      vpc 5
    '''}

    golden_parsed_output_4 = {
        'interface': {
            'port-channel5': {
                'description': 'Port Channel Config Tst',
                'switchport_mode': 'trunk',
                'trunk_native_vlan': '2253',
                'trunk_vlans': '2253',
                'speed': 10000,
                'vpc': '5'
            },
        },
    }

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        intf_obj = ShowRunningConfigInterface(device=self.device)
        parsed_output = intf_obj.parse(interface='nve1')
        self.assertEqual(parsed_output, self.golden_parsed_output)

    def test_golden_1(self):
        self.device = Mock(**self.golden_output_1)
        intf_obj = ShowRunningConfigInterface(device=self.device)
        parsed_output = intf_obj.parse(interface='nve1')
        self.assertEqual(parsed_output, self.golden_parsed_output_1)

    def test_golden_2(self):
        self.device = Mock(**self.golden_output_2)
        intf_obj = ShowRunningConfigInterface(device=self.device)
        parsed_output = intf_obj.parse(interface='Ethernet1/1')
        self.assertEqual(parsed_output, self.golden_parsed_output_2)

    def test_empty(self):
        self.device1 = Mock(**self.empty_output)
        intf_obj = ShowRunningConfigInterface(device=self.device1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = intf_obj.parse(interface='nve1')

    def test_golden_3(self):
        self.device = Mock(**self.golden_output_3)
        intf_obj = ShowRunningConfigInterface(device=self.device)
        parsed_output = intf_obj.parse(interface='Ethernet1/4')
        self.assertEqual(parsed_output, self.golden_parsed_output_3)

    def test_golden_4(self):
        self.device = Mock(**self.golden_output_4)
        intf_obj = ShowRunningConfigInterface(device=self.device)
        parsed_output = intf_obj.parse(interface='port-channel10')
        self.assertEqual(parsed_output, self.golden_parsed_output_4)


class TestShowNveInterface(unittest.TestCase):
    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output = {'interface':
                                {'nve1':
                                     {'state': 'Up',
                                      'encapsulation': 'VXLAN',
                                      'source_interface':
                                          {'loopback1':
                                               {'secondary': '0.0.0.0',
                                                'primary': '10.9.0.1'}
                                           },
                                      'vpc_capability':
                                          {'VPC-VIP-Only':
                                               {'notified': False}
                                           }
                                      }
                                 }
                            }

    golden_output = {'execute.return_value': '''\
        CH-P2-TOR-1# sh nve interface nve 1 detail
        Interface: nve1, State: Up, encapsulation: VXLAN
         VPC Capability: VPC-VIP-Only [not-notified]
         Local Router MAC: 00f2.8bff.737a
         Host Learning Mode: Control-Plane
         Source-Interface: loopback1 (primary: 10.9.0.1, secondary: 0.0.0.0)
         Source Interface State: Up
         IR Capability Mode: No
         Virtual RMAC Advertisement: No
         NVE Flags:
         Interface Handle: 0x49000001
         Source Interface hold-down-time: 180
         Source Interface hold-up-time: 30
         Remaining hold-down time: 0 seconds
         Virtual Router MAC: N/A
         Interface state: nve-intf-add-complete
         unknown-peer-forwarding: disable
         down-stream vni config mode: n/a
        Nve Src node last notif sent: None
        Nve Mcast Src node last notif sent: None
        Nve MultiSite Src node last notif sent: None
    '''
                     }

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = ShowNveInterface(device=self.device)
        parsed_output = obj.parse(interface='nve1')
        self.assertEqual(parsed_output, self.golden_parsed_output)

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowNveInterface(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse(interface='nve1')


#############################################################################
# unittest For show interface description
#############################################################################
class test_show_interface_description(unittest.TestCase):
    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output = {
        "interfaces": {
            "Ethernet1/1.110": {
                "description": "--",
                "speed": "10G",
                "type": "eth"
            },
            "Ethernet1/1.115": {
                "description": "--",
                "speed": "10G",
                "type": "eth"
            },
            "Ethernet1/1.120": {
                "description": "--",
                "speed": "10G",
                "type": "eth"
            },
            "Ethernet1/1.390": {
                "description": "--",
                "speed": "10G",
                "type": "eth"
            },
            "Ethernet1/1.410": {
                "description": "--",
                "speed": "10G",
                "type": "eth"
            },
            "Ethernet1/1.415": {
                "description": "--",
                "speed": "10G",
                "type": "eth"
            },
            "Ethernet1/1.420": {
                "description": "--",
                "speed": "10G",
                "type": "eth"
            },
            "Ethernet1/1.90": {
                "description": "--",
                "speed": "10G",
                "type": "eth"
            },
            "Ethernet1/2": {
                "description": "--",
                "speed": "10G",
                "type": "eth"
            },
            "Ethernet1/2.90": {
                "description": "--",
                "speed": "10G",
                "type": "eth"
            },
            "Ethernet1/2.110": {
                "description": "--",
                "speed": "10G",
                "type": "eth"
            },
            "Ethernet1/2.115": {
                "description": "--",
                "speed": "10G",
                "type": "eth"
            },
            "Ethernet1/2.120": {
                "description": "--",
                "speed": "10G",
                "type": "eth"
            },
            "Ethernet1/2.390": {
                "description": "--",
                "speed": "10G",
                "type": "eth"
            },
            "Ethernet1/2.410": {
                "description": "--",
                "speed": "10G",
                "type": "eth"
            },
            "Ethernet1/2.415": {
                "description": "--",
                "speed": "10G",
                "type": "eth"
            },
            "Ethernet1/2.420": {
                "description": "--",
                "speed": "10G",
                "type": "eth"
            },
            "Port-channel13": {
                "description": "--"
            },
            "Port-channel23": {
                "description": "--"
            },
            "Loopback0": {
                "description": "--"
            },
            "Loopback300": {
                "description": "--"
            },
            "mgmt0": {
                "description": "--"
            }
        }
    }

    golden_output = {'execute.return_value': '''
        -------------------------------------------------------------------------------
        Interface                Description
        -------------------------------------------------------------------------------
        mgmt0                    --

        -------------------------------------------------------------------------------
        Port          Type   Speed   Description
        -------------------------------------------------------------------------------
        Eth1/1.90     eth    10G     --
        Eth1/1.110    eth    10G     --
        Eth1/1.115    eth    10G     --
        Eth1/1.120    eth    10G     --
        Eth1/1.390    eth    10G     --
        Eth1/1.410    eth    10G     --
        Eth1/1.415    eth    10G     --
        Eth1/1.420    eth    10G     --
        Eth1/2        eth    10G     --
        Eth1/2.90     eth    10G     --
        Eth1/2.110    eth    10G     --
        Eth1/2.115    eth    10G     --
        Eth1/2.120    eth    10G     --
        Eth1/2.390    eth    10G     --
        Eth1/2.410    eth    10G     --
        Eth1/2.415    eth    10G     --
        Eth1/2.420    eth    10G     --

        -------------------------------------------------------------------------------
        Interface                Description
        -------------------------------------------------------------------------------
        Po13                     --
        Po23                     --

        -------------------------------------------------------------------------------
        Interface                Description
        -------------------------------------------------------------------------------
        Lo0                      --
        Lo300                    --
    '''}

    golden_parsed_interface_output = {
        "interfaces": {
            "Ethernet1/1": {
                "description": "--",
                "speed": "10G",
                "type": "eth"
            }
        }
    }

    golden_interface_output = {'execute.return_value': '''
        -------------------------------------------------------------------------------
        Port          Type   Speed   Description
        -------------------------------------------------------------------------------
        Eth1/1        eth    10G     --
    '''}

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowInterfaceDescription(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = ShowInterfaceDescription(device=self.device)
        parsed_output = obj.parse()
        self.maxDiff = None
        self.assertEqual(parsed_output, self.golden_parsed_output)

    def test_golden_interface(self):
        self.device = Mock(**self.golden_interface_output)
        obj = ShowInterfaceDescription(device=self.device)
        parsed_output = obj.parse(interface='Eth1/1')
        self.maxDiff = None
        self.assertEqual(parsed_output, self.golden_parsed_interface_output)


#############################################################################
# unitest For show interface status
#############################################################################
class test_show_interface_status(unittest.TestCase):
    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output = {
        'interfaces': {
            'Ethernet1/1': {
                'duplex_code': 'full',
                'name': 'AOTLXPRPBD10001',
                'port_speed': '10G',
                'status': 'connected',
                'type': '10g',
                'vlan': 'trunk'
            },
            'Ethernet1/2': {
                'duplex_code': 'full',
                'name': 'AOTLXPRPBD10004',
                'port_speed': '10G',
                'status': 'connected',
                'type': '10g',
                'vlan': '360'
            },
            'Ethernet1/43': {
                'duplex_code': 'auto',
                'port_speed': 'auto',
                'status': 'disabled',
                'type': '10g',
                'vlan': '1'
            },
            'Ethernet1/52.511': {
                'duplex_code': 'full',
                'port_speed': '10G',
                'status': 'connected',
                'type': '10Gbase-LR',
                'vlan': 'routed'
            },
            'Port-channel147': {
                'duplex_code': 'full',
                'name': 'AOTLXPRPBD10112',
                'port_speed': '10G',
                'status': 'connected',
                'vlan': '360'
            },
            'Vlan1': {
                'duplex_code': 'auto',
                'port_speed': 'auto',
                'status': 'down',
                'vlan': 'routed'
            },
            'Vlan366': {
                'duplex_code': 'auto',
                'name': 'BigData',
                'port_speed': 'auto',
                'status': 'connected',
                'vlan': 'routed'
            },
            'mgmt0': {
                'duplex_code': 'full',
                'name': 'ES1SW18AUN6_6/22',
                'port_speed': '1000',
                'status': 'connected',
                'vlan': 'routed'
            },
            'Nve1': {
                'duplex_code': 'auto',
                'port_speed': 'auto',
                'status': 'connected',
            },
            'Loopback0': {
                'duplex_code': 'auto',
                'status': 'connected',
                'vlan': 'routed',
            },
        }
    }

    golden_output = {'execute.return_value': '''
        --------------------------------------------------------------------------------
        Port          Name               Status    Vlan      Duplex  Speed   Type
        --------------------------------------------------------------------------------
        mgmt0         ES1SW18AUN6_6/22   connected routed    full    1000    --

        --------------------------------------------------------------------------------
        Port          Name               Status    Vlan      Duplex  Speed   Type
        --------------------------------------------------------------------------------
        Eth1/1        AOTLXPRPBD10001    connected trunk     full    10G     10g
        Eth1/2        AOTLXPRPBD10004    connected 360       full    10G     10g
        Eth1/43       --                 disabled  1         auto    auto    10g
        Eth1/52.511   --                 connected routed    full    10G     10Gbase-LR
        Po147         AOTLXPRPBD10112    connected 360       full    10G     --
        Vlan1         --                 down      routed    auto    auto    --
        Vlan366       BigData            connected routed    auto    auto    --
        nve1          --                 connected --        auto    auto    --
        Lo0           --                 connected routed    auto    --      --
    '''}

    golden_parsed_interface_output = {
        'interfaces': {
            'Ethernet1/1': {
                'duplex_code': 'full',
                'name': 'AOTLXPRPBD10001',
                'port_speed': '10G',
                'status': 'connected',
                'type': '10g',
                'vlan': 'trunk'}
        }
    }

    golden_interface_output = {'execute.return_value': '''
        Port          Name               Status    Vlan      Duplex  Speed   Type
        --------------------------------------------------------------------------------
        Eth1/1        AOTLXPRPBD10001    connected trunk     full    10G     10g
    '''}

    golden_output_2 = {'execute.return_value': '''
    --------------------------------------------------------------------------------
    Port          Name               Status    Vlan      Duplex  Speed   Type
    --------------------------------------------------------------------------------
    Po135         DO-DD01            connected 51        full    a-10G   --
    Po140         DO-UCS01-B         connected trunk     full    a-10G   --
    mgmt0         --                 connected routed    full    a-1000  --
    Eth101/1/1    DODC01             connected 101       full    a-1000
    Eth101/1/2    DO-EXCH-01         connected 101       full    a-1000
    '''}

    golden_parsed_output_2 = {
        'interfaces': {
            'Ethernet101/1/1': {
                'duplex_code': 'full',
                'name': 'DODC01',
                'port_speed': 'a-1000',
                'status': 'connected',
                'vlan': '101',
            },
            'Ethernet101/1/2': {
                'duplex_code': 'full',
                'name': 'DO-EXCH-01',
                'port_speed': 'a-1000',
                'status': 'connected',
                'vlan': '101',
            },
            'Port-channel135': {
                'duplex_code': 'full',
                'name': 'DO-DD01',
                'port_speed': 'a-10G',
                'status': 'connected',
                'vlan': '51',
            },
            'Port-channel140': {
                'duplex_code': 'full',
                'name': 'DO-UCS01-B',
                'port_speed': 'a-10G',
                'status': 'connected',
                'vlan': 'trunk',
            },
            'mgmt0': {
                'duplex_code': 'full',
                'port_speed': 'a-1000',
                'status': 'connected',
                'vlan': 'routed',
            },
        },
    }

    golden_output_3 = {'execute.return_value': '''
        N7K-1-LAB# show int status

        --------------------------------------------------------------------------------
        Port Name Status Vlan Duplex Speed Type
        --------------------------------------------------------------------------------
        mgmt0 -- connected routed full a-1000 --
        Eth1/1 *** N7K-2-FLEXP connected trunk full a-10G SFP-H10GB-C
        Eth1/2 *** N7K-2-FLEXP connected trunk full a-10G SFP-H10GB-C
        Eth1/3 *** P2P L3-CIS- connected routed full a-1000 1000base-T
        Eth1/4 *** FEX 2248TP  connected 1      full a-10G  Fabric Exte
        Eth1/5 *** L2 L3-CIS-N connected trunk full a-1000 1000base-T
        Eth1/6 *** L2POE Gi1/0 connected trunk full a-1000 1000base-T
        Eth1/7 *** To ACI leaf connected trunk full a-1000 1000base-SX
        Eth1/8 -- sfpAbsent routed auto auto --
        Eth1/9 -- sfpAbsent routed auto auto --
    '''}

    golden_parsed_output_3 = {
        'interfaces': {
            'Ethernet1/1': {
                'duplex_code': 'full',
                'name': '*** N7K-2-FLEXP',
                'port_speed': 'a-10G',
                'status': 'connected',
                'type': 'SFP-H10GB-C',
                'vlan': 'trunk',
            },
            'Ethernet1/2': {
                'duplex_code': 'full',
                'name': '*** N7K-2-FLEXP',
                'port_speed': 'a-10G',
                'status': 'connected',
                'type': 'SFP-H10GB-C',
                'vlan': 'trunk',
            },
            'Ethernet1/3': {
                'duplex_code': 'full',
                'name': '*** P2P L3-CIS-',
                'port_speed': 'a-1000',
                'status': 'connected',
                'type': '1000base-T',
                'vlan': 'routed',
            },
            'Ethernet1/4': {
                'duplex_code': 'full',
                'name': '*** FEX 2248TP',
                'port_speed': 'a-10G',
                'status': 'connected',
                'type': 'Fabric Exte',
                'vlan': '1',
            },
            'Ethernet1/5': {
                'duplex_code': 'full',
                'name': '*** L2 L3-CIS-N',
                'port_speed': 'a-1000',
                'status': 'connected',
                'type': '1000base-T',
                'vlan': 'trunk',
            },
            'Ethernet1/6': {
                'duplex_code': 'full',
                'name': '*** L2POE Gi1/0',
                'port_speed': 'a-1000',
                'status': 'connected',
                'type': '1000base-T',
                'vlan': 'trunk',
            },
            'Ethernet1/7': {
                'duplex_code': 'full',
                'name': '*** To ACI leaf',
                'port_speed': 'a-1000',
                'status': 'connected',
                'type': '1000base-SX',
                'vlan': 'trunk',
            },
            'Ethernet1/8': {
                'duplex_code': 'auto',
                'port_speed': 'auto',
                'status': 'sfpAbsent',
                'vlan': 'routed',
            },
            'Ethernet1/9': {
                'duplex_code': 'auto',
                'port_speed': 'auto',
                'status': 'sfpAbsent',
                'vlan': 'routed',
            },
            'mgmt0': {
                'duplex_code': 'full',
                'port_speed': 'a-1000',
                'status': 'connected',
                'vlan': 'routed',
            },
        },
    }

    golden_output_4 = {'execute.return_value': '''
        ----------------------------------------------------------------------------------------------
         Port           Name                Status     Vlan       Duplex   Speed    Type              
        ----------------------------------------------------------------------------------------------
         mgmt0          --                  connected  routed     full     1G       --               
         Eth1/1         --                  sfpabsent  trunk      full     inherit  --               
         Eth1/2         --                  sfpabsent  trunk      full     inherit  --               
         Eth1/3         --                  sfpabsent  trunk      full     inherit  --               
         Eth1/4         --                  sfpabsent  trunk      full     inherit  --               
         Eth1/5         --                  sfpabsent  trunk      full     inherit  --               
         Eth1/6         --                  sfpabsent  trunk      full     inherit  --               
         Eth1/7         --                  sfpabsent  trunk      full     inherit  --               
         Eth1/8         --                  sfpabsent  trunk      full     inherit  --               
         Eth1/9         --                  sfpabsent  trunk      full     inherit  --               
         Eth1/10        --                  sfpabsent  trunk      full     inherit  --               
         Eth1/11        --                  sfpabsent  trunk      full     inherit  --               
         Eth1/12        --                  sfpabsent  trunk      full     inherit  --               
         Eth1/13        --                  sfpabsent  trunk      full     inherit  --               
         Eth1/14        --                  sfpabsent  trunk      full     inherit  --               
         Eth1/15        --                  sfpabsent  trunk      full     inherit  --               
         Eth1/16        --                  sfpabsent  trunk      full     inherit  --               
         Eth1/17        --                  sfpabsent  trunk      full     inherit  --               
         Eth1/18        --                  sfpabsent  trunk      full     inherit  --               
         Eth1/19        --                  sfpabsent  trunk      full     inherit  --               
         Eth1/20        --                  sfpabsent  trunk      full     inherit  --               
         Eth1/21        --                  sfpabsent  trunk      full     inherit  --               
         Eth1/22        --                  sfpabsent  trunk      full     inherit  --               
         Eth1/23        --                  out-of-ser trunk      full     40G      QSFP-40G-SR-BD   
         Eth1/24        --                  notconnect trunk      full     inherit  QSFP-40G-SR-BD   
         Eth1/25        --                  sfpabsent  routed     full     inherit  --               
         Eth1/25.1      --                  parentdown routed     full     inherit  --               
         Eth1/26        --                  sfpabsent  routed     full     inherit  --               
         Eth1/26.2      --                  parentdown routed     full     inherit  --               
         Eth1/27        --                  sfpabsent  routed     full     inherit  --               
         Eth1/27.3      --                  parentdown routed     full     inherit  --               
         Eth1/28        --                  sfpabsent  routed     full     inherit  --               
         Eth1/28.4      --                  parentdown routed     full     inherit  --               
         Eth1/29        --                  sfpabsent  routed     full     inherit  --               
         Eth1/29.5      --                  parentdown routed     full     inherit  --               
         Eth1/30        --                  sfpabsent  routed     full     inherit  --               
         Eth1/30.6      --                  parentdown routed     full     inherit  --               
         Eth1/31        --                  connected  routed     full     100G     QSFP-40/100-SRBD 
         Eth1/31.21     --                  connected  routed     full     100G     QSFP-40/100-SRBD 
         Eth1/32        --                  connected  routed     full     100G     QSFP-40/100-SRBD 
         Eth1/32.22     --                  connected  routed     full     100G     QSFP-40/100-SRBD 
         Lo0            --                  connected  routed     auto     --       --               
         Lo1            --                  connected  routed     auto     --       --               
         Lo1023         --                  connected  routed     auto     --       --               

        ----------------------------------------------------------------
         Interface     Name                Status    Reason             
        ----------------------------------------------------------------
         Tunnel7       --                  up        no-reason         
         Tunnel8       --                  up        no-reason         
         Tunnel36      --                  up        no-reason         
         Tunnel37      --                  up        no-reason         
         Tunnel38      --                  up        no-reason         
         Tunnel39      --                  up        no-reason         
         Tunnel40      --                  up        no-reason         
         Tunnel41      --                  up        no-reason         
         Tunnel42      --                  up        no-reason         
         Tunnel43      --                  up        no-reason         
         Tunnel44      --                  up        no-reason         
         Tunnel45      --                  up        no-reason         
         Tunnel46      --                  up        no-reason         
         Tunnel47      --                  up        no-reason         
            '''}

    golden_parsed_output_4 = {
        "interfaces": {
            "mgmt0": {
                "status": "connected",
                "vlan": "routed",
                "duplex_code": "full",
                "port_speed": "1G"
            },
            "Ethernet1/1": {
                "status": "sfpabsent",
                "vlan": "trunk",
                "duplex_code": "full",
                "port_speed": "inherit"
            },
            "Ethernet1/2": {
                "status": "sfpabsent",
                "vlan": "trunk",
                "duplex_code": "full",
                "port_speed": "inherit"
            },
            "Ethernet1/3": {
                "status": "sfpabsent",
                "vlan": "trunk",
                "duplex_code": "full",
                "port_speed": "inherit"
            },
            "Ethernet1/4": {
                "status": "sfpabsent",
                "vlan": "trunk",
                "duplex_code": "full",
                "port_speed": "inherit"
            },
            "Ethernet1/5": {
                "status": "sfpabsent",
                "vlan": "trunk",
                "duplex_code": "full",
                "port_speed": "inherit"
            },
            "Ethernet1/6": {
                "status": "sfpabsent",
                "vlan": "trunk",
                "duplex_code": "full",
                "port_speed": "inherit"
            },
            "Ethernet1/7": {
                "status": "sfpabsent",
                "vlan": "trunk",
                "duplex_code": "full",
                "port_speed": "inherit"
            },
            "Ethernet1/8": {
                "status": "sfpabsent",
                "vlan": "trunk",
                "duplex_code": "full",
                "port_speed": "inherit"
            },
            "Ethernet1/9": {
                "status": "sfpabsent",
                "vlan": "trunk",
                "duplex_code": "full",
                "port_speed": "inherit"
            },
            "Ethernet1/10": {
                "status": "sfpabsent",
                "vlan": "trunk",
                "duplex_code": "full",
                "port_speed": "inherit"
            },
            "Ethernet1/11": {
                "status": "sfpabsent",
                "vlan": "trunk",
                "duplex_code": "full",
                "port_speed": "inherit"
            },
            "Ethernet1/12": {
                "status": "sfpabsent",
                "vlan": "trunk",
                "duplex_code": "full",
                "port_speed": "inherit"
            },
            "Ethernet1/13": {
                "status": "sfpabsent",
                "vlan": "trunk",
                "duplex_code": "full",
                "port_speed": "inherit"
            },
            "Ethernet1/14": {
                "status": "sfpabsent",
                "vlan": "trunk",
                "duplex_code": "full",
                "port_speed": "inherit"
            },
            "Ethernet1/15": {
                "status": "sfpabsent",
                "vlan": "trunk",
                "duplex_code": "full",
                "port_speed": "inherit"
            },
            "Ethernet1/16": {
                "status": "sfpabsent",
                "vlan": "trunk",
                "duplex_code": "full",
                "port_speed": "inherit"
            },
            "Ethernet1/17": {
                "status": "sfpabsent",
                "vlan": "trunk",
                "duplex_code": "full",
                "port_speed": "inherit"
            },
            "Ethernet1/18": {
                "status": "sfpabsent",
                "vlan": "trunk",
                "duplex_code": "full",
                "port_speed": "inherit"
            },
            "Ethernet1/19": {
                "status": "sfpabsent",
                "vlan": "trunk",
                "duplex_code": "full",
                "port_speed": "inherit"
            },
            "Ethernet1/20": {
                "status": "sfpabsent",
                "vlan": "trunk",
                "duplex_code": "full",
                "port_speed": "inherit"
            },
            "Ethernet1/21": {
                "status": "sfpabsent",
                "vlan": "trunk",
                "duplex_code": "full",
                "port_speed": "inherit"
            },
            "Ethernet1/22": {
                "status": "sfpabsent",
                "vlan": "trunk",
                "duplex_code": "full",
                "port_speed": "inherit"
            },
            "Ethernet1/23": {
                "status": "out-of-ser",
                "vlan": "trunk",
                "duplex_code": "full",
                "port_speed": "40G",
                "type": "QSFP-40G-SR-BD"
            },
            "Ethernet1/24": {
                "status": "notconnect",
                "vlan": "trunk",
                "duplex_code": "full",
                "port_speed": "inherit",
                "type": "QSFP-40G-SR-BD"
            },
            "Ethernet1/25": {
                "status": "sfpabsent",
                "vlan": "routed",
                "duplex_code": "full",
                "port_speed": "inherit"
            },
            "Ethernet1/25.1": {
                "status": "parentdown",
                "vlan": "routed",
                "duplex_code": "full",
                "port_speed": "inherit"
            },
            "Ethernet1/26": {
                "status": "sfpabsent",
                "vlan": "routed",
                "duplex_code": "full",
                "port_speed": "inherit"
            },
            "Ethernet1/26.2": {
                "status": "parentdown",
                "vlan": "routed",
                "duplex_code": "full",
                "port_speed": "inherit"
            },
            "Ethernet1/27": {
                "status": "sfpabsent",
                "vlan": "routed",
                "duplex_code": "full",
                "port_speed": "inherit"
            },
            "Ethernet1/27.3": {
                "status": "parentdown",
                "vlan": "routed",
                "duplex_code": "full",
                "port_speed": "inherit"
            },
            "Ethernet1/28": {
                "status": "sfpabsent",
                "vlan": "routed",
                "duplex_code": "full",
                "port_speed": "inherit"
            },
            "Ethernet1/28.4": {
                "status": "parentdown",
                "vlan": "routed",
                "duplex_code": "full",
                "port_speed": "inherit"
            },
            "Ethernet1/29": {
                "status": "sfpabsent",
                "vlan": "routed",
                "duplex_code": "full",
                "port_speed": "inherit"
            },
            "Ethernet1/29.5": {
                "status": "parentdown",
                "vlan": "routed",
                "duplex_code": "full",
                "port_speed": "inherit"
            },
            "Ethernet1/30": {
                "status": "sfpabsent",
                "vlan": "routed",
                "duplex_code": "full",
                "port_speed": "inherit"
            },
            "Ethernet1/30.6": {
                "status": "parentdown",
                "vlan": "routed",
                "duplex_code": "full",
                "port_speed": "inherit"
            },
            "Ethernet1/31": {
                "status": "connected",
                "vlan": "routed",
                "duplex_code": "full",
                "port_speed": "100G",
                "type": "QSFP-40/100-SRBD"
            },
            "Ethernet1/31.21": {
                "status": "connected",
                "vlan": "routed",
                "duplex_code": "full",
                "port_speed": "100G",
                "type": "QSFP-40/100-SRBD"
            },
            "Ethernet1/32": {
                "status": "connected",
                "vlan": "routed",
                "duplex_code": "full",
                "port_speed": "100G",
                "type": "QSFP-40/100-SRBD"
            },
            "Ethernet1/32.22": {
                "status": "connected",
                "vlan": "routed",
                "duplex_code": "full",
                "port_speed": "100G",
                "type": "QSFP-40/100-SRBD"
            },
            "Loopback0": {
                "status": "connected",
                "vlan": "routed",
                "duplex_code": "auto"
            },
            "Loopback1": {
                "status": "connected",
                "vlan": "routed",
                "duplex_code": "auto"
            },
            "Loopback1023": {
                "status": "connected",
                "vlan": "routed",
                "duplex_code": "auto"
            },
            "Tunnel7": {"status": "up", "reason": "no-reason"},
            "Tunnel8": {"status": "up", "reason": "no-reason"},
            "Tunnel36": {"status": "up", "reason": "no-reason"},
            "Tunnel37": {"status": "up", "reason": "no-reason"},
            "Tunnel38": {"status": "up", "reason": "no-reason"},
            "Tunnel39": {"status": "up", "reason": "no-reason"},
            "Tunnel40": {"status": "up", "reason": "no-reason"},
            "Tunnel41": {"status": "up", "reason": "no-reason"},
            "Tunnel42": {"status": "up", "reason": "no-reason"},
            "Tunnel43": {"status": "up", "reason": "no-reason"},
            "Tunnel44": {"status": "up", "reason": "no-reason"},
            "Tunnel45": {"status": "up", "reason": "no-reason"},
            "Tunnel46": {"status": "up", "reason": "no-reason"},
            "Tunnel47": {"status": "up", "reason": "no-reason"}
        }
    }

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowInterfaceStatus(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = ShowInterfaceStatus(device=self.device)
        parsed_output = obj.parse()
        self.maxDiff = None
        self.assertEqual(parsed_output, self.golden_parsed_output)

    def test_golden_interface(self):
        self.device = Mock(**self.golden_interface_output)
        obj = ShowInterfaceStatus(device=self.device)
        parsed_output = obj.parse(interface='Eth1/1')
        self.maxDiff = None
        self.assertEqual(parsed_output, self.golden_parsed_interface_output)

    def test_golden_2(self):
        self.device = Mock(**self.golden_output_2)
        obj = ShowInterfaceStatus(device=self.device)
        parsed_output = obj.parse(interface='Eth1/1')
        self.maxDiff = None
        self.assertEqual(parsed_output, self.golden_parsed_output_2)

    def test_golden_3(self):
        self.device = Mock(**self.golden_output_3)
        obj = ShowInterfaceStatus(device=self.device)
        parsed_output = obj.parse()
        self.maxDiff = None
        self.assertEqual(parsed_output, self.golden_parsed_output_3)

    def test_golden_4(self):
        self.device = Mock(**self.golden_output_4)
        obj = ShowInterfaceStatus(device=self.device)
        parsed_output = obj.parse()
        self.maxDiff = None
        self.assertEqual(parsed_output, self.golden_parsed_output_4)


# ===========================================
# Unit test for 'show interface capabilities'
# ===========================================
class TestShowInterfaceCapabilities(unittest.TestCase):
    '''unit test for "show lldp all'''
    device = Device(name='aDevice')

    empty_output = {'execute.return_value': ''}

    golden_output = {'execute.return_value': '''
        Ethernet1/4
            Model:                 N9K-C93108TC-EX
            Type (Non SFP):        10g
            Speed:                 100,1000,10000
            Duplex:                full
            Trunk encap. type:     802.1Q
            Channel:               yes
            Broadcast suppression: percentage(0-100)
            Flowcontrol:           rx-(off/on),tx-(off/on)
            Rate mode:             dedicated
            Port mode:             Routed,Switched
            QOS scheduling:        rx-(8q2t),tx-(7q)
            CoS rewrite:           yes
            ToS rewrite:           yes
            SPAN:                  yes
            UDLD:                  yes
            MDIX:                  yes
            TDR capable:           no
            Link Debounce:         yes
            Link Debounce Time:    yes
            FEX Fabric:            yes
            dot1Q-tunnel mode:     yes
            Pvlan Trunk capable:   no
            Port Group Members:    4
            EEE (efficient-eth):   no
            PFC capable:           yes
            Buffer Boost capable:  no
            Breakout capable:      no
            MACSEC capable:        no
        '''
                     }

    golden_parsed_output = {
        "Ethernet1/4": {
            "model": "N9K-C93108TC-EX",
            "sfp": False,
            "type": "10g",
            "speed": [100, 1000, 10000],
            "duplex": "full",
            "trunk_encap_type": "802.1Q",
            "channel": "yes",
            "broadcast_suppression": {"type": "percentage", "value": "0-100"},
            "flowcontrol": {"rx": "off/on", "tx": "off/on"},
            "rate_mode": "dedicated",
            "port_mode": "Routed,Switched",
            "qos_scheduling": {"rx": "8q2t", "tx": "7q"},
            "cos_rewrite": "yes",
            "tos_rewrite": "yes",
            "span": "yes",
            "udld": "yes",
            "mdix": "yes",
            "tdr_capable": "no",
            "link_debounce": "yes",
            "link_debounce_time": "yes",
            "fex_fabric": "yes",
            "dot1q_tunnel_mode": "yes",
            "pvlan_trunk_capable": "no",
            "port_group_members": 4,
            "eee_efficient_eth": "no",
            "pfc_capable": "yes",
            "buffer_boost_capable": "no",
            "breakout_capable": "no",
            "macsec_capable": "no",
        }
    }

    golden_output_1 = {'execute.return_value': '''
        Ethernet1/1/1
            Model:                 N9K-C9236C
            Type (SFP capable):    QSFP-100G-CR4
            Speed:                 1000,10000
            Duplex:                full
            Trunk encap. type:     802.1Q
            Channel:               yes
            Broadcast suppression: percentage(0-100)
            Flowcontrol:           rx-(off/on),tx-(off/on)
            Rate mode:             dedicated
            Port mode:             Routed,Switched
            QOS scheduling:        rx-(8q2t),tx-(7q)
            CoS rewrite:           yes
            ToS rewrite:           yes
            SPAN:                  yes
            UDLD:                  yes
            MDIX:                  no
            TDR capable:           no
            Link Debounce:         yes
            Link Debounce Time:    yes
            FEX Fabric:            no
            dot1Q-tunnel mode:     no
            Pvlan Trunk capable:   no
            Port Group Members:    1
            EEE (efficient-eth):   no
            PFC capable:           yes
            Buffer Boost capable:  no
            Breakout capable:      no
            MACSEC capable:        no

        Ethernet1/3
            Model:                 N9K-C93108TC-EX
            Type (Non SFP):        10g
            Speed:                 100,1000,10000
            Duplex:                full
            Trunk encap. type:     802.1Q
            Channel:               yes
            Broadcast suppression: percentage(0-100)
            Flowcontrol:           rx-(off/on),tx-(off/on)
            Rate mode:             dedicated
            Port mode:             Routed,Switched
            QOS scheduling:        rx-(8q2t),tx-(7q)
            CoS rewrite:           yes
            ToS rewrite:           yes
            SPAN:                  yes
            UDLD:                  yes
            MDIX:                  yes
            TDR capable:           no
            Link Debounce:         yes
            Link Debounce Time:    yes
            FEX Fabric:            yes
            dot1Q-tunnel mode:     yes
            Pvlan Trunk capable:   no
            Port Group Members:    3
            EEE (efficient-eth):   no
            PFC capable:           yes
            Buffer Boost capable:  no
            Breakout capable:      no
            MACSEC capable:        no
          
        Ethernet1/17
            Model:                 N9K-C9236C
            Type (SFP capable):    QSFP-100G-AOC1M
            Speed:                 1000,10000,25000,40000,50000,100000
            Duplex:                full
            Trunk encap. type:     802.1Q
            Channel:               yes
            Broadcast suppression: percentage(0-100)
            Flowcontrol:           rx-(off/on),tx-(off/on)
            Rate mode:             dedicated
            Port mode:             Routed,Switched
            QOS scheduling:        rx-(8q2t),tx-(7q)
            CoS rewrite:           yes
            ToS rewrite:           yes
            SPAN:                  yes
            UDLD:                  yes
            MDIX:                  no
            TDR capable:           no
            Link Debounce:         yes
            Link Debounce Time:    yes
            FEX Fabric:            no
            dot1Q-tunnel mode:     no
            Pvlan Trunk capable:   no
            Port Group Members:    17
            EEE (efficient-eth):   no
            PFC capable:           yes
            Buffer Boost capable:  no
            Breakout capable:      yes
            MACSEC capable:        no
        '''
                       }

    golden_parsed_output_1 = {
        "Ethernet1/1/1": {
            "model": "N9K-C9236C",
            "sfp": True,
            "type": "QSFP-100G-CR4",
            "speed": [1000, 10000],
            "duplex": "full",
            "trunk_encap_type": "802.1Q",
            "channel": "yes",
            "broadcast_suppression": {"type": "percentage", "value": "0-100"},
            "flowcontrol": {"rx": "off/on", "tx": "off/on"},
            "rate_mode": "dedicated",
            "port_mode": "Routed,Switched",
            "qos_scheduling": {"rx": "8q2t", "tx": "7q"},
            "cos_rewrite": "yes",
            "tos_rewrite": "yes",
            "span": "yes",
            "udld": "yes",
            "mdix": "no",
            "tdr_capable": "no",
            "link_debounce": "yes",
            "link_debounce_time": "yes",
            "fex_fabric": "no",
            "dot1q_tunnel_mode": "no",
            "pvlan_trunk_capable": "no",
            "port_group_members": 1,
            "eee_efficient_eth": "no",
            "pfc_capable": "yes",
            "buffer_boost_capable": "no",
            "breakout_capable": "no",
            "macsec_capable": "no",
        },
        "Ethernet1/3": {
            "model": "N9K-C93108TC-EX",
            "sfp": False,
            "type": "10g",
            "speed": [100, 1000, 10000],
            "duplex": "full",
            "trunk_encap_type": "802.1Q",
            "channel": "yes",
            "broadcast_suppression": {"type": "percentage", "value": "0-100"},
            "flowcontrol": {"rx": "off/on", "tx": "off/on"},
            "rate_mode": "dedicated",
            "port_mode": "Routed,Switched",
            "qos_scheduling": {"rx": "8q2t", "tx": "7q"},
            "cos_rewrite": "yes",
            "tos_rewrite": "yes",
            "span": "yes",
            "udld": "yes",
            "mdix": "yes",
            "tdr_capable": "no",
            "link_debounce": "yes",
            "link_debounce_time": "yes",
            "fex_fabric": "yes",
            "dot1q_tunnel_mode": "yes",
            "pvlan_trunk_capable": "no",
            "port_group_members": 3,
            "eee_efficient_eth": "no",
            "pfc_capable": "yes",
            "buffer_boost_capable": "no",
            "breakout_capable": "no",
            "macsec_capable": "no",
        },
        "Ethernet1/17": {
            "model": "N9K-C9236C",
            "sfp": True,
            "type": "QSFP-100G-AOC1M",
            "speed": [1000, 10000, 25000, 40000, 50000, 100000],
            "duplex": "full",
            "trunk_encap_type": "802.1Q",
            "channel": "yes",
            "broadcast_suppression": {"type": "percentage", "value": "0-100"},
            "flowcontrol": {"rx": "off/on", "tx": "off/on"},
            "rate_mode": "dedicated",
            "port_mode": "Routed,Switched",
            "qos_scheduling": {"rx": "8q2t", "tx": "7q"},
            "cos_rewrite": "yes",
            "tos_rewrite": "yes",
            "span": "yes",
            "udld": "yes",
            "mdix": "no",
            "tdr_capable": "no",
            "link_debounce": "yes",
            "link_debounce_time": "yes",
            "fex_fabric": "no",
            "dot1q_tunnel_mode": "no",
            "pvlan_trunk_capable": "no",
            "port_group_members": 17,
            "eee_efficient_eth": "no",
            "pfc_capable": "yes",
            "buffer_boost_capable": "no",
            "breakout_capable": "yes",
            "macsec_capable": "no",
        },
    }

    def test_empty(self):
        self.maxDiff = None
        self.device = Mock(**self.empty_output)
        obj = ShowInterfaceCapabilities(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output)
        obj = ShowInterfaceCapabilities(device=self.device)
        parsed_output = obj.parse(interface='Ethernet1/4')

        self.assertEqual(parsed_output, self.golden_parsed_output)

    def test_golden2(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_1)
        obj = ShowInterfaceCapabilities(device=self.device)
        parsed_output = obj.parse()

        self.assertEqual(parsed_output, self.golden_parsed_output_1)


# ===========================================
# Unit test for 'show interface transceiver'
# ===========================================
class TestShowInterfaceTransceiver(unittest.TestCase):
    '''unit test for "show interface transceiver'''
    device = Device(name='aDevice')

    empty_output = {'execute.return_value': ''}

    golden_output = {'execute.return_value': '''
        Ethernet1/4
            transceiver is present
            type is QSFP-40G-CR4
            name is CISCO-TYCO
            part number is 2821248-5
            revision is D
            serial number is TED2318K229-B
            nominal bitrate is 10300 MBit/sec per channel
            Link length supported for copper is 3 m
            cisco id is 13
            cisco extended id number is 16
            cisco part number is 37-1317-03
            cisco product id is QSFP-H40G-CU3M
            cisco version id is V03
        '''
                     }

    golden_parsed_output = {
        'Ethernet1/4': {'cis_part_number': '37-1317-03',
                        'cis_product_id': 'QSFP-H40G-CU3M',
                        'cis_version_id': 'V03',
                        'cisco_id': '13',
                        'name': 'CISCO-TYCO',
                        'nominal_bitrate': 10300,
                        'part_number': '2821248-5',
                        'revision': 'D',
                        'serial_number': 'TED2318K229-B',
                        'transceiver_present': True,
                        'transceiver_type': 'QSFP-40G-CR4'
                        }
    }

    golden_output_1 = {'execute.return_value': '''
        Ethernet1/2
            transceiver is present
            type is QSFP-DD-400G-COPPER
            name is CISCO-LEONI
            part number is L45593-K218-C20
            revision is 00
            serial number is LCC2411GC93-A
            nominal bitrate is 425000 MBit/sec per channel
            cisco id is 0x18
            cisco part number is 37-1843-01
            cisco product id is QDD-400-CU2M
            cisco version id is V01
            vendor OUI is a8b0ae
            date code is 20031400
            clei code is CMPQAGSCAA
            power class is 1 (1.5 W maximum)
            max power is 1.50 W
            cable attenuation is 0/0/0/0/0 dB for bands 5/7/12.9/25.8/56 GHz
            near-end lanes used none
            far-end lane code for 8 lanes aaaaaaaa
            media interface is copper cable unequalized
            Advertising code is Passive Cu
            Host electrical interface code is 200GAUI-4 C2M (Annex 120E)
            Cable Length is   2.0 M
            CMIS version is  4
        
        '''
                       }

    golden_parsed_output_1 = {
        'Ethernet1/2': {'advertising_code': 'Passive Cu',
                        'cable_attenuation': '0/0/0/0/0 dB for bands 5/7/12.9/25.8/56 '
                                             'GHz',
                        'cable_length': 2.0,
                        'cis_part_number': '37-1843-01',
                        'cis_product_id': 'QDD-400-CU2M',
                        'cis_version_id': 'V01',
                        'cisco_id': '0x18',
                        'clei': 'CMPQAGSCAA',
                        'cmis_ver': 4,
                        'date_code': '20031400',
                        'far_end_lanes': '8 lanes aaaaaaaa',
                        'host_electrical_intf': '200GAUI-4 C2M (Annex 120E)',
                        'max_power': 1.5,
                        'media_interface': 'copper cable unequalized',
                        'name': 'CISCO-LEONI',
                        'near_end_lanes': 'none',
                        'nominal_bitrate': 425000,
                        'part_number': 'L45593-K218-C20',
                        'power_class': '1 (1.5 W maximum)',
                        'revision': '00',
                        'serial_number': 'LCC2411GC93-A',
                        'vendor_oui': 'a8b0ae',
                        'transceiver_present': True,
                        'transceiver_type': 'QSFP-DD-400G-COPPER'
                        }
    }

    golden_output_2 = {'execute.return_value': '''
        Ethernet1/1
            transceiver is present
            type is QSFP-DD-400G-COPPER
            name is CISCO-LEONI
            part number is L45593-K218-C20
            revision is 00
            serial number is LCC2411GG1W-A
            nominal bitrate is 425000 MBit/sec per channel
            cisco id is 0x18
            cisco part number is 37-1843-01
            cisco product id is QDD-400-CU2M
            cisco version id is V01
            vendor OUI is a8b0ae
            date code is 20031400
            clei code is CMPQAGSCAA
            power class is 1 (1.5 W maximum)
            max power is 1.50 W
            cable attenuation is 0/0/0/0/0 dB for bands 5/7/12.9/25.8/56 GHz
            near-end lanes used none
            far-end lane code for 8 lanes aaaaaaaa
            media interface is copper cable unequalized
            Advertising code is Passive Cu
            Host electrical interface code is 200GAUI-4 C2M (Annex 120E)
            Cable Length is   2.0 M
            CMIS version is  4

        Ethernet1/30
            transceiver is present
            type is QSFP-40G-CR4
            name is CISCO-TYCO
            part number is 2821248-5
            revision is D
            serial number is TED2318K1QR-B
            nominal bitrate is 10300 MBit/sec per channel
            Link length supported for copper is 3 m
            cisco id is 13
            cisco extended id number is 16
            cisco part number is 37-1317-03
            cisco product id is QSFP-H40G-CU3M
            cisco version id is V03

        Ethernet1/52
            transceiver is present
            type is QSFP-DD-400G-FR4
            name is CISCO-INNOLIGHT
            part number is T-DQ4CNT-NCI
            revision is 2B
            serial number is INL24265523
            nominal bitrate is 425000 MBit/sec per channel
            cisco id is 0x18
            cisco part number is 10-3321-01
            cisco product id is QDD-400G-FR4-S
            cisco version id is V01
            firmware version is 204.154
            Link length SMF is 2 km
            Nominal transmitter wavelength is 1301.00 nm
            Wavelength tolerance is 6.500 nm
            host lane count is 8
            media lane count is 4
            max module temperature is 75 deg C
            min module temperature is 0 deg C
            min operational voltage is 3.14 V
            vendor OUI is 447c7f
            date code is 200627
            clei code is CMUIAUNCAA
            power class is 6 (12.0 W maximum)
            max power is 12.00 W
            near-end lanes used none
            far-end lane code for 8 lanes Undefined
            media interface is 1310 nm EML
            Advertising code is Optical Interfaces: SMF
            Host electrical interface code is 400GAUI-8 C2M (Annex 120E)
            media interface advertising code is 400G-FR4

        Ethernet1/56
            transceiver is not present

        Ethernet1/63
            transceiver is present
            type is QSFP-DD-400G-DR4
            name is CISCO-INNOLIGHT
            part number is T-DP4CNH-NCI
            revision is 2B
            serial number is INL24173669
            nominal bitrate is 425000 MBit/sec per channel
            cisco id is 0x18
            cisco part number is 10-3320-01
            cisco product id is QDD-400G-DR4-S
            cisco version id is V01
            firmware version is 204.154
            Link length SMF is 0.5 km
            Nominal transmitter wavelength is 1311.00 nm
            Wavelength tolerance is 6.500 nm
            host lane count is 8
            media lane count is 4
            max module temperature is 75 deg C
            min module temperature is 0 deg C
            min operational voltage is 3.14 V
            vendor OUI is 447c7f
            date code is 200422
            clei code is CMUIAUPCAA
            power class is 6 (12.0 W maximum)
            max power is 12.00 W
            near-end lanes used none
            far-end lane code for 8 lanes Undefined
            media interface is 1310 nm EML
            Advertising code is Optical Interfaces: SMF
            Host electrical interface code is 400GAUI-8 C2M (Annex 120E)
            media interface advertising code is 400GBASE-DR4 (Cl 124)
        '''
                       }

    golden_parsed_output_2 = {
        "Ethernet1/1": {
            "advertising_code": "Passive Cu",
            "cable_attenuation": "0/0/0/0/0 dB for bands 5/7/12.9/25.8/56 " "GHz",
            "cable_length": 2.0,
            "cis_part_number": "37-1843-01",
            "cis_product_id": "QDD-400-CU2M",
            "cis_version_id": "V01",
            "cisco_id": "0x18",
            "clei": "CMPQAGSCAA",
            "cmis_ver": 4,
            "date_code": "20031400",
            "far_end_lanes": "8 lanes aaaaaaaa",
            "host_electrical_intf": "200GAUI-4 C2M (Annex 120E)",
            "max_power": 1.5,
            "media_interface": "copper cable unequalized",
            "name": "CISCO-LEONI",
            "near_end_lanes": "none",
            "nominal_bitrate": 425000,
            "part_number": "L45593-K218-C20",
            "power_class": "1 (1.5 W maximum)",
            "revision": "00",
            "serial_number": "LCC2411GG1W-A",
            "vendor_oui": "a8b0ae",
            "transceiver_present": True,
            "transceiver_type": "QSFP-DD-400G-COPPER",
        },
        "Ethernet1/30": {
            "cis_part_number": "37-1317-03",
            "cis_product_id": "QSFP-H40G-CU3M",
            "cis_version_id": "V03",
            "cisco_id": "13",
            "name": "CISCO-TYCO",
            "nominal_bitrate": 10300,
            "part_number": "2821248-5",
            "revision": "D",
            "serial_number": "TED2318K1QR-B",
            "transceiver_present": True,
            "transceiver_type": "QSFP-40G-CR4",
        },
        "Ethernet1/52": {
            "advertising_code": "Optical Interfaces: SMF",
            "cis_part_number": "10-3321-01",
            "cis_product_id": "QDD-400G-FR4-S",
            "cis_version_id": "V01",
            "cisco_id": "0x18",
            "clei": "CMUIAUNCAA",
            "date_code": "200627",
            "far_end_lanes": "8 lanes Undefined",
            "firmware_ver": "204.154",
            "host_electrical_intf": "400GAUI-8 C2M (Annex 120E)",
            "host_lane_count": 8,
            "link_length": "2 km",
            "max_mod_temp": 75,
            "max_power": 12.0,
            "media_interface": "1310 nm EML",
            "media_interface_advert_code": "400G-FR4",
            "media_lane_count": 4,
            "min_mod_temp": 0,
            "min_oper_volt": "3.14 V",
            "name": "CISCO-INNOLIGHT",
            "near_end_lanes": "none",
            "nominal_bitrate": 425000,
            "nominal_trans_wavelength": "1301.00 nm",
            "part_number": "T-DQ4CNT-NCI",
            "power_class": "6 (12.0 W maximum)",
            "revision": "2B",
            "serial_number": "INL24265523",
            "vendor_oui": "447c7f",
            "wavelength_tolerance": "6.500 nm",
            "transceiver_present": True,
            "transceiver_type": "QSFP-DD-400G-FR4",
        },
        "Ethernet1/56": {
            "transceiver_present": False
        },
        "Ethernet1/63": {
            "advertising_code": "Optical Interfaces: SMF",
            "cis_part_number": "10-3320-01",
            "cis_product_id": "QDD-400G-DR4-S",
            "cis_version_id": "V01",
            "cisco_id": "0x18",
            "clei": "CMUIAUPCAA",
            "date_code": "200422",
            "far_end_lanes": "8 lanes Undefined",
            "firmware_ver": "204.154",
            "host_electrical_intf": "400GAUI-8 C2M (Annex 120E)",
            "host_lane_count": 8,
            "link_length": "0.5 km",
            "max_mod_temp": 75,
            "max_power": 12.0,
            "media_interface": "1310 nm EML",
            "media_interface_advert_code": "400GBASE-DR4 (Cl 124)",
            "media_lane_count": 4,
            "min_mod_temp": 0,
            "min_oper_volt": "3.14 V",
            "name": "CISCO-INNOLIGHT",
            "near_end_lanes": "none",
            "nominal_bitrate": 425000,
            "nominal_trans_wavelength": "1311.00 nm",
            "part_number": "T-DP4CNH-NCI",
            "power_class": "6 (12.0 W maximum)",
            "revision": "2B",
            "serial_number": "INL24173669",
            "vendor_oui": "447c7f",
            "wavelength_tolerance": "6.500 nm",
            "transceiver_present": True,
            "transceiver_type": "QSFP-DD-400G-DR4",
        },
    }

    def test_empty(self):
        self.maxDiff = None
        self.device = Mock(**self.empty_output)
        obj = ShowInterfaceTransceiver(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output)
        obj = ShowInterfaceTransceiver(device=self.device)
        parsed_output = obj.parse(interface='Ethernet1/4')

        self.assertEqual(parsed_output, self.golden_parsed_output)

    def test_golden2(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_1)
        obj = ShowInterfaceTransceiver(device=self.device)
        parsed_output = obj.parse(interface='Ethernet1/2')

        self.assertEqual(parsed_output, self.golden_parsed_output_1)

    def test_golden3(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_2)
        obj = ShowInterfaceTransceiver(device=self.device)
        parsed_output = obj.parse()

        self.assertEqual(parsed_output, self.golden_parsed_output_2)


# ===========================================
# Unit test for 'show interface fec'
# ===========================================
class TestShowInterfaceFec(unittest.TestCase):
    '''unit test for "show interface fec'''
    device = Device(name='aDevice')

    empty_output = {'execute.return_value': ''}

    golden_output = {'execute.return_value': '''
        --------------------------------------------------------------------------------
        Name          Ifindex       Admin-fec Oper-fec  Status    Speed   Type
        --------------------------------------------------------------------------------
        Eth1/1        0x1a000000    auto      auto      disabled  auto    QSFP-DD-400G-COPPER
        Eth1/2        0x1a000200    auto      auto      disabled  auto    QSFP-DD-400G-COPPER
        Eth1/3        0x1a000400    auto      auto      disabled  auto    QSFP-40G-CR4
        Eth1/4        0x1a000600    auto      auto      disabled  auto    QSFP-40G-CR4
        Eth1/5        0x1a000800    auto      auto      disabled  auto    QSFP-100G-CR4
        Eth1/6        0x1a000a00    auto      auto      disabled  auto    QSFP-100G-AOC15M
        Eth1/7        0x1a000c00    auto      auto      disabled  auto    QSFP-40G-CR4
        Eth1/8        0x1a000e00    auto      auto      disabled  auto    QSFP-40G-CR4
        Eth1/9        0x1a001000    auto      auto      disabled  auto    QSFP-40G-CR4
        Eth1/10       0x1a001200    auto      auto      disabled  auto    QSFP-40G-CR4
        '''
                     }

    golden_parsed_output = {
        "Eth1/1": {
            "admin-fec": "auto",
            "ifindex": "0x1a000000",
            "oper-fec": "auto",
            "speed": "auto",
            "status": "disabled",
            "type": "QSFP-DD-400G-COPPER",
        },
        "Eth1/10": {
            "admin-fec": "auto",
            "ifindex": "0x1a001200",
            "oper-fec": "auto",
            "speed": "auto",
            "status": "disabled",
            "type": "QSFP-40G-CR4",
        },
        "Eth1/2": {
            "admin-fec": "auto",
            "ifindex": "0x1a000200",
            "oper-fec": "auto",
            "speed": "auto",
            "status": "disabled",
            "type": "QSFP-DD-400G-COPPER",
        },
        "Eth1/3": {
            "admin-fec": "auto",
            "ifindex": "0x1a000400",
            "oper-fec": "auto",
            "speed": "auto",
            "status": "disabled",
            "type": "QSFP-40G-CR4",
        },
        "Eth1/4": {
            "admin-fec": "auto",
            "ifindex": "0x1a000600",
            "oper-fec": "auto",
            "speed": "auto",
            "status": "disabled",
            "type": "QSFP-40G-CR4",
        },
        "Eth1/5": {
            "admin-fec": "auto",
            "ifindex": "0x1a000800",
            "oper-fec": "auto",
            "speed": "auto",
            "status": "disabled",
            "type": "QSFP-100G-CR4",
        },
        "Eth1/6": {
            "admin-fec": "auto",
            "ifindex": "0x1a000a00",
            "oper-fec": "auto",
            "speed": "auto",
            "status": "disabled",
            "type": "QSFP-100G-AOC15M",
        },
        "Eth1/7": {
            "admin-fec": "auto",
            "ifindex": "0x1a000c00",
            "oper-fec": "auto",
            "speed": "auto",
            "status": "disabled",
            "type": "QSFP-40G-CR4",
        },
        "Eth1/8": {
            "admin-fec": "auto",
            "ifindex": "0x1a000e00",
            "oper-fec": "auto",
            "speed": "auto",
            "status": "disabled",
            "type": "QSFP-40G-CR4",
        },
        "Eth1/9": {
            "admin-fec": "auto",
            "ifindex": "0x1a001000",
            "oper-fec": "auto",
            "speed": "auto",
            "status": "disabled",
            "type": "QSFP-40G-CR4",
        },
    }

    def test_empty(self):
        self.maxDiff = None
        self.device = Mock(**self.empty_output)
        obj = ShowInterfaceTransceiverDetails(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output)
        obj = ShowInterfaceFec(device=self.device)
        parsed_output = obj.parse()

        self.assertEqual(parsed_output, self.golden_parsed_output)


# ===========================================
# Unit test for 'show interface hardware-mappings'
# ===========================================
class TestShowInterfaceHardwareMap(unittest.TestCase):
    '''unit test for "show interface hardware-mappings'''
    device = Device(name='aDevice')

    empty_output = {'execute.return_value': ''}

    golden_output = {'execute.return_value': '''
        -------------------------------------------------------------------------------------------------------
        Name       Ifindex  Smod Unit HPort FPort NPort VPort Slice SPort SrcId MacId MacSP VIF  Block BlkSrcID
        -------------------------------------------------------------------------------------------------------
        Eth1/1/1   38000000 1    0    16    255   0     -1    0     16    32    4     0     1544 0     32
        Eth1/1/2   38001000 1    0    17    255   1     -1    0     17    34    4     2     1544 0     34
        Eth1/1/3   38002000 1    0    18    255   2     -1    0     18    36    4     4     3    0     36
        Eth1/1/4   38003000 1    0    19    255   3     -1    0     19    38    4     6     4    0     38
        Eth1/2/1   3800a000 1    0    12    255   4     -1    0     12    24    3     0     1544 0     24
        Eth1/2/2   3800b000 1    0    13    255   5     -1    0     13    26    3     2     6    0     26
        Eth1/2/3   3800c000 1    0    14    255   6     -1    0     14    28    3     4     7    0     28
        Eth1/2/4   3800d000 1    0    15    255   7     -1    0     15    30    3     6     8    0     30
        Eth1/3     1a000400 1    0    20    255   8     -1    0     20    40    5     0     9    0     40
        Eth1/4     1a000600 1    0    8     255   12    -1    0     8     16    2     0     13   0     16

        -------------------------------------------------------------------------------------------------------
        Name       Ifindex  Smod Unit HPort FPort NPort VPort Slice SPort SrcId MacId MacSP VIF  Block BlkSrcID
        -------------------------------------------------------------------------------------------------------
        Po1        16000000 0    0    1     0     54914 2     0     0     0     -1    -1    1537 0     0
        Po48       1600002f 0    0    2     0     54914 3     0     0     0     -1    -1    1538 0     0
        Po50       16000031 0    0    3     0     54914 4     0     0     0     -1    -1    1539 0     0
        Po52       16000033 0    0    4     0     54914 5     0     0     0     -1    -1    1540 0     0
        Po101      16000064 0    0    5     0     54914 6     0     0     0     -1    -1    1541 0     0
        Po102      16000065 0    0    6     0     54914 7     0     0     0     -1    -1    1542 0     0
        Po105      16000068 0    0    7     0     54914 8     0     0     0     -1    -1    1543 0     0
        Po130      16000081 0    0    8     0     54914 9     0     0     0     -1    -1    1544 0     0
        '''
                     }

    golden_parsed_output = {
        "Ethernet1/1/1": {
            "blksrcid": 32,
            "block": 0,
            "fport": 255,
            "hport": 16,
            "ifindex": "38000000",
            "macid": 4,
            "macsp": 0,
            "nport": 0,
            "slice": 0,
            "smod": 1,
            "sport": 16,
            "srcid": 32,
            "unit": 0,
            "vif": 1544,
            "vport": -1,
        },
        "Ethernet1/1/2": {
            "blksrcid": 34,
            "block": 0,
            "fport": 255,
            "hport": 17,
            "ifindex": "38001000",
            "macid": 4,
            "macsp": 2,
            "nport": 1,
            "slice": 0,
            "smod": 1,
            "sport": 17,
            "srcid": 34,
            "unit": 0,
            "vif": 1544,
            "vport": -1,
        },
        "Ethernet1/1/3": {
            "blksrcid": 36,
            "block": 0,
            "fport": 255,
            "hport": 18,
            "ifindex": "38002000",
            "macid": 4,
            "macsp": 4,
            "nport": 2,
            "slice": 0,
            "smod": 1,
            "sport": 18,
            "srcid": 36,
            "unit": 0,
            "vif": 3,
            "vport": -1,
        },
        "Ethernet1/1/4": {
            "blksrcid": 38,
            "block": 0,
            "fport": 255,
            "hport": 19,
            "ifindex": "38003000",
            "macid": 4,
            "macsp": 6,
            "nport": 3,
            "slice": 0,
            "smod": 1,
            "sport": 19,
            "srcid": 38,
            "unit": 0,
            "vif": 4,
            "vport": -1,
        },
        "Ethernet1/2/1": {
            "blksrcid": 24,
            "block": 0,
            "fport": 255,
            "hport": 12,
            "ifindex": "3800a000",
            "macid": 3,
            "macsp": 0,
            "nport": 4,
            "slice": 0,
            "smod": 1,
            "sport": 12,
            "srcid": 24,
            "unit": 0,
            "vif": 1544,
            "vport": -1,
        },
        "Ethernet1/2/2": {
            "blksrcid": 26,
            "block": 0,
            "fport": 255,
            "hport": 13,
            "ifindex": "3800b000",
            "macid": 3,
            "macsp": 2,
            "nport": 5,
            "slice": 0,
            "smod": 1,
            "sport": 13,
            "srcid": 26,
            "unit": 0,
            "vif": 6,
            "vport": -1,
        },
        "Ethernet1/2/3": {
            "blksrcid": 28,
            "block": 0,
            "fport": 255,
            "hport": 14,
            "ifindex": "3800c000",
            "macid": 3,
            "macsp": 4,
            "nport": 6,
            "slice": 0,
            "smod": 1,
            "sport": 14,
            "srcid": 28,
            "unit": 0,
            "vif": 7,
            "vport": -1,
        },
        "Ethernet1/2/4": {
            "blksrcid": 30,
            "block": 0,
            "fport": 255,
            "hport": 15,
            "ifindex": "3800d000",
            "macid": 3,
            "macsp": 6,
            "nport": 7,
            "slice": 0,
            "smod": 1,
            "sport": 15,
            "srcid": 30,
            "unit": 0,
            "vif": 8,
            "vport": -1,
        },
        "Ethernet1/3": {
            "blksrcid": 40,
            "block": 0,
            "fport": 255,
            "hport": 20,
            "ifindex": "1a000400",
            "macid": 5,
            "macsp": 0,
            "nport": 8,
            "slice": 0,
            "smod": 1,
            "sport": 20,
            "srcid": 40,
            "unit": 0,
            "vif": 9,
            "vport": -1,
        },
        "Ethernet1/4": {
            "blksrcid": 16,
            "block": 0,
            "fport": 255,
            "hport": 8,
            "ifindex": "1a000600",
            "macid": 2,
            "macsp": 0,
            "nport": 12,
            "slice": 0,
            "smod": 1,
            "sport": 8,
            "srcid": 16,
            "unit": 0,
            "vif": 13,
            "vport": -1,
        },
        "Port-channel1": {
            "blksrcid": 0,
            "block": 0,
            "fport": 0,
            "hport": 1,
            "ifindex": "16000000",
            "macid": -1,
            "macsp": -1,
            "nport": 54914,
            "slice": 0,
            "smod": 0,
            "sport": 0,
            "srcid": 0,
            "unit": 0,
            "vif": 1537,
            "vport": 2,
        },
        "Port-channel101": {
            "blksrcid": 0,
            "block": 0,
            "fport": 0,
            "hport": 5,
            "ifindex": "16000064",
            "macid": -1,
            "macsp": -1,
            "nport": 54914,
            "slice": 0,
            "smod": 0,
            "sport": 0,
            "srcid": 0,
            "unit": 0,
            "vif": 1541,
            "vport": 6,
        },
        "Port-channel102": {
            "blksrcid": 0,
            "block": 0,
            "fport": 0,
            "hport": 6,
            "ifindex": "16000065",
            "macid": -1,
            "macsp": -1,
            "nport": 54914,
            "slice": 0,
            "smod": 0,
            "sport": 0,
            "srcid": 0,
            "unit": 0,
            "vif": 1542,
            "vport": 7,
        },
        "Port-channel105": {
            "blksrcid": 0,
            "block": 0,
            "fport": 0,
            "hport": 7,
            "ifindex": "16000068",
            "macid": -1,
            "macsp": -1,
            "nport": 54914,
            "slice": 0,
            "smod": 0,
            "sport": 0,
            "srcid": 0,
            "unit": 0,
            "vif": 1543,
            "vport": 8,
        },
        "Port-channel130": {
            "blksrcid": 0,
            "block": 0,
            "fport": 0,
            "hport": 8,
            "ifindex": "16000081",
            "macid": -1,
            "macsp": -1,
            "nport": 54914,
            "slice": 0,
            "smod": 0,
            "sport": 0,
            "srcid": 0,
            "unit": 0,
            "vif": 1544,
            "vport": 9,
        },
        "Port-channel48": {
            "blksrcid": 0,
            "block": 0,
            "fport": 0,
            "hport": 2,
            "ifindex": "1600002f",
            "macid": -1,
            "macsp": -1,
            "nport": 54914,
            "slice": 0,
            "smod": 0,
            "sport": 0,
            "srcid": 0,
            "unit": 0,
            "vif": 1538,
            "vport": 3,
        },
        "Port-channel50": {
            "blksrcid": 0,
            "block": 0,
            "fport": 0,
            "hport": 3,
            "ifindex": "16000031",
            "macid": -1,
            "macsp": -1,
            "nport": 54914,
            "slice": 0,
            "smod": 0,
            "sport": 0,
            "srcid": 0,
            "unit": 0,
            "vif": 1539,
            "vport": 4,
        },
        "Port-channel52": {
            "blksrcid": 0,
            "block": 0,
            "fport": 0,
            "hport": 4,
            "ifindex": "16000033",
            "macid": -1,
            "macsp": -1,
            "nport": 54914,
            "slice": 0,
            "smod": 0,
            "sport": 0,
            "srcid": 0,
            "unit": 0,
            "vif": 1540,
            "vport": 5,
        },
    }

    def test_empty(self):
        self.maxDiff = None
        self.device = Mock(**self.empty_output)
        obj = ShowInterfaceHardwareMap(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output)
        obj = ShowInterfaceHardwareMap(device=self.device)
        parsed_output = obj.parse()
        # import pprint
        # pprint.pprint(parsed_output)

        self.assertEqual(parsed_output, self.golden_parsed_output)


if __name__ == '__main__':
    unittest.main()

# vim: ft=python et sw=4
