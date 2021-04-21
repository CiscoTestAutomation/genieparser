# Python
import unittest
from unittest.mock import Mock

# ATS
from pyats.topology import Device

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

from genie.libs.parser.ios.show_protocols import ShowIpProtocols

from genie.libs.parser.iosxe.tests.test_show_protocols import TestShowIpProtocols as \
                                                              TestShowIpProtocols_iosxe

from genie.libs.parser.utils.common import format_output                                                        
# =================================
# Unit test for 'show ip protocols'
# =================================
class TestShowIpProtocols(TestShowIpProtocols_iosxe):

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

if __name__ == '__main__':
    unittest.main()