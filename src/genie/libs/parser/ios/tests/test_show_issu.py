
# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device

# Genie
from genie.metaparser.util.exceptions import SchemaEmptyParserError
from genie.libs.parser.ios.show_issu import ShowIssuStateDetail,\
                                              ShowIssuRollbackTimer

from genie.libs.parser.iosxe.tests.test_show_issu import test_show_issu_state_detail as test_show_issu_state_detail_iosxe,\
                                                         test_show_issu_rollback_timer as test_show_issu_rollback_timer_iosxe


# =======================================
#  Unit test for 'show issu state detail'
# =======================================
class test_show_issu_state_detail(test_show_issu_state_detail_iosxe):

    golden_output_ios = {'execute.return_value': '''
        Router# show issu state detail
 
        --- Starting installation state synchronization ---
        Finished installation state synchronization
        No ISSU operation is in progress
    '''}

    golden_parsed_output_ios = {
        "slot": {
            "default": {
                "issu_in_progress": False
            }
        }
     }

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowIssuStateDetail(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()    

    def test_golden_ios(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_ios)
        obj = ShowIssuStateDetail(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_ios)
        

# =========================================
#  Unit test for 'show issu rollback-timer'
# =========================================
class test_show_issu_rollback_timer(test_show_issu_rollback_timer_iosxe):

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowIssuRollbackTimer(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()    

    def test_golden_1(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_1)
        obj = ShowIssuRollbackTimer(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_1)

    def test_golden_2(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_2)
        obj = ShowIssuRollbackTimer(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_2)


if __name__ == '__main__':
    unittest.main()
