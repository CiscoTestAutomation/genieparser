import re
import unittest
from unittest.mock import Mock

from ats.topology import Device

from genie.metaparser.util.exceptions import SchemaEmptyParserError

from genie.libs.parser.asa.show_inventory import ShowInventory

# =============================================
# Parser for 'show inventory'
# =============================================
class test_show_inventory(unittest.TestCase):

    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output = {
         'inventory': {
            'name': 'module 2',
            'descr': 'WS-SVC-ASASM-1 Adaptive Security Appliance Service Module',
            'pid': 'WS-SVC-ASA-SM1',
            'vid': 'V02',
            'sn': 'SAL2052037Y'
        }
    }

    golden_output = {'execute.return_value': '''
        DevNet-asa-sm-1/admin# show inventory
        Name: "module 2", DESCR: "WS-SVC-ASASM-1 Adaptive Security Appliance Service Module"
        PID: WS-SVC-ASA-SM1    , VID: V02     , SN: SAL2052037Y
    '''}

    def test_empty(self):
        self.device1 = Mock(**self.empty_output)
        interface_obj = ShowInventory(device=self.device1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = interface_obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        interface_obj = ShowInventory(device=self.device)
        parsed_output = interface_obj.parse()
        self.maxDiff = None
        self.assertEqual(parsed_output, self.golden_parsed_output)

if __name__ == '__main__':
    unittest.main()