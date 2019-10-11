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

if __name__ == '__main__':
    unittest.main()
