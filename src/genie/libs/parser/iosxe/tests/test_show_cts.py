import unittest
from unittest.mock import Mock

from genie.metaparser.util.exceptions import SchemaEmptyParserError
from genie.libs.parser.iosxe.show_cts import ShowCtsPacs, ShowCtsEnvironmentData


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


# =========================================
# Unit test for 'show cts environment-data'
# =========================================
class TestShowCtsEnvironmentData(unittest.TestCase):
    """Unit test for 'show cts environment-data'"""

    maxDiff = None
    empty_output = {'execute.return_value': ''}
    golden_parsed_output1 = {
    "cts_env": {
            "current_state": "COMPLETE",
            "last_status": "Successful",
            "sgt_tags": "0-16",
            "tag_status": "Unknown",
            "server_list_name": "CTSServerList1-0089",
            "server_count": 4,
            "servers": {
                1: {
                    "server_ip": "10.1.100.4",
                    "port": 1812,
                    "aid": "A1A1A1A1A1A1A1A1A1A1A1A1A1A1A1A1A",
                    "server_status": "ALIVE",
                    "auto_test": "FALSE",
                    "keywrap_enable": "FALSE",
                    "idle_time_mins": 60,
                    "dead_time_secs": 20
                },
                2: {
                    "server_ip": "10.1.100.5",
                    "port": 1812,
                    "aid": "A1A1A1A1A1A1A1A1A1A1A1A1A1A1A1A1A",
                    "server_status": "ALIVE",
                    "auto_test": "FALSE",
                    "keywrap_enable": "FALSE",
                    "idle_time_mins": 60,
                    "dead_time_secs": 20
                },
                3: {
                    "server_ip": "10.1.100.6",
                    "port": 1812,
                    "aid": "A1A1A1A1A1A1A1A1A1A1A1A1A1A1A1A1A",
                    "server_status": "ALIVE",
                    "auto_test": "FALSE",
                    "keywrap_enable": "FALSE",
                    "idle_time_mins": 60,
                    "dead_time_secs": 20
                },
                4: {
                    "server_ip": "10.1.100.6",
                    "port": 1812,
                    "aid": "A1A1A1A1A1A1A1A1A1A1A1A1A1A1A1A1A",
                    "server_status": "ALIVE",
                    "auto_test": "FALSE",
                    "keywrap_enable": "FALSE",
                    "idle_time_mins": 60,
                    "dead_time_secs": 20
                }
            },
            "security_groups": {
                1: {
                    "sec_group": "0-15",
                    "sec_group_name": "Unit0"
                },
                2: {
                    "sec_group": "2-12",
                    "sec_group_name": "Unit1"
                },
                3: {
                    "sec_group": "3-10",
                    "sec_group_name": "Unit2"
                },
                4: {
                    "sec_group": "4-11",
                    "sec_group_name": "Device11"
                },
                5: {
                    "sec_group": "3215-08",
                    "sec_group_name": "K2"
                },
                6: {
                    "sec_group": "9999-06",
                    "sec_group_name": "Q1"
                },
                7: {
                    "sec_group": "68-10",
                    "sec_group_name": "North"
                },
                8: {
                    "sec_group": "5016-00",
                    "sec_group_name": "Quarantine"
                },
                9: {
                    "sec_group": "8000-00",
                    "sec_group_name": "TEST_8000"
                }
            },
            "env_data_lifetime_secs": "86400",
            "last_update": {
                "date": "Tue, Jul/21/2020",
                "time": "20:04:42",
                "time_zone": "PDT"
            },
            "expiration": "0:00:46:51",
            "refresh": "0:00:46:51",
            "cache_data_status" : "NONE",
            "state_machine_status": "running"
        }
    }

    golden_output1 = {'execute.return_value': '''
CTS Environment Data
====================
Current state = COMPLETE
Last status = Successful
Local Device SGT:
  SGT tag = 0-16:Unknown
Server List Info:
Installed list: CTSServerList1-0089, 4 server(s):
 *Server: 10.1.100.4, port 1812, A-ID A1A1A1A1A1A1A1A1A1A1A1A1A1A1A1A1A
          Status = ALIVE
          auto-test = FALSE, keywrap-enable = FALSE, idle-time = 60 mins, deadtime = 20 secs
 *Server: 10.1.100.5, port 1812, A-ID A1A1A1A1A1A1A1A1A1A1A1A1A1A1A1A1A
          Status = ALIVE
          auto-test = FALSE, keywrap-enable = FALSE, idle-time = 60 mins, deadtime = 20 secs
 *Server: 10.1.100.6, port 1812, A-ID A1A1A1A1A1A1A1A1A1A1A1A1A1A1A1A1A
          Status = ALIVE
          auto-test = FALSE, keywrap-enable = FALSE, idle-time = 60 mins, deadtime = 20 secs
 *Server: 10.1.100.6, port 1812, A-ID A1A1A1A1A1A1A1A1A1A1A1A1A1A1A1A1A
          Status = ALIVE
          auto-test = FALSE, keywrap-enable = FALSE, idle-time = 60 mins, deadtime = 20 secs
Security Group Name Table:
    0-15:Unit0
    2-12:Unit1
    3-10:Unit2
    4-11:Device11
    3215-08:K2
    9999-06:Q1
    68-10:North
    5016-00:Quarantine
    8000-00:TEST_8000
Environment Data Lifetime = 86400 secs 
Last update time = 20:04:42 PDT Tue Jul 21 2020
Env-data expires in   0:00:46:51 (dd:hr:mm:sec)
Env-data refreshes in 0:00:46:51 (dd:hr:mm:sec)
Cache data applied           = NONE
State Machine is running
        
    '''}

    def test_show_cts_environment_data_full(self):
        self.device = Mock(**self.golden_output1)
        obj = ShowCtsEnvironmentData(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output1)

    def test_show_cts_environment_data_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowCtsEnvironmentData(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()


if __name__ == '__main__':
    unittest.main()
