# Python
import unittest
from unittest.mock import Mock

# ATS
from pyats.topology import Device

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError
from genie.libs.parser.junos.show_bfd import (ShowBFDSession,)


# =================================
# Unit test for 'show bfd session'
# =================================
class TestShowBFDSession(unittest.TestCase):
    '''unit test for "show bfd session'''
    device = Device(name='aDevice')
    maxDiff = None

    empty_output = {'execute.return_value': ''}

    golden_parsed_output = {
        'bfd-session-information': {
            'bfd-session': [{
                'session-adaptive-multiplier': '3',
                'session-detection-time': '1.500',
                'session-neighbor': '10.34.2.250',
                'session-state': 'Up',
                'session-transmission-interval': '0.500'
            },
            {
                'session-adaptive-multiplier': '3',
                'session-detection-time': '1.500',
                'session-interface': 'ge-0/0/0.0',
                'session-neighbor': '127.0.0.64',
                'session-state': 'Up',
                'session-transmission-interval': '0.500'
            }
            ]
        }
        }

    golden_output = {
        'execute.return_value':
        '''
        Address                  State     Interface      Time     Interval  Multiplier
        10.34.2.250             Up                       1.500     0.500        3
        127.0.0.64               Up        ge-0/0/0.0     1.500     0.500        3
        '''
    }

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowBFDSession(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = ShowBFDSession(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


if __name__ == '__main__':
    unittest.main()