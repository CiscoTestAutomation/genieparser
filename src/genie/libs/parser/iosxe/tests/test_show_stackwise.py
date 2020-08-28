import unittest
from unittest.mock import Mock

from genie.metaparser.util.exceptions import SchemaEmptyParserError
from genie.libs.parser.iosxe.show_stackwise import Show_Stackwise_Virtual_Dual_Active_Detection


# ============================================================
# Unit test for 'show_stackwise_virtual_dual_active_detection'
# ============================================================
class test_show_stackwise_virtual_dual_active_detection(unittest.TestCase):
    """Unit test for 'show_stackwise_virtual_dual_active_detection'"""

    maxDiff = None
    empty_output = {'execute.return_value': ''}
    golden_parsed_output1 = {
        "dad_port": {
            "switches": {
                1: {
                    "FortyGigabitEthernet1/0/3": {
                        "status": "up"
                    },
                    "FortyGigabitEthernet1/0/4": {
                        "status": "up"
                    }
                },
                2: {
                    "FortyGigabitEthernet2/0/3": {
                        "status": "up"
                        },
                    "FortyGigabitEthernet2/0/4": {
                        "status": "up"
                        }
                }
            }
        }
    }

    golden_output1 = {'execute.return_value': '''
Dual-Active-Detection Configuration:
-------------------------------------
Switch  Dad port                        Status
------  ------------                    ---------
1       FortyGigabitEthernet1/0/3       up
        FortyGigabitEthernet1/0/4       up
2       FortyGigabitEthernet2/0/3       up
        FortyGigabitEthernet2/0/4       up   
    '''}

    def test_show_stackwise_virtual_dual_active_detection_full(self):
        self.device = Mock(**self.golden_output1)
        obj = Show_Stackwise_Virtual_Dual_Active_Detection(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output1)

    def test_show_stackwise_virtual_dual_active_detection_empty(self):
        self.device = Mock(**self.empty_output)
        obj = Show_Stackwise_Virtual_Dual_Active_Detection(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()


if __name__ == '__main__':
    unittest.main()
