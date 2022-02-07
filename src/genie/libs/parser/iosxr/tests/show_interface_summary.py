import unittest
from unittest.mock import Mock

from pyats.topology import Device

from genie.libs.parser.iosxr.show_interface import ShowInterfaceSummary


class test_show_interface_summary(unittest.TestCase):
    ''' Unit test for "show interface summary" '''

    device = Device(name='aDevice')

    empty_output = {'execute.return_value': ''}

    golden_parsed_output_brief = {
        "interface_types": {
            "ALL_TYPES": {
                "total": "60",
                "up": "30",
                "down": "0",
                "admin_down": "30"
            },
            "IFT_ETHERBUNDLE": {
                "total": "1",
                "up": "1",
                "down": "0",
                "admin_down": "0"
            },
            "IFT_VLAN_SUBIF": {
                "total": "28",
                "up": "19",
                "down": "0",
                "admin_down": "9"
            },
            "IFT_FORTYGETHERNET": {
                "total": "2",
                "up": "1",
                "down": "0",
                "admin_down": "1"
            },
            "IFT_HUNDREDGE": {
                "total": "4",
                "up": "3",
                "down": "0",
                "admin_down": "1"
            },
            "IFT_LOOPBACK": {
                "total": "2",
                "up": "2",
                "down": "0",
                "admin_down": "0"
            },
            "IFT_ETHERNET": {
                "total": "2",
                "up": "2",
                "down": "0",
                "admin_down": "0"
            },
            "IFT_NULL": {
                "total": "1",
                "up": "1",
                "down": "0",
                "admin_down": "0"
            },
            "IFT_TENGETHERNET": {
                "total": "20",
                "up": "1",
                "down": "0",
                "admin_down": "19"
            },
        }
    }

    golden_output_brief = {'execute.return_value': '''
Mon Feb  7 09:43:34.089 CET
Interface Type          Total    UP       Down     Admin Down
--------------          -----    --       ----     ----------
ALL TYPES               60       30       0        30
--------------
IFT_ETHERBUNDLE         1        1        0        0
IFT_VLAN_SUBIF          28       19       0        9
IFT_FORTYGETHERNET      2        1        0        1
IFT_HUNDREDGE           4        3        0        1
IFT_LOOPBACK            2        2        0        0
IFT_ETHERNET            2        2        0        0
IFT_NULL                1        1        0        0
IFT_TENGETHERNET        20       1        0        19

    '''}

    def test_show_interface_summary(self):
        self.device = Mock(**self.golden_output_brief)
        obj = ShowInterfaceSummary(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_brief)


if __name__ == '__main__':
    unittest.main()
