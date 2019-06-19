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
        'Chassis': {
            'description': 'ASA 5555-X with SW, 8 GE Data, 1 GE Mgmt',
            'pid': 'ASA5555',
            'vid': 'V01',
            'sn': 'AAAAA11111'
        },
        'power supply 1': {
            'description': 'ASA 5545-X/5555-X AC Power Supply',
            'pid': 'AAA-AAA-AAA',
            'vid': 'N/A',
            'sn': 'AAA111'
        },
        'Storage Device 1': {
            'description': 'Micron 128 GB SSD MLC, Model Number: C11111-AAAAAAAA',
            'pid': 'N/A',
            'vid': 'N/A',
            'sn': 'AAAAA11111'
        },
        'module 100': {
            'description': 'WS-SVC-ASASM-1 Adaptive Security Appliance Service Module',
            'pid': 'AA-AAA-111-111',
            'vid': 'V01',
            'sn': 'AAAAA11111'
        }
    }

    golden_output = {'execute.return_value': '''
        ciscoasa> show inventory
        Name: "Chassis", DESCR: "ASA 5555-X with SW, 8 GE Data, 1 GE Mgmt"
        PID: ASA5555, VID: V01, SN: AAAAA11111
         
        Name: "power supply 1", DESCR: "ASA 5545-X/5555-X AC Power Supply"
        PID: AAA-AAA-AAA, VID: N/A, SN: AAA111
         
        Name: "Storage Device 1", DESCR: "Micron 128 GB SSD MLC, Model Number: C11111-AAAAAAAA"
        PID: N/A, VID: N/A, SN: AAAAA11111

        Name: "module 100", DESCR: "WS-SVC-ASASM-1 Adaptive Security Appliance Service Module"
        PID: AA-AAA-111-111    , VID: V01     , SN: AAAAA11111
    '''}

    def test_empty(self):
        self.device1 = Mock(**self.empty_output)
        obj = ShowInventory(device=self.device1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = ShowInventory(device=self.device)
        parsed_output = obj.parse()
        self.maxDiff = None
        self.assertEqual(parsed_output, self.golden_parsed_output)

if __name__ == '__main__':
    unittest.main()