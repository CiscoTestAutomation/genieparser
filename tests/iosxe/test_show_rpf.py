# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device

# Metaparset
from genie.metaparser.util.exceptions import SchemaEmptyParserError, \
                                       SchemaMissingKeyError

# Parser
from genie.libs.parser.iosxe.show_rpf import ShowIpRpf, ShowIpv6Rpf


# =============================================
# Unit test for 'show ip rpf <x.x.x.x>'
# Unit test for 'show ip rpf vrf xxx <x.x.x.x>'
# ==============================================
class test_show_ip_rpf(unittest.TestCase):
    
    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}
    
    golden_parsed_output = {
        "vrf": {
            "default": {
                 "source_address": "172.16.10.13",
                 "path": {
                      "172.16.121.10 BRI0": {
                           "neighbor_address": "172.16.121.10",
                           "neighbor_host": "sj1.cisco.com",
                           "distance_preferred_lookup": True,
                           "recursion_count": 0,
                           "interface_name": "BRI0",
                           "originated_topology": "ipv4 unicast base",
                           "lookup_topology": "ipv4 multicast base",
                           "route_mask": "172.16.0.0/16",
                           "table_type": "unicast"
                      }
                 },
                 "source_host": "host1"
            }}}

    golden_output = {'execute.return_value': '''\
        RPF information for host1 (172.16.10.13)
          RPF interface: BRI0
          RPF neighbor: sj1.cisco.com (172.16.121.10)
          RPF route/mask: 172.16.0.0/255.255.0.0
          RPF type: unicast
          RPF recursion count: 0
          Doing distance-preferred lookups across tables
          RPF topology: ipv4 multicast base, originated from ipv4 unicast base
    '''}

    golden_parsed_output2 = {
        "vrf": {
            "VRF1": {
                 "source_host": "?",
                 "source_address": "10.1.1.100",
                 "path": {
                      "10.1.1.5 Ethernet3/0": {
                           "neighbor_address": "10.1.1.5",
                           "table_feature": "rip",
                           "neighbor_host": "?",
                           "interface_name": "Ethernet3/0",
                           "table_type": "unicast",
                           "lookup_vrf": "blue",
                           "recursion_count": 0,
                           "distance_preferred_lookup": True,
                           "route_mask": "10.1.1.0/24"
                      }}}}}

    golden_output2 = {'execute.return_value': '''\
        RPF information for ? (10.1.1.100)
          RPF interface: Ethernet3/0
          RPF neighbor: ? (10.1.1.5)
          RPF route/mask: 10.1.1.0/24
          RPF type: unicast (rip)
          RPF recursion count: 0
          Doing distance-preferred lookups across tables
          Using Group Based VRF Select, RPF VRF: blue
    '''}

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
class test_show_ipv6_rpf(unittest.TestCase):
    
    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}
    
    golden_parsed_output = {
        "vrf": {
            "default": {
                 "source_address": "2001:99:99::99",
                 "path": {
                      "2001:99:99::99 GigabitEthernet1 128": {
                           "table_type": "mroute",
                           "admin_distance": "128",
                           "recursion_count": 0,
                           "interface_name": "GigabitEthernet1",
                           "metric": 0,
                           "neighbor_address": "2001:99:99::99",
                           "route_mask": "2001:99:99::99/128"
                      }}}}}

    golden_output = {'execute.return_value': '''\
        RPF information for 2001:99:99::99
          RPF interface: GigabitEthernet1
          RPF neighbor: 2001:99:99::99
          RPF route/mask: 2001:99:99::99/128
          RPF type: Mroute
          RPF recursion count: 0
          Metric preference: 128
          Metric: 0
    '''}

    golden_parsed_output2 = {
        "vrf": {
            "VRF1": {
                 "source_address": "2001:99:99::99",
                 "path": {
                      "2001:99:99::99 GigabitEthernet3 128": {
                           "table_type": "mroute",
                           "admin_distance": "128",
                           "recursion_count": 0,
                           "interface_name": "GigabitEthernet3",
                           "metric": 0,
                           "neighbor_address": "2001:99:99::99",
                           "route_mask": "2001:99:99::99/128"
                      }}}}}

    golden_output2 = {'execute.return_value': '''\
        RPF information for 2001:99:99::99
          RPF interface: GigabitEthernet3
          RPF neighbor: 2001:99:99::99
          RPF route/mask: 2001:99:99::99/128
          RPF type: Mroute
          RPF recursion count: 0
          Metric preference: 128
          Metric: 0
    '''}

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