# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device

# Genie
from genie.metaparser.util.exceptions import SchemaEmptyParserError
from genie.libs.parser.iosxe.c9500.show_issu import ShowIssuStateDetail,\
                                                    ShowIssuRollbackTimer


# =======================================
#  Unit test for 'show issu state detail'
# =======================================
class test_show_issu_state_detail(unittest.TestCase):

    device = Device(name='aDevice')

    empty_output = {'execute.return_value': ''}

    golden_output_1 = {'execute.return_value': '''
        show issu state detail

        --- Starting local lock acquisition on R0 ---

        Finished local lock acquisition on R0



        Current ISSU Status: Disabled       

        Previous ISSU Operation: N/A        

        =======================================================

        System Check                        Status

        -------------------------------------------------------

        Platform ISSU Support               No

        Standby Online                      No

        Autoboot Enabled                    Yes

        SSO Mode                            No

        Install Boot                        No

        Valid Boot Media                    Yes

        =======================================================

        No ISSU operation is in progress


    '''}

    golden_parsed_output_1 = {
        "slot": {
            "R0": {
                "issu_in_progress": False,
                "current_status": "Disabled",
                'previous_operation': 'N/A',
                "system_check": {
                    "platform_issu_support": "No",
                    "standby_online": "No",
                    "autoboot_enabled": "Yes",
                    "sso_mode": "No",
                    "install_boot": "No",
                    "valid_boot_media": "Yes"
                }
            }
        }
    }

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowIssuStateDetail(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()    

    def test_golden_1(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_1)
        obj = ShowIssuStateDetail(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_1)


# =========================================
#  Unit test for 'show issu rollback-timer'
# =========================================
class test_show_issu_rollback_timer(unittest.TestCase):

    device = Device(name='aDevice')

    empty_output = {'execute.return_value': ''}

    golden_output_1 = {'execute.return_value': '''
        show issu rollback-timer

        --- Starting local lock acquisition on R0 ---

        Finished local lock acquisition on R0



        Rollback: inactive, no ISSU operation is in progress

    '''}

    golden_parsed_output_1 = {
        'rollback_timer_reason': 'no ISSU operation is in progress',
        'rollback_timer_state': 'inactive',
    }

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


if __name__ == '__main__':
    unittest.main()
