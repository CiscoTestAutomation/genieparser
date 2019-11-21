import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device

from genie.metaparser.util.exceptions import SchemaEmptyParserError, \
                                       SchemaMissingKeyError

from genie.libs.parser.ios.show_routing import (ShowIpRoute,
                                            ShowIpRouteWord,
                                            ShowIpv6Route, 
                                            ShowIpv6RouteWord,
                                            ShowIpv6RouteUpdated, 
                                            ShowIpRouteSummary)

from genie.libs.parser.iosxe.tests.test_show_routing import \
                        TestShowIpRoute as test_show_ip_route_iosxe,\
                        TestShowIpv6RouteUpdated as test_show_ipv6_route_updated_iosxe,\
                        TestShowIpv6RouteWord as test_show_ipv6_route_word_iosxe,\
                        TestShowIpRouteSummary as test_show_ip_route_summary_iosxe

# ============================================
# unit test for 'show ip route'
# =============================================
class test_show_ip_route_ios(unittest.TestCase):
    """
       unit test for show ip route
    """
    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output_with_route ={
        "entry": {
            "192.168.234.0/24": {
                "mask": "24",
                "type": "internal",
                "known_via": "eigrp 1",
                "ip": "192.168.234.0",
                "redist_via": "eigrp",
                "distance": "90",
                "metric": "3072",
                "redist_via_tag": "1",
                "update": {
                    "age": "3d04h",
                    "interface": "GigabitEthernet0/2.4",
                    "from": "192.168.9.2"
                },
                "paths": {
                    1: {
                        "age": "3d04h",
                        "interface": "GigabitEthernet0/2.4",
                        "from": "192.168.9.2",
                        "metric": "3072",
                        "share_count": "1",
                        "nexthop": "192.168.9.2",
                        "merge_labels": False,
                        "prefer_non_rib_labels": False,
                    }
                }
            }
        },
        "total_prefixes": 1
    }

    golden_output_with_route = {'execute.return_value':'''
    show ip route 192.168.234.0
    Routing entry for 192.168.234.0/24
      Known via "eigrp 1", distance 90, metric 3072, type internal
      Redistributing via eigrp 1
      Last update from 192.168.9.2 on GigabitEthernet0/2.4, 3d04h ago
      Routing Descriptor Blocks:
      * 192.168.9.2, from 192.168.9.2, 3d04h ago, via GigabitEthernet0/2.4
          Route metric is 3072, traffic share count is 1
          Total delay is 20 microseconds, minimum bandwidth is 1000000 Kbit
          Reliability 255/255, minimum MTU 1500 bytes
          Loading 1/255, Hops 1
      '''}

    def test_empty_1(self):
        self.device = Mock(**self.empty_output)
        obj = ShowIpRouteWord(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse(route='192.168.234.0')

    def test_show_ip_route_with_route(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_with_route)
        obj = ShowIpRouteWord(device=self.device)
        parsed_output = obj.parse(route='192.168.234.0')
        self.assertEqual(parsed_output, self.golden_parsed_output_with_route)

class test_show_ip_route(test_show_ip_route_iosxe):

    def test_empty_1(self):
        self.device = Mock(**self.empty_output)
        obj = ShowIpRoute(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_show_ip_route_1(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_1)
        obj = ShowIpRoute(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output_1)

    def test_show_ip_route_2_with_vrf(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_2_with_vrf)
        obj = ShowIpRoute(device=self.device)

        parsed_output = obj.parse(vrf='VRF1')
        self.assertEqual(parsed_output, self.golden_parsed_output_2_with_vrf)

###################################################
# unit test for show ipv6 route updated
####################################################
class test_show_ipv6_route_updated(test_show_ipv6_route_updated_iosxe):

    def test_empty_1(self):
        self.device = Mock(**self.empty_output)
        obj = ShowIpv6RouteUpdated(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_show_ipv6_route_1(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_1)
        obj = ShowIpv6RouteUpdated(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output_1)

    def test_show_ipv6_route_2(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_2)
        obj = ShowIpv6RouteUpdated(device=self.device)
        parsed_output = obj.parse(vrf='VRF1')
        self.assertEqual(parsed_output,self.golden_parsed_output_2)

###################################################
# unit test for show ipv6 route <WROD>
####################################################
class test_show_ipv6_route_word(test_show_ipv6_route_word_iosxe):
    """unit test for show ipv6 route <WORD>"""

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowIpv6RouteWord(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse(route='2001:db8:400:4::4:1')

    def test_golden(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_with_ipv6_route)
        obj = ShowIpv6RouteWord(device=self.device)
        parsed_output = obj.parse(route='2001:db8:400:4::4:1')
        self.assertEqual(parsed_output,self.golden_parsed_output_with_route)


###################################################
# unit test for show ip route summary
####################################################
class test_show_ip_route_summary(test_show_ip_route_summary_iosxe):

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowIpRouteSummary(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden_1(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_1)
        obj = ShowIpRouteSummary(device=self.device)
        parsed_output = obj.parse(vrf='VRF1')
        self.assertEqual(parsed_output,self.golden_parsed_output_1)



if __name__ == '__main__':
    unittest.main()