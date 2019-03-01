#!/bin/env python
import unittest
from unittest.mock import Mock
from ats.topology import Device

from genie.metaparser.util.exceptions import SchemaEmptyParserError,\
                                       SchemaMissingKeyError
from genie.libs.parser.ios.show_acl import ShowAccessLists
from genie.libs.parser.iosxe.tests.test_show_acl import test_show_acl as test_show_acl_iosxe


class test_show_access_lists(unittest.TestCase):

    def test_empty(self):
        self.dev1 = Mock(**self.empty_output)
        obj = ShowAccessLists(device=self.dev1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden(self):
        self.maxDiff = None
        self.dev_c3850 = Mock(**self.golden_output)
        obj = ShowAccessLists(device=self.dev_c3850)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output)


if __name__ == '__main__':
    unittest.main()

