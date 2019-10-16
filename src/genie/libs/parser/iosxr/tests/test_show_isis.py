# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError, SchemaMissingKeyError

# iosxr show_mrib
from genie.libs.parser.iosxr.show_isis import (ShowIsis,
                                               ShowIsisAdjacency, 
                                               ShowIsisNeighbors,
                                               ShowIsisDatabaseDetail,
                                               ShowIsisSegmentRoutingLabelTable)


# ==================================================
#  Unit test for 'show isis adjacency'
# ==================================================

class TestShowIsisAdjacency(unittest.TestCase):
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

class TestShowIsisNeighbors(unittest.TestCase):
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

class TestShowIsisSegmentRoutingLabelTable(unittest.TestCase):
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

class TestShowIsis(unittest.TestCase):
    ''' Unitest for commands:
        * show isis -> ShowIsis
    '''

    maxDiff = None

    empty_output = {'execute.return_value': ''}

    golden_parsed_output_1 = {
        "instance": {
            "test": {
                "process_id": "test",
                "instance": "0",
                "vrf": {
                    "default": {
                        "system_id": "3333.3333.3333",
                        "is_levels": "level-1-2",
                        "manual_area_address": ["49.0002"],
                        "routing_area_address": ["49.0002", "49.0001"],
                        "non_stop_forwarding": "Disabled",
                        "most_recent_startup_mode": "Cold Restart",
                        "te_connection_status": "Down",
                        "topology": {
                            "IPv4 Unicast": {
                                "level": {
                                    1: {
                                        "generate_style": "Wide",
                                        "accept_style": "Wide",
                                        "metric": 10,
                                        "ispf_status": "Disabled",
                                    },
                                    2: {
                                        "generate_style": "Wide",
                                        "accept_style": "Wide",
                                        "metric": 10,
                                        "ispf_status": "Disabled",
                                    },
                                },
                                "protocols_redistributed": False,
                                "distance": 115,
                                "adv_passive_only": False,
                            },
                            "IPv6 Unicast": {
                                "level": {
                                    1: {
                                        "metric": 10, 
                                        "ispf_status": "Disabled"},
                                    2: {
                                        "metric": 10, 
                                        "ispf_status": "Disabled"},
                                },
                                "protocols_redistributed": False,
                                "distance": 115,
                                "adv_passive_only": False,
                            },
                        },
                        "srlb": "not allocated",
                        "srgb": "not allocated",
                        "interfaces": {
                            "Loopback0": {
                                "running_state": "running actively",
                                "configuration_state": "active in configuration",
                            },
                            "GigabitEthernet0/0/0/0": {
                                "running_state": "running actively",
                                "configuration_state": "active in configuration",
                            },
                            "GigabitEthernet0/0/0/1": {
                                "running_state": "running actively",
                                "configuration_state": "active in configuration",
                            },
                            "GigabitEthernet0/0/0/2": {
                                "running_state": "running actively",
                                "configuration_state": "active in configuration",
                            },
                            "GigabitEthernet0/0/0/3": {
                                "running_state": "running actively",
                                "configuration_state": "active in configuration",
                            },
                        },
                    }
                },
            }
        }
    }

    golden_output_1 = {'execute.return_value': '''
        IS-IS Router: test
          System Id: 3333.3333.3333
          Instance Id: 0
          IS Levels: level-1-2
          Manual area address(es):
            49.0002
          Routing for area address(es):
            49.0002
            49.0001
          Non-stop forwarding: Disabled
          Most recent startup mode: Cold Restart
          TE connection status: Down
          Topologies supported by IS-IS:
            IPv4 Unicast
              Level-1
                Metric style (generate/accept): Wide/Wide
                Metric: 10
                ISPF status: Disabled
              Level-2
                Metric style (generate/accept): Wide/Wide
                Metric: 10
                ISPF status: Disabled
              No protocols redistributed
              Distance: 115
              Advertise Passive Interface Prefixes Only: No
            IPv6 Unicast
              Level-1
                Metric: 10
                ISPF status: Disabled
              Level-2
                Metric: 10
                ISPF status: Disabled
              No protocols redistributed
              Distance: 115
              Advertise Passive Interface Prefixes Only: No
          SRLB not allocated
          SRGB not allocated
          Interfaces supported by IS-IS:
            Loopback0 is running actively (active in configuration)
            GigabitEthernet0/0/0/0 is running actively (active in configuration)
            GigabitEthernet0/0/0/1 is running actively (active in configuration)
            GigabitEthernet0/0/0/2 is running actively (active in configuration)
            GigabitEthernet0/0/0/3 is running actively (active in configuration)
    '''}

    def test_show_isis_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowIsis(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_show_isis_1(self):
        self.device = Mock(**self.golden_output_1)
        obj = ShowIsis(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_1)

class TestShowIsisDatabaseDetail(unittest.TestCase):
    ''' Unit tests for commands/parser:
        * show isis database detail / ShowIsisDatabaseDetail
    ''' 
    maxDiff = None

    empty_output = {'execute.return_value': ''}

    golden_parsed_output_1 = {
        "instance": {
            "test": {
                "level": {
                    1: {
                        "lspid": {
                            "R3.00-00": {
                                "lsp": {
                                    "seq_num": "0x0000000d",
                                    "checksum": "0x0476",
                                    "local_router": True,
                                    "holdtime": 578,
                                    "attach_bit": 1,
                                    "p_bit": 0,
                                    "overload_bit": 0,
                                },
                                "area_address": "49.0002",
                                "nlpid": ["0xcc", "0x8e"],
                                "ip_address": "3.3.3.3",
                                "extended_ipv4_reachability": {
                                    "3.3.3.0/24": {
                                        "ip_prefix": "3.3.3.0",
                                        "prefix_length": "24",
                                        "metric": 10,
                                    },
                                    "10.2.3.0/24": {
                                        "ip_prefix": "10.2.3.0",
                                        "prefix_length": "24",
                                        "metric": 10,
                                    },
                                },
                                "hostname": "R3",
                                "ipv6_address": "2001:db8:3:3:3::3",
                                "mt_ipv6_reachability": {
                                    "2001:db8:3:3:3::3/128": {
                                        "ip_prefix": "2001:db8:3:3:3::3",
                                        "prefix_length": "128",
                                        "metric": 10,
                                    },
                                    "2001:db8:10:2::/64": {
                                        "ip_prefix": "2001:db8:10:2::",
                                        "prefix_length": "64",
                                        "metric": 10,
                                    },
                                },
                                "mt_entries": {
                                    "Standard (IPv4 Unicast)": {},
                                    "IPv6 Unicast": {
                                        "attach_bit": 1,
                                        "p_bit": 0,
                                        "overload_bit": 0,
                                    },
                                },
                                "extended_is_neighbor": {
                                    "R3.03": {"metric": 10},
                                    "R5.01": {"metric": 10},
                                },
                                "mt_is_neighbor": {
                                    "R3.03": {
                                        "metric": 10, 
                                        "mt_id": "MT (IPv6 Unicast)"},
                                    "R5.01": {
                                        "metric": 10, 
                                        "mt_id": "MT (IPv6 Unicast)"},
                                },
                            },
                            "R3.03-00": {
                                "lsp": {
                                    "seq_num": "0x00000007",
                                    "checksum": "0x8145",
                                    "local_router": False,
                                    "holdtime": 988,
                                    "attach_bit": 0,
                                    "p_bit": 0,
                                    "overload_bit": 0,
                                },
                                "extended_is_neighbor": {
                                    "R3.00": {
                                        "metric": 0},
                                    "R4.00": {
                                        "metric": 0},
                                },
                            },
                            "R3.05-00": {
                                "lsp": {
                                    "seq_num": "0x00000004",
                                    "checksum": "0x7981",
                                    "local_router": False,
                                    "holdtime": 600,
                                    "attach_bit": 0,
                                    "p_bit": 0,
                                    "overload_bit": 0,
                                },
                                "extended_is_neighbor": {
                                    "R3.00": {
                                        "metric": 0},
                                    "R6.00": {
                                        "metric": 0},
                                },
                            },
                            "R4.00-00": {
                                "lsp": {
                                    "seq_num": "0x0000000c",
                                    "checksum": "0x5c39",
                                    "local_router": False,
                                    "holdtime": 1115,
                                    "received": 1200,
                                    "attach_bit": 0,
                                    "p_bit": 0,
                                    "overload_bit": 0,
                                },
                                "area_address": "49.0002",
                                "extended_is_neighbor": {
                                    "R3.03": {
                                        "metric": 10},
                                    "R4.01": {
                                        "metric": 10},
                                },
                                "nlpid": ["0xcc", "0x8e"],
                                "ip_address": "4.4.4.4",
                                "extended_ipv4_reachability": {
                                    "4.4.4.4/32": {
                                        "ip_prefix": "4.4.4.4",
                                        "prefix_length": "32",
                                        "metric": 10,
                                    },
                                    "10.3.4.0/24": {
                                        "ip_prefix": "10.3.4.0",
                                        "prefix_length": "24",
                                        "metric": 10,
                                    },
                                },
                                "hostname": "R4",
                                "mt_is_neighbor": {
                                    "R3.03": {
                                        "metric": 10, 
                                        "mt_id": "MT (IPv6 Unicast)"},
                                    "R4.01": {
                                        "metric": 10, 
                                        "mt_id": "MT (IPv6 Unicast)"},
                                },
                                "ipv6_address": "2001:db8:4:4:4::4",
                                "mt_ipv6_reachability": {
                                    "2001:db8:4:4:4::4/128": {
                                        "ip_prefix": "2001:db8:4:4:4::4",
                                        "prefix_length": "128",
                                        "metric": 10,
                                    },
                                    "2001:db8:10:3::/64": {
                                        "ip_prefix": "2001:db8:10:3::",
                                        "prefix_length": "64",
                                        "metric": 10,
                                    },
                                },
                                "mt_entries": {
                                    "Standard (IPv4 Unicast)": {},
                                    "IPv6 Unicast": {
                                        "attach_bit": 0,
                                        "p_bit": 0,
                                        "overload_bit": 0,
                                    },
                                },
                            },
                            "R4.01-00": {
                                "lsp": {
                                    "seq_num": "0x00000004",
                                    "checksum": "0xf9a0",
                                    "local_router": False,
                                    "holdtime": 616,
                                    "received": 1200,
                                    "attach_bit": 0,
                                    "p_bit": 0,
                                    "overload_bit": 0,
                                },
                                "extended_is_neighbor": {
                                    "R4.00": {
                                        "metric": 0},
                                    "R5.00": {
                                        "metric": 0},
                                },
                            },
                            "R5.00-00": {
                                "lsp": {
                                    "seq_num": "0x00000009",
                                    "checksum": "0x09f9",
                                    "local_router": False,
                                    "holdtime": 980,
                                    "received": 1199,
                                    "attach_bit": 1,
                                    "p_bit": 0,
                                    "overload_bit": 0,
                                },
                                "area_address": "49.0002",
                                "nlpid": ["0xcc", "0x8e"],
                                "mt_entries": {
                                    "Standard (IPv4 Unicast)": {},
                                    "IPv6 Unicast": {
                                        "attach_bit": 1,
                                        "p_bit": 0,
                                        "overload_bit": 0,
                                    },
                                },
                                "hostname": "R5",
                                "extended_is_neighbor": {
                                    "R5.01": {
                                        "metric": 10},
                                    "R4.01": {
                                        "metric": 10},
                                },
                                "mt_is_neighbor": {
                                    "R5.01": {
                                        "metric": 10, 
                                        "mt_id": "MT (IPv6 Unicast)"},
                                    "R4.01": {
                                        "metric": 10, 
                                        "mt_id": "MT (IPv6 Unicast)"},
                                },
                                "ip_address": "5.5.5.5",
                                "extended_ipv4_reachability": {
                                    "5.5.5.5/32": {
                                        "ip_prefix": "5.5.5.5",
                                        "prefix_length": "32",
                                        "metric": 10,
                                    },
                                    "10.3.5.0/24": {
                                        "ip_prefix": "10.3.5.0",
                                        "prefix_length": "24",
                                        "metric": 10,
                                    },
                                },
                                "ipv6_address": "2001:db8:5:5:5::5",
                                "mt_ipv6_reachability": {
                                    "2001:db8:5:5:5::5/128": {
                                        "ip_prefix": "2001:db8:5:5:5::5",
                                        "prefix_length": "128",
                                        "metric": 10,
                                    },
                                    "2001:db8:10:3::/64": {
                                        "ip_prefix": "2001:db8:10:3::",
                                        "prefix_length": "64",
                                        "metric": 10,
                                    },
                                },
                            },
                            "R5.01-00": {
                                "lsp": {
                                    "seq_num": "0x00000004",
                                    "checksum": "0x4ac5",
                                    "local_router": False,
                                    "holdtime": 521,
                                    "received": 1199,
                                    "attach_bit": 0,
                                    "p_bit": 0,
                                    "overload_bit": 0,
                                },
                                "extended_is_neighbor": {
                                    "R5.00": {
                                        "metric": 0},
                                    "R3.00": {
                                        "metric": 0},
                                },
                            },
                            "R5.03-00": {
                                "lsp": {
                                    "seq_num": "0x00000004",
                                    "checksum": "0x3c38",
                                    "local_router": False,
                                    "holdtime": 1023,
                                    "received": 1199,
                                    "attach_bit": 0,
                                    "p_bit": 0,
                                    "overload_bit": 0,
                                },
                                "extended_is_neighbor": {
                                    "R5.00": {
                                        "metric": 0},
                                    "R7.00": {
                                        "metric": 0},
                                },
                            },
                            "R6.00-00": {
                                "lsp": {
                                    "seq_num": "0x00000008",
                                    "checksum": "0x1869",
                                    "local_router": False,
                                    "holdtime": 923,
                                    "received": 1199,
                                    "attach_bit": 0,
                                    "p_bit": 0,
                                    "overload_bit": 0,
                                },
                                "area_address": "49.0002",
                                "nlpid": ["0xcc", "0x8e"],
                                "router_id": "6.6.6.6",
                                "ip_address": "6.6.6.6",
                                "mt_entries": {
                                    "IPv6 Unicast": {
                                        "attach_bit": 0,
                                        "p_bit": 0,
                                        "overload_bit": 0,
                                    },
                                    "Standard (IPv4 Unicast)": {},
                                },
                                "hostname": "R6",
                                "mt_is_neighbor": {
                                    "R7.02": {
                                        "metric": 40, 
                                        "mt_id": "MT (IPv6 Unicast)"},
                                    "R3.05": {
                                        "metric": 40, 
                                        "mt_id": "MT (IPv6 Unicast)"},
                                },
                                "extended_is_neighbor": {
                                    "R7.02": {
                                        "metric": 40},
                                    "R3.05": {
                                        "metric": 40},
                                },
                                "extended_ipv4_reachability": {
                                    "6.6.6.0/24": {
                                        "ip_prefix": "6.6.6.0",
                                        "prefix_length": "24",
                                        "metric": 1,
                                    },
                                    "10.6.7.0/24": {
                                        "ip_prefix": "10.6.7.0",
                                        "prefix_length": "24",
                                        "metric": 40,
                                    },
                                    "10.3.6.0/24": {
                                        "ip_prefix": "10.3.6.0",
                                        "prefix_length": "24",
                                        "metric": 40,
                                    },
                                },
                                "mt_ipv6_reachability": {
                                    "2001:db8:6:6:6::6/128": {
                                        "ip_prefix": "2001:db8:6:6:6::6",
                                        "prefix_length": "128",
                                        "metric": 1,
                                    },
                                    "2001:db8:10:6::/64": {
                                        "ip_prefix": "2001:db8:10:6::",
                                        "prefix_length": "64",
                                        "metric": 40,
                                    },
                                },
                            },
                            "R7.00-00": {
                                "lsp": {
                                    "seq_num": "0x00000008",
                                    "checksum": "0xaba8",
                                    "local_router": False,
                                    "holdtime": 965,
                                    "received": 1198,
                                    "attach_bit": 1,
                                    "p_bit": 0,
                                    "overload_bit": 0,
                                },
                                "area_address": "49.0002",
                                "nlpid": ["0xcc", "0x8e"],
                                "router_id": "7.7.7.7",
                                "ip_address": "7.7.7.7",
                                "mt_entries": {
                                    "IPv6 Unicast": {
                                        "attach_bit": 0,
                                        "p_bit": 0,
                                        "overload_bit": 0,
                                    },
                                    "Standard (IPv4 Unicast)": {},
                                },
                                "hostname": "R7",
                                "mt_is_neighbor": {
                                    "R7.02": {
                                        "metric": 40, 
                                        "mt_id": "MT (IPv6 Unicast)"},
                                    "R5.03": {
                                        "metric": 40, 
                                        "mt_id": "MT (IPv6 Unicast)"},
                                },
                                "extended_is_neighbor": {
                                    "R7.02": {
                                        "metric": 40},
                                    "R5.03": {
                                        "metric": 40},
                                },
                                "ip_interarea": {
                                    "10.7.8.0/24": {
                                        "address_family": {
                                            "ipv4 unicast": {
                                                "metric": 40},
                                            "IPv6 Unicast": {
                                                "metric": 40},
                                        }
                                    }
                                },
                                "extended_ipv4_reachability": {
                                    "7.7.7.7/32": {
                                        "ip_prefix": "7.7.7.7",
                                        "prefix_length": "32",
                                        "metric": 1,
                                    },
                                    "10.7.9.0/24": {
                                        "ip_prefix": "10.7.9.0",
                                        "prefix_length": "24",
                                        "metric": 40,
                                    },
                                },
                                "mt_ipv6_reachability": {
                                    "2001:db8:7:7:7::7/128": {
                                        "ip_prefix": "2001:db8:7:7:7::7",
                                        "prefix_length": "128",
                                        "metric": 1,
                                    }
                                },
                            },
                            "R7.02-00": {
                                "lsp": {
                                    "seq_num": "0x00000005",
                                    "checksum": "0x8c3d",
                                    "local_router": False,
                                    "holdtime": 884,
                                    "received": 1198,
                                    "attach_bit": 0,
                                    "p_bit": 0,
                                    "overload_bit": 0,
                                },
                                "extended_is_neighbor": {
                                    "R6.00": {"metric": 0},
                                    "R7.00": {"metric": 0},
                                },
                            },
                        },
                        "total_lsp_count": 11,
                        "local_lsp_count": 1,
                    },
                    2: {
                        "lspid": {
                            "R2.00-00": {
                                "lsp": {
                                    "seq_num": "0x00000009",
                                    "checksum": "0x5188",
                                    "local_router": False,
                                    "holdtime": 1082,
                                    "received": 1199,
                                    "attach_bit": 0,
                                    "p_bit": 0,
                                    "overload_bit": 0,
                                },
                                "area_address": "49.0001",
                                "nlpid": ["0xcc", "0x8e"],
                                "mt_entries": {
                                    "Standard (IPv4 Unicast)": {},
                                    "IPv6 Unicast": {
                                        "attach_bit": 0,
                                        "p_bit": 0,
                                        "overload_bit": 0,
                                    },
                                },
                                "hostname": "R2",
                                "extended_is_neighbor": {
                                    "R3.07": {
                                        "metric": 10}},
                                "mt_is_neighbor": {
                                    "R3.07": {
                                        "metric": 10, 
                                        "mt_id": "MT (IPv6 Unicast)"}
                                },
                                "ip_address": "2.2.2.2",
                                "extended_ipv4_reachability": {
                                    "2.2.2.2/32": {
                                        "ip_prefix": "2.2.2.2",
                                        "prefix_length": "32",
                                        "metric": 10,
                                    },
                                    "10.1.2.0/24": {
                                        "ip_prefix": "10.1.2.0",
                                        "prefix_length": "24",
                                        "metric": 10,
                                    },
                                },
                                "ipv6_address": "2001:db8:2:2:2::2",
                                "mt_ipv6_reachability": {
                                    "2001:db8:2:2:2::2/128": {
                                        "ip_prefix": "2001:db8:2:2:2::2",
                                        "prefix_length": "128",
                                        "metric": 10,
                                    },
                                    "2001:db8:10:1::/64": {
                                        "ip_prefix": "2001:db8:10:1::",
                                        "prefix_length": "64",
                                        "metric": 10,
                                    },
                                },
                            },
                            "R3.00-00": {
                                "lsp": {
                                    "seq_num": "0x00000011",
                                    "checksum": "0x4c4c",
                                    "local_router": True,
                                    "holdtime": 979,
                                    "attach_bit": 0,
                                    "p_bit": 0,
                                    "overload_bit": 0,
                                },
                                "area_address": "49.0002",
                                "extended_is_neighbor": {
                                    "R3.07": {
                                        "metric": 10},
                                    "R5.01": {
                                        "metric": 10},
                                },
                                "nlpid": ["0xcc", "0x8e"],
                                "ip_address": "3.3.3.3",
                                "extended_ipv4_reachability": {
                                    "3.3.3.0/24": {
                                        "ip_prefix": "3.3.3.0",
                                        "prefix_length": "24",
                                        "metric": 10,
                                    },
                                    "10.2.3.0/24": {
                                        "ip_prefix": "10.2.3.0",
                                        "prefix_length": "24",
                                        "metric": 10,
                                    },
                                },
                                "hostname": "R3",
                                "mt_is_neighbor": {
                                    "R3.07": {
                                        "metric": 10, 
                                        "mt_id": "MT (IPv6 Unicast)"},
                                    "R5.01": {
                                        "metric": 10, 
                                        "mt_id": "MT (IPv6 Unicast)"},
                                },
                                "ipv6_address": "2001:db8:3:3:3::3",
                                "mt_ipv6_reachability": {
                                    "2001:db8:3:3:3::3/128": {
                                        "ip_prefix": "2001:db8:3:3:3::3",
                                        "prefix_length": "128",
                                        "metric": 10,
                                    },
                                    "2001:db8:10:2::/64": {
                                        "ip_prefix": "2001:db8:10:2::",
                                        "prefix_length": "64",
                                        "metric": 10,
                                    },
                                },
                                "mt_entries": {
                                    "Standard (IPv4 Unicast)": {},
                                    "IPv6 Unicast": {
                                        "attach_bit": 0,
                                        "p_bit": 0,
                                        "overload_bit": 0,
                                    },
                                },
                            },
                            "R3.07-00": {
                                "lsp": {
                                    "seq_num": "0x00000007",
                                    "checksum": "0x652a",
                                    "local_router": False,
                                    "holdtime": 604,
                                    "attach_bit": 0,
                                    "p_bit": 0,
                                    "overload_bit": 0,
                                },
                                "extended_is_neighbor": {
                                    "R3.00": {
                                        "metric": 0},
                                    "R2.00": {
                                        "metric": 0},
                                },
                            },
                            "R5.00-00": {
                                "lsp": {
                                    "seq_num": "0x0000000b",
                                    "checksum": "0x93bc",
                                    "local_router": False,
                                    "holdtime": 903,
                                    "received": 1199,
                                    "attach_bit": 0,
                                    "p_bit": 0,
                                    "overload_bit": 0,
                                },
                                "area_address": "49.0002",
                                "nlpid": ["0xcc", "0x8e"],
                                "mt_entries": {
                                    "Standard (IPv4 Unicast)": {},
                                    "IPv6 Unicast": {
                                        "attach_bit": 0,
                                        "p_bit": 0,
                                        "overload_bit": 0,
                                    },
                                },
                                "hostname": "R5",
                                "extended_is_neighbor": {
                                    "R5.01": {
                                        "metric": 10},
                                    "R5.03": {
                                        "metric": 10},
                                },
                                "mt_is_neighbor": {
                                    "R5.01": {
                                        "metric": 10, 
                                        "mt_id": "MT (IPv6 Unicast)"},
                                    "R5.03": {
                                        "metric": 10, 
                                        "mt_id": "MT (IPv6 Unicast)"},
                                },
                                "ip_address": "5.5.5.5",
                                "extended_ipv4_reachability": {
                                    "5.5.5.5/32": {
                                        "ip_prefix": "5.5.5.5",
                                        "prefix_length": "32",
                                        "metric": 10,
                                    },
                                    "10.3.5.0/24": {
                                        "ip_prefix": "10.3.5.0",
                                        "prefix_length": "24",
                                        "metric": 10,
                                    },
                                },
                                "ipv6_address": "2001:db8:5:5:5::5",
                                "mt_ipv6_reachability": {
                                    "2001:db8:5:5:5::5/128": {
                                        "ip_prefix": "2001:db8:5:5:5::5",
                                        "prefix_length": "128",
                                        "metric": 10,
                                    },
                                    "2001:db8:10:3::/64": {
                                        "ip_prefix": "2001:db8:10:3::",
                                        "prefix_length": "64",
                                        "metric": 10,
                                    },
                                },
                            },
                            "R5.01-00": {
                                "lsp": {
                                    "seq_num": "0x00000004",
                                    "checksum": "0x6236",
                                    "local_router": False,
                                    "holdtime": 426,
                                    "received": 1199,
                                    "attach_bit": 0,
                                    "p_bit": 0,
                                    "overload_bit": 0,
                                },
                                "extended_is_neighbor": {
                                    "R5.00": {
                                        "metric": 0},
                                    "R3.00": {
                                        "metric": 0},
                                },
                            },
                            "R5.03-00": {
                                "lsp": {
                                    "seq_num": "0x00000004",
                                    "checksum": "0x54a8",
                                    "local_router": False,
                                    "holdtime": 965,
                                    "received": 1199,
                                    "attach_bit": 0,
                                    "p_bit": 0,
                                    "overload_bit": 0,
                                },
                                "extended_is_neighbor": {
                                    "R5.00": {
                                        "metric": 0},
                                    "R7.00": {
                                        "metric": 0},
                                },
                            },
                            "R7.00-00": {
                                "lsp": {
                                    "seq_num": "0x00000009",
                                    "checksum": "0x7d78",
                                    "local_router": False,
                                    "holdtime": 766,
                                    "received": 1198,
                                    "attach_bit": 0,
                                    "p_bit": 0,
                                    "overload_bit": 0,
                                },
                                "area_address": "49.0002",
                                "nlpid": ["0xcc", "0x8e"],
                                "router_id": "7.7.7.7",
                                "ip_address": "7.7.7.7",
                                "mt_entries": {
                                    "IPv6 Unicast": {
                                        "attach_bit": 0,
                                        "p_bit": 0,
                                        "overload_bit": 0,
                                    },
                                    "Standard (IPv4 Unicast)": {},
                                },
                                "hostname": "R7",
                                "mt_is_neighbor": {
                                    "R9.01": {
                                        "metric": 40, 
                                        "mt_id": "MT (IPv6 Unicast)"},
                                    "R8.01": {
                                        "metric": 40, 
                                        "mt_id": "MT (IPv6 Unicast)"},
                                },
                                "extended_is_neighbor": {
                                    "R9.01": {
                                        "metric": 40},
                                    "R8.01": {
                                        "metric": 40},
                                },
                                "extended_ipv4_reachability": {
                                    "10.6.7.0/24": {
                                        "ip_prefix": "10.6.7.0",
                                        "prefix_length": "24",
                                        "metric": 40,
                                    },
                                    "7.7.7.7/32": {
                                        "ip_prefix": "7.7.7.7",
                                        "prefix_length": "32",
                                        "metric": 1,
                                    },
                                },
                                "mt_ipv6_reachability": {
                                    "2001:db8:10:6::/64": {
                                        "ip_prefix": "2001:db8:10:6::",
                                        "prefix_length": "64",
                                        "metric": 40,
                                    },
                                    "2001:db8:7:7:7::7/128": {
                                        "ip_prefix": "2001:db8:7:7:7::7",
                                        "prefix_length": "128",
                                        "metric": 1,
                                    },
                                },
                            },
                            "R8.00-00": {
                                "lsp": {
                                    "seq_num": "0x00000005",
                                    "checksum": "0x1309",
                                    "local_router": False,
                                    "holdtime": 453,
                                    "received": 1198,
                                    "attach_bit": 0,
                                    "p_bit": 0,
                                    "overload_bit": 0,
                                },
                                "area_address": "49.0003",
                                "nlpid": ["0xcc", "0x8e"],
                                "mt_entries": {
                                    "Standard (IPv4 Unicast)": {},
                                    "IPv6 Unicast": {
                                        "attach_bit": 0,
                                        "p_bit": 0,
                                        "overload_bit": 0,
                                    },
                                },
                                "hostname": "R8",
                                "extended_is_neighbor": {
                                    "R8.01": {
                                        "metric": 10}},
                                "mt_is_neighbor": {
                                    "R8.01": {
                                        "metric": 10, 
                                        "mt_id": "MT (IPv6 Unicast)"}
                                },
                                "ip_address": "8.8.8.8",
                                "extended_ipv4_reachability": {
                                    "8.8.8.8/32": {
                                        "ip_prefix": "8.8.8.8",
                                        "prefix_length": "32",
                                        "metric": 10,
                                    },
                                    "10.7.8.0/24": {
                                        "ip_prefix": "10.7.8.0",
                                        "prefix_length": "24",
                                        "metric": 10,
                                    },
                                },
                                "ipv6_address": "2001:db8:8:8:8::8",
                                "mt_ipv6_reachability": {
                                    "2001:db8:8:8:8::8/128": {
                                        "ip_prefix": "2001:db8:8:8:8::8",
                                        "prefix_length": "128",
                                        "metric": 10,
                                    },
                                    "2001:db8:10:7::/64": {
                                        "ip_prefix": "2001:db8:10:7::",
                                        "prefix_length": "64",
                                        "metric": 10,
                                    },
                                },
                            },
                            "R8.01-00": {
                                "lsp": {
                                    "seq_num": "0x00000004",
                                    "checksum": "0x9503",
                                    "local_router": False,
                                    "holdtime": 1143,
                                    "received": 1198,
                                    "attach_bit": 0,
                                    "p_bit": 0,
                                    "overload_bit": 0,
                                },
                                "extended_is_neighbor": {
                                    "R8.00": {
                                        "metric": 0},
                                    "R7.00": {
                                        "metric": 0},
                                },
                            },
                            "R9.00-00": {
                                "lsp": {
                                    "seq_num": "0x00000006",
                                    "checksum": "0xfd4e",
                                    "local_router": False,
                                    "holdtime": 800,
                                    "received": 1198,
                                    "attach_bit": 0,
                                    "p_bit": 0,
                                    "overload_bit": 0,
                                },
                                "area_address": "49.0004",
                                "nlpid": ["0xcc", "0x8e"],
                                "mt_entries": {
                                    "Standard (IPv4 Unicast)": {},
                                    "IPv6 Unicast": {
                                        "attach_bit": 0,
                                        "p_bit": 0,
                                        "overload_bit": 0,
                                    },
                                },
                                "hostname": "R9",
                                "extended_is_neighbor": {
                                    "R9.01": {
                                        "metric": 10}},
                                "mt_is_neighbor": {
                                    "R9.01": {
                                        "metric": 10, 
                                        "mt_id": "MT (IPv6 Unicast)"}
                                },
                                "ip_address": "9.9.9.9",
                                "extended_ipv4_reachability": {
                                    "9.9.9.9/32": {
                                        "ip_prefix": "9.9.9.9",
                                        "prefix_length": "32",
                                        "metric": 10,
                                    },
                                    "10.7.9.0/24": {
                                        "ip_prefix": "10.7.9.0",
                                        "prefix_length": "24",
                                        "metric": 10,
                                    },
                                    "10.9.10.0/24": {
                                        "ip_prefix": "10.9.10.0",
                                        "prefix_length": "24",
                                        "metric": 10,
                                    },
                                    "10.10.10.10/32": {
                                        "ip_prefix": "10.10.10.10",
                                        "prefix_length": "32",
                                        "metric": 20,
                                    },
                                },
                                "ipv6_address": "2001:db8:9:9:9::9",
                                "mt_ipv6_reachability": {
                                    "2001:db8:9:9:9::9/128": {
                                        "ip_prefix": "2001:db8:9:9:9::9",
                                        "prefix_length": "128",
                                        "metric": 10,
                                    },
                                    "2001:db8:10:7::/64": {
                                        "ip_prefix": "2001:db8:10:7::",
                                        "prefix_length": "64",
                                        "metric": 10,
                                    },
                                },
                                "ipv6_reachability": {
                                    "2001:2:2:2::2/128": {
                                        "ip_prefix": "2001:2:2:2::2",
                                        "prefix_length": "128",
                                        "metric": "10",
                                    }
                                },
                            },
                            "R9.01-00": {
                                "lsp": {
                                    "seq_num": "0x00000003",
                                    "checksum": "0xfdce",
                                    "local_router": False,
                                    "holdtime": 706,
                                    "received": 1198,
                                    "attach_bit": 0,
                                    "p_bit": 0,
                                    "overload_bit": 0,
                                },
                                "extended_is_neighbor": {
                                    "R9.00": {
                                        "metric": 0},
                                    "R7.00": {
                                        "metric": 0},
                                },
                            },
                        },
                        "total_lsp_count": 11,
                        "local_lsp_count": 1,
                    },
                }
            }
        }
    }

    golden_output_1 = {'execute.return_value': '''
        RP/0/RP0/CPU0:R3#show isis database detail
        Wed Jan 30 22:07:52.759 UTC

        IS-IS test (Level-1) Link State Database
        LSPID                 LSP Seq Num  LSP Checksum  LSP Holdtime/Rcvd  ATT/P/OL
        R3.00-00            * 0x0000000d   0x0476        578  /*            1/0/0
          Area Address:   49.0002
          NLPID:          0xcc
          NLPID:          0x8e
          IP Address:     3.3.3.3
          Metric: 10         IP-Extended 3.3.3.0/24
          Metric: 10         IP-Extended 10.2.3.0/24
          Hostname:       R3
          IPv6 Address:   2001:db8:3:3:3::3
          Metric: 10         MT (IPv6 Unicast) IPv6 2001:db8:3:3:3::3/128
          Metric: 10         MT (IPv6 Unicast) IPv6 2001:db8:10:2::/64
          MT:             Standard (IPv4 Unicast)
          MT:             IPv6 Unicast                                 1/0/0
          Metric: 10         IS-Extended R3.03
          Metric: 10         IS-Extended R5.01          
          Metric: 10         MT (IPv6 Unicast) IS-Extended R3.03
          Metric: 10         MT (IPv6 Unicast) IS-Extended R5.01
        R3.03-00              0x00000007   0x8145        988  /*            0/0/0
          Metric: 0          IS-Extended R3.00
          Metric: 0          IS-Extended R4.00
        R3.05-00              0x00000004   0x7981        600  /*            0/0/0
          Metric: 0          IS-Extended R3.00
          Metric: 0          IS-Extended R6.00
        R4.00-00              0x0000000c   0x5c39        1115 /1200         0/0/0
          Area Address:   49.0002
          Metric: 10         IS-Extended R3.03
          Metric: 10         IS-Extended R4.01
          NLPID:          0xcc
          NLPID:          0x8e
          IP Address:     4.4.4.4
          Metric: 10         IP-Extended 4.4.4.4/32
          Metric: 10         IP-Extended 10.3.4.0/24          
          Hostname:       R4
          Metric: 10         MT (IPv6 Unicast) IS-Extended R3.03
          Metric: 10         MT (IPv6 Unicast) IS-Extended R4.01
          IPv6 Address:   2001:db8:4:4:4::4
          Metric: 10         MT (IPv6 Unicast) IPv6 2001:db8:4:4:4::4/128
          Metric: 10         MT (IPv6 Unicast) IPv6 2001:db8:10:3::/64
          MT:             Standard (IPv4 Unicast)
          MT:             IPv6 Unicast                                 0/0/0
        R4.01-00              0x00000004   0xf9a0        616  /1200         0/0/0
          Metric: 0          IS-Extended R4.00
          Metric: 0          IS-Extended R5.00
        R5.00-00              0x00000009   0x09f9        980  /1199         1/0/0
          Area Address:   49.0002
          NLPID:          0xcc
          NLPID:          0x8e
          MT:             Standard (IPv4 Unicast)
          MT:             IPv6 Unicast                                 1/0/0
          Hostname:       R5
          Metric: 10         IS-Extended R5.01
          Metric: 10         IS-Extended R4.01          
          Metric: 10         MT (IPv6 Unicast) IS-Extended R5.01
          Metric: 10         MT (IPv6 Unicast) IS-Extended R4.01          
          IP Address:     5.5.5.5
          Metric: 10         IP-Extended 5.5.5.5/32
          Metric: 10         IP-Extended 10.3.5.0/24          
          IPv6 Address:   2001:db8:5:5:5::5
          Metric: 10         MT (IPv6 Unicast) IPv6 2001:db8:5:5:5::5/128
          Metric: 10         MT (IPv6 Unicast) IPv6 2001:db8:10:3::/64
        R5.01-00              0x00000004   0x4ac5        521  /1199         0/0/0
          Metric: 0          IS-Extended R5.00
          Metric: 0          IS-Extended R3.00
        R5.03-00              0x00000004   0x3c38        1023 /1199         0/0/0
          Metric: 0          IS-Extended R5.00
          Metric: 0          IS-Extended R7.00
        R6.00-00              0x00000008   0x1869        923  /1199         0/0/0
          Area Address:   49.0002
          NLPID:          0xcc
          NLPID:          0x8e
          Router ID:      6.6.6.6
          IP Address:     6.6.6.6
          MT:             IPv6 Unicast                                 0/0/0
          MT:             Standard (IPv4 Unicast)
          Hostname:       R6
          Metric: 40         MT (IPv6 Unicast) IS-Extended R7.02
          Metric: 40         MT (IPv6 Unicast) IS-Extended R3.05
          Metric: 40         IS-Extended R7.02
          Metric: 40         IS-Extended R3.05
          Metric: 1          IP-Extended 6.6.6.0/24
          Metric: 40         IP-Extended 10.6.7.0/24
          Metric: 40         IP-Extended 10.3.6.0/24
          Metric: 1          MT (IPv6 Unicast) IPv6 2001:db8:6:6:6::6/128
          Metric: 40         MT (IPv6 Unicast) IPv6 2001:db8:10:6::/64
        R7.00-00              0x00000008   0xaba8        965  /1198         1/0/0
          Area Address:   49.0002
          NLPID:          0xcc
          NLPID:          0x8e
          Router ID:      7.7.7.7
          IP Address:     7.7.7.7
          MT:             IPv6 Unicast                                 0/0/0
          MT:             Standard (IPv4 Unicast)
          Hostname:       R7
          Metric: 40         MT (IPv6 Unicast) IS-Extended R7.02
          Metric: 40         MT (IPv6 Unicast) IS-Extended R5.03
          Metric: 40         IS-Extended R7.02
          Metric: 40         IS-Extended R5.03
          Metric: 40         IP-Extended-Interarea 10.7.8.0/24
          Metric: 1          IP-Extended 7.7.7.7/32
          Metric: 40         IP-Extended 10.7.9.0/24          
          Metric: 40         MT (IPv6 Unicast) IPv6-Interarea 2001:db8:10:7::/64
          Metric: 1          MT (IPv6 Unicast) IPv6 2001:db8:7:7:7::7/128          
        R7.02-00              0x00000005   0x8c3d        884  /1198         0/0/0
          Metric: 0          IS-Extended R6.00
          Metric: 0          IS-Extended R7.00

         Total Level-1 LSP count: 11     Local Level-1 LSP count: 1

        IS-IS test (Level-2) Link State Database
        LSPID                 LSP Seq Num  LSP Checksum  LSP Holdtime/Rcvd  ATT/P/OL
        R2.00-00              0x00000009   0x5188        1082 /1199         0/0/0
          Area Address:   49.0001
          NLPID:          0xcc
          NLPID:          0x8e
          MT:             Standard (IPv4 Unicast)
          MT:             IPv6 Unicast                                 0/0/0
          Hostname:       R2
          Metric: 10         IS-Extended R3.07
          Metric: 10         MT (IPv6 Unicast) IS-Extended R3.07
          IP Address:     2.2.2.2
          Metric: 10         IP-Extended 2.2.2.2/32
          Metric: 10         IP-Extended 10.1.2.0/24
          IPv6 Address:   2001:db8:2:2:2::2
          Metric: 10         MT (IPv6 Unicast) IPv6 2001:db8:2:2:2::2/128
          Metric: 10         MT (IPv6 Unicast) IPv6 2001:db8:10:1::/64
        R3.00-00            * 0x00000011   0x4c4c        979  /*            0/0/0
          Area Address:   49.0002
          Metric: 10         IS-Extended R3.07
          Metric: 10         IS-Extended R5.01
          NLPID:          0xcc
          NLPID:          0x8e
          IP Address:     3.3.3.3
          Metric: 10         IP-Extended 3.3.3.0/24
          Metric: 10         IP-Extended 10.2.3.0/24
          Hostname:       R3
          Metric: 10         MT (IPv6 Unicast) IS-Extended R3.07
          Metric: 10         MT (IPv6 Unicast) IS-Extended R5.01
          IPv6 Address:   2001:db8:3:3:3::3
          Metric: 10         MT (IPv6 Unicast) IPv6 2001:db8:3:3:3::3/128
          Metric: 10         MT (IPv6 Unicast) IPv6 2001:db8:10:2::/64
          MT:             Standard (IPv4 Unicast)
          MT:             IPv6 Unicast                                 0/0/0
        R3.07-00              0x00000007   0x652a        604  /*            0/0/0
          Metric: 0          IS-Extended R3.00
          Metric: 0          IS-Extended R2.00
        R5.00-00              0x0000000b   0x93bc        903  /1199         0/0/0
          Area Address:   49.0002
          NLPID:          0xcc
          NLPID:          0x8e
          MT:             Standard (IPv4 Unicast)
          MT:             IPv6 Unicast                                 0/0/0
          Hostname:       R5
          Metric: 10         IS-Extended R5.01
          Metric: 10         IS-Extended R5.03
          Metric: 10         MT (IPv6 Unicast) IS-Extended R5.01
          Metric: 10         MT (IPv6 Unicast) IS-Extended R5.03
          IP Address:     5.5.5.5
          Metric: 10         IP-Extended 5.5.5.5/32
          Metric: 10         IP-Extended 10.3.5.0/24          
          IPv6 Address:   2001:db8:5:5:5::5
          Metric: 10         MT (IPv6 Unicast) IPv6 2001:db8:5:5:5::5/128
          Metric: 10         MT (IPv6 Unicast) IPv6 2001:db8:10:3::/64          
        R5.01-00              0x00000004   0x6236        426  /1199         0/0/0
          Metric: 0          IS-Extended R5.00
          Metric: 0          IS-Extended R3.00
        R5.03-00              0x00000004   0x54a8        965  /1199         0/0/0
          Metric: 0          IS-Extended R5.00
          Metric: 0          IS-Extended R7.00
        R7.00-00              0x00000009   0x7d78        766  /1198         0/0/0
          Area Address:   49.0002
          NLPID:          0xcc
          NLPID:          0x8e
          Router ID:      7.7.7.7
          IP Address:     7.7.7.7
          MT:             IPv6 Unicast                                 0/0/0
          MT:             Standard (IPv4 Unicast)
          Hostname:       R7
          Metric: 40         MT (IPv6 Unicast) IS-Extended R9.01
          Metric: 40         MT (IPv6 Unicast) IS-Extended R8.01          
          Metric: 40         IS-Extended R9.01
          Metric: 40         IS-Extended R8.01          
          Metric: 40         IP-Extended 10.6.7.0/24
          Metric: 1          IP-Extended 7.7.7.7/32          
          Metric: 40         MT (IPv6 Unicast) IPv6 2001:db8:10:6::/64
          Metric: 1          MT (IPv6 Unicast) IPv6 2001:db8:7:7:7::7/128          
        R8.00-00              0x00000005   0x1309        453  /1198         0/0/0
          Area Address:   49.0003
          NLPID:          0xcc
          NLPID:          0x8e
          MT:             Standard (IPv4 Unicast)
          MT:             IPv6 Unicast                                 0/0/0
          Hostname:       R8
          Metric: 10         IS-Extended R8.01
          Metric: 10         MT (IPv6 Unicast) IS-Extended R8.01
          IP Address:     8.8.8.8
          Metric: 10         IP-Extended 8.8.8.8/32
          Metric: 10         IP-Extended 10.7.8.0/24
          IPv6 Address:   2001:db8:8:8:8::8
          Metric: 10         MT (IPv6 Unicast) IPv6 2001:db8:8:8:8::8/128
          Metric: 10         MT (IPv6 Unicast) IPv6 2001:db8:10:7::/64
        R8.01-00              0x00000004   0x9503        1143 /1198         0/0/0
          Metric: 0          IS-Extended R8.00
          Metric: 0          IS-Extended R7.00
        R9.00-00              0x00000006   0xfd4e        800  /1198         0/0/0
          Area Address:   49.0004
          NLPID:          0xcc
          NLPID:          0x8e
          MT:             Standard (IPv4 Unicast)
          MT:             IPv6 Unicast                                 0/0/0
          Hostname:       R9
          Metric: 10         IS-Extended R9.01
          Metric: 10         MT (IPv6 Unicast) IS-Extended R9.01
          IP Address:     9.9.9.9
          Metric: 10         IP-Extended 9.9.9.9/32
          Metric: 10         IP-Extended 10.7.9.0/24
          Metric: 10         IP-Extended 10.9.10.0/24
          Metric: 20         IP-Extended 10.10.10.10/32
          IPv6 Address:   2001:db8:9:9:9::9
          Metric: 10         MT (IPv6 Unicast) IPv6 2001:db8:9:9:9::9/128
          Metric: 10         MT (IPv6 Unicast) IPv6 2001:db8:10:7::/64
          Metric: 10         IPv6 2001:2:2:2::2/128
        R9.01-00              0x00000003   0xfdce        706  /1198         0/0/0
          Metric: 0          IS-Extended R9.00
          Metric: 0          IS-Extended R7.00

         Total Level-2 LSP count: 11     Local Level-2 LSP count: 1
    '''}

    golden_parsed_output_2 = {
        "instance": {
            "isp": {
                "level": {
                    1: {
                        "lspid": {
                            "router-5.00-00": {
                                "lsp": {
                                    "seq_num": "0x00000003",
                                    "checksum": "0x8074460",
                                    "local_router": False,
                                    "holdtime": 457,
                                    "attach_bit": 0,
                                    "p_bit": 0,
                                    "overload_bit": 0,
                                },
                                "area_address": "49",
                                "nlpid": ["0xcc"],
                                "hostname": "router-5",
                                "ip_address": "172.1.1.5",
                                "ip_neighbor": {
                                    "172.3.55.0/24": {
                                        "ip_prefix": "172.3.55.0",
                                        "prefix_length": "24",
                                        "metric": 0,
                                    },
                                    "172.6.1.0/24": {
                                        "ip_prefix": "172.6.1.0",
                                        "prefix_length": "24",
                                        "metric": 10,
                                    },
                                    "172.7.0.0/24": {
                                        "ip_prefix": "172.7.0.0",
                                        "prefix_length": "24",
                                        "metric": 10,
                                    },
                                },
                                "is_neighbor": {
                                    "router-11.00": {
                                        "metric": 10},
                                    "router-11.01": {
                                        "metric": 10},
                                },
                            },
                            "router-11.00-00": {
                                "lsp": {
                                    "seq_num": "0x0000000b",
                                    "checksum": "0x8074460",
                                    "local_router": True,
                                    "holdtime": 1161,
                                    "attach_bit": 0,
                                    "p_bit": 0,
                                    "overload_bit": 0,
                                },
                                "area_address": "49",
                                "nlpid": ["0xcc"],
                                "hostname": "router-11",
                                "ip_address": "172.1.11.11",
                                "ip_neighbor": {
                                    "172.1.111.0/24": {
                                        "ip_prefix": "172.1.111.0",
                                        "prefix_length": "24",
                                        "metric": 0,
                                    },
                                    "172.6.1.0/24": {
                                        "ip_prefix": "172.6.1.0",
                                        "prefix_length": "24",
                                        "metric": 10,
                                    },
                                    "172.7.0.0/24": {
                                        "ip_prefix": "172.7.0.0",
                                        "prefix_length": "24",
                                        "metric": 10,
                                    },
                                },
                                "is_neighbor": {
                                    "router-11.01": {
                                        "metric": 10},
                                    "router-5.00": {
                                        "metric": 10},
                                },
                            },
                            "router-11.01-00": {
                                "lsp": {
                                    "seq_num": "0x00000001",
                                    "checksum": "0x80770ec",
                                    "local_router": True,
                                    "holdtime": 457,
                                    "attach_bit": 0,
                                    "p_bit": 0,
                                    "overload_bit": 0,
                                },
                                "is_neighbor": {
                                    "router-11.00": {
                                        "metric": 0},
                                    "router-5.00": {
                                        "metric": 0},
                                },
                            },
                        },
                        "total_lsp_count": 3,
                        "local_lsp_count": 2,
                    },
                    2: {
                        "lspid": {
                            "router-5.00-00": {
                                "lsp": {
                                    "seq_num": "0x00000005",
                                    "checksum": "0x807997c",
                                    "local_router": False,
                                    "holdtime": 457,
                                    "attach_bit": 0,
                                    "p_bit": 0,
                                    "overload_bit": 0,
                                },
                                "area_address": "49",
                                "nlpid": ["0xcc"],
                                "hostname": "router-5",
                                "ip_address": "172.6.1.5",
                                "ip_neighbor": {
                                    "172.3.55.0/24": {
                                        "ip_prefix": "172.3.55.0",
                                        "prefix_length": "24",
                                        "metric": 0,
                                    },
                                    "172.6.1.0/24": {
                                        "ip_prefix": "172.6.1.0",
                                        "prefix_length": "24",
                                        "metric": 10,
                                    },
                                    "172.1.0.0/24": {
                                        "ip_prefix": "172.1.0.0",
                                        "prefix_length": "24",
                                        "metric": 10,
                                    },
                                    "172.8.111.0/24": {
                                        "ip_prefix": "172.8.111.0",
                                        "prefix_length": "24",
                                        "metric": 10,
                                    },
                                },
                                "is_neighbor": {
                                    "router-11.00": {
                                        "metric": 10},
                                    "router-11.01": {
                                        "metric": 10},
                                },
                            },
                            "router-11.00-00": {
                                "lsp": {
                                    "seq_num": "0x0000000d",
                                    "checksum": "0x807997c",
                                    "local_router": True,
                                    "holdtime": 1184,
                                    "attach_bit": 0,
                                    "p_bit": 0,
                                    "overload_bit": 0,
                                },
                                "area_address": "49",
                                "nlpid": ["0xcc"],
                                "hostname": "router-11",
                                "ip_address": "172.28.111.111",
                                "ip_neighbor": {
                                    "172.8.111.0/24": {
                                        "ip_prefix": "172.8.111.0",
                                        "prefix_length": "24",
                                        "metric": 0,
                                    },
                                    "172.6.1.0/24": {
                                        "ip_prefix": "172.6.1.0",
                                        "prefix_length": "24",
                                        "metric": 10,
                                    },
                                    "172.7.0.0/24": {
                                        "ip_prefix": "172.7.0.0",
                                        "prefix_length": "24",
                                        "metric": 10,
                                    },
                                    "172.3.55.0/24": {
                                        "ip_prefix": "172.3.55.0",
                                        "prefix_length": "24",
                                        "metric": 10,
                                    },
                                },
                                "is_neighbor": {
                                    "router-11.01": {
                                        "metric": 10},
                                    "router-5.00": {
                                        "metric": 10},
                                },
                            },
                            "router-gsr11.01-00": {
                                "lsp": {
                                    "seq_num": "0x00000001",
                                    "checksum": "0x80770ec",
                                    "local_router": True,
                                    "holdtime": 457,
                                    "attach_bit": 0,
                                    "p_bit": 0,
                                    "overload_bit": 0,
                                },
                                "is_neighbor": {
                                    "router-11.00": {
                                        "metric": 0},
                                    "router-5.00": {
                                        "metric": 0},
                                },
                            },
                        },
                        "total_lsp_count": 3,
                        "local_lsp_count": 2,
                    },
                }
            }
        }
    }

    # asr9k
    golden_output_2 = {'execute.return_value': '''
        router# show isis database detail
        IS-IS isp (Level-1) Link State Database
            LSPID                 LSP Seq Num  LSP Checksum  LSP Holdtime  ATT/P/OL
            router-5.00-00     0x00000003   0x8074460        457             0/0/0
              Area Address: 49
              NLPID:       0xcc
              Hostname:    router-5
              IP Address:  172.1.1.5
              Metric: 0          IP 172.3.55.0/24
              Metric: 10         IP 172.6.1.0/24
              Metric: 10         IP 172.7.0.0/24
              Metric: 10         IS router-11.00
              Metric: 10         IS router-11.01
            router-11.00-00  * 0x0000000b   0x8074460        1161            0/0/0
              Area Address: 49
              NLPID:       0xcc
              Hostname:    router-11
              IP Address:  172.1.11.11
              Metric: 0          IP 172.1.111.0/24
              Metric: 10         IP 172.6.1.0/24
              Metric: 10         IP 172.7.0.0/24
              Metric: 10         IS router-11.01
              Metric: 10         IS router-5.00
            router-11.01-00  * 0x00000001   0x80770ec        457             0/0/0
              Metric: 0          IS router-11.00
              Metric: 0          IS router-5.00
             Total LSP count: 3 (L1: 3, L2 0, local L1: 2, local L2 0)
            IS-IS isp (Level-2) Link State Database
            LSPID                 LSP Seq Num  LSP Checksum  LSP Holdtime  ATT/P/OL
            router-5.00-00     0x00000005   0x807997c        457             0/0/0
              Area Address: 49
              NLPID:       0xcc
              Hostname:    router-5
              IP Address:  172.6.1.5
              Metric: 0          IP 172.3.55.0/24
              Metric: 10         IP 172.6.1.0/24
              Metric: 10         IP 172.1.0.0/24
              Metric: 10         IS router-11.00
              Metric: 10         IS router-11.01
              Metric: 10         IP 172.8.111.0/24
            router-11.00-00  * 0x0000000d   0x807997c        1184            0/0/0
              Area Address: 49
              NLPID:       0xcc
              Hostname:    router-11
              IP Address:  172.28.111.111
              Metric: 0          IP 172.8.111.0/24
              Metric: 10         IP 172.6.1.0/24
              Metric: 10         IP 172.7.0.0/24
              Metric: 10         IS router-11.01
              Metric: 10         IS router-5.00
              Metric: 10         IP 172.3.55.0/24
            router-gsr11.01-00  * 0x00000001   0x80770ec        457             0/0/0
              Metric: 0          IS router-11.00
              Metric: 0          IS router-5.00
             Total LSP count: 3 (L1: 0, L2 3, local L1: 0, local L2 2)
    '''}

    golden_parsed_output_3 = {
        "instance": {
            None: {
                "level": {
                    1: {
                        "lspid": {
                            "0000.0C00.0C35.00-00": {
                                "lsp": {
                                    "seq_num": "0x0000000C",
                                    "checksum": "0x5696",
                                    "local_router": False,
                                    "holdtime": 325,
                                    "attach_bit": 0,
                                    "p_bit": 0,
                                    "overload_bit": 0,
                                },
                                "area_address": "39.0001",
                                "is_neighbor": {
                                    "0000.0C00.62E6.03": {
                                        "metric": 10}},
                                "es_neighbor": {
                                    "0000.0C00.0C35": {
                                        "metric": 0}},
                            },
                            "0000.0C00.40AF.00-00": {
                                "lsp": {
                                    "seq_num": "0x00000009",
                                    "checksum": "0x8452",
                                    "local_router": True,
                                    "holdtime": 608,
                                    "attach_bit": 1,
                                    "p_bit": 0,
                                    "overload_bit": 0,
                                },
                                "area_address": "47.0004.004D.0001",
                                "topology": ["IPv4 (0x0)", "IPv6 (0x2)"],
                                "nlpid": ["0x8E"],
                                "ip_address": "172.16.21.49",
                                "is_neighbor": {
                                    "0800.2B16.24EA.01": {
                                        "metric": 10},
                                    "0000.0C00.62E6.03": {
                                        "metric": 10},
                                    "cisco.03": {
                                        "metric": 10},
                                },
                                "es_neighbor": {
                                    "0000.0C00.40AF": {
                                        "metric": 0}},
                                "ipv6_address": "2001:0DB8::/32",
                                "ipv6_reachability": {
                                    "2001:0DB8::/64": {
                                        "ip_prefix": "2001:0DB8::",
                                        "prefix_length": "64",
                                        "metric": "10",
                                    }
                                },
                                "extended_is_neighbor": {
                                    "cisco.03": {
                                        "metric": 5},
                                    "cisco1.03": {
                                        "metric": 10},
                                },
                            },
                        }
                    }
                }
            }
        }
    }

    # ncs5k
    golden_output_3 = {'execute.return_value': '''
        IS-IS Level-1 Link State Database
        LSPID                 LSP Seq Num  LSP Checksum  LSP Holdtime  ATT/P/OL
        0000.0C00.0C35.00-00  0x0000000C   0x5696        325           0/0/0
          Area Address: 47.0004.004D.0001
          Area Address: 39.0001
          Metric: 10   IS 0000.0C00.62E6.03
          Metric: 0    ES 0000.0C00.0C35
        0000.0C00.40AF.00-00* 0x00000009   0x8452        608           1/0/0
          Area Address: 47.0004.004D.0001
          Topology: IPv4 (0x0) IPv6 (0x2)
          NLPID: 0xCC 0x8E
          IP Address: 172.16.21.49
          Metric: 10   IS 0800.2B16.24EA.01
          Metric: 10   IS 0000.0C00.62E6.03
          Metric: 0    ES 0000.0C00.40AF
          IPv6 Address: 2001:0DB8::/32
          Metric: 10   IPv6 (MT-IPv6) 2001:0DB8::/64
          Metric: 5    IS-Extended cisco.03
          Metric: 10   IS-Extended cisco1.03
          Metric: 10    IS (MT-IPv6) cisco.03
    '''}

    def test_empty_output(self):
        self.device = Mock(**self.empty_output)
        obj = ShowIsisDatabaseDetail(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_output_1(self):
        self.device = Mock(**self.golden_output_1)
        obj = ShowIsisDatabaseDetail(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_1)

    def test_output_2(self):
        self.device = Mock(**self.golden_output_2)
        obj = ShowIsisDatabaseDetail(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_2)

    def test_output_3(self):
        self.device = Mock(**self.golden_output_3)
        obj = ShowIsisDatabaseDetail(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_3)

if __name__ == '__main__':
    unittest.main()
