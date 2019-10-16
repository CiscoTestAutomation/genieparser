# Python
import unittest
from unittest.mock import Mock

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError, SchemaMissingKeyError

# iosxr show_isis
from genie.libs.parser.iosxr.show_isis import (
    ShowIsis,
    ShowIsisSpfLog,
    ShowIsisSpfLogDetail,
    ShowIsisHostname,
    ShowIsisProtocol,
    ShowIsisNeighbors,
    ShowIsisAdjacency, 
    ShowIsisStatistics,
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

if __name__ == '__main__':
    unittest.main()
