# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError, SchemaMissingKeyError

from genie.libs.parser.ios.show_protocols import ShowIpProtocols, \
                                                 ShowIpProtocolsSectionRip, \
                                                 ShowIpv6ProtocolsSectionRip

from genie.libs.parser.iosxe.tests.test_show_protocols import test_show_ip_protocols as \
                                                              test_show_ip_protocols_iosxe, \
                                                              test_show_ip_protocols_section_rip as \
                                                              test_show_ip_protocols_section_rip_iosxe, \
                                                              test_show_ipv6_protocols as \
                                                              test_show_ipv6_protocols_iosxe

from genie.libs.parser.utils.common import format_output                                                        
# =================================
# Unit test for 'show ip protocols'
# =================================
class test_show_ip_protocols(test_show_ip_protocols_iosxe):

    def test_show_ip_protocols_full1(self):
        super().test_show_ip_protocols_full1()
        self.maxDiff = None

        def mapper(key):
            return self.outputs[key]

        self.device.execute = Mock()
        self.device.execute.side_effect = mapper
        
        obj = ShowIpProtocols(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output1)

    def test_show_ip_protocols_full2(self):
        super().test_show_ip_protocols_full2()
        
        self.maxDiff = None

        def mapper(key):
            return self.outputs[key]

        self.device.execute = Mock()
        self.device.execute.side_effect = mapper
        
        obj = ShowIpProtocols(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output2)

    def test_show_ip_protocols_empty(self):
        self.maxDiff = None
        self.device = Mock(**self.empty_output)
        obj = ShowIpProtocols(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

class test_show_ip_protocols_section_rip(test_show_ip_protocols_section_rip_iosxe):
    golden_parsed_output_ios = {
        'protocols': {
            'bgp': {
                'instance': {
                    'default': {
                        'bgp_id': 100,
                        'vrf': {
                            'default': {
                                'address_family': {
                                    'ipv4': {
                                        'igp_sync': False,
                                        'automatic_route_summarization': False,
                                        'redistribute': {
                                            'connected': {
                                                },
                                            'static': {
                                                },
                                            },
                                        'neighbor': {
                                            '10.13.13.13': {
                                                'neighbor_id': '10.13.13.13',
                                                'distance': 200,
                                                'last_update': '02:20:54',
                                                },
                                            '10.18.18.18': {
                                                'neighbor_id': '10.18.18.18',
                                                'distance': 200,
                                                'last_update': '03:26:15',
                                                },
                                            },
                                        'preference': {
                                            'multi_values': {
                                                'external': 20,
                                                'internal': 200,
                                                'local': 200,
                                                },
                                            },
                                        'timers': {
                                            'update_interval': 60,
                                            'next_update': 0,
                                        },
                                        },
                                    },
                                },
                            },
                        },
                    },
                },
            },
        }

    golden_output_ios = {'execute.return_value': '''\
    Router# show ip protocols vrf vpn1
    Routing Protocol is "bgp 100"
      Sending updates every 60 seconds, next due in 0 sec
      Outgoing update filter list for all interfaces is
      Incoming update filter list for all interfaces is
      IGP synchronization is disabled
      Automatic route summarization is disabled
      Redistributing:connected, static
      Routing for Networks:
      Routing Information Sources:
        Gateway         Distance      Last Update
        10.13.13.13          200      02:20:54
        10.18.18.18          200      03:26:15
      Distance:external 20 internal 200 local 200
      '''
      }
    def test_empty(self):
        self.device1 = Mock(**self.empty_output)
        obj = ShowIpProtocolsSectionRip(device=self.device1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden_vrf_default(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output)
        obj = ShowIpProtocolsSectionRip(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)

    def test_golden_vrf_vrf1(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_2)
        obj = ShowIpProtocolsSectionRip(device=self.device)
        parsed_output = obj.parse(vrf="VRF1")
        self.assertEqual(parsed_output, self.golden_parsed_output_2)

    def test_golden_vrf_vrf_ios(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_ios)
        obj = ShowIpProtocolsSectionRip(device=self.device)
        parsed_output = obj.parse(vrf="VRF1")
        self.assertEqual(parsed_output, self.golden_parsed_output_ios)


# ============================================
# unit test for 'show ipv6 protocols | sec rip'
# unit test for 'show ipv6 protocols vrf {vrf} | sec rip'
# ============================================
class test_show_ipv6_protocols(test_show_ipv6_protocols_iosxe):

    def test_empty(self):
        self.device1 = Mock(**self.empty_output)
        obj = ShowIpv6ProtocolsSectionRip(device=self.device1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden_vrf_default(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output)
        obj = ShowIpv6ProtocolsSectionRip(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)

    def test_golden_vrf_vrf1(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_2)
        obj = ShowIpv6ProtocolsSectionRip(device=self.device)
        parsed_output = obj.parse(vrf="VRF1")
        self.assertEqual(parsed_output, self.golden_parsed_output_2)


if __name__ == '__main__':
    unittest.main()
