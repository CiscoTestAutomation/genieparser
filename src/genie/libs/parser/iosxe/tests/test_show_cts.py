import unittest
from unittest.mock import Mock

from genie.metaparser.util.exceptions import SchemaEmptyParserError
from genie.libs.parser.iosxe.show_cts import ShowCtsPacs, ShowCtsRoleBasedCounters


# =============================
# Unit test for 'show cts pacs'
# =============================
class TestShowCtsPacs(unittest.TestCase):
    """Unit test for 'show cts pacs'"""

    maxDiff = None
    empty_output = {'execute.return_value': ''}
    golden_parsed_output1 = {
        "aid": "1100E046659D4275B644BF946EFA49CD",
        "pac_info": {
            "aid": "1100E046659D4275B644BF946EFA49CD",
            "pac_type": "Cisco Trustsec",
            "i_id": "gw1",
            "a_id_info": "Identity Services Engine",
        "credential_lifetime": "Sun, Sep/06/2020"
        },
        "pac_opaque": "000200B80003000100040010207FCE2A590A44BA0DE959740A348AF00006009C00030100F57E4D71BDE3BD2850B2B63C92E18122000000135EDA996F00093A805A004010F4EDAF81FB6900D03013E907ED81BFB83EE273B8E563BE48DC16B2E9164B1AA6711281937B734E8C449280FCEAF4BE668545B5A55BE20C6346C42AFFCA87FFDDA0AC6A480F9AEE147541EE51FB67CDE0580FD8A746978C78C2CB9E7855BB1667469896AB18902424344AC094B3162EF09488CDB0D6A95139",
        "refresh_timer": "6w3d"
    }

    golden_output1 = {'execute.return_value': '''
AID: 1100E046659D4275B644BF946EFA49CD
PAC-Info:
  PAC-type = Cisco Trustsec
  AID: 1100E046659D4275B644BF946EFA49CD
  I-ID: gw1
  A-ID-Info: Identity Services Engine
  Credential Lifetime: 19:56:32 PDT Sun Sep 06 2020
PAC-Opaque: 000200B80003000100040010207FCE2A590A44BA0DE959740A348AF00006009C00030100F57E4D71BDE3BD2850B2B63C92E18122000000135EDA996F00093A805A004010F4EDAF81FB6900D03013E907ED81BFB83EE273B8E563BE48DC16B2E9164B1AA6711281937B734E8C449280FCEAF4BE668545B5A55BE20C6346C42AFFCA87FFDDA0AC6A480F9AEE147541EE51FB67CDE0580FD8A746978C78C2CB9E7855BB1667469896AB18902424344AC094B3162EF09488CDB0D6A95139
Refresh timer is set for 6w3d

    '''}

    def test_show_cts_pacs_full(self):
        self.device = Mock(**self.golden_output1)
        obj = ShowCtsPacs(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output1)

    def test_show_cts_pacs_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowCtsPacs(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()


if __name__ == '__main__':
    unittest.main()
# ============================================
# Unit test for 'show cts role-based counters'
# ============================================
class TestShowCtsRoleBasedCounters(unittest.TestCase):
    """Unit test for 'show cts role-based counters'"""

    maxDiff = None
    empty_output = {'execute.return_value': ''}
    golden_parsed_output1 = {
        "cts_rb_count": {
            1: {
                "src_group": "*",
                "dst_group": "*",
                "sw_denied_count": 0,
                "hw_denied_count": 0,
                "sw_permit_count": 2,
                "hw_permit_count": 30802626587,
                "sw_monitor_count": 0,
                "hw_monitor_count": 0
            },
            2: {
                "src_group": 2,
                "dst_group": 0,
                "sw_denied_count": 0,
                "hw_denied_count": 4794060,
                "sw_permit_count": 0,
                "hw_permit_count": 0,
                "sw_monitor_count": 0,
                "hw_monitor_count": 0
            },
            3: {
                "src_group": 7,
                "dst_group": 0,
                "sw_denied_count": 0,
                "hw_denied_count": 0,
                "sw_permit_count": 0,
                "hw_permit_count": 0,
                "sw_monitor_count": 0,
                "hw_monitor_count": 0
            },
            4: {
                "src_group": 99,
                "dst_group": 0,
                "sw_denied_count": 0,
                "hw_denied_count": 0,
                "sw_permit_count": 0,
                "hw_permit_count": 0,
                "sw_monitor_count": 0,
                "hw_monitor_count": 0
            },
            5: {
                "src_group": 100,
                "dst_group": 0,
                "sw_denied_count": 0,
                "hw_denied_count": 0,
                "sw_permit_count": 0,
                "hw_permit_count": 0,
                "sw_monitor_count": 0,
                "hw_monitor_count": 0
            },
            6: {
                "src_group": 103,
                "dst_group": 0,
                "sw_denied_count": 0,
                "hw_denied_count": 0,
                "sw_permit_count": 0,
                "hw_permit_count": 0,
                "sw_monitor_count": 0,
                "hw_monitor_count": 0
            },
            7: {
                "src_group": 104,
                "dst_group": 0,
                "sw_denied_count": 0,
                "hw_denied_count": 0,
                "sw_permit_count": 0,
                "hw_permit_count": 0,
                "sw_monitor_count": 0,
                "hw_monitor_count": 0
            },
            8: {
                "src_group": 2,
                "dst_group": 2,
                "sw_denied_count": 0,
                "hw_denied_count": 4,
                "sw_permit_count": 0,
                "hw_permit_count": 0,
                "sw_monitor_count": 0,
                "hw_monitor_count": 0
            },
            9: {
                "src_group": 7,
                "dst_group": 2,
                "sw_denied_count": 0,
                "hw_denied_count": 0,
                "sw_permit_count": 0,
                "hw_permit_count": 0,
                "sw_monitor_count": 0,
                "hw_monitor_count": 0
            },
            10: {
                "src_group": 99,
                "dst_group": 2,
                "sw_denied_count": 0,
                "hw_denied_count": 0,
                "sw_permit_count": 0,
                "hw_permit_count": 0,
                "sw_monitor_count": 0,
                "hw_monitor_count": 0
            },
            11: {
                "src_group": 100,
                "dst_group": 2,
                "sw_denied_count": 0,
                "hw_denied_count": 0,
                "sw_permit_count": 0,
                "hw_permit_count": 0,
                "sw_monitor_count": 0,
                "hw_monitor_count": 0
            },
            12: {
                "src_group": 103,
                "dst_group": 2,
                "sw_denied_count": 0,
                "hw_denied_count": 0,
                "sw_permit_count": 0,
                "hw_permit_count": 0,
                "sw_monitor_count": 0,
                "hw_monitor_count": 0
            },
            13: {
                "src_group": 104,
                "dst_group": 2,
                "sw_denied_count": 0,
                "hw_denied_count": 0,
                "sw_permit_count": 0,
                "hw_permit_count": 0,
                "sw_monitor_count": 0,
                "hw_monitor_count": 0
            },
            14: {
                "src_group": 2,
                "dst_group": 3,
                "sw_denied_count": 0,
                "hw_denied_count": 0,
                "sw_permit_count": 0,
                "hw_permit_count": 0,
                "sw_monitor_count": 0,
                "hw_monitor_count": 0
            },
            15: {
                "src_group": 7,
                "dst_group": 3,
                "sw_denied_count": 0,
                "hw_denied_count": 0,
                "sw_permit_count": 0,
                "hw_permit_count": 0,
                "sw_monitor_count": 0,
                "hw_monitor_count": 0
            },
            16: {
                "src_group": 99,
                "dst_group": 3,
                "sw_denied_count": 0,
                "hw_denied_count": 0,
                "sw_permit_count": 0,
                "hw_permit_count": 0,
                "sw_monitor_count": 0,
                "hw_monitor_count": 0
            },
            17: {
                "src_group": 100,
                "dst_group": 3,
                "sw_denied_count": 0,
                "hw_denied_count": 0,
                "sw_permit_count": 0,
                "hw_permit_count": 0,
                "sw_monitor_count": 0,
                "hw_monitor_count": 0
            },
            18: {
                "src_group": 103,
                "dst_group": 3,
                "sw_denied_count": 0,
                "hw_denied_count": 0,
                "sw_permit_count": 0,
                "hw_permit_count": 0,
                "sw_monitor_count": 0,
                "hw_monitor_count": 0
            },
            19: {
                "src_group": 104,
                "dst_group": 3,
                "sw_denied_count": 0,
                "hw_denied_count": 0,
                "sw_permit_count": 0,
                "hw_permit_count": 0,
                "sw_monitor_count": 0,
                "hw_monitor_count": 0
            },
            20: {
                "src_group": 2,
                "dst_group": 5,
                "sw_denied_count": 0,
                "hw_denied_count": 0,
                "sw_permit_count": 0,
                "hw_permit_count": 0,
                "sw_monitor_count": 0,
                "hw_monitor_count": 0
            },
            21: {
                "src_group": 7,
                "dst_group": 5,
                "sw_denied_count": 0,
                "hw_denied_count": 0,
                "sw_permit_count": 0,
                "hw_permit_count": 0,
                "sw_monitor_count": 0,
                "hw_monitor_count": 0
            },
            22: {
                "src_group": 99,
                "dst_group": 5,
                "sw_denied_count": 0,
                "hw_denied_count": 0,
                "sw_permit_count": 0,
                "hw_permit_count": 0,
                "sw_monitor_count": 0,
                "hw_monitor_count": 0
            },
            23: {
                "src_group": 100,
                "dst_group": 5,
                "sw_denied_count": 0,
                "hw_denied_count": 0,
                "sw_permit_count": 0,
                "hw_permit_count": 0,
                "sw_monitor_count": 0,
                "hw_monitor_count": 0
            },
            24: {
                "src_group": 104,
                "dst_group": 5,
                "sw_denied_count": 0,
                "hw_denied_count": 0,
                "sw_permit_count": 0,
                "hw_permit_count": 0,
                "sw_monitor_count": 0,
                "hw_monitor_count": 0
            },
            25: {
                "src_group": 2,
                "dst_group": 6,
                "sw_denied_count": 0,
                "hw_denied_count": 0,
                "sw_permit_count": 0,
                "hw_permit_count": 0,
                "sw_monitor_count": 0,
                "hw_monitor_count": 0
            },
            26: {
                "src_group": 7,
                "dst_group": 6,
                "sw_denied_count": 0,
                "hw_denied_count": 0,
                "sw_permit_count": 0,
                "hw_permit_count": 0,
                "sw_monitor_count": 0,
                "hw_monitor_count": 0
            },
            27: {
                "src_group": 99,
                "dst_group": 6,
                "sw_denied_count": 0,
                "hw_denied_count": 0,
                "sw_permit_count": 0,
                "hw_permit_count": 0,
                "sw_monitor_count": 0,
                "hw_monitor_count": 0
            },
            28: {
                "src_group": 100,
                "dst_group": 6,
                "sw_denied_count": 0,
                "hw_denied_count": 0,
                "sw_permit_count": 0,
                "hw_permit_count": 0,
                "sw_monitor_count": 0,
                "hw_monitor_count": 0
            },
            29: {
                "src_group": 103,
                "dst_group": 6,
                "sw_denied_count": 0,
                "hw_denied_count": 0,
                "sw_permit_count": 0,
                "hw_permit_count": 0,
                "sw_monitor_count": 0,
                "hw_monitor_count": 0
            },
            30: {
                "src_group": 104,
                "dst_group": 6,
                "sw_denied_count": 0,
                "hw_denied_count": 0,
                "sw_permit_count": 0,
                "hw_permit_count": 0,
                "sw_monitor_count": 0,
                "hw_monitor_count": 0
            },
            31: {
                "src_group": 2,
                "dst_group": 10,
                "sw_denied_count": 0,
                "hw_denied_count": 113596,
                "sw_permit_count": 0,
                "hw_permit_count": 0,
                "sw_monitor_count": 0,
                "hw_monitor_count": 0
            },
            32: {
                "src_group": 7,
                "dst_group": 10,
                "sw_denied_count": 0,
                "hw_denied_count": 0,
                "sw_permit_count": 0,
                "hw_permit_count": 0,
                "sw_monitor_count": 0,
                "hw_monitor_count": 0
            },
            33: {
                "src_group": 2,
                "dst_group": 3003,
                "sw_denied_count": 0,
                "hw_denied_count": 490980,
                "sw_permit_count": 0,
                "hw_permit_count": 8594929,
                "sw_monitor_count": 0,
                "hw_monitor_count": 0
            },
            34: {
                "src_group": 7,
                "dst_group": 3003,
                "sw_denied_count": 0,
                "hw_denied_count": 0,
                "sw_permit_count": 0,
                "hw_permit_count": 0,
                "sw_monitor_count": 0,
                "hw_monitor_count": 0
            },
            35: {
                "src_group": 99,
                "dst_group": 3003,
                "sw_denied_count": 0,
                "hw_denied_count": 0,
                "sw_permit_count": 0,
                "hw_permit_count": 0,
                "sw_monitor_count": 0,
                "hw_monitor_count": 0
            },
            36: {
                "src_group": 100,
                "dst_group": 3003,
                "sw_denied_count": 0,
                "hw_denied_count": 0,
                "sw_permit_count": 0,
                "hw_permit_count": 0,
                "sw_monitor_count": 0,
                "hw_monitor_count": 0
            },
            37: {
                "src_group": 102,
                "dst_group": 3003,
                "sw_denied_count": 0,
                "hw_denied_count": 0,
                "sw_permit_count": 0,
                "hw_permit_count": 0,
                "sw_monitor_count": 0,
                "hw_monitor_count": 0
            },
            38: {
                "src_group": 103,
                "dst_group": 3003,
                "sw_denied_count": 0,
                "hw_denied_count": 0,
                "sw_permit_count": 0,
                "hw_permit_count": 0,
                "sw_monitor_count": 0,
                "hw_monitor_count": 0
            },
            39: {
                "src_group": 104,
                "dst_group": 3003,
                "sw_denied_count": 0,
                "hw_denied_count": 0,
                "sw_permit_count": 0,
                "hw_permit_count": 0,
                "sw_monitor_count": 0,
                "hw_monitor_count": 0
            },
            40: {
                "src_group": 2,
                "dst_group": 3004,
                "sw_denied_count": 0,
                "hw_denied_count": 1055,
                "sw_permit_count": 0,
                "hw_permit_count": 0,
                "sw_monitor_count": 0,
                "hw_monitor_count": 0
            },
            41: {
                "src_group": 7,
                "dst_group": 3004,
                "sw_denied_count": 0,
                "hw_denied_count": 0,
                "sw_permit_count": 0,
                "hw_permit_count": 0,
                "sw_monitor_count": 0,
                "hw_monitor_count": 0
            },
            42: {
                "src_group": 99,
                "dst_group": 3004,
                "sw_denied_count": 0,
                "hw_denied_count": 0,
                "sw_permit_count": 0,
                "hw_permit_count": 0,
                "sw_monitor_count": 0,
                "hw_monitor_count": 0
            },
            43: {
                "src_group": 100,
                "dst_group": 3004,
                "sw_denied_count": 0,
                "hw_denied_count": 0,
                "sw_permit_count": 0,
                "hw_permit_count": 0,
                "sw_monitor_count": 0,
                "hw_monitor_count": 0
            },
            44: {
                "src_group": 102,
                "dst_group": 3004,
                "sw_denied_count": 0,
                "hw_denied_count": 0,
                "sw_permit_count": 0,
                "hw_permit_count": 0,
                "sw_monitor_count": 0,
                "hw_monitor_count": 0
            },
            45: {
                "src_group": 103,
                "dst_group": 3004,
                "sw_denied_count": 0,
                "hw_denied_count": 0,
                "sw_permit_count": 0,
                "hw_permit_count": 0,
                "sw_monitor_count": 0,
                "hw_monitor_count": 0
            },
            46: {
                "src_group": 104,
                "dst_group": 3004,
                "sw_denied_count": 0,
                "hw_denied_count": 0,
                "sw_permit_count": 0,
                "hw_permit_count": 0,
                "sw_monitor_count": 0,
                "hw_monitor_count": 0
            },
            47: {
                "src_group": 2,
                "dst_group": 3005,
                "sw_denied_count": 0,
                "hw_denied_count": 73,
                "sw_permit_count": 0,
                "hw_permit_count": 58,
                "sw_monitor_count": 0,
                "hw_monitor_count": 0
            }
        }
    }

    golden_output1 = {'execute.return_value': '''
Role-based IPv4 counters
From    To      SW-Denied  HW-Denied  SW-Permitt HW-Permitt SW-Monitor HW-Monitor
*       *       0          0          2          30802626587 0          0         
2       0       0          4794060    0          0          0          0         
7       0       0          0          0          0          0          0         
99      0       0          0          0          0          0          0         
100     0       0          0          0          0          0          0         
103     0       0          0          0          0          0          0         
104     0       0          0          0          0          0          0         
2       2       0          4          0          0          0          0         
7       2       0          0          0          0          0          0         
99      2       0          0          0          0          0          0         
100     2       0          0          0          0          0          0         
103     2       0          0          0          0          0          0         
104     2       0          0          0          0          0          0         
2       3       0          0          0          0          0          0         
7       3       0          0          0          0          0          0         
99      3       0          0          0          0          0          0         
100     3       0          0          0          0          0          0         
103     3       0          0          0          0          0          0         
104     3       0          0          0          0          0          0         
2       5       0          0          0          0          0          0         
7       5       0          0          0          0          0          0         
99      5       0          0          0          0          0          0         
100     5       0          0          0          0          0          0         
104     5       0          0          0          0          0          0         
2       6       0          0          0          0          0          0         
7       6       0          0          0          0          0          0         
99      6       0          0          0          0          0          0         
100     6       0          0          0          0          0          0         
103     6       0          0          0          0          0          0         
104     6       0          0          0          0          0          0         
2       10      0          113596     0          0          0          0         
7       10      0          0          0          0          0          0    
2       3003    0          490980     0          8594929    0          0         
7       3003    0          0          0          0          0          0         
99      3003    0          0          0          0          0          0         
100     3003    0          0          0          0          0          0         
102     3003    0          0          0          0          0          0         
103     3003    0          0          0          0          0          0         
104     3003    0          0          0          0          0          0         
2       3004    0          1055       0          0          0          0         
7       3004    0          0          0          0          0          0         
99      3004    0          0          0          0          0          0         
100     3004    0          0          0          0          0          0         
102     3004    0          0          0          0          0          0         
103     3004    0          0          0          0          0          0         
104     3004    0          0          0          0          0          0         
2       3005    0          73         0          58         0          0 
    '''}

    def test_show_cts_role_based_counters_full(self):
        self.device = Mock(**self.golden_output1)
        obj = ShowCtsRoleBasedCounters(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output1)

    def test_show_cts_role_based_counters_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowCtsRoleBasedCounters(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()


if __name__ == '__main__':
    unittest.main()
