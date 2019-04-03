# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device

# Metaparset
from genie.metaparser.util.exceptions import SchemaEmptyParserError, \
                                       SchemaMissingKeyError

# Parser
from genie.libs.parser.ios.show_igmp import ShowIpIgmpInterface, \
                                   ShowIpIgmpGroupsDetail, \
                                   ShowIpIgmpSsmMapping

from genie.libs.parser.iosxe.tests.test_show_igmp import test_show_ip_igmp_interface as test_show_ip_igmp_interface_iosxe,\
                                                         test_show_ip_igmp_groups_detail as test_show_ip_igmp_groups_detail_iosxe, \
                                                         test_show_ip_igmp_ssm_mapping as test_show_ip_igmp_ssm_mapping_iosxe

# ==================================================
# Unit test for 'show ip igmp interface'
# Unit test for 'show ip igmp vrf <WORD> interface'
# ==================================================
class test_show_ip_igmp_interface(test_show_ip_igmp_interface_iosxe):


    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowIpIgmpInterface(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden_default_vrf(self):
        self.device = Mock(**self.golden_output)
        obj = ShowIpIgmpInterface(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output)

    def test_golden_non_default_vrf(self):
        self.device = Mock(**self.golden_output_1)
        obj = ShowIpIgmpInterface(device=self.device)
        parsed_output = obj.parse(vrf='VRF1')
        self.assertEqual(parsed_output,self.golden_parsed_output_1)


# =====================================================
# Unit test for 'show ip igmp groups detail'
# Unit test for 'show ip igmp vrf <WORD> groups detail'
# =====================================================
class test_show_ip_igmp_groups_detail(test_show_ip_igmp_groups_detail_iosxe):

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowIpIgmpGroupsDetail(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden_default_vrf(self):
        self.device = Mock(**self.golden_output)
        obj = ShowIpIgmpGroupsDetail(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output)

    def test_golden_non_default_vrf(self):
        self.device = Mock(**self.golden_output_1)
        obj = ShowIpIgmpGroupsDetail(device=self.device)
        parsed_output = obj.parse(vrf='VRF1')
        self.assertEqual(parsed_output,self.golden_parsed_output_1)

    def test_golden_3(self):
        self.device = Mock(**self.golden_output_3)
        obj = ShowIpIgmpGroupsDetail(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output_3)

# ===========================================================
# Unit test for 'show ip igmp ssm-mapping <WROD>'
# Unit test for 'show ip igmp vrf <WORD> ssm-mapping <WORD>'
# ============================================================
class test_show_ip_igmp_ssm_mapping(test_show_ip_igmp_ssm_mapping_iosxe):
    
    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}
    
    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowIpIgmpSsmMapping(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse(group='239.1.1.1')

    def test_golden_default_vrf(self):
        self.device = Mock(**self.golden_output)
        obj = ShowIpIgmpSsmMapping(device=self.device)
        parsed_output = obj.parse(group='239.1.1.1')
        self.assertEqual(parsed_output,self.golden_parsed_output)

    def test_golden_non_default_vrf(self):
        self.device = Mock(**self.golden_output_1)
        obj = ShowIpIgmpSsmMapping(device=self.device)
        parsed_output = obj.parse(vrf='VRF1', group='239.1.1.1')
        self.assertEqual(parsed_output,self.golden_parsed_output_1)
if __name__ == '__main__':
    unittest.main()