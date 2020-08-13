# Python
import unittest
from unittest.mock import Mock

# ATS
from pyats.topology import Device

# Metaparset
from genie.metaparser.util.exceptions import SchemaEmptyParserError,\
                                             SchemaMissingKeyError

# Parser
from genie.libs.parser.iosxe.show_sdwan_reboot_history import ShowSdwanRebootHistory


# ============================================
# Parser for the following commands
#   * 'show sdwan reboot history'
# ============================================
class TestShowSdwanRebootHistory(unittest.TestCase):
    device = Device(name='aDevice')
    maxDiff = None 
    empty_output = {'execute.return_value' : ''}
    golden_output = {'execute.return_value': '''
        srp_vedge# show reboot history

        REBOOT DATE TIME           REBOOT REASON                                 
        -------------------------------------------------------------------------
        2020-06-04T04:54:36+00:00  Initiated by user                             
        2020-06-16T09:19:57+00:00  Initiated by user                             
        2020-06-18T13:28:53+00:00  Initiated by user - activate 99.99.999-4542  
    '''}

    golden_parsed_output = {'reboot_date_time': {
                    '2020-06-04T04:54:36+00:00': {
                        'reboot_reason': 'Initiated by user'
                        },
                    '2020-06-16T09:19:57+00:00': {
                        'reboot_reason': 'Initiated by user'
                        },
                    '2020-06-18T13:28:53+00:00': {
                        'reboot_reason': 'Initiated by user - activate 99.99.999-4542'
                }
            }
        }
    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowSdwanRebootHistory(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()
    
    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = ShowSdwanRebootHistory(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output)

if __name__ == '__main__':
		unittest.main()   