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
        test_show_line as test_show_line_iosxe,\
        test_show_users as test_show_users_iosxe

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


class test_show_users(test_show_users_iosxe):

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

