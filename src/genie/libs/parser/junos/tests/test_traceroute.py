# Python
import unittest
from unittest.mock import Mock

# PyATS
from pyats.topology import Device

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# junos traceroute
from genie.libs.parser.junos.traceroute import (Traceroute)


class TestTraceroute(unittest.TestCase):
    """ Unit tests for:
            * traceroute {ipaddress} no-resolve
    """

    device = Device(name='aDevice')

    empty_output = {'execute.return_value': ''}

    golden_output = {'execute.return_value': '''
        traceroute 30.0.0.2 no-resolve
        traceroute to example.local (30.0.0.2), 30 hops max, 52 byte packets
         1  r1 20.0.0.2  1.792 ms  1.142 ms  0.831 ms
         2  30.0.0.2  1.734 ms  1.234 ms  0.855 ms
    '''}

    golden_parsed_output = {
        'traceroute': {
            'to': {
                'domain': 'example.local',
                'address': '30.0.0.2'
            },
            'max-hops': '30',
            'packet-size': '52',
            'hops': {
                'hop': [
                    {
                        'hop-number': '1',
                        'router-name': 'r1',
                        'address': '20.0.0.2',
                        'round-trip-time': '1.792 ms  1.142 ms  0.831 ms'
                    },
                    {
                        'hop-number': '2',
                        'address': '30.0.0.2',
                        'round-trip-time': '1.734 ms  1.234 ms  0.855 ms'
                    }
                ]
            }
        }
    }

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = Traceroute(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            obj.parse(addr='30.0.0.2')

    def test_traceroute(self):
        self.device = Mock(**self.golden_output)
        obj = Traceroute(device=self.device)
        parsed_output = obj.parse(addr='30.0.0.2')
        self.assertEqual(parsed_output, self.golden_parsed_output)


if __name__ == '__main__':
    unittest.main()