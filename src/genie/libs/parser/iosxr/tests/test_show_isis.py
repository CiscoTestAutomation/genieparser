# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError, SchemaMissingKeyError

# iosxr show_mrib
from genie.libs.parser.iosxr.show_isis import ShowIsisAdjacency, \
                                              ShowIsisNeighbors, \
                                              ShowIsisSegmentRoutingLabelTable,\
                                              ShowIsisStatistics


# ==================================================
#  Unit test for 'show isis adjacency'
# ==================================================

class test_show_isis_adjacency(unittest.TestCase):
    '''Unit test for 'show isis adjacency'''

    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output1 = {
        'isis': {
            'p': {
                'vrf': {
                    'default': {
                        'level': {
                            'Level-1': {
                                'interfaces': {
                                    'PO0/1/0/1': {
                                        'system_id': {
                                            '12a4': {
                                                'interface': 'Port-channel0/1/0/1',
                                                'snpa': '*PtoP*',
                                                'state': 'Up',
                                                'hold': '23',
                                                'changed': '00:00:06',
                                                'nsf': 'Capable',
                                                'bfd': 'Init'}}},
                                    'Gi0/6/0/2': {
                                        'system_id': {
                                            '12a4': {
                                                'interface': 'GigabitEthernet0/6/0/2',
                                                'snpa': '0004.2893.f2f6',
                                                'state': 'Up',
                                                'hold': '56',
                                                'changed': '00:04:01',
                                                'nsf': 'Capable',
                                                'bfd': 'Up'}}}},
                                'total_adjacency_count': 2},
                            'Level-2': {
                                'interfaces': {
                                    'PO0/1/0/1': {
                                        'system_id': {
                                            '12a4': {
                                                'interface': 'Port-channel0/1/0/1',
                                                'snpa': '*PtoP*',
                                                'state': 'Up',
                                                'hold': '23',
                                                'changed': '00:00:06',
                                                'nsf': 'Capable',
                                                'bfd': 'None'}}},
                                    'Gi0/6/0/2': {
                                        'system_id': {
                                            '12a4': {
                                                'interface': 'GigabitEthernet0/6/0/2',
                                                'snpa': '0004.2893.f2f6',
                                                'state': 'Up',
                                                'hold': '26',
                                                'changed': '00:00:13',
                                                'nsf': 'Capable',
                                                'bfd': 'Init'}}}},
                                'total_adjacency_count': 2}}}}}}}

    golden_output1 = {'execute.return_value': '''
          IS-IS p Level-1 adjacencies:
          System Id      Interface        SNPA           State Hold     Changed  NSF      BFD
          12a4           PO0/1/0/1        *PtoP*         Up    23       00:00:06 Capable  Init
          12a4           Gi0/6/0/2        0004.2893.f2f6 Up    56       00:04:01 Capable  Up
          
          Total adjacency count: 2
          
          IS-IS p Level-2 adjacencies:
          System Id      Interface        SNPA           State Hold     Changed  NSF      BFD
          12a4           PO0/1/0/1        *PtoP*         Up    23       00:00:06 Capable  None
          12a4           Gi0/6/0/2        0004.2893.f2f6 Up    26       00:00:13 Capable  Init
          
          Total adjacency count: 2
    '''}

    golden_parsed_output2 = {
        'isis': {
            'test': {
                'vrf': {
                    'default': {
                        'level': {
                            'Level-1': {
                                'interfaces': {
                                    'Gi0/0/0/0.115': {
                                        'system_id': {
                                            'R1_xe': {
                                                'interface': 'GigabitEthernet0/0/0/0.115',
                                                'snpa': 'fa16.3eab.a39d',
                                                'state': 'Up',
                                                'hold': '23',
                                                'changed': '22:30:27',
                                                'nsf': 'Yes',
                                                'ipv4_bfd': 'None',
                                                'ipv6_bfd': 'None'}}},
                                    'Gi0/0/0/1.115': {
                                        'system_id': {
                                            'R3_nx': {
                                                'interface': 'GigabitEthernet0/0/0/1.115',
                                                'snpa': '5e00.4002.0007',
                                                'state': 'Up',
                                                'hold': '20',
                                                'changed': '22:30:27',
                                                'nsf': 'Yes',
                                                'ipv4_bfd': 'None',
                                                'ipv6_bfd': 'None'}}}},
                                'total_adjacency_count': 2},
                            'Level-2': {
                                'interfaces': {
                                    'Gi0/0/0/0.115': {
                                        'system_id': {
                                            'R1_xe': {
                                                'interface': 'GigabitEthernet0/0/0/0.115',
                                                'snpa': 'fa16.3eab.a39d',
                                                'state': 'Up',
                                                'hold': '26',
                                                'changed': '22:30:26',
                                                'nsf': 'Yes',
                                                'ipv4_bfd': 'None',
                                                'ipv6_bfd': 'None'}}},
                                    'Gi0/0/0/1.115': {
                                        'system_id': {
                                            'R3_nx': {
                                                'interface': 'GigabitEthernet0/0/0/1.115',
                                                'snpa': '5e00.4002.0007',
                                                'state': 'Up',
                                                'hold': '23',
                                                'changed': '22:30:27',
                                                'nsf': 'Yes',
                                                'ipv4_bfd': 'None',
                                                'ipv6_bfd': 'None'}}}},
                                'total_adjacency_count': 2}}}}},
            'test1': {
                'vrf': {
                    'default': {
                        'level': {
                            'Level-1': {},
                            'Level-2': {}}}}}}}



    golden_output2 = {'execute.return_value': '''
        +++ R2_xr: executing command 'show isis adjacency' +++
        show isis adjacency
        Wed Apr 17 16:25:06.870 UTC
        
        IS-IS test Level-1 adjacencies:
        System Id      Interface        SNPA           State Hold Changed  NSF IPv4 IPv6
                                                                               BFD  BFD
        R1_xe          Gi0/0/0/0.115    fa16.3eab.a39d Up    23   22:30:27 Yes None None
        R3_nx          Gi0/0/0/1.115    5e00.4002.0007 Up    20   22:30:27 Yes None None
        
        Total adjacency count: 2
        
        IS-IS test Level-2 adjacencies:
        System Id      Interface        SNPA           State Hold Changed  NSF IPv4 IPv6
                                                                               BFD  BFD
        R1_xe          Gi0/0/0/0.115    fa16.3eab.a39d Up    26   22:30:26 Yes None None
        R3_nx          Gi0/0/0/1.115    5e00.4002.0007 Up    23   22:30:27 Yes None None
        
        Total adjacency count: 2
        
        IS-IS test1 Level-1 adjacencies:
        System Id      Interface        SNPA           State Hold Changed  NSF IPv4 IPv6
                                                                       BFD  BFD

        IS-IS test1 Level-2 adjacencies:
        System Id      Interface        SNPA           State Hold Changed  NSF IPv4 IPv6
                                                                       BFD  BFD
    '''}

    def test_show_isis_adjacency_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowIsisAdjacency(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_show_isis_adjacency_golden1(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output1)
        obj = ShowIsisAdjacency(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output1)

    def test_show_isis_adjacency_golden2(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output2)
        obj = ShowIsisAdjacency(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output2)


# ====================================
#  Unit test for 'show isis neighbors'
# ====================================

class test_show_isis_neighbors(unittest.TestCase):
    '''Unit test for "show isis neighbors"'''

    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output1 = {
        'isis': {
            'test': {
                'vrf': {
                    'default': {
                        'interfaces': {
                            'GigabitEthernet0/0/0/0.115': {
                                'neighbors': {
                                    'R1_xe': {
                                        'snpa': 'fa16.3eab.a39d',
                                        'state': 'Up',
                                        'holdtime': '24',
                                        'type': 'L1L2',
                                        'ietf_nsf': 'Capable'}}},
                            'GigabitEthernet0/0/0/1.115': {
                                'neighbors': {
                                    'R3_nx': {
                                        'snpa': '5e00.4002.0007',
                                        'state': 'Up',
                                        'holdtime': '25',
                                        'type': 'L1L2',
                                        'ietf_nsf': 'Capable'}}}},
                        'total_neighbor_count': 2}}}}}

    golden_output1 = {'execute.return_value': '''
        +++ R2_xr: executing command 'show isis neighbors' +++
        show isis neighbors
        Wed Apr 17 16:21:30.075 UTC

        IS-IS test neighbors:
        System Id      Interface        SNPA           State Holdtime Type IETF-NSF
        R1_xe          Gi0/0/0/0.115    fa16.3eab.a39d Up    24       L1L2 Capable
        R3_nx          Gi0/0/0/1.115    5e00.4002.0007 Up    25       L1L2 Capable
        
        Total neighbor count: 2
    '''}

    golden_parsed_output2 = {
        'isis': {
            'test': {
                'vrf': {
                    'default': {
                        'interfaces': {
                            'GigabitEthernet0/0/0/0.115': {
                                'neighbors': {
                                    'R1_xe': {
                                        'snpa': 'fa16.3eab.a39d',
                                        'state': 'Up',
                                        'holdtime': '22',
                                        'type': 'L1L2',
                                        'ietf_nsf': 'Capable'}}},
                            'GigabitEthernet0/0/0/1.115': {
                                'neighbors': {
                                    'R3_nx': {
                                        'snpa': '5e00.4002.0007',
                                        'state': 'Up',
                                        'holdtime': '22',
                                        'type': 'L1L2',
                                        'ietf_nsf': 'Capable'}}}},
                        'total_neighbor_count': 2}}},
            'test1': {
                'vrf': {
                    'default': {}}}}}

    golden_output2 = {'execute.return_value': '''
        show isis neighbors
        Thu Apr 18 11:00:22.192 UTC
        
        IS-IS test neighbors:
        System Id      Interface        SNPA           State Holdtime Type IETF-NSF
        R1_xe          Gi0/0/0/0.115    fa16.3eab.a39d Up    22       L1L2 Capable
        R3_nx          Gi0/0/0/1.115    5e00.4002.0007 Up    22       L1L2 Capable
        
        Total neighbor count: 2
        
        IS-IS test1 neighbors:
        System Id      Interface        SNPA           State Holdtime Type IETF-NSF
    '''}

    def test_show_isis_neighbors_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowIsisNeighbors(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_show_isis_neighbors_golden1(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output1)
        obj = ShowIsisNeighbors(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output1)

    def test_show_isis_neighbors_golden2(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output2)
        obj = ShowIsisNeighbors(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output2)


# ======================================================
#  Unit test for 'show isis segment-routing label table'
# ======================================================

class test_show_isis_segment_routing_label_table(unittest.TestCase):
    '''Unit test for "show isis segment-routing label table"'''

    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output1 = {
        'instance': {
            'SR': {
                'label': {
                    16001: {
                        'prefix_interface': 'Loopback0'},
                    16002: {
                        'prefix_interface': '10.2.2.2/32'},
                    16003: {
                        'prefix_interface': '10.3.3.3/32'}
                }
            }
        }
    }

    golden_output1 = {'execute.return_value': '''
        RP/0/RP0/CPU0:iosxrv9000-1#show isis segment-routing label table 
        Mon Sep 30 13:22:32.921 EDT
            
        IS-IS SR IS Label Table
        Label         Prefix/Interface
        ----------    ----------------
        16001         Loopback0
        16002         10.2.2.2/32
        16003         10.3.3.3/32
    '''}

    def test_show_isis_segment_routing_label_table_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowIsisSegmentRoutingLabelTable(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_show_isis_segment_routing_label_table_golden1(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output1)
        obj = ShowIsisSegmentRoutingLabelTable(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output1)


class TestShowIsisStatistics(unittest.TestCase):
    maxDiff = None

    empty_output = {'execute.return_value': ''}

    parsed_output_1 = {
        "isis": {
            "test": {
                "psnp_cache": {
                    "hits": 21, 
                    "tries": 118},
                "csnp_cache": {
                    "hits": 1398, 
                    "tries": 1501, 
                    "updates": 204},
                "lsp": {
                    "checksum_errors_received": 0, 
                    "dropped": 0},
                "snp": {
                    "dropped": 0},
                "upd": {
                    "max_queue_size": 3, 
                    "queue_size": 0},
                "transmit_time": {
                    "hello": {
                        "average_transmit_time_sec": 0,
                        "average_transmit_time_nsec": 66473,
                        "rate_per_sec": 15,
                    },
                    "csnp": {
                        "average_transmit_time_sec": 0,
                        "average_transmit_time_nsec": 45979,
                        "rate_per_sec": 2,
                    },
                    "psnp": {
                        "average_transmit_time_sec": 0,
                        "average_transmit_time_nsec": 4113,
                        "rate_per_sec": 0,
                    },
                    "lsp": {
                        "average_transmit_time_sec": 0,
                        "average_transmit_time_nsec": 14392,
                        "rate_per_sec": 0,
                    },
                },
                "process_time": {
                    "hello": {
                        "average_process_time_sec": 0,
                        "average_process_time_nsec": 51163,
                        "rate_per_sec": 9,
                    },
                    "csnp": {
                        "average_process_time_sec": 0,
                        "average_process_time_nsec": 26914,
                        "rate_per_sec": 1,
                    },
                    "psnp": {
                        "average_process_time_sec": 0,
                        "average_process_time_nsec": 39758,
                        "rate_per_sec": 0,
                    },
                    "lsp": {
                        "average_process_time_sec": 0,
                        "average_process_time_nsec": 52706,
                        "rate_per_sec": 0,
                    },
                },
                "level": {
                    1: {
                        "lsp": {
                            "new": 11, 
                            "refresh": 15},
                        "address_family": {
                            "IPv4 Unicast": {
                                "total_spf_calculation": 18,
                                "full_spf_calculation": 16,
                                "ispf_calculation": 0,
                                "next_hop_calculation": 0,
                                "partial_route_calculation": 2,
                                "periodic_spf_calculation": 3,
                            },
                            "IPv6 Unicast": {
                                "total_spf_calculation": 19,
                                "full_spf_calculation": 17,
                                "ispf_calculation": 0,
                                "next_hop_calculation": 0,
                                "partial_route_calculation": 2,
                                "periodic_spf_calculation": 3,
                            },
                        },
                    },
                    2: {
                        "lsp": {
                            "new": 13, 
                            "refresh": 11},
                        "address_family": {
                            "IPv4 Unicast": {
                                "total_spf_calculation": 23,
                                "full_spf_calculation": 15,
                                "ispf_calculation": 0,
                                "next_hop_calculation": 0,
                                "partial_route_calculation": 8,
                                "periodic_spf_calculation": 4,
                            },
                            "IPv6 Unicast": {
                                "total_spf_calculation": 22,
                                "full_spf_calculation": 14,
                                "ispf_calculation": 0,
                                "next_hop_calculation": 0,
                                "partial_route_calculation": 8,
                                "periodic_spf_calculation": 4,
                            },
                        },
                    },
                },
                "interface": {
                    "Loopback0": {
                        "level": {
                            1: {
                                "lsps_sourced": {
                                    "sent": 0,
                                    "received": 0,
                                    "flooding_duplicates": 51,
                                    "arrival_time_throttled": 0,
                                },
                                "csnp": {
                                    "sent": 0, 
                                    "received": 0},
                                "psnp": {
                                    "sent": 0, 
                                    "received": 0},
                            },
                            2: {
                                "lsps_sourced": {
                                    "sent": 0,
                                    "received": 0,
                                    "flooding_duplicates": 46,
                                    "arrival_time_throttled": 0,
                                },
                                "csnp": {
                                    "sent": 0, 
                                    "received": 0},
                                "psnp": {
                                    "sent": 0, 
                                    "received": 0},
                            },
                        }
                    },
                    "GigabitEthernet0/0/0/0": {
                        "level": {
                            1: {
                                "hello": {
                                    "received": 594, 
                                    "sent": 593},
                                "dr": {
                                    "elections": 1},
                                "lsps_sourced": {
                                    "sent": 0,
                                    "received": 0,
                                    "flooding_duplicates": 51,
                                    "arrival_time_throttled": 0,
                                },
                                "csnp": {
                                    "sent": 0, 
                                    "received": 0},
                                "psnp": {
                                    "sent": 0, 
                                    "received": 0},
                            },
                            2: {
                                "hello": {
                                    "received": 1779, 
                                    "sent": 594},
                                "dr": {
                                    "elections": 1},
                                "lsps_sourced": {
                                    "sent": 63,
                                    "received": 7,
                                    "flooding_duplicates": 0,
                                    "arrival_time_throttled": 0,
                                },
                                "csnp": {
                                    "sent": 595, 
                                    "received": 0},
                                "psnp": {
                                    "sent": 0, 
                                    "received": 0},
                            },
                        }
                    },
                    "GigabitEthernet0/0/0/1": {
                        "level": {
                            1: {
                                "hello": {
                                    "received": 1294, 
                                    "sent": 604},
                                "dr": {
                                    "elections": 5},
                                "lsps_sourced": {
                                    "sent": 47,
                                    "received": 15,
                                    "flooding_duplicates": 8,
                                    "arrival_time_throttled": 0,
                                },
                                "csnp": {
                                    "sent": 339, 
                                    "received": 0},
                                "psnp": {
                                    "sent": 0, 
                                    "received": 1},
                            },
                            2: {
                                "hello": {
                                    "received": 724, 
                                    "sent": 281},
                                "dr": {
                                    "elections": 5},
                                "lsps_sourced": {
                                    "sent": 0,
                                    "received": 0,
                                    "flooding_duplicates": 42,
                                    "arrival_time_throttled": 0,
                                },
                                "csnp": {
                                    "sent": 0, 
                                    "received": 0},
                                "psnp": {
                                    "sent": 0, 
                                    "received": 0},
                            },
                        }
                    },
                    "GigabitEthernet0/0/0/2": {
                        "level": {
                            1: {
                                "hello": {
                                    "received": 1739, 
                                    "sent": 572},
                                "dr": {
                                    "elections": 3},
                                "lsps_sourced": {
                                    "sent": 51,
                                    "received": 31,
                                    "flooding_duplicates": 0,
                                    "arrival_time_throttled": 0,
                                },
                                "csnp": {
                                    "sent": 567, 
                                    "received": 0},
                                "psnp": {
                                    "sent": 0, 
                                    "received": 0},
                            },
                            2: {
                                "hello": {
                                    "received": 597, 
                                    "sent": 0},
                                "dr": {
                                    "elections": 1},
                                "lsps_sourced": {
                                    "sent": 0,
                                    "received": 0,
                                    "flooding_duplicates": 46,
                                    "arrival_time_throttled": 0,
                                },
                                "csnp": {
                                    "sent": 0, 
                                    "received": 0},
                                "psnp": {
                                    "sent": 0, 
                                    "received": 0},
                            },
                        }
                    },
                    "GigabitEthernet0/0/0/3": {
                        "level": {
                            1: {
                                "hello": {
                                    "received": 598, 
                                    "sent": 1115},
                                "dr": {
                                    "elections": 3},
                                "lsps_sourced": {
                                    "sent": 38,
                                    "received": 26,
                                    "flooding_duplicates": 5,
                                    "arrival_time_throttled": 0,
                                },
                                "csnp": {
                                    "sent": 0, 
                                    "received": 370},
                                "psnp": {
                                    "sent": 0, 
                                    "received": 0},
                            },
                            2: {
                                "hello": {
                                    "received": 596, 
                                    "sent": 1113},
                                "dr": {
                                    "elections": 3},
                                "lsps_sourced": {
                                    "sent": 18,
                                    "received": 39,
                                    "flooding_duplicates": 3,
                                    "arrival_time_throttled": 0,
                                },
                                "csnp": {
                                    "sent": 0, 
                                    "received": 370},
                                "psnp": {
                                    "sent": 0, 
                                    "received": 0},
                            },
                        }
                    },
                },
            }
        }
    }



    golden_output_1 = {'execute.return_value': '''
        IS-IS test statistics:
            Fast PSNP cache (hits/tries): 21/118
            Fast CSNP cache (hits/tries): 1398/1501
            Fast CSNP cache updates: 204
            LSP checksum errors received: 0
            LSP Dropped: 0
            SNP Dropped: 0
            UPD Max Queue size: 3
            UPD Queue size: 0
            Average transmit times and rate:
              Hello:          0 s,      66473 ns,         15/s
              CSNP:           0 s,      45979 ns,          2/s
              PSNP:           0 s,       4113 ns,          0/s
              LSP:            0 s,      14392 ns,          0/s
            Average process times and rate:
              Hello:          0 s,      51163 ns,          9/s
              CSNP:           0 s,      26914 ns,          1/s
              PSNP:           0 s,      39758 ns,          0/s
              LSP:            0 s,      52706 ns,          0/s
            Level-1:
              LSPs sourced (new/refresh): 11/15
              IPv4 Unicast
                Total SPF calculations     : 18
                Full SPF calculations      : 16
                ISPF calculations          : 0
                Next Hop Calculations      : 0
                Partial Route Calculations : 2
                Periodic SPF calculations  : 3
              IPv6 Unicast
                Total SPF calculations     : 19
                Full SPF calculations      : 17
                ISPF calculations          : 0
                Next Hop Calculations      : 0
                Partial Route Calculations : 2
                Periodic SPF calculations  : 3
            Level-2:
              LSPs sourced (new/refresh): 13/11
              IPv4 Unicast
                Total SPF calculations     : 23
                Full SPF calculations      : 15
                ISPF calculations          : 0
                Next Hop Calculations      : 0
                Partial Route Calculations : 8
                Periodic SPF calculations  : 4
              IPv6 Unicast
                Total SPF calculations     : 22
                Full SPF calculations      : 14
                ISPF calculations          : 0
                Next Hop Calculations      : 0
                Partial Route Calculations : 8
                Periodic SPF calculations  : 4
          Interface Loopback0:
            Level-1 LSPs (sent/rcvd)  : 0/0
            Level-1 CSNPs (sent/rcvd) : 0/0
            Level-1 PSNPs (sent/rcvd) : 0/0
            Level-1 LSP Flooding Duplicates     : 51
            Level-1 LSPs Arrival Time Throttled : 0
            Level-2 LSPs (sent/rcvd)  : 0/0
            Level-2 CSNPs (sent/rcvd) : 0/0
            Level-2 PSNPs (sent/rcvd) : 0/0
            Level-2 LSP Flooding Duplicates     : 46
            Level-2 LSPs Arrival Time Throttled : 0
          Interface GigabitEthernet0/0/0/0:
            Level-1 Hellos (sent/rcvd): 594/593
            Level-1 DR Elections      : 1
            Level-1 LSPs (sent/rcvd)  : 0/0
            Level-1 CSNPs (sent/rcvd) : 0/0
            Level-1 PSNPs (sent/rcvd) : 0/0
            Level-1 LSP Flooding Duplicates     : 51
            Level-1 LSPs Arrival Time Throttled : 0
            Level-2 Hellos (sent/rcvd): 1779/594
            Level-2 DR Elections      : 1
            Level-2 LSPs (sent/rcvd)  : 63/7
            Level-2 CSNPs (sent/rcvd) : 595/0
            Level-2 PSNPs (sent/rcvd) : 0/0
            Level-2 LSP Flooding Duplicates     : 0
            Level-2 LSPs Arrival Time Throttled : 0
          Interface GigabitEthernet0/0/0/1:
            Level-1 Hellos (sent/rcvd): 1294/604
            Level-1 DR Elections      : 5
            Level-1 LSPs (sent/rcvd)  : 47/15
            Level-1 CSNPs (sent/rcvd) : 339/0
            Level-1 PSNPs (sent/rcvd) : 0/1
            Level-1 LSP Flooding Duplicates     : 8
            Level-1 LSPs Arrival Time Throttled : 0
            Level-2 Hellos (sent/rcvd): 724/281
            Level-2 DR Elections      : 5
            Level-2 LSPs (sent/rcvd)  : 0/0
            Level-2 CSNPs (sent/rcvd) : 0/0
            Level-2 PSNPs (sent/rcvd) : 0/0
            Level-2 LSP Flooding Duplicates     : 42
            Level-2 LSPs Arrival Time Throttled : 0
          Interface GigabitEthernet0/0/0/2:
            Level-1 Hellos (sent/rcvd): 1739/572
            Level-1 DR Elections      : 3
            Level-1 LSPs (sent/rcvd)  : 51/31
            Level-1 CSNPs (sent/rcvd) : 567/0
            Level-1 PSNPs (sent/rcvd) : 0/0
            Level-1 LSP Flooding Duplicates     : 0
            Level-1 LSPs Arrival Time Throttled : 0
            Level-2 Hellos (sent/rcvd): 597/0
            Level-2 DR Elections      : 1
            Level-2 LSPs (sent/rcvd)  : 0/0
            Level-2 CSNPs (sent/rcvd) : 0/0
            Level-2 PSNPs (sent/rcvd) : 0/0
            Level-2 LSP Flooding Duplicates     : 46
            Level-2 LSPs Arrival Time Throttled : 0
          Interface GigabitEthernet0/0/0/3:
            Level-1 Hellos (sent/rcvd): 598/1115
            Level-1 DR Elections      : 3
            Level-1 LSPs (sent/rcvd)  : 38/26
            Level-1 CSNPs (sent/rcvd) : 0/370
            Level-1 PSNPs (sent/rcvd) : 0/0
            Level-1 LSP Flooding Duplicates     : 5
            Level-1 LSPs Arrival Time Throttled : 0
            Level-2 Hellos (sent/rcvd): 596/1113
            Level-2 DR Elections      : 3
            Level-2 LSPs (sent/rcvd)  : 18/39
            Level-2 CSNPs (sent/rcvd) : 0/370
            Level-2 PSNPs (sent/rcvd) : 0/0
            Level-2 LSP Flooding Duplicates     : 3
            Level-2 LSPs Arrival Time Throttled : 0
    '''}

    def test_empty_output(self):
        self.device = Mock(**self.empty_output)
        obj = ShowIsisStatistics(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            obj.parse()
    
    def test_golden_output_1(self):
        self.device = Mock(**self.golden_output_1)
        obj = ShowIsisStatistics(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.parsed_output_1)

if __name__ == '__main__':
    unittest.main()
