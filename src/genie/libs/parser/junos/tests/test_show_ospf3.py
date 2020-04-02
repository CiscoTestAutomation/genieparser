import unittest
from unittest.mock import Mock

from pyats.topology import Device
from pyats.topology import loader
from genie.metaparser.util.exceptions import SchemaEmptyParserError
from genie.libs.parser.junos.show_ospf3 import ShowOspf3Interface

class TestShowOspf3Interface(unittest.TestCase):

    device = Device(name='aDevice')

    empty_output = {'execute.return_value': ''}

    golden_output = {'execute.return_value': '''
        show ospf3 interface | no-more
        Interface           State   Area            DR ID           BDR ID          Nbrs
        ge-0/0/0.0          PtToPt  0.0.0.8         0.0.0.0         0.0.0.0            1
        ge-0/0/1.0          PtToPt  0.0.0.8         0.0.0.0         0.0.0.0            1
        lo0.0               DR      0.0.0.8         10.189.5.252    0.0.0.0            0
    '''}

    golden_parsed_output = {
            "ospf3-interface-information": {
                "ospf3-interface": [
                    {
                        "bdr-id": "0.0.0.0",
                        "dr-id": "0.0.0.0",
                        "interface-name": "ge-0/0/0.0",
                        "neighbor-count": "1",
                        "ospf-area": "0.0.0.8",
                        "ospf-interface-state": "PtToPt"
                    },
                    {
                        "bdr-id": "0.0.0.0",
                        "dr-id": "0.0.0.0",
                        "interface-name": "ge-0/0/1.0",
                        "neighbor-count": "1",
                        "ospf-area": "0.0.0.8",
                        "ospf-interface-state": "PtToPt"
                    },
                    {
                        "bdr-id": "0.0.0.0",
                        "dr-id": "10.189.5.252",
                        "interface-name": "lo0.0",
                        "neighbor-count": "0",
                        "ospf-area": "0.0.0.8",
                        "ospf-interface-state": "DR"
                    }
                ]
            }
        }

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowOspf3Interface(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = ShowOspf3Interface(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)

if __name__ == '__main__':
    unittest.main()