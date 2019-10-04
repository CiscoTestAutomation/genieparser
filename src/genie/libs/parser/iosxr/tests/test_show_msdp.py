# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# iosxr show msdp
from genie.libs.parser.iosxr.show_msdp import ShowMsdpPeer


class test_show_msdp_peer(unittest.TestCase):
    """
        Commands:
        show ip msdp peer
        show ip msdp vrf <vrf> peer
    """
    device = Device(name='aDevice')

    empty_output = {'execute.return_value': ''}

    expected_output_1 = {
        'vrf': {
            'default': {
                'peer': {
                    '202.202.33.3': {
                        'connect_source_address': '202.202.11.1',
                        'elapsed_time': '00:00:09',
                        'nsr': {
                            'oper_downs': 0,
                            'state': 'StopRead',
                            'up_down_time': '1d02h'},
                        'password': 'None',
                        'peer_as': 4134,
                        'reset': '999',
                        'sa_filter': {
                            'in': {
                                '(S,G)': {
                                    'filter': 'none'},
                                'RP': {
                                    'filter': 'none'}},
                            'out': {
                                '(S,G)': {
                                    'filter': 'none'},
                                'RP': {
                                    'filter': 'none'}}},
                        'sa_request': {
                            'input_filter': 'none',
                            'sa_request_to_peer': 'disabled'},
                        'session_state': 'Inactive',
                        'statistics': {
                            'conn_count_cleared': '00:01:25',
                            'output_message_discarded': 0,
                            'queue': {
                                'size_input': 0,
                                'size_output': 0},
                            'received': {
                                'sa_message': 0,
                                'tlv_message': 0},
                            'sent': {
                                'tlv_message': 3}},
                        'timer': {
                            'keepalive_interval': 30,
                            'peer_timeout_interval': 75},
                        'ttl_threshold': 2}}}}}

    device_output_1 = {
        'execute.return_value': '''MSDP Peer 202.202.33.3 (?), AS 4134
        Description:
          Connection status:
            State: Inactive, Resets: 999, Connection Source: 202.202.11.1
            Uptime(Downtime): 00:00:09, SA messages received: 0
            TLV messages sent/received: 3/0
          Output messages discarded: 0
            Connection and counters cleared 00:01:25 ago
          SA Filtering:
            Input (S,G) filter: none
            Input RP filter: none
            Output (S,G) filter: none
            Output RP filter: none
          SA-Requests:
            Input filter: none
            Sending SA-Requests to peer: disabled
          Password: None
          Peer ttl threshold: 2
          Input queue size: 0, Output queue size: 0
          KeepAlive timer period: 30
          Peer Timeout timer period: 75
          NSR:
            State: StopRead, Oper-Downs: 0
            NSR-Uptime(NSR-Downtime): 1d02h
    '''}

    expected_output_2 = {
        'vrf': {
            'default': {
                'peer': {
                    '1.1.1.1': {
                        'connect_source_address': '22.22.22.23',
                        'description': 'R1',
                        'elapsed_time': '18:19:47',
                        'nsr': {
                            'oper_downs': 0,
                            'state': 'Unknown',
                            'up_down_time': '22:46:31'},
                        'password': 'None',
                        'peer_as': 0,
                        'reset': '0',
                        'sa_filter': {
                            'in': {
                                '(S,G)': {
                                    'filter': 'safilin'},
                                'RP': {
                                    'filter': 'none'}},
                            'out': {
                                '(S,G)': {
                                    'filter': 'safilout'},
                                'RP': {
                                    'filter': 'none'}}},
                        'sa_request': {
                            'input_filter': 'none',
                            'sa_request_to_peer': 'disabled'},
                        'session_state': 'Listen',
                        'statistics': {
                            'conn_count_cleared': '22:46:31',
                            'output_message_discarded': 0,
                            'queue': {
                                'size_input': 0,
                                'size_output': 0},
                            'received': {
                                'sa_message': 0,
                                'tlv_message': 0},
                            'sent': {
                                'tlv_message': 0}},
                        'timer': {
                            'keepalive_interval': 30,
                            'peer_timeout_interval': 75},
                        'ttl_threshold': 222}}}}}

    device_output_2 = {'execute.return_value': '''
        MSDP Peer 1.1.1.1 (?), AS 0
        Description: R1
          Connection status:
            State: Listen, Resets: 0, Connection Source: 22.22.22.23
            Uptime(Downtime): 18:19:47, SA messages received: 0
            TLV messages sent/received: 0/0
          Output messages discarded: 0
            Connection and counters cleared 22:46:31 ago
          SA Filtering:
            Input (S,G) filter: safilin
            Input RP filter: none
            Output (S,G) filter: safilout
            Output RP filter: none
          SA-Requests:
            Input filter: none
            Sending SA-Requests to peer: disabled
          Password: None 
          Peer ttl threshold: 222
          Input queue size: 0, Output queue size: 0
          KeepAlive timer period: 30
          Peer Timeout timer period: 75
          NSR:
            State: Unknown, Oper-Downs: 0
            NSR-Uptime(NSR-Downtime): 22:46:31
    '''}

    def test_show_msdp_peer_empty(self):
        self.maxDiff = None
        self.device = Mock(**self.empty_output)
        obj = ShowMsdpPeer(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_show_msdp_peer_1(self):
        self.maxDiff = None
        self.device = Mock(**self.device_output_1)
        obj = ShowMsdpPeer(device=self.device)
        parsed_output = obj.parse()

        self.assertEqual(parsed_output, self.expected_output_1)

    def test_show_msdp_peer_2(self):
        self.maxDiff = None
        self.device = Mock(**self.device_output_2)
        obj = ShowMsdpPeer(device=self.device)
        parsed_output = obj.parse()

        self.assertEqual(parsed_output, self.expected_output_2)


if __name__ == '__main__':
    unittest.main()
