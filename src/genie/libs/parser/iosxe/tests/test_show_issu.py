
# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device

# Genie
from genie.metaparser.util.exceptions import SchemaEmptyParserError
from genie.libs.parser.iosxe.show_issu import ShowIssuStateDetail


# =======================================
#  Unit test for 'show issu state detail'
# =======================================
class test_show_issu_state_detail(unittest.TestCase):

    device = Device(name='aDevice')

    empty_output = {'execute.return_value': ''}

    golden_output_1 = {'execute.return_value': '''
        PE1#show issu state  detail 
        --- Starting local lock acquisition on R0 ---
        Finished local lock acquisition on R0

        --- Starting installation state synchronization ---
        Finished installation state synchronization

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
        'issu_in_progress': True,
        'slot': 
            {'R1': 
                {'context': 'vty 0',
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
        'issu_in_progress': True,
        'slot': 
            {'R1': 
                {'context': 'vty 0',
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
        'issu_in_progress': True,
        'slot': 
            {'R1': 
                {'context': 'vty 0',
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
        'issu_in_progress': False}

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

if __name__ == '__main__':
    unittest.main()
