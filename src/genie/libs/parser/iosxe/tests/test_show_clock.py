#!/bin/env python
import unittest
from unittest.mock import Mock
from ats.topology import Device

from genie.metaparser.util.exceptions import SchemaEmptyParserError,\
                                             SchemaMissingKeyError
from genie.libs.parser.iosxe.show_system import ShowClock


class test_show_access_lists(unittest.TestCase):
    device = Device(name='aDevice')
    empty_output = {'execute.return_value': '      '}

    golden_parsed_output = {}

    golden_output = {'execute.return_value': '''\
        Router#show clock
        Load for five secs: 1%/0%; one minute: 2%; five minutes: 3%
        Time source is NTP, 18:56:04.554 JST Mon Oct 17 2016

        18:56:04.554 JST Mon Oct 17 2016
    '''
    }

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        intf_obj = ShowClock(device=self.device)
        parsed_output = intf_obj.parse()
        self.maxDiff = None
        import pdb; pdb.set_trace()
        self.assertEqual(parsed_output,self.golden_parsed_output)

    def test_empty(self):
        self.device1 = Mock(**self.empty_output)
        intf_obj = ShowClock(device=self.device1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = intf_obj.parse()


if __name__ == '__main__':
    unittest.main()

