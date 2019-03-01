#!/bin/env python
import unittest
from unittest.mock import Mock

from genie.metaparser.util.exceptions import SchemaEmptyParserError,\
                                       SchemaMissingKeyError

from genie.libs.parser.ios.show_lldp import ShowLldp, ShowLldpEntry, \
                                   ShowLldpNeighborsDetail, \
                                   ShowLldpTraffic, \
                                   ShowLldpInterface

from genie.libs.parser.iosxe.tests.test_show_lldp import test_show_lldp as test_show_lldp_iosxe ,\
                                                         test_show_lldp_entry as test_show_lldp_entry_iosxe,\
                                                         test_show_lldp_traffic as test_show_lldp_traffic_iosxe,\
                                                         test_show_lldp_neighbor_detail as test_show_lldp_neighbor_detail_iosxe,\
                                                         test_show_lldp_interface as test_show_lldp_interface_iosxe


class test_show_lldp(test_show_lldp_iosxe):
    def test_empty(self):
        self.dev1 = Mock(**self.empty_output)
        obj = ShowLldp(device=self.dev1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden(self):
        self.maxDiff = None
        self.dev_c3850 = Mock(**self.golden_output)
        obj = ShowLldp(device=self.dev_c3850)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output)

class test_show_lldp_entry(test_show_lldp_entry_iosxe):
    def test_empty(self):
        self.dev1 = Mock(**self.empty_output)
        obj = ShowLldpEntry(device=self.dev1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse(entry='GigabitEthernet1/0/19')

    def test_golden(self):
        self.maxDiff = None
        self.dev_c3850 = Mock(**self.golden_output)
        obj = ShowLldpEntry(device=self.dev_c3850)
        parsed_output = obj.parse(entry='*')
        self.assertEqual(parsed_output,self.golden_parsed_output)


class test_show_lldp_neighbor_detail(test_show_lldp_neighbor_detail_iosxe):

    def test_empty(self):
        self.dev1 = Mock(**self.empty_output)
        obj = ShowLldpNeighborsDetail(device=self.dev1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden(self):
        self.maxDiff = None
        self.dev_c3850 = Mock(**self.golden_output)
        obj = ShowLldpNeighborsDetail(device=self.dev_c3850)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output)


class test_show_lldp_traffic(test_show_lldp_traffic_iosxe):

    def test_empty(self):
        self.dev1 = Mock(**self.empty_output)
        obj = ShowLldpTraffic(device=self.dev1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden(self):
        self.maxDiff = None
        self.dev_c3850 = Mock(**self.golden_output)
        obj = ShowLldpTraffic(device=self.dev_c3850)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output)


class test_show_lldp_interface(test_show_lldp_interface_iosxe):

    def test_empty(self):
        self.dev1 = Mock(**self.empty_output)
        obj = ShowLldpInterface(device=self.dev1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden(self):
        self.maxDiff = None
        self.dev_c3850 = Mock(**self.golden_output)
        obj = ShowLldpInterface(device=self.dev_c3850)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output)


if __name__ == '__main__':
    unittest.main()

