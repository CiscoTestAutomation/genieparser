
# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device

# Genie
from genie.metaparser.util.exceptions import SchemaEmptyParserError
from genie.libs.parser.iosxe.show_issu import ShowIssuStateDetail,\
                                              ShowIssuRollbackTimer


# =======================================
#  Unit test for 'show issu state detail'
# =======================================
class test_show_issu_state_detail(unittest.TestCase):

    device = Device(name='aDevice')

    empty_output = {'execute.return_value': ''}

    golden_output_1 = {'execute.return_value': '''
        PE1#show issu state  detail 
        --- Starting local lock acquisition on R1 ---
        Finished local lock acquisition on R1

        Slot being modified: R1
          Loadversion time: 20180430 20:31:25 on vty 0
          Last operation: acceptversion
          Rollback: inactive, timer canceled by acceptversion
          Original (rollback) image: harddisk:asr1000rpx86-universalk9.16.08.01sprd1.SPA.bin
          Running image: harddisk:asr1000rpx86-universalk9.BLD_V168_1_THROTTLE_LATEST_20180426_165658_V16_8_0_265.SSA.bin
          Operating mode: sso, terminal state reached
        '''}

    golden_parsed_output_1 = {
        'slot': 
            {'R1': 
                {'issu_in_progress': True,
                'context': 'vty 0',
                'last_operation': 'acceptversion',
                'loadversion_time': '20180430 20:31:25',
                'operating_mode': 'sso',
                'original_rollback_image': 'harddisk:asr1000rpx86-universalk9.16.08.01sprd1.SPA.bin',
                'rollback_reason': 'timer canceled by acceptversion',
                'rollback_state': 'inactive',
                'running_image': 'harddisk:asr1000rpx86-universalk9.BLD_V168_1_THROTTLE_LATEST_20180426_165658_V16_8_0_265.SSA.bin',
                'runversion_executed': False,
                'terminal_state_reached': True}}}

    golden_output_2 = {'execute.return_value': '''
        PE1#show issu state detail 
        --- Starting local lock acquisition on R1 ---
        Finished local lock acquisition on R1

        Slot being modified: R1
          Loadversion time: 20180430 19:13:51 on vty 0
          Last operation: runversion
          Rollback: automatic, remaining time before rollback: 00:24:26
          Original (rollback) image: harddisk:asr1000rpx86-universalk9.16.08.01sprd1.SPA.bin
          Running image: harddisk:asr1000rpx86-universalk9.BLD_V168_1_THROTTLE_LATEST_20180426_165658_V16_8_0_265.SSA.bin
          Operating mode: sso, terminal state not reached
          Notes: runversion executed, active RP is being provisioned
        '''}

    golden_parsed_output_2 = {
        'slot': 
            {'R1': 
                {'issu_in_progress': True,
                'context': 'vty 0',
                'last_operation': 'runversion',
                'loadversion_time': '20180430 19:13:51',
                'operating_mode': 'sso',
                'original_rollback_image': 'harddisk:asr1000rpx86-universalk9.16.08.01sprd1.SPA.bin',
                'rollback_state': 'automatic',
                'rollback_time': '00:24:26',
                'running_image': 'harddisk:asr1000rpx86-universalk9.BLD_V168_1_THROTTLE_LATEST_20180426_165658_V16_8_0_265.SSA.bin',
                'runversion_executed': True,
                'terminal_state_reached': False}}}

    golden_output_3 = {'execute.return_value': '''
        PE1#show issu state detail 
        --- Starting local lock acquisition on R0 ---
        Finished local lock acquisition on R0

        --- Starting installation state synchronization ---
        Finished installation state synchronization

        --- Starting local lock acquisition on R1 ---
        Finished local lock acquisition on R1

        Slot being modified: R1
          Loadversion time: 20180430 19:13:51 on vty 0
          Last operation: loadversion
          Rollback: automatic, remaining time before rollback: 00:29:53
          Original (rollback) image: harddisk:asr1000rpx86-universalk9.16.08.01sprd1.SPA.bin
          Running image: harddisk:asr1000rpx86-universalk9.BLD_V168_1_THROTTLE_LATEST_20180426_165658_V16_8_0_265.SSA.bin
          Operating mode: sso, terminal state reached
        '''}

    golden_parsed_output_3 = {
        'slot':
            {'R0':
                {'issu_in_progress': False},
            'R1':
                {'issu_in_progress': True,
                'context': 'vty 0',
                'last_operation': 'loadversion',
                'loadversion_time': '20180430 19:13:51',
                'operating_mode': 'sso',
                'original_rollback_image': 'harddisk:asr1000rpx86-universalk9.16.08.01sprd1.SPA.bin',
                'rollback_state': 'automatic',
                'rollback_time': '00:29:53',
                'running_image': 'harddisk:asr1000rpx86-universalk9.BLD_V168_1_THROTTLE_LATEST_20180426_165658_V16_8_0_265.SSA.bin',
                'runversion_executed': False,
                'terminal_state_reached': True}}}

    golden_output_4 = {'execute.return_value': '''
        PE1#show issu state detail
        --- Starting local lock acquisition on R0 ---
        Finished local lock acquisition on R0

        --- Starting installation state synchronization ---
        Finished installation state synchronization

        No ISSU operation is in progress
        '''}

    golden_parsed_output_4 = {
        'slot':
            {'R0':
                {'issu_in_progress': False}}}

    golden_output_5 = {'execute.return_value': '''
        R1#show issu state detail
        --- Starting local lock acquisition on switch 1 ---
        Finished local lock acquisition on switch 1

        No ISSU operation is in progress
        '''}

    golden_parsed_output_5 = {
        'slot':
            {'1':
                {'issu_in_progress': False}}}

    golden_output_6 = {'execute.return_value': '''
                              Slot = 1
                      RP State = Active
                    ISSU State = Init
                 Boot Variable = bootdisk:,1;
                Operating Mode = sso
               Primary Version = N/A
             Secondary Version = N/A
               Current Version = bootdisk:s2t54-adventerprisek9-mz.SPA.151-1.SY.bin
                Variable Store = PrstVbl
    '''}

    golden_parsed_output_6 = {
        "slot": {
            "R1": {
                "rp_state": "Active",
                "issu_state": "Init",
                "boot_variable": "bootdisk:,1;",
                "operating_mode": "sso",
                "primary_version": "N/A",
                "secondary_version": "N/A",
                "running_image": "bootdisk:s2t54-adventerprisek9-mz.SPA.151-1.SY.bin",
                "variable_store": "PrstVbl",
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

    def test_golden_2(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_2)
        obj = ShowIssuStateDetail(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_2)

    def test_golden_3(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_3)
        obj = ShowIssuStateDetail(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_3)

    def test_golden_4(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_4)
        obj = ShowIssuStateDetail(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_4)

    def test_golden_5(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_5)
        obj = ShowIssuStateDetail(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_5)

    def test_golden_6(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_6)
        obj = ShowIssuStateDetail(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_6)

# =========================================
#  Unit test for 'show issu rollback-timer'
# =========================================
class test_show_issu_rollback_timer(unittest.TestCase):

    device = Device(name='aDevice')

    empty_output = {'execute.return_value': ''}

    golden_output_1 = {'execute.return_value': '''
        PE1#show issu rollback-timer 
        --- Starting local lock acquisition on R0 ---
        Finished local lock acquisition on R0

        --- Starting installation state synchronization ---
        Finished installation state synchronization

        Rollback: inactive, no ISSU operation is in progress
        '''}

    golden_parsed_output_1 = {
        'rollback_timer_reason': 'no ISSU operation is in progress',
        'rollback_timer_state': 'inactive'}

    golden_output_2 = {'execute.return_value': '''
        PE1#show issu rollback-timer 
        --- Starting local lock acquisition on R0 ---
        Finished local lock acquisition on R0

        --- Starting installation state synchronization ---
        Finished installation state synchronization

        Rollback: inactive, timer canceled by acceptversion
        '''}

    golden_parsed_output_2 = {
        'rollback_timer_reason': 'timer canceled by acceptversion',
        'rollback_timer_state': 'inactive'}

    # IOS 
    golden_output_3 = {'execute.return_value': '''
        #show issu rollback-timer
            Rollback Process State = Not in progress
          Configured Rollback Time = 00:45:00
    '''}

    golden_parsed_output_3 = {
        'rollback_timer_state': 'Not in progress', 
        'rollback_timer_time': '00:45:00'
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

    def test_golden_2(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_2)
        obj = ShowIssuRollbackTimer(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_2)

    def test_golden_3(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_3)
        obj = ShowIssuRollbackTimer(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_3)

if __name__ == '__main__':
    unittest.main()
