#!/bin/env python
import unittest
from unittest.mock import Mock
from ats.topology import Device

from genie.metaparser.util.exceptions import SchemaEmptyParserError,\
                                       SchemaMissingKeyError

from genie.libs.parser.ios.show_access_session import ShowAccessSession

from genie.libs.parser.iosxe.tests.test_show_access_session import \
        test_show_access_session as test_show_access_session_iosxe


class test_show_access_session(test_show_access_session_iosxe):

    def test_empty(self):
        self.dev1 = Mock(**self.empty_output)
        obj = ShowAccessSession(device=self.dev1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden(self):
        self.maxDiff = None
        self.dev_c3850 = Mock(**self.golden_output)
        obj = ShowAccessSession(device=self.dev_c3850)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output)

if __name__ == '__main__':
    unittest.main()

