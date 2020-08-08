# Python
import unittest
from unittest.mock import Mock

# ATS
from pyats.topology import Device

# Metaparset
from genie.metaparser.util.exceptions import SchemaEmptyParserError,\
                                             SchemaMissingKeyError

# Parser
from genie.libs.parser.iosxe.show_sdwan_version import ShowSdwanVersion


# ============================================
# Parser for the following commands
#   * 'show sdwan version'
# ============================================
class TestShowSdwanVersion(unittest.TestCase):
    device = Device(name='aDevice')
    maxDiff = None 
    empty_output = {'execute.return_value' : ''}
    golden_output = {'execute.return_value': '''
        BR8-ISR4451#show sdwan version
        17.3.01.0.214   
    '''}

    golden_parsed_output = {'version': '17.3.01.0.214'}

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowSdwanVersion(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()
    
    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = ShowSdwanVersion(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output)

if __name__ == '__main__':
		unittest.main()   