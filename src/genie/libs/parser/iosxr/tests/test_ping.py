import unittest
from unittest.mock import Mock

from pyats.topology import Device

from genie.metaparser.util.exceptions import SchemaEmptyParserError

from genie.libs.parser.iosxr.ping import Ping


class TestShowBfdSessionDestinationDetailss(unittest.TestCase):

    device = Device(name='aDevice')

    empty_device_output = {'execute.return_value': '''
      '''}

    expected_parsed_output = {
                  'ping': {
                     'address': '10.4.1.1',
                     'data_bytes': 100,
                     'repeat': 100,
                      'result_per_line': ['!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!',
                                          '!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!'],
                     'statistics': {
                        'received': 100,
                        'round_trip': {
                        'avg_ms': 14,
                        'max_ms': 2,
                        'min_ms': 1
                        },
                        'send': 100,
                        'success_rate_percent': 100.0
                     },
                     'timeout_secs': 2
                  }
               }

    device_output = {'execute.return_value': '''
      Type escape sequence to abort.
      Sending 100, 100-byte ICMP Echos to 10.4.1.1, timeout is 2 seconds:
      !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
      !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
      Success rate is 100 percent (100/100), round-trip min/avg/max = 1/2/14 ms
    '''}

    @classmethod
    def setUpClass(cls):
        cls.maxDiff = None

    def test_ping_1(self):

        self.device = Mock(**self.device_output)
        obj = Ping(device=self.device)
        parsed_output = obj.parse(addr='10.4.1.1', source='10.4.1.2', count=100)
        self.assertEqual(parsed_output, self.expected_parsed_output)

    def test_show_bfd_destination_details_empty_output(self):

        self.device = Mock(**self.empty_device_output)
        obj = Ping(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse(addr=None)

if __name__ == '__main__':
    unittest.main()
