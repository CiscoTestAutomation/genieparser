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
                                              ShowIsisInterface


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


class TestShowIsisInterface(unittest.TestCase):
    ''' Unit test for commands:
        * show isis interface -> ShowIsisInterface
    ''' 

    maxDiff = None 

    empty_output = {'execute.return_value': ''}

    parsed_output_1 = {
        "instance": {
            "test": {
                "interface": {
                    "Loopback0": {
                        "state": "Enabled",
                        "adjacency_formation": "Enabled",
                        "prefix_advertisement": "Enabled",
                        "ipv4_bfd": False,
                        "ipv6_bfd": False,
                        "bfd_min_interval": 150,
                        "bfd_multiplier": 3,
                        "bandwidth": 0,
                        "circuit_type": "level-1-2",
                        "media_type": "Loop",
                        "circuit_number": 0,
                        "level": {
                            1: {
                                "adjacency_count": 0,
                                "lsp_pacing_interval_ms": 33,
                                "psnp_entry_queue_size": 0,
                                "hello_interval_sec": 10,
                                "hello_multiplier": 3,
                            },
                            2: {
                                "adjacency_count": 0,
                                "lsp_pacing_interval_ms": 33,
                                "psnp_entry_queue_size": 0,
                                "hello_interval_sec": 10,
                                "hello_multiplier": 3,
                            },
                        },
                        "clns_io": {
                            "protocol_state": "Up", 
                            "mtu": 1500},
                        "topology": {
                            "ipv4 unicast": {
                                "state": "Enabled",
                                "adjacency_formation": "Running",
                                "prefix_advertisement": "Running",
                                "metric": {
                                    "level": {
                                        1: 10, 
                                        2: 10}},
                                "weight": {
                                    "level": {
                                        1: 0, 
                                        2: 0}},
                                "mpls": {
                                    "mpls_max_label_stack": "1/3/10 (PRI/BKP/SRTE)",
                                    "ldp_sync": {
                                        "level": {
                                            1: "Disabled", 
                                            2: "Disabled"}},
                                },
                                "frr": {
                                    "level": {
                                        1: {
                                            "state": "Not Enabled", 
                                            "type": "None"},
                                        2: {
                                            "state": "Not Enabled", 
                                            "type": "None"},
                                    }
                                },
                            },
                            "ipv6 unicast": {
                                "state": "Enabled",
                                "adjacency_formation": "Running",
                                "prefix_advertisement": "Running",
                                "metric": {
                                    "level": {
                                        1: 10, 
                                        2: 10}},
                                "weight": {
                                    "level": {
                                        1: 0, 
                                        2: 0}},
                                "mpls": {
                                    "mpls_max_label_stack": "1/3/10 (PRI/BKP/SRTE)",
                                    "ldp_sync": {
                                        "level": {
                                            1: "Disabled", 
                                            2: "Disabled"}},
                                },
                                "frr": {
                                    "level": {
                                        1: {
                                            "state": "Not Enabled", 
                                            "type": "None"},
                                        2: {
                                            "state": "Not Enabled", 
                                            "type": "None"},
                                    }
                                },
                            },
                        },
                        "address_family": {
                            "IPv4": {
                                "state": "Enabled",
                                "forwarding_address": ["0.0.0.0"],
                                "global_prefix": ["3.3.3.0/24"],
                            },
                            "IPv6": {
                                "state": "Enabled",
                                "forwarding_address": ["::"],
                                "global_prefix": ["2001:db8:3:3:3::3/128"],
                            },
                        },
                        "lsp": {
                            "transmit_timer_expires_ms": 0,
                            "transmission_state": "idle",
                            "lsp_transmit_back_to_back_limit_window_msec": 0,
                            "lsp_transmit_back_to_back_limit": 10,
                        },
                    },
                    "GigabitEthernet0/0/0/0": {
                        "state": "Enabled",
                        "adjacency_formation": "Enabled",
                        "prefix_advertisement": "Enabled",
                        "ipv4_bfd": False,
                        "ipv6_bfd": False,
                        "bfd_min_interval": 150,
                        "bfd_multiplier": 3,
                        "bandwidth": 1000000,
                        "circuit_type": "level-1-2",
                        "media_type": "LAN",
                        "circuit_number": 7,
                        "level": {
                            1: {
                                "adjacency_count": 0,
                                "lan_id": "R3.07",
                                "priority": {
                                    "local": "64", 
                                    "dis": "none (no DIS elected)"},
                                "next_lan_iih_sec": 5,
                                "lsp_pacing_interval_ms": 33,
                                "psnp_entry_queue_size": 0,
                                "hello_interval_sec": 10,
                                "hello_multiplier": 3,
                            },
                            2: {
                                "adjacency_count": 1,
                                "lan_id": "R3.07",
                                "priority": {
                                    "local": "64", 
                                    "dis": "64"},
                                "next_lan_iih_sec": 3,
                                "lsp_pacing_interval_ms": 33,
                                "psnp_entry_queue_size": 0,
                                "hello_interval_sec": 10,
                                "hello_multiplier": 3,
                            },
                        },
                        "clns_io": {
                            "protocol_state": "Up",
                            "mtu": 1497,
                            "snpa": "fa16.3ee6.6bd7",
                            "layer2_mcast_groups_membership": {
                                "all_level_1_iss": "Yes",
                                "all_level_2_iss": "Yes",
                            },
                        },
                        "topology": {
                            "ipv4 unicast": {
                                "state": "Enabled",
                                "adjacency_formation": "Running",
                                "prefix_advertisement": "Running",
                                "metric": {
                                    "level": {
                                        1: 10, 
                                        2: 10}},
                                "weight": {
                                    "level": {
                                        1: 0, 
                                        2: 0}},
                                "mpls": {
                                    "mpls_max_label_stack": "1/3/10 (PRI/BKP/SRTE)",
                                    "ldp_sync": {
                                        "level": {
                                            1: "Disabled", 
                                            2: "Disabled"}},
                                },
                                "frr": {
                                    "level": {
                                        1: {
                                            "state": "Not Enabled", 
                                            "type": "None"},
                                        2: {
                                            "state": "Not Enabled", 
                                            "type": "None"},
                                    }
                                },
                            },
                            "ipv6 unicast": {
                                "state": "Enabled",
                                "adjacency_formation": "Running",
                                "prefix_advertisement": "Running",
                                "metric": {
                                    "level": {
                                        1: 10, 
                                        2: 10}},
                                "weight": {
                                    "level": {
                                        1: 0, 
                                        2: 0}},
                                "mpls": {
                                    "mpls_max_label_stack": "1/3/10 (PRI/BKP/SRTE)",
                                    "ldp_sync": {
                                        "level": {
                                            1: "Disabled", 
                                            2: "Disabled"}},
                                },
                                "frr": {
                                    "level": {
                                        1: {
                                            "state": "Not Enabled", 
                                            "type": "None"},
                                        2: {
                                            "state": "Not Enabled", 
                                            "type": "None"},
                                    }
                                },
                            },
                        },
                        "address_family": {
                            "IPv4": {
                                "state": "Enabled",
                                "forwarding_address": ["10.2.3.3"],
                                "global_prefix": ["10.2.3.0/24"],
                            },
                            "IPv6": {
                                "state": "Enabled",
                                "forwarding_address": ["fe80::f816:3eff:fee6:6bd7"],
                                "global_prefix": ["2001:db8:10:2::/64"],
                            },
                        },
                        "lsp": {
                            "transmit_timer_expires_ms": 0,
                            "transmission_state": "idle",
                            "lsp_transmit_back_to_back_limit_window_msec": 0,
                            "lsp_transmit_back_to_back_limit": 9,
                        },
                    },
                    "GigabitEthernet0/0/0/1": {
                        "state": "Enabled",
                        "adjacency_formation": "Enabled",
                        "prefix_advertisement": "Enabled",
                        "ipv4_bfd": False,
                        "ipv6_bfd": False,
                        "bfd_min_interval": 150,
                        "bfd_multiplier": 3,
                        "bandwidth": 1000000,
                        "circuit_type": "level-1-2",
                        "media_type": "LAN",
                        "circuit_number": 5,
                        "level": {
                            1: {
                                "adjacency_count": 1,
                                "lan_id": "R3.05",
                                "priority": {
                                    "local": "64", 
                                    "dis": "64"},
                                "next_lan_iih_sec": 2,
                                "lsp_pacing_interval_ms": 33,
                                "psnp_entry_queue_size": 0,
                                "hello_interval_sec": 10,
                                "hello_multiplier": 3,
                            },
                            2: {
                                "adjacency_count": 0,
                                "lan_id": "R3.05",
                                "priority": {
                                    "local": "64", 
                                    "dis": "none (no DIS elected)"},
                                "next_lan_iih_sec": 6,
                                "lsp_pacing_interval_ms": 33,
                                "psnp_entry_queue_size": 0,
                                "hello_interval_sec": 10,
                                "hello_multiplier": 3,
                            },
                        },
                        "clns_io": {
                            "protocol_state": "Up",
                            "mtu": 1497,
                            "snpa": "fa16.3eb0.d50f",
                            "layer2_mcast_groups_membership": {
                                "all_level_1_iss": "Yes",
                                "all_level_2_iss": "Yes",
                            },
                        },
                        "topology": {
                            "ipv4 unicast": {
                                "state": "Enabled",
                                "adjacency_formation": "Running",
                                "prefix_advertisement": "Running",
                                "metric": {
                                    "level": {
                                        1: 10, 
                                        2: 10}},
                                "weight": {
                                    "level": {
                                        1: 0, 
                                        2: 0}},
                                "mpls": {
                                    "mpls_max_label_stack": "1/3/10 (PRI/BKP/SRTE)",
                                    "ldp_sync": {
                                        "level": {
                                            1: "Disabled", 
                                            2: "Disabled"}},
                                },
                                "frr": {
                                    "level": {
                                        1: {
                                            "state": "Not Enabled", 
                                            "type": "None"},
                                        2: {
                                            "state": "Not Enabled", 
                                            "type": "None"},
                                    }
                                },
                            },
                            "ipv6 unicast": {
                                "state": "Enabled",
                                "adjacency_formation": "Running",
                                "prefix_advertisement": "Running",
                                "metric": {
                                    "level": {
                                        1: 10, 
                                        2: 10}},
                                "weight": {
                                    "level": {
                                        1: 0, 
                                        2: 0}},
                                "mpls": {
                                    "mpls_max_label_stack": "1/3/10 (PRI/BKP/SRTE)",
                                    "ldp_sync": {
                                        "level": {
                                            1: "Disabled", 
                                            2: "Disabled"}},
                                },
                                "frr": {
                                    "level": {
                                        1: {
                                            "state": "Not Enabled", 
                                            "type": "None"},
                                        2: {
                                            "state": "Not Enabled", 
                                            "type": "None"},
                                    }
                                },
                            },
                        },
                        "address_family": {
                            "IPv4": {
                                "state": "Enabled",
                                "forwarding_address": ["10.3.6.3"],
                                "global_prefix": ["10.3.6.0/24"],
                            },
                            "IPv6": {
                                "state": "Enabled",
                                "forwarding_address": ["fe80::f816:3eff:feb0:d50f"],
                                "global_prefix": ["2001:db8:10:3::/64"],
                            },
                        },
                        "lsp": {
                            "transmit_timer_expires_ms": 0,
                            "transmission_state": "idle",
                            "lsp_transmit_back_to_back_limit_window_msec": 0,
                            "lsp_transmit_back_to_back_limit": 9,
                        },
                    },
                    "GigabitEthernet0/0/0/2": {
                        "state": "Enabled",
                        "adjacency_formation": "Enabled",
                        "prefix_advertisement": "Enabled",
                        "ipv4_bfd": False,
                        "ipv6_bfd": False,
                        "bfd_min_interval": 150,
                        "bfd_multiplier": 3,
                        "bandwidth": 1000000,
                        "circuit_type": "level-1-2",
                        "media_type": "LAN",
                        "circuit_number": 3,
                        "level": {
                            1: {
                                "adjacency_count": 1,
                                "lan_id": "R3.03",
                                "priority": {
                                    "local": "64", 
                                    "dis": "64"},
                                "next_lan_iih_sec": 1,
                                "lsp_pacing_interval_ms": 33,
                                "psnp_entry_queue_size": 0,
                                "hello_interval_sec": 10,
                                "hello_multiplier": 3,
                            },
                            2: {
                                "adjacency_count": 0,
                                "lan_id": "R3.03",
                                "priority": {
                                    "local": "64", 
                                    "dis": "none (no DIS elected)"},
                                "next_lan_iih_sec": 6,
                                "lsp_pacing_interval_ms": 33,
                                "psnp_entry_queue_size": 0,
                                "hello_interval_sec": 10,
                                "hello_multiplier": 3,
                            },
                        },
                        "clns_io": {
                            "protocol_state": "Up",
                            "mtu": 1497,
                            "snpa": "fa16.3ead.2906",
                            "layer2_mcast_groups_membership": {
                                "all_level_1_iss": "Yes",
                                "all_level_2_iss": "Yes",
                            },
                        },
                        "topology": {
                            "ipv4 unicast": {
                                "state": "Enabled",
                                "adjacency_formation": "Running",
                                "prefix_advertisement": "Running",
                                "metric": {
                                    "level": {
                                        1: 10, 
                                        2: 10}},
                                "weight": {
                                    "level": {
                                        1: 0, 
                                        2: 0}},
                                "mpls": {
                                    "mpls_max_label_stack": "1/3/10 (PRI/BKP/SRTE)",
                                    "ldp_sync": {
                                        "level": {
                                            1: "Disabled", 
                                            2: "Disabled"}},
                                },
                                "frr": {
                                    "level": {
                                        1: {
                                            "state": "Not Enabled", 
                                            "type": "None"},
                                        2: {
                                            "state": "Not Enabled", 
                                            "type": "None"},
                                    }
                                },
                            },
                            "ipv6 unicast": {
                                "state": "Enabled",
                                "adjacency_formation": "Running",
                                "prefix_advertisement": "Running",
                                "metric": {
                                    "level": {
                                        1: 10, 
                                        2: 10}},
                                "weight": {
                                    "level": {
                                        1: 0, 
                                        2: 0}},
                                "mpls": {
                                    "mpls_max_label_stack": "1/3/10 (PRI/BKP/SRTE)",
                                    "ldp_sync": {
                                        "level": {
                                            1: "Disabled",
                                            2: "Disabled"}},
                                },
                                "frr": {
                                    "level": {
                                        1: {
                                            "state": "Not Enabled", 
                                            "type": "None"},
                                        2: {
                                            "state": "Not Enabled", 
                                            "type": "None"},
                                    }
                                },
                            },
                        },
                        "address_family": {
                            "IPv4": {
                                "state": "Enabled",
                                "forwarding_address": ["10.3.4.3"],
                                "global_prefix": ["10.3.4.0/24"],
                            },
                            "IPv6": {
                                "state": "Enabled",
                                "forwarding_address": ["fe80::f816:3eff:fead:2906"],
                                "global_prefix": ["None (No global addresses are configured)"],
                            },
                        },
                        "lsp": {
                            "transmit_timer_expires_ms": 0,
                            "transmission_state": "idle",
                            "lsp_transmit_back_to_back_limit_window_msec": 0,
                            "lsp_transmit_back_to_back_limit": 9,
                        },
                    },
                    "GigabitEthernet0/0/0/3": {
                        "state": "Enabled",
                        "adjacency_formation": "Enabled",
                        "prefix_advertisement": "Enabled",
                        "ipv4_bfd": False,
                        "ipv6_bfd": False,
                        "bfd_min_interval": 150,
                        "bfd_multiplier": 3,
                        "bandwidth": 1000000,
                        "circuit_type": "level-1-2",
                        "media_type": "LAN",
                        "circuit_number": 1,
                        "level": {
                            1: {
                                "adjacency_count": 1,
                                "lan_id": "R5.01",
                                "priority": {
                                    "local": "64", 
                                    "dis": "64"},
                                "next_lan_iih_sec": 3,
                                "lsp_pacing_interval_ms": 33,
                                "psnp_entry_queue_size": 0,
                                "hello_interval_sec": 10,
                                "hello_multiplier": 3,
                            },
                            2: {
                                "adjacency_count": 1,
                                "lan_id": "R5.01",
                                "priority": {
                                    "local": "64", 
                                    "dis": "64"},
                                "next_lan_iih_sec": 2,
                                "lsp_pacing_interval_ms": 33,
                                "psnp_entry_queue_size": 0,
                                "hello_interval_sec": 10,
                                "hello_multiplier": 3,
                            },
                        },
                        "clns_io": {
                            "protocol_state": "Up",
                            "mtu": 1497,
                            "snpa": "fa16.3e1c.d826",
                            "layer2_mcast_groups_membership": {
                                "all_level_1_iss": "Yes",
                                "all_level_2_iss": "Yes",
                            },
                        },
                        "topology": {
                            "ipv4 unicast": {
                                "state": "Enabled",
                                "adjacency_formation": "Running",
                                "prefix_advertisement": "Running",
                                "metric": {
                                    "level": {
                                        1: 10, 
                                        2: 10}},
                                "weight": {
                                    "level": {
                                        1: 0, 
                                        2: 0}},
                                "mpls": {
                                    "mpls_max_label_stack": "1/3/10 (PRI/BKP/SRTE)",
                                    "ldp_sync": {
                                        "level": {
                                            1: "Disabled", 
                                            2: "Disabled"}},
                                },
                                "frr": {
                                    "level": {
                                        1: {
                                            "state": "Not Enabled", 
                                            "type": "None"},
                                        2: {
                                            "state": "Not Enabled", 
                                            "type": "None"},
                                    }
                                },
                            },
                            "ipv6 unicast": {
                                "state": "Enabled",
                                "adjacency_formation": "Running",
                                "prefix_advertisement": "Running",
                                "metric": {
                                    "level": {
                                        1: 10, 
                                        2: 10}},
                                "weight": {
                                    "level": {
                                        1: 0, 
                                        2: 0}},
                                "mpls": {
                                    "mpls_max_label_stack": "1/3/10 (PRI/BKP/SRTE)",
                                    "ldp_sync": {
                                        "level": {
                                            1: "Disabled", 
                                            2: "Disabled"}},
                                },
                                "frr": {
                                    "level": {
                                        1: {
                                            "state": "Not Enabled", 
                                            "type": "None"},
                                        2: {
                                            "state": "Not Enabled", 
                                            "type": "None"},
                                    }
                                },
                            },
                        },
                        "address_family": {
                            "IPv4": {
                                "state": "Enabled",
                                "forwarding_address": ["10.3.5.3"],
                                "global_prefix": ["10.3.5.0/24"],
                            },
                            "IPv6": {
                                "state": "Enabled",
                                "forwarding_address": ["fe80::f816:3eff:fe1c:d826"],
                                "global_prefix": ["None (No global addresses are configured)"],
                            },
                        },
                        "lsp": {
                            "transmit_timer_expires_ms": 0,
                            "transmission_state": "idle",
                            "lsp_transmit_back_to_back_limit_window_msec": 0,
                            "lsp_transmit_back_to_back_limit": 9,
                        },
                    },
                }
            }
        }
    }


    golden_parsed_output_1 = {'execute.return_value': '''
        IS-IS test Interfaces
        Loopback0                   Enabled
          Adjacency Formation:      Enabled
          Prefix Advertisement:     Enabled
          IPv4 BFD:                 Disabled
          IPv6 BFD:                 Disabled
          BFD Min Interval:         150
          BFD Multiplier:           3
          Bandwidth:                0

          Circuit Type:             level-1-2
          Media Type:               Loop
          Circuit Number:           0

          Level-1
            Adjacency Count:        0
            LSP Pacing Interval:    33 ms
            PSNP Entry Queue Size:  0
            Hello Interval:         10 s
            Hello Multiplier:       3
          Level-2
            Adjacency Count:        0
            LSP Pacing Interval:    33 ms
            PSNP Entry Queue Size:  0
            Hello Interval:         10 s
            Hello Multiplier:       3

          CLNS I/O
            Protocol State:         Up
            MTU:                    1500

          IPv4 Unicast Topology:    Enabled
            Adjacency Formation:    Running
            Prefix Advertisement:   Running
            Metric (L1/L2):         10/10
            Weight (L1/L2):         0/0
            MPLS Max Label Stack:   1/3/10 (PRI/BKP/SRTE)
            MPLS LDP Sync (L1/L2):  Disabled/Disabled
            FRR (L1/L2):            L1 Not Enabled     L2 Not Enabled
              FRR Type:             None               None
          IPv6 Unicast Topology:    Enabled
            Adjacency Formation:    Running
            Prefix Advertisement:   Running
            Metric (L1/L2):         10/10
            Weight (L1/L2):         0/0
            MPLS Max Label Stack:   1/3/10 (PRI/BKP/SRTE)
            MPLS LDP Sync (L1/L2):  Disabled/Disabled
            FRR (L1/L2):            L1 Not Enabled     L2 Not Enabled
              FRR Type:             None               None

          IPv4 Address Family:      Enabled
            Protocol State:         Up
            Forwarding Address(es): 0.0.0.0
            Global Prefix(es):      3.3.3.0/24
          IPv6 Address Family:      Enabled
            Protocol State:         Up
            Forwarding Address(es): ::
            Global Prefix(es):      2001:db8:3:3:3::3/128

          LSP transmit timer expires in 0 ms
          LSP transmission is idle
          Can send up to 10 back-to-back LSPs in the next 0 ms

        GigabitEthernet0/0/0/0      Enabled
          Adjacency Formation:      Enabled
          Prefix Advertisement:     Enabled
          IPv4 BFD:                 Disabled
          IPv6 BFD:                 Disabled
          BFD Min Interval:         150
          BFD Multiplier:           3
          Bandwidth:                1000000

          Circuit Type:             level-1-2
          Media Type:               LAN
          Circuit Number:           7

          Level-1
            Adjacency Count:        0
            LAN ID:                 R3.07
            Priority (Local/DIS):   64/none (no DIS elected)
            Next LAN IIH in:        5 s
            LSP Pacing Interval:    33 ms
            PSNP Entry Queue Size:  0
            Hello Interval:         10 s
            Hello Multiplier:       3
          Level-2
            Adjacency Count:        1
            LAN ID:                 R3.07
            Priority (Local/DIS):   64/64
            Next LAN IIH in:        3 s
            LSP Pacing Interval:    33 ms
            PSNP Entry Queue Size:  0
            Hello Interval:         10 s
            Hello Multiplier:       3

          CLNS I/O
            Protocol State:         Up
            MTU:                    1497
            SNPA:                   fa16.3ee6.6bd7
            Layer-2 MCast Groups Membership:
              All Level-1 ISs:      Yes
              All Level-2 ISs:      Yes

          IPv4 Unicast Topology:    Enabled
            Adjacency Formation:    Running
            Prefix Advertisement:   Running
            Metric (L1/L2):         10/10
            Weight (L1/L2):         0/0
            MPLS Max Label Stack:   1/3/10 (PRI/BKP/SRTE)
            MPLS LDP Sync (L1/L2):  Disabled/Disabled
            FRR (L1/L2):            L1 Not Enabled     L2 Not Enabled
              FRR Type:             None               None
          IPv6 Unicast Topology:    Enabled
            Adjacency Formation:    Running
            Prefix Advertisement:   Running
            Metric (L1/L2):         10/10
            Weight (L1/L2):         0/0
            MPLS Max Label Stack:   1/3/10 (PRI/BKP/SRTE)
            MPLS LDP Sync (L1/L2):  Disabled/Disabled
            FRR (L1/L2):            L1 Not Enabled     L2 Not Enabled
              FRR Type:             None               None

          IPv4 Address Family:      Enabled
            Protocol State:         Up
            Forwarding Address(es): 10.2.3.3
            Global Prefix(es):      10.2.3.0/24
          IPv6 Address Family:      Enabled
            Protocol State:         Up
            Forwarding Address(es): fe80::f816:3eff:fee6:6bd7
            Global Prefix(es):      2001:db8:10:2::/64

          LSP transmit timer expires in 0 ms
          LSP transmission is idle
          Can send up to 9 back-to-back LSPs in the next 0 ms

        GigabitEthernet0/0/0/1      Enabled
          Adjacency Formation:      Enabled
          Prefix Advertisement:     Enabled
          IPv4 BFD:                 Disabled
          IPv6 BFD:                 Disabled
          BFD Min Interval:         150
          BFD Multiplier:           3
          Bandwidth:                1000000

          Circuit Type:             level-1-2
          Media Type:               LAN
          Circuit Number:           5

          Level-1
            Adjacency Count:        1
            LAN ID:                 R3.05
            Priority (Local/DIS):   64/64
            Next LAN IIH in:        2 s
            LSP Pacing Interval:    33 ms
            PSNP Entry Queue Size:  0
            Hello Interval:         10 s
            Hello Multiplier:       3
          Level-2
            Adjacency Count:        0
            LAN ID:                 R3.05
            Priority (Local/DIS):   64/none (no DIS elected)
            Next LAN IIH in:        6 s
            LSP Pacing Interval:    33 ms
            PSNP Entry Queue Size:  0
            Hello Interval:         10 s
            Hello Multiplier:       3

          CLNS I/O
            Protocol State:         Up
            MTU:                    1497
            SNPA:                   fa16.3eb0.d50f
            Layer-2 MCast Groups Membership:
              All Level-1 ISs:      Yes
              All Level-2 ISs:      Yes

          IPv4 Unicast Topology:    Enabled
            Adjacency Formation:    Running
            Prefix Advertisement:   Running
            Metric (L1/L2):         10/10
            Weight (L1/L2):         0/0
            MPLS Max Label Stack:   1/3/10 (PRI/BKP/SRTE)
            MPLS LDP Sync (L1/L2):  Disabled/Disabled
            FRR (L1/L2):            L1 Not Enabled     L2 Not Enabled
              FRR Type:             None               None
          IPv6 Unicast Topology:    Enabled
            Adjacency Formation:    Running
            Prefix Advertisement:   Running
            Metric (L1/L2):         10/10
            Weight (L1/L2):         0/0
            MPLS Max Label Stack:   1/3/10 (PRI/BKP/SRTE)
            MPLS LDP Sync (L1/L2):  Disabled/Disabled
            FRR (L1/L2):            L1 Not Enabled     L2 Not Enabled
              FRR Type:             None               None

          IPv4 Address Family:      Enabled
            Protocol State:         Up
            Forwarding Address(es): 10.3.6.3
            Global Prefix(es):      10.3.6.0/24
          IPv6 Address Family:      Enabled
            Protocol State:         Up
            Forwarding Address(es): fe80::f816:3eff:feb0:d50f
            Global Prefix(es):      2001:db8:10:3::/64

          LSP transmit timer expires in 0 ms
          LSP transmission is idle
          Can send up to 9 back-to-back LSPs in the next 0 ms

        GigabitEthernet0/0/0/2      Enabled
          Adjacency Formation:      Enabled
          Prefix Advertisement:     Enabled
          IPv4 BFD:                 Disabled
          IPv6 BFD:                 Disabled
          BFD Min Interval:         150
          BFD Multiplier:           3
          Bandwidth:                1000000

          Circuit Type:             level-1-2
          Media Type:               LAN
          Circuit Number:           3

          Level-1
            Adjacency Count:        1
            LAN ID:                 R3.03
            Priority (Local/DIS):   64/64
            Next LAN IIH in:        1 s
            LSP Pacing Interval:    33 ms
            PSNP Entry Queue Size:  0
            Hello Interval:         10 s
            Hello Multiplier:       3
          Level-2
            Adjacency Count:        0
            LAN ID:                 R3.03
            Priority (Local/DIS):   64/none (no DIS elected)
            Next LAN IIH in:        6 s
            LSP Pacing Interval:    33 ms
            PSNP Entry Queue Size:  0
            Hello Interval:         10 s
            Hello Multiplier:       3

          CLNS I/O
            Protocol State:         Up
            MTU:                    1497
            SNPA:                   fa16.3ead.2906
            Layer-2 MCast Groups Membership:
              All Level-1 ISs:      Yes
              All Level-2 ISs:      Yes

          IPv4 Unicast Topology:    Enabled
            Adjacency Formation:    Running
            Prefix Advertisement:   Running
            Metric (L1/L2):         10/10
            Weight (L1/L2):         0/0
            MPLS Max Label Stack:   1/3/10 (PRI/BKP/SRTE)
            MPLS LDP Sync (L1/L2):  Disabled/Disabled
            FRR (L1/L2):            L1 Not Enabled     L2 Not Enabled
              FRR Type:             None               None
          IPv6 Unicast Topology:    Enabled
            Adjacency Formation:    Running
            Prefix Advertisement:   Running
            Metric (L1/L2):         10/10
            Weight (L1/L2):         0/0
            MPLS Max Label Stack:   1/3/10 (PRI/BKP/SRTE)
            MPLS LDP Sync (L1/L2):  Disabled/Disabled
            FRR (L1/L2):            L1 Not Enabled     L2 Not Enabled
              FRR Type:             None               None

          IPv4 Address Family:      Enabled
            Protocol State:         Up
            Forwarding Address(es): 10.3.4.3
            Global Prefix(es):      10.3.4.0/24
          IPv6 Address Family:      Enabled
            Protocol State:         Up
            Forwarding Address(es): fe80::f816:3eff:fead:2906
            Global Prefix(es):      None (No global addresses are configured)

          LSP transmit timer expires in 0 ms
          LSP transmission is idle
          Can send up to 9 back-to-back LSPs in the next 0 ms

        GigabitEthernet0/0/0/3      Enabled
          Adjacency Formation:      Enabled
          Prefix Advertisement:     Enabled
          IPv4 BFD:                 Disabled
          IPv6 BFD:                 Disabled
          BFD Min Interval:         150
          BFD Multiplier:           3
          Bandwidth:                1000000

          Circuit Type:             level-1-2
          Media Type:               LAN
          Circuit Number:           1

          Level-1
            Adjacency Count:        1
            LAN ID:                 R5.01
            Priority (Local/DIS):   64/64
            Next LAN IIH in:        3 s
            LSP Pacing Interval:    33 ms
            PSNP Entry Queue Size:  0
            Hello Interval:         10 s
            Hello Multiplier:       3
          Level-2
            Adjacency Count:        1
            LAN ID:                 R5.01
            Priority (Local/DIS):   64/64
            Next LAN IIH in:        2 s
            LSP Pacing Interval:    33 ms
            PSNP Entry Queue Size:  0
            Hello Interval:         10 s
            Hello Multiplier:       3

          CLNS I/O
            Protocol State:         Up
            MTU:                    1497
            SNPA:                   fa16.3e1c.d826
            Layer-2 MCast Groups Membership:
              All Level-1 ISs:      Yes
              All Level-2 ISs:      Yes

          IPv4 Unicast Topology:    Enabled
            Adjacency Formation:    Running
            Prefix Advertisement:   Running
            Metric (L1/L2):         10/10
            Weight (L1/L2):         0/0
            MPLS Max Label Stack:   1/3/10 (PRI/BKP/SRTE)
            MPLS LDP Sync (L1/L2):  Disabled/Disabled
            FRR (L1/L2):            L1 Not Enabled     L2 Not Enabled
              FRR Type:             None               None
          IPv6 Unicast Topology:    Enabled
            Adjacency Formation:    Running
            Prefix Advertisement:   Running
            Metric (L1/L2):         10/10
            Weight (L1/L2):         0/0
            MPLS Max Label Stack:   1/3/10 (PRI/BKP/SRTE)
            MPLS LDP Sync (L1/L2):  Disabled/Disabled
            FRR (L1/L2):            L1 Not Enabled     L2 Not Enabled
              FRR Type:             None               None

          IPv4 Address Family:      Enabled
            Protocol State:         Up
            Forwarding Address(es): 10.3.5.3
            Global Prefix(es):      10.3.5.0/24
          IPv6 Address Family:      Enabled
            Protocol State:         Up
            Forwarding Address(es): fe80::f816:3eff:fe1c:d826
            Global Prefix(es):      None (No global addresses are configured)

          LSP transmit timer expires in 0 ms
          LSP transmission is idle
          Can send up to 9 back-to-back LSPs in the next 0 ms
    '''}

    def test_empty_output(self):
        self.device = Mock(**self.empty_output)
        obj = ShowIsisInterface(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            obj.parse()

    def test_golden_output_1(self):
        self.device = Mock(**self.golden_parsed_output_1)
        obj = ShowIsisInterface(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.parsed_output_1)


if __name__ == '__main__':
    unittest.main()
