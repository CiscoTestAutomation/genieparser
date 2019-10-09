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
                                               ShowIsisSegmentRoutingLabelTable,
                                               ShowIsisSpfLog)


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

class TestShowIsisSpfLog(unittest.TestCase):
    ''' Unit Tests for:
        * show isis spf-log -> ShowIsisSpfLog
    '''
    maxDiff = None

    empty_output = {'execute.return_value': ''}

    parsed_output_1 = {
        "instance": {
            "TEST": {
                "level": {
                    2: {
                        "address_family": {
                            "IPv4 Unicast": {
                                "log_date": {
                                    "Mon Oct  7 2019": {
                                        "timestamp": {
                                            "17:57:50.131": {
                                                "log_type": "PPFRR",
                                                "time_ms": 0,
                                                "total_nodes": 64,
                                                "trigger_count": 1,
                                                "triggers": "PERPREFIXFRR",
                                            },
                                            "18:12:49.690": {
                                                "log_type": "FSPF",
                                                "time_ms": 0,
                                                "total_nodes": 64,
                                                "trigger_count": 1,
                                                "triggers": "PERIODIC",
                                            },
                                            "18:12:50.192": {
                                                "log_type": "PPFRR",
                                                "time_ms": 0,
                                                "total_nodes": 64,
                                                "trigger_count": 1,
                                                "triggers": "PERPREFIXFRR",
                                            },
                                            "18:27:49.750": {
                                                "log_type": "FSPF",
                                                "time_ms": 0,
                                                "total_nodes": 64,
                                                "trigger_count": 1,
                                                "triggers": "PERIODIC",
                                            },
                                            "18:27:50.252": {
                                                "log_type": "PPFRR",
                                                "time_ms": 0,
                                                "total_nodes": 64,
                                                "trigger_count": 1,
                                                "triggers": "PERPREFIXFRR",
                                            },
                                            "18:42:49.811": {
                                                "log_type": "FSPF",
                                                "time_ms": 0,
                                                "total_nodes": 64,
                                                "trigger_count": 1,
                                                "triggers": "PERIODIC",
                                            },
                                            "18:42:50.313": {
                                                "log_type": "PPFRR",
                                                "time_ms": 0,
                                                "total_nodes": 64,
                                                "trigger_count": 1,
                                                "triggers": "PERPREFIXFRR",
                                            },
                                            "18:57:49.871": {
                                                "log_type": "FSPF",
                                                "time_ms": 0,
                                                "total_nodes": 64,
                                                "trigger_count": 1,
                                                "triggers": "PERIODIC",
                                            },
                                            "18:57:50.373": {
                                                "log_type": "PPFRR",
                                                "time_ms": 0,
                                                "total_nodes": 64,
                                                "trigger_count": 1,
                                                "triggers": "PERPREFIXFRR",
                                            },
                                            "19:12:49.932": {
                                                "log_type": "FSPF",
                                                "time_ms": 0,
                                                "total_nodes": 64,
                                                "trigger_count": 1,
                                                "triggers": "PERIODIC",
                                            },
                                            "19:12:50.434": {
                                                "log_type": "PPFRR",
                                                "time_ms": 0,
                                                "total_nodes": 64,
                                                "trigger_count": 1,
                                                "triggers": "PERPREFIXFRR",
                                            },
                                            "19:27:49.992": {
                                                "log_type": "FSPF",
                                                "time_ms": 0,
                                                "total_nodes": 64,
                                                "trigger_count": 1,
                                                "triggers": "PERIODIC",
                                            },
                                            "19:27:50.494": {
                                                "log_type": "PPFRR",
                                                "time_ms": 0,
                                                "total_nodes": 64,
                                                "trigger_count": 1,
                                                "triggers": "PERPREFIXFRR",
                                            },
                                            "19:42:50.053": {
                                                "log_type": "FSPF",
                                                "time_ms": 0,
                                                "total_nodes": 64,
                                                "trigger_count": 1,
                                                "triggers": "PERIODIC",
                                            },
                                            "19:42:50.555": {
                                                "log_type": "PPFRR",
                                                "time_ms": 0,
                                                "total_nodes": 64,
                                                "trigger_count": 1,
                                                "triggers": "PERPREFIXFRR",
                                            },
                                            "19:57:50.113": {
                                                "log_type": "FSPF",
                                                "time_ms": 0,
                                                "total_nodes": 64,
                                                "trigger_count": 1,
                                                "triggers": "PERIODIC",
                                            },
                                            "19:57:50.615": {
                                                "log_type": "PPFRR",
                                                "time_ms": 0,
                                                "total_nodes": 64,
                                                "trigger_count": 1,
                                                "triggers": "PERPREFIXFRR",
                                            },
                                            "20:12:50.174": {
                                                "log_type": "FSPF",
                                                "time_ms": 0,
                                                "total_nodes": 64,
                                                "trigger_count": 1,
                                                "triggers": "PERIODIC",
                                            },
                                            "20:12:50.676": {
                                                "log_type": "PPFRR",
                                                "time_ms": 0,
                                                "total_nodes": 64,
                                                "trigger_count": 1,
                                                "triggers": "PERPREFIXFRR",
                                            },
                                            "20:27:50.234": {
                                                "log_type": "FSPF",
                                                "time_ms": 0,
                                                "total_nodes": 64,
                                                "trigger_count": 1,
                                                "triggers": "PERIODIC",
                                            },
                                            "20:27:50.736": {
                                                "log_type": "PPFRR",
                                                "time_ms": 0,
                                                "total_nodes": 64,
                                                "trigger_count": 1,
                                                "triggers": "PERPREFIXFRR",
                                            },
                                            "20:42:50.295": {
                                                "log_type": "FSPF",
                                                "time_ms": 0,
                                                "total_nodes": 64,
                                                "trigger_count": 1,
                                                "triggers": "PERIODIC",
                                            },
                                            "20:42:50.797": {
                                                "log_type": "PPFRR",
                                                "time_ms": 0,
                                                "total_nodes": 64,
                                                "trigger_count": 1,
                                                "triggers": "PERPREFIXFRR",
                                            },
                                            "20:57:50.355": {
                                                "log_type": "FSPF",
                                                "time_ms": 0,
                                                "total_nodes": 64,
                                                "trigger_count": 1,
                                                "triggers": "PERIODIC",
                                            },
                                            "20:57:50.857": {
                                                "log_type": "PPFRR",
                                                "time_ms": 0,
                                                "total_nodes": 64,
                                                "trigger_count": 1,
                                                "triggers": "PERPREFIXFRR",
                                            },
                                            "21:12:50.416": {
                                                "log_type": "FSPF",
                                                "time_ms": 0,
                                                "total_nodes": 64,
                                                "trigger_count": 1,
                                                "triggers": "PERIODIC",
                                            },
                                            "21:12:50.918": {
                                                "log_type": "PPFRR",
                                                "time_ms": 0,
                                                "total_nodes": 64,
                                                "trigger_count": 1,
                                                "triggers": "PERPREFIXFRR",
                                            },
                                            "21:27:50.476": {
                                                "log_type": "FSPF",
                                                "time_ms": 0,
                                                "total_nodes": 64,
                                                "trigger_count": 1,
                                                "triggers": "PERIODIC",
                                            },
                                            "21:27:50.978": {
                                                "log_type": "PPFRR",
                                                "time_ms": 0,
                                                "total_nodes": 64,
                                                "trigger_count": 1,
                                                "triggers": "PERPREFIXFRR",
                                            },
                                            "21:42:50.537": {
                                                "log_type": "FSPF",
                                                "time_ms": 0,
                                                "total_nodes": 64,
                                                "trigger_count": 1,
                                                "triggers": "PERIODIC",
                                            },
                                            "21:42:51.039": {
                                                "log_type": "PPFRR",
                                                "time_ms": 0,
                                                "total_nodes": 64,
                                                "trigger_count": 1,
                                                "triggers": "PERPREFIXFRR",
                                            },
                                            "21:57:50.597": {
                                                "log_type": "FSPF",
                                                "time_ms": 0,
                                                "total_nodes": 64,
                                                "trigger_count": 1,
                                                "triggers": "PERIODIC",
                                            },
                                            "21:57:51.099": {
                                                "log_type": "PPFRR",
                                                "time_ms": 0,
                                                "total_nodes": 64,
                                                "trigger_count": 1,
                                                "triggers": "PERPREFIXFRR",
                                            },
                                            "22:12:50.658": {
                                                "log_type": "FSPF",
                                                "time_ms": 0,
                                                "total_nodes": 64,
                                                "trigger_count": 1,
                                                "triggers": "PERIODIC",
                                            },
                                            "22:12:51.159": {
                                                "log_type": "PPFRR",
                                                "time_ms": 0,
                                                "total_nodes": 64,
                                                "trigger_count": 1,
                                                "triggers": "PERPREFIXFRR",
                                            },
                                            "22:27:50.718": {
                                                "log_type": "FSPF",
                                                "time_ms": 0,
                                                "total_nodes": 64,
                                                "trigger_count": 1,
                                                "triggers": "PERIODIC",
                                            },
                                            "22:27:51.220": {
                                                "log_type": "PPFRR",
                                                "time_ms": 0,
                                                "total_nodes": 64,
                                                "trigger_count": 1,
                                                "triggers": "PERPREFIXFRR",
                                            },
                                            "22:42:50.779": {
                                                "log_type": "FSPF",
                                                "time_ms": 0,
                                                "total_nodes": 64,
                                                "trigger_count": 1,
                                                "triggers": "PERIODIC",
                                            },
                                            "22:42:51.280": {
                                                "log_type": "PPFRR",
                                                "time_ms": 0,
                                                "total_nodes": 64,
                                                "trigger_count": 1,
                                                "triggers": "PERPREFIXFRR",
                                            },
                                            "22:57:50.839": {
                                                "log_type": "FSPF",
                                                "time_ms": 0,
                                                "total_nodes": 64,
                                                "trigger_count": 1,
                                                "triggers": "PERIODIC",
                                            },
                                            "22:57:51.341": {
                                                "log_type": "PPFRR",
                                                "time_ms": 0,
                                                "total_nodes": 64,
                                                "trigger_count": 1,
                                                "triggers": "PERPREFIXFRR",
                                            },
                                            "23:12:50.899": {
                                                "log_type": "FSPF",
                                                "time_ms": 0,
                                                "total_nodes": 64,
                                                "trigger_count": 1,
                                                "triggers": "PERIODIC",
                                            },
                                            "23:12:51.401": {
                                                "log_type": "PPFRR",
                                                "time_ms": 0,
                                                "total_nodes": 64,
                                                "trigger_count": 1,
                                                "triggers": "PERPREFIXFRR",
                                            },
                                            "23:27:50.960": {
                                                "log_type": "FSPF",
                                                "time_ms": 0,
                                                "total_nodes": 64,
                                                "trigger_count": 1,
                                                "triggers": "PERIODIC",
                                            },
                                            "23:27:51.462": {
                                                "log_type": "PPFRR",
                                                "time_ms": 0,
                                                "total_nodes": 64,
                                                "trigger_count": 1,
                                                "triggers": "PERPREFIXFRR",
                                            },
                                            "23:42:51.020": {
                                                "log_type": "FSPF",
                                                "time_ms": 0,
                                                "total_nodes": 64,
                                                "trigger_count": 1,
                                                "triggers": "PERIODIC",
                                            },
                                            "23:42:51.522": {
                                                "log_type": "PPFRR",
                                                "time_ms": 0,
                                                "total_nodes": 64,
                                                "trigger_count": 1,
                                                "triggers": "PERPREFIXFRR",
                                            },
                                            "23:57:51.081": {
                                                "log_type": "FSPF",
                                                "time_ms": 0,
                                                "total_nodes": 64,
                                                "trigger_count": 1,
                                                "triggers": "PERIODIC",
                                            },
                                            "23:57:51.583": {
                                                "log_type": "PPFRR",
                                                "time_ms": 0,
                                                "total_nodes": 64,
                                                "trigger_count": 1,
                                                "triggers": "PERPREFIXFRR",
                                            },
                                        }
                                    },
                                    "Tue Oct  8 2019": {
                                        "timestamp": {
                                            "00:00:17.514": {
                                                "log_type": "PRC",
                                                "time_ms": 0,
                                                "total_nodes": 64,
                                                "trigger_count": 6,
                                                "first_trigger_lsp": "bla-host1.12-34",
                                                "triggers": "PREFIXBAD",
                                            },
                                            "00:00:18.016": {
                                                "log_type": "PPFRR",
                                                "time_ms": 0,
                                                "total_nodes": 64,
                                                "trigger_count": 1,
                                                "triggers": "PERPREFIXFRR",
                                            },
                                            "00:02:24.523": {
                                                "log_type": "PRC",
                                                "time_ms": 0,
                                                "total_nodes": 64,
                                                "trigger_count": 6,
                                                "first_trigger_lsp": "bla-host2.13-34",
                                                "triggers": "PREFIXGOOD",
                                            },
                                            "00:02:25.025": {
                                                "log_type": "PPFRR",
                                                "time_ms": 0,
                                                "total_nodes": 64,
                                                "trigger_count": 1,
                                                "triggers": "PERPREFIXFRR",
                                            },
                                            "00:12:51.141": {
                                                "log_type": "FSPF",
                                                "time_ms": 0,
                                                "total_nodes": 64,
                                                "trigger_count": 1,
                                                "triggers": "PERIODIC",
                                            },
                                            "00:12:51.643": {
                                                "log_type": "PPFRR",
                                                "time_ms": 0,
                                                "total_nodes": 64,
                                                "trigger_count": 1,
                                                "triggers": "PERPREFIXFRR",
                                            },
                                            "00:27:51.202": {
                                                "log_type": "FSPF",
                                                "time_ms": 0,
                                                "total_nodes": 64,
                                                "trigger_count": 1,
                                                "triggers": "PERIODIC",
                                            },
                                            "00:27:51.704": {
                                                "log_type": "PPFRR",
                                                "time_ms": 0,
                                                "total_nodes": 64,
                                                "trigger_count": 1,
                                                "triggers": "PERPREFIXFRR",
                                            },
                                            "00:42:51.262": {
                                                "log_type": "FSPF",
                                                "time_ms": 0,
                                                "total_nodes": 64,
                                                "trigger_count": 1,
                                                "triggers": "PERIODIC",
                                            },
                                            "00:42:51.764": {
                                                "log_type": "PPFRR",
                                                "time_ms": 0,
                                                "total_nodes": 64,
                                                "trigger_count": 1,
                                                "triggers": "PERPREFIXFRR",
                                            },
                                            "00:57:51.323": {
                                                "log_type": "FSPF",
                                                "time_ms": 0,
                                                "total_nodes": 64,
                                                "trigger_count": 1,
                                                "triggers": "PERIODIC",
                                            },
                                            "00:57:51.825": {
                                                "log_type": "PPFRR",
                                                "time_ms": 0,
                                                "total_nodes": 64,
                                                "trigger_count": 1,
                                                "triggers": "PERPREFIXFRR",
                                            },
                                            "01:12:51.383": {
                                                "log_type": "FSPF",
                                                "time_ms": 0,
                                                "total_nodes": 64,
                                                "trigger_count": 1,
                                                "triggers": "PERIODIC",
                                            },
                                            "01:12:51.885": {
                                                "log_type": "PPFRR",
                                                "time_ms": 0,
                                                "total_nodes": 64,
                                                "trigger_count": 1,
                                                "triggers": "PERPREFIXFRR",
                                            },
                                            "01:27:51.444": {
                                                "log_type": "FSPF",
                                                "time_ms": 0,
                                                "total_nodes": 64,
                                                "trigger_count": 1,
                                                "triggers": "PERIODIC",
                                            },
                                            "01:27:51.946": {
                                                "log_type": "PPFRR",
                                                "time_ms": 0,
                                                "total_nodes": 64,
                                                "trigger_count": 1,
                                                "triggers": "PERPREFIXFRR",
                                            },
                                            "01:42:51.504": {
                                                "log_type": "FSPF",
                                                "time_ms": 0,
                                                "total_nodes": 64,
                                                "trigger_count": 1,
                                                "triggers": "PERIODIC",
                                            },
                                            "01:42:52.006": {
                                                "log_type": "PPFRR",
                                                "time_ms": 0,
                                                "total_nodes": 64,
                                                "trigger_count": 1,
                                                "triggers": "PERPREFIXFRR",
                                            },
                                            "01:57:51.565": {
                                                "log_type": "FSPF",
                                                "time_ms": 0,
                                                "total_nodes": 64,
                                                "trigger_count": 1,
                                                "triggers": "PERIODIC",
                                            },
                                            "01:57:52.067": {
                                                "log_type": "PPFRR",
                                                "time_ms": 0,
                                                "total_nodes": 64,
                                                "trigger_count": 1,
                                                "triggers": "PERPREFIXFRR",
                                            },
                                            "02:12:51.625": {
                                                "log_type": "FSPF",
                                                "time_ms": 0,
                                                "total_nodes": 64,
                                                "trigger_count": 1,
                                                "triggers": "PERIODIC",
                                            },
                                            "02:12:52.127": {
                                                "log_type": "PPFRR",
                                                "time_ms": 0,
                                                "total_nodes": 64,
                                                "trigger_count": 1,
                                                "triggers": "PERPREFIXFRR",
                                            },
                                            "02:27:51.686": {
                                                "log_type": "FSPF",
                                                "time_ms": 0,
                                                "total_nodes": 64,
                                                "trigger_count": 1,
                                                "triggers": "PERIODIC",
                                            },
                                            "02:27:52.187": {
                                                "log_type": "PPFRR",
                                                "time_ms": 0,
                                                "total_nodes": 64,
                                                "trigger_count": 1,
                                                "triggers": "PERPREFIXFRR",
                                            },
                                            "02:42:51.746": {
                                                "log_type": "FSPF",
                                                "time_ms": 0,
                                                "total_nodes": 64,
                                                "trigger_count": 1,
                                                "triggers": "PERIODIC",
                                            },
                                            "02:42:52.248": {
                                                "log_type": "PPFRR",
                                                "time_ms": 0,
                                                "total_nodes": 64,
                                                "trigger_count": 1,
                                                "triggers": "PERPREFIXFRR",
                                            },
                                            "02:57:51.807": {
                                                "log_type": "FSPF",
                                                "time_ms": 0,
                                                "total_nodes": 64,
                                                "trigger_count": 1,
                                                "triggers": "PERIODIC",
                                            },
                                            "02:57:52.308": {
                                                "log_type": "PPFRR",
                                                "time_ms": 0,
                                                "total_nodes": 64,
                                                "trigger_count": 1,
                                                "triggers": "PERPREFIXFRR",
                                            },
                                            "03:12:51.867": {
                                                "log_type": "FSPF",
                                                "time_ms": 0,
                                                "total_nodes": 64,
                                                "trigger_count": 1,
                                                "triggers": "PERIODIC",
                                            },
                                            "03:12:52.369": {
                                                "log_type": "PPFRR",
                                                "time_ms": 0,
                                                "total_nodes": 64,
                                                "trigger_count": 1,
                                                "triggers": "PERPREFIXFRR",
                                            },
                                            "03:27:51.927": {
                                                "log_type": "FSPF",
                                                "time_ms": 0,
                                                "total_nodes": 64,
                                                "trigger_count": 1,
                                                "triggers": "PERIODIC",
                                            },
                                            "03:27:52.429": {
                                                "log_type": "PPFRR",
                                                "time_ms": 0,
                                                "total_nodes": 64,
                                                "trigger_count": 1,
                                                "triggers": "PERPREFIXFRR",
                                            },
                                            "03:42:51.988": {
                                                "log_type": "FSPF",
                                                "time_ms": 0,
                                                "total_nodes": 64,
                                                "trigger_count": 1,
                                                "triggers": "PERIODIC",
                                            },
                                            "03:42:52.490": {
                                                "log_type": "PPFRR",
                                                "time_ms": 0,
                                                "total_nodes": 64,
                                                "trigger_count": 1,
                                                "triggers": "PERPREFIXFRR",
                                            },
                                            "03:57:52.048": {
                                                "log_type": "FSPF",
                                                "time_ms": 0,
                                                "total_nodes": 64,
                                                "trigger_count": 1,
                                                "triggers": "PERIODIC",
                                            },
                                            "03:57:52.550": {
                                                "log_type": "PPFRR",
                                                "time_ms": 0,
                                                "total_nodes": 64,
                                                "trigger_count": 1,
                                                "triggers": "PERPREFIXFRR",
                                            },
                                            "04:12:52.109": {
                                                "log_type": "FSPF",
                                                "time_ms": 0,
                                                "total_nodes": 64,
                                                "trigger_count": 1,
                                                "triggers": "PERIODIC",
                                            },
                                            "04:12:52.611": {
                                                "log_type": "PPFRR",
                                                "time_ms": 0,
                                                "total_nodes": 64,
                                                "trigger_count": 1,
                                                "triggers": "PERPREFIXFRR",
                                            },
                                            "04:27:52.169": {
                                                "log_type": "FSPF",
                                                "time_ms": 0,
                                                "total_nodes": 64,
                                                "trigger_count": 1,
                                                "triggers": "PERIODIC",
                                            },
                                            "04:27:52.671": {
                                                "log_type": "PPFRR",
                                                "time_ms": 0,
                                                "total_nodes": 64,
                                                "trigger_count": 1,
                                                "triggers": "PERPREFIXFRR",
                                            },
                                            "04:42:52.230": {
                                                "log_type": "FSPF",
                                                "time_ms": 0,
                                                "total_nodes": 64,
                                                "trigger_count": 1,
                                                "triggers": "PERIODIC",
                                            },
                                            "04:42:52.732": {
                                                "log_type": "PPFRR",
                                                "time_ms": 0,
                                                "total_nodes": 64,
                                                "trigger_count": 1,
                                                "triggers": "PERPREFIXFRR",
                                            },
                                            "04:57:52.290": {
                                                "log_type": "FSPF",
                                                "time_ms": 0,
                                                "total_nodes": 64,
                                                "trigger_count": 1,
                                                "triggers": "PERIODIC",
                                            },
                                            "04:57:52.792": {
                                                "log_type": "PPFRR",
                                                "time_ms": 0,
                                                "total_nodes": 64,
                                                "trigger_count": 1,
                                                "triggers": "PERPREFIXFRR",
                                            },
                                            "05:12:52.351": {
                                                "log_type": "FSPF",
                                                "time_ms": 0,
                                                "total_nodes": 64,
                                                "trigger_count": 1,
                                                "triggers": "PERIODIC",
                                            },
                                            "05:12:52.853": {
                                                "log_type": "PPFRR",
                                                "time_ms": 0,
                                                "total_nodes": 64,
                                                "trigger_count": 1,
                                                "triggers": "PERPREFIXFRR",
                                            },
                                            "05:27:52.411": {
                                                "log_type": "FSPF",
                                                "time_ms": 0,
                                                "total_nodes": 64,
                                                "trigger_count": 1,
                                                "triggers": "PERIODIC",
                                            },
                                            "05:27:52.913": {
                                                "log_type": "PPFRR",
                                                "time_ms": 0,
                                                "total_nodes": 64,
                                                "trigger_count": 1,
                                                "triggers": "PERPREFIXFRR",
                                            },
                                            "05:42:52.472": {
                                                "log_type": "FSPF",
                                                "time_ms": 0,
                                                "total_nodes": 64,
                                                "trigger_count": 1,
                                                "triggers": "PERIODIC",
                                            },
                                            "05:42:52.974": {
                                                "log_type": "PPFRR",
                                                "time_ms": 0,
                                                "total_nodes": 64,
                                                "trigger_count": 1,
                                                "triggers": "PERPREFIXFRR",
                                            },
                                            "05:57:52.532": {
                                                "log_type": "FSPF",
                                                "time_ms": 0,
                                                "total_nodes": 64,
                                                "trigger_count": 1,
                                                "triggers": "PERIODIC",
                                            },
                                            "05:57:53.034": {
                                                "log_type": "PPFRR",
                                                "time_ms": 0,
                                                "total_nodes": 64,
                                                "trigger_count": 1,
                                                "triggers": "PERPREFIXFRR",
                                            },
                                            "06:12:52.593": {
                                                "log_type": "FSPF",
                                                "time_ms": 0,
                                                "total_nodes": 64,
                                                "trigger_count": 1,
                                                "triggers": "PERIODIC",
                                            },
                                            "06:12:53.095": {
                                                "log_type": "PPFRR",
                                                "time_ms": 0,
                                                "total_nodes": 64,
                                                "trigger_count": 1,
                                                "triggers": "PERPREFIXFRR",
                                            },
                                            "06:27:52.653": {
                                                "log_type": "FSPF",
                                                "time_ms": 0,
                                                "total_nodes": 64,
                                                "trigger_count": 1,
                                                "triggers": "PERIODIC",
                                            },
                                            "06:27:53.155": {
                                                "log_type": "PPFRR",
                                                "time_ms": 0,
                                                "total_nodes": 64,
                                                "trigger_count": 1,
                                                "triggers": "PERPREFIXFRR",
                                            },
                                            "06:42:52.714": {
                                                "log_type": "FSPF",
                                                "time_ms": 0,
                                                "total_nodes": 64,
                                                "trigger_count": 1,
                                                "triggers": "PERIODIC",
                                            },
                                            "06:42:53.216": {
                                                "log_type": "PPFRR",
                                                "time_ms": 0,
                                                "total_nodes": 64,
                                                "trigger_count": 1,
                                                "triggers": "PERPREFIXFRR",
                                            },
                                            "06:57:52.774": {
                                                "log_type": "FSPF",
                                                "time_ms": 0,
                                                "total_nodes": 64,
                                                "trigger_count": 1,
                                                "triggers": "PERIODIC",
                                            },
                                            "06:57:53.276": {
                                                "log_type": "PPFRR",
                                                "time_ms": 0,
                                                "total_nodes": 64,
                                                "trigger_count": 1,
                                                "triggers": "PERPREFIXFRR",
                                            },
                                            "07:12:52.834": {
                                                "log_type": "FSPF",
                                                "time_ms": 0,
                                                "total_nodes": 64,
                                                "trigger_count": 1,
                                                "triggers": "PERIODIC",
                                            },
                                            "07:12:53.336": {
                                                "log_type": "PPFRR",
                                                "time_ms": 0,
                                                "total_nodes": 64,
                                                "trigger_count": 1,
                                                "triggers": "PERPREFIXFRR",
                                            },
                                            "07:27:52.895": {
                                                "log_type": "FSPF",
                                                "time_ms": 0,
                                                "total_nodes": 64,
                                                "trigger_count": 1,
                                                "triggers": "PERIODIC",
                                            },
                                            "07:27:53.397": {
                                                "log_type": "PPFRR",
                                                "time_ms": 0,
                                                "total_nodes": 64,
                                                "trigger_count": 1,
                                                "triggers": "PERPREFIXFRR",
                                            },
                                            "07:42:52.955": {
                                                "log_type": "FSPF",
                                                "time_ms": 0,
                                                "total_nodes": 64,
                                                "trigger_count": 1,
                                                "triggers": "PERIODIC",
                                            },
                                            "07:42:53.457": {
                                                "log_type": "PPFRR",
                                                "time_ms": 0,
                                                "total_nodes": 64,
                                                "trigger_count": 1,
                                                "triggers": "PERPREFIXFRR",
                                            },
                                            "07:57:53.015": {
                                                "log_type": "FSPF",
                                                "time_ms": 0,
                                                "total_nodes": 64,
                                                "trigger_count": 1,
                                                "triggers": "PERIODIC",
                                            },
                                            "07:57:53.517": {
                                                "log_type": "PPFRR",
                                                "time_ms": 0,
                                                "total_nodes": 64,
                                                "trigger_count": 1,
                                                "triggers": "PERPREFIXFRR",
                                            },
                                            "08:12:53.076": {
                                                "log_type": "FSPF",
                                                "time_ms": 0,
                                                "total_nodes": 64,
                                                "trigger_count": 1,
                                                "triggers": "PERIODIC",
                                            },
                                            "08:12:53.578": {
                                                "log_type": "PPFRR",
                                                "time_ms": 0,
                                                "total_nodes": 64,
                                                "trigger_count": 1,
                                                "triggers": "PERPREFIXFRR",
                                            },
                                            "08:15:04.265": {
                                                "log_type": "PRC",
                                                "time_ms": 0,
                                                "total_nodes": 64,
                                                "trigger_count": 1,
                                                "first_trigger_lsp": "bla-9.blahlab-cld.12-34",
                                                "triggers": "PREFIXBAD",
                                            },
                                            "08:15:04.418": {
                                                "log_type": "PRC",
                                                "time_ms": 0,
                                                "total_nodes": 64,
                                                "trigger_count": 1,
                                                "first_trigger_lsp": "bla-9.blahlab-cld.12-34",
                                                "triggers": "PREFIXGOOD",
                                            },
                                            "08:15:04.920": {
                                                "log_type": "PPFRR",
                                                "time_ms": 0,
                                                "total_nodes": 64,
                                                "trigger_count": 1,
                                                "triggers": "PERPREFIXFRR",
                                            },
                                            "08:17:55.366": {
                                                "log_type": "PRC",
                                                "time_ms": 0,
                                                "total_nodes": 64,
                                                "trigger_count": 1,
                                                "first_trigger_lsp": "bla-9.blahlab-cld.12-34",
                                                "triggers": "PREFIXBAD",
                                            },
                                            "08:17:55.868": {
                                                "log_type": "PPFRR",
                                                "time_ms": 0,
                                                "total_nodes": 64,
                                                "trigger_count": 1,
                                                "triggers": "PERPREFIXFRR",
                                            },
                                            "08:27:53.136": {
                                                "log_type": "FSPF",
                                                "time_ms": 0,
                                                "total_nodes": 64,
                                                "trigger_count": 1,
                                                "triggers": "PERIODIC",
                                            },
                                            "08:27:53.638": {
                                                "log_type": "PPFRR",
                                                "time_ms": 0,
                                                "total_nodes": 64,
                                                "trigger_count": 1,
                                                "triggers": "PERPREFIXFRR",
                                            },
                                            "08:42:53.197": {
                                                "log_type": "FSPF",
                                                "time_ms": 0,
                                                "total_nodes": 64,
                                                "trigger_count": 1,
                                                "triggers": "PERIODIC",
                                            },
                                            "08:42:53.699": {
                                                "log_type": "PPFRR",
                                                "time_ms": 0,
                                                "total_nodes": 64,
                                                "trigger_count": 1,
                                                "triggers": "PERPREFIXFRR",
                                            },
                                            "08:57:53.257": {
                                                "log_type": "FSPF",
                                                "time_ms": 0,
                                                "total_nodes": 64,
                                                "trigger_count": 1,
                                                "triggers": "PERIODIC",
                                            },
                                            "08:57:53.759": {
                                                "log_type": "PPFRR",
                                                "time_ms": 0,
                                                "total_nodes": 64,
                                                "trigger_count": 1,
                                                "triggers": "PERPREFIXFRR",
                                            },
                                            "09:12:53.318": {
                                                "log_type": "FSPF",
                                                "time_ms": 0,
                                                "total_nodes": 64,
                                                "trigger_count": 1,
                                                "triggers": "PERIODIC",
                                            },
                                            "09:12:53.820": {
                                                "log_type": "PPFRR",
                                                "time_ms": 0,
                                                "total_nodes": 64,
                                                "trigger_count": 1,
                                                "triggers": "PERPREFIXFRR",
                                            },
                                            "09:27:53.378": {
                                                "log_type": "FSPF",
                                                "time_ms": 0,
                                                "total_nodes": 64,
                                                "trigger_count": 1,
                                                "triggers": "PERIODIC",
                                            },
                                            "09:27:53.880": {
                                                "log_type": "PPFRR",
                                                "time_ms": 0,
                                                "total_nodes": 64,
                                                "trigger_count": 1,
                                                "triggers": "PERPREFIXFRR",
                                            },
                                            "09:42:53.439": {
                                                "log_type": "FSPF",
                                                "time_ms": 0,
                                                "total_nodes": 64,
                                                "trigger_count": 1,
                                                "triggers": "PERIODIC",
                                            },
                                            "09:42:53.941": {
                                                "log_type": "PPFRR",
                                                "time_ms": 0,
                                                "total_nodes": 64,
                                                "trigger_count": 1,
                                                "triggers": "PERPREFIXFRR",
                                            },
                                            "09:57:53.499": {
                                                "log_type": "FSPF",
                                                "time_ms": 0,
                                                "total_nodes": 64,
                                                "trigger_count": 1,
                                                "triggers": "PERIODIC",
                                            },
                                            "09:57:54.001": {
                                                "log_type": "PPFRR",
                                                "time_ms": 0,
                                                "total_nodes": 64,
                                                "trigger_count": 1,
                                                "triggers": "PERPREFIXFRR",
                                            },
                                            "10:12:53.560": {
                                                "log_type": "FSPF",
                                                "time_ms": 0,
                                                "total_nodes": 64,
                                                "trigger_count": 1,
                                                "triggers": "PERIODIC",
                                            },
                                            "10:12:54.061": {
                                                "log_type": "PPFRR",
                                                "time_ms": 0,
                                                "total_nodes": 64,
                                                "trigger_count": 1,
                                                "triggers": "PERPREFIXFRR",
                                            },
                                            "10:27:53.620": {
                                                "log_type": "FSPF",
                                                "time_ms": 0,
                                                "total_nodes": 64,
                                                "trigger_count": 1,
                                                "triggers": "PERIODIC",
                                            },
                                            "10:27:54.122": {
                                                "log_type": "PPFRR",
                                                "time_ms": 0,
                                                "total_nodes": 64,
                                                "trigger_count": 1,
                                                "triggers": "PERPREFIXFRR",
                                            },
                                            "10:42:53.681": {
                                                "log_type": "FSPF",
                                                "time_ms": 0,
                                                "total_nodes": 64,
                                                "trigger_count": 1,
                                                "triggers": "PERIODIC",
                                            },
                                            "10:42:54.182": {
                                                "log_type": "PPFRR",
                                                "time_ms": 0,
                                                "total_nodes": 64,
                                                "trigger_count": 1,
                                                "triggers": "PERPREFIXFRR",
                                            },
                                            "10:57:53.741": {
                                                "log_type": "FSPF",
                                                "time_ms": 0,
                                                "total_nodes": 64,
                                                "trigger_count": 1,
                                                "triggers": "PERIODIC",
                                            },
                                            "10:57:54.243": {
                                                "log_type": "PPFRR",
                                                "time_ms": 0,
                                                "total_nodes": 64,
                                                "trigger_count": 1,
                                                "triggers": "PERPREFIXFRR",
                                            },
                                            "11:12:53.801": {
                                                "log_type": "FSPF",
                                                "time_ms": 0,
                                                "total_nodes": 64,
                                                "trigger_count": 1,
                                                "triggers": "PERIODIC",
                                            },
                                            "11:12:54.303": {
                                                "log_type": "PPFRR",
                                                "time_ms": 0,
                                                "total_nodes": 64,
                                                "trigger_count": 1,
                                                "triggers": "PERPREFIXFRR",
                                            },
                                            "11:27:53.862": {
                                                "log_type": "FSPF",
                                                "time_ms": 0,
                                                "total_nodes": 64,
                                                "trigger_count": 1,
                                                "triggers": "PERIODIC",
                                            },
                                            "11:27:54.364": {
                                                "log_type": "PPFRR",
                                                "time_ms": 0,
                                                "total_nodes": 64,
                                                "trigger_count": 1,
                                                "triggers": "PERPREFIXFRR",
                                            },
                                            "11:42:53.922": {
                                                "log_type": "FSPF",
                                                "time_ms": 0,
                                                "total_nodes": 64,
                                                "trigger_count": 1,
                                                "triggers": "PERIODIC",
                                            },
                                            "11:42:54.424": {
                                                "log_type": "PPFRR",
                                                "time_ms": 0,
                                                "total_nodes": 64,
                                                "trigger_count": 1,
                                                "triggers": "PERPREFIXFRR",
                                            },
                                            "11:57:53.983": {
                                                "log_type": "FSPF",
                                                "time_ms": 0,
                                                "total_nodes": 64,
                                                "trigger_count": 1,
                                                "triggers": "PERIODIC",
                                            },
                                            "11:57:54.485": {
                                                "log_type": "PPFRR",
                                                "time_ms": 0,
                                                "total_nodes": 64,
                                                "trigger_count": 1,
                                                "triggers": "PERPREFIXFRR",
                                            },
                                        }
                                    },
                                }
                            }
                        }
                    }
                }
            }
        }
    }

    golden_output_1 = {'execute.return_value': '''
        RP/0/RSP0/CPU0:bl1-tatooine#show isis spf-log
        Tue Oct  8 17:37:35.029 EDT

           IS-IS TEST Level 2 IPv4 Unicast Route Calculation Log
                            Time Total Trig.
        Timestamp    Type   (ms) Nodes Count First Trigger LSP    Triggers
        ------------ ----- ----- ----- ----- -------------------- -----------------------
        --- Mon Oct  7 2019 ---
        17:57:50.131 PPFRR     0    64     1                      PERPREFIXFRR
        18:12:49.690  FSPF     0    64     1                      PERIODIC
        18:12:50.192 PPFRR     0    64     1                      PERPREFIXFRR
        18:27:49.750  FSPF     0    64     1                      PERIODIC
        18:27:50.252 PPFRR     0    64     1                      PERPREFIXFRR
        18:42:49.811  FSPF     0    64     1                      PERIODIC
        18:42:50.313 PPFRR     0    64     1                      PERPREFIXFRR
        18:57:49.871  FSPF     0    64     1                      PERIODIC
        18:57:50.373 PPFRR     0    64     1                      PERPREFIXFRR
        19:12:49.932  FSPF     0    64     1                      PERIODIC
        19:12:50.434 PPFRR     0    64     1                      PERPREFIXFRR
        19:27:49.992  FSPF     0    64     1                      PERIODIC
        19:27:50.494 PPFRR     0    64     1                      PERPREFIXFRR
        19:42:50.053  FSPF     0    64     1                      PERIODIC
        19:42:50.555 PPFRR     0    64     1                      PERPREFIXFRR
        19:57:50.113  FSPF     0    64     1                      PERIODIC
        19:57:50.615 PPFRR     0    64     1                      PERPREFIXFRR
        20:12:50.174  FSPF     0    64     1                      PERIODIC
        20:12:50.676 PPFRR     0    64     1                      PERPREFIXFRR
        20:27:50.234  FSPF     0    64     1                      PERIODIC
        20:27:50.736 PPFRR     0    64     1                      PERPREFIXFRR
        20:42:50.295  FSPF     0    64     1                      PERIODIC
        20:42:50.797 PPFRR     0    64     1                      PERPREFIXFRR
        20:57:50.355  FSPF     0    64     1                      PERIODIC
        20:57:50.857 PPFRR     0    64     1                      PERPREFIXFRR
        21:12:50.416  FSPF     0    64     1                      PERIODIC
        21:12:50.918 PPFRR     0    64     1                      PERPREFIXFRR
        21:27:50.476  FSPF     0    64     1                      PERIODIC
        21:27:50.978 PPFRR     0    64     1                      PERPREFIXFRR
        21:42:50.537  FSPF     0    64     1                      PERIODIC
        21:42:51.039 PPFRR     0    64     1                      PERPREFIXFRR
        21:57:50.597  FSPF     0    64     1                      PERIODIC
        21:57:51.099 PPFRR     0    64     1                      PERPREFIXFRR
        22:12:50.658  FSPF     0    64     1                      PERIODIC
        22:12:51.159 PPFRR     0    64     1                      PERPREFIXFRR
        22:27:50.718  FSPF     0    64     1                      PERIODIC
        22:27:51.220 PPFRR     0    64     1                      PERPREFIXFRR
        22:42:50.779  FSPF     0    64     1                      PERIODIC
        22:42:51.280 PPFRR     0    64     1                      PERPREFIXFRR
        22:57:50.839  FSPF     0    64     1                      PERIODIC
        22:57:51.341 PPFRR     0    64     1                      PERPREFIXFRR
        23:12:50.899  FSPF     0    64     1                      PERIODIC
        23:12:51.401 PPFRR     0    64     1                      PERPREFIXFRR
        23:27:50.960  FSPF     0    64     1                      PERIODIC
        23:27:51.462 PPFRR     0    64     1                      PERPREFIXFRR
        23:42:51.020  FSPF     0    64     1                      PERIODIC
        23:42:51.522 PPFRR     0    64     1                      PERPREFIXFRR
        23:57:51.081  FSPF     0    64     1                      PERIODIC
        23:57:51.583 PPFRR     0    64     1                      PERPREFIXFRR
        --- Tue Oct  8 2019 ---
        00:00:17.514   PRC     0    64     6      bla-host1.12-34 PREFIXBAD
        00:00:18.016 PPFRR     0    64     1                      PERPREFIXFRR
        00:02:24.523   PRC     0    64     6      bla-host2.13-34 PREFIXGOOD
        00:02:25.025 PPFRR     0    64     1                      PERPREFIXFRR
        00:12:51.141  FSPF     0    64     1                      PERIODIC
        00:12:51.643 PPFRR     0    64     1                      PERPREFIXFRR
        00:27:51.202  FSPF     0    64     1                      PERIODIC
        00:27:51.704 PPFRR     0    64     1                      PERPREFIXFRR
        00:42:51.262  FSPF     0    64     1                      PERIODIC
        00:42:51.764 PPFRR     0    64     1                      PERPREFIXFRR
        00:57:51.323  FSPF     0    64     1                      PERIODIC
        00:57:51.825 PPFRR     0    64     1                      PERPREFIXFRR
        01:12:51.383  FSPF     0    64     1                      PERIODIC
        01:12:51.885 PPFRR     0    64     1                      PERPREFIXFRR
        01:27:51.444  FSPF     0    64     1                      PERIODIC
        01:27:51.946 PPFRR     0    64     1                      PERPREFIXFRR
        01:42:51.504  FSPF     0    64     1                      PERIODIC
        01:42:52.006 PPFRR     0    64     1                      PERPREFIXFRR
        01:57:51.565  FSPF     0    64     1                      PERIODIC
        01:57:52.067 PPFRR     0    64     1                      PERPREFIXFRR
        02:12:51.625  FSPF     0    64     1                      PERIODIC
        02:12:52.127 PPFRR     0    64     1                      PERPREFIXFRR
        02:27:51.686  FSPF     0    64     1                      PERIODIC
        02:27:52.187 PPFRR     0    64     1                      PERPREFIXFRR
        02:42:51.746  FSPF     0    64     1                      PERIODIC
        02:42:52.248 PPFRR     0    64     1                      PERPREFIXFRR
        02:57:51.807  FSPF     0    64     1                      PERIODIC
        02:57:52.308 PPFRR     0    64     1                      PERPREFIXFRR
        03:12:51.867  FSPF     0    64     1                      PERIODIC
        03:12:52.369 PPFRR     0    64     1                      PERPREFIXFRR
        03:27:51.927  FSPF     0    64     1                      PERIODIC
        03:27:52.429 PPFRR     0    64     1                      PERPREFIXFRR
        03:42:51.988  FSPF     0    64     1                      PERIODIC
        03:42:52.490 PPFRR     0    64     1                      PERPREFIXFRR
        03:57:52.048  FSPF     0    64     1                      PERIODIC
        03:57:52.550 PPFRR     0    64     1                      PERPREFIXFRR
        04:12:52.109  FSPF     0    64     1                      PERIODIC
        04:12:52.611 PPFRR     0    64     1                      PERPREFIXFRR
        04:27:52.169  FSPF     0    64     1                      PERIODIC
        04:27:52.671 PPFRR     0    64     1                      PERPREFIXFRR
        04:42:52.230  FSPF     0    64     1                      PERIODIC
        04:42:52.732 PPFRR     0    64     1                      PERPREFIXFRR
        04:57:52.290  FSPF     0    64     1                      PERIODIC
        04:57:52.792 PPFRR     0    64     1                      PERPREFIXFRR
        05:12:52.351  FSPF     0    64     1                      PERIODIC
        05:12:52.853 PPFRR     0    64     1                      PERPREFIXFRR
        05:27:52.411  FSPF     0    64     1                      PERIODIC
        05:27:52.913 PPFRR     0    64     1                      PERPREFIXFRR
        05:42:52.472  FSPF     0    64     1                      PERIODIC
        05:42:52.974 PPFRR     0    64     1                      PERPREFIXFRR
        05:57:52.532  FSPF     0    64     1                      PERIODIC
        05:57:53.034 PPFRR     0    64     1                      PERPREFIXFRR
        06:12:52.593  FSPF     0    64     1                      PERIODIC
        06:12:53.095 PPFRR     0    64     1                      PERPREFIXFRR
        06:27:52.653  FSPF     0    64     1                      PERIODIC
        06:27:53.155 PPFRR     0    64     1                      PERPREFIXFRR
        06:42:52.714  FSPF     0    64     1                      PERIODIC
        06:42:53.216 PPFRR     0    64     1                      PERPREFIXFRR
        06:57:52.774  FSPF     0    64     1                      PERIODIC
        06:57:53.276 PPFRR     0    64     1                      PERPREFIXFRR
        07:12:52.834  FSPF     0    64     1                      PERIODIC
        07:12:53.336 PPFRR     0    64     1                      PERPREFIXFRR
        07:27:52.895  FSPF     0    64     1                      PERIODIC
        07:27:53.397 PPFRR     0    64     1                      PERPREFIXFRR
        07:42:52.955  FSPF     0    64     1                      PERIODIC
        07:42:53.457 PPFRR     0    64     1                      PERPREFIXFRR
        07:57:53.015  FSPF     0    64     1                      PERIODIC
        07:57:53.517 PPFRR     0    64     1                      PERPREFIXFRR
        08:12:53.076  FSPF     0    64     1                      PERIODIC
        08:12:53.578 PPFRR     0    64     1                      PERPREFIXFRR
        08:15:04.265   PRC     0    64     1 bla-9.blahlab-cld.12-34 PREFIXBAD
        08:15:04.418   PRC     0    64     1 bla-9.blahlab-cld.12-34 PREFIXGOOD
        08:15:04.920 PPFRR     0    64     1                      PERPREFIXFRR
        08:17:55.366   PRC     0    64     1 bla-9.blahlab-cld.12-34 PREFIXBAD
        08:17:55.868 PPFRR     0    64     1                      PERPREFIXFRR
        08:27:53.136  FSPF     0    64     1                      PERIODIC
        08:27:53.638 PPFRR     0    64     1                      PERPREFIXFRR
        08:42:53.197  FSPF     0    64     1                      PERIODIC
        08:42:53.699 PPFRR     0    64     1                      PERPREFIXFRR
        08:57:53.257  FSPF     0    64     1                      PERIODIC
        08:57:53.759 PPFRR     0    64     1                      PERPREFIXFRR
        09:12:53.318  FSPF     0    64     1                      PERIODIC
        09:12:53.820 PPFRR     0    64     1                      PERPREFIXFRR
        09:27:53.378  FSPF     0    64     1                      PERIODIC
        09:27:53.880 PPFRR     0    64     1                      PERPREFIXFRR
        09:42:53.439  FSPF     0    64     1                      PERIODIC
        09:42:53.941 PPFRR     0    64     1                      PERPREFIXFRR
        09:57:53.499  FSPF     0    64     1                      PERIODIC
        09:57:54.001 PPFRR     0    64     1                      PERPREFIXFRR
        10:12:53.560  FSPF     0    64     1                      PERIODIC
        10:12:54.061 PPFRR     0    64     1                      PERPREFIXFRR
        10:27:53.620  FSPF     0    64     1                      PERIODIC
        10:27:54.122 PPFRR     0    64     1                      PERPREFIXFRR
        10:42:53.681  FSPF     0    64     1                      PERIODIC
        10:42:54.182 PPFRR     0    64     1                      PERPREFIXFRR
        10:57:53.741  FSPF     0    64     1                      PERIODIC
        10:57:54.243 PPFRR     0    64     1                      PERPREFIXFRR
        11:12:53.801  FSPF     0    64     1                      PERIODIC
        11:12:54.303 PPFRR     0    64     1                      PERPREFIXFRR
        11:27:53.862  FSPF     0    64     1                      PERIODIC
        11:27:54.364 PPFRR     0    64     1                      PERPREFIXFRR
        11:42:53.922  FSPF     0    64     1                      PERIODIC
        11:42:54.424 PPFRR     0    64     1                      PERPREFIXFRR
        11:57:53.983  FSPF     0    64     1                      PERIODIC
        11:57:54.485 PPFRR     0    64     1                      PERPREFIXFRR
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

if __name__ == '__main__':
    unittest.main()
