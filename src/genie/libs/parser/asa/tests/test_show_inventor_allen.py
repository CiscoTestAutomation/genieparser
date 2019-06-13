import re
import unittest
from unittest.mock import Mock

from ats.topology import Device

from genie.metaparser.util.exceptions import SchemaEmptyParserError

from genie.libs.parser.asa.show_inventory_allen import ShowInventory

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
            'sn': 'FGL170441BU'
        },
        'power supply 1': {
            'description': 'ASA 5545-X/5555-X AC Power Supply',
            'pid': 'ASA-PWR-AC',
            'vid': 'N/A',
            'sn': '2CS1AX'
        },
        'Storage Device 1': {
            'description': 'Micron 128 GB SSD MLC, Model Number: C400-MTFDDAC128MAM',
            'pid': 'N/A',
            'vid': 'N/A',
            'sn': 'MXA174201RR'
        },
        'module 100': {
            'description': 'WS-SVC-ASASM-1 Adaptive Security Appliance Service Module',
            'pid': 'WS-SVC-ASA-SM1',
            'vid': 'V01',
            'sn': 'SAL1234567Z'
        }
    }

    golden_output = {'execute.return_value': '''
        ciscoasa> show inventory
        Name: "Chassis", DESCR: "ASA 5555-X with SW, 8 GE Data, 1 GE Mgmt"
        PID: ASA5555, VID: V01, SN: FGL170441BU
         
        Name: "power supply 1", DESCR: "ASA 5545-X/5555-X AC Power Supply"
        PID: ASA-PWR-AC, VID: N/A, SN: 2CS1AX
         
        Name: "Storage Device 1", DESCR: "Micron 128 GB SSD MLC, Model Number: C400-MTFDDAC128MAM"
        PID: N/A, VID: N/A, SN: MXA174201RR

        Name: "module 100", DESCR: "WS-SVC-ASASM-1 Adaptive Security Appliance Service Module"
        PID: WS-SVC-ASA-SM1    , VID: V01     , SN: SAL1234567Z
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