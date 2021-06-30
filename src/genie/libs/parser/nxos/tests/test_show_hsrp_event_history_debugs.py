
# Python
import re
import unittest
from unittest.mock import Mock

# ATS
from pyats.topology import Device

# Parser
from genie.libs.parser.nxos.show_hsrp_event_history_debugs import ShowHsrpEventHistoryDebugs

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError, SchemaMissingKeyError


# ========================================================
# Unit test for 'show hsrp internal event-history debugs'       
# ========================================================
class test_show_hsrp_event_history_debugs(unittest.TestCase):
    
    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}
    
    golden_parsed_output = {
        "debug_logs": {
            "1": {
                "date": "2021 May 18",
                "time": "20:19:01.952265",
                "proc_name": "hsrp_engine",
                "pid": "24530",
                "debug_msg": "Time Taken For Show Run: Time=0.000556"
            },
            "2": {
                "date": "2021 May 18",
                "time": "20:19:01.952260",
                "proc_name": "hsrp_engine",
                "pid": "24530",
                "debug_msg": "fu_acfg_gen done"
            },
            "3": {
                "date": "2021 May 18",
                "time": "20:19:01.951701",
                "proc_name": "hsrp_engine",
                "pid": "24530",
                "debug_msg": "fu_acfg_gen called"
            },
            "4": {
                "date": "2021 May 18",
                "time": "20:19:01.921566",
                "proc_name": "hsrp_engine",
                "pid": "24530",
                "debug_msg": "Time Taken For Show Run: Time=0.000575"
            },
            "5": {
                "date": "2021 May 18",
                "time": "20:19:01.921561",
                "proc_name": "hsrp_engine",
                "pid": "24530",
                "debug_msg": "fu_acfg_gen done"
            },
            "6": {
                "date": "2021 May 18",
                "time": "20:19:01.920983",
                "proc_name": "hsrp_engine",
                "pid": "24530",
                "debug_msg": "fu_acfg_gen called"
            },
            "7": {
                "date": "2021 May 18",
                "time": "20:17:47.755495",
                "proc_name": "hsrp_engine",
                "pid": "24530",
                "debug_msg": "Time Taken For Show Run: Time=0.000772"
            },
            "8": {
                "date": "2021 May 18",
                "time": "20:17:47.755489",
                "proc_name": "hsrp_engine",
                "pid": "24530",
                "debug_msg": "fu_acfg_gen done"
            },
            "9": {
                "date": "2021 May 18",
                "time": "20:17:47.754709",
                "proc_name": "hsrp_engine",
                "pid": "24530",
                "debug_msg": "fu_acfg_gen called"
            },
            "10": {
                "date": "2021 May 18",
                "time": "20:17:47.738852",
                "proc_name": "hsrp_engine",
                "pid": "24530",
                "debug_msg": "Time Taken For Show Run: Time=0.000523"
            },
            "11": {
                "date": "2021 May 18",
                "time": "20:17:47.738847",
                "proc_name": "hsrp_engine",
                "pid": "24530",
                "debug_msg": "fu_acfg_gen done"
            },
            "12": {
                "date": "2021 May 18",
                "time": "20:17:47.738321",
                "proc_name": "hsrp_engine",
                "pid": "24530",
                "debug_msg": "fu_acfg_gen called"
            },
            "13": {
                "date": "2021 May 18",
                "time": "20:16:35.011020",
                "proc_name": "hsrp_engine",
                "pid": "24530",
                "debug_msg": "Time Taken For Show Run: Time=0.000566"
            },
            "14": {
                "date": "2021 May 18",
                "time": "20:16:35.011013",
                "proc_name": "hsrp_engine",
                "pid": "24530",
                "debug_msg": "fu_acfg_gen done"
            },
            "15": {
                "date": "2021 May 18",
                "time": "20:16:35.010446",
                "proc_name": "hsrp_engine",
                "pid": "24530",
                "debug_msg": "fu_acfg_gen called"
            },
            "16": {
                "date": "2021 May 18",
                "time": "20:16:34.979256",
                "proc_name": "hsrp_engine",
                "pid": "24530",
                "debug_msg": "Time Taken For Show Run: Time=0.001010"
            },
            "17": {
                "date": "2021 May 18",
                "time": "20:16:34.979244",
                "proc_name": "hsrp_engine",
                "pid": "24530",
                "debug_msg": "fu_acfg_gen done"
            },
            "18": {
                "date": "2021 May 18",
                "time": "20:16:34.978236",
                "proc_name": "hsrp_engine",
                "pid": "24530",
                "debug_msg": "fu_acfg_gen called"
            },
            "19": {
                "date": "2021 May 18",
                "time": "20:15:21.097689",
                "proc_name": "hsrp_engine",
                "pid": "24530",
                "debug_msg": "Time Taken For Show Run: Time=0.000600"
            },
            "20": {
                "date": "2021 May 18",
                "time": "20:15:21.097683",
                "proc_name": "hsrp_engine",
                "pid": "24530",
                "debug_msg": "fu_acfg_gen done"
            }
        }
    }

    golden_output = {'execute.return_value': '''
        [1] 2021 May 18 20:19:01.952265 [hsrp_engine] E_DEBUG    [24530]:[0]:  Time Taken For Show Run: Time=0.000556
        [2] 2021 May 18 20:19:01.952260 [hsrp_engine] E_DEBUG    [24530]:[0]:  fu_acfg_gen done
        [3] 2021 May 18 20:19:01.951701 [hsrp_engine] E_DEBUG    [24530]:[0]:  fu_acfg_gen called
        [4] 2021 May 18 20:19:01.921566 [hsrp_engine] E_DEBUG    [24530]:[0]:  Time Taken For Show Run: Time=0.000575
        [5] 2021 May 18 20:19:01.921561 [hsrp_engine] E_DEBUG    [24530]:[0]:  fu_acfg_gen done
        [6] 2021 May 18 20:19:01.920983 [hsrp_engine] E_DEBUG    [24530]:[0]:  fu_acfg_gen called
        [7] 2021 May 18 20:17:47.755495 [hsrp_engine] E_DEBUG    [24530]:[0]:  Time Taken For Show Run: Time=0.000772
        [8] 2021 May 18 20:17:47.755489 [hsrp_engine] E_DEBUG    [24530]:[0]:  fu_acfg_gen done
        [9] 2021 May 18 20:17:47.754709 [hsrp_engine] E_DEBUG    [24530]:[0]:  fu_acfg_gen called
        [10] 2021 May 18 20:17:47.738852 [hsrp_engine] E_DEBUG    [24530]:[0]:  Time Taken For Show Run: Time=0.000523
        [11] 2021 May 18 20:17:47.738847 [hsrp_engine] E_DEBUG    [24530]:[0]:  fu_acfg_gen done
        [12] 2021 May 18 20:17:47.738321 [hsrp_engine] E_DEBUG    [24530]:[0]:  fu_acfg_gen called
        [13] 2021 May 18 20:16:35.011020 [hsrp_engine] E_DEBUG    [24530]:[0]:  Time Taken For Show Run: Time=0.000566
        [14] 2021 May 18 20:16:35.011013 [hsrp_engine] E_DEBUG    [24530]:[0]:  fu_acfg_gen done
        [15] 2021 May 18 20:16:35.010446 [hsrp_engine] E_DEBUG    [24530]:[0]:  fu_acfg_gen called
        [16] 2021 May 18 20:16:34.979256 [hsrp_engine] E_DEBUG    [24530]:[0]:  Time Taken For Show Run: Time=0.001010
        [17] 2021 May 18 20:16:34.979244 [hsrp_engine] E_DEBUG    [24530]:[0]:  fu_acfg_gen done
        [18] 2021 May 18 20:16:34.978236 [hsrp_engine] E_DEBUG    [24530]:[0]:  fu_acfg_gen called
        [19] 2021 May 18 20:15:21.097689 [hsrp_engine] E_DEBUG    [24530]:[0]:  Time Taken For Show Run: Time=0.000600
        [20] 2021 May 18 20:15:21.097683 [hsrp_engine] E_DEBUG    [24530]:[0]:  fu_acfg_gen done
        '''}

    def test_show_hsrp_event_history_debugs(self):
        self.device = Mock(**self.golden_output)
        obj = ShowHsrpEventHistoryDebugs(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output)

if __name__ == '__main__':
    unittest.main()

