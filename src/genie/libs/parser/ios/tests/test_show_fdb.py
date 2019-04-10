#!/bin/env python
import unittest
from unittest.mock import Mock
from ats.topology import Device

from genie.metaparser.util.exceptions import SchemaEmptyParserError,\
                                       SchemaMissingKeyError

from genie.libs.parser.ios.show_fdb import ShowMacAddressTable,\
                                            ShowMacAddressTableAgingTime,\
                                            ShowMacAddressTableLearning

from genie.libs.parser.iosxe.tests.test_show_fdb import \
            test_show_mac_address_table as test_show_mac_address_table_iosxe,\
            test_show_mac_address_table_aging_time as test_show_mac_address_table_aging_time_iosxe,\
            test_show_mac_address_table_learning as test_show_mac_address_table_learning_iosxe



class test_show_mac_address_table(test_show_mac_address_table_iosxe):

    def test_empty(self):
        self.dev1 = Mock(**self.empty_output)
        obj = ShowMacAddressTable(device=self.dev1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden(self):
        self.maxDiff = None
        self.dev_c3850 = Mock(**self.golden_output)
        obj = ShowMacAddressTable(device=self.dev_c3850)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output)


class test_show_mac_address_table_aging_time(test_show_mac_address_table_aging_time_iosxe):

    def test_empty(self):
        self.dev1 = Mock(**self.empty_output)
        obj = ShowMacAddressTableAgingTime(device=self.dev1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden(self):
        self.maxDiff = None
        self.dev_c3850 = Mock(**self.golden_output)
        obj = ShowMacAddressTableAgingTime(device=self.dev_c3850)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output)


class test_show_mac_address_table_learning(test_show_mac_address_table_learning_iosxe):

    def test_empty(self):
        self.dev1 = Mock(**self.empty_output)
        obj = ShowMacAddressTableLearning(device=self.dev1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden(self):
        self.maxDiff = None
        self.dev_c3850 = Mock(**self.golden_output)
        obj = ShowMacAddressTableLearning(device=self.dev_c3850)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output)


if __name__ == '__main__':
    unittest.main()

