# Python
import unittest
from unittest.mock import Mock

# ATS
from pyats.topology import Device

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# iosxr show msdp
from genie.libs.parser.iosxr.show_msdp import ShowMsdpPeer, ShowMsdpContext, ShowMsdpSummary, ShowMsdpSaCache, ShowMsdpStatisticsPeer


class TestShowMsdpPeer(unittest.TestCase):
    """
        Commands:
        show msdp peer
        show msdp peer <peer>
        show msdp vrf <vrf> peer
        show msdp vrf <vrf> peer <peer>
    """
    device = Device(name='aDevice')

    empty_output = {'execute.return_value': ''}

    expected_output_1 = {
        'vrf': {
            'default': {
                'peer': {
                    '192.168.229.3': {
                        'connect_source_address': '192.168.100.1',
                        'elapsed_time': '00:00:09',
                        'nsr': {
                            'oper_downs': 0,
                            'state': 'StopRead',
                            'up_down_time': '1d02h'},
                        'password': 'None',
                        'peer_as': 65109,
                        'peer_name': '?',
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
        'execute.return_value': '''
        Router# show msdp peer

        MSDP Peer 192.168.229.3 (?), AS 65109
        Description:
            Connection status:
            State: Inactive, Resets: 999, Connection Source: 192.168.100.1
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
            'VRF1': {
                'peer': {
                    '10.4.1.1': {
                        'connect_source_address': '10.151.22.23',
                        'description': 'R1',
                        'elapsed_time': '18:19:47',
                        'nsr': {
                            'oper_downs': 0,
                            'state': 'Unknown',
                            'up_down_time': '22:46:31'},
                        'password': 'None',
                        'peer_as': 0,
                        'peer_name': '?',
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
        Router# show msdp vrf VRF1 peer

        MSDP Peer 10.4.1.1 (?), AS 0
        Description: R1
            Connection status:
            State: Listen, Resets: 0, Connection Source: 10.151.22.23
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

    device_output_3 = {'execute.return_value': '''
    +++ Device: executing command 'show msdp peer 10.4.1.1' +++
    show msdp peer 10.4.1.1
    Wed Nov 20 16:12:35.742 UTC
    MSDP Peer 10.4.1.1 (?), AS 65000
    Description: 
      Connection status:
        State: Established, Resets: 0, Connection Source: 10.16.2.2
        Uptime(Downtime): 6d16h, SA messages received: 31005
        TLV messages sent/received: 19295/10336
      Output messages discarded: 0
        Connection and counters cleared 6d16h ago
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
        State: Unknown, Oper-Downs: 0
        NSR-Uptime(NSR-Downtime): 6d16h
    '''}

    expected_output_3 = {
    'vrf': {
        'default': {
            'peer': {
                '10.4.1.1': {
                    'connect_source_address': '10.16.2.2',
                    'elapsed_time': '6d16h',
                    'nsr': {
                        'oper_downs': 0,
                        'state': 'Unknown',
                        'up_down_time': '6d16h',
                    },
                    'password': 'None',
                    'peer_as': 65000,
                    'peer_name': '?',
                    'reset': '0',
                    'sa_filter': {
                        'in': {
                            '(S,G)': {
                                'filter': 'none',
                            },
                            'RP': {
                                'filter': 'none',
                            },
                        },
                        'out': {
                            '(S,G)': {
                                'filter': 'none',
                            },
                            'RP': {
                                'filter': 'none',
                            },
                        },
                    },
                    'sa_request': {
                        'input_filter': 'none',
                        'sa_request_to_peer': 'disabled',
                    },
                    'session_state': 'Established',
                    'statistics': {
                        'conn_count_cleared': '6d16h',
                        'output_message_discarded': 0,
                        'queue': {
                            'size_input': 0,
                            'size_output': 0,
                        },
                        'received': {
                            'sa_message': 31005,
                            'tlv_message': 10336,
                        },
                        'sent': {
                            'tlv_message': 19295,
                        },
                    },
                    'timer': {
                        'keepalive_interval': 30,
                        'peer_timeout_interval': 75,
                    },
                    'ttl_threshold': 2,
                },
            },
        },
    },
}

    device_output_4 = {'execute.return_value': '''
    +++ Device: executing command 'show msdp vrf VRF1 peer 10.4.1.1' +++
    show msdp vrf VRF1 peer 10.4.1.1
    Wed Nov 20 16:32:18.700 UTC
    MSDP Peer 10.4.1.1 (?), AS 65000
    Description: 
      Connection status:
        State: Established, Resets: 0, Connection Source: 10.16.2.2
        Uptime(Downtime): 6d17h, SA messages received: 31080
        TLV messages sent/received: 19335/10361
      Output messages discarded: 0
        Connection and counters cleared 6d17h ago
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
        State: Unknown, Oper-Downs: 0
        NSR-Uptime(NSR-Downtime): 6d17h
    '''}

    expected_output_4 = {
    'vrf': {
        'VRF1': {
            'peer': {
                '10.4.1.1': {
                    'connect_source_address': '10.16.2.2',
                    'elapsed_time': '6d17h',
                    'nsr': {
                        'oper_downs': 0,
                        'state': 'Unknown',
                        'up_down_time': '6d17h',
                    },
                    'password': 'None',
                    'peer_as': 65000,
                    'peer_name': '?',
                    'reset': '0',
                    'sa_filter': {
                        'in': {
                            '(S,G)': {
                                'filter': 'none',
                            },
                            'RP': {
                                'filter': 'none',
                            },
                        },
                        'out': {
                            '(S,G)': {
                                'filter': 'none',
                            },
                            'RP': {
                                'filter': 'none',
                            },
                        },
                    },
                    'sa_request': {
                        'input_filter': 'none',
                        'sa_request_to_peer': 'disabled',
                    },
                    'session_state': 'Established',
                    'statistics': {
                        'conn_count_cleared': '6d17h',
                        'output_message_discarded': 0,
                        'queue': {
                            'size_input': 0,
                            'size_output': 0,
                        },
                        'received': {
                            'sa_message': 31080,
                            'tlv_message': 10361,
                        },
                        'sent': {
                            'tlv_message': 19335,
                        },
                    },
                    'timer': {
                        'keepalive_interval': 30,
                        'peer_timeout_interval': 75,
                    },
                    'ttl_threshold': 2,
                },
            },
        },
    },
}

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
        parsed_output = obj.parse(vrf='VRF1')
        self.assertEqual(parsed_output, self.expected_output_2)

    def test_show_msdp_peer_3(self):
        self.maxDiff = None
        self.device = Mock(**self.device_output_3)
        obj = ShowMsdpPeer(device=self.device)
        parsed_output = obj.parse(peer='10.4.1.1')
        self.assertEqual(parsed_output, self.expected_output_3)

    def test_show_msdp_peer_4(self):
        self.maxDiff = None
        self.device = Mock(**self.device_output_4)
        obj = ShowMsdpPeer(device=self.device)
        parsed_output = obj.parse(vrf='VRF1', peer='10.4.1.1')
        self.assertEqual(parsed_output, self.expected_output_4)


class TestShowMsdpContext(unittest.TestCase):
    """
        Commands:
        show msdp context
        show msdp vrf <vrf> context
    """
    device = Device(name='aDevice')

    empty_output = {'execute.return_value': ''}

    expected_output_1 = {
        'vrf': {
            'default': {
                'config': {
                    'allow_encaps_count': 0,
                    'default_peer_address': '0.0.0.0',
                    'maximum_sa': 20000,
                    'originator_address': '172.16.76.1',
                    'originator_interface': 'Loopback150',
                    'sa_holdtime': 150},
                'context_info': {
                    'table_count': {
                        'active': 2,
                        'total': 2},
                    'table_id': '0xe0000000',
                    'vrf_id': '0x60000000'},
                'inheritable_config': {
                    'keepalive_period': 30,
                    'maximum_sa': 0,
                    'peer_timeout_period': 75,
                    'ttl': 2},
                'mrib_update_counts': {
                    'g_routes': 26,
                    'sg_routes': 447,
                    'total_updates': 473,
                    'with_no_changes': 0},
                'mrib_update_drops': {
                    'auto_rp_address': 2,
                    'invalid_group': 0,
                    'invalid_group_length': 0,
                    'invalid_source': 0},
                'sa_cache': {
                    'external_sas': {
                        'current': 3,
                        'high_water_mark': 3},
                    'groups': {
                        'current': 2,
                        'high_water_mark': 2},
                    'rps': {
                        'current': 3,
                        'high_water_mark': 0},
                    'sources': {
                        'current': 12,
                        'high_water_mark': 12}}}}}

    device_output_1 = {'execute.return_value': '''
        Router# show msdp context

        MSDP context information for default
            VRF ID    : 0x60000000
            Table ID    : 0xe0000000
            Table Count (Active/Total) : 2/2
        Inheritable Configuration
            TTL    : 2
            Maximum SAs    : 0
            Keepalive Period    : 30
            Peer Timeout Period : 75
            Connect Source    :   
            SA Filter In    :   
            SA Filter Out    :   
            RP Filter In    :   
            RP Filter Out    :   
        Configuration
            Originator Address    : 172.16.76.1
            Originator Interface Name    : Loopback150
            Default Peer Address    : 0.0.0.0
            SA Holdtime    : 150
            Allow Encaps Count    : 0
            Context Maximum SAs    : 20000
        SA Cache Counts    (Current/High Water Mark)
            Groups    :    2/2   
            Sources    :    12/12   
            RPs    :    3/0   
            External SAs :    3/3   
        MRIB Update Counts
            Total updates    : 473
            With no changes    : 0
            (*,G) routes    : 26
            (S,G) routes    : 447
        MRIB Update Drops
            Invalid group    : 0
            Invalid group length : 0
            Invalid source    : 0
            Auto-RP Address    : 2
'''}

    expected_output_2 = {
        'vrf': {
            'VRF1': {
                'config': {
                    'allow_encaps_count': 0,
                    'default_peer_address': '0.0.0.0',
                    'maximum_sa': 22222,
                    'originator_address': '10.151.22.23',
                    'originator_interface': 'Loopback3',
                    'sa_holdtime': 150},
                'context_info': {
                    'table_count': {
                        'active': 1,
                        'total': 1},
                    'table_id': '0xe0000011',
                    'vrf_id': '0x60000002'},
                'inheritable_config': {
                    'connect_source': 'Loopback3',
                    'keepalive_period': 30,
                    'maximum_sa': 0,
                    'peer_timeout_period': 75,
                    'sa_filter': {
                        'in': 'safilin',
                        'out': 'safilout'},
                    'ttl': 222},
                'mrib_update_counts': {
                    'g_routes': 0,
                    'sg_routes': 0,
                    'total_updates': 0,
                    'with_no_changes': 0},
                'mrib_update_drops': {
                    'auto_rp_address': 0,
                    'invalid_group': 0,
                    'invalid_group_length': 0,
                    'invalid_source': 0},
                'sa_cache': {
                    'external_sas': {
                        'current': 0,
                        'high_water_mark': 0},
                    'groups': {
                        'current': 0,
                        'high_water_mark': 0},
                    'rps': {
                        'current': 0,
                        'high_water_mark': 0},
                    'sources': {
                        'current': 0,
                        'high_water_mark': 0}}}}}

    device_output_2 = {'execute.return_value': '''
    Router# show msdp vrf VRF1 context

    MSDP context information for VRF1
        VRF ID    : 0x60000002
        Table ID    : 0xe0000011
        Table Count (Active/Total) : 1/1
    Inheritable Configuration
        TTL    : 222
        Maximum SAs    : 0
        Keepalive Period    : 30
        Peer Timeout Period : 75
        Connect Source    : Loopback3
        SA Filter In    : safilin
        SA Filter Out    : safilout
        RP Filter In    :   
        RP Filter Out    :   
    Configuration
        Originator Address    : 10.151.22.23
        Originator Interface Name    : Loopback3
        Default Peer Address    : 0.0.0.0
        SA Holdtime    : 150
        Allow Encaps Count    : 0
        Context Maximum SAs    : 22222
    SA Cache Counts    (Current/High Water Mark)
        Groups    :    0/0   
        Sources    :    0/0   
        RPs    :    0/0   
        External SAs :    0/0   
    MRIB Update Counts
        Total updates    : 0
        With no changes    : 0
        (*,G) routes    : 0
        (S,G) routes    : 0
    MRIB Update Drops
        Invalid group    : 0
        Invalid group length : 0
        Invalid source    : 0
        Auto-RP Address    : 0
    '''}

    def test_show_msdp_context_empty(self):
        self.maxDiff = None
        self.device = Mock(**self.empty_output)
        obj = ShowMsdpContext(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_show_msdp_context_1(self):
        self.maxDiff = None
        self.device = Mock(**self.device_output_1)
        obj = ShowMsdpContext(device=self.device)
        parsed_output = obj.parse()

        self.assertEqual(parsed_output, self.expected_output_1)

    def test_show_msdp_context_2(self):
        self.maxDiff = None
        self.device = Mock(**self.device_output_2)
        obj = ShowMsdpContext(device=self.device)
        parsed_output = obj.parse(vrf='VRF1')

        self.assertEqual(parsed_output, self.expected_output_2)


class TestShowMsdpSummary(unittest.TestCase):
    """
        Commands:
        show msdp summary
        show msdp vrf <vrf> summary
    """
    device = Device(name='aDevice')

    empty_output = {'execute.return_value': ''}

    expected_output_1 = {
        'vrf': {
            'VRF1': {
                'current_external_active_sa': 0,
                'maximum_external_sa_global': 20000,
                'peer_address': {
                    '10.4.1.1': {
                        'active_sa_cnt': 0,
                        'as': 0,
                        'cfg_max_ext_sas': 0,
                        'name': 'R1',
                        'reset_count': 0,
                        'state': 'Listen',
                        'tlv': {
                            'receive': 0,
                            'sent': 0,
                        },
                        'uptime_downtime': '18:25:02',
                    },
                    '10.229.11.11': {
                        'active_sa_cnt': 0,
                        'as': 0,
                        'cfg_max_ext_sas': 0,
                        'name': '?',
                        'reset_count': 0,
                        'state': 'Listen',
                        'tlv': {
                            'receive': 0,
                            'sent': 0,
                        },
                        'uptime_downtime': '18:14:53',
                    },
                },
            },
        },
    }

    device_output_1 = {'execute.return_value': '''
    Router# show msdp vrf VRF1 summary

    Maximum External SA's Global : 20000
    Current External Active SAs : 0

    MSDP Peer Status Summary
       Peer Address    AS    State    Uptime/    Reset Peer    Active Cfg.Max    TLV
        Downtime    Count Name    SA Cnt Ext.SAs recv/sent
       10.4.1.1    0    Listen    18:25:02    0    R1    0    0    0/0
       10.229.11.11    0    Listen    18:14:53    0    ?    0    0    0/0
    '''}

    expected_output_2 = {
        'vrf': {
            'default': {
                'current_external_active_sa': 0,
                'maximum_external_sa_global': 20000,
                'peer_address': {
                    '10.64.4.4': {
                        'active_sa_cnt': 0,
                        'as': 200,
                        'cfg_max_ext_sas': 444,
                        'name': 'R4',
                        'reset_count': 0,
                        'state': 'Connect',
                        'tlv': {
                            'receive': 0,
                            'sent': 0,
                        },
                        'uptime_downtime': '20:35:48',
                    },
                },
            },
        },
    }

    device_output_2 = {'execute.return_value': '''
        Fri Jun 16 15:47:02.865 UTC
    Out of Resource Handling Enabled
    Maximum External SA's Global : 20000
    Current External Active SAs : 0

    MSDP Peer Status Summary
       Peer Address    AS    State    Uptime/    Reset Peer    Active Cfg.Max    TLV
        Downtime    Count Name    SA Cnt Ext.SAs recv/sent
       10.64.4.4    200    Connect    20:35:48    0    R4    0    444    0/0
    '''}

    def test_show_msdp_summary_empty(self):
        self.maxDiff = None
        self.device = Mock(**self.empty_output)
        obj = ShowMsdpSummary(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_show_msdp_summary_1(self):
        self.maxDiff = None
        self.device = Mock(**self.device_output_1)
        obj = ShowMsdpSummary(device=self.device)
        parsed_output = obj.parse(vrf='VRF1')
        self.assertEqual(parsed_output, self.expected_output_1)

    def test_show_msdp_summary_2(self):
        self.maxDiff = None
        self.device = Mock(**self.device_output_2)
        obj = ShowMsdpSummary(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.expected_output_2)


class TestShowMsdpSaCache(unittest.TestCase):
    """
         Commands:
         show msdp sa-cache
         show msdp sa-cache {group}
         show msdp vrf {vrf} sa-cache
         show msdp vrf {vrf} sa-cache {group}
     """
    device = Device(name='aDevice')

    empty_output = {'execute.return_value': ''}

    device_output_1 = {'execute.return_value': '''
    RP/0/0/CPU0:XR5#show msdp vrf VRF1 sa-cache

    MSDP Flags:
    E - set MRIB E flag , L - domain local source is active,
    EA - externally active source, PI - PIM is interested in the group,
    DE - SAs have been denied.    Timers age/expiration,
    Cache Entry:
    (10.1.1.10, 239.1.1.1), RP 192.168.1.1, MBGP/AS 200, 00:01:02/00:01:32
        Learned from peer 192.168.1.1, RPF peer 192.168.1.1
        SAs recvd 2, Encapsulated data received: 0
        grp flags: PI,    src flags: E, EA, PI
    '''}

    expected_output_1 = {
        'vrf': {
            'VRF1': {
                'sa_cache': {
                    '239.1.1.1 10.1.1.10': {
                        'expire': '00:01:32',
                        'group': '239.1.1.1',
                        'origin_rp': {
                            '192.168.1.1': {
                                'rp_address': '192.168.1.1',
                            },
                        },
                        'peer_as': 200,
                        'peer_learned_from': '192.168.1.1',
                        'rpf_peer': '192.168.1.1',
                        'source_addr': '10.1.1.10',
                        'flags': {
                            'grp': ['PI'],
                            'src': ['E', 'EA', 'PI'],
                        },
                        'statistics': {
                            'received': {
                                'encapsulated_data_received': 0,
                                'sa': 2,
                            },
                        },
                        'up_time': '00:01:02',
                    },
                },
            },
        },
    }

    device_output_2 = {'execute.return_value': '''
    RP/0/0/CPU0:XR5#show msdp sa-cache

    MSDP Flags:
    E - set MRIB E flag , L - domain local source is active,
    EA - externally active source, PI - PIM is interested in the group,
    DE - SAs have been denied.    Timers age/expiration,
    Cache Entry:
    (10.1.1.10, 239.1.1.1), RP 192.168.1.1, MBGP/AS 200, 00:01:02/00:01:32
        Learned from peer 192.168.1.1, RPF peer 192.168.1.1
        SAs recvd 2, Encapsulated data received: 0
        grp flags: PI,    src flags: E, EA, PI
    '''}

    expected_output_2 = {
        'vrf': {
            'default': {
                'sa_cache': {
                    '239.1.1.1 10.1.1.10': {
                        'expire': '00:01:32',
                        'group': '239.1.1.1',
                        'origin_rp': {
                            '192.168.1.1': {
                                'rp_address': '192.168.1.1',
                            },
                        },
                        'peer_as': 200,
                        'peer_learned_from': '192.168.1.1',
                        'rpf_peer': '192.168.1.1',
                        'source_addr': '10.1.1.10',
                        'flags': {
                            'grp': ['PI'],
                            'src': ['E', 'EA', 'PI'],
                        },
                        'statistics': {
                            'received': {
                                'encapsulated_data_received': 0,
                                'sa': 2,
                            },
                        },
                        'up_time': '00:01:02',
                    },
                },
            },
        },
    }

    device_output_3 = {'execute.return_value': '''
    +++ Device: executing command 'show msdp sa-cache 10.4.1.1' +++
    show msdp sa-cache 10.4.1.1
    Wed Nov 20 20:25:03.135 UTC
    
    MSDP Flags:
    E - set MRIB E flag , L - domain local source is active,
    EA - externally active source, PI - PIM is interested in the group,
    DE - SAs have been denied.  Timers age/expiration,
    Cache Entry:
    (10.4.1.1, 239.1.1.1), RP 10.4.1.1, MBGP/AS 65000, 6d21h/00:01:42
      Learned from peer 10.4.1.1, RPF peer 10.4.1.1
      SAs recvd 10605, Encapsulated data received: 0
        grp flags: none,  src flags: EA
    (10.4.1.1, 239.2.2.1), RP 10.4.1.1, MBGP/AS 65000, 6d21h/00:01:42
      Learned from peer 10.4.1.1, RPF peer 10.4.1.1
      SAs recvd 10605, Encapsulated data received: 0
        grp flags: none,  src flags: EA
    (10.4.1.1, 239.3.3.1), RP 10.4.1.1, MBGP/AS 65000, 6d21h/00:01:42
      Learned from peer 10.4.1.1, RPF peer 10.4.1.1
      SAs recvd 10605, Encapsulated data received: 0
        grp flags: none,  src flags: EA
    RP/0/RP0/CPU0:Device#
    '''}
    expected_output_3 = {
    'vrf': {
        'default': {
            'sa_cache': {
                '239.1.1.1 10.4.1.1': {
                    'expire': '00:01:42',
                    'flags': {
                        'grp': ['none'],
                        'src': ['EA'],
                    },
                    'group': '239.1.1.1',
                    'origin_rp': {
                        '10.4.1.1': {
                            'rp_address': '10.4.1.1',
                        },
                    },
                    'peer_as': 65000,
                    'peer_learned_from': '10.4.1.1',
                    'rpf_peer': '10.4.1.1',
                    'source_addr': '10.4.1.1',
                    'statistics': {
                        'received': {
                            'encapsulated_data_received': 0,
                            'sa': 10605,
                        },
                    },
                    'up_time': '6d21h',
                },
                '239.2.2.1 10.4.1.1': {
                    'expire': '00:01:42',
                    'flags': {
                        'grp': ['none'],
                        'src': ['EA'],
                    },
                    'group': '239.2.2.1',
                    'origin_rp': {
                        '10.4.1.1': {
                            'rp_address': '10.4.1.1',
                        },
                    },
                    'peer_as': 65000,
                    'peer_learned_from': '10.4.1.1',
                    'rpf_peer': '10.4.1.1',
                    'source_addr': '10.4.1.1',
                    'statistics': {
                        'received': {
                            'encapsulated_data_received': 0,
                            'sa': 10605,
                        },
                    },
                    'up_time': '6d21h',
                },
                '239.3.3.1 10.4.1.1': {
                    'expire': '00:01:42',
                    'flags': {
                        'grp': ['none'],
                        'src': ['EA'],
                    },
                    'group': '239.3.3.1',
                    'origin_rp': {
                        '10.4.1.1': {
                            'rp_address': '10.4.1.1',
                        },
                    },
                    'peer_as': 65000,
                    'peer_learned_from': '10.4.1.1',
                    'rpf_peer': '10.4.1.1',
                    'source_addr': '10.4.1.1',
                    'statistics': {
                        'received': {
                            'encapsulated_data_received': 0,
                            'sa': 10605,
                        },
                    },
                    'up_time': '6d21h',
                },
            },
        },
    },
}

    device_output_4 = {'execute.return_value': '''
    +++ Device: executing command 'show msdp vrf VRF1 sa-cache 10.4.1.1' +++
    show msdp vrf VRF1 sa-cache 10.4.1.1
    Wed Nov 20 19:16:31.452 UTC
    
    MSDP Flags:
    E - set MRIB E flag , L - domain local source is active,
    EA - externally active source, PI - PIM is interested in the group,
    DE - SAs have been denied.  Timers age/expiration,
    Cache Entry:
    (10.4.1.1, 239.1.1.1), RP 10.4.1.1, MBGP/AS 65000, 6d19h/00:02:08
      Learned from peer 10.4.1.1, RPF peer 10.4.1.1
      SAs recvd 10536, Encapsulated data received: 0
        grp flags: none,  src flags: EA
    (10.4.1.1, 239.2.2.1), RP 10.4.1.1, MBGP/AS 65000, 6d19h/00:02:08
      Learned from peer 10.4.1.1, RPF peer 10.4.1.1
      SAs recvd 10536, Encapsulated data received: 0
        grp flags: none,  src flags: EA
    (10.4.1.1, 239.3.3.1), RP 10.4.1.1, MBGP/AS 65000, 6d19h/00:02:08
      Learned from peer 10.4.1.1, RPF peer 10.4.1.1
      SAs recvd 10536, Encapsulated data received: 0
        grp flags: none,  src flags: EA'''}

    expected_output_4 = {
    'vrf': {
        'VRF1': {
            'sa_cache': {
                '239.1.1.1 10.4.1.1': {
                    'expire': '00:02:08',
                    'flags': {
                        'grp': ['none'],
                        'src': ['EA'],
                    },
                    'group': '239.1.1.1',
                    'origin_rp': {
                        '10.4.1.1': {
                            'rp_address': '10.4.1.1',
                        },
                    },
                    'peer_as': 65000,
                    'peer_learned_from': '10.4.1.1',
                    'rpf_peer': '10.4.1.1',
                    'source_addr': '10.4.1.1',
                    'statistics': {
                        'received': {
                            'encapsulated_data_received': 0,
                            'sa': 10536,
                        },
                    },
                    'up_time': '6d19h',
                },
                '239.2.2.1 10.4.1.1': {
                    'expire': '00:02:08',
                    'flags': {
                        'grp': ['none'],
                        'src': ['EA'],
                    },
                    'group': '239.2.2.1',
                    'origin_rp': {
                        '10.4.1.1': {
                            'rp_address': '10.4.1.1',
                        },
                    },
                    'peer_as': 65000,
                    'peer_learned_from': '10.4.1.1',
                    'rpf_peer': '10.4.1.1',
                    'source_addr': '10.4.1.1',
                    'statistics': {
                        'received': {
                            'encapsulated_data_received': 0,
                            'sa': 10536,
                        },
                    },
                    'up_time': '6d19h',
                },
                '239.3.3.1 10.4.1.1': {
                    'expire': '00:02:08',
                    'flags': {
                        'grp': ['none'],
                        'src': ['EA'],
                    },
                    'group': '239.3.3.1',
                    'origin_rp': {
                        '10.4.1.1': {
                            'rp_address': '10.4.1.1',
                        },
                    },
                    'peer_as': 65000,
                    'peer_learned_from': '10.4.1.1',
                    'rpf_peer': '10.4.1.1',
                    'source_addr': '10.4.1.1',
                    'statistics': {
                        'received': {
                            'encapsulated_data_received': 0,
                            'sa': 10536,
                        },
                    },
                    'up_time': '6d19h',
                },
            },
        },
    },
}

    def test_show_msdp_sacache_empty(self):
        self.maxDiff = None
        self.device = Mock(**self.empty_output)
        obj = ShowMsdpSaCache(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_show_msdp_sacache_1(self):
        self.maxDiff = None
        self.device = Mock(**self.device_output_1)
        obj = ShowMsdpSaCache(device=self.device)
        parsed_output = obj.parse(vrf='VRF1')
        self.assertEqual(parsed_output, self.expected_output_1)

    def test_show_msdp_sacache_2(self):
        self.maxDiff = None
        self.device = Mock(**self.device_output_2)
        obj = ShowMsdpSaCache(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.expected_output_2)

    def test_show_msdp_sacache_3(self):
        self.maxDiff = None
        self.device = Mock(**self.device_output_3)
        obj = ShowMsdpSaCache(device=self.device)
        parsed_output = obj.parse(group='10.4.1.1')
        self.assertEqual(parsed_output, self.expected_output_3)

    def test_show_msdp_sacache_4(self):
        self.maxDiff = None
        self.device = Mock(**self.device_output_4)
        obj = ShowMsdpSaCache(device=self.device)
        parsed_output = obj.parse(vrf='VRF1', group='10.4.1.1')
        self.assertEqual(parsed_output, self.expected_output_4)


class TestShowMsdpStatisticsPeer(unittest.TestCase):
    """
         Commands:
         show msdp statistics peer
         show msdp statistics peer <peer>
         show msdp vrf <vrf> statistics peer
         show msdp vrf <vrf> statistics peer <peer>
     """
    device = Device(name='aDevice')

    empty_output = {'execute.return_value': ''}

    device_output_1 = {'execute.return_value': '''
    RP/0/0/CPU0:Devicevr#show msdp vrf VRF1 statistics peer 
    Fri Jun 16 15:52:06.775 UTC
    MSDP Peer Statistics :- VRF1
    Peer 10.4.1.1 : AS is 0, State is Listen, 0 active SAs
        TLV Rcvd : 0 total
                   0 keepalives, 0 notifications
                   0 SAs, 0 SA Requests
                   0 SA responses, 0 unknowns
        TLV Sent : 0 total
                   0 keepalives, 0 notifications
                   0 SAs, 0 SA Requests
                   0 SA responses
        SA msgs  : 0 received, 0 sent
    Peer 10.229.11.11 : AS is 0, State is Listen, 0 active SAs
        TLV Rcvd : 0 total
                   0 keepalives, 0 notifications
                   0 SAs, 0 SA Requests
                   0 SA responses, 0 unknowns
        TLV Sent : 0 total
                   0 keepalives, 0 notifications
                   0 SAs, 0 SA Requests
                   0 SA responses
        SA msgs  : 0 received, 0 sent

    '''}

    expected_output_1 = {
        'vrf': {
            'VRF1': {
                'peer': {
                    '10.4.1.1': {
                        'active_sa': 0,
                        'as': 0,
                        'sa_msgs': {
                            'received': 0,
                            'sent': 0,
                        },
                        'state': 'Listen',
                        'tlv_rcvd': {
                            'keepalives': 0,
                            'notifications': 0,
                            'request': 0,
                            'sa': 0,
                            'sa_response': 0,
                            'total': 0,
                            'unknowns': 0,
                        },
                        'tlv_sent': {
                            'keepalives': 0,
                            'notifications': 0,
                            'request': 0,
                            'sa': 0,
                            'sa_response': 0,
                            'total': 0,
                        },
                    },
                    '10.229.11.11': {
                        'active_sa': 0,
                        'as': 0,
                        'sa_msgs': {
                            'received': 0,
                            'sent': 0,
                        },
                        'state': 'Listen',
                        'tlv_rcvd': {
                            'keepalives': 0,
                            'notifications': 0,
                            'request': 0,
                            'sa': 0,
                            'sa_response': 0,
                            'total': 0,
                            'unknowns': 0,
                        },
                        'tlv_sent': {
                            'keepalives': 0,
                            'notifications': 0,
                            'request': 0,
                            'sa': 0,
                            'sa_response': 0,
                            'total': 0,
                        },
                    },
                },
            },
        },
    }

    device_output_2 = {'execute.return_value': '''
    P/0/0/CPU0:Devicevr#show msdp statistics peer 
    Fri Jun 16 15:52:01.005 UTC
    MSDP Peer Statistics :- default
    Peer 10.64.4.4 : AS is 200, State is Connect, 0 active SAs
        TLV Rcvd : 0 total
                   0 keepalives, 0 notifications
                   0 SAs, 0 SA Requests
                   0 SA responses, 0 unknowns
        TLV Sent : 0 total
                   0 keepalives, 0 notifications
                   0 SAs, 0 SA Requests
                   0 SA responses
        SA msgs  : 0 received, 0 sent
    '''}

    expected_output_2 = {
        'vrf': {
            'default': {
                'peer': {
                    '10.64.4.4': {
                        'active_sa': 0,
                        'as': 200,
                        'sa_msgs': {
                            'received': 0,
                            'sent': 0,
                        },
                        'state': 'Connect',
                        'tlv_rcvd': {
                            'keepalives': 0,
                            'notifications': 0,
                            'request': 0,
                            'sa': 0,
                            'sa_response': 0,
                            'total': 0,
                            'unknowns': 0,
                        },
                        'tlv_sent': {
                            'keepalives': 0,
                            'notifications': 0,
                            'request': 0,
                            'sa': 0,
                            'sa_response': 0,
                            'total': 0,
                        },
                    },
                },
            },
        },
    }

    device_output_3 = {'execute.return_value': '''
    +++ Device: executing command 'show msdp statistics peer 10.4.1.1' +++
    show msdp statistics peer 10.4.1.1
    Wed Nov 20 16:36:52.240 UTC
    MSDP Peer Statistics :- default
    Peer 10.4.1.1 : AS is 65000, State is Established, 3 active SAs
        TLV Rcvd : 10362 total
                   1 keepalives, 0 notifications
                   10361 SAs, 0 SA Requests
                   0 SA responses, 0 unknowns
        TLV Sent : 19344 total
                   19344 keepalives, 0 notifications
                   0 SAs, 0 SA Requests
                   0 SA responses
        SA msgs  : 31083 received, 0 sent
    RP/0/RP0/CPU0:Device#
    '''}

    expected_output_3 = {
    'vrf': {
        'default': {
            'peer': {
                '10.4.1.1': {
                    'active_sa': 3,
                    'as': 65000,
                    'sa_msgs': {
                        'received': 31083,
                        'sent': 0,
                    },
                    'state': 'Established',
                    'tlv_rcvd': {
                        'keepalives': 1,
                        'notifications': 0,
                        'request': 0,
                        'sa': 10361,
                        'sa_response': 0,
                        'total': 10362,
                        'unknowns': 0,
                    },
                    'tlv_sent': {
                        'keepalives': 19344,
                        'notifications': 0,
                        'request': 0,
                        'sa': 0,
                        'sa_response': 0,
                        'total': 19344,
                    },
                },
            },
        },
    },
}

    device_output_4 = {'execute.return_value': '''
    +++ Device: executing command 'show msdp vrf VRF1 statistics peer 10.4.1.1' +++
    show msdp vrf VRF1 statistics peer 10.4.1.1
    Wed Nov 20 16:37:11.526 UTC
    MSDP Peer Statistics :- VRF1
    Peer 10.4.1.1 : AS is 65000, State is Established, 3 active SAs
        TLV Rcvd : 10366 total
                   1 keepalives, 0 notifications
                   10365 SAs, 0 SA Requests
                   0 SA responses, 0 unknowns
        TLV Sent : 19345 total
                   19345 keepalives, 0 notifications
                   0 SAs, 0 SA Requests
                   0 SA responses
        SA msgs  : 31095 received, 0 sent
    RP/0/RP0/CPU0:Device#
    '''}

    expected_output_4 = {
    'vrf': {
        'VRF1': {
            'peer': {
                '10.4.1.1': {
                    'active_sa': 3,
                    'as': 65000,
                    'sa_msgs': {
                        'received': 31095,
                        'sent': 0,
                    },
                    'state': 'Established',
                    'tlv_rcvd': {
                        'keepalives': 1,
                        'notifications': 0,
                        'request': 0,
                        'sa': 10365,
                        'sa_response': 0,
                        'total': 10366,
                        'unknowns': 0,
                    },
                    'tlv_sent': {
                        'keepalives': 19345,
                        'notifications': 0,
                        'request': 0,
                        'sa': 0,
                        'sa_response': 0,
                        'total': 19345,
                    },
                },
            },
        },
    },
}

    def test_show_msdp_statistics_peer_empty(self):
        self.maxDiff = None
        self.device = Mock(**self.empty_output)
        obj = ShowMsdpStatisticsPeer(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_show_msdp_statistics_peer_1(self):
        self.maxDiff = None
        self.device = Mock(**self.device_output_1)
        obj = ShowMsdpStatisticsPeer(device=self.device)
        parsed_output = obj.parse(vrf='VRF1')
        self.assertEqual(parsed_output, self.expected_output_1)

    def test_show_msdp_statistics_peer_2(self):
        self.maxDiff = None
        self.device = Mock(**self.device_output_2)
        obj = ShowMsdpStatisticsPeer(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.expected_output_2)

    def test_show_msdp_statistics_peer_3(self):
        self.maxDiff = None
        self.device = Mock(**self.device_output_3)
        obj = ShowMsdpStatisticsPeer(device=self.device)
        parsed_output = obj.parse(peer='10.4.1.1')
        self.assertEqual(parsed_output, self.expected_output_3)

    def test_show_msdp_statistics_peer_4(self):
        self.maxDiff = None
        self.device = Mock(**self.device_output_4)
        obj = ShowMsdpStatisticsPeer(device=self.device)
        parsed_output = obj.parse(vrf='VRF1', peer='10.4.1.1')
        self.assertEqual(parsed_output, self.expected_output_4)

if __name__ == '__main__':
    unittest.main()
