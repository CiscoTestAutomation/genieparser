# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device

# Metaparset
from genie.metaparser.util.exceptions import SchemaEmptyParserError, \
                                       SchemaMissingKeyError

# Parser
from genie.libs.parser.ios.show_mld import ShowIpv6MldInterface, \
                                   ShowIpv6MldGroupsDetail, \
                                   ShowIpv6MldSsmMap

from genie.libs.parser.iosxe.tests.test_show_mld import test_show_ipv6_mld_interface as test_show_ipv6_mld_interface_iosxe,\
                                                        test_show_ipv6_mld_groups_detail as test_show_ipv6_mld_groups_detail_iosxe,\
                                                        test_show_ipv6_mld_ssm_mapping as test_show_ipv6_mld_ssm_mapping_iosxe
# ==================================================
# Unit test for 'show ipv6 mld interface'
# Unit test for 'show ipv6 mld vrf <WORD> interface'
# ==================================================
class test_show_ipv6_mld_interface(test_show_ipv6_mld_interface_iosxe):

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowIpv6MldInterface(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden_default_vrf(self):
        self.device = Mock(**self.golden_output)
        obj = ShowIpv6MldInterface(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output)

    def test_golden_non_default_vrf(self):
        self.device = Mock(**self.golden_output_1)
        obj = ShowIpv6MldInterface(device=self.device)
        parsed_output = obj.parse(vrf='VRF1')
        self.assertEqual(parsed_output,self.golden_parsed_output_1)


# =====================================================
# Unit test for 'show ipv6 mld groups detail'
# Unit test for 'show ipv6 mld vrf <WORD> groups detail'
# =====================================================
class test_show_ipv6_mld_groups_detail(test_show_ipv6_mld_groups_detail_iosxe):

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowIpv6MldGroupsDetail(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden_default_vrf(self):
        self.device = Mock(**self.golden_output)
        obj = ShowIpv6MldGroupsDetail(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output)

    def test_golden_non_default_vrf(self):
        self.device = Mock(**self.golden_output_1)
        obj = ShowIpv6MldGroupsDetail(device=self.device)
        parsed_output = obj.parse(vrf='VRF1')
        self.assertEqual(parsed_output,self.golden_parsed_output_1)


# ===========================================================
# Unit test for 'show ipv6 mld ssm-mapping <WROD>'
# Unit test for 'show ipv6 mld vrf <WORD> ssm-mapping <WORD>'
# ============================================================
class test_show_ipv6_mld_ssm_mapping(test_show_ipv6_mld_ssm_mapping_iosxe):

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowIpv6MldSsmMap(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse(group='ff35:1::1')

    def test_golden_default_vrf(self):
        self.device = Mock(**self.golden_output)
        obj = ShowIpv6MldSsmMap(device=self.device)
        parsed_output = obj.parse(group='ff35:1::1')
        self.assertEqual(parsed_output,self.golden_parsed_output)

    def test_golden_non_default_vrf(self):
        self.device = Mock(**self.golden_output_1)
        obj = ShowIpv6MldSsmMap(device=self.device)
        parsed_output = obj.parse(vrf='VRF1', group='ff35:1::1')
        self.assertEqual(parsed_output,self.golden_parsed_output_1)

if __name__ == '__main__':
    unittest.main()