# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device

# Metaparset
from genie.metaparser.util.exceptions import SchemaEmptyParserError, \
                                       SchemaMissingKeyError

from genie.libs.parser.iosxe.tests.test_show_config import test_show_configuration_lock as test_show_configuration_lock_iosxe

# Parser
from genie.libs.parser.ios.show_config import ShowConfigurationLock


# ======================================================
# Parser for 'show configuration lock'
#=======================================================
class test_show_configuration_lock(test_show_configuration_lock_iosxe):

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowConfigurationLock(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = ShowConfigurationLock(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)
    
    def test_golden_optional(self):
        self.device = Mock(**self.golden_output_optional)
        obj = ShowConfigurationLock(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_optional)

if __name__ == '__main__':
    unittest.main()
