# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device

# Metaparset
from genie.metaparser.util.exceptions import SchemaEmptyParserError, \
                                             SchemaMissingKeyError

# Parser
from genie.libs.parser.iosxe.show_clns import ShowClnsInterface,\
                                              ShowClnsProtocol,\
                                              ShowClnsNeighborsDetail,\
                                              ShowClnsIsNeighborsDetail,\
                                              ShowClnsTraffic

# =========================================================
# Unit test for 'show clns interface'
#               'show show clns interface <inteface>'
# =========================================================
class test_show_ip_interface(unittest.TestCase):
    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output = {
        'interfaces':{
            'GigabitEthernet1':{
                'status':'up',
                'line_protocol': 'up',
                'clns_protocol_processing': False,
            },
            'GigabitEthernet2': {
                'status': 'up',
                'line_protocol': 'up',
                'checksum_enabled': True,
                'mtu': 1497,
                'encapsulation': 'SAP',
                'erpdus_enabled': True,
                'min_interval_msec': 10,
                'clns_fast_switching': True,
                'clns_sse_switching': False,
                'dec_compatibility_mode': 'OFF',
                'next_esh_ish_in': 20,
                'routing_protocol': {
                    'IS-IS': {
                        'process_id':{
                            'test': {
                               'level_type': 'level-1-2',
                                'interface_number': '0x1',
                                'local_circuit_id': '0x1',
                                'neighbor_extended_local_circuit_id': '0x0',
                                'hello_interval':{
                                    'level-1': {
                                        'next_is_is_lan_hello_in': 1,
                                    } ,
                                    'level-2': {
                                        'next_is_is_lan_hello_in': 645,
                                    },
                                },
                                'level-1': {
                                    'metric': 10,
                                    'dr_id': 'R2.01',
                                    'circuit_id': 'R2.01',
                                    'ipv6_metric': 10,
                                },
                                'level-2': {
                                    'metric': 10,
                                    'dr_id': '0000.0000.0000.00',
                                    'circuit_id': 'R2.01',
                                    'ipv6_metric': 10,
                                },
                                'priority':{
                                    'level-1':{
                                        'priority': 64,
                                    },
                                    'level-2': {
                                        'priority': 64,
                                    },
                                } ,
                                'adjacencies':{
                                    'level-1': {
                                        'number_of_active_adjancies': 1
                                    },
                                    'level-2': {
                                        'number_of_active_adjancies': 0
                                    },
                                }
                            }
                        },
                    }
                }
            }
        }
    }

    golden_output = {'execute.return_value': '''\
    R2#show clns interface
    GigabitEthernet1 is up, line protocol is up
      CLNS protocol processing disabled
    GigabitEthernet2 is up, line protocol is up
      Checksums enabled, MTU 1497, Encapsulation SAP
      ERPDUs enabled, min. interval 10 msec.
      CLNS fast switching enabled
      CLNS SSE switching disabled
      DEC compatibility mode OFF for this interface
      Next ESH/ISH in 20 seconds
      Routing Protocol: IS-IS (test)
        Circuit Type: level-1-2
        Interface number 0x1, local circuit ID 0x1
        Neighbor Extended Local Circuit ID: 0x0
        Level-1 Metric: 10, Priority: 64, Circuit ID: R2.01
        DR ID: R2.01
        Level-1 IPv6 Metric: 10
        Number of active level-1 adjacencies: 1
        Level-2 Metric: 10, Priority: 64, Circuit ID: R2.01
        DR ID: 0000.0000.0000.00
        Level-2 IPv6 Metric: 10
        Number of active level-2 adjacencies: 0
        Next IS-IS LAN Level-1 Hello in 1 seconds
        Next IS-IS LAN Level-2 Hello in 645 milliseconds
    '''}


    def test_empty(self):
        self.device1 = Mock(**self.empty_output)
        obj = ShowClnsInterface(device=self.device1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden_clns_interface(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output)
        obj = ShowClnsInterface(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


# =========================================================
# Unit test for 'show clns protocol'
# =========================================================
class test_show_clns_protocol(unittest.TestCase):
    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output = {
        'IS-IS':{
            'process_tag': 'VRF1',
            'system_id': '2222.2222.2222.00',
            'process_handle': '0x10001',
            'is_type': 'level-1-2',
            'manual_area_address':['49.0001'],
            'routing_for_area_address':['49.0001'],
            'interfaces':{
                'GigabitEthernet4':{
                    'topology': ['ipv4','ipv6'],
                },
                'Loopback1': {
                    'topology': ['ipv4', 'ipv6'],
                },
            },
            'redistribute':'static (on by default)',
            'distance_for_l2_clns_routes':110,
            'rrr_level': 'none',
            'metrics':{
              'generate_narrow': 'none',
              'accept_narrow': 'none',
              'generate_wide': 'level-1-2',
              'accept_wide': 'level-1-2',
            }

        }
    }

    golden_output = {'execute.return_value': '''\
    R2#show clns protocol
    IS-IS Router: VRF1 (0x10001)
      System Id: 2222.2222.2222.00  IS-Type: level-1-2
      Manual area address(es):
        49.0001
      Routing for area address(es):
        49.0001
      Interfaces supported by IS-IS:
        GigabitEthernet4 - IP - IPv6
        Loopback1 - IP - IPv6
      Redistribute:
        static (on by default)
      Distance for L2 CLNS routes: 110
      RRR level: none
      Generate narrow metrics: none
      Accept narrow metrics:   none
      Generate wide metrics:   level-1-2
      Accept wide metrics:     level-1-2
    '''}

    def test_empty(self):
        self.device1 = Mock(**self.empty_output)
        obj = ShowClnsProtocol(device=self.device1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden_clns_protocol(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output)
        obj = ShowClnsProtocol(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)

# =========================================================
# Unit test for 'show clns neighbors detail'
# =========================================================
class test_show_clns_neighbors_detail(unittest.TestCase):
    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output = {
        'tag': {
            'VRF1': {
                'system_id':{
                    'R7':{
                        'type':{
                            'L2': {
                                'interface': 'GigabitEthernet4',
                                'state': 'up',
                                'snpa': '5e00.c006.0007',
                                'holdtime': 26,
                                'protocol': 'M-ISIS',
                            },
                        }
                    },
                },
                'area_address': ['49.0002'],
                'ip_address': ['20.2.7.7*'],
                'ipv6_address': ['FE80::5C00:C0FF:FE06:7'],
                'uptime': '00:23:58',
                'nsf': 'capable',
                'topology': ['ipv4', 'ipv6'],
                'interface': 'GigabitEthernet4',
            }
        }
    }

    golden_output = {'execute.return_value': '''\
    R2#show clns neighbors detail

    Tag VRF1:
    System Id       Interface     SNPA                State  Holdtime  Type Protocol
    R7              Gi4           5e00.c006.0007      Up     26        L2   M-ISIS
      Area Address(es): 49.0002
      IP Address(es):  20.2.7.7*
      IPv6 Address(es): FE80::5C00:C0FF:FE06:7
      Uptime: 00:23:58
      NSF capable
      Topology: IPv4, IPv6
      Interface name: GigabitEthernet4
    '''}

    def test_empty(self):
        self.device1 = Mock(**self.empty_output)
        obj = ShowClnsNeighborsDetail(device=self.device1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden_clns_neighbor_detail(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output)
        obj = ShowClnsNeighborsDetail(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


# =========================================================
# Unit test for 'show clns is-neighbor detail'
# =========================================================
class test_show_clns_is_neighbor_detail(unittest.TestCase):
    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output = {
        'tag':{
            'VRF1':{
                'system_id': 'R7',
                'interface': 'GigabitEthernet4',
                'state': 'up',
                'type': 'L2',
                'priority': 64,
                'circuit_id': 'R2.01',
                'format': 'Phase V',
                'area_address': ['49.0002'],
                'ip_address': ['20.2.7.7*'],
                'ipv6_address': ['FE80::5C00:C0FF:FE06:7'],
                'uptime': '00:24:24',
                'nsf': 'capable',
                'topology':['ipv4','ipv6'],
            }
        }
    }

    golden_output = {'execute.return_value': '''\
    R2#show clns is-neighbors detail

    Tag VRF1:
    System Id       Interface     State  Type Priority  Circuit Id         Format
    R7              Gi4           Up     L2   64        R2.01              Phase V
      Area Address(es): 49.0002
      IP Address(es):  20.2.7.7*
      IPv6 Address(es): FE80::5C00:C0FF:FE06:7
      Uptime: 00:24:24
      NSF capable
      Topology: IPv4, IPv6
      Interface name: GigabitEthernet4

    '''}

    def test_empty(self):
        self.device1 = Mock(**self.empty_output)
        obj = ShowClnsIsNeighborsDetail(device=self.device1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden_clns_is_neighbor_detail(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output)
        obj = ShowClnsIsNeighborsDetail(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


# =========================================================
# Unit test for 'show clns traffic'
# =========================================================
class test_show_clns_traffic(unittest.TestCase):
    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output = {
        'clns':{
            'last_clear': 'never',
            'output': 168,
            'input': 4021,
            'local': 0,
            'forward': 0,
            'dropped_protocol': 0,
            'discards': {
                'hdr_syntax': 0,
                'checksum': 0,
                'lifetime': 0,
                'output_cngstn': 0,
                'no_route': 0,
                'discard_route': 0,
                'dst_unreachable': 0,
                'encaps_failed': 0,
                'nlp_unknown': 0,
                'not_an_is': 0,
            },
            'options':{
                'packets': 0,
                'total': 0 ,
                'bad': 0,
                'gqos': 0,
                'cngstn_exprncd': 0,
            },
            'segments':{
                'segmented': 0,
                'failed': 0,
            },
            'broadcasts': {
                'sent': 0,
                'rcvd': 0,
            },
        },
        'echos':{
            'rcvd':{
                'requests':0,
                'replied':0,
            },
            'sent': {
                'requests': 0,
                'replied': 0,
            },
        },
        'packet_counters': {
            'level': {
                'level-all': {
                    'esh': {
                        'rcvd': 0,
                        'sent': 0,
                    },
                    'ish': {
                        'rcvd': 0,
                        'sent': 168,
                    },
                    'rd': {
                        'rcvd': 0,
                        'sent': 0,
                    },
                    'qcf': {
                        'rcvd': 0,
                        'sent': 0,
                    },
                },
            },
        },
        'tunneling': {
            'ip': {
                'rcvd': 0,
                'sent': 0,
                'rcvd_dropped':0,
            },
            'ipv6': {
                'rcvd': 0,
                'sent': 0,
                'rcvd_dropped': 0,
            },
        },
        'iso-igrp': {
            'query': {
                 'rcvd': 0,
                 'sent': 0,
            },
            'update': {
                'rcvd': 0,
                'sent': 0,
            },
            'router_hello': {
                'rcvd': 0,
                'sent': 0,
            },
            'syntax_errors': 0
        },
        'tag':{
            'VRF1':{
                'IS-IS': {
                    'last_clear': 'never',
                    'hello':{
                        'level-1': {
                            'rcvd': 533,
                            'sent': 497,
                        },
                        'level-2': {
                            'rcvd': 611,
                            'sent': 843,
                        },
                        'ptp':{
                            'rcvd': 0,
                            'sent': 0,
                        },
                    },
                    'lsp_sourced': {
                        'level-1': {
                            'new': 3,
                            'refresh': 4,
                        },
                        'level-2': {
                            'new': 4,
                            'refresh': 5,
                        },
                    },
                    'lsp_flooded': {
                        'level-1': {
                            'sent': 0,
                            'rcvd': 0,
                        },
                        'level-2': {
                            'sent': 5,
                            'rcvd': 5,
                        },
                    },
                    'lsp_retransmissions': 0,
                    'csnp': {
                        'level-1': {
                            'rcvd': 0,
                            'sent': 0,
                        },
                        'level-2': {
                            'rcvd': 0,
                            'sent': 170,
                        },
                    },
                    'psnp': {
                        'level-1': {
                            'rcvd': 0,
                            'sent': 0,
                        },
                        'level-2': {
                            'rcvd': 0,
                            'sent': 0,
                        },
                    },
                    'dr_election': {
                        'level-1': 1,
                        'level-2': 2,
                    },
                    'spf_calculation': {
                        'level-1':  14,
                        'level-2':  17,
                    },
                    'partial_route_calculation': {
                        'level-1': 0,
                        'level-2': 1,
                    },
                    'lsp_checksum_errors_received': 0,
                    'update_process_queue_depth': '0/200',
                    'update_process_packets_dropped': 0
                }
            }
        }
    }


    golden_output = {'execute.return_value': '''\
    R2#show clns traffic
    CLNS:  Time since last clear: never
    CLNS & ESIS Output: 168, Input: 4021
    Dropped Protocol not enabled on interface: 0
    CLNS Local: 0, Forward: 0
    CLNS Discards:
      Hdr Syntax: 0, Checksum: 0, Lifetime: 0, Output cngstn: 0
      No Route: 0, Discard Route: 0, Dst Unreachable 0, Encaps. Failed: 0
      NLP Unknown: 0, Not an IS: 0
    CLNS Options: Packets 0, total 0 , bad 0, GQOS 0, cngstn exprncd 0
    CLNS Segments:  Segmented: 0, Failed: 0
    CLNS Broadcasts: sent: 0, rcvd: 0
    Echos: Rcvd 0 requests, 0 replies
          Sent 0 requests, 0 replies
    ESIS(sent/rcvd): ESHs: 0/0, ISHs: 168/0, RDs: 0/0, QCF: 0/0
    Tunneling (sent/rcvd): IP: 0/0, IPv6: 0/0
    Tunneling dropped (rcvd) IP/IPV6:  0
    ISO-IGRP: Querys (sent/rcvd): 0/0 Updates (sent/rcvd): 0/0
    ISO-IGRP: Router Hellos: (sent/rcvd): 0/0
    ISO-IGRP Syntax Errors: 0

    Tag VRF1:
    IS-IS: Time since last clear: never
    IS-IS: Level-1 Hellos (sent/rcvd): 497/533
    IS-IS: Level-2 Hellos (sent/rcvd): 843/611
    IS-IS: PTP Hellos     (sent/rcvd): 0/0
    IS-IS: Level-1 LSPs sourced (new/refresh): 3/4
    IS-IS: Level-2 LSPs sourced (new/refresh): 4/5
    IS-IS: Level-1 LSPs flooded (sent/rcvd): 0/0
    IS-IS: Level-2 LSPs flooded (sent/rcvd): 5/5
    IS-IS: LSP Retransmissions: 0
    IS-IS: Level-1 CSNPs (sent/rcvd): 0/0
    IS-IS: Level-2 CSNPs (sent/rcvd): 170/0
    IS-IS: Level-1 PSNPs (sent/rcvd): 0/0
    IS-IS: Level-2 PSNPs (sent/rcvd): 0/0
    IS-IS: Level-1 DR Elections: 1
    IS-IS: Level-2 DR Elections: 2
    IS-IS: Level-1 SPF Calculations: 14
    IS-IS: Level-2 SPF Calculations: 17
    IS-IS: Level-1 Partial Route Calculations: 0
    IS-IS: Level-2 Partial Route Calculations: 1
    IS-IS: LSP checksum errors received: 0
    IS-IS: Update process queue depth: 0/200
    IS-IS: Update process packets dropped: 0

    '''}

    def test_empty(self):
        self.device1 = Mock(**self.empty_output)
        obj = ShowClnsTraffic(device=self.device1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden_clns_protocol(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output)
        obj = ShowClnsTraffic(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)

if __name__ == '__main__':
    unittest.main()