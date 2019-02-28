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
    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_parsed_ios = {'vrf':
                             {'default':
                                  {'address_family':
                                       {'ipv4 unicast':
                                            {'ip':
                                                 {'0.0.0.0/24':
                                                      {'nexthop':
                                                           {'172.16.1.1':
                                                                {'protocol':
                                                                     {'static':
                                                                          {'metric': '0',
                                                                           'preference': '254',
                                                                           'uptime': '01:40:40'}}}}}}}}}}}

    golden_output_ios = {'execute.return_value': '''
      R1#show ip route
      Codes: L - local, C - connected, S - static, R - RIP, M - mobile, B - BGP
        D - EIGRP, EX - EIGRP external, O - OSPF, IA - OSPF inter area
        N1 - OSPF NSSA external type 1, N2 - OSPF NSSA external type 2
        E1 - OSPF external type 1, E2 - OSPF external type 2
        i - IS-IS, su - IS-IS summary, L1 - IS-IS level-1, L2 - IS-IS level-2
        ia - IS-IS inter area, * - candidate default, U - per-user static route
        o - ODR, P - periodic downloaded static route, H - NHRP, l - LISP
        a - application route
        + - replicated route, % - next hop override, p - overrides from PfR

        S*       0.0.0.0 [254/0] via 172.16.1.1

      '''}

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
