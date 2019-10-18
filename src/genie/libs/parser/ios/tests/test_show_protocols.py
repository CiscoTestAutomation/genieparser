# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

from genie.libs.parser.ios.show_protocols import (ShowIpProtocols, 
                                                  ShowIpProtocolsSectionRip, 
                                                  ShowIpv6ProtocolsSectionRip,)

from genie.libs.parser.iosxe.tests.test_show_protocols import TestShowIpProtocols as \
                                                              TestShowIpProtocolsXE, \
                                                              TestShowIpProtocolsSectionRip as \
                                                              TestShowIpProtocolsSectionRipXE, \
                                                              TestShowIpv6Protocols as \
                                                              TestShowIpv6ProtocolsXE

from genie.libs.parser.utils.common import format_output                                                        
# =================================
# Unit test for 'show ip protocols'
# =================================
class TestShowIpProtocols(TestShowIpProtocolsXE):

    def test_show_ip_protocols_full1(self):
        super().test_show_ip_protocols_1()
        self.maxDiff = None

        def mapper(key):
            return self.outputs[key]

        self.device.execute = Mock()
        self.device.execute.side_effect = mapper
        
        obj = ShowIpProtocols(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_1)

    def test_show_ip_protocols_full2(self):
        super().test_show_ip_protocols_2()
        
        self.maxDiff = None

        def mapper(key):
            return self.outputs[key]

        self.device.execute = Mock()
        self.device.execute.side_effect = mapper
        
        obj = ShowIpProtocols(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_2)

    def test_show_ip_protocols_empty(self):
        self.maxDiff = None
        self.device = Mock(**self.empty_output)
        obj = ShowIpProtocols(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

class TestShowIpProtocolsSectionRip(TestShowIpProtocolsSectionRipXE):
    
    def test_empty(self):
        self.device1 = Mock(**self.empty_output)
        obj = ShowIpProtocolsSectionRip(device=self.device1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden_vrf_default(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_1)
        obj = ShowIpProtocolsSectionRip(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_1)

    def test_golden_vrf_vrf1(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_2)
        obj = ShowIpProtocolsSectionRip(device=self.device)
        parsed_output = obj.parse(vrf="VRF1")
        self.assertEqual(parsed_output, self.golden_parsed_output_2)

# ============================================
# unit test for 'show ipv6 protocols | sec rip'
# unit test for 'show ipv6 protocols vrf {vrf} | sec rip'
# ============================================
class TestShowIpv6Protocols(TestShowIpv6ProtocolsXE):

    def test_empty(self):
        self.device1 = Mock(**self.empty_output)
        obj = ShowIpv6ProtocolsSectionRip(device=self.device1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden_vrf_default(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_1)
        obj = ShowIpv6ProtocolsSectionRip(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_1)

    def test_golden_vrf_vrf1(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_2)
        obj = ShowIpv6ProtocolsSectionRip(device=self.device)
        parsed_output = obj.parse(vrf="VRF1")
        self.assertEqual(parsed_output, self.golden_parsed_output_2)


if __name__ == '__main__':
    unittest.main()
