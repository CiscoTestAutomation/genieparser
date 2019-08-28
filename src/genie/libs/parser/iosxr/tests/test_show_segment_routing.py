#!/bin/env python
import unittest
from unittest.mock import Mock

from ats.topology import Device

from genie.metaparser.util.exceptions import SchemaEmptyParserError, SchemaMissingKeyError

from genie.libs.parser.iosxr.show_segment_routing import ShowSegmentRoutingPrefixSidMap,\
                                                            ShowPceIPV4Peer,\
                                                            ShowPceIPV4PeerDetail,\
                                                            ShowPceIPV4PeerPrefix,\
                                                            ShowPceIpv4TopologySummary,\
                                                            ShowPceLsp,\
                                                            ShowPceLspDetail, \
                                                            ShowSegment_RoutingLocal_BlockInconsistencies,\
                                                            ShowSegment_RoutingMapping_ServerPrefix_Sid_MapIPV4

# =============================================================
# Unittest for:
#   * 'Show Segment Routing Prefix Sid Map'
# =============================================================
class test_show_routing_prefix_sid_map(unittest.TestCase):
    
    device = Device(name='DeviceA')
    dev2 = Device(name='DeviceB')



    empty_output = {'execute.return_value': ''}

    golden_output = {'execute.return_value': '''
        RP/0/0/CPU0:router# show isis segment-routing prefix-sid-map active-policy

            IS-IS 1 active policy
        Prefix               SID Index    Range        Flags
        1.1.1.100/32         100          20          
        1.1.1.150/32         150          10          

        Number of mapping entries: 2

        RP/0/0/CPU0:router# show isis segment-routing prefix-sid-map backup-policy

        IS-IS 1 backup policy
        Prefix               SID Index    Range        Flags
        1.1.1.100/32         100          20          
        1.1.1.150/32         150          10          

        Number of mapping entries: 2

        RP/0/0/CPU0:router# show ospf segment-routing prefix-sid-map active-policy

                SRMS active policy for Process ID 1

        Prefix               SID Index    Range        Flags
        1.1.1.100/32         100          20          
        1.1.1.150/32         150          10           

        Number of mapping entries: 2

        RP/0/0/CPU0:router# show ospf segment-routing prefix-sid-map backup-policy

                SRMS backup policy for Process ID 1

        Prefix               SID Index    Range        Flags
        1.1.1.100/32         100          20          
        1.1.1.150/32         150          10          

        Number of mapping entries: 2
    '''}

    golden_parsed_output = {
        'isis': {
        'name': 'isis',
        'active': {
            'status': True,
            'isis_id': 1,
            'algorithm': {
                'prefix': '1.1.1.100/32',
                'sid_index': 100,
                'range': 20
            },
            'entries': 2
            },
            'backup': {
                'status': False,
                'isis_id': 1,
                'algorithm': {
                    'prefix': '1.1.1.100/32',
                    'sid_index': 100,
                    'range': 20
                },
                'entries': 2
            }
        },
        'ospf': {
            'name': 'ospf',
            'active': {
                'status': True,
                'algorithm': {
                    'prefix': '1.1.1.100/32',
                    'sid_index': 100,
                    'range': 20
                },
                'process_id': 1,
                'entries': 2
            },
            'backup': {
                'status': False,
                'algorithm': {
                    'prefix': '1.1.1.100/32',
                    'sid_index': 100,
                    'range': 20
                },
                'process_id': 1,
                'entries': 2
            }
        }
    }


    def test_empty_output(self):
        self.device1 = Mock(**self.empty_output)
        obj = ShowSegmentRoutingPrefixSidMap(device=self.device1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed = obj.parse()

    def test_golden_output(self):
        self.maxDiff = None
        self.dev2 = Mock(**self.golden_output)
        obj = ShowSegmentRoutingPrefixSidMap(device = self.dev2)
        parsed = obj.parse()
        self.assertEqual(parsed, self.golden_parsed_output)
        


class test_show_pce_ivp4_peer(unittest.TestCase):
    
    dev1 = Device(name = 'DeviceA')
    dev2 = Device(name = 'DeviceB')

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
        'database': {
            '192.168.0.1': {
                'peer_address': '192.168.0.1',
                'state': True,
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
        obj = ShowPceIPV4Peer(device = self.dev1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed = obj.parse()

    def test_golden_output(self):
        self.maxDiff = None
        self.dev2 = Mock(**self.golden_output)
        obj = ShowPceIPV4Peer(device = self.dev2)
        parsed = obj.parse()
        self.assertEqual(parsed, self.golden_parsed_output)

class test_show_pce_ipv4_peer_detail(unittest.TestCase):
    
    dev1 = Device(name = 'DeviceA')
    dev2 = Device(name = 'DeviceB')

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
        'database': {
            '192.168.0.1': {
                'peer_address': '192.168.0.1',
                'state': True,
                'capabilities': {
                    'stateful': True,
                    'segment-routing': True,
                    'update': True
                },
                'pcep': {
                    'pcep_uptime': '00:01:50',
                    'pcep_local_id': 0,
                    'pcep_remote_id': 0
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
        obj = ShowPceIPV4PeerDetail(device = self.dev1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed = obj.parse()

    def test_golden_output(self):
        self.maxDiff = None
        self.dev2 = Mock(**self.golden_output)
        obj = ShowPceIPV4PeerDetail(device = self.dev2)
        parsed = obj.parse()
        self.assertEqual(parsed, self.golden_parsed_output)

class test_Show_Pce_IPV4_Peer_prefix(unittest.TestCase):
    dev1 = Device(name = 'DeviceA')
    dev2 = Device(name = 'DeviceB')

    empty_output = {'execute.return_value': ''}

    golden_output = {'execute.return_value': '''
        RP/0/RSP0/CPU0:router# show pce ipv4 prefix

        PCE's prefix database:
        ----------------------
        Node 1
        TE router ID: 192.168.0.1
        Host name: rtrA
        ISIS system ID: 1921.6800.1001 level-1
        Advertised Prefixes:
        192.168.0.1

        Node 2
        TE router ID: 192.168.0.2
        Host name: rtrB
        ISIS system ID: 1921.6800.1002 level-2
        Advertised Prefixes:
        192.168.0.2
    '''}

    golden_parsed_output = {
        'prefix': {
            1: {
                'node': 1,
                'te_router_id': '192.168.0.1',
                'host_name': 'rtrA',
                '1921.6800.1001': {
                    'system_id': '1921.6800.1001',
                    'level': 1
                },
                'advertised_prefixes': '192.168.0.1'
            },
            2: {
                'node': 2,
                'te_router_id': '192.168.0.2',
                'host_name': 'rtrB',
                '1921.6800.1002': {
                    'system_id': '1921.6800.1002',
                    'level': 2
                },
                'advertised_prefixes': '192.168.0.2'
            }
        }
    }


    def test_empty_output(self):
        self.dev1 = Mock(**self.empty_output)
        obj = ShowPceIPV4PeerPrefix(device = self.dev1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed = obj.parse()

    def test_golden_output(self):
        self.maxDiff = None
        self.dev2 = Mock(**self.golden_output)
        obj = ShowPceIPV4PeerPrefix(device = self.dev2)
        parsed = obj.parse()
        self.assertEqual(parsed, self.golden_parsed_output)


class test_Show_Pce_Ipv4_Topology_Summary(unittest.TestCase):
    dev1 = Device(name = 'DeviceA')
    dev2 = Device(name = 'DeviceB')

    empty_output = {'execute.return_value' : ''}

    golden_output = {'execute.return_value' : '''
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
        'summary': {
            'topology_nodes': 4,
            'prefixes': {
                'prefixes': 4,
                'prefix_sids': 4
            }, 
            'links': {
                'links': 12,
                'adjancency_sids': 24
            }
        }
    }

    def test_empty_output(self):
        self.dev1 = Mock(**self.empty_output)
        obj = ShowPceIpv4TopologySummary(device = self.dev1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed = obj.parse()

    def test_golden_output(self):
        self.maxDiff = None
        self.dev2 = Mock(**self.golden_output)
        obj = ShowPceIpv4TopologySummary(device = self.dev2)
        parsed = obj.parse()
        self.assertEqual(parsed, self.golden_parsed_output)


class test_show_Pce_Lsp(unittest.TestCase):
    dev1 = Device(name = 'DeviceA')
    dev2 = Device(name = 'DeviceB')

    empty_output = {'execute.return_value' : ''}


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
                'pcc': '192.168.0.1',
                'tunnel_name': 'rtrA_t1',
                'lsps': {
                    0: {
                        'lsp_number': 0,
                        'source': '192.168.0.1',
                        'destination': '192.168.0.4',
                        'tunnel_id': 1,
                        'lsp_id': 2,
                        'state': {
                            'admin': True,
                            'operation': True
                        },
                        'setup_type':
                        'Segment Routing',
                        'binding_sid': 24013
                    }
                }
            }
        }
    }


    def test_empty_output(self):
        self.dev1 = Mock(**self.empty_output)
        obj = ShowPceLsp(device = self.dev1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed = obj.parse()

    def test_golden_output(self):
        self.maxDiff = None
        self.dev2 = Mock(**self.golden_output)
        obj = ShowPceLsp(device = self.dev2)
        parsed = obj.parse()
        self.assertEqual(parsed, self.golden_parsed_output)

class test_Show_Pce_Lsp_Detail(unittest.TestCase):
    dev1 = Device(name = 'DeviceA')
    dev2 = Device(name = 'DeviceB')

    empty_output = {'execute.return_value': ''}

    golden_output = {'execute.return_value' : '''
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
            SID[1]: Adj, Label 24000, Address: local 14.14.14.2 remote 14.14.14.4
        Computed path:
            Metric type: TE, Accumulated Metric 42
            SID[0]: Adj, Label 24000, Address: local 10.10.10.1 remote 10.10.10.2
            SID[1]: Adj, Label 24000, Address: local 14.14.14.2 remote 14.14.14.4
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
            SID[1]: Adj, Label 24000, Address: local 14.14.14.2 remote 14.14.14.4
        Computed path:
            Metric type: TE, Accumulated Metric 42
            SID[0]: Adj, Label 24000, Address: local 10.10.10.1 remote 10.10.10.2
            SID[1]: Adj, Label 24000, Address: local 14.14.14.2 remote 14.14.14.4
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
                'pcc': '192.168.0.1',
                'tunnel_name': 'rtrA_t1',
                'lsps': {
                    0: {
                        'lsp_number': 0,
                        'source': '192.168.0.1',
                        'destination': '192.168.0.4',
                        'tunnel_id': 1,
                        'lsp_id': 2,
                        'state': {
                            'admin': True,
                            'operation': True
                        },
                        'setup_type': 'segment routing',
                        'binding_sid': 24013,
                        'pcep_information': {
                            'plsp_id': 2,
                            'plsp_flags': 'd:1 s:0 r:0 a:1 o:1'
                        },
                        'paths': {
                            'reported': {
                                'path': 'reported',
                                'metric_type': 'te',
                                'accumulated_metric': 42,
                                'sids': {
                                    0: {
                                        'sid_number': 0,
                                        'sid_label': 24000,
                                        'sid_local_address': '10.10.10.1',
                                        'sid_remote_address': '10.10.10.2'
                                    },
                                    1: {
                                        'sid_number': 1,
                                        'sid_label': 24000,
                                        'sid_local_address': '14.14.14.2',
                                        'sid_remote_address': '14.14.14.4'
                                    }
                                }
                            },
                            'computed': {
                                'path': 'computed',
                                'metric_type': 'te',
                                'accumulated_metric': 42,
                                'sids': {
                                    0: {
                                        'sid_number': 0,
                                        'sid_label': 24000,
                                        'sid_local_address': '10.10.10.1',
                                        'sid_remote_address': '10.10.10.2'
                                    },
                                    1: {
                                        'sid_number': 1,
                                        'sid_label': 24000,
                                        'sid_local_address': '14.14.14.2',
                                        'sid_remote_address': '14.14.14.4'
                                    }
                                }
                            },
                            'recorded': {
                                'path': 'recorded',
                                'none': 'none'
                            }
                        }
                    },
                    'event_history': {
                        'june 13 2016 13:28:29': {
                            'time': 'june 13 2016 13:28:29',
                            'report': {
                                'event': 'report',
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
                        'june 13 2016 13:28:28': {
                            'time': 'june 13 2016 13:28:28',
                            'report': {
                                'event': 'report',
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
                                'event': 'create',
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
        obj = ShowPceLspDetail(device = self.dev1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed = obj.parse()

    def test_golden_output(self):
        self.maxDiff = None
        self.dev2 = Mock(**self.golden_output)
        obj = ShowPceLspDetail(device = self.dev2)
        parsed = obj.parse()
        self.assertEqual(parsed, self.golden_parsed_output)

class Test_Show_Segment_Routing_Local_Block_Inconsistencies(unittest.TestCase):
    dev1 = Device(name = 'DeviceA')
    dev2 = Device(name = 'DeviceB')

    empty_output = {'execute.return_value' : ''}

    golden_output = {'execute.return_value' : '''
    RP/0/RSP0/CPU0:router(config)# show segment-routing local-block inconsistencies
    Tue Aug 15 13:53:30.555 EDT
    SRLB inconsistencies range: Start/End: 30000/30009
    '''}

    golden_parsed_output = {
        'dates' : {
            'tue aug 15 13:53:30.555 edt' : {
                'date' : 'tue aug 15 13:53:30.555 edt',
                'inconsistencies' : {
                    'srlb' : {
                        'inconsistency' : 'srlb',
                        'range' : {
                            'start' : 30000,
                            'end' : 30009,
                        }
                    }
                }
            }
        }
    }

    def test_empty_output(self):
        self.dev1 = Mock(**self.empty_output)
        obj = ShowSegment_RoutingLocal_BlockInconsistencies(device = self.dev1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed = obj.parse()

    def test_golden_output(self):
        self.maxDiff = None
        self.dev2 = Mock(**self.golden_output)
        obj = ShowSegment_RoutingLocal_BlockInconsistencies (device = self.dev2)
        parsed = obj.parse()
        self.assertEqual(parsed, self.golden_parsed_output)

class Test_Show_Segment_Routing_Mapping_Server_Prefix_Sid_Map_IPV4(unittest.TestCase):
    dev1 = Device(name = 'DeviceA')
    dev2 = Device(name = 'DeviceB')

    empty_output = {'execute.return_value' : ''}

    golden_output = {'execute.return_value' : '''
    Prefix               SID Index    Range        Flags
    20.1.1.0/24          400          300          
    10.1.1.1/32          10           200          
    Number of mapping entries: 2
    '''}

    golden_parsed_output = {
        'ipv4': {
            '20.1.1.0/24': {
                'prefix': '20.1.1.0/24',
                'sid_index': 400,
                'range': 300
            },
            '10.1.1.1/32': {
                'prefix': '10.1.1.1/32',
                'sid_index': 10,
                'range': 200
            },
        'entries': 2
        }
    }

    def test_empty_output(self):
        self.dev1 = Mock(**self.empty_output)
        obj = ShowSegment_RoutingMapping_ServerPrefix_Sid_MapIPV4(device = self.dev1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed = obj.parse()

    def test_golden_output(self):
        self.maxDiff = None
        self.dev2 = Mock(**self.golden_output)
        obj = ShowSegment_RoutingMapping_ServerPrefix_Sid_MapIPV4(device = self.dev2)
        parsed = obj.parse()
        self.assertEqual(parsed, self.golden_parsed_output)



if __name__ == '__main__':
    unittest.main()