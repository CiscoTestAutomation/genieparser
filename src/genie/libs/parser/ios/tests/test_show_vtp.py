# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device

# Metaparset
from genie.metaparser.util.exceptions import SchemaEmptyParserError, \
                                       SchemaMissingKeyError

# Parser
from genie.libs.parser.ios.show_vtp import ShowVtpStatus

from genie.libs.parser.iosxe.tests.test_show_vtp import \
        test_show_vtp_status as test_show_vtp_status_iosxe


# ============================================
# unit test for 'show vtp status'
# ============================================
class test_show_vtp_status(test_show_vtp_status_iosxe):
    
    pass


    # def test_empty(self):
    #     self.device1 = Mock(**self.empty_output)
    #     obj = ShowVtpStatus(device=self.device1)
    #     with self.assertRaises(SchemaEmptyParserError):
    #         parsed_output = obj.parse()

    # def test_golden(self):
    #     self.device = Mock(**self.golden_output)
    #     obj = ShowVtpStatus(device=self.device)
    #     parsed_output = obj.parse()
    #     self.maxDiff = None
    #     self.assertEqual(parsed_output,self.golden_parsed_output)


if __name__ == '__main__':
    unittest.main()