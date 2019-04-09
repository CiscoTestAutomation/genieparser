
# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError,\
                                             SchemaMissingKeyError

# ios show_snmp
from genie.libs.parser.ios.show_snmp import ShowSnmpMib

# iosxe/test_show_snmp
from genie.libs.parser.iosxe.tests.test_show_snmp import \
        test_show_snmp_mib as test_show_snmp_mib_iosxe

# =============================
# Unit test for 'show snmp mib'
# =============================
class test_show_snmp_mib(test_show_snmp_mib_iosxe):
    '''Unit test for "show snmp mib" '''

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowSnmpMib(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden_1(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output1)
        obj = ShowSnmpMib(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output1)


if __name__ == '__main__':
    unittest.main()

