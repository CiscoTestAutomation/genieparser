# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device

# Metaparset
from genie.metaparser.util.exceptions import SchemaEmptyParserError, \
                                       SchemaMissingKeyError

# Parser
from genie.libs.parser.ios.show_mcast import ShowIpMroute,\
                                    ShowIpv6Mroute, \
                                    ShowIpMrouteStatic, \
                                    ShowIpMulticast

from genie.libs.parser.iosxe.tests.test_show_mcast import test_show_ip_mroute as test_show_ip_mroute_iosxe,\
                                                    test_show_ipv6_mroute as test_show_ipv6_mroute_iosxe,\
                                                    test_show_ip_mroute_static as test_show_ip_mroute_static_iosxe,\
                                                    test_show_ip_multicast as test_show_ip_multicast_iosxe
# =======================================
# Unit test for 'show ip mroute'
# Unit test for 'show ip mroute vrf xxx'
# =======================================
class test_show_ip_mroute(test_show_ip_mroute_iosxe):

    def test_empty(self):
        self.device1 = Mock(**self.empty_output)
        obj = ShowIpMroute(device=self.device1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden_vrf_default(self):
        self.device = Mock(**self.golden_output)
        obj = ShowIpMroute(device=self.device)
        parsed_output = obj.parse()
        self.maxDiff = None
        self.assertEqual(parsed_output,self.golden_parsed_output)

    def test_golden_vrf_non_default(self):
        self.device = Mock(**self.golden_output2)
        obj = ShowIpMroute(device=self.device)
        parsed_output = obj.parse(vrf='VRF1')
        self.maxDiff = None
        self.assertEqual(parsed_output,self.golden_parsed_output2)


# =======================================
# Unit test for 'show ipv6 mroute'
# Unit test for 'show ipv6 mroute vrf xxx'
# =======================================
class test_show_ipv6_mroute(test_show_ipv6_mroute_iosxe):

    def test_empty(self):
        self.device1 = Mock(**self.empty_output)
        obj = ShowIpv6Mroute(device=self.device1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden_vrf_default(self):
        self.device = Mock(**self.golden_output)
        obj = ShowIpv6Mroute(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output)

    def test_golden_vrf_non_default(self):
        self.device = Mock(**self.golden_output2)
        obj = ShowIpv6Mroute(device=self.device)
        parsed_output = obj.parse(vrf='VRF1')
        self.assertEqual(parsed_output,self.golden_parsed_output2)


# =============================================
# Unit test for 'show ip mroute static'
# Unit test for 'show ip mroute vrf xxx static'
# =============================================
class test_show_ip_mroute_static(test_show_ip_mroute_static_iosxe):

    def test_empty(self):
        self.device1 = Mock(**self.empty_output)
        obj = ShowIpMrouteStatic(device=self.device1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden_vrf_default(self):
        self.device = Mock(**self.golden_output)
        obj = ShowIpMrouteStatic(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output)

    def test_golden_vrf_non_default(self):
        self.device = Mock(**self.golden_output2)
        obj = ShowIpMrouteStatic(device=self.device)
        parsed_output = obj.parse(vrf='VRF1')
        self.assertEqual(parsed_output,self.golden_parsed_output2)


# =============================================
# Unit test for 'show ip multicast'
# Unit test for 'show ip multicast vrf xxx'
# =============================================
class test_show_ip_multicast(test_show_ip_multicast_iosxe):

    def test_empty(self):
        self.device1 = Mock(**self.empty_output)
        obj = ShowIpMulticast(device=self.device1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden_vrf_default(self):
        self.device = Mock(**self.golden_output)
        obj = ShowIpMulticast(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output)

    def test_golden_vrf_non_default(self):
        self.device = Mock(**self.golden_output2)
        obj = ShowIpMulticast(device=self.device)
        parsed_output = obj.parse(vrf='VRF1')
        self.assertEqual(parsed_output,self.golden_parsed_output2)


if __name__ == '__main__':
    unittest.main()