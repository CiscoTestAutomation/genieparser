import unittest
from unittest.mock import Mock

from ats.topology import Device

from genie.metaparser.util.exceptions import SchemaEmptyParserError

from genie.libs.parser.ios.show_ip_route import ShowIpRoute, ShowIpv6Route
from genie.libs.parser.iosxe.tests.test_show_ip_route import test_show_ip_route as test_show_ip_route_iosxe

# =========================================
#  Unit test for 'show ip route bgp'
#                'show ip route vrf <WORD> bgp'
#                'show ipv6 route bgp'
#                'show ipv6 route vrf <WORD> bgp'
# =========================================
class test_show_ip_route(test_show_ip_route_iosxe):

    def test_empty(self):
        self.device1 = Mock(**self.empty_output)
        route_map_obj = ShowIpRoute(device=self.device1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = route_map_obj.parse(protocol='bgp', ip='ip')

    def test_golden1(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output1)
        route_map_obj = ShowIpRoute(device=self.device)
        parsed_output = route_map_obj.parse(protocol='bgp', ip='ip')
        self.assertEqual(parsed_output,self.golden_parsed_output1)

    def test_golden2(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output2)
        route_map_obj = ShowIpRoute(device=self.device)
        parsed_output = route_map_obj.parse(protocol='bgp', vrf='VRF1', ip='ip')
        self.assertEqual(parsed_output,self.golden_parsed_output2)

    def test_golden3(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output3)
        route_map_obj = ShowIpv6Route(device=self.device)
        parsed_output = route_map_obj.parse(protocol='bgp', ip='ipv6')
        self.assertEqual(parsed_output,self.golden_parsed_output3)

    def test_golden4(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output4)
        route_map_obj = ShowIpv6Route(device=self.device)
        parsed_output = route_map_obj.parse(protocol='bgp', vrf='VRF1', ip='ipv6')
        self.assertEqual(parsed_output,self.golden_parsed_output4)

if __name__ == '__main__':
    unittest.main()
