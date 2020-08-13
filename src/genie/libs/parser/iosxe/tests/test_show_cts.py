import unittest
from unittest.mock import Mock

from genie.metaparser.util.exceptions import SchemaEmptyParserError
from genie.libs.parser.iosxe.show_cts import Show_Cts_Sxp_Connections_Brief


# ==============================================
# Unit test for 'show_cts_sxp_connections_brief'
# ==============================================
class test_show_cts_sxp_connections_brief(unittest.TestCase):
    """Unit test for 'show_cts_sxp_connections_brief'"""

    maxDiff = None
    empty_output = {'execute.return_value': ''}
    golden_parsed_output1 = {
    "sxp_connections": {
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
            "seq_export": "Not Set",
            "seq_import": "Not Set"
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
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()


if __name__ == '__main__':
    unittest.main()
