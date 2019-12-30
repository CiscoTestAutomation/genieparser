#!/bin/env python
import unittest
from unittest.mock import Mock
from genie.metaparser.util.exceptions import SchemaEmptyParserError,\
                                       SchemaMissingKeyError

from genie.libs.parser.ios.show_dot1x import ShowDot1xAllDetail, \
                                    ShowDot1xAllSummary, \
                                    ShowDot1xAllCount, \
                                    ShowDot1xAllStatistics

from genie.libs.parser.iosxe.tests.test_show_dot1x import test_show_dot1x_all_details as test_show_dot1x_all_details_iosxe,\
                                                          test_show_dot1x_all_summary as test_show_dot1x_all_summary_iosxe,\
                                                          test_show_dot1x_all_count as test_show_dot1x_all_count_iosxe,\
                                                          test_show_dot1x_all_statistics as test_show_dot1x_all_statistics_iosxe

class test_show_dot1x_all_details(test_show_dot1x_all_details_iosxe):
    maxDiff = None
    def test_empty(self):
        self.dev1 = Mock(**self.empty_output)
        obj = ShowDot1xAllDetail(device=self.dev1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden(self):
        self.dev_c3850 = Mock(**self.golden_output)
        obj = ShowDot1xAllDetail(device=self.dev_c3850)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output)

    def test_golden_1(self):
        self.dev_c3850 = Mock(**self.golden_output_1)
        obj = ShowDot1xAllDetail(device=self.dev_c3850)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output_1)
        
    def test_golden_2(self):
        self.dev_c3850 = Mock(**self.golden_output_2)
        obj = ShowDot1xAllDetail(device=self.dev_c3850)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output_2)

class test_show_dot1x_all_summary(test_show_dot1x_all_summary_iosxe):

    def test_empty(self):
        self.dev1 = Mock(**self.empty_output)
        obj = ShowDot1xAllSummary(device=self.dev1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden(self):
        self.maxDiff = None
        self.dev_c3850 = Mock(**self.golden_output)
        obj = ShowDot1xAllSummary(device=self.dev_c3850)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output)

    def test_golden_1(self):
        self.maxDiff = None
        self.dev_c3850 = Mock(**self.golden_output_1)
        obj = ShowDot1xAllSummary(device=self.dev_c3850)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output_1)


class test_show_dot1x_all_count(test_show_dot1x_all_count_iosxe):

    def test_empty(self):
        self.dev1 = Mock(**self.empty_output)
        obj = ShowDot1xAllCount(device=self.dev1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden(self):
        self.maxDiff = None
        self.dev_c3850 = Mock(**self.golden_output)
        obj = ShowDot1xAllCount(device=self.dev_c3850)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output)


class test_show_dot1x_all_statistics(test_show_dot1x_all_statistics_iosxe):

    def test_empty(self):
        self.dev1 = Mock(**self.empty_output)
        obj = ShowDot1xAllStatistics(device=self.dev1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden(self):
        self.maxDiff = None
        self.dev_c3850 = Mock(**self.golden_output)
        obj = ShowDot1xAllStatistics(device=self.dev_c3850)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output)

    def test_golden_1(self):
        self.maxDiff = None
        self.dev_c3850 = Mock(**self.golden_output_1)
        obj = ShowDot1xAllStatistics(device=self.dev_c3850)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output_1)


if __name__ == '__main__':
    unittest.main()

