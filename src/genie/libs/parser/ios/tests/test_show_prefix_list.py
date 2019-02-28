# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device

# Metaparset
from genie.metaparser.util.exceptions import SchemaEmptyParserError, \
                                       SchemaMissingKeyError

# Parser
from genie.libs.parser.ios.show_prefix_list import ShowIpPrefixListDetail, \
                                          ShowIpv6PrefixListDetail

from genie.libs.parser.iosxe.tests.test_show_prefix_list import test_show_ip_prefix_list_detail as test_show_ip_prefix_list_detail_iosxe,\
                                                                test_show_ipv6_prefix_list_detail as test_show_ipv6_prefix_list_detail_iosxe
# ==============================================
# Unit test for 'show ip prefix-list detail'
# ==============================================
class test_show_ip_prefix_list_detail(test_show_ip_prefix_list_detail_iosxe):

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowIpPrefixListDetail(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = ShowIpPrefixListDetail(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output)


# ==============================================
# Unit test for 'show ipv6 prefix-list detail'
# ==============================================
class test_show_ipv6_prefix_list_detail(test_show_ipv6_prefix_list_detail_iosxe):

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowIpv6PrefixListDetail(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = ShowIpv6PrefixListDetail(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output)

if __name__ == '__main__':
    unittest.main()