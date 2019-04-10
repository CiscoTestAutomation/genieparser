#!/bin/env python
import unittest
from unittest.mock import Mock
from ats.topology import Device

from genie.metaparser.util.exceptions import SchemaEmptyParserError,\
                                             SchemaMissingKeyError
# ios show_session
from genie.libs.parser.ios.show_session import ShowLine,\
                                               ShowUsers
# iosxe/test_show_session
from genie.libs.parser.iosxe.tests.test_show_session import \
        test_show_line as test_show_line_iosxe


class test_show_line(test_show_line_iosxe):

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        line_obj = ShowLine(device=self.device)
        parsed_output = line_obj.parse()
        self.maxDiff = None
        self.assertEqual(parsed_output,self.golden_parsed_output)

    def test_empty(self):
        self.device1 = Mock(**self.empty_output)
        line_obj = ShowLine(device=self.device1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = line_obj.parse()


class test_show_users(unittest.TestCase):

    device = Device(name='aDevice')

    empty_output = {'execute.return_value': '      '}

    golden_output = {'execute.return_value': '''\
       Router# show users
        Line         User      Host(s)                 Idle    Location
        *  0 con 0             idle                    01:58
          10 vty 0             Virtual-Access2          0      1212321
    '''}

    golden_parsed_output = {
        "line": {
            "0 con 0": {
                "active": True,
                "host": "idle",
                "idle": "01:58"
            },
            "10 vty 0": {
                "active": False,
                "location": "1212321",
                "host": "Virtual-Access2",
                "idle": "0"
            }
        }
    }

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        users_obj = ShowUsers(device=self.device)
        parsed_output = users_obj.parse()
        self.maxDiff = None
        self.assertEqual(parsed_output,self.golden_parsed_output)

    def test_empty(self):
        self.device1 = Mock(**self.empty_output)
        users_obj = ShowUsers(device=self.device1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = users_obj.parse()


if __name__ == '__main__':
    unittest.main()

