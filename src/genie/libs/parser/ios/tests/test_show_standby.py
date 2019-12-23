
# Python
import re
import unittest
from unittest.mock import Mock

# ATS
from pyats.topology import Device

# Parser
from genie.libs.parser.ios.show_standby import ShowStandbyInternal,\
                                      ShowStandbyAll,\
                                      ShowStandbyDelay

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

from genie.libs.parser.ios.show_standby import ShowStandbyDelay,\
                                               ShowStandbyAll,\
                                               ShowStandbyInternal

from genie.libs.parser.iosxe.tests.test_show_standby import test_show_standby_internal as test_show_standby_internal_iosxe,\
                                                            test_show_standby_all as test_show_standby_all_iosxe,\
                                                            test_show_standby_delay as test_show_standby_delay_iosxe
# =========================================
#   Unit test for 'show standby internal'
# =========================================

class test_show_standby_internal(test_show_standby_internal_iosxe):

    def test_golden(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output)
        standby_internal_obj = ShowStandbyInternal(device=self.device)
        parsed_output = standby_internal_obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output)

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        standby_internal_obj = ShowStandbyInternal(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = standby_internal_obj.parse()


# ======================================
#   Unit test for 'show standby all'
# ======================================

class test_show_standby_all(test_show_standby_all_iosxe):
    
    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    def test_golden(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output)
        standby_all_obj = ShowStandbyAll(device=self.device)
        parsed_output = standby_all_obj.parse()
        #import pprint ; pprint.pprint(parsed_output)
        self.assertEqual(parsed_output,self.golden_parsed_output)

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        standby_all_obj = ShowStandbyAll(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = standby_all_obj.parse()

# =========================================
#   Unit test for 'show standby delay'
# =========================================

class test_show_standby_delay(test_show_standby_delay_iosxe):

    def test_golden(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output)
        standby_delay_obj = ShowStandbyDelay(device=self.device)
        parsed_output = standby_delay_obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output)

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        standby_delay_obj = ShowStandbyDelay(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = standby_delay_obj.parse()

if __name__ == '__main__':
    unittest.main()

# vim: ft=python et sw=4
