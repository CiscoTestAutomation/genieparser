#!/bin/env python
import unittest
from unittest.mock import Mock
from ats.topology import Device

from genie.metaparser.util.exceptions import SchemaEmptyParserError,\
                                       SchemaMissingKeyError
from genie.libs.parser.ios.show_memory import ShowMemoryStatistics

from genie.libs.parser.iosxe.tests.test_show_memory import test_show_memory_statistics as test_show_memory_statistics_iosxe

class test_show_memory_statistics(test_show_memory_statistics_iosxe):

    def test_empty(self):
        self.dev = Mock(**self.empty_output)
        obj = ShowMemoryStatistics(device=self.dev)
        with self.assertRaises(SchemaEmptyParserError):
            parsered_output = obj.parse()

    def test_golden(self):
        self.maxDiff = None
        self.dev = Mock(**self.golden_output)
        obj = ShowMemoryStatistics(device=self.dev)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)

        
if __name__ == '__main__':
    unittest.main()

