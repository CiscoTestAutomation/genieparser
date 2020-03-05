#!/bin/env python
import unittest
from unittest.mock import Mock
from pyats.topology import Device

from genie.metaparser.util.exceptions import SchemaEmptyParserError,\
                                             SchemaMissingKeyError
                                             
from genie.libs.parser.ios.show_system import ShowClock


class test_show_clock(unittest.TestCase):
    device = Device(name='aDevice')
    empty_output = {'execute.return_value': '      '}

    golden_parsed_output = {
        'day': '17',
        'month': 'Oct',
        'time': '18:56:04.554',
        'day_of_week': 'Mon',
        'year': '2016',
        'timezone': 'EST'}

    golden_output = {'execute.return_value': '''\
        Router#show clock
        Load for five secs: 1%/0%; one minute: 2%; five minutes: 3%
        Time source is NTP, 18:56:04.554 EST Mon Oct 17 2016

        18:56:04.554 EST Mon Oct 17 2016
    '''
    }

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        clock_obj = ShowClock(device=self.device)
        parsed_output = clock_obj.parse()
        self.maxDiff = None
        self.assertEqual(parsed_output,self.golden_parsed_output)

    def test_empty(self):
        self.device1 = Mock(**self.empty_output)
        clock_obj = ShowClock(device=self.device1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = clock_obj.parse()


if __name__ == '__main__':
    unittest.main()

