import unittest
from unittest.mock import Mock

from pyats.topology import loader, Device
from genie.metaparser.util.exceptions import SchemaEmptyParserError
from genie.libs.parser.junos.show_chassis import ShowChassisFpcDetail

class TestShowChassisFpcDetail(unittest.TestCase):

    maxDiff = None

    device = Device(name='test-device')

    empty_output = {'execute.return_value': ''}

    golden_output = {'execute.return_value': '''
        show chassis fpc detail
        Slot 0 information:
        State                               Online    
        Temperature                      Testing
        Total CPU DRAM                  511 MB
        Total RLDRAM                     10 MB
        Total DDR DRAM                    0 MB
        FIPS Capable                        False 
        FIPS Mode                           False 
        Start time                          2019-08-29 09:09:16 UTC
        Uptime                              208 days, 22 hours, 50 minutes, 26 seconds
    '''}

    golden_parsed_output = {
        "fpc-information": {
        "fpc": {
            "fips-capable": "False",
            "fips-mode": "False",
            "memory-ddr-dram-size": "0",
            "memory-dram-size": "511",
            "memory-rldram-size": "10",
            "slot": "0",
            "start-time": {
                "#text": "2019-08-29 09:09:16 UTC"
            },
            "state": "Online",
            "temperature": {
                "#text": "Testing"
            },
            "up-time": {
                "#text": "208 days, 22 hours, 50 minutes, 26 seconds"
            }
        }
    }
    }

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowChassisFpcDetail(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = ShowChassisFpcDetail(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)

if __name__ == '__main__':
    unittest.main()