
# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError,\
                                             SchemaMissingKeyError

# iosxe show_ospf
from genie.libs.parser.iosxe.show_ospf import (ShowIpOspf,
                                               ShowIpOspfInterface,
                                               ShowIpOspfNeighborDetail,
                                               ShowIpOspfShamLinks,
                                               ShowIpOspfVirtualLinks,
                                               ShowIpOspfDatabase,
                                               ShowIpOspfDatabaseRouter,
                                               ShowIpOspfDatabaseExternal,
                                               ShowIpOspfDatabaseNetwork,
                                               ShowIpOspfDatabaseSummary,
                                               ShowIpOspfDatabaseOpaqueArea,
                                               ShowIpOspfMplsLdpInterface,
                                               ShowIpOspfMplsTrafficEngLink,
                                               ShowIpOspfMaxMetric,
                                               ShowIpOspfTraffic,
                                               ShowIpOspfNeighbor,
                                               ShowIpOspfDatabaseRouterSelfOriginate,
                                               ShowIpOspfInterfaceBrief,
                                               ShowIpOspfSegmentRouting,
                                               ShowIpOspfSegmentRoutingAdjacencySid,
                                               ShowIpOspfSegmentRoutingLocalBlock,
                                               ShowIpOspfSegmentRoutingGlobalBlock,
                                               ShowIpOspfFastRerouteTiLfa,
                                               ShowIpOspfDatabaseOpaqueAreaSelfOriginate,
                                               ShowIpOspfSegmentRoutingProtectedAdjacencies,
                                               ShowIpOspfSegmentRoutingSidDatabase,
                                               ShowIpOspfDatabaseOpaqueAreaAdvRouter)


# =====================================================================
# Unit test for 'show ip ospf {process_id} segment-routing local-block'
# =====================================================================
class test_show_ip_ospf_segment_routing_local_block(unittest.TestCase):

    '''Unit test for "show ip ospf" '''

    device = Device(name='aDevice')

    empty_output = {'execute.return_value': ''}

    golden_output1 = {'execute.return_value': '''
        PE1#show ip ospf 65109 segment-routing local-block
 
            OSPF Router with ID (10.4.1.1) (Process ID 65109)
 
        OSPF Segment Routing Local Blocks in Area 8
         
          Router ID        SR Capable   SRLB Base   SRLB Range 
        --------------------------------------------------------
         *10.4.1.1          Yes          15000       1000       
          10.16.2.2          Yes          15000       1000       
         
        PE1#
    '''}

    golden_parsed_output1 = {
        'instance':
            {'65109':
                {'router_id': '10.4.1.1',
                'areas':
                    {'0.0.0.8':
                        {'router_id':
                            {'10.4.1.1':
                                {'sr_capable': 'Yes',
                                'srlb_base': 15000,
                                'srlb_range': 1000},
                            '10.16.2.2':
                                {'sr_capable': 'Yes',
                                'srlb_base': 15000,
                                'srlb_range': 1000}}}},
                            }}}

    golden_parsed_output2 = {
        "instance": {
            "88": {
                "router_id": "10.4.113.144",
                "areas": {
                    "0.0.0.8": {
                        "router_id": {
                            "10.16.2.2": {
                                "sr_capable": "No"
                            },
                            "10.36.3.3": {
                                "sr_capable": "No"
                            },
                            "10.64.4.4": {
                                "sr_capable": "No"
                            },
                            "10.4.113.142": {
                                "sr_capable": "No"
                            },
                            "10.4.113.144": {
                                "sr_capable": "No"
                            },
                            "10.4.113.99": {
                                "sr_capable": "No"
                            }
                        }
                    }
                }
            }
        }
    }
    golden_output2 = {'execute.return_value': '''
        show ip ospf segment-routing local-block
      
                OSPF Router with ID (10.4.113.144) (Process ID 88)

                OSPF Segment Routing Local Blocks in Area 8

        Router ID        SR Capable   SRLB Base   SRLB Range
        --------------------------------------------------------
        10.16.2.2          No
        10.36.3.3          No
        10.64.4.4          No
        10.4.113.142  No
       *10.4.113.144  No
        10.4.113.99   No
    '''}

    def test_show_ip_ospf_segment_routing_local_block_empty(self):
        self.maxDiff = None
        self.device = Mock(**self.empty_output)
        obj = ShowIpOspfSegmentRoutingLocalBlock(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse(process_id=65109)

    def test_show_ip_ospf_segment_routing_local_block_full1(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output1)
        obj = ShowIpOspfSegmentRoutingLocalBlock(device=self.device)
        parsed_output = obj.parse(process_id=65109)
        self.assertEqual(parsed_output, self.golden_parsed_output1)

    def test_golden2(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output2)
        obj = ShowIpOspfSegmentRoutingLocalBlock(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output2)


# ============================
# Unit test for 'show ip ospf'
# ============================
class test_show_ip_ospf(unittest.TestCase):

    '''Unit test for "show ip ospf" '''

    device = Device(name='aDevice')
    
    empty_output = {'execute.return_value': ''}

    golden_parsed_output1 = {
        'vrf': 
            {'default': 
                {'address_family': 
                    {'ipv4': 
                        {'instance': 
                            {'1': 
                                {'adjacency_stagger': 
                                    {'initial_number': 300,
                                    'maximum_number': 300},
                                'area_transit': True,
                                'enable': True,
                                'areas': 
                                    {'0.0.0.0': 
                                        {'area_id': '0.0.0.0',
                                        'area_type': 'normal',
                                        'ranges': 
                                            {'10.4.0.0/16': 
                                                {'advertise': True,
                                                'cost': 10,
                                                'prefix': '10.4.0.0/16'}},
                                        'rrr_enabled': True,
                                        'statistics': 
                                            {'area_scope_lsa_cksum_sum': '0x07CF20',
                                            'area_scope_lsa_count': 19,
                                            'area_scope_opaque_lsa_cksum_sum': '0x000000',
                                            'area_scope_opaque_lsa_count': 0,
                                            'dcbitless_lsa_count': 5,
                                            'donotage_lsa_count': 0,
                                            'flood_list_length': 0,
                                            'indication_lsa_count': 0,
                                            'interfaces_count': 3,
                                            'loopback_count': 1,
                                            'spf_last_executed': '00:19:54.849',
                                            'spf_runs_count': 41}}},
                                'auto_cost': 
                                    {'bandwidth_unit': 'mbps',
                                    'enable': False,
                                    'reference_bandwidth': 100},
                                'bfd': 
                                    {'enable': True,
                                    'strict_mode': True},
                                'database_control': 
                                    {'max_lsa': 123},
                                'db_exchange_summary_list_optimization': True,
                                'elapsed_time': '1d01h',
                                'event_log': 
                                    {'enable': True,
                                    'max_events': 1000,
                                    'mode': 'cyclic'},
                                'external_flood_list_length': 0,
                                'graceful_restart': 
                                    {'cisco': 
                                        {'enable': False,
                                        'helper_enable': True,
                                        'type': 'cisco'},
                                    'ietf': 
                                        {'enable': False,
                                        'helper_enable': True,
                                        'type': 'ietf'}},
                                'lls': True,
                                'lsa_group_pacing_timer': 240,
                                'nsr': 
                                    {'enable': False},
                                'nssa': True,
                                'numbers': 
                                    {'dc_bitless': 0,
                                    'do_not_age': 0,
                                    'external_lsa': 1,
                                    'external_lsa_checksum': '0x007F60',
                                    'opaque_as_lsa': 0,
                                    'opaque_as_lsa_checksum': '0x000000'},
                                'opqaue_lsa': True,
                                'interface_flood_pacing_timer': 33,
                                'retransmission_pacing_timer': 66,
                                'router_id': '10.4.1.1',
                                'spf_control': 
                                    {'incremental_spf': False,
                                    'throttle': 
                                        {'lsa': 
                                            {'arrival': 100,
                                            'hold': 200,
                                            'maximum': 5000,
                                            'start': 50},
                                        'spf': 
                                            {'hold': 200,
                                            'maximum': 5000,
                                            'start': 50}}},
                                'start_time': '00:23:49.050',
                                'stub_router': 
                                    {'always': 
                                        {'always': False,
                                        'external_lsa': False,
                                        'include_stub': False,
                                        'summary_lsa': False}},
                                'total_areas': 1,
                                'total_areas_transit_capable': 0,
                                'total_normal_areas': 1,
                                'total_nssa_areas': 0,
                                'total_stub_areas': 0},
                            '2': 
                                {'adjacency_stagger': 
                                    {'initial_number': 300,
                                     'maximum_number': 300},
                                'area_transit': True,
                                'enable': False,
                                'areas': 
                                    {'0.0.0.1': 
                                        {'area_id': '0.0.0.1',
                                        'area_type': 'normal',
                                        'ranges': 
                                            {'10.4.1.0/24': 
                                                {'advertise': True,
                                                'prefix': '10.4.1.0/24'}},
                                        'statistics': 
                                            {'area_scope_lsa_cksum_sum': '0x053FED',
                                            'area_scope_lsa_count': 11,
                                            'area_scope_opaque_lsa_cksum_sum': '0x000000',
                                            'area_scope_opaque_lsa_count': 0,
                                            'dcbitless_lsa_count': 1,
                                            'donotage_lsa_count': 0,
                                            'flood_list_length': 0,
                                            'indication_lsa_count': 0,
                                            'interfaces_count': 2,
                                            'spf_last_executed': '03:26:37.769',
                                            'spf_runs_count': 97}}},
                                'auto_cost': 
                                    {'bandwidth_unit': 'mbps',
                                    'enable': False,
                                    'reference_bandwidth': 100},
                                'bfd': 
                                    {'enable': True},
                                'db_exchange_summary_list_optimization': True,
                                'domain_id_type': '0x0005',
                                'domain_id_value': '0.0.0.2',
                                'elapsed_time': '23:34:42.224',
                                'external_flood_list_length': 0,
                                'flags': 
                                    {'abr': True,
                                    'asbr': True},
                                'graceful_restart': 
                                    {'cisco': 
                                        {'enable': False,
                                        'helper_enable': True,
                                        'type': 'cisco'},
                                    'ietf': 
                                        {'enable': False,
                                        'helper_enable': True,
                                        'type': 'ietf'}},
                                'lls': True,
                                'lsa_group_pacing_timer': 240,
                                'nsr': 
                                    {'enable': True},
                                'nssa': True,
                                'numbers': 
                                    {'dc_bitless': 0,
                                    'do_not_age': 0,
                                    'external_lsa': 0,
                                    'external_lsa_checksum': '0x000000',
                                    'opaque_as_lsa': 0,
                                    'opaque_as_lsa_checksum': '0x000000'},
                                'opqaue_lsa': True,
                                'redistribution': 
                                    {'bgp': 
                                        {'bgp_id': 100,
                                        'subnets': 'subnets'
                                        }},
                                'interface_flood_pacing_timer': 33,
                                'retransmission_pacing_timer': 66,
                                'router_id': '10.229.11.11',
                                'spf_control': 
                                    {'incremental_spf': False,
                                    'throttle': 
                                        {'lsa': 
                                            {'arrival': 100,
                                            'hold': 200,
                                            'maximum': 5000,
                                            'start': 50},
                                        'spf': 
                                            {'hold': 200,
                                            'maximum': 5000,
                                            'start': 50}}},
                                'start_time': '02:17:25.010',
                                'stub_router': 
                                    {'always': 
                                        {'always': False,
                                        'external_lsa': False,
                                        'include_stub': False,
                                        'summary_lsa': False}},
                                'total_areas': 1,
                                'total_areas_transit_capable': 0,
                                'total_normal_areas': 1,
                                'total_nssa_areas': 0,
                                'total_stub_areas': 0}}}}}}}

    golden_output1 = {'execute.return_value': '''
        R1_ospf_xe#show ip ospf 
         Routing Process "ospf 1" with ID 10.4.1.1
         Start time: 00:23:49.050, Time elapsed: 1d01h
         Supports only single TOS(TOS0) routes
         Supports opaque LSA
         Supports Link-local Signaling (LLS)
         Supports area transit capability
         Supports NSSA (compatible with RFC 3101)
         Supports Database Exchange Summary List Optimization (RFC 5243)
         Event-log enabled, Maximum number of events: 1000, Mode: cyclic
         Router is not originating router-LSAs with maximum metric
         Initial SPF schedule delay 50 msecs
         Minimum hold time between two consecutive SPFs 200 msecs
         Maximum wait time between two consecutive SPFs 5000 msecs
         Incremental-SPF disabled
         Initial LSA throttle delay 50 msecs
         Minimum hold time for LSA throttle 200 msecs
         Maximum wait time for LSA throttle 5000 msecs
         Minimum LSA arrival 100 msecs
         LSA group pacing timer 240 secs
         Interface flood pacing timer 33 msecs
         Retransmission pacing timer 66 msecs
         Maximum number of non self-generated LSA allowed 123
         EXCHANGE/LOADING adjacency limit: initial 300, process maximum 300
         Number of external LSA 1. Checksum Sum 0x007F60
         Number of opaque AS LSA 0. Checksum Sum 0x000000
         Number of DCbitless external and opaque AS LSA 0
         Number of DoNotAge external and opaque AS LSA 0
         Number of areas in this router is 1. 1 normal 0 stub 0 nssa
         Number of areas transit capable is 0
         External flood list length 0
         IETF NSF helper support enabled
         Cisco NSF helper support enabled
         BFD is enabled in strict mode
         Reference bandwidth unit is 100 mbps
            Area BACKBONE(0.0.0.0)
                Number of interfaces in this area is 3 (1 loopback)
                Area has RRR enabled
                Area has no authentication
                SPF algorithm last executed 00:19:54.849 ago
                SPF algorithm executed 41 times
                Area ranges are
                 10.4.0.0/16 Active(10 - configured) Advertise
                Number of LSA 19. Checksum Sum 0x07CF20
                Number of opaque link LSA 0. Checksum Sum 0x000000
                Number of DCbitless LSA 5
                Number of indication LSA 0
                Number of DoNotAge LSA 0
                Flood list length 0

         Routing Process "ospf 2" with ID 10.229.11.11
           Domain ID type 0x0005, value 0.0.0.2
         Start time: 02:17:25.010, Time elapsed: 23:34:42.224
         Routing Process is shutdown
         Supports only single TOS(TOS0) routes
         Supports opaque LSA
         Supports Link-local Signaling (LLS)
         Supports area transit capability
         Supports NSSA (compatible with RFC 3101)
         Supports Database Exchange Summary List Optimization (RFC 5243)
         Connected to MPLS VPN Superbackbone, VRF VRF1
         Event-log disabled
         It is an area border and autonomous system boundary router
         Redistributing External Routes from,
            bgp 100, includes subnets in redistribution
         Router is not originating router-LSAs with maximum metric
         Initial SPF schedule delay 50 msecs
         Minimum hold time between two consecutive SPFs 200 msecs
         Maximum wait time between two consecutive SPFs 5000 msecs
         Incremental-SPF disabled
         Initial LSA throttle delay 50 msecs
         Minimum hold time for LSA throttle 200 msecs
         Maximum wait time for LSA throttle 5000 msecs
         Minimum LSA arrival 100 msecs
         LSA group pacing timer 240 secs
         Interface flood pacing timer 33 msecs
         Retransmission pacing timer 66 msecs
         EXCHANGE/LOADING adjacency limit: initial 300, process maximum 300
         Number of external LSA 0. Checksum Sum 0x000000
         Number of opaque AS LSA 0. Checksum Sum 0x000000
         Number of DCbitless external and opaque AS LSA 0
         Number of DoNotAge external and opaque AS LSA 0
         Number of areas in this router is 1. 1 normal 0 stub 0 nssa
         Number of areas transit capable is 0
         External flood list length 0
         Non-Stop Routing enabled
         IETF NSF helper support enabled
         Cisco NSF helper support enabled
         Reference bandwidth unit is 100 mbps
         BFD is enabled
            Area 1
                Number of interfaces in this area is 2
                Area has no authentication
                SPF algorithm last executed 03:26:37.769 ago
                SPF algorithm executed 97 times
                Area ranges are
                 10.4.1.0/24 Passive Advertise
                Number of LSA 11. Checksum Sum 0x053FED
                Number of opaque link LSA 0. Checksum Sum 0x000000
                Number of DCbitless LSA 1
                Number of indication LSA 0
                Number of DoNotAge LSA 0
                Flood list length 0
        '''}

    golden_parsed_output2 = {
        'vrf': {
            'default': {
                'address_family': {
                    'ipv4': {
                        'instance': {
                            '65109': {
                                'adjacency_stagger': {
                                    'initial_number': 300,
                                    'maximum_number': 300
                                },
                                'area_transit': True,
                                'areas': {
                                    '0.0.0.8': {
                                        'area_id': '0.0.0.8',
                                        'area_type': 'normal',
                                        'ranges': {},
                                        'statistics': {
                                            'area_scope_lsa_cksum_sum': '0x07FAE2',
                                            'area_scope_lsa_count': 21,
                                            'area_scope_opaque_lsa_cksum_sum': '0x000000',
                                            'area_scope_opaque_lsa_count': 0,
                                            'dcbitless_lsa_count': 0,
                                            'donotage_lsa_count': 0,
                                            'flood_list_length': 0,
                                            'indication_lsa_count': 0,
                                            'interfaces_count': 2,
                                            'loopback_count': 1,
                                            'spf_last_executed': '13:02:02.080',
                                            'spf_runs_count': 8
                                        }
                                    }
                                },
                                'auto_cost': {
                                    'bandwidth_unit': 'mbps',
                                    'enable': True,
                                    'reference_bandwidth': 2488
                                },
                                'bfd': {
                                    'enable': False
                                },
                                'db_exchange_summary_list_optimization': True,
                                'elapsed_time': '13:07:02.634',
                                'enable': True,
                                'event_log': {
                                    'enable': True,
                                    'max_events': 1000,
                                    'mode': 'cyclic'
                                },
                                'external_flood_list_length': 0,
                                'graceful_restart': {
                                    'cisco': {
                                        'enable': False,
                                        'helper_enable': True,
                                        'type': 'cisco'
                                    },
                                    'ietf': {
                                        'enable': False,
                                        'helper_enable': True,
                                        'type': 'ietf'
                                    }
                                },
                                'interface_flood_pacing_timer': 33,
                                'lls': True,
                                'lsa_group_pacing_timer': 240,
                                'nsr': {
                                    'enable': False
                                },
                                'nssa': True,
                                'numbers': {
                                    'dc_bitless': 0,
                                    'do_not_age': 0,
                                    'external_lsa': 2,
                                    'external_lsa_checksum': '0x00F934',
                                    'opaque_as_lsa': 0,
                                    'opaque_as_lsa_checksum': '0x000000'
                                },
                                'opqaue_lsa': True,
                                'retransmission_pacing_timer': 66,
                                'router_id': '10.169.197.254',
                                'spf_control': {
                                    'incremental_spf': False,
                                    'throttle': {
                                        'lsa': {
                                            'arrival': 100,
                                            'hold': 200,
                                            'maximum': 5000,
                                            'start': 50},
                                        'spf': {
                                            'hold': 3000,
                                            'maximum': 3000,
                                            'start': 500
                                        }
                                    }
                                },
                                'start_time': '00:02:39.151',
                                'stub_router': {
                                    'on_startup': {
                                        'include_stub': True,
                                        'on_startup': 300,
                                        'state': 'inactive'
                                    }
                                },
                                'total_areas': 1,
                                'total_areas_transit_capable': 0,
                                'total_normal_areas': 1,
                                'total_nssa_areas': 0,
                                'total_stub_areas': 0,
                            }
                        }
                    }
                }
            }
        }
    }

    golden_output2 = {'execute.return_value': '''
        R1_ospf_xe#show ip ospf 
        Load for five secs: 1%/0%; one minute: 1%; five minutes: 1%
        Time source is NTP, 23:17:46.919 EST Fri May 3 2019

         Routing Process "ospf 65109" with ID 10.169.197.254
         Start time: 00:02:39.151, Time elapsed: 13:07:02.634
         Supports only single TOS(TOS0) routes
         Supports opaque LSA
         Supports Link-local Signaling (LLS)
         Supports area transit capability
         Supports NSSA (compatible with RFC 3101)
         Supports Database Exchange Summary List Optimization (RFC 5243)
         Event-log enabled, Maximum number of events: 1000, Mode: cyclic
         Originating router-LSAs with maximum metric
            Condition: on startup for 300 seconds, State: inactive
            Advertise stub links with maximum metric in router-LSAs
            Unset reason: timer expired, Originated for 300 seconds
            Unset time: 00:07:39.152, Time elapsed: 13:02:02.633
         Initial SPF schedule delay 500 msecs
         Minimum hold time between two consecutive SPFs 3000 msecs
         Maximum wait time between two consecutive SPFs 3000 msecs
         Incremental-SPF disabled
         Initial LSA throttle delay 50 msecs
         Minimum hold time for LSA throttle 200 msecs
         Maximum wait time for LSA throttle 5000 msecs
         Minimum LSA arrival 100 msecs
         LSA group pacing timer 240 secs
         Interface flood pacing timer 33 msecs
         Retransmission pacing timer 66 msecs
         EXCHANGE/LOADING adjacency limit: initial 300, process maximum 300
         Number of external LSA 2. Checksum Sum 0x00F934
         Number of opaque AS LSA 0. Checksum Sum 0x000000
         Number of DCbitless external and opaque AS LSA 0
         Number of DoNotAge external and opaque AS LSA 0
         Number of areas in this router is 1. 1 normal 0 stub 0 nssa
         Number of areas transit capable is 0
         External flood list length 0
         IETF NSF helper support enabled
         Cisco NSF helper support enabled
         Reference bandwidth unit is 2488 mbps
            Area 8
                Number of interfaces in this area is 2 (1 loopback)
            Area has no authentication
            SPF algorithm last executed 13:02:02.080 ago
            SPF algorithm executed 8 times
            Area ranges are
            Number of LSA 21. Checksum Sum 0x07FAE2
            Number of opaque link LSA 0. Checksum Sum 0x000000
            Number of DCbitless LSA 0
            Number of indication LSA 0
            Number of DoNotAge LSA 0
            Flood list length 0
        '''}

    def test_show_ip_ospf_full1(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output1)
        obj = ShowIpOspf(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output1)

    def test_show_ip_ospf_full2(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output2)
        obj = ShowIpOspf(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output2)

    def test_show_ip_ospf_empty(self):
        self.maxDiff = None
        self.device = Mock(**self.empty_output)
        obj = ShowIpOspf(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

class test_show_ip_ospf_interface_brief(unittest.TestCase):
    '''Unit test for "show ip ospf interface brief" '''

    device = Device(name='aDevice')
    
    empty_output = {'execute.return_value': ''}
    golden_parsed_output_brief = {
    'instance': {
        '65109': {
            'areas': {
                '0.0.0.8': {
                    'interfaces': {
                        'Loopback0': {
                            'ip_address': '10.169.197.254/32',
                            'cost': 1,
                            'state': 'LOOP',
                            'nbrs_full': 0,
                            'nbrs_count': 0,
                            },
                        'GigabitEthernet4': {
                            'ip_address': '10.169.197.98/30',
                            'cost': 1000,
                            'state': 'P2P',
                            'nbrs_full': 1,
                            'nbrs_count': 1,
                            },
                        'GigabitEthernet2': {
                            'ip_address': '10.169.197.94/30',
                            'cost': 1000,
                            'state': 'BDR',
                            'nbrs_full': 1,
                            'nbrs_count': 1,
                            },
                        },
                    },
                },
            },
        },
    }

    golden_output_brief = {'execute.return_value': '''
        show ip ospf interface brief
        Load for five secs: 2%/0%; one minute: 2%; five minutes: 1%
        Time source is NTP, 01:20:44.789 EST Wed Jul 17 2019

        Interface    PID   Area            IP Address/Mask    Cost  State Nbrs F/C
        Lo0          65109  8               10.169.197.254/32 1     LOOP  0/0
        Gi4          65109  8               10.169.197.98/30  1000  P2P   1/1
        Gi2          65109  8               10.169.197.94/30  1000  BDR   1/1
    '''}

    def test_show_ip_ospf_interface_brief(self):
        self.device = Mock(**self.golden_output_brief)
        obj = ShowIpOspfInterfaceBrief(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_brief)

# ======================================
# Unit test for 'show ip ospf interface'
# ======================================
class test_show_ip_ospf_interface(unittest.TestCase):

    '''Unit test for "show ip ospf interface" '''

    device = Device(name='aDevice')
    
    empty_output = {'execute.return_value': ''}

    golden_parsed_output1 = {
        'vrf': 
            {'VRF1': 
                {'address_family': 
                    {'ipv4': 
                        {'instance': 
                            {'2': 
                                {'areas': 
                                    {'0.0.0.1': 
                                        {'interfaces': 
                                            {'GigabitEthernet3': 
                                                {'attached': 'interface enable',
                                                'bdr_ip_addr': '10.186.5.5',
                                                'bdr_router_id': '10.115.55.55',
                                                'bfd': 
                                                    {'enable': False},
                                                'cost': 1,
                                                'dead_interval': 40,
                                                'demand_circuit': False,
                                                'dr_ip_addr': '10.186.5.1',
                                                'dr_router_id': '10.229.11.11',
                                                'enable': True,
                                                'flood_queue_length': 0,
                                                'ipfrr_candidate': True,
                                                'ipfrr_protected': True,
                                                'graceful_restart': 
                                                    {'cisco': 
                                                        {'helper': True,
                                                        'type': 'cisco'},
                                                    'ietf': 
                                                        {'helper': True,
                                                        'type': 'ietf'}},
                                                'lls': True,
                                                'oob_resync_timeout': 40,
                                                'hello_interval': 10,
                                                'hello_timer': '00:00:08',
                                                'if_cfg': True,
                                                'index': '1/1/1',
                                                'interface_id': 9,
                                                'interface_type': 'broadcast',
                                                'ip_address': '10.186.5.1/24',
                                                'last_flood_scan_length': 0,
                                                'last_flood_scan_time_msec': 0,
                                                'line_protocol': True,
                                                'max_flood_scan_length': 7,
                                                'max_flood_scan_time_msec': 1,
                                                'name': 'GigabitEthernet3',
                                                'neighbors': 
                                                    {'10.115.55.55': 
                                                        {'bdr_router_id': '10.115.55.55'}},
                                                'next': '0x0(0)/0x0(0)/0x0(0)',
                                                'passive': False,
                                                'priority': 1,
                                                'retransmit_interval': 5,
                                                'router_id': '10.229.11.11',
                                                'state': 'dr',
                                                'statistics': 
                                                    {'adj_nbr_count': 1,
                                                    'nbr_count': 1,
                                                    'num_nbrs_suppress_hello': 0},
                                                'ti_lfa_protected': False,
                                                'topology': 
                                                    {0: 
                                                        {'cost': 1,
                                                        'disabled': False,
                                                        'name': 'Base',
                                                        'shutdown': False}},
                                                'transmit_delay': 1,
                                                'wait_interval': 40}},
                                        'sham_links': 
                                            {'10.229.11.11 10.151.22.22': 
                                                {'attached': 'not attached',
                                                'bfd': 
                                                    {'enable': False},
                                                'cost': 111,
                                                'dead_interval': 40,
                                                'demand_circuit': True,
                                                'enable': True,
                                                'flood_queue_length': 0,
                                                'graceful_restart': 
                                                    {'cisco': 
                                                        {'helper': True,
                                                        'type': 'cisco'},
                                                    'ietf': 
                                                        {'helper': True,
                                                        'type': 'ietf'}},
                                                'lls': True,
                                                'oob_resync_timeout': 40,
                                                'hello_interval': 10,
                                                'hello_timer': '00:00:00',
                                                'index': '1/2/2',
                                                'interface_id': 14,
                                                'interface_type': 'sham-link',
                                                'ip_address': '0.0.0.0/0',
                                                'last_flood_scan_length': 1,
                                                'last_flood_scan_time_msec': 0,
                                                'line_protocol': True,
                                                'max_flood_scan_length': 5,
                                                'max_flood_scan_time_msec': 1,
                                                'name': 'SL1',
                                                'next': '0x0(0)/0x0(0)/0x0(0)',
                                                'passive': False,
                                                'retransmit_interval': 5,
                                                'router_id': '10.229.11.11',
                                                'state': 'point-to-point',
                                                'statistics': 
                                                    {'adj_nbr_count': 1,
                                                    'nbr_count': 1,
                                                    'num_nbrs_suppress_hello': 0},
                                                'ti_lfa_protected': False,
                                                'ttl_security': 
                                                    {'enable': True,
                                                    'hops': 3},
                                                'topology': 
                                                    {0: 
                                                        {'cost': 111,
                                                        'disabled': False,
                                                        'name': 'Base',
                                                        'shutdown': False}},
                                                'transmit_delay': 1,
                                                'wait_interval': 40}}}}}}}}},
            'default': 
                {'address_family': 
                    {'ipv4': 
                        {'instance': 
                            {'1': 
                                {'areas': 
                                    {'0.0.0.0': 
                                        {'interfaces': 
                                            {'GigabitEthernet1': 
                                                {'attached': 'interface enable',
                                                'authentication': 
                                                    {'auth_trailer_key': 
                                                        {'crypto_algorithm': 'md5',
                                                        'youngest_key_id': 2}},
                                                'bdr_ip_addr': '10.1.4.1',
                                                'bdr_router_id': '10.4.1.1',
                                                'bfd': 
                                                    {'enable': False},
                                                'cost': 1,
                                                'dead_interval': 40,
                                                'demand_circuit': False,
                                                'dr_ip_addr': '10.1.4.4',
                                                'dr_router_id': '10.64.4.4',
                                                'enable': True,
                                                'flood_queue_length': 0,
                                                'ipfrr_candidate': True,
                                                'ipfrr_protected': True,
                                                'graceful_restart': 
                                                    {'cisco': 
                                                        {'helper': True,
                                                        'type': 'cisco'},
                                                    'ietf': 
                                                        {'helper': True,
                                                        'type': 'ietf'}},
                                                'lls': True,
                                                'oob_resync_timeout': 40,
                                                'hello_interval': 10,
                                                'hello_timer': '00:00:08',
                                                'if_cfg': True,
                                                'index': '1/2/2',
                                                'interface_id': 7,
                                                'interface_type': 'broadcast',
                                                'ip_address': '10.1.4.1/24',
                                                'last_flood_scan_length': 3,
                                                'last_flood_scan_time_msec': 0,
                                                'line_protocol': True,
                                                'max_flood_scan_length': 3,
                                                'max_flood_scan_time_msec': 1,
                                                'name': 'GigabitEthernet1',
                                                'neighbors': 
                                                    {'10.64.4.4': 
                                                        {'dr_router_id': '10.64.4.4'}},
                                                'next': '0x0(0)/0x0(0)/0x0(0)',
                                                'passive': False,
                                                'priority': 1,
                                                'retransmit_interval': 5,
                                                'router_id': '10.4.1.1',
                                                'state': 'bdr',
                                                'statistics': 
                                                    {'adj_nbr_count': 1,
                                                    'nbr_count': 1,
                                                    'num_nbrs_suppress_hello': 0},
                                                'ti_lfa_protected': False,
                                                'topology': 
                                                    {0: 
                                                        {'cost': 1,
                                                        'disabled': False,
                                                        'name': 'Base',
                                                        'shutdown': False}},
                                                'transmit_delay': 1,
                                                'wait_interval': 40},
                                            'GigabitEthernet2': 
                                                {'attached': 'interface enable',
                                                'authentication': 
                                                    {'auth_trailer_key': 
                                                        {'crypto_algorithm': 'simple'}},
                                                'bdr_ip_addr': '10.1.2.2',
                                                'bdr_router_id': '10.16.2.2',
                                                'bfd': 
                                                    {'enable': False},
                                                'cost': 1,
                                                'dead_interval': 40,
                                                'demand_circuit': False,
                                                'dr_ip_addr': '10.1.2.1',
                                                'dr_router_id': '10.4.1.1',
                                                'enable': True,
                                                'flood_queue_length': 0,
                                                'ipfrr_candidate': True,
                                                'ipfrr_protected': True,
                                                'graceful_restart': 
                                                    {'cisco': 
                                                        {'helper': True,
                                                        'type': 'cisco'},
                                                    'ietf': 
                                                        {'helper': True,
                                                        'type': 'ietf'}},
                                                'lls': True,
                                                'oob_resync_timeout': 40,
                                                'hello_interval': 10,
                                                'hello_timer': '00:00:05',
                                                'if_cfg': True,
                                                'index': '1/3/3',
                                                'interface_id': 8,
                                                'interface_type': 'broadcast',
                                                'ip_address': '10.1.2.1/24',
                                                'last_flood_scan_length': 1,
                                                'last_flood_scan_time_msec': 0,
                                                'line_protocol': True,
                                                'max_flood_scan_length': 3,
                                                'max_flood_scan_time_msec': 1,
                                                'name': 'GigabitEthernet2',
                                                'neighbors': 
                                                    {'10.16.2.2': 
                                                        {'bdr_router_id': '10.16.2.2'}},
                                                'next': '0x0(0)/0x0(0)/0x0(0)',
                                                'passive': False,
                                                'prefix_suppression': True,
                                                'priority': 1,
                                                'retransmit_interval': 5,
                                                'router_id': '10.4.1.1',
                                                'state': 'dr',
                                                'statistics': 
                                                    {'adj_nbr_count': 1,
                                                    'nbr_count': 1,
                                                    'num_nbrs_suppress_hello': 0},
                                                'ti_lfa_protected': False,
                                                'topology': 
                                                    {0: 
                                                        {'cost': 1,
                                                        'disabled': False,
                                                        'name': 'Base',
                                                        'shutdown': False}},
                                                'transmit_delay': 1,
                                                'wait_interval': 40},
                                            'Loopback0': 
                                                {'attached': 'interface enable',
                                                'bfd': 
                                                    {'enable': False},
                                                'cost': 1,
                                                'demand_circuit': False,
                                                'enable': True,
                                                'if_cfg': True,
                                                'interface_id': 11,
                                                'interface_type': 'loopback',
                                                'ip_address': '10.4.1.1/32',
                                                'line_protocol': True,
                                                'name': 'Loopback0',
                                                'router_id': '10.4.1.1',
                                                'stub_host': True,
                                                'topology': 
                                                    {0: 
                                                        {'cost': 1,
                                                        'disabled': False,
                                                        'name': 'Base',
                                                        'shutdown': False}}}}}}}}}}}}}

    golden_parsed_output2 = {
        'vrf': 
            {'VRF1': 
                {'address_family': 
                    {'ipv4': 
                        {'instance': 
                            {'2': 
                                {'areas': 
                                    {'0.0.0.1': 
                                        {'interfaces': 
                                            {'Loopback1': 
                                                {'attached': 'interface enable',
                                                'bfd': 
                                                    {'enable': False},
                                                'cost': 1,
                                                'demand_circuit': False,
                                                'enable': True,
                                                'if_cfg': True,
                                                'interface_type': 'loopback',
                                                'ip_address': '10.94.44.44/32',
                                                'line_protocol': True,
                                                'name': 'Loopback1',
                                                'router_id': '10.64.4.4',
                                                'stub_host': True,
                                                'topology': 
                                                    {0: 
                                                        {'cost': 1,
                                                        'disabled': False,
                                                        'name': 'Base',
                                                        'shutdown': False}}}},
                                        'virtual_links': 
                                            {'0.0.0.1 10.64.4.4': 
                                                {'attached': 'not attached',
                                                'bfd': 
                                                    {'enable': False},
                                                'cost': 1,
                                                'dead_interval': 44,
                                                'demand_circuit': True,
                                                'enable': True,
                                                'flood_queue_length': 0,
                                                'graceful_restart': 
                                                    {'cisco': 
                                                        {'helper': True,
                                                        'type': 'cisco'},
                                                    'ietf': 
                                                        {'helper': True,
                                                        'type': 'ietf'}},
                                                'hello_interval': 4,
                                                'hello_timer': '00:00:02',
                                                'index': '2/6',
                                                'interface_type': 'virtual-link',
                                                'ip_address': '10.19.4.4/24',
                                                'last_flood_scan_length': 2,
                                                'last_flood_scan_time_msec': 0,
                                                'line_protocol': True,
                                                'lls': True,
                                                'max_flood_scan_length': 8,
                                                'max_flood_scan_time_msec': 0,
                                                'name': 'VL1',
                                                'next': '0x0(0)/0x0(0)',
                                                'oob_resync_timeout': 44,
                                                'passive': False,
                                                'retransmit_interval': 5,
                                                'router_id': '10.64.4.4',
                                                'state': 'point-to-point',
                                                'statistics': 
                                                    {'adj_nbr_count': 1,
                                                    'nbr_count': 1,
                                                    'num_nbrs_suppress_hello': 0},
                                                'topology': 
                                                    {0: 
                                                        {'cost': 1,
                                                        'disabled': False,
                                                        'name': 'Base',
                                                        'shutdown': False}},
                                                'transmit_delay': 1,
                                                'wait_interval': 40}}}}}}}}},
            'default': 
                {'address_family': 
                    {'ipv4': 
                        {'instance': 
                            {'1': 
                                {'areas': 
                                    {'0.0.0.1': 
                                        {'interfaces': 
                                            {'GigabitEthernet0/0': 
                                                {'attached': 'interface enable',
                                                'bdr_ip_addr': '10.229.4.2',
                                                'bdr_router_id': '10.16.2.2',
                                                'bfd': 
                                                    {'enable': False},
                                                'cost': 1,
                                                'dead_interval': 40,
                                                'demand_circuit': False,
                                                'dr_ip_addr': '10.229.4.4',
                                                'dr_router_id': '10.64.4.4',
                                                'enable': True,
                                                'flood_queue_length': 0,
                                                'graceful_restart': 
                                                    {'cisco': 
                                                        {'helper': True,
                                                        'type': 'cisco'},
                                                    'ietf': 
                                                        {'helper': True,
                                                        'type': 'ietf'}},
                                                'hello_interval': 10,
                                                'hello_timer': '00:00:02',
                                                'if_cfg': True,
                                                'index': '2/3',
                                                'interface_type': 'broadcast',
                                                'ip_address': '10.229.4.4/24',
                                                'last_flood_scan_length': 1,
                                                'last_flood_scan_time_msec': 0,
                                                'line_protocol': True,
                                                'lls': True,
                                                'max_flood_scan_length': 10,
                                                'max_flood_scan_time_msec': 10,
                                                'name': 'GigabitEthernet0/0',
                                                'neighbors': 
                                                    {'10.16.2.2': 
                                                        {'bdr_router_id': '10.16.2.2'}},
                                                'next': '0x0(0)/0x0(0)',
                                                'oob_resync_timeout': 40,
                                                'passive': False,
                                                'priority': 1,
                                                'retransmit_interval': 5,
                                                'router_id': '10.64.4.4',
                                                'state': 'dr',
                                                'statistics': 
                                                    {'adj_nbr_count': 1,
                                                    'nbr_count': 1,
                                                    'num_nbrs_suppress_hello': 0},
                                                'topology': 
                                                    {0: 
                                                        {'cost': 1,
                                                        'disabled': False,
                                                        'name': 'Base',
                                                        'shutdown': False}},
                                                'transmit_delay': 1,
                                                'wait_interval': 40},
                                            'GigabitEthernet0/1': 
                                                {'attached': 'interface enable',
                                                'bdr_ip_addr': '10.19.4.3',
                                                'bdr_router_id': '10.36.3.3',
                                                'bfd': 
                                                    {'enable': False},
                                                'cost': 1,
                                                'dead_interval': 40,
                                                'demand_circuit': False,
                                                'dr_ip_addr': '10.19.4.4',
                                                'dr_router_id': '10.64.4.4',
                                                'enable': True,
                                                'flood_queue_length': 0,
                                                'graceful_restart': 
                                                    {'cisco': 
                                                        {'helper': True,
                                                        'type': 'cisco'},
                                                    'ietf': 
                                                        {'helper': True,
                                                        'type': 'ietf'}},
                                                'hello_interval': 10,
                                                'hello_timer': '00:00:02',
                                                'if_cfg': True,
                                                'index': '3/4',
                                                'interface_type': 'broadcast',
                                                'ip_address': '10.19.4.4/24',
                                                'last_flood_scan_length': 0,
                                                'last_flood_scan_time_msec': 0,
                                                'line_protocol': True,
                                                'lls': True,
                                                'max_flood_scan_length': 11,
                                                'max_flood_scan_time_msec': 1,
                                                'name': 'GigabitEthernet0/1',
                                                'neighbors': 
                                                    {'10.36.3.3': 
                                                        {'bdr_router_id': '10.36.3.3'}},
                                                'next': '0x0(0)/0x0(0)',
                                                'oob_resync_timeout': 40,
                                                'passive': False,
                                                'priority': 1,
                                                'retransmit_interval': 5,
                                                'router_id': '10.64.4.4',
                                                'state': 'dr',
                                                'statistics': 
                                                    {'adj_nbr_count': 1,
                                                    'nbr_count': 1,
                                                    'num_nbrs_suppress_hello': 0},
                                                'topology': 
                                                    {0: 
                                                        {'cost': 1,
                                                        'disabled': False,
                                                        'name': 'Base',
                                                        'shutdown': False}},
                                                'transmit_delay': 1,
                                                'wait_interval': 40},
                                            'Loopback0': 
                                                {'attached': 'interface enable',
                                                'bfd': 
                                                    {'enable': False},
                                                    'cost': 1,
                                                    'demand_circuit': False,
                                                    'enable': True,
                                                    'if_cfg': True,
                                                    'interface_type': 'loopback',
                                                    'ip_address': '10.64.4.4/32',
                                                    'line_protocol': True,
                                                    'name': 'Loopback0',
                                                    'router_id': '10.64.4.4',
                                                    'stub_host': True,
                                                    'topology': 
                                                        {0: 
                                                            {'cost': 1,
                                                            'disabled': False,
                                                            'name': 'Base',
                                                            'shutdown': False}}}}}}}}}}}}}

    golden_parsed_output3 = {
        'vrf': {
            'default': {
                'address_family': {
                    'ipv4': {
                        'instance': {
                            '65109': {
                                'areas': {
                                    '0.0.0.8': {
                                        'interfaces': {
                                            'GigabitEthernet2': {
                                                'attached': 'network statement',
                                                'bdr_ip_addr': '10.169.197.94',
                                                'bdr_router_id': '10.169.197.254',
                                                'bfd': {'enable': False},
                                                'cost': 1000,
                                                'dead_interval': 40,
                                                'demand_circuit': False,
                                                'dr_ip_addr': '10.169.197.93',
                                                'dr_router_id': '10.169.197.252',
                                                'enable': True,
                                                'flood_queue_length': 0,
                                                'graceful_restart': {
                                                    'cisco': {
                                                        'helper': True,
                                                        'type': 'cisco'},
                                                    'ietf': {
                                                        'helper': True,
                                                        'type': 'ietf'}},
                                                'hello_interval': 10,
                                                'hello_timer': '00:00:06',
                                                'index': '1/1/1',
                                                'interface_id': 8,
                                                'interface_type': 'broadcast',
                                                'ip_address': '10.169.197.94/30',
                                                'ipfrr_candidate': True,
                                                'ipfrr_protected': True,
                                                'last_flood_scan_length': 3,
                                                'last_flood_scan_time_msec': 0,
                                                'line_protocol': True,
                                                'lls': True,
                                                'max_flood_scan_length': 10,
                                                'max_flood_scan_time_msec': 1,
                                                'name': 'GigabitEthernet2',
                                                'neighbors': {'10.169.197.252': {'dr_router_id': '10.169.197.252'}},
                                                'next': '0x0(0)/0x0(0)/0x0(0)',
                                                'oob_resync_timeout': 40,
                                                'passive': False,
                                                'priority': 1,
                                                'retransmit_interval': 5,
                                                'router_id': '10.169.197.254',
                                                'state': 'bdr',
                                                'statistics': {
                                                    'adj_nbr_count': 1,
                                                    'nbr_count': 1,
                                                    'num_nbrs_suppress_hello': 0},
                                                'ti_lfa_protected': False,
                                                 'topology': {
                                                    0: {
                                                        'cost': 1000,
                                                        'disabled': False,
                                                        'name': 'Base',
                                                        'shutdown': False}},
                                                'transmit_delay': 1,
                                                'wait_interval': 40}}}}}}}}}}}

    golden_parsed_output4 = {
        'vrf': {
            'default': {
                'address_family': {
                    'ipv4': {
                        'instance': {
                            '8888': {
                                'areas': {
                                    '0.0.0.8': {
                                        'interfaces': {
                                            'GigabitEthernet2': {
                                                'router_id': '10.4.1.1',
                                                'interface_type': 'point-to-point',
                                                'cost': 1,
                                                'demand_circuit': False,
                                                'bfd': {
                                                    'enable': False,
                                                },
                                                'name': 'GigabitEthernet2',
                                                'ip_address': '10.0.0.6/30',
                                                'interface_id': 8,
                                                'attached': 'network statement',
                                                'enable': True,
                                                'line_protocol': True,
                                                'topology': {
                                                    0: {
                                                        'cost': 1,
                                                        'name': 'Base',
                                                        'disabled': False,
                                                        'shutdown': False,
                                                    },
                                                },
                                                'transmit_delay': 1,
                                                'state': 'point-to-point',
                                                'hello_interval': 10,
                                                'dead_interval': 40,
                                                'wait_interval': 40,
                                                'retransmit_interval': 5,
                                                'oob_resync_timeout': 40,
                                                'passive': False,
                                                'hello_timer': '00:00:00',
                                                'lls': True,
                                                'graceful_restart': {
                                                    'cisco': {
                                                        'type': 'cisco',
                                                        'helper': True,
                                                    },
                                                    'ietf': {
                                                        'type': 'ietf',
                                                        'helper': True,
                                                    },
                                                },
                                                'ipfrr_protected': True,
                                                'ipfrr_candidate': True,
                                                'ti_lfa_protected': False,
                                                'index': '1/1/1',
                                                'flood_queue_length': 0,
                                                'next': '0x0(0)/0x0(0)/0x0(0)',
                                                'last_flood_scan_length': 1,
                                                'max_flood_scan_length': 14,
                                                'last_flood_scan_time_msec': 1,
                                                'max_flood_scan_time_msec': 8,
                                                'statistics': {
                                                    'nbr_count': 1,
                                                    'adj_nbr_count': 1,
                                                    'num_nbrs_suppress_hello': 0,
                                                },
                                                'teapp': {
                                                    'topology_id': '0x0',
                                                    'SRTE': {
                                                        'affinity': {
                                                            'length': 32,
                                                            'bits': '0x00000010',
                                                        },
                                                        'extended_affinity': {
                                                            'length': 32,
                                                            'bits': '0x00000010',
                                                        },
                                                    },
                                                },
                                                'sr_policy_manager': {
                                                    'te_opaque_lsa': 'Source of link information OSPF',
                                                },
                                                'sr_mpls_enabled': True,
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

    def test_show_ip_ospf_interface_full1(self):
        
        self.maxDiff = None

        def mapper(key):
            return self.outputs[key]

        raw1 = '''\
            R1_ospf_xe#show ip ospf interface
            Loopback0 is up, line protocol is up 
              Internet Address 10.4.1.1/32, Interface ID 11, Area 0
              Attached via Interface Enable
              Process ID 1, Router ID 10.4.1.1, Network Type LOOPBACK, Cost: 1
              Topology-MTID    Cost    Disabled    Shutdown      Topology Name
                    0           1         no          no            Base
              Enabled by interface config, including secondary ip addresses
              Loopback interface is treated as a stub Host
            GigabitEthernet2 is up, line protocol is up (connected)
              Internet Address 10.1.2.1/24, Interface ID 8, Area 0
              Attached via Interface Enable
              Process ID 1, Router ID 10.4.1.1, Network Type BROADCAST, Cost: 1
              Topology-MTID    Cost    Disabled    Shutdown      Topology Name
                    0           1         no          no            Base
              Enabled by interface config, including secondary ip addresses
              Transmit Delay is 1 sec, State DR, Priority 1
              Designated Router (ID) 10.4.1.1, Interface address 10.1.2.1
              Backup Designated router (ID) 10.16.2.2, Interface address 10.1.2.2
              Timer intervals configured, Hello 10, Dead 40, Wait 40, Retransmit 5
                oob-resync timeout 40
                Hello due in 00:00:05
              Supports Link-local Signaling (LLS)
              Cisco NSF helper support enabled
              IETF NSF helper support enabled
              Prefix-suppression is enabled
              Can be protected by per-prefix Loop-Free FastReroute
              Can be used for per-prefix Loop-Free FastReroute repair paths
              Not Protected by per-prefix TI-LFA
              Index 1/3/3, flood queue length 0
              Next 0x0(0)/0x0(0)/0x0(0)
              Last flood scan length is 1, maximum is 3
              Last flood scan time is 0 msec, maximum is 1 msec
              Simple password authentication enabled
              Neighbor Count is 1, Adjacent neighbor count is 1 
                Adjacent with neighbor 10.16.2.2  (Backup Designated Router)
              Suppress hello for 0 neighbor(s)
            GigabitEthernet1 is up, line protocol is up 
              Internet Address 10.1.4.1/24, Interface ID 7, Area 0
              Attached via Interface Enable
              Process ID 1, Router ID 10.4.1.1, Network Type BROADCAST, Cost: 1
              Topology-MTID    Cost    Disabled    Shutdown      Topology Name
                    0           1         no          no            Base
              Enabled by interface config, including secondary ip addresses
              Transmit Delay is 1 sec, State BDR, Priority 1
              Designated Router (ID) 10.64.4.4, Interface address 10.1.4.4
              Backup Designated router (ID) 10.4.1.1, Interface address 10.1.4.1
              Timer intervals configured, Hello 10, Dead 40, Wait 40, Retransmit 5
                oob-resync timeout 40
                Hello due in 00:00:08
              Supports Link-local Signaling (LLS)
              Cisco NSF helper support enabled
              IETF NSF helper support enabled
              Can be protected by per-prefix Loop-Free FastReroute
              Can be used for per-prefix Loop-Free FastReroute repair paths
              Not Protected by per-prefix TI-LFA
              Index 1/2/2, flood queue length 0
              Next 0x0(0)/0x0(0)/0x0(0)
              Last flood scan length is 3, maximum is 3
              Last flood scan time is 0 msec, maximum is 1 msec
              Cryptographic authentication enabled
                Youngest key id is 2
                Rollover in progress, 1 neighbor(s) using the old key(s):
                key id 1 algorithm MD5
              Neighbor Count is 1, Adjacent neighbor count is 1 
                Adjacent with neighbor 10.64.4.4  (Designated Router)
              Suppress hello for 0 neighbor(s)
            OSPF_SL1 is up, line protocol is up 
              Internet Address 0.0.0.0/0, Interface ID 14, Area 1
              Attached via Not Attached
              Process ID 2, Router ID 10.229.11.11, Network Type SHAM_LINK, Cost: 111
              Topology-MTID    Cost    Disabled    Shutdown      Topology Name
                    0           111       no          no            Base
              Configured as demand circuit
              Run as demand circuit
              DoNotAge LSA not allowed (Number of DCbitless LSA is 1)
              Transmit Delay is 1 sec, State POINT_TO_POINT
              Timer intervals configured, Hello 10, Dead 40, Wait 40, Retransmit 5
                oob-resync timeout 40
                Hello due in 00:00:00
              Supports Link-local Signaling (LLS)
              Cisco NSF helper support enabled
              IETF NSF helper support enabled
              Strict TTL checking enabled, up to 3 hops allowed
              Can not be protected by per-prefix Loop-Free FastReroute
              Can not be used for per-prefix Loop-Free FastReroute repair paths
              Not Protected by per-prefix TI-LFA
              Index 1/2/2, flood queue length 0
              Next 0x0(0)/0x0(0)/0x0(0)
              Last flood scan length is 1, maximum is 5
              Last flood scan time is 0 msec, maximum is 1 msec
              Neighbor Count is 1, Adjacent neighbor count is 1 
                Adjacent with neighbor 10.151.22.22
              Suppress hello for 0 neighbor(s)
            GigabitEthernet3 is up, line protocol is up 
              Internet Address 10.186.5.1/24, Interface ID 9, Area 1
              Attached via Interface Enable
              Process ID 2, Router ID 10.229.11.11, Network Type BROADCAST, Cost: 1
              Topology-MTID    Cost    Disabled    Shutdown      Topology Name
                    0           1         no          no            Base
              Enabled by interface config, including secondary ip addresses
              Transmit Delay is 1 sec, State DR, Priority 1
              Designated Router (ID) 10.229.11.11, Interface address 10.186.5.1
              Backup Designated router (ID) 10.115.55.55, Interface address 10.186.5.5
              Timer intervals configured, Hello 10, Dead 40, Wait 40, Retransmit 5
                oob-resync timeout 40
                Hello due in 00:00:08
              Supports Link-local Signaling (LLS)
              Cisco NSF helper support enabled
              IETF NSF helper support enabled
              Can be protected by per-prefix Loop-Free FastReroute
              Can be used for per-prefix Loop-Free FastReroute repair paths
              Not Protected by per-prefix TI-LFA
              Index 1/1/1, flood queue length 0
              Next 0x0(0)/0x0(0)/0x0(0)
              Last flood scan length is 0, maximum is 7
              Last flood scan time is 0 msec, maximum is 1 msec
              Neighbor Count is 1, Adjacent neighbor count is 1 
                Adjacent with neighbor 10.115.55.55  (Backup Designated Router)
              Suppress hello for 0 neighbor(s)
            '''

        raw2 = '''\
            R1_ospf_xe#show ip ospf sham-links | i OSPF_SL1
              Sham Link OSPF_SL1 to address 10.151.22.22 is up
            '''

        raw3 = '''\
            R1_ospf_xe#show running-config | i sham-link | i 10.151.22.22
              area 1 sham-link 10.229.11.11 10.151.22.22 cost 111 ttl-security hops 3
            '''

        raw4 = '''\
            R1_ospf_xe#show running-config | section router ospf 1
              router ospf 1
                mpls traffic-eng router-id Loopback0
                mpls traffic-eng area 0
            '''

        raw5 = '''\
            R1_ospf_xe#show running-config | section router ospf 2
              router ospf 2 vrf VRF1
                area 1 virtual-link 10.100.5.5
                area 1 sham-link 10.229.11.11 10.151.22.22 cost 111 ttl-security hops 3
                redistribute bgp
            '''

        self.outputs = {}
        self.outputs['show ip ospf interface'] = raw1
        self.outputs['show ip ospf sham-links | i OSPF_SL1'] = raw2
        self.outputs['show running-config | i sham-link | i 10.151.22.22'] = raw3
        self.outputs['show running-config | section router ospf 1'] = raw4
        self.outputs['show running-config | section router ospf 2'] = raw5

        self.device.execute = Mock()
        self.device.execute.side_effect = mapper
        
        obj = ShowIpOspfInterface(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output1)

    def test_show_ip_ospf_interface_full2(self):
        
        self.maxDiff = None

        def mapper(key):
            return self.outputs[key]

        raw1 = '''\
            R4_ospf_iosv#show ip ospf interface (including virtual-link)
            OSPF_VL1 is up, line protocol is up 
              Internet Address 10.19.4.4/24, Area 1, Attached via Not Attached
              Process ID 2, Router ID 10.64.4.4, Network Type VIRTUAL_LINK, Cost: 1
              Topology-MTID    Cost    Disabled    Shutdown      Topology Name
                    0           1         no          no            Base
              Configured as demand circuit
              Run as demand circuit
              DoNotAge LSA not allowed (Number of DCbitless LSA is 7)
              Transmit Delay is 1 sec, State POINT_TO_POINT
              Timer intervals configured, Hello 4, Dead 44, Wait 40, Retransmit 5
                oob-resync timeout 44
                Hello due in 00:00:02
              Supports Link-local Signaling (LLS)
              Cisco NSF helper support enabled
              IETF NSF helper support enabled
              Index 2/6, flood queue length 0
              Next 0x0(0)/0x0(0)
              Last flood scan length is 2, maximum is 8
              Last flood scan time is 0 msec, maximum is 0 msec
              Neighbor Count is 1, Adjacent neighbor count is 1 
                Adjacent with neighbor 10.36.3.3
              Suppress hello for 0 neighbor(s)
            Loopback0 is up, line protocol is up 
              Internet Address 10.64.4.4/32, Area 1, Attached via Interface Enable
              Process ID 1, Router ID 10.64.4.4, Network Type LOOPBACK, Cost: 1
              Topology-MTID    Cost    Disabled    Shutdown      Topology Name
                    0           1         no          no            Base
              Enabled by interface config, including secondary ip addresses
              Loopback interface is treated as a stub Host
            GigabitEthernet0/1 is up, line protocol is up 
              Internet Address 10.19.4.4/24, Area 1, Attached via Interface Enable
              Process ID 1, Router ID 10.64.4.4, Network Type BROADCAST, Cost: 1
              Topology-MTID    Cost    Disabled    Shutdown      Topology Name
                    0           1         no          no            Base
              Enabled by interface config, including secondary ip addresses
              Transmit Delay is 1 sec, State DR, Priority 1
              Designated Router (ID) 10.64.4.4, Interface address 10.19.4.4
              Backup Designated router (ID) 10.36.3.3, Interface address 10.19.4.3
              Timer intervals configured, Hello 10, Dead 40, Wait 40, Retransmit 5
                oob-resync timeout 40
                Hello due in 00:00:02
              Supports Link-local Signaling (LLS)
              Cisco NSF helper support enabled
              IETF NSF helper support enabled
              Index 3/4, flood queue length 0
              Next 0x0(0)/0x0(0)
              Last flood scan length is 0, maximum is 11
              Last flood scan time is 0 msec, maximum is 1 msec
              Neighbor Count is 1, Adjacent neighbor count is 1 
                Adjacent with neighbor 10.36.3.3  (Backup Designated Router)
              Suppress hello for 0 neighbor(s)
            GigabitEthernet0/0 is up, line protocol is up 
              Internet Address 10.229.4.4/24, Area 1, Attached via Interface Enable
              Process ID 1, Router ID 10.64.4.4, Network Type BROADCAST, Cost: 1
              Topology-MTID    Cost    Disabled    Shutdown      Topology Name
                    0           1         no          no            Base
              Enabled by interface config, including secondary ip addresses
              Transmit Delay is 1 sec, State DR, Priority 1
              Designated Router (ID) 10.64.4.4, Interface address 10.229.4.4
              Backup Designated router (ID) 10.16.2.2, Interface address 10.229.4.2
              Timer intervals configured, Hello 10, Dead 40, Wait 40, Retransmit 5
                oob-resync timeout 40
                Hello due in 00:00:02
              Supports Link-local Signaling (LLS)
              Cisco NSF helper support enabled
              IETF NSF helper support enabled
              Index 2/3, flood queue length 0
              Next 0x0(0)/0x0(0)
              Last flood scan length is 1, maximum is 10
              Last flood scan time is 0 msec, maximum is 10 msec
              Neighbor Count is 1, Adjacent neighbor count is 1 
                Adjacent with neighbor 10.16.2.2  (Backup Designated Router)
              Suppress hello for 0 neighbor(s)
            Loopback1 is up, line protocol is up 
              Internet Address 10.94.44.44/32, Area 1, Attached via Interface Enable
              Process ID 2, Router ID 10.64.4.4, Network Type LOOPBACK, Cost: 1
              Topology-MTID    Cost    Disabled    Shutdown      Topology Name
                    0           1         no          no            Base
              Enabled by interface config, including secondary ip addresses
              Loopback interface is treated as a stub Host
            '''

        raw2 = '''\
            R1_ospf_xe#show ip ospf virtual-links | i OSPF_VL1
              Virtual Link OSPF_VL1 to router 10.100.5.5 is down
            '''

        raw3 = '''\
            R1_ospf_xe#show running-config | i virtual-link | i 10.100.5.5
              area 1 virtual-link 10.100.5.5
            '''

        raw4 = '''\
            R1_ospf_xe#show running-config | section router ospf 1
              router ospf 1
                mpls traffic-eng router-id Loopback0
                mpls traffic-eng area 0
            '''

        raw5 = '''\
            R1_ospf_xe#show running-config | section router ospf 2
              router ospf 2 vrf VRF1
                area 1 virtual-link 10.100.5.5
                area 1 sham-link 10.229.11.11 10.151.22.22 cost 111 ttl-security hops 3
                redistribute bgp
            '''

        self.outputs = {}
        self.outputs['show ip ospf interface'] = raw1
        self.outputs['show ip ospf virtual-links | i OSPF_VL1'] = raw2
        self.outputs['show running-config | i virtual-link | i 10.100.5.5'] = raw3
        self.outputs['show running-config | section router ospf 1'] = raw4
        self.outputs['show running-config | section router ospf 2'] = raw5

        self.device.execute = Mock()
        self.device.execute.side_effect = mapper
        
        obj = ShowIpOspfInterface(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output2)

    def test_show_ip_ospf_interface_full3(self):

        self.maxDiff = None

        raw1='''\
            show ip ospf interface GigabitEthernet2
            Load for five secs: 2%/0%; one minute: 2%; five minutes: 2%
            Time source is NTP, 04:44:14.272 EST Sat Jun 15 2019

            GigabitEthernet2 is up, line protocol is up 
              Internet Address 10.169.197.94/30, Interface ID 8, Area 8
              Attached via Network Statement
              Process ID 65109, Router ID 10.169.197.254, Network Type BROADCAST, Cost: 1000
              Topology-MTID    Cost    Disabled    Shutdown      Topology Name
                    0           1000      no          no            Base
              Transmit Delay is 1 sec, State BDR, Priority 1
              Designated Router (ID) 10.169.197.252, Interface address 10.169.197.93
              Backup Designated router (ID) 10.169.197.254, Interface address 10.169.197.94
              Timer intervals configured, Hello 10, Dead 40, Wait 40, Retransmit 5
                oob-resync timeout 40
                Hello due in 00:00:06
              Supports Link-local Signaling (LLS)
              Cisco NSF helper support enabled
              IETF NSF helper support enabled
              Can be protected by per-prefix Loop-Free FastReroute
              Can be used for per-prefix Loop-Free FastReroute repair paths
              Not Protected by per-prefix TI-LFA
              Index 1/1/1, flood queue length 0
              Next 0x0(0)/0x0(0)/0x0(0)
              Last flood scan length is 3, maximum is 10
              Last flood scan time is 0 msec, maximum is 1 msec
              Neighbor Count is 1, Adjacent neighbor count is 1 
                Adjacent with neighbor 10.169.197.252  (Designated Router)
              Suppress hello for 0 neighbor(s)
        '''

        raw2='''\
         show running-config | section router ospf 65109
         router ospf 65109
         router-id 10.169.197.254
         max-metric router-lsa on-startup 300
         auto-cost reference-bandwidth 2488
         timers throttle spf 500 3000 3000
         network 10.1.8.0 0.0.0.255 area 8
         network 10.169.197.4 0.0.0.3 area 8
         network 10.169.197.88 0.0.0.3 area 8
         network 10.169.197.92 0.0.0.3 area 8
         network 10.169.197.96 0.0.0.3 area 8
         network 10.169.197.254 0.0.0.0 area 8
         mpls ldp sync
         action 50 cli command "router ospf 65109"
        '''

        def mapper(key):
            return self.outputs[key]

        self.outputs = {}
        self.outputs['show ip ospf interface GigabitEthernet2'] = raw1
        self.outputs['show running-config | section router ospf 65109'] = raw2        

        self.device.execute = Mock()
        self.device.execute.side_effect = mapper
        
        obj = ShowIpOspfInterface(device=self.device)
        parsed_output = obj.parse(interface='GigabitEthernet2')
        self.assertEqual(parsed_output, self.golden_parsed_output3)


    def test_show_ip_ospf_interface_full4(self):

        self.maxDiff = None

        raw1='''\
            show ip ospf interface GigabitEthernet2
            GigabitEthernet2 is up, line protocol is up 
                Internet Address 10.0.0.6/30, Interface ID 8, Area 8
                Attached via Network Statement
                Process ID 8888, Router ID 10.4.1.1, Network Type POINT_TO_POINT, Cost: 1
                Topology-MTID    Cost    Disabled    Shutdown      Topology Name
                        0           1         no          no            Base
                Transmit Delay is 1 sec, State POINT_TO_POINT
                Timer intervals configured, Hello 10, Dead 40, Wait 40, Retransmit 5
                    oob-resync timeout 40
                    Hello due in 00:00:00
                Supports Link-local Signaling (LLS)
                Cisco NSF helper support enabled
                IETF NSF helper support enabled
                Can be protected by per-prefix Loop-Free FastReroute
                Can be used for per-prefix Loop-Free FastReroute repair paths
                Not Protected by per-prefix TI-LFA
                Segment Routing enabled for MPLS forwarding
                Index 1/1/1, flood queue length 0
                Next 0x0(0)/0x0(0)/0x0(0)
                Last flood scan length is 1, maximum is 14
                Last flood scan time is 1 msec, maximum is 8 msec
                Neighbor Count is 1, Adjacent neighbor count is 1 
                    Adjacent with neighbor 10.229.11.11
                Suppress hello for 0 neighbor(s)
                TEAPP:
                    Topology Id:0x0
                    TEAPP:SRTE
                        Affinity: length 32, bits 0x00000010
                        Extended affinity: length 32, bits 0x00000010 
                SR Policy Manager:
                    TE Opaque LSA: Source of link information OSPF
        '''

        raw2='''\
         PE1#show running-config | section router ospf 8888 
            router ospf 8888
            router-id 10.4.1.1
            segment-routing area 8 mpls
            segment-routing mpls
            network 0.0.0.0 255.255.255.255 area 8
        '''

        def mapper(key):
            return self.outputs[key]

        self.outputs = {}
        self.outputs['show ip ospf interface GigabitEthernet2'] = raw1
        self.outputs['show running-config | section router ospf 8888'] = raw2        

        self.device.execute = Mock()
        self.device.execute.side_effect = mapper
        
        obj = ShowIpOspfInterface(device=self.device)
        parsed_output = obj.parse(interface='GigabitEthernet2')
        self.assertEqual(parsed_output, self.golden_parsed_output4)

    def test_show_ip_ospf_interface_empty(self):
        self.maxDiff = None
        self.device = Mock(**self.empty_output)
        obj = ShowIpOspfInterface(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()


# ============================================
# Unit test for 'show ip ospf neighbor detail'
# ============================================
class test_show_ip_ospf_neighbor_detail(unittest.TestCase):

    '''Unit test for "show ip ospf neighbor detail" '''

    device = Device(name='aDevice')
    
    empty_output = {'execute.return_value': ''}

    golden_parsed_output1 = {
        'vrf': 
            {'VRF1': 
                {'address_family': 
                    {'ipv4': 
                        {'instance': 
                            {'2': 
                                {'areas': 
                                    {'0.0.0.1': 
                                        {'interfaces': 
                                            {'GigabitEthernet3': 
                                                {'neighbors': 
                                                    {'10.115.55.55': 
                                                        {'address': '10.186.5.5',
                                                        'bdr_ip_addr': '10.186.5.5',
                                                        'dead_timer': '00:00:34',
                                                        'dr_ip_addr': '10.186.5.1',
                                                        'first': '0x0(0)/0x0(0)/0x0(0)',
                                                        'index': '1/1/1,',
                                                        'interface': 'GigabitEthernet3',
                                                        'neighbor_router_id': '10.115.55.55',
                                                        'uptime': '15:47:14',
                                                        'next': '0x0(0)/0x0(0)/0x0(0)',
                                                        'priority': 1,
                                                        'state': 'full',
                                                        'statistics': 
                                                            {'last_retrans_max_scan_length': 6,
                                                            'last_retrans_max_scan_time_msec': 0,
                                                            'last_retrans_scan_length': 1,
                                                            'last_retrans_scan_time_msec': 0,
                                                            'nbr_event_count': 6,
                                                            'nbr_retrans_qlen': 0,
                                                            'total_retransmission': 6}}}}},
                                        'sham_links': 
                                            {'10.229.11.11 10.151.22.22': 
                                                {'neighbors': 
                                                    {'10.151.22.22': 
                                                        {'address': '10.151.22.22',
                                                        'bdr_ip_addr': '0.0.0.0',
                                                        'dead_timer': '00:00:35',
                                                        'dr_ip_addr': '0.0.0.0',
                                                        'first': '0x0(0)/0x0(0)/0x0(0)',
                                                        'hello_options': '0x2',
                                                        'dbd_options': '0x42',
                                                        'index': '1/2/2,',
                                                        'interface': 'OSPF_SL1',
                                                        'neighbor_router_id': '10.151.22.22',
                                                        'uptime': '07:41:59',
                                                        'next': '0x0(0)/0x0(0)/0x0(0)',
                                                        'priority': 0,
                                                        'state': 'full',
                                                        'statistics': 
                                                            {'last_retrans_max_scan_length': 1,
                                                            'last_retrans_max_scan_time_msec': 0,
                                                            'last_retrans_scan_length': 1,
                                                            'last_retrans_scan_time_msec': 0,
                                                            'nbr_event_count': 6,
                                                            'nbr_retrans_qlen': 0,
                                                            'total_retransmission': 2}}}}}}}}}}}},
            'default': 
                {'address_family': 
                    {'ipv4': 
                        {'instance': 
                            {'1': 
                                {'areas': 
                                    {'0.0.0.0': 
                                        {'interfaces': 
                                            {'GigabitEthernet1': 
                                                {'neighbors': 
                                                    {'10.64.4.4': 
                                                        {'address': '10.1.4.4',
                                                        'bdr_ip_addr': '10.1.4.1',
                                                        'dead_timer': '00:00:35',
                                                        'dr_ip_addr': '10.1.4.4',
                                                        'first': '0x0(0)/0x0(0)/0x0(0)',
                                                        'index': '1/1/1,',
                                                        'interface': 'GigabitEthernet1',
                                                        'neighbor_router_id': '10.64.4.4',
                                                        'uptime': '1d01h',
                                                        'next': '0x0(0)/0x0(0)/0x0(0)',
                                                        'priority': 1,
                                                        'state': 'full',
                                                        'statistics': 
                                                            {'last_retrans_max_scan_length': 1,
                                                            'last_retrans_max_scan_time_msec': 0,
                                                            'last_retrans_scan_length': 0,
                                                            'last_retrans_scan_time_msec': 0,
                                                            'nbr_event_count': 6,
                                                            'nbr_retrans_qlen': 0,
                                                            'total_retransmission': 1}}}},
                                            'GigabitEthernet2': 
                                                {'neighbors': 
                                                    {'10.16.2.2': 
                                                        {'address': '10.1.2.2',
                                                        'bdr_ip_addr': '10.1.2.2',
                                                        'dead_timer': '00:00:33',
                                                        'dr_ip_addr': '10.1.2.1',
                                                        'first': '0x0(0)/0x0(0)/0x0(0)',
                                                        'hello_options': '0x2',
                                                        'dbd_options': '0x42',
                                                        'index': '1/2/2,',
                                                        'interface': 'GigabitEthernet2',
                                                        'interface_id': 'unknown',
                                                        'neighbor_router_id': '10.16.2.2',
                                                        'uptime': '08:04:20',
                                                        'next': '0x0(0)/0x0(0)/0x0(0)',
                                                        'priority': 1,
                                                        'state': 'full',
                                                        'statistics': 
                                                            {'last_retrans_max_scan_length': 0,
                                                            'last_retrans_max_scan_time_msec': 0,
                                                            'last_retrans_scan_length': 0,
                                                            'last_retrans_scan_time_msec': 0,
                                                            'nbr_event_count': 6,
                                                            'nbr_retrans_qlen': 0,
                                                            'total_retransmission': 0}}}}}}}}}}}}}}

    golden_parsed_output2 = {
        'vrf': 
            {'default': 
                {'address_family': 
                    {'ipv4': 
                        {'instance': 
                            {'1': 
                                {'areas': 
                                    {'0.0.0.1': 
                                        {'interfaces': 
                                            {'GigabitEthernet0/0': 
                                                {'neighbors': 
                                                    {'10.16.2.2': 
                                                        {'address': '10.229.4.2',
                                                        'bdr_ip_addr': '10.229.4.2',
                                                        'dead_timer': '00:00:34',
                                                        'dr_ip_addr': '10.229.4.4',
                                                        'first': '0x0(0)/0x0(0)',
                                                        'index': '1/1,',
                                                        'interface': 'GigabitEthernet0/0',
                                                        'neighbor_router_id': '10.16.2.2',
                                                        'uptime': '05:07:40',
                                                        'next': '0x0(0)/0x0(0)',
                                                        'priority': 1,
                                                        'state': 'full',
                                                        'statistics': 
                                                            {'last_retrans_max_scan_length': 1,
                                                            'last_retrans_max_scan_time_msec': 0,
                                                            'last_retrans_scan_length': 1,
                                                            'last_retrans_scan_time_msec': 0,
                                                            'nbr_event_count': 6,
                                                            'nbr_retrans_qlen': 0,
                                                            'total_retransmission': 1}}}},
                                            'GigabitEthernet0/1': 
                                                {'neighbors': 
                                                    {'10.36.3.3': 
                                                        {'address': '10.19.4.3',
                                                        'bdr_ip_addr': '10.19.4.3',
                                                        'dead_timer': '00:00:33',
                                                        'dr_ip_addr': '10.19.4.4',
                                                        'first': '0x0(0)/0x0(0)',
                                                        'hello_options': '0x2',
                                                        'dbd_options': '0x42',
                                                        'index': '2/2,',
                                                        'interface': 'GigabitEthernet0/1',
                                                        'neighbor_router_id': '10.36.3.3',
                                                        'uptime': '16:31:06',
                                                        'next': '0x0(0)/0x0(0)',
                                                        'priority': 1,
                                                        'state': 'full',
                                                        'statistics': 
                                                            {'last_retrans_max_scan_length': 1,
                                                            'last_retrans_max_scan_time_msec': 0,
                                                            'last_retrans_scan_length': 1,
                                                            'last_retrans_scan_time_msec': 0,
                                                            'nbr_event_count': 6,
                                                            'nbr_retrans_qlen': 0,
                                                            'total_retransmission': 2}}}}},
                                        'virtual_links': 
                                            {'0.0.0.1 10.64.4.4,': 
                                                {'neighbors': 
                                                    {'10.36.3.3': 
                                                        {'address': '10.229.3.3',
                                                        'bdr_ip_addr': '0.0.0.0',
                                                        'dead_timer': '00:00:41',
                                                        'dr_ip_addr': '0.0.0.0',
                                                        'first': '0x0(0)/0x0(0)',
                                                        'hello_options': '0x2',
                                                        'dbd_options': '0x42',
                                                        'index': '1/3,',
                                                        'interface': 'OSPF_VL1',
                                                        'neighbor_router_id': '10.36.3.3',
                                                        'uptime': '05:07:21',
                                                        'next': '0x0(0)/0x0(0)',
                                                        'priority': 0,
                                                        'state': 'full',
                                                        'statistics': 
                                                            {'last_retrans_max_scan_length': 1,
                                                            'last_retrans_max_scan_time_msec': 0,
                                                            'last_retrans_scan_length': 1,
                                                            'last_retrans_scan_time_msec': 0,
                                                            'nbr_event_count': 12,
                                                            'nbr_retrans_qlen': 0,
                                                            'total_retransmission': 3}}}}}}}}}}}}}}

    golden_parsed_output3 = {
        'vrf': 
            {'default': 
                {'address_family': 
                    {'ipv4': 
                        {'instance': 
                            {'1668': 
                                {'areas': 
                                    {'0.0.0.0': 
                                        {'interfaces': 
                                            {'TenGigabitEthernet3/1/1': 
                                                {'neighbors': 
                                                    {'10.196.55.33': 
                                                        {'address': '10.196.55.33',
                                                        'bdr_ip_addr': '0.0.0.0',
                                                        'dead_timer': '00:00:03',
                                                        'dr_ip_addr': '10.196.55.38',
                                                        'first': '0x0(0)/0x625F62BC(13775196)',
                                                        'hello_options': '0x2',
                                                        'index': '2/2,',
                                                        'interface': 'TenGigabitEthernet3/1/1',
                                                        'neighbor_router_id': '10.196.55.33',
                                                        'next': '0x0(0)/0x625F62BC(13775196)',
                                                        'priority': 0,
                                                        'state': 'full',
                                                        'statistics': 
                                                            {'last_retrans_max_scan_length': 2,
                                                            'last_retrans_max_scan_time_msec': 4,
                                                            'last_retrans_scan_length': 0,
                                                            'last_retrans_scan_time_msec': 0,
                                                            'nbr_event_count': 12,
                                                            'nbr_retrans_qlen': 3,
                                                            'total_retransmission': 5},
                                                        'uptime': '3d21h'}}},
                                            'TenGigabitEthernet3/1/2': 
                                                {'neighbors': 
                                                    {'10.196.55.41': 
                                                        {'address': '10.196.55.41',
                                                        'bdr_ip_addr': '0.0.0.0',
                                                        'dead_timer': '00:00:03',
                                                        'dr_ip_addr': '10.196.55.46',
                                                        'first': '0x0(0)/0x0(0)',
                                                        'hello_options': '0x2',
                                                        'index': '1/1,',
                                                        'interface': 'TenGigabitEthernet3/1/2',
                                                        'neighbor_router_id': '10.196.55.41',
                                                        'next': '0x0(0)/0x0(0)',
                                                        'priority': 0,
                                                        'state': 'full',
                                                        'statistics': 
                                                            {'last_retrans_max_scan_length': 1,
                                                            'last_retrans_max_scan_time_msec': 0,
                                                            'last_retrans_scan_length': 0,
                                                            'last_retrans_scan_time_msec': 0,
                                                            'nbr_event_count': 22,
                                                            'nbr_retrans_qlen': 0,
                                                            'total_retransmission': 1},
                                                        'uptime': '3d00h'}}},
                                            'TenGigabitEthernet3/1/5': 
                                                {'neighbors': 
                                                    {'10.196.55.49': 
                                                        {'address': '10.196.55.49',
                                                        'bdr_ip_addr': '0.0.0.0',
                                                        'dead_timer': '00:00:03',
                                                        'dr_ip_addr': '10.196.55.54',
                                                        'first': '0x0(0)/0x625F6304(13775194)',
                                                        'hello_options': '0x2',
                                                        'index': '3/3,',
                                                        'interface': 'TenGigabitEthernet3/1/5',
                                                        'neighbor_router_id': '10.196.55.49',
                                                        'next': '0x0(0)/0x625F6304(13775194)',
                                                        'priority': 0,
                                                        'state': 'full',
                                                        'statistics': 
                                                            {'last_retrans_max_scan_length': 3,
                                                            'last_retrans_max_scan_time_msec': 4,
                                                            'last_retrans_scan_length': 0,
                                                            'last_retrans_scan_time_msec': 0,
                                                            'nbr_event_count': 12,
                                                            'nbr_retrans_qlen': 5,
                                                            'total_retransmission': 6},
                                                        'uptime': '3d00h'}}}}}}},
                            '1666': 
                                {'areas': 
                                    {'0.0.6.130': 
                                        {'interfaces': 
                                            {'TenGigabitEthernet3/1/3': 
                                                {'neighbors': 
                                                    {'10.196.55.21': 
                                                        {'address': '10.196.55.21',
                                                        'bdr_ip_addr': '0.0.0.0',
                                                        'dead_timer': '00:00:03',
                                                        'dr_ip_addr': '10.196.55.26',
                                                        'first': '0x0(0)/0x0(0)',
                                                        'hello_options': '0x2',
                                                        'index': '1/1,',
                                                        'interface': 'TenGigabitEthernet3/1/3',
                                                        'neighbor_router_id': '10.196.55.21',
                                                        'next': '0x0(0)/0x0(0)',
                                                        'priority': 0,
                                                        'state': 'full',
                                                        'statistics': 
                                                            {'last_retrans_max_scan_length': 0,
                                                            'last_retrans_max_scan_time_msec': 0,
                                                            'last_retrans_scan_length': 0,
                                                            'last_retrans_scan_time_msec': 0,
                                                            'nbr_event_count': 12,
                                                            'nbr_retrans_qlen': 0,
                                                            'total_retransmission': 0},
                                                        'uptime': '3d00h'}}},
                                            'TenGigabitEthernet3/1/4': 
                                                {'neighbors': 
                                                    {'10.196.55.93': 
                                                        {'address': '10.196.55.93',
                                                        'bdr_ip_addr': '0.0.0.0',
                                                        'dead_timer': '00:00:03',
                                                        'dr_ip_addr': '10.196.55.98',
                                                        'first': '0x0(0)/0x0(0)',
                                                        'hello_options': '0x2',
                                                        'index': '2/2,',
                                                        'interface': 'TenGigabitEthernet3/1/4',
                                                        'neighbor_router_id': '10.196.55.93',
                                                        'next': '0x0(0)/0x0(0)',
                                                        'priority': 0,
                                                        'state': 'full',
                                                        'statistics': 
                                                            {'last_retrans_max_scan_length': 0,
                                                            'last_retrans_max_scan_time_msec': 0,
                                                            'last_retrans_scan_length': 0,
                                                            'last_retrans_scan_time_msec': 0,
                                                            'nbr_event_count': 18,
                                                            'nbr_retrans_qlen': 0,
                                                            'total_retransmission': 0},
                                                        'uptime': '3d00h'}}}}}}}}}}}}}

    def test_show_ip_ospf_neighbor_detail_full1(self):
        
        self.maxDiff = None

        def mapper(key):
            return self.outputs[key]

        raw1 = '''\
            R1_ospf_xe#show ip ospf neighbor detail 
            Neighbor 10.16.2.2, interface address 10.1.2.2, interface-id unknown
                In the area 0 via interface GigabitEthernet2
                Neighbor priority is 1, State is FULL, 6 state changes
                DR is 10.1.2.1 BDR is 10.1.2.2
                Options is 0x2 in Hello (E-bit)
                Options is 0x42 in DBD (E-bit, O-bit)
                Dead timer due in 00:00:33
                Neighbor is up for 08:04:20
                Index 1/2/2, retransmission queue length 0, number of retransmission 0
                First 0x0(0)/0x0(0)/0x0(0) Next 0x0(0)/0x0(0)/0x0(0)
                Last retransmission scan length is 0, maximum is 0
                Last retransmission scan time is 0 msec, maximum is 0 msec
            Neighbor 10.64.4.4, interface address 10.1.4.4
                In the area 0 via interface GigabitEthernet1
                Neighbor priority is 1, State is FULL, 6 state changes
                DR is 10.1.4.4 BDR is 10.1.4.1
                Options is 0x12 in Hello (E-bit, L-bit)
                Options is 0x52 in DBD (E-bit, L-bit, O-bit)
                LLS Options is 0x1 (LR)
                Dead timer due in 00:00:35
                Neighbor is up for 1d01h   
                Index 1/1/1, retransmission queue length 0, number of retransmission 1
                First 0x0(0)/0x0(0)/0x0(0) Next 0x0(0)/0x0(0)/0x0(0)
                Last retransmission scan length is 0, maximum is 1
                Last retransmission scan time is 0 msec, maximum is 0 msec
            Neighbor 10.151.22.22, interface address 10.151.22.22
                In the area 1 via interface OSPF_SL1
                Neighbor priority is 0, State is FULL, 6 state changes
                DR is 0.0.0.0 BDR is 0.0.0.0
                Options is 0x2 in Hello (E-bit)
                Options is 0x42 in DBD (E-bit, O-bit)
                Dead timer due in 00:00:35
                Neighbor is up for 07:41:59
                Index 1/2/2, retransmission queue length 0, number of retransmission 2
                First 0x0(0)/0x0(0)/0x0(0) Next 0x0(0)/0x0(0)/0x0(0)
                Last retransmission scan length is 1, maximum is 1
                Last retransmission scan time is 0 msec, maximum is 0 msec
            Neighbor 10.115.55.55, interface address 10.186.5.5
                In the area 1 via interface GigabitEthernet3
                Neighbor priority is 1, State is FULL, 6 state changes
                DR is 10.186.5.1 BDR is 10.186.5.5
                Options is 0x12 in Hello (E-bit, L-bit)
                Options is 0x52 in DBD (E-bit, L-bit, O-bit)
                LLS Options is 0x1 (LR)
                Dead timer due in 00:00:34
                Neighbor is up for 15:47:14
                Index 1/1/1, retransmission queue length 0, number of retransmission 6
                First 0x0(0)/0x0(0)/0x0(0) Next 0x0(0)/0x0(0)/0x0(0)
                Last retransmission scan length is 1, maximum is 6
                Last retransmission scan time is 0 msec, maximum is 0 msec
            '''

        raw2_1 = '''\
            R1_ospf_xe#show ip ospf interface | i GigabitEthernet2
            GigabitEthernet2 is up, line protocol is up 
              Internet Address 10.1.2.1/24, Interface ID 8, Area 0
              Attached via Interface Enable
              Process ID 1, Router ID 10.4.1.1, Network Type BROADCAST, Cost: 1
              Topology-MTID    Cost    Disabled    Shutdown      Topology Name
                    0           1         no          no            Base
              Enabled by interface config, including secondary ip addresses
              Transmit Delay is 1 sec, State DR, Priority 1
              Designated Router (ID) 10.4.1.1, Interface address 10.1.2.1
              Backup Designated router (ID) 10.16.2.2, Interface address 10.1.2.2
              Timer intervals configured, Hello 10, Dead 40, Wait 40, Retransmit 5
                oob-resync timeout 40
                Hello due in 00:00:05
              Supports Link-local Signaling (LLS)
              Cisco NSF helper support enabled
              IETF NSF helper support enabled
              Can be protected by per-prefix Loop-Free FastReroute
              Can be used for per-prefix Loop-Free FastReroute repair paths
              Not Protected by per-prefix TI-LFA
              Index 1/3/3, flood queue length 0
              Next 0x0(0)/0x0(0)/0x0(0)
              Last flood scan length is 1, maximum is 3
              Last flood scan time is 0 msec, maximum is 1 msec
              Neighbor Count is 1, Adjacent neighbor count is 1 
                Adjacent with neighbor 10.16.2.2  (Backup Designated Router)
              Suppress hello for 0 neighbor(s)
            '''

        raw2_2 = '''\
            R1_ospf_xe#show ip ospf interface | i GigabitEthernet1
            GigabitEthernet1 is up, line protocol is up 
              Internet Address 10.1.4.1/24, Interface ID 7, Area 0
              Attached via Interface Enable
              Process ID 1, Router ID 10.4.1.1, Network Type BROADCAST, Cost: 1
              Topology-MTID    Cost    Disabled    Shutdown      Topology Name
                    0           1         no          no            Base
              Enabled by interface config, including secondary ip addresses
              Transmit Delay is 1 sec, State BDR, Priority 1
              Designated Router (ID) 10.64.4.4, Interface address 10.1.4.4
              Backup Designated router (ID) 10.4.1.1, Interface address 10.1.4.1
              Timer intervals configured, Hello 10, Dead 40, Wait 40, Retransmit 5
                oob-resync timeout 40
                Hello due in 00:00:08
              Supports Link-local Signaling (LLS)
              Cisco NSF helper support enabled
              IETF NSF helper support enabled
              Can be protected by per-prefix Loop-Free FastReroute
              Can be used for per-prefix Loop-Free FastReroute repair paths
              Not Protected by per-prefix TI-LFA
              Index 1/2/2, flood queue length 0
              Next 0x0(0)/0x0(0)/0x0(0)
              Last flood scan length is 3, maximum is 3
              Last flood scan time is 0 msec, maximum is 1 msec
              Neighbor Count is 1, Adjacent neighbor count is 1 
                Adjacent with neighbor 10.64.4.4  (Designated Router)
              Suppress hello for 0 neighbor(s)
            '''

        raw2_3 = '''
            R1_ospf_xe#show ip ospf interface | i OSPF_SL1
            OSPF_SL1 is up, line protocol is up 
              Internet Address 0.0.0.0/0, Interface ID 14, Area 1
              Attached via Not Attached
              Process ID 2, Router ID 10.229.11.11, Network Type SHAM_LINK, Cost: 111
              Topology-MTID    Cost    Disabled    Shutdown      Topology Name
                    0           111       no          no            Base
              Configured as demand circuit
              Run as demand circuit
              DoNotAge LSA not allowed (Number of DCbitless LSA is 1)
              Transmit Delay is 1 sec, State POINT_TO_POINT
              Timer intervals configured, Hello 10, Dead 40, Wait 40, Retransmit 5
                oob-resync timeout 40
                Hello due in 00:00:00
              Supports Link-local Signaling (LLS)
              Cisco NSF helper support enabled
              IETF NSF helper support enabled
              Strict TTL checking enabled, up to 3 hops allowed
              Can not be protected by per-prefix Loop-Free FastReroute
              Can not be used for per-prefix Loop-Free FastReroute repair paths
              Not Protected by per-prefix TI-LFA
              Index 1/2/2, flood queue length 0
              Next 0x0(0)/0x0(0)/0x0(0)
              Last flood scan length is 1, maximum is 5
              Last flood scan time is 0 msec, maximum is 1 msec
              Neighbor Count is 1, Adjacent neighbor count is 1 
                Adjacent with neighbor 10.151.22.22
              Suppress hello for 0 neighbor(s)
            '''

        raw2_4 = '''
            R1_ospf_xe#show ip ospf interface | i GigabitEthernet3
            GigabitEthernet3 is up, line protocol is up 
              Internet Address 10.186.5.1/24, Interface ID 9, Area 1
              Attached via Interface Enable
              Process ID 2, Router ID 10.229.11.11, Network Type BROADCAST, Cost: 1
              Topology-MTID    Cost    Disabled    Shutdown      Topology Name
                    0           1         no          no            Base
              Enabled by interface config, including secondary ip addresses
              Transmit Delay is 1 sec, State DR, Priority 1
              Designated Router (ID) 10.229.11.11, Interface address 10.186.5.1
              Backup Designated router (ID) 10.115.55.55, Interface address 10.186.5.5
              Timer intervals configured, Hello 10, Dead 40, Wait 40, Retransmit 5
                oob-resync timeout 40
                Hello due in 00:00:08
              Supports Link-local Signaling (LLS)
              Cisco NSF helper support enabled
              IETF NSF helper support enabled
              Can be protected by per-prefix Loop-Free FastReroute
              Can be used for per-prefix Loop-Free FastReroute repair paths
              Not Protected by per-prefix TI-LFA
              Index 1/1/1, flood queue length 0
              Next 0x0(0)/0x0(0)/0x0(0)
              Last flood scan length is 0, maximum is 7
              Last flood scan time is 0 msec, maximum is 1 msec
              Neighbor Count is 1, Adjacent neighbor count is 1 
                Adjacent with neighbor 10.115.55.55  (Backup Designated Router)
              Suppress hello for 0 neighbor(s)
            '''

        raw3_1 = '''\
            R1_ospf_xe#show ip ospf sham-links | i OSPF_SL1
              Sham Link OSPF_SL1 to address 10.151.22.22 is up
            '''

        raw3_2 = '''\
            R1_ospf_xe#show running-config | i sham-link | i 10.151.22.22
              area 1 sham-link 10.229.11.11 10.151.22.22 cost 111 ttl-security hops 3
            '''

        raw4_1 = '''\
            R1_ospf_xe#show running-config | section router ospf 1
              router ospf 1
                mpls traffic-eng router-id Loopback0
                mpls traffic-eng area 0
            '''

        raw4_2 = '''\
            R1_ospf_xe#show running-config | section router ospf 2
              router ospf 2 vrf VRF1
                area 1 virtual-link 10.100.5.5
                area 1 sham-link 10.229.11.11 10.151.22.22 cost 111 ttl-security hops 3
                redistribute bgp
            '''

        self.outputs = {}
        self.outputs['show ip ospf neighbor detail'] = raw1
        self.outputs['show ip ospf interface | section GigabitEthernet2'] = raw2_1
        self.outputs['show ip ospf interface | section GigabitEthernet1'] = raw2_2
        self.outputs['show ip ospf interface | section OSPF_SL1'] = raw2_3
        self.outputs['show ip ospf interface | section GigabitEthernet3'] = raw2_4
        self.outputs['show ip ospf sham-links | i OSPF_SL1'] = raw3_1
        self.outputs['show running-config | i sham-link | i 10.151.22.22'] = raw3_2
        self.outputs['show running-config | section router ospf 1'] = raw4_1
        self.outputs['show running-config | section router ospf 2'] = raw4_2

        self.device.execute = Mock()
        self.device.execute.side_effect = mapper
        
        obj = ShowIpOspfNeighborDetail(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output1)

    def test_show_ip_ospf_neighbor_detail_full2(self):
        
        self.maxDiff = None

        def mapper(key):
            return self.outputs[key]

        raw1 = '''\
            R4_ospf_iosv#show ip ospf neighbor detail (including virtual-link)
            Neighbor 10.36.3.3, interface address 10.229.3.3
                In the area 0 via interface OSPF_VL1
                Neighbor priority is 0, State is FULL, 12 state changes
                DR is 0.0.0.0 BDR is 0.0.0.0
                Options is 0x2 in Hello (E-bit)
                Options is 0x42 in DBD (E-bit, O-bit)
                Dead timer due in 00:00:41
                Neighbor is up for 05:07:21
                Index 1/3, retransmission queue length 0, number of retransmission 3
                First 0x0(0)/0x0(0) Next 0x0(0)/0x0(0)
                Last retransmission scan length is 1, maximum is 1
                Last retransmission scan time is 0 msec, maximum is 0 msec
            Neighbor 10.36.3.3, interface address 10.19.4.3
                In the area 1 via interface GigabitEthernet0/1
                Neighbor priority is 1, State is FULL, 6 state changes
                DR is 10.19.4.4 BDR is 10.19.4.3
                Options is 0x2 in Hello (E-bit)
                Options is 0x42 in DBD (E-bit, O-bit)
                Dead timer due in 00:00:33
                Neighbor is up for 16:31:06
                Index 2/2, retransmission queue length 0, number of retransmission 2
                First 0x0(0)/0x0(0) Next 0x0(0)/0x0(0)
                Last retransmission scan length is 1, maximum is 1
                Last retransmission scan time is 0 msec, maximum is 0 msec
            Neighbor 10.16.2.2, interface address 10.229.4.2
                In the area 1 via interface GigabitEthernet0/0
                Neighbor priority is 1, State is FULL, 6 state changes
                DR is 10.229.4.4 BDR is 10.229.4.2
                Options is 0x12 in Hello (E-bit, L-bit)
                Options is 0x52 in DBD (E-bit, L-bit, O-bit)
                LLS Options is 0x1 (LR)
                Dead timer due in 00:00:34
                Neighbor is up for 05:07:40
                Index 1/1, retransmission queue length 0, number of retransmission 1
                First 0x0(0)/0x0(0) Next 0x0(0)/0x0(0)
                Last retransmission scan length is 1, maximum is 1
                Last retransmission scan time is 0 msec, maximum is 0 msec
            '''

        raw2_1 = '''\
            R4_ospf_iosv#show ip ospf interface | section OSPF_VL1
            OSPF_VL1 is up, line protocol is up 
                Internet Address 10.19.4.4/24, Area 0, Attached via Not Attached
                Process ID 1, Router ID 10.64.4.4, Network Type VIRTUAL_LINK, Cost: 1
                Topology-MTID    Cost    Disabled    Shutdown      Topology Name
                    0           1         no          no            Base
                Configured as demand circuit
                Run as demand circuit
                DoNotAge LSA not allowed (Number of DCbitless LSA is 7)
                Transmit Delay is 1 sec, State POINT_TO_POINT
                Timer intervals configured, Hello 4, Dead 44, Wait 40, Retransmit 5
                oob-resync timeout 44
                Hello due in 00:00:02
                Supports Link-local Signaling (LLS)
                Cisco NSF helper support enabled
                IETF NSF helper support enabled
                Index 2/6, flood queue length 0
                Next 0x0(0)/0x0(0)
                Last flood scan length is 2, maximum is 8
                Last flood scan time is 0 msec, maximum is 0 msec
                Neighbor Count is 1, Adjacent neighbor count is 1 
                Adjacent with neighbor 10.36.3.3
                Suppress hello for 0 neighbor(s)
            '''

        raw2_2 = '''\
            R4_ospf_iosv#show ip ospf interface | section GigabitEthernet0/1
            GigabitEthernet0/1 is up, line protocol is up 
                Internet Address 10.19.4.4/24, Area 1, Attached via Interface Enable
                Process ID 1, Router ID 10.64.4.4, Network Type BROADCAST, Cost: 1
                Topology-MTID    Cost    Disabled    Shutdown      Topology Name
                    0           1         no          no            Base
                Enabled by interface config, including secondary ip addresses
                Transmit Delay is 1 sec, State DR, Priority 1
                Designated Router (ID) 10.64.4.4, Interface address 10.19.4.4
                Backup Designated router (ID) 10.36.3.3, Interface address 10.19.4.3
                Timer intervals configured, Hello 10, Dead 40, Wait 40, Retransmit 5
                oob-resync timeout 40
                Hello due in 00:00:02
                Supports Link-local Signaling (LLS)
                Cisco NSF helper support enabled
                IETF NSF helper support enabled
                Index 3/4, flood queue length 0
                Next 0x0(0)/0x0(0)
                Last flood scan length is 0, maximum is 11
                Last flood scan time is 0 msec, maximum is 1 msec
                Neighbor Count is 1, Adjacent neighbor count is 1 
                Adjacent with neighbor 10.36.3.3  (Backup Designated Router)
                Suppress hello for 0 neighbor(s)
            '''

        raw2_3 = '''\
            R4_ospf_iosv#show ip ospf interface | section GigabitEthernet0/0
            GigabitEthernet0/0 is up, line protocol is up 
                Internet Address 10.229.4.4/24, Area 1, Attached via Interface Enable
                Process ID 1, Router ID 10.64.4.4, Network Type BROADCAST, Cost: 1
                Topology-MTID    Cost    Disabled    Shutdown      Topology Name
                    0           1         no          no            Base
                Enabled by interface config, including secondary ip addresses
                Transmit Delay is 1 sec, State DR, Priority 1
                Designated Router (ID) 10.64.4.4, Interface address 10.229.4.4
                Backup Designated router (ID) 10.16.2.2, Interface address 10.229.4.2
                Timer intervals configured, Hello 10, Dead 40, Wait 40, Retransmit 5
                oob-resync timeout 40
                Hello due in 00:00:02
                Supports Link-local Signaling (LLS)
                Cisco NSF helper support enabled
                IETF NSF helper support enabled
                Index 2/3, flood queue length 0
                Next 0x0(0)/0x0(0)
                Last flood scan length is 1, maximum is 10
                Last flood scan time is 0 msec, maximum is 10 msec
                Neighbor Count is 1, Adjacent neighbor count is 1 
                Adjacent with neighbor 10.16.2.2  (Backup Designated Router)
                Suppress hello for 0 neighbor(s)
            '''

        raw3_1 = '''\
            R1_ospf_xe#show ip ospf virtual-links | i OSPF_VL1
              Virtual Link OSPF_VL1 to router 10.100.5.5 is down
            '''

        raw3_2 = '''\
            R1_ospf_xe#show running-config | i virtual-link | i 10.100.5.5
              area 1 virtual-link 10.100.5.5
            '''

        raw4_1 = '''\
            R1_ospf_xe#show running-config | section router ospf 1
              router ospf 1
                mpls traffic-eng router-id Loopback0
                mpls traffic-eng area 0
            '''

        raw4_2 = '''\
            R1_ospf_xe#show running-config | section router ospf 2
              router ospf 2 vrf VRF1
                area 1 virtual-link 10.100.5.5
                area 1 sham-link 10.229.11.11 10.151.22.22 cost 111 ttl-security hops 3
                redistribute bgp
            '''

        self.outputs = {}
        self.outputs['show ip ospf neighbor detail'] = raw1
        self.outputs['show ip ospf interface | section OSPF_VL1'] = raw2_1
        self.outputs['show ip ospf interface | section GigabitEthernet0/1'] = raw2_2
        self.outputs['show ip ospf interface | section GigabitEthernet0/0'] = raw2_3

        self.outputs['show ip ospf virtual-links | i OSPF_VL1'] = raw3_1
        self.outputs['show running-config | i virtual-link | i 10.100.5.5'] = raw3_2
        
        self.outputs['show running-config | section router ospf 1'] = raw4_1
        self.outputs['show running-config | section router ospf 2'] = raw4_2

        self.device.execute = Mock()
        self.device.execute.side_effect = mapper
        
        obj = ShowIpOspfNeighborDetail(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output2)

    def test_show_ip_ospf_neighbor_detail_full3(self):

        self.maxDiff = None

        def mapper(key):
            return self.outputs[key]

        raw1 = '''\
            nhq-choke-VSS#sh ip ospf neighbor detail
            Neighbor 10.196.55.49, interface address 10.196.55.49
                In the area 0 via interface TenGigabitEthernet3/1/5
                Neighbor priority is 0, State is FULL, 12 state changes
                DR is 10.196.55.54 BDR is 0.0.0.0
                Options is 0x2 in Hello (E-bit)
                Options is 0x2 in DBD (E-bit)
                Dead timer due in 00:00:03
                Neighbor is up for 3d00h
                Index 3/3, retransmission queue length 5, number of retransmission 6
                First 0x0(0)/0x625F6304(13775194) Next 0x0(0)/0x625F6304(13775194)
                Last retransmission scan length is 0, maximum is 3
                Last retransmission scan time is 0 msec, maximum is 4 msec
                Link State retransmission due in 2344 msec
            Neighbor 10.196.55.41, interface address 10.196.55.41
                In the area 0 via interface TenGigabitEthernet3/1/2
                Neighbor priority is 0, State is FULL, 22 state changes
                DR is 10.196.55.46 BDR is 0.0.0.0
                Options is 0x2 in Hello (E-bit)
                Options is 0x2 in DBD (E-bit)
                Dead timer due in 00:00:03
                Neighbor is up for 3d00h
                Index 1/1, retransmission queue length 0, number of retransmission 1
                First 0x0(0)/0x0(0) Next 0x0(0)/0x0(0)
                Last retransmission scan length is 0, maximum is 1
                Last retransmission scan time is 0 msec, maximum is 0 msec
            Neighbor 10.196.55.33, interface address 10.196.55.33
                In the area 0 via interface TenGigabitEthernet3/1/1
                Neighbor priority is 0, State is FULL, 12 state changes
                DR is 10.196.55.38 BDR is 0.0.0.0
                Options is 0x2 in Hello (E-bit)
                Options is 0x2 in DBD (E-bit)
                Dead timer due in 00:00:03
                Neighbor is up for 3d21h
                Index 2/2, retransmission queue length 3, number of retransmission 5
                First 0x0(0)/0x625F62BC(13775196) Next 0x0(0)/0x625F62BC(13775196)
                Last retransmission scan length is 0, maximum is 2
                Last retransmission scan time is 0 msec, maximum is 4 msec
                Link State retransmission due in 4356 msec
            Neighbor 10.196.55.93, interface address 10.196.55.93
                In the area 1666 via interface TenGigabitEthernet3/1/4
                Neighbor priority is 0, State is FULL, 18 state changes
                DR is 10.196.55.98 BDR is 0.0.0.0
                Options is 0x2 in Hello (E-bit)
                Options is 0x2 in DBD (E-bit)
                Dead timer due in 00:00:03
                Neighbor is up for 3d00h
                Index 2/2, retransmission queue length 0, number of retransmission 0
                First 0x0(0)/0x0(0) Next 0x0(0)/0x0(0)
                Last retransmission scan length is 0, maximum is 0
                Last retransmission scan time is 0 msec, maximum is 0 msec
            Neighbor 10.196.55.21, interface address 10.196.55.21
                In the area 1666 via interface TenGigabitEthernet3/1/3
                Neighbor priority is 0, State is FULL, 12 state changes
                DR is 10.196.55.26 BDR is 0.0.0.0
                Options is 0x2 in Hello (E-bit)
                Options is 0x2 in DBD (E-bit)
                Dead timer due in 00:00:03
                Neighbor is up for 3d00h
                Index 1/1, retransmission queue length 0, number of retransmission 0
                First 0x0(0)/0x0(0) Next 0x0(0)/0x0(0)
                Last retransmission scan length is 0, maximum is 0
                Last retransmission scan time is 0 msec, maximum is 0 msec
            '''

        raw2_1 = '''\
            nhq-choke-VSS#show ip ospf interface | section TenGigabitEthernet3/1/1
            TenGigabitEthernet3/1/1 is up, line protocol is up (connected) 
              Internet Address 10.196.55.38/29, Area 0, Attached via Interface Enable
              Process ID 1668, Router ID 10.21.52.10, Network Type BROADCAST, Cost: 1
              Topology-MTID    Cost    Disabled    Shutdown      Topology Name
                    0           1         no          no            Base
              Enabled by interface config, including secondary ip addresses
              Transmit Delay is 1 sec, State DR, Priority 1
              Designated Router (ID) 10.21.52.10, Interface address 10.196.55.38
              No backup designated router on this network
              Timer intervals configured, Hello 1, Dead 4, Wait 4, Retransmit 5
                oob-resync timeout 40
                Hello due in 00:00:00
              Supports Link-local Signaling (LLS)
              Cisco NSF helper support enabled
              IETF NSF helper support enabled
              Index 1/1, flood queue length 0
              Next 0x0(0)/0x0(0)
              Last flood scan length is 2, maximum is 40
              Last flood scan time is 0 msec, maximum is 4 msec
              Neighbor Count is 1, Adjacent neighbor count is 1 
                Adjacent with neighbor 10.196.55.33
              Suppress hello for 0 neighbor(s)
              Cryptographic authentication enabled
                Youngest key id is 1
            '''

        raw2_2 = '''\
            nhq-choke-VSS#show ip ospf interface | section TenGigabitEthernet3/1/2
            TenGigabitEthernet3/1/2 is up, line protocol is up (connected) 
              Internet Address 10.196.55.46/29, Area 0, Attached via Interface Enable
              Process ID 1668, Router ID 10.21.52.10, Network Type BROADCAST, Cost: 1
              Topology-MTID    Cost    Disabled    Shutdown      Topology Name
                    0           1         no          no            Base
              Enabled by interface config, including secondary ip addresses
              Transmit Delay is 1 sec, State DR, Priority 1
              Designated Router (ID) 10.21.52.10, Interface address 10.196.55.46
              No backup designated router on this network
              Timer intervals configured, Hello 1, Dead 4, Wait 4, Retransmit 5
                oob-resync timeout 40
                Hello due in 00:00:00
              Supports Link-local Signaling (LLS)
              Cisco NSF helper support enabled
              IETF NSF helper support enabled
              Index 2/2, flood queue length 0
              Next 0x0(0)/0x0(0)
              Last flood scan length is 2, maximum is 40
              Last flood scan time is 0 msec, maximum is 4 msec
              Neighbor Count is 1, Adjacent neighbor count is 1 
                Adjacent with neighbor 10.196.55.41
              Suppress hello for 0 neighbor(s)
              Cryptographic authentication enabled
                Youngest key id is 1
            '''

        raw2_3 = '''\
            nhq-choke-VSS#show ip ospf interface | section TenGigabitEthernet3/1/3
            TenGigabitEthernet3/1/3 is up, line protocol is up (connected) 
              Internet Address 10.196.55.26/29, Area 1666, Attached via Interface Enable
              Process ID 1666, Router ID 10.15.21.9, Network Type BROADCAST, Cost: 1000
              Topology-MTID    Cost    Disabled    Shutdown      Topology Name
                    0           1000      no          no            Base
              Enabled by interface config, including secondary ip addresses
              Transmit Delay is 1 sec, State DR, Priority 1
              Designated Router (ID) 10.15.21.9, Interface address 10.196.55.26
              No backup designated router on this network
              Timer intervals configured, Hello 1, Dead 4, Wait 4, Retransmit 5
                oob-resync timeout 40
                Hello due in 00:00:00
              Supports Link-local Signaling (LLS)
              Cisco NSF helper support enabled
              IETF NSF helper support enabled
              Index 2/2, flood queue length 0
              Next 0x0(0)/0x0(0)
              Last flood scan length is 1, maximum is 3
              Last flood scan time is 0 msec, maximum is 4 msec
              Neighbor Count is 1, Adjacent neighbor count is 1 
                Adjacent with neighbor 10.196.55.21
              Suppress hello for 0 neighbor(s)
            '''

        raw2_4 = '''\
            nhq-choke-VSS#show ip ospf interface | section TenGigabitEthernet3/1/4
            TenGigabitEthernet3/1/4 is up, line protocol is up (connected) 
              Internet Address 10.196.55.98/29, Area 1666, Attached via Interface Enable
              Process ID 1666, Router ID 10.15.21.9, Network Type BROADCAST, Cost: 1
              Topology-MTID    Cost    Disabled    Shutdown      Topology Name
                    0           1         no          no            Base
              Enabled by interface config, including secondary ip addresses
              Transmit Delay is 1 sec, State DR, Priority 1
              Designated Router (ID) 10.15.21.9, Interface address 10.196.55.98
              No backup designated router on this network
              Timer intervals configured, Hello 1, Dead 4, Wait 4, Retransmit 5
                oob-resync timeout 40
                Hello due in 00:00:00
              Supports Link-local Signaling (LLS)
              Cisco NSF helper support enabled
              IETF NSF helper support enabled
              Index 3/3, flood queue length 0
              Next 0x0(0)/0x0(0)
              Last flood scan length is 1, maximum is 3
              Last flood scan time is 0 msec, maximum is 4 msec
              Neighbor Count is 1, Adjacent neighbor count is 1 
                Adjacent with neighbor 10.196.55.93
              Suppress hello for 0 neighbor(s)
            '''

        raw2_5 = '''\
            nhq-choke-VSS#show ip ospf interface | section TenGigabitEthernet3/1/5
            TenGigabitEthernet3/1/5 is up, line protocol is up (connected) 
              Internet Address 10.196.55.54/29, Area 0, Attached via Interface Enable
              Process ID 1668, Router ID 10.21.52.10, Network Type BROADCAST, Cost: 100
              Topology-MTID    Cost    Disabled    Shutdown      Topology Name
                    0           100       no          no            Base
              Enabled by interface config, including secondary ip addresses
              Transmit Delay is 1 sec, State DR, Priority 1
              Designated Router (ID) 10.21.52.10, Interface address 10.196.55.54
              No backup designated router on this network
              Timer intervals configured, Hello 1, Dead 4, Wait 4, Retransmit 5
                oob-resync timeout 40
                Hello due in 00:00:00
              Supports Link-local Signaling (LLS)
              Cisco NSF helper support enabled
              IETF NSF helper support enabled
              Index 3/3, flood queue length 0
              Next 0x0(0)/0x0(0)
              Last flood scan length is 2, maximum is 40
              Last flood scan time is 0 msec, maximum is 4 msec
              Neighbor Count is 1, Adjacent neighbor count is 1 
                Adjacent with neighbor 10.196.55.49
              Suppress hello for 0 neighbor(s)
              Cryptographic authentication enabled
                Youngest key id is 1
            '''

        raw3_1 = '''\
            R1_ospf_xe#show running-config | section router ospf 1666
            router ospf 1666
            '''

        raw3_2 = '''\
            R1_ospf_xe#show running-config | section router ospf 1668
            router ospf 1668
              router-id 10.21.52.10
            '''

        self.outputs = {}
        self.outputs['show ip ospf neighbor detail'] = raw1
        self.outputs['show ip ospf interface | section TenGigabitEthernet3/1/1'] = raw2_1
        self.outputs['show ip ospf interface | section TenGigabitEthernet3/1/2'] = raw2_2
        self.outputs['show ip ospf interface | section TenGigabitEthernet3/1/3'] = raw2_3
        self.outputs['show ip ospf interface | section TenGigabitEthernet3/1/4'] = raw2_4
        self.outputs['show ip ospf interface | section TenGigabitEthernet3/1/5'] = raw2_5

        self.outputs['show running-config | section router ospf 1666'] = raw3_1
        self.outputs['show running-config | section router ospf 1668'] = raw3_2

        self.device.execute = Mock()
        self.device.execute.side_effect = mapper
        obj = ShowIpOspfNeighborDetail(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output3)
    
    golden_output4 = {'execute.return_value': '''
        show ip ospf neighbor detail
        Neighbor 10.16.2.2, interface address 192.168.154.2, interface-id 24
            In the area 8 via interface GigabitEthernet0/1/2
            Neighbor priority is 0, State is FULL, 6 state changes
            DR is 0.0.0.0 BDR is 0.0.0.0
            SR adj label 16
            Options is 0x12 in Hello (E-bit, L-bit)
            Options is 0x52 in DBD (E-bit, L-bit, O-bit)
            LLS Options is 0x1 (LR)
            Dead timer due in 00:00:38
            Neighbor is up for 3d16h
            Index 1/3/3, retransmission queue length 0, number of retransmission 0
            First 0x0(0)/0x0(0)/0x0(0) Next 0x0(0)/0x0(0)/0x0(0)
            Last retransmission scan length is 0, maximum is 0
            Last retransmission scan time is 0 msec, maximum is 0 msec
        Neighbor 10.16.2.2, interface address 192.168.4.2, interface-id 23
            In the area 8 via interface GigabitEthernet0/1/1
            Neighbor priority is 0, State is FULL, 6 state changes
            DR is 0.0.0.0 BDR is 0.0.0.0
            SR adj label 17
            Options is 0x12 in Hello (E-bit, L-bit)
            Options is 0x52 in DBD (E-bit, L-bit, O-bit)
            LLS Options is 0x1 (LR)
            Dead timer due in 00:00:35
            Neighbor is up for 1w0d
            Index 1/4/4, retransmission queue length 0, number of retransmission 2
            First 0x0(0)/0x0(0)/0x0(0) Next 0x0(0)/0x0(0)/0x0(0)
            Last retransmission scan length is 1, maximum is 1
            Last retransmission scan time is 0 msec, maximum is 0 msec
    '''}
    
    golden_parsed_output4 = {
        'vrf': {
            'default': {
                'address_family': {
                    'ipv4': {
                        'instance': {
                            '65109': {
                                'areas': {
                                    '0.0.0.8': {
                                        'interfaces': {
                                            'GigabitEthernet5': {
                                                'neighbors': {
                                                    '10.16.2.2': {
                                                        'neighbor_router_id': '10.16.2.2',
                                                        'interface': 'GigabitEthernet5',
                                                        'address': '10.225.0.15',
                                                        'interface_id': '11',
                                                        'priority': 0,
                                                        'state': 'full',
                                                        'statistics': {
                                                            'nbr_event_count': 6,
                                                            'nbr_retrans_qlen': 0,
                                                            'total_retransmission': 0,
                                                            'last_retrans_scan_length': 0,
                                                            'last_retrans_max_scan_length': 0,
                                                            'last_retrans_scan_time_msec': 0,
                                                            'last_retrans_max_scan_time_msec': 0,
                                                            },
                                                        'dr_ip_addr': '0.0.0.0',
                                                        'bdr_ip_addr': '0.0.0.0',
                                                        'sr_adj_label': '16',
                                                        'dead_timer': '00:00:31',
                                                        'uptime': '6d07h',
                                                        'index': '1/4/4,',
                                                        'first': '0x0(0)/0x0(0)/0x0(0)',
                                                        'next': '0x0(0)/0x0(0)/0x0(0)',
                                                        },
                                                    },
                                                },
                                            'GigabitEthernet4': {
                                                'neighbors': {
                                                    '10.16.2.2': {
                                                        'neighbor_router_id': '10.16.2.2',
                                                        'interface': 'GigabitEthernet4',
                                                        'address': '10.225.0.16',
                                                        'interface_id': '10',
                                                        'priority': 0,
                                                        'state': 'full',
                                                        'statistics': {
                                                            'nbr_event_count': 6,
                                                            'nbr_retrans_qlen': 0,
                                                            'total_retransmission': 0,
                                                            'last_retrans_scan_length': 0,
                                                            'last_retrans_max_scan_length': 0,
                                                            'last_retrans_scan_time_msec': 0,
                                                            'last_retrans_max_scan_time_msec': 0,
                                                            },
                                                        'dr_ip_addr': '0.0.0.0',
                                                        'bdr_ip_addr': '0.0.0.0',
                                                        'dead_timer': '00:00:32',
                                                        'uptime': '6d07h',
                                                        'index': '1/3/3,',
                                                        'first': '0x0(0)/0x0(0)/0x0(0)',
                                                        'next': '0x0(0)/0x0(0)/0x0(0)',
                                                        },
                                                    },
                                                },
                                            'GigabitEthernet3': {
                                                'neighbors': {
                                                    '10.16.2.2': {
                                                        'neighbor_router_id': '10.16.2.2',
                                                        'interface': 'GigabitEthernet3',
                                                        'address': '10.225.0.17',
                                                        'interface_id': '9',
                                                        'priority': 0,
                                                        'state': 'full',
                                                        'statistics': {
                                                            'nbr_event_count': 6,
                                                            'nbr_retrans_qlen': 0,
                                                            'total_retransmission': 0,
                                                            'last_retrans_scan_length': 0,
                                                            'last_retrans_max_scan_length': 0,
                                                            'last_retrans_scan_time_msec': 0,
                                                            'last_retrans_max_scan_time_msec': 0,
                                                            },
                                                        'dr_ip_addr': '0.0.0.0',
                                                        'bdr_ip_addr': '0.0.0.0',
                                                        'dead_timer': '00:00:34',
                                                        'uptime': '6d07h',
                                                        'index': '1/2/2,',
                                                        'first': '0x0(0)/0x0(0)/0x0(0)',
                                                        'next': '0x0(0)/0x0(0)/0x0(0)',
                                                        },
                                                    },
                                                },
                                            'GigabitEthernet2': {
                                                'neighbors': {
                                                    '10.16.2.2': {
                                                        'neighbor_router_id': '10.16.2.2',
                                                        'interface': 'GigabitEthernet2',
                                                        'address': '10.225.0.18',
                                                        'interface_id': '8',
                                                        'priority': 0,
                                                        'state': 'full',
                                                        'statistics': {
                                                            'nbr_event_count': 6,
                                                            'nbr_retrans_qlen': 0,
                                                            'total_retransmission': 0,
                                                            'last_retrans_scan_length': 0,
                                                            'last_retrans_max_scan_length': 0,
                                                            'last_retrans_scan_time_msec': 0,
                                                            'last_retrans_max_scan_time_msec': 0,
                                                            },
                                                        'dr_ip_addr': '0.0.0.0',
                                                        'bdr_ip_addr': '0.0.0.0',
                                                        'dead_timer': '00:00:35',
                                                        'uptime': '6d07h',
                                                        'index': '1/1/1,',
                                                        'first': '0x0(0)/0x0(0)/0x0(0)',
                                                        'next': '0x0(0)/0x0(0)/0x0(0)',
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
                },
            },
        }

    def test_golden4(self):
        self.maxDiff = None

        def mapper(key):
            return self.outputs[key]
        raw1 = '''
        Neighbor 10.16.2.2, interface address 10.225.0.15, interface-id 11
            In the area 8 via interface GigabitEthernet5
            Neighbor priority is 0, State is FULL, 6 state changes
            DR is 0.0.0.0 BDR is 0.0.0.0
            SR adj label 16
            Options is 0x12 in Hello (E-bit, L-bit)
            Options is 0x52 in DBD (E-bit, L-bit, O-bit)
            LLS Options is 0x1 (LR)
            Dead timer due in 00:00:31
            Neighbor is up for 6d07h
            Index 1/4/4, retransmission queue length 0, number of retransmission 0
            First 0x0(0)/0x0(0)/0x0(0) Next 0x0(0)/0x0(0)/0x0(0)
            Last retransmission scan length is 0, maximum is 0
            Last retransmission scan time is 0 msec, maximum is 0 msec
        Neighbor 10.16.2.2, interface address 10.225.0.16, interface-id 10
            In the area 8 via interface GigabitEthernet4
            Neighbor priority is 0, State is FULL, 6 state changes
            DR is 0.0.0.0 BDR is 0.0.0.0
            Options is 0x12 in Hello (E-bit, L-bit)
            Options is 0x52 in DBD (E-bit, L-bit, O-bit)
            LLS Options is 0x1 (LR)
            Dead timer due in 00:00:32
            Neighbor is up for 6d07h
            Index 1/3/3, retransmission queue length 0, number of retransmission 0
            First 0x0(0)/0x0(0)/0x0(0) Next 0x0(0)/0x0(0)/0x0(0)
            Last retransmission scan length is 0, maximum is 0
            Last retransmission scan time is 0 msec, maximum is 0 msec
        Neighbor 10.16.2.2, interface address 10.225.0.17, interface-id 9
            In the area 8 via interface GigabitEthernet3
            Neighbor priority is 0, State is FULL, 6 state changes
            DR is 0.0.0.0 BDR is 0.0.0.0
            Options is 0x12 in Hello (E-bit, L-bit)
            Options is 0x52 in DBD (E-bit, L-bit, O-bit)
            LLS Options is 0x1 (LR)
            Dead timer due in 00:00:34
            Neighbor is up for 6d07h
            Index 1/2/2, retransmission queue length 0, number of retransmission 0
            First 0x0(0)/0x0(0)/0x0(0) Next 0x0(0)/0x0(0)/0x0(0)
            Last retransmission scan length is 0, maximum is 0
            Last retransmission scan time is 0 msec, maximum is 0 msec
        Neighbor 10.16.2.2, interface address 10.225.0.18, interface-id 8
            In the area 8 via interface GigabitEthernet2
            Neighbor priority is 0, State is FULL, 6 state changes
            DR is 0.0.0.0 BDR is 0.0.0.0
            Options is 0x12 in Hello (E-bit, L-bit)
            Options is 0x52 in DBD (E-bit, L-bit, O-bit)
            LLS Options is 0x1 (LR)
            Dead timer due in 00:00:35
            Neighbor is up for 6d07h
            Index 1/1/1, retransmission queue length 0, number of retransmission 0
            First 0x0(0)/0x0(0)/0x0(0) Next 0x0(0)/0x0(0)/0x0(0)
            Last retransmission scan length is 0, maximum is 0
            Last retransmission scan time is 0 msec, maximum is 0 msec
            '''
        raw2_1 = '''
            show ip ospf interface | section GigabitEthernet5
            GigabitEthernet5 is up, line protocol is up
            Internet Address 10.225.0.28/30, Interface ID 11, Area 8
            Attached via Network Statement
            Process ID 65109, Router ID 10.4.1.1, Network Type POINT_TO_POINT, Cost: 1
            Topology-MTID    Cost    Disabled    Shutdown      Topology Name
                    0           1         no          no            Base
            Transmit Delay is 1 sec, State POINT_TO_POINT
            Timer intervals configured, Hello 10, Dead 40, Wait 40, Retransmit 5
                oob-resync timeout 40
                Hello due in 00:00:01
            Supports Link-local Signaling (LLS)
            Cisco NSF helper support enabled
            IETF NSF helper support enabled
            Can be protected by per-prefix Loop-Free FastReroute
            Can be used for per-prefix Loop-Free FastReroute repair paths
            Not Protected by per-prefix TI-LFA
            Index 1/4/4, flood queue length 0
            Next 0x0(0)/0x0(0)/0x0(0)
            Last flood scan length is 1, maximum is 10
            Last flood scan time is 0 msec, maximum is 9 msec
            Neighbor Count is 1, Adjacent neighbor count is 1
                Adjacent with neighbor 10.16.2.2
            Suppress hello for 0 neighbor(s)
        '''
        raw2_2 = '''
            show ip ospf interface | section GigabitEthernet4
            GigabitEthernet4 is up, line protocol is up
            Internet Address 10.225.0.29/30, Interface ID 10, Area 8
            Attached via Network Statement
            Process ID 65109, Router ID 10.4.1.1, Network Type POINT_TO_POINT, Cost: 1
            Topology-MTID    Cost    Disabled    Shutdown      Topology Name
                    0           1         no          no            Base
            Transmit Delay is 1 sec, State POINT_TO_POINT
            Timer intervals configured, Hello 10, Dead 40, Wait 40, Retransmit 5
                oob-resync timeout 40
                Hello due in 00:00:07
            Supports Link-local Signaling (LLS)
            Cisco NSF helper support enabled
            IETF NSF helper support enabled
            Can be protected by per-prefix Loop-Free FastReroute
            Can be used for per-prefix Loop-Free FastReroute repair paths
            Not Protected by per-prefix TI-LFA
            Index 1/3/3, flood queue length 0
            Next 0x0(0)/0x0(0)/0x0(0)
            Last flood scan length is 1, maximum is 10
            Last flood scan time is 0 msec, maximum is 1 msec
            Neighbor Count is 1, Adjacent neighbor count is 1
                Adjacent with neighbor 10.16.2.2
            Suppress hello for 0 neighbor(s)
        '''
        raw2_3 = '''
            show ip ospf interface | section GigabitEthernet3
            GigabitEthernet3 is up, line protocol is up
            Internet Address 10.225.0.30/30, Interface ID 9, Area 8
            Attached via Network Statement
            Process ID 65109, Router ID 10.4.1.1, Network Type POINT_TO_POINT, Cost: 1
            Topology-MTID    Cost    Disabled    Shutdown      Topology Name
                    0           1         no          no            Base
            Transmit Delay is 1 sec, State POINT_TO_POINT
            Timer intervals configured, Hello 10, Dead 40, Wait 40, Retransmit 5
                oob-resync timeout 40
                Hello due in 00:00:05
            Supports Link-local Signaling (LLS)
            Cisco NSF helper support enabled
            IETF NSF helper support enabled
            Can be protected by per-prefix Loop-Free FastReroute
            Can be used for per-prefix Loop-Free FastReroute repair paths
            Not Protected by per-prefix TI-LFA
            Index 1/2/2, flood queue length 0
            Next 0x0(0)/0x0(0)/0x0(0)
            Last flood scan length is 1, maximum is 10
            Last flood scan time is 1 msec, maximum is 1 msec
            Neighbor Count is 1, Adjacent neighbor count is 1
                Adjacent with neighbor 10.16.2.2
            Suppress hello for 0 neighbor(s)
        '''
        raw2_4 = '''
            show ip ospf interface | section GigabitEthernet2
            GigabitEthernet2 is up, line protocol is up
            Internet Address 10.225.0.31/30, Interface ID 8, Area 8
            Attached via Network Statement
            Process ID 65109, Router ID 10.4.1.1, Network Type POINT_TO_POINT, Cost: 1
            Topology-MTID    Cost    Disabled    Shutdown      Topology Name
                    0           1         no          no            Base
            Transmit Delay is 1 sec, State POINT_TO_POINT
            Timer intervals configured, Hello 10, Dead 40, Wait 40, Retransmit 5
                oob-resync timeout 40
                Hello due in 00:00:06
            Supports Link-local Signaling (LLS)
            Cisco NSF helper support enabled
            IETF NSF helper support enabled
            Can be protected by per-prefix Loop-Free FastReroute
            Can be used for per-prefix Loop-Free FastReroute repair paths
            Not Protected by per-prefix TI-LFA
            Index 1/1/1, flood queue length 0
            Next 0x0(0)/0x0(0)/0x0(0)
            Last flood scan length is 1, maximum is 10
            Last flood scan time is 0 msec, maximum is 1 msec
            Neighbor Count is 1, Adjacent neighbor count is 1
                Adjacent with neighbor 10.16.2.2
            Suppress hello for 0 neighbor(s)
        '''

        raw3_1 = '''
            show running-config | section router ospf 65109
            router ospf 65109
            router-id 10.4.1.1
            network 0.0.0.0 255.255.255.255 area 8
        '''

        self.outputs = {}
        self.outputs['show ip ospf neighbor detail'] = raw1
        self.outputs['show ip ospf interface | section GigabitEthernet5'] = raw2_1
        self.outputs['show ip ospf interface | section GigabitEthernet4'] = raw2_2
        self.outputs['show ip ospf interface | section GigabitEthernet3'] = raw2_3
        self.outputs['show ip ospf interface | section GigabitEthernet2'] = raw2_4

        self.outputs['show running-config | section router ospf 65109'] = raw3_1

        self.device.execute = Mock()
        self.device.execute.side_effect = mapper
        
        obj = ShowIpOspfNeighborDetail(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output4)

    def test_show_ip_ospf_neighbor_detail_empty(self):
        self.maxDiff = None
        self.device = Mock(**self.empty_output)
        obj = ShowIpOspfNeighborDetail(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()


# =======================================
# Unit test for 'show ip ospf sham-links'
# =======================================
class test_show_ip_ospf_sham_links(unittest.TestCase):

    '''Unit test for "show ip ospf sham-links"'''

    device = Device(name='aDevice')
    
    empty_output = {'execute.return_value': ''}

    golden_parsed_output1 = {
        'vrf': 
            {'VRF1': 
                {'address_family': 
                    {'ipv4': 
                        {'instance': 
                            {'2': 
                                {'areas': 
                                    {'0.0.0.1': 
                                        {'sham_links': 
                                            {'10.229.11.11 10.151.22.22': 
                                                {'adjacency_state': 'full',
                                                'cost': 111,
                                                'dcbitless_lsa_count': 1,
                                                'dead_interval': 40,
                                                'demand_circuit': True,
                                                'donotage_lsa': 'not allowed',
                                                'first': '0x0(0)/0x0(0)/0x0(0)',
                                                'hello_interval': 10,
                                                'hello_timer': '00:00:00',
                                                'index': '1/2/2',
                                                'last_retransmission_max_length': 1,
                                                'last_retransmission_max_scan': 0,
                                                'last_retransmission_scan_length': 1,
                                                'last_retransmission_scan_time': 0,
                                                'link_state': 'up',
                                                'local_id': '10.229.11.11',
                                                'name': 'SL0',
                                                'next': '0x0(0)/0x0(0)/0x0(0)',
                                                'remote_id': '10.151.22.22',
                                                'retrans_qlen': 0,
                                                'state': 'point_to_point,',
                                                'ttl_security': 
                                                    {'enable': True,
                                                    'hops': 3},
                                                'total_retransmission': 2,
                                                'transit_area_id': '0.0.0.1',
                                                'wait_interval': 40}}}}}}}}}}}

    def test_show_ip_ospf_sham_links_full1(self):
        
        self.maxDiff = None

        def mapper(key):
            return self.outputs[key]

        raw1 = '''\
            R1_ospf_xe#show ip ospf sham-links 
            Sham Link OSPF_SL0 to address 10.151.22.22 is up
            Area 1 source address 10.229.11.11
              Run as demand circuit
              DoNotAge LSA not allowed (Number of DCbitless LSA is 1). Cost of using 111 State POINT_TO_POINT,
              Timer intervals configured, Hello 10, Dead 40, Wait 40,
              Strict TTL checking enabled, up to 3 hops allowed
                Hello due in 00:00:00
                Adjacency State FULL
                Index 1/2/2, retransmission queue length 0, number of retransmission 2
                First 0x0(0)/0x0(0)/0x0(0) Next 0x0(0)/0x0(0)/0x0(0)
                Last retransmission scan length is 1, maximum is 1
                Last retransmission scan time is 0 msec, maximum is 0 msec
            '''

        raw2 = '''\
            R1_ospf_xe#show ip ospf interface | section OSPF_SL0
            OSPF_SL0 is down, line protocol is down
              Internet Address 0.0.0.0/0, Interface ID 15, Area 1
              Attached via Not Attached
              Process ID 2, Router ID 10.229.11.11, Network Type SHAM_LINK, Cost: 111
              Topology-MTID    Cost    Disabled    Shutdown      Topology Name
                    0           111       no          no            Base
              Configured as demand circuit
              Run as demand circuit
              DoNotAge LSA not allowed (Number of DCbitless LSA is 1)
              Transmit Delay is 1 sec, State DOWN
              Timer intervals configured, Hello 10, Dead 40, Wait 40, Retransmit 5
                oob-resync timeout 40
            '''

        raw3 = '''\
            R1_ospf_xe#show running-config | section router ospf 2
              router ospf 2 vrf VRF1
                area 1 virtual-link 10.100.5.5
                area 1 sham-link 10.229.11.11 10.151.22.22 cost 111 ttl-security hops 3
                redistribute bgp
            '''

        self.outputs = {}
        self.outputs['show ip ospf sham-links'] = raw1
        self.outputs['show ip ospf interface | section OSPF_SL0'] = raw2
        self.outputs['show running-config | section router ospf 2'] = raw3

        self.device.execute = Mock()
        self.device.execute.side_effect = mapper
        
        obj = ShowIpOspfShamLinks(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output1)

    def test_show_ip_ospf_sham_links_empty(self):
        self.maxDiff = None
        self.device = Mock(**self.empty_output)
        obj = ShowIpOspfShamLinks(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()


# ==========================================
# Unit test for 'show ip ospf virtual-links'
# ==========================================
class test_show_ip_ospf_virtual_links(unittest.TestCase):

    '''Unit test for "show ip ospf virtual-links"'''

    device = Device(name='aDevice')
    
    empty_output = {'execute.return_value': ''}

    golden_parsed_output1 = {
        'vrf': 
            {'VRF1': 
                {'address_family': 
                    {'ipv4': 
                        {'instance': 
                            {'2': 
                                {'areas': 
                                    {'0.0.0.1': 
                                        {'virtual_links': 
                                            {'0.0.0.1 10.36.3.3': 
                                                {'adjacency_state': 'full',
                                                'dcbitless_lsa_count': 7,
                                                'dead_interval': 40,
                                                'demand_circuit': True,
                                                'donotage_lsa': 'not allowed',
                                                'first': '0x0(0)/0x0(0)',
                                                'hello_interval': 10,
                                                'hello_timer': '00:00:08',
                                                'index': '1/3',
                                                'interface': 'GigabitEthernet0/1',
                                                'last_retransmission_max_length': 0,
                                                'last_retransmission_max_scan': 0,
                                                'last_retransmission_scan_length': 0,
                                                'last_retransmission_scan_time': 0,
                                                'link_state': 'up',
                                                'name': 'VL0',
                                                'next': '0x0(0)/0x0(0)',
                                                'retrans_qlen': 0,
                                                'retransmit_interval': 5,
                                                'router_id': '10.36.3.3',
                                                'state': 'point-to-point,',
                                                'topology': 
                                                    {0: 
                                                        {'cost': 1,
                                                        'disabled': False,
                                                        'name': 'Base',
                                                        'shutdown': False}},
                                                'total_retransmission': 0,
                                                'transit_area_id': '0.0.0.1',
                                                'transmit_delay': 1,
                                                'wait_interval': 40}}}}}}}}}}}

    def test_show_ip_ospf_virtual_links_full1(self):
        
        self.maxDiff = None

        def mapper(key):
            return self.outputs[key]

        raw1 = '''\
            R4_ospf_iosv#show ip ospf virtual-links 
            Virtual Link OSPF_VL0 to router 10.36.3.3 is up
              Run as demand circuit
              DoNotAge LSA not allowed (Number of DCbitless LSA is 7).
              Transit area 1, via interface GigabitEthernet0/1
             Topology-MTID    Cost    Disabled     Shutdown      Topology Name
                    0           1         no          no            Base
              Transmit Delay is 1 sec, State POINT_TO_POINT,
              Timer intervals configured, Hello 10, Dead 40, Wait 40, Retransmit 5
                Hello due in 00:00:08
                Adjacency State FULL
                Index 1/3, retransmission queue length 0, number of retransmission 0
                First 0x0(0)/0x0(0) Next 0x0(0)/0x0(0)
                Last retransmission scan length is 0, maximum is 0
                Last retransmission scan time is 0 msec, maximum is 0 msec
            '''

        raw2 = '''\
            R1_ospf_xe#show ip ospf interface | section OSPF_VL0
            OSPF_VL0 is down, line protocol is down
              Internet Address 0.0.0.0/0, Interface ID 16, Area 0
              Attached via Not Attached
              Process ID 2, Router ID 10.229.11.11, Network Type VIRTUAL_LINK, Cost: 65535
              Topology-MTID    Cost    Disabled    Shutdown      Topology Name
                    0           65535     no          no            Base
              Configured as demand circuit
              Run as demand circuit
              DoNotAge LSA not allowed (Number of DCbitless LSA is 1)
              Transmit Delay is 1 sec, State DOWN
              Timer intervals configured, Hello 10, Dead 40, Wait 40, Retransmit 5
                oob-resync timeout 40
            '''

        raw3 = '''\
            R1_ospf_xe#show running-config | section router ospf 2
              router ospf 2 vrf VRF1
                area 1 virtual-link 10.100.5.5
                area 1 sham-link 10.229.11.11 10.151.22.22 cost 111 ttl-security hops 3
                redistribute bgp
            '''

        self.outputs = {}
        self.outputs['show ip ospf virtual-links'] = raw1
        self.outputs['show ip ospf interface | section OSPF_VL0'] = raw2
        self.outputs['show running-config | section router ospf 2'] = raw3

        self.device.execute = Mock()
        self.device.execute.side_effect = mapper
        
        obj = ShowIpOspfVirtualLinks(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output1)

    def test_show_ip_ospf_sham_links_empty(self):
        self.maxDiff = None
        self.device = Mock(**self.empty_output)
        obj = ShowIpOspfVirtualLinks(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()


# =====================================
# Unit test for 'show ip ospf database'
# =====================================
class test_show_ip_ospf_database(unittest.TestCase):

    '''Unit test for "show ip ospf database" '''

    device = Device(name='aDevice')

    empty_output = {'execute.return_value': ''}

    golden_parsed_output1 = {
        'vrf': 
            {'default': 
                {'address_family': 
                    {'ipv4': 
                        {'instance': 
                            {'1': 
                                {'areas': 
                                    {'0.0.0.9': 
                                        {'database': 
                                            {'lsa_types': 
                                                {1: 
                                                    {'lsa_type': 1,
                                                    'lsas': 
                                                        {'10.4.1.1': 
                                                            {'adv_router': '10.4.1.1',
                                                            'lsa_id': '10.4.1.1',
                                                            'ospfv2': 
                                                                {'header': 
                                                                    {'adv_router': '10.4.1.1',
                                                                    'age': 167,
                                                                    'checksum': '0x00D8C6',
                                                                    'link_count': 1,
                                                                    'lsa_id': '10.4.1.1',
                                                                    'seq_num': '0x8000000D'}}}}}}}}}},
                            '65109': 
                                {'areas': 
                                    {'0.0.0.0': 
                                        {'database': 
                                            {'lsa_types': 
                                                {1: 
                                                    {'lsa_type': 1,
                                                    'lsas': 
                                                        {'172.31.197.252': 
                                                            {'adv_router': '172.31.197.252',
                                                            'lsa_id': '172.31.197.252',
                                                            'ospfv2': 
                                                                {'header': 
                                                                    {'adv_router': '172.31.197.252',
                                                                    'age': 1802,
                                                                    'checksum': '0x007F23',
                                                                    'link_count': 5,
                                                                    'lsa_id': '172.31.197.252',
                                                                    'seq_num': '0x80000161'}}},
                                                        '172.31.197.253': 
                                                            {'adv_router': '172.31.197.253',
                                                            'lsa_id': '172.31.197.253',
                                                            'ospfv2': 
                                                                {'header': 
                                                                    {'adv_router': '172.31.197.253',
                                                                    'age': 1784,
                                                                    'checksum': '0x00CC34',
                                                                    'link_count': 8,
                                                                    'lsa_id': '172.31.197.253',
                                                                    'seq_num': '0x80000103'}}},
                                                        '172.31.197.254': 
                                                            {'adv_router': '172.31.197.254',
                                                            'lsa_id': '172.31.197.254',
                                                            'ospfv2': 
                                                                {'header': 
                                                                    {'adv_router': '172.31.197.254',
                                                                    'age': 1675,
                                                                    'checksum': '0x007A61',
                                                                    'link_count': 3,
                                                                    'lsa_id': '172.31.197.254',
                                                                    'seq_num': '0x8000000C'}}},
                                                        '192.168.255.0': 
                                                            {'adv_router': '192.168.255.0',
                                                            'lsa_id': '192.168.255.0',
                                                            'ospfv2': 
                                                                {'header': 
                                                                    {'adv_router': '192.168.255.0',
                                                                    'age': 226,
                                                                    'checksum': '0x006975',
                                                                    'link_count': 501,
                                                                    'lsa_id': '192.168.255.0',
                                                                    'seq_num': '0x80000069'}}},
                                                        '192.168.165.119': 
                                                            {'adv_router': '192.168.165.119',
                                                            'lsa_id': '192.168.165.119',
                                                            'ospfv2': 
                                                                {'header': 
                                                                    {'adv_router': '192.168.165.119',
                                                                    'age': 1089,
                                                                    'checksum': '0x0080E0',
                                                                    'link_count': 2,
                                                                    'lsa_id': '192.168.165.119',
                                                                    'seq_num': '0x80000029'}}},
                                                        '192.168.165.120': 
                                                            {'adv_router': '192.168.165.120',
                                                            'lsa_id': '192.168.165.120',
                                                            'ospfv2': 
                                                                {'header': 
                                                                    {'adv_router': '192.168.165.120',
                                                                    'age': 1482,
                                                                    'checksum': '0x0063CB',
                                                                    'link_count': 2,
                                                                    'lsa_id': '192.168.165.120',
                                                                    'seq_num': '0x80000033'}}},
                                                        '192.168.165.220': 
                                                            {'adv_router': '192.168.165.220',
                                                            'lsa_id': '192.168.165.220',
                                                            'ospfv2': 
                                                                {'header': 
                                                                    {'adv_router': '192.168.165.220',
                                                                    'age': 525,
                                                                    'checksum': '0x004E8E',
                                                                    'link_count': 3,
                                                                    'lsa_id': '192.168.165.220',
                                                                    'seq_num': '0x800000DE'}}},
                                                        '10.22.102.64': 
                                                            {'adv_router': '10.22.102.64',
                                                            'lsa_id': '10.22.102.64',
                                                            'ospfv2': 
                                                                {'header': 
                                                                    {'adv_router': '10.22.102.64',
                                                                    'age': 2794,
                                                                    'checksum': '0x002254',
                                                                    'link_count': 3,
                                                                    'lsa_id': '10.22.102.64',
                                                                    'seq_num': '0x80000043'}}}}},
                                                2: 
                                                    {'lsa_type': 2,
                                                    'lsas': 
                                                        {'172.31.197.102': 
                                                            {'adv_router': '192.168.165.220',
                                                            'lsa_id': '172.31.197.102',
                                                            'ospfv2': 
                                                                {'header': 
                                                                    {'adv_router': '192.168.165.220',
                                                                    'age': 525,
                                                                    'checksum': '0x0094CD',
                                                                    'lsa_id': '172.31.197.102',
                                                                    'seq_num': '0x80000058'}}},
                                                        '172.31.197.93': 
                                                            {'adv_router': '172.31.197.252',
                                                            'lsa_id': '172.31.197.93',
                                                            'ospfv2': 
                                                                {'header': 
                                                                    {'adv_router': '172.31.197.252',
                                                                    'age': 1802,
                                                                    'checksum': '0x002D67',
                                                                    'lsa_id': '172.31.197.93',
                                                                    'seq_num': '0x80000008'}}},
                                                        '172.31.197.97': 
                                                            {'adv_router': '172.31.197.253',
                                                            'lsa_id': '172.31.197.97',
                                                            'ospfv2': 
                                                                {'header': 
                                                                    {'adv_router': '172.31.197.253',
                                                                    'age': 1356,
                                                                    'checksum': '0x000D83',
                                                                    'lsa_id': '172.31.197.97',
                                                                    'seq_num': '0x80000006'}}},
                                                        '192.168.255.0': 
                                                            {'adv_router': '172.31.197.253',
                                                            'lsa_id': '192.168.255.0',
                                                            'ospfv2': 
                                                                {'header': 
                                                                    {'adv_router': '172.31.197.253',
                                                                    'age': 2213,
                                                                    'checksum': '0x00D374',
                                                                    'lsa_id': '192.168.255.0',
                                                                    'seq_num': '0x80000BA8'}}},
                                                        '10.1.1.2': 
                                                            {'adv_router': '172.31.197.253',
                                                            'lsa_id': '10.1.1.2',
                                                            'ospfv2': 
                                                                {'header': 
                                                                    {'adv_router': '172.31.197.253',
                                                                    'age': 70,
                                                                    'checksum': '0x0015EF',
                                                                    'lsa_id': '10.1.1.2',
                                                                     'seq_num': '0x8000003F'}}},
                                                        '192.168.165.49': 
                                                            {'adv_router': '172.31.197.253',
                                                            'lsa_id': '192.168.165.49',
                                                            'ospfv2': 
                                                                {'header': 
                                                                    {'adv_router': '172.31.197.253',
                                                                    'age': 499,
                                                                    'checksum': '0x005CBC',
                                                                    'lsa_id': '192.168.165.49',
                                                                     'seq_num': '0x8000001A'}}},
                                                        '192.168.165.57': 
                                                            {'adv_router': '172.31.197.253',
                                                            'lsa_id': '192.168.165.57',
                                                            'ospfv2': 
                                                                {'header': 
                                                                    {'adv_router': '172.31.197.253',
                                                                    'age': 927,
                                                                    'checksum': '0x0008FE',
                                                                    'lsa_id': '192.168.165.57',
                                                                    'seq_num': '0x80000023'}}},
                                                        '10.22.102.49': 
                                                            {'adv_router': '172.31.197.252',
                                                            'lsa_id': '10.22.102.49',
                                                            'ospfv2': 
                                                                {'header': 
                                                                    {'adv_router': '172.31.197.252',
                                                                    'age': 289,
                                                                    'checksum': '0x007AD0',
                                                                    'lsa_id': '10.22.102.49',
                                                                    'seq_num': '0x8000005B'}}},
                                                        '10.22.102.57': 
                                                            {'adv_router': '172.31.197.253',
                                                            'lsa_id': '10.22.102.57',
                                                            'ospfv2': 
                                                                {'header': 
                                                                    {'adv_router': '172.31.197.253',
                                                                    'age': 2641,
                                                                    'checksum': '0x0062F8',
                                                                    'lsa_id': '10.22.102.57',
                                                                    'seq_num': '0x80000041'}}}}}}}}}}}}}}}}

    golden_output1 = {'execute.return_value': '''
        Router#show ip ospf database
        Load for five secs: 71%/0%; one minute: 11%; five minutes: 9%
        Time source is NTP, 20:29:26.348 EST Fri Nov 11 2016


                    OSPF Router with ID (172.31.197.254) (Process ID 65109)

                Router Link States (Area 0)

        Link ID         ADV Router      Age         Seq#       Checksum Link count
        10.22.102.64    10.22.102.64    2794        0x80000043 0x002254 3
        172.31.197.252  172.31.197.252  1802        0x80000161 0x007F23 5
        172.31.197.253  172.31.197.253  1784        0x80000103 0x00CC34 8
        172.31.197.254  172.31.197.254  1675        0x8000000C 0x007A61 3
        192.168.255.0   192.168.255.0   226         0x80000069 0x006975 501
        192.168.165.119 192.168.165.119 1089        0x80000029 0x0080E0 2
        192.168.165.120 192.168.165.120 1482        0x80000033 0x0063CB 2
        192.168.165.220 192.168.165.220 525         0x800000DE 0x004E8E 3

                Net Link States (Area 0)

        Link ID         ADV Router      Age         Seq#       Checksum
        10.1.1.2        172.31.197.253  70          0x8000003F 0x0015EF
        10.22.102.49    172.31.197.252  289         0x8000005B 0x007AD0
        10.22.102.57    172.31.197.253  2641        0x80000041 0x0062F8
        172.31.197.93   172.31.197.252  1802        0x80000008 0x002D67
        172.31.197.97   172.31.197.253  1356        0x80000006 0x000D83
        172.31.197.102  192.168.165.220 525         0x80000058 0x0094CD
        192.168.255.0   172.31.197.253  2213        0x80000BA8 0x00D374
        192.168.165.49  172.31.197.253  499         0x8000001A 0x005CBC
        192.168.165.57  172.31.197.253  927         0x80000023 0x0008FE

                    OSPF Router with ID (10.4.1.1) (Process ID 1)

                Router Link States (Area 9)

        Link ID         ADV Router      Age         Seq#       Checksum Link count
        10.4.1.1        10.4.1.1        167         0x8000000D 0x00D8C6 1
        Router#
        '''}

    golden_parsed_output2 = {
        'vrf': 
            {'default': 
                {'address_family': 
                    {'ipv4': 
                        {'instance': 
                            {'65109': 
                                {'areas': 
                                    {'0.0.0.8': 
                                        {'database': 
                                            {'lsa_types': 
                                                {1: 
                                                    {'lsa_type': 1,
                                                    'lsas': 
                                                        {'192.168.165.220': 
                                                            {'adv_router': '192.168.165.220',
                                                            'lsa_id': '192.168.165.220',
                                                            'ospfv2': 
                                                                {'header': 
                                                                    {'adv_router': '192.168.165.220',
                                                                    'age': 113,
                                                                    'checksum': '0x007C93',
                                                                    'link_count': 2,
                                                                    'lsa_id': '192.168.165.220',
                                                                    'seq_num': '0x800006E3'}}},
                                                        '192.168.255.0': 
                                                            {'adv_router': '192.168.255.0',
                                                            'lsa_id': '192.168.255.0',
                                                            'ospfv2': 
                                                                {'header': 
                                                                    {'adv_router': '192.168.255.0',
                                                                    'age': 1407,
                                                                    'checksum': '0x00ADD6',
                                                                    'link_count': 501,
                                                                    'lsa_id': '192.168.255.0',
                                                                    'seq_num': '0x800007BC'}}},
                                                        '10.22.102.64': 
                                                            {'adv_router': '10.22.102.64',
                                                            'lsa_id': '10.22.102.64',
                                                            'ospfv2': 
                                                                {'header': 
                                                                    {'adv_router': '10.22.102.64',
                                                                    'age': 2220,
                                                                    'checksum': '0x008BD8',
                                                                    'link_count': 3,
                                                                    'lsa_id': '10.22.102.64',
                                                                    'seq_num': '0x800003EC'}}},
                                                        '172.31.197.252': 
                                                            {'adv_router': '172.31.197.252',
                                                            'lsa_id': '172.31.197.252',
                                                            'ospfv2': 
                                                                {'header': 
                                                                    {'adv_router': '172.31.197.252',
                                                                    'age': 1272,
                                                                    'checksum': '0x00B9E5',
                                                                    'link_count': 6,
                                                                    'lsa_id': '172.31.197.252',
                                                                    'seq_num': '0x80000DBD'}}},
                                                        '172.31.197.253': 
                                                            {'adv_router': '172.31.197.253',
                                                            'lsa_id': '172.31.197.253',
                                                            'ospfv2': 
                                                                {'header': 
                                                                    {'adv_router': '172.31.197.253',
                                                                    'age': 663,
                                                                    'checksum': '0x00FFD8',
                                                                    'link_count': 4,
                                                                    'lsa_id': '172.31.197.253',
                                                                    'seq_num': '0x8000009D'}}},
                                                        '172.31.197.254': 
                                                            {'adv_router': '172.31.197.254',
                                                            'lsa_id': '172.31.197.254',
                                                            'ospfv2': 
                                                                {'header': 
                                                                    {'adv_router': '172.31.197.254',
                                                                    'age': 1900,
                                                                    'checksum': '0x00D029',
                                                                    'link_count': 3,
                                                                    'lsa_id': '172.31.197.254',
                                                                    'seq_num': '0x800000D9'}}}}},
                                                2: 
                                                    {'lsa_type': 2,
                                                    'lsas': 
                                                        {'192.168.255.0': 
                                                            {'adv_router': '172.31.197.252',
                                                            'lsa_id': '192.168.255.0',
                                                            'ospfv2': 
                                                                {'header': 
                                                                    {'adv_router': '172.31.197.252',
                                                                    'age': 26,
                                                                    'checksum': '0x009E8D',
                                                                    'lsa_id': '192.168.255.0',
                                                                    'seq_num': '0x800000D1'}}},
                                                        '10.22.102.50': 
                                                            {'adv_router': '10.22.102.64',
                                                            'lsa_id': '10.22.102.50',
                                                            'ospfv2': 
                                                                {'header': 
                                                                    {'adv_router': '10.22.102.64',
                                                                    'age': 220,
                                                                    'checksum': '0x003A0A',
                                                                    'lsa_id': '10.22.102.50',
                                                                    'seq_num': '0x800000AD'}}},
                                                        '10.22.102.58': 
                                                            {'adv_router': '10.22.102.64',
                                                            'lsa_id': '10.22.102.58',
                                                            'ospfv2': 
                                                                {'header': 
                                                                    {'adv_router': '10.22.102.64',
                                                                    'age': 1220,
                                                                    'checksum': '0x00E2CD',
                                                                    'lsa_id': '10.22.102.58',
                                                                    'seq_num': '0x80000038'}}},
                                                        '172.31.197.102': 
                                                            {'adv_router': '192.168.165.220',
                                                            'lsa_id': '172.31.197.102',
                                                            'ospfv2': 
                                                                {'header': 
                                                                    {'adv_router': '192.168.165.220',
                                                                    'age': 113,
                                                                    'checksum': '0x009ACA',
                                                                    'lsa_id': '172.31.197.102',
                                                                    'seq_num': '0x80000055'}}},
                                                        '172.31.197.94': 
                                                            {'adv_router': '172.31.197.254',
                                                            'lsa_id': '172.31.197.94',
                                                            'ospfv2': 
                                                                {'header': 
                                                                    {'adv_router': '172.31.197.254',
                                                                    'age': 911,
                                                                    'checksum': '0x007ACC',
                                                                    'lsa_id': '172.31.197.94',
                                                                    'seq_num': '0x80000052'}}},
                                                        '172.31.197.97': 
                                                            {'adv_router': '172.31.197.253',
                                                            'lsa_id': '172.31.197.97',
                                                            'ospfv2': 
                                                                {'header': 
                                                                    {'adv_router': '172.31.197.253',
                                                                    'age': 663,
                                                                    'checksum': '0x00AAB4',
                                                                    'lsa_id': '172.31.197.97',
                                                                    'seq_num': '0x80000037'}}}}},
                                                3: {'lsa_type': 3,
                                                    'lsas': 
                                                        {'192.168.165.119': 
                                                            {'adv_router': '172.31.197.252',
                                                            'lsa_id': '192.168.165.119',
                                                            'ospfv2': 
                                                                {'header': 
                                                                    {'adv_router': '172.31.197.252',
                                                                    'age': 1030,
                                                                    'checksum': '0x007847',
                                                                    'lsa_id': '192.168.165.119',
                                                                    'seq_num': '0x800000D4'}}},
                                                        '192.168.165.120': 
                                                            {'adv_router': '172.31.197.252',
                                                            'lsa_id': '192.168.165.120',
                                                            'ospfv2': 
                                                                {'header': 
                                                                    {'adv_router': '172.31.197.252',
                                                                    'age': 26,
                                                                    'checksum': '0x005160',
                                                                    'lsa_id': '192.168.165.120',
                                                                    'seq_num': '0x800003DE'}}},
                                                        '192.168.165.48': 
                                                            {'adv_router': '172.31.197.252',
                                                            'lsa_id': '192.168.165.48',
                                                            'ospfv2': 
                                                                {'header': 
                                                                    {'adv_router': '172.31.197.252',
                                                                    'age': 26,
                                                                    'checksum': '0x0006F6',
                                                                    'lsa_id': '192.168.165.48',
                                                                    'seq_num': '0x800003DF'}}},
                                                        '192.168.165.56': 
                                                            {'adv_router': '172.31.197.252',
                                                            'lsa_id': '192.168.165.56',
                                                            'ospfv2': 
                                                                {'header': 
                                                                    {'adv_router': '172.31.197.252',
                                                                    'age': 1779,
                                                                    'checksum': '0x00D42E',
                                                                    'lsa_id': '192.168.165.56',
                                                                    'seq_num': '0x800000D4'}}}}},
                                                4: {'lsa_type': 4,
                                                    'lsas': 
                                                        {'192.168.165.119': 
                                                            {'adv_router': '172.31.197.252',
                                                            'lsa_id': '192.168.165.119',
                                                            'ospfv2': 
                                                                {'header': 
                                                                    {'adv_router': '172.31.197.252',
                                                                    'age': 1030,
                                                                    'checksum': '0x00605F',
                                                                    'lsa_id': '192.168.165.119',
                                                                    'seq_num': '0x800000D4'}}},
                                                        '192.168.165.120': 
                                                            {'adv_router': '172.31.197.252',
                                                            'lsa_id': '192.168.165.120',
                                                            'ospfv2': 
                                                                {'header': 
                                                                    {'adv_router': '172.31.197.252',
                                                                    'age': 26,
                                                                    'checksum': '0x003978',
                                                                    'lsa_id': '192.168.165.120',
                                                                    'seq_num': '0x800003DE'}}}}}}}}}}}}}}}}

    golden_output2 = {'execute.return_value': '''
        Router#show ip ospf database
        Load for five secs: 1%/0%; one minute: 4%; five minutes: 6%
        Time source is NTP, 15:40:22.269 EST Sun Nov 6 2016


                    OSPF Router with ID (172.31.197.254) (Process ID 65109)

                Router Link States (Area 8)

        Link ID         ADV Router      Age         Seq#       Checksum Link count
        10.22.102.64    10.22.102.64    2220        0x800003EC 0x008BD8 3
        172.31.197.252  172.31.197.252  1272        0x80000DBD 0x00B9E5 6
        172.31.197.253  172.31.197.253  663         0x8000009D 0x00FFD8 4
        172.31.197.254  172.31.197.254  1900        0x800000D9 0x00D029 3
        192.168.255.0   192.168.255.0   1407        0x800007BC 0x00ADD6 501
        192.168.165.220 192.168.165.220 113         0x800006E3 0x007C93 2

                Net Link States (Area 8)

        Link ID         ADV Router      Age         Seq#       Checksum
        10.22.102.50    10.22.102.64    220         0x800000AD 0x003A0A
        10.22.102.58    10.22.102.64    1220        0x80000038 0x00E2CD
        172.31.197.94   172.31.197.254  911         0x80000052 0x007ACC
        172.31.197.97   172.31.197.253  663         0x80000037 0x00AAB4
        172.31.197.102  192.168.165.220 113         0x80000055 0x009ACA
        192.168.255.0   172.31.197.252  26           0x800000D1 0x009E8D

                Summary Net Link States (Area 8)

        Link ID         ADV Router      Age         Seq#       Checksum
        192.168.165.48  172.31.197.252  26          0x800003DF 0x0006F6
        192.168.165.56  172.31.197.252  1779        0x800000D4 0x00D42E
        192.168.165.119 172.31.197.252  1030        0x800000D4 0x007847
        192.168.165.120 172.31.197.252  26          0x800003DE 0x005160

                Summary ASB Link States (Area 8)

        Link ID         ADV Router      Age         Seq#       Checksum
        192.168.165.119 172.31.197.252  1030        0x800000D4 0x00605F
        192.168.165.120 172.31.197.252  26          0x800003DE 0x003978
        Router#
        '''}

    golden_parsed_output3 = {
        'vrf': 
            {'default': 
                {'address_family': 
                    {'ipv4': 
                        {'instance': 
                            {'65109': 
                                {'areas': 
                                    {'0.0.0.0': 
                                        {'database': 
                                            {'lsa_types': 
                                                {1: 
                                                    {'lsa_type': 1,
                                                    'lsas': 
                                                        {'192.168.101.2': 
                                                            {'adv_router': '192.168.101.2',
                                                            'lsa_id': '192.168.101.2',
                                                            'ospfv2': 
                                                                {'header': 
                                                                    {'adv_router': '192.168.101.2',
                                                                    'age': 1548,
                                                                    'checksum': '0x007D6B',
                                                                    'link_count': 501,
                                                                    'lsa_id': '192.168.101.2',
                                                                     'seq_num': '0x8000005F'}}},
                                                        '192.168.135.119': 
                                                            {'adv_router': '192.168.135.119',
                                                            'lsa_id': '192.168.135.119',
                                                            'ospfv2': 
                                                                {'header': 
                                                                    {'adv_router': '192.168.135.119',
                                                                    'age': 533,
                                                                    'checksum': '0x0090D8',
                                                                    'link_count': 2,
                                                                    'lsa_id': '192.168.135.119',
                                                                    'seq_num': '0x80000021'}}},
                                                        '192.168.135.120': 
                                                            {'adv_router': '192.168.135.120',
                                                            'lsa_id': '192.168.135.120',
                                                            'ospfv2': 
                                                                {'header': 
                                                                    {'adv_router': '192.168.135.120',
                                                                    'age': 919,
                                                                    'checksum': '0x0073C3',
                                                                    'link_count': 2,
                                                                    'lsa_id': '192.168.135.120',
                                                                    'seq_num': '0x8000002B'}}},
                                                        '192.168.135.220': 
                                                            {'adv_router': '192.168.135.220',
                                                            'lsa_id': '192.168.135.220',
                                                            'ospfv2': 
                                                                {'header': 
                                                                    {'adv_router': '192.168.135.220',
                                                                    'age': 2014,
                                                                    'checksum': '0x006085',
                                                                    'link_count': 3,
                                                                    'lsa_id': '192.168.135.220',
                                                                    'seq_num': '0x800000D5'}}},
                                                        '10.22.102.64': 
                                                            {'adv_router': '10.22.102.64',
                                                            'lsa_id': '10.22.102.64',
                                                            'ospfv2': 
                                                                {'header': 
                                                                    {'adv_router': '10.22.102.64',
                                                                    'age': 1111,
                                                                    'checksum': '0x002C4F',
                                                                    'link_count': 3,
                                                                    'lsa_id': '10.22.102.64',
                                                                    'seq_num': '0x8000003E'}}},
                                                        '192.168.178.142': 
                                                            {'adv_router': '192.168.178.142',
                                                            'lsa_id': '192.168.178.142',
                                                            'ospfv2': 
                                                                {'header': 
                                                                    {'adv_router': '192.168.178.142',
                                                                    'age': 768,
                                                                    'checksum': '0x00C5E7',
                                                                    'link_count': 5,
                                                                    'lsa_id': '192.168.178.142',
                                                                    'seq_num': '0x80000155'}}},
                                                        '192.168.198.253': 
                                                            {'adv_router': '192.168.198.253',
                                                            'lsa_id': '192.168.198.253',
                                                            'ospfv2': 
                                                                {'header': 
                                                                    {'adv_router': '192.168.198.253',
                                                                    'age': 657,
                                                                    'checksum': '0x00E328',
                                                                    'link_count': 8,
                                                                    'lsa_id': '192.168.198.253',
                                                                    'seq_num': '0x800000F8'}}},
                                                        '192.168.198.254': 
                                                            {'adv_router': '192.168.198.254',
                                                            'lsa_id': '192.168.198.254',
                                                            'ospfv2': 
                                                                {'header': 
                                                                    {'adv_router': '192.168.198.254',
                                                                    'age': 656,
                                                                    'checksum': '0x007A2A',
                                                                    'link_count': 3,
                                                                    'lsa_id': '192.168.198.254',
                                                                    'seq_num': '0x8000002F'}}}}},
                                                2: 
                                                    {'lsa_type': 2,
                                                    'lsas': 
                                                        {'192.168.101.2': 
                                                            {'adv_router': '192.168.198.253',
                                                            'lsa_id': '192.168.101.2',
                                                            'ospfv2': 
                                                                {'header': 
                                                                    {'adv_router': '192.168.198.253',
                                                                    'age': 2501,
                                                                    'checksum': '0x00DF6E',
                                                                    'lsa_id': '192.168.101.2',
                                                                    'seq_num': '0x80000BA2'}}},
                                                        '192.168.135.49': 
                                                            {'adv_router': '192.168.198.253',
                                                            'lsa_id': '192.168.135.49',
                                                            'ospfv2': 
                                                                {'header': 
                                                                    {'adv_router': '192.168.198.253',
                                                                    'age': 1006,
                                                                    'checksum': '0x0068B6',
                                                                    'lsa_id': '192.168.135.49',
                                                                    'seq_num': '0x80000014'}}},
                                                        '192.168.135.57': 
                                                            {'adv_router': '192.168.198.253',
                                                            'lsa_id': '192.168.135.57',
                                                            'ospfv2': 
                                                                {'header': 
                                                                    {'adv_router': '192.168.198.253',
                                                                    'age': 2072,
                                                                    'checksum': '0x0014F8',
                                                                    'lsa_id': '192.168.135.57',
                                                                    'seq_num': '0x8000001D'}}},
                                                        '10.22.102.49': 
                                                            {'adv_router': '192.168.178.142',
                                                            'lsa_id': '10.22.102.49',
                                                            'ospfv2': 
                                                                {'header': 
                                                                    {'adv_router': '192.168.178.142',
                                                                    'age': 1763,
                                                                    'checksum': '0x008CC7',
                                                                    'lsa_id': '10.22.102.49',
                                                                    'seq_num': '0x80000052'}}},
                                                        '10.22.102.57': 
                                                            {'adv_router': '192.168.198.253',
                                                            'lsa_id': '10.22.102.57',
                                                            'ospfv2': 
                                                                {'header': 
                                                                    {'adv_router': '192.168.198.253',
                                                                    'age': 89,
                                                                    'checksum': '0x006CF3',
                                                                    'lsa_id': '10.22.102.57',
                                                                    'seq_num': '0x8000003C'}}},
                                                        '10.1.1.2': 
                                                            {'adv_router': '192.168.198.253',
                                                            'lsa_id': '10.1.1.2',
                                                            'ospfv2': 
                                                                {'header': 
                                                                    {'adv_router': '192.168.198.253',
                                                                    'age': 547,
                                                                    'checksum': '0x0021E9',
                                                                    'lsa_id': '10.1.1.2',
                                                                    'seq_num': '0x80000039'}}},
                                                        '192.168.198.102': 
                                                            {'adv_router': '192.168.135.220',
                                                            'lsa_id': '192.168.198.102',
                                                            'ospfv2': 
                                                                {'header': 
                                                                    {'adv_router': '192.168.135.220',
                                                                    'age': 2014,
                                                                    'checksum': '0x00A6C4',
                                                                    'lsa_id': '192.168.198.102',
                                                                    'seq_num': '0x8000004F'}}},
                                                        '192.168.198.94': 
                                                            {'adv_router': '192.168.198.254',
                                                            'lsa_id': '192.168.198.94',
                                                            'ospfv2': 
                                                                {'header': 
                                                                    {'adv_router': '192.168.198.254',
                                                                    'age': 639,
                                                                    'checksum': '0x001B7C',
                                                                    'lsa_id': '192.168.198.94',
                                                                    'seq_num': '0x80000002'}}},
                                                        '192.168.198.97': 
                                                            {'adv_router': '192.168.198.253',
                                                            'lsa_id': '192.168.198.97',
                                                            'ospfv2': 
                                                                {'header': 
                                                                    {'adv_router': '192.168.198.253',
                                                                    'age': 657,
                                                                    'checksum': '0x00177E',
                                                                    'lsa_id': '192.168.198.97',
                                                                    'seq_num': '0x80000001'}}}}}}}}}}}}}}}}

    golden_output3 = {'execute.return_value': '''
        1006#show ip ospf database
        Load for five secs: 0%/0%; one minute: 0%; five minutes: 0%
        Time source is NTP, 15:51:24.610 EST Fri Nov 11 2016


                    OSPF Router with ID (192.168.178.142) (Process ID 65109)

                Router Link States (Area 0)

        Link ID         ADV Router      Age         Seq#       Checksum Link count
        10.22.102.64    10.22.102.64    1111        0x8000003E 0x002C4F 3
        192.168.178.142 192.168.178.142 768         0x80000155 0x00C5E7 5
        192.168.198.253 192.168.198.253 657         0x800000F8 0x00E328 8
        192.168.198.254 192.168.198.254 656         0x8000002F 0x007A2A 3
        192.168.101.2   192.168.101.2   1548        0x8000005F 0x007D6B 501
        192.168.135.119 192.168.135.119 533         0x80000021 0x0090D8 2
        192.168.135.120 192.168.135.120 919         0x8000002B 0x0073C3 2
        192.168.135.220 192.168.135.220 2014        0x800000D5 0x006085 3

                Net Link States (Area 0)

        Link ID         ADV Router      Age         Seq#       Checksum
        10.1.1.2        192.168.198.253 547         0x80000039 0x0021E9
        10.22.102.49    192.168.178.142 1763        0x80000052 0x008CC7
        10.22.102.57    192.168.198.253 89          0x8000003C 0x006CF3
        192.168.198.94  192.168.198.254 639         0x80000002 0x001B7C
        192.168.198.97  192.168.198.253 657         0x80000001 0x00177E
        192.168.198.102 192.168.135.220 2014        0x8000004F 0x00A6C4
        192.168.101.2   192.168.198.253 2501        0x80000BA2 0x00DF6E
        192.168.135.49  192.168.198.253 1006        0x80000014 0x0068B6
        192.168.135.57  192.168.198.253 2072        0x8000001D 0x0014F8
        1006#
        '''}

    def test_show_ip_ospf_database_full1(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output1)
        obj = ShowIpOspfDatabase(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output1)

    def test_show_ip_ospf_database_full2(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output2)
        obj = ShowIpOspfDatabase(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output2)

    def test_show_ip_ospf_database_full3(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output3)
        obj = ShowIpOspfDatabase(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output3)

    def test_show_ip_ospf_database_empty(self):
        self.maxDiff = None
        self.device = Mock(**self.empty_output)
        obj = ShowIpOspfDatabase(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()


# ============================================
# Unit test for 'show ip ospf database router'
# ============================================
class test_show_ip_ospf_database_router(unittest.TestCase):

    '''Unit test for "show ip ospf database router" '''

    device = Device(name='aDevice')
    
    empty_output = {'execute.return_value': ''}

    golden_parsed_output1 = {
        'vrf': 
            {'default': 
                {'address_family': 
                    {'ipv4': 
                        {'instance': 
                            {'1': 
                                {'areas': 
                                    {'0.0.0.0': 
                                        {'database': 
                                            {'lsa_types': 
                                                {1: 
                                                    {'lsa_type': 1,
                                                    'lsas': 
                                                        {'10.4.1.1 10.4.1.1': 
                                                            {'adv_router': '10.4.1.1',
                                                            'lsa_id': '10.4.1.1',
                                                            'ospfv2': 
                                                                {'body': 
                                                                    {'router': 
                                                                        {'links': 
                                                                            {'10.4.1.1': 
                                                                                {'link_data': '255.255.255.255',
                                                                                'link_id': '10.4.1.1',
                                                                                'num_mtid_metrics': 2,
                                                                                'topologies': 
                                                                                    {0: 
                                                                                        {'metric': 1,
                                                                                        'mt_id': 0,
                                                                                        'tos': 0},
                                                                                    32: 
                                                                                        {'metric': 1,
                                                                                        'mt_id': 32},
                                                                                    33: 
                                                                                        {'metric': 1,
                                                                                        'mt_id': 33}},
                                                                                'type': 'stub network'},
                                                                            '10.1.2.1': 
                                                                                {'link_data': '10.1.2.1',
                                                                                'link_id': '10.1.2.1',
                                                                                'num_mtid_metrics': 0,
                                                                                'topologies': 
                                                                                    {0: 
                                                                                        {'metric': 1,
                                                                                        'mt_id': 0,
                                                                                        'tos': 0}},
                                                                                'type': 'transit network'},
                                                                            '10.1.4.4': 
                                                                                {'link_data': '10.1.4.1',
                                                                                'link_id': '10.1.4.4',
                                                                                'num_mtid_metrics': 0,
                                                                                'topologies': 
                                                                                    {0: 
                                                                                        {'metric': 1,
                                                                                        'mt_id': 0,
                                                                                        'tos': 0}},
                                                                                'type': 'transit network'}},
                                                                        'num_of_links': 3}},
                                                                'header': 
                                                                    {'adv_router': '10.4.1.1',
                                                                    'age': 742,
                                                                    'checksum': '0x6228',
                                                                    'length': 60,
                                                                    'lsa_id': '10.4.1.1',
                                                                    'option': 'None',
                                                                    'option_desc': 'No TOS-capability, DC',
                                                                    'seq_num': '8000003D',
                                                                    'type': 1}}},
                                                        '10.16.2.2 10.16.2.2': 
                                                            {'adv_router': '10.16.2.2',
                                                            'lsa_id': '10.16.2.2',
                                                            'ospfv2': 
                                                                {'body': 
                                                                    {'router': 
                                                                        {'links': 
                                                                            {'10.1.2.1': 
                                                                                {'link_data': '10.1.2.2',
                                                                                'link_id': '10.1.2.1',
                                                                                'num_mtid_metrics': 0,
                                                                                'topologies': 
                                                                                    {0: 
                                                                                        {'metric': 1,
                                                                                        'mt_id': 0,
                                                                                        'tos': 0}},
                                                                                'type': 'transit network'},
                                                                            '10.2.3.3': 
                                                                                {'link_data': '10.2.3.2',
                                                                                'link_id': '10.2.3.3',
                                                                                'num_mtid_metrics': 0,
                                                                                'topologies': 
                                                                                    {0: 
                                                                                        {'metric': 1,
                                                                                        'mt_id': 0,
                                                                                        'tos': 0}},
                                                                                'type': 'transit network'},
                                                                            '10.2.4.4': 
                                                                                {'link_data': '10.2.4.2',
                                                                                'link_id': '10.2.4.4',
                                                                                'num_mtid_metrics': 0,
                                                                                'topologies': 
                                                                                    {0: {'metric': 1,
                                                                                           'mt_id': 0,
                                                                                           'tos': 0}},
                                                                                'type': 'transit network'},
                                                                            '10.16.2.2': 
                                                                                {'link_data': '255.255.255.255',
                                                                                'link_id': '10.16.2.2',
                                                                                'num_mtid_metrics': 0,
                                                                                'topologies': 
                                                                                    {0: 
                                                                                        {'metric': 1,
                                                                                        'mt_id': 0,
                                                                                        'tos': 0}},
                                                                                'type': 'stub network'}},
                                                                        'num_of_links': 4}},
                                                                'header': 
                                                                    {'adv_router': '10.16.2.2',
                                                                    'age': 1520,
                                                                    'checksum': '0x672A',
                                                                    'length': 72,
                                                                    'lsa_id': '10.16.2.2',
                                                                    'option': 'None',
                                                                    'option_desc': 'No TOS-capability, No DC',
                                                                    'seq_num': '80000013',
                                                                    'type': 1}}},
                                                        '10.36.3.3 10.36.3.3': 
                                                            {'adv_router': '10.36.3.3',
                                                            'lsa_id': '10.36.3.3',
                                                            'ospfv2': 
                                                                {'body': 
                                                                    {'router': 
                                                                        {'links': 
                                                                            {'10.2.3.3': 
                                                                                {'link_data': '10.2.3.3',
                                                                                'link_id': '10.2.3.3',
                                                                                'num_mtid_metrics': 0,
                                                                                'topologies': 
                                                                                    {0: 
                                                                                        {'metric': 1,
                                                                                        'mt_id': 0,
                                                                                        'tos': 0}},
                                                                                'type': 'transit network'},
                                                                            '10.3.4.4': 
                                                                                {'link_data': '10.3.4.3',
                                                                                'link_id': '10.3.4.4',
                                                                                'num_mtid_metrics': 0,
                                                                                'topologies': 
                                                                                    {0: 
                                                                                        {'metric': 1,
                                                                                        'mt_id': 0,
                                                                                        'tos': 0}},
                                                                                'type': 'transit network'},
                                                                            '10.36.3.3': 
                                                                                {'link_data': '255.255.255.255',
                                                                                'link_id': '10.36.3.3',
                                                                                'num_mtid_metrics': 0,
                                                                                'topologies': 
                                                                                    {0: 
                                                                                        {'metric': 1,
                                                                                        'mt_id': 0,
                                                                                        'tos': 0}},
                                                                                'type': 'stub network'}},
                                                                        'num_of_links': 3}},
                                                                'header': 
                                                                    {'adv_router': '10.36.3.3',
                                                                    'age': 235,
                                                                    'checksum': '0x75F8',
                                                                    'length': 60,
                                                                    'lsa_id': '10.36.3.3',
                                                                    'option': 'None',
                                                                    'option_desc': 'No TOS-capability, DC',
                                                                    'seq_num': '80000033',
                                                                    'type': 1}}},
                                                        '10.64.4.4 10.64.4.4': 
                                                            {'adv_router': '10.64.4.4',
                                                            'lsa_id': '10.64.4.4',
                                                            'ospfv2': 
                                                                {'body': 
                                                                    {'router': 
                                                                        {'links': 
                                                                            {'10.1.4.4': 
                                                                                {'link_data': '10.1.4.4',
                                                                                'link_id': '10.1.4.4',
                                                                                'num_mtid_metrics': 0,
                                                                                'topologies': 
                                                                                    {0: 
                                                                                        {'metric': 1,
                                                                                        'mt_id': 0,
                                                                                        'tos': 0}},
                                                                                'type': 'transit network'},
                                                                            '10.2.4.4': 
                                                                                {'link_data': '10.2.4.4',
                                                                                'link_id': '10.2.4.4',
                                                                                'num_mtid_metrics': 0,
                                                                                'topologies': 
                                                                                    {0: 
                                                                                        {'metric': 1,
                                                                                        'mt_id': 0,
                                                                                        'tos': 0}},
                                                                                'type': 'transit network'},
                                                                            '10.3.4.4': 
                                                                                {'link_data': '10.3.4.4',
                                                                                'link_id': '10.3.4.4',
                                                                                'num_mtid_metrics': 0,
                                                                                'topologies': 
                                                                                    {0: 
                                                                                        {'metric': 1,
                                                                                        'mt_id': 0,
                                                                                        'tos': 0}},
                                                                                'type': 'transit network'},
                                                                            '10.64.4.4': 
                                                                                {'link_data': '255.255.255.255',
                                                                                'link_id': '10.64.4.4',
                                                                                'num_mtid_metrics': 0,
                                                                                'topologies': 
                                                                                    {0: 
                                                                                        {'metric': 1,
                                                                                        'mt_id': 0,
                                                                                        'tos': 0}},
                                                                                'type': 'stub network'}},
                                                                        'num_of_links': 4}},
                                                                'header': 
                                                                    {'adv_router': '10.64.4.4',
                                                                    'age': 1486,
                                                                    'as_boundary_router': True,
                                                                    'checksum': '0xA57C',
                                                                    'length': 72,
                                                                    'lsa_id': '10.64.4.4',
                                                                    'option': 'None',
                                                                    'option_desc': 'No '
                                                                       'TOS-capability, '
                                                                       'DC',
                                                                    'seq_num': '80000036',
                                                                    'type': 1}}}}}}}}}},
                            '2': 
                                {'areas': 
                                    {'0.0.0.1': 
                                        {'database': 
                                            {'lsa_types': 
                                                {1: 
                                                    {'lsa_type': 1,
                                                     'lsas': 
                                                        {'10.229.11.11 10.229.11.11': 
                                                            {'adv_router': '10.229.11.11',
                                                            'lsa_id': '10.229.11.11',
                                                            'ospfv2': 
                                                                {'body': 
                                                                    {'router': 
                                                                        {'links': 
                                                                            {'10.186.5.1': 
                                                                                {'link_data': '10.186.5.1',
                                                                                'link_id': '10.186.5.1',
                                                                                'num_mtid_metrics': 0,
                                                                                'topologies': 
                                                                                    {0: 
                                                                                        {'metric': 1,
                                                                                        'mt_id': 0,
                                                                                        'tos': 0}},
                                                                                'type': 'transit network'},
                                                                            '10.151.22.22': 
                                                                                {'link_data': '0.0.0.14',
                                                                                'link_id': '10.151.22.22',
                                                                                'num_mtid_metrics': 0,
                                                                                'topologies': 
                                                                                    {0: 
                                                                                        {'metric': 111,
                                                                                        'mt_id': 0,
                                                                                        'tos': 0}},
                                                                                'type': 'another router (point-to-point)'}},
                                                                        'num_of_links': 2}},
                                                                'header': 
                                                                    {'adv_router': '10.229.11.11',
                                                                    'age': 651,
                                                                    'area_border_router': True,
                                                                    'as_boundary_router': True,
                                                                    'checksum': '0x9CE3',
                                                                    'length': 48,
                                                                    'lsa_id': '10.229.11.11',
                                                                    'option': 'None',
                                                                    'option_desc': 'No TOS-capability, DC',
                                                                    'seq_num': '8000003E',
                                                                    'type': 1}}},
                                                        '10.151.22.22 10.151.22.22': 
                                                            {'adv_router': '10.151.22.22',
                                                            'lsa_id': '10.151.22.22',
                                                            'ospfv2': 
                                                                {'body': 
                                                                    {'router': 
                                                                        {'links': 
                                                                            {'10.229.11.11': 
                                                                                {'link_data': '0.0.0.6',
                                                                                'link_id': '10.229.11.11',
                                                                                'num_mtid_metrics': 0,
                                                                                'topologies': 
                                                                                    {0: 
                                                                                        {'metric': 1,
                                                                                        'mt_id': 0,
                                                                                        'tos': 0}},
                                                                                'type': 'another router (point-to-point)'},
                                                                            '10.229.6.6': 
                                                                                {'link_data': '10.229.6.2',
                                                                                'link_id': '10.229.6.6',
                                                                                'num_mtid_metrics': 0,
                                                                                'topologies': 
                                                                                    {0: 
                                                                                        {'metric': 40,
                                                                                        'mt_id': 0,
                                                                                        'tos': 0}},
                                                                                'type': 'transit network'}},
                                                                        'num_of_links': 2}},
                                                                'header': 
                                                                    {'adv_router': '10.151.22.22',
                                                                    'age': 480,
                                                                    'area_border_router': True,
                                                                    'as_boundary_router': True,
                                                                    'checksum': '0xC41A',
                                                                    'length': 48,
                                                                    'lsa_id': '10.151.22.22',
                                                                    'option': 'None',
                                                                    'option_desc': 'No '
                                                                               'TOS-capability, '
                                                                               'No '
                                                                               'DC',
                                                                    'seq_num': '80000019',
                                                                    'type': 1}}},
                                                        '10.36.3.3 10.36.3.3': 
                                                            {'adv_router': '10.36.3.3',
                                                            'lsa_id': '10.36.3.3',
                                                            'ospfv2': 
                                                                {'body': 
                                                                    {'router': 
                                                                        {'links': 
                                                                            {'10.19.7.7': 
                                                                                {'link_data': '10.19.7.3',
                                                                                'link_id': '10.19.7.7',
                                                                                'num_mtid_metrics': 0,
                                                                                'topologies': 
                                                                                    {0: 
                                                                                        {'metric': 1,
                                                                                        'mt_id': 0,
                                                                                        'tos': 0}},
                                                                                'type': 'transit network'}},
                                                                        'num_of_links': 1}},
                                                                'header': 
                                                                    {'adv_router': '10.36.3.3',
                                                                    'age': 1128,
                                                                    'area_border_router': True,
                                                                    'as_boundary_router': True,
                                                                    'checksum': '0x5845',
                                                                    'length': 36,
                                                                    'lsa_id': '10.36.3.3',
                                                                    'option': 'None',
                                                                    'option_desc': 'No TOS-capability, DC',
                                                                    'seq_num': '80000035',
                                                                    'type': 1}}},
                                                        '10.115.55.55 10.115.55.55': 
                                                            {'adv_router': '10.115.55.55',
                                                            'lsa_id': '10.115.55.55',
                                                            'ospfv2': 
                                                                {'body': 
                                                                    {'router': 
                                                                        {'links': 
                                                                            {'10.186.5.1': 
                                                                                {'link_data': '10.186.5.5',
                                                                                'link_id': '10.186.5.1',
                                                                                'num_mtid_metrics': 0,
                                                                                'topologies': 
                                                                                    {0: 
                                                                                        {'metric': 1,
                                                                                        'mt_id': 0,
                                                                                        'tos': 0}},
                                                                                'type': 'transit network'},
                                                                            '10.115.6.6': 
                                                                                {'link_data': '10.115.6.5',
                                                                                'link_id': '10.115.6.6',
                                                                                'num_mtid_metrics': 0,
                                                                                'topologies': 
                                                                                    {0: 
                                                                                        {'metric': 30,
                                                                                        'mt_id': 0,
                                                                                        'tos': 0}},
                                                                                'type': 'transit network'},
                                                                            '10.115.55.55': 
                                                                                {'link_data': '255.255.255.255',
                                                                                'link_id': '10.115.55.55',
                                                                                'num_mtid_metrics': 0,
                                                                                'topologies': 
                                                                                    {0: 
                                                                                        {'metric': 1,
                                                                                        'mt_id': 0,
                                                                                        'tos': 0}},
                                                                                'type': 'stub network'}},
                                                                        'num_of_links': 3}},
                                                                'header': 
                                                                    {'adv_router': '10.115.55.55',
                                                                    'age': 318,
                                                                    'checksum': '0xE7BC',
                                                                    'length': 60,
                                                                    'lsa_id': '10.115.55.55',
                                                                    'option': 'None',
                                                                    'option_desc': 'No TOS-capability, DC',
                                                                    'seq_num': '80000037',
                                                                    'type': 1}}},
                                                        '10.84.66.66 10.84.66.66': 
                                                            {'adv_router': '10.84.66.66',
                                                            'lsa_id': '10.84.66.66',
                                                            'ospfv2': 
                                                                {'body': 
                                                                    {'router': 
                                                                        {'links': 
                                                                            {'10.229.6.6': 
                                                                                {'link_data': '10.229.6.6',
                                                                                'link_id': '10.229.6.6',
                                                                                'num_mtid_metrics': 0,
                                                                                'topologies': 
                                                                                    {0: 
                                                                                        {'metric': 1,
                                                                                        'mt_id': 0,
                                                                                        'tos': 0}},
                                                                                'type': 'transit network'},
                                                                            '10.115.6.6': 
                                                                                {'link_data': '10.115.6.6',
                                                                                'link_id': '10.115.6.6',
                                                                                'num_mtid_metrics': 0,
                                                                                'topologies': 
                                                                                    {0: 
                                                                                        {'metric': 30,
                                                                                        'mt_id': 0,
                                                                                        'tos': 0}},
                                                                                'type': 'transit network'},
                                                                            '10.166.7.6': 
                                                                                {'link_data': '10.166.7.6',
                                                                                'link_id': '10.166.7.6',
                                                                                'num_mtid_metrics': 0,
                                                                                'topologies': {0: {'metric': 30,
                                                                                               'mt_id': 0,
                                                                                               'tos': 0}},
                                                                                'type': 'transit '
                                                                                    'network'},
                                                                                '10.84.66.66': {'link_data': '255.255.255.255',
                                                                                'link_id': '10.84.66.66',
                                                                                'num_mtid_metrics': 0,
                                                                                'topologies': {0: {'metric': 1,
                                                                                                  'mt_id': 0,
                                                                                                  'tos': 0}},
                                                                                'type': 'stub network'}},
                                                                        'num_of_links': 4}},
                                                                'header': 
                                                                    {'adv_router': '10.84.66.66',
                                                                    'age': 520,
                                                                    'checksum': '0x1282',
                                                                    'length': 72,
                                                                    'lsa_id': '10.84.66.66',
                                                                    'option': 'None',
                                                                    'option_desc': 'No '
                                                                               'TOS-capability, '
                                                                               'DC',
                                                                    'seq_num': '8000003C',
                                                                    'type': 1}}},
                                                        '10.1.77.77 10.1.77.77': 
                                                            {'adv_router': '10.1.77.77',
                                                            'lsa_id': '10.1.77.77',
                                                            'ospfv2': 
                                                                {'body': 
                                                                    {'router': 
                                                                        {'links': 
                                                                            {'10.19.7.7': 
                                                                                {'link_data': '10.19.7.7',
                                                                                'link_id': '10.19.7.7',
                                                                                'num_mtid_metrics': 0,
                                                                                'topologies': 
                                                                                    {0: 
                                                                                        {'metric': 1,
                                                                                        'mt_id': 0,
                                                                                        'tos': 0}},
                                                                                'type': 'transit network'},
                                                                            '10.166.7.6': 
                                                                                {'link_data': '10.166.7.7',
                                                                                'link_id': '10.166.7.6',
                                                                                'num_mtid_metrics': 0,
                                                                                'topologies': 
                                                                                    {0: 
                                                                                        {'metric': 30,
                                                                                        'mt_id': 0,
                                                                                        'tos': 0}},
                                                                                'type': 'transit network'},
                                                                            '10.1.77.77': 
                                                                                {'link_data': '255.255.255.255',
                                                                                'link_id': '10.1.77.77',
                                                                                'num_mtid_metrics': 0,
                                                                                'topologies': 
                                                                                    {0: 
                                                                                        {'metric': 1,
                                                                                        'mt_id': 0,
                                                                                        'tos': 0}},
                                                                                'type': 'stub network'}},
                                                                        'num_of_links': 3}},
                                                                'header': 
                                                                    {'adv_router': '10.1.77.77',
                                                                    'age': 288,
                                                                    'checksum': '0x1379',
                                                                    'length': 60,
                                                                    'lsa_id': '10.1.77.77',
                                                                    'option': 'None',
                                                                    'option_desc': 'No TOS-capability, DC',
                                                                    'seq_num': '80000030',
                                                                    'type': 1}}}}}}}}}},
                            '3':
                                {'areas':
                                    {'0.0.0.0':
                                        {'database':
                                            {'lsa_types':
                                                {1:
                                                    {'lsa_type': 1,
                                                     'lsas':
                                                        {'10.115.11.11 10.115.11.11':
                                                            {'adv_router': '10.115.11.11',
                                                            'lsa_id': '10.115.11.11',
                                                            'ospfv2':
                                                                {'body':
                                                                    {'router':
                                                                        {'links':
                                                                            {'10.115.11.11':
                                                                                {'link_data': '255.255.255.255',
                                                                                'link_id': '10.115.11.11',
                                                                                'num_mtid_metrics': 0,
                                                                                'topologies':
                                                                                    {0:
                                                                                        {'metric': 1,
                                                                                        'mt_id': 0,
                                                                                        'tos': 0}},
                                                                                'type': 'stub network'}},
                                                                        'num_of_links': 1}},
                                                                'header':
                                                                    {'adv_router': '10.115.11.11',
                                                                    'age': 50,
                                                                    'as_boundary_router': True,
                                                                    'checksum': '0x881A',
                                                                    'length': 36,
                                                                    'lsa_id': '10.115.11.11',
                                                                    'option': 'None',
                                                                    'option_desc': 'No TOS-capability, DC',
                                                                    'seq_num': '80000001',
                                                                    'type': 1}}}}}}}},
                                    '0.0.0.11':
                                        {'database':
                                            {'lsa_types':
                                                {1:
                                                    {'lsa_type': 1,
                                                     'lsas':
                                                        {'10.115.11.11 10.115.11.11':
                                                            {'adv_router': '10.115.11.11',
                                                            'lsa_id': '10.115.11.11',
                                                            'ospfv2':
                                                                {'body':
                                                                    {'router':
                                                                        {'num_of_links': 0}},
                                                                'header':
                                                                    {'adv_router': '10.115.11.11',
                                                                    'age': 8,
                                                                    'as_boundary_router': True,
                                                                    'checksum': '0x1D1B',
                                                                    'length': 24,
                                                                    'lsa_id': '10.115.11.11',
                                                                    'option': 'None',
                                                                    'option_desc': 'No TOS-capability, DC',
                                                                    'seq_num': '80000001',
                                                                    'type': 1}}}}}}}}}}}}}}}}

    golden_output1 = {'execute.return_value': '''
        R1_ospf_xe#show ip ospf database router 

            OSPF Router with ID (10.4.1.1) (Process ID 1)

                Router Link States (Area 0)

          LS age: 742
          Options: (No TOS-capability, DC)
          LS Type: Router Links
          Link State ID: 10.4.1.1
          Advertising Router: 10.4.1.1
          LS Seq Number: 8000003D
          Checksum: 0x6228
          Length: 60
          Number of Links: 3

            Link connected to: a Stub Network
             (Link ID) Network/subnet number: 10.4.1.1
             (Link Data) Network Mask: 255.255.255.255
              Number of MTID metrics: 2
               TOS 0 Metrics: 1
               MTID 32 Metrics: 1
               MTID 33 Metrics: 1

            Link connected to: a Transit Network
             (Link ID) Designated Router address: 10.1.2.1
             (Link Data) Router Interface address: 10.1.2.1
              Number of MTID metrics: 0
               TOS 0 Metrics: 1

            Link connected to: a Transit Network
             (Link ID) Designated Router address: 10.1.4.4
             (Link Data) Router Interface address: 10.1.4.1
              Number of MTID metrics: 0
               TOS 0 Metrics: 1


          LS age: 1520
          Options: (No TOS-capability, No DC)
          LS Type: Router Links
          Link State ID: 10.16.2.2
          Advertising Router: 10.16.2.2
          LS Seq Number: 80000013
          Checksum: 0x672A
          Length: 72
          Number of Links: 4

            Link connected to: a Stub Network
             (Link ID) Network/subnet number: 10.16.2.2
             (Link Data) Network Mask: 255.255.255.255
              Number of MTID metrics: 0
               TOS 0 Metrics: 1

            Link connected to: a Transit Network
             (Link ID) Designated Router address: 10.2.3.3
             (Link Data) Router Interface address: 10.2.3.2
              Number of MTID metrics: 0
               TOS 0 Metrics: 1

            Link connected to: a Transit Network
             (Link ID) Designated Router address: 10.2.4.4
             (Link Data) Router Interface address: 10.2.4.2
              Number of MTID metrics: 0
               TOS 0 Metrics: 1

            Link connected to: a Transit Network
             (Link ID) Designated Router address: 10.1.2.1
             (Link Data) Router Interface address: 10.1.2.2
              Number of MTID metrics: 0
               TOS 0 Metrics: 1


          LS age: 235
          Options: (No TOS-capability, DC)
          LS Type: Router Links
          Link State ID: 10.36.3.3
          Advertising Router: 10.36.3.3
          LS Seq Number: 80000033
          Checksum: 0x75F8
          Length: 60
          Number of Links: 3

            Link connected to: a Stub Network
             (Link ID) Network/subnet number: 10.36.3.3
             (Link Data) Network Mask: 255.255.255.255
              Number of MTID metrics: 0
               TOS 0 Metrics: 1

            Link connected to: a Transit Network
             (Link ID) Designated Router address: 10.3.4.4
             (Link Data) Router Interface address: 10.3.4.3
              Number of MTID metrics: 0
               TOS 0 Metrics: 1

            Link connected to: a Transit Network
             (Link ID) Designated Router address: 10.2.3.3
             (Link Data) Router Interface address: 10.2.3.3
              Number of MTID metrics: 0
               TOS 0 Metrics: 1


          LS age: 1486
          Options: (No TOS-capability, DC)
          LS Type: Router Links
          Link State ID: 10.64.4.4
          Advertising Router: 10.64.4.4
          LS Seq Number: 80000036
          Checksum: 0xA57C
          Length: 72
          AS Boundary Router
          Number of Links: 4

            Link connected to: a Stub Network
             (Link ID) Network/subnet number: 10.64.4.4
             (Link Data) Network Mask: 255.255.255.255
              Number of MTID metrics: 0
               TOS 0 Metrics: 1

            Link connected to: a Transit Network
             (Link ID) Designated Router address: 10.2.4.4
             (Link Data) Router Interface address: 10.2.4.4
              Number of MTID metrics: 0
               TOS 0 Metrics: 1

            Link connected to: a Transit Network
             (Link ID) Designated Router address: 10.3.4.4
             (Link Data) Router Interface address: 10.3.4.4
              Number of MTID metrics: 0
               TOS 0 Metrics: 1

            Link connected to: a Transit Network
             (Link ID) Designated Router address: 10.1.4.4
             (Link Data) Router Interface address: 10.1.4.4
              Number of MTID metrics: 0
               TOS 0 Metrics: 1



                    OSPF Router with ID (10.229.11.11) (Process ID 2)

                        Router Link States (Area 1)
                  
          LS age: 1128
          Options: (No TOS-capability, DC)
          LS Type: Router Links
          Link State ID: 10.36.3.3
          Advertising Router: 10.36.3.3
          LS Seq Number: 80000035
          Checksum: 0x5845
          Length: 36
          Area Border Router
          AS Boundary Router
          Number of Links: 1

            Link connected to: a Transit Network
             (Link ID) Designated Router address: 10.19.7.7
             (Link Data) Router Interface address: 10.19.7.3
              Number of MTID metrics: 0
               TOS 0 Metrics: 1


          LS age: 651
          Options: (No TOS-capability, DC)
          LS Type: Router Links
          Link State ID: 10.229.11.11
          Advertising Router: 10.229.11.11
          LS Seq Number: 8000003E
          Checksum: 0x9CE3
          Length: 48
          Area Border Router
          AS Boundary Router
          Number of Links: 2

            Link connected to: another Router (point-to-point)
             (Link ID) Neighboring Router ID: 10.151.22.22
             (Link Data) Router Interface address: 0.0.0.14
              Number of MTID metrics: 0
               TOS 0 Metrics: 111

            Link connected to: a Transit Network
             (Link ID) Designated Router address: 10.186.5.1
             (Link Data) Router Interface address: 10.186.5.1
              Number of MTID metrics: 0
               TOS 0 Metrics: 1


          LS age: 480
          Options: (No TOS-capability, No DC)
          LS Type: Router Links
          Link State ID: 10.151.22.22
          Advertising Router: 10.151.22.22
          LS Seq Number: 80000019
          Checksum: 0xC41A
          Length: 48
          Area Border Router
          AS Boundary Router
          Number of Links: 2

            Link connected to: a Transit Network
             (Link ID) Designated Router address: 10.229.6.6
             (Link Data) Router Interface address: 10.229.6.2
              Number of MTID metrics: 0
               TOS 0 Metrics: 40

            Link connected to: another Router (point-to-point)
             (Link ID) Neighboring Router ID: 10.229.11.11
             (Link Data) Router Interface address: 0.0.0.6
              Number of MTID metrics: 0
               TOS 0 Metrics: 1

                  
          LS age: 318
          Options: (No TOS-capability, DC)
          LS Type: Router Links
          Link State ID: 10.115.55.55
          Advertising Router: 10.115.55.55
          LS Seq Number: 80000037
          Checksum: 0xE7BC
          Length: 60
          Number of Links: 3

            Link connected to: a Stub Network
             (Link ID) Network/subnet number: 10.115.55.55
             (Link Data) Network Mask: 255.255.255.255
              Number of MTID metrics: 0
               TOS 0 Metrics: 1

            Link connected to: a Transit Network
             (Link ID) Designated Router address: 10.115.6.6
             (Link Data) Router Interface address: 10.115.6.5
              Number of MTID metrics: 0
               TOS 0 Metrics: 30

            Link connected to: a Transit Network
             (Link ID) Designated Router address: 10.186.5.1
             (Link Data) Router Interface address: 10.186.5.5
              Number of MTID metrics: 0
               TOS 0 Metrics: 1


          LS age: 520
          Options: (No TOS-capability, DC)
          LS Type: Router Links
          Link State ID: 10.84.66.66
          Advertising Router: 10.84.66.66
          LS Seq Number: 8000003C
          Checksum: 0x1282
          Length: 72
          Number of Links: 4

            Link connected to: a Stub Network
             (Link ID) Network/subnet number: 10.84.66.66
             (Link Data) Network Mask: 255.255.255.255
              Number of MTID metrics: 0
               TOS 0 Metrics: 1

            Link connected to: a Transit Network
             (Link ID) Designated Router address: 10.166.7.6
             (Link Data) Router Interface address: 10.166.7.6
              Number of MTID metrics: 0
               TOS 0 Metrics: 30

            Link connected to: a Transit Network
             (Link ID) Designated Router address: 10.229.6.6
             (Link Data) Router Interface address: 10.229.6.6
              Number of MTID metrics: 0
               TOS 0 Metrics: 1

            Link connected to: a Transit Network
             (Link ID) Designated Router address: 10.115.6.6
             (Link Data) Router Interface address: 10.115.6.6
              Number of MTID metrics: 0
               TOS 0 Metrics: 30


          LS age: 288
          Options: (No TOS-capability, DC)
          LS Type: Router Links
          Link State ID: 10.1.77.77
          Advertising Router: 10.1.77.77
          LS Seq Number: 80000030
          Checksum: 0x1379
          Length: 60
          Number of Links: 3

            Link connected to: a Stub Network
             (Link ID) Network/subnet number: 10.1.77.77
             (Link Data) Network Mask: 255.255.255.255
              Number of MTID metrics: 0
               TOS 0 Metrics: 1

            Link connected to: a Transit Network
             (Link ID) Designated Router address: 10.166.7.6
             (Link Data) Router Interface address: 10.166.7.7
              Number of MTID metrics: 0
               TOS 0 Metrics: 30

            Link connected to: a Transit Network
             (Link ID) Designated Router address: 10.19.7.7
             (Link Data) Router Interface address: 10.19.7.7
              Number of MTID metrics: 0
               TOS 0 Metrics: 1



                    OSPF Router with ID (10.115.11.11) (Process ID 3)

                        Router Link States (Area 0)

          LS age: 50
          Options: (No TOS-capability, DC)
          LS Type: Router Links
          Link State ID: 10.115.11.11
          Advertising Router: 10.115.11.11
          LS Seq Number: 80000001
          Checksum: 0x881A
          Length: 36
          AS Boundary Router
          Number of Links: 1

            Link connected to: a Stub Network
             (Link ID) Network/subnet number: 10.115.11.11
             (Link Data) Network Mask: 255.255.255.255
              Number of MTID metrics: 0
               TOS 0 Metrics: 1



                        Router Link States (Area 11)

          LS age: 8
          Options: (No TOS-capability, DC)
          LS Type: Router Links
          Link State ID: 10.115.11.11
          Advertising Router: 10.115.11.11
          LS Seq Number: 80000001
          Checksum: 0x1D1B
          Length: 24
          AS Boundary Router
          Number of Links: 0
        '''}

    def test_show_ip_ospf_database_router_full1(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output1)
        obj = ShowIpOspfDatabaseRouter(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output1)

    def test_show_ip_ospf_database_router_empty(self):
        self.maxDiff = None
        self.device = Mock(**self.empty_output)
        obj = ShowIpOspfDatabaseRouter(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()


# ==============================================
# Unit test for 'show ip ospf database external'
# ==============================================
class test_show_ip_ospf_database_external(unittest.TestCase):

    '''Unit test for "show ip ospf database external" '''

    device = Device(name='aDevice')
    
    empty_output = {'execute.return_value': ''}

    golden_parsed_output1 = {
        'vrf': 
            {'default': 
                {'address_family': 
                    {'ipv4': 
                        {'instance': 
                            {'1': 
                                {'areas': 
                                    {'0.0.0.0': 
                                        {'database': 
                                            {'lsa_types': 
                                                {5: 
                                                    {'lsa_type': 5,
                                                    'lsas': 
                                                        {'10.94.44.44 10.64.4.4': 
                                                            {'adv_router': '10.64.4.4',
                                                            'lsa_id': '10.94.44.44',
                                                            'ospfv2': 
                                                                {'body': 
                                                                    {'external': 
                                                                        {'network_mask': '255.255.255.255',
                                                                        'topologies': 
                                                                            {0: 
                                                                                {'external_route_tag': 0,
                                                                                'flags': 'E',
                                                                                'forwarding_address': '0.0.0.0',
                                                                                'metric': 20,
                                                                                'mt_id': 0}}}},
                                                                'header': 
                                                                    {'adv_router': '10.64.4.4',
                                                                    'age': 1595,
                                                                    'checksum': '0x7F60',
                                                                    'length': 36,
                                                                    'lsa_id': '10.94.44.44',
                                                                    'option': 'None',
                                                                    'option_desc': 'No TOS-capability, DC, Upward',
                                                                        'seq_num': '80000001',
                                                                        'type': 5}}}}}}}}}},
                            '2': {}}}}}}}


    golden_output1 = {'execute.return_value': '''
        R1_ospf_xe#show ip ospf database external 

            OSPF Router with ID (10.4.1.1) (Process ID 1)

                Type-5 AS External Link States

          LS age: 1595
          Options: (No TOS-capability, DC, Upward)
          LS Type: AS External Link
          Link State ID: 10.94.44.44 (External Network Number )
          Advertising Router: 10.64.4.4
          LS Seq Number: 80000001
          Checksum: 0x7F60
          Length: 36
          Network Mask: /32
                Metric Type: 2 (Larger than any link state path)
                MTID: 0 
                Metric: 20 
                Forward Address: 0.0.0.0
                External Route Tag: 0


                    OSPF Router with ID (10.229.11.11) (Process ID 2)
        '''}

    def test_show_ip_ospf_database_external_full1(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output1)
        obj = ShowIpOspfDatabaseExternal(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output1)

    def test_show_ip_ospf_database_external_empty(self):
        self.maxDiff = None
        self.device = Mock(**self.empty_output)
        obj = ShowIpOspfDatabaseExternal(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()


# ==============================================
# Unit test for 'show ip ospf database netwwork'
# ==============================================
class test_show_ip_ospf_database_network(unittest.TestCase):

    '''Unit test for "show ip ospf database network" '''

    device = Device(name='aDevice')
    
    empty_output = {'execute.return_value': ''}

    golden_parsed_output1 = {
        'vrf': 
            {'default': 
                {'address_family': 
                    {'ipv4': 
                        {'instance': 
                            {'1': 
                                {'areas': 
                                    {'0.0.0.0': 
                                        {'database': 
                                            {'lsa_types': 
                                                {2: 
                                                    {'lsa_type': 2,
                                                    'lsas': 
                                                        {'10.1.2.1 10.4.1.1': 
                                                            {'adv_router': '10.4.1.1',
                                                            'lsa_id': '10.1.2.1',
                                                            'ospfv2': 
                                                                {'body': 
                                                                    {'network': 
                                                                        {'attached_routers': 
                                                                            {'10.4.1.1': {},
                                                                            '10.16.2.2': {}},
                                                                        'network_mask': '255.255.255.0'}},
                                                                'header': 
                                                                    {'adv_router': '10.4.1.1',
                                                                    'age': 786,
                                                                    'checksum': '0x3DD0',
                                                                    'length': 32,
                                                                    'lsa_id': '10.1.2.1',
                                                                    'option': 'None',
                                                                    'option_desc': 'No TOS-capability, DC',
                                                                    'seq_num': '8000000F',
                                                                    'type': 2}}},
                                                        '10.1.4.4 10.64.4.4': 
                                                            {'adv_router': '10.64.4.4',
                                                            'lsa_id': '10.1.4.4',
                                                            'ospfv2': 
                                                                {'body': 
                                                                    {'network': 
                                                                        {'attached_routers': 
                                                                            {'10.4.1.1': {},
                                                                            '10.64.4.4': {}},
                                                                        'network_mask': '255.255.255.0'}},
                                                                'header': 
                                                                    {'adv_router': '10.64.4.4',
                                                                    'age': 1496,
                                                                    'checksum': '0xA431',
                                                                    'length': 32,
                                                                    'lsa_id': '10.1.4.4',
                                                                    'option': 'None',
                                                                    'option_desc': 'No TOS-capability, DC',
                                                                    'seq_num': '8000002E',
                                                                    'type': 2}}},
                                                        '10.2.3.3 10.36.3.3': 
                                                            {'adv_router': '10.36.3.3',
                                                            'lsa_id': '10.2.3.3',
                                                            'ospfv2': 
                                                                {'body': 
                                                                    {'network': 
                                                                        {'attached_routers': 
                                                                            {'10.16.2.2': {},
                                                                            '10.36.3.3': {}},
                                                                        'network_mask': '255.255.255.0'}},
                                                                'header': 
                                                                    {'adv_router': '10.36.3.3',
                                                                    'age': 774,
                                                                    'checksum': '0x2ACF',
                                                                    'length': 32,
                                                                    'lsa_id': '10.2.3.3',
                                                                    'option': 'None',
                                                                    'option_desc': 'No TOS-capability, DC',
                                                                    'seq_num': '8000000F',
                                                                    'type': 2}}},
                                                        '10.2.4.4 10.64.4.4': 
                                                            {'adv_router': '10.64.4.4',
                                                            'lsa_id': '10.2.4.4',
                                                            'ospfv2': 
                                                                {'body': 
                                                                    {'network': 
                                                                        {'attached_routers': 
                                                                            {'10.16.2.2': {},
                                                                            '10.64.4.4': {}},
                                                                        'network_mask': '255.255.255.0'}},
                                                                'header': 
                                                                    {'adv_router': '10.64.4.4',
                                                                    'age': 747,
                                                                    'checksum': '0x9E6',
                                                                    'length': 32,
                                                                    'lsa_id': '10.2.4.4',
                                                                    'option': 'None',
                                                                    'option_desc': 'No '
                                                                    'TOS-capability, '
                                                                    'DC',
                                                                    'seq_num': '8000000F',
                                                                    'type': 2}}},
                                                        '10.3.4.4 10.64.4.4': 
                                                            {'adv_router': '10.64.4.4',
                                                            'lsa_id': '10.3.4.4',
                                                            'ospfv2': 
                                                                {'body': 
                                                                    {'network': 
                                                                        {'attached_routers': 
                                                                            {'10.36.3.3': {},
                                                                            '10.64.4.4': {}},
                                                                        'network_mask': '255.255.255.0'}},
                                                                'header': 
                                                                    {'adv_router': '10.64.4.4',
                                                                    'age': 992,
                                                                    'checksum': '0xF0DA',
                                                                    'length': 32,
                                                                    'lsa_id': '10.3.4.4',
                                                                    'option': 'None',
                                                                    'option_desc': 'No '
                                                                    'TOS-capability, '
                                                                    'DC',
                                                                    'seq_num': '8000002E',
                                                                    'type': 2}}}}}}}}}},
                            '2': 
                                {'areas': 
                                    {'0.0.0.1': 
                                        {'database': 
                                            {'lsa_types': 
                                                {2: 
                                                {'lsa_type': 2,
                                                'lsas': 
                                                    {'10.186.5.1 10.229.11.11': 
                                                        {'adv_router': '10.229.11.11',
                                                        'lsa_id': '10.186.5.1',
                                                        'ospfv2': 
                                                            {'body': 
                                                                {'network': 
                                                                    {'attached_routers': 
                                                                        {'10.229.11.11': {},
                                                                        '10.115.55.55': {}},
                                                                    'network_mask': '255.255.255.0'}},
                                                            'header': 
                                                                {'adv_router': '10.229.11.11',
                                                                'age': 1445,
                                                                'checksum': '0xDFD8',
                                                                'length': 32,
                                                                'lsa_id': '10.186.5.1',
                                                                'option': 'None',
                                                                'option_desc': 'No TOS-capability, DC',
                                                                'seq_num': '80000032',
                                                                'type': 2}}},
                                                    '10.229.6.6 10.84.66.66': 
                                                        {'adv_router': '10.84.66.66',
                                                        'lsa_id': '10.229.6.6',
                                                        'ospfv2': 
                                                            {'body': 
                                                                {'network': 
                                                                    {'attached_routers': 
                                                                        {'10.151.22.22': {},
                                                                        '10.84.66.66': {}},
                                                                    'network_mask': '255.255.255.0'}},
                                                            'header': 
                                                                {'adv_router': '10.84.66.66',
                                                                'age': 1073,
                                                                'checksum': '0x415E',
                                                                'length': 32,
                                                                'lsa_id': '10.229.6.6',
                                                                'option': 'None',
                                                                'option_desc': 'No TOS-capability, DC',
                                                                'seq_num': '8000000F',
                                                                'type': 2}}},
                                                    '10.19.7.7 10.1.77.77': 
                                                        {'adv_router': '10.1.77.77',
                                                        'lsa_id': '10.19.7.7',
                                                        'ospfv2': 
                                                            {'body': 
                                                                {'network': 
                                                                    {'attached_routers': 
                                                                        {'10.36.3.3': {},
                                                                        '10.1.77.77': {}},
                                                                    'network_mask': '255.255.255.0'}},
                                                            'header': 
                                                                {'adv_router': '10.1.77.77',
                                                                'age': 849,
                                                                'checksum': '0x5C19',
                                                                'length': 32,
                                                                'lsa_id': '10.19.7.7',
                                                                'option': 'None',
                                                                'option_desc': 'No TOS-capability, DC',
                                                                'seq_num': '8000002A',
                                                                'type': 2}}},
                                                    '10.115.6.6 10.84.66.66': 
                                                        {'adv_router': '10.84.66.66',
                                                        'lsa_id': '10.115.6.6',
                                                        'ospfv2': 
                                                            {'body': 
                                                                {'network': 
                                                                    {'attached_routers': 
                                                                        {'10.115.55.55': {},
                                                                        '10.84.66.66': {}},
                                                                    'network_mask': '255.255.255.0'}},
                                                            'header': 
                                                                {'adv_router': '10.84.66.66',
                                                                'age': 564,
                                                                'checksum': '0x619C',
                                                                'length': 32,
                                                                'lsa_id': '10.115.6.6',
                                                                'option': 'None',
                                                                'option_desc': 'No '
                                                                'TOS-capability, '
                                                                'DC',
                                                                'seq_num': '80000029',
                                                                'type': 2}}},
                                                    '10.166.7.6 10.84.66.66': 
                                                        {'adv_router': '10.84.66.66',
                                                        'lsa_id': '10.166.7.6',
                                                        'ospfv2': 
                                                            {'body': 
                                                                {'network': 
                                                                    {'attached_routers': 
                                                                        {'10.84.66.66': {},
                                                                        '10.1.77.77': {}},
                                                                    'network_mask': '255.255.255.0'}},
                                                            'header': 
                                                                {'adv_router': '10.84.66.66',
                                                                'age': 1845,
                                                                'checksum': '0x980A',
                                                                'length': 32,
                                                                'lsa_id': '10.166.7.6',
                                                                'option': 'None',
                                                                'option_desc': 'No TOS-capability, DC',
                                                                'seq_num': '8000002A',
                                                                'type': 2}}}}}}}}}}}}}}}}

    golden_output1 = {'execute.return_value': '''
        R1_ospf_xe#show ip ospf database network 

            OSPF Router with ID (10.4.1.1) (Process ID 1)

                Net Link States (Area 0)

          LS age: 786
          Options: (No TOS-capability, DC)
          LS Type: Network Links
          Link State ID: 10.1.2.1 (address of Designated Router)
          Advertising Router: 10.4.1.1
          LS Seq Number: 8000000F
          Checksum: 0x3DD0
          Length: 32
          Network Mask: /24
                Attached Router: 10.4.1.1
                Attached Router: 10.16.2.2

          LS age: 1496
          Options: (No TOS-capability, DC)
          LS Type: Network Links
          Link State ID: 10.1.4.4 (address of Designated Router)
          Advertising Router: 10.64.4.4
          LS Seq Number: 8000002E
          Checksum: 0xA431
          Length: 32
          Network Mask: /24
                Attached Router: 10.64.4.4
                Attached Router: 10.4.1.1

          LS age: 774
          Options: (No TOS-capability, DC)
          LS Type: Network Links
          Link State ID: 10.2.3.3 (address of Designated Router)
          Advertising Router: 10.36.3.3
          LS Seq Number: 8000000F
          Checksum: 0x2ACF
          Length: 32
          Network Mask: /24
                Attached Router: 10.16.2.2
                Attached Router: 10.36.3.3

          LS age: 747
          Options: (No TOS-capability, DC)
          LS Type: Network Links
          Link State ID: 10.2.4.4 (address of Designated Router)
          Advertising Router: 10.64.4.4
          LS Seq Number: 8000000F
          Checksum: 0x9E6
          Length: 32
          Network Mask: /24
                Attached Router: 10.64.4.4
                Attached Router: 10.16.2.2

          LS age: 992
          Options: (No TOS-capability, DC)
          LS Type: Network Links
          Link State ID: 10.3.4.4 (address of Designated Router)
          Advertising Router: 10.64.4.4
          LS Seq Number: 8000002E
          Checksum: 0xF0DA
          Length: 32
          Network Mask: /24
                Attached Router: 10.64.4.4
                Attached Router: 10.36.3.3


                    OSPF Router with ID (10.229.11.11) (Process ID 2)

                        Net Link States (Area 1)
                  
          LS age: 1445
          Options: (No TOS-capability, DC)
          LS Type: Network Links
          Link State ID: 10.186.5.1 (address of Designated Router)
          Advertising Router: 10.229.11.11
          LS Seq Number: 80000032
          Checksum: 0xDFD8
          Length: 32
          Network Mask: /24
                Attached Router: 10.229.11.11
                Attached Router: 10.115.55.55

          LS age: 1073
          Options: (No TOS-capability, DC)
          LS Type: Network Links
          Link State ID: 10.229.6.6 (address of Designated Router)
          Advertising Router: 10.84.66.66
          LS Seq Number: 8000000F
          Checksum: 0x415E
          Length: 32
          Network Mask: /24
                Attached Router: 10.84.66.66
                Attached Router: 10.151.22.22

          LS age: 849
          Options: (No TOS-capability, DC)
          LS Type: Network Links
          Link State ID: 10.19.7.7 (address of Designated Router)
          Advertising Router: 10.1.77.77
          LS Seq Number: 8000002A
          Checksum: 0x5C19
          Length: 32
          Network Mask: /24
                Attached Router: 10.1.77.77
                Attached Router: 10.36.3.3

          LS age: 564
          Options: (No TOS-capability, DC)
          LS Type: Network Links
          Link State ID: 10.115.6.6 (address of Designated Router)
          Advertising Router: 10.84.66.66
          LS Seq Number: 80000029
          Checksum: 0x619C
          Length: 32
          Network Mask: /24
                Attached Router: 10.84.66.66
                Attached Router: 10.115.55.55

          LS age: 1845
          Options: (No TOS-capability, DC)
          LS Type: Network Links
          Link State ID: 10.166.7.6 (address of Designated Router)
          Advertising Router: 10.84.66.66
          LS Seq Number: 8000002A
          Checksum: 0x980A
          Length: 32
          Network Mask: /24
                Attached Router: 10.84.66.66
                Attached Router: 10.1.77.77
        '''}

    def test_show_ip_ospf_database_network_full1(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output1)
        obj = ShowIpOspfDatabaseNetwork(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output1)

    def test_show_ip_ospf_database_network_empty(self):
        self.maxDiff = None
        self.device = Mock(**self.empty_output)
        obj = ShowIpOspfDatabaseNetwork(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()


# ==============================================
# Unit test for 'show ip ospf database summary'
# ==============================================
class test_show_ip_ospf_database_summary(unittest.TestCase):

    '''Unit test for "show ip ospf database summary" '''

    device = Device(name='aDevice')
    
    empty_output = {'execute.return_value': ''}

    golden_parsed_output1 = {
        'vrf': 
            {'default': 
                {'address_family': 
                    {'ipv4': 
                        {'instance': 
                            {'1': 
                                {'areas': 
                                    {'0.0.0.0': 
                                        {'database': 
                                            {'lsa_types': 
                                                {3: 
                                                    {'lsa_type': 3,
                                                    'lsas': 
                                                        {'10.186.3.0 10.4.1.1': 
                                                            {'adv_router': '10.4.1.1',
                                                            'lsa_id': '10.186.3.0',
                                                            'ospfv2': 
                                                                {'body': 
                                                                    {'summary': 
                                                                        {'network_mask': '255.255.255.0',
                                                                        'topologies': 
                                                                            {0: 
                                                                                {'metric': 1,
                                                                                'mt_id': 0}}}},
                                                                'header': 
                                                                    {'adv_router': '10.4.1.1',
                                                                    'age': 422,
                                                                    'checksum': '0x43DC',
                                                                    'length': 28,
                                                                    'lsa_id': '10.186.3.0',
                                                                    'option': 'None',
                                                                    'option_desc': 'No TOS-capability, DC, Upward',
                                                                    'seq_num': '80000001',
                                                                    'type': 3}}},
                                                        '10.186.3.0 10.36.3.3': 
                                                            {'adv_router': '10.36.3.3',
                                                            'lsa_id': '10.186.3.0',
                                                            'ospfv2': 
                                                                {'body': 
                                                                    {'summary': 
                                                                        {'network_mask': '255.255.255.0',
                                                                        'topologies': 
                                                                            {0: 
                                                                                {'metric': 40,
                                                                                'mt_id': 0}}}},
                                                                'header': 
                                                                    {'adv_router': '10.36.3.3',
                                                                    'age': 372,
                                                                    'checksum': '0x6EA1',
                                                                    'length': 28,
                                                                    'lsa_id': '10.186.3.0',
                                                                    'option': 'None',
                                                                    'option_desc': 'No TOS-capability, No DC, Upward',
                                                                    'seq_num': '80000002',
                                                                    'type': 3}}},
                                                        '10.229.3.0 10.36.3.3': 
                                                            {'adv_router': '10.36.3.3',
                                                            'lsa_id': '10.229.3.0',
                                                            'ospfv2': 
                                                                {'body': 
                                                                    {'summary': 
                                                                        {'network_mask': '255.255.255.0',
                                                                        'topologies': 
                                                                            {0: 
                                                                                {'metric': 40,
                                                                                'mt_id': 0}}}},
                                                                'header': 
                                                                    {'adv_router': '10.36.3.3',
                                                                    'age': 372,
                                                                    'checksum': '0x62AC',
                                                                    'length': 28,
                                                                    'lsa_id': '10.229.3.0',
                                                                    'option': 'None',
                                                                    'option_desc': 'No TOS-capability, No DC, Upward',
                                                                    'seq_num': '80000002',
                                                                    'type': 3}}},
                                                        '10.229.4.0 10.36.3.3': 
                                                            {'adv_router': '10.36.3.3',
                                                            'lsa_id': '10.229.4.0',
                                                            'ospfv2': 
                                                                {'body': 
                                                                    {'summary': 
                                                                        {'network_mask': '255.255.255.0',
                                                                        'topologies': 
                                                                            {0: 
                                                                                {'metric': 41,
                                                                                'mt_id': 0}}}},
                                                                'header': 
                                                                    {'adv_router': '10.36.3.3',
                                                                    'age': 131,
                                                                    'checksum': '0x5DAD',
                                                                    'length': 28,
                                                                    'lsa_id': '10.229.4.0',
                                                                    'option': 'None',
                                                                    'option_desc': 'No TOS-capability, No DC, Upward',
                                                                    'seq_num': '80000004',
                                                                    'type': 3}}},
                                                        '10.19.4.0 10.36.3.3': 
                                                            {'adv_router': '10.36.3.3',
                                                            'lsa_id': '10.19.4.0',
                                                            'ospfv2': 
                                                                {'body': 
                                                                    {'summary': 
                                                                        {'network_mask': '255.255.255.0',
                                                                        'topologies': 
                                                                            {0: 
                                                                                {'metric': 40,
                                                                                'mt_id': 0}}}},
                                                                'header': 
                                                                    {'adv_router': '10.36.3.3',
                                                                    'age': 372,
                                                                    'checksum': '0x4BC1',
                                                                    'length': 28,
                                                                    'lsa_id': '10.19.4.0',
                                                                    'option': 'None',
                                                                    'option_desc': 'No TOS-capability, No DC, Upward',
                                                                    'seq_num': '80000002',
                                                                    'type': 3}}},
                                                        '10.64.4.4 10.36.3.3': 
                                                            {'adv_router': '10.36.3.3',
                                                            'lsa_id': '10.64.4.4',
                                                            'ospfv2': 
                                                                {'body': 
                                                                    {'summary': 
                                                                        {'network_mask': '255.255.255.255',
                                                                        'topologies': 
                                                                            {0: 
                                                                                {'metric': 41,
                                                                                'mt_id': 0}}}},
                                                                'header': 
                                                                    {'adv_router': '10.36.3.3',
                                                                    'age': 131,
                                                                    'checksum': '0xEF26',
                                                                    'length': 28,
                                                                    'lsa_id': '10.64.4.4',
                                                                    'option': 'None',
                                                                    'option_desc': 'No TOS-capability, No DC, Upward',
                                                                    'seq_num': '80000003',
                                                                    'type': 3}}}}}}}},
                                    '0.0.0.1': 
                                        {'database': 
                                            {'lsa_types': 
                                                {3: 
                                                    {'lsa_type': 3,
                                                    'lsas': 
                                                        {'10.4.0.0 10.4.1.1': 
                                                            {'adv_router': '10.4.1.1',
                                                            'lsa_id': '10.4.0.0',
                                                            'ospfv2': 
                                                                {'body': 
                                                                    {'summary': 
                                                                        {'network_mask': '255.255.0.0',
                                                                        'topologies': 
                                                                            {0: 
                                                                                {'metric': 10,
                                                                                'mt_id': 0}}}},
                                                                'header': 
                                                                    {'adv_router': '10.4.1.1',
                                                                    'age': 424,
                                                                    'checksum': '0x5CCA',
                                                                    'length': 28,
                                                                    'lsa_id': '10.4.0.0',
                                                                    'option': 'None',
                                                                    'option_desc': 'No TOS-capability, DC, Upward',
                                                                    'seq_num': '80000001',
                                                                    'type': 3}}},
                                                        '10.1.2.0 10.4.1.1': 
                                                            {'adv_router': '10.4.1.1',
                                                            'lsa_id': '10.1.2.0',
                                                            'ospfv2': 
                                                                {'body': 
                                                                    {'summary': 
                                                                        {'network_mask': '255.255.255.0',
                                                                        'topologies': 
                                                                            {0: 
                                                                                {'metric': 111,
                                                                                'mt_id': 0}}}},
                                                                'header': 
                                                                    {'adv_router': '10.4.1.1',
                                                                    'age': 422,
                                                                    'checksum': '0xC6EF',
                                                                    'length': 28,
                                                                    'lsa_id': '10.1.2.0',
                                                                    'option': 'None',
                                                                    'option_desc': 'No '
                                                                                'TOS-capability, '
                                                                                'DC, '
                                                                                'Upward',
                                                                    'seq_num': '80000001',
                                                                    'type': 3}}},
                                                        '10.1.3.0 10.4.1.1': 
                                                            {'adv_router': '10.4.1.1',
                                                            'lsa_id': '10.1.3.0',
                                                            'ospfv2': 
                                                                {'body': 
                                                                    {'summary': 
                                                                        {'network_mask': '255.255.255.0',
                                                                        'topologies': 
                                                                            {0: 
                                                                                {'metric': 65535,
                                                                                'mt_id': 0}}}},
                                                                'header': 
                                                                    {'adv_router': '10.4.1.1',
                                                                    'age': 364,
                                                                    'checksum': '0x5FC4',
                                                                    'length': 28,
                                                                    'lsa_id': '10.1.3.0',
                                                                    'option': 'None',
                                                                    'option_desc': 'No '
                                                                    'TOS-capability, '
                                                                    'DC, '
                                                                    'Upward',
                                                                    'seq_num': '80000002',
                                                                    'type': 3}}},
                                                        '10.2.3.0 10.4.1.1': 
                                                            {'adv_router': '10.4.1.1',
                                                            'lsa_id': '10.2.3.0',
                                                            'ospfv2': 
                                                                {'body':    
                                                                    {'summary': 
                                                                        {'network_mask': '255.255.255.0',
                                                                        'topologies': 
                                                                            {0: 
                                                                                {'metric': 65868,
                                                                                'mt_id': 0}}}},
                                                                'header': 
                                                                    {'adv_router': '10.4.1.1',
                                                                    'age': 365,
                                                                    'checksum': '0x6174',
                                                                    'length': 28,
                                                                    'lsa_id': '10.2.3.0',
                                                                    'option': 'None',
                                                                    'option_desc': 'No TOS-capability, DC, Upward',
                                                                    'seq_num': '80000001',
                                                                    'type': 3}}},
                                                        '10.229.3.0 10.4.1.1': 
                                                            {'adv_router': '10.4.1.1',
                                                            'lsa_id': '10.229.3.0',
                                                            'ospfv2': 
                                                                {'body': 
                                                                    {'summary': 
                                                                        {'network_mask': '255.255.255.0',
                                                                        'topologies': 
                                                                            {0: 
                                                                                {'metric': 65575,
                                                                                'mt_id': 0}}}},
                                                                'header': 
                                                                    {'adv_router': '10.4.1.1',
                                                                    'age': 365,
                                                                    'checksum': '0x628F',
                                                                    'length': 28,
                                                                    'lsa_id': '10.229.3.0',
                                                                    'option': 'None',
                                                                    'option_desc': 'No TOS-capability, DC, Upward',
                                                                    'seq_num': '80000001',
                                                                    'type': 3}}},
                                                        '10.229.4.0 10.4.1.1': 
                                                            {'adv_router': '10.4.1.1',
                                                            'lsa_id': '10.229.4.0',
                                                            'ospfv2': 
                                                                {'body': 
                                                                    {'summary': 
                                                                        {'network_mask': '255.255.255.0',
                                                                        'topologies': 
                                                                            {0: 
                                                                                {'metric': 65576,
                                                                                'mt_id': 0}}}},
                                                                'header': 
                                                                    {'adv_router': '10.4.1.1',
                                                                    'age': 130,
                                                                    'checksum': '0x5D90',
                                                                    'length': 28,
                                                                    'lsa_id': '10.229.4.0',
                                                                    'option': 'None',
                                                                    'option_desc': 'No TOS-capability, DC, Upward',
                                                                    'seq_num': '80000003',
                                                                    'type': 3}}},
                                                        '10.19.4.0 10.4.1.1': 
                                                            {'adv_router': '10.4.1.1',
                                                            'lsa_id': '10.19.4.0',
                                                            'ospfv2': 
                                                                {'body': 
                                                                    {'summary': 
                                                                        {'network_mask': '255.255.255.0',
                                                                        'topologies': 
                                                                            {0: 
                                                                                {'metric': 65575,
                                                                                'mt_id': 0}}}},
                                                                'header': 
                                                                    {'adv_router': '10.4.1.1',
                                                                    'age': 365,
                                                                    'checksum': '0x4BA4',
                                                                    'length': 28,
                                                                    'lsa_id': '10.19.4.0',
                                                                    'option': 'None',
                                                                    'option_desc': 'No TOS-capability, DC, Upward',
                                                                    'seq_num': '80000001',
                                                                    'type': 3}}},
                                                        '10.36.3.3 10.4.1.1': 
                                                            {'adv_router': '10.4.1.1',
                                                            'lsa_id': '10.36.3.3',
                                                            'ospfv2': 
                                                                {'body': 
                                                                    {'summary': 
                                                                        {'network_mask': '255.255.255.255',
                                                                        'topologies': 
                                                                            {0: 
                                                                                {'metric': 65536,
                                                                                'mt_id': 0}}}},
                                                                'header': 
                                                                    {'adv_router': '10.4.1.1',
                                                                    'age': 365,
                                                                    'checksum': '0x8E97',
                                                                    'length': 28,
                                                                    'lsa_id': '10.36.3.3',
                                                                    'option': 'None',
                                                                    'option_desc': 'No TOS-capability, DC, Upward',
                                                                    'seq_num': '80000001',
                                                                    'type': 3}}},
                                                        '10.64.4.4 10.4.1.1': 
                                                            {'adv_router': '10.4.1.1',
                                                            'lsa_id': '10.64.4.4',
                                                            'ospfv2': 
                                                                {'body': 
                                                                    {'summary': 
                                                                        {'network_mask': '255.255.255.255',
                                                                        'topologies': 
                                                                            {0: 
                                                                                {'metric': 65576,
                                                                                'mt_id': 0}}}},
                                                                'header': 
                                                                    {'adv_router': '10.4.1.1',
                                                                    'age': 130,
                                                                    'checksum': '0xEF09',
                                                                    'length': 28,
                                                                    'lsa_id': '10.64.4.4',
                                                                    'option': 'None',
                                                                    'option_desc': 'No TOS-capability, DC, Upward',
                                                                    'seq_num': '80000002',
                                                                    'type': 3}}}}}}}}}}}}}}}}

    golden_output1 = {'execute.return_value': '''
        R1_ospf_xe#show ip ospf database summary 

            OSPF Router with ID (10.4.1.1) (Process ID 1)

                Summary Net Link States (Area 0)

          LS age: 131
          Options: (No TOS-capability, No DC, Upward)
          LS Type: Summary Links(Network)
          Link State ID: 10.64.4.4 (summary Network Number)
          Advertising Router: 10.36.3.3
          LS Seq Number: 80000003
          Checksum: 0xEF26
          Length: 28
          Network Mask: /32
                MTID: 0         Metric: 41 

          LS age: 422
          Options: (No TOS-capability, DC, Upward)
          LS Type: Summary Links(Network)
          Link State ID: 10.186.3.0 (summary Network Number)
          Advertising Router: 10.4.1.1
          LS Seq Number: 80000001
          Checksum: 0x43DC
          Length: 28
          Network Mask: /24
                MTID: 0         Metric: 1 

          LS age: 372
          Options: (No TOS-capability, No DC, Upward)
          LS Type: Summary Links(Network)
          Link State ID: 10.186.3.0 (summary Network Number)
          Advertising Router: 10.36.3.3
          LS Seq Number: 80000002
          Checksum: 0x6EA1
          Length: 28
          Network Mask: /24
                MTID: 0         Metric: 40 

          LS age: 372
          Options: (No TOS-capability, No DC, Upward)
          LS Type: Summary Links(Network)
          Link State ID: 10.229.3.0 (summary Network Number)
          Advertising Router: 10.36.3.3
          LS Seq Number: 80000002
          Checksum: 0x62AC
          Length: 28
          Network Mask: /24
                MTID: 0         Metric: 40 

          LS age: 131
          Options: (No TOS-capability, No DC, Upward)
          LS Type: Summary Links(Network)
          Link State ID: 10.229.4.0 (summary Network Number)
          Advertising Router: 10.36.3.3
          LS Seq Number: 80000004
          Checksum: 0x5DAD
          Length: 28
          Network Mask: /24
                MTID: 0         Metric: 41 

          LS age: 372
          Options: (No TOS-capability, No DC, Upward)
          LS Type: Summary Links(Network)
          Link State ID: 10.19.4.0 (summary Network Number)
          Advertising Router: 10.36.3.3
          LS Seq Number: 80000002
          Checksum: 0x4BC1
          Length: 28
          Network Mask: /24
                MTID: 0         Metric: 40 


                        Summary Net Link States (Area 1)

          LS age: 424
          Options: (No TOS-capability, DC, Upward)
          LS Type: Summary Links(Network)
          Link State ID: 10.4.0.0 (summary Network Number)
          Advertising Router: 10.4.1.1
          LS Seq Number: 80000001
          Checksum: 0x5CCA
          Length: 28
          Network Mask: /16
                MTID: 0         Metric: 10 

          LS age: 365
          Options: (No TOS-capability, DC, Upward)
          LS Type: Summary Links(Network)
          Link State ID: 10.36.3.3 (summary Network Number)
          Advertising Router: 10.4.1.1
          LS Seq Number: 80000001
          Checksum: 0x8E97
          Length: 28
          Network Mask: /32
                MTID: 0         Metric: 65536 

          LS age: 130
          Options: (No TOS-capability, DC, Upward)
          LS Type: Summary Links(Network)
          Link State ID: 10.64.4.4 (summary Network Number)
          Advertising Router: 10.4.1.1
          LS Seq Number: 80000002
          Checksum: 0xEF09
          Length: 28
          Network Mask: /32
                MTID: 0         Metric: 65576 

          LS age: 422
          Options: (No TOS-capability, DC, Upward)
          LS Type: Summary Links(Network)
          Link State ID: 10.1.2.0 (summary Network Number)
          Advertising Router: 10.4.1.1
          LS Seq Number: 80000001
          Checksum: 0xC6EF
          Length: 28
          Network Mask: /24
                MTID: 0         Metric: 111 

          LS age: 364
          Options: (No TOS-capability, DC, Upward)
          LS Type: Summary Links(Network)
          Link State ID: 10.1.3.0 (summary Network Number)
          Advertising Router: 10.4.1.1
          LS Seq Number: 80000002
          Checksum: 0x5FC4
          Length: 28
          Network Mask: /24
                MTID: 0         Metric: 65535 

          LS age: 365
          Options: (No TOS-capability, DC, Upward)
          LS Type: Summary Links(Network)
          Link State ID: 10.2.3.0 (summary Network Number)
          Advertising Router: 10.4.1.1
          LS Seq Number: 80000001
          Checksum: 0x6174
          Length: 28
          Network Mask: /24
                MTID: 0         Metric: 65868 

          LS age: 365
          Options: (No TOS-capability, DC, Upward)
          LS Type: Summary Links(Network)
          Link State ID: 10.229.3.0 (summary Network Number)
          Advertising Router: 10.4.1.1
          LS Seq Number: 80000001
          Checksum: 0x628F
          Length: 28
          Network Mask: /24
                MTID: 0         Metric: 65575 

          LS age: 130
          Options: (No TOS-capability, DC, Upward)
          LS Type: Summary Links(Network)
          Link State ID: 10.229.4.0 (summary Network Number)
          Advertising Router: 10.4.1.1
          LS Seq Number: 80000003
          Checksum: 0x5D90
          Length: 28
          Network Mask: /24
                MTID: 0         Metric: 65576 
                  
          LS age: 365
          Options: (No TOS-capability, DC, Upward)
          LS Type: Summary Links(Network)
          Link State ID: 10.19.4.0 (summary Network Number)
          Advertising Router: 10.4.1.1
          LS Seq Number: 80000001
          Checksum: 0x4BA4
          Length: 28
          Network Mask: /24
                MTID: 0         Metric: 65575 
        '''}

    def test_show_ip_ospf_database_summary_full1(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output1)
        obj = ShowIpOspfDatabaseSummary(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output1)

    def test_show_ip_ospf_database_summary_empty(self):
        self.maxDiff = None
        self.device = Mock(**self.empty_output)
        obj = ShowIpOspfDatabaseSummary(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()


# =================================================
# Unit test for 'show ip ospf database opaque-area'
# =================================================
class test_show_ip_ospf_database_opaque_area(unittest.TestCase):

    '''Unit test for commands:
        * 'show ip ospf database opaque-area'
        * 'show ip ospf database opaque-area self-originate'
        * 'show ip ospf database opaque-area adv-router {address}'
    '''

    device = Device(name='aDevice')
    
    empty_output = {'execute.return_value': ''}

    golden_parsed_output1 = {
        'vrf': 
            {'default': 
                {'address_family': 
                    {'ipv4': 
                        {'instance': 
                            {'1': 
                                {'areas': 
                                    {'0.0.0.0': 
                                        {'database': 
                                            {'lsa_types': 
                                                {10: 
                                                    {'lsa_type': 10,
                                                    'lsas': 
                                                        {'10.1.0.0 10.4.1.1': 
                                                            {'adv_router': '10.4.1.1',
                                                            'lsa_id': '10.1.0.0',
                                                            'ospfv2': 
                                                                {'body': 
                                                                    {'opaque': 
                                                                        {'num_of_links': 0,
                                                                         'mpls_te_router_id': '10.4.1.1',}},
                                                                'header': 
                                                                    {'adv_router': '10.4.1.1',
                                                                    'age': 370,
                                                                    'checksum': '0x56D2',
                                                                    'fragment_number': 0,
                                                                    'length': 28,
                                                                    'lsa_id': '10.1.0.0',                                                                    
                                                                    'opaque_id': 0,
                                                                    'opaque_type': 1,
                                                                    'option': 'None',
                                                                    'option_desc': 'No '
                                                                                'TOS-capability, '
                                                                                'DC',
                                                                    'seq_num': '80000002',
                                                                    'type': 10}}},
                                                        '10.1.0.0 10.16.2.2': 
                                                            {'adv_router': '10.16.2.2',
                                                            'lsa_id': '10.1.0.0',
                                                            'ospfv2': 
                                                                {'body': 
                                                                    {'opaque': 
                                                                        {'num_of_links': 0,
                                                                        'mpls_te_router_id': '10.16.2.2',}},
                                                                'header': 
                                                                    {'adv_router': '10.16.2.2',
                                                                    'age': 1420,
                                                                    'checksum': '0x1E21',
                                                                    'fragment_number': 0,
                                                                    'length': 28,
                                                                    'lsa_id': '10.1.0.0',                                                                    
                                                                    'opaque_id': 0,
                                                                    'opaque_type': 1,
                                                                    'option': 'None',
                                                                    'option_desc': 'No '
                                                                                'TOS-capability, '
                                                                                'No '
                                                                                'DC',
                                                                    'seq_num': '80000002',
                                                                    'type': 10}}},
                                                        '10.1.0.0 10.36.3.3': 
                                                            {'adv_router': '10.36.3.3',
                                                            'lsa_id': '10.1.0.0',
                                                            'ospfv2': 
                                                                {'body': 
                                                                    {'opaque': 
                                                                        {'num_of_links': 0,
                                                                         'mpls_te_router_id': '10.36.3.3',}},
                                                                'header': 
                                                                    {'adv_router': '10.36.3.3',
                                                                    'age': 123,
                                                                    'checksum': '0x5EBA',
                                                                    'fragment_number': 0,
                                                                    'length': 28,
                                                                    'lsa_id': '10.1.0.0',                                                                    
                                                                    'opaque_id': 0,
                                                                    'opaque_type': 1,
                                                                    'option': 'None',
                                                                    'option_desc': 'No '
                                                                                'TOS-capability, '
                                                                                'DC',
                                                                    'seq_num': '80000002',
                                                                    'type': 10}}},
                                                        '10.1.0.1 10.4.1.1': 
                                                            {'adv_router': '10.4.1.1',
                                                            'lsa_id': '10.1.0.1',
                                                            'ospfv2': 
                                                                {'body': 
                                                                    {'opaque': 
                                                                        {'link_tlvs': 
                                                                            {1: 
                                                                                {'admin_group': '0x0',
                                                                                'igp_metric': 1,
                                                                                'link_id': '10.1.4.4',
                                                                                'link_name': 'broadcast network',
                                                                                'link_type': 2,
                                                                                'local_if_ipv4_addrs': 
                                                                                    {'10.1.4.1': {}},
                                                                                'max_bandwidth': 125000000,
                                                                                'max_reservable_bandwidth': 93750000,
                                                                                'remote_if_ipv4_addrs': 
                                                                                    {'0.0.0.0': {}},
                                                                                'te_metric': 1,
                                                                                'total_priority': 8,
                                                                                'unreserved_bandwidths': 
                                                                                    {'0 93750000': 
                                                                                        {'priority': 0,
                                                                                        'unreserved_bandwidth': 93750000},
                                                                                    '1 93750000': 
                                                                                        {'priority': 1,
                                                                                        'unreserved_bandwidth': 93750000},
                                                                                    '2 93750000': 
                                                                                        {'priority': 2,
                                                                                        'unreserved_bandwidth': 93750000},
                                                                                    '3 93750000': 
                                                                                        {'priority': 3,
                                                                                        'unreserved_bandwidth': 93750000},
                                                                                    '4 93750000': 
                                                                                        {'priority': 4,
                                                                                        'unreserved_bandwidth': 93750000},
                                                                                    '5 93750000': 
                                                                                        {'priority': 5,
                                                                                        'unreserved_bandwidth': 93750000},
                                                                                    '6 93750000': 
                                                                                        {'priority': 6,
                                                                                        'unreserved_bandwidth': 93750000},
                                                                                    '7 93750000': 
                                                                                        {'priority': 7,
                                                                                        'unreserved_bandwidth': 93750000}}}},
                                                                        'num_of_links': 1}},
                                                                'header': 
                                                                    {'adv_router': '10.4.1.1',
                                                                    'age': 370,
                                                                    'checksum': '0x6586',
                                                                    'fragment_number': 1,
                                                                    'length': 124,
                                                                    'lsa_id': '10.1.0.1',
                                                                    'opaque_id': 1,
                                                                    'opaque_type': 1,
                                                                    'option': 'None',
                                                                    'option_desc': 'No TOS-capability, DC',
                                                                    'seq_num': '80000002',
                                                                    'type': 10}}},
                                                        '10.1.0.2 10.4.1.1': 
                                                            {'adv_router': '10.4.1.1',
                                                            'lsa_id': '10.1.0.2',
                                                            'ospfv2': 
                                                                {'body': 
                                                                    {'opaque': 
                                                                        {'link_tlvs': 
                                                                            {1: 
                                                                                {'admin_group': '0x0',
                                                                                'igp_metric': 1,
                                                                                'link_id': '10.1.2.1',
                                                                                'link_name': 'broadcast network',
                                                                                'link_type': 2,
                                                                                'local_if_ipv4_addrs': {'10.1.2.1': {}},
                                                                                'max_bandwidth': 125000000,
                                                                                'max_reservable_bandwidth': 93750000,
                                                                                'remote_if_ipv4_addrs': {'0.0.0.0': {}},
                                                                                'te_metric': 1,
                                                                                'total_priority': 8,
                                                                                'unreserved_bandwidths': 
                                                                                    {'0 93750000': 
                                                                                        {'priority': 0,
                                                                                        'unreserved_bandwidth': 93750000},
                                                                                    '1 93750000': 
                                                                                        {'priority': 1,
                                                                                        'unreserved_bandwidth': 93750000},
                                                                                    '2 93750000': 
                                                                                        {'priority': 2,
                                                                                        'unreserved_bandwidth': 93750000},
                                                                                    '3 93750000': 
                                                                                        {'priority': 3,
                                                                                        'unreserved_bandwidth': 93750000},
                                                                                    '4 93750000': 
                                                                                        {'priority': 4,
                                                                                        'unreserved_bandwidth': 93750000},
                                                                                    '5 93750000': 
                                                                                        {'priority': 5,
                                                                                        'unreserved_bandwidth': 93750000},
                                                                                    '6 93750000': 
                                                                                        {'priority': 6,
                                                                                        'unreserved_bandwidth': 93750000},
                                                                                    '7 93750000': 
                                                                                        {'priority': 7,
                                                                                        'unreserved_bandwidth': 93750000}}}},
                                                                        'num_of_links': 1}},
                                                                'header': 
                                                                    {'adv_router': '10.4.1.1',
                                                                    'age': 370,
                                                                    'checksum': '0xB43D',
                                                                    'fragment_number': 2,
                                                                    'length': 124,
                                                                    'lsa_id': '10.1.0.2',
                                                                    'opaque_id': 2,
                                                                    'opaque_type': 1,
                                                                    'option': 'None',
                                                                    'option_desc': 'No TOS-capability, DC',
                                                                    'seq_num': '80000002',
                                                                    'type': 10}}},
                                                        '10.1.0.37 10.16.2.2': 
                                                            {'adv_router': '10.16.2.2',
                                                            'lsa_id': '10.1.0.37',
                                                            'ospfv2': 
                                                                {'body': 
                                                                    {'opaque': 
                                                                        {'link_tlvs': 
                                                                            {1: 
                                                                                {'admin_group': '0x0',
                                                                                'link_id': '10.2.3.3',
                                                                                'link_name': 'broadcast network',
                                                                                'link_type': 2,
                                                                                'local_if_ipv4_addrs': {'10.2.3.2': {}},
                                                                                'max_bandwidth': 125000000,
                                                                                'max_reservable_bandwidth': 93750000,
                                                                                'remote_if_ipv4_addrs': {'0.0.0.0': {}},
                                                                                'te_metric': 1,
                                                                                'total_priority': 8,
                                                                                'unreserved_bandwidths': 
                                                                                    {'0 93750000': 
                                                                                        {'priority': 0,
                                                                                        'unreserved_bandwidth': 93750000},
                                                                                    '1 93750000': 
                                                                                        {'priority': 1,
                                                                                        'unreserved_bandwidth': 93750000},
                                                                                    '2 93750000': 
                                                                                        {'priority': 2,
                                                                                        'unreserved_bandwidth': 93750000},
                                                                                    '3 93750000': 
                                                                                        {'priority': 3,
                                                                                        'unreserved_bandwidth': 93750000},
                                                                                    '4 93750000': 
                                                                                        {'priority': 4,
                                                                                        'unreserved_bandwidth': 93750000},
                                                                                    '5 93750000': 
                                                                                        {'priority': 5,
                                                                                        'unreserved_bandwidth': 93750000},
                                                                                    '6 93750000': 
                                                                                        {'priority': 6,
                                                                                        'unreserved_bandwidth': 93750000},
                                                                                    '7 93750000': 
                                                                                        {'priority': 7,
                                                                                        'unreserved_bandwidth': 93750000}}}},
                                                                        'num_of_links': 1}},
                                                                'header': 
                                                                    {'adv_router': '10.16.2.2',
                                                                    'age': 1010,
                                                                    'checksum': '0xE691',
                                                                    'fragment_number': 37,
                                                                    'length': 116,
                                                                    'lsa_id': '10.1.0.37',
                                                                    'opaque_id': 37,
                                                                    'opaque_type': 1,
                                                                    'option': 'None',
                                                                    'option_desc': 'No TOS-capability, No DC',
                                                                    'seq_num': '80000003',
                                                                    'type': 10}}},
                                                        '10.1.0.38 10.16.2.2': 
                                                            {'adv_router': '10.16.2.2',
                                                            'lsa_id': '10.1.0.38',
                                                            'ospfv2': 
                                                                {'body': 
                                                                    {'opaque': 
                                                                        {'link_tlvs': 
                                                                            {1: 
                                                                                {'admin_group': '0x0',
                                                                                'link_id': '10.2.4.4',
                                                                                'link_name': 'broadcast network',
                                                                                'link_type': 2,
                                                                                'local_if_ipv4_addrs': 
                                                                                    {'10.2.4.2': {}},
                                                                                'max_bandwidth': 125000000,
                                                                                'max_reservable_bandwidth': 93750000,
                                                                                'remote_if_ipv4_addrs': 
                                                                                    {'0.0.0.0': {}},
                                                                                'te_metric': 1,
                                                                                'total_priority': 8,
                                                                                'unreserved_bandwidths': 
                                                                                    {'0 93750000': 
                                                                                        {'priority': 0,
                                                                                        'unreserved_bandwidth': 93750000},
                                                                                    '1 93750000': 
                                                                                        {'priority': 1,
                                                                                        'unreserved_bandwidth': 93750000},
                                                                                    '2 93750000': 
                                                                                        {'priority': 2,
                                                                                        'unreserved_bandwidth': 93750000},
                                                                                    '3 93750000': 
                                                                                        {'priority': 3,
                                                                                        'unreserved_bandwidth': 93750000},
                                                                                    '4 93750000': 
                                                                                        {'priority': 4,
                                                                                        'unreserved_bandwidth': 93750000},
                                                                                    '5 93750000': 
                                                                                        {'priority': 5,
                                                                                        'unreserved_bandwidth': 93750000},
                                                                                    '6 93750000': 
                                                                                        {'priority': 6,
                                                                                        'unreserved_bandwidth': 93750000},
                                                                                    '7 93750000': 
                                                                                        {'priority': 7,
                                                                                        'unreserved_bandwidth': 93750000}}}},
                                                                        'num_of_links': 1}},
                                                                'header': 
                                                                    {'adv_router': '10.16.2.2',
                                                                    'age': 1000,
                                                                    'checksum': '0x254F',
                                                                    'fragment_number': 38,
                                                                    'length': 116,
                                                                    'lsa_id': '10.1.0.38',
                                                                    'opaque_id': 38,
                                                                    'opaque_type': 1,
                                                                    'option': 'None',
                                                                    'option_desc': 'No TOS-capability, No DC',
                                                                    'seq_num': '80000003',
                                                                    'type': 10}}},
                                                        '10.1.0.39 10.16.2.2': 
                                                            {'adv_router': '10.16.2.2',
                                                            'lsa_id': '10.1.0.39',
                                                            'ospfv2': 
                                                                {'body': 
                                                                    {'opaque': 
                                                                        {'link_tlvs': 
                                                                            {1: 
                                                                                {'admin_group': '0x0',
                                                                                'link_id': '10.1.2.1',
                                                                                'link_name': 'broadcast network',
                                                                                'link_type': 2,
                                                                                'local_if_ipv4_addrs': 
                                                                                    {'10.1.2.2': {}},
                                                                                'max_bandwidth': 125000000,
                                                                                'max_reservable_bandwidth': 93750000,
                                                                                'remote_if_ipv4_addrs': 
                                                                                    {'0.0.0.0': {}},
                                                                                'te_metric': 1,
                                                                                'total_priority': 8,
                                                                                'unreserved_bandwidths': 
                                                                                    {'0 93750000': 
                                                                                        {'priority': 0,
                                                                                        'unreserved_bandwidth': 93750000},
                                                                                    '1 93750000': 
                                                                                        {'priority': 1,
                                                                                        'unreserved_bandwidth': 93750000},
                                                                                    '2 93750000': 
                                                                                        {'priority': 2,
                                                                                        'unreserved_bandwidth': 93750000},
                                                                                    '3 93750000': 
                                                                                        {'priority': 3,
                                                                                        'unreserved_bandwidth': 93750000},
                                                                                    '4 93750000': 
                                                                                        {'priority': 4,
                                                                                        'unreserved_bandwidth': 93750000},
                                                                                    '5 93750000': 
                                                                                        {'priority': 5,
                                                                                        'unreserved_bandwidth': 93750000},
                                                                                    '6 93750000': 
                                                                                        {'priority': 6,
                                                                                        'unreserved_bandwidth': 93750000},
                                                                                    '7 93750000': 
                                                                                        {'priority': 7,
                                                                                        'unreserved_bandwidth': 93750000}}}},
                                                                        'num_of_links': 1}},
                                                                'header': 
                                                                    {'adv_router': '10.16.2.2',
                                                                    'age': 1000,
                                                                    'checksum': '0x4438',
                                                                    'fragment_number': 39,
                                                                    'length': 116,
                                                                    'lsa_id': '10.1.0.39',
                                                                    'opaque_id': 39,
                                                                    'opaque_type': 1,
                                                                    'option': 'None',
                                                                    'option_desc': 'No TOS-capability, No DC',
                                                                    'seq_num': '80000003',
                                                                    'type': 10}}},
                                                        '10.1.0.4 10.36.3.3': 
                                                            {'adv_router': '10.36.3.3',
                                                            'lsa_id': '10.1.0.4',
                                                            'ospfv2': 
                                                                {'body': 
                                                                    {'opaque': 
                                                                        {'link_tlvs': 
                                                                            {1: 
                                                                                {'admin_group': '0x0',
                                                                                'igp_metric': 1,
                                                                                'link_id': '10.3.4.4',
                                                                                'link_name': 'broadcast network',
                                                                                'link_type': 2,
                                                                                'local_if_ipv4_addrs': {'10.3.4.3': {}},
                                                                                'max_bandwidth': 125000000,
                                                                                'max_reservable_bandwidth': 93750000,
                                                                                'remote_if_ipv4_addrs': {'0.0.0.0': {}},
                                                                                'te_metric': 1,
                                                                                'total_priority': 8,
                                                                                'unreserved_bandwidths': 
                                                                                    {'0 93750000': 
                                                                                        {'priority': 0,
                                                                                        'unreserved_bandwidth': 93750000},
                                                                                    '1 93750000': 
                                                                                        {'priority': 1,
                                                                                        'unreserved_bandwidth': 93750000},
                                                                                    '2 93750000': 
                                                                                        {'priority': 2,
                                                                                        'unreserved_bandwidth': 93750000},
                                                                                    '3 93750000': 
                                                                                        {'priority': 3,
                                                                                        'unreserved_bandwidth': 93750000},
                                                                                    '4 93750000': 
                                                                                        {'priority': 4,
                                                                                        'unreserved_bandwidth': 93750000},
                                                                                    '5 93750000': 
                                                                                        {'priority': 5,
                                                                                        'unreserved_bandwidth': 93750000},
                                                                                    '6 93750000': 
                                                                                        {'priority': 6,
                                                                                        'unreserved_bandwidth': 93750000},
                                                                                    '7 93750000': 
                                                                                        {'priority': 7,
                                                                                        'unreserved_bandwidth': 93750000}}}},
                                                                        'num_of_links': 1}},
                                                                'header': 
                                                                    {'adv_router': '10.36.3.3',
                                                                    'age': 123,
                                                                    'checksum': '0x915D',
                                                                    'fragment_number': 4,
                                                                    'length': 160,
                                                                    'lsa_id': '10.1.0.4',
                                                                    'opaque_id': 4,
                                                                    'opaque_type': 1,
                                                                    'option': 'None',
                                                                    'option_desc': 'No TOS-capability, DC',
                                                                    'seq_num': '80000002',
                                                                    'type': 10}}},
                                                        '10.1.0.6 10.36.3.3': 
                                                            {'adv_router': '10.36.3.3',
                                                            'lsa_id': '10.1.0.6',
                                                            'ospfv2': 
                                                                {'body': 
                                                                    {'opaque': 
                                                                        {'link_tlvs': 
                                                                            {1: 
                                                                                {'admin_group': '0x0',
                                                                                'igp_metric': 1,
                                                                                'link_id': '10.2.3.3',
                                                                                'link_name': 'broadcast network',
                                                                                'link_type': 2,
                                                                                'local_if_ipv4_addrs': 
                                                                                    {'10.2.3.3': {}},
                                                                                'max_bandwidth': 125000000,
                                                                                'max_reservable_bandwidth': 93750000,
                                                                                'remote_if_ipv4_addrs': {'0.0.0.0': {}},
                                                                                'te_metric': 1,
                                                                                'total_priority': 8,
                                                                                'unreserved_bandwidths': 
                                                                                    {'0 93750000': 
                                                                                        {'priority': 0,
                                                                                        'unreserved_bandwidth': 93750000},
                                                                                    '1 93750000': 
                                                                                        {'priority': 1,
                                                                                        'unreserved_bandwidth': 93750000},
                                                                                    '2 93750000': 
                                                                                        {'priority': 2,
                                                                                        'unreserved_bandwidth': 93750000},
                                                                                    '3 93750000': 
                                                                                        {'priority': 3,
                                                                                        'unreserved_bandwidth': 93750000},
                                                                                    '4 93750000': 
                                                                                        {'priority': 4,
                                                                                        'unreserved_bandwidth': 93750000},
                                                                                    '5 93750000': 
                                                                                        {'priority': 5,
                                                                                        'unreserved_bandwidth': 93750000},
                                                                                    '6 93750000': 
                                                                                        {'priority': 6,
                                                                                        'unreserved_bandwidth': 93750000},
                                                                                    '7 93750000': 
                                                                                        {'priority': 7,
                                                                                        'unreserved_bandwidth': 93750000}}}},
                                                                        'num_of_links': 1}},
                                                                'header': 
                                                                    {'adv_router': '10.36.3.3',
                                                                    'age': 123,
                                                                    'checksum': '0x5EC',
                                                                    'fragment_number': 6,
                                                                    'length': 160,
                                                                    'lsa_id': '10.1.0.6',
                                                                    'opaque_id': 6,
                                                                    'opaque_type': 1,
                                                                    'option': 'None',
                                                                    'option_desc': 'No TOS-capability, DC',
                                                                    'seq_num': '80000002',
                                                                    'type': 10}}}}}}}}}},
                            '2': {}}}}}}}

    golden_output1 = {'execute.return_value': '''
        R1_ospf_xe#show ip ospf database opaque-area 

            OSPF Router with ID (10.4.1.1) (Process ID 1)

                Type-10 Opaque Area Link States (Area 0)

          LS age: 370
          Options: (No TOS-capability, DC)
          LS Type: Opaque Area Link
          Link State ID: 10.1.0.0
          Opaque Type: 1 (Traffic Engineering)
          Opaque ID: 0
          Advertising Router: 10.4.1.1
          LS Seq Number: 80000002
          Checksum: 0x56D2
          Length: 28
          Fragment number : 0

            MPLS TE router ID : 10.4.1.1

            Number of Links : 0

          LS age: 1420
          Options: (No TOS-capability, No DC)
          LS Type: Opaque Area Link
          Link State ID: 10.1.0.0
          Opaque Type: 1 (Traffic Engineering)
          Opaque ID: 0
          Advertising Router: 10.16.2.2
          LS Seq Number: 80000002
          Checksum: 0x1E21
          Length: 28
          Fragment number : 0

            MPLS TE router ID : 10.16.2.2

            Number of Links : 0

          LS age: 123
          Options: (No TOS-capability, DC)
          LS Type: Opaque Area Link
          Link State ID: 10.1.0.0
          Opaque Type: 1 (Traffic Engineering)
          Opaque ID: 0
          Advertising Router: 10.36.3.3
          LS Seq Number: 80000002
          Checksum: 0x5EBA
          Length: 28
          Fragment number : 0

            MPLS TE router ID : 10.36.3.3

            Number of Links : 0

          LS age: 370
          Options: (No TOS-capability, DC)
          LS Type: Opaque Area Link
          Link State ID: 10.1.0.1
          Opaque Type: 1 (Traffic Engineering)
          Opaque ID: 1
          Advertising Router: 10.4.1.1
          LS Seq Number: 80000002
          Checksum: 0x6586
          Length: 124
          Fragment number : 1

            Link connected to Broadcast network
              Link ID : 10.1.4.4
              Interface Address : 10.1.4.1
              Admin Metric : 1
              Maximum bandwidth : 125000000
              Maximum reservable bandwidth : 93750000
              Number of Priority : 8
              Priority 0 : 93750000     Priority 1 : 93750000   
              Priority 2 : 93750000     Priority 3 : 93750000   
              Priority 4 : 93750000     Priority 5 : 93750000   
              Priority 6 : 93750000     Priority 7 : 93750000   
              Affinity Bit : 0x0
              IGP Metric : 1

            Number of Links : 1

          LS age: 370
          Options: (No TOS-capability, DC)
          LS Type: Opaque Area Link
          Link State ID: 10.1.0.2
          Opaque Type: 1 (Traffic Engineering)
          Opaque ID: 2
          Advertising Router: 10.4.1.1
          LS Seq Number: 80000002
          Checksum: 0xB43D
          Length: 124
          Fragment number : 2
                  
            Link connected to Broadcast network
              Link ID : 10.1.2.1
              Interface Address : 10.1.2.1
              Admin Metric : 1
              Maximum bandwidth : 125000000
              Maximum reservable bandwidth : 93750000
              Number of Priority : 8
              Priority 0 : 93750000     Priority 1 : 93750000   
              Priority 2 : 93750000     Priority 3 : 93750000   
              Priority 4 : 93750000     Priority 5 : 93750000   
              Priority 6 : 93750000     Priority 7 : 93750000   
              Affinity Bit : 0x0
              IGP Metric : 1

            Number of Links : 1

          LS age: 123
          Options: (No TOS-capability, DC)
          LS Type: Opaque Area Link
          Link State ID: 10.1.0.4
          Opaque Type: 1 (Traffic Engineering)
          Opaque ID: 4
          Advertising Router: 10.36.3.3
          LS Seq Number: 80000002
          Checksum: 0x915D
          Length: 160
          Fragment number : 4

            Link connected to Broadcast network
              Link ID : 10.3.4.4
              Interface Address : 10.3.4.3
              Admin Metric : 1
              Maximum bandwidth : 125000000
              Maximum reservable bandwidth : 93750000
              Number of Priority : 8
              Priority 0 : 93750000     Priority 1 : 93750000   
              Priority 2 : 93750000     Priority 3 : 93750000   
              Priority 4 : 93750000     Priority 5 : 93750000   
              Priority 6 : 93750000     Priority 7 : 93750000   
              Affinity Bit : 0x0
              IGP Metric : 1
              Unknown SubTLV type 32771 length 32

            Number of Links : 1

          LS age: 123
          Options: (No TOS-capability, DC)
          LS Type: Opaque Area Link
          Link State ID: 10.1.0.6
          Opaque Type: 1 (Traffic Engineering)
          Opaque ID: 6
          Advertising Router: 10.36.3.3
          LS Seq Number: 80000002
          Checksum: 0x5EC
          Length: 160
          Fragment number : 6

            Link connected to Broadcast network
              Link ID : 10.2.3.3
              Interface Address : 10.2.3.3
              Admin Metric : 1
              Maximum bandwidth : 125000000
              Maximum reservable bandwidth : 93750000
              Number of Priority : 8
              Priority 0 : 93750000     Priority 1 : 93750000   
              Priority 2 : 93750000     Priority 3 : 93750000   
              Priority 4 : 93750000     Priority 5 : 93750000   
              Priority 6 : 93750000     Priority 7 : 93750000   
              Affinity Bit : 0x0
              IGP Metric : 1
              Unknown SubTLV type 32771 length 32

            Number of Links : 1

          LS age: 1010
          Options: (No TOS-capability, No DC)
          LS Type: Opaque Area Link
          Link State ID: 10.1.0.37
          Opaque Type: 1 (Traffic Engineering)
          Opaque ID: 37
          Advertising Router: 10.16.2.2
          LS Seq Number: 80000003
          Checksum: 0xE691
          Length: 116
          Fragment number : 37

            Link connected to Broadcast network
              Link ID : 10.2.3.3
              Interface Address : 10.2.3.2
              Admin Metric : 1
              Maximum bandwidth : 125000000
              Maximum reservable bandwidth : 93750000
              Number of Priority : 8
              Priority 0 : 93750000     Priority 1 : 93750000   
              Priority 2 : 93750000     Priority 3 : 93750000   
              Priority 4 : 93750000     Priority 5 : 93750000   
              Priority 6 : 93750000     Priority 7 : 93750000   
              Affinity Bit : 0x0

            Number of Links : 1

          LS age: 1000
          Options: (No TOS-capability, No DC)
          LS Type: Opaque Area Link
          Link State ID: 10.1.0.38
          Opaque Type: 1 (Traffic Engineering)
          Opaque ID: 38
          Advertising Router: 10.16.2.2
          LS Seq Number: 80000003
          Checksum: 0x254F
          Length: 116
          Fragment number : 38

            Link connected to Broadcast network
              Link ID : 10.2.4.4
              Interface Address : 10.2.4.2
              Admin Metric : 1
              Maximum bandwidth : 125000000
              Maximum reservable bandwidth : 93750000
              Number of Priority : 8
              Priority 0 : 93750000     Priority 1 : 93750000   
              Priority 2 : 93750000     Priority 3 : 93750000   
              Priority 4 : 93750000     Priority 5 : 93750000   
              Priority 6 : 93750000     Priority 7 : 93750000   
              Affinity Bit : 0x0

            Number of Links : 1

          LS age: 1000
          Options: (No TOS-capability, No DC)
          LS Type: Opaque Area Link
          Link State ID: 10.1.0.39
          Opaque Type: 1 (Traffic Engineering)
          Opaque ID: 39
          Advertising Router: 10.16.2.2
          LS Seq Number: 80000003
          Checksum: 0x4438
          Length: 116
          Fragment number : 39

            Link connected to Broadcast network
              Link ID : 10.1.2.1
              Interface Address : 10.1.2.2
              Admin Metric : 1
              Maximum bandwidth : 125000000
              Maximum reservable bandwidth : 93750000
              Number of Priority : 8
              Priority 0 : 93750000     Priority 1 : 93750000   
              Priority 2 : 93750000     Priority 3 : 93750000   
              Priority 4 : 93750000     Priority 5 : 93750000   
              Priority 6 : 93750000     Priority 7 : 93750000   
              Affinity Bit : 0x0

            Number of Links : 1


            OSPF Router with ID (10.229.11.11) (Process ID 2)
        '''}

    golden_parsed_output2 = {
        "vrf": {
            "default": {
                "address_family": {
                    "ipv4": {
                        "instance": {
                            "65109": {
                                "areas": {
                                    "0.0.0.8": {
                                        "database": {
                                            "lsa_types": {
                                                10: {
                                                    "lsa_type": 10,
                                                    "lsas": {
                                                        "10.1.0.0 10.4.1.1": {
                                                            "adv_router": "10.4.1.1",
                                                            "lsa_id": "10.1.0.0",
                                                            "ospfv2": {
                                                                "body": {
                                                                    "opaque": {
                                                                        "mpls_te_router_id": "10.4.1.1",
                                                                        "num_of_links": 0
                                                                    }
                                                                },
                                                                "header": {
                                                                    "age": 49,
                                                                    "option": "None",
                                                                    "option_desc": "No TOS-capability, DC",
                                                                    "type": 10,
                                                                    "lsa_id": "10.1.0.0",
                                                                    "adv_router": "10.4.1.1",
                                                                    "opaque_type": 1,
                                                                    "opaque_id": 0,
                                                                    "seq_num": "80000001",
                                                                    "checksum": "0x58D1",
                                                                    "length": 28,
                                                                    "fragment_number": 0
                                                                }
                                                            }
                                                        },
                                                        "10.1.0.15 10.4.1.1": {
                                                            "adv_router": "10.4.1.1",
                                                            "lsa_id": "10.1.0.15",
                                                            "ospfv2": {
                                                                "body": {
                                                                    "opaque": {
                                                                        "link_tlvs": {
                                                                            1: {
                                                                                "link_type": 1,
                                                                                "link_name": "point-to-point network",
                                                                                "link_id": "10.16.2.2",
                                                                                "remote_if_ipv4_addrs": {
                                                                                    "192.168.220.2": {}
                                                                                },
                                                                                "local_if_ipv4_addrs": {
                                                                                    "192.168.220.1": {}
                                                                                },
                                                                                "te_metric": 1,
                                                                                "max_bandwidth": 176258176,
                                                                                "igp_metric": 1
                                                                            }
                                                                        },
                                                                        "num_of_links": 1
                                                                    }
                                                                },
                                                                "header": {
                                                                    "age": 49,
                                                                    "option": "None",
                                                                    "option_desc": "No TOS-capability, DC",
                                                                    "type": 10,
                                                                    "lsa_id": "10.1.0.15",
                                                                    "adv_router": "10.4.1.1",
                                                                    "opaque_type": 1,
                                                                    "opaque_id": 15,
                                                                    "seq_num": "80000001",
                                                                    "checksum": "0x917E",
                                                                    "length": 80,
                                                                    "fragment_number": 15
                                                                }
                                                            }
                                                        },
                                                        "10.1.0.16 10.4.1.1": {
                                                            "adv_router": "10.4.1.1",
                                                            "lsa_id": "10.1.0.16",
                                                            "ospfv2": {
                                                                "body": {
                                                                    "opaque": {
                                                                        "link_tlvs": {
                                                                            1: {
                                                                                "link_type": 1,
                                                                                "link_name": "point-to-point network",
                                                                                "link_id": "10.16.2.2",
                                                                                "remote_if_ipv4_addrs": {
                                                                                    "192.168.111.2": {}
                                                                                },
                                                                                "local_if_ipv4_addrs": {
                                                                                    "192.168.111.1": {}
                                                                                },
                                                                                "te_metric": 1,
                                                                                "max_bandwidth": 125000000,
                                                                                "igp_metric": 1
                                                                            }
                                                                        },
                                                                        "num_of_links": 1
                                                                    }
                                                                },
                                                                "header": {
                                                                    "age": 49,
                                                                    "option": "None",
                                                                    "option_desc": "No TOS-capability, DC",
                                                                    "type": 10,
                                                                    "lsa_id": "10.1.0.16",
                                                                    "adv_router": "10.4.1.1",
                                                                    "opaque_type": 1,
                                                                    "opaque_id": 16,
                                                                    "seq_num": "80000001",
                                                                    "checksum": "0x8A09",
                                                                    "length": 80,
                                                                    "fragment_number": 16
                                                                }
                                                            }
                                                        },
                                                        "10.1.0.17 10.4.1.1": {
                                                            "adv_router": "10.4.1.1",
                                                            "lsa_id": "10.1.0.17",
                                                            "ospfv2": {
                                                                "body": {
                                                                    "opaque": {
                                                                        "link_tlvs": {
                                                                            1: {
                                                                                "link_type": 1,
                                                                                "link_name": "point-to-point network",
                                                                                "link_id": "10.16.2.2",
                                                                                "remote_if_ipv4_addrs": {
                                                                                    "192.168.4.2": {}
                                                                                },
                                                                                "local_if_ipv4_addrs": {
                                                                                    "192.168.4.1": {}
                                                                                },
                                                                                "te_metric": 1,
                                                                                "max_bandwidth": 125000000,
                                                                                "igp_metric": 1
                                                                            }
                                                                        },
                                                                        "num_of_links": 1
                                                                    }
                                                                },
                                                                "header": {
                                                                    "age": 49,
                                                                    "option": "None",
                                                                    "option_desc": "No TOS-capability, DC",
                                                                    "type": 10,
                                                                    "lsa_id": "10.1.0.17",
                                                                    "adv_router": "10.4.1.1",
                                                                    "opaque_type": 1,
                                                                    "opaque_id": 17,
                                                                    "seq_num": "80000001",
                                                                    "checksum": "0xC2CD",
                                                                    "length": 80,
                                                                    "fragment_number": 17
                                                                }
                                                            }
                                                        },
                                                        "10.1.0.18 10.4.1.1": {
                                                            "adv_router": "10.4.1.1",
                                                            "lsa_id": "10.1.0.18",
                                                            "ospfv2": {
                                                                "body": {
                                                                    "opaque": {
                                                                        "link_tlvs": {
                                                                            1: {
                                                                                "link_type": 1,
                                                                                "link_name": "point-to-point network",
                                                                                "link_id": "10.16.2.2",
                                                                                "remote_if_ipv4_addrs": {
                                                                                    "192.168.154.2": {}
                                                                                },
                                                                                "local_if_ipv4_addrs": {
                                                                                    "192.168.154.1": {}
                                                                                },
                                                                                "te_metric": 1,
                                                                                "max_bandwidth": 125000000,
                                                                                "igp_metric": 1
                                                                            }
                                                                        },
                                                                        "num_of_links": 1
                                                                    }
                                                                },
                                                                "header": {
                                                                    "age": 49,
                                                                    "option": "None",
                                                                    "option_desc": "No TOS-capability, DC",
                                                                    "type": 10,
                                                                    "lsa_id": "10.1.0.18",
                                                                    "adv_router": "10.4.1.1",
                                                                    "opaque_type": 1,
                                                                    "opaque_id": 18,
                                                                    "seq_num": "80000001",
                                                                    "checksum": "0xFA92",
                                                                    "length": 80,
                                                                    "fragment_number": 18
                                                                }
                                                            }
                                                        },
                                                        "10.16.0.0 10.4.1.1": {
                                                            "adv_router": "10.4.1.1",
                                                            "lsa_id": "10.16.0.0",
                                                            "ospfv2": {
                                                                "body": {
                                                                    "opaque": {
                                                                        "router_capabilities_tlv": {
                                                                            1: {
                                                                                "tlv_type": "Router Information",
                                                                                "length": 4,
                                                                                "information_capabilities": {
                                                                                    "graceful_restart_helper": True,
                                                                                    "stub_router": True
                                                                                }
                                                                            }
                                                                        },
                                                                        "sr_algorithm_tlv": {
                                                                            1: {
                                                                                "tlv_type": "Segment Routing Algorithm",
                                                                                "length": 2,
                                                                                "algorithm": {
                                                                                    "spf": True,
                                                                                    "strict_spf": True
                                                                                }
                                                                            }
                                                                        },
                                                                        "sid_range_tlvs": {
                                                                            1: {
                                                                                "tlv_type": "Segment Routing Range",
                                                                                "length": 12,
                                                                                "range_size": 8000,
                                                                                "sub_tlvs": {
                                                                                    1: {
                                                                                        "type": "SID/Label",
                                                                                        "length": 3,
                                                                                        "label": 16000
                                                                                    }
                                                                                }
                                                                            }
                                                                        },
                                                                        "node_msd_tlvs": {
                                                                            1: {
                                                                                "tlv_type": "Segment Routing Node MSD",
                                                                                "length": 2,
                                                                                "sub_type": {
                                                                                    "node_max_sid_depth_value": 13
                                                                                }
                                                                            }
                                                                        },
                                                                        "local_block_tlvs": {
                                                                            1: {
                                                                                "tlv_type": "Segment Routing Local Block",
                                                                                "length": 12,
                                                                                "range_size": 1000,
                                                                                "sub_tlvs": {
                                                                                    1: {
                                                                                        "type": "SID/Label",
                                                                                        "length": 3,
                                                                                        "label": 15000
                                                                                    }
                                                                                }
                                                                            }
                                                                        }
                                                                    }
                                                                },
                                                                "header": {
                                                                    "age": 49,
                                                                    "option": "None",
                                                                    "option_desc": "No TOS-capability, DC",
                                                                    "type": 10,
                                                                    "lsa_id": "10.16.0.0",
                                                                    "adv_router": "10.4.1.1",
                                                                    "opaque_id": 0,
                                                                    "seq_num": "80000001",
                                                                    "checksum": "0xD28C",
                                                                    "length": 76
                                                                }
                                                            }
                                                        },
                                                        "10.49.0.0 10.4.1.1": {
                                                            "adv_router": "10.4.1.1",
                                                            "lsa_id": "10.49.0.0",
                                                            "ospfv2": {
                                                                "body": {
                                                                    "opaque": {
                                                                        "extended_prefix_tlvs": {
                                                                            1: {
                                                                                "tlv_type": "Extended Prefix",
                                                                                "length": 20,
                                                                                "prefix": "10.4.1.1/32",
                                                                                "af": 0,
                                                                                "route_type": "Intra",
                                                                                "flags": "N-bit",
                                                                                "sub_tlvs": {
                                                                                    1: {
                                                                                        "type": "Prefix SID",
                                                                                        "length": 8,
                                                                                        "flags": "None",
                                                                                        "mt_id": 0,
                                                                                        "algo": "SPF",
                                                                                        "sid": 1
                                                                                    }
                                                                                }
                                                                            }
                                                                        }
                                                                    }
                                                                },
                                                                "header": {
                                                                    "age": 49,
                                                                    "option": "None",
                                                                    "option_desc": "No TOS-capability, DC",
                                                                    "type": 10,
                                                                    "lsa_id": "10.49.0.0",
                                                                    "adv_router": "10.4.1.1",
                                                                    "opaque_id": 0,
                                                                    "seq_num": "80000001",
                                                                    "checksum": "0xEFA7",
                                                                    "length": 44
                                                                }
                                                            }
                                                        },
                                                        "10.64.0.20 10.4.1.1": {
                                                            "adv_router": "10.4.1.1",
                                                            "lsa_id": "10.64.0.20",
                                                            "ospfv2": {
                                                                "body": {
                                                                    "opaque": {
                                                                        "extended_link_tlvs": {
                                                                            1: {
                                                                                "tlv_type": "Extended Link",
                                                                                "length": 68,
                                                                                "link_name": "another router (point-to-point)",
                                                                                "link_type": 1,
                                                                                "link_id": "10.16.2.2",
                                                                                "link_data": "192.168.220.1",
                                                                                "sub_tlvs": {
                                                                                    1: {
                                                                                        "type": "Adj SID",
                                                                                        "length": 7,
                                                                                        "flags": "L-Bit, V-bit",
                                                                                        "mt_id": 0,
                                                                                        "weight": 0,
                                                                                        "label": 19
                                                                                    },
                                                                                    2: {
                                                                                        "type": "Remote Intf Addr",
                                                                                        "remote_interface_address": "192.168.220.2"
                                                                                    },
                                                                                    3: {
                                                                                        "type": "Local / Remote Intf ID",
                                                                                        "local_interface_id": 20,
                                                                                        "remote_interface_id": 20
                                                                                    }
                                                                                }
                                                                            }
                                                                        }
                                                                    }
                                                                },
                                                                "header": {
                                                                    "age": 49,
                                                                    "option": "None",
                                                                    "option_desc": "No TOS-capability, DC",
                                                                    "type": 10,
                                                                    "lsa_id": "10.64.0.20",
                                                                    "adv_router": "10.4.1.1",
                                                                    "opaque_id": 20,
                                                                    "seq_num": "80000001",
                                                                    "checksum": "0xF52F",
                                                                    "length": 92
                                                                }
                                                            }
                                                        },
                                                        "10.64.0.21 10.4.1.1": {
                                                            "adv_router": "10.4.1.1",
                                                            "lsa_id": "10.64.0.21",
                                                            "ospfv2": {
                                                                "body": {
                                                                    "opaque": {
                                                                        "extended_link_tlvs": {
                                                                            1: {
                                                                                "tlv_type": "Extended Link",
                                                                                "length": 68,
                                                                                "link_name": "another router (point-to-point)",
                                                                                "link_type": 1,
                                                                                "link_id": "10.16.2.2",
                                                                                "link_data": "192.168.111.1",
                                                                                "sub_tlvs": {
                                                                                    1: {
                                                                                        "type": "Adj SID",
                                                                                        "length": 7,
                                                                                        "flags": "L-Bit, V-bit",
                                                                                        "mt_id": 0,
                                                                                        "weight": 0,
                                                                                        "label": 18
                                                                                    },
                                                                                    2: {
                                                                                        "type": "Remote Intf Addr",
                                                                                        "remote_interface_address": "192.168.111.2"
                                                                                    },
                                                                                    3: {
                                                                                        "type": "Local / Remote Intf ID",
                                                                                        "local_interface_id": 21,
                                                                                        "remote_interface_id": 22
                                                                                    }
                                                                                }
                                                                            }
                                                                        }
                                                                    }
                                                                },
                                                                "header": {
                                                                    "age": 49,
                                                                    "option": "None",
                                                                    "option_desc": "No TOS-capability, DC",
                                                                    "type": 10,
                                                                    "lsa_id": "10.64.0.21",
                                                                    "adv_router": "10.4.1.1",
                                                                    "opaque_id": 21,
                                                                    "seq_num": "80000001",
                                                                    "checksum": "0xB764",
                                                                    "length": 92
                                                                }
                                                            }
                                                        },
                                                        "10.64.0.22 10.4.1.1": {
                                                            "adv_router": "10.4.1.1",
                                                            "lsa_id": "10.64.0.22",
                                                            "ospfv2": {
                                                                "body": {
                                                                    "opaque": {
                                                                        "extended_link_tlvs": {
                                                                            1: {
                                                                                "tlv_type": "Extended Link",
                                                                                "length": 68,
                                                                                "link_name": "another router (point-to-point)",
                                                                                "link_type": 1,
                                                                                "link_id": "10.16.2.2",
                                                                                "link_data": "192.168.4.1",
                                                                                "sub_tlvs": {
                                                                                    1: {
                                                                                        "type": "Adj SID",
                                                                                        "length": 7,
                                                                                        "flags": "L-Bit, V-bit",
                                                                                        "mt_id": 0,
                                                                                        "weight": 0,
                                                                                        "label": 17
                                                                                    },
                                                                                    2: {
                                                                                        "type": "Remote Intf Addr",
                                                                                        "remote_interface_address": "192.168.4.2"
                                                                                    },
                                                                                    3: {
                                                                                        "type": "Local / Remote Intf ID",
                                                                                        "local_interface_id": 22,
                                                                                        "remote_interface_id": 23
                                                                                    }
                                                                                }
                                                                            }
                                                                        }
                                                                    }
                                                                },
                                                                "header": {
                                                                    "age": 49,
                                                                    "option": "None",
                                                                    "option_desc": "No TOS-capability, DC",
                                                                    "type": 10,
                                                                    "lsa_id": "10.64.0.22",
                                                                    "adv_router": "10.4.1.1",
                                                                    "opaque_id": 22,
                                                                    "seq_num": "80000001",
                                                                    "checksum": "0xF420",
                                                                    "length": 92
                                                                }
                                                            }
                                                        },
                                                        "10.64.0.23 10.4.1.1": {
                                                            "adv_router": "10.4.1.1",
                                                            "lsa_id": "10.64.0.23",
                                                            "ospfv2": {
                                                                "body": {
                                                                    "opaque": {
                                                                        "extended_link_tlvs": {
                                                                            1: {
                                                                                "tlv_type": "Extended Link",
                                                                                "length": 68,
                                                                                "link_name": "another router (point-to-point)",
                                                                                "link_type": 1,
                                                                                "link_id": "10.16.2.2",
                                                                                "link_data": "192.168.154.1",
                                                                                "sub_tlvs": {
                                                                                    1: {
                                                                                        "type": "Adj SID",
                                                                                        "length": 7,
                                                                                        "flags": "L-Bit, V-bit",
                                                                                        "mt_id": 0,
                                                                                        "weight": 0,
                                                                                        "label": 16
                                                                                    },
                                                                                    2: {
                                                                                        "type": "Remote Intf Addr",
                                                                                        "remote_interface_address": "192.168.154.2"
                                                                                    },
                                                                                    3: {
                                                                                        "type": "Local / Remote Intf ID",
                                                                                        "local_interface_id": 23,
                                                                                        "remote_interface_id": 24
                                                                                    }
                                                                                }
                                                                            }
                                                                        }
                                                                    }
                                                                },
                                                                "header": {
                                                                    "age": 49,
                                                                    "option": "None",
                                                                    "option_desc": "No TOS-capability, DC",
                                                                    "type": 10,
                                                                    "lsa_id": "10.64.0.23",
                                                                    "adv_router": "10.4.1.1",
                                                                    "opaque_id": 23,
                                                                    "seq_num": "80000001",
                                                                    "checksum": "0x32DB",
                                                                    "length": 92
                                                                }
                                                            }
                                                        }
                                                    }
                                                }
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }

    golden_output2 = {'execute.return_value': '''
      PE1#show ip ospf database opaque-area self-originate
     
                OSPF Router with ID (10.4.1.1) (Process ID 65109)
     
                    Type-10 Opaque Area Link States (Area 8)
     
      LS age: 49
      Options: (No TOS-capability, DC)
      LS Type: Opaque Area Link
      Link State ID: 10.1.0.0
      Opaque Type: 1 (Traffic Engineering)
      Opaque ID: 0
      Advertising Router: 10.4.1.1
      LS Seq Number: 80000001
      Checksum: 0x58D1
      Length: 28
      Fragment number : 0
     
        MPLS TE router ID : 10.4.1.1
     
        Number of Links : 0
     
      LS age: MAXAGE(49)
      Options: (No TOS-capability, DC)
      LS Type: Opaque Area Link
      Link State ID: 10.1.0.15
      Opaque Type: 1 (Traffic Engineering)
      Opaque ID: 15
      Advertising Router: 10.4.1.1
      LS Seq Number: 80000001
      Checksum: 0x917E
      Length: 80
      Fragment number : 15
     
        Link connected to Point-to-Point network
          Link ID : 10.16.2.2
          Neighbor Address : 192.168.220.2
          Interface Address : 192.168.220.1
          Admin Metric : 1
          Maximum bandwidth : 176258176
          IGP Metric : 1
     
        Number of Links : 1
     
      LS age: 49
      Options: (No TOS-capability, DC)
      LS Type: Opaque Area Link
      Link State ID: 10.1.0.16
      Opaque Type: 1 (Traffic Engineering)
      Opaque ID: 16
      Advertising Router: 10.4.1.1
      LS Seq Number: 80000001
      Checksum: 0x8A09
      Length: 80
      Fragment number : 16
     
        Link connected to Point-to-Point network
          Link ID : 10.16.2.2
          Neighbor Address : 192.168.111.2
          Interface Address : 192.168.111.1
          Admin Metric : 1
          Maximum bandwidth : 125000000
          IGP Metric : 1
     
        Number of Links : 1
     
      LS age: 49
      Options: (No TOS-capability, DC)
      LS Type: Opaque Area Link
      Link State ID: 10.1.0.17
      Opaque Type: 1 (Traffic Engineering)
      Opaque ID: 17
      Advertising Router: 10.4.1.1
      LS Seq Number: 80000001
      Checksum: 0xC2CD
      Length: 80
      Fragment number : 17
     
        Link connected to Point-to-Point network
          Link ID : 10.16.2.2
          Neighbor Address : 192.168.4.2
          Interface Address : 192.168.4.1
          Admin Metric : 1
          Maximum bandwidth : 125000000
          IGP Metric : 1
     
        Number of Links : 1
     
      LS age: 49
      Options: (No TOS-capability, DC)
      LS Type: Opaque Area Link
      Link State ID: 10.1.0.18
      Opaque Type: 1 (Traffic Engineering)
      Opaque ID: 18
      Advertising Router: 10.4.1.1
      LS Seq Number: 80000001
      Checksum: 0xFA92
      Length: 80
      Fragment number : 18
     
        Link connected to Point-to-Point network
          Link ID : 10.16.2.2
          Neighbor Address : 192.168.154.2
          Interface Address : 192.168.154.1
          Admin Metric : 1
          Maximum bandwidth : 125000000
          IGP Metric : 1
     
        Number of Links : 1
     
      LS age: 49
      Options: (No TOS-capability, DC)
      LS Type: Opaque Area Link
      Link State ID: 10.16.0.0
      Opaque Type: 4 (Router Information)
      Opaque ID: 0
      Advertising Router: 10.4.1.1
      LS Seq Number: 80000001
      Checksum: 0xD28C
      Length: 76
     
        TLV Type: Router Information
        Length: 4
        Capabilities:
          Graceful Restart Helper
          Stub Router Support
     
        TLV Type: Segment Routing Algorithm
        Length: 2
          Algorithm: SPF
          Algorithm: Strict SPF
     
        TLV Type: Segment Routing Range
        Length: 12
          Range Size: 8000
     
          Sub-TLV Type: SID/Label
          Length: 3
            Label: 16000
     
        TLV Type: Segment Routing Node MSD
        Length: 2
          Sub-type: Node Max Sid Depth, Value: 13
     
        TLV Type: Segment Routing Local Block
        Length: 12
          Range Size: 1000
     
          Sub-TLV Type: SID/Label
          Length: 3
            Label: 15000
     
      LS age: 49
      Options: (No TOS-capability, DC)
      LS Type: Opaque Area Link
      Link State ID: 10.49.0.0
      Opaque Type: 7 (Extended Prefix)
      Opaque ID: 0
      Advertising Router: 10.4.1.1
      LS Seq Number: 80000001
      Checksum: 0xEFA7
      Length: 44
     
        TLV Type: Extended Prefix
        Length: 20
          Prefix    : 10.4.1.1/32
          AF        : 0
          Route-type: Intra
          Flags     : N-bit
     
          Sub-TLV Type: Prefix SID
          Length: 8
            Flags : None
            MTID  : 0
            Algo  : SPF
            SID   : 1
     
      LS age: 49
      Options: (No TOS-capability, DC)
      LS Type: Opaque Area Link
      Link State ID: 10.64.0.20
      Opaque Type: 8 (Extended Link)
      Opaque ID: 20
      Advertising Router: 10.4.1.1
      LS Seq Number: 80000001
      Checksum: 0xF52F
      Length: 92
     
        TLV Type: Extended Link
        Length: 68
        Link connected to : another Router (point-to-point)
        (Link ID) Designated Router address: 10.16.2.2
        (Link Data) Interface IP address: 192.168.220.1
     
          Sub-TLV Type: Adj SID
          Length : 7
            Flags  : L-Bit, V-bit
            MTID   : 0
            Weight : 0
            Label  : 19
     
          Sub-TLV Type: Remote Intf Addr
            Remote Interface Address   : 192.168.220.2
     
          Sub-TLV Type: Local / Remote Intf ID
            Local Interface ID   : 20
            Remote Interface ID   : 20
     
      LS age: 49
      Options: (No TOS-capability, DC)
      LS Type: Opaque Area Link
      Link State ID: 10.64.0.21
      Opaque Type: 8 (Extended Link)
      Opaque ID: 21
      Advertising Router: 10.4.1.1
      LS Seq Number: 80000001
      Checksum: 0xB764
      Length: 92
     
        TLV Type: Extended Link
        Length: 68
        Link connected to : another Router (point-to-point)
        (Link ID) Neighboring Router ID: 10.16.2.2
        (Link Data) Interface IP address: 192.168.111.1
     
          Sub-TLV Type: Adj SID
          Length : 7
            Flags  : L-Bit, V-bit
            MTID   : 0
            Weight : 0
            Label  : 18
     
          Sub-TLV Type: Remote Intf Addr
            Remote Interface Address   : 192.168.111.2
     
          Sub-TLV Type: Local / Remote Intf ID
            Local Interface ID   : 21
            Remote Interface ID   : 22
     
      LS age: 49
      Options: (No TOS-capability, DC)
      LS Type: Opaque Area Link
      Link State ID: 10.64.0.22
      Opaque Type: 8 (Extended Link)
      Opaque ID: 22
      Advertising Router: 10.4.1.1
      LS Seq Number: 80000001
      Checksum: 0xF420
      Length: 92
     
        TLV Type: Extended Link
        Length: 68
        Link connected to : another Router (point-to-point)
        (Link ID) Neighboring Router ID: 10.16.2.2
        (Link Data) Interface IP address: 192.168.4.1
     
          Sub-TLV Type: Adj SID
          Length : 7
            Flags  : L-Bit, V-bit
            MTID   : 0
            Weight : 0
            Label  : 17
     
          Sub-TLV Type: Remote Intf Addr
            Remote Interface Address   : 192.168.4.2
     
          Sub-TLV Type: Local / Remote Intf ID
            Local Interface ID   : 22
            Remote Interface ID   : 23
     
      LS age: 49
      Options: (No TOS-capability, DC)
      LS Type: Opaque Area Link
      Link State ID: 10.64.0.23
      Opaque Type: 8 (Extended Link)
      Opaque ID: 23
      Advertising Router: 10.4.1.1
      LS Seq Number: 80000001
      Checksum: 0x32DB
      Length: 92
     
        TLV Type: Extended Link
        Length: 68
        Link connected to : another Router (point-to-point)
        (Link ID) Neighboring Router ID: 10.16.2.2
        (Link Data) Interface IP address: 192.168.154.1
     
          Sub-TLV Type: Adj SID
          Length : 7
            Flags  : L-Bit, V-bit
            MTID   : 0
            Weight : 0
            Label  : 16
     
          Sub-TLV Type: Remote Intf Addr
            Remote Interface Address   : 192.168.154.2
     
          Sub-TLV Type: Local / Remote Intf ID
            Local Interface ID   : 23
            Remote Interface ID   : 24
    '''}

    golden_output3 = {'execute.return_value': '''
        show ip ospf database opaque-area adv-router 10.4.1.1

            OSPF Router with ID (10.4.1.1) (Process ID 65109)

                Type-10 Opaque Area Link States (Area 8)

        LS age: 1663
        Options: (No TOS-capability, DC)
        LS Type: Opaque Area Link
        Link State ID: 10.1.0.0
        Opaque Type: 1 (Traffic Engineering)
        Opaque ID: 0
        Advertising Router: 10.4.1.1
        LS Seq Number: 8000013B
        Checksum: 0xE00E
        Length: 28
        Fragment number : 0

            MPLS TE router ID : 10.4.1.1

            Number of Links : 0

        LS age: 1663
        Options: (No TOS-capability, DC)
        LS Type: Opaque Area Link
        Link State ID: 10.1.0.3
        Opaque Type: 1 (Traffic Engineering)
        Opaque ID: 3
        Advertising Router: 10.4.1.1
        LS Seq Number: 8000013B
        Checksum: 0xFF9E
        Length: 80
        Fragment number : 3

            Link connected to Point-to-Point network
            Link ID : 10.229.11.11
            Neighbor Address : 10.0.0.9
            Interface Address : 10.0.0.10
            Admin Metric : 10
            Maximum bandwidth : 125000000
            IGP Metric : 10

            Number of Links : 1

        LS age: 1663
        Options: (No TOS-capability, DC)
        LS Type: Opaque Area Link
        Link State ID: 10.1.0.4
        Opaque Type: 1 (Traffic Engineering)
        Opaque ID: 4
        Advertising Router: 10.4.1.1
        LS Seq Number: 8000013B
        Checksum: 0xAE06
        Length: 80
        Fragment number : 4

            Link connected to Point-to-Point network
            Link ID : 10.151.22.22
            Neighbor Address : 10.0.0.13
            Interface Address : 10.0.0.14
            Admin Metric : 100
            Maximum bandwidth : 125000000
            IGP Metric : 100

            Number of Links : 1

        LS age: 1663
        Options: (No TOS-capability, DC)
        LS Type: Opaque Area Link
        Link State ID: 10.1.0.5
        Opaque Type: 1 (Traffic Engineering)
        Opaque ID: 5
        Advertising Router: 10.4.1.1
        LS Seq Number: 8000013B
        Checksum: 0xFE8D
        Length: 80
        Fragment number : 5

            Link connected to Point-to-Point network
            Link ID : 10.151.22.22
            Neighbor Address : 10.0.0.25
            Interface Address : 10.0.0.26
            Admin Metric : 1000
            Maximum bandwidth : 125000000
            IGP Metric : 1000

            Number of Links : 1

        LS age: 1663
        Options: (No TOS-capability, DC)
        LS Type: Opaque Area Link
        Link State ID: 10.16.0.0
        Opaque Type: 4 (Router Information)
        Opaque ID: 0
        Advertising Router: 10.4.1.1
        LS Seq Number: 8000013B
        Checksum: 0x5BC8
        Length: 76

            TLV Type: Router Information
            Length: 4
            Capabilities:
            Graceful Restart Helper
            Stub Router Support

            TLV Type: Segment Routing Algorithm
            Length: 2
            Algorithm: SPF
            Algorithm: Strict SPF

            TLV Type: Segment Routing Range
            Length: 12
            Range Size: 8000

            Sub-TLV Type: SID/Label
            Length: 3
                Label: 16000

            TLV Type: Segment Routing Node MSD
            Length: 2
            Sub-type: Node Max Sid Depth, Value: 13

            TLV Type: Segment Routing Local Block
            Length: 12
            Range Size: 1000

            Sub-TLV Type: SID/Label
            Length: 3
                Label: 15000

        LS age: 1663
        Options: (No TOS-capability, DC)
        LS Type: Opaque Area Link
        Link State ID: 10.49.0.0
        Opaque Type: 7 (Extended Prefix)
        Opaque ID: 0
        Advertising Router: 10.4.1.1
        LS Seq Number: 80000133
        Checksum: 0x88DB
        Length: 44

            TLV Type: Extended Prefix
            Length: 20
            Prefix    : 10.4.1.1/32
            AF        : 0
            Route-type: Intra
            Flags     : N-bit

            Sub-TLV Type: Prefix SID
            Length: 8
                Flags : None
                MTID  : 0
                Algo  : SPF
                SID   : 1

        LS age: 1663
        Options: (No TOS-capability, DC)
        LS Type: Opaque Area Link
        Link State ID: 10.64.0.9
        Opaque Type: 8 (Extended Link)
        Opaque ID: 9
        Advertising Router: 10.4.1.1
        LS Seq Number: 8000013C
        Checksum: 0xA666
        Length: 104

            TLV Type: Extended Link
            Length: 80
            Link connected to : another Router (point-to-point)
            (Link ID) Neighboring Router ID: 10.229.11.11
            (Link Data) Interface IP address: 10.0.0.10

            Sub-TLV Type: Adj SID
            Length : 7
                Flags  : L-Bit, V-bit
                MTID   : 0
                Weight : 0
                Label  : 18

            Sub-TLV Type: Adj SID
            Length : 7
                Flags  : L-Bit, V-bit, B-bit
                MTID   : 0
                Weight : 0
                Label  : 19

            Sub-TLV Type: Remote Intf Addr
                Remote Interface Address   : 10.0.0.9

            Sub-TLV Type: Local / Remote Intf ID
                Local Interface ID   : 9
                Remote Interface ID   : 9

        LS age: 1663
        Options: (No TOS-capability, DC)
        LS Type: Opaque Area Link
        Link State ID: 10.64.0.10
        Opaque Type: 8 (Extended Link)
        Opaque ID: 10
        Advertising Router: 10.4.1.1
        LS Seq Number: 8000013C
        Checksum: 0xEBE6
        Length: 104

            TLV Type: Extended Link
            Length: 80
            Link connected to : another Router (point-to-point)
            (Link ID) Neighboring Router ID: 10.151.22.22
            (Link Data) Interface IP address: 10.0.0.14

            Sub-TLV Type: Adj SID
            Length : 7
                Flags  : L-Bit, V-bit
                MTID   : 0
                Weight : 0
                Label  : 17

            Sub-TLV Type: Adj SID
            Length : 7
                Flags  : L-Bit, V-bit, B-bit
                MTID   : 0
                Weight : 0
                Label  : 21

            Sub-TLV Type: Remote Intf Addr
                Remote Interface Address   : 10.0.0.13

            Sub-TLV Type: Local / Remote Intf ID
                Local Interface ID   : 10
                Remote Interface ID   : 8

        LS age: 1663
        Options: (No TOS-capability, DC)
        LS Type: Opaque Area Link
        Link State ID: 10.64.0.11
        Opaque Type: 8 (Extended Link)
        Opaque ID: 11
        Advertising Router: 10.4.1.1
        LS Seq Number: 8000013D
        Checksum: 0xB8F1
        Length: 104

            TLV Type: Extended Link
            Length: 80
            Link connected to : another Router (point-to-point)
            (Link ID) Neighboring Router ID: 10.151.22.22
            (Link Data) Interface IP address: 10.0.0.26

            Sub-TLV Type: Adj SID
            Length : 7
                Flags  : L-Bit, V-bit
                MTID   : 0
                Weight : 0
                Label  : 16

            Sub-TLV Type: Adj SID
            Length : 7
                Flags  : L-Bit, V-bit, B-bit
                MTID   : 0
                Weight : 0
                Label  : 20

            Sub-TLV Type: Remote Intf Addr
                Remote Interface Address   : 10.0.0.25

            Sub-TLV Type: Local / Remote Intf ID
                Local Interface ID   : 11
                Remote Interface ID   : 9
    '''}

    golden_parsed_output3 = {
        'vrf': {
            'default': {
                'address_family': {
                    'ipv4': {
                        'instance': {
                            '65109': {
                                'areas': {
                                    '0.0.0.8': {
                                        'database': {
                                            'lsa_types': {
                                                10: {
                                                    'lsa_type': 10,
                                                    'lsas': {
                                                        '10.1.0.0 10.4.1.1': {
                                                            'adv_router': '10.4.1.1',
                                                            'lsa_id': '10.1.0.0',
                                                            'ospfv2': {
                                                                'body': {
                                                                    'opaque': {
                                                                        'mpls_te_router_id': '10.4.1.1',
                                                                        'num_of_links': 0
                                                                    }
                                                                },
                                                                'header': {
                                                                    'age': 1663,
                                                                    'option': 'None',
                                                                    'option_desc': 'No TOS-capability, DC',
                                                                    'type': 10,
                                                                    'lsa_id': '10.1.0.0',
                                                                    'adv_router': '10.4.1.1',
                                                                    'opaque_type': 1,
                                                                    'opaque_id': 0,
                                                                    'seq_num': '8000013B',
                                                                    'checksum': '0xE00E',
                                                                    'length': 28,
                                                                    'fragment_number': 0
                                                                }
                                                            }
                                                        },
                                                        '10.1.0.3 10.4.1.1': {
                                                            'adv_router': '10.4.1.1',
                                                            'lsa_id': '10.1.0.3',
                                                            'ospfv2': {
                                                                'body': {
                                                                    'opaque': {
                                                                        'link_tlvs': {
                                                                            1: {
                                                                                'link_type': 1,
                                                                                'link_name': 'point-to-point network',
                                                                                'link_id': '10.229.11.11',
                                                                                'remote_if_ipv4_addrs': {
                                                                                    '10.0.0.9': {}
                                                                                },
                                                                                'local_if_ipv4_addrs': {
                                                                                    '10.0.0.10': {}
                                                                                },
                                                                                'te_metric': 10,
                                                                                'max_bandwidth': 125000000,
                                                                                'igp_metric': 10
                                                                            }
                                                                        },
                                                                        'num_of_links': 1
                                                                    }
                                                                },
                                                                'header': {
                                                                    'age': 1663,
                                                                    'option': 'None',
                                                                    'option_desc': 'No TOS-capability, DC',
                                                                    'type': 10,
                                                                    'lsa_id': '10.1.0.3',
                                                                    'adv_router': '10.4.1.1',
                                                                    'opaque_type': 1,
                                                                    'opaque_id': 3,
                                                                    'seq_num': '8000013B',
                                                                    'checksum': '0xFF9E',
                                                                    'length': 80,
                                                                    'fragment_number': 3
                                                                }
                                                            }
                                                        },
                                                        '10.1.0.4 10.4.1.1': {
                                                            'adv_router': '10.4.1.1',
                                                            'lsa_id': '10.1.0.4',
                                                            'ospfv2': {
                                                                'body': {
                                                                    'opaque': {
                                                                        'link_tlvs': {
                                                                            1: {
                                                                                'link_type': 1,
                                                                                'link_name': 'point-to-point network',
                                                                                'link_id': '10.151.22.22',
                                                                                'remote_if_ipv4_addrs': {
                                                                                    '10.0.0.13': {}
                                                                                },
                                                                                'local_if_ipv4_addrs': {
                                                                                    '10.0.0.14': {}
                                                                                },
                                                                                'te_metric': 100,
                                                                                'max_bandwidth': 125000000,
                                                                                'igp_metric': 100
                                                                            }
                                                                        },
                                                                        'num_of_links': 1
                                                                    }
                                                                },
                                                                'header': {
                                                                    'age': 1663,
                                                                    'option': 'None',
                                                                    'option_desc': 'No TOS-capability, DC',
                                                                    'type': 10,
                                                                    'lsa_id': '10.1.0.4',
                                                                    'adv_router': '10.4.1.1',
                                                                    'opaque_type': 1,
                                                                    'opaque_id': 4,
                                                                    'seq_num': '8000013B',
                                                                    'checksum': '0xAE06',
                                                                    'length': 80,
                                                                    'fragment_number': 4
                                                                }
                                                            }
                                                        },
                                                        '10.1.0.5 10.4.1.1': {
                                                            'adv_router': '10.4.1.1',
                                                            'lsa_id': '10.1.0.5',
                                                            'ospfv2': {
                                                                'body': {
                                                                    'opaque': {
                                                                        'link_tlvs': {
                                                                            1: {
                                                                                'link_type': 1,
                                                                                'link_name': 'point-to-point network',
                                                                                'link_id': '10.151.22.22',
                                                                                'remote_if_ipv4_addrs': {
                                                                                    '10.0.0.25': {}
                                                                                },
                                                                                'local_if_ipv4_addrs': {
                                                                                    '10.0.0.26': {}
                                                                                },
                                                                                'te_metric': 1000,
                                                                                'max_bandwidth': 125000000,
                                                                                'igp_metric': 1000
                                                                            }
                                                                        },
                                                                        'num_of_links': 1
                                                                    }
                                                                },
                                                                'header': {
                                                                    'age': 1663,
                                                                    'option': 'None',
                                                                    'option_desc': 'No TOS-capability, DC',
                                                                    'type': 10,
                                                                    'lsa_id': '10.1.0.5',
                                                                    'adv_router': '10.4.1.1',
                                                                    'opaque_type': 1,
                                                                    'opaque_id': 5,
                                                                    'seq_num': '8000013B',
                                                                    'checksum': '0xFE8D',
                                                                    'length': 80,
                                                                    'fragment_number': 5
                                                                }
                                                            }
                                                        },
                                                        '10.16.0.0 10.4.1.1': {
                                                            'adv_router': '10.4.1.1',
                                                            'lsa_id': '10.16.0.0',
                                                            'ospfv2': {
                                                                'body': {
                                                                    'opaque': {
                                                                        'router_capabilities_tlv': {
                                                                            1: {
                                                                                'tlv_type': 'Router Information',
                                                                                'length': 4,
                                                                                'information_capabilities': {
                                                                                    'graceful_restart_helper': True,
                                                                                    'stub_router': True
                                                                                }
                                                                            }
                                                                        },
                                                                        'sr_algorithm_tlv': {
                                                                            1: {
                                                                                'tlv_type': 'Segment Routing Algorithm',
                                                                                'length': 2,
                                                                                'algorithm': {
                                                                                    'spf': True,
                                                                                    'strict_spf': True
                                                                                }
                                                                            }
                                                                        },
                                                                        'sid_range_tlvs': {
                                                                            1: {
                                                                                'tlv_type': 'Segment Routing Range',
                                                                                'length': 12,
                                                                                'range_size': 8000,
                                                                                'sub_tlvs': {
                                                                                    1: {
                                                                                        'type': 'SID/Label',
                                                                                        'length': 3,
                                                                                        'label': 16000
                                                                                    }
                                                                                }
                                                                            }
                                                                        },
                                                                        'node_msd_tlvs': {
                                                                            1: {
                                                                                'tlv_type': 'Segment Routing Node MSD',
                                                                                'length': 2,
                                                                                'sub_type': {
                                                                                    'node_max_sid_depth_value': 13
                                                                                }
                                                                            }
                                                                        },
                                                                        'local_block_tlvs': {
                                                                            1: {
                                                                                'tlv_type': 'Segment Routing Local Block',
                                                                                'length': 12,
                                                                                'range_size': 1000,
                                                                                'sub_tlvs': {
                                                                                    1: {
                                                                                        'type': 'SID/Label',
                                                                                        'length': 3,
                                                                                        'label': 15000
                                                                                    }
                                                                                }
                                                                            }
                                                                        }
                                                                    }
                                                                },
                                                                'header': {
                                                                    'age': 1663,
                                                                    'option': 'None',
                                                                    'option_desc': 'No TOS-capability, DC',
                                                                    'type': 10,
                                                                    'lsa_id': '10.16.0.0',
                                                                    'adv_router': '10.4.1.1',
                                                                    'opaque_id': 0,
                                                                    'seq_num': '8000013B',
                                                                    'checksum': '0x5BC8',
                                                                    'length': 76
                                                                }
                                                            }
                                                        },
                                                        '10.49.0.0 10.4.1.1': {
                                                            'adv_router': '10.4.1.1',
                                                            'lsa_id': '10.49.0.0',
                                                            'ospfv2': {
                                                                'body': {
                                                                    'opaque': {
                                                                        'extended_prefix_tlvs': {
                                                                            1: {
                                                                                'tlv_type': 'Extended Prefix',
                                                                                'length': 20,
                                                                                'prefix': '10.4.1.1/32',
                                                                                'af': 0,
                                                                                'route_type': 'Intra',
                                                                                'flags': 'N-bit',
                                                                                'sub_tlvs': {
                                                                                    1: {
                                                                                        'type': 'Prefix SID',
                                                                                        'length': 8,
                                                                                        'flags': 'None',
                                                                                        'mt_id': 0,
                                                                                        'algo': 'SPF',
                                                                                        'sid': 1
                                                                                    }
                                                                                }
                                                                            }
                                                                        }
                                                                    }
                                                                },
                                                                'header': {
                                                                    'age': 1663,
                                                                    'option': 'None',
                                                                    'option_desc': 'No TOS-capability, DC',
                                                                    'type': 10,
                                                                    'lsa_id': '10.49.0.0',
                                                                    'adv_router': '10.4.1.1',
                                                                    'opaque_id': 0,
                                                                    'seq_num': '80000133',
                                                                    'checksum': '0x88DB',
                                                                    'length': 44
                                                                }
                                                            }
                                                        },
                                                        '10.64.0.9 10.4.1.1': {
                                                            'adv_router': '10.4.1.1',
                                                            'lsa_id': '10.64.0.9',
                                                            'ospfv2': {
                                                                'body': {
                                                                    'opaque': {
                                                                        'extended_link_tlvs': {
                                                                            1: {
                                                                                'tlv_type': 'Extended Link',
                                                                                'length': 80,
                                                                                'link_name': 'another router (point-to-point)',
                                                                                'link_type': 1,
                                                                                'link_id': '10.229.11.11',
                                                                                'link_data': '10.0.0.10',
                                                                                'sub_tlvs': {
                                                                                    1: {
                                                                                        'type': 'Adj SID',
                                                                                        'length': 7,
                                                                                        'flags': 'L-Bit, V-bit',
                                                                                        'mt_id': 0,
                                                                                        'weight': 0,
                                                                                        'label': 18
                                                                                    },
                                                                                    2: {
                                                                                        'type': 'Adj SID',
                                                                                        'length': 7,
                                                                                        'flags': 'L-Bit, V-bit, B-bit',
                                                                                        'mt_id': 0,
                                                                                        'weight': 0,
                                                                                        'label': 19
                                                                                    },
                                                                                    3: {
                                                                                        'type': 'Remote Intf Addr',
                                                                                        'remote_interface_address': '10.0.0.9'
                                                                                    },
                                                                                    4: {
                                                                                        'type': 'Local / Remote Intf ID',
                                                                                        'local_interface_id': 9,
                                                                                        'remote_interface_id': 9
                                                                                    }
                                                                                }
                                                                            }
                                                                        }
                                                                    }
                                                                },
                                                                'header': {
                                                                    'age': 1663,
                                                                    'option': 'None',
                                                                    'option_desc': 'No TOS-capability, DC',
                                                                    'type': 10,
                                                                    'lsa_id': '10.64.0.9',
                                                                    'adv_router': '10.4.1.1',
                                                                    'opaque_id': 9,
                                                                    'seq_num': '8000013C',
                                                                    'checksum': '0xA666',
                                                                    'length': 104
                                                                }
                                                            }
                                                        },
                                                        '10.64.0.10 10.4.1.1': {
                                                            'adv_router': '10.4.1.1',
                                                            'lsa_id': '10.64.0.10',
                                                            'ospfv2': {
                                                                'body': {
                                                                    'opaque': {
                                                                        'extended_link_tlvs': {
                                                                            1: {
                                                                                'tlv_type': 'Extended Link',
                                                                                'length': 80,
                                                                                'link_name': 'another router (point-to-point)',
                                                                                'link_type': 1,
                                                                                'link_id': '10.151.22.22',
                                                                                'link_data': '10.0.0.14',
                                                                                'sub_tlvs': {
                                                                                    1: {
                                                                                        'type': 'Adj SID',
                                                                                        'length': 7,
                                                                                        'flags': 'L-Bit, V-bit',
                                                                                        'mt_id': 0,
                                                                                        'weight': 0,
                                                                                        'label': 17
                                                                                    },
                                                                                    2: {
                                                                                        'type': 'Adj SID',
                                                                                        'length': 7,
                                                                                        'flags': 'L-Bit, V-bit, B-bit',
                                                                                        'mt_id': 0,
                                                                                        'weight': 0,
                                                                                        'label': 21
                                                                                    },
                                                                                    3: {
                                                                                        'type': 'Remote Intf Addr',
                                                                                        'remote_interface_address': '10.0.0.13'
                                                                                    },
                                                                                    4: {
                                                                                        'type': 'Local / Remote Intf ID',
                                                                                        'local_interface_id': 10,
                                                                                        'remote_interface_id': 8
                                                                                    }
                                                                                }
                                                                            }
                                                                        }
                                                                    }
                                                                },
                                                                'header': {
                                                                    'age': 1663,
                                                                    'option': 'None',
                                                                    'option_desc': 'No TOS-capability, DC',
                                                                    'type': 10,
                                                                    'lsa_id': '10.64.0.10',
                                                                    'adv_router': '10.4.1.1',
                                                                    'opaque_id': 10,
                                                                    'seq_num': '8000013C',
                                                                    'checksum': '0xEBE6',
                                                                    'length': 104
                                                                }
                                                            }
                                                        },
                                                        '10.64.0.11 10.4.1.1': {
                                                            'adv_router': '10.4.1.1',
                                                            'lsa_id': '10.64.0.11',
                                                            'ospfv2': {
                                                                'body': {
                                                                    'opaque': {
                                                                        'extended_link_tlvs': {
                                                                            1: {
                                                                                'tlv_type': 'Extended Link',
                                                                                'length': 80,
                                                                                'link_name': 'another router (point-to-point)',
                                                                                'link_type': 1,
                                                                                'link_id': '10.151.22.22',
                                                                                'link_data': '10.0.0.26',
                                                                                'sub_tlvs': {
                                                                                    1: {
                                                                                        'type': 'Adj SID',
                                                                                        'length': 7,
                                                                                        'flags': 'L-Bit, V-bit',
                                                                                        'mt_id': 0,
                                                                                        'weight': 0,
                                                                                        'label': 16
                                                                                    },
                                                                                    2: {
                                                                                        'type': 'Adj SID',
                                                                                        'length': 7,
                                                                                        'flags': 'L-Bit, V-bit, B-bit',
                                                                                        'mt_id': 0,
                                                                                        'weight': 0,
                                                                                        'label': 20
                                                                                    },
                                                                                    3: {
                                                                                        'type': 'Remote Intf Addr',
                                                                                        'remote_interface_address': '10.0.0.25'
                                                                                    },
                                                                                    4: {
                                                                                        'type': 'Local / Remote Intf ID',
                                                                                        'local_interface_id': 11,
                                                                                        'remote_interface_id': 9
                                                                                    }
                                                                                }
                                                                            }
                                                                        }
                                                                    }
                                                                },
                                                                'header': {
                                                                    'age': 1663,
                                                                    'option': 'None',
                                                                    'option_desc': 'No TOS-capability, DC',
                                                                    'type': 10,
                                                                    'lsa_id': '10.64.0.11',
                                                                    'adv_router': '10.4.1.1',
                                                                    'opaque_id': 11,
                                                                    'seq_num': '8000013D',
                                                                    'checksum': '0xB8F1',
                                                                    'length': 104
                                                                }
                                                            }
                                                        }
                                                    }
                                                }
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }


    def test_show_ip_ospf_database_opaque_area_full1(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output1)
        obj = ShowIpOspfDatabaseOpaqueArea(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output1)

    def test_show_ip_ospf_database_opaque_area_full2(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output2)        
        obj = ShowIpOspfDatabaseOpaqueAreaSelfOriginate(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output2)
    
    def test_show_ip_ospf_database_opaque_area_adv_router(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output3)        
        obj = ShowIpOspfDatabaseOpaqueAreaAdvRouter(device=self.device)
        parsed_output = obj.parse(address='10.4.1.1')
        self.assertEqual(parsed_output, self.golden_parsed_output3)

    def test_show_ip_ospf_database_opaque_area_empty(self):
        self.maxDiff = None
        self.device = Mock(**self.empty_output)
        obj = ShowIpOspfDatabaseOpaqueArea(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()


# ===============================================
# Unit test for 'show ip ospf mpls ldp interface'
# ===============================================
class test_show_ip_ospf_mpls_ldp_interface(unittest.TestCase):

    '''Unit test for "show ip ospf mpls ldp interface" '''

    device = Device(name='aDevice')
    
    empty_output = {'execute.return_value': ''}

    golden_parsed_output1 = {
        'vrf': 
            {'VRF1': 
                {'address_family': 
                    {'ipv4': 
                        {'instance': 
                            {'2': 
                                {'areas': 
                                    {'0.0.0.1': 
                                        {'interfaces': 
                                            {'GigabitEthernet3': 
                                                {'mpls': 
                                                    {'ldp': 
                                                        {'autoconfig': False,
                                                        'autoconfig_area_id': '0.0.0.1',
                                                        'holddown_timer': False,
                                                        'igp_sync': False,
                                                        'state': 'down',
                                                         'state_info': 'pending LDP'}}},
                                            'OSPF_SL1': 
                                                {'mpls': 
                                                    {'ldp': 
                                                        {'autoconfig': False,
                                                        'autoconfig_area_id': '0.0.0.1',
                                                        'holddown_timer': False,
                                                        'igp_sync': False,
                                                        'state': 'up'}}}}}},
                                'mpls': 
                                    {'ldp': 
                                        {'autoconfig': False,
                                        'autoconfig_area_id': '0.0.0.1'}}}}}}},
            'default': 
                {'address_family': 
                    {'ipv4': 
                        {'instance': 
                            {'1': 
                                {'areas': 
                                    {'0.0.0.0': 
                                        {'interfaces': 
                                            {'GigabitEthernet1': 
                                                {'mpls': 
                                                    {'ldp': 
                                                        {'autoconfig': False,
                                                        'autoconfig_area_id': '0.0.0.0',
                                                        'holddown_timer': False,
                                                        'igp_sync': False,
                                                        'state': 'up'}}},
                                            'GigabitEthernet2': 
                                                {'mpls': 
                                                    {'ldp': 
                                                        {'autoconfig': False,
                                                        'autoconfig_area_id': '0.0.0.0',
                                                        'holddown_timer': False,
                                                        'igp_sync': False,
                                                        'state': 'up'}}},
                                            'TenGigabitEthernet3/0/1': 
                                                {'mpls': 
                                                    {'ldp': 
                                                        {'autoconfig': False,
                                                        'autoconfig_area_id': '0.0.0.0',
                                                        'holddown_timer': False,
                                                        'igp_sync': False,
                                                        'state': 'down'}}},
                                            'Loopback1': 
                                                {'mpls': 
                                                    {'ldp': 
                                                        {'autoconfig': False,
                                                        'autoconfig_area_id': '0.0.0.0',
                                                        'holddown_timer': False,
                                                        'igp_sync': False,
                                                        'state': 'up'}}}}}},
                                'mpls': 
                                    {'ldp': 
                                        {'autoconfig': False,
                                        'autoconfig_area_id': '0.0.0.0'}}}}}}}}}

    golden_output1 = {'execute.return_value': '''
        R1_ospf_xe#show ip ospf mpls ldp interface 
        Loopback1
          Process ID 1, Area 0
          LDP is not configured through LDP autoconfig
          LDP-IGP Synchronization : Not required
          Holddown timer is disabled
          Interface is up 
        GigabitEthernet2
          Process ID 1, Area 0
          LDP is not configured through LDP autoconfig
          LDP-IGP Synchronization : Not required
          Holddown timer is disabled
          Interface is up 
        GigabitEthernet1
          Process ID 1, Area 0
          LDP is not configured through LDP autoconfig
          LDP-IGP Synchronization : Not required
          Holddown timer is disabled
          Interface is up 
        OSPF_SL1
          Process ID 2, VRF VRF1, Area 1
          LDP is not configured through LDP autoconfig
          LDP-IGP Synchronization : Not required
          Holddown timer is disabled
          Interface is up 
        GigabitEthernet3
          Process ID 2, VRF VRF1, Area 1
          LDP is not configured through LDP autoconfig
          LDP-IGP Synchronization : Not required
          Holddown timer is disabled
          Interface is down and pending LDP
        TenGigabitEthernet3/0/1
          Process ID 1, Area 0
          LDP is not configured through LDP autoconfig
          LDP-IGP Synchronization : Not required
          Holddown timer is disabled
          Interface is down
        '''}

    golden_parsed_output2 = {
        'vrf': 
            {'default': 
                {'address_family': 
                    {'ipv4': 
                        {'instance': 
                            {'65109': 
                                {'areas': 
                                    {'0.0.0.8': 
                                        {'interfaces': 
                                            {'GigabitEthernet0/0/0': 
                                                {'mpls': 
                                                    {'ldp': 
                                                        {'autoconfig': False,
                                                        'autoconfig_area_id': '0.0.0.8',
                                                        'holddown_timer': False,
                                                        'igp_sync': True,
                                                        'state': 'up'}}},
                                            'GigabitEthernet0/0/2': 
                                                {'mpls': 
                                                    {'ldp': 
                                                        {'autoconfig': False,
                                                        'autoconfig_area_id': '0.0.0.8',
                                                        'holddown_timer': False,
                                                        'igp_sync': True,
                                                        'state': 'up'}}},
                                            'Loopback0': 
                                                {'mpls': 
                                                    {'ldp': 
                                                        {'autoconfig': False,
                                                        'autoconfig_area_id': '0.0.0.8',
                                                        'holddown_timer': False,
                                                        'igp_sync': False,
                                                        'state': 'up'}}}}}},
                                'mpls': 
                                    {'ldp': 
                                        {'autoconfig': False,
                                        'autoconfig_area_id': '0.0.0.8'}}}}}}}}}

    golden_output2 = {'execute.return_value': '''
        Router#sh ip ospf mpls ldp interface
        Load for five secs: 8%/0%; one minute: 6%; five minutes: 7%
        Time source is NTP, 10:36:51.278 EST Mon Nov 7 2016

        Loopback0
          Process ID 65109, Area 8
          LDP is not configured through LDP autoconfig
          LDP-IGP Synchronization : Not required
          Holddown timer is disabled
          Interface is up 
        GigabitEthernet0/0/2
          Process ID 65109, Area 8
          LDP is not configured through LDP autoconfig
          LDP-IGP Synchronization : Required
          Holddown timer is not configured
          Interface is up 
        GigabitEthernet0/0/0
          Process ID 65109, Area 8
          LDP is not configured through LDP autoconfig
          LDP-IGP Synchronization : Required
          Holddown timer is not configured
          Interface is up 
        '''}

    def test_show_ip_ospf_mpls_ldp_interface_full1(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output1)
        obj = ShowIpOspfMplsLdpInterface(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output1)

    def test_show_ip_ospf_mpls_ldp_interface_full2(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output2)
        obj = ShowIpOspfMplsLdpInterface(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output2)

    def test_show_ip_ospf_mpls_ldp_interface_empty(self):
        self.maxDiff = None
        self.device = Mock(**self.empty_output)
        obj = ShowIpOspfMplsLdpInterface(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()


# ==================================================
# Unit test for 'show ip ospf mpls traffic-eng link'
# ==================================================
class test_show_ip_ospf_mpls_traffic_eng_link(unittest.TestCase):

    '''Unit test for "show ip ospf mpls traffic-eng link" '''

    device = Device(name='aDevice')
    
    empty_output = {'execute.return_value': ''}

    golden_parsed_output1 = {
        'vrf': 
            {'VRF1': 
                {'address_family': 
                    {'ipv4': 
                        {'instance': 
                            {'2': 
                                {'areas': 
                                    {'0.0.0.1': 
                                        {'mpls': 
                                            {'te': 
                                                {'enable': False}}}},
                                'mpls': 
                                    {'te': 
                                        {'router_id': '10.229.11.11'}}}}}}},
            'default': 
                {'address_family': 
                    {'ipv4': 
                        {'instance': 
                            {'1': 
                                {'areas': 
                                    {'0.0.0.0': 
                                        {'mpls': 
                                            {'te': 
                                                {'area_instance': 2,
                                                'enable': True,
                                                'link_hash_bucket': 
                                                    {8: 
                                                        {'link_fragments': 
                                                            {2: 
                                                                {'affinity_bit': '0x0',
                                                                'igp_admin_metric': 1,
                                                                'interface_address': '10.1.2.1',
                                                                'link_id': '10.1.2.1',
                                                                'link_instance': 2,
                                                                'max_bandwidth': 125000000,
                                                                'max_reservable_bandwidth': 93750000,
                                                                'network_type': 'broadcast network',
                                                                'te_admin_metric': 1,
                                                                'total_priority': 8,
                                                                'unreserved_bandwidths': 
                                                                    {'0 93750000': 
                                                                        {'priority': 0,
                                                                        'unreserved_bandwidth': 93750000},
                                                                    '1 93750000': 
                                                                        {'priority': 1,
                                                                        'unreserved_bandwidth': 93750000},
                                                                    '2 93750000': 
                                                                        {'priority': 2,
                                                                        'unreserved_bandwidth': 93750000},
                                                                    '3 93750000': 
                                                                        {'priority': 3,
                                                                        'unreserved_bandwidth': 93750000},
                                                                    '4 93750000': 
                                                                        {'priority': 4,
                                                                        'unreserved_bandwidth': 93750000},
                                                                    '5 93750000': 
                                                                        {'priority': 5,
                                                                        'unreserved_bandwidth': 93750000},
                                                                    '6 93750000': 
                                                                        {'priority': 6,
                                                                        'unreserved_bandwidth': 93750000},
                                                                    '7 93750000': 
                                                                        {'priority': 7,
                                                                        'unreserved_bandwidth': 93750000}}}}},
                                                    9: 
                                                        {'link_fragments': 
                                                            {1: 
                                                                {'affinity_bit': '0x0',
                                                                'igp_admin_metric': 1,
                                                                'interface_address': '10.1.4.1',
                                                                'link_id': '10.1.4.4',
                                                                'link_instance': 2,
                                                                'max_bandwidth': 125000000,
                                                                'max_reservable_bandwidth': 93750000,
                                                                'network_type': 'broadcast network',
                                                                'te_admin_metric': 1,
                                                                'total_priority': 8,
                                                                'unreserved_bandwidths': 
                                                                    {'0 93750000': 
                                                                        {'priority': 0,
                                                                        'unreserved_bandwidth': 93750000},
                                                                    '1 93750000': 
                                                                        {'priority': 1,
                                                                        'unreserved_bandwidth': 93750000},
                                                                    '2 93750000': 
                                                                        {'priority': 2,
                                                                        'unreserved_bandwidth': 93750000},
                                                                    '3 93750000': 
                                                                        {'priority': 3,
                                                                        'unreserved_bandwidth': 93750000},
                                                                    '4 93750000': 
                                                                        {'priority': 4,
                                                                        'unreserved_bandwidth': 93750000},
                                                                    '5 93750000': 
                                                                        {'priority': 5,
                                                                        'unreserved_bandwidth': 93750000},
                                                                    '6 93750000': 
                                                                        {'priority': 6,
                                                                        'unreserved_bandwidth': 93750000},
                                                                    '7 93750000': 
                                                                        {'priority': 7,
                                                                        'unreserved_bandwidth': 93750000}}}}}},
                                                'total_links': 2}}}},
                                'mpls': 
                                    {'te': 
                                        {'router_id': '10.4.1.1'}}}}}}}}}
    
    def test_show_ip_ospf_mpls_traffic_eng_link_full1(self):
        
        self.maxDiff = None

        def mapper(key):
            return self.outputs[key]
        
        raw1 = '''\
            R1_ospf_xe#show ip ospf mpls traffic-eng link 

            OSPF Router with ID (10.4.1.1) (Process ID 1)

            Area 0 has 2 MPLS TE links. Area instance is 2.

            Links in hash bucket 8.
            Link is associated with fragment 2. Link instance is 2
              Link connected to Broadcast network
              Link ID : 10.1.2.1
              Interface Address : 10.1.2.1
              Admin Metric te: 1 igp: 1
              Maximum bandwidth : 125000000
              Maximum reservable bandwidth : 93750000
              Number of Priority : 8
              Priority 0 : 93750000     Priority 1 : 93750000   
              Priority 2 : 93750000     Priority 3 : 93750000   
              Priority 4 : 93750000     Priority 5 : 93750000   
              Priority 6 : 93750000     Priority 7 : 93750000   
              Affinity Bit : 0x0

            Links in hash bucket 9.
            Link is associated with fragment 1. Link instance is 2
              Link connected to Broadcast network
              Link ID : 10.1.4.4
              Interface Address : 10.1.4.1
              Admin Metric te: 1 igp: 1
              Maximum bandwidth : 125000000
              Maximum reservable bandwidth : 93750000
              Number of Priority : 8
              Priority 0 : 93750000     Priority 1 : 93750000   
              Priority 2 : 93750000     Priority 3 : 93750000   
              Priority 4 : 93750000     Priority 5 : 93750000   
              Priority 6 : 93750000     Priority 7 : 93750000   
              Affinity Bit : 0x0

                OSPF Router with ID (10.229.11.11) (Process ID 2)

            Area 1 MPLS TE not initialized
            '''
        raw2 = '''\
            R1_ospf_xe#show running-config | section router ospf 1
              router ospf 1
            '''
        raw3 = '''\
            R1_ospf_xe#show running-config | section router ospf 2
              router ospf 2 vrf VRF1
            '''

        self.outputs = {}
        self.outputs['show ip ospf mpls traffic-eng link'] = raw1
        self.outputs['show running-config | section router ospf 1'] = raw2
        self.outputs['show running-config | section router ospf 2'] = raw3
        self.device.execute = Mock()
        self.device.execute.side_effect = mapper
        obj = ShowIpOspfMplsTrafficEngLink(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output1)

    def test_show_ip_ospf_mpls_traffic_eng_link_empty(self):
        self.maxDiff = None
        self.device = Mock(**self.empty_output)
        obj = ShowIpOspfMplsTrafficEngLink(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()


# =======================================
# Unit test for 'show ip ospf max-metric'
# =======================================
class test_show_ip_ospf_max_metric(unittest.TestCase):

    '''Unit test for "show ip ospf max-metric" '''

    device = Device(name='aDevice')

    empty_output = {'execute.return_value': ''}

    golden_parsed_output1 = {
        'vrf': 
            {'default': 
                {'address_family': 
                    {'ipv4': 
                        {'instance': 
                            {'1': 
                                {'router_id': '10.4.1.1',
                                'base_topology_mtid': 
                                    {'0': 
                                        {'router_lsa_max_metric': 
                                            {False: {},
                                            },
                                        'start_time': '00:01:58.313',
                                        'time_elapsed': '00:54:43.859'}}},
                            '65109': 
                                {'router_id': '10.0.187.164',
                                'base_topology_mtid': 
                                    {'0': 
                                        {'router_lsa_max_metric': 
                                            {True: 
                                                {'advertise_lsa_metric': 16711680,
                                                'condition': 'on startup for 5 seconds',
                                                'state': 'inactive',
                                                'unset_reason': 'timer expired, Originated for 5 seconds',
                                                'unset_time': '00:02:03.314',
                                                'unset_time_elapsed': '00:54:38.858',
                                                },
                                            },
                                        'start_time': '00:01:58.314',
                                        'time_elapsed': '00:54:43.858'}}}}}}}}}

    golden_output1 = {'execute.return_value': '''
        Router#sh ip ospf max-metric
        Load for five secs: 99%/0%; one minute: 89%; five minutes: 58%
        Time source is NTP, 17:13:44.700 EST Sat Nov 12 2016


                    OSPF Router with ID (10.0.187.164) (Process ID 65109)


                        Base Topology (MTID 0)

         Start time: 00:01:58.314, Time elapsed: 00:54:43.858
         Originating router-LSAs with maximum metric
            Condition: on startup for 5 seconds, State: inactive
            Advertise summary-LSAs with metric 16711680
            Unset reason: timer expired, Originated for 5 seconds
            Unset time: 00:02:03.314, Time elapsed: 00:54:38.858


                    OSPF Router with ID (10.4.1.1) (Process ID 1)


                        Base Topology (MTID 0)

         Start time: 00:01:58.313, Time elapsed: 00:54:43.859
         Router is not originating router-LSAs with maximum metric
        '''}

    golden_parsed_output2 = {'vrf': {'default': 
        {'address_family': 
            {'ipv4': 
                {'instance': 
                    {'1111': 
                        {'base_topology_mtid': 
                            {'0': 
                                {'router_lsa_max_metric': 
                                    {True: 
                                        {'condition': 'on '
                                          'startup '
                                          'for '
                                          '300 '
                                          'seconds',
                                         'state': 'active',
                                         'time_remaining': '00:03:55'}},
                                  'start_time': '00:02:24.554',
                                  'time_elapsed': '00:01:04.061'}},
                           'router_id': '10.4.1.1'}}}}}}}

    golden_output2 = {'execute.return_value': '''
        show ip ospf max-metric
        Load for five secs: 3%/0%; one minute: 3%; five minutes: 1%
        Time source is NTP, *07:52:19.838 EST Tue Jun 18 2019
        OSPF Router with ID (10.4.1.1) (Process ID 1111)
        Base Topology (MTID 0)
        Start time: 00:02:24.554, Time elapsed: 00:01:04.061
        Originating router-LSAs with maximum metric, Time remaining: 00:03:55
        Condition: on startup for 300 seconds, State: active
        '''}

    def test_show_ip_ospf_max_metric_full1(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output1)
        obj = ShowIpOspfMaxMetric(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output1)

    def test_show_ip_ospf_max_metric_full2(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output2)
        obj = ShowIpOspfMaxMetric(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output2)

    def test_show_ip_ospf_max_metric_empty(self):
        self.maxDiff = None
        self.device = Mock(**self.empty_output)
        obj = ShowIpOspfMaxMetric(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()


# ====================================
# Unit test for 'show ip ospf traffic'
# ====================================
class test_show_ip_ospf_traffic(unittest.TestCase):

    '''Unit test for "show ip ospf traffic" '''

    device = Device(name='aDevice')

    empty_output = {'execute.return_value': ''}

    golden_parsed_output1 = {
        'ospf_statistics': 
            {'last_clear_traffic_counters': 'never',
            'rcvd': 
                {'checksum_errors': 0,
                'database_desc': 938,
                'hello': 2024732,
                'link_state_acks': 75666,
                'link_state_req': 323,
                'link_state_updates': 11030,
                'total': 2112690},
            'sent': 
                {'database_desc': 1176,
                'hello': 2381794,
                'link_state_acks': 8893,
                'link_state_req': 43,
                'link_state_updates': 92224,
                'total': 2509472}},
        'vrf': 
            {'default': 
                {'address_family': 
                    {'ipv4': 
                        {'instance': 
                            {'65109': 
                                {'router_id': '10.169.197.252',
                                'ospf_queue_statistics': 
                                    {'limit': 
                                        {'inputq': 0,
                                        'outputq': 0,
                                        'updateq': 200},
                                    'drops': 
                                        {'inputq': 0,
                                        'outputq': 0,
                                        'updateq': 0},
                                    'max_delay_msec': 
                                        {'inputq': 49,
                                        'outputq': 2,
                                        'updateq': 2},
                                    'max_size': 
                                        {'total': 
                                            {'inputq': 14,
                                            'outputq': 6,
                                            'updateq': 14,
                                            },
                                        'invalid': 
                                            {'inputq': 0,
                                            'outputq': 0,
                                            'updateq': 0,
                                            },
                                        'hello': 
                                            {'inputq': 0,
                                            'outputq': 0,
                                            'updateq': 0,
                                            },
                                        'db_des': 
                                            {'inputq': 0,
                                            'outputq': 0,
                                            'updateq': 0,
                                            },
                                        'ls_req': 
                                            {'inputq': 0,
                                            'outputq': 0,
                                            'updateq': 0,
                                            },
                                        'ls_upd': 
                                            {'inputq': 0,
                                            'outputq': 0,
                                            'updateq': 0,
                                            },
                                        'ls_ack': 
                                            {'inputq': 14,
                                            'outputq': 6,
                                            'updateq': 14,
                                            },
                                        },
                                    'current_size': 
                                        {'total': 
                                            {'inputq': 0,
                                            'outputq': 0,
                                            'updateq': 0,
                                            },
                                        'invalid': 
                                            {'inputq': 0,
                                            'outputq': 0,
                                            'updateq': 0,
                                            },
                                        'hello': 
                                            {'inputq': 0,
                                            'outputq': 0,
                                            'updateq': 0,
                                            },
                                        'db_des': 
                                            {'inputq': 0,
                                            'outputq': 0,
                                            'updateq': 0,
                                            },
                                        'ls_req': 
                                            {'inputq': 0,
                                            'outputq': 0,
                                            'updateq': 0,
                                            },
                                        'ls_upd': 
                                            {'inputq': 0,
                                            'outputq': 0,
                                            'updateq': 0,
                                            },
                                        'ls_ack': 
                                            {'inputq': 0,
                                            'outputq': 0,
                                            'updateq': 0,
                                            },
                                        },
                                    },
                                'interface_statistics': 
                                    {'interfaces': 
                                        {'GigabitEthernet0/0/0': 
                                            {'last_clear_traffic_counters': 'never',
                                            'ospf_header_errors': 
                                                {'adjacency_throttle': 0,
                                                'area_mismatch': 0,
                                                'auth_type': 0,
                                                'authentication': 0,
                                                'bad_source': 0,
                                                'bfd': 0,
                                                'checksum': 0,
                                                'duplicate_id': 0,
                                                'hello': 0,
                                                'instance_id': 0,
                                                'length': 0,
                                                'lls': 0,
                                                'mtu_mismatch': 0,
                                                'nbr_ignored': 0,
                                                'no_sham_link': 0,
                                                'no_virtual_link': 0,
                                                'self_originated': 0,
                                                'test_discard': 0,
                                                'ttl_check_fail': 0,
                                                'unknown_neighbor': 1,
                                                'version': 0},
                                            'ospf_lsa_errors': 
                                                {'checksum': 0,
                                                'data': 0,
                                                'length': 0,
                                                'type': 0},
                                            'ospf_packets_received_sent': 
                                                {'type': 
                                                    {'rx_db_des': 
                                                        {'bytes': 4980,
                                                        'packets': 145},
                                                    'rx_hello': 
                                                        {'bytes': 18443216,
                                                        'packets': 384238},
                                                    'rx_invalid': 
                                                        {'bytes': 0,
                                                        'packets': 0},
                                                    'rx_ls_ack': 
                                                        {'bytes': 713980,
                                                        'packets': 11840},
                                                    'rx_ls_req': 
                                                        {'bytes': 9180,
                                                        'packets': 57},
                                                    'rx_ls_upd': 
                                                        {'bytes': 242036,
                                                        'packets': 2581},
                                                    'rx_total': 
                                                        {'bytes': 19413392,
                                                        'packets': 398861},
                                                    'tx_db_des': 
                                                        {'bytes': 50840,
                                                        'packets': 475},
                                                    'tx_failed': 
                                                        {'bytes': 0,
                                                        'packets': 0},
                                                    'tx_hello': 
                                                        {'bytes': 30825036,
                                                        'packets': 385336},
                                                    'tx_ls_ack': 
                                                        {'bytes': 187352,
                                                        'packets': 2473},
                                                    'tx_ls_req': 
                                                        {'bytes': 404,
                                                        'packets': 7},
                                                    'tx_ls_upd': 
                                                        {'bytes': 13558188,
                                                        'packets': 12658},
                                                    'tx_total': 
                                                        {'bytes': 44621820,
                                                        'packets': 400949}}}},
                                        'GigabitEthernet0/0/1': 
                                            {'last_clear_traffic_counters': 'never',
                                            'ospf_header_errors': 
                                                {'adjacency_throttle': 0,
                                                'area_mismatch': 0,
                                                'auth_type': 0,
                                                'authentication': 0,
                                                'bad_source': 0,
                                                'bfd': 0,
                                                'checksum': 0,
                                                'duplicate_id': 0,
                                                'hello': 0,
                                                'instance_id': 0,
                                                'length': 0,
                                                'lls': 0,
                                                'mtu_mismatch': 0,
                                                'nbr_ignored': 0,
                                                'no_sham_link': 0,
                                                'no_virtual_link': 0,
                                                'self_originated': 0,
                                                'test_discard': 0,
                                                'ttl_check_fail': 0,
                                                'unknown_neighbor': 0,
                                                'version': 0},
                                            'ospf_lsa_errors': 
                                                {'checksum': 0,
                                                'data': 0,
                                                'length': 0,
                                                'type': 0},
                                            'ospf_packets_received_sent': 
                                                {'type': 
                                                    {'rx_db_des': 
                                                        {'bytes': 11844,
                                                        'packets': 47},
                                                    'rx_hello': 
                                                        {'bytes': 18812552,
                                                        'packets': 391929},
                                                    'rx_invalid': 
                                                        {'bytes': 0,
                                                        'packets': 0},
                                                    'rx_ls_ack': 
                                                        {'bytes': 18804556,
                                                        'packets': 19064},
                                                    'rx_ls_req': 
                                                        {'bytes': 25212,
                                                        'packets': 22},
                                                    'rx_ls_upd': 
                                                        {'bytes': 231124,
                                                        'packets': 1902},
                                                    'rx_total': 
                                                        {'bytes': 37885288,
                                                        'packets': 412964},
                                                    'tx_db_des': 
                                                        {'bytes': 54772,
                                                        'packets': 53},
                                                    'tx_failed': 
                                                        {'bytes': 0,
                                                        'packets': 0},
                                                    'tx_hello': 
                                                        {'bytes': 31355000,
                                                        'packets': 391938},
                                                    'tx_ls_ack': 
                                                        {'bytes': 167024,
                                                        'packets': 1871},
                                                    'tx_ls_req': 
                                                        {'bytes': 6632,
                                                        'packets': 10},
                                                    'tx_ls_upd': 
                                                        {'bytes': 26983772,
                                                        'packets': 26114},
                                                    'tx_total': 
                                                        {'bytes': 58567200,
                                                        'packets': 419986}}}},
                                        'GigabitEthernet0/0/3': 
                                            {'last_clear_traffic_counters': 'never',
                                            'ospf_header_errors': 
                                                {'adjacency_throttle': 0,
                                                'area_mismatch': 0,
                                                'auth_type': 0,
                                                'authentication': 0,
                                                'bad_source': 0,
                                                'bfd': 0,
                                                'checksum': 0,
                                                'duplicate_id': 0,
                                                'hello': 0,
                                                'instance_id': 0,
                                                'length': 0,
                                                'lls': 0,
                                                'mtu_mismatch': 0,
                                                'nbr_ignored': 3,
                                                'no_sham_link': 0,
                                                'no_virtual_link': 0,
                                                'self_originated': 0,
                                                'test_discard': 0,
                                                'ttl_check_fail': 0,
                                                'unknown_neighbor': 0,
                                                'version': 0},
                                            'ospf_lsa_errors': 
                                                {'checksum': 0,
                                                'data': 0,
                                                'length': 0,
                                                'type': 0},
                                            'ospf_packets_received_sent': 
                                                {'type': 
                                                    {'rx_db_des': 
                                                        {'bytes': 25932,
                                                        'packets': 636},
                                                    'rx_hello': 
                                                        {'bytes': 20276152,
                                                        'packets': 422436},
                                                    'rx_invalid': 
                                                        {'bytes': 0,
                                                        'packets': 0},
                                                    'rx_ls_ack': 
                                                        {'bytes': 788256,
                                                        'packets': 12534},
                                                    'rx_ls_req': 
                                                        {'bytes': 29088,
                                                        'packets': 191},
                                                    'rx_ls_upd': 
                                                        {'bytes': 170236,
                                                        'packets': 1967},
                                                    'rx_total': 
                                                        {'bytes': 21289664,
                                                        'packets': 437764},
                                                    'tx_db_des': 
                                                        {'bytes': 73492,
                                                        'packets': 508},
                                                    'tx_failed': 
                                                        {'bytes': 0,
                                                        'packets': 0},
                                                    'tx_hello': 
                                                        {'bytes': 31262032,
                                                        'packets': 390845},
                                                    'tx_ls_ack': 
                                                        {'bytes': 127024,
                                                        'packets': 1956},
                                                    'tx_ls_req': 
                                                        {'bytes': 644,
                                                        'packets': 10},
                                                    'tx_ls_upd': 
                                                        {'bytes': 15890600,
                                                        'packets': 15015},
                                                    'tx_total': 
                                                        {'bytes': 47353792,
                                                        'packets': 408334}}}},
                                        'GigabitEthernet0/0/4': 
                                            {'last_clear_traffic_counters': 'never',
                                            'ospf_header_errors': 
                                                {'adjacency_throttle': 0,
                                                'area_mismatch': 0,
                                                'auth_type': 0,
                                                'authentication': 0,
                                                'bad_source': 0,
                                                'bfd': 0,
                                                'checksum': 0,
                                                'duplicate_id': 0,
                                                'hello': 0,
                                                'instance_id': 0,
                                                'length': 0,
                                                'lls': 0,
                                                'mtu_mismatch': 0,
                                                'nbr_ignored': 0,
                                                'no_sham_link': 0,
                                                'no_virtual_link': 0,
                                                'self_originated': 0,
                                                'test_discard': 0,
                                                'ttl_check_fail': 0,
                                                'unknown_neighbor': 0,
                                                'version': 0},
                                            'ospf_lsa_errors': 
                                                {'checksum': 0,
                                                'data': 0,
                                                'length': 0,
                                                'type': 0},
                                            'ospf_packets_received_sent': 
                                                {'type': 
                                                    {'rx_db_des': 
                                                        {'bytes': 524,
                                                        'packets': 12},
                                                    'rx_hello': 
                                                        {'bytes': 14716084,
                                                        'packets': 306586},
                                                    'rx_invalid': 
                                                        {'bytes': 0,
                                                        'packets': 0},
                                                    'rx_ls_ack': 
                                                        {'bytes': 613440,
                                                        'packets': 10100},
                                                    'rx_ls_req': 
                                                        {'bytes': 1032,
                                                        'packets': 6},
                                                    'rx_ls_upd': 
                                                        {'bytes': 165556,
                                                        'packets': 1706},
                                                    'rx_total': 
                                                        {'bytes': 15496636,
                                                        'packets': 318410},
                                                    'tx_db_des': 
                                                        {'bytes': 2816,
                                                        'packets': 19},
                                                    'tx_failed': 
                                                        {'bytes': 0,
                                                        'packets': 0},
                                                    'tx_hello': 
                                                        {'bytes': 24538936,
                                                        'packets': 306737},
                                                    'tx_ls_ack': 
                                                        {'bytes': 132900,
                                                        'packets': 1690},
                                                    'tx_ls_req': 
                                                        {'bytes': 336,
                                                        'packets': 6},
                                                    'tx_ls_upd': 
                                                        {'bytes': 10449232,
                                                        'packets': 11120},
                                                    'tx_total': 
                                                        {'bytes': 35124220,
                                                        'packets': 319572}}}},
                                        'GigabitEthernet0/0/5': 
                                            {'last_clear_traffic_counters': 'never',
                                            'ospf_header_errors': 
                                                {'adjacency_throttle': 0,
                                                'area_mismatch': 0,
                                                'auth_type': 0,
                                                'authentication': 0,
                                                'bad_source': 0,
                                                'bfd': 0,
                                                'checksum': 0,
                                                'duplicate_id': 0,
                                                'hello': 0,
                                                'instance_id': 0,
                                                'length': 0,
                                                'lls': 0,
                                                'mtu_mismatch': 0,
                                                'nbr_ignored': 0,
                                                'no_sham_link': 0,
                                                'no_virtual_link': 0,
                                                'self_originated': 0,
                                                'test_discard': 0,
                                                'ttl_check_fail': 0,
                                                'unknown_neighbor': 0,
                                                'version': 0},
                                            'ospf_lsa_errors': 
                                                {'checksum': 0,
                                                'data': 0,
                                                'length': 0,
                                                'type': 0},
                                            'ospf_packets_received_sent': 
                                                {'type': 
                                                    {'rx_db_des': 
                                                        {'bytes': 0,
                                                        'packets': 0},
                                                    'rx_hello': 
                                                        {'bytes': 0,
                                                        'packets': 0},
                                                    'rx_invalid': 
                                                        {'bytes': 0,
                                                        'packets': 0},
                                                    'rx_ls_ack': 
                                                        {'bytes': 0,
                                                        'packets': 0},
                                                    'rx_ls_req': 
                                                        {'bytes': 0,
                                                        'packets': 0},
                                                    'rx_ls_upd': 
                                                        {'bytes': 0,
                                                        'packets': 0},
                                                    'rx_total': 
                                                        {'bytes': 0,
                                                        'packets': 0},
                                                    'tx_db_des': 
                                                        {'bytes': 0,
                                                        'packets': 0},
                                                    'tx_failed': 
                                                        {'bytes': 0,
                                                        'packets': 0},
                                                    'tx_hello': 
                                                        {'bytes': 27731564,
                                                        'packets': 364889},
                                                    'tx_ls_ack': 
                                                        {'bytes': 0,
                                                        'packets': 0},
                                                    'tx_ls_req': 
                                                        {'bytes': 0,
                                                        'packets': 0},
                                                    'tx_ls_upd': 
                                                        {'bytes': 0,
                                                        'packets': 0},
                                                    'tx_total': 
                                                        {'bytes': 27731564,
                                                        'packets': 364889}}}},
                                        'GigabitEthernet0/0/6': 
                                            {'last_clear_traffic_counters': 'never',
                                            'ospf_header_errors': 
                                                {'adjacency_throttle': 0,
                                                'area_mismatch': 0,
                                                'auth_type': 0,
                                                'authentication': 0,
                                                'bad_source': 0,
                                                'bfd': 0,
                                                'checksum': 0,
                                                'duplicate_id': 0,
                                                'hello': 0,
                                                'instance_id': 0,
                                                'length': 0,
                                                'lls': 0,
                                                'mtu_mismatch': 0,
                                                'nbr_ignored': 0,
                                                'no_sham_link': 0,
                                                'no_virtual_link': 0,
                                                'self_originated': 0,
                                                'test_discard': 0,
                                                'ttl_check_fail': 0,
                                                'unknown_neighbor': 0,
                                                'version': 0},
                                            'ospf_lsa_errors': 
                                                {'checksum': 0,
                                                'data': 0,
                                                'length': 0,
                                                'type': 0},
                                            'ospf_packets_received_sent': 
                                                {'type': 
                                                    {'rx_db_des': 
                                                        {'bytes': 1232,
                                                        'packets': 36},
                                                    'rx_hello': 
                                                        {'bytes': 8125472,
                                                        'packets': 169281},
                                                    'rx_invalid': 
                                                        {'bytes': 0,
                                                        'packets': 0},
                                                    'rx_ls_ack': 
                                                        {'bytes': 8733808,
                                                        'packets': 9327},
                                                    'rx_ls_req': 
                                                        {'bytes': 25080,
                                                        'packets': 20},
                                                    'rx_ls_upd': 
                                                        {'bytes': 76640,
                                                        'packets': 908},
                                                    'rx_total': 
                                                        {'bytes': 16962232,
                                                        'packets': 179572},
                                                    'tx_db_des': 
                                                        {'bytes': 43560,
                                                        'packets': 40},
                                                    'tx_failed': 
                                                        {'bytes': 0,
                                                        'packets': 0},
                                                    'tx_hello': 
                                                        {'bytes': 13552440,
                                                        'packets': 169411},
                                                    'tx_ls_ack': 
                                                        {'bytes': 63396,
                                                        'packets': 899},
                                                    'tx_ls_req': 
                                                        {'bytes': 224,
                                                        'packets': 4},
                                                    'tx_ls_upd': 
                                                        {'bytes': 12553264,
                                                        'packets': 12539},
                                                    'tx_total': 
                                                        {'bytes': 26212884,
                                                        'packets': 182893}}}},
                                        'GigabitEthernet0/0/7': 
                                            {'last_clear_traffic_counters': 'never',
                                            'ospf_header_errors': 
                                                {'adjacency_throttle': 0,
                                                'area_mismatch': 0,
                                                'auth_type': 0,
                                                'authentication': 0,
                                                'bad_source': 0,
                                                'bfd': 0,
                                                'checksum': 0,
                                                'duplicate_id': 0,
                                                'hello': 0,
                                                'instance_id': 0,
                                                'length': 0,
                                                'lls': 0,
                                                'mtu_mismatch': 0,
                                                'nbr_ignored': 0,
                                                'no_sham_link': 0,
                                                'no_virtual_link': 0,
                                                'self_originated': 0,
                                                'test_discard': 0,
                                                'ttl_check_fail': 0,
                                                'unknown_neighbor': 0,
                                                'version': 0},
                                            'ospf_lsa_errors': 
                                                {'checksum': 0,
                                                'data': 0,
                                                'length': 0,
                                                'type': 0},
                                            'ospf_packets_received_sent': 
                                                {'type': 
                                                    {'rx_db_des': 
                                                        {'bytes': 2524,
                                                        'packets': 62},
                                                    'rx_hello': 
                                                        {'bytes': 16812472,
                                                        'packets': 350262},
                                                    'rx_invalid': 
                                                        {'bytes': 0,
                                                        'packets': 0},
                                                    'rx_ls_ack': 
                                                        {'bytes': 759424,
                                                        'packets': 12801},
                                                    'rx_ls_req': 
                                                        {'bytes': 4452,
                                                        'packets': 27},
                                                    'rx_ls_upd': 
                                                        {'bytes': 11921824,
                                                        'packets': 1966},
                                                    'rx_total': 
                                                        {'bytes': 29500696,
                                                        'packets': 365118},
                                                    'tx_db_des': 
                                                        {'bytes': 11964,
                                                        'packets': 81},
                                                    'tx_failed': 
                                                        {'bytes': 0,
                                                        'packets': 0},
                                                    'tx_hello': 
                                                        {'bytes': 29795828,
                                                        'packets': 372638},
                                                    'tx_ls_ack': 
                                                        {'bytes': 256,
                                                        'packets': 4},
                                                    'tx_ls_req': 
                                                        {'bytes': 336,
                                                        'packets': 6},
                                                    'tx_ls_upd': 
                                                        {'bytes': 13471532,
                                                        'packets': 14778},
                                                    'tx_total': 
                                                        {'bytes': 43279916,
                                                        'packets': 387507}}}}}},
                                'summary_traffic_statistics': 
                                    {'ospf_header_errors': 
                                        {'adjacency_throttle': 0,
                                        'area_mismatch': 0,
                                        'auth_type': 0,
                                        'authentication': 0,
                                        'bad_source': 0,
                                        'bfd': 0,
                                        'checksum': 0,
                                        'duplicate_id': 0,
                                        'hello': 0,
                                        'instance_id': 0,
                                        'length': 0,
                                        'lls': 0,
                                        'mtu_mismatch': 0,
                                        'nbr_ignored': 3,
                                        'no_sham_link': 0,
                                        'no_virtual_link': 0,
                                        'self_originated': 0,
                                        'test_discard': 0,
                                        'ttl_check_fail': 0,
                                        'unknown_neighbor': 1,
                                        'version': 0},
                                    'ospf_lsa_errors': 
                                        {'checksum': 0,
                                        'data': 0,
                                        'length': 0,
                                        'type': 0},
                                    'ospf_packets_received_sent': 
                                        {'type': 
                                            {'rx_db_des': 
                                                {'bytes': 47036,
                                                'packets': 938},
                                            'rx_hello': 
                                                {'bytes': 97185948,
                                                'packets': 2024732},
                                            'rx_invalid': 
                                                {'bytes': 0,
                                                'packets': 0},
                                            'rx_ls_ack': 
                                                {'bytes': 30413464,
                                                'packets': 75666},
                                            'rx_ls_req': 
                                                {'bytes': 94044,
                                                'packets': 323},
                                            'rx_ls_upd': 
                                                {'bytes': 12807416,
                                                'packets': 11030},
                                            'rx_total': 
                                                {'bytes': 140547908,
                                                'packets': 2112689},
                                            'tx_db_des': 
                                                {'bytes': 237444,
                                                'packets': 1176},
                                            'tx_failed': 
                                                {'bytes': 0,
                                                'packets': 0},
                                            'tx_hello': 
                                                {'bytes': 189060836,
                                                'packets': 2381794},
                                            'tx_ls_ack': 
                                                {'bytes': 677952,
                                                'packets': 8893},
                                            'tx_ls_req': 
                                                {'bytes': 8576,
                                                'packets': 43},
                                            'tx_ls_upd': 
                                                {'bytes': 92906588,
                                                'packets': 92224},
                                            'tx_total': 
                                                {'bytes': 282891396,
                                                'packets': 2484130}}}}}}}}}}}

    golden_output1 = {'execute.return_value': '''
        1006#show ip ospf traffic
        Load for five secs: 0%/0%; one minute: 0%; five minutes: 0%
        Time source is NTP, 16:43:31.626 EST Fri Oct 28 2016


        OSPF statistics:
          Last clearing of OSPF traffic counters never
          Rcvd: 2112690 total, 0 checksum errors
            2024732 hello, 938 database desc, 323 link state req
            11030 link state updates, 75666 link state acks
          Sent: 2509472 total
            2381794 hello, 1176 database desc, 43 link state req
            92224 link state updates, 8893 link state acks



                    OSPF Router with ID (10.169.197.252) (Process ID 65109)

        OSPF queue statistics for process ID 65109:

                           InputQ     UpdateQ    OutputQ
          Limit            0          200        0
          Drops            0          0          0
          Max delay [msec] 49         2          2
          Max size         14         14         6
            Invalid        0          0          0
            Hello          0          0          0
            DB des         0          0          0
            LS req         0          0          0
            LS upd         0          0          0
            LS ack         14         14         6
          Current size     0          0          0
            Invalid        0          0          0
            Hello          0          0          0
            DB des         0          0          0
            LS req         0          0          0
            LS upd         0          0          0
            LS ack         0          0          0


        Interface statistics:


            Interface GigabitEthernet0/0/6

        Last clearing of interface traffic counters never

        OSPF packets received/sent
          Type          Packets              Bytes
          RX Invalid    0                    0
          RX Hello      169281               8125472
          RX DB des     36                   1232
          RX LS req     20                   25080
          RX LS upd     908                  76640
          RX LS ack     9327                 8733808
          RX Total      179572               16962232

          TX Failed     0                    0
          TX Hello      169411               13552440
          TX DB des     40                   43560
          TX LS req     4                    224
          TX LS upd     12539                12553264
          TX LS ack     899                  63396
          TX Total      182893               26212884

        OSPF header errors
          Length 0, Instance ID 0, Checksum 0, Auth Type 0,
          Version 0, Bad Source 0, No Virtual Link 0,
          Area Mismatch 0, No Sham Link 0, Self Originated 0,
          Duplicate ID 0, Hello 0, MTU Mismatch 0,
          Nbr Ignored 0, LLS 0, Unknown Neighbor 0,
          Authentication 0, TTL Check Fail 0, Adjacency Throttle 0,
          BFD 0, Test discard 0

        OSPF LSA errors
          Type 0, Length 0, Data 0, Checksum 0



            Interface GigabitEthernet0/0/1

        Last clearing of interface traffic counters never

        OSPF packets received/sent
          Type          Packets              Bytes
          RX Invalid    0                    0
          RX Hello      391929               18812552
          RX DB des     47                   11844
          RX LS req     22                   25212
          RX LS upd     1902                 231124
          RX LS ack     19064                18804556
          RX Total      412964               37885288

          TX Failed     0                    0
          TX Hello      391938               31355000
          TX DB des     53                   54772
          TX LS req     10                   6632
          TX LS upd     26114                26983772
          TX LS ack     1871                 167024
          TX Total      419986               58567200

        OSPF header errors
          Length 0, Instance ID 0, Checksum 0, Auth Type 0,
          Version 0, Bad Source 0, No Virtual Link 0,
          Area Mismatch 0, No Sham Link 0, Self Originated 0,
          Duplicate ID 0, Hello 0, MTU Mismatch 0,
          Nbr Ignored 0, LLS 0, Unknown Neighbor 0,
          Authentication 0, TTL Check Fail 0, Adjacency Throttle 0,
          BFD 0, Test discard 0

        OSPF LSA errors
          Type 0, Length 0, Data 0, Checksum 0



            Interface GigabitEthernet0/0/4

        Last clearing of interface traffic counters never

        OSPF packets received/sent
          Type          Packets              Bytes
          RX Invalid    0                    0
          RX Hello      306586               14716084
          RX DB des     12                   524
          RX LS req     6                    1032
          RX LS upd     1706                 165556
          RX LS ack     10100                613440
          RX Total      318410               15496636

          TX Failed     0                    0
          TX Hello      306737               24538936
          TX DB des     19                   2816
          TX LS req     6                    336
          TX LS upd     11120                10449232
          TX LS ack     1690                 132900
          TX Total      319572               35124220

        OSPF header errors
          Length 0, Instance ID 0, Checksum 0, Auth Type 0,
          Version 0, Bad Source 0, No Virtual Link 0,
          Area Mismatch 0, No Sham Link 0, Self Originated 0,
          Duplicate ID 0, Hello 0, MTU Mismatch 0,
          Nbr Ignored 0, LLS 0, Unknown Neighbor 0,
          Authentication 0, TTL Check Fail 0, Adjacency Throttle 0,
          BFD 0, Test discard 0

        OSPF LSA errors
          Type 0, Length 0, Data 0, Checksum 0



            Interface GigabitEthernet0/0/0

        Last clearing of interface traffic counters never

        OSPF packets received/sent
          Type          Packets              Bytes
          RX Invalid    0                    0
          RX Hello      384238               18443216
          RX DB des     145                  4980
          RX LS req     57                   9180
          RX LS upd     2581                 242036
          RX LS ack     11840                713980
          RX Total      398861               19413392

          TX Failed     0                    0
          TX Hello      385336               30825036
          TX DB des     475                  50840
          TX LS req     7                    404
          TX LS upd     12658                13558188
          TX LS ack     2473                 187352
          TX Total      400949               44621820

        OSPF header errors
          Length 0, Instance ID 0, Checksum 0, Auth Type 0,
          Version 0, Bad Source 0, No Virtual Link 0,
          Area Mismatch 0, No Sham Link 0, Self Originated 0,
          Duplicate ID 0, Hello 0, MTU Mismatch 0,
          Nbr Ignored 0, LLS 0, Unknown Neighbor 1,
          Authentication 0, TTL Check Fail 0, Adjacency Throttle 0,
          BFD 0, Test discard 0

        OSPF LSA errors
          Type 0, Length 0, Data 0, Checksum 0



            Interface GigabitEthernet0/0/3

        Last clearing of interface traffic counters never

        OSPF packets received/sent
          Type          Packets              Bytes
          RX Invalid    0                    0
          RX Hello      422436               20276152
          RX DB des     636                  25932
          RX LS req     191                  29088
          RX LS upd     1967                 170236
          RX LS ack     12534                788256
          RX Total      437764               21289664

          TX Failed     0                    0
          TX Hello      390845               31262032
          TX DB des     508                  73492
          TX LS req     10                   644
          TX LS upd     15015                15890600
          TX LS ack     1956                 127024
          TX Total      408334               47353792

        OSPF header errors
          Length 0, Instance ID 0, Checksum 0, Auth Type 0,
          Version 0, Bad Source 0, No Virtual Link 0,
          Area Mismatch 0, No Sham Link 0, Self Originated 0,
          Duplicate ID 0, Hello 0, MTU Mismatch 0,
          Nbr Ignored 3, LLS 0, Unknown Neighbor 0,
          Authentication 0, TTL Check Fail 0, Adjacency Throttle 0,
          BFD 0, Test discard 0

        OSPF LSA errors
          Type 0, Length 0, Data 0, Checksum 0



            Interface GigabitEthernet0/0/5

        Last clearing of interface traffic counters never

        OSPF packets received/sent
          Type          Packets              Bytes
          RX Invalid    0                    0
          RX Hello      0                    0
          RX DB des     0                    0
          RX LS req     0                    0
          RX LS upd     0                    0
          RX LS ack     0                    0
          RX Total      0                    0

          TX Failed     0                    0
          TX Hello      364889               27731564
          TX DB des     0                    0
          TX LS req     0                    0
          TX LS upd     0                    0
          TX LS ack     0                    0
          TX Total      364889               27731564

        OSPF header errors
          Length 0, Instance ID 0, Checksum 0, Auth Type 0,
          Version 0, Bad Source 0, No Virtual Link 0,
          Area Mismatch 0, No Sham Link 0, Self Originated 0,
          Duplicate ID 0, Hello 0, MTU Mismatch 0,
          Nbr Ignored 0, LLS 0, Unknown Neighbor 0,
          Authentication 0, TTL Check Fail 0, Adjacency Throttle 0,
          BFD 0, Test discard 0

        OSPF LSA errors
          Type 0, Length 0, Data 0, Checksum 0



            Interface GigabitEthernet0/0/7

        Last clearing of interface traffic counters never

        OSPF packets received/sent
          Type          Packets              Bytes
          RX Invalid    0                    0
          RX Hello      350262               16812472
          RX DB des     62                   2524
          RX LS req     27                   4452
          RX LS upd     1966                 11921824
          RX LS ack     12801                759424
          RX Total      365118               29500696

          TX Failed     0                    0
          TX Hello      372638               29795828
          TX DB des     81                   11964
          TX LS req     6                    336
          TX LS upd     14778                13471532
          TX LS ack     4                    256
          TX Total      387507               43279916

        OSPF header errors
          Length 0, Instance ID 0, Checksum 0, Auth Type 0,
          Version 0, Bad Source 0, No Virtual Link 0,
          Area Mismatch 0, No Sham Link 0, Self Originated 0,
          Duplicate ID 0, Hello 0, MTU Mismatch 0,
          Nbr Ignored 0, LLS 0, Unknown Neighbor 0,
          Authentication 0, TTL Check Fail 0, Adjacency Throttle 0,
          BFD 0, Test discard 0

        OSPF LSA errors
          Type 0, Length 0, Data 0, Checksum 0



        Summary traffic statistics for process ID 65109:

        OSPF packets received/sent

          Type          Packets              Bytes
          RX Invalid    0                    0
          RX Hello      2024732              97185948
          RX DB des     938                  47036
          RX LS req     323                  94044
          RX LS upd     11030                12807416
          RX LS ack     75666                30413464
          RX Total      2112689              140547908

          TX Failed     0                    0
          TX Hello      2381794              189060836
          TX DB des     1176                 237444
          TX LS req     43                   8576
          TX LS upd     92224                92906588
          TX LS ack     8893                 677952
          TX Total      2484130              282891396

        OSPF header errors
          Length 0, Instance ID 0, Checksum 0, Auth Type 0,
          Version 0, Bad Source 0, No Virtual Link 0,
          Area Mismatch 0, No Sham Link 0, Self Originated 0,
          Duplicate ID 0, Hello 0, MTU Mismatch 0,
          Nbr Ignored 3, LLS 0, Unknown Neighbor 1,
          Authentication 0, TTL Check Fail 0, Adjacency Throttle 0,
          BFD 0, Test discard 0

        OSPF LSA errors
          Type 0, Length 0, Data 0, Checksum 0

        1006#
        '''}

    golden_parsed_output = {
        'ospf_statistics': {
            'last_clear_traffic_counters': 'never',
            'rcvd': {
                'total': 1082870,
                'checksum_errors': 0,
                'hello': 961667,
                'database_desc': 1688,
                'link_state_req': 32,
                'link_state_updates': 94694,
                'link_state_acks': 24370,
            },
            'sent': {
                'total': 1072239,
                'hello': 932534,
                'database_desc': 1251,
                'link_state_req': 170,
                'link_state_updates': 74590,
                'link_state_acks': 63700,
            },
        },
        'vrf': {
            'default': {
                'address_family': {
                    'ipv4': {
                        'instance': {
                            '888': {
                                'router_id': '192.168.36.220',
                                'ospf_queue_statistics': {
                                    'limit': {
                                        'inputq': 0,
                                        'updateq': 200,
                                        'outputq': 0,
                                    },
                                    'drops': {
                                        'inputq': 0,
                                        'updateq': 0,
                                        'outputq': 0,
                                    },
                                    'max_delay_msec': {
                                        'inputq': 344,
                                        'updateq': 269,
                                        'outputq': 12,
                                    },
                                    'max_size': {
                                        'total': {
                                            'inputq': 5,
                                            'updateq': 5,
                                            'outputq': 2,
                                        },
                                        'invalid': {
                                            'inputq': 0,
                                            'updateq': 0,
                                            'outputq': 0,
                                        },
                                        'hello': {
                                            'inputq': 1,
                                            'updateq': 0,
                                            'outputq': 1,
                                        },
                                        'db_des': {
                                            'inputq': 2,
                                            'updateq': 0,
                                            'outputq': 1,
                                        },
                                        'ls_req': {
                                            'inputq': 0,
                                            'updateq': 0,
                                            'outputq': 0,
                                        },
                                        'ls_upd': {
                                            'inputq': 2,
                                            'updateq': 5,
                                            'outputq': 0,
                                        },
                                        'ls_ack': {
                                            'inputq': 0,
                                            'updateq': 0,
                                            'outputq': 0,
                                        },
                                    },
                                    'current_size': {
                                        'total': {
                                            'inputq': 0,
                                            'updateq': 0,
                                            'outputq': 0,
                                        },
                                        'invalid': {
                                            'inputq': 0,
                                            'updateq': 0,
                                            'outputq': 0,
                                        },
                                        'hello': {
                                            'inputq': 0,
                                            'updateq': 0,
                                            'outputq': 0,
                                        },
                                        'db_des': {
                                            'inputq': 0,
                                            'updateq': 0,
                                            'outputq': 0,
                                        },
                                        'ls_req': {
                                            'inputq': 0,
                                            'updateq': 0,
                                            'outputq': 0,
                                        },
                                        'ls_upd': {
                                            'inputq': 0,
                                            'updateq': 0,
                                            'outputq': 0,
                                        },
                                        'ls_ack': {
                                            'inputq': 0,
                                            'updateq': 0,
                                            'outputq': 0,
                                        },
                                    },
                                },
                                'interface_statistics': {
                                    'interfaces': {
                                        'GigabitEthernet0/0/0': {
                                            'last_clear_traffic_counters': 'never',
                                            'ospf_packets_received_sent': {
                                                'type': {
                                                    'rx_invalid': {
                                                        'packets': 0,
                                                        'bytes': 0,
                                                    },
                                                    'rx_hello': {
                                                        'packets': 495694,
                                                        'bytes': 23793308,
                                                    },
                                                    'rx_db_des': {
                                                        'packets': 1676,
                                                        'bytes': 298812,
                                                    },
                                                    'rx_ls_req': {
                                                        'packets': 30,
                                                        'bytes': 1392,
                                                    },
                                                    'rx_ls_upd': {
                                                        'packets': 46764,
                                                        'bytes': 4399320,
                                                    },
                                                    'rx_ls_ack': {
                                                        'packets': 6580,
                                                        'bytes': 316460,
                                                    },
                                                    'rx_total': {
                                                        'packets': 550744,
                                                        'bytes': 28809292,
                                                    },
                                                    'tx_failed': {
                                                        'packets': 0,
                                                        'bytes': 0,
                                                    },
                                                    'tx_hello': {
                                                        'packets': 466574,
                                                        'bytes': 37324132,
                                                    },
                                                    'tx_db_des': {
                                                        'packets': 1238,
                                                        'bytes': 326112,
                                                    },
                                                    'tx_ls_req': {
                                                        'packets': 169,
                                                        'bytes': 10388,
                                                    },
                                                    'tx_ls_upd': {
                                                        'packets': 47473,
                                                        'bytes': 4865652,
                                                    },
                                                    'tx_ls_ack': {
                                                        'packets': 36140,
                                                        'bytes': 2827140,
                                                    },
                                                    'tx_total': {
                                                        'packets': 551594,
                                                        'bytes': 45353424,
                                                    },
                                                },
                                            },
                                            'ospf_header_errors': {
                                                'length': 0,
                                                'instance_id': 0,
                                                'checksum': 0,
                                                'auth_type': 0,
                                                'version': 0,
                                                'bad_source': 0,
                                                'no_virtual_link': 0,
                                                'area_mismatch': 0,
                                                'no_sham_link': 0,
                                                'self_originated': 0,
                                                'duplicate_id': 0,
                                                'hello': 0,
                                                'mtu_mismatch': 0,
                                                'nbr_ignored': 0,
                                                'lls': 0,
                                                'unknown_neighbor': 419,
                                                'authentication': 0,
                                                'ttl_check_fail': 0,
                                                'test_discard': 0,
                                            },
                                            'ospf_lsa_errors': {
                                                'type': 0,
                                                'length': 0,
                                                'data': 0,
                                                'checksum': 0,
                                            },
                                        },
                                        'TenGigabitEthernet0/2/0': {
                                            'last_clear_traffic_counters': 'never',
                                            'ospf_packets_received_sent': {
                                                'type': {
                                                    'rx_invalid': {
                                                        'packets': 0,
                                                        'bytes': 0,
                                                    },
                                                    'rx_hello': {
                                                        'packets': 465973,
                                                        'bytes': 22366692,
                                                    },
                                                    'rx_db_des': {
                                                        'packets': 12,
                                                        'bytes': 1764,
                                                    },
                                                    'rx_ls_req': {
                                                        'packets': 2,
                                                        'bytes': 312,
                                                    },
                                                    'rx_ls_upd': {
                                                        'packets': 47930,
                                                        'bytes': 4445532,
                                                    },
                                                    'rx_ls_ack': {
                                                        'packets': 17790,
                                                        'bytes': 971660,
                                                    },
                                                    'rx_total': {
                                                        'packets': 531707,
                                                        'bytes': 27785960,
                                                    },
                                                    'tx_failed': {
                                                        'packets': 0,
                                                        'bytes': 0,
                                                    },
                                                    'tx_hello': {
                                                        'packets': 465960,
                                                        'bytes': 37276652,
                                                    },
                                                    'tx_db_des': {
                                                        'packets': 13,
                                                        'bytes': 2592,
                                                    },
                                                    'tx_ls_req': {
                                                        'packets': 1,
                                                        'bytes': 56,
                                                    },
                                                    'tx_ls_upd': {
                                                        'packets': 27117,
                                                        'bytes': 2661612,
                                                    },
                                                    'tx_ls_ack': {
                                                        'packets': 27560,
                                                        'bytes': 2130760,
                                                    },
                                                    'tx_total': {
                                                        'packets': 520651,
                                                        'bytes': 42071672,
                                                    },
                                                },
                                            },
                                            'ospf_header_errors': {
                                                'length': 0,
                                                'instance_id': 0,
                                                'checksum': 0,
                                                'auth_type': 0,
                                                'version': 0,
                                                'bad_source': 0,
                                                'no_virtual_link': 0,
                                                'area_mismatch': 0,
                                                'no_sham_link': 0,
                                                'self_originated': 0,
                                                'duplicate_id': 0,
                                                'hello': 0,
                                                'mtu_mismatch': 0,
                                                'nbr_ignored': 0,
                                                'lls': 0,
                                                'unknown_neighbor': 0,
                                                'authentication': 0,
                                                'ttl_check_fail': 0,
                                                'test_discard': 0,
                                            },
                                            'ospf_lsa_errors': {
                                                'type': 0,
                                                'length': 0,
                                                'data': 0,
                                                'checksum': 0,
                                            },
                                        },
                                    },
                                },
                                'summary_traffic_statistics': {
                                    'ospf_packets_received_sent': {
                                        'type': {
                                            'rx_invalid': {
                                                'packets': 0,
                                                'bytes': 0,
                                            },
                                            'rx_hello': {
                                                'packets': 961667,
                                                'bytes': 46160000,
                                            },
                                            'rx_db_des': {
                                                'packets': 1688,
                                                'bytes': 300576,
                                            },
                                            'rx_ls_req': {
                                                'packets': 32,
                                                'bytes': 1704,
                                            },
                                            'rx_ls_upd': {
                                                'packets': 94694,
                                                'bytes': 8844852,
                                            },
                                            'rx_ls_ack': {
                                                'packets': 24370,
                                                'bytes': 1288120,
                                            },
                                            'rx_total': {
                                                'packets': 1082451,
                                                'bytes': 56595252,
                                            },
                                            'tx_failed': {
                                                'packets': 0,
                                                'bytes': 0,
                                            },
                                            'tx_hello': {
                                                'packets': 932534,
                                                'bytes': 74600784,
                                            },
                                            'tx_db_des': {
                                                'packets': 1251,
                                                'bytes': 328704,
                                            },
                                            'tx_ls_req': {
                                                'packets': 170,
                                                'bytes': 10444,
                                            },
                                            'tx_ls_upd': {
                                                'packets': 74590,
                                                'bytes': 7527264,
                                            },
                                            'tx_ls_ack': {
                                                'packets': 63700,
                                                'bytes': 4957900,
                                            },
                                            'tx_total': {
                                                'packets': 1072245,
                                                'bytes': 87425096,
                                            },
                                        },
                                    },
                                    'ospf_header_errors': {
                                        'length': 0,
                                        'instance_id': 0,
                                        'checksum': 0,
                                        'auth_type': 0,
                                        'version': 0,
                                        'bad_source': 0,
                                        'no_virtual_link': 0,
                                        'area_mismatch': 0,
                                        'no_sham_link': 0,
                                        'self_originated': 0,
                                        'duplicate_id': 0,
                                        'hello': 0,
                                        'mtu_mismatch': 0,
                                        'nbr_ignored': 0,
                                        'lls': 0,
                                        'unknown_neighbor': 419,
                                        'authentication': 0,
                                        'ttl_check_fail': 0,
                                        'test_discard': 0,
                                    },
                                    'ospf_lsa_errors': {
                                        'type': 0,
                                        'length': 0,
                                        'data': 0,
                                        'checksum': 0,
                                    },
                                },
                            },
                        },
                    },
                },
            },
        },
    }
    golden_output = {'execute.return_value': '''
        show ip ospf traffic
        Load for five secs: 6%/1%; one minute: 20%; five minutes: 14%
        Time source is NTP, 01:06:03.667 EST Thu Jan 2 2020


        OSPF statistics:
        Last clearing of OSPF traffic counters never
        Rcvd: 1082870 total, 0 checksum errors
            961667 hello, 1688 database desc, 32 link state req
            94694 link state updates, 24370 link state acks
        Sent: 1072239 total
            932534 hello, 1251 database desc, 170 link state req
            74590 link state updates, 63700 link state acks

                    OSPF Router with ID (192.168.36.220) (Process ID 888)

        OSPF queue statistics for process ID 888:

                        InputQ     UpdateQ    OutputQ
        Limit            0          200        0         
        Drops            0          0          0         
        Max delay [msec] 344        269        12        
        Max size         5          5          2         
            Invalid        0          0          0         
            Hello          1          0          1         
            DB des         2          0          1         
            LS req         0          0          0         
            LS upd         2          5          0         
            LS ack         0          0          0         
        Current size     0          0          0         
            Invalid        0          0          0         
            Hello          0          0          0         
            DB des         0          0          0         
            LS req         0          0          0         
            LS upd         0          0          0         
            LS ack         0          0          0         


        Interface statistics:


            Interface GigabitEthernet0/0/0

        Last clearing of interface traffic counters never

        OSPF packets received/sent
        Type          Packets              Bytes
        RX Invalid    0                    0
        RX Hello      495694               23793308
        RX DB des     1676                 298812
        RX LS req     30                   1392
        RX LS upd     46764                4399320
        RX LS ack     6580                 316460
        RX Total      550744               28809292

        TX Failed     0                    0
        TX Hello      466574               37324132
        TX DB des     1238                 326112
        TX LS req     169                  10388
        TX LS upd     47473                4865652
        TX LS ack     36140                2827140
        TX Total      551594               45353424

        OSPF header errors
        Length 0, Instance ID 0, Checksum 0, Auth Type 0,
        Version 0, Bad Source 0, No Virtual Link 0,
        Area Mismatch 0, No Sham Link 0, Self Originated 0,
        Duplicate ID 0, Hello 0, MTU Mismatch 0,
        Nbr Ignored 0, LLS 0, Unknown Neighbor 419,
        Authentication 0, TTL Check Fail 0, Test discard 0

        OSPF LSA errors
        Type 0, Length 0, Data 0, Checksum 0



            Interface TenGigabitEthernet0/2/0

        Last clearing of interface traffic counters never

        OSPF packets received/sent
        Type          Packets              Bytes
        RX Invalid    0                    0
        RX Hello      465973               22366692
        RX DB des     12                   1764
        RX LS req     2                    312
        RX LS upd     47930                4445532
        RX LS ack     17790                971660
        RX Total      531707               27785960

        TX Failed     0                    0
        TX Hello      465960               37276652
        TX DB des     13                   2592
        TX LS req     1                    56
        TX LS upd     27117                2661612
        TX LS ack     27560                2130760
        TX Total      520651               42071672

        OSPF header errors
        Length 0, Instance ID 0, Checksum 0, Auth Type 0,
        Version 0, Bad Source 0, No Virtual Link 0,
        Area Mismatch 0, No Sham Link 0, Self Originated 0,
        Duplicate ID 0, Hello 0, MTU Mismatch 0,
        Nbr Ignored 0, LLS 0, Unknown Neighbor 0,
        Authentication 0, TTL Check Fail 0, Test discard 0

        OSPF LSA errors
        Type 0, Length 0, Data 0, Checksum 0



        Summary traffic statistics for process ID 888:

        OSPF packets received/sent

        Type          Packets              Bytes
        RX Invalid    0                    0
        RX Hello      961667               46160000
        RX DB des     1688                 300576
        RX LS req     32                   1704
        RX LS upd     94694                8844852
        RX LS ack     24370                1288120
        RX Total      1082451              56595252

        TX Failed     0                    0
        TX Hello      932534               74600784
        TX DB des     1251                 328704
        TX LS req     170                  10444
        TX LS upd     74590                7527264
        TX LS ack     63700                4957900
        TX Total      1072245              87425096

        OSPF header errors
        Length 0, Instance ID 0, Checksum 0, Auth Type 0,
        Version 0, Bad Source 0, No Virtual Link 0,
        Area Mismatch 0, No Sham Link 0, Self Originated 0,
        Duplicate ID 0, Hello 0, MTU Mismatch 0,
        Nbr Ignored 0, LLS 0, Unknown Neighbor 419,
        Authentication 0, TTL Check Fail 0, Test discard 0

        OSPF LSA errors
        Type 0, Length 0, Data 0, Checksum 0
    '''}

    golden_parsed_output2 = {
        'vrf': {
            'default': {
                'address_family': {
                    'ipv4': {
                        'instance': {
                            '10000': {
                                'summary_traffic_statistics': {
                                    'ospf_packets_received_sent': {
                                        'type': {
                                            'rx_invalid': {
                                                'packets': 0,
                                                'bytes': 0,
                                            },
                                            'rx_hello': {
                                                'packets': 0,
                                                'bytes': 0,
                                            },
                                            'rx_db_des': {
                                                'packets': 0,
                                                'bytes': 0,
                                            },
                                            'rx_ls_req': {
                                                'packets': 0,
                                                'bytes': 0,
                                            },
                                            'rx_ls_upd': {
                                                'packets': 0,
                                                'bytes': 0,
                                            },
                                            'rx_ls_ack': {
                                                'packets': 0,
                                                'bytes': 0,
                                            },
                                            'rx_total': {
                                                'packets': 0,
                                                'bytes': 0,
                                            },
                                            'tx_failed': {
                                                'packets': 0,
                                                'bytes': 0,
                                            },
                                            'tx_hello': {
                                                'packets': 0,
                                                'bytes': 0,
                                            },
                                            'tx_db_des': {
                                                'packets': 0,
                                                'bytes': 0,
                                            },
                                            'tx_ls_req': {
                                                'packets': 0,
                                                'bytes': 0,
                                            },
                                            'tx_ls_upd': {
                                                'packets': 0,
                                                'bytes': 0,
                                            },
                                            'tx_ls_ack': {
                                                'packets': 0,
                                                'bytes': 0,
                                            },
                                            'tx_total': {
                                                'packets': 0,
                                                'bytes': 0,
                                            },
                                        },
                                    },
                                    'ospf_header_errors': {
                                        'length': 0,
                                        'instance_id': 0,
                                        'checksum': 0,
                                        'auth_type': 0,
                                        'version': 0,
                                        'bad_source': 0,
                                        'no_virtual_link': 0,
                                        'area_mismatch': 0,
                                        'no_sham_link': 0,
                                        'self_originated': 0,
                                        'duplicate_id': 0,
                                        'hello': 0,
                                        'mtu_mismatch': 0,
                                        'nbr_ignored': 0,
                                        'lls': 0,
                                        'unknown_neighbor': 0,
                                        'authentication': 0,
                                        'ttl_check_fail': 0,
                                        'adjacency_throttle': 0,
                                        'bfd': 0,
                                        'test_discard': 0,
                                    },
                                    'ospf_lsa_errors': {
                                        'type': 0,
                                        'length': 0,
                                        'data': 0,
                                        'checksum': 0,
                                    },
                                },
                            },
                            '888': {
                                'router_id': '10.19.13.14',
                                'ospf_queue_statistics': {
                                    'limit': {
                                        'inputq': 0,
                                        'updateq': 200,
                                        'outputq': 0,
                                    },
                                    'drops': {
                                        'inputq': 0,
                                        'updateq': 0,
                                        'outputq': 0,
                                    },
                                    'max_delay_msec': {
                                        'inputq': 3,
                                        'updateq': 2,
                                        'outputq': 1,
                                    },
                                    'max_size': {
                                        'total': {
                                            'inputq': 4,
                                            'updateq': 3,
                                            'outputq': 2,
                                        },
                                        'invalid': {
                                            'inputq': 0,
                                            'updateq': 0,
                                            'outputq': 0,
                                        },
                                        'hello': {
                                            'inputq': 4,
                                            'updateq': 0,
                                            'outputq': 1,
                                        },
                                        'db_des': {
                                            'inputq': 0,
                                            'updateq': 0,
                                            'outputq': 1,
                                        },
                                        'ls_req': {
                                            'inputq': 0,
                                            'updateq': 0,
                                            'outputq': 0,
                                        },
                                        'ls_upd': {
                                            'inputq': 0,
                                            'updateq': 3,
                                            'outputq': 0,
                                        },
                                        'ls_ack': {
                                            'inputq': 0,
                                            'updateq': 0,
                                            'outputq': 0,
                                        },
                                    },
                                    'current_size': {
                                        'total': {
                                            'inputq': 0,
                                            'updateq': 0,
                                            'outputq': 0,
                                        },
                                        'invalid': {
                                            'inputq': 0,
                                            'updateq': 0,
                                            'outputq': 0,
                                        },
                                        'hello': {
                                            'inputq': 0,
                                            'updateq': 0,
                                            'outputq': 0,
                                        },
                                        'db_des': {
                                            'inputq': 0,
                                            'updateq': 0,
                                            'outputq': 0,
                                        },
                                        'ls_req': {
                                            'inputq': 0,
                                            'updateq': 0,
                                            'outputq': 0,
                                        },
                                        'ls_upd': {
                                            'inputq': 0,
                                            'updateq': 0,
                                            'outputq': 0,
                                        },
                                        'ls_ack': {
                                            'inputq': 0,
                                            'updateq': 0,
                                            'outputq': 0,
                                        },
                                    },
                                },
                                'interface_statistics': {
                                    'interfaces': {
                                        'Tunnel65541': {
                                            'last_clear_traffic_counters': 'never',
                                            'ospf_packets_received_sent': {
                                                'type': {
                                                    'rx_invalid': {
                                                        'packets': 0,
                                                        'bytes': 0,
                                                    },
                                                    'rx_hello': {
                                                        'packets': 0,
                                                        'bytes': 0,
                                                    },
                                                    'rx_db_des': {
                                                        'packets': 0,
                                                        'bytes': 0,
                                                    },
                                                    'rx_ls_req': {
                                                        'packets': 0,
                                                        'bytes': 0,
                                                    },
                                                    'rx_ls_upd': {
                                                        'packets': 0,
                                                        'bytes': 0,
                                                    },
                                                    'rx_ls_ack': {
                                                        'packets': 0,
                                                        'bytes': 0,
                                                    },
                                                    'rx_total': {
                                                        'packets': 0,
                                                        'bytes': 0,
                                                    },
                                                    'tx_failed': {
                                                        'packets': 0,
                                                        'bytes': 0,
                                                    },
                                                    'tx_hello': {
                                                        'packets': 62301,
                                                        'bytes': 5980896,
                                                    },
                                                    'tx_db_des': {
                                                        'packets': 0,
                                                        'bytes': 0,
                                                    },
                                                    'tx_ls_req': {
                                                        'packets': 0,
                                                        'bytes': 0,
                                                    },
                                                    'tx_ls_upd': {
                                                        'packets': 0,
                                                        'bytes': 0,
                                                    },
                                                    'tx_ls_ack': {
                                                        'packets': 0,
                                                        'bytes': 0,
                                                    },
                                                    'tx_total': {
                                                        'packets': 62301,
                                                        'bytes': 5980896,
                                                    },
                                                },
                                            },
                                            'ospf_header_errors': {
                                                'length': 0,
                                                'instance_id': 0,
                                                'checksum': 0,
                                                'auth_type': 0,
                                                'version': 0,
                                                'bad_source': 0,
                                                'no_virtual_link': 0,
                                                'area_mismatch': 0,
                                                'no_sham_link': 0,
                                                'self_originated': 0,
                                                'duplicate_id': 0,
                                                'hello': 0,
                                                'mtu_mismatch': 0,
                                                'nbr_ignored': 0,
                                                'lls': 0,
                                                'unknown_neighbor': 0,
                                                'authentication': 0,
                                                'ttl_check_fail': 0,
                                                'adjacency_throttle': 0,
                                                'bfd': 0,
                                                'test_discard': 0,
                                            },
                                            'ospf_lsa_errors': {
                                                'type': 0,
                                                'length': 0,
                                                'data': 0,
                                                'checksum': 0,
                                            },
                                        },
                                        'GigabitEthernet0/1/7': {
                                            'last_clear_traffic_counters': 'never',
                                            'ospf_packets_received_sent': {
                                                'type': {
                                                    'rx_invalid': {
                                                        'packets': 0,
                                                        'bytes': 0,
                                                    },
                                                    'rx_hello': {
                                                        'packets': 70493,
                                                        'bytes': 3383664,
                                                    },
                                                    'rx_db_des': {
                                                        'packets': 3,
                                                        'bytes': 1676,
                                                    },
                                                    'rx_ls_req': {
                                                        'packets': 1,
                                                        'bytes': 36,
                                                    },
                                                    'rx_ls_upd': {
                                                        'packets': 14963,
                                                        'bytes': 1870388,
                                                    },
                                                    'rx_ls_ack': {
                                                        'packets': 880,
                                                        'bytes': 76140,
                                                    },
                                                    'rx_total': {
                                                        'packets': 86340,
                                                        'bytes': 5331904,
                                                    },
                                                    'tx_failed': {
                                                        'packets': 0,
                                                        'bytes': 0,
                                                    },
                                                    'tx_hello': {
                                                        'packets': 1,
                                                        'bytes': 100,
                                                    },
                                                    'tx_db_des': {
                                                        'packets': 4,
                                                        'bytes': 416,
                                                    },
                                                    'tx_ls_req': {
                                                        'packets': 1,
                                                        'bytes': 968,
                                                    },
                                                    'tx_ls_upd': {
                                                        'packets': 1,
                                                        'bytes': 108,
                                                    },
                                                    'tx_ls_ack': {
                                                        'packets': 134,
                                                        'bytes': 9456,
                                                    },
                                                    'tx_total': {
                                                        'packets': 141,
                                                        'bytes': 11048,
                                                    },
                                                },
                                            },
                                            'ospf_header_errors': {
                                                'length': 0,
                                                'instance_id': 0,
                                                'checksum': 0,
                                                'auth_type': 0,
                                                'version': 0,
                                                'bad_source': 0,
                                                'no_virtual_link': 0,
                                                'area_mismatch': 0,
                                                'no_sham_link': 0,
                                                'self_originated': 0,
                                                'duplicate_id': 0,
                                                'hello': 0,
                                                'mtu_mismatch': 0,
                                                'nbr_ignored': 0,
                                                'lls': 0,
                                                'unknown_neighbor': 0,
                                                'authentication': 0,
                                                'ttl_check_fail': 0,
                                                'adjacency_throttle': 0,
                                                'bfd': 0,
                                                'test_discard': 0,
                                            },
                                            'ospf_lsa_errors': {
                                                'type': 0,
                                                'length': 0,
                                                'data': 0,
                                                'checksum': 0,
                                            },
                                        },
                                        'GigabitEthernet0/1/6': {
                                            'last_clear_traffic_counters': 'never',
                                            'ospf_packets_received_sent': {
                                                'type': {
                                                    'rx_invalid': {
                                                        'packets': 0,
                                                        'bytes': 0,
                                                    },
                                                    'rx_hello': {
                                                        'packets': 70504,
                                                        'bytes': 3384192,
                                                    },
                                                    'rx_db_des': {
                                                        'packets': 3,
                                                        'bytes': 1676,
                                                    },
                                                    'rx_ls_req': {
                                                        'packets': 1,
                                                        'bytes': 36,
                                                    },
                                                    'rx_ls_upd': {
                                                        'packets': 14809,
                                                        'bytes': 1866264,
                                                    },
                                                    'rx_ls_ack': {
                                                        'packets': 877,
                                                        'bytes': 76028,
                                                    },
                                                    'rx_total': {
                                                        'packets': 86194,
                                                        'bytes': 5328196,
                                                    },
                                                    'tx_failed': {
                                                        'packets': 0,
                                                        'bytes': 0,
                                                    },
                                                    'tx_hello': {
                                                        'packets': 1,
                                                        'bytes': 100,
                                                    },
                                                    'tx_db_des': {
                                                        'packets': 4,
                                                        'bytes': 416,
                                                    },
                                                    'tx_ls_req': {
                                                        'packets': 1,
                                                        'bytes': 968,
                                                    },
                                                    'tx_ls_upd': {
                                                        'packets': 1,
                                                        'bytes': 108,
                                                    },
                                                    'tx_ls_ack': {
                                                        'packets': 117,
                                                        'bytes': 8668,
                                                    },
                                                    'tx_total': {
                                                        'packets': 124,
                                                        'bytes': 10260,
                                                    },
                                                },
                                            },
                                            'ospf_header_errors': {
                                                'length': 0,
                                                'instance_id': 0,
                                                'checksum': 0,
                                                'auth_type': 0,
                                                'version': 0,
                                                'bad_source': 0,
                                                'no_virtual_link': 0,
                                                'area_mismatch': 0,
                                                'no_sham_link': 0,
                                                'self_originated': 0,
                                                'duplicate_id': 0,
                                                'hello': 0,
                                                'mtu_mismatch': 0,
                                                'nbr_ignored': 0,
                                                'lls': 0,
                                                'unknown_neighbor': 0,
                                                'authentication': 0,
                                                'ttl_check_fail': 0,
                                                'adjacency_throttle': 0,
                                                'bfd': 0,
                                                'test_discard': 0,
                                            },
                                            'ospf_lsa_errors': {
                                                'type': 0,
                                                'length': 0,
                                                'data': 0,
                                                'checksum': 0,
                                            },
                                        },
                                    },
                                },
                                'summary_traffic_statistics': {
                                    'ospf_packets_received_sent': {
                                        'type': {
                                            'rx_invalid': {
                                                'packets': 0,
                                                'bytes': 0,
                                            },
                                            'rx_hello': {
                                                'packets': 159187,
                                                'bytes': 7640968,
                                            },
                                            'rx_db_des': {
                                                'packets': 10240,
                                                'bytes': 337720,
                                            },
                                            'rx_ls_req': {
                                                'packets': 5,
                                                'bytes': 216,
                                            },
                                            'rx_ls_upd': {
                                                'packets': 31899,
                                                'bytes': 4010656,
                                            },
                                            'rx_ls_ack': {
                                                'packets': 2511,
                                                'bytes': 201204,
                                            },
                                            'rx_total': {
                                                'packets': 203842,
                                                'bytes': 12190764,
                                            },
                                            'tx_failed': {
                                                'packets': 0,
                                                'bytes': 0,
                                            },
                                            'tx_hello': {
                                                'packets': 208493,
                                                'bytes': 20592264,
                                            },
                                            'tx_db_des': {
                                                'packets': 10540,
                                                'bytes': 15808320,
                                            },
                                            'tx_ls_req': {
                                                'packets': 5,
                                                'bytes': 3112,
                                            },
                                            'tx_ls_upd': {
                                                'packets': 33998,
                                                'bytes': 5309252,
                                            },
                                            'tx_ls_ack': {
                                                'packets': 17571,
                                                'bytes': 1220144,
                                            },
                                            'tx_total': {
                                                'packets': 270607,
                                                'bytes': 42933092,
                                            },
                                        },
                                    },
                                    'ospf_header_errors': {
                                        'length': 0,
                                        'instance_id': 0,
                                        'checksum': 0,
                                        'auth_type': 0,
                                        'version': 0,
                                        'bad_source': 0,
                                        'no_virtual_link': 0,
                                        'area_mismatch': 0,
                                        'no_sham_link': 0,
                                        'self_originated': 0,
                                        'duplicate_id': 0,
                                        'hello': 0,
                                        'mtu_mismatch': 0,
                                        'nbr_ignored': 2682,
                                        'lls': 0,
                                        'unknown_neighbor': 0,
                                        'authentication': 0,
                                        'ttl_check_fail': 0,
                                        'adjacency_throttle': 0,
                                        'bfd': 0,
                                        'test_discard': 0,
                                    },
                                    'ospf_lsa_errors': {
                                        'type': 0,
                                        'length': 0,
                                        'data': 0,
                                        'checksum': 0,
                                    },
                                },
                            },
                        },
                    },
                },
            },
        },
        'ospf_statistics': {
            'last_clear_traffic_counters': 'never',
            'rcvd': {
                'total': 204136,
                'checksum_errors': 0,
                'hello': 159184,
                'database_desc': 10240,
                'link_state_req': 5,
                'link_state_updates': 31899,
                'link_state_acks': 2511,
            },
            'sent': {
                'total': 281838,
                'hello': 219736,
                'database_desc': 10540,
                'link_state_req': 5,
                'link_state_updates': 33998,
                'link_state_acks': 17571,
            },
        },
    }
    golden_output2 = {'execute.return_value': '''
        show ip ospf traffic

        Summary traffic statistics for process ID 10000:

        OSPF packets received/sent

        Type          Packets              Bytes
        RX Invalid    0                    0
        RX Hello      0                    0
        RX DB des     0                    0
        RX LS req     0                    0
        RX LS upd     0                    0
        RX LS ack     0                    0
        RX Total      0                    0

        TX Failed     0                    0
        TX Hello      0                    0
        TX DB des     0                    0
        TX LS req     0                    0
        TX LS upd     0                    0
        TX LS ack     0                    0
        TX Total      0                    0

        OSPF header errors
        Length 0, Instance ID 0, Checksum 0, Auth Type 0,
        Version 0, Bad Source 0, No Virtual Link 0,
        Area Mismatch 0, No Sham Link 0, Self Originated 0,
        Duplicate ID 0, Hello 0, MTU Mismatch 0,
        Nbr Ignored 0, LLS 0, Unknown Neighbor 0,
        Authentication 0, TTL Check Fail 0, Adjacency Throttle 0,
        BFD 0, Test discard 0

        OSPF LSA errors
        Type 0, Length 0, Data 0, Checksum 0


        OSPF statistics:
        Last clearing of OSPF traffic counters never
        Rcvd: 204136 total, 0 checksum errors
                159184 hello, 10240 database desc, 5 link state req
                31899 link state updates, 2511 link state acks
        Sent: 281838 total
                219736 hello, 10540 database desc, 5 link state req
                33998 link state updates, 17571 link state acks



                    OSPF Router with ID (10.19.13.14) (Process ID 888)

        OSPF queue statistics for process ID 888:

                        InputQ     UpdateQ    OutputQ
        Limit            0          200        0
        Drops            0          0          0
        Max delay [msec] 3          2          1
        Max size         4          3          2
            Invalid        0          0          0
            Hello          4          0          1
            DB des         0          0          1
            LS req         0          0          0
            LS upd         0          3          0
            LS ack         0          0          0
        Current size     0          0          0
            Invalid        0          0          0
            Hello          0          0          0
            DB des         0          0          0
            LS req         0          0          0
            LS upd         0          0          0
            LS ack         0          0          0


        Interface statistics:


            Interface Tunnel65541

        Last clearing of interface traffic counters never

        OSPF packets received/sent
        Type          Packets              Bytes
        RX Invalid    0                    0
        RX Hello      0                    0
        RX DB des     0                    0
        RX LS req     0                    0
        RX LS upd     0                    0
        RX LS ack     0                    0
        RX Total      0                    0

        TX Failed     0                    0
        TX Hello      62301                5980896
        TX DB des     0                    0
        TX LS req     0                    0
        TX LS upd     0                    0
        TX LS ack     0                    0
        TX Total      62301                5980896

        OSPF header errors
        Length 0, Instance ID 0, Checksum 0, Auth Type 0,
        Version 0, Bad Source 0, No Virtual Link 0,
        Area Mismatch 0, No Sham Link 0, Self Originated 0,
        Duplicate ID 0, Hello 0, MTU Mismatch 0,
        Nbr Ignored 0, LLS 0, Unknown Neighbor 0,
        Authentication 0, TTL Check Fail 0, Adjacency Throttle 0,
        BFD 0, Test discard 0

        OSPF LSA errors
        Type 0, Length 0, Data 0, Checksum 0



            Interface GigabitEthernet0/1/7

        Last clearing of interface traffic counters never

        OSPF packets received/sent
        Type          Packets              Bytes
        RX Invalid    0                    0
        RX Hello      79715                3826316
        RX DB des     54                   6708
        RX LS req     2                    72
        RX LS upd     16831                2110728
        RX LS ack     1580                 122140
        RX Total      98182                6065964

        TX Failed     0                    0
        TX Hello      73397                7339656
        TX DB des     59                   72276
        TX LS req     3                    2052
        TX LS upd     9359                 1560172
        TX LS ack     9656                 671164
        TX Total      92474                9645320

        OSPF header errors
        Length 0, Instance ID 0, Checksum 0, Auth Type 0,
        Version 0, Bad Source 0, No Virtual Link 0,
        Area Mismatch 0, No Sham Link 0, Self Originated 0,
        Duplicate ID 0, Hello 0, MTU Mismatch 0,
        Nbr Ignored 9, LLS 0, Unknown Neighbor 0,
        Authentication 0, TTL Check Fail 0, Adjacency Throttle 0,
        BFD 0, Test discard 0

        OSPF LSA errors
        Type 0, Length 0, Data 0, Checksum 0



        Neighbor Statistics for interface GigabitEthernet0/1/7

        Neighbor 10.189.5.253 traffic statistics

        Last clearing of neighbor traffic counters never

        OSPF packets received/sent
        Type          Packets              Bytes
        RX Invalid    0                    0
        RX Hello      70493                3383664
        RX DB des     3                    1676
        RX LS req     1                    36
        RX LS upd     14963                1870388
        RX LS ack     880                  76140
        RX Total      86340                5331904

        TX Failed     0                    0
        TX Hello      1                    100
        TX DB des     4                    416
        TX LS req     1                    968
        TX LS upd     1                    108
        TX LS ack     134                  9456
        TX Total      141                  11048

        OSPF header errors
        Length 0, Instance ID 0, Checksum 0, Auth Type 0,
        Version 0, Bad Source 0, No Virtual Link 0,
        Area Mismatch 0, No Sham Link 0, Self Originated 0,
        Duplicate ID 0, Hello 0, MTU Mismatch 0,
        Nbr Ignored 0, LLS 0, Unknown Neighbor 0,
        Authentication 0, TTL Check Fail 0, Adjacency Throttle 0,
        BFD 0, Test discard 0

        OSPF LSA errors
        Type 0, Length 0, Data 0, Checksum 0



            Interface GigabitEthernet0/1/6

        Last clearing of interface traffic counters never

        OSPF packets received/sent
        Type          Packets              Bytes
        RX Invalid    0                    0
        RX Hello      79472                3814652
        RX DB des     10186                331012
        RX LS req     3                    144
        RX LS upd     15068                1899928
        RX LS ack     931                  79064
        RX Total      105660               6124800

        TX Failed     0                    0
        TX Hello      72795                7271712
        TX DB des     10481                15736044
        TX LS req     2                    1060
        TX LS upd     24639                3749080
        TX LS ack     7915                 548980
        TX Total      115832               27306876

        OSPF header errors
        Length 0, Instance ID 0, Checksum 0, Auth Type 0,
        Version 0, Bad Source 0, No Virtual Link 0,
        Area Mismatch 0, No Sham Link 0, Self Originated 0,
        Duplicate ID 0, Hello 0, MTU Mismatch 0,
        Nbr Ignored 2673, LLS 0, Unknown Neighbor 0,
        Authentication 0, TTL Check Fail 0, Adjacency Throttle 0,
        BFD 0, Test discard 0

        OSPF LSA errors
        Type 0, Length 0, Data 0, Checksum 0



        Neighbor Statistics for interface GigabitEthernet0/1/6

        Neighbor 10.189.5.252 traffic statistics

        Last clearing of neighbor traffic counters never

        OSPF packets received/sent
        Type          Packets              Bytes
        RX Invalid    0                    0
        RX Hello      70504                3384192
        RX DB des     3                    1676
        RX LS req     1                    36
        RX LS upd     14809                1866264
        RX LS ack     877                  76028
        RX Total      86194                5328196

        TX Failed     0                    0
        TX Hello      1                    100
        TX DB des     4                    416
        TX LS req     1                    968
        TX LS upd     1                    108
        TX LS ack     117                  8668
        TX Total      124                  10260

        OSPF header errors
        Length 0, Instance ID 0, Checksum 0, Auth Type 0,
        Version 0, Bad Source 0, No Virtual Link 0,
        Area Mismatch 0, No Sham Link 0, Self Originated 0,
        Duplicate ID 0, Hello 0, MTU Mismatch 0,
        Nbr Ignored 0, LLS 0, Unknown Neighbor 0,
        Authentication 0, TTL Check Fail 0, Adjacency Throttle 0,
        BFD 0, Test discard 0

        OSPF LSA errors
        Type 0, Length 0, Data 0, Checksum 0



        Summary traffic statistics for process ID 888:

        OSPF packets received/sent

        Type          Packets              Bytes
        RX Invalid    0                    0
        RX Hello      159187               7640968
        RX DB des     10240                337720
        RX LS req     5                    216
        RX LS upd     31899                4010656
        RX LS ack     2511                 201204
        RX Total      203842               12190764

        TX Failed     0                    0
        TX Hello      208493               20592264
        TX DB des     10540                15808320
        TX LS req     5                    3112
        TX LS upd     33998                5309252
        TX LS ack     17571                1220144
        TX Total      270607               42933092

        OSPF header errors
        Length 0, Instance ID 0, Checksum 0, Auth Type 0,
        Version 0, Bad Source 0, No Virtual Link 0,
        Area Mismatch 0, No Sham Link 0, Self Originated 0,
        Duplicate ID 0, Hello 0, MTU Mismatch 0,
        Nbr Ignored 2682, LLS 0, Unknown Neighbor 0,
        Authentication 0, TTL Check Fail 0, Adjacency Throttle 0,
        BFD 0, Test discard 0

        OSPF LSA errors
        Type 0, Length 0, Data 0, Checksum 0
    '''}

    def test_show_ip_ospf_traffic_empty(self):
        self.maxDiff = None
        self.device = Mock(**self.empty_output)
        obj = ShowIpOspfTraffic(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_show_ip_ospf_traffic_full1(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output1)
        obj = ShowIpOspfTraffic(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output1)

    def test_golden(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output)
        obj = ShowIpOspfTraffic(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)

    def test_golden2(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output2)
        obj = ShowIpOspfTraffic(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output2)


# ============================================
# Unit test for:
#   'show ip ospf neighbor '
#   'show ip ospf neighbor {interface}'
# ============================================
class test_show_ip_ospf_neighbor(unittest.TestCase):

    '''Unit test for:
      "show ip ospf neighbor" 
      "show ip ospf neighbor {interface}"
    '''

    device = Device(name='aDevice')

    empty_output = {'execute.return_value': ''}

    golden_parsed_output = {
        'interfaces': 
            {'GigabitEthernet0/0/0': 
                {'neighbors':
                    {'172.18.197.242':
                        {'address': '172.19.197.93',
                        'dead_time': '00:00:32',
                        'priority': 1,
                        'state': 'FULL/BDR'},
                    '172.19.197.251':
                        {'address': '172.19.197.91',
                        'dead_time': '00:00:32',
                        'priority': 1,
                        'state': 'FULL/BDR'}}},
            'GigabitEthernet0/0/2': 
                {'neighbors':
                    {'172.19.197.252': 
                        {'address': '172.19.197.92',
                        'dead_time': '00:00:32',
                        'priority': 1,
                        'state': 'FULL/BDR'}}},
            'GigabitEthernet0/0/3': 
                {'neighbors':
                    {'172.19.197.253':
                        {'address': '172.19.197.94',
                        'dead_time': '00:00:32',
                        'priority': 1,
                        'state': 'FULL/BDR'}}},
            'GigabitEthernet0/0/4': 
                {'neighbors':
                    {'172.19.197.254':
                        {'address': '172.19.197.90',
                        'dead_time': '00:00:32',
                        'priority': 1,
                        'state': 'FULL/BDR'}}}}}


    golden_output = {'execute.return_value':'''
        Router#show ip ospf neighbor
        Load for five secs: 2%/0%; one minute: 9%; five minutes: 15%
        Time source is NTP, 20:44:07.304 EST Wed Nov 2 2016


        Neighbor ID     Pri   State           Dead Time   Address         Interface
        172.18.197.242    1   FULL/BDR        00:00:32    172.19.197.93   GigabitEthernet0/0/0
        172.19.197.251    1   FULL/BDR        00:00:32    172.19.197.91   GigabitEthernet0/0/0
        172.19.197.252    1   FULL/BDR        00:00:32    172.19.197.92   GigabitEthernet0/0/2
        172.19.197.253    1   FULL/BDR        00:00:32    172.19.197.94   GigabitEthernet0/0/3
        172.19.197.254    1   FULL/BDR        00:00:32    172.19.197.90   GigabitEthernet0/0/4
        Router#
        '''}

    golden_parsed_output2 = {
      'interfaces': {
        'GigabitEthernet4': {
          'neighbors': {
            '10.16.2.2': {
              'address': '10.169.197.97',
              'dead_time': '00:00:32',
              'priority': 0,
              'state': 'FULL/  -'}}}}}

    golden_output2 = {'execute.return_value':'''
      show ip ospf neighbor GigabitEthernet4
      Neighbor ID     Pri   State           Dead Time   Address         Interface
      10.16.2.2           0   FULL/  -        00:00:32    10.169.197.97  GigabitEthernet4
    '''}

    def test_show_ip_ospf_neighbor_empty(self):
        self.maxDiff= None
        self.device = Mock(**self.empty_output)
        obj = ShowIpOspfNeighbor(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_show_ip_ospf_neighbor_full1(self):
        self.maxDiff = None
        self.device=Mock(**self.golden_output)
        obj=ShowIpOspfNeighbor(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)

    def test_show_ip_ospf_neighbor_full2(self):
        self.maxDiff = None
        self.device=Mock(**self.golden_output2)
        obj=ShowIpOspfNeighbor(device=self.device)
        parsed_output = obj.parse(interface='GigabitEthernet4')
        self.assertEqual(parsed_output, self.golden_parsed_output2)


# ===========================================================
# Unit test for 'show ip ospf database router self-originate'
# ===========================================================
class test_show_ip_ospf_database_router_self_originate(unittest.TestCase):

    '''Unit test for "show ip ospf database router self-originate" '''

    device = Device(name='aDevice')

    empty_output = {'execute.return_value': ''}

    golden_parsed_output = {
        'vrf': {
            'default': {
                'address_family': {
                    'ipv4': {
                        'instance': {
                            '65109': {
                                'areas': {
                                    '0.0.0.8': {
                                        'database': {
                                            'lsa_types': {
                                                1: {
                                                    'lsa_type': 1,
                                                    'lsas': {
                                                        '10.169.197.254 10.169.197.254': {
                                                            'adv_router': '10.169.197.254',
                                                            'lsa_id': '10.169.197.254',
                                                            'ospfv2': {
                                                                'body': {
                                                                    'router': {
                                                                        'links': {
                                                                            '10.169.197.252': {
                                                                                'link_data': '10.169.197.94',
                                                                                'link_id': '10.169.197.252',
                                                                                'num_mtid_metrics': 0,
                                                                                'topologies': {
                                                                                    0: {
                                                                                        'metric': 65535,
                                                                                        'mt_id': 0,
                                                                                        'tos': 0,
                                                                                    }
                                                                                },
                                                                                'type': 'another '
                                                                                        'router '
                                                                                        '(point-to-point)'},
                                                                            '10.169.197.254': {
                                                                                'link_data': '255.255.255.255',
                                                                                'link_id': '10.169.197.254',
                                                                                'num_mtid_metrics': 0,
                                                                                'topologies': {
                                                                                    0: {
                                                                                        'metric': 1,
                                                                                        'mt_id': 0,
                                                                                        'tos': 0}
                                                                                },
                                                                                'type': 'stub '
                                                                                        'network'},
                                                                            '10.169.197.92': {
                                                                                'link_data': '255.255.255.252',
                                                                                'link_id': '10.169.197.92',
                                                                                'num_mtid_metrics': 0,
                                                                                'topologies': {
                                                                                    0: {
                                                                                        'metric': 1000,
                                                                                        'mt_id': 0,
                                                                                        'tos': 0}
                                                                                },
                                                                                'type': 'stub '
                                                                                        'network'}
                                                                        },
                                                                        'num_of_links': 3}
                                                                    },
                                                                    'header': {
                                                                        'adv_router': '10.169.197.254',
                                                                                      'age': 1141,
                                                                                      'checksum': '0x1D38',
                                                                                      'length': 60,
                                                                                      'lsa_id': '10.169.197.254',
                                                                                      'option': 'None',
                                                                                      'option_desc': 'No '
                                                                                                     'TOS-capability, '
                                                                                                     'DC',
                                                                                      'seq_num': '80000031',
                                                                                      'type': 1}
                                                                    }
                                                                }
                                                            }
                                                        }
                                                    }
                                                }
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }

    golden_output = {'execute.return_value':'''
        Load for five secs: 1%/0%; one minute: 1%; five minutes: 1%
        Time source is NTP, 00:59:52.329 EST Thu May 30 2019


                    OSPF Router with ID (10.169.197.254) (Process ID 65109)

                        Router Link States (Area 8)

          Exception Flag: Announcing maximum link costs for topology Base with MTID 0
          LS age: 1141
          Options: (No TOS-capability, DC)
          LS Type: Router Links
          Link State ID: 10.169.197.254
          Advertising Router: 10.169.197.254
          LS Seq Number: 80000031
          Checksum: 0x1D38
          Length: 60
          Number of Links: 3

            Link connected to: a Stub Network
             (Link ID) Network/subnet number: 10.169.197.254
             (Link Data) Network Mask: 255.255.255.255
              Number of MTID metrics: 0
               TOS 0 Metrics: 1

            Link connected to: another Router (point-to-point)
             (Link ID) Neighboring Router ID: 10.169.197.252
             (Link Data) Router Interface address: 10.169.197.94
              Number of MTID metrics: 0
               TOS 0 Metrics: 65535

            Link connected to: a Stub Network
             (Link ID) Network/subnet number: 10.169.197.92
             (Link Data) Network Mask: 255.255.255.252
              Number of MTID metrics: 0
               TOS 0 Metrics: 1000
        '''}

    def test_show_ip_ospf_neighbor_empty(self):
        self.maxDiff= None
        self.device = Mock(**self.empty_output)
        obj = ShowIpOspfDatabaseRouterSelfOriginate(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_show_ip_ospf_neighbor_full1(self):
        self.maxDiff = None
        self.device=Mock(**self.golden_output)
        obj=ShowIpOspfDatabaseRouterSelfOriginate(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


# ===================================================
# Unit tests for:
#   'show ip ospf segment-routing global-block'
#   'show ip ospf {pid} segment-routing global-block'
# ===================================================
class show_ip_ospf_segment_routing_global_block(unittest.TestCase):
    device = Device(name='aDevice')

    empty_output = {'execute.return_value': ''}

    golden_output = {'execute.return_value': '''
        show ip ospf 1234 segment-routing global-block
 
                    OSPF Router with ID (10.4.1.1) (Process ID 1234)
         
        OSPF Segment Routing Global Blocks in Area 3
         
          Router ID:      SR Capable: SR Algorithm: SRGB Base: SRGB Range:  SID/Label:
         
         *10.4.1.1         Yes         SPF,StrictSPF 16000      8000         Label    
          10.16.2.2         Yes         SPF,StrictSPF 16000      8000         Label  
    '''}

    golden_parsed_output = {
        'process_id': {
            1234: {
                'router_id': '10.4.1.1',
                'area': 3,
                'routers': {
                    '10.4.1.1': {
                        'router_id': '10.4.1.1',
                        'sr_capable': 'Yes',
                        'sr_algorithm': 'SPF,StrictSPF',
                        'srgb_base': 16000,
                        'srgb_range': 8000,
                        'sid_label': 'Label'
                    },
                    '10.16.2.2': {
                        'router_id': '10.16.2.2',
                        'sr_capable': 'Yes',
                        'sr_algorithm': 'SPF,StrictSPF',
                        'srgb_base': 16000,
                        'srgb_range': 8000,
                        'sid_label': 'Label'
                    }
                }
            }
        }
    }

    golden_output_2 = {'execute.return_value': '''
        show ip ospf segment-routing global-block

                    OSPF Router with ID (10.4.1.1) (Process ID 1)
        
        OSPF Segment Routing Global Blocks in Area 0
        
          Router ID:      SR Capable: SR Algorithm: SRGB Base: SRGB Range:  SID/Label:
        
         *10.4.1.1         No
          10.16.2.2         No
          10.36.3.3         No
    '''}

    golden_parsed_output_2 = {
        'process_id': {
            1: {
                'router_id': '10.4.1.1',
                'area': 0,
                'routers': {
                    '10.4.1.1': {
                        'router_id': '10.4.1.1',
                        'sr_capable': 'No'
                    },
                    '10.16.2.2': {
                        'router_id': '10.16.2.2',
                        'sr_capable': 'No'
                    },
                    '10.36.3.3': {
                        'router_id': '10.36.3.3',
                        'sr_capable': 'No'
                    }
                }
            }
        }
    }

    def test_show_ip_ospf_segment_routing_empty(self):
        self.maxDiff= None
        self.device = Mock(**self.empty_output)
        obj = ShowIpOspfSegmentRoutingGlobalBlock(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_show_ip_ospf_segment_routing(self):
        self.maxDiff = None
        self.device=Mock(**self.golden_output)
        obj=ShowIpOspfSegmentRoutingGlobalBlock(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)

    def test_show_ip_ospf_segment_routing_pid(self):
        self.maxDiff = None
        self.device=Mock(**self.golden_output)
        obj=ShowIpOspfSegmentRoutingGlobalBlock(device=self.device)
        parsed_output = obj.parse(process_id=1234)
        self.assertEqual(parsed_output, self.golden_parsed_output)

    def test_show_ip_ospf_segment_routing_pid2(self):
        self.maxDiff = None
        self.device=Mock(**self.golden_output_2)
        obj=ShowIpOspfSegmentRoutingGlobalBlock(device=self.device)
        parsed_output = obj.parse(process_id=1234)
        self.assertEqual(parsed_output, self.golden_parsed_output_2)

class test_show_ip_ospf_segment_routing_adjacency_sid(unittest.TestCase):
    ''' Test case for command:
          * show ip ospf {bgp_as} segment-routing adjacency-sid
    '''

    device = Device(name='aDevice')

    empty_output = {'execute.return_value': ''}

    golden_output_1 = {'execute.return_value': '''
        PE1#show ip ospf 65109 segment-routing adjacency-sid
 
                    OSPF Router with ID (10.4.1.1) (Process ID 65109)
            Flags: S - Static, D - Dynamic,  P - Protected, U - Unprotected, G - Group, L - Adjacency Lost
         
        Adj-Sid  Neighbor ID     Interface          Neighbor Addr   Flags   Backup Nexthop  Backup Interface 
        -------- --------------- ------------------ --------------- ------- --------------- ------------------
        16       10.16.2.2         Gi0/1/2            192.168.154.2       D U   
        17       10.16.2.2         Gi0/1/1            192.168.4.2       D U   
        18       10.16.2.2         Gi0/1/0            192.168.111.2       D U   
        19       10.16.2.2         Te0/0/0            192.168.220.2       D U    
    '''}

    parsed_output_1 = {
        'process_id': {
            '65109': {
                'router_id': '10.4.1.1',
                'adjacency_sids': {
                    '16': {
                       'flags': 'D U',
                       'interface': 'GigabitEthernet0/1/2',
                       'neighbor_address': '192.168.154.2',
                       'neighbor_id': '10.16.2.2'},
                    '17': {
                        'flags': 'D U',
                        'interface': 'GigabitEthernet0/1/1',
                        'neighbor_address': '192.168.4.2',
                        'neighbor_id': '10.16.2.2'},
                    '18': {
                        'flags': 'D U',
                        'interface': 'GigabitEthernet0/1/0',
                        'neighbor_address': '192.168.111.2',
                        'neighbor_id': '10.16.2.2'},
                    '19': {
                        'flags': 'D U',
                        'interface': 'TenGigabitEthernet0/0/0',
                        'neighbor_address': '192.168.220.2',
                        'neighbor_id': '10.16.2.2'}}}}}

    def test_show_ip_ospf_segment_routing_empty(self):
        self.maxDiff = None
        self.device=Mock(**self.empty_output)
        obj=ShowIpOspfSegmentRoutingAdjacencySid(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_show_ip_ospf_segment_routing_1(self):
        self.maxDiff = None
        self.device=Mock(**self.golden_output_1)
        obj=ShowIpOspfSegmentRoutingAdjacencySid(device=self.device)
        parsed_output = obj.parse(process_id=65109)
        self.assertEqual(parsed_output, self.parsed_output_1)

# ================================================
# Unit test for 'show ip ospf fast-reroute ti-lfa'
# ================================================

class test_show_ip_ospf_fast_reroute_ti_lfa(unittest.TestCase):

    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output = {
        'process_id': {
            65109: {
                'router_id': '10.4.1.1',
                'ospf_object': {
                    'Process ID (65109)': {
                        'ipfrr_enabled': 'no',
                        'sr_enabled': 'yes',
                        'ti_lfa_configured': 'no',
                        'ti_lfa_enabled': 'no',
                        },
                    'Area 8': {
                        'ipfrr_enabled': 'no',
                        'sr_enabled': 'yes',
                        'ti_lfa_configured': 'no',
                        'ti_lfa_enabled': 'no',
                        },
                    'Loopback0': {
                        'ipfrr_enabled': 'no',
                        'sr_enabled': 'no',
                        'ti_lfa_configured': 'no',
                        'ti_lfa_enabled': 'no',
                        },
                    'GigabitEthernet0/1/2': {
                        'ipfrr_enabled': 'no',
                        'sr_enabled': 'yes',
                        'ti_lfa_configured': 'no',
                        'ti_lfa_enabled': 'no',
                        },
                    'GigabitEthernet0/1/1': {
                        'ipfrr_enabled': 'no',
                        'sr_enabled': 'yes',
                        'ti_lfa_configured': 'no',
                        'ti_lfa_enabled': 'no',
                        },
                    'GigabitEthernet0/1/0': {
                        'ipfrr_enabled': 'no',
                        'sr_enabled': 'yes',
                        'ti_lfa_configured': 'no',
                        'ti_lfa_enabled': 'no',
                        },
                    'TenGigabitEthernet0/0/': {
                        'ipfrr_enabled': 'no',
                        'sr_enabled': 'yes',
                        'ti_lfa_configured': 'no',
                        'ti_lfa_enabled': 'no',
                        },
                    'AS external': {
                        'ipfrr_enabled': 'no',
                        'sr_enabled': 'yes',
                        'ti_lfa_configured': 'no',
                        'ti_lfa_enabled': 'no',
                        },
                    },
                },
            },
        }

    golden_output = {'execute.return_value': '''
        show ip ospf fast-reroute ti-lfa
        OSPF Router with ID (10.4.1.1) (Process ID 65109)

        OSPF                    IPFRR    SR       TI-LFA      TI-LFA       
        Object                  enabled  enabled  configured  enabled      
        --------------------------------------------------------------------
        Process ID (65109)       no       yes      no          no           
        Area 8                  no       yes      no          no           
        Loopback0               no       no       no          no           
        GigabitEthernet0/1/2    no       yes      no          no           
        GigabitEthernet0/1/1    no       yes      no          no           
        GigabitEthernet0/1/0    no       yes      no          no           
        TenGigabitEthernet0/0/  no       yes      no          no           
        AS external             no       yes      no          no       
    '''}

    golden_parsed_output2 = {
        'process_id': {
            65109: {
                'router_id': '10.4.1.1',
                'ospf_object': {
                    'Process ID (65109)': {
                        'ipfrr_enabled': 'no',
                        'sr_enabled': 'yes',
                        'ti_lfa_configured': 'yes',
                        'ti_lfa_enabled': 'yes (inactive)',
                        },
                    'Area 8': {
                        'ipfrr_enabled': 'yes',
                        'sr_enabled': 'yes',
                        'ti_lfa_configured': 'yes',
                        'ti_lfa_enabled': 'yes',
                        },
                    'Loopback0': {
                        'ipfrr_enabled': 'yes',
                        'sr_enabled': 'no',
                        'ti_lfa_configured': 'no',
                        'ti_lfa_enabled': 'yes (inactive)',
                        },
                    'GigabitEthernet5': {
                        'ipfrr_enabled': 'yes',
                        'sr_enabled': 'yes',
                        'ti_lfa_configured': 'no',
                        'ti_lfa_enabled': 'yes',
                        },
                    'GigabitEthernet4': {
                        'ipfrr_enabled': 'yes',
                        'sr_enabled': 'yes',
                        'ti_lfa_configured': 'no',
                        'ti_lfa_enabled': 'yes',
                        },
                    'GigabitEthernet3': {
                        'ipfrr_enabled': 'yes',
                        'sr_enabled': 'yes',
                        'ti_lfa_configured': 'no',
                        'ti_lfa_enabled': 'yes',
                        },
                    'GigabitEthernet2': {
                        'ipfrr_enabled': 'yes',
                        'sr_enabled': 'yes',
                        'ti_lfa_configured': 'no',
                        'ti_lfa_enabled': 'yes',
                        },
                    'AS external': {
                        'ipfrr_enabled': 'no',
                        'sr_enabled': 'yes',
                        'ti_lfa_configured': 'yes',
                        'ti_lfa_enabled': 'yes (inactive)',
                        },
                    },
                },
            },
        }

    golden_output2 = {'execute.return_value': '''
    show ip ospf fast-reroute ti-lfa

    OSPF Router with ID (10.4.1.1) (Process ID 65109)

    OSPF                    IPFRR    SR       TI-LFA      TI-LFA
    Object                  enabled  enabled  configured  enabled
    --------------------------------------------------------------------
    Process ID (65109)       no       yes      yes         yes (inactive)
    Area 8                  yes      yes      yes         yes
    Loopback0               yes      no       no          yes (inactive)
    GigabitEthernet5        yes      yes      no          yes
    GigabitEthernet4        yes      yes      no          yes
    GigabitEthernet3        yes      yes      no          yes
    GigabitEthernet2        yes      yes      no          yes
    AS external             no       yes      yes         yes (inactive)
    '''}

    def test_empty(self):
        self.device1 = Mock(**self.empty_output)
        obj = ShowIpOspfFastRerouteTiLfa(device=self.device1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = ShowIpOspfFastRerouteTiLfa(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output)

    def test_golden2(self):
        self.device = Mock(**self.golden_output2)
        obj = ShowIpOspfFastRerouteTiLfa(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output2)

# ===================================================================
# Unit test for 'show ip ospf segment-routing protected-adjacencies'
# ===================================================================

class test_show_ip_ospf_segment_routing_protected_adjacencies(unittest.TestCase):

    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_output = {'execute.return_value': '''
        show ip ospf segment-routing protected-adjacencies

                OSPF Router with ID (10.4.1.1) (Process ID 65109)

                            Area with ID (8)

        Neighbor ID     Interface          Address         Adj-Sid      Backup Nexthop  Backup Interface
        --------------- ------------------ --------------- ------------ --------------- ------------------
        10.151.22.22     Gi5                10.0.0.25       20           10.0.0.9        Gi3
        10.151.22.22     Gi4                10.0.0.13       21           10.0.0.9        Gi3
        10.229.11.11     Gi3                10.0.0.9        22           10.0.0.13       Gi4
    '''}

    golden_parsed_output = {
        'process_id': {
            65109: {
                'router_id': '10.4.1.1',
                'areas': {
                    '0.0.0.8': {                        
                        'neighbors': {
                            '10.151.22.22': {
                                'interfaces': {
                                    'GigabitEthernet5': {
                                        'address': '10.0.0.25',
                                        'adj_sid': 20,
                                        'backup_nexthop': '10.0.0.9',
                                        'backup_interface': 'GigabitEthernet3',
                                        },
                                    'GigabitEthernet4': {
                                        'address': '10.0.0.13',
                                        'adj_sid': 21,
                                        'backup_nexthop': '10.0.0.9',
                                        'backup_interface': 'GigabitEthernet3',
                                        },
                                    },
                                },
                            '10.229.11.11': {
                                'interfaces': {
                                    'GigabitEthernet3': {
                                        'address': '10.0.0.9',
                                        'adj_sid': 22,
                                        'backup_nexthop': '10.0.0.13',
                                        'backup_interface': 'GigabitEthernet4',
                                        },
                                    },
                                },
                            },
                        },
                    },
                },
            },
        }

    golden_output_2 = {'execute.return_value': '''
        PE1#show ip ospf segment-routing protected-adjacencies

            OSPF Router with ID (10.4.1.1) (Process ID 65109)
    '''}

    parsed_output_2 = {
        'process_id': {
            65109: {
                'router_id': '10.4.1.1'
            }
        }
    }
    golden_output_3 = {'execute.return_value':'''
    show ip ospf segment-routing protected-adjacencies
    Load for five secs: 0%/0%; one minute: 1%; five minutes: 1%
    Time source is NTP, 15:31:18.236 EST Thu Oct 31 2019
                OSPF Router with ID (10.16.2.2) (Process ID 65109)
                              Area with ID (8)
    Neighbor ID     Interface          Address         Adj-Sid      Backup Nexthop  Backup Interface  
    --------------- ------------------ --------------- ------------ --------------- ------------------
    10.4.1.1         Gi0/1/6            10.16.2.2          17          
    '''}

    parsed_output_3 = {
        'process_id': {
            65109: {
                'router_id': '10.16.2.2',
                'areas': {
                    '0.0.0.8': {
                        'neighbors': {
                            '10.4.1.1': {
                                'interfaces': {
                                    'GigabitEthernet0/1/6': {
                                        'address': '10.16.2.2',
                                        'adj_sid': 17}}}}}}}}}

    def test_empty(self):
        self.device1 = Mock(**self.empty_output)
        obj = ShowIpOspfSegmentRoutingProtectedAdjacencies(device=self.device1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = ShowIpOspfSegmentRoutingProtectedAdjacencies(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output)

    def test_golden_2(self):
        self.device = Mock(**self.golden_output_2)
        obj = ShowIpOspfSegmentRoutingProtectedAdjacencies(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.parsed_output_2)

    def test_golden_3(self):
        self.device = Mock(**self.golden_output_3)
        obj = ShowIpOspfSegmentRoutingProtectedAdjacencies(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.parsed_output_3)

class test_show_ip_ospf_segment_routing_sid_database(unittest.TestCase):
    """ Test case for command:
          * show ip ospf segment-routing sid-database
    """
    device = Device(name='aDevice')

    empty_output = {'execute.return_value': ''}

    golden_output = {'execute.return_value': '''
        show ip ospf segment-routing sid-database

                    OSPF Router with ID (10.4.1.1) (Process ID 1234)

        OSPF Segment Routing SIDs

        Codes: L - local, N - label not programmed,
               M - mapping-server

        SID             Prefix              Adv-Rtr-Id       Area-Id  Type      Algo
        --------------  ------------------  ---------------  -------  --------  ----
        1       (L)     10.4.1.1/32          10.4.1.1          8        Intra     0  
        2               10.16.2.2/32          10.16.2.2          8        Intra     0  
    '''}

    golden_parsed_output = {
        'process_id': {
            1234: {
                'router_id': '10.4.1.1',
                'sids': {
                    'total_entries': 2,
                    1: {
                        'index': {
                            1: {
                                'prefix': '10.4.1.1/32',
                                'codes': 'L',
                                'adv_rtr_id': '10.4.1.1',
                                'area_id': '0.0.0.8',
                                'type': 'Intra',
                                'algo': 0
                            }
                        }
                    },
                    2: {
                        'index': {
                            1: {
                                'prefix': '10.16.2.2/32',
                                'adv_rtr_id': '10.16.2.2',
                                'area_id': '0.0.0.8',
                                'type': 'Intra',
                                'algo': 0
                            }
                        }
                    }
                }
            }
        }
    }

    golden_parsed_output2 = {
        'process_id': {
            65109: {
                'router_id': '10.4.1.1',
                },
            },
        }

    golden_output2 = {'execute.return_value': '''
        show ip ospf segment-routing sid-database

            OSPF Router with ID (10.4.1.1) (Process ID 65109)
    '''}

    golden_parsed_output3 = {
        'process_id': {
            65109: {
                'router_id': '10.4.1.1',
                'sids': {
                    'total_entries': 4,
                    1: {
                        'index': {
                            1: {
                                'prefix': '10.4.1.1/32',
                                'codes': 'L',
                                'adv_rtr_id': '10.4.1.1',
                                'area_id': '0.0.0.8',
                                'type': 'Intra',
                                'algo': 0
                            },
                            2: {
                                'prefix': '10.4.1.2/32',
                                'adv_rtr_id': '10.4.1.2',
                                'area_id': '0.0.0.8',
                                'type': 'Intra',
                                'algo': 0
                            }
                        }
                    },
                    11: {
                        'index': {
                            1: {
                                'prefix': '10.4.1.2/32',
                                'adv_rtr_id': '10.4.1.2',
                                'area_id': '0.0.0.8',
                                'type': 'Intra',
                                'algo': 0
                            }
                        }
                    },
                    45: {
                        'index': {
                            1: {
                                'prefix': '10.4.1.3/32',
                                'codes': 'M',
                                'type': 'Unknown',
                                'algo': 0
                            }
                        }
                    }
                }
            }
        }
    }

    golden_output3 = {'execute.return_value': '''
        show ip ospf segment-routing sid-database

            OSPF Router with ID (10.4.1.1) (Process ID 65109)

        OSPF Segment Routing SIDs

        Codes: L - local, N - label not programmed,
            M - mapping-server

        SID             Prefix              Adv-Rtr-Id       Area-Id  Type      Algo
        --------------  ------------------  ---------------  -------  --------  ----
        1       (L)     10.4.1.1/32         10.4.1.1          8        Intra     0
                        10.4.1.2/32         10.4.1.2          8        Intra     0
        11              10.4.1.2/32         10.4.1.2          8        Intra     0
        45      (M)     10.4.1.3/32                                    Unknown   0
    '''}

    def test_empty(self):
        self.maxDiff = None
        self.device = Mock(**self.empty_output)
        obj = ShowIpOspfSegmentRoutingSidDatabase(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden1(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output)
        obj = ShowIpOspfSegmentRoutingSidDatabase(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)
    
    def test_golden2(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output2)
        obj = ShowIpOspfSegmentRoutingSidDatabase(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output2)
    
    def test_golden3(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output3)
        obj = ShowIpOspfSegmentRoutingSidDatabase(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output3)

# =============================================
# Unit test for 'show ip ospf segment-routing'
# =============================================

class test_show_ip_ospf_segment_routing(unittest.TestCase):

    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_output = {'execute.return_value': '''
        show ip ospf segment-routing             
    
                OSPF Router with ID (10.16.2.2) (Process ID 65109)
    
        Global segment-routing state: Enabled
        
        Segment Routing enabled:
                Area    Topology name    Forwarding    Strict SPF   
                    8    Base             MPLS          Capable
            AS external    Base             MPLS          Not applicable
        
        SR Attributes
            Prefer non-SR (LDP) Labels
            Do not advertise Explicit Null
        
        Global Block (SRGB):
            Range: 16000 - 23999
            State: Created
        
        Local Block (SRLB):
            Range: 15000 - 15999
            State: Created
        
        Registered with SR App, client handle: 2
        SR algo 0 Connected map notifications active (handle 0x0), bitmask 0x1
        SR algo 0 Active policy map notifications active (handle 0x2), bitmask 0xC
        SR algo 1 Connected map notifications active (handle 0x1), bitmask 0x1
        SR algo 1 Active policy map notifications active (handle 0x3), bitmask 0xC
        Registered with MPLS, client-id: 100
        
        Max labels: platform 16, available 13
        Max labels pushed by OSPF: uloop tunnels 10, TI-LFA tunnels 10
        mfi label reservation ack not pending
        
        Bind Retry timer not running
        Adj Label Bind Retry timer not running
        sr-app locks requested: srgb 0, srlb 0
        TEAPP:
        TE Router ID 10.16.2.2
    '''}

    golden_parsed_output = {
        'process_id': {
            65109: {
                'router_id': '10.16.2.2',
                'sr_attributes': {
                    'sr_label_preferred': False,
                    'advertise_explicit_null': False,
                    },
                'mfi_label_reservation_ack_pending': False,
                'bind_retry_timer_running': False,
                'adj_label_bind_retry_timer_running': False,
                'global_segment_routing_state': 'Enabled',
                'segment_routing_enabled': {
                    'area': {
                        '0.0.0.8': {
                            'topology_name': 'Base',
                            'forwarding': 'MPLS',
                            'strict_spf': 'Capable',
                            },
                        'AS external': {
                            'topology_name': 'Base',
                            'forwarding': 'MPLS',
                            'strict_spf': 'Not applicable',
                            },
                        },
                    },
                'global_block_srgb': {
                    'range': {
                        'start': 16000,
                        'end': 23999,
                        },
                    'state': 'Created',
                    },
                'local_block_srlb': {
                    'range': {
                        'start': 15000,
                        'end': 15999,
                        },
                    'state': 'Created',
                    },
                'registered_with': {
                    'SR App': {
                        'client_handle': 2,
                        'sr_algo': {
                            0: {
                                'connected_map_notifications_active': {
                                    'handle': '0x0',
                                    'bit_mask': '0x1',
                                    },
                                'active_policy_map_notifications_active': {
                                    'handle': '0x2',
                                    'bit_mask': '0xC',
                                    },
                                },
                            1: {
                                'connected_map_notifications_active': {
                                    'handle': '0x1',
                                    'bit_mask': '0x1',
                                    },
                                'active_policy_map_notifications_active': {
                                    'handle': '0x3',
                                    'bit_mask': '0xC',
                                    },
                                },
                            },
                        },
                    'MPLS': {
                        'client_id': 100,
                        },
                    },
                'max_labels': {
                    'platform': 16,
                    'available': 13,
                    'pushed_by_ospf': {
                        'uloop_tunnels': 10,
                        'ti_lfa_tunnels': 10,
                        },
                    },
                'srp_app_locks_requested': {
                    'srgb': 0,
                    'srlb': 0,
                    },
                'teapp': {
                    'te_router_id': '10.16.2.2',
                    },
                },
            },
        }
    
    golden_output2 = {'execute.return_value': '''
    show ip ospf segment-routing

            OSPF Router with ID (10.4.1.1) (Process ID 65109)

    Global segment-routing state: Not configured
    '''}

    golden_parsed_output2 = {
        'process_id': {
            65109: {
                'router_id': '10.4.1.1',
                'sr_attributes': {
                    'sr_label_preferred': True,
                    'advertise_explicit_null': True,
                    },
                'mfi_label_reservation_ack_pending': True,
                'bind_retry_timer_running': True,
                'adj_label_bind_retry_timer_running': True,
                },
            },
        }

    def test_empty(self):
        self.device1 = Mock(**self.empty_output)
        obj = ShowIpOspfSegmentRouting(device=self.device1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = ShowIpOspfSegmentRouting(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output)
    
    def test_golden2(self):
        self.device = Mock(**self.golden_output2)
        obj = ShowIpOspfSegmentRouting(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output2)

if __name__ == '__main__':
    unittest.main()