#!/bin/env python
import unittest
from unittest.mock import Mock
from pyats.topology import Device

from genie.metaparser.util.exceptions import SchemaEmptyParserError, SchemaMissingKeyError

from genie.libs.parser.ios.show_power import ShowStackPower, ShowPowerInline

from genie.libs.parser.iosxe.tests.test_show_power import \
                test_show_stack_power as test_show_stack_power_iosxe,\
                test_show_power_inline_interface as test_show_power_inline_interface_iosxe


class test_show_stack_power(test_show_stack_power_iosxe):

    def test_empty(self):
        self.dev1 = Mock(**self.empty_output)
        platform_obj = ShowStackPower(device=self.dev1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = platform_obj.parse()    

    def test_golden(self):
        self.maxDiff = None
        self.dev_c3850 = Mock(**self.golden_output_c3850)
        platform_obj = ShowStackPower(device=self.dev_c3850)
        parsed_output = platform_obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output_c3850)


class test_show_power_inline_interface(test_show_power_inline_interface_iosxe):

    def test_empty(self):
        self.dev1 = Mock(**self.empty_output)
        platform_obj = ShowPowerInline(device=self.dev1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = platform_obj.parse(interface='Gi1/0/13')

    def test_golden(self):
        self.maxDiff = None
        self.dev_c3850 = Mock(**self.golden_output_c3850)
        platform_obj = ShowPowerInline(device=self.dev_c3850)
        parsed_output = platform_obj.parse(interface='Gi1/0/13')
        self.assertEqual(parsed_output,self.golden_parsed_output_c3850)


if __name__ == '__main__':
    unittest.main()

