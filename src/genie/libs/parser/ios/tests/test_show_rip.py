# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError, SchemaMissingKeyError

from genie.libs.parser.ios.show_rip import ShowIpRipDatabase, \
										   ShowIpv6Rip

from genie.libs.parser.iosxe.tests.test_show_rip import test_show_ip_rip_database as \
                                                        test_show_ip_rip_database_iosxe, \
                                                        test_show_ipv6_rip as \
                                                        test_show_ipv6_rip_iosxe

# ============================================
# Parser for 'show ip rip database'
# Parser for 'show ip rip database vrf {vrf}'
# ============================================
class test_show_ip_rip_database(test_show_ip_rip_database_iosxe):
	def test_empty(self):
		self.device1 = Mock(**self.empty_output)
		obj = ShowIpRipDatabase(device=self.device1)
		with self.assertRaises(SchemaEmptyParserError):
			parsed_output = obj.parse()

	def test_golden_vrf_default(self):
		self.maxDiff = None
		self.device = Mock(**self.golden_output)
		obj = ShowIpRipDatabase(device=self.device)
		parsed_output = obj.parse()
		self.assertEqual(parsed_output, self.golden_parsed_output)

	def test_golden_vrf_vrf1(self):
		self.maxDiff = None
		self.device = Mock(**self.golden_output_2)
		obj = ShowIpRipDatabase(device=self.device)
		parsed_output = obj.parse(vrf="VRF1")
		self.assertEqual(parsed_output, self.golden_parsed_output_2)


# ============================================
# unit test for 'show ipv6 rip'
# unit test for 'show ipv6 rip vrf {vrf}'
# ============================================
class test_show_ipv6_rip(test_show_ipv6_rip_iosxe):
	def test_empty(self):
	    self.device1 = Mock(**self.empty_output)
	    obj = ShowIpv6Rip(device=self.device1)
	    with self.assertRaises(SchemaEmptyParserError):
	        parsed_output = obj.parse()

	def test_golden_vrf_default(self):
	    self.maxDiff = None
	    self.device = Mock(**self.golden_output)
	    obj = ShowIpv6Rip(device=self.device)
	    parsed_output = obj.parse()
	    self.assertEqual(parsed_output, self.golden_parsed_output)

	def test_golden_vrf_vrf1(self):
	    self.maxDiff = None
	    self.device = Mock(**self.golden_output_2)
	    obj = ShowIpv6Rip(device=self.device)
	    parsed_output = obj.parse(vrf="VRF1")
	    self.assertEqual(parsed_output, self.golden_parsed_output_2)

	def test_golden_vrf_vrf1_non_distribution(self):
	    self.maxDiff = None
	    self.device = Mock(**self.golden_output_3)
	    obj = ShowIpv6Rip(device=self.device)
	    parsed_output = obj.parse(vrf="VRF1")
	    self.assertEqual(parsed_output, self.golden_parsed_output_3)

if __name__ == '__main__':
    unittest.main()