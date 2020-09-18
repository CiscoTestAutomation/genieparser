# Import the Python mock functionality
import unittest
from unittest.mock import Mock

# pyATS
from pyats.topology import Device
from pyats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError, SchemaMissingKeyError

# asa show_traffic
from genie.libs.parser.asa.show_traffic import ShowTraffic

# =================================
# Unit test for 'show traffic'
# =================================
class test_show_traffic(unittest.TestCase):

    '''Unit test for "show traffic"'''

    empty_output = {'execute.return_value': ''}

    # Specify the expected result for the parsed output
    golden_parsed_output1 = {
            "GigabitEthernet0/0": {
              "received": {
                "duration": 1799431,
                "packets": 4501617383,
                "bytes": 314808980561,
                "packets_sec": 2000,
                "bytes_sec": 174001
              },
              "transmitted": {
                "duration": 1799431,
                "packets": 643491,
                "bytes": 129611530,
                "packets_sec": 0,
                "bytes_sec": 0
              },
              "packets_input_1_minute": 30943,
              "bytes_input_1_minute": 2164029,
              "packets_output_1_minute": 0,
              "bytes_output_1_minute": 0,
              "packets_drop_rate_1_minute": 0,
              "packets_input_5_minute": 37071,
              "bytes_input_5_minute": 2592560,
              "packets_output_5_minute": 0,
              "bytes_output_5_minute": 0,
              "packets_drop_rate_5_minute": 0
            },
        }
    # Specify the expected unparsed output
    golden_output1 = {'execute.return_value': '''
        ciscoasa# show traffic
        GigabitEthernet0/0:
                received (in 1799431.270 secs):
                        4501617383 packets      314808980561 bytes
                        2000 pkts/sec   174001 bytes/sec
                transmitted (in 1799431.270 secs):
                        643491 packets  129611530 bytes
                        0 pkts/sec      0 bytes/sec
            1 minute input rate 30943 pkts/sec,  2164029 bytes/sec
            1 minute output rate 0 pkts/sec,  0 bytes/sec
            1 minute drop rate, 0 pkts/sec
            5 minute input rate 37071 pkts/sec,  2592560 bytes/sec
            5 minute output rate 0 pkts/sec,  0 bytes/sec
            5 minute drop rate, 0 pkts/sec
        '''}

    def test_show_traffic_full1(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output1)
        obj = ShowTraffic(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output1)

    def test_show_traffic_empty(self):
        self.maxDiff = None
        self.device = Mock(**self.empty_output)
        obj = ShowTraffic(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

if __name__ == '__main__':
    unittest.main()