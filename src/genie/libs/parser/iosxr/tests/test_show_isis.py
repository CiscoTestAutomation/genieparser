# Python
import unittest
from unittest.mock import Mock

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError, SchemaMissingKeyError

# iosxr show_isis
from genie.libs.parser.iosxr.show_isis import (
    ShowIsis,
    ShowIsisLspLog,
    ShowIsisSpfLog,
    ShowIsisProtocol,
    ShowIsisHostname,
    ShowIsisInterface,
    ShowIsisAdjacency,
    ShowIsisNeighbors,
    ShowIsisStatistics,
    ShowIsisPrivateAll,
    ShowIsisSpfLogDetail,
    ShowIsisDatabaseDetail,
    ShowIsisSegmentRoutingLabelTable,
    ShowIsisFastRerouteSummary
)

# ==================================================
#  Unit test for 'show isis fast-reroute summary'
# ==================================================
class TestShowIsisFastRerouteSummary(unittest.TestCase):

    ''' Unit test for 'show isis fast-reroute summary' '''

    empty_output = {'execute.return_value': ''}

    golden_parsed_output = {
        'instance':{
            'SR':{
                'topology':{
                    'IPv4 Unicast':{
                        'level':{
                            1:{
                                'all_paths_protected':{
                                    'critical_priority' : 0,
                                    'high_priority' : 0,
                                    'medium_priority' : 0,
                                    'low_priority' : 0,
                                    'total' : 0,
                                    },
                                'some_paths_protected':{
                                    'critical_priority' : 0,
                                    'high_priority' : 0,
                                    'medium_priority' : 0,
                                    'low_priority' : 0,
                                    'total' : 0,
                                    },
                                'unprotected':{
                                    'critical_priority' : 0,
                                    'high_priority' : 0,
                                    'medium_priority' : 4,
                                    'low_priority' : 6,
                                    'total' : 10,
                                    },
                                'protection_coverage':{
                                    'critical_priority' : '0.00%',
                                    'high_priority' : '0.00%',
                                    'medium_priority' : '0.00%',
                                    'low_priority' : '0.00%',
                                    'total' : '0.00%',
                                    },
                                    },
                            2:{
                                'all_paths_protected':{
                                    'critical_priority' : 0,
                                    'high_priority' : 0,
                                    'medium_priority' : 0,
                                    'low_priority' : 0,
                                    'total' : 0,
                                },
                                'some_paths_protected':{
                                    'critical_priority' : 0,
                                    'high_priority' : 0,
                                    'medium_priority' : 0,
                                    'low_priority' : 0,
                                    'total' : 0,
                                },
                                'unprotected':{
                                    'critical_priority' : 0,
                                    'high_priority' : 0,
                                    'medium_priority' : 1,
                                    'low_priority' : 0,
                                    'total' : 1,
                                },
                                'protection_coverage':{
                                    'critical_priority' : '0.00%',
                                    'high_priority' : '0.00%',
                                    'medium_priority' : '0.00%',
                                    'low_priority' : '0.00%',
                                    'total' : '0.00%',
                                },
                            },
                        },
                    },
                },
            },
        },
    }

    golden_output = {'execute.return_value': '''
    RP/0/RP0/CPU0:R3#show isis fast-reroute summary
    Thu Aug 29 15:31:09.046 UTC

    IS-IS SR IPv4 Unicast FRR summary

                          Critical   High       Medium     Low        Total
                          Priority   Priority   Priority   Priority
    Prefixes reachable in L1
        All paths protected     0          0          0          0          0
        Some paths protected    0          0          0          0          0
        Unprotected             0          0          4          6          10
        Protection coverage     0.00%      0.00%      0.00%      0.00%      0.00%
    Prefixes reachable in L2
        All paths protected     0          0          0          0          0
        Some paths protected    0          0          0          0          0
        Unprotected             0          0          1          0          1
        Protection coverage     0.00%      0.00%      0.00%      0.00%      0.00%
    '''}

    def test_show_isis_fast_reroute_summary_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowIsisFastRerouteSummary(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_show_isis_fast_reroute_summary_golden(self):
        self.device = Mock(**self.golden_output)
        obj = ShowIsisFastRerouteSummary(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)

# ==================================================
#  Unit test for 'show isis adjacency'
# ==================================================

class TestShowIsisAdjacency(unittest.TestCase):
    '''Unit test for 'show isis adjacency'''

    empty_output = {'execute.return_value': ''}

    maxDiff = None

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
                                                'snpa': '0004.28ff.868a',
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
                                                'snpa': '0004.28ff.868a',
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
          12a4           Gi0/6/0/2        0004.28ff.868a Up    56       00:04:01 Capable  Up

          Total adjacency count: 2

          IS-IS p Level-2 adjacencies:
          System Id      Interface        SNPA           State Hold     Changed  NSF      BFD
          12a4           PO0/1/0/1        *PtoP*         Up    23       00:00:06 Capable  None
          12a4           Gi0/6/0/2        0004.28ff.868a Up    26       00:00:13 Capable  Init

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
                                                'snpa': 'fa16.3eff.4f49',
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
                                                'snpa': '5e00.40ff.0209',
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
                                                'snpa': 'fa16.3eff.4f49',
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
                                                'snpa': '5e00.40ff.0209',
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
        R1_xe          Gi0/0/0/0.115    fa16.3eff.4f49 Up    23   22:30:27 Yes None None
        R3_nx          Gi0/0/0/1.115    5e00.40ff.0209 Up    20   22:30:27 Yes None None

        Total adjacency count: 2

        IS-IS test Level-2 adjacencies:
        System Id      Interface        SNPA           State Hold Changed  NSF IPv4 IPv6
                                                                               BFD  BFD
        R1_xe          Gi0/0/0/0.115    fa16.3eff.4f49 Up    26   22:30:26 Yes None None
        R3_nx          Gi0/0/0/1.115    5e00.40ff.0209 Up    23   22:30:27 Yes None None

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
        self.device = Mock(**self.golden_output1)
        obj = ShowIsisAdjacency(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output1)

    def test_show_isis_adjacency_golden2(self):
        self.device = Mock(**self.golden_output2)
        obj = ShowIsisAdjacency(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output2)


# ====================================
#  Unit test for 'show isis neighbors'
# ====================================

class TestShowIsisNeighbors(unittest.TestCase):
    '''Unit test for "show isis neighbors"'''

    maxDiff = None

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
                                        'snpa': 'fa16.3eff.4f49',
                                        'state': 'Up',
                                        'holdtime': '24',
                                        'type': 'L1L2',
                                        'ietf_nsf': 'Capable'}}},
                            'GigabitEthernet0/0/0/1.115': {
                                'neighbors': {
                                    'R3_nx': {
                                        'snpa': '5e00.40ff.0209',
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
        R1_xe          Gi0/0/0/0.115    fa16.3eff.4f49 Up    24       L1L2 Capable
        R3_nx          Gi0/0/0/1.115    5e00.40ff.0209 Up    25       L1L2 Capable

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
                                        'snpa': 'fa16.3eff.4f49',
                                        'state': 'Up',
                                        'holdtime': '22',
                                        'type': 'L1L2',
                                        'ietf_nsf': 'Capable'}}},
                            'GigabitEthernet0/0/0/1.115': {
                                'neighbors': {
                                    'R3_nx': {
                                        'snpa': '5e00.40ff.0209',
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
        R1_xe          Gi0/0/0/0.115    fa16.3eff.4f49 Up    22       L1L2 Capable
        R3_nx          Gi0/0/0/1.115    5e00.40ff.0209 Up    22       L1L2 Capable

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
        self.device = Mock(**self.golden_output1)
        obj = ShowIsisNeighbors(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output1)

    def test_show_isis_neighbors_golden2(self):
        self.device = Mock(**self.golden_output2)
        obj = ShowIsisNeighbors(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output2)


# ======================================================
#  Unit test for 'show isis segment-routing label table'
# ======================================================

class TestShowIsisSegmentRoutingLabelTable(unittest.TestCase):
    '''Unit test for "show isis segment-routing label table"'''

    maxDiff = None

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
                        "system_id": "3333.33ff.6666",
                        "is_levels": "level-1-2",
                        "manual_area_address": ["49.0002"],
                        "routing_area_address": ["49.0002", "49.0001"],
                        "non_stop_forwarding": "Disabled",
                        "most_recent_startup_mode": "Cold Restart",
                        "te_connection_status": "Down",
                        "topology": {
                            "IPv4 Unicast": {
                                'vrf': {
                                    'default': {
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
                                },
                            },
                            "IPv6 Unicast": {
                                'vrf': {
                                    'default': {
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
                                    }
                                }
                            },
                        },
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
          System Id: 3333.33ff.6666
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

    golden_parsed_output_2 = {
        'instance': {
            'Cisco': {
                'process_id': 'Cisco',
                'instance': '0',
                'vrf': {
                    'default': {
                        'system_id': '1781.81ff.43c7',
                        'is_levels': 'level-2-only',
                        'manual_area_address': ['49.0000'],
                        'routing_area_address': ['49.0000'],
                        'non_stop_forwarding': 'Disabled',
                        'most_recent_startup_mode': 'Cold Restart',
                        'te_connection_status': 'Up',
                        'topology': {
                            'IPv4 Unicast': {
                                'vrf': {
                                    'default': {
                                        'level': {
                                            2: {
                                                'generate_style': 'Wide',
                                                'accept_style': 'Wide',
                                                'metric': 100000,
                                                'ispf_status': 'Disabled',
                                            },
                                        },
                                        'protocols_redistributed': True,
                                        'redistributing': ['Connected', 'Static', 'OSPF process 65001', 'OSPF process 65002', 'OSPF process 65003'],
                                        'distance': 115,
                                        'adv_passive_only': True,
                                    },
                                },
                            },
                        },
                        'srlb': {
                            'start': 15000,
                            'end': 15999,
                        },
                        'srgb': {
                            'start': 16000,
                            'end': 81534,
                        },
                        'interfaces': {
                            'Bundle-Ether1': {
                                'running_state': 'running suppressed',
                                'configuration_state': 'active in configuration',
                            },
                            'Bundle-Ether2': {
                                'running_state': 'running suppressed',
                                'configuration_state': 'active in configuration',
                            },
                            'Loopback0': {
                                'running_state': 'running passively',
                                'configuration_state': 'passive in configuration',
                            },
                            'TenGigE0/0/1/2': {
                                'running_state': 'running suppressed',
                                'configuration_state': 'active in configuration',
                            },
                            'TenGigE0/0/1/3': {
                                'running_state': 'disabled',
                                'configuration_state': 'active in configuration',
                            },
                            'TenGigE0/5/0/1': {
                                'running_state': 'disabled',
                                'configuration_state': 'active in configuration',
                            },
                        },
                    },
                },
            },
        },
    }

    golden_output_2 = {'execute.return_value': '''
    +++ genie-Router: executing command 'show isis' +++
        show isis

        Mon Oct  7 16:22:11.993 EDT

        IS-IS Router: Cisco
        System Id: 1781.81ff.43c7
        Instance Id: 0
        IS Levels: level-2-only
        Manual area address(es):
            49.0000
        Routing for area address(es):
            49.0000
        Non-stop forwarding: Disabled
        Most recent startup mode: Cold Restart
        TE connection status: Up
        Topologies supported by IS-IS:
            IPv4 Unicast
            Level-2
                Metric style (generate/accept): Wide/Wide
                Metric: 100000
                ISPF status: Disabled
            Redistributing:
                Connected
                Static
                OSPF process 65001
                OSPF process 65002
                OSPF process 65003
            Distance: 115
            Advertise Passive Interface Prefixes Only: Yes
        SRLB allocated: 15000 - 15999
        SRGB allocated: 16000 - 81534
        Interfaces supported by IS-IS:
            Bundle-Ether1 is running suppressed (active in configuration)
            Bundle-Ether2 is running suppressed (active in configuration)
            Loopback0 is running passively (passive in configuration)
            TenGigE0/0/1/2 is running suppressed (active in configuration)
            TenGigE0/0/1/3 is disabled (active in configuration)
            TenGigE0/5/0/1 is disabled (active in configuration)
        RP/0/RSP0/CPU0:genie-Router#

    '''}

    golden_parsed_output_3 = {
        'instance': {
            'test': {
                'process_id': 'test',
                'instance': '0',
                'vrf': {
                    'default': {
                        'system_id': '4444.44ff.8888',
                        'is_levels': 'level-1',
                        'manual_area_address': ['49.0002'],
                        'routing_area_address': ['49.0002'],
                        'non_stop_forwarding': 'Disabled',
                        'most_recent_startup_mode': 'Cold Restart',
                        'te_connection_status': 'Down',
                        'topology': {
                            'IPv4 Unicast': {
                                'vrf': {
                                    'default': {
                                        'level': {
                                            1: {
                                                'generate_style': 'Wide',
                                                'accept_style': 'Wide',
                                                'metric': 10,
                                                'ispf_status': 'Disabled',
                                            },
                                        },
                                        'protocols_redistributed': False,
                                        'distance': 115,
                                        'adv_passive_only': False,
                                    },
                                },
                            },
                            'IPv6 Unicast': {
                                'vrf': {
                                    'default': {
                                        'level': {
                                            1: {
                                                'metric': 10,
                                                'ispf_status': 'Disabled',
                                            },
                                        },
                                        'protocols_redistributed': False,
                                        'distance': 115,
                                        'adv_passive_only': False,
                                    },
                                },
                            },
                        },
                        'interfaces': {
                            'Loopback0': {
                                'running_state': 'running actively',
                                'configuration_state': 'active in configuration',
                            },
                            'GigabitEthernet0/0/0/0': {
                                'running_state': 'running actively',
                                'configuration_state': 'active in configuration',
                            },
                            'GigabitEthernet0/0/0/1': {
                                'running_state': 'running actively',
                                'configuration_state': 'active in configuration',
                            },
                        },
                    },
                },
            },
        },
    }
    golden_output_3 = {'execute.return_value': '''
        show isis
        Mon Nov 25 22:23:10.670 UTC

        IS-IS Router: test
        System Id: 4444.44ff.8888
        Instance Id: 0
        IS Levels: level-1
        Manual area address(es):
            49.0002
        Routing for area address(es):
            49.0002
        Non-stop forwarding: Disabled
        Most recent startup mode: Cold Restart
        TE connection status: Down
        Topologies supported by IS-IS:
            IPv4 Unicast
            Level-1
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
            No protocols redistributed
            Distance: 115
            Advertise Passive Interface Prefixes Only: No
        SRLB not allocated
        SRGB not allocated
        Interfaces supported by IS-IS:
            Loopback0 is running actively (active in configuration)
            GigabitEthernet0/0/0/0 is running actively (active in configuration)
            GigabitEthernet0/0/0/1 is running actively (active in configuration)

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

    def test_show_isis_2(self):
        self.device = Mock(**self.golden_output_2)
        obj = ShowIsis(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_2)

    def test_show_isis_3(self):
        self.device = Mock(**self.golden_output_3)
        obj = ShowIsis(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_3)


class TestShowIsisSpfLog(unittest.TestCase):
    ''' Unit Tests for command/parser
        * show isis spf-log/ShowIsisSpfLog
    '''
    maxDiff = None

    empty_output = {'execute.return_value': ''}

    parsed_output_1 = {
        "instance": {
            "TEST": {
                "address_family": {
                    "IPv4 Unicast": {
                        "spf_log": {
                            1: {
                                "start_timestamp": "Mon Oct  7 2019 23:12:51.401",
                                "level": 2,
                                "type": "PPFRR",
                                "time_ms": 0,
                                "total_nodes": 64,
                                "trigger_count": 1,
                                "triggers": "PERPREFIXFRR",
                            },
                            2: {
                                "start_timestamp": "Mon Oct  7 2019 23:27:50.960",
                                "level": 2,
                                "type": "FSPF",
                                "time_ms": 0,
                                "total_nodes": 64,
                                "trigger_count": 1,
                                "triggers": "PERIODIC",
                            },
                            3: {
                                "start_timestamp": "Tue Oct  8 2019 00:00:17.514",
                                "level": 2,
                                "type": "PRC",
                                "time_ms": 0,
                                "total_nodes": 64,
                                "trigger_count": 6,
                                "first_trigger_lsp": "bla-host1.12-34",
                                "triggers": "PREFIXBAD",
                            },
                            4: {
                                "start_timestamp": "Tue Oct  8 2019 00:02:24.523",
                                "level": 2,
                                "type": "PRC",
                                "time_ms": 0,
                                "total_nodes": 64,
                                "trigger_count": 6,
                                "first_trigger_lsp": "bla-host2.13-34",
                                "triggers": "PREFIXGOOD",
                            },
                            5: {
                                "start_timestamp": "Tue Oct  8 2019 00:02:25.025",
                                "level": 2,
                                "type": "PPFRR",
                                "time_ms": 0,
                                "total_nodes": 64,
                                "trigger_count": 1,
                                "triggers": "PERPREFIXFRR",
                            },
                            6: {
                                "start_timestamp": "Tue Oct  8 2019 08:15:04.265",
                                "level": 2,
                                "type": "PRC",
                                "time_ms": 0,
                                "total_nodes": 64,
                                "trigger_count": 1,
                                "first_trigger_lsp": "bla-9.blahlab-cld.12-34",
                                "triggers": "PREFIXBAD",
                            },
                            7: {
                                "start_timestamp": "Tue Oct  8 2019 08:15:04.418",
                                "level": 2,
                                "type": "PRC",
                                "time_ms": 0,
                                "total_nodes": 64,
                                "trigger_count": 1,
                                "first_trigger_lsp": "bla-9.blahlab-cld.12-34",
                                "triggers": "PREFIXGOOD",
                            },
                            8: {
                                "start_timestamp": "Tue Oct  8 2019 08:17:55.366",
                                "level": 2,
                                "type": "PRC",
                                "time_ms": 0,
                                "total_nodes": 64,
                                "trigger_count": 1,
                                "first_trigger_lsp": "bla-9.blahlab-cld.12-34",
                                "triggers": "PREFIXBAD",
                            },
                        }
                    }
                }
            }
        }
    }


    golden_output_1 = {'execute.return_value': '''
        #show isis spf-log
        Tue Oct  8 17:37:35.029 EDT

           IS-IS TEST Level 2 IPv4 Unicast Route Calculation Log
                            Time Total Trig.
        Timestamp    Type   (ms) Nodes Count First Trigger LSP    Triggers
        ------------ ----- ----- ----- ----- -------------------- -----------------------
        --- Mon Oct  7 2019 ---
        23:12:51.401 PPFRR     0    64     1                      PERPREFIXFRR
        23:27:50.960  FSPF     0    64     1                      PERIODIC
        --- Tue Oct  8 2019 ---
        00:00:17.514   PRC     0    64     6      bla-host1.12-34 PREFIXBAD
        00:02:24.523   PRC     0    64     6      bla-host2.13-34 PREFIXGOOD
        00:02:25.025 PPFRR     0    64     1                      PERPREFIXFRR
        08:15:04.265   PRC     0    64     1 bla-9.blahlab-cld.12-34 PREFIXBAD
        08:15:04.418   PRC     0    64     1 bla-9.blahlab-cld.12-34 PREFIXGOOD
        08:17:55.366   PRC     0    64     1 bla-9.blahlab-cld.12-34 PREFIXBAD
    '''}

    parsed_output_2 = {
        "instance": {
            "1": {
                "address_family": {
                    "IPv4 Unicast": {
                        "spf_log": {
                            1: {
                                "start_timestamp": "Thurs Aug 19 2004 12:00:50.787",
                                "level": 1,
                                "type": "FSPF",
                                "time_ms": 1,
                                "total_nodes": 1,
                                "trigger_count": 3,
                                "first_trigger_lsp": "ensoft-grs7.00-00",
                                "triggers": "LSPHEADER TLVCODE",
                            },
                            2: {
                                "start_timestamp": "Thurs Aug 19 2004 12:00:52.846",
                                "level": 1,
                                "type": "FSPF",
                                "time_ms": 1,
                                "total_nodes": 1,
                                "trigger_count": 1,
                                "first_trigger_lsp": "ensoft-grs7.00-00",
                                "triggers": "LSPHEADER",
                            },
                            3: {
                                "start_timestamp": "Thurs Aug 19 2004 12:00:56.049",
                                "level": 1,
                                "type": "FSPF",
                                "time_ms": 1,
                                "total_nodes": 1,
                                "trigger_count": 1,
                                "first_trigger_lsp": "ensoft-grs7.00-00",
                                "triggers": "TLVCODE",
                            },
                            4: {
                                "start_timestamp": "Thurs Aug 19 2004 12:01:02.620",
                                "level": 1,
                                "type": "FSPF",
                                "time_ms": 1,
                                "total_nodes": 1,
                                "trigger_count": 2,
                                "first_trigger_lsp": "ensoft-grs7.00-00",
                                "triggers": "NEWADJ LINKTLV",
                            },
                            5: {
                                "start_timestamp": "Mon Aug 19 2004 12:00:50.790",
                                "level": 1,
                                "type": "FSPF",
                                "time_ms": 0,
                                "total_nodes": 1,
                                "trigger_count": 4,
                                "first_trigger_lsp": "ensoft-grs7.00-00",
                                "triggers": "LSPHEADER TLVCODE",
                            },
                            6: {
                                "start_timestamp": "Mon Aug 19 2004 12:00:54.043",
                                "level": 1,
                                "type": "FSPF",
                                "time_ms": 1,
                                "total_nodes": 1,
                                "trigger_count": 2,
                                "first_trigger_lsp": "ensoft-grs7.00-00",
                                "triggers": "NEWADJ LSPHEADER",
                            },
                            7: {
                                "start_timestamp": "Mon Aug 19 2004 12:00:55.922",
                                "level": 1,
                                "type": "FSPF",
                                "time_ms": 1,
                                "total_nodes": 2,
                                "trigger_count": 1,
                                "first_trigger_lsp": "ensoft-grs7.00-00",
                                "triggers": "NEWLSPO",
                            },
                        }
                    }
                }
            }
        }
    }

    # From ncs5k/ncs6k/asr9k documentation
    golden_output_2 = {'execute.return_value': '''
        # show isis spf-log

               IS-IS 1 Level 1 IPv4 Unicast Route Calculation Log
                           Time  Total Trig
          Timestamp   Type (ms)  Nodes Count First Trigger LSP Triggers
          ----------- ---- ----  ----- ----- ----- ------- --- --------
          --- Thurs Aug 19 2004 ---
          12:00:50.787  FSPF  1    1     3   ensoft-grs7.00-00 LSPHEADER TLVCODE
          12:00:52.846  FSPF  1    1     1   ensoft-grs7.00-00 LSPHEADER
          12:00:56.049  FSPF  1    1     1   ensoft-grs7.00-00 TLVCODE
          12:01:02.620  FSPF  1    1     2   ensoft-grs7.00-00 NEWADJ LINKTLV

               IS-IS 1 Level 1 IPv4 Unicast Route Calculation Log
                           Time  Total Trig
          Timestamp   Type (ms)  Nodes Count First Trigger LSP Triggers
          ----------- ---- ----  ----- ----- ----- ------- --- --------
          --- Mon Aug 19 2004 ---
          12:00:50.790  FSPF  0    1     4   ensoft-grs7.00-00 LSPHEADER TLVCODE
          12:00:54.043  FSPF  1    1     2   ensoft-grs7.00-00 NEWADJ LSPHEADER
          12:00:55.922  FSPF  1    2     1   ensoft-grs7.00-00 NEWLSPO
    '''}

    def test_empty_output(self):
        device = Mock(**self.empty_output)
        obj = ShowIsisSpfLog(device=device)
        with self.assertRaises(SchemaEmptyParserError):
            obj.parse()

    def test_golden_output_1(self):
        device = Mock(**self.golden_output_1)
        obj = ShowIsisSpfLog(device=device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.parsed_output_1)

    def test_golden_output_2(self):
        device = Mock(**self.golden_output_2)
        obj = ShowIsisSpfLog(device=device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.parsed_output_2)

class TestShowIsisSpfLogDetail(unittest.TestCase):
    ''' Unit tests for commands/parsers
        * show isis spf-log detail/ShowIsisSpfLogDetail
    '''
    maxDiff = None

    empty_output = {'execute.return_value': ''}

    parsed_output_1 = {
        'instance': {
            'isp': {
                'address_family': {
                    'IPv4 Unicast': {
                        'spf_log': {
                            1: {
                                'type': 'FSPF',
                                'time_ms': 1,
                                'level': 1,
                                'total_nodes': 1,
                                'trigger_count': 1,
                                'first_trigger_lsp': '12a5.00-00',
                                'triggers': 'NEWLSP0',
                                'start_timestamp': 'Mon Aug 16 2004 19:25:35.140',
                                'delay': {
                                    'since_first_trigger_ms': 51,
                                },
                                'spt_calculation': {
                                    'cpu_time_ms': 0,
                                    'real_time_ms': 0,
                                },
                                'prefix_update': {
                                    'cpu_time_ms': 1,
                                    'real_time_ms': 1,
                                },
                                'new_lsp_arrivals': 0,
                                'next_wait_interval_ms': 200,
                                'results': {
                                    'nodes': {
                                        'reach': 1,
                                        'unreach': 0,
                                        'total': 1,
                                    },
                                    'prefixes': {
                                        'items': {
                                            'critical_priority': {
                                                'reach': 0,
                                                'unreach': 0,
                                                'total': 0,
                                            },
                                            'high_priority': {
                                                'reach': 0,
                                                'unreach': 0,
                                                'total': 0,
                                            },
                                            'medium_priority': {
                                                'reach': 0,
                                                'unreach': 0,
                                                'total': 0,
                                            },
                                            'low_priority': {
                                                'reach': 0,
                                                'unreach': 0,
                                                'total': 0,
                                            },
                                            'all_priority': {
                                                'reach': 0,
                                                'unreach': 0,
                                                'total': 0,
                                            },
                                        },
                                        'routes': {
                                            'critical_priority': {
                                                'reach': 0,
                                                'total': 0,
                                            },
                                            'high_priority': {
                                                'reach': 0,
                                                'total': 0,
                                            },
                                            'medium_priority': {
                                                'reach': 0,
                                                'total': 0,
                                            },
                                            'low_priority': {
                                                'reach': 0,
                                                'total': 0,
                                            },
                                            'all_priority': {
                                                'reach': 0,
                                                'total': 0,
                                            },
                                        },
                                    },
                                },
                            },
                        },
                    },
                },
            },
        },
    }

    golden_output_1 = {'execute.return_value': '''
        # show isis spf-log detail

              ISIS isp Level 1 IPv4 Unicast Route Calculation Log
                           Time  Total Trig
          Timestamp   Type (ms)  Nodes Count First Trigger LSP   Triggers
            Mon Aug 16 2004
          19:25:35.140  FSPF  1    1     1             12a5.00-00 NEWLSP0
            Delay:              51ms (since first trigger)
            SPT Calculation
              CPU Time:         0ms
              Real Time:        0ms
            Prefix Updates
              CPU Time:         1ms
              Real Time:        1ms
            New LSP Arrivals:    0
            Next Wait Interval: 200ms
                                        Results
                                  Reach Unreach Total
             Nodes:                   1       0     1
             Prefixes (Items)
               Critical Priority:     0       0     0
               High Priority:         0       0     0
               Medium Priority        0       0     0
               Low Priority           0       0     0

               All Priorities         0       0     0
             Prefixes (Routes)
               Critical Priority:     0       -     0
               High Priority:         0       -     0
               Medium Priority        0        -    0
               Low Priority:          0        -    0

               All Priorities         0        -    0
    '''}

    golden_output_2 = {'execute.return_value': '''
        show isis spf-log detail

        Mon Oct 21 10:41:33.540 EDT

        IS-IS Genie Level 2 IPv4 Unicast Route Calculation Log
                            Time Total Trig.
        Timestamp    Type   (ms) Nodes Count First Trigger LSP    Triggers
        ------------ ----- ----- ----- ----- -------------------- -----------------------
        --- Sun Oct 20 2019 ---
        15:53:18.505 PPFRR     5    71     1                      PERPREFIXFRR
        Delay:                 0ms (since first trigger)
        New LSP Arrivals:      0
        SR uloop:              No
        Next Wait Interval:    0ms
        Interrupted:           No
        RIB Batches:           0
        Timings (ms):          +--Total--+
                                Real   CPU
            SPT Calculation:         5     5
            Route Update:            0     0
                                ----- -----
            Full Calculation:        5     5
        16:08:18.055  FSPF     0    71     1                      PERIODIC
        Delay:                 50ms (since first trigger)
                                899545ms (since end of last calculation)
        New LSP Arrivals:      0
        SR uloop:              No
        Next Wait Interval:    150ms
        RIB Batches:           0 (0 critical, 0 high, 0 medium, 0 low)
        Timings (ms):          +--Total--+
                                Real   CPU
            SPT Calculation:         0     0
            Route Update:            0     0
                                ----- -----
            Full Calculation:        0     0
        16:08:18.555 PPFRR     5    71     1                      PERPREFIXFRR
        Delay:                 0ms (since first trigger)
                                500ms (since end of last calculation)
        New LSP Arrivals:      0
        SR uloop:              No
        Next Wait Interval:    0ms
        Interrupted:           No
        RIB Batches:           0
        Timings (ms):          +--Total--+
                                Real   CPU
            SPT Calculation:         5     5
            Route Update:            0     0
                                ----- -----
            Full Calculation:        5     5
    '''}

    parsed_output_2 = {
        'instance': {
            'Genie': {
                'address_family': {
                    'IPv4 Unicast': {
                        'spf_log': {
                            1: {
                                'type': 'PPFRR',
                                'time_ms': 5,
                                'level': 2,
                                'total_nodes': 71,
                                'trigger_count': 1,
                                'triggers': 'PERPREFIXFRR',
                                'start_timestamp': 'Timestamp    Type    15:53:18.505',
                                'delay': {
                                    'since_first_trigger_ms': 0,
                                },
                                'new_lsp_arrivals': 0,
                                'sr_uloop': 'No',
                                'next_wait_interval_ms': 0,
                                'interrupted': 'No',
                                'rib_batches': {
                                    'total': '0',
                                },
                                'spt_calculation': {
                                    'cpu_time_ms': 5,
                                    'real_time_ms': 5,
                                },
                                'prefix_update': {
                                    'cpu_time_ms': 0,
                                    'real_time_ms': 0,
                                },
                                'full_calculation': {
                                    'cpu_time_ms': 5,
                                    'real_time_ms': 5,
                                },
                            },
                            2: {
                                'type': 'FSPF',
                                'time_ms': 0,
                                'level': 2,
                                'total_nodes': 71,
                                'trigger_count': 1,
                                'triggers': 'PERIODIC',
                                'start_timestamp': 'Real   CPU 16:08:18.055',
                                'delay': {
                                    'since_first_trigger_ms': 50,
                                    'since_end_of_last_calculation': 899545,
                                },
                                'new_lsp_arrivals': 0,
                                'sr_uloop': 'No',
                                'next_wait_interval_ms': 150,
                                'rib_batches': {
                                    'total': '0',
                                    'critical': '0',
                                    'high': '0',
                                    'medium': '0',
                                    'low': '0',
                                },
                                'spt_calculation': {
                                    'cpu_time_ms': 0,
                                    'real_time_ms': 0,
                                },
                                'prefix_update': {
                                    'cpu_time_ms': 0,
                                    'real_time_ms': 0,
                                },
                                'full_calculation': {
                                    'cpu_time_ms': 0,
                                    'real_time_ms': 0,
                                },
                            },
                            3: {
                                'type': 'PPFRR',
                                'time_ms': 5,
                                'level': 2,
                                'total_nodes': 71,
                                'trigger_count': 1,
                                'triggers': 'PERPREFIXFRR',
                                'start_timestamp': 'Real   CPU 16:08:18.555',
                                'delay': {
                                    'since_first_trigger_ms': 0,
                                    'since_end_of_last_calculation': 500,
                                },
                                'new_lsp_arrivals': 0,
                                'sr_uloop': 'No',
                                'next_wait_interval_ms': 0,
                                'interrupted': 'No',
                                'rib_batches': {
                                    'total': '0',
                                },
                                'spt_calculation': {
                                    'cpu_time_ms': 5,
                                    'real_time_ms': 5,
                                },
                                'prefix_update': {
                                    'cpu_time_ms': 0,
                                    'real_time_ms': 0,
                                },
                                'full_calculation': {
                                    'cpu_time_ms': 5,
                                    'real_time_ms': 5,
                                },
                            },
                        },
                    },
                },
            },
        },
    }

    def test_empty_output(self):
        device = Mock(**self.empty_output)
        obj = ShowIsisSpfLogDetail(device=device)
        with self.assertRaises(SchemaEmptyParserError):
            obj.parse()

    def test_golden_output_1(self):
        device = Mock(**self.golden_output_1)
        obj = ShowIsisSpfLogDetail(device=device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.parsed_output_1)

    def test_golden_output_2(self):
        device = Mock(**self.golden_output_2)
        obj = ShowIsisSpfLogDetail(device=device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.parsed_output_2)

class TestIsisHostname(unittest.TestCase):
    ''' Unit tests for commands:
        * show isis hostname / ShowIsisHostname
        * show isis instance {instance} hostname / ShowIsisHostname
    '''
    maxDiff = None

    empty_output = {'execute.return_value': ''}

    golden_parsed_output_1 = {
        'isis': {
            'TEST1': {
                'vrf': {
                    'default': {
                        'level': {
                            2: {
                                'system_id': {
                                    '5286.44ff.91b9': {
                                        'dynamic_hostname': 'host-1.bla-site3'},
                                    '9839.23ff.9c50': {
                                        'dynamic_hostname': 'host3-bla'},
                                    '3549.63ff.9ab5': {
                                        'dynamic_hostname': 'abc-3.bla-site4'},
                                    '0670.70ff.b1b1': {
                                            'dynamic_hostname': 'host2-abc'},
                                    '9853.99ff.fb21': {
                                        'dynamic_hostname': 'abc2-xyz',
                                        'local_router': True}}}}}}}}}

    golden_output_1 = {'execute.return_value': '''
        show isis hostname

        Thu Oct  3 10:53:16.534 EDT

        IS-IS TEST1 hostnames
        Level  System ID      Dynamic Hostname
         2     5286.44ff.91b9 host-1.bla-site3
         2     9839.23ff.9c50 host3-bla
         2     3549.63ff.9ab5 abc-3.bla-site4
         2     0670.70ff.b1b1 host2-abc
         2   * 9853.99ff.fb21 abc2-xyz
    '''}

    golden_parsed_output_2 = {
        "isis": {
            "test": {
                "vrf": {
                    "default": {
                        "level": {
                            2: {
                                "system_id": {
                                    "2222.22ff.4444": {
                                        "dynamic_hostname": "R2"},
                                    "8888.88ff.1111": {
                                        "dynamic_hostname": "R8"},
                                    "7777.77ff.eeee": {
                                        "dynamic_hostname": "R7"},
                                    "3333.33ff.6666": {
                                        "dynamic_hostname": "R3",
                                        "local_router": True,
                                    },
                                    "5555.55ff.aaaa": {
                                        "dynamic_hostname": "R5"},
                                    "9999.99ff.3333": {
                                        "dynamic_hostname": "R9"},
                                }
                            },
                            1: {
                                "system_id": {
                                    "4444.44ff.8888": {
                                        "dynamic_hostname": "R4"},
                                    "6666.66ff.cccc": {
                                        "dynamic_hostname": "R6"},
                                    "7777.77ff.eeee": {
                                        "dynamic_hostname": "R7"},
                                    "3333.33ff.6666": {
                                        "dynamic_hostname": "R3",
                                        "local_router": True,
                                    },
                                    "5555.55ff.aaaa": {
                                        "dynamic_hostname": "R5"},
                                }
                            },
                        }
                    }
                }
            }
        }
    }


    golden_output_2 = {'execute.return_value': '''
        show isis hostname
        IS-IS test hostnames
        Level  System ID      Dynamic Hostname
         2     2222.22ff.4444 R2
         1     4444.44ff.8888 R4
         1     6666.66ff.cccc R6
         2     8888.88ff.1111 R8
         1,2   7777.77ff.eeee R7
         1,2 * 3333.33ff.6666 R3
         1,2   5555.55ff.aaaa R5
         2     9999.99ff.3333 R9
    '''}

    def test_empty_output(self):
        self.device = Mock(**self.empty_output)
        obj = ShowIsisHostname(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            obj.parse()

    def test_golden_output_1(self):
        self.device = Mock(**self.golden_output_1)
        obj = ShowIsisHostname(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_1)

    def test_golden_output_2(self):
        self.device = Mock(**self.golden_output_2)
        obj = ShowIsisHostname(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_2)


class TestShowIsisStatistics(unittest.TestCase):
    ''' Unit tests for commands/parsers
        * show isis statistics/ShowIsisStatistics
    '''
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

    parsed_output_2 = {
        'isis': {
            'COEUR': {
                'csnp_cache': {
                    'hits': 0,
                    'tries': 49,
                    'updates': 66,
                },
                'interface': {
                    'Bundle-Ether10': {
                        'level': {
                            1: {
                                'csnp': {
                                    'received': 24,
                                    'sent': 24,
                                },
                                'lsps_sourced': {
                                    'arrival_time_throttled': 0,
                                    'flooding_duplicates': 162,
                                    'received': 57776373,
                                    'sent': 2218410,
                                },
                                'psnp': {
                                    'received': 1576294,
                                    'sent': 33297781,
                                },
                            },
                        },
                    },
                    'Bundle-Ether11': {
                        'level': {
                            1: {
                                'csnp': {
                                    'received': 36,
                                    'sent': 25,
                                },
                                'lsps_sourced': {
                                    'arrival_time_throttled': 0,
                                    'flooding_duplicates': 15,
                                    'received': 57701052,
                                    'sent': 2724240,
                                },
                                'psnp': {
                                    'received': 1761310,
                                    'sent': 33274400,
                                },
                            },
                        },
                    },
                    'Loopback0': {
                    },
                    'Loopback6': {
                    },
                },
                'level': {
                    1: {
                        'address_family': {
                            'IPv4 Unicast': {
                                'full_spf_calculation': 331056,
                                'ispf_calculation': 0,
                                'next_hop_calculation': 4,
                                'partial_route_calculation': 891257,
                                'periodic_spf_calculation': 39298,
                                'total_spf_calculation': 1222317,
                            },
                            'IPv6 Unicast': {
                                'full_spf_calculation': 177541,
                                'ispf_calculation': 0,
                                'next_hop_calculation': 4,
                                'partial_route_calculation': 57170,
                                'periodic_spf_calculation': 43596,
                                'total_spf_calculation': 234715,
                            },
                        },
                        'lsp': {
                            'new': 9140,
                            'refresh': 117187,
                        },
                    },
                },
                'lsp': {
                    'checksum_errors_received': 0,
                    'dropped': 0,
                },
                'process_time': {
                    'csnp': {
                        'average_process_time_nsec': 1249805,
                        'average_process_time_sec': 0,
                        'rate_per_sec': 0,
                    },
                    'hello': {
                        'average_process_time_nsec': 999833,
                        'average_process_time_sec': 0,
                        'rate_per_sec': 0,
                    },
                    'lsp': {
                        'average_process_time_nsec': 999840,
                        'average_process_time_sec': 0,
                        'rate_per_sec': 0,
                    },
                    'psnp': {
                        'average_process_time_nsec': 999835,
                        'average_process_time_sec': 0,
                        'rate_per_sec': 0,
                    },
                },
                'psnp_cache': {
                    'hits': 57508538,
                    'tries': 115477425,
                },
                'snp': {
                    'dropped': 0,
                },
                'transmit_time': {
                    'csnp': {
                        'average_transmit_time_nsec': 0,
                        'average_transmit_time_sec': 0,
                        'rate_per_sec': 0,
                    },
                    'hello': {
                        'average_transmit_time_nsec': 999840,
                        'average_transmit_time_sec': 0,
                        'rate_per_sec': 0,
                    },
                    'lsp': {
                        'average_transmit_time_nsec': 999840,
                        'average_transmit_time_sec': 0,
                        'rate_per_sec': 0,
                    },
                    'psnp': {
                        'average_transmit_time_nsec': 999836,
                        'average_transmit_time_sec': 0,
                        'rate_per_sec': 0,
                    },
                },
                'upd': {
                    'max_queue_size': 20,
                },
            },
        },
    }
    golden_output_2 = {'execute.return_value': '''
        RP/0/RSP0/CPU0:XXXX#sh isis stat
        Fri Sep 25 18:17:07.477 FRANCE

        IS-IS COEUR statistics:
            Fast PSNP cache (hits/tries): 57508538/115477425
            Fast CSNP cache (hits/tries): 0/49
            Fast CSNP cache updates: 66
            LSP checksum errors received: 0
            LSP Dropped: 0
            SNP Dropped: 0
            UPD Max Queue size: 20
            Average transmit times and rate:
              Hello:          0 s,     999840 ns,          0/s
              CSNP:           0 s,          0 ns,          0/s
              PSNP:           0 s,     999836 ns,          0/s
              LSP:            0 s,     999840 ns,          0/s
            Average process times and rate:
              Hello:          0 s,     999833 ns,          0/s
              CSNP:           0 s,    1249805 ns,          0/s
              PSNP:           0 s,     999835 ns,          0/s
              LSP:            0 s,     999840 ns,          0/s
            Level-1:
              LSPs sourced (new/refresh): 9140/117187
              IPv4 Unicast
                Total SPF calculations     : 1222317
                Full SPF calculations      : 331056
                ISPF calculations          : 0
                Next Hop Calculations      : 4
                Partial Route Calculations : 891257
                Periodic SPF calculations  : 39298
              IPv6 Unicast
                Total SPF calculations     : 234715
                Full SPF calculations      : 177541
                ISPF calculations          : 0
                Next Hop Calculations      : 4
                Partial Route Calculations : 57170
                Periodic SPF calculations  : 43596
          Interface Bundle-Ether10:
            PTP Hellos (sent/rcvd)    : 26609054/5327323
            LSP Retransmissions       : 11
            Level-1 LSPs (sent/rcvd)  : 2218410/57776373
          Level-1 CSNPs (sent/rcvd) : 24/24
            Level-1 PSNPs (sent/rcvd) : 33297781/1576294
            Level-1 LSP Flooding Duplicates     : 162
            Level-1 LSPs Arrival Time Throttled : 0
          Interface Bundle-Ether11:
            PTP Hellos (sent/rcvd)    : 26608031/5327345
            LSP Retransmissions       : 15
            Level-1 LSPs (sent/rcvd)  : 2724240/57701052
            Level-1 CSNPs (sent/rcvd) : 25/36
            Level-1 PSNPs (sent/rcvd) : 33274400/1761310
            Level-1 LSP Flooding Duplicates     : 15
            Level-1 LSPs Arrival Time Throttled : 0
          Interface Loopback0:
          Interface Loopback6:
        RP/0/RSP0/CPU0:XXXX#
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

    def test_golden_output_2(self):
        self.device = Mock(**self.golden_output_2)
        obj = ShowIsisStatistics(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.parsed_output_2)


class TestShowIsisProtocol(unittest.TestCase):
    ''' Unit tests for command/parser
        * show isis protocol / ShowIsisProtocol
    '''
    maxDiff = None

    empty_output = {'execute.return_value': ''}

    golden_parsed_output_1 = {
        "instance": {
            "TEST": {
                "process_id": "TEST",
                "instance": "0",
                "vrf": {
                    "default": {
                        "system_id": "0123.45ff.f077",
                        "is_levels": "level-2-only",
                        "manual_area_address": ["90.0000"],
                        "routing_area_address": ["90.0000"],
                        "non_stop_forwarding": "Disabled",
                        "most_recent_startup_mode": "Cold Restart",
                        "te_connection_status": "Up",
                        "topology": {
                            "IPv4 Unicast": {
                                'vrf': {
                                    'default': {
                                        "level": {
                                            2: {
                                                "generate_style": "Wide",
                                                "accept_style": "Wide",
                                                "metric": 100000,
                                                "ispf_status": "Disabled",
                                            }
                                        },
                                        "protocols_redistributed": False,
                                        "distance": 115,
                                        "adv_passive_only": True,
                                    }
                                }
                            }
                        },
                        "srlb": {
                            "start": 15000,
                            "end": 15999},
                        "srgb": {
                            "start": 16000,
                            "end": 81534},
                        "interfaces": {
                            "GigabitEthernet0/0/0/1": {
                                "running_state": "running suppressed",
                                "configuration_state": "active in configuration",
                            },
                            "GigabitEthernet0/0/0/2": {
                                "running_state": "running suppressed",
                                "configuration_state": "active in configuration",
                            },
                            "GigabitEthernet0/0/0/3": {
                                "running_state": "running suppressed",
                                "configuration_state": "active in configuration",
                            },
                            "Loopback0": {
                                "running_state": "running passively",
                                "configuration_state": "passive in configuration",
                            },
                            "GigabitEthernet0/0/0/4": {
                                "running_state": "running suppressed",
                                "configuration_state": "active in configuration",
                            },
                            "GigabitEthernet0/0/0/5": {
                                "running_state": "running suppressed",
                                "configuration_state": "active in configuration",
                            },
                            "GigabitEthernet0/0/0/6": {
                                "running_state": "disabled",
                                "configuration_state": "active in configuration",
                            },
                            "GigabitEthernet0/0/0/7": {
                                "running_state": "disabled",
                                "configuration_state": "active in configuration",
                            },
                        },
                    }
                },
            }
        }
    }

    golden_output_1 = {'execute.return_value': '''
        #show isis protocol
        Wed Oct  9 13:07:59.452 EDT

        IS-IS Router: TEST
          System Id: 0123.45ff.f077
          Instance Id: 0
          IS Levels: level-2-only
          Manual area address(es):
            90.0000
          Routing for area address(es):
            90.0000
          Non-stop forwarding: Disabled
          Most recent startup mode: Cold Restart
          TE connection status: Up
          Topologies supported by IS-IS:
            IPv4 Unicast
              Level-2
                Metric style (generate/accept): Wide/Wide
                Metric: 100000
                ISPF status: Disabled
              No protocols redistributed
              Distance: 115
              Advertise Passive Interface Prefixes Only: Yes
          SRLB allocated: 15000 - 15999
          SRGB allocated: 16000 - 81534
          Interfaces supported by IS-IS:
            GigabitEthernet0/0/0/1 is running suppressed (active in configuration)
            GigabitEthernet0/0/0/2 is running suppressed (active in configuration)
            GigabitEthernet0/0/0/3 is running suppressed (active in configuration)
            Loopback0 is running passively (passive in configuration)
            GigabitEthernet0/0/0/4 is running suppressed (active in configuration)
            GigabitEthernet0/0/0/5 is running suppressed (active in configuration)
            GigabitEthernet0/0/0/6 is disabled (active in configuration)
            GigabitEthernet0/0/0/7 is disabled (active in configuration)
    '''}

    golden_parsed_output_2 = {
        "instance": {
            "test": {
                "process_id": "test",
                "instance": "0",
                "vrf": {
                    "default": {
                        "system_id": "2222.22ff.4444",
                        "is_levels": "level-1-2",
                        "manual_area_address": ["49.0001"],
                        "routing_area_address": ["49.0001"],
                        "non_stop_forwarding": "Disabled",
                        "most_recent_startup_mode": "Cold Restart",
                        "te_connection_status": "Down",
                        "topology": {
                            "IPv4 Unicast": {
                                "vrf": {
                                    "default": {
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
                                    }
                                }
                            },
                            "IPv6 Unicast": {
                                "vrf": {
                                    "default": {
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
                                    }
                                }
                            },
                        },
                        "interfaces": {
                            "Loopback0": {
                                "running_state": "running actively",
                                "configuration_state": "active in configuration",
                            },
                            "GigabitEthernet0/0/0/0.115": {
                                "running_state": "running actively",
                                "configuration_state": "active in configuration",
                            },
                            "GigabitEthernet0/0/0/1.115": {
                                "running_state": "running actively",
                                "configuration_state": "active in configuration",
                            },
                        },
                    }
                },
            },
            "test1": {
                "process_id": "test1",
                "instance": "0",
                "vrf": {
                    "VRF1": {
                        "system_id": "2222.22ff.4444",
                        "is_levels": "level-1-2",
                        "manual_area_address": ["49.0001"],
                        "routing_area_address": ["49.0001"],
                        "non_stop_forwarding": "Disabled",
                        "most_recent_startup_mode": "Cold Restart",
                        "te_connection_status": "Down",
                        "topology": {
                            "IPv4 Unicast": {
                                "vrf": {
                                    "VRF1": {
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
                                    }
                                }
                            },
                            "IPv6 Unicast": {
                                "vrf": {
                                    "VRF1": {
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
                                    }
                                }
                            },
                        },
                        "interfaces": {
                            "Loopback300": {
                                "running_state": "running actively",
                                "configuration_state": "active in configuration",
                            },
                            "GigabitEthernet0/0/0/0.415": {
                                "running_state": "running actively",
                                "configuration_state": "active in configuration",
                            },
                            "GigabitEthernet0/0/0/1.415": {
                                "running_state": "running actively",
                                "configuration_state": "active in configuration",
                            },
                        },
                    }
                },
            },
            "test2": {
                "process_id": "test2",
                "instance": "0",
                "vrf": {
                    "VRF1": {
                        "system_id": "0000.0000.0000",
                        "is_levels": "level-1-2",
                        "non_stop_forwarding": "Disabled",
                        "most_recent_startup_mode": "Cold Restart",
                        "te_connection_status": "Down",
                    }
                },
            },
        }
    }

    golden_output_2 = {'execute.return_value': '''
        # show isis protocol
        IS-IS Router: test
          System Id: 2222.22ff.4444
          Instance Id: 0
          IS Levels: level-1-2
          Manual area address(es):
            49.0001
          Routing for area address(es):
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
            GigabitEthernet0/0/0/0.115 is running actively (active in configuration)
            GigabitEthernet0/0/0/1.115 is running actively (active in configuration)

        IS-IS Router: test1
          VRF context: VRF1
          System Id: 2222.22ff.4444
          Instance Id: 0
          IS Levels: level-1-2
          Manual area address(es):
            49.0001
          Routing for area address(es):
            49.0001
          Non-stop forwarding: Disabled
          Most recent startup mode: Cold Restart
          TE connection status: Down
          Topologies supported by IS-IS:
            IPv4 Unicast VRF VRF1
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
            IPv6 Unicast VRF VRF1
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
            Loopback300 is running actively (active in configuration)
            GigabitEthernet0/0/0/0.415 is running actively (active in configuration)
            GigabitEthernet0/0/0/1.415 is running actively (active in configuration)

        IS-IS Router: test2
          VRF context: VRF1
          System Id: 0000.0000.0000 (Not configured, protocol disabled)
          Instance Id: 0
          IS Levels: level-1-2
          Manual area address(es):
          Routing for area address(es):
          Non-stop forwarding: Disabled
          Most recent startup mode: Cold Restart
          TE connection status: Down
          Topologies supported by IS-IS:
            none
          SRLB not allocated
          SRGB not allocated
          Interfaces supported by IS-IS:
    '''}

    def test_empty_output(self):
        device = Mock(**self.empty_output)
        obj = ShowIsisProtocol(device=device)
        with self.assertRaises(SchemaEmptyParserError):
            obj.parse()

    def test_golden_parsed_output_1(self):
        device = Mock(**self.golden_output_1)
        obj = ShowIsisProtocol(device=device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_1)

    def test_golden_parsed_output_2(self):
        device = Mock(**self.golden_output_2)
        obj = ShowIsisProtocol(device=device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_2)

class TestShowIsisLspLog(unittest.TestCase):
    ''' UT for commands/parsers:
        * show isis lsp-log / ShowIsisLspLog
    '''
    maxDiff = None

    empty_output = {'execute.return_value': ''}

    golden_parsed_output_1 = {
        "instance": {
            "TEST": {
                "lsp_log": {
                    1: {
                        "count": 1,
                        "level": 2,
                        "triggers": "IPEXT",
                        "received_timestamp": "Thu Sep 26 2019 09:39:16.648",
                    },
                    2: {
                        "count": 1,
                        "level": 2,
                        "triggers": "IPEXT",
                        "received_timestamp": "Thu Sep 26 2019 10:29:02.303",
                    },
                    3: {
                        "count": 1,
                        "level": 2,
                        "triggers": "IPEXT",
                        "received_timestamp": "Mon Sep 30 2019 00:00:17.274",
                    },
                    4: {
                        "count": 1,
                        "level": 2,
                        "triggers": "IPEXT",
                        "received_timestamp": "Mon Sep 30 2019 00:02:25.263",
                    },
                    5: {
                        "count": 2,
                        "level": 2,
                        "interface": "Bundle-Ether2",
                        "triggers": "DELADJ",
                        "received_timestamp": "Fri Oct  4 2019 16:10:11.734",
                    },
                    6: {
                        "count": 2,
                        "level": 2,
                        "interface": "Bundle-Ether2",
                        "triggers": "ADJSIDADD",
                        "received_timestamp": "Fri Oct  4 2019 16:17:45.821",
                    },
                }
            }
        }
    }

    golden_output_1 = {'execute.return_value': '''
        #show isis lsp-log
        Tue Oct  8 17:38:16.254 EDT

           IS-IS TEST Level 2 LSP log
        When          Count  Interface          Triggers
        --- Thu Sep 26 2019 ---
        09:39:16.648      1                     IPEXT
        10:29:02.303      1                     IPEXT
        --- Mon Sep 30 2019 ---
        00:00:17.274      1                     IPEXT
        00:02:25.263      1                     IPEXT
        --- Fri Oct  4 2019 ---
        16:10:11.734      2  BE2                DELADJ
        16:17:45.821      2  BE2                ADJSIDADD
    '''}

    golden_parsed_output_2 = {
        "instance": {
            "isp": {
                "lsp_log": {
                    1: {
                        "count": 1,
                        "level": 1,
                        "received_timestamp": "00:02:36"},
                    2: {
                        "count": 1,
                        "level": 1,
                        "triggers": "LSPREGEN",
                        "received_timestamp": "00:02:31",
                    },
                    3: {
                        "count": 1,
                        "level": 1,
                        "interface": "Port-channel4/1",
                        "triggers": "NEWADJ",
                        "received_timestamp": "00:02:24",
                    },
                    4: {
                        "count": 1,
                        "level": 1,
                        "interface": "GigabitEthernet5/0",
                        "triggers": "DIS",
                        "received_timestamp": "00:02:23",
                    },
                    5: {
                        "count": 1,
                        "level": 1,
                        "interface": "Loopback0",
                        "triggers": "IPUP",
                        "received_timestamp": "00:01:12",
                    },
                    6: {
                        "count": 1,
                        "level": 2,
                        "received_timestamp": "00:02:36"},
                    7: {
                        "count": 1,
                        "level": 2,
                        "triggers": "LSPREGEN",
                        "received_timestamp": "00:02:30",
                    },
                    8: {
                        "count": 1,
                        "level": 2,
                        "interface": "GigabitEthernet5/0",
                        "triggers": "DIS",
                        "received_timestamp": "00:02:23",
                    },
                    9: {
                        "count": 1,
                        "level": 2,
                        "interface": "Loopback0",
                        "triggers": "IPUP",
                        "received_timestamp": "00:01:12",
                    },
                }
            }
        }
    }


    # From asr9k docs
    golden_output_2 = {'execute.return_value': '''
        # show isis lsp-log
        ISIS isp Level 1 LSP log
          When       Count      Interface       Triggers
        00:02:36         1
        00:02:31         1                      LSPREGEN
        00:02:24         1      PO4/1           NEWADJ
        00:02:23         1      Gi5/0           DIS
        00:01:12         1      Lo0             IPUP

        ISIS isp Level 2 LSP log
          When       Count      Interface       Triggers
        00:02:36         1
        00:02:30         1                      LSPREGEN
        00:02:23         1      Gi5/0           DIS
        00:01:12         1      Lo0             IPUP
    '''}

    golden_parsed_output_3 = {
        "instance": {
            "": {
                "lsp_log": {
                    1: {
                        "count": 3,
                        "level": 1,
                        "triggers": "CONFIG NEWADJ DIS",
                        "received_timestamp": "07:05:18",
                    },
                    2: {
                        "count": 2,
                        "level": 1,
                        "interface": "Ethernet0",
                        "triggers": "NEWADJ DIS",
                        "received_timestamp": "07:05:13",
                    },
                    3: {
                        "count": 2,
                        "level": 2,
                        "triggers": "CONFIG NEWADJ",
                        "received_timestamp": "07:05:24",
                    },
                    4: {
                        "count": 1,
                        "level": 2,
                        "interface": "Ethernet0",
                        "triggers": "NEWADJ",
                        "received_timestamp": "07:05:23",
                    },
                    5: {
                        "count": 3,
                        "level": 2,
                        "interface": "Loopback0",
                        "triggers": "CONFIG DELADJ",
                        "received_timestamp": "07:01:39",
                    },
                }
            }
        }
    }

    # From ncs6k docs
    golden_output_3 = {'execute.return_value': '''
        Router# show isis lsp-log
            Level 1 LSP log
          When       Count      Interface   Triggers
        07:05:18        3                   CONFIG NEWADJ DIS
        07:05:13        2       Ethernet0   NEWADJ DIS
            Level 2 LSP log
          When       Count      Interface   Triggers
        07:05:24        2                   CONFIG NEWADJ
        07:05:23        1       Ethernet0   NEWADJ
        07:01:39        3       Loopback0   CONFIG DELADJ
    '''}

    golden_parsed_output_4 = {
        "instance": {
            "isp": {
                "lsp_log": {
                    1: {
                        "count": 1,
                        "level": 1,
                        "received_timestamp": "00:02:36"},
                    2: {
                        "count": 1,
                        "level": 1,
                        "triggers": "LSPREGEN",
                        "received_timestamp": "00:02:31",
                    },
                    3: {
                        "count": 1,
                        "level": 1,
                        "interface": "Port-channel4/1",
                        "triggers": "DELADJ",
                        "received_timestamp": "00:02:26",
                    },
                    4: {
                        "count": 1,
                        "level": 1,
                        "interface": "Port-channel4/1",
                        "triggers": "NEWADJ",
                        "received_timestamp": "00:02:24",
                    },
                    5: {
                        "count": 1,
                        "level": 2,
                        "received_timestamp": "00:02:36"},
                    6: {
                        "count": 1,
                        "level": 2,
                        "triggers": "LSPREGEN",
                        "received_timestamp": "00:02:30",
                    },
                    7: {
                        "count": 1,
                        "level": 2,
                        "interface": "Port-channel4/1",
                        "triggers": "DELADJ",
                        "received_timestamp": "00:02:26",
                    },
                    8: {
                        "count": 1,
                        "level": 2,
                        "interface": "Loopback0",
                        "triggers": "IPUP",
                        "received_timestamp": "00:01:12",
                    },
                }
            }
        }
    }

    # from ncs5k docs
    golden_output_4 = {'execute.return_value': '''
        #show isis lsp-log
        ISIS isp Level 1 LSP log
          When       Count      Interface       Triggers
        00:02:36         1
        00:02:31         1                      LSPREGEN
        00:02:26         1      PO4/1           DELADJ
        00:02:24         1      PO4/1           NEWADJ

        ISIS isp Level 2 LSP log
          When       Count      Interface       Triggers
        00:02:36         1
        00:02:30         1                      LSPREGEN
        00:02:26         1      PO4/1           DELADJ
        00:01:12         1      Lo0             IPUP
    '''}

    def test_empty_output(self):
        device = Mock(**self.empty_output)
        obj = ShowIsisLspLog(device=device)
        with self.assertRaises(SchemaEmptyParserError):
            obj.parse()

    def test_golden_output_1(self):
        device = Mock(**self.golden_output_1)
        obj = ShowIsisLspLog(device=device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_1)

    def test_golden_output_2(self):
        device = Mock(**self.golden_output_2)
        obj = ShowIsisLspLog(device=device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_2)

    def test_golden_output_3(self):
        device = Mock(**self.golden_output_3)
        obj = ShowIsisLspLog(device=device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_3)

    def test_golden_output_4(self):
        device = Mock(**self.golden_output_4)
        obj = ShowIsisLspLog(device=device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_4)


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
                                "global_prefix": ["10.36.3.0/24"],
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
                            "snpa": "fa16.3eff.52be",
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
                                "forwarding_address": ["fe80::f816:3eff:feff:52be"],
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
                            "snpa": "fa16.3eff.86bf",
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
                                "forwarding_address": ["fe80::f816:3eff:feff:86bf"],
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
                            "snpa": "fa16.3eff.d6b3",
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
                                "forwarding_address": ["fe80::f816:3eff:feff:d6b3"],
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
                            "snpa": "fa16.3eff.f442",
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
                                "forwarding_address": ["fe80::f816:3eff:feff:f442"],
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
            Global Prefix(es):      10.36.3.0/24
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
            SNPA:                   fa16.3eff.52be
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
            Forwarding Address(es): fe80::f816:3eff:feff:52be
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
            SNPA:                   fa16.3eff.86bf
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
            Forwarding Address(es): fe80::f816:3eff:feff:86bf
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
            SNPA:                   fa16.3eff.d6b3
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
            Forwarding Address(es): fe80::f816:3eff:feff:d6b3
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
            SNPA:                   fa16.3eff.f442
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
            Forwarding Address(es): fe80::f816:3eff:feff:f442
            Global Prefix(es):      None (No global addresses are configured)

          LSP transmit timer expires in 0 ms
          LSP transmission is idle
          Can send up to 9 back-to-back LSPs in the next 0 ms
    '''}

    parsed_output_2 = {
        'instance': {
            'Genie': {
                'interface': {
                    'Bundle-Ether2': {
                        'state': 'Enabled',
                        'adjacency_formation': 'Enabled',
                        'prefix_advertisement': 'Disabled (Suppressed in IS-IS cfg)',
                        'ipv4_bfd': False,
                        'ipv6_bfd': False,
                        'bfd_min_interval': 150,
                        'bfd_multiplier': 3,
                        'rsi_srlg': 'Registered',
                        'bandwidth': 100000000,
                        'circuit_type': 'level-2-only',
                        'media_type': 'P2P',
                        'circuit_number': 0,
                        'extended_circuit_number': 113,
                        'next_p2p_iih_in': 4,
                        'lsp_rexmit_queue_size': 1,
                        'level': {
                            2: {
                                'adjacency_count': 1,
                                'lsp_pacing_interval_ms': 33,
                                'psnp_entry_queue_size': 0,
                                'hello_interval_sec': 10,
                                'hello_multiplier': 3,
                            },
                        },
                        'clns_io': {
                            'protocol_state': 'Up',
                            'mtu': 9199,
                            'snpa': '008a.96ff.1790',
                            'layer2_mcast_groups_membership': {
                                'all_level_1_iss': 'Yes',
                                'all_level_2_iss': 'Yes',
                            },
                        },
                        'topology': {
                            'ipv4 unicast': {
                                'state': 'Enabled',
                                'adjacency_formation': 'Running',
                                'prefix_advertisement': 'Disabled (Intf suppressed in IS-IS cfg)',
                                'metric': {
                                    'level': {
                                        1: 10,
                                        2: 10,
                                    },
                                },
                                'weight': {
                                    'level': {
                                        1: 0,
                                        2: 0,
                                    },
                                },
                                'mpls': {
                                    'mpls_max_label_stack': '3/3/12/0 (PRI/BKP/SRTE/SRAT)',
                                    'ldp_sync': {
                                        'level': {
                                            1: 'Disabled',
                                            2: 'Disabled',
                                        },
                                    },
                                },
                                'frr': {
                                    'level': {
                                        1: {
                                            'state': 'Enabled',
                                            'type': 'per-prefix',
                                            'direct_lfa': {
                                                'state': 'Enabled',
                                            },
                                            'remote_lfa': {
                                                'state': 'Not Enabled',
                                                'tie_breaker': 'Default',
                                                'line_card_disjoint': '30',
                                                'lowest_backup_metric': '20',
                                                'node_protecting': '40',
                                                'primary_path': '10',
                                            },
                                            'ti_lfa': {
                                                'state': 'Enabled',
                                                'tie_breaker': 'Default',
                                                'link_protecting': 'Enabled',
                                                'line_card_disjoint': '0',
                                                'node_protecting': '100',
                                                'srlg_disjoint': '0',
                                            },
                                        },
                                        2: {
                                            'state': 'Enabled',
                                            'type': 'per-prefix',
                                            'direct_lfa': {
                                                'state': 'Enabled',
                                            },
                                            'remote_lfa': {
                                                'state': 'Not Enabled',
                                                'tie_breaker': 'Default',
                                                'line_card_disjoint': '30',
                                                'lowest_backup_metric': '20',
                                                'node_protecting': '40',
                                                'primary_path': '10',
                                            },
                                            'ti_lfa': {
                                                'state': 'Enabled',
                                                'tie_breaker': 'Default',
                                                'link_protecting': 'Enabled',
                                                'line_card_disjoint': '0',
                                                'node_protecting': '100',
                                                'srlg_disjoint': '0',
                                            },
                                        },
                                    },
                                },
                            },
                        },
                        'address_family': {
                            'IPv4': {
                                'state': 'Enabled',
                                'forwarding_address': ['172.18.0.1'],
                                'global_prefix': ['Unknown (Intf suppressed in IS-IS cfg)'],
                            },
                        },
                        'lsp': {
                            'transmit_timer_expires_ms': 0,
                            'transmission_state': 'idle',
                            'lsp_transmit_back_to_back_limit_window_msec': 0,
                            'lsp_transmit_back_to_back_limit': 9,
                        },
                        'underlying_interface': {
                            'HundredGigE0/0/0/1': {
                                'index': '0x55',
                            },
                        },
                    },
                    'TenGigE0/0/0/0/0': {
                        'state': 'Disabled',
                    },
                    'TenGigE0/0/0/4/0': {
                        'state': 'Enabled',
                        'adjacency_formation': 'Enabled',
                        'prefix_advertisement': 'Disabled (Suppressed in IS-IS cfg)',
                        'ipv4_bfd': True,
                        'ipv6_bfd': False,
                        'bfd_min_interval': 250,
                        'bfd_multiplier': 3,
                        'rsi_srlg': 'Registered',
                        'bandwidth': 10000000,
                        'circuit_type': 'level-2-only',
                        'media_type': 'P2P',
                        'circuit_number': 0,
                        'extended_circuit_number': 27,
                        'next_p2p_iih_in': 5,
                        'lsp_rexmit_queue_size': 0,
                        'level': {
                            2: {
                                'adjacency_count': 1,
                                'lsp_pacing_interval_ms': 33,
                                'psnp_entry_queue_size': 0,
                                'hello_interval_sec': 10,
                                'hello_multiplier': 3,
                            },
                        },
                        'clns_io': {
                            'protocol_state': 'Up',
                            'mtu': 9199,
                            'snpa': '008a.96ff.131b',
                            'layer2_mcast_groups_membership': {
                                'all_level_1_iss': 'Yes',
                                'all_level_2_iss': 'Yes',
                            },
                        },
                        'topology': {
                            'ipv4 unicast': {
                                'state': 'Enabled',
                                'adjacency_formation': 'Running',
                                'prefix_advertisement': 'Disabled (Intf suppressed in IS-IS cfg)',
                                'metric': {
                                    'level': {
                                        1: 10,
                                        2: 10,
                                    },
                                },
                                'weight': {
                                    'level': {
                                        1: 0,
                                        2: 0,
                                    },
                                },
                                'mpls': {
                                    'mpls_max_label_stack': '3/3/12/0 (PRI/BKP/SRTE/SRAT)',
                                    'ldp_sync': {
                                        'level': {
                                            1: 'Disabled',
                                            2: 'Disabled',
                                        },
                                    },
                                },
                                'frr': {
                                    'level': {
                                        1: {
                                            'state': 'Not Enabled',
                                            'type': 'None',
                                        },
                                        2: {
                                            'state': 'Not Enabled',
                                            'type': 'None',
                                        },
                                    },
                                },
                            },
                        },
                        'address_family': {
                            'IPv4': {
                                'state': 'Enabled',
                                'forwarding_address': ['172.16.2.133'],
                                'global_prefix': ['Unknown (Intf suppressed in IS-IS cfg)'],
                            },
                        },
                        'lsp': {
                            'transmit_timer_expires_ms': 0,
                            'transmission_state': 'idle',
                            'lsp_transmit_back_to_back_limit_window_msec': 0,
                            'lsp_transmit_back_to_back_limit': 9,
                        },
                    },
                },
            },
        },
    }

    golden_parsed_output_2 = {'execute.return_value': '''
        +++ genie-Router: executing command 'show isis interface' +++
        show isis interface

        Mon Oct 21 10:46:56.224 EDT

        IS-IS Genie Interfaces
        Bundle-Ether2               Enabled
        Adjacency Formation:      Enabled
        Prefix Advertisement:     Disabled (Suppressed in IS-IS cfg)
        IPv4 BFD:                 Disabled
        IPv6 BFD:                 Disabled
        BFD Min Interval:         150
        BFD Multiplier:           3
        RSI SRLG:                 Registered
        Bandwidth:                100000000

        Circuit Type:             level-2-only (Interface circuit type is level-1-2)
        Media Type:               P2P
        Circuit Number:           0
        Extended Circuit Number:  113
        Next P2P IIH in:          4 s
        LSP Rexmit Queue Size:    1

        Level-2
            Adjacency Count:        1
            LSP Pacing Interval:    33 ms
            PSNP Entry Queue Size:  0
            Hello Interval:         10 s
            Hello Multiplier:       3

        CLNS I/O
            Protocol State:         Up
            MTU:                    9199
            SNPA:                   008a.96ff.1790
            Layer-2 MCast Groups Membership:
            All ISs:              Yes

        IPv4 Unicast Topology:    Enabled
            Adjacency Formation:    Running
            Prefix Advertisement:   Disabled (Intf suppressed in IS-IS cfg)
            Metric (L1/L2):         10/10
            Weight (L1/L2):         0/0
            MPLS Max Label Stack:   3/3/12/0 (PRI/BKP/SRTE/SRAT)
            MPLS LDP Sync (L1/L2):  Disabled/Disabled
            FRR (L1/L2):            L1 Enabled         L2 Enabled
            FRR Type:             per-prefix         per-prefix
            Direct LFA:           Enabled            Enabled
            Remote LFA:           Not Enabled        Not Enabled
            Tie Breaker          Default            Default
            Line-card disjoint   30                 30
            Lowest backup metric 20                 20
            Node protecting      40                 40
            Primary path         10                 10
            TI LFA:               Enabled            Enabled
            Tie Breaker          Default            Default
            Link Protecting      Enabled            Enabled
            Line-card disjoint   0                  0
            Node protecting      100                100
            SRLG disjoint        0                  0

        IPv4 Address Family:      Enabled
            Protocol State:         Up
            Forwarding Address(es): 172.18.0.1
            Global Prefix(es):      Unknown (Intf suppressed in IS-IS cfg)

        LSP transmit timer expires in 0 ms
        LSP transmission is idle
        Can send up to 9 back-to-back LSPs in the next 0 ms

        Underlying Interface List
            IfName: Hu0/0/0/1 IfIndex: 0x55


        TenGigE0/0/0/0/0            Disabled (No topologies cfg on the intf)
        TenGigE0/0/0/4/0            Enabled
        Adjacency Formation:      Enabled
        Prefix Advertisement:     Disabled (Suppressed in IS-IS cfg)
        IPv4 BFD:                 Enabled
        IPv6 BFD:                 Disabled
        BFD Min Interval:         250
        BFD Multiplier:           3
        RSI SRLG:                 Registered
        Bandwidth:                10000000

        Circuit Type:             level-2-only (Interface circuit type is level-1-2)
        Media Type:               P2P
        Circuit Number:           0
        Extended Circuit Number:  27
        Next P2P IIH in:          5 s
        LSP Rexmit Queue Size:    0

        Level-2
            Adjacency Count:        1
            LSP Pacing Interval:    33 ms
            PSNP Entry Queue Size:  0
            Hello Interval:         10 s
            Hello Multiplier:       3

        CLNS I/O
            Protocol State:         Up
            MTU:                    9199
            SNPA:                   008a.96ff.131b
            Layer-2 MCast Groups Membership:
            All ISs:              Yes

        IPv4 Unicast Topology:    Enabled
            Adjacency Formation:    Running
            Prefix Advertisement:   Disabled (Intf suppressed in IS-IS cfg)
            Metric (L1/L2):         10/10
            Weight (L1/L2):         0/0
            MPLS Max Label Stack:   3/3/12/0 (PRI/BKP/SRTE/SRAT)
            MPLS LDP Sync (L1/L2):  Disabled/Disabled
            FRR (L1/L2):            L1 Not Enabled     L2 Not Enabled
            FRR Type:             None               None

        IPv4 Address Family:      Enabled
            Protocol State:         Up
            Forwarding Address(es): 172.16.2.133
            Global Prefix(es):      Unknown (Intf suppressed in IS-IS cfg)

        LSP transmit timer expires in 0 ms
        LSP transmission is idle
        Can send up to 9 back-to-back LSPs in the next 0 ms

        RP/0/RP0/CPU0:genie-Router#

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

    def test_golden_output_2(self):
        self.device = Mock(**self.golden_parsed_output_2)
        obj = ShowIsisInterface(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.parsed_output_2)

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
                                "ip_address": "10.36.3.3",
                                "extended_ipv4_reachability": {
                                    "10.36.3.0/24": {
                                        "ip_prefix": "10.36.3.0",
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
                                "ip_address": "10.64.4.4",
                                "extended_ipv4_reachability": {
                                    "10.64.4.4/32": {
                                        "ip_prefix": "10.64.4.4",
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
                                "ip_address": "10.100.5.5",
                                "extended_ipv4_reachability": {
                                    "10.100.5.5/32": {
                                        "ip_prefix": "10.100.5.5",
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
                                "router_id": "10.144.6.6",
                                "ip_address": "10.144.6.6",
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
                                    "10.144.6.0/24": {
                                        "ip_prefix": "10.144.6.0",
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
                                "router_id": "10.196.7.7",
                                "ip_address": "10.196.7.7",
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
                                'ip_interarea': {
                                    '10.7.8.0/24': {
                                        'address_family': {
                                            'ipv4 unicast': {
                                                'metric': 40,
                                            },
                                        },
                                    },
                                    '2001:db8:10:7::/64': {
                                        'address_family': {
                                            'IPv6 Unicast': {
                                                'metric': 40,
                                            },
                                        },
                                    },
                                },
                                "extended_ipv4_reachability": {
                                    "10.196.7.7/32": {
                                        "ip_prefix": "10.196.7.7",
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
                                "ip_address": "10.16.2.2",
                                "extended_ipv4_reachability": {
                                    "10.16.2.2/32": {
                                        "ip_prefix": "10.16.2.2",
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
                                "ip_address": "10.36.3.3",
                                "extended_ipv4_reachability": {
                                    "10.36.3.0/24": {
                                        "ip_prefix": "10.36.3.0",
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
                                "ip_address": "10.100.5.5",
                                "extended_ipv4_reachability": {
                                    "10.100.5.5/32": {
                                        "ip_prefix": "10.100.5.5",
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
                                "router_id": "10.196.7.7",
                                "ip_address": "10.196.7.7",
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
                                    "10.196.7.7/32": {
                                        "ip_prefix": "10.196.7.7",
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
                                "ip_address": "10.1.8.8",
                                "extended_ipv4_reachability": {
                                    "10.1.8.8/32": {
                                        "ip_prefix": "10.1.8.8",
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
                                "ip_address": "10.69.9.9",
                                "extended_ipv4_reachability": {
                                    "10.69.9.9/32": {
                                        "ip_prefix": "10.69.9.9",
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
          IP Address:     10.36.3.3
          Metric: 10         IP-Extended 10.36.3.0/24
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
          IP Address:     10.64.4.4
          Metric: 10         IP-Extended 10.64.4.4/32
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
          IP Address:     10.100.5.5
          Metric: 10         IP-Extended 10.100.5.5/32
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
          Router ID:      10.144.6.6
          IP Address:     10.144.6.6
          MT:             IPv6 Unicast                                 0/0/0
          MT:             Standard (IPv4 Unicast)
          Hostname:       R6
          Metric: 40         MT (IPv6 Unicast) IS-Extended R7.02
          Metric: 40         MT (IPv6 Unicast) IS-Extended R3.05
          Metric: 40         IS-Extended R7.02
          Metric: 40         IS-Extended R3.05
          Metric: 1          IP-Extended 10.144.6.0/24
          Metric: 40         IP-Extended 10.6.7.0/24
          Metric: 40         IP-Extended 10.3.6.0/24
          Metric: 1          MT (IPv6 Unicast) IPv6 2001:db8:6:6:6::6/128
          Metric: 40         MT (IPv6 Unicast) IPv6 2001:db8:10:6::/64
        R7.00-00              0x00000008   0xaba8        965  /1198         1/0/0
          Area Address:   49.0002
          NLPID:          0xcc
          NLPID:          0x8e
          Router ID:      10.196.7.7
          IP Address:     10.196.7.7
          MT:             IPv6 Unicast                                 0/0/0
          MT:             Standard (IPv4 Unicast)
          Hostname:       R7
          Metric: 40         MT (IPv6 Unicast) IS-Extended R7.02
          Metric: 40         MT (IPv6 Unicast) IS-Extended R5.03
          Metric: 40         IS-Extended R7.02
          Metric: 40         IS-Extended R5.03
          Metric: 40         IP-Extended-Interarea 10.7.8.0/24
          Metric: 1          IP-Extended 10.196.7.7/32
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
          IP Address:     10.16.2.2
          Metric: 10         IP-Extended 10.16.2.2/32
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
          IP Address:     10.36.3.3
          Metric: 10         IP-Extended 10.36.3.0/24
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
          IP Address:     10.100.5.5
          Metric: 10         IP-Extended 10.100.5.5/32
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
          Router ID:      10.196.7.7
          IP Address:     10.196.7.7
          MT:             IPv6 Unicast                                 0/0/0
          MT:             Standard (IPv4 Unicast)
          Hostname:       R7
          Metric: 40         MT (IPv6 Unicast) IS-Extended R9.01
          Metric: 40         MT (IPv6 Unicast) IS-Extended R8.01
          Metric: 40         IS-Extended R9.01
          Metric: 40         IS-Extended R8.01
          Metric: 40         IP-Extended 10.6.7.0/24
          Metric: 1          IP-Extended 10.196.7.7/32
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
          IP Address:     10.1.8.8
          Metric: 10         IP-Extended 10.1.8.8/32
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
          IP Address:     10.69.9.9
          Metric: 10         IP-Extended 10.69.9.9/32
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
                                "ip_address": "172.16.186.5",
                                "ip_neighbor": {
                                    "172.16.115.0/24": {
                                        "ip_prefix": "172.16.115.0",
                                        "prefix_length": "24",
                                        "metric": 0,
                                    },
                                    "172.16.166.0/24": {
                                        "ip_prefix": "172.16.166.0",
                                        "prefix_length": "24",
                                        "metric": 10,
                                    },
                                    "172.16.166.0/24": {
                                        "ip_prefix": "172.16.166.0",
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
                                "ip_address": "172.16.196.11",
                                "ip_neighbor": {
                                    "172.16.76.0/24": {
                                        "ip_prefix": "172.16.76.0",
                                        "prefix_length": "24",
                                        "metric": 0,
                                    },
                                    "172.16.166.0/24": {
                                        "ip_prefix": "172.16.166.0",
                                        "prefix_length": "24",
                                        "metric": 10,
                                    },
                                    "172.16.166.0/24": {
                                        "ip_prefix": "172.16.166.0",
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
                                "ip_address": "172.16.166.5",
                                "ip_neighbor": {
                                    "172.16.115.0/24": {
                                        "ip_prefix": "172.16.115.0",
                                        "prefix_length": "24",
                                        "metric": 0,
                                    },
                                    "172.16.166.0/24": {
                                        "ip_prefix": "172.16.166.0",
                                        "prefix_length": "24",
                                        "metric": 10,
                                    },
                                    "172.16.94.0/24": {
                                        "ip_prefix": "172.16.94.0",
                                        "prefix_length": "24",
                                        "metric": 10,
                                    },
                                    "172.16.21.0/24": {
                                        "ip_prefix": "172.16.21.0",
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
                                    "172.16.21.0/24": {
                                        "ip_prefix": "172.16.21.0",
                                        "prefix_length": "24",
                                        "metric": 0,
                                    },
                                    "172.16.166.0/24": {
                                        "ip_prefix": "172.16.166.0",
                                        "prefix_length": "24",
                                        "metric": 10,
                                    },
                                    "172.16.166.0/24": {
                                        "ip_prefix": "172.16.166.0",
                                        "prefix_length": "24",
                                        "metric": 10,
                                    },
                                    "172.16.115.0/24": {
                                        "ip_prefix": "172.16.115.0",
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
              IP Address:  172.16.186.5
              Metric: 0          IP 172.16.115.0/24
              Metric: 10         IP 172.16.166.0/24
              Metric: 10         IP 172.16.166.0/24
              Metric: 10         IS router-11.00
              Metric: 10         IS router-11.01
            router-11.00-00  * 0x0000000b   0x8074460        1161            0/0/0
              Area Address: 49
              NLPID:       0xcc
              Hostname:    router-11
              IP Address:  172.16.196.11
              Metric: 0          IP 172.16.76.0/24
              Metric: 10         IP 172.16.166.0/24
              Metric: 10         IP 172.16.166.0/24
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
              IP Address:  172.16.166.5
              Metric: 0          IP 172.16.115.0/24
              Metric: 10         IP 172.16.166.0/24
              Metric: 10         IP 172.16.94.0/24
              Metric: 10         IS router-11.00
              Metric: 10         IS router-11.01
              Metric: 10         IP 172.16.21.0/24
            router-11.00-00  * 0x0000000d   0x807997c        1184            0/0/0
              Area Address: 49
              NLPID:       0xcc
              Hostname:    router-11
              IP Address:  172.28.111.111
              Metric: 0          IP 172.16.21.0/24
              Metric: 10         IP 172.16.166.0/24
              Metric: 10         IP 172.16.166.0/24
              Metric: 10         IS router-11.01
              Metric: 10         IS router-5.00
              Metric: 10         IP 172.16.115.0/24
            router-gsr11.01-00  * 0x00000001   0x80770ec        457             0/0/0
              Metric: 0          IS router-11.00
              Metric: 0          IS router-5.00
             Total LSP count: 3 (L1: 0, L2 3, local L1: 0, local L2 2)
    '''}

    golden_parsed_output_3 = {
        "instance": {
            "": {
                "level": {
                    1: {
                        "lspid": {
                            "0000.0CFF.0C35.00-00": {
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
                                    "0000.0CFF.62E6.03": {
                                        "metric": 10}},
                                "es_neighbor": {
                                    "0000.0CFF.0C35": {
                                        "metric": 0}},
                            },
                            "0000.0CFF.40AF.00-00": {
                                "lsp": {
                                    "seq_num": "0x00000009",
                                    "checksum": "0x8452",
                                    "local_router": True,
                                    "holdtime": 608,
                                    "attach_bit": 1,
                                    "p_bit": 0,
                                    "overload_bit": 0,
                                },
                                "area_address": "47.0004.00FF.4D4E",
                                "topology": ["IPv4 (0x0)", "IPv6 (0x2)"],
                                "nlpid": ["0x8E"],
                                "ip_address": "172.16.21.49",
                                "is_neighbor": {
                                    "0800.2BFF.3A01.01": {
                                        "metric": 10},
                                    "0000.0CFF.62E6.03": {
                                        "metric": 10},
                                    "cisco.03": {
                                        "metric": 10},
                                },
                                "es_neighbor": {
                                    "0000.0CFF.40AF": {
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
        0000.0CFF.0C35.00-00  0x0000000C   0x5696        325           0/0/0
          Area Address: 47.0004.00FF.4D4E
          Area Address: 39.0001
          Metric: 10   IS 0000.0CFF.62E6.03
          Metric: 0    ES 0000.0CFF.0C35
        0000.0CFF.40AF.00-00* 0x00000009   0x8452        608           1/0/0
          Area Address: 47.0004.00FF.4D4E
          Topology: IPv4 (0x0) IPv6 (0x2)
          NLPID: 0xCC 0x8E
          IP Address: 172.16.21.49
          Metric: 10   IS 0800.2BFF.3A01.01
          Metric: 10   IS 0000.0CFF.62E6.03
          Metric: 0    ES 0000.0CFF.40AF
          IPv6 Address: 2001:0DB8::/32
          Metric: 10   IPv6 (MT-IPv6) 2001:0DB8::/64
          Metric: 5    IS-Extended cisco.03
          Metric: 10   IS-Extended cisco1.03
          Metric: 10    IS (MT-IPv6) cisco.03
    '''}

    golden_parsed_output_4 = {
        'instance': {
            'Genie': {
                'level': {
                    2: {
                        'lspid': {
                            'core1-genie.00-00': {
                                'lsp': {
                                    'seq_num': '0x0000a302',
                                    'checksum': '0x1a0e',
                                    'local_router': False,
                                    'holdtime': 58285,
                                    'received': 65534,
                                    'attach_bit': 0,
                                    'p_bit': 0,
                                    'overload_bit': 0,
                                },
                                'area_address': '49.0000',
                                'nlpid': ['0xcc'],
                                'ip_address': '10.154.219.57',
                                'hostname': 'core1-genie',
                                'router_cap': '10.154.219.57 D:0 S:0',
                                'extended_ipv4_reachability': {
                                    '10.154.219.57/32': {
                                        'ip_prefix': '10.154.219.57',
                                        'prefix_length': '32',
                                        'metric': 0,
                                    },
                                },
                                'extended_is_neighbor': {
                                    'core2-genie.00': {
                                        'metric': 50,
                                    },
                                    'tcore4-genie.00': {
                                        'metric': 250,
                                    },
                                    'bl1-genie.00': {
                                        'metric': 1000,
                                    },
                                    'bl2-genie.00': {
                                        'metric': 1000,
                                    },
                                },
                            },
                            'core2-genie.00-00': {
                                'lsp': {
                                    'seq_num': '0x0000a15b',
                                    'checksum': '0xfcfe',
                                    'local_router': False,
                                    'holdtime': 60939,
                                    'received': 65534,
                                    'attach_bit': 0,
                                    'p_bit': 0,
                                    'overload_bit': 0,
                                },
                                'area_address': '49.0000',
                                'nlpid': ['0xcc'],
                                'ip_address': '10.154.219.58',
                                'hostname': 'core2-genie',
                                'router_cap': '10.154.219.58 D:0 S:0',
                                'extended_ipv4_reachability': {
                                    '10.154.219.58/32': {
                                        'ip_prefix': '10.154.219.58',
                                        'prefix_length': '32',
                                        'metric': 0,
                                    },
                                },
                                'extended_is_neighbor': {
                                    'core1-genie.00': {
                                        'metric': 50,
                                    },
                                    'bl2-genie.00': {
                                        'metric': 1000,
                                    },
                                    'bl1-genie.00': {
                                        'metric': 1000,
                                    },
                                    'tcore3-genie.00': {
                                        'metric': 250,
                                    },
                                },
                            },
                            'dis17-genie_RE1.00-00': {
                                'lsp': {
                                    'seq_num': '0x00000215',
                                    'checksum': '0xf5f4',
                                    'local_router': False,
                                    'holdtime': 32551,
                                    'received': 65535,
                                    'attach_bit': 0,
                                    'p_bit': 0,
                                    'overload_bit': 0,
                                },
                                'area_address': '49.0000',
                                'tlv': 14,
                                'tlv_length': 2,
                                'nlpid': ['0xcc', '0x8e'],
                                'router_id': '10.154.219.102',
                                'ip_address': '10.154.219.102',
                                'hostname': 'dis17-genie_RE1',
                                'extended_is_neighbor': {
                                    'tcore4-genie.00': {
                                        'metric': 100,
                                    },
                                    'tcore3-genie.00': {
                                        'metric': 100,
                                    },
                                },
                                'extended_ipv4_reachability': {
                                    '10.154.219.102/32': {
                                        'ip_prefix': '10.154.219.102',
                                        'prefix_length': '32',
                                        'metric': 0,
                                    },
                                },
                                'router_cap': '10.154.219.102 D:0 S:0',
                            },
                        },
                    },
                },
            },
        },
    }

    golden_output_4 = {'execute.return_value': '''
        show isis database detail

        Mon Oct 22 10:40:56.529 EDT

        IS-IS Genie (Level-2) Link State Database
        LSPID                 LSP Seq Num  LSP Checksum  LSP Holdtime/Rcvd  ATT/P/OL
        core1-genie.00-00  0x0000a302   0x1a0e        58285/65534        0/0/0
        Area Address:   49.0000
        NLPID:          0xcc
        IP Address:     10.154.219.57
        Hostname:       core1-genie
        Router Cap:     10.154.219.57 D:0 S:0
        Metric: 0          IP-Extended 10.154.219.57/32
        Metric: 50         IS-Extended core2-genie.00
        Metric: 250        IS-Extended tcore4-genie.00
        Metric: 1000       IS-Extended bl1-genie.00
        Metric: 1000       IS-Extended bl2-genie.00
        core2-genie.00-00  0x0000a15b   0xfcfe        60939/65534        0/0/0
        Area Address:   49.0000
        NLPID:          0xcc
        IP Address:     10.154.219.58
        Hostname:       core2-genie
        Router Cap:     10.154.219.58 D:0 S:0
        Metric: 0          IP-Extended 10.154.219.58/32
        Metric: 50         IS-Extended core1-genie.00
        Metric: 1000       IS-Extended bl2-genie.00
        Metric: 1000       IS-Extended bl1-genie.00
        Metric: 250        IS-Extended tcore3-genie.00
        dis17-genie_RE1.00-00  0x00000215   0xf5f4        32551/65535        0/0/0
        Area Address:   49.0000
        TLV 14:         Length: 2
        NLPID:          0xcc
        NLPID:          0x8e
        Router ID:      10.154.219.102
        IP Address:     10.154.219.102
        Hostname:       dis17-genie_RE1
        Metric: 100        IS-Extended tcore4-genie.00
        Metric: 100        IS-Extended tcore3-genie.00
        Metric: 0          IP-Extended 10.154.219.102/32
        Router Cap:     10.154.219.102 D:0 S:0
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

    def test_output_4(self):
        self.device = Mock(**self.golden_output_4)
        obj = ShowIsisDatabaseDetail(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_4)

class TestShowIsisPrivateAll(unittest.TestCase):

    maxDiff = None
    empty_output = {'execute.return_value': ''}

    golden_parsed_output = {
        'instance': {
            'TEST': {
                'cfg_refcount': 57,
                'isis_is_level': 'level-2-only',
                'ignore_cksum_errs': True,
                'cfg_log_drops': False,
                'nsf_cfg_purgetime': 90,
                'nsf2_t1_delay': 1,
                'nsf2_t1_max_num_exp': 10,
                'nsf_cfg_interval': 300,
                'address_family_table': {
                    'IPv4': {
                        'ref_count': 1,
                    },
                    'IPv6': {
                        'ref_count': 0,
                    },
                },
                'link_topology_table': {
                    'Standard (IPv4 Unicast)': {
                        'ref_count': 1,
                        'index': 0,
                        'is_running': True,
                        'list_linkage': {
                            'next': '0x0',
                            'previous': '0x44b3f24',
                        },
                    },
                },
                'topology_table': {
                    'IPv4 Unicast': {
                        'configuration': {
                            'check_adjacencies': '(not set)',
                            'attached_bit': '(not set)',
                            'max_paths': '(not set)',
                            'is_mcast_intact_set': False,
                            'mcast_intact': False,
                            'is_igp_intact_set': False,
                            'igp_intact': False,
                            'is_first_hop_source_set': False,
                            'first_hop_source': False,
                        },
                        'ref_count': 23,
                        'index': 0,
                        'ltopo_index': 0,
                        'list_linkage': {
                            'next': '0x0',
                            'previous': '0x44b51fc',
                        },
                    },
                },
                'area_configuration_table': {
                    'cross_level': {
                        'is_lsp_gen_interval_set': True,
                        'lsp_gen_interval': {
                            'initial_wait_msecs': 20,
                            'secondary_wait_msecs': 100,
                            'maximum_wait_msecs': 5000,
                        },
                        'is_lsp_arrivaltime_parameter_set': False,
                        'lsp_arrivaltime_parameter': {
                            'backoff_cfg': {
                                'initial_wait_msecs': 50,
                                'secondary_wait_msecs': 200,
                                'maximum_wait_msecs': 5000,
                            },
                            'max_count': 0,
                            'max_window_size_msec': 120001,
                        },
                        'is_lsp_checksum_interval_set': False,
                        'lsp_checksum_interval_secs': 0,
                        'is_lsp_refresh_interval_set': True,
                        'lsp_refresh_interval_secs': 35000,
                        'is_lsp_lifetime_set': True,
                        'lsp_lifetime_secs': 65535,
                        'is_lsp_mtu_set': False,
                        'lsp_mtu': 0,
                        'is_auth_cfg_ctx_set': False,
                        'auth_cfg_ctx': {
                            'alg': 'None',
                            'failure_mode': 'Drop',
                            'password': '0xdecafbad',
                            'accept_password': '0xdecafbad',
                        },
                        'is_snp_authentication_options_set': False,
                        'snp_authentication_options': 0,
                        'is_overload_set': False,
                        'overload_mode': -1,
                        'overload_on_startup_secs': 0,
                        'per_topo': {
                            'IPv4 Unicast': {
                                'is_metric_style_set': True,
                                'generate_metric_mask': 2,
                                'accept_metric_mask': 2,
                                'summary_table': '0x15431f50',
                                'metric': 100000,
                                'is_spf_interval_set': True,
                                'spf_interval': {
                                    'initial_wait_msecs': 50,
                                    'secondary_wait_msecs': 150,
                                    'maximum_wait_msecs': 5000,
                                },
                                'spf_periodic_interval_secs': '(not set)',
                                'ispf_state': '(not set)',
                                'max_redist_prefixes': '(not set)',
                                'topo_index': {
                                    0: {
                                        'is_spf_prefix_priority_acl_names_set': False,
                                        'spf_prefix_priority_acl_names': '0x0',
                                        'is_spf_prefix_priority_tags_set': False,
                                        'spf_prefix_priority_tags': 0,
                                    },
                                    1: {
                                        'is_spf_prefix_priority_acl_names_set': True,
                                        'spf_prefix_priority_acl_names': '0x154b92c4',
                                        'is_spf_prefix_priority_tags_set': False,
                                        'spf_prefix_priority_tags': 0,
                                    },
                                    2: {
                                        'is_spf_prefix_priority_acl_names_set': True,
                                        'spf_prefix_priority_acl_names': '0x155a0e3c',
                                        'is_spf_prefix_priority_tags_set': False,
                                        'spf_prefix_priority_tags': 0,
                                    },
                                    3: {
                                        'is_spf_prefix_priority_acl_names_set': False,
                                        'spf_prefix_priority_acl_names': '0x0',
                                        'is_spf_prefix_priority_tags_set': False,
                                        'spf_prefix_priority_tags': 0,
                                    },
                                },
                            },
                        },
                    },
                    'level-1': {
                        'is_lsp_gen_interval_set': False,
                        'lsp_gen_interval': {
                            'initial_wait_msecs': 50,
                            'secondary_wait_msecs': 200,
                            'maximum_wait_msecs': 5000,
                        },
                        'is_lsp_arrivaltime_parameter_set': False,
                        'lsp_arrivaltime_parameter': {
                            'backoff_cfg': {
                                'initial_wait_msecs': 50,
                                'secondary_wait_msecs': 200,
                                'maximum_wait_msecs': 5000,
                            },
                            'max_count': 0,
                            'max_window_size_msec': 120001,
                        },
                        'is_lsp_checksum_interval_set': False,
                        'lsp_checksum_interval_secs': 0,
                        'is_lsp_refresh_interval_set': False,
                        'lsp_refresh_interval_secs': 0,
                        'is_lsp_lifetime_set': False,
                        'lsp_lifetime_secs': 0,
                        'is_lsp_mtu_set': False,
                        'lsp_mtu': 0,
                        'is_auth_cfg_ctx_set': False,
                        'auth_cfg_ctx': {
                            'alg': 'None',
                            'failure_mode': 'Drop',
                            'password': '0xdecafbad',
                            'accept_password': '0xdecafbad',
                        },
                        'is_snp_authentication_options_set': False,
                        'snp_authentication_options': 0,
                        'is_overload_set': False,
                        'overload_mode': 0,
                        'overload_on_startup_secs': 0,
                        'per_topo': {
                            'IPv4 Unicast': {
                                'is_metric_style_set': False,
                                'generate_metric_mask': 0,
                                'accept_metric_mask': 0,
                                'summary_table': '0x15431fac',
                                'metric': '(not set)',
                                'is_spf_interval_set': False,
                                'spf_interval': {
                                    'initial_wait_msecs': 50,
                                    'secondary_wait_msecs': 200,
                                    'maximum_wait_msecs': 5000,
                                },
                                'spf_periodic_interval_secs': '(not set)',
                                'ispf_state': '(not set)',
                                'max_redist_prefixes': '(not set)',
                                'topo_index': {
                                    0: {
                                        'is_spf_prefix_priority_acl_names_set': False,
                                        'spf_prefix_priority_acl_names': '0x0',
                                        'is_spf_prefix_priority_tags_set': False,
                                        'spf_prefix_priority_tags': 0,
                                    },
                                    1: {
                                        'is_spf_prefix_priority_acl_names_set': False,
                                        'spf_prefix_priority_acl_names': '0x0',
                                        'is_spf_prefix_priority_tags_set': False,
                                        'spf_prefix_priority_tags': 0,
                                    },
                                    2: {
                                        'is_spf_prefix_priority_acl_names_set': False,
                                        'spf_prefix_priority_acl_names': '0x0',
                                        'is_spf_prefix_priority_tags_set': False,
                                        'spf_prefix_priority_tags': 0,
                                    },
                                    3: {
                                        'is_spf_prefix_priority_acl_names_set': False,
                                        'spf_prefix_priority_acl_names': '0x0',
                                        'is_spf_prefix_priority_tags_set': False,
                                        'spf_prefix_priority_tags': 0,
                                    },
                                },
                            },
                        },
                    },
                    'level-2': {
                        'is_lsp_gen_interval_set': False,
                        'lsp_gen_interval': {
                            'initial_wait_msecs': 50,
                            'secondary_wait_msecs': 200,
                            'maximum_wait_msecs': 5000,
                        },
                        'is_lsp_arrivaltime_parameter_set': False,
                        'lsp_arrivaltime_parameter': {
                            'backoff_cfg': {
                                'initial_wait_msecs': 50,
                                'secondary_wait_msecs': 200,
                                'maximum_wait_msecs': 5000,
                            },
                            'max_count': 0,
                            'max_window_size_msec': 120001,
                        },
                        'is_lsp_checksum_interval_set': False,
                        'lsp_checksum_interval_secs': 0,
                        'is_lsp_refresh_interval_set': False,
                        'lsp_refresh_interval_secs': 0,
                        'is_lsp_lifetime_set': False,
                        'lsp_lifetime_secs': 0,
                        'is_lsp_mtu_set': False,
                        'lsp_mtu': 0,
                        'is_auth_cfg_ctx_set': False,
                        'auth_cfg_ctx': {
                            'alg': 'None',
                            'failure_mode': 'Drop',
                            'password': '0xdecafbad',
                            'accept_password': '0xdecafbad',
                        },
                        'is_snp_authentication_options_set': False,
                        'snp_authentication_options': 0,
                        'is_overload_set': False,
                        'overload_mode': 0,
                        'overload_on_startup_secs': 0,
                        'per_topo': {
                            'IPv4 Unicast': {
                                'is_metric_style_set': False,
                                'generate_metric_mask': 0,
                                'accept_metric_mask': 0,
                                'summary_table': '0x1539cef4',
                                'metric': '(not set)',
                                'is_spf_interval_set': False,
                                'spf_interval': {
                                    'initial_wait_msecs': 50,
                                    'secondary_wait_msecs': 200,
                                    'maximum_wait_msecs': 5000,
                                },
                                'spf_periodic_interval_secs': '(not set)',
                                'ispf_state': '(not set)',
                                'max_redist_prefixes': '(not set)',
                                'topo_index': {
                                    0: {
                                        'is_spf_prefix_priority_acl_names_set': False,
                                        'spf_prefix_priority_acl_names': '0x0',
                                        'is_spf_prefix_priority_tags_set': False,
                                        'spf_prefix_priority_tags': 0,
                                    },
                                    1: {
                                        'is_spf_prefix_priority_acl_names_set': False,
                                        'spf_prefix_priority_acl_names': '0x0',
                                        'is_spf_prefix_priority_tags_set': False,
                                        'spf_prefix_priority_tags': 0,
                                    },
                                    2: {
                                        'is_spf_prefix_priority_acl_names_set': False,
                                        'spf_prefix_priority_acl_names': '0x0',
                                        'is_spf_prefix_priority_tags_set': False,
                                        'spf_prefix_priority_tags': 0,
                                    },
                                    3: {
                                        'is_spf_prefix_priority_acl_names_set': False,
                                        'spf_prefix_priority_acl_names': '0x0',
                                        'is_spf_prefix_priority_tags_set': False,
                                        'spf_prefix_priority_tags': 0,
                                    },
                                },
                            },
                        },
                    },
                },
                'area_tables': {
                    'level-2': {
                        'index': 1,
                        'idb_list': {
                            'sll_head': '0x151942e0',
                            'sll_tail': '0x15193fd4',
                            'sll_count': 8,
                            'sll_maximum': 0,
                        },
                        'list_linkage': {
                            'next': '0x0',
                            'previous': '0x44b2534',
                        },
                        'adj_db': '0x1540cee4',
                        'adj_log': '0x1539b844',
                        'uni_db_log': '0x15411024',
                        'upd_db': {
                            'lock': {
                                'rwlock': {
                                    'active': 0,
                                    'spare': '0x0',
                                    'blockedwriters': 0,
                                    'blockedreaders': 0,
                                    'heavy': 0,
                                    'lock': {
                                        'count': -2147483648,
                                        'owner': 0,
                                    },
                                    'owner': 4294967294,
                                },
                                'description': '0x15393cf0',
                            },
                            'tree': {
                                'root': '0x0',
                                'key_size': 8,
                                'size': 0,
                                'node_alloc_data': '0x15393cd0',
                                'node_alloc_fn': '0x42fd024',
                                'node_free_fn': '0x42fd08a',
                                'data_to_str_fn': '0x42fd094',
                            },
                            'tree_node_chunks': {
                                'name': '0x448764c',
                                'size': 28,
                                'flags': 1297,
                                'chunk': '0x1543146c',
                                'num_allocated_elements': 0,
                            },
                            'area': '0x15393bfc',
                            'log': '0x15432024',
                            'name': 'L2 Update DB',
                        },
                        'nsf_ietf_csnp_rcvd': False,
                        'overload_bit_on_startup_timer': '0x15017530',
                        'overload_bit_trigger_expired': True,
                        'upd_periodic_timer': '0x150174d0',
                        'checksum_ptimer': {
                            'tv_sec': 3657420,
                            'tv_nsec': 458761224,
                        },
                        'dec_db': {
                            'lock': {
                                'rwlock': {
                                    'active': 0,
                                    'spare': '0x0',
                                    'blockedwriters': 0,
                                    'blockedreaders': 0,
                                    'heavy': 0,
                                    'lock': {
                                        'count': -2147483648,
                                        'owner': 0,
                                    },
                                    'owner': 4294967294,
                                },
                                'description': '0x153942b0',
                            },
                            'tree': {
                                'root': '0x1539f9d4',
                                'key_size': 8,
                                'size': 82,
                                'node_alloc_data': '0x15394290',
                                'node_alloc_fn': '0x42fd024',
                                'node_free_fn': '0x42fd08a',
                                'data_to_str_fn': '0x42fd094',
                            },
                            'tree_node_chunks': {
                                'name': '0x448764c',
                                'size': 28,
                                'flags': 1297,
                                'chunk': '0x1539f844',
                                'num_allocated_elements': 82,
                            },
                            'area': '0x15393bfc',
                            'log': '0x15453024',
                            'name': 'L2 Decision DB',
                        },
                        'node_db': {
                            'node_created_fn': '0x424fd84',
                            'node_destroyed_fn': '0x424ffa6',
                            'node_ltopo_created_fn': '0x42500b6',
                            'node_ltopo_destroyed_fn': '0x42503ba',
                            'node_topo_created_fn': '0x4250536',
                            'node_topo_destroyed_fn': '0x42506b4',
                            'callback_context': '0x15393bfc',
                            'root_element': '0x151fb9bc',
                            'num_nodes': 64,
                        },
                        'stats': {
                            'ta_lsp_build': 850,
                            'ta_lsp_refresh': 219,
                        },
                        'trap_stats': {
                            'corr_lsps': 0,
                            'auth_type_fails': 0,
                            'auth_fails': 0,
                            'lsp_dbase_oloads': 4,
                            'man_addr_drop_from_areas': 0,
                            'attmpt_to_ex_max_seq_nums': 0,
                            'seq_num_skips': 1,
                            'own_lsp_purges': 3,
                            'id_field_len_mismatches': 0,
                            'lsp_errors': 0,
                        },
                        'per_ltopo': {
                            'Standard (IPv4 Unicast)': {
                                'area': '0x15393bfc',
                                'ltopo_index': 'Standard (IPv4 Unicast)',
                                'roca_event': {
                                    'mutex': {
                                        'mutex': {
                                            'count': -2147483648,
                                            'owner': 0,
                                        },
                                        'description': '0x1500ee28',
                                    },
                                    'timer': {
                                        'timer': '0x150179bc',
                                        'num_execution_events': 1,
                                        'is_pending': False,
                                        'is_executing': False,
                                        'postponed_schedule_time': {
                                            'tv_sec': 0,
                                            'tv_nsec': 0,
                                        },
                                        'last_execution_time': {
                                            'tv_sec': 3657197,
                                            'tv_nsec': 824108467,
                                        },
                                    },
                                    'log': '0x15474024',
                                    'class': '<error>',
                                },
                                'spf_periodic_timer': '0x1501798c',
                                'paths': {
                                    'classification': 0,
                                    'is_sorted': False,
                                    'array': '0x1540d45c',
                                    'num_elements': 64,
                                },
                                'unreached': {
                                    'classification': 0,
                                    'is_sorted': False,
                                    'array': '0x1540d4b4',
                                    'num_elements': 0,
                                },
                                'firsthopchanged': {
                                    'classification': 0,
                                    'is_sorted': True,
                                    'array': '0x1540d4e0',
                                    'num_elements': 0,
                                },
                                'linkchanged': {
                                    'classification': 2,
                                    'is_sorted': True,
                                    'array': '0x1540d66c',
                                    'num_elements': 0,
                                },
                                'reachable_area_addresses': '0x1540d430',
                                'stats': {
                                    'num_spfs': 5004,
                                    'num_ispfs': 0,
                                    'num_nhcs': 10,
                                    'num_prcs': 1219,
                                    'num_periodic_spfs': 3876,
                                },
                            },
                        },
                        'per_topo': {
                            'IPv4 Unicast': {
                                'area': '0x15393bfc',
                                'topo_index': 'IPv4 Unicast',
                                'te': {
                                    'link_holddown_timer': '0x150181cc',
                                    'purge_link_info_timer': '0x1501819c',
                                    'log': '0x153a8d24',
                                    'tunnel_table': '0x153ab844',
                                    'info_from_te': '0x0',
                                    'pce_info_from_te': '0x0',
                                    'is_pce_ready': False,
                                },
                                'overloaded_count': 0,
                                'overload_bit_trigger_running': False,
                                'bgp_converged_notify_h': '0x0',
                                'added_first_hops': '0x0',
                                'deleted_first_hops': '0x0',
                                'postponed_added_first_hops': '0x0',
                                'postponed_deleted_first_hops': '0x0',
                                'prefixeschanged': '0x0',
                                'nodechanged': '0x0',
                                'prefix_priority_acl': {
                                    'critical': '0x0',
                                    'high': '0x15604868',
                                    'medium': '0x156047dc',
                                    'low': '0x0',
                                },
                                'num_redist_prefixes': 166,
                                'max_redist_prefixes_exceeded': False,
                                'max_redist_prefixes_alarm_on': False,
                                'has_prefix_policy_changed': False,
                            },
                        },
                        'per_af': {
                            'IPv4': {
                                'router_id': '0x15192388',
                            },
                            'IPv6': {
                                'router_id': '0x0',
                            },
                        },
                    },
                },
                'interfaces': {
                    'TenGigE0/0/1/3': {
                        'im_handle': '0x180',
                        'name': 'TenGigE0_0_1_3',
                        'ref_count': 2,
                        'index': 4,
                        'snmp_index': 21,
                        'chkpt': {
                            'objid': '0x0',
                        },
                        'cfg': {
                            'refcount': 7,
                            'is_p2p': True,
                            'enabled_mode': 'Active',
                            'circuit_type': 'level-1-2',
                            'ipv4_bfd_enabled': True,
                            'ipv6_bfd_enabled': False,
                            'bfd_interval': 250,
                            'bfd_multiplier': 3,
                            'topos': 'IPv4 Unicast',
                            'cross_levels': {
                                'per_topo': {
                                    'IPv4 Unicast': {
                                        'metric': 10,
                                        'weight': '(not set)',
                                        'ldp_sync_cfg': '(not set)',
                                        'admin_tag': '(not set)',
                                        'frr_type': '(not set)',
                                        'is_lkgp_set': 0,
                                    },
                                },
                                'is_auth_cfg_ctx_set': False,
                                'auth_cfg_ctx': {
                                    'alg': 'None',
                                    'failure_mode': 'Drop',
                                    'password': '0x0',
                                    'accept_password': '0x0',
                                },
                                'hello_interval_msecs': '(not set)',
                                'hello_multiplier': '(not set)',
                                'csnp_interval_secs': '(not set)',
                                'lsp_pacing_interval_msecs': '(not set)',
                                'lsp_fast_flood_threshold': '(not set)',
                                'lsp_rexmit_interval_secs': '(not set)',
                                'min_lsp_rexmit_interval_msecs': '(not set)',
                                'dr_priority': '(not set)',
                                'is_hello_padding_set': False,
                                'hello_padding': 'Never',
                            },
                            'per_level': {
                                'Level-1': {
                                    'per_topo': {
                                        'IPv4 Unicast': {
                                            'metric': '(not set)',
                                            'weight': '(not set)',
                                            'ldp_sync_cfg': '(not set)',
                                            'admin_tag': '(not set)',
                                            'frr_type': '(not set)',
                                            'is_lkgp_set': 0,
                                        },
                                    },
                                    'is_auth_cfg_ctx_set': False,
                                    'auth_cfg_ctx': {
                                        'alg': 'None',
                                        'failure_mode': 'Drop',
                                        'password': '0x0',
                                        'accept_password': '0x0',
                                    },
                                    'hello_interval_msecs': '(not set)',
                                    'hello_multiplier': '(not set)',
                                    'csnp_interval_secs': '(not set)',
                                    'lsp_pacing_interval_msecs': '(not set)',
                                    'lsp_fast_flood_threshold': '(not set)',
                                    'lsp_rexmit_interval_secs': '(not set)',
                                    'min_lsp_rexmit_interval_msecs': '(not set)',
                                    'dr_priority': '(not set)',
                                    'is_hello_padding_set': False,
                                    'hello_padding': 'Never',
                                },
                                'Level-2': {
                                    'per_topo': {
                                        'IPv4 Unicast': {
                                            'metric': '(not set)',
                                            'weight': '(not set)',
                                            'ldp_sync_cfg': '(not set)',
                                            'admin_tag': '(not set)',
                                            'frr_type': '(not set)',
                                            'is_lkgp_set': 0,
                                        },
                                    },
                                    'is_auth_cfg_ctx_set': False,
                                    'auth_cfg_ctx': {
                                        'alg': 'None',
                                        'failure_mode': 'Drop',
                                        'password': '0x0',
                                        'accept_password': '0x0',
                                    },
                                    'hello_interval_msecs': '(not set)',
                                    'hello_multiplier': '(not set)',
                                    'csnp_interval_secs': '(not set)',
                                    'lsp_pacing_interval_msecs': '(not set)',
                                    'lsp_fast_flood_threshold': '(not set)',
                                    'lsp_rexmit_interval_secs': '(not set)',
                                    'min_lsp_rexmit_interval_msecs': '(not set)',
                                    'dr_priority': '(not set)',
                                    'is_hello_padding_set': False,
                                    'hello_padding': 'Never',
                                },
                            },
                        },
                        'per_topo': {
                            'IPv4 Unicast': {
                                'refcount': 2,
                            },
                        },
                        'topos_enabled_active': 'IPv4 Unicast',
                        'per_area': {
                            'Level-2': {
                                'area_linkage': '0x15194244',
                                'idb': '0x151916d8',
                                'area': '0x15393bfc',
                                'adj_filter': '0x0',
                                'csnp_control': {
                                    'timer': '0x0',
                                    'next_lsp_id': '0000.0000.0000.00-00',
                                    'building_packets': False,
                                },
                                'psnp_timer': '0x0',
                                'nsf_ietf': {
                                    'full_csnp_set_rcvd': False,
                                    'csnp_set_rcvd': {
                                        'list_head': '0x0',
                                        'list_size': 0,
                                    },
                                },
                                'adj_up_count': 0,
                                'lan_adj_up_count': 0,
                                'adj_list': '0x0',
                                'per_ltopo': {
                                    'Standard (IPv4 Unicast)': {
                                        'num_requested_adjs': 0,
                                        'num_adjs': 0,
                                    },
                                },
                                'tmrs_active': False,
                                'adj_filter_match_all': False,
                                'lsp_count': {
                                    'in': 24185,
                                    'out': 140529,
                                },
                                'csnp_count': {
                                    'in': 17,
                                    'out': 17,
                                },
                                'psnp_count': {
                                    'in': 134275,
                                    'out': 23143,
                                },
                                'lsp_flooding_dup_count': 3,
                                'lsp_drop_count': 0,
                            },
                        },
                        'media': {
                            '0x440cbe0': {
                                'caps_id': 30,
                                'media_class': 'LAN',
                                'encaps_overhead': 3,
                            },
                        },
                        'media_specific': {
                            'p2p': {
                                'hello_timer': '0x156bace8',
                                'last_hello': {
                                    'tv_sec': 0,
                                    'tv_nsec': 0,
                                },
                                'recent_hello_send_count': 0,
                                'adj_state': 2,
                                'do_ietf_3way': True,
                                'received_ietf_3way': False,
                                'neighbor_extended_circuit_number': 0,
                                'neighbor_system_id': '0000.0000.0000',
                                'mib_counters': {
                                    'circuit_type': 0,
                                    'adj_changes': 29,
                                    'num_adj': 0,
                                    'init_fails': 0,
                                    'rej_adjs': 0,
                                    'id_field_len_mismatches': 0,
                                    'max_area_addr_mismatches': 0,
                                    'auth_type_fails': 0,
                                    'auth_fails': 0,
                                    'lan_des_is_canges': 0,
                                    'index': 0,
                                },
                                'init_csnp_wait': {
                                    'tv_sec': 0,
                                    'tv_nsec': 0,
                                },
                                'lsp_rexmit_queue': {
                                    'sll_head': '0x0',
                                    'sll_tail': '0x0',
                                    'sll_count': 0,
                                    'sll_maximum': 0,
                                },
                                'lsp_rexmit_timer': '0x157111ac',
                                'nsf_ietf': {
                                    't1_timer': '0x156bacb8',
                                    'num_t1_expiries': 0,
                                    'first_t1_expiry_seen': False,
                                    'rr_sent': False,
                                    'ra_rcvd': False,
                                    'all_ra_seen': False,
                                    'ra_required_nbr_count': 0,
                                },
                                'stats': {
                                    'iih_count': {
                                        'in': 160726,
                                        'out': 160689,
                                    },
                                    'iih_nomem': 0,
                                    'lsp_retransmits': 72,
                                },
                                'p2p_over_lan': {
                                    'mcast_state': {
                                        'is_mcast_group_member': True,
                                        'mcast_join_reason': 2,
                                    },
                                    'snpa_info': {
                                        'im_attr_macaddr_notify_handle': '0x1514d188',
                                        'snpa': '00c1.64ff.4ef2',
                                        'is_snpa_ok': True,
                                    },
                                },
                            },
                        },
                        'clns': {
                            'im_node': {
                                'exist_registered': True,
                                'node_exists': True,
                                'state_registered': True,
                                'node_up': False,
                            },
                            'mtu': 9199,
                        },
                        'per_af': {
                            'IPv4': {
                                'im_node': {
                                    'exist_registered': True,
                                    'node_exists': True,
                                    'state_registered': True,
                                    'node_up': False,
                                },
                                'local_address': '0.0.0.0',
                                'is_nexthop_addr_registered': True,
                                'is_global_prefix_registered': False,
                                'is_running_passive': False,
                            },
                        },
                        'nsf_waiting_for_running': False,
                        'nsf_ietf_waiting_for_sent_rr': False,
                        'is_media_ready': True,
                        'im_base_caps_exist_registered': True,
                        'tmrs_active': False,
                        'lsp_pacing_timer': '0x0',
                        'lsp_sent_last_id': '0000.0000.0000.00-00',
                        'lsp_sent_last_area': 1,
                        'lsp_send_b2b_limit': 10,
                        'lsp_send_b2b_limit_window_end': {
                            'tv_sec': 1407814,
                            'tv_nsec': 256518783,
                        },
                        'mesh_group': '0x0',
                        'lsp_send_requested': False,
                        'lsp_send_in_progress': False,
                        'mpls_ldp_sync': {
                            'im_attr_ldp_sync_info_notify_handle': 0,
                            'ldp_sync_info': False,
                            'is_ldp_sync_info_ok': 0,
                        },
                        'mpls_ldpv6_sync': {
                            'im_attr_ldp_sync_info_notify_handle': '0x0',
                            'ldp_sync_info': False,
                            'is_ldp_sync_info_ok': 0,
                        },
                        'stats': {
                            'ish_recv_count': 0,
                            'esh_recv_count': 0,
                            'unk_recv_count': 0,
                        },
                        'pri_label_stack_limit': 1,
                        'bkp_label_stack_limit': 3,
                        'srte_label_stack_limit': 10,
                        'srat_label_stack_limit': 10,
                        'bandwidth': 10000000,
                        'is_pme_delay_loss_set': False,
                        'pme_avg_delay': '(not set)',
                        'pme_min_delay': '(not set)',
                        'pme_max_delay': '(not set)',
                        'pme_delay_var': '(not set)',
                        'pme_loss': '(not set)',
                        'pme_total_bw': '(not set)',
                        'pme_rsvp_te_bw': '(not set)',
                        'rsvp_max_res_bw': '0 kbits/sec',
                        'rsvp_unres_prio_7': '0 kbits/sec',
                    },
                    'Loopback0': {
                        'im_handle': '0x8000160',
                        'name': 'Loopback0',
                        'ref_count': 3,
                        'index': 0,
                        'snmp_index': 46,
                        'chkpt': {
                            'objid': '0x0',
                        },
                        'cfg': {
                            'refcount': 4,
                            'is_p2p': False,
                            'enabled_mode': 'Passive',
                            'circuit_type': 'level-1-2',
                            'ipv4_bfd_enabled': False,
                            'ipv6_bfd_enabled': False,
                            'bfd_interval': 150,
                            'bfd_multiplier': 3,
                            'topos': 'IPv4 Unicast',
                            'cross_levels': {
                                'per_topo': {
                                    'IPv4 Unicast': {
                                        'metric': '(not set)',
                                        'weight': '(not set)',
                                        'ldp_sync_cfg': '(not set)',
                                        'admin_tag': '(not set)',
                                        'frr_type': '(not set)',
                                        'is_lkgp_set': 0,
                                    },
                                },
                                'is_auth_cfg_ctx_set': False,
                                'auth_cfg_ctx': {
                                    'alg': 'None',
                                    'failure_mode': 'Drop',
                                    'password': '0x0',
                                    'accept_password': '0x0',
                                },
                                'hello_interval_msecs': '(not set)',
                                'hello_multiplier': '(not set)',
                                'csnp_interval_secs': '(not set)',
                                'lsp_pacing_interval_msecs': '(not set)',
                                'lsp_fast_flood_threshold': '(not set)',
                                'lsp_rexmit_interval_secs': '(not set)',
                                'min_lsp_rexmit_interval_msecs': '(not set)',
                                'dr_priority': '(not set)',
                                'is_hello_padding_set': False,
                                'hello_padding': 'Never',
                            },
                            'per_level': {
                                'Level-1': {
                                    'per_topo': {
                                        'IPv4 Unicast': {
                                            'metric': '(not set)',
                                            'weight': '(not set)',
                                            'ldp_sync_cfg': '(not set)',
                                            'admin_tag': '(not set)',
                                            'frr_type': '(not set)',
                                            'is_lkgp_set': 0,
                                        },
                                    },
                                    'is_auth_cfg_ctx_set': False,
                                    'auth_cfg_ctx': {
                                        'alg': 'None',
                                        'failure_mode': 'Drop',
                                        'password': '0x0',
                                        'accept_password': '0x0',
                                    },
                                    'hello_interval_msecs': '(not set)',
                                    'hello_multiplier': '(not set)',
                                    'csnp_interval_secs': '(not set)',
                                    'lsp_pacing_interval_msecs': '(not set)',
                                    'lsp_fast_flood_threshold': '(not set)',
                                    'lsp_rexmit_interval_secs': '(not set)',
                                    'min_lsp_rexmit_interval_msecs': '(not set)',
                                    'dr_priority': '(not set)',
                                    'is_hello_padding_set': False,
                                    'hello_padding': 'Never',
                                },
                                'Level-2': {
                                    'per_topo': {
                                        'IPv4 Unicast': {
                                            'metric': '(not set)',
                                            'weight': '(not set)',
                                            'ldp_sync_cfg': '(not set)',
                                            'admin_tag': '(not set)',
                                            'frr_type': '(not set)',
                                            'is_lkgp_set': 0,
                                        },
                                    },
                                    'is_auth_cfg_ctx_set': False,
                                    'auth_cfg_ctx': {
                                        'alg': 'None',
                                        'failure_mode': 'Drop',
                                        'password': '0x0',
                                        'accept_password': '0x0',
                                    },
                                    'hello_interval_msecs': '(not set)',
                                    'hello_multiplier': '(not set)',
                                    'csnp_interval_secs': '(not set)',
                                    'lsp_pacing_interval_msecs': '(not set)',
                                    'lsp_fast_flood_threshold': '(not set)',
                                    'lsp_rexmit_interval_secs': '(not set)',
                                    'min_lsp_rexmit_interval_msecs': '(not set)',
                                    'dr_priority': '(not set)',
                                    'is_hello_padding_set': False,
                                    'hello_padding': 'Never',
                                },
                            },
                        },
                        'per_topo': {
                            'IPv4 Unicast': {
                                'refcount': 2,
                            },
                        },
                        'topos_enabled_passive': 'IPv4 Unicast',
                        'media': {
                            '0x440cc90': {
                            },
                        },
                        'clns': {
                            'im_node': {
                                'exist_registered': False,
                                'node_exists': False,
                                'state_registered': False,
                                'node_up': False,
                            },
                            'mtu': 0,
                        },
                        'per_af': {
                            'IPv4': {
                                'im_node': {
                                    'exist_registered': True,
                                    'node_exists': True,
                                    'state_registered': True,
                                    'node_up': True,
                                },
                                'local_address': '0.0.0.0',
                                'is_nexthop_addr_registered': False,
                                'is_global_prefix_registered': True,
                                'is_running_passive': True,
                            },
                        },
                        'nsf_waiting_for_running': False,
                        'nsf_ietf_waiting_for_sent_rr': False,
                        'is_media_ready': False,
                        'im_base_caps_exist_registered': True,
                        'tmrs_active': False,
                        'lsp_pacing_timer': '0x0',
                        'lsp_sent_last_id': '0000.0000.0000.00-00',
                        'lsp_sent_last_area': 0,
                        'lsp_send_b2b_limit': 0,
                        'lsp_send_b2b_limit_window_end': {
                            'tv_sec': 0,
                            'tv_nsec': 0,
                        },
                        'mesh_group': '0x0',
                        'lsp_send_requested': False,
                        'lsp_send_in_progress': False,
                        'mpls_ldp_sync': {
                            'im_attr_ldp_sync_info_notify_handle': 0,
                            'ldp_sync_info': False,
                            'is_ldp_sync_info_ok': 0,
                        },
                        'mpls_ldpv6_sync': {
                            'im_attr_ldp_sync_info_notify_handle': '0x0',
                            'ldp_sync_info': False,
                            'is_ldp_sync_info_ok': 0,
                        },
                        'stats': {
                            'ish_recv_count': 0,
                            'esh_recv_count': 0,
                            'unk_recv_count': 0,
                        },
                        'pri_label_stack_limit': '(not set)',
                        'bkp_label_stack_limit': '(not set)',
                        'srte_label_stack_limit': '(not set)',
                        'srat_label_stack_limit': '(not set)',
                        'bandwidth': '(not set)',
                        'is_pme_delay_loss_set': False,
                        'pme_avg_delay': '(not set)',
                        'pme_min_delay': '(not set)',
                        'pme_max_delay': '(not set)',
                        'pme_delay_var': '(not set)',
                        'pme_loss': '(not set)',
                        'pme_total_bw': '(not set)',
                        'pme_rsvp_te_bw': '(not set)',
                        'rsvp_max_res_bw': '0 kbits/sec',
                        'rsvp_unres_prio_7': '0 kbits/sec',
                    },
                },
            },
        },
    }

    golden_output = {'execute.return_value': '''
        RP/0/RSP0/CPU0:bl1-tatooine#show isis private all
        Tue Oct  8 17:36:24.107 EDT

        +++++++++++++++++++++++ IS-IS TEST Global Private Data ++++++++++++++++++++++++

        ISIS TEST private data:
          cfg_refcount                                      : 57
          isis_is_level                                     : level-2-only
          ignore_cksum_errs                                 : TRUE
          cfg_log_drops                                     : FALSE
          nsf_cfg_purgetime                                 : 90
          nsf2_t1_delay                                     : 1
          nsf2_t1_max_num_exp                               : 10
          nsf_cfg_interval                                  : 300
          Address Family Table
            IPv4
              ref_count                                     : 1
            IPv6
              ref_count                                     : 0
          Link Topology Table
            Standard (IPv4 Unicast)
              ref_count                                     : 1
              index                                         : 0
              is_running                                    : TRUE
              list_linkage.next                             : 0x0
              list_linkage.previous                         : 0x44b3f24
          Topology Table
            IPv4 Unicast
              Configuration:
                check_adjacencies                           : (not set)
                attached_bit                                : (not set)
                max_paths                                   : (not set)
                is_mcast_intact_set                         : FALSE
                mcast_intact                                : FALSE
                is_igp_intact_set                           : FALSE
                igp_intact                                  : FALSE
                is_first_hop_source_set                     : FALSE
                first_hop_source                            : FALSE
              ref_count                                     : 23
              index                                         : 0
              ltopo_index                                   : 0
              list_linkage.next                             : 0x0
              list_linkage.previous                         : 0x44b51fc
          Area Configuration Table
            Cross Levels
              is_lsp_gen_interval_set                       : TRUE
              lsp_gen_interval.initial_wait_msecs           : 20
              lsp_gen_interval.secondary_wait_msecs         : 100
              lsp_gen_interval.maximum_wait_msecs           : 5000
              is_lsp_arrivaltime_parameter_set              : FALSE
              lsp_arrivaltime_parameter.backoff_cfg.initial_wait_msecs: 50
              lsp_arrivaltime_parameter.backoff_cfg.secondary_wait_msecs: 200
              lsp_arrivaltime_parameter.backoff_cfg.maximum_wait_msecs: 5000
              lsp_arrivaltime_parameter.max_count           : 0
              lsp_arrivaltime_parameter.max_window_size_msec: 120001
              is_lsp_checksum_interval_set                  : FALSE
              lsp_checksum_interval_secs                    : 0
              is_lsp_refresh_interval_set                   : TRUE
              lsp_refresh_interval_secs                     : 35000
              is_lsp_lifetime_set                           : TRUE
              lsp_lifetime_secs                             : 65535
              is_lsp_mtu_set                                : FALSE
              lsp_mtu                                       : 0
              is_auth_cfg_ctx_set                           : FALSE
              auth_cfg_ctx.alg                              : None
              auth_cfg_ctx.failure_mode                     : Drop
              auth_cfg_ctx.password                         : 0xdecafbad
              auth_cfg_ctx.accept_password                  : 0xdecafbad
              is_snp_authentication_options_set             : FALSE
              snp_authentication_options                    : 0
              is_overload_set                               : FALSE
              overload_mode                                 : -1
              overload_on_startup_secs                      : 0
              per_topo[IPv4 Unicast]                        :
                is_metric_style_set                         : TRUE
                generate_metric_mask                        : 2
                accept_metric_mask                          : 2
                summary_table                               : 0x15431f50
                metric                                      : 100000
                is_spf_interval_set                         : TRUE
                spf_interval.initial_wait_msecs             : 50
                spf_interval.secondary_wait_msecs           : 150
                spf_interval.maximum_wait_msecs             : 5000
                spf_periodic_interval_secs                  : (not set)
                ispf_state                                  : (not set)
                max_redist_prefixes                         : (not set)
                  [000] is_spf_prefix_priority_acl_names_set : FALSE
                  [000] spf_prefix_priority_acl_names        : 0x0
                  [001] is_spf_prefix_priority_acl_names_set : TRUE
                  [001] spf_prefix_priority_acl_names        : 0x154b92c4
                  [002] is_spf_prefix_priority_acl_names_set : TRUE
                  [002] spf_prefix_priority_acl_names        : 0x155a0e3c
                  [003] is_spf_prefix_priority_acl_names_set : FALSE
                  [003] spf_prefix_priority_acl_names        : 0x0
                  [000] is_spf_prefix_priority_tags_set      : FALSE
                  [000] spf_prefix_priority_tags             : 0
                  [001] is_spf_prefix_priority_tags_set      : FALSE
                  [001] spf_prefix_priority_tags             : 0
                  [002] is_spf_prefix_priority_tags_set      : FALSE
                  [002] spf_prefix_priority_tags             : 0
                  [003] is_spf_prefix_priority_tags_set      : FALSE
                  [003] spf_prefix_priority_tags             : 0
            Level-1
              is_lsp_gen_interval_set                       : FALSE
              lsp_gen_interval.initial_wait_msecs           : 50
              lsp_gen_interval.secondary_wait_msecs         : 200
              lsp_gen_interval.maximum_wait_msecs           : 5000
              is_lsp_arrivaltime_parameter_set              : FALSE
              lsp_arrivaltime_parameter.backoff_cfg.initial_wait_msecs: 50
              lsp_arrivaltime_parameter.backoff_cfg.secondary_wait_msecs: 200
              lsp_arrivaltime_parameter.backoff_cfg.maximum_wait_msecs: 5000
              lsp_arrivaltime_parameter.max_count           : 0
              lsp_arrivaltime_parameter.max_window_size_msec: 120001
              is_lsp_checksum_interval_set                  : FALSE
              lsp_checksum_interval_secs                    : 0
              is_lsp_refresh_interval_set                   : FALSE
              lsp_refresh_interval_secs                     : 0
              is_lsp_lifetime_set                           : FALSE
              lsp_lifetime_secs                             : 0
              is_lsp_mtu_set                                : FALSE
              lsp_mtu                                       : 0
              is_auth_cfg_ctx_set                           : FALSE
              auth_cfg_ctx.alg                              : None
              auth_cfg_ctx.failure_mode                     : Drop
              auth_cfg_ctx.password                         : 0xdecafbad
              auth_cfg_ctx.accept_password                  : 0xdecafbad
              is_snp_authentication_options_set             : FALSE
              snp_authentication_options                    : 0
              is_overload_set                               : FALSE
              overload_mode                                 : 0
              overload_on_startup_secs                      : 0
              per_topo[IPv4 Unicast]                        :
                is_metric_style_set                         : FALSE
                generate_metric_mask                        : 0
                accept_metric_mask                          : 0
                summary_table                               : 0x15431fac
                metric                                      : (not set)
                is_spf_interval_set                         : FALSE
                spf_interval.initial_wait_msecs             : 50
                spf_interval.secondary_wait_msecs           : 200
                spf_interval.maximum_wait_msecs             : 5000
                spf_periodic_interval_secs                  : (not set)
                ispf_state                                  : (not set)
                max_redist_prefixes                         : (not set)
                  [000] is_spf_prefix_priority_acl_names_set : FALSE
                  [000] spf_prefix_priority_acl_names        : 0x0
                  [001] is_spf_prefix_priority_acl_names_set : FALSE
                  [001] spf_prefix_priority_acl_names        : 0x0
                  [002] is_spf_prefix_priority_acl_names_set : FALSE
                  [002] spf_prefix_priority_acl_names        : 0x0
                  [003] is_spf_prefix_priority_acl_names_set : FALSE
                  [003] spf_prefix_priority_acl_names        : 0x0
                  [000] is_spf_prefix_priority_tags_set      : FALSE
                  [000] spf_prefix_priority_tags             : 0
                  [001] is_spf_prefix_priority_tags_set      : FALSE
                  [001] spf_prefix_priority_tags             : 0
                  [002] is_spf_prefix_priority_tags_set      : FALSE
                  [002] spf_prefix_priority_tags             : 0
                  [003] is_spf_prefix_priority_tags_set      : FALSE
                  [003] spf_prefix_priority_tags             : 0
            Level-2
              is_lsp_gen_interval_set                       : FALSE
              lsp_gen_interval.initial_wait_msecs           : 50
              lsp_gen_interval.secondary_wait_msecs         : 200
              lsp_gen_interval.maximum_wait_msecs           : 5000
              is_lsp_arrivaltime_parameter_set              : FALSE
              lsp_arrivaltime_parameter.backoff_cfg.initial_wait_msecs: 50
              lsp_arrivaltime_parameter.backoff_cfg.secondary_wait_msecs: 200
              lsp_arrivaltime_parameter.backoff_cfg.maximum_wait_msecs: 5000
              lsp_arrivaltime_parameter.max_count           : 0
              lsp_arrivaltime_parameter.max_window_size_msec: 120001
              is_lsp_checksum_interval_set                  : FALSE
              lsp_checksum_interval_secs                    : 0
              is_lsp_refresh_interval_set                   : FALSE
              lsp_refresh_interval_secs                     : 0
              is_lsp_lifetime_set                           : FALSE
              lsp_lifetime_secs                             : 0
              is_lsp_mtu_set                                : FALSE
              lsp_mtu                                       : 0
              is_auth_cfg_ctx_set                           : FALSE
              auth_cfg_ctx.alg                              : None
              auth_cfg_ctx.failure_mode                     : Drop
              auth_cfg_ctx.password                         : 0xdecafbad
              auth_cfg_ctx.accept_password                  : 0xdecafbad
              is_snp_authentication_options_set             : FALSE
              snp_authentication_options                    : 0
              is_overload_set                               : FALSE
              overload_mode                                 : 0
              overload_on_startup_secs                      : 0
              per_topo[IPv4 Unicast]                        :
                is_metric_style_set                         : FALSE
                generate_metric_mask                        : 0
                accept_metric_mask                          : 0
                summary_table                               : 0x1539cef4
                metric                                      : (not set)
                is_spf_interval_set                         : FALSE
                spf_interval.initial_wait_msecs             : 50
                spf_interval.secondary_wait_msecs           : 200
                spf_interval.maximum_wait_msecs             : 5000
                spf_periodic_interval_secs                  : (not set)
                ispf_state                                  : (not set)
                max_redist_prefixes                         : (not set)
                  [000] is_spf_prefix_priority_acl_names_set : FALSE
                  [000] spf_prefix_priority_acl_names        : 0x0
                  [001] is_spf_prefix_priority_acl_names_set : FALSE
                  [001] spf_prefix_priority_acl_names        : 0x0
                  [002] is_spf_prefix_priority_acl_names_set : FALSE
                  [002] spf_prefix_priority_acl_names        : 0x0
                  [003] is_spf_prefix_priority_acl_names_set : FALSE
                  [003] spf_prefix_priority_acl_names        : 0x0
                  [000] is_spf_prefix_priority_tags_set      : FALSE
                  [000] spf_prefix_priority_tags             : 0
                  [001] is_spf_prefix_priority_tags_set      : FALSE
                  [001] spf_prefix_priority_tags             : 0
                  [002] is_spf_prefix_priority_tags_set      : FALSE
                  [002] spf_prefix_priority_tags             : 0
                  [003] is_spf_prefix_priority_tags_set      : FALSE
                  [003] spf_prefix_priority_tags             : 0
          Area Table
          Level-2
            index                                           : 1
            idb_list.sll_head                               : 0x151942e0
            idb_list.sll_tail                               : 0x15193fd4
            idb_list.sll_count                              : 8
            idb_list.sll_maximum                            : 0
            list_linkage.next                               : 0x0
            list_linkage.previous                           : 0x44b2534
            adj_db                                          : 0x1540cee4
            adj_log                                         : 0x1539b844
            uni_db_log                                      : 0x15411024
            upd_db.lock.rwlock.__active                     : 0
            upd_db.lock.rwlock.__spare                      : 0x0
            upd_db.lock.rwlock.__blockedwriters             : 0
            upd_db.lock.rwlock.__blockedreaders             : 0
            upd_db.lock.rwlock.__heavy                      : 0
            upd_db.lock.rwlock.__lock.__count               : -2147483648
            upd_db.lock.rwlock.__lock.__owner               : 0
            upd_db.lock.rwlock.__owner                      : 4294967294
            upd_db.lock.description                         : 0x15393cf0
            upd_db.tree.root                                : 0x0
            upd_db.tree.key_size                            : 8
            upd_db.tree.size                                : 0
            upd_db.tree.node_alloc_data                     : 0x15393cd0
            upd_db.tree.node_alloc_fn                       : 0x42fd024
            upd_db.tree.node_free_fn                        : 0x42fd08a
            upd_db.tree.data_to_str_fn                      : 0x42fd094
            upd_db.tree_node_chunks.name                    : 0x448764c
            upd_db.tree_node_chunks.size                    : 28
            upd_db.tree_node_chunks.flags                   : 1297
            upd_db.tree_node_chunks.chunk                   : 0x1543146c
            upd_db.tree_node_chunks.num_allocated_elements  : 0
            upd_db.area                                     : 0x15393bfc
            upd_db.log                                      : 0x15432024
            upd_db.name                                     : L2 Update DB
            nsf_ietf_csnp_rcvd                              : FALSE
            overload_bit_on_startup_timer                   : 0x15017530
            overload_bit_trigger_expired                    : TRUE
            overload_bit_forced_reasons                     :
            upd_periodic_timer                              : 0x150174d0
            checksum_ptimer.tv_sec                          : 3657420
            checksum_ptimer.tv_nsec                         : 458761224
            dec_db.lock.rwlock.__active                     : 0
            dec_db.lock.rwlock.__spare                      : 0x0
            dec_db.lock.rwlock.__blockedwriters             : 0
            dec_db.lock.rwlock.__blockedreaders             : 0
            dec_db.lock.rwlock.__heavy                      : 0
            dec_db.lock.rwlock.__lock.__count               : -2147483648
            dec_db.lock.rwlock.__lock.__owner               : 0
            dec_db.lock.rwlock.__owner                      : 4294967294
            dec_db.lock.description                         : 0x153942b0
            dec_db.tree.root                                : 0x1539f9d4
            dec_db.tree.key_size                            : 8
            dec_db.tree.size                                : 82
            dec_db.tree.node_alloc_data                     : 0x15394290
            dec_db.tree.node_alloc_fn                       : 0x42fd024
            dec_db.tree.node_free_fn                        : 0x42fd08a
            dec_db.tree.data_to_str_fn                      : 0x42fd094
            dec_db.tree_node_chunks.name                    : 0x448764c
            dec_db.tree_node_chunks.size                    : 28
            dec_db.tree_node_chunks.flags                   : 1297
            dec_db.tree_node_chunks.chunk                   : 0x1539f844
            dec_db.tree_node_chunks.num_allocated_elements  : 82
            dec_db.area                                     : 0x15393bfc
            dec_db.log                                      : 0x15453024
            dec_db.name                                     : L2 Decision DB
            node_db.node_created_fn                         : 0x424fd84
            node_db.node_destroyed_fn                       : 0x424ffa6
            node_db.node_ltopo_created_fn                   : 0x42500b6
            node_db.node_ltopo_destroyed_fn                 : 0x42503ba
            node_db.node_topo_created_fn                    : 0x4250536
            node_db.node_topo_destroyed_fn                  : 0x42506b4
            node_db.callback_context                        : 0x15393bfc
            node_db.root_element                            : 0x151fb9bc
            node_db.num_nodes                               : 64
            stats.ta_lsp_build                              : 850
            stats.ta_lsp_refresh                            : 219
            trap_stats.isisSysStatCorrLSPs                  : 0
            trap_stats.isisSysStatAuthTypeFails             : 0
            trap_stats.isisSysStatAuthFails                 : 0
            trap_stats.isisSysStatLSPDbaseOloads            : 4
            trap_stats.isisSysStatManAddrDropFromAreas      : 0
            trap_stats.isisSysStatAttmptToExMaxSeqNums      : 0
            trap_stats.isisSysStatSeqNumSkips               : 1
            trap_stats.isisSysStatOwnLSPPurges              : 3
            trap_stats.isisSysStatIDFieldLenMismatches      : 0
            trap_stats.isisSysStatLSPErrors                 : 0
            per_ltopo[Standard (IPv4 Unicast)]              :
              area                                          : 0x15393bfc
              ltopo_index                                   : Standard (IPv4 Unicast)
              roca_event.mutex.mutex.__count                : -2147483648
              roca_event.mutex.mutex.__owner                : 0
              roca_event.mutex.description                  : 0x1500ee28
              roca_event.timer.timer                        : 0x150179bc
              roca_event.timer.num_execution_events         : 1
              roca_event.timer.is_pending                   : FALSE
              roca_event.timer.is_executing                 : FALSE
              roca_event.timer.postponed_schedule_time.tv_sec: 0
              roca_event.timer.postponed_schedule_time.tv_nsec: 0
              roca_event.timer.last_execution_time.tv_sec   : 3657197
              roca_event.timer.last_execution_time.tv_nsec  : 824108467
              roca_event.log                                : 0x15474024
              roca_event.class                              : <error>
              spf_periodic_timer                            : 0x1501798c
              paths.classification                          : 0
              paths.is_sorted                               : FALSE
              paths.array                                   : 0x1540d45c
              paths.num_elements                            : 64
              unreached.classification                      : 0
              unreached.is_sorted                           : FALSE
              unreached.array                               : 0x1540d4b4
              unreached.num_elements                        : 0
              firsthopchanged.classification                : 0
              firsthopchanged.is_sorted                     : TRUE
              firsthopchanged.array                         : 0x1540d4e0
              firsthopchanged.num_elements                  : 0
              linkchanged.classification                    : 2
              linkchanged.is_sorted                         : TRUE
              linkchanged.array                             : 0x1540d66c
              linkchanged.num_elements                      : 0
              reachable_area_addresses                      : 0x1540d430
              stats.num_spfs                                : 5004
              stats.num_ispfs                               : 0
              stats.num_nhcs                                : 10
              stats.num_prcs                                : 1219
              stats.num_periodic_spfs                       : 3876
            per_topo[IPv4 Unicast]                          :
              area                                          : 0x15393bfc
              topo_index                                    : IPv4 Unicast
              te.link_holddown_timer                        : 0x150181cc
              te.purge_link_info_timer                      : 0x1501819c
              te.log                                        : 0x153a8d24
              te.tunnel_table                               : 0x153ab844
              te.info_from_te                               : 0x0
              te.pce_info_from_te                           : 0x0
              te.is_pce_ready                               : FALSE
              overloaded_count                              : 0
              overload_bit_trigger_running                  : FALSE
              bgp_converged_notify_h                        : 0x0
              added_first_hops                              : 0x0
              deleted_first_hops                            : 0x0
              postponed_added_first_hops                    : 0x0
              postponed_deleted_first_hops                  : 0x0
              prefixeschanged                               : 0x0
              nodechanged                                   : 0x0
              prefix_priority_acl[ISIS_PREFIX_PRIORITY_CRITICAL]: 0x0
              prefix_priority_acl[ISIS_PREFIX_PRIORITY_HIGH]: 0x15604868
              prefix_priority_acl[ISIS_PREFIX_PRIORITY_MED] : 0x156047dc
              prefix_priority_acl[ISIS_PREFIX_PRIORITY_LOW] : 0x0
              num_redist_prefixes                           : 166
              max_redist_prefixes_exceeded                  : FALSE
              max_redist_prefixes_alarm_on                  : FALSE
              has_prefix_policy_changed                     : FALSE
            per_af[IPv4]                                    :
              router_id                                     : 0x15192388
            per_af[IPv6]                                    :
              router_id                                     : 0x0

        ++++++++++++++++++++++ IS-IS TEST Interface Private Data ++++++++++++++++++++++

        Interface TenGigE0/0/1/3
          im_handle                                         : 0x180
          name                                              : TenGigE0_0_1_3
          ref_count                                         : 2
          index                                             : 4
          snmp_index                                        : 21
          chkpt.objid                                       : 0x0
          cfg.refcount                                      : 7
          cfg.is_p2p                                        : TRUE
          cfg.enabled_mode                                  : Active
          cfg.circuit_type                                  : level-1-2
          cfg.ipv4_bfd_enabled                              : TRUE
          cfg.ipv6_bfd_enabled                              : FALSE
          cfg.bfd_interval                                  : 250
          cfg.bfd_multiplier                                : 3
          cfg.topos                                         : IPv4 Unicast
          per_topo[IPv4 Unicast]                            :
            refcount                                        : 2
          cfg.cross_levels                                  :
            per_topo[IPv4 Unicast]                          :
              metric                                        : 10
              weight                                        : (not set)
              ldp_sync_cfg                                  : (not set)
              admin_tag                                     : (not set)
              frr_type                                      : (not set)
              is_lkgp_set                                   : 0
            is_auth_cfg_ctx_set                             : FALSE
            auth_cfg_ctx.alg                                : None
            auth_cfg_ctx.failure_mode                       : Drop
            auth_cfg_ctx.password                           : 0x0
            auth_cfg_ctx.accept_password                    : 0x0
            hello_interval_msecs                            : (not set)
            hello_multiplier                                : (not set)
            csnp_interval_secs                              : (not set)
            lsp_pacing_interval_msecs                       : (not set)
            lsp_fast_flood_threshold                        : (not set)
            lsp_rexmit_interval_secs                        : (not set)
            min_lsp_rexmit_interval_msecs                   : (not set)
            dr_priority                                     : (not set)
            is_hello_padding_set                            : FALSE
            hello_padding                                   : Never
          cfg.per_level[Level-1]                            :
            per_topo[IPv4 Unicast]                          :
              metric                                        : (not set)
              weight                                        : (not set)
              ldp_sync_cfg                                  : (not set)
              admin_tag                                     : (not set)
              frr_type                                      : (not set)
              is_lkgp_set                                   : 0
            is_auth_cfg_ctx_set                             : FALSE
            auth_cfg_ctx.alg                                : None
            auth_cfg_ctx.failure_mode                       : Drop
            auth_cfg_ctx.password                           : 0x0
            auth_cfg_ctx.accept_password                    : 0x0
            hello_interval_msecs                            : (not set)
            hello_multiplier                                : (not set)
            csnp_interval_secs                              : (not set)
            lsp_pacing_interval_msecs                       : (not set)
            lsp_fast_flood_threshold                        : (not set)
            lsp_rexmit_interval_secs                        : (not set)
            min_lsp_rexmit_interval_msecs                   : (not set)
            dr_priority                                     : (not set)
            is_hello_padding_set                            : FALSE
            hello_padding                                   : Never
          cfg.per_level[Level-2]                            :
            per_topo[IPv4 Unicast]                          :
              metric                                        : (not set)
              weight                                        : (not set)
              ldp_sync_cfg                                  : (not set)
              admin_tag                                     : (not set)
              frr_type                                      : (not set)
              is_lkgp_set                                   : 0
            is_auth_cfg_ctx_set                             : FALSE
            auth_cfg_ctx.alg                                : None
            auth_cfg_ctx.failure_mode                       : Drop
            auth_cfg_ctx.password                           : 0x0
            auth_cfg_ctx.accept_password                    : 0x0
            hello_interval_msecs                            : (not set)
            hello_multiplier                                : (not set)
            csnp_interval_secs                              : (not set)
            lsp_pacing_interval_msecs                       : (not set)
            lsp_fast_flood_threshold                        : (not set)
            lsp_rexmit_interval_secs                        : (not set)
            min_lsp_rexmit_interval_msecs                   : (not set)
            dr_priority                                     : (not set)
            is_hello_padding_set                            : FALSE
            hello_padding                                   : Never
          topos_enabled_passive                             :
          topos_enabled_active                              : IPv4 Unicast
          per_area[Level-2]                                 :
            area_linkage                                    : 0x15194244
            idb                                             : 0x151916d8
            area                                            : 0x15393bfc
            adj_filter                                      : 0x0
            csnp_control.timer                              : 0x0
            csnp_control.next_lsp_id                        : 0000.0000.0000.00-00
            csnp_control.building_packets                   : FALSE
            psnp_timer                                      : 0x0
            nsf_ietf.full_csnp_set_rcvd                     : FALSE
            nsf_ietf.csnp_set_rcvd.list_head                : 0x0
            nsf_ietf.csnp_set_rcvd.list_size                : 0
            adj_up_count                                    : 0
            lan_adj_up_count                                : 0
            adj_list                                        : 0x0
            per_ltopo[Standard (IPv4 Unicast)]              :
              num_requested_adjs                            : 0
              num_adjs                                      : 0
            tmrs_active                                     : FALSE
            adj_filter_match_all                            : FALSE
            lsp_count.in                                    : 24185
            lsp_count.out                                   : 140529
            csnp_count.in                                   : 17
            csnp_count.out                                  : 17
            psnp_count.in                                   : 134275
            psnp_count.out                                  : 23143
            lsp_flooding_dup_count                          : 3
            lsp_drop_count                                  : 0
          media                                             : 0x440cbe0
            caps_id                                         : 30
            media_class                                     : LAN
            encaps_overhead                                 : 3
          media_specific.p2p.hello_timer                    : 0x156bace8
          media_specific.p2p.last_hello.tv_sec              : 0
          media_specific.p2p.last_hello.tv_nsec             : 0
          media_specific.p2p.recent_hello_send_count        : 0
          media_specific.p2p.adj_state                      : 2
          media_specific.p2p.do_ietf_3way                   : TRUE
          media_specific.p2p.received_ietf_3way             : FALSE
          media_specific.p2p.neighbor_extended_circuit_number: 0
          media_specific.p2p.neighbor_system_id             : 0000.0000.0000
          media_specific.p2p.mib_counters.isisCircuitType   : 0
          media_specific.p2p.mib_counters.isisCircAdjChanges: 29
          media_specific.p2p.mib_counters.isisCircNumAdj    : 0
          media_specific.p2p.mib_counters.isisCircInitFails : 0
          media_specific.p2p.mib_counters.isisCircRejAdjs   : 0
          media_specific.p2p.mib_counters.isisCircIDFieldLenMismatches: 0
          media_specific.p2p.mib_counters.isisCircMaxAreaAddrMismatches: 0
          media_specific.p2p.mib_counters.isisCircAuthTypeFails: 0
          media_specific.p2p.mib_counters.isisCircAuthFails : 0
          media_specific.p2p.mib_counters.isisCircLANDesISChanges: 0
          media_specific.p2p.mib_counters.isisCircIndex     : 0
          media_specific.p2p.init_csnp_wait.tv_sec          : 0
          media_specific.p2p.init_csnp_wait.tv_nsec         : 0
          media_specific.p2p.lsp_rexmit_queue.sll_head      : 0x0
          media_specific.p2p.lsp_rexmit_queue.sll_tail      : 0x0
          media_specific.p2p.lsp_rexmit_queue.sll_count     : 0
          media_specific.p2p.lsp_rexmit_queue.sll_maximum   : 0
          media_specific.p2p.lsp_rexmit_timer               : 0x157111ac
          media_specific.p2p.nsf_ietf
            t1_timer                                        : 0x156bacb8
            num_t1_expiries                                 : 0
            first_t1_expiry_seen                            : FALSE
            rr_sent                                         : FALSE
            ra_rcvd                                         : FALSE
            all_ra_seen                                     : FALSE
            ra_required_nbr_count                           : 0
            RA-expected neighbor list:
          media_specific.p2p.stats.iih_count.in             : 160726
          media_specific.p2p.stats.iih_count.out            : 160689
          media_specific.p2p.stats.iih_nomem                : 0
          media_specific.p2p.stats.lsp_retransmits          : 72
          media_specific.p2p.p2p_over_lan
            mcast_state.is_mcast_group_member               : TRUE
            mcast_state.mcast_join_reason                   : 2
            snpa_info.im_attr_macaddr_notify_handle         : 0x1514d188
            snpa_info.snpa                                  : 00c1.64ff.4ef2
            snpa_info.is_snpa_ok                            : TRUE
          clns.im_node.exist_registered                     : TRUE
          clns.im_node.node_exists                          : TRUE
          clns.im_node.state_registered                     : TRUE
          clns.im_node.node_up                              : FALSE
          clns.mtu                                          : 9199
          per_af[IPv4]
            im_node.exist_registered                        : TRUE
            im_node.node_exists                             : TRUE
            im_node.state_registered                        : TRUE
            im_node.node_up                                 : FALSE
            local_address                                   : 0.0.0.0
            is_nexthop_addr_registered                      : TRUE
            is_global_prefix_registered                     : FALSE
            is_running_passive                              : FALSE
          ltopos_ready_active                               :
          nsf_waiting_for_running                           : FALSE
          nsf_ietf_waiting_for_sent_rr                      : FALSE
          is_media_ready                                    : TRUE
          im_base_caps_exist_registered                     : TRUE
          tmrs_active                                       : FALSE
          lsp_pacing_timer                                  : 0x0
          lsp_sent_last_id                                  : 0000.0000.0000.00-00
          lsp_sent_last_area                                : 1
          lsp_send_b2b_limit                                : 10
          lsp_send_b2b_limit_window_end.tv_sec              : 1407814
          lsp_send_b2b_limit_window_end.tv_nsec             : 256518783
          mesh_group                                        : 0x0
          lsp_send_requested                                : FALSE
          lsp_send_in_progress                              : FALSE
          mpls_ldp_sync.im_attr_ldp_sync_info_notify_handle : 0
          mpls_ldp_sync.ldp_sync_info                       : FALSE
          mpls_ldp_sync.is_ldp_sync_info_ok                 : 0
          mpls_ldpv6_sync.im_attr_ldp_sync_info_notify_handle: 0x0
          mpls_ldpv6_sync.ldp_sync_info                     : FALSE
          mpls_ldpv6_sync.is_ldp_sync_info_ok               : 0
          stats.ish_recv_count                              : 0
          stats.esh_recv_count                              : 0
          stats.unk_recv_count                              : 0
          pri_label_stack_limit                             : 1
          bkp_label_stack_limit                             : 3
          srte_label_stack_limit                            : 10
          srat_label_stack_limit                            : 10
          bandwidth                                         : 10000000
          is_pme_delay_loss_set                             : FALSE
          pme_avg_delay                                     : (not set)
          pme_min_delay                                     : (not set)
          pme_max_delay                                     : (not set)
          pme_delay_var                                     : (not set)
          pme_loss                                          : (not set)
          pme_total_bw                                      : (not set)
          pme_rsvp_te_bw                                    : (not set)
          rsvp_max_res_bw                                   : 0 kbits/sec
          rsvp_unres_prio_7                                 : 0 kbits/sec
        Interface Loopback0
          im_handle                                         : 0x8000160
          name                                              : Loopback0
          ref_count                                         : 3
          index                                             : 0
          snmp_index                                        : 46
          chkpt.objid                                       : 0x0
          cfg.refcount                                      : 4
          cfg.is_p2p                                        : FALSE
          cfg.enabled_mode                                  : Passive
          cfg.circuit_type                                  : level-1-2
          cfg.ipv4_bfd_enabled                              : FALSE
          cfg.ipv6_bfd_enabled                              : FALSE
          cfg.bfd_interval                                  : 150
          cfg.bfd_multiplier                                : 3
          cfg.topos                                         : IPv4 Unicast
          per_topo[IPv4 Unicast]                            :
            refcount                                        : 2
          cfg.cross_levels                                  :
            per_topo[IPv4 Unicast]                          :
              metric                                        : (not set)
              weight                                        : (not set)
              ldp_sync_cfg                                  : (not set)
              admin_tag                                     : (not set)
              frr_type                                      : (not set)
              is_lkgp_set                                   : 0
            is_auth_cfg_ctx_set                             : FALSE
            auth_cfg_ctx.alg                                : None
            auth_cfg_ctx.failure_mode                       : Drop
            auth_cfg_ctx.password                           : 0x0
            auth_cfg_ctx.accept_password                    : 0x0
            hello_interval_msecs                            : (not set)
            hello_multiplier                                : (not set)
            csnp_interval_secs                              : (not set)
            lsp_pacing_interval_msecs                       : (not set)
            lsp_fast_flood_threshold                        : (not set)
            lsp_rexmit_interval_secs                        : (not set)
            min_lsp_rexmit_interval_msecs                   : (not set)
            dr_priority                                     : (not set)
            is_hello_padding_set                            : FALSE
            hello_padding                                   : Never
          cfg.per_level[Level-1]                            :
            per_topo[IPv4 Unicast]                          :
              metric                                        : (not set)
              weight                                        : (not set)
              ldp_sync_cfg                                  : (not set)
              admin_tag                                     : (not set)
              frr_type                                      : (not set)
              is_lkgp_set                                   : 0
            is_auth_cfg_ctx_set                             : FALSE
            auth_cfg_ctx.alg                                : None
            auth_cfg_ctx.failure_mode                       : Drop
            auth_cfg_ctx.password                           : 0x0
            auth_cfg_ctx.accept_password                    : 0x0
            hello_interval_msecs                            : (not set)
            hello_multiplier                                : (not set)
            csnp_interval_secs                              : (not set)
            lsp_pacing_interval_msecs                       : (not set)
            lsp_fast_flood_threshold                        : (not set)
            lsp_rexmit_interval_secs                        : (not set)
            min_lsp_rexmit_interval_msecs                   : (not set)
            dr_priority                                     : (not set)
            is_hello_padding_set                            : FALSE
            hello_padding                                   : Never
          cfg.per_level[Level-2]                            :
            per_topo[IPv4 Unicast]                          :
              metric                                        : (not set)
              weight                                        : (not set)
              ldp_sync_cfg                                  : (not set)
              admin_tag                                     : (not set)
              frr_type                                      : (not set)
              is_lkgp_set                                   : 0
            is_auth_cfg_ctx_set                             : FALSE
            auth_cfg_ctx.alg                                : None
            auth_cfg_ctx.failure_mode                       : Drop
            auth_cfg_ctx.password                           : 0x0
            auth_cfg_ctx.accept_password                    : 0x0
            hello_interval_msecs                            : (not set)
            hello_multiplier                                : (not set)
            csnp_interval_secs                              : (not set)
            lsp_pacing_interval_msecs                       : (not set)
            lsp_fast_flood_threshold                        : (not set)
            lsp_rexmit_interval_secs                        : (not set)
            min_lsp_rexmit_interval_msecs                   : (not set)
            dr_priority                                     : (not set)
            is_hello_padding_set                            : FALSE
            hello_padding                                   : Never
          topos_enabled_passive                             : IPv4 Unicast
          topos_enabled_active                              :
          media                                             : 0x440cc90
          clns.im_node.exist_registered                     : FALSE
          clns.im_node.node_exists                          : FALSE
          clns.im_node.state_registered                     : FALSE
          clns.im_node.node_up                              : FALSE
          clns.mtu                                          : 0
          per_af[IPv4]
            im_node.exist_registered                        : TRUE
            im_node.node_exists                             : TRUE
            im_node.state_registered                        : TRUE
            im_node.node_up                                 : TRUE
            local_address                                   : 0.0.0.0
            is_nexthop_addr_registered                      : FALSE
            is_global_prefix_registered                     : TRUE
            is_running_passive                              : TRUE
          ltopos_ready_active                               :
          nsf_waiting_for_running                           : FALSE
          nsf_ietf_waiting_for_sent_rr                      : FALSE
          is_media_ready                                    : FALSE
          im_base_caps_exist_registered                     : TRUE
          tmrs_active                                       : FALSE
          lsp_pacing_timer                                  : 0x0
          lsp_sent_last_id                                  : 0000.0000.0000.00-00
          lsp_sent_last_area                                : 0
          lsp_send_b2b_limit                                : 0
          lsp_send_b2b_limit_window_end.tv_sec              : 0
          lsp_send_b2b_limit_window_end.tv_nsec             : 0
          mesh_group                                        : 0x0
          lsp_send_requested                                : FALSE
          lsp_send_in_progress                              : FALSE
          mpls_ldp_sync.im_attr_ldp_sync_info_notify_handle : 0
          mpls_ldp_sync.ldp_sync_info                       : FALSE
          mpls_ldp_sync.is_ldp_sync_info_ok                 : 0
          mpls_ldpv6_sync.im_attr_ldp_sync_info_notify_handle: 0x0
          mpls_ldpv6_sync.ldp_sync_info                     : FALSE
          mpls_ldpv6_sync.is_ldp_sync_info_ok               : 0
          stats.ish_recv_count                              : 0
          stats.esh_recv_count                              : 0
          stats.unk_recv_count                              : 0
          pri_label_stack_limit                             : (not set)
          bkp_label_stack_limit                             : (not set)
          srte_label_stack_limit                            : (not set)
          srat_label_stack_limit                            : (not set)
          bandwidth                                         : (not set)
          is_pme_delay_loss_set                             : FALSE
          pme_avg_delay                                     : (not set)
          pme_min_delay                                     : (not set)
          pme_max_delay                                     : (not set)
          pme_delay_var                                     : (not set)
          pme_loss                                          : (not set)
          pme_total_bw                                      : (not set)
          pme_rsvp_te_bw                                    : (not set)
          rsvp_max_res_bw                                   : 0 kbits/sec
          rsvp_unres_prio_7                                 : 0 kbits/sec
    '''}

    def test_empty_output(self):
        device = Mock(**self.empty_output)
        obj = ShowIsisPrivateAll(device=device)
        with self.assertRaises(SchemaEmptyParserError):
            obj.parse()

    def test_golden_output(self):
        device = Mock(**self.golden_output)
        obj = ShowIsisPrivateAll(device=device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)

if __name__ == '__main__':
    unittest.main()
