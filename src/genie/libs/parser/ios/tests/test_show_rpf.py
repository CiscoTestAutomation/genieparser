# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device

# Metaparset
from genie.metaparser.util.exceptions import SchemaEmptyParserError, \
                                       SchemaMissingKeyError
# Parser
from genie.libs.parser.ios.show_rpf import ShowIpRpf, ShowIpv6Rpf

from genie.libs.parser.iosxe.tests.test_show_rpf import \
                    test_show_ip_rpf as test_show_ip_rpf_iosxe,\
                    test_show_ipv6_rpf as test_show_ipv6_rpf_iosxe

# =============================================
# Unit test for 'show ip rpf <x.x.x.x>'
# Unit test for 'show ip rpf vrf xxx <x.x.x.x>'
# ==============================================
class test_show_ip_rpf(test_show_ip_rpf_iosxe):

    def test_empty(self):
        self.device1 = Mock(**self.empty_output)
        obj = ShowIpRpf(device=self.device1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse(mroute='172.16.10.13')

    def test_golden_vrf_default(self):
        self.device = Mock(**self.golden_output)
        obj = ShowIpRpf(device=self.device)
        parsed_output = obj.parse(mroute='172.16.10.13')
        self.assertEqual(parsed_output,self.golden_parsed_output)

    def test_golden_vrf_non_default(self):
        self.device = Mock(**self.golden_output2)
        obj = ShowIpRpf(device=self.device)
        parsed_output = obj.parse(mroute='10.1.1.100', vrf='VRF1')
        self.assertEqual(parsed_output,self.golden_parsed_output2)


# =============================================
# Unit test for 'show ipv6 rpf <x.x.x.x>'
# Unit test for 'show ipv6 rpf vrf xxx <x.x.x.x>'
# ==============================================
class test_show_ipv6_rpf(test_show_ipv6_rpf_iosxe):

    def test_empty(self):
        self.device1 = Mock(**self.empty_output)
        obj = ShowIpv6Rpf(device=self.device1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse(mroute='2001:99:99::99')

    def test_golden_vrf_default(self):
        self.device = Mock(**self.golden_output)
        obj = ShowIpv6Rpf(device=self.device)
        parsed_output = obj.parse(mroute='2001:99:99::99')
        self.assertEqual(parsed_output,self.golden_parsed_output)

    def test_golden_vrf_non_default(self):
        self.device = Mock(**self.golden_output2)
        obj = ShowIpv6Rpf(device=self.device)
        parsed_output = obj.parse(mroute='2001:99:99::99', vrf='VRF1')
        self.assertEqual(parsed_output,self.golden_parsed_output2)


if __name__ == '__main__':
    unittest.main()