#!/bin/env python
import unittest
from unittest.mock import Mock

from pyats.topology import Device

from genie.metaparser.util.exceptions import SchemaEmptyParserError, SchemaMissingKeyError

from genie.libs.parser.iosxr.show_segment_routing import ShowPceLsp,\
    ShowPceIPV4Peer,\
    ShowPceLspDetail,\
    ShowPceIPV4PeerDetail,\
    ShowPceIPV4PeerPrefix,\
    ShowPceIpv4TopologySummary,\
    ShowIsisSegmentRoutingPrefixSidMap,\
    ShowOspfSegmentRoutingPrefixSidMap,\
    ShowSegmentRoutingLocalBlockInconsistencies,\
    ShowSegmentRoutingMappingServerPrefixSidMapIPV4,\
    ShowSegmentRoutingMappingServerPrefixSidMapIPV4Detail

# =============================================================
# Unittest for:
#   * 'Show Isis Segment Routing Prefix Sid Map'
# =============================================================


class test_show_isis_routing_prefix_sid_map(unittest.TestCase):

    device = Device(name='DeviceA')
    dev2 = Device(name='DeviceB')

    empty_output = {'execute.return_value': ''}

    golden_output = {'execute.return_value': '''
        RP/0/0/CPU0:router# show isis segment-routing prefix-sid-map active-policy

        IS-IS 1 active policy
        Prefix               SID Index    Range        Flags
        10.4.1.100/32         100          20
        10.4.1.150/32         150          10

        Number of mapping entries: 2

        RP/0/0/CPU0:router# show isis segment-routing prefix-sid-map backup-policy

        IS-IS 1 backup policy
        Prefix               SID Index    Range        Flags
        10.4.1.100/32         100          20
        10.4.1.150/32         150          10

        Number of mapping entries: 2
    '''}

    golden_parsed_output = {
        'process_id': {
            1: {
                'policy': {
                    'active': {
                        'sid': {
                            100: {
                                'prefix': '10.4.1.100/32',
                                'range': 20,
                            },
                            150: {
                                'prefix': '10.4.1.150/32',
                                'range': 10,
                            }
                        },
                        'number_of_mapping_entries': 2,
                    },
                    'backup': {
                        'sid': {
                            100: {
                                'prefix': '10.4.1.100/32',
                                'range': 20,
                            },
                            150: {
                                'prefix': '10.4.1.150/32',
                                'range': 10,
                            }
                        },
                        'number_of_mapping_entries': 2,
                    },
                }
            }
        }
    }

    def test_empty_output(self):
        self.device1 = Mock(**self.empty_output)
        obj = ShowIsisSegmentRoutingPrefixSidMap(device=self.device1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed = obj.parse()

    def test_golden_output(self):
        self.maxDiff = None
        self.dev2 = Mock(**self.golden_output)
        obj = ShowIsisSegmentRoutingPrefixSidMap(device=self.dev2)
        parsed = obj.parse()
        self.assertEqual(parsed, self.golden_parsed_output)


# =============================================================
# Unittest for:
#   * 'Show Ospf Segment Routing Prefix Sid Map'
# =============================================================
class test_show_ospf_routing_prefix_sid_map(unittest.TestCase):

    device = Device(name='DeviceA')
    dev2 = Device(name='DeviceB')

    empty_output = {'execute.return_value': ''}

    golden_output = {'execute.return_value': '''
        RP/0/0/CPU0:router# show ospf segment-routing prefix-sid-map active-policy

                SRMS active policy for Process ID 1

        Prefix               SID Index    Range        Flags
        10.4.1.100/32         100          20
        10.4.1.150/32         150          10

        Number of mapping entries: 2

        RP/0/0/CPU0:router# show ospf segment-routing prefix-sid-map backup-policy

                SRMS backup policy for Process ID 1

        Prefix               SID Index    Range        Flags
        10.4.1.100/32         100          20
        10.4.1.150/32         150          10

        Number of mapping entries: 2
    '''}

    golden_parsed_output = {
        'process_id': {
            1: {
                'policy': {
                    'active': {
                        'sid': {
                            100: {
                                'prefix': '10.4.1.100/32',
                                'range': 20,
                            },
                            150: {
                                'prefix': '10.4.1.150/32',
                                'range': 10,
                            }
                        },
                        'number_of_mapping_entries': 2,
                    },
                    'backup': {
                        'sid': {
                            100: {
                                'prefix': '10.4.1.100/32',
                                'range': 20,
                            },
                            150: {
                                'prefix': '10.4.1.150/32',
                                'range': 10,
                            }
                        },
                        'number_of_mapping_entries': 2,
                    },
                }
            }
        }
    }

    def test_empty_output(self):
        self.device1 = Mock(**self.empty_output)
        obj = ShowOspfSegmentRoutingPrefixSidMap(device=self.device1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed = obj.parse()

    def test_golden_output(self):
        self.maxDiff = None
        self.dev2 = Mock(**self.golden_output)
        obj = ShowOspfSegmentRoutingPrefixSidMap(device=self.dev2)
        parsed = obj.parse()
        self.assertEqual(parsed, self.golden_parsed_output)

# =============================================================
# Unittest for:
#   * 'Show pce ipv4 peer'
# =============================================================


class test_show_pce_ivp4_peer(unittest.TestCase):

    dev1 = Device(name='DeviceA')
    dev2 = Device(name='DeviceB')

    empty_output = {'execute.return_value': ''}

    golden_output = {'execute.return_value': '''
    RP/0/RSP0/CPU0:router# show pce ipv4 peer

    PCE's peer database:
    --------------------
    Peer address: 192.168.0.1
    State: Up
    Capabilities: Stateful, Segment-Routing, Update
    '''}

    golden_parsed_output = {
        'pce_peer_database': {
            '192.168.0.1': {
                'state': 'Up',
                'capabilities': {
                    'stateful': True,
                    'segment-routing': True,
                    'update': True
                }
            }
        }
    }

    def test_empty_output(self):
        self.dev1 = Mock(**self.empty_output)
        obj = ShowPceIPV4Peer(device=self.dev1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed = obj.parse()

    def test_golden_output(self):
        self.maxDiff = None
        self.dev2 = Mock(**self.golden_output)
        obj = ShowPceIPV4Peer(device=self.dev2)
        parsed = obj.parse()
        self.assertEqual(parsed, self.golden_parsed_output)


# =============================================================
# Unittest for:
#   * 'show pce ipv4 peer detail'
# =============================================================
class test_show_pce_ipv4_peer_detail(unittest.TestCase):

    dev1 = Device(name='DeviceA')
    dev2 = Device(name='DeviceB')

    empty_output = {'execute.return_value': ''}

    golden_output = {'execute.return_value': '''
    RP/0/RSP0/CPU0:router# show pce ipv4 peer detail
    PCE's peer database:
    --------------------
    Peer address: 192.168.0.1
    State: Up
    Capabilities: Stateful, Segment-Routing, Update
    PCEP has been up for: 00:01:50
    PCEP session ID: local 0, remote 0
    Sending KA every 30 seconds
    Minimum acceptable KA interval: 20 seconds
    Peer timeout after 120 seconds
    Statistics:
        Keepalive messages: rx     4 tx     4
        Request messages:   rx     3 tx     0
        Reply messages:     rx     0 tx     3
        Error messages:     rx     0 tx     0
        Open messages:      rx     1 tx     1
        Report messages:    rx     4 tx     0
        Update messages:    rx     0 tx     2
        Initiate messages:  rx     0 tx     0
    '''}

    golden_parsed_output = {
        'pce_peer_database': {
            '192.168.0.1': {
                'state': 'Up',
                'capabilities': {
                    'stateful': True,
                    'segment-routing': True,
                    'update': True
                },
                'pcep': {
                    'uptime': '00:01:50',
                    'session_id_local': 0,
                    'session_id_remote': 0
                },
                'ka': {
                    'sending_intervals': 30,
                    'minimum_acceptable_inteval': 20
                },
                'peer_timeout': 120,
                'statistics': {
                    'rx': {
                        'keepalive_messages': 4,
                        'request_messages': 3,
                        'reply_messages': 0,
                        'error_messages': 0,
                        'open_messages': 1,
                        'report_messages': 4,
                        'update_messages': 0,
                        'initiate_messages': 0
                    },
                    'tx': {
                        'keepalive_messages': 4,
                        'request_messages': 0,
                        'reply_messages': 3,
                        'error_messages': 0,
                        'open_messages': 1,
                        'report_messages': 0,
                        'update_messages': 2,
                        'initiate_messages': 0
                    }
                }
            }
        }
    }

    def test_empty_output(self):
        self.dev1 = Mock(**self.empty_output)
        obj = ShowPceIPV4PeerDetail(device=self.dev1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed = obj.parse()

    def test_golden_output(self):
        self.maxDiff = None
        self.dev2 = Mock(**self.golden_output)
        obj = ShowPceIPV4PeerDetail(device=self.dev2)
        parsed = obj.parse()
        self.assertEqual(parsed, self.golden_parsed_output)


# =============================================================
# Unittest for:
#   * 'show pce ipv4 prefix'
# =============================================================
class test_Show_Pce_IPV4_Peer_prefix(unittest.TestCase):
    dev1 = Device(name='DeviceA')
    dev2 = Device(name='DeviceB')

    empty_output = {'execute.return_value': ''}

    golden_output = {'execute.return_value': '''
        RP/0/RSP0/CPU0:router# show pce ipv4 prefix

        PCE's prefix database:
        ----------------------
        Node 1
        TE router ID: 192.168.0.4
        Host name: rtrD
        ISIS system ID: 1921.68ff.1004 level-1 ASN: 65001 domain ID: 1111
        ISIS system ID: 1921.68ff.1004 level-2 ASN: 65001 domain ID: 1111
        ISIS system ID: 1921.68ff.1004 level-2 ASN: 65001 domain ID: 9999
        Advertised Prefixes:
        192.168.0.4
        192.168.0.4
        192.168.0.4
        192.168.0.6

        Node 2
        TE router ID: 192.168.0.1
        Host name: rtrA
        ISIS system ID: 1921.68ff.1001 level-2
        Advertised Prefixes:
        192.168.0.1
    '''}

    golden_parsed_output = {
        'nodes': {
            1: {
                'te_router_id': '192.168.0.4',
                'host_name': 'rtrD',
                'isis_system_id': [
                    '1921.68ff.1004 level-1',
                    '1921.68ff.1004 level-2',
                    '1921.68ff.1004 level-2'],
                'asn': [
                    65001,
                    65001,
                    65001],
                'domain_id': [
                    1111,
                    1111,
                    9999],
                'advertised_prefixes': [
                    '192.168.0.4',
                    '192.168.0.4',
                    '192.168.0.4',
                    '192.168.0.6']},
            2: {
                'te_router_id': '192.168.0.1',
                'host_name': 'rtrA',
                                'isis_system_id': ['1921.68ff.1001 level-2'],
                'advertised_prefixes': ['192.168.0.1']}}}

    def test_empty_output(self):
        self.dev1 = Mock(**self.empty_output)
        obj = ShowPceIPV4PeerPrefix(device=self.dev1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed = obj.parse()

    def test_golden_output(self):
        self.maxDiff = None
        self.dev2 = Mock(**self.golden_output)
        obj = ShowPceIPV4PeerPrefix(device=self.dev2)
        parsed = obj.parse()
        self.assertEqual(parsed, self.golden_parsed_output)


# =============================================================
# Unittest for:
#   * 'show pce ipv4 topology summary'
# =============================================================
class test_Show_Pce_Ipv4_Topology_Summary(unittest.TestCase):
    dev1 = Device(name='DeviceA')
    dev2 = Device(name='DeviceB')

    empty_output = {'execute.return_value': ''}

    golden_output = {'execute.return_value': '''
        RP/0/RSP0/CPU0:router# show pce ipv4 topology summary

        PCE's topology database summary:
        --------------------------------

        Topology nodes:                4
        Prefixes:                      4
        Prefix SIDs:                 4
        Links:                        12
        Adjacency SIDs:             24
    '''}

    golden_parsed_output = {
    'pce_topology_database_summary': {
        'adjancency_sids': {
            'total': 24,
        },
        'links': {
            'total': 12,
        },
        'prefix_sids': {
            'total': 4,
        },
        'prefixes': 4,
        'topology_nodes': 4,
    },
}

    expected_output_2 = {
        'pce_topology_database_summary': {
            'adjancency_sids': {
                'epe': 0,
                'protected': 0,
                'total': 0,
                'unprotected': 0,
            },
            'links': {
                'epe': 0,
                'total': 0,
            },
            'prefix_sids': {
                'regular': 0,
                'strict': 0,
                'total': 0,
            },
            'prefixes': 0,
            'private_information': {
                'consistent': 'yes',
                'lookup_nodes': 0,
                'update_stats': {
                    'links': {
                        'added': 0,
                        'deleted': 0,
                    },
                    'noded': {
                        'added': 0,
                        'deleted': 0,
                    },
                    'prefix': {
                        'added': 0,
                        'deleted': 0,
                    },
                },
            },
            'topology_nodes': 0,
        },
    }
    device_output_2 = {'execute.return_value': '''

        PCE's topology database summary:
        --------------------------------

        Topology nodes:                0
        Prefixes:                      0
        Prefix SIDs:
          Total:                       0
          Regular:                     0
          Strict:                      0
        Links:
          Total:                       0
          EPE:                         0
        Adjacency SIDs:
          Total:                       0
          Unprotected:                 0
          Protected:                   0
          EPE:                         0

        Private Information:
        Lookup Nodes                   0
        Consistent                   yes
        Update Stats (from IGP and/or BGP):
          Noded added:                 0
          Noded deleted:               0
          Links added:                 0
          Links deleted:               0
          Prefix added:                0
          Prefix deleted:              0
    '''}

    def test_empty_output(self):
        self.dev1 = Mock(**self.empty_output)
        obj = ShowPceIpv4TopologySummary(device=self.dev1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed = obj.parse()

    def test_golden_output(self):
        self.maxDiff = None
        self.dev2 = Mock(**self.golden_output)
        obj = ShowPceIpv4TopologySummary(device=self.dev2)
        parsed = obj.parse()
        self.assertEqual(parsed, self.golden_parsed_output)

    def test_golden_output_2(self):
        self.maxDiff = None
        self.dev3 = Mock(**self.device_output_2)
        obj = ShowPceIpv4TopologySummary(device=self.dev3)
        parsed = obj.parse()
        self.assertEqual(parsed, self.expected_output_2)


# =============================================================
# Unittest for:
#   * 'show pce lsp'
# =============================================================
class test_show_Pce_Lsp(unittest.TestCase):
    dev1 = Device(name='DeviceA')
    dev2 = Device(name='DeviceB')

    empty_output = {'execute.return_value': ''}

    golden_output = {'execute.return_value': '''
        RP/0/RSP0/CPU0:router# show pce lsp

        PCE's tunnel database:
        ----------------------
        PCC 192.168.0.1:

        Tunnel Name: rtrA_t1
        LSPs:
        LSP[0]:
        source 192.168.0.1, destination 192.168.0.4, tunnel ID 1, LSP ID 2
        State: Admin up, Operation up
        Setup type: Segment Routing
        Binding SID: 24013
    '''}

    golden_parsed_output = {
        'pcc': {
            '192.168.0.1': {
                'tunnel_name': {
                    'rtrA_t1': {
                        'lsps': {
                            0: {
                                'source': '192.168.0.1',
                                'destination': '192.168.0.4',
                                'tunnel_id': 1,
                                'lsp_id': 2,
                                'admin_state': 'up',
                                'operation_state': 'up',
                                'setup_type': 'Segment Routing',
                                'binding_sid': 24013
                            }
                        }
                    }
                }
            }
        }
    }

    def test_empty_output(self):
        self.dev1 = Mock(**self.empty_output)
        obj = ShowPceLsp(device=self.dev1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed = obj.parse()

    def test_golden_output(self):
        self.maxDiff = None
        self.dev2 = Mock(**self.golden_output)
        obj = ShowPceLsp(device=self.dev2)
        parsed = obj.parse()
        self.assertEqual(parsed, self.golden_parsed_output)

# =============================================================
# Unittest for:
#   * 'show pce lsp detail'
# =============================================================


class test_Show_Pce_Lsp_Detail(unittest.TestCase):
    dev1 = Device(name='DeviceA')
    dev2 = Device(name='DeviceB')

    empty_output = {'execute.return_value': ''}

    golden_output = {'execute.return_value': '''
        RP/0/RSP0/CPU0:router# show pce lsp detail

        PCE's tunnel database:
        ----------------------
        PCC 192.168.0.1:

        Tunnel Name: rtrA_t1
        LSPs:
        LSP[0]:
        source 192.168.0.1, destination 192.168.0.4, tunnel ID 1, LSP ID 2
        State: Admin up, Operation up
        Setup type: Segment Routing
        Binding SID: 24013
        PCEP information:
            plsp-id 2, flags: D:1 S:0 R:0 A:1 O:1
        Reported path:
            Metric type: TE, Accumulated Metric 42
            SID[0]: Adj, Label 24000, Address: local 10.10.10.1 remote 10.10.10.2
            SID[1]: Adj, Label 24000, Address: local 10.19.14.2 remote 10.19.14.4
        Computed path:
            Metric type: TE, Accumulated Metric 42
            SID[0]: Adj, Label 24000, Address: local 10.10.10.1 remote 10.10.10.2
            SID[1]: Adj, Label 24000, Address: local 10.19.14.2 remote 10.19.14.4
        Recorded path:
            None

        RP/0/RSP0/CPU0:router# show pce lsp detail

        PCE's tunnel database:
        ----------------------
        PCC 192.168.0.1:

        Tunnel Name: rtrA_t1
        LSPs:
        LSP[0]:
        source 192.168.0.1, destination 192.168.0.4, tunnel ID 1, LSP ID 2
        State: Admin up, Operation up
        Setup type: Segment Routing
        Binding SID: 24013
        PCEP information:
            plsp-id 2, flags: D:1 S:0 R:0 A:1 O:1
        Reported path:
            Metric type: TE, Accumulated Metric 42
            SID[0]: Adj, Label 24000, Address: local 10.10.10.1 remote 10.10.10.2
            SID[1]: Adj, Label 24000, Address: local 10.19.14.2 remote 10.19.14.4
        Computed path:
            Metric type: TE, Accumulated Metric 42
            SID[0]: Adj, Label 24000, Address: local 10.10.10.1 remote 10.10.10.2
            SID[1]: Adj, Label 24000, Address: local 10.19.14.2 remote 10.19.14.4
        Recorded path:
            None
        Event history (latest first):
        Time                      Event
        June 13 2016 13:28:29     Report
                                Symbolic-name: rtrA_t1, LSP-ID: 2,
                                Source: 192.168.0.1 Destination: 192.168.0.4,
                                D:1, R:0, A:1 O:1, Sig.BW: 0, Act.BW: 0
        June 13 2016 13:28:28     Report
                                Symbolic-name: rtrA_t1, LSP-ID: 2,
                                Source: 192.168.0.1 Destination: 192.168.0.4,
                                D:1, R:0, A:1 O:1, Sig.BW: 0, Act.BW: 0
        June 13 2016 13:28:28     Create
                                Symbolic-name: rtrA_t1, PLSP-ID: 2,
                                Peer: 192.168.0.1
    '''}

    golden_parsed_output = {
        'pcc': {
            '192.168.0.1': {
                'tunnel_name': 'rtrA_t1',
                'lsps': {
                    0: {
                        'source': '192.168.0.1',
                        'destination': '192.168.0.4',
                        'tunnel_id': 1,
                        'lsp_id': 2,
                        'admin_state': 'up',
                        'operation_state': 'up',
                        'setup_type': 'segment routing',
                        'binding_sid': 24013,
                        'pcep_information': {
                            'plsp_id': 2,
                            'flags': {
                                'd': 1,
                                's': 0,
                                'r': 0,
                                'a': 1,
                                'o': 1,
                            }
                        },
                        'paths': {
                            'reported': {
                                'metric_type': 'TE',
                                'accumulated_metric': 42,
                                'sids': {
                                    0: {
                                        'type': 'Adj',
                                        'label': 24000,
                                        'local_address': '10.10.10.1',
                                        'remote_address': '10.10.10.2'
                                    },
                                    1: {
                                        'type': 'Adj',
                                        'label': 24000,
                                        'local_address': '10.19.14.2',
                                        'remote_address': '10.19.14.4'
                                    }
                                }
                            },
                            'computed': {
                                'metric_type': 'TE',
                                'accumulated_metric': 42,
                                'sids': {
                                    0: {
                                        'type': 'Adj',
                                        'label': 24000,
                                        'local_address': '10.10.10.1',
                                        'remote_address': '10.10.10.2'
                                    },
                                    1: {
                                        'type': 'Adj',
                                        'label': 24000,
                                        'local_address': '10.19.14.2',
                                        'remote_address': '10.19.14.4'
                                    }
                                }
                            },
                            'recorded': {}
                        }
                    },
                    'event_history': {
                        'June 13 2016 13:28:29': {
                            'report': {
                                'symbolic_name': 'rtrA_t1',
                                'lsp-id': 2,
                                'source': '192.168.0.1',
                                'destination': '192.168.0.4',
                                'flags': {
                                    'd': 1,
                                    'r': 0,
                                    'a': 1,
                                    'o': 1,
                                    'sig_bw': 0,
                                    'act_bw': 0
                                }
                            }
                        },
                        'June 13 2016 13:28:28': {
                            'report': {
                                'symbolic_name': 'rtrA_t1',
                                'lsp-id': 2,
                                'source': '192.168.0.1',
                                'destination': '192.168.0.4',
                                'flags': {
                                    'd': 1,
                                    'r': 0,
                                    'a': 1,
                                    'o': 1,
                                    'sig_bw': 0,
                                    'act_bw': 0
                                }
                            },
                            'create': {
                                'symbolic_name': 'rtrA_t1',
                                'plsp-id': 2,
                                'peer': '192.168.0.1'
                            }
                        }
                    }
                }
            }
        }
    }

    def test_empty_output(self):
        self.dev1 = Mock(**self.empty_output)
        obj = ShowPceLspDetail(device=self.dev1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed = obj.parse()

    def test_golden_output(self):
        self.maxDiff = None
        self.dev2 = Mock(**self.golden_output)
        obj = ShowPceLspDetail(device=self.dev2)
        parsed = obj.parse()
        self.assertEqual(parsed, self.golden_parsed_output)

# =============================================================
# Unittest for:
#   * 'show segment-routing local-block inconsistencies'
# =============================================================


class Test_Show_Segment_Routing_Local_Block_Inconsistencies(unittest.TestCase):
    dev1 = Device(name='DeviceA')
    dev2 = Device(name='DeviceB')

    empty_output = {'execute.return_value': ''}

    golden_output = {'execute.return_value': '''
    RP/0/RSP0/CPU0:router(config)# show segment-routing local-block inconsistencies
    Tue Aug 15 13:53:30.555 EDT
    SRLB inconsistencies range: Start/End: 30000/30009
    '''}

    golden_parsed_output = {
        'srlb_inconsistencies_range': {
            'start': 30000,
            'end': 30009,
        }
    }

    def test_empty_output(self):
        self.dev1 = Mock(**self.empty_output)
        obj = ShowSegmentRoutingLocalBlockInconsistencies(device=self.dev1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed = obj.parse()

    def test_golden_output(self):
        self.maxDiff = None
        self.dev2 = Mock(**self.golden_output)
        obj = ShowSegmentRoutingLocalBlockInconsistencies(device=self.dev2)
        parsed = obj.parse()
        self.assertEqual(parsed, self.golden_parsed_output)


# ====================================================================
# Unittest for:
#   * 'show segment-routing mapping-server prefix-sid-map ipv4'
# ====================================================================
class Test_Show_Segment_Routing_Mapping_Server_Prefix_Sid_Map_IPV4(
        unittest.TestCase):
    dev1 = Device(name='DeviceA')
    dev2 = Device(name='DeviceB')

    empty_output = {'execute.return_value': ''}

    golden_output = {'execute.return_value': '''
    show segment-routing mapping-server prefix-sid-map ipv4
    Prefix               SID Index    Range        Flags
    10.186.1.0/24          400          300
    10.1.1.1/32          10           200
    Number of mapping entries: 2
    '''}

    golden_parsed_output = {
        'ipv4': {
            'number_of_mapping_entries': 2,
            'prefix': {
                '10.186.1.0/24': {
                    'sid_index': 400,
                    'range': 300
                },
                '10.1.1.1/32': {
                    'sid_index': 10,
                    'range': 200
                }
            },
        }
    }

    def test_empty_output(self):
        self.dev1 = Mock(**self.empty_output)
        obj = ShowSegmentRoutingMappingServerPrefixSidMapIPV4(
            device=self.dev1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed = obj.parse()

    def test_golden_output(self):
        self.maxDiff = None
        self.dev2 = Mock(**self.golden_output)
        obj = ShowSegmentRoutingMappingServerPrefixSidMapIPV4(
            device=self.dev2)
        parsed = obj.parse()
        self.assertEqual(parsed, self.golden_parsed_output)

# ====================================================================
# Unittest for:
#   * 'show segment-routing mapping-server prefix-sid-map ipv4 detail'
# ====================================================================


class Test_Show_Segment_Routing_Mapping_Server_Prefix_Sid_Map_IPV_4Detail(
        unittest.TestCase):
    dev1 = Device(name='DeviceA')
    dev2 = Device(name='DeviceB')

    empty_output = {'execute.return_value': ''}

    golden_output = {'execute.return_value': '''
        RP/0/0/CPU0:router# show segment-routing mapping-server prefix-sid-map ipv4 detail
        Prefix
        10.186.1.0/24
            SID Index:      400
            Range:          300
            Last Prefix:    10.229.44.0/24
            Last SID Index: 699
            Flags:
        10.1.1.1/32
            SID Index:      10
            Range:          200
    '''}

    golden_parsed_output = {
        'ipv4': {
            'prefix': {
                '10.186.1.0/24': {
                    'sid_index': 400,
                    'range': 300,
                    'last_prefix': '10.229.44.0/24',
                    'last_sid_index': 699
                },
                '10.1.1.1/32': {
                    'sid_index': 10,
                    'range': 200
                },
            }
        }
    }

    def test_empty_output(self):
        self.dev1 = Mock(**self.empty_output)
        obj = ShowSegmentRoutingMappingServerPrefixSidMapIPV4Detail(
            device=self.dev1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed = obj.parse()

    def test_golden_output(self):
        self.maxDiff = None
        self.dev2 = Mock(**self.golden_output)
        obj = ShowSegmentRoutingMappingServerPrefixSidMapIPV4Detail(
            device=self.dev2)
        parsed = obj.parse()
        self.assertEqual(parsed, self.golden_parsed_output)


if __name__ == '__main__':
    unittest.main()
