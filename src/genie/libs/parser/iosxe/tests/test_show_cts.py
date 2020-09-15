import unittest
from unittest.mock import Mock

from genie.metaparser.util.exceptions import SchemaEmptyParserError
from genie.libs.parser.iosxe.show_cts import ShowCtsPacs, ShowCtsRoleBasedCounters, Show_Cts_Sxp_Connections_Brief


# ==============================================
# Unit test for 'show_cts_sxp_connections_brief'
# ==============================================
class test_show_cts_sxp_connections_brief(unittest.TestCase):
    """Unit test for 'show_cts_sxp_connections_brief'"""

    maxDiff = None
    empty_output = {'execute.return_value': ''}
    golden_parsed_output1 = {
        "sxp_connections": {
            "total_sxp_connections": 16,
            "status": {
                "sxp_status": "Enabled",
                "highest_version": 4,
                "default_pw": "Set",
                "key_chain": "Not Set",
                "key_chain_name": "Not Applicable",
                "source_ip": "192.168.2.24",
                "conn_retry": 120,
                "reconcile_secs": 120,
                "retry_timer": "not running",
                "peer_sequence_traverse_limit_for_export": "Not Set",
                "peer_sequence_traverse_limit_for_import": "Not Set"
            },
            "sxp_peers": {
                "10.100.123.1": {
                    "source_ip": "192.168.2.24",
                    "conn_status": "On",
                    "duration": "44:19:54:52"
                },
                "10.100.123.2": {
                    "source_ip": "192.168.2.24",
                    "conn_status": "On",
                    "duration": "44:19:54:52"
                },
                "10.100.123.3": {
                    "source_ip": "192.168.2.24",
                    "conn_status": "On",
                    "duration": "44:19:54:52"
                },
                "10.100.123.4": {
                    "source_ip": "192.168.2.24",
                    "conn_status": "On",
                    "duration": "44:19:54:52"
                },
                "10.100.123.5": {
                    "source_ip": "192.168.2.24",
                    "conn_status": "On",
                    "duration": "44:18:58:47"
                },
                "10.100.123.6": {
                    "source_ip": "192.168.2.24",
                    "conn_status": "On",
                    "duration": "20:12:53:40"
                },
                "10.100.123.7": {
                    "source_ip": "192.168.2.24",
                    "conn_status": "On",
                    "duration": "44:18:58:47"
                },
                "10.100.123.8": {
                    "source_ip": "192.168.2.24",
                    "conn_status": "On",
                    "duration": "20:12:40:41"
                },
                "10.100.123.9": {
                    "source_ip": "192.168.2.24",
                    "conn_status": "On",
                    "duration": "44:18:58:47"
                },
                "10.100.123.10": {
                    "source_ip": "192.168.2.24",
                    "conn_status": "On",
                    "duration": "44:18:58:47"
                },
                "10.100.123.11": {
                    "source_ip": "192.168.2.24",
                    "conn_status": "On",
                    "duration": "44:22:21:10"
                },
                "10.100.123.12": {
                    "source_ip": "192.168.2.24",
                    "conn_status": "On",
                    "duration": "44:18:58:47"
                },
                "10.100.123.13": {
                    "source_ip": "192.168.2.24",
                    "conn_status": "On",
                    "duration": "45:08:24:37"
                },
                "10.100.123.14": {
                    "source_ip": "192.168.2.24",
                    "conn_status": "On",
                    "duration": "45:08:24:37"
                },
                "10.100.123.15": {
                    "source_ip": "192.168.2.24",
                    "conn_status": "On",
                    "duration": "36:11:31:08"
                },
                "10.100.123.16": {
                    "source_ip": "192.168.2.24",
                    "conn_status": "On",
                    "duration": "36:12:13:50"
                }
            }
        }
    }

    golden_output1 = {'execute.return_value': '''
       There are no SXP Connections.
 SXP              : Enabled
 Highest Version Supported: 4
 Default Password : Set
 Default Key-Chain: Not Set
 Default Key-Chain Name: Not Applicable
 Default Source IP: 192.168.2.24
Connection retry open period: 120 secs
Reconcile period: 120 secs
Retry open timer is not running
Peer-Sequence traverse limit for export: Not Set
Peer-Sequence traverse limit for import: Not Set

----------------------------------------------------------------------------------------------------------------------------------
Peer_IP          Source_IP        Conn Status                                          Duration
----------------------------------------------------------------------------------------------------------------------------------
10.100.123.1    192.168.2.24   On                                                   44:19:54:52 (dd:hr:mm:sec)
10.100.123.2    192.168.2.24   On                                                   44:19:54:52 (dd:hr:mm:sec)
10.100.123.3    192.168.2.24   On                                                   44:19:54:52 (dd:hr:mm:sec)
10.100.123.4    192.168.2.24   On                                                   44:19:54:52 (dd:hr:mm:sec)
10.100.123.5    192.168.2.24   On                                                   44:18:58:47 (dd:hr:mm:sec)
10.100.123.6    192.168.2.24   On                                                   20:12:53:40 (dd:hr:mm:sec)
10.100.123.7    192.168.2.24   On                                                   44:18:58:47 (dd:hr:mm:sec)
10.100.123.8    192.168.2.24   On                                                   20:12:40:41 (dd:hr:mm:sec)
10.100.123.9    192.168.2.24   On                                                   44:18:58:47 (dd:hr:mm:sec)
10.100.123.10   192.168.2.24   On                                                   44:18:58:47 (dd:hr:mm:sec)
10.100.123.11   192.168.2.24   On                                                   44:22:21:10 (dd:hr:mm:sec)
10.100.123.12   192.168.2.24   On                                                   44:18:58:47 (dd:hr:mm:sec)
10.100.123.13   192.168.2.24   On                                                   45:08:24:37 (dd:hr:mm:sec)
10.100.123.14   192.168.2.24   On                                                   45:08:24:37 (dd:hr:mm:sec)
10.100.123.15   192.168.2.24   On                                                   36:11:31:08 (dd:hr:mm:sec)
10.100.123.16   192.168.2.24   On                                                   36:12:13:50 (dd:hr:mm:sec)

Total num of SXP Connections = 16 
    '''}

    def test_show_cts_sxp_connections_brief_full(self):
        self.device = Mock(**self.golden_output1)
        obj = Show_Cts_Sxp_Connections_Brief(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output1)

    def test_show_cts_sxp_connections_brief_empty(self):
        self.device = Mock(**self.empty_output)
        obj = Show_Cts_Sxp_Connections_Brief(device=self.device)

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
                "src_group": "2",
                "dst_group": "0",
                "sw_denied_count": 0,
                "hw_denied_count": 4794060,
                "sw_permit_count": 0,
                "hw_permit_count": 0,
                "sw_monitor_count": 0,
                "hw_monitor_count": 0
            },
            3: {
                "src_group": "7",
                "dst_group": "0",
                "sw_denied_count": 0,
                "hw_denied_count": 0,
                "sw_permit_count": 0,
                "hw_permit_count": 0,
                "sw_monitor_count": 0,
                "hw_monitor_count": 0
            },
            4: {
                "src_group": "99",
                "dst_group": "0",
                "sw_denied_count": 0,
                "hw_denied_count": 0,
                "sw_permit_count": 0,
                "hw_permit_count": 0,
                "sw_monitor_count": 0,
                "hw_monitor_count": 0
            },
            5: {
                "src_group": "100",
                "dst_group": "0",
                "sw_denied_count": 0,
                "hw_denied_count": 0,
                "sw_permit_count": 0,
                "hw_permit_count": 0,
                "sw_monitor_count": 0,
                "hw_monitor_count": 0
            },
            6: {
                "src_group": "103",
                "dst_group": "0",
                "sw_denied_count": 0,
                "hw_denied_count": 0,
                "sw_permit_count": 0,
                "hw_permit_count": 0,
                "sw_monitor_count": 0,
                "hw_monitor_count": 0
            },
            7: {
                "src_group": "104",
                "dst_group": "0",
                "sw_denied_count": 0,
                "hw_denied_count": 0,
                "sw_permit_count": 0,
                "hw_permit_count": 0,
                "sw_monitor_count": 0,
                "hw_monitor_count": 0
            },
            8: {
                "src_group": "2",
                "dst_group": "2",
                "sw_denied_count": 0,
                "hw_denied_count": 4,
                "sw_permit_count": 0,
                "hw_permit_count": 0,
                "sw_monitor_count": 0,
                "hw_monitor_count": 0
            },
            9: {
                "src_group": "7",
                "dst_group": "2",
                "sw_denied_count": 0,
                "hw_denied_count": 0,
                "sw_permit_count": 0,
                "hw_permit_count": 0,
                "sw_monitor_count": 0,
                "hw_monitor_count": 0
            },
            10: {
                "src_group": "99",
                "dst_group": "2",
                "sw_denied_count": 0,
                "hw_denied_count": 0,
                "sw_permit_count": 0,
                "hw_permit_count": 0,
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
