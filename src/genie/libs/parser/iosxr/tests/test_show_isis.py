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
    ShowIsisSpfLogDetail,
    ShowIsisDatabaseDetail,
    ShowIsisSegmentRoutingLabelTable,
)

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
                        "system_id": "3333.3333.3333",
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

    golden_parsed_output_2 = {
        'instance': {
            'Cisco': {
                'process_id': 'Cisco',
                'instance': '0',
                'vrf': {
                    'default': {
                        'system_id': '1781.8132.1195',
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
        System Id: 1781.8132.1195 
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
        "instance": {
            "isp": {
                "address_family": {
                    "IPv4 Unicast": {
                        "spf_log": {
                            1: {
                                "type": "FSPF",
                                "time_ms": 1,
                                "level": 1,
                                "total_nodes": 1,
                                "trigger_count": 1,
                                "first_trigger_lsp": "12a5.00-00",
                                "triggers": "NEWLSP0",
                                "start_timestamp": "Mon Aug 16 2004 19:25:35.140",
                                "delay_ms": 51, 
                                "delay_info": "since first trigger",
                                "spt_calculation": {
                                    "cpu_time_ms": 0, 
                                    "real_time_ms": 0},
                                "prefix_update": {
                                    "cpu_time_ms": 1, 
                                    "real_time_ms": 1},
                                "new_lsp_arrivals": 0,
                                "next_wait_interval_ms": 200,
                                "results": {
                                    "nodes": {
                                        "reach": 1, 
                                        "unreach": 0, 
                                        "total": 1},
                                    "prefixes": {
                                        "items": {
                                            "critical_priority": {
                                                "reach": 0,
                                                "unreach": 0,
                                                "total": 0,
                                            },
                                            "high_priority": {
                                                "reach": 0,
                                                "unreach": 0,
                                                "total": 0,
                                            },
                                            "medium_priority": {
                                                "reach": 0,
                                                "unreach": 0,
                                                "total": 0,
                                            },
                                            "low_priority": {
                                                "reach": 0,
                                                "unreach": 0,
                                                "total": 0,
                                            },
                                            "all_priority": {
                                                "reach": 0,
                                                "unreach": 0,
                                                "total": 0,
                                            },
                                        },                                        
                                        "routes": {
                                            "critical_priority": {
                                                "reach": 0, 
                                                "total": 0},
                                            "high_priority": {
                                                "reach": 0, 
                                                "total": 0},
                                            "medium_priority": {
                                                "reach": 0, 
                                                "total": 0},
                                            "low_priority": {
                                                "reach": 0, 
                                                "total": 0},
                                            "all_priority": {
                                                "reach": 0, 
                                                "total": 0
                                            },
                                        }
                                    },
                                },
                            },
                        }
                    }
                }
            }
        }
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
                                    '5286.4470.2149': {
                                        'dynamic_hostname': 'host-1.bla-site3'}, 
                                    '9839.2319.8337': {
                                        'dynamic_hostname': 'host3-bla'}, 
                                    '3549.6375.2540': {
                                        'dynamic_hostname': 'abc-3.bla-site4'}, 
                                    '0670.7021.9090': {
                                            'dynamic_hostname': 'host2-abc'},
                                    '9853.9997.6489': {
                                        'dynamic_hostname': 'abc2-xyz', 
                                        'local_router': True}}}}}}}}}

    golden_output_1 = {'execute.return_value': '''
        show isis hostname

        Thu Oct  3 10:53:16.534 EDT

        IS-IS TEST1 hostnames
        Level  System ID      Dynamic Hostname
         2     5286.4470.2149 host-1.bla-site3
         2     9839.2319.8337 host3-bla
         2     3549.6375.2540 abc-3.bla-site4
         2     0670.7021.9090 host2-abc
         2   * 9853.9997.6489 abc2-xyz
    '''}

    golden_parsed_output_2 = {
        "isis": {
            "test": {
                "vrf": {
                    "default": {
                        "level": {
                            2: {
                                "system_id": {
                                    "2222.2222.2222": {
                                        "dynamic_hostname": "R2"},
                                    "8888.8888.8888": {
                                        "dynamic_hostname": "R8"},
                                    "7777.7777.7777": {
                                        "dynamic_hostname": "R7"},
                                    "3333.3333.3333": {
                                        "dynamic_hostname": "R3",
                                        "local_router": True,
                                    },
                                    "5555.5555.5555": {
                                        "dynamic_hostname": "R5"},
                                    "9999.9999.9999": {
                                        "dynamic_hostname": "R9"},
                                }
                            },
                            1: {
                                "system_id": {
                                    "4444.4444.4444": {
                                        "dynamic_hostname": "R4"},
                                    "6666.6666.6666": {
                                        "dynamic_hostname": "R6"},
                                    "7777.7777.7777": {
                                        "dynamic_hostname": "R7"},
                                    "3333.3333.3333": {
                                        "dynamic_hostname": "R3",
                                        "local_router": True,
                                    },
                                    "5555.5555.5555": {
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
         2     2222.2222.2222 R2
         1     4444.4444.4444 R4
         1     6666.6666.6666 R6
         2     8888.8888.8888 R8
         1,2   7777.7777.7777 R7
         1,2 * 3333.3333.3333 R3
         1,2   5555.5555.5555 R5
         2     9999.9999.9999 R9
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
                        "system_id": "0123.4567.8910",
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
          System Id: 0123.4567.8910
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
                        "system_id": "2222.2222.2222",
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
                        "system_id": "2222.2222.2222",
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
          System Id: 2222.2222.2222
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
          System Id: 2222.2222.2222
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
