import unittest
from unittest.mock import Mock

# ATS
from pyats.topology import Device

from genie.metaparser.util.exceptions import SchemaEmptyParserError, \
                                       SchemaMissingKeyError

from genie.libs.parser.ios.show_static_routing import ShowIpStaticRoute, \
                                             ShowIpv6StaticDetail

from genie.libs.parser.iosxe.tests.test_show_static_routing import \
                                            test_show_ip_static_route as test_show_ip_static_route_iosxe,\
                                            test_show_ipv6_static_detail as test_show_ipv6_static_detail_iosxe
# ============================================
# unit test for 'show ip static route'
# =============================================
class test_show_ip_static_route(test_show_ip_static_route_iosxe):
    def test_empty_1(self):
        self.device = Mock(**self.empty_output)
        obj = ShowIpStaticRoute(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()


    def test_show_ip_static_route_1(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_1)
        obj = ShowIpStaticRoute(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output_1)

    def test_show_ip_static_route_2(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_2)
        obj = ShowIpStaticRoute(device=self.device)
        parsed_output = obj.parse(vrf='VRF1')
        self.assertEqual(parsed_output, self.golden_parsed_output_2)

# ============================================
# unit test for 'show ipv6 static detail'
# =============================================
class test_show_ipv6_static_detail(test_show_ipv6_static_detail_iosxe):

    def test_empty_detail_1(self):
        self.device = Mock(**self.empty_output)
        obj = ShowIpv6StaticDetail(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()


    def test_show_ip_static_detail_1(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_detail_1)
        obj = ShowIpv6StaticDetail(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output_detail_1)

    def test_show_ip_static_route_2(self):
         self.maxDiff = None
         self.device = Mock(**self.golden_output_detail_2)
         obj = ShowIpv6StaticDetail(device=self.device)
         parsed_output = obj.parse(vrf='VRF1')
         self.assertEqual(parsed_output, self.golden_parsed_output_detail_2)

if __name__ == '__main__':
    unittest.main()