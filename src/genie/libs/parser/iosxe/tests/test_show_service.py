# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device

# Metaparset
from genie.metaparser.util.exceptions import SchemaEmptyParserError, \
                                       SchemaMissingKeyError

# Parser
from genie.libs.parser.iosxe.show_service import ShowServiceGroupStats


# ============================================
# Parser for 'show service-group stats'
# ============================================
class test_show_service_group_stats(unittest.TestCase):
    
    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}
    
    golden_parsed_output = {
        'global_statistics': {
            'num_of_groups' : 1,
            'num_of_members' : 2
        },
        'Service Group 1 statistics' : {
            'num_of_interfaces' : 1,
            'num_of_members' : 2,
            'Sub-interface': 2,
            'members_joined': 103,
            'members_left': 101
        }
    }

    golden_output = {'execute.return_value': '''\
        Load for five secs: 98%/0%; one minute: 98%; five minutes: 96%
        Time source is NTP, 18:59:13.897 JST Web Nov 9 2016

        Service Group global statistics:
         Number of groups:     1
         Number of members:    2
        Service Group 1 statistics:
         Number of Interfaces: 1
         Number of members:    2
          Sub-interface:       2
         Members joined:       103
         Members left:         101

    '''}

    def test_empty(self):
        self.device1 = Mock(**self.empty_output)
        obj = ShowServiceGroupStats(device=self.device1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = ShowServiceGroupStats(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output)


if __name__ == '__main__':
    unittest.main()