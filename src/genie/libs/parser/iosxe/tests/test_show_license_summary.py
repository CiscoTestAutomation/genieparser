# Python
import unittest
from unittest.mock import Mock

# ATS
from pyats.topology import Device

# Metaparset
from genie.metaparser.util.exceptions import SchemaEmptyParserError, \
                                       SchemaMissingKeyError

# Parser
from genie.libs.parser.iosxe.show_license import ShowLicenseSummary

# ============================================
# Test for 'show license summary'
# ============================================
class test_show_license_summary(unittest.TestCase):
    
    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}
    
    golden_parsed_output = {
       'license_usage':{
          'network-advantage':{
             'entitlement':'(C9300-48 Network Advan...)',
             'count':'1',
             'status':'IN USE'
          },
          'dna-advantage':{
             'entitlement':'(C9300-48 DNA Advantage)',
             'count':'1',
             'status':'IN USE'
          }
       }
    }

    golden_output = {'execute.return_value': '''\
    License Usage:
    License                 Entitlement Tag               Count Status
    -----------------------------------------------------------------------------
    network-advantage       (C9300-48 Network Advan...)       1 IN USE
    dna-advantage           (C9300-48 DNA Advantage)          1 IN USE
    '''}

    def test_empty(self):
        self.device1 = Mock(**self.empty_output)
        obj = ShowLicenseSummary(device=self.device1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = ShowLicenseSummary(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output)



if __name__ == '__main__':
    unittest.main()