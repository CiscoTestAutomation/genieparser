# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device

# Metaparset
from genie.metaparser.util.exceptions import SchemaEmptyParserError, \
                                       SchemaMissingKeyError

# Parser
from genie.libs.parser.iosxe.show_service import ShowServiceGroupState


# ============================================
# Parser for 'show service-group state'
# ============================================
class test_show_service_group_state(unittest.TestCase):
    
    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}
    
    golden_parsed_output = {
        'service_group_state':{
            1 : {
                'state' : 'Up'
            }
        }
    }

    golden_output = {'execute.return_value': '''\
        Load for five secs: 98%/0%; one minute: 98%; five minutes: 96%
        Time source is NTP, 18:59:13.897 JST Web Nov 9 2016

        Group    State
            1       Up
    '''}


    def test_empty(self):
        self.device1 = Mock(**self.empty_output)
        obj = ShowServiceGroupState(device=self.device1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = ShowServiceGroupState(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output)


if __name__ == '__main__':
    unittest.main()