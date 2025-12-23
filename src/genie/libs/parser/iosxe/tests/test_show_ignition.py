# Import the Python mock functionality
import unittest
from unittest.mock import Mock

# pyATS
from pyats.topology import Device
from pyats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError, SchemaMissingKeyError

# iosxe show_crypto
from genie.libs.parser.iosxe.show_ignition import ShowIgnition

# =================================
# Unit test for 'show crypto ikev2 sa detail'
# =================================
class test_show_ignition(unittest.TestCase):

    '''Unit test for "show ignition"'''

    empty_output = {'execute.return_value': ''}

    # Specify the expected result for the parsed output
    golden_parsed_output1 = {
        "ignition_status": {
            "ignition_mgmt": "Enabled",
            "input_volt": "14.080 V",
            "pwr_state": "Power on",
            "sense": "Enabled",
            "shutdown_time": "0.0 s to off [will begin power down at ~100 sec]",
            "battery_type": "12v",
            "undervoltage": "9.000 V",
            "overvoltage": "37.000 V",
            "sense_on_threshold": "13.200 V",
            "sense_off_threshold": "12.800 V",
            "undervoltage_time_delay": "20.0 s",
            "overvoltage_time_delay": "1.0 s",
            "ignition_off_time_delay": "7200.0 s",
        }
    }

    # Specify the expected unparsed output
    golden_output1 = {'execute.return_value': '''
Status:
  Ignition management: Enabled
  Input voltage:       14.080 V
  Ignition status:     Power on
  Ignition Sense:      Enabled
  Shutdown timer:      0.0 s to off [will begin power down at ~100 sec]
  Config-ed battery:   12v
Thresholds:
  Undervoltage:        9.000 V
  Overvoltage:         37.000 V
  Sense on:            13.200 V
  Sense off:           12.800 V
  Undervoltage timer:  20.0 s
  Overvoltage timer:   1.0 s
  Ignition-Off timer:  7200.0 s
        '''}

    def test_show_ignition(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output1)
        obj = ShowIgnition(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output1)


if __name__ == '__main__':
    unittest.main()