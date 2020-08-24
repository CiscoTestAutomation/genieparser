# Python
import unittest
from unittest.mock import Mock

# ATS
from pyats.topology import Device

# Metaparset
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# Parser
from genie.libs.parser.iosxe.show_app_hosting import ShowApphostingList


# ============================================
# Parser for the following commands
#   * 'show app-hosting list'
# ============================================
class TestShowApphostingList(unittest.TestCase):
    device = Device(name='aDevice')
    maxDiff = None 
    empty_output = {'execute.return_value' : ''}
    golden_output = {'execute.return_value': '''
        vm11#show app-hosting list                                                                                                                                
        App id                                   State                                                                                                            
        ---------------------------------------------------------                                                                                                 
        utd                                      RUNNING   
        '''
        }

    golden_parsed_output = {
        'app_id': {
            'utd': {
                'state': 'RUNNING'
                }
            }
        }

    
    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowApphostingList(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()
    
    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = ShowApphostingList(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output)

if __name__ == '__main__':
	unittest.main()