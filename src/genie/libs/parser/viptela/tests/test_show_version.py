# Python
import unittest
from unittest.mock import Mock

# ATS
from pyats.topology import Device

# Metaparset
from genie.metaparser.util.exceptions import SchemaEmptyParserError,\
                                             SchemaMissingKeyError

# Parser
from genie.libs.parser.viptela.show_version import ShowVersion


# ============================================
# Parser for the following commands
#   * 'show version'
# ============================================
class TestShowVersion(unittest.TestCase):
    device = Device(name='aDevice')
    maxDiff = None 
    empty_output = {'execute.return_value' : ''}

    golden_output = {'execute.return_value': '''
        srp_vedge# show version
        99.99.999-4567
    '''}

    golden_parsed_output = {'version': '99.99.999-4567'}

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowVersion(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()
    
    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = ShowVersion(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output)


if __name__ == '__main__':
		unittest.main()   