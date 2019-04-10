# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device

# Metaparset
from genie.metaparser.util.exceptions import SchemaEmptyParserError, \
                                       SchemaMissingKeyError

from genie.libs.parser.iosxe.tests.test_show_service import \
			test_show_service_group_state as test_show_service_group_state_iosxe, \
            test_show_service_group_stats as test_show_service_group_stats_iosxe, \
            test_show_traffic_stats as test_show_traffic_stats_iosxe

# Parser
from genie.libs.parser.ios.show_service import ShowServiceGroupState, \
											   ShowServiceGroupStats, \
											   ShowServiceGroupTrafficStats

# ============================================
# Test for 'show service-group state'
# ============================================

class test_show_service_group_state(test_show_service_group_state_iosxe):
	def test_empty(self):
		self.device1 = Mock(**self.empty_output)
		obj = ShowServiceGroupState(device=self.device1)
		with self.assertRaises(SchemaEmptyParserError):
			parsed_output = obj.parse()

	def test_golden(self):
		self.device = Mock(**self.golden_output)
		obj = ShowServiceGroupState(device=self.device)
		parsed_output = obj.parse()
		self.assertEqual(parsed_output,self.golden_parsed_output)

# ============================================
# Test for 'show service-group stats'
# ============================================
class test_show_service_group_stats(test_show_service_group_stats_iosxe):
	def test_empty(self):
		self.device1 = Mock(**self.empty_output)
		obj = ShowServiceGroupStats(device=self.device1)
		with self.assertRaises(SchemaEmptyParserError):
			parsed_output = obj.parse()

	def test_golden_1(self):
		self.device = Mock(**self.golden_output_1)
		obj = ShowServiceGroupStats(device=self.device)
		parsed_output = obj.parse()
		self.assertEqual(parsed_output,self.golden_parsed_output_1)

	def test_golden_2(self):
		self.device = Mock(**self.golden_output_2)
		obj = ShowServiceGroupStats(device=self.device)
		parsed_output = obj.parse()
		self.assertEqual(parsed_output,self.golden_parsed_output_2)


class test_show_traffic_stats(test_show_traffic_stats_iosxe):
    """unit test for show service-group traffic-stats"""

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowServiceGroupTrafficStats(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output)
        obj = ShowServiceGroupTrafficStats(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output)

    def test_show_group(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_group)
        obj = ShowServiceGroupTrafficStats(device=self.device)
        parsed_output = obj.parse(group="group 1")
        self.assertEqual(parsed_output,self.golden_parsed_output_group)
        

if __name__ == '__main__':
		unittest.main()