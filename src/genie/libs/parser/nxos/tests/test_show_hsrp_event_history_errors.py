
# Python
import re
import unittest
from unittest.mock import Mock

# ATS
from pyats.topology import Device

# Parser
from genie.libs.parser.nxos.show_hsrp_event_history_err import ShowHsrpEventHistoryErrors

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError, SchemaMissingKeyError


# =======================================================
# Unit test for 'show hsrp internal event-history errors'       
# =======================================================
class test_show_hsrp_event_history_errors(unittest.TestCase):
    
    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}
    
    golden_parsed_output = {
        "error_logs": {
            "1": {
                "date": "2021 May 18",
                "time": "03:14:54.489303",
                "proc_name": "hsrp_engine",
                "pid": "24530",
                "error_msg": "Engine Demux: Info='Unexpected MTS message', Opcode=409604"
            },
            "2": {
                "date": "2021 May 18",
                "time": "03:14:54.217444",
                "proc_name": "hsrp_engine",
                "pid": "24530",
                "error_msg": "(Acast) Get Bundle For IOD Failed: Reason='No bundle found for VLAN', AddrType=IPv6, VLAN=3"
            },
            "3": {
                "date": "2021 May 18",
                "time": "03:14:54.217428",
                "proc_name": "hsrp_engine",
                "pid": "24530",
                "error_msg": "(Acast) Get Bundle For IOD Failed: Reason='No bundle found for VLAN', AddrType=IPv4, VLAN=3"
            },
            "4": {
                "date": "2021 May 18",
                "time": "03:14:54.217021",
                "proc_name": "hsrp_engine",
                "pid": "24530",
                "error_msg": "Engine Demux: Info='Unexpected MTS message', Opcode=409604"
            },
            "5": {
                "date": "2021 May 18",
                "time": "03:14:46.160122",
                "proc_name": "hsrp_engine",
                "pid": "24530",
                "error_msg": "Engine Demux: Info='Unexpected MTS message', Opcode=409604"
            },
            "6": {
                "date": "2021 May 18",
                "time": "03:14:13.887116",
                "proc_name": "hsrp_engine",
                "pid": "24530",
                "error_msg": "Engine Demux: Info='Unexpected MTS message', Opcode=7972"
            },
            "7": {
                "date": "2021 May 18",
                "time": "03:14:13.886187",
                "proc_name": "hsrp_engine",
                "pid": "24530",
                "error_msg": "Engine Demux: Info='Unexpected MTS message', Opcode=409604"
            },
            "8": {
                "date": "2021 May 18",
                "time": "03:14:13.870140",
                "proc_name": "hsrp_engine",
                "pid": "24530",
                "error_msg": "(Acast) Get Bundle For IOD Failed: Reason='No bundle found for VLAN', AddrType=IPv6, VLAN=2"
            },
            "9": {
                "date": "2021 May 18",
                "time": "03:14:13.870123",
                "proc_name": "hsrp_engine",
                "pid": "24530",
                "error_msg": "(Acast) Get Bundle For IOD Failed: Reason='No bundle found for VLAN', AddrType=IPv4, VLAN=2"
            },
            "10": {
                "date": "2021 May 18",
                "time": "03:14:13.869766",
                "proc_name": "hsrp_engine",
                "pid": "24530",
                "error_msg": "Engine Demux: Info='Unexpected MTS message', Opcode=409604"
            },
            "11": {
                "date": "2021 May 18",
                "time": "03:14:06.694680",
                "proc_name": "hsrp_engine",
                "pid": "24530",
                "error_msg": "Engine Demux: Info='Unexpected MTS message', Opcode=409604"
            },
            "12": {
                "date": "2021 May 18",
                "time": "03:13:41.464033",
                "proc_name": "hsrp_engine",
                "pid": "24530",
                "error_msg": "Engine Demux: Info='Unexpected MTS message', Opcode=7972"
            },
            "13": {
                "date": "2021 May 18",
                "time": "03:13:41.462313",
                "proc_name": "hsrp_engine",
                "pid": "24530",
                "error_msg": "Engine Demux: Info='Unexpected MTS message', Opcode=409604"
            },
            "14": {
                "date": "2021 May 18",
                "time": "03:13:41.444570",
                "proc_name": "hsrp_engine",
                "pid": "24530",
                "error_msg": "(Acast) Get Bundle For IOD Failed: Reason='No bundle found for VLAN', AddrType=IPv6, VLAN=3"
            },
            "15": {
                "date": "2021 May 18",
                "time": "03:13:41.444549",
                "proc_name": "hsrp_engine",
                "pid": "24530",
                "error_msg": "(Acast) Get Bundle For IOD Failed: Reason='No bundle found for VLAN', AddrType=IPv4, VLAN=3"
            },
            "16": {
                "date": "2021 May 18",
                "time": "03:13:41.444133",
                "proc_name": "hsrp_engine",
                "pid": "24530",
                "error_msg": "Engine Demux: Info='Unexpected MTS message', Opcode=409604"
            },
            "17": {
                "date": "2021 May 18",
                "time": "03:13:28.308280",
                "proc_name": "hsrp_engine",
                "pid": "24530",
                "error_msg": "Engine Demux: Info='Unexpected MTS message', Opcode=409604"
            },
            "18": {
                "date": "2021 May 18",
                "time": "03:13:17.423021",
                "proc_name": "hsrp_engine",
                "pid": "24530",
                "error_msg": "Engine Demux: Info='Unexpected MTS message', Opcode=7972"
            },
            "19": {
                "date": "2021 May 18",
                "time": "03:13:17.422138",
                "proc_name": "hsrp_engine",
                "pid": "24530",
                "error_msg": "Engine Demux: Info='Unexpected MTS message', Opcode=409604"
            },
            "20": {
                "date": "2021 May 18",
                "time": "03:13:17.389821",
                "proc_name": "hsrp_engine",
                "pid": "24530",
                "error_msg": "(Acast) Get Bundle For IOD Failed: Reason='No bundle found for VLAN', AddrType=IPv6, VLAN=3"
            },
            "21": {
                "date": "2021 May 18",
                "time": "03:13:17.389804",
                "proc_name": "hsrp_engine",
                "pid": "24530",
                "error_msg": "(Acast) Get Bundle For IOD Failed: Reason='No bundle found for VLAN', AddrType=IPv4, VLAN=3"
            },
            "22": {
                "date": "2021 May 18",
                "time": "03:13:17.388826",
                "proc_name": "hsrp_engine",
                "pid": "24530",
                "error_msg": "Engine Demux: Info='Unexpected MTS message', Opcode=409604"
            }
        }
    }

    golden_output = {'execute.return_value': '''
        [1] 2021 May 18 03:14:54.489303 [hsrp_engine] E_DEBUG    [24530]:Engine Demux: Info='Unexpected MTS message', Opcode=409604
        [2] 2021 May 18 03:14:54.217444 [hsrp_engine] E_DEBUG    [24530]:(Acast) Get Bundle For IOD Failed: Reason='No bundle found for VLAN', AddrType=IPv6, VLAN=3
        [3] 2021 May 18 03:14:54.217428 [hsrp_engine] E_DEBUG    [24530]:(Acast) Get Bundle For IOD Failed: Reason='No bundle found for VLAN', AddrType=IPv4, VLAN=3
        [4] 2021 May 18 03:14:54.217021 [hsrp_engine] E_DEBUG    [24530]:Engine Demux: Info='Unexpected MTS message', Opcode=409604
        [5] 2021 May 18 03:14:46.160122 [hsrp_engine] E_DEBUG    [24530]:Engine Demux: Info='Unexpected MTS message', Opcode=409604
        [6] 2021 May 18 03:14:13.887116 [hsrp_engine] E_DEBUG    [24530]:Engine Demux: Info='Unexpected MTS message', Opcode=7972
        [7] 2021 May 18 03:14:13.886187 [hsrp_engine] E_DEBUG    [24530]:Engine Demux: Info='Unexpected MTS message', Opcode=409604
        [8] 2021 May 18 03:14:13.870140 [hsrp_engine] E_DEBUG    [24530]:(Acast) Get Bundle For IOD Failed: Reason='No bundle found for VLAN', AddrType=IPv6, VLAN=2
        [9] 2021 May 18 03:14:13.870123 [hsrp_engine] E_DEBUG    [24530]:(Acast) Get Bundle For IOD Failed: Reason='No bundle found for VLAN', AddrType=IPv4, VLAN=2
        [10] 2021 May 18 03:14:13.869766 [hsrp_engine] E_DEBUG    [24530]:Engine Demux: Info='Unexpected MTS message', Opcode=409604
        [11] 2021 May 18 03:14:06.694680 [hsrp_engine] E_DEBUG    [24530]:Engine Demux: Info='Unexpected MTS message', Opcode=409604
        [12] 2021 May 18 03:13:41.464033 [hsrp_engine] E_DEBUG    [24530]:Engine Demux: Info='Unexpected MTS message', Opcode=7972
        [13] 2021 May 18 03:13:41.462313 [hsrp_engine] E_DEBUG    [24530]:Engine Demux: Info='Unexpected MTS message', Opcode=409604
        [14] 2021 May 18 03:13:41.444570 [hsrp_engine] E_DEBUG    [24530]:(Acast) Get Bundle For IOD Failed: Reason='No bundle found for VLAN', AddrType=IPv6, VLAN=3
        [15] 2021 May 18 03:13:41.444549 [hsrp_engine] E_DEBUG    [24530]:(Acast) Get Bundle For IOD Failed: Reason='No bundle found for VLAN', AddrType=IPv4, VLAN=3
        [16] 2021 May 18 03:13:41.444133 [hsrp_engine] E_DEBUG    [24530]:Engine Demux: Info='Unexpected MTS message', Opcode=409604
        [17] 2021 May 18 03:13:28.308280 [hsrp_engine] E_DEBUG    [24530]:Engine Demux: Info='Unexpected MTS message', Opcode=409604
        [18] 2021 May 18 03:13:17.423021 [hsrp_engine] E_DEBUG    [24530]:Engine Demux: Info='Unexpected MTS message', Opcode=7972
        [19] 2021 May 18 03:13:17.422138 [hsrp_engine] E_DEBUG    [24530]:Engine Demux: Info='Unexpected MTS message', Opcode=409604
        [20] 2021 May 18 03:13:17.389821 [hsrp_engine] E_DEBUG    [24530]:(Acast) Get Bundle For IOD Failed: Reason='No bundle found for VLAN', AddrType=IPv6, VLAN=3
        [21] 2021 May 18 03:13:17.389804 [hsrp_engine] E_DEBUG    [24530]:(Acast) Get Bundle For IOD Failed: Reason='No bundle found for VLAN', AddrType=IPv4, VLAN=3
        [22] 2021 May 18 03:13:17.388826 [hsrp_engine] E_DEBUG    [24530]:Engine Demux: Info='Unexpected MTS message', Opcode=409604
        '''}

    def test_show_hsrp_event_history_errors(self):
        self.device = Mock(**self.golden_output)
        obj = ShowHsrpEventHistoryErrors(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output)

if __name__ == '__main__':
    unittest.main()

