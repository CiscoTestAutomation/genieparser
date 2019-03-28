# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device

# Metaparset
from genie.metaparser.util.exceptions import SchemaEmptyParserError, \
                                       SchemaMissingKeyError

from genie.libs.parser.iosxe.tests.test_show_bfd import test_show_bfd as test_show_bfd_iosxe

# Parser
from genie.libs.parser.ios.show_bfd import ShowBfdNeighborsDetails

# ============================================
# IOS unit test for the following show command
#	* show bfd neighbors details
#	* show bfd neighbors client {client} details
# ============================================
class test_show_bfd(test_show_bfd_iosxe):

	def test_empty(self):
	    self.device = Mock(**self.empty_output)
	    obj = ShowBfdNeighborsDetails(device=self.device)
	    with self.assertRaises(SchemaEmptyParserError):
	      parsed_output = obj.parse()

	def test_golden(self):
		self.device = Mock(**self.golden_output)
		obj = ShowBfdNeighborsDetails(device=self.device)
		parsed_output = obj.parse()
		self.assertEqual(parsed_output,self.golden_parsed_output)

	def test_empty_osf_details(self):
		self.device = Mock(**self.empty_output)
		obj = ShowBfdNeighborsDetails(device=self.device)
		with self.assertRaises(SchemaEmptyParserError):
		  parsed_output = obj.parse(client='ospf')

	def test_golden_osf_details(self):
		self.device = Mock(**self.golden_output_client_osf_details)
		obj = ShowBfdNeighborsDetails(device=self.device)
		parsed_output = obj.parse(client='ospf')
		self.assertEqual(parsed_output,self.golden_parsed_output_client_osf_details)

if __name__ == '__main__':
		unittest.main()
