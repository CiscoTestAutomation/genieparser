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

from genie.libs.parser.iosxe.tests.test_show_rpf import test_show_ipv6_rpf as test_show_ipv6_rpf_iosxe

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
                "source_address": "192.168.16.226",
                "source_host": "?",
                "mofrr": "Enabled",
                "path": {
                    "192.168.145.2 Ethernet1/4": {
                        "interface_name": "Ethernet1/4",
                        "neighbor_host": "?",
                        "neighbor_address": "192.168.145.2",
                        "table_type": "unicast",
                        "table_feature": "ospf",
                        "table_feature_instance": "200",
                        "distance_preferred_lookup": True,
                        "lookup_topology": "ipv4 multicast base",
                        "originated_topology": "ipv4 unicast base"
                    }
                }
            }
        }
    }

    golden_output = {'execute.return_value': '''\
        Router# show ip rpf 192.168.16.226
        RPF information for ? (192.168.16.226) MoFRR Enabled
          RPF interface: Ethernet1/4
          RPF neighbor: ? (192.168.145.2)
          RPF route/mask: 255.255.255.225
          RPF type: unicast (ospf 200)
          Doing distance-preferred lookups across tables
          RPF topology: ipv4 multicast base, originated from ipv4 unicast base
    '''}

    golden_parsed_output2 = {
        "vrf": {
            "VRF1": {
                "source_address": "192.168.16.226",
                "source_host": "?",
                "mofrr": "Enabled",
                "path": {
                    "192.168.145.2 Ethernet1/4": {
                        "interface_name": "Ethernet1/4",
                        "neighbor_host": "?",
                        "neighbor_address": "192.168.145.2",
                        "table_type": "unicast",
                        "table_feature": "ospf",
                        "table_feature_instance": "200",
                        "distance_preferred_lookup": True,
                        "lookup_topology": "ipv4 multicast base",
                        "originated_topology": "ipv4 unicast base"
                    }
                }
            }
        }
    }

    golden_output2 = {'execute.return_value': '''\
        Router# show ip rpf 192.168.16.226
        RPF information for ? (192.168.16.226) MoFRR Enabled
          RPF interface: Ethernet1/4
          RPF neighbor: ? (192.168.145.2)
          RPF route/mask: 255.255.255.225
          RPF type: unicast (ospf 200)
          Doing distance-preferred lookups across tables
          RPF topology: ipv4 multicast base, originated from ipv4 unicast base
    '''}

    def test_empty(self):
        self.device1 = Mock(**self.empty_output)
        obj = ShowIpRpf(device=self.device1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse(mroute='172.16.10.13')

    def test_golden_vrf_default(self):
        self.device = Mock(**self.golden_output)
        obj = ShowIpRpf(device=self.device)
        parsed_output = obj.parse(mroute='192.168.16.226')
        self.assertEqual(parsed_output,self.golden_parsed_output)

    def test_golden_vrf_non_default(self):
        self.device = Mock(**self.golden_output2)
        obj = ShowIpRpf(device=self.device)
        parsed_output = obj.parse(mroute='192.168.16.226', vrf='VRF1')
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