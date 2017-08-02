
# Python
import unittest
from unittest.mock import Mock
import xml.etree.ElementTree as ET

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from metaparser.util.exceptions import SchemaEmptyParserError, SchemaMissingKeyError

# nxos show_bgp
from parser.nxos.show_bgp import ShowBgpProcessVrfAll, ShowBgpPeerSession,\
                                 ShowBgpPeerPolicy, ShowBgpPeerTemplate,\
                                 ShowBgpVrfAllAll,\
                                 ShowBgpVrfAllNeighbors,\
                                 ShowBgpVrfAllAllNextHopDatabase,\
                                 ShowBgpVrfAllAllSummary,\
                                 ShowBgpVrfAllAllDampeningParameters,\
                                 ShowBgpVrfAllNeighborsAdvertisedRoutes,\
                                 ShowBgpVrfAllNeighborsRoutes,\
                                 ShowBgpVrfAllNeighborsReceivedRoutes,\
                                 ShowRunningConfigBgp


# =========================================
#  Unit test for 'show bgp process vrf all'
# =========================================

class test_show_bgp_process_vrf_all_cli(unittest.TestCase):

    '''Unit test for show bgp process vrf all - CLI'''
    
    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output1 = {
        'bgp_as_path_entries': 0,
        'bgp_asformat': 'asplain',
        'bgp_isolate_mode': 'No',
        'bgp_memory_state': 'ok',
        'bgp_mmode': 'Initialized',
        'bgp_paths_per_hwm_attr': 1,
        'bgp_performance_mode': 'No',
        'bgp_pid': 29474,
        'bgp_protocol_started_reason': 'configuration',
        'bgp_protocol_state': 'running',
        'bgp_tag': '100',
        'bytes_used': 368,
        'bytes_used_as_path_entries': 0,
        'entries_pending_delete': 0,
        'hwm_attr_entries': 5,
        'hwm_entries_pending_delete': 0,
        'num_attr_entries': 4,
        'segment_routing_global_block': '10000-25000',
        'vrf': 
            {'VRF1': {
                'address_family': 
                    {'ipv4 unicast': 
                        {'aggregate_label': '492287',
                        'export_rt_list': '100:100',
                        'import_rt_list': '100:100',
                        'label_mode': 'per-prefix',
                        'peers': 
                            {1: 
                                {'active_peers': 0,
                                 'aggregates': 2,
                                 'networks': 1,
                                 'paths': 5,
                                 'routes': 5}},
                        'redistribution': 
                            {'direct': 
                                {'route_map': 'genie_redistribution'},
                             'eigrp': 
                                {'route_map': 'test-map'},
                             'static': 
                                {'route_map': 'genie_redistribution'}},
                        'table_id': '0x10',
                        'table_state': 'up'},
                    'ipv6 unicast': {
                        'aggregate_label': '492288',
                        'export_rt_list': '100:100',
                        'import_rt_list': '100:100',
                        'label_mode': 'per-prefix',
                        'next_hop_trigger_delay':
                            {'critical': 3000,
                             'non_critical': 10000,
                            },
                        'peers': 
                            {0: 
                                {'active_peers': 0,
                                 'aggregates': 1,
                                 'networks': 1,
                                 'paths': 4,
                                 'routes': 4}},
                        'redistribution': 
                            {'direct': 
                                {'route_map': 'genie_redistribution'},
                             'static': 
                                {'route_map': 'genie_redistribution'}},
                        'table_id': '0x80000010',
                        'table_state': 'up'}},
                'cluster_id': '0.0.0.0',
                'conf_router_id': '0.0.0.0',
                'confed_id': 0,
                'num_conf_peers': 1,
                'num_established_peers': 0,
                'num_pending_conf_peers': 0,
                'router_id': '11.11.11.11',
                'vrf_id': '3',
                'vrf_rd': '100:100',
                'vrf_state': 'up'},
             'default': 
                {'address_family': 
                    {'ipv4 unicast': 
                        {'peers': 
                            {1: 
                                {'active_peers': 0,
                                'aggregates': 0,
                                'networks': 0,
                                'paths': 0,
                                'routes': 0}},
                         'table_id': '0x1',
                         'table_state': 'up'},
                    'ipv6 label unicast': 
                        {'peers': 
                            {0: 
                                {'active_peers': 0,
                                 'aggregates': 0,
                                 'networks': 0,
                                 'paths': 0,
                                 'routes': 0}},
                         'table_id': '0x80000001',
                         'table_state': 'up'},
                    'ipv6 unicast': 
                        {'peers': 
                            {0: 
                                {'active_peers': 0,
                                'aggregates': 0,
                                'networks': 0,
                                'paths': 0,
                                'routes': 0}},
                         'table_id': '0x80000001',
                         'table_state': 'up'},
                    'vpnv4 unicast': 
                        {'peers': 
                            {1: 
                                {'active_peers': 1,
                                 'aggregates': 0,
                                 'networks': 0,
                                 'paths': 5,
                                 'routes': 5}},
                         'table_id': '0x1',
                         'table_state': 'up'},
                    'vpnv6 unicast': 
                        {'peers': 
                            {1: 
                                {'active_peers': 1,
                                'aggregates': 0,
                                 'networks': 0,
                                 'paths': 4,
                                 'routes': 4}},
                         'table_id': '0x80000001',
                         'table_state': 'up'}},
                 'cluster_id': '0.0.0.0',
                 'conf_router_id': '1.1.1.1',
                 'confed_id': 0,
                 'num_conf_peers': 3,
                 'num_established_peers': 1,
                 'num_pending_conf_peers': 0,
                 'router_id': '1.1.1.1',
                 'vrf_id': '1',
                 'vrf_rd': 'not configured',
                 'vrf_state': 'up'}}}

    golden_output1 = {'execute.return_value': '''
        BGP Process Information
        BGP Process ID                 : 29474
        BGP Protocol Started, reason:  : configuration
        BGP Protocol Tag               : 100
        BGP Performance Mode:          : No
        BGP Protocol State             : Running
        BGP Isolate Mode               : No
        BGP MMODE                      : Initialized
        BGP Memory State               : OK
        BGP asformat                   : asplain
        Segment Routing Global Block   : 10000-25000

        BGP attributes information
        Number of attribute entries    : 4
        HWM of attribute entries       : 5
        Bytes used by entries          : 368
        Entries pending delete         : 0
        HWM of entries pending delete  : 0
        BGP paths per attribute HWM    : 1
        BGP AS path entries            : 0
        Bytes used by AS path entries  : 0

        Confcheck capabilities in use:
          1. CAP_FEATURE_BGP_5_2_1 (refcount = 7)

        Information regarding configured VRFs:

        BGP Information for VRF VRF1
        VRF Id                         : 3
        VRF state                      : UP
        Router-ID                      : 11.11.11.11
        Configured Router-ID           : 0.0.0.0
        Confed-ID                      : 0
        Cluster-ID                     : 0.0.0.0
        No. of configured peers        : 1
        No. of pending config peers    : 0
        No. of established peers       : 0
        VRF RD                         : 100:100

            Information for address family IPv4 Unicast in VRF VRF1
            Table Id                   : 10
            Table state                : UP
            Peers      Active-peers    Routes     Paths      Networks   Aggregates
            1          0               5          5          1          2         

            Redistribution                
                direct, route-map genie_redistribution
                static, route-map genie_redistribution
                eigrp, route-map test-map

            Export RT list: 100:100
            Import RT list: 100:100
            Label mode: per-prefix
            Aggregate label: 492287

            Information for address family IPv6 Unicast in VRF VRF1
            Table Id                   : 0x80000010
            Table state                : UP
            Peers      Active-peers    Routes     Paths      Networks   Aggregates
            0          0               4          4          1          1         

            Redistribution                
                direct, route-map genie_redistribution
                static, route-map genie_redistribution

            Export RT list: 100:100
            Import RT list: 100:100
            Label mode: per-prefix
            Aggregate label: 492288

            Nexthop trigger-delay
                critical 3000 ms
                non-critical 10000 ms

        BGP Information for VRF default
        VRF Id                         : 1
        VRF state                      : UP
        Router-ID                      : 1.1.1.1
        Configured Router-ID           : 1.1.1.1
        Confed-ID                      : 0
        Cluster-ID                     : 0.0.0.0
        No. of configured peers        : 3
        No. of pending config peers    : 0
        No. of established peers       : 1
        VRF RD                         : Not configured

            Information for address family IPv4 Unicast in VRF default
            Table Id                   : 1
            Table state                : UP
            Peers      Active-peers    Routes     Paths      Networks   Aggregates
            1          0               0          0          0          0         

            Redistribution                
                None


            Information for address family IPv6 Unicast in VRF default
            Table Id                   : 80000001
            Table state                : UP
            Peers      Active-peers    Routes     Paths      Networks   Aggregates
            0          0               0          0          0          0         

            Redistribution                
                None


            Information for address family VPNv4 Unicast in VRF default
            Table Id                   : 1
            Table state                : UP
            Peers      Active-peers    Routes     Paths      Networks   Aggregates
            1          1               5          5          0          0         

            Redistribution                
                None

            Retain RT: enabled all

            Information for address family VPNv6 Unicast in VRF default
            Table Id                   : 80000001
            Table state                : UP
            Peers      Active-peers    Routes     Paths      Networks   Aggregates
            1          1               4          4          0          0         

            Redistribution                
                None


            Information for address family IPv6 Label Unicast in VRF default
            Table Id                   : 80000001
            Table state                : UP
            Peers      Active-peers    Routes     Paths      Networks   Aggregates
            0          0               0          0          0          0         

            Redistribution                
                None
        '''}

    golden_parsed_output2 = {
        'bgp_as_path_entries': 0,
        'bgp_asformat': 'asplain',
        'bgp_isolate_mode': 'Yes',
        'bgp_memory_state': 'ok',
        'bgp_mmode': 'Initialized',
        'bgp_paths_per_hwm_attr': 3,
        'bgp_performance_mode': 'No',
        'bgp_pid': 26549,
        'bgp_protocol_started_reason': 'configuration',
        'bgp_protocol_state': 'running (isolate)',
        'bgp_tag': '333',
        'bytes_used': 784,
        'bytes_used_as_path_entries': 0,
        'entries_pending_delete': 0,
        'hwm_attr_entries': 8,
        'hwm_entries_pending_delete': 0,
        'num_attr_entries': 7,
        'segment_routing_global_block': '10000-25000',
        'vrf': 
            {'VRF1': 
                {'cluster_id': '0.0.0.0',
                'conf_router_id': '0.0.0.0',
                'confed_id': 0,
                'num_conf_peers': 2,
                'num_established_peers': 0,
                'num_pending_conf_peers': 0,
                'router_id': '0.0.0.0',
                'vrf_id': '3',
                'vrf_rd': 'not configured',
                'vrf_state': 'up'},
            'ac': 
                {'address_family': 
                    {'ipv4 unicast': 
                        {'next_hop_trigger_delay': 
                            {'critical': 3000,
                            'non_critical': 10000},
                        'peers': 
                            {1: 
                                {'active_peers': 0,
                                'aggregates': 0,
                                'networks': 0,
                                'paths': 0,
                                'routes': 0}},
                        'table_id': '0x4',
                        'table_state': 'up'},
                    'ipv6 unicast': 
                        {'next_hop_trigger_delay': 
                            {'critical': 3000,
                            'non_critical': 10000},
                        'peers': 
                            {0: 
                                {'active_peers': 0,
                                'aggregates': 0,
                                'networks': 0,
                                'paths': 0,
                                'routes': 0}},
                        'table_id': '0x80000004',
                        'table_state': 'up'}},
                'cluster_id': '0.0.0.0',
                'conf_router_id': '0.0.0.0',
                'confed_id': 0,
                'num_conf_peers': 1,
                'num_established_peers': 0,
                'num_pending_conf_peers': 0,
                'router_id': '0.0.0.0',
                'vrf_id': '4',
                'vrf_rd': 'not configured',
                'vrf_state': 'up'},
            'default': 
                {'address_family': 
                    {'ipv4 label unicast': 
                        {'next_hop_trigger_delay': 
                            {'critical': 3000,
                            'non_critical': 10000},
                        'peers': 
                            {0: 
                                {'active_peers': 0,
                                'aggregates': 0,
                                'networks': 0,
                                'paths': 7,
                                'routes': 4}},
                        'table_id': '0x1',
                        'table_state': 'up'},
                    'ipv4 multicast': 
                        {'next_hop_trigger_delay': 
                            {'critical': 3000,
                            'non_critical': 10000},
                        'peers': 
                            {3: 
                                {'active_peers': 0,
                                'aggregates': 0,
                                'networks': 0,
                                'paths': 3,
                                'routes': 3}},
                        'redistribution': 
                            {'static': 
                                {'route_map': 'PERMIT_ALL_RM'}},
                        'route_reflector': True,
                        'table_id': '0x1',
                        'table_state': 'up'},
                    'ipv4 unicast': 
                        {'label_mode': 'per-prefix',
                        'next_hop_trigger_delay': 
                            {'critical': 3000,
                            'non_critical': 10000},
                        'peers': 
                            {5: 
                                {'active_peers': 0,
                                'aggregates': 1,
                                'networks': 1,
                                'paths': 7,
                                'routes': 4}},
                        'redistribution': 
                            {'static': 
                                {'route_map': 'ADD_RT_400_400'}},
                        'route_reflector': True,
                        'table_id': '0x1',
                        'table_state': 'up'},
                    'ipv6 multicast': 
                        {'next_hop_trigger_delay': 
                            {'critical': 3000,
                            'non_critical': 10000},
                        'peers': 
                            {4: 
                                {'active_peers': 0,
                                'aggregates': 0,
                                'networks': 0,
                                'paths': 3,
                                'routes': 3}},
                        'redistribution': 
                            {'static': 
                                {'route_map': 'PERMIT_ALL_RM'}},
                        'route_reflector': True,
                        'table_id': '0x80000001',
                        'table_state': 'up'},
                    'ipv6 unicast': 
                        {'next_hop_trigger_delay': 
                            {'critical': 3000,
                            'non_critical': 10000},
                        'peers': 
                            {4: 
                                {'active_peers': 0,
                                'aggregates': 0,
                                'networks': 0,
                                'paths': 5,
                                'routes': 3}},
                        'redistribution': 
                            {'static': 
                                {'route_map': 'PERMIT_ALL_RM'}},
                        'route_reflector': True,
                        'table_id': '0x80000001',
                        'table_state': 'up'},
                    'link-state': 
                        {'next_hop_trigger_delay': 
                            {'critical': 3000,
                            'non_critical': 10000},
                        'peers': 
                            {4: 
                                {'active_peers': 0,
                                'aggregates': 0,
                                'networks': 0,
                                'paths': 0,
                                'routes': 0}},
                        'route_reflector': True,
                        'table_id': '0x1',
                        'table_state': 'up'},
                    'vpnv4 unicast': 
                        {'next_hop_trigger_delay': 
                            {'critical': 4,
                            'non_critical': 5},
                        'peers': 
                            {3: 
                                {'active_peers': 0,
                                'aggregates': 0,
                                'networks': 0,
                                'paths': 7,
                                'routes': 5}},
                        'route_reflector': True,
                        'table_id': '0x1',
                        'table_state': 'up'},
                    'vpnv6 unicast': 
                        {'next_hop_trigger_delay': 
                            {'critical': 3000,
                            'non_critical': 10000},
                        'peers': 
                            {3: 
                                {'active_peers': 0,
                                'aggregates': 0,
                                'networks': 0,
                                'paths': 7,
                                'routes': 5}},
                        'route_reflector': True,
                        'table_id': '0x80000001',
                        'table_state': 'up'}},
                'cluster_id': '0.0.0.3',
                'conf_router_id': '0.0.0.0',
                'confed_id': 0,
                'num_conf_peers': 6,
                'num_established_peers': 0,
                'num_pending_conf_peers': 0,
                'router_id': '3.3.3.3',
                'vrf_id': '1',
                'vrf_rd': 'not configured',
                'vrf_state': 'up'},
            'management': 
                {'cluster_id': '0.0.0.0',
                'conf_router_id': '0.0.0.0',
                'confed_id': 0,
                'num_conf_peers': 1,
                'num_established_peers': 0,
                'num_pending_conf_peers': 0,
                'router_id': '0.0.0.0',
                'vrf_id': '2',
                'vrf_rd': 'not configured',
                'vrf_state': 'up'},
            'vpn1': 
                {'address_family': 
                    {'ipv4 multicast': 
                        {'next_hop_trigger_delay': 
                            {'critical': 3000,
                            'non_critical': 10000},
                        'peers': 
                            {0: 
                                {'active_peers': 0,
                                'aggregates': 0,
                                'networks': 0,
                                'paths': 2,
                                'routes': 2}},
                        'redistribution': 
                            {'static': {'route_map': 'PERMIT_ALL_RM'}},
                        'table_id': '0x5',
                        'table_state': 'up'},
                    'ipv4 unicast': 
                        {'aggregate_label': '492287',
                        'export_default_map': 'PERMIT_ALL_RM',
                        'export_default_prefix_count': 2,
                        'export_default_prefix_limit': 1000,
                        'export_rt_list': '100:1 '
                                          '400:400',
                        'import_default_map': 'PERMIT_ALL_RM',
                        'import_default_prefix_count': 3,
                        'import_default_prefix_limit': 1000,
                        'import_rt_list': '100:1',
                        'label_mode': 'per-vrf',
                        'next_hop_trigger_delay': 
                            {'critical': 3000,
                            'non_critical': 10000},
                        'peers': 
                            {2: 
                                {'active_peers': 0,
                                'aggregates': 0,
                                'networks': 0,
                                'paths': 5,
                                'routes': 3}},
                        'redistribution': 
                            {'static': {'route_map': 'PERMIT_ALL_RM'}},
                        'table_id': '0x5',
                        'table_state': 'up'},
                    'ipv6 multicast': 
                        {'next_hop_trigger_delay': 
                            {'critical': 3000,
                            'non_critical': 10000},
                        'peers': 
                            {0: 
                                {'active_peers': 0,
                                'aggregates': 0,
                                'networks': 0,
                                'paths': 2,
                                'routes': 2}},
                        'redistribution': 
                            {'static': {'route_map': 'PERMIT_ALL_RM'}},
                        'table_id': '0x80000005',
                        'table_state': 'up'},
                    'ipv6 unicast': 
                        {'aggregate_label': '492288',
                        'export_default_map': 'PERMIT_ALL_RM',
                        'export_default_prefix_count': 2,
                        'export_default_prefix_limit': 1000,
                        'export_rt_list': '1:100 '
                                          '600:600',
                        'import_default_map': 'PERMIT_ALL_RM',
                        'import_default_prefix_count': 3,
                        'import_default_prefix_limit': 1000,
                        'import_rt_list': '1:100',
                        'label_mode': 'per-vrf',
                        'next_hop_trigger_delay': 
                            {'critical': 3000,
                            'non_critical': 10000},
                        'peers': 
                            {2: 
                                {'active_peers': 0,
                                'aggregates': 0,
                                'networks': 0,
                                'paths': 5,
                                'routes': 3}},
                        'redistribution': 
                            {'static': {'route_map': 'PERMIT_ALL_RM'}},
                        'table_id': '0x80000005',
                        'table_state': 'up'}},
                'cluster_id': '0.0.0.0',
                'conf_router_id': '0.0.0.0',
                'confed_id': 0,
                'num_conf_peers': 2,
                'num_established_peers': 0,
                'num_pending_conf_peers': 0,
                'router_id': '33.33.33.33',
                'vrf_id': '5',
                'vrf_rd': '1:100',
                'vrf_state': 'up'},
            'vpn2': 
                {'address_family': 
                    {'ipv4 unicast': 
                        {'import_rt_list': '400:400',
                        'label_mode': 'per-vrf',
                        'next_hop_trigger_delay': 
                            {'critical': 3000,
                            'non_critical': 10000},
                        'peers': 
                            {0: 
                                {'active_peers': 0,
                                'aggregates': 0,
                                'networks': 0,
                                'paths': 2,
                                'routes': 2}},
                        'table_id': '0x6',
                        'table_state': 'up'},
                    'ipv6 unicast': 
                        {'import_rt_list': '600:600',
                        'label_mode': 'per-vrf',
                        'next_hop_trigger_delay': 
                            {'critical': 3000,
                            'non_critical': 10000},
                        'peers': 
                            {0: 
                                {'active_peers': 0,
                                'aggregates': 0,
                                'networks': 0,
                                'paths': 2,
                                'routes': 2}},
                        'table_id': '0x80000006',
                        'table_state': 'up'}},
                'cluster_id': '0.0.0.0',
                'conf_router_id': '0.0.0.0',
                'confed_id': 0,
                'num_conf_peers': 0,
                'num_established_peers': 0,
                'num_pending_conf_peers': 0,
                'router_id': '0.0.0.0',
                'vrf_id': '6',
                'vrf_rd': '2:100',
                'vrf_state': 'up'}}}

    golden_output2 = {'execute.return_value': '''
        BGP Process Information
        BGP Process ID                 : 26549
        BGP Protocol Started, reason:  : configuration
        BGP Performance Mode:          : No
        BGP Protocol Tag               : 333
        BGP Protocol State             : Running (Isolate)
        BGP Isolate Mode               : Yes
        BGP MMODE                      : Initialized
        BGP Memory State               : OK
        BGP asformat                   : asplain
        Segment Routing Global Block   : 10000-25000

        BGP attributes information
        Number of attribute entries    : 7
        HWM of attribute entries       : 8
        Bytes used by entries          : 784
        Entries pending delete         : 0
        HWM of entries pending delete  : 0
        BGP paths per attribute HWM    : 3
        BGP AS path entries            : 0
        Bytes used by AS path entries  : 0

        Confcheck capabilities in use:
          1. CAP_FEATURE_BGP_5_2_1 (refcount = 2)

        Information regarding configured VRFs:

        BGP Information for VRF VRF1
        VRF Id                         : 3
        VRF state                      : UP
        Router-ID                      : 0.0.0.0
        Configured Router-ID           : 0.0.0.0
        Confed-ID                      : 0
        Cluster-ID                     : 0.0.0.0
        No. of configured peers        : 2
        No. of pending config peers    : 0
        No. of established peers       : 0
        VRF RD                         : Not configured

        BGP Information for VRF ac
        VRF Id                         : 4
        VRF state                      : UP
        Router-ID                      : 0.0.0.0
        Configured Router-ID           : 0.0.0.0
        Confed-ID                      : 0
        Cluster-ID                     : 0.0.0.0
        No. of configured peers        : 1
        No. of pending config peers    : 0
        No. of established peers       : 0
        VRF RD                         : Not configured

            Information for address family IPv4 Unicast in VRF ac
            Table Id                   : 0x4
            Table state                : UP
            Peers      Active-peers    Routes     Paths      Networks   Aggregates
            1          0               0          0          0          0         

            Redistribution                
                None

            Wait for IGP convergence is not configured


            Nexthop trigger-delay
                critical 3000 ms
                non-critical 10000 ms

            Information for address family IPv6 Unicast in VRF ac
            Table Id                   : 0x80000004
            Table state                : UP
            Peers      Active-peers    Routes     Paths      Networks   Aggregates
            0          0               0          0          0          0         

            Redistribution                
                None

            Wait for IGP convergence is not configured


            Nexthop trigger-delay
                critical 3000 ms
                non-critical 10000 ms

        BGP Information for VRF default
        VRF Id                         : 1
        VRF state                      : UP
        Router-ID                      : 3.3.3.3
        Configured Router-ID           : 0.0.0.0
        Confed-ID                      : 0
        Cluster-ID                     : 0.0.0.3
        No. of configured peers        : 6
        No. of pending config peers    : 0
        No. of established peers       : 0
        VRF RD                         : Not configured

            Information for address family IPv4 Unicast in VRF default
            Table Id                   : 0x1
            Table state                : UP
            Peers      Active-peers    Routes     Paths      Networks   Aggregates
            5          0               4          7          1          1         

            Redistribution                
                static, route-map ADD_RT_400_400

            Wait for IGP convergence is not configured
            Label mode: per-prefix
            Is a Route-reflector


            Nexthop trigger-delay
                critical 3000 ms
                non-critical 10000 ms

            Information for address family IPv4 Multicast in VRF default
            Table Id                   : 0x1
            Table state                : UP
            Peers      Active-peers    Routes     Paths      Networks   Aggregates
            3          0               3          3          0          0         

            Redistribution                
                static, route-map PERMIT_ALL_RM

            Wait for IGP convergence is not configured
            Is a Route-reflector


            Nexthop trigger-delay
                critical 3000 ms
                non-critical 10000 ms

            Information for address family IPv6 Unicast in VRF default
            Table Id                   : 0x80000001
            Table state                : UP
            Peers      Active-peers    Routes     Paths      Networks   Aggregates
            4          0               3          5          0          0         

            Redistribution                
                static, route-map PERMIT_ALL_RM

            Wait for IGP convergence is not configured
            Is a Route-reflector


            Nexthop trigger-delay
                critical 3000 ms
                non-critical 10000 ms

            Information for address family IPv6 Multicast in VRF default
            Table Id                   : 0x80000001
            Table state                : UP
            Peers      Active-peers    Routes     Paths      Networks   Aggregates
            4          0               3          3          0          0         

            Redistribution                
                static, route-map PERMIT_ALL_RM

            Wait for IGP convergence is not configured
            Is a Route-reflector


            Nexthop trigger-delay
                critical 3000 ms
                non-critical 10000 ms

            Information for address family VPNv4 Unicast in VRF default
            Table Id                   : 0x1
            Table state                : UP
            Peers      Active-peers    Routes     Paths      Networks   Aggregates
            3          0               5          7          0          0         

            Redistribution                
                None

            Wait for IGP convergence is not configured
            Is a Route-reflector


            Nexthop trigger-delay
                critical 4 ms
                non-critical 5 ms

            Information for address family VPNv6 Unicast in VRF default
            Table Id                   : 0x80000001
            Table state                : UP
            Peers      Active-peers    Routes     Paths      Networks   Aggregates
            3          0               5          7          0          0         

            Redistribution                
                None

            Wait for IGP convergence is not configured
            Is a Route-reflector


            Nexthop trigger-delay
                critical 3000 ms
                non-critical 10000 ms

            Information for address family IPv4 Label Unicast in VRF default
            Table Id                   : 0x1
            Table state                : UP
            Peers      Active-peers    Routes     Paths      Networks   Aggregates
            0          0               4          7          0          0         

            Redistribution                
                None

            Wait for IGP convergence is not configured


            Nexthop trigger-delay
                critical 3000 ms
                non-critical 10000 ms

            Information for address family Link-State in VRF default
            Table Id                   : 0x1
            Table state                : UP
            Peers      Active-peers    Routes     Paths      Networks   Aggregates
            4          0               0          0          0          0         

            Redistribution                
                None

            Wait for IGP convergence is not configured
            Is a Route-reflector


            Nexthop trigger-delay
                critical 3000 ms
                non-critical 10000 ms

        BGP Information for VRF management
        VRF Id                         : 2
        VRF state                      : UP
        Router-ID                      : 0.0.0.0
        Configured Router-ID           : 0.0.0.0
        Confed-ID                      : 0
        Cluster-ID                     : 0.0.0.0
        No. of configured peers        : 1
        No. of pending config peers    : 0
        No. of established peers       : 0
        VRF RD                         : Not configured

        BGP Information for VRF vpn1
        VRF Id                         : 5
        VRF state                      : UP
        Router-ID                      : 33.33.33.33
        Configured Router-ID           : 0.0.0.0
        Confed-ID                      : 0
        Cluster-ID                     : 0.0.0.0
        No. of configured peers        : 2
        No. of pending config peers    : 0
        No. of established peers       : 0
        VRF RD                         : 1:100
        VRF EVPN RD                    : 1:100

            Information for address family IPv4 Unicast in VRF vpn1
            Table Id                   : 0x5
            Table state                : UP
            Peers      Active-peers    Routes     Paths      Networks   Aggregates
            2          0               3          5          0          0         

            Redistribution                
                static, route-map PERMIT_ALL_RM

            Wait for IGP convergence is not configured
            Import route-map PERMIT_ALL_RM
            Export route-map PERMIT_ALL_RM
            Export RT list:
                100:1
                400:400
            Import RT list:
                100:1
            Label mode: per-vrf
            Aggregate label: 492287
            Import default limit       : 1000
            Import default prefix count : 3
            Import default map         : PERMIT_ALL_RM
            Export default limit       : 1000
            Export default prefix count : 2
            Export default map         : PERMIT_ALL_RM


            Nexthop trigger-delay
                critical 3000 ms
                non-critical 10000 ms

            Information for address family IPv4 Multicast in VRF vpn1
            Table Id                   : 0x5
            Table state                : UP
            Peers      Active-peers    Routes     Paths      Networks   Aggregates
            0          0               2          2          0          0         

            Redistribution                
                static, route-map PERMIT_ALL_RM

            Wait for IGP convergence is not configured


            Nexthop trigger-delay
                critical 3000 ms
                non-critical 10000 ms

            Information for address family IPv6 Unicast in VRF vpn1
            Table Id                   : 0x80000005
            Table state                : UP
            Peers      Active-peers    Routes     Paths      Networks   Aggregates
            2          0               3          5          0          0         

            Redistribution                
                static, route-map PERMIT_ALL_RM

            Wait for IGP convergence is not configured
            Import route-map PERMIT_ALL_RM
            Export route-map PERMIT_ALL_RM
            Export RT list:
                1:100
                600:600
            Import RT list:
                1:100
            Label mode: per-vrf
            Aggregate label: 492288
            Import default limit       : 1000
            Import default prefix count : 3
            Import default map         : PERMIT_ALL_RM
            Export default limit       : 1000
            Export default prefix count : 2
            Export default map         : PERMIT_ALL_RM


            Nexthop trigger-delay
                critical 3000 ms
                non-critical 10000 ms

            Information for address family IPv6 Multicast in VRF vpn1
            Table Id                   : 0x80000005
            Table state                : UP
            Peers      Active-peers    Routes     Paths      Networks   Aggregates
            0          0               2          2          0          0         

            Redistribution                
                static, route-map PERMIT_ALL_RM

            Wait for IGP convergence is not configured


            Nexthop trigger-delay
                critical 3000 ms
                non-critical 10000 ms

        BGP Information for VRF vpn2
        VRF Id                         : 6
        VRF state                      : UP
        Router-ID                      : 0.0.0.0
        Configured Router-ID           : 0.0.0.0
        Confed-ID                      : 0
        Cluster-ID                     : 0.0.0.0
        No. of configured peers        : 0
        No. of pending config peers    : 0
        No. of established peers       : 0
        VRF RD                         : 2:100
        VRF EVPN RD                    : 2:100

            Information for address family IPv4 Unicast in VRF vpn2
            Table Id                   : 0x6
            Table state                : UP
            Peers      Active-peers    Routes     Paths      Networks   Aggregates
            0          0               2          2          0          0         

            Redistribution                
                None

            Wait for IGP convergence is not configured
            Import RT list:
                400:400
            Label mode: per-vrf


            Nexthop trigger-delay
                critical 3000 ms
                non-critical 10000 ms

            Information for address family IPv6 Unicast in VRF vpn2
            Table Id                   : 0x80000006
            Table state                : UP
            Peers      Active-peers    Routes     Paths      Networks   Aggregates
            0          0               2          2          0          0         

            Redistribution                
                None

            Wait for IGP convergence is not configured
            Import RT list:
                600:600
            Label mode: per-vrf


            Nexthop trigger-delay
                critical 3000 ms
                non-critical 10000 ms
        '''}

    def test_show_bgp_process_vrf_all_golden1_cli(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output1)
        obj = ShowBgpProcessVrfAll(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output1)

    def test_show_bgp_process_vrf_all_golden2_cli(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output2)
        obj = ShowBgpProcessVrfAll(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output2)

    def test_show_bgp_process_vrf_all_empty_cli(self):
        self.device = Mock(**self.empty_output)
        obj = ShowBgpProcessVrfAll(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()


class test_show_bgp_process_vrf_all_xml(unittest.TestCase):

    '''Unit test for show bgp process vrf all - XML'''
    
    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output = {
        'bgp_as_path_entries': 0,
        'bgp_asformat': 'asplain',
        'bgp_isolate_mode': 'No',
        'bgp_memory_state': 'ok',
        'bgp_mmode': 'Initialized',
        'bgp_paths_per_hwm_attr': 3,
        'bgp_performance_mode': 'No',
        'bgp_pid': 23800,
        'bgp_protocol_started_reason': 'configuration',
        'bgp_protocol_state': 'running',
        'bgp_tag': '333',
        'bytes_used': 560,
        'bytes_used_as_path_entries': 0,
        'entries_pending_delete': 0,
        'hwm_attr_entries': 5,
        'hwm_entries_pending_delete': 0,
        'num_attr_entries': 5,
        'segment_routing_global_block': '10000-25000',
        'vrf': 
            {'ac': 
                {'address_family': 
                    {'ipv4 unicast': 
                        {'next_hop_trigger_delay': 
                            {'critical': 3000,
                            'non_critical': 10000},
                        'peers':
                            {0:
                                {'active_peers': 0,
                                'aggregates': 0,
                                'networks': 0,
                                'paths': 0,
                                'routes': 0}},
                        'table_id': '0x4',
                        'table_state': 'up'},
                    'ipv6 unicast':
                        {'next_hop_trigger_delay':
                            {'critical': 3000,
                            'non_critical': 10000},
                        'peers':
                            {0:
                                {'active_peers': 0,
                                'aggregates': 0,
                                'networks': 0,
                                'paths': 0,
                                'routes': 0}},
                        'table_id': '0x80000004',
                        'table_state': 'up'}},
                'cluster_id': '0.0.0.0',
                'conf_router_id': '0.0.0.0',
                'confed_id': 0,
                'num_conf_peers': 0,
                'num_established_peers': 0,
                'num_pending_conf_peers': 0,
                'router_id': '0.0.0.0',
                'vrf_id': '4',
                'vrf_rd': 'not configured',
                'vrf_state': 'up'},
            'default':
                {'address_family':
                    {'ipv4 label unicast':
                        {'next_hop_trigger_delay':
                            {'critical': 3000,
                            'non_critical': 10000},
                        'peers':
                            {0:
                                {'active_peers': 0,
                                'aggregates': 0,
                                'networks': 0,
                                'paths': 5,
                                'routes': 3}},
                        'table_id': '0x1',
                        'table_state': 'up'},
                    'ipv4 multicast':
                        {'next_hop_trigger_delay':
                            {'critical': 3000,
                            'non_critical': 10000},
                        'peers':
                            {3:
                                {'active_peers': 0,
                                'aggregates': 0,
                                'networks': 0,
                                'paths': 3,
                                'routes': 3}},
                        'redistribution':
                            {'static':
                                {'route_map': 'PERMIT_ALL_RM'}},
                        'route_reflector': True,
                        'table_id': '0x1',
                        'table_state': 'up'},
                    'ipv4 unicast':
                        {'label_mode': 'per-prefix',
                        'next_hop_trigger_delay':
                            {'critical': 3000,
                            'non_critical': 10000},
                        'peers':
                            {5:
                                {'active_peers': 0,
                                'aggregates': 0,
                                'networks': 0,
                                'paths': 5,
                                'routes': 3}},
                        'redistribution':
                            {'static':
                                {'route_map': 'ADD_RT_400_400'}},
                        'route_reflector': True,
                        'table_id': '0x1',
                        'table_state': 'up'},
                    'ipv6 multicast':
                        {'next_hop_trigger_delay':
                            {'critical': 3000,
                                              'non_critical': 10000},
                        'peers':
                            {4:
                                {'active_peers': 0,
                                'aggregates': 0,
                                'networks': 0,
                                'paths': 3,
                                'routes': 3}},
                        'redistribution':
                            {'static':
                                {'route_map': 'PERMIT_ALL_RM'}},
                        'route_reflector': True,
                        'table_id': '0x80000001',
                        'table_state': 'up'},
                    'ipv6 unicast':
                        {'next_hop_trigger_delay':
                            {'critical': 3000,
                            'non_critical': 10000},
                        'peers':
                            {4:
                                {'active_peers': 0,
                                'aggregates': 0,
                                'networks': 0,
                                'paths': 5,
                                'routes': 3}},
                        'redistribution':
                            {'static':
                                {'route_map': 'PERMIT_ALL_RM'}},
                        'route_reflector': True,
                        'table_id': '0x80000001',
                        'table_state': 'up'},
                    'link-state':
                        {'next_hop_trigger_delay':
                            {'critical': 3000,
                            'non_critical': 10000},
                        'peers':
                            {4:
                                {'active_peers': 0,
                                'aggregates': 0,
                                'networks': 0,
                                'paths': 0,
                                'routes': 0}},
                        'route_reflector': True,
                        'table_id': '0x1',
                        'table_state': 'up'},
                    'vpnv4 unicast':
                        {'next_hop_trigger_delay':
                            {'critical': 3000,
                            'non_critical': 10000},
                        'peers':
                            {3:
                                {'active_peers': 0,
                                'aggregates': 0,
                                'networks': 0,
                                'paths': 7,
                                'routes': 5}},
                        'route_reflector': True,
                        'table_id': '0x1',
                        'table_state': 'up'},
                    'vpnv6 unicast':
                        {'next_hop_trigger_delay':
                            {'critical': 3000,
                            'non_critical': 10000},
                        'peers':
                            {3:
                                {'active_peers': 0,
                                'aggregates': 0,
                                'networks': 0,
                                'paths': 7,
                                'routes': 5}},
                        'route_reflector': True,
                        'table_id': '0x80000001',
                        'table_state': 'up'}},
                'cluster_id': '0.0.0.0',
                'conf_router_id': '0.0.0.0',
                'confed_id': 0,
                'num_conf_peers': 6,
                'num_established_peers': 0,
                'num_pending_conf_peers': 0,
                'router_id': '3.3.3.3',
                'vrf_id': '1',
                'vrf_rd': 'not configured',
                'vrf_state': 'up'},
            'management':
                {'cluster_id': '0.0.0.0',
                'conf_router_id': '0.0.0.0',
                'confed_id': 0,
                'num_conf_peers': 1,
                'num_established_peers': 0,
                'num_pending_conf_peers': 0,
                'router_id': '0.0.0.0',
                'vrf_id': '2',
                'vrf_rd': 'not configured',
                'vrf_state': 'up'},
            'vpn1':
                {'address_family':
                    {'ipv4 multicast':
                        {'next_hop_trigger_delay':
                            {'critical': 3000,
                            'non_critical': 10000},
                        'peers':
                            {0:
                                {'active_peers': 0,
                                'aggregates': 0,
                                'networks': 0,
                                'paths': 2,
                                'routes': 2}},
                        'redistribution':
                            {'static':
                                {'route_map': 'PERMIT_ALL_RM'}},
                        'table_id': '0x5',
                        'table_state': 'up'},
                    'ipv4 unicast':
                        {'aggregate_label': '492287',
                        'export_default_map': 'PERMIT_ALL_RM',
                        'export_default_prefix_count': 2,
                        'export_default_prefix_limit': 1000,
                        'export_rt_list': '100:1 400:400',
                        'import_default_map': 'PERMIT_ALL_RM',
                        'import_default_prefix_count': 3,
                        'import_default_prefix_limit': 1000,
                        'import_rt_list': '100:1',
                        'label_mode': 'per-vrf',
                        'next_hop_trigger_delay':
                            {'critical': 3000,
                            'non_critical': 10000},
                        'peers':
                            {0:
                                {'active_peers': 0,
                                'aggregates': 0,
                                'networks': 0,
                                'paths': 5,
                                'routes': 3}},
                        'redistribution':
                            {'static':
                                {'route_map': 'PERMIT_ALL_RM'}},
                        'table_id': '0x5',
                        'table_state': 'up'},
                    'ipv6 multicast':
                        {'next_hop_trigger_delay':
                            {'critical': 3000,
                            'non_critical': 10000},
                        'peers':
                            {0:
                                {'active_peers': 0,
                                'aggregates': 0,
                                'networks': 0,
                                'paths': 2,
                                'routes': 2}},
                        'redistribution':
                            {'static':
                                {'route_map': 'PERMIT_ALL_RM'}},
                        'table_id': '0x80000005',
                        'table_state': 'up'},
                    'ipv6 unicast':
                        {'aggregate_label': '492288',
                        'export_default_map': 'PERMIT_ALL_RM',
                        'export_default_prefix_count': 2,
                        'export_default_prefix_limit': 1000,
                        'export_rt_list': '1:100 600:600',
                        'import_default_map': 'PERMIT_ALL_RM',
                        'import_default_prefix_count': 3,
                        'import_default_prefix_limit': 1000,
                        'import_rt_list': '1:100',
                        'label_mode': 'per-vrf',
                        'next_hop_trigger_delay': {'critical': 3000,
                                             'non_critical': 10000},
                        'peers': {0: {'active_peers': 0,
                                'aggregates': 0,
                                'networks': 0,
                                'paths': 5,
                                'routes': 3}},
                        'redistribution':
                            {'static':
                                {'route_map': 'PERMIT_ALL_RM'}},
                        'table_id': '0x80000005',
                        'table_state': 'up'}},
                'cluster_id': '0.0.0.0',
                'conf_router_id': '0.0.0.0',
                'confed_id': 0,
                'num_conf_peers': 0,
                'num_established_peers': 0,
                'num_pending_conf_peers': 0,
                'router_id': '0.0.0.0',
                'vrf_id': '5',
                'vrf_rd': '1:100',
                'vrf_state': 'up'},
            'vpn2':
                {'address_family':
                    {'ipv4 unicast':
                        {'import_rt_list': '400:400',
                        'label_mode': 'per-vrf',
                        'next_hop_trigger_delay':
                            {'critical': 3000,
                            'non_critical': 10000},
                        'peers':
                            {0:
                                {'active_peers': 0,
                                'aggregates': 0,
                                'networks': 0,
                                'paths': 2,
                                'routes': 2}},
                        'table_id': '0x6',
                        'table_state': 'up'},
                    'ipv6 unicast':
                        {'import_rt_list': '600:600',
                        'label_mode': 'per-vrf',
                        'next_hop_trigger_delay':
                            {'critical': 3000,
                            'non_critical': 10000},
                        'peers':
                            {0:
                                {'active_peers': 0,
                                'aggregates': 0,
                                'networks': 0,
                                'paths': 2,
                                'routes': 2}},
                        'table_id': '0x80000006',
                        'table_state': 'up'}},
                'cluster_id': '0.0.0.0',
                'conf_router_id': '0.0.0.0',
                'confed_id': 0,
                'num_conf_peers': 0,
                'num_established_peers': 0,
                'num_pending_conf_peers': 0,
                'router_id': '0.0.0.0',
                'vrf_id': '6',
                'vrf_rd': '2:100',
                'vrf_state': 'up'}}}

    golden_output = {'execute.return_value': '''<?xml version="1.0" encoding="ISO-8859-1"?>
        <nf:rpc-reply xmlns="http://www.cisco.com/nxos:1.0:bgp" xmlns:nf="urn:ietf:params:xml:ns:netconf:base:1.0">
         <nf:data>
          <show>
           <bgp>
            <__XML__OPT_Cmd_show_ip_bgp_session_cmd_vrf>
             <process>
              <__XML__OPT_Cmd_show_bgp_process_cmd_vrf>
               <__XML__OPT_Cmd_show_bgp_process_cmd___readonly__>
                <__readonly__>
                 <processid>23800</processid>
                 <protocolstartedreason>configuration</protocolstartedreason>
                 <protocoltag>333</protocoltag>
                 <protocolstate>Running</protocolstate>
                 <isolatemode>No</isolatemode>
                 <mmode>Initialized</mmode>
                 <memorystate>OK</memorystate>
                 <forwardingstatesaved>false</forwardingstatesaved>
                 <asformat>asplain</asformat>
                 <srgbmin>10000</srgbmin>
                 <srgbmax>25000</srgbmax>
                 <attributeentries>5</attributeentries>
                 <hwmattributeentries>5</hwmattributeentries>
                 <bytesused>560</bytesused>
                 <entriespendingdelete>0</entriespendingdelete>
                 <hwmentriespendingdelete>0</hwmentriespendingdelete>
                 <pathsperattribute>3</pathsperattribute>
                 <aspathentries>0</aspathentries>
                 <aspathbytes>0</aspathbytes>
                 <TABLE_vrf>
                  <ROW_vrf>
                   <vrf-name-out>ac</vrf-name-out>
                   <vrf-id>4</vrf-id>
                   <vrf-state>UP</vrf-state>
                   <vrf-delete-pending>false</vrf-delete-pending>
                   <vrf-router-id>0.0.0.0</vrf-router-id>
                   <vrf-cfgd-id>0.0.0.0</vrf-cfgd-id>
                   <vrf-confed-id>0</vrf-confed-id>
                   <vrf-cluster-id>0.0.0.0</vrf-cluster-id>
                   <vrf-peers>0</vrf-peers>
                   <vrf-pending-peers>0</vrf-pending-peers>
                   <vrf-est-peers>0</vrf-est-peers>
                   <TABLE_af>
                    <ROW_af>
                     <af-id>0</af-id>
                     <af-name>IPv4 Unicast</af-name>
                     <af-table-id>4</af-table-id>
                     <af-state>UP</af-state>
                     <af-num-peers>0</af-num-peers>
                     <af-num-active-peers>0</af-num-active-peers>
                     <af-peer-routes>0</af-peer-routes>
                     <af-peer-paths>0</af-peer-paths>
                     <af-peer-networks>0</af-peer-networks>
                     <af-peer-aggregates>0</af-peer-aggregates>
                     <af-rr>false</af-rr>
                     <default-information-enabled>false</default-information-enabled>
                     <nexthop-trigger-delay-critical>3000</nexthop-trigger-delay-critical>
                     <nexthop-trigger-delay-non-critical>10000</nexthop-trigger-delay-non-critical>
                    </ROW_af>
                    <ROW_af>
                     <af-id>2</af-id>
                     <af-name>IPv6 Unicast</af-name>
                     <af-table-id>80000004</af-table-id>
                     <af-state>UP</af-state>
                     <af-num-peers>0</af-num-peers>
                     <af-num-active-peers>0</af-num-active-peers>
                     <af-peer-routes>0</af-peer-routes>
                     <af-peer-paths>0</af-peer-paths>
                     <af-peer-networks>0</af-peer-networks>
                     <af-peer-aggregates>0</af-peer-aggregates>
                     <af-rr>false</af-rr>
                     <default-information-enabled>false</default-information-enabled>
                     <nexthop-trigger-delay-critical>3000</nexthop-trigger-delay-critical>
                     <nexthop-trigger-delay-non-critical>10000</nexthop-trigger-delay-non-critical>
                    </ROW_af>
                   </TABLE_af>
                  </ROW_vrf>
                  <ROW_vrf>
                   <vrf-name-out>default</vrf-name-out>
                   <vrf-id>1</vrf-id>
                   <vrf-state>UP</vrf-state>
                   <vrf-delete-pending>false</vrf-delete-pending>
                   <vrf-router-id>3.3.3.3</vrf-router-id>
                   <vrf-cfgd-id>0.0.0.0</vrf-cfgd-id>
                   <vrf-confed-id>0</vrf-confed-id>
                   <vrf-cluster-id>0.0.0.0</vrf-cluster-id>
                   <vrf-peers>6</vrf-peers>
                   <vrf-pending-peers>0</vrf-pending-peers>
                   <vrf-est-peers>0</vrf-est-peers>
                   <TABLE_af>
                    <ROW_af>
                     <af-id>0</af-id>
                     <af-name>IPv4 Unicast</af-name>
                     <af-table-id>1</af-table-id>
                     <af-state>UP</af-state>
                     <af-num-peers>5</af-num-peers>
                     <af-num-active-peers>0</af-num-active-peers>
                     <af-peer-routes>3</af-peer-routes>
                     <af-peer-paths>5</af-peer-paths>
                     <af-peer-networks>0</af-peer-networks>
                     <af-peer-aggregates>0</af-peer-aggregates>
                     <TABLE_redist>
                      <ROW_redist>
                       <protocol>static</protocol>
                       <route-map>ADD_RT_400_400</route-map>
                      </ROW_redist>
                     </TABLE_redist>
                     <af-label-mode>per-prefix</af-label-mode>
                     <af-rr>true</af-rr>
                     <default-information-enabled>false</default-information-enabled>
                     <nexthop-trigger-delay-critical>3000</nexthop-trigger-delay-critical>
                     <nexthop-trigger-delay-non-critical>10000</nexthop-trigger-delay-non-critical>
                    </ROW_af>
                    <ROW_af>
                     <af-id>1</af-id>
                     <af-name>IPv4 Multicast</af-name>
                     <af-table-id>1</af-table-id>
                     <af-state>UP</af-state>
                     <af-num-peers>3</af-num-peers>
                     <af-num-active-peers>0</af-num-active-peers>
                     <af-peer-routes>3</af-peer-routes>
                     <af-peer-paths>3</af-peer-paths>
                     <af-peer-networks>0</af-peer-networks>
                     <af-peer-aggregates>0</af-peer-aggregates>
                     <TABLE_redist>
                      <ROW_redist>
                       <protocol>static</protocol>
                       <route-map>PERMIT_ALL_RM</route-map>
                      </ROW_redist>
                     </TABLE_redist>
                     <af-rr>true</af-rr>
                     <default-information-enabled>false</default-information-enabled>
                     <nexthop-trigger-delay-critical>3000</nexthop-trigger-delay-critical>
                     <nexthop-trigger-delay-non-critical>10000</nexthop-trigger-delay-non-critical>
                    </ROW_af>
                    <ROW_af>
                     <af-id>2</af-id>
                     <af-name>IPv6 Unicast</af-name>
                     <af-table-id>80000001</af-table-id>
                     <af-state>UP</af-state>
                     <af-num-peers>4</af-num-peers>
                     <af-num-active-peers>0</af-num-active-peers>
                     <af-peer-routes>3</af-peer-routes>
                     <af-peer-paths>5</af-peer-paths>
                     <af-peer-networks>0</af-peer-networks>
                     <af-peer-aggregates>0</af-peer-aggregates>
                     <TABLE_redist>
                      <ROW_redist>
                       <protocol>static</protocol>
                       <route-map>PERMIT_ALL_RM</route-map>
                      </ROW_redist>
                     </TABLE_redist>
                     <af-rr>true</af-rr>
                     <default-information-enabled>false</default-information-enabled>
                     <nexthop-trigger-delay-critical>3000</nexthop-trigger-delay-critical>
                     <nexthop-trigger-delay-non-critical>10000</nexthop-trigger-delay-non-critical>
                    </ROW_af>
                    <ROW_af>
                     <af-id>3</af-id>
                     <af-name>IPv6 Multicast</af-name>
                     <af-table-id>80000001</af-table-id>
                     <af-state>UP</af-state>
                     <af-num-peers>4</af-num-peers>
                     <af-num-active-peers>0</af-num-active-peers>
                     <af-peer-routes>3</af-peer-routes>
                     <af-peer-paths>3</af-peer-paths>
                     <af-peer-networks>0</af-peer-networks>
                     <af-peer-aggregates>0</af-peer-aggregates>
                     <TABLE_redist>
                      <ROW_redist>
                       <protocol>static</protocol>
                       <route-map>PERMIT_ALL_RM</route-map>
                      </ROW_redist>
                     </TABLE_redist>
                     <af-rr>true</af-rr>
                     <default-information-enabled>false</default-information-enabled>
                     <nexthop-trigger-delay-critical>3000</nexthop-trigger-delay-critical>
                     <nexthop-trigger-delay-non-critical>10000</nexthop-trigger-delay-non-critical>
                    </ROW_af>
                    <ROW_af>
                     <af-id>4</af-id>
                     <af-name>VPNv4 Unicast</af-name>
                     <af-table-id>1</af-table-id>
                     <af-state>UP</af-state>
                     <af-num-peers>3</af-num-peers>
                     <af-num-active-peers>0</af-num-active-peers>
                     <af-peer-routes>5</af-peer-routes>
                     <af-peer-paths>7</af-peer-paths>
                     <af-peer-networks>0</af-peer-networks>
                     <af-peer-aggregates>0</af-peer-aggregates>
                     <af-rr>true</af-rr>
                     <default-information-enabled>false</default-information-enabled>
                     <nexthop-trigger-delay-critical>3000</nexthop-trigger-delay-critical>
                     <nexthop-trigger-delay-non-critical>10000</nexthop-trigger-delay-non-critical>
                    </ROW_af>
                    <ROW_af>
                     <af-id>5</af-id>
                     <af-name>VPNv6 Unicast</af-name>
                     <af-table-id>80000001</af-table-id>
                     <af-state>UP</af-state>
                     <af-num-peers>3</af-num-peers>
                     <af-num-active-peers>0</af-num-active-peers>
                     <af-peer-routes>5</af-peer-routes>
                     <af-peer-paths>7</af-peer-paths>
                     <af-peer-networks>0</af-peer-networks>
                     <af-peer-aggregates>0</af-peer-aggregates>
                     <af-rr>true</af-rr>
                     <default-information-enabled>false</default-information-enabled>
                     <nexthop-trigger-delay-critical>3000</nexthop-trigger-delay-critical>
                     <nexthop-trigger-delay-non-critical>10000</nexthop-trigger-delay-non-critical>
                    </ROW_af>
                    <ROW_af>
                     <af-id>11</af-id>
                     <af-name>IPv4 Label Unicast</af-name>
                     <af-table-id>1</af-table-id>
                     <af-state>UP</af-state>
                     <af-num-peers>0</af-num-peers>
                     <af-num-active-peers>0</af-num-active-peers>
                     <af-peer-routes>3</af-peer-routes>
                     <af-peer-paths>5</af-peer-paths>
                     <af-peer-networks>0</af-peer-networks>
                     <af-peer-aggregates>0</af-peer-aggregates>
                     <af-rr>false</af-rr>
                     <default-information-enabled>false</default-information-enabled>
                     <nexthop-trigger-delay-critical>3000</nexthop-trigger-delay-critical>
                     <nexthop-trigger-delay-non-critical>10000</nexthop-trigger-delay-non-critical>
                    </ROW_af>
                    <ROW_af>
                     <af-id>13</af-id>
                     <af-name>Link-State</af-name>
                     <af-table-id>1</af-table-id>
                     <af-state>UP</af-state>
                     <af-num-peers>4</af-num-peers>
                     <af-num-active-peers>0</af-num-active-peers>
                     <af-peer-routes>0</af-peer-routes>
                     <af-peer-paths>0</af-peer-paths>
                     <af-peer-networks>0</af-peer-networks>
                     <af-peer-aggregates>0</af-peer-aggregates>
                     <af-rr>true</af-rr>
                     <default-information-enabled>false</default-information-enabled>
                     <nexthop-trigger-delay-critical>3000</nexthop-trigger-delay-critical>
                     <nexthop-trigger-delay-non-critical>10000</nexthop-trigger-delay-non-critical>
                    </ROW_af>
                   </TABLE_af>
                  </ROW_vrf>
                  <ROW_vrf>
                   <vrf-name-out>management</vrf-name-out>
                   <vrf-id>2</vrf-id>
                   <vrf-state>UP</vrf-state>
                   <vrf-delete-pending>false</vrf-delete-pending>
                   <vrf-router-id>0.0.0.0</vrf-router-id>
                   <vrf-cfgd-id>0.0.0.0</vrf-cfgd-id>
                   <vrf-confed-id>0</vrf-confed-id>
                   <vrf-cluster-id>0.0.0.0</vrf-cluster-id>
                   <vrf-peers>1</vrf-peers>
                   <vrf-pending-peers>0</vrf-pending-peers>
                   <vrf-est-peers>0</vrf-est-peers>
                  </ROW_vrf>
                  <ROW_vrf>
                   <vrf-name-out>vpn1</vrf-name-out>
                   <vrf-id>5</vrf-id>
                   <vrf-state>UP</vrf-state>
                   <vrf-delete-pending>false</vrf-delete-pending>
                   <vrf-router-id>0.0.0.0</vrf-router-id>
                   <vrf-cfgd-id>0.0.0.0</vrf-cfgd-id>
                   <vrf-confed-id>0</vrf-confed-id>
                   <vrf-cluster-id>0.0.0.0</vrf-cluster-id>
                   <vrf-peers>0</vrf-peers>
                   <vrf-pending-peers>0</vrf-pending-peers>
                   <vrf-est-peers>0</vrf-est-peers>
                   <vrf-rd>1:100</vrf-rd>
                   <TABLE_af>
                    <ROW_af>
                     <af-id>0</af-id>
                     <af-name>IPv4 Unicast</af-name>
                     <af-table-id>5</af-table-id>
                     <af-state>UP</af-state>
                     <af-num-peers>0</af-num-peers>
                     <af-num-active-peers>0</af-num-active-peers>
                     <af-peer-routes>3</af-peer-routes>
                     <af-peer-paths>5</af-peer-paths>
                     <af-peer-networks>0</af-peer-networks>
                     <af-peer-aggregates>0</af-peer-aggregates>
                     <TABLE_redist>
                      <ROW_redist>
                       <protocol>static</protocol>
                       <route-map>PERMIT_ALL_RM</route-map>
                      </ROW_redist>
                     </TABLE_redist>
                     <af-import-rmap>PERMIT_ALL_RM</af-import-rmap>
                     <af-export-rmap>PERMIT_ALL_RM</af-export-rmap>
                     <TABLE_evpn_export_rt>
                      <ROW_evpn_export_rt>
                       <evpn-export-rt>100:1</evpn-export-rt>
                      </ROW_evpn_export_rt>
                      <ROW_evpn_export_rt>
                       <evpn-export-rt>400:400</evpn-export-rt>
                      </ROW_evpn_export_rt>
                     </TABLE_evpn_export_rt>
                     <TABLE_evpn_import_rt>
                      <ROW_evpn_import_rt>
                       <evpn-import-rt>100:1</evpn-import-rt>
                      </ROW_evpn_import_rt>
                     </TABLE_evpn_import_rt>
                     <af-label-mode>per-vrf</af-label-mode>
                     <af-aggregate-label>492287</af-aggregate-label>
                     <importdefault_prefixlimit>1000</importdefault_prefixlimit>
                     <importdefault_prefixcount>3</importdefault_prefixcount>
                     <importdefault_map>PERMIT_ALL_RM</importdefault_map>
                     <exportdefault_prefixlimit>1000</exportdefault_prefixlimit>
                     <exportdefault_prefixcount>2</exportdefault_prefixcount>
                     <exportdefault_map>PERMIT_ALL_RM</exportdefault_map>
                     <af-rr>false</af-rr>
                     <default-information-enabled>false</default-information-enabled>
                     <nexthop-trigger-delay-critical>3000</nexthop-trigger-delay-critical>
                     <nexthop-trigger-delay-non-critical>10000</nexthop-trigger-delay-non-critical>
                    </ROW_af>
                    <ROW_af>
                     <af-id>1</af-id>
                     <af-name>IPv4 Multicast</af-name>
                     <af-table-id>5</af-table-id>
                     <af-state>UP</af-state>
                     <af-num-peers>0</af-num-peers>
                     <af-num-active-peers>0</af-num-active-peers>
                     <af-peer-routes>2</af-peer-routes>
                     <af-peer-paths>2</af-peer-paths>
                     <af-peer-networks>0</af-peer-networks>
                     <af-peer-aggregates>0</af-peer-aggregates>
                     <TABLE_redist>
                      <ROW_redist>
                       <protocol>static</protocol>
                       <route-map>PERMIT_ALL_RM</route-map>
                      </ROW_redist>
                     </TABLE_redist>
                     <af-rr>false</af-rr>
                     <default-information-enabled>false</default-information-enabled>
                     <nexthop-trigger-delay-critical>3000</nexthop-trigger-delay-critical>
                     <nexthop-trigger-delay-non-critical>10000</nexthop-trigger-delay-non-critical>
                    </ROW_af>
                    <ROW_af>
                     <af-id>2</af-id>
                     <af-name>IPv6 Unicast</af-name>
                     <af-table-id>80000005</af-table-id>
                     <af-state>UP</af-state>
                     <af-num-peers>0</af-num-peers>
                     <af-num-active-peers>0</af-num-active-peers>
                     <af-peer-routes>3</af-peer-routes>
                     <af-peer-paths>5</af-peer-paths>
                     <af-peer-networks>0</af-peer-networks>
                     <af-peer-aggregates>0</af-peer-aggregates>
                     <TABLE_redist>
                      <ROW_redist>
                       <protocol>static</protocol>
                       <route-map>PERMIT_ALL_RM</route-map>
                      </ROW_redist>
                     </TABLE_redist>
                     <af-import-rmap>PERMIT_ALL_RM</af-import-rmap>
                     <af-export-rmap>PERMIT_ALL_RM</af-export-rmap>
                     <TABLE_evpn_export_rt>
                      <ROW_evpn_export_rt>
                       <evpn-export-rt>1:100</evpn-export-rt>
                      </ROW_evpn_export_rt>
                      <ROW_evpn_export_rt>
                       <evpn-export-rt>600:600</evpn-export-rt>
                      </ROW_evpn_export_rt>
                     </TABLE_evpn_export_rt>
                     <TABLE_evpn_import_rt>
                      <ROW_evpn_import_rt>
                       <evpn-import-rt>1:100</evpn-import-rt>
                      </ROW_evpn_import_rt>
                     </TABLE_evpn_import_rt>
                     <af-label-mode>per-vrf</af-label-mode>
                     <af-aggregate-label>492288</af-aggregate-label>
                     <importdefault_prefixlimit>1000</importdefault_prefixlimit>
                     <importdefault_prefixcount>3</importdefault_prefixcount>
                     <importdefault_map>PERMIT_ALL_RM</importdefault_map>
                     <exportdefault_prefixlimit>1000</exportdefault_prefixlimit>
                     <exportdefault_prefixcount>2</exportdefault_prefixcount>
                     <exportdefault_map>PERMIT_ALL_RM</exportdefault_map>
                     <af-rr>false</af-rr>
                     <default-information-enabled>false</default-information-enabled>
                     <nexthop-trigger-delay-critical>3000</nexthop-trigger-delay-critical>
                     <nexthop-trigger-delay-non-critical>10000</nexthop-trigger-delay-non-critical>
                    </ROW_af>
                    <ROW_af>
                     <af-id>3</af-id>
                     <af-name>IPv6 Multicast</af-name>
                     <af-table-id>80000005</af-table-id>
                     <af-state>UP</af-state>
                     <af-num-peers>0</af-num-peers>
                     <af-num-active-peers>0</af-num-active-peers>
                     <af-peer-routes>2</af-peer-routes>
                     <af-peer-paths>2</af-peer-paths>
                     <af-peer-networks>0</af-peer-networks>
                     <af-peer-aggregates>0</af-peer-aggregates>
                     <TABLE_redist>
                      <ROW_redist>
                       <protocol>static</protocol>
                       <route-map>PERMIT_ALL_RM</route-map>
                      </ROW_redist>
                     </TABLE_redist>
                     <af-rr>false</af-rr>
                     <default-information-enabled>false</default-information-enabled>
                     <nexthop-trigger-delay-critical>3000</nexthop-trigger-delay-critical>
                     <nexthop-trigger-delay-non-critical>10000</nexthop-trigger-delay-non-critical>
                    </ROW_af>
                   </TABLE_af>
                  </ROW_vrf>
                  <ROW_vrf>
                   <vrf-name-out>vpn2</vrf-name-out>
                   <vrf-id>6</vrf-id>
                   <vrf-state>UP</vrf-state>
                   <vrf-delete-pending>false</vrf-delete-pending>
                   <vrf-router-id>0.0.0.0</vrf-router-id>
                   <vrf-cfgd-id>0.0.0.0</vrf-cfgd-id>
                   <vrf-confed-id>0</vrf-confed-id>
                   <vrf-cluster-id>0.0.0.0</vrf-cluster-id>
                   <vrf-peers>0</vrf-peers>
                   <vrf-pending-peers>0</vrf-pending-peers>
                   <vrf-est-peers>0</vrf-est-peers>
                   <vrf-rd>2:100</vrf-rd>
                   <TABLE_af>
                    <ROW_af>
                     <af-id>0</af-id>
                     <af-name>IPv4 Unicast</af-name>
                     <af-table-id>6</af-table-id>
                     <af-state>UP</af-state>
                     <af-num-peers>0</af-num-peers>
                     <af-num-active-peers>0</af-num-active-peers>
                     <af-peer-routes>2</af-peer-routes>
                     <af-peer-paths>2</af-peer-paths>
                     <af-peer-networks>0</af-peer-networks>
                     <af-peer-aggregates>0</af-peer-aggregates>
                     <TABLE_evpn_import_rt>
                      <ROW_evpn_import_rt>
                       <evpn-import-rt>400:400</evpn-import-rt>
                      </ROW_evpn_import_rt>
                     </TABLE_evpn_import_rt>
                     <af-label-mode>per-vrf</af-label-mode>
                     <af-rr>false</af-rr>
                     <default-information-enabled>false</default-information-enabled>
                     <nexthop-trigger-delay-critical>3000</nexthop-trigger-delay-critical>
                     <nexthop-trigger-delay-non-critical>10000</nexthop-trigger-delay-non-critical>
                    </ROW_af>
                    <ROW_af>
                     <af-id>2</af-id>
                     <af-name>IPv6 Unicast</af-name>
                     <af-table-id>80000006</af-table-id>
                     <af-state>UP</af-state>
                     <af-num-peers>0</af-num-peers>
                     <af-num-active-peers>0</af-num-active-peers>
                     <af-peer-routes>2</af-peer-routes>
                     <af-peer-paths>2</af-peer-paths>
                     <af-peer-networks>0</af-peer-networks>
                     <af-peer-aggregates>0</af-peer-aggregates>
                     <TABLE_evpn_import_rt>
                      <ROW_evpn_import_rt>
                       <evpn-import-rt>600:600</evpn-import-rt>
                      </ROW_evpn_import_rt>
                     </TABLE_evpn_import_rt>
                     <af-label-mode>per-vrf</af-label-mode>
                     <af-rr>false</af-rr>
                     <default-information-enabled>false</default-information-enabled>
                     <nexthop-trigger-delay-critical>3000</nexthop-trigger-delay-critical>
                     <nexthop-trigger-delay-non-critical>10000</nexthop-trigger-delay-non-critical>
                    </ROW_af>
                   </TABLE_af>
                  </ROW_vrf>
                 </TABLE_vrf>
                </__readonly__>
               </__XML__OPT_Cmd_show_bgp_process_cmd___readonly__>
              </__XML__OPT_Cmd_show_bgp_process_cmd_vrf>
             </process>
            </__XML__OPT_Cmd_show_ip_bgp_session_cmd_vrf>
           </bgp>
          </show>
         </nf:data>
        </nf:rpc-reply>
        '''}

    def test_show_bgp_process_vrf_all_golden_xml(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output)
        obj = ShowBgpProcessVrfAll(device=self.device, context='xml')
        parsed_output = obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output)


class test_show_bgp_process_vrf_all_yang(unittest.TestCase):

    '''Unit test for show bgp process vrf all - YANG'''
    
    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    parsed_output = {
        'bgp_pid': 333,
        'vrf': 
            {'default': 
                {'address_family': 
                    {'ipv4 labeled unicast': 
                        {'advertise_inactive_routes': False,
                        'ebgp_max_paths': 1,
                        'enabled': True,
                        'graceful_restart': False,
                        'ibgp_max_paths': 1},
                    'ipv4 unicast': 
                        {'advertise_inactive_routes': False,
                        'ebgp_max_paths': 1,
                        'enabled': True,
                        'graceful_restart': False,
                        'ibgp_max_paths': 1},
                    'ipv6 unicast': 
                        {'advertise_inactive_routes': False,
                        'ebgp_max_paths': 1,
                        'enabled': True,
                        'graceful_restart': False,
                        'ibgp_max_paths': 1},
                    'l3vpn ipv4 unicast': 
                        {'advertise_inactive_routes': False,
                        'ebgp_max_paths': 1,
                        'enabled': True,
                        'graceful_restart': False,
                        'ibgp_max_paths': 1},
                    'l3vpn ipv6 unicast': 
                        {'advertise_inactive_routes': False,
                        'ebgp_max_paths': 1,
                        'enabled': True,
                        'graceful_restart': False,
                        'ibgp_max_paths': 1}},
                'cluster_id': '0.0.03', 
                 'router_id': '0.0.0.0'}}}

    cli_output = {'execute.return_value': '''
        BGP Process Information
        BGP Process ID                 : 29474
        BGP Protocol Started, reason:  : configuration
        BGP Protocol Tag               : 100
        BGP Performance Mode           : No
        BGP Protocol State             : Running
        BGP Isolate Mode               : No
        BGP MMODE                      : Initialized
        BGP Memory State               : OK
        BGP asformat                   : asplain
        Segment Routing Global Block   : 10000-25000

        BGP attributes information
        Number of attribute entries    : 4
        HWM of attribute entries       : 5
        Bytes used by entries          : 368
        Entries pending delete         : 0
        HWM of entries pending delete  : 0
        BGP paths per attribute HWM    : 1
        BGP AS path entries            : 0
        Bytes used by AS path entries  : 0

        Confcheck capabilities in use:
          1. CAP_FEATURE_BGP_5_2_1 (refcount = 7)

        Information regarding configured VRFs:

        BGP Information for VRF VRF1
        VRF Id                         : 3
        VRF state                      : UP
        Router-ID                      : 11.11.11.11
        Configured Router-ID           : 0.0.0.0
        Confed-ID                      : 0
        Cluster-ID                     : 0.0.0.0
        No. of configured peers        : 1
        No. of pending config peers    : 0
        No. of established peers       : 0
        VRF RD                         : 100:100

            Information for address family IPv4 Unicast in VRF VRF1
            Table Id                   : 10
            Table state                : UP
            Peers      Active-peers    Routes     Paths      Networks   Aggregates
            1          0               5          5          1          2         

            Redistribution                
                direct, route-map genie_redistribution
                static, route-map genie_redistribution
                eigrp, route-map test-map

            Export RT list: 100:100
            Import RT list: 100:100
            Label mode: per-prefix
            Aggregate label: 492287

            Information for address family IPv6 Unicast in VRF VRF1
            Table Id                   : 0x80000010
            Table state                : UP
            Peers      Active-peers    Routes     Paths      Networks   Aggregates
            0          0               4          4          1          1         

            Redistribution                
                direct, route-map genie_redistribution
                static, route-map genie_redistribution

            Export RT list: 100:100
            Import RT list: 100:100
            Label mode: per-prefix
            Aggregate label: 492288

            Nexthop trigger-delay
                critical 3000 ms
                non-critical 10000 ms

        BGP Information for VRF default
        VRF Id                         : 1
        VRF state                      : UP
        Router-ID                      : 1.1.1.1
        Configured Router-ID           : 1.1.1.1
        Confed-ID                      : 0
        Cluster-ID                     : 0.0.0.0
        No. of configured peers        : 3
        No. of pending config peers    : 0
        No. of established peers       : 1
        VRF RD                         : Not configured

            Information for address family IPv4 Unicast in VRF default
            Table Id                   : 1
            Table state                : UP
            Peers      Active-peers    Routes     Paths      Networks   Aggregates
            1          0               0          0          0          0         

            Redistribution                
                None


            Information for address family IPv6 Unicast in VRF default
            Table Id                   : 80000001
            Table state                : UP
            Peers      Active-peers    Routes     Paths      Networks   Aggregates
            0          0               0          0          0          0         

            Redistribution                
                None


            Information for address family VPNv4 Unicast in VRF default
            Table Id                   : 1
            Table state                : UP
            Peers      Active-peers    Routes     Paths      Networks   Aggregates
            1          1               5          5          0          0         

            Redistribution                
                None

            Retain RT: enabled all

            Information for address family VPNv6 Unicast in VRF default
            Table Id                   : 80000001
            Table state                : UP
            Peers      Active-peers    Routes     Paths      Networks   Aggregates
            1          1               4          4          0          0         

            Redistribution                
                None


            Information for address family IPv6 Label Unicast in VRF default
            Table Id                   : 80000001
            Table state                : UP
            Peers      Active-peers    Routes     Paths      Networks   Aggregates
            0          0               0          0          0          0         

            Redistribution                
                None
        '''}

    class etree_holder():
        def __init__(self):
            self.data = ET.fromstring('''
                <rpc-reply xmlns="urn:ietf:params:xml:ns:netconf:base:1.0" message-id="101">
                    <data>
                        <bgp xmlns="http://openconfig.net/yang/bgp">
                            <global>
                                <afi-safis>
                                    <afi-safi xmlns="http://openconfig.net/yang/bgp-multiprotocol">
                                        <afi-safi-name>none</afi-safi-name>
                                        <config>
                                            <afi-safi-name>none</afi-safi-name>
                                        </config>
                                        <graceful-restart>
                                            <state>
                                                <enabled>false</enabled>
                                            </state>
                                        </graceful-restart>
                                        <state>
                                            <afi-safi-name>none</afi-safi-name>
                                            <enabled>true</enabled>
                                        </state>
                                        <route-selection-options>
                                            <config>
                                                <advertise-inactive-routes>false</advertise-inactive-routes>
                                            </config>
                                            <state>
                                                <advertise-inactive-routes>false</advertise-inactive-routes>
                                            </state>
                                        </route-selection-options>
                                        <use-multiple-paths>
                                            <ebgp>
                                                <config>
                                                    <maximum-paths>1</maximum-paths>
                                                </config>
                                                <state>
                                                    <maximum-paths>1</maximum-paths>
                                                </state>
                                            </ebgp>
                                            <ibgp>
                                                <config>
                                                    <maximum-paths>1</maximum-paths>
                                                </config>
                                                <state>
                                                    <maximum-paths>1</maximum-paths>
                                                </state>
                                            </ibgp>
                                        </use-multiple-paths>
                                    </afi-safi>
                                    <afi-safi xmlns="http://openconfig.net/yang/bgp-multiprotocol">
                                        <afi-safi-name>none</afi-safi-name>
                                        <config>
                                            <afi-safi-name>none</afi-safi-name>
                                        </config>
                                        <graceful-restart>
                                            <state>
                                                <enabled>false</enabled>
                                            </state>
                                        </graceful-restart>
                                        <state>
                                            <afi-safi-name>none</afi-safi-name>
                                            <enabled>true</enabled>
                                        </state>
                                        <route-selection-options>
                                            <config>
                                                <advertise-inactive-routes>false</advertise-inactive-routes>
                                            </config>
                                            <state>
                                                <advertise-inactive-routes>false</advertise-inactive-routes>
                                            </state>
                                        </route-selection-options>
                                        <use-multiple-paths>
                                            <ebgp>
                                                <config>
                                                    <maximum-paths>1</maximum-paths>
                                                </config>
                                                <state>
                                                    <maximum-paths>1</maximum-paths>
                                                </state>
                                            </ebgp>
                                            <ibgp>
                                                <config>
                                                    <maximum-paths>1</maximum-paths>
                                                </config>
                                                <state>
                                                    <maximum-paths>1</maximum-paths>
                                                </state>
                                            </ibgp>
                                        </use-multiple-paths>
                                    </afi-safi>
                                    <afi-safi xmlns="http://openconfig.net/yang/bgp-multiprotocol">
                                        <afi-safi-name>L3VPN_IPV6_UNICAST</afi-safi-name>
                                        <config>
                                            <afi-safi-name>L3VPN_IPV6_UNICAST</afi-safi-name>
                                        </config>
                                        <graceful-restart>
                                            <state>
                                                <enabled>false</enabled>
                                            </state>
                                        </graceful-restart>
                                        <state>
                                            <afi-safi-name>L3VPN_IPV6_UNICAST</afi-safi-name>
                                            <enabled>true</enabled>
                                        </state>
                                        <route-selection-options>
                                            <config>
                                                <advertise-inactive-routes>false</advertise-inactive-routes>
                                            </config>
                                            <state>
                                                <advertise-inactive-routes>false</advertise-inactive-routes>
                                            </state>
                                        </route-selection-options>
                                        <use-multiple-paths>
                                            <ebgp>
                                                <config>
                                                    <maximum-paths>1</maximum-paths>
                                                </config>
                                                <state>
                                                    <maximum-paths>1</maximum-paths>
                                                </state>
                                            </ebgp>
                                            <ibgp>
                                                <config>
                                                    <maximum-paths>1</maximum-paths>
                                                </config>
                                                <state>
                                                    <maximum-paths>1</maximum-paths>
                                                </state>
                                            </ibgp>
                                        </use-multiple-paths>
                                    </afi-safi>
                                    <afi-safi xmlns="http://openconfig.net/yang/bgp-multiprotocol">
                                        <afi-safi-name>L3VPN_IPV4_UNICAST</afi-safi-name>
                                        <config>
                                            <afi-safi-name>L3VPN_IPV4_UNICAST</afi-safi-name>
                                        </config>
                                        <graceful-restart>
                                            <state>
                                                <enabled>false</enabled>
                                            </state>
                                        </graceful-restart>
                                        <state>
                                            <afi-safi-name>L3VPN_IPV4_UNICAST</afi-safi-name>
                                            <enabled>true</enabled>
                                        </state>
                                        <route-selection-options>
                                            <config>
                                                <advertise-inactive-routes>false</advertise-inactive-routes>
                                            </config>
                                            <state>
                                                <advertise-inactive-routes>false</advertise-inactive-routes>
                                            </state>
                                        </route-selection-options>
                                        <use-multiple-paths>
                                            <ebgp>
                                                <config>
                                                    <maximum-paths>1</maximum-paths>
                                                </config>
                                                <state>
                                                    <maximum-paths>1</maximum-paths>
                                                </state>
                                            </ebgp>
                                            <ibgp>
                                                <config>
                                                    <maximum-paths>1</maximum-paths>
                                                </config>
                                                <state>
                                                    <maximum-paths>1</maximum-paths>
                                                </state>
                                            </ibgp>
                                        </use-multiple-paths>
                                    </afi-safi>
                                    <afi-safi xmlns="http://openconfig.net/yang/bgp-multiprotocol">
                                        <afi-safi-name>IPV6_UNICAST</afi-safi-name>
                                        <config>
                                            <afi-safi-name>IPV6_UNICAST</afi-safi-name>
                                        </config>
                                        <graceful-restart>
                                            <state>
                                                <enabled>false</enabled>
                                            </state>
                                        </graceful-restart>
                                        <state>
                                            <afi-safi-name>IPV6_UNICAST</afi-safi-name>
                                            <enabled>true</enabled>
                                        </state>
                                        <route-selection-options>
                                            <config>
                                                <advertise-inactive-routes>false</advertise-inactive-routes>
                                            </config>
                                            <state>
                                                <advertise-inactive-routes>false</advertise-inactive-routes>
                                            </state>
                                        </route-selection-options>
                                        <use-multiple-paths>
                                            <ebgp>
                                                <config>
                                                    <maximum-paths>1</maximum-paths>
                                                </config>
                                                <state>
                                                    <maximum-paths>1</maximum-paths>
                                                </state>
                                            </ebgp>
                                            <ibgp>
                                                <config>
                                                    <maximum-paths>1</maximum-paths>
                                                </config>
                                                <state>
                                                    <maximum-paths>1</maximum-paths>
                                                </state>
                                            </ibgp>
                                        </use-multiple-paths>
                                    </afi-safi>
                                    <afi-safi xmlns="http://openconfig.net/yang/bgp-multiprotocol">
                                        <afi-safi-name>IPV4_UNICAST</afi-safi-name>
                                        <config>
                                            <afi-safi-name>IPV4_UNICAST</afi-safi-name>
                                        </config>
                                        <graceful-restart>
                                            <state>
                                                <enabled>false</enabled>
                                            </state>
                                        </graceful-restart>
                                        <state>
                                            <afi-safi-name>IPV4_UNICAST</afi-safi-name>
                                            <enabled>true</enabled>
                                        </state>
                                        <route-selection-options>
                                            <config>
                                                <advertise-inactive-routes>false</advertise-inactive-routes>
                                            </config>
                                            <state>
                                                <advertise-inactive-routes>false</advertise-inactive-routes>
                                            </state>
                                        </route-selection-options>
                                        <use-multiple-paths>
                                            <ebgp>
                                                <config>
                                                    <maximum-paths>1</maximum-paths>
                                                </config>
                                                <state>
                                                    <maximum-paths>1</maximum-paths>
                                                </state>
                                            </ebgp>
                                            <ibgp>
                                                <config>
                                                    <maximum-paths>1</maximum-paths>
                                                </config>
                                                <state>
                                                    <maximum-paths>1</maximum-paths>
                                                </state>
                                            </ibgp>
                                        </use-multiple-paths>
                                    </afi-safi>
                                    <afi-safi xmlns="http://openconfig.net/yang/bgp-multiprotocol">
                                        <afi-safi-name>none</afi-safi-name>
                                        <config>
                                            <afi-safi-name>none</afi-safi-name>
                                        </config>
                                        <graceful-restart>
                                            <state>
                                                <enabled>false</enabled>
                                            </state>
                                        </graceful-restart>
                                        <state>
                                            <afi-safi-name>none</afi-safi-name>
                                            <enabled>true</enabled>
                                        </state>
                                        <route-selection-options>
                                            <config>
                                                <advertise-inactive-routes>false</advertise-inactive-routes>
                                            </config>
                                            <state>
                                                <advertise-inactive-routes>false</advertise-inactive-routes>
                                            </state>
                                        </route-selection-options>
                                        <use-multiple-paths>
                                            <ebgp>
                                                <config>
                                                    <maximum-paths>1</maximum-paths>
                                                </config>
                                                <state>
                                                    <maximum-paths>1</maximum-paths>
                                                </state>
                                            </ebgp>
                                            <ibgp>
                                                <config>
                                                    <maximum-paths>1</maximum-paths>
                                                </config>
                                                <state>
                                                    <maximum-paths>1</maximum-paths>
                                                </state>
                                            </ibgp>
                                        </use-multiple-paths>
                                    </afi-safi>
                                    <afi-safi xmlns="http://openconfig.net/yang/bgp-multiprotocol">
                                        <afi-safi-name>IPV4_LABELED_UNICAST</afi-safi-name>
                                        <config>
                                            <afi-safi-name>IPV4_LABELED_UNICAST</afi-safi-name>
                                        </config>
                                        <graceful-restart>
                                            <state>
                                                <enabled>false</enabled>
                                            </state>
                                        </graceful-restart>
                                        <state>
                                            <afi-safi-name>IPV4_LABELED_UNICAST</afi-safi-name>
                                            <enabled>true</enabled>
                                        </state>
                                        <route-selection-options>
                                            <config>
                                                <advertise-inactive-routes>false</advertise-inactive-routes>
                                            </config>
                                            <state>
                                                <advertise-inactive-routes>false</advertise-inactive-routes>
                                            </state>
                                        </route-selection-options>
                                        <use-multiple-paths>
                                            <ebgp>
                                                <config>
                                                    <maximum-paths>1</maximum-paths>
                                                </config>
                                                <state>
                                                    <maximum-paths>1</maximum-paths>
                                                </state>
                                            </ebgp>
                                            <ibgp>
                                                <config>
                                                    <maximum-paths>1</maximum-paths>
                                                </config>
                                                <state>
                                                    <maximum-paths>1</maximum-paths>
                                                </state>
                                            </ibgp>
                                        </use-multiple-paths>
                                    </afi-safi>
                                </afi-safis>
                                <graceful-restart>
                                    <config>
                                        <enabled>false</enabled>
                                        <helper-only>false</helper-only>
                                        <restart-time>120</restart-time>
                                        <stale-routes-time>300</stale-routes-time>
                                    </config>
                                    <state>
                                        <enabled>false</enabled>
                                        <helper-only>false</helper-only>
                                        <restart-time>120</restart-time>
                                        <stale-routes-time>300</stale-routes-time>
                                    </state>
                                </graceful-restart>
                                <use-multiple-paths xmlns="http://openconfig.net/yang/bgp-multiprotocol">
                                    <ebgp>
                                        <config>
                                            <maximum-paths>1</maximum-paths>
                                        </config>
                                        <state>
                                            <maximum-paths>1</maximum-paths>
                                        </state>
                                    </ebgp>
                                    <ibgp>
                                        <config>
                                            <maximum-paths>1</maximum-paths>
                                        </config>
                                        <state>
                                            <maximum-paths>1</maximum-paths>
                                        </state>
                                    </ibgp>
                                </use-multiple-paths>
                                <config>
                                    <as>333</as>
                                    <router-id>0.0.0.0</router-id>
                                </config>
                                <state>
                                    <as>333</as>
                                    <router-id>0.0.0.0</router-id>
                                </state>
                            </global>
                            <neighbors>
                                <neighbor>
                                    <graceful-restart>
                                        <state>
                                            <enabled>false</enabled>
                                            <helper-only>false</helper-only>
                                            <restart-time>120</restart-time>
                                            <stale-routes-time>300</stale-routes-time>
                                        </state>
                                    </graceful-restart>
                                    <config>
                                        <description/>
                                        <peer-as/>
                                        <remove-private-as/>
                                        <peer-group/>
                                        <neighbor-address>4.4.4.4</neighbor-address>
                                    </config>
                                    <ebgp-multihop>
                                        <config>
                                            <multihop-ttl>0</multihop-ttl>
                                        </config>
                                        <state>
                                            <enabled>false</enabled>
                                            <multihop-ttl>0</multihop-ttl>
                                        </state>
                                    </ebgp-multihop>
                                    <logging-options>
                                        <config>
                                            <log-neighbor-state-changes>true</log-neighbor-state-changes>
                                        </config>
                                        <state>
                                            <log-neighbor-state-changes>true</log-neighbor-state-changes>
                                        </state>
                                    </logging-options>
                                    <route-reflector>
                                        <config>
                                            <route-reflector-cluster-id>3</route-reflector-cluster-id>
                                        </config>
                                        <state>
                                            <route-reflector-cluster-id>3</route-reflector-cluster-id>
                                        </state>
                                    </route-reflector>
                                    <state>
                                        <description/>
                                        <peer-as/>
                                        <remove-private-as/>
                                        <peer-group/>
                                        <neighbor-address>4.4.4.4</neighbor-address>
                                    </state>
                                    <timers>
                                        <config>
                                            <hold-time>180</hold-time>
                                            <keepalive-interval>60</keepalive-interval>
                                        </config>
                                        <state>
                                            <hold-time>180</hold-time>
                                            <keepalive-interval>60</keepalive-interval>
                                        </state>
                                    </timers>
                                    <transport>
                                        <config>
                                            <passive-mode>false</passive-mode>
                                        </config>
                                        <state>
                                            <local-address>0.0.0.0</local-address>
                                            <passive-mode>false</passive-mode>
                                            <local-port xmlns="http://openconfig.net/yang/bgp-operational">unspecified</local-port>
                                            <remote-address xmlns="http://openconfig.net/yang/bgp-operational">4.4.4.4</remote-address>
                                            <remote-port xmlns="http://openconfig.net/yang/bgp-operational">unspecified</remote-port>
                                        </state>
                                    </transport>
                                    <neighbor-address>4.4.4.4</neighbor-address>
                                </neighbor>
                                <neighbor>
                                    <afi-safis>
                                        <afi-safi xmlns="http://openconfig.net/yang/bgp-multiprotocol">
                                            <afi-safi-name>IPV6_UNICAST</afi-safi-name>
                                            <config>
                                                <afi-safi-name>IPV6_UNICAST</afi-safi-name>
                                            </config>
                                            <graceful-restart>
                                                <state>
                                                    <enabled>false</enabled>
                                                </state>
                                            </graceful-restart>
                                            <state>
                                                <afi-safi-name>IPV6_UNICAST</afi-safi-name>
                                                <enabled>true</enabled>
                                            </state>
                                        </afi-safi>
                                        <afi-safi xmlns="http://openconfig.net/yang/bgp-multiprotocol">
                                            <afi-safi-name>L3VPN_IPV6_UNICAST</afi-safi-name>
                                            <config>
                                                <afi-safi-name>L3VPN_IPV6_UNICAST</afi-safi-name>
                                            </config>
                                            <graceful-restart>
                                                <state>
                                                    <enabled>false</enabled>
                                                </state>
                                            </graceful-restart>
                                            <state>
                                                <afi-safi-name>L3VPN_IPV6_UNICAST</afi-safi-name>
                                                <enabled>true</enabled>
                                            </state>
                                        </afi-safi>
                                        <afi-safi xmlns="http://openconfig.net/yang/bgp-multiprotocol">
                                            <afi-safi-name>none</afi-safi-name>
                                            <config>
                                                <afi-safi-name>none</afi-safi-name>
                                            </config>
                                            <graceful-restart>
                                                <state>
                                                    <enabled>false</enabled>
                                                </state>
                                            </graceful-restart>
                                            <state>
                                                <afi-safi-name>none</afi-safi-name>
                                                <enabled>true</enabled>
                                            </state>
                                        </afi-safi>
                                        <afi-safi xmlns="http://openconfig.net/yang/bgp-multiprotocol">
                                            <afi-safi-name>none</afi-safi-name>
                                            <config>
                                                <afi-safi-name>none</afi-safi-name>
                                            </config>
                                            <graceful-restart>
                                                <state>
                                                    <enabled>false</enabled>
                                                </state>
                                            </graceful-restart>
                                            <state>
                                                <afi-safi-name>none</afi-safi-name>
                                                <enabled>true</enabled>
                                            </state>
                                        </afi-safi>
                                        <afi-safi xmlns="http://openconfig.net/yang/bgp-multiprotocol">
                                            <afi-safi-name>none</afi-safi-name>
                                            <config>
                                                <afi-safi-name>none</afi-safi-name>
                                            </config>
                                            <graceful-restart>
                                                <state>
                                                    <enabled>false</enabled>
                                                </state>
                                            </graceful-restart>
                                            <state>
                                                <afi-safi-name>none</afi-safi-name>
                                                <enabled>true</enabled>
                                            </state>
                                        </afi-safi>
                                        <afi-safi xmlns="http://openconfig.net/yang/bgp-multiprotocol">
                                            <afi-safi-name>IPV4_UNICAST</afi-safi-name>
                                            <config>
                                                <afi-safi-name>IPV4_UNICAST</afi-safi-name>
                                            </config>
                                            <graceful-restart>
                                                <state>
                                                    <enabled>false</enabled>
                                                </state>
                                            </graceful-restart>
                                            <state>
                                                <afi-safi-name>IPV4_UNICAST</afi-safi-name>
                                                <enabled>true</enabled>
                                            </state>
                                        </afi-safi>
                                        <afi-safi xmlns="http://openconfig.net/yang/bgp-multiprotocol">
                                            <afi-safi-name>L3VPN_IPV4_UNICAST</afi-safi-name>
                                            <config>
                                                <afi-safi-name>L3VPN_IPV4_UNICAST</afi-safi-name>
                                            </config>
                                            <graceful-restart>
                                                <state>
                                                    <enabled>false</enabled>
                                                </state>
                                            </graceful-restart>
                                            <state>
                                                <afi-safi-name>L3VPN_IPV4_UNICAST</afi-safi-name>
                                                <enabled>true</enabled>
                                            </state>
                                        </afi-safi>
                                    </afi-safis>
                                    <as-path-options>
                                        <config>
                                            <allow-own-as>0</allow-own-as>
                                        </config>
                                        <state>
                                            <allow-own-as>0</allow-own-as>
                                        </state>
                                    </as-path-options>
                                    <graceful-restart>
                                        <state>
                                            <enabled>false</enabled>
                                            <helper-only>false</helper-only>
                                            <restart-time>120</restart-time>
                                            <stale-routes-time>300</stale-routes-time>
                                        </state>
                                    </graceful-restart>
                                    <config>
                                        <description/>
                                        <peer-as>333</peer-as>
                                        <remove-private-as/>
                                        <send-community>BOTH</send-community>
                                        <peer-group/>
                                        <neighbor-address>21.0.102.1</neighbor-address>
                                    </config>
                                    <ebgp-multihop>
                                        <config>
                                            <multihop-ttl>0</multihop-ttl>
                                        </config>
                                        <state>
                                            <enabled>false</enabled>
                                            <multihop-ttl>0</multihop-ttl>
                                        </state>
                                    </ebgp-multihop>
                                    <logging-options>
                                        <config>
                                            <log-neighbor-state-changes>true</log-neighbor-state-changes>
                                        </config>
                                        <state>
                                            <log-neighbor-state-changes>true</log-neighbor-state-changes>
                                        </state>
                                    </logging-options>
                                    <route-reflector>
                                        <config>
                                            <route-reflector-client>true</route-reflector-client>
                                            <route-reflector-cluster-id>3</route-reflector-cluster-id>
                                        </config>
                                        <state>
                                            <route-reflector-client>true</route-reflector-client>
                                            <route-reflector-cluster-id>3</route-reflector-cluster-id>
                                        </state>
                                    </route-reflector>
                                    <state>
                                        <description/>
                                        <peer-as>333</peer-as>
                                        <remove-private-as/>
                                        <send-community>BOTH</send-community>
                                        <peer-group/>
                                        <neighbor-address>21.0.102.1</neighbor-address>
                                    </state>
                                    <timers>
                                        <config>
                                            <hold-time>180</hold-time>
                                            <keepalive-interval>60</keepalive-interval>
                                            <minimum-advertisement-interval>0</minimum-advertisement-interval>
                                        </config>
                                        <state>
                                            <hold-time>180</hold-time>
                                            <keepalive-interval>60</keepalive-interval>
                                            <minimum-advertisement-interval>0</minimum-advertisement-interval>
                                        </state>
                                    </timers>
                                    <transport>
                                        <config>
                                            <passive-mode>false</passive-mode>
                                        </config>
                                        <state>
                                            <local-address>0.0.0.0</local-address>
                                            <passive-mode>false</passive-mode>
                                            <local-port xmlns="http://openconfig.net/yang/bgp-operational">unspecified</local-port>
                                            <remote-address xmlns="http://openconfig.net/yang/bgp-operational">21.0.102.1</remote-address>
                                            <remote-port xmlns="http://openconfig.net/yang/bgp-operational">unspecified</remote-port>
                                        </state>
                                    </transport>
                                    <neighbor-address>21.0.102.1</neighbor-address>
                                </neighbor>
                                <neighbor>
                                    <afi-safis>
                                        <afi-safi xmlns="http://openconfig.net/yang/bgp-multiprotocol">
                                            <afi-safi-name>IPV6_UNICAST</afi-safi-name>
                                            <config>
                                                <afi-safi-name>IPV6_UNICAST</afi-safi-name>
                                            </config>
                                            <graceful-restart>
                                                <state>
                                                    <enabled>false</enabled>
                                                </state>
                                            </graceful-restart>
                                            <ipv6-unicast>
                                                <config>
                                                    <send-default-route>false</send-default-route>
                                                </config>
                                                <state>
                                                    <send-default-route>false</send-default-route>
                                                </state>
                                            </ipv6-unicast>
                                            <state>
                                                <afi-safi-name>IPV6_UNICAST</afi-safi-name>
                                                <enabled>true</enabled>
                                            </state>
                                        </afi-safi>
                                        <afi-safi xmlns="http://openconfig.net/yang/bgp-multiprotocol">
                                            <afi-safi-name>none</afi-safi-name>
                                            <config>
                                                <afi-safi-name>none</afi-safi-name>
                                            </config>
                                            <graceful-restart>
                                                <state>
                                                    <enabled>false</enabled>
                                                </state>
                                            </graceful-restart>
                                            <state>
                                                <afi-safi-name>none</afi-safi-name>
                                                <enabled>true</enabled>
                                            </state>
                                        </afi-safi>
                                        <afi-safi xmlns="http://openconfig.net/yang/bgp-multiprotocol">
                                            <afi-safi-name>none</afi-safi-name>
                                            <config>
                                                <afi-safi-name>none</afi-safi-name>
                                            </config>
                                            <graceful-restart>
                                                <state>
                                                    <enabled>false</enabled>
                                                </state>
                                            </graceful-restart>
                                            <state>
                                                <afi-safi-name>none</afi-safi-name>
                                                <enabled>true</enabled>
                                            </state>
                                        </afi-safi>
                                        <afi-safi xmlns="http://openconfig.net/yang/bgp-multiprotocol">
                                            <afi-safi-name>IPV4_UNICAST</afi-safi-name>
                                            <config>
                                                <afi-safi-name>IPV4_UNICAST</afi-safi-name>
                                            </config>
                                            <graceful-restart>
                                                <state>
                                                    <enabled>false</enabled>
                                                </state>
                                            </graceful-restart>
                                            <ipv4-unicast>
                                                <config>
                                                    <send-default-route>false</send-default-route>
                                                </config>
                                                <state>
                                                    <send-default-route>false</send-default-route>
                                                </state>
                                            </ipv4-unicast>
                                            <state>
                                                <afi-safi-name>IPV4_UNICAST</afi-safi-name>
                                                <enabled>true</enabled>
                                            </state>
                                        </afi-safi>
                                    </afi-safis>
                                    <as-path-options>
                                        <config>
                                            <allow-own-as>0</allow-own-as>
                                        </config>
                                        <state>
                                            <allow-own-as>0</allow-own-as>
                                        </state>
                                    </as-path-options>
                                    <graceful-restart>
                                        <state>
                                            <enabled>false</enabled>
                                            <helper-only>false</helper-only>
                                            <restart-time>120</restart-time>
                                            <stale-routes-time>300</stale-routes-time>
                                        </state>
                                    </graceful-restart>
                                    <config>
                                        <description/>
                                        <peer-as>888</peer-as>
                                        <remove-private-as/>
                                        <send-community>BOTH</send-community>
                                        <peer-group/>
                                        <neighbor-address>fec1::2002</neighbor-address>
                                    </config>
                                    <ebgp-multihop>
                                        <config>
                                            <multihop-ttl>0</multihop-ttl>
                                        </config>
                                        <state>
                                            <enabled>false</enabled>
                                            <multihop-ttl>0</multihop-ttl>
                                        </state>
                                    </ebgp-multihop>
                                    <logging-options>
                                        <config>
                                            <log-neighbor-state-changes>true</log-neighbor-state-changes>
                                        </config>
                                        <state>
                                            <log-neighbor-state-changes>true</log-neighbor-state-changes>
                                        </state>
                                    </logging-options>
                                    <route-reflector>
                                        <config>
                                            <route-reflector-client>false</route-reflector-client>
                                            <route-reflector-cluster-id>3</route-reflector-cluster-id>
                                        </config>
                                        <state>
                                            <route-reflector-client>false</route-reflector-client>
                                            <route-reflector-cluster-id>3</route-reflector-cluster-id>
                                        </state>
                                    </route-reflector>
                                    <state>
                                        <description/>
                                        <peer-as>888</peer-as>
                                        <remove-private-as/>
                                        <send-community>BOTH</send-community>
                                        <peer-group/>
                                        <neighbor-address>fec1::2002</neighbor-address>
                                    </state>
                                    <timers>
                                        <config>
                                            <hold-time>180</hold-time>
                                            <keepalive-interval>60</keepalive-interval>
                                            <minimum-advertisement-interval>0</minimum-advertisement-interval>
                                        </config>
                                        <state>
                                            <hold-time>180</hold-time>
                                            <keepalive-interval>60</keepalive-interval>
                                            <minimum-advertisement-interval>0</minimum-advertisement-interval>
                                        </state>
                                    </timers>
                                    <transport>
                                        <config>
                                            <passive-mode>false</passive-mode>
                                        </config>
                                        <state>
                                            <local-address>::</local-address>
                                            <passive-mode>false</passive-mode>
                                            <local-port xmlns="http://openconfig.net/yang/bgp-operational">unspecified</local-port>
                                            <remote-address xmlns="http://openconfig.net/yang/bgp-operational">fec1::2002</remote-address>
                                            <remote-port xmlns="http://openconfig.net/yang/bgp-operational">unspecified</remote-port>
                                        </state>
                                    </transport>
                                    <neighbor-address>fec1::2002</neighbor-address>
                                </neighbor>
                                <neighbor>
                                    <afi-safis>
                                        <afi-safi xmlns="http://openconfig.net/yang/bgp-multiprotocol">
                                            <afi-safi-name>IPV4_UNICAST</afi-safi-name>
                                            <config>
                                                <afi-safi-name>IPV4_UNICAST</afi-safi-name>
                                            </config>
                                            <graceful-restart>
                                                <state>
                                                    <enabled>false</enabled>
                                                </state>
                                            </graceful-restart>
                                            <ipv4-unicast>
                                                <config>
                                                    <send-default-route>false</send-default-route>
                                                </config>
                                                <state>
                                                    <send-default-route>false</send-default-route>
                                                </state>
                                            </ipv4-unicast>
                                            <state>
                                                <afi-safi-name>IPV4_UNICAST</afi-safi-name>
                                                <enabled>true</enabled>
                                            </state>
                                        </afi-safi>
                                    </afi-safis>
                                    <as-path-options>
                                        <config>
                                            <allow-own-as>0</allow-own-as>
                                        </config>
                                        <state>
                                            <allow-own-as>0</allow-own-as>
                                        </state>
                                    </as-path-options>
                                    <graceful-restart>
                                        <state>
                                            <enabled>false</enabled>
                                            <helper-only>false</helper-only>
                                            <restart-time>120</restart-time>
                                            <stale-routes-time>300</stale-routes-time>
                                        </state>
                                    </graceful-restart>
                                    <config>
                                        <description/>
                                        <peer-as>333</peer-as>
                                        <remove-private-as/>
                                        <send-community>BOTH</send-community>
                                        <peer-group/>
                                        <neighbor-address>fec1::1002</neighbor-address>
                                    </config>
                                    <ebgp-multihop>
                                        <config>
                                            <multihop-ttl>0</multihop-ttl>
                                        </config>
                                        <state>
                                            <enabled>false</enabled>
                                            <multihop-ttl>0</multihop-ttl>
                                        </state>
                                    </ebgp-multihop>
                                    <logging-options>
                                        <config>
                                            <log-neighbor-state-changes>true</log-neighbor-state-changes>
                                        </config>
                                        <state>
                                            <log-neighbor-state-changes>true</log-neighbor-state-changes>
                                        </state>
                                    </logging-options>
                                    <route-reflector>
                                        <config>
                                            <route-reflector-client>true</route-reflector-client>
                                            <route-reflector-cluster-id>3</route-reflector-cluster-id>
                                        </config>
                                        <state>
                                            <route-reflector-client>true</route-reflector-client>
                                            <route-reflector-cluster-id>3</route-reflector-cluster-id>
                                        </state>
                                    </route-reflector>
                                    <state>
                                        <description/>
                                        <peer-as>333</peer-as>
                                        <remove-private-as/>
                                        <send-community>BOTH</send-community>
                                        <peer-group/>
                                        <neighbor-address>fec1::1002</neighbor-address>
                                    </state>
                                    <timers>
                                        <config>
                                            <hold-time>180</hold-time>
                                            <keepalive-interval>60</keepalive-interval>
                                            <minimum-advertisement-interval>0</minimum-advertisement-interval>
                                        </config>
                                        <state>
                                            <hold-time>180</hold-time>
                                            <keepalive-interval>60</keepalive-interval>
                                            <minimum-advertisement-interval>0</minimum-advertisement-interval>
                                        </state>
                                    </timers>
                                    <transport>
                                        <config>
                                            <passive-mode>false</passive-mode>
                                        </config>
                                        <state>
                                            <local-address>::</local-address>
                                            <passive-mode>false</passive-mode>
                                            <local-port xmlns="http://openconfig.net/yang/bgp-operational">unspecified</local-port>
                                            <remote-address xmlns="http://openconfig.net/yang/bgp-operational">fec1::1002</remote-address>
                                            <remote-port xmlns="http://openconfig.net/yang/bgp-operational">unspecified</remote-port>
                                        </state>
                                    </transport>
                                    <neighbor-address>fec1::1002</neighbor-address>
                                </neighbor>
                                <neighbor>
                                    <afi-safis>
                                        <afi-safi xmlns="http://openconfig.net/yang/bgp-multiprotocol">
                                            <afi-safi-name>IPV6_UNICAST</afi-safi-name>
                                            <config>
                                                <afi-safi-name>IPV6_UNICAST</afi-safi-name>
                                            </config>
                                            <graceful-restart>
                                                <state>
                                                    <enabled>false</enabled>
                                                </state>
                                            </graceful-restart>
                                            <state>
                                                <afi-safi-name>IPV6_UNICAST</afi-safi-name>
                                                <enabled>true</enabled>
                                            </state>
                                        </afi-safi>
                                        <afi-safi xmlns="http://openconfig.net/yang/bgp-multiprotocol">
                                            <afi-safi-name>L3VPN_IPV6_UNICAST</afi-safi-name>
                                            <config>
                                                <afi-safi-name>L3VPN_IPV6_UNICAST</afi-safi-name>
                                            </config>
                                            <graceful-restart>
                                                <state>
                                                    <enabled>false</enabled>
                                                </state>
                                            </graceful-restart>
                                            <state>
                                                <afi-safi-name>L3VPN_IPV6_UNICAST</afi-safi-name>
                                                <enabled>true</enabled>
                                            </state>
                                        </afi-safi>
                                        <afi-safi xmlns="http://openconfig.net/yang/bgp-multiprotocol">
                                            <afi-safi-name>none</afi-safi-name>
                                            <config>
                                                <afi-safi-name>none</afi-safi-name>
                                            </config>
                                            <graceful-restart>
                                                <state>
                                                    <enabled>false</enabled>
                                                </state>
                                            </graceful-restart>
                                            <state>
                                                <afi-safi-name>none</afi-safi-name>
                                                <enabled>true</enabled>
                                            </state>
                                        </afi-safi>
                                        <afi-safi xmlns="http://openconfig.net/yang/bgp-multiprotocol">
                                            <afi-safi-name>none</afi-safi-name>
                                            <config>
                                                <afi-safi-name>none</afi-safi-name>
                                            </config>
                                            <graceful-restart>
                                                <state>
                                                    <enabled>false</enabled>
                                                </state>
                                            </graceful-restart>
                                            <state>
                                                <afi-safi-name>none</afi-safi-name>
                                                <enabled>true</enabled>
                                            </state>
                                        </afi-safi>
                                        <afi-safi xmlns="http://openconfig.net/yang/bgp-multiprotocol">
                                            <afi-safi-name>none</afi-safi-name>
                                            <config>
                                                <afi-safi-name>none</afi-safi-name>
                                            </config>
                                            <graceful-restart>
                                                <state>
                                                    <enabled>false</enabled>
                                                </state>
                                            </graceful-restart>
                                            <state>
                                                <afi-safi-name>none</afi-safi-name>
                                                <enabled>true</enabled>
                                            </state>
                                        </afi-safi>
                                        <afi-safi xmlns="http://openconfig.net/yang/bgp-multiprotocol">
                                            <afi-safi-name>IPV4_UNICAST</afi-safi-name>
                                            <config>
                                                <afi-safi-name>IPV4_UNICAST</afi-safi-name>
                                            </config>
                                            <graceful-restart>
                                                <state>
                                                    <enabled>false</enabled>
                                                </state>
                                            </graceful-restart>
                                            <ipv4-unicast>
                                                <config>
                                                    <send-default-route>false</send-default-route>
                                                </config>
                                                <state>
                                                    <send-default-route>false</send-default-route>
                                                </state>
                                            </ipv4-unicast>
                                            <state>
                                                <afi-safi-name>IPV4_UNICAST</afi-safi-name>
                                                <enabled>true</enabled>
                                            </state>
                                        </afi-safi>
                                        <afi-safi xmlns="http://openconfig.net/yang/bgp-multiprotocol">
                                            <afi-safi-name>L3VPN_IPV4_UNICAST</afi-safi-name>
                                            <config>
                                                <afi-safi-name>L3VPN_IPV4_UNICAST</afi-safi-name>
                                            </config>
                                            <graceful-restart>
                                                <state>
                                                    <enabled>false</enabled>
                                                </state>
                                            </graceful-restart>
                                            <state>
                                                <afi-safi-name>L3VPN_IPV4_UNICAST</afi-safi-name>
                                                <enabled>true</enabled>
                                            </state>
                                        </afi-safi>
                                    </afi-safis>
                                    <as-path-options>
                                        <config>
                                            <allow-own-as>0</allow-own-as>
                                        </config>
                                        <state>
                                            <allow-own-as>0</allow-own-as>
                                        </state>
                                    </as-path-options>
                                    <graceful-restart>
                                        <state>
                                            <enabled>false</enabled>
                                            <helper-only>false</helper-only>
                                            <restart-time>120</restart-time>
                                            <stale-routes-time>300</stale-routes-time>
                                        </state>
                                    </graceful-restart>
                                    <config>
                                        <description/>
                                        <peer-as>333</peer-as>
                                        <remove-private-as/>
                                        <send-community>BOTH</send-community>
                                        <peer-group/>
                                        <neighbor-address>21.0.101.1</neighbor-address>
                                    </config>
                                    <ebgp-multihop>
                                        <config>
                                            <multihop-ttl>0</multihop-ttl>
                                        </config>
                                        <state>
                                            <enabled>false</enabled>
                                            <multihop-ttl>0</multihop-ttl>
                                        </state>
                                    </ebgp-multihop>
                                    <logging-options>
                                        <config>
                                            <log-neighbor-state-changes>true</log-neighbor-state-changes>
                                        </config>
                                        <state>
                                            <log-neighbor-state-changes>true</log-neighbor-state-changes>
                                        </state>
                                    </logging-options>
                                    <route-reflector>
                                        <config>
                                            <route-reflector-client>true</route-reflector-client>
                                            <route-reflector-cluster-id>3</route-reflector-cluster-id>
                                        </config>
                                        <state>
                                            <route-reflector-client>true</route-reflector-client>
                                            <route-reflector-cluster-id>3</route-reflector-cluster-id>
                                        </state>
                                    </route-reflector>
                                    <state>
                                        <description/>
                                        <peer-as>333</peer-as>
                                        <remove-private-as/>
                                        <send-community>BOTH</send-community>
                                        <peer-group/>
                                        <neighbor-address>21.0.101.1</neighbor-address>
                                    </state>
                                    <timers>
                                        <config>
                                            <hold-time>180</hold-time>
                                            <keepalive-interval>60</keepalive-interval>
                                            <minimum-advertisement-interval>0</minimum-advertisement-interval>
                                        </config>
                                        <state>
                                            <hold-time>180</hold-time>
                                            <keepalive-interval>60</keepalive-interval>
                                            <minimum-advertisement-interval>0</minimum-advertisement-interval>
                                        </state>
                                    </timers>
                                    <transport>
                                        <config>
                                            <passive-mode>false</passive-mode>
                                        </config>
                                        <state>
                                            <local-address>0.0.0.0</local-address>
                                            <passive-mode>false</passive-mode>
                                            <local-port xmlns="http://openconfig.net/yang/bgp-operational">unspecified</local-port>
                                            <remote-address xmlns="http://openconfig.net/yang/bgp-operational">21.0.101.1</remote-address>
                                            <remote-port xmlns="http://openconfig.net/yang/bgp-operational">unspecified</remote-port>
                                        </state>
                                    </transport>
                                    <neighbor-address>21.0.101.1</neighbor-address>
                                </neighbor>
                                <neighbor>
                                    <afi-safis>
                                        <afi-safi xmlns="http://openconfig.net/yang/bgp-multiprotocol">
                                            <afi-safi-name>IPV6_UNICAST</afi-safi-name>
                                            <config>
                                                <afi-safi-name>IPV6_UNICAST</afi-safi-name>
                                            </config>
                                            <graceful-restart>
                                                <state>
                                                    <enabled>false</enabled>
                                                </state>
                                            </graceful-restart>
                                            <ipv6-unicast>
                                                <config>
                                                    <send-default-route>false</send-default-route>
                                                </config>
                                                <state>
                                                    <send-default-route>false</send-default-route>
                                                </state>
                                            </ipv6-unicast>
                                            <state>
                                                <afi-safi-name>IPV6_UNICAST</afi-safi-name>
                                                <enabled>true</enabled>
                                            </state>
                                        </afi-safi>
                                        <afi-safi xmlns="http://openconfig.net/yang/bgp-multiprotocol">
                                            <afi-safi-name>L3VPN_IPV6_UNICAST</afi-safi-name>
                                            <config>
                                                <afi-safi-name>L3VPN_IPV6_UNICAST</afi-safi-name>
                                            </config>
                                            <graceful-restart>
                                                <state>
                                                    <enabled>false</enabled>
                                                </state>
                                            </graceful-restart>
                                            <state>
                                                <afi-safi-name>L3VPN_IPV6_UNICAST</afi-safi-name>
                                                <enabled>true</enabled>
                                            </state>
                                        </afi-safi>
                                        <afi-safi xmlns="http://openconfig.net/yang/bgp-multiprotocol">
                                            <afi-safi-name>none</afi-safi-name>
                                            <config>
                                                <afi-safi-name>none</afi-safi-name>
                                            </config>
                                            <graceful-restart>
                                                <state>
                                                    <enabled>false</enabled>
                                                </state>
                                            </graceful-restart>
                                            <state>
                                                <afi-safi-name>none</afi-safi-name>
                                                <enabled>true</enabled>
                                            </state>
                                        </afi-safi>
                                        <afi-safi xmlns="http://openconfig.net/yang/bgp-multiprotocol">
                                            <afi-safi-name>none</afi-safi-name>
                                            <config>
                                                <afi-safi-name>none</afi-safi-name>
                                            </config>
                                            <graceful-restart>
                                                <state>
                                                    <enabled>false</enabled>
                                                </state>
                                            </graceful-restart>
                                            <state>
                                                <afi-safi-name>none</afi-safi-name>
                                                <enabled>true</enabled>
                                            </state>
                                        </afi-safi>
                                        <afi-safi xmlns="http://openconfig.net/yang/bgp-multiprotocol">
                                            <afi-safi-name>none</afi-safi-name>
                                            <config>
                                                <afi-safi-name>none</afi-safi-name>
                                            </config>
                                            <graceful-restart>
                                                <state>
                                                    <enabled>false</enabled>
                                                </state>
                                            </graceful-restart>
                                            <state>
                                                <afi-safi-name>none</afi-safi-name>
                                                <enabled>true</enabled>
                                            </state>
                                        </afi-safi>
                                        <afi-safi xmlns="http://openconfig.net/yang/bgp-multiprotocol">
                                            <afi-safi-name>IPV4_UNICAST</afi-safi-name>
                                            <config>
                                                <afi-safi-name>IPV4_UNICAST</afi-safi-name>
                                            </config>
                                            <graceful-restart>
                                                <state>
                                                    <enabled>false</enabled>
                                                </state>
                                            </graceful-restart>
                                            <ipv4-unicast>
                                                <config>
                                                    <send-default-route>false</send-default-route>
                                                </config>
                                                <state>
                                                    <send-default-route>false</send-default-route>
                                                </state>
                                            </ipv4-unicast>
                                            <state>
                                                <afi-safi-name>IPV4_UNICAST</afi-safi-name>
                                                <enabled>true</enabled>
                                            </state>
                                        </afi-safi>
                                        <afi-safi xmlns="http://openconfig.net/yang/bgp-multiprotocol">
                                            <afi-safi-name>L3VPN_IPV4_UNICAST</afi-safi-name>
                                            <config>
                                                <afi-safi-name>L3VPN_IPV4_UNICAST</afi-safi-name>
                                            </config>
                                            <graceful-restart>
                                                <state>
                                                    <enabled>false</enabled>
                                                </state>
                                            </graceful-restart>
                                            <state>
                                                <afi-safi-name>L3VPN_IPV4_UNICAST</afi-safi-name>
                                                <enabled>true</enabled>
                                            </state>
                                        </afi-safi>
                                    </afi-safis>
                                    <as-path-options>
                                        <config>
                                            <allow-own-as>0</allow-own-as>
                                        </config>
                                        <state>
                                            <allow-own-as>0</allow-own-as>
                                        </state>
                                    </as-path-options>
                                    <graceful-restart>
                                        <state>
                                            <enabled>false</enabled>
                                            <helper-only>false</helper-only>
                                            <restart-time>120</restart-time>
                                            <stale-routes-time>300</stale-routes-time>
                                        </state>
                                    </graceful-restart>
                                    <config>
                                        <description/>
                                        <peer-as>888</peer-as>
                                        <remove-private-as/>
                                        <send-community>BOTH</send-community>
                                        <peer-group/>
                                        <neighbor-address>21.0.201.1</neighbor-address>
                                    </config>
                                    <ebgp-multihop>
                                        <config>
                                            <multihop-ttl>0</multihop-ttl>
                                        </config>
                                        <state>
                                            <enabled>false</enabled>
                                            <multihop-ttl>0</multihop-ttl>
                                        </state>
                                    </ebgp-multihop>
                                    <logging-options>
                                        <config>
                                            <log-neighbor-state-changes>true</log-neighbor-state-changes>
                                        </config>
                                        <state>
                                            <log-neighbor-state-changes>true</log-neighbor-state-changes>
                                        </state>
                                    </logging-options>
                                    <route-reflector>
                                        <config>
                                            <route-reflector-client>false</route-reflector-client>
                                            <route-reflector-cluster-id>3</route-reflector-cluster-id>
                                        </config>
                                        <state>
                                            <route-reflector-client>false</route-reflector-client>
                                            <route-reflector-cluster-id>3</route-reflector-cluster-id>
                                        </state>
                                    </route-reflector>
                                    <state>
                                        <description/>
                                        <peer-as>888</peer-as>
                                        <remove-private-as/>
                                        <send-community>BOTH</send-community>
                                        <peer-group/>
                                        <neighbor-address>21.0.201.1</neighbor-address>
                                    </state>
                                    <timers>
                                        <config>
                                            <hold-time>180</hold-time>
                                            <keepalive-interval>60</keepalive-interval>
                                            <minimum-advertisement-interval>0</minimum-advertisement-interval>
                                        </config>
                                        <state>
                                            <hold-time>180</hold-time>
                                            <keepalive-interval>60</keepalive-interval>
                                            <minimum-advertisement-interval>0</minimum-advertisement-interval>
                                        </state>
                                    </timers>
                                    <transport>
                                        <config>
                                            <passive-mode>false</passive-mode>
                                        </config>
                                        <state>
                                            <local-address>0.0.0.0</local-address>
                                            <passive-mode>false</passive-mode>
                                            <local-port xmlns="http://openconfig.net/yang/bgp-operational">unspecified</local-port>
                                            <remote-address xmlns="http://openconfig.net/yang/bgp-operational">21.0.201.1</remote-address>
                                            <remote-port xmlns="http://openconfig.net/yang/bgp-operational">unspecified</remote-port>
                                        </state>
                                    </transport>
                                    <neighbor-address>21.0.201.1</neighbor-address>
                                </neighbor>
                            </neighbors>
                        </bgp>
                    </data>
                </rpc-reply>
            ''')

    yang_output = {'get.return_value': etree_holder()}

    # def test_show_bgp_process_vrf_all_golden_yang(self):
    #     self.maxDiff = None
    #     self.device = Mock(**self.yang_output)
    #     obj = ShowBgpProcessVrfAll(device=self.device, context='yang')
    #     try:
    #         parsed_output = obj.parse()
    #         self.assertEqual(parsed_output,self.parsed_output)
    #     except SchemaMissingKeyError:
    #         pass

# =============================================
#  Unit test for 'show bgp peer-session <WORD>'
# =============================================

class test_show_bgp_peer_session(unittest.TestCase):
    
    '''Unit test for show bgp peer-session <WORD>'''

    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output = {
        'peer_session': 
            {'PEER-SESSION': 
                {'bfd': True,
                 'description': 'PEER-SESSION',
                 'disable_connectivity_check': True,
                 'ebgp_multihop_enable': True,
                 'ebgp_multihop_limit': 255,
                 'holdtime': 111,
                 'inherited_vrf_default': '2.2.2.5',
                 'keepalive': 222,
                 'local_as': True,
                 'transport_connection_mode': 'Passive',
                 'password': True,
                 'remote_as': True,
                 'shutdown': True,
                 'suppress_capabilities': True,
                 'update_source': 'interface: '
                                 'loopback0'}}}

    golden_output = {'execute.return_value': '''
        N7k# show running-config | inc peer-session
            inherit peer-session PEER-SESSION
        template peer-session PEER-SESSION
            inherit peer-session PEER-SESSION
        
        N7k# show bgp peer-session PEER-SESSION
        Commands configured in this template:
          Shutdown
          Update Source - interface: loopback0
          Description - description: PEER-SESSION
          Password
          EBGP Multihop - hop limit: 255
          Disable Connectivity Check
          Suppress Capabilities
          Passive Only
          Timers - hold time: 111, keepalive: 222
          Remote AS
          Local AS
          Enable Bfd
        Inherited commands:
        Inherited by the following peers:
          VRF default: 2.2.2.5
        '''}

    def test_show_bgp_peer_session_golden(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output)
        obj = ShowBgpPeerSession(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output)

    def test_show_bgp_peer_session_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowBgpPeerSession(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()


# ============================================
#  Unit test for 'show bgp peer-policy <WORD>'       
# ============================================

class test_show_bgp_peer_policy(unittest.TestCase):
    
    '''Unit test for show bgp peer-policy <WORD>'''

    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output = {
        'peer_policy': {
            'PEER-POLICY': {
                'allowas_in': True,
                'as_override': True,
                'default_originate': True,
                'default_originate_route_map': 'test',
                'inherited_vrf_default': '2.2.2.5',
                'maximum_prefix_max_prefix_no': 300,
                'route_map_name_in': 'test-map',
                'route_map_name_out': 'test-map',
                'route_reflector_client': True,
                'send_community': True,
                'send_ext_community': True,
                'site_of_origin': True,
                'soft_reconfiguration': True}}}

    golden_output = {'execute.return_value': '''
        N7k# show running-config | inc peer-policy
          template peer-policy PEER-POLICY
              inherit peer-policy PEER-POLICY 10
              inherit peer-policy PEER-POLICY2 20
        
        N7k# show bgp peer-policy PEER-POLICY
        Commands configured in this template:
          Send Community
          Send Ext-community
          Route Reflector Client
          Route-map Inbound - policy-name: test-map
          Route-map Outbound - policy-name: test-map
          Maximum Prefixes - prefix limit: 300
          Default Originate - route-map: test
          Soft-Reconfig
          Site-of-origin
          Allowas-in
          AS-override
        Inherited commands:
        Inherited by the following peers:
          VRF default: 2.2.2.5
        N7k#
        '''}

    def test_show_bgp_peer_policy_golden(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output)
        obj = ShowBgpPeerPolicy(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output)

    def test_show_bgp_peer_policy_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowBgpPeerPolicy(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()


# ==============================================
#  Unit test for 'show bgp peer-template <WORD>'       
# ==============================================

class test_show_bgp_peer_template(unittest.TestCase):
    
    '''Unit test for show bgp peer-template <WORD>'''

    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output = {
        'peer_template':
            {'PEER':
                {'bfd_live_detection': True,
                'disable_connected_check': True,
                'description': 'DESC',
                'holdtime': 26,
                'inherit_template': 'PEER-SESSION',
                'keepalive_interval': 13,
                'nbr_transport_connection_mode': 'Passive',
                'num_hops_bgp_peer': 255,
                'private_as_updates': False,
                'remote_as': 500,
                'tcp_md5_auth': 'enabled',
                'update_source': 'loopback1'}}}

    golden_output = {'execute.return_value': '''
        N7k# show running-config | inc peer
          template peer PEER
            inherit peer-session PEER-SESSION
          template peer-policy PEER-POLICY
          template peer-session PEER-SESSION
          template peer-session test_tahigash
            inherit peer-session PEER-SESSION
              inherit peer-policy PEER-POLICY 10
              inherit peer-policy PEER-POLICY2 20

        N7k# show bgp peer-template PEER
        BGP peer-template is PEER
        Remote AS 500
        Inherits session configuration from session-template PEER-SESSION
        Description: DESC
        Using loopback1 as update source for this peer
        Connected check is disabled
        BFD live-detection is configured
        External BGP peer might be upto 255 hops away
        TCP MD5 authentication is enabled
        Only passive connection setup allowed
        Neighbor local-as command not active
        Private AS numbers removed from updates sent to this neighbor
        Hold time = 26, keepalive interval is 13 seconds

        Members of peer-template PEER:
        '''}

    def test_show_bgp_peer_template_golden(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output)
        obj = ShowBgpPeerTemplate(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output)

    def test_show_bgp_peer_template_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowBgpPeerTemplate(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()


# =====================================
#  Unit test for 'show bgp vrf all all'       
# =====================================

class test_show_bgp_vrf_all_all(unittest.TestCase):
    
    '''Unit test for show bgp vrf all all'''

    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output1 = {
        'vrf':
            {'VRF1':
                {'address_family':
                    {'ipv4 unicast':
                        {'aggregate_address_as_set': True,
                        'aggregate_address_ipv4_address': '11.0.0.0',
                        'aggregate_address_ipv4_mask': '8',
                        'aggregate_address_summary_only': True,
                        'bgp_table_version': 35,
                        'local_router_id': '11.11.11.11',
                        'prefixes':
                            {'11.0.0.0/8':
                                {'index':
                                    {1:
                                        {'next_hop': '0.0.0.0',
                                        'localprf': 100,
                                        'origin_codes': 'i',
                                        'path_type': 'a',
                                        'status_codes': '*>',
                                        'weight': 32768},
                                    2:
                                        {'next_hop': '4.4.4.4',
                                        'localprf': 100,
                                        'metric': 0,
                                        'origin_codes': 'e',
                                        'path_type': 'a',
                                        'status_codes': '*>',
                                        'weight': 32768},
                                    3:
                                        {'next_hop': '6.6.6.6',
                                        'localprf': 100,
                                        'metric': 0,
                                        'origin_codes': 'e',
                                        'path_type': 'a',
                                        'status_codes': '*>',
                                        'weight': 32768}}},
                                    '11.11.11.11/32':
                                        {'index':
                                            {1:
                                            {'next_hop': '0.0.0.0',
                                            'localprf': 100,
                                            'metric': 0,
                                            'origin_codes': '?',
                                            'path_type': 'r',
                                            'status_codes': '*>',
                                            'weight': 32768}}},
                            '123.0.0.0/8':
                                {'index':
                                    {1:
                                        {'next_hop': '0.0.0.0',
                                        'localprf': 100,
                                        'origin_codes': 'i',
                                        'path_type': 'a',
                                        'status_codes': ' ',
                                        'weight': 32768}}},
                            '33.33.33.33/32':
                                {'index':
                                    {1:
                                        {'next_hop': '3.3.3.3',
                                        'localprf': 100,
                                        'metric': 0,
                                        'origin_codes': '?',
                                        'path_type': 'i',
                                        'status_codes': '*>',
                                        'weight': 0}}},
                            '34.34.34.0/24':
                                {'index':
                                    {1:
                                        {'next_hop': '0.0.0.0',
                                        'localprf': 100,
                                        'origin_codes': 'i',
                                        'path_type': 'l',
                                        'status_codes': ' ',
                                        'weight': 32768}}}}},
                    'ipv6 unicast':
                        {'bgp_table_version': 28,
                        'local_router_id': '11.11.11.11',
                        'prefixes':
                            {'2000::/8':
                                {'index':
                                    {1:
                                        {'next_hop': '0::',
                                        'localprf': 100,
                                        'origin_codes': 'i',
                                        'path_type': 'a',
                                        'status_codes': '*>',
                                        'weight': 32768}}},
                            '2001:111:222::/64':
                                {'index':
                                    {1:
                                        {'next_hop': '0::',
                                        'localprf': 100,
                                        'origin_codes': 'i',
                                        'path_type': 'l',
                                        'status_codes': ' ',
                                        'weight': 32768}}},
                            '2001::11/128':
                                {'index':
                                    {1:
                                        {'next_hop': '0::',
                                        'localprf': 100,
                                        'metric': 0,
                                        'origin_codes': '?',
                                        'path_type': 'r',
                                        'status_codes': '*>',
                                        'weight': 32768}}},
                            '2001::33/128':
                                {'index':
                                    {1:
                                        {'next_hop': '::ffff:3.3.3.3',
                                        'localprf': 100,
                                        'metric': 0,
                                        'origin_codes': '?',
                                        'path_type': 'i',
                                        'status_codes': '*>',
                                        'weight': 0}}}},
                        'v6_aggregate_address_as_set': True,
                        'v6_aggregate_address_ipv6_address': '2000::/8',
                        'v6_aggregate_address_summary_only': True}}},
            'default':
                {'address_family':
                    {'vpnv4 unicast':
                        {'bgp_table_version': 48,
                        'local_router_id': '1.1.1.1'},
                    'vpnv4 unicast RD 100:100':
                        {'aggregate_address_as_set': True,
                        'aggregate_address_ipv4_address': '11.0.0.0',
                        'aggregate_address_ipv4_mask': '8',
                        'aggregate_address_summary_only': True,
                        'bgp_table_version': 48,
                        'default_vrf': 'VRF1',
                        'local_router_id': '1.1.1.1',
                        'prefixes':
                            {'11.0.0.0/8':
                                {'index':
                                    {1:
                                        {'next_hop': '0.0.0.0',
                                        'localprf': 100,
                                        'origin_codes': 'i',
                                        'path_type': 'a',
                                        'status_codes': '*>',
                                        'weight': 32768}}},
                            '11.11.11.11/32':
                                {'index':
                                    {1:
                                        {'next_hop': '0.0.0.0',
                                        'localprf': 100,
                                        'metric': 0,
                                        'origin_codes': '?',
                                        'path_type': 'r',
                                        'status_codes': '*>',
                                        'weight': 32768}}},
                            '123.0.0.0/8':
                                {'index':
                                    {1:
                                        {'next_hop': '0.0.0.0',
                                        'localprf': 100,
                                        'origin_codes': 'i',
                                        'path_type': 'a',
                                        'status_codes': ' ',
                                        'weight': 32768}}},
                            '33.33.33.33/32':
                                {'index':
                                    {1:
                                        {'next_hop': '3.3.3.3',
                                        'localprf': 100,
                                        'metric': 0,
                                        'origin_codes': '?',
                                        'path_type': 'i',
                                        'status_codes': '*>',
                                        'weight': 0}}},
                            '34.34.34.0/24':
                                {'index':
                                    {1:
                                        {'next_hop': '0.0.0.0',
                                        'localprf': 100,
                                        'origin_codes': 'i',
                                        'path_type': 'l',
                                        'status_codes': ' ',
                                        'weight': 32768}}}},
                        'route_distinguisher': '100:100'},
                    'vpnv6 unicast':
                        {'bgp_table_version': 41,
                        'local_router_id': '1.1.1.1'},
                    'vpnv6 unicast RD 100:100':
                        {'bgp_table_version': 41,
                        'default_vrf': 'VRF1',
                        'local_router_id': '1.1.1.1',
                        'prefixes':
                            {'2000::/8':
                                {'index':
                                    {1:
                                        {'next_hop': '0::',
                                        'localprf': 100,
                                        'origin_codes': 'i',
                                        'path_type': 'a',
                                        'status_codes': '*>',
                                        'weight': 32768}}},
                            '2001:111:222::/64':
                                {'index':
                                    {1:
                                        {'next_hop': '0::',
                                        'localprf': 100,
                                        'origin_codes': 'i',
                                        'path_type': 'l',
                                        'status_codes': ' ',
                                        'weight': 32768}}},
                            '2001::11/128':
                                {'index':
                                    {1:
                                        {'next_hop': '0::',
                                        'localprf': 100,
                                        'metric': 0,
                                        'origin_codes': '?',
                                        'path_type': 'r',
                                        'status_codes': '*>',
                                        'weight': 32768}}},
                            '2001::33/128':
                                {'index':
                                    {1:
                                        {'next_hop': '::ffff:3.3.3.3',
                                        'localprf': 100,
                                        'metric': 0,
                                        'origin_codes': '?',
                                        'path_type': 'i',
                                        'status_codes': '*>',
                                        'weight': 0}}}},
                        'route_distinguisher': '100:100',
                        'v6_aggregate_address_as_set': True,
                        'v6_aggregate_address_ipv6_address': '2000::/8',
                        'v6_aggregate_address_summary_only': True}}}}}

    golden_output1 = {'execute.return_value': '''
        N7k# show bgp vrf all all
        BGP routing table information for VRF VRF1, address family IPv4 Unicast
        BGP table version is 35, local router ID is 11.11.11.11
        Status: s-suppressed, x-deleted, S-stale, d-dampened, h-history, *-valid, >-best
        Path type: i-internal, e-external, c-confed, l-local, a-aggregate, r-redist
        Origin codes: i - IGP, e - EGP, ? - incomplete, | - multipath

           Network            Next Hop            Metric     LocPrf     Weight Path
        *>a11.0.0.0/8         0.0.0.0                           100      32768 i
                              4.4.4.4                  0        100      32768 e
                              6.6.6.6                  0        100      32768 e                              
        *>r11.11.11.11/32     0.0.0.0                  0        100      32768 ?
        *>i33.33.33.33/32     3.3.3.3                  0        100          0 ?
          l34.34.34.0/24      0.0.0.0                           100      32768 i
          a123.0.0.0/8        0.0.0.0                           100      32768 i

        BGP routing table information for VRF VRF1, address family IPv6 Unicast
        BGP table version is 28, local router ID is 11.11.11.11
        Status: s-suppressed, x-deleted, S-stale, d-dampened, h-history, *-valid, >-best
        Path type: i-internal, e-external, c-confed, l-local, a-aggregate, r-redist
        Origin codes: i - IGP, e - EGP, ? - incomplete, | - multipath

           Network            Next Hop            Metric     LocPrf     Weight Path
        *>a2000::/8           0::                               100      32768 i
        *>r2001::11/128       0::                      0        100      32768 ?
        *>i2001::33/128       ::ffff:3.3.3.3           0        100          0 ?
          l2001:111:222::/64  0::                               100      32768 i

        BGP routing table information for VRF default, address family VPNv4 Unicast
        BGP table version is 48, local router ID is 1.1.1.1
        Status: s-suppressed, x-deleted, S-stale, d-dampened, h-history, *-valid, >-best
        Path type: i-internal, e-external, c-confed, l-local, a-aggregate, r-redist
        Origin codes: i - IGP, e - EGP, ? - incomplete, | - multipath

           Network            Next Hop            Metric     LocPrf     Weight Path
        Route Distinguisher: 100:100     (VRF VRF1)
        *>a11.0.0.0/8         0.0.0.0                           100      32768 i
        *>r11.11.11.11/32     0.0.0.0                  0        100      32768 ?
        *>i33.33.33.33/32     3.3.3.3                  0        100          0 ?
          l34.34.34.0/24      0.0.0.0                           100      32768 i
          a123.0.0.0/8        0.0.0.0                           100      32768 i

        BGP routing table information for VRF default, address family VPNv6 Unicast
        BGP table version is 41, local router ID is 1.1.1.1
        Status: s-suppressed, x-deleted, S-stale, d-dampened, h-history, *-valid, >-best
        Path type: i-internal, e-external, c-confed, l-local, a-aggregate, r-redist
        Origin codes: i - IGP, e - EGP, ? - incomplete, | - multipath

           Network            Next Hop            Metric     LocPrf     Weight Path
        Route Distinguisher: 100:100     (VRF VRF1)
        *>a2000::/8           0::                               100      32768 i
        *>r2001::11/128       0::                      0        100      32768 ?
        *>i2001::33/128       ::ffff:3.3.3.3           0        100          0 ?
          l2001:111:222::/64  0::                               100      32768 i
        '''}

    golden_parsed_output2 = {
        'vrf':
            {'default':
                {'address_family':
                    {'l2vpn evpn':
                        {'bgp_table_version': 381,
                        'local_router_id': '1.1.1.2',
                        'prefixes':
                            {'[2]:[0]:[0]:[48]:[0000.1986.6d99]:[0]:[0.0.0.0]/216':
                                {'index':
                                    {1:
                                        {'next_hop': '1.2.1.1',
                                        'localprf': 100,
                                        'origin_codes': 'i',
                                        'path_type': 'l',
                                        'status_codes': '*>',
                                        'weight': 32768}}},
                            '[2]:[0]:[0]:[48]:[0000.1986.6d99]:[128]:[2004:ab4:123:20::44]/368':
                                {'index':
                                    {1:
                                        {'next_hop': '1.2.1.1',
                                        'localprf': 100,
                                        'origin_codes': 'i',
                                        'path_type': 'l',
                                        'status_codes': '*>',
                                        'weight': 32768}}},
                            '[2]:[0]:[0]:[48]:[0000.1986.6d99]:[32]:[100.100.20.44]/272':
                                {'index':
                                    {1:
                                        {'next_hop': '1.2.1.1',
                                        'localprf': 100,
                                        'origin_codes': 'i',
                                        'path_type': 'l',
                                        'status_codes': '*>',
                                        'weight': 32768}}}}}}}}}

    golden_output2 = {'execute.return_value': '''
        BGP routing table information for VRF default, address family L2VPN EVPN
        BGP table version is 381, Local Router ID is 1.1.1.2
        Status: s-suppressed, x-deleted, S-stale, d-dampened, h-history, *-valid, >-best
        Path type: i-internal, e-external, c-confed, l-local, a-aggregate, r-redist, I-injected
        Origin codes: i - IGP, e - EGP, ? - incomplete, | - multipath, & - backup

           Network            Next Hop            Metric     LocPrf     Weight Path
        Route Distinguisher: 1.1.1.2:32868    (L2VNI 5020)
        *>l[2]:[0]:[0]:[48]:[0000.1986.6d99]:[0]:[0.0.0.0]/216
                              1.2.1.1                           100      32768 i
        *>l[2]:[0]:[0]:[48]:[0000.1986.6d99]:[32]:[100.100.20.44]/272
                              1.2.1.1                           100      32768 i
        *>l[2]:[0]:[0]:[48]:[0000.1986.6d99]:[128]:[2004:ab4:123:20::44]/368
                              1.2.1.1                           100      32768 i
        '''}

    golden_parsed_output3 = {
        'vrf':
            {'default':
                {'address_family':
                    {'ipv4 label unicast':
                        {'bgp_table_version': 28,
                        'local_router_id': '21.0.101.1',
                        'prefixes':
                            {'1.1.1.0/24':
                                {'index':
                                    {1:
                                        {'next_hop': '0.0.0.0',
                                        'localprf': 100,
                                        'origin_codes': 'i',
                                        'path_type': 'l',
                                        'status_codes': '*>',
                                        'weight': 32768}}},
                            '1.3.1.0/24':
                                {'index':
                                    {1:
                                        {'next_hop': '0.0.0.0',
                                        'localprf': 100,
                                        'metric': 4444,
                                        'origin_codes': '?',
                                        'path_type': 'r',
                                        'status_codes': '*>',
                                        'weight': 32768}}},
                            '1.3.2.0/24':
                                {'index':
                                    {1:
                                        {'next_hop': '0.0.0.0',
                                        'localprf': 100,
                                        'metric': 4444,
                                        'origin_codes': '?',
                                        'path_type': 'r',
                                        'status_codes': '*>',
                                        'weight': 32768}}},
                            '104.0.0.0/8':
                                {'index':
                                    {3:
                                        {'next_hop': '0.0.0.0',
                                        'localprf': 100,
                                        'metric': 4444,
                                        'origin_codes': '?',
                                        'path_type': 'r',
                                        'status_codes': '*>',
                                        'weight': 32768},
                                    2:
                                        {'next_hop': '21.0.0.2',
                                        'localprf': 100,
                                        'metric': 0,
                                        'origin_codes': '?',
                                        'path_type': 'i',
                                        'status_codes': '* ',
                                        'weight': 0},
                                    1:
                                        {'next_hop': 'fec1::112',
                                        'localprf': 100,
                                        'metric': 0,
                                        'origin_codes': '?',
                                        'path_type': 'i',
                                        'status_codes': '* ',
                                        'weight': 0}}},
                            '204.0.0.0/8':
                                {'index':
                                    {3:
                                        {'next_hop': '0.0.0.0',
                                        'localprf': 100,
                                        'metric': 4444,
                                        'origin_codes': '?',
                                        'path_type': 'r',
                                        'status_codes': '*>',
                                        'weight': 32768},
                                    2:
                                        {'next_hop': '21.0.0.2',
                                        'localprf': 100,
                                        'metric': 0,
                                        'origin_codes': '?',
                                        'path_type': 'i',
                                        'status_codes': '* ',
                                        'weight': 0},
                                    1:
                                        {'next_hop': 'fec1::112',
                                        'localprf': 100,
                                        'metric': 0,
                                        'origin_codes': '?',
                                        'path_type': 'i',
                                        'status_codes': '* ',
                                        'weight': 0}}},
                            '4.0.0.0/8':
                                {'index':
                                    {2:
                                        {'next_hop': '21.0.0.2',
                                        'localprf': 100,
                                        'metric': 0,
                                        'origin_codes': '?',
                                        'path_type': 'i',
                                        'status_codes': '*>',
                                        'weight': 0},
                                    1:
                                        {'next_hop': 'fec1::112',
                                        'localprf': 100,
                                        'metric': 0,
                                        'origin_codes': '?',
                                        'path_type': 'i',
                                        'status_codes': '* ',
                                        'weight': 0}}}}},
                    'ipv4 multicast':
                        {'bgp_table_version': 19,
                        'local_router_id': '21.0.101.1',
                        'prefixes':
                            {'1.1.1.0/24':
                                {'index':
                                    {1:
                                        {'next_hop': '0.0.0.0',
                                        'localprf': 100,
                                        'metric': 3333,
                                        'origin_codes': '?',
                                        'path_type': 'r',
                                        'status_codes': '*>',
                                        'weight': 32768}}},
                            '1.2.1.0/24':
                                {'index':
                                    {1:
                                        {'next_hop': '0.0.0.0',
                                        'localprf': 100,
                                        'metric': 3333,
                                        'origin_codes': '?',
                                        'path_type': 'r',
                                        'status_codes': '*>',
                                        'weight': 32768}}},
                            '102.0.0.0/8':
                                {'index':
                                    {1:
                                        {'next_hop': '0.0.0.0',
                                        'localprf': 100,
                                        'metric': 3333,
                                        'origin_codes': '?',
                                        'path_type': 'r',
                                        'status_codes': '*>',
                                        'weight': 32768}}},
                            '104.0.0.0/8':
                                {'index':
                                    {1:
                                        {'next_hop': '21.0.0.2',
                                        'localprf': 100,
                                        'metric': 0,
                                        'origin_codes': '?',
                                        'path_type': 'i',
                                        'status_codes': '*>',
                                        'weight': 0}}},
                            '2.0.0.0/8':
                                {'index':
                                    {1:
                                        {'next_hop': '0.0.0.0',
                                        'localprf': 100,
                                        'metric': 3333,
                                        'origin_codes': '?',
                                        'path_type': 'r',
                                        'status_codes': '*>',
                                        'weight': 32768}}},
                            '202.0.0.0/8':
                                {'index':
                                    {1:
                                        {'next_hop': '0.0.0.0',
                                        'localprf': 100,
                                        'metric': 3333,
                                        'origin_codes': '?',
                                        'path_type': 'r',
                                        'status_codes': '*>',
                                        'weight': 32768}}},
                            '204.0.0.0/8':
                                {'index':
                                    {1:
                                        {'next_hop': '21.0.0.2',
                                        'localprf': 100,
                                        'metric': 0,
                                        'origin_codes': '?',
                                        'path_type': 'i',
                                        'status_codes': '*>',
                                        'weight': 0}}},
                            '4.0.0.0/8':
                                {'index':
                                    {1:
                                        {'next_hop': '21.0.0.2',
                                        'localprf': 100,
                                        'metric': 0,
                                        'origin_codes': '?',
                                        'path_type': 'i',
                                        'status_codes': '*>',
                                        'weight': 0}}}}},
                    'ipv4 unicast':
                        {'bgp_table_version': 25,
                        'local_router_id': '21.0.101.1',
                        'prefixes':
                            {'1.1.1.0/24':
                                {'index':
                                    {1:
                                        {'next_hop': '0.0.0.0',
                                        'localprf': 100,
                                        'origin_codes': 'i',
                                        'path_type': 'l',
                                        'status_codes': '*>',
                                        'weight': 32768},
                                    2:
                                        {'next_hop': '0.0.0.0',
                                        'localprf': 100,
                                        'origin_codes': 'i',
                                        'path_type': 'i',
                                        'status_codes': '* ',
                                        'weight': 32768}}},
                            '1.3.1.0/24':
                                {'index':
                                    {1:
                                        {'next_hop': '0.0.0.0',
                                        'localprf': 100,
                                        'metric': 4444,
                                        'origin_codes': '?',
                                        'path_type': 'r',
                                        'status_codes': '*>',
                                        'weight': 32768}}},
                            '1.3.2.0/24':
                                {'index':
                                    {1:
                                        {'next_hop': '0.0.0.0',
                                        'localprf': 100,
                                        'metric': 4444,
                                        'origin_codes': '?',
                                        'path_type': 'r',
                                        'status_codes': '*>',
                                        'weight': 32768}}},
                            '104.0.0.0/8':
                                {'index':
                                    {3:
                                        {'next_hop': '0.0.0.0',
                                        'localprf': 100,
                                        'metric': 4444,
                                        'origin_codes': '?',
                                        'path_type': 'r',
                                        'status_codes': '*>',
                                        'weight': 32768},
                                    2:
                                        {'next_hop': '21.0.0.2',
                                        'localprf': 100,
                                        'metric': 0,
                                        'origin_codes': '?',
                                        'path_type': 'i',
                                        'status_codes': '* ',
                                        'weight': 0},
                                    1:
                                        {'next_hop': 'fec1::112',
                                        'localprf': 100,
                                        'metric': 0,
                                        'origin_codes': '?',
                                        'path_type': 'i',
                                        'status_codes': '* ',
                                        'weight': 0}}},
                            '204.0.0.0/8':
                                {'index':
                                    {3:
                                        {'next_hop': '0.0.0.0',
                                        'localprf': 100,
                                        'metric': 4444,
                                        'origin_codes': '?',
                                        'path_type': 'r',
                                        'status_codes': '*>',
                                        'weight': 32768},
                                    2:
                                        {'next_hop': '21.0.0.2',
                                        'localprf': 100,
                                        'metric': 0,
                                        'origin_codes': '?',
                                        'path_type': 'i',
                                        'status_codes': '* ',
                                        'weight': 0},
                                    1:
                                        {'next_hop': 'fec1::112',
                                        'localprf': 100,
                                        'metric': 0,
                                        'origin_codes': '?',
                                        'path_type': 'i',
                                        'status_codes': '* ',
                                        'weight': 0}}},
                            '4.0.0.0/8':
                                {'index':
                                    {2:
                                        {'next_hop': '21.0.0.2',
                                        'localprf': 100,
                                        'metric': 0,
                                        'origin_codes': '?',
                                        'path_type': 'i',
                                        'status_codes': '*>',
                                        'weight': 0},
                                    1:
                                        {'next_hop': 'fec1::112',
                                        'localprf': 100,
                                        'metric': 0,
                                        'origin_codes': '?',
                                        'path_type': 'i',
                                        'status_codes': '* ',
                                        'weight': 0}}}}},
                    'ipv6 unicast':
                        {'bgp_table_version': 7,
                        'local_router_id': '21.0.101.1',
                        'prefixes':
                            {'2001:11::1/128':
                                {'index':
                                    {1:
                                        {'next_hop': '0::',
                                        'localprf': 100,
                                        'metric': 0,
                                        'origin_codes': '?',
                                        'path_type': 'r',
                                        'status_codes': '*>',
                                        'weight': 32768}}}}},
                    'vpnv4 unicast':
                        {'bgp_table_version': 23,
                        'local_router_id': '21.0.101.1'},
                    'vpnv4 unicast RD 1:100':
                        {'bgp_table_version': 23,
                        'default_vrf': 'vpn1',
                        'local_router_id': '21.0.101.1',
                        'prefixes':
                            {'1.1.1.0/24':
                                {'index':
                                    {1:
                                        {'next_hop': '0.0.0.0',
                                        'localprf': 100,
                                        'origin_codes': 'i',
                                        'path_type': 'l',
                                        'status_codes': '*>',
                                        'weight': 32768}}},
                            '1.3.1.0/24':
                                {'index':
                                    {1:
                                        {'next_hop': '0.0.0.0',
                                        'localprf': 100,
                                        'metric': 4444,
                                        'origin_codes': '?',
                                        'path_type': 'r',
                                        'status_codes': '*>',
                                        'weight': 32768}}},
                            '1.3.2.0/24':
                                {'index':
                                    {1:
                                        {'next_hop': '0.0.0.0',
                                        'localprf': 100,
                                        'metric': 4444,
                                        'origin_codes': '?',
                                        'path_type': 'r',
                                        'status_codes': '*>',
                                        'weight': 32768}}},
                            '104.0.0.0/8':
                                {'index':
                                    {1:
                                        {'next_hop': '0.0.0.0',
                                        'localprf': 100,
                                        'metric': 4444,
                                        'origin_codes': '?',
                                        'path_type': 'r',
                                        'status_codes': '*>',
                                        'weight': 32768}}},
                            '204.0.0.0/8':
                                {'index':
                                    {1:
                                        {'next_hop': '0.0.0.0',
                                        'localprf': 100,
                                        'metric': 4444,
                                        'origin_codes': '?',
                                        'path_type': 'r',
                                        'status_codes': '*>',
                                        'weight': 32768}}},
                            '4.0.0.0/8':
                                {'index':
                                    {1:
                                        {'next_hop': '21.0.0.2',
                                        'localprf': 100,
                                        'metric': 0,
                                        'origin_codes': '?',
                                        'path_type': 'i',
                                        'status_codes': '*>',
                                        'weight': 0}}}},
                        'route_distinguisher': '1:100'},
                    'vpnv4 unicast RD 2:100':
                        {'bgp_table_version': 23,
                        'default_vrf': 'vpn2',
                        'local_router_id': '21.0.101.1',
                        'prefixes':
                            {'1.3.1.0/24':
                                {'index':
                                    {1:
                                        {'next_hop': '0.0.0.0',
                                        'localprf': 100,
                                        'metric': 4444,
                                        'origin_codes': '?',
                                        'path_type': 'r',
                                        'status_codes': '*>',
                                        'weight': 32768}}},
                            '1.3.2.0/24':
                                {'index':
                                    {1:
                                        {'next_hop': '0.0.0.0',
                                        'localprf': 100,
                                        'metric': 4444,
                                        'origin_codes': '?',
                                        'path_type': 'r',
                                        'status_codes': '*>',
                                        'weight': 32768}}},
                            '104.0.0.0/8':
                                {'index':
                                    {1:
                                        {'next_hop': '0.0.0.0',
                                        'localprf': 100,
                                        'metric': 4444,
                                        'origin_codes': '?',
                                        'path_type': 'r',
                                        'status_codes': '*>',
                                        'weight': 32768}}},
                            '204.0.0.0/8':
                                {'index':
                                    {1:
                                        {'next_hop': '0.0.0.0',
                                        'localprf': 100,
                                        'metric': 4444,
                                        'origin_codes': '?',
                                        'path_type': 'r',
                                        'status_codes': '*>',
                                        'weight': 32768}}}},
                        'route_distinguisher': '2:100'},                        
                    'vpnv6 unicast':
                        {'bgp_table_version': 7,
                        'local_router_id': '21.0.101.1'},
                    'vpnv6 unicast RD 2:100':
                        {'bgp_table_version': 7,
                        'default_vrf': 'vpn2',
                        'local_router_id': '21.0.101.1',
                        'prefixes':
                            {'2001:11::1/128':
                                {'index':
                                    {1:
                                        {'next_hop': '0::',
                                        'localprf': 100,
                                        'metric': 0,
                                        'origin_codes': '?',
                                        'path_type': 'r',
                                        'status_codes': '*>',
                                        'weight': 32768}}}},
                        'route_distinguisher': '2:100'},
                    'vpnv6 unicast RD 1:100':
                        {'bgp_table_version': 7,
                        'default_vrf': 'vpn1',
                        'local_router_id': '21.0.101.1',
                        'prefixes':
                            {'2001:11::1/128':
                                {'index':
                                    {1:
                                        {'next_hop': '0::',
                                        'localprf': 100,
                                        'metric': 0,
                                        'origin_codes': '?',
                                        'path_type': 'r',
                                        'status_codes': '*>',
                                        'weight': 32768}}}},
                        'route_distinguisher': '1:100'},
                    }},
            'vpn1':
                {'address_family':
                    {'ipv4 multicast':
                        {'bgp_table_version': 6,
                        'local_router_id': '11.11.11.11',
                        'prefixes':
                            {'1.3.1.0/24':
                                {'index':
                                    {1:
                                        {'next_hop': '0.0.0.0',
                                        'localprf': 100,
                                        'metric': 0,
                                        'origin_codes': '?',
                                        'path_type': 'r',
                                        'status_codes': '*>',
                                        'weight': 32768}}},
                            '1.3.2.0/24':
                                {'index':
                                    {1:
                                        {'next_hop': '0.0.0.0',
                                        'localprf': 100,
                                        'metric': 0,
                                        'origin_codes': '?',
                                        'path_type': 'r',
                                        'status_codes': '*>',
                                        'weight': 32768}}},
                            '104.0.0.0/8':
                                {'index':
                                    {1:
                                        {'next_hop': '0.0.0.0',
                                        'localprf': 100,
                                        'metric': 0,
                                        'origin_codes': '?',
                                        'path_type': 'r',
                                        'status_codes': '*>',
                                        'weight': 32768}}},
                            '204.0.0.0/8':
                                {'index':
                                    {1:
                                        {'next_hop': '0.0.0.0',
                                        'localprf': 100,
                                        'metric': 0,
                                        'origin_codes': '?',
                                        'path_type': 'r',
                                        'status_codes': '*>',
                                        'weight': 32768}}}}},
                    'ipv4 unicast':
                        {'bgp_table_version': 19,
                        'local_router_id': '11.11.11.11',
                        'prefixes':
                            {'1.1.1.0/24':
                                {'index':
                                    {1:
                                        {'next_hop': '0.0.0.0',
                                        'localprf': 100,
                                        'origin_codes': 'i',
                                        'path_type': 'l',
                                        'status_codes': '*>',
                                        'weight': 32768}}},
                            '1.3.1.0/24':
                                {'index':
                                    {1:
                                        {'next_hop': '0.0.0.0',
                                        'localprf': 100,
                                        'metric': 4444,
                                        'origin_codes': '?',
                                        'path_type': 'r',
                                        'status_codes': '*>',
                                        'weight': 32768}}},
                            '1.3.2.0/24':
                                {'index':
                                    {1:
                                        {'next_hop': '0.0.0.0',
                                        'localprf': 100,
                                        'metric': 4444,
                                        'origin_codes': '?',
                                        'path_type': 'r',
                                        'status_codes': '*>',
                                        'weight': 32768}}},
                            '104.0.0.0/8':
                                {'index':
                                    {1:
                                        {'next_hop': '0.0.0.0',
                                        'localprf': 100,
                                        'metric': 4444,
                                        'origin_codes': '?',
                                        'path_type': 'r',
                                        'status_codes': '*>',
                                        'weight': 32768}}},
                            '204.0.0.0/8':
                                {'index':
                                    {1:
                                        {'next_hop': '0.0.0.0',
                                        'localprf': 100,
                                        'metric': 4444,
                                        'origin_codes': '?',
                                        'path_type': 'r',
                                        'status_codes': '*>',
                                        'weight': 32768}}},
                            '4.0.0.0/8':
                                {'index':
                                    {1:
                                        {'next_hop': '21.0.0.2',
                                        'localprf': 100,
                                        'metric': 0,
                                        'origin_codes': '?',
                                        'path_type': 'i',
                                        'status_codes': '*>',
                                        'weight': 0}}}}},
                    'ipv6 unicast':
                        {'bgp_table_version': 6,
                        'local_router_id': '11.11.11.11',
                        'prefixes':
                            {'2001:11::1/128':
                                {'index':
                                    {1:
                                        {'next_hop': '0::',
                                        'localprf': 100,
                                        'metric': 0,
                                        'origin_codes': '?',
                                        'path_type': 'r',
                                        'status_codes': '*>',
                                        'weight': 32768}}}}}}},
            'vpn2':
                {'address_family':
                    {'ipv4 unicast':
                        {'bgp_table_version': 6,
                        'local_router_id': '22.22.22.22',
                        'prefixes':
                            {'1.3.1.0/24':
                                {'index':
                                    {1:
                                        {'next_hop': '0.0.0.0',
                                        'localprf': 100,
                                        'metric': 4444,
                                        'origin_codes': '?',
                                        'path_type': 'r',
                                        'status_codes': '*>',
                                        'weight': 32768}}},
                            '1.3.2.0/24':
                                {'index':
                                    {1:
                                        {'next_hop': '0.0.0.0',
                                        'localprf': 100,
                                        'metric': 4444,
                                        'origin_codes': '?',
                                        'path_type': 'r',
                                        'status_codes': '*>',
                                        'weight': 32768}}},
                            '104.0.0.0/8':
                                {'index':
                                    {1:
                                        {'next_hop': '0.0.0.0',
                                        'localprf': 100,
                                        'metric': 4444,
                                        'origin_codes': '?',
                                        'path_type': 'r',
                                        'status_codes': '*>',
                                        'weight': 32768}}},
                            '204.0.0.0/8':
                                {'index':
                                    {1:
                                        {'next_hop': '0.0.0.0',
                                        'localprf': 100,
                                        'metric': 4444,
                                        'origin_codes': '?',
                                        'path_type': 'r',
                                        'status_codes': '*>',
                                        'weight': 32768}}}}},
                    'ipv6 unicast':
                        {'bgp_table_version': 3,
                        'local_router_id': '22.22.22.22',
                        'prefixes':
                            {'2001:11::1/128':
                                {'index':
                                    {1:
                                        {'next_hop': '0::',
                                        'localprf': 100,
                                        'metric': 0,
                                        'origin_codes': '?',
                                        'path_type': 'r',
                                        'status_codes': '*>',
                                        'weight': 32768}}}}}}}}}

    golden_output3 = {'execute.return_value': '''
        BGP routing table information for VRF default, address family IPv4 Unicast
        BGP table version is 25, Local Router ID is 21.0.101.1
        Status: s-suppressed, x-deleted, S-stale, d-dampened, h-history, *-valid, >-best
        Path type: i-internal, e-external, c-confed, l-local, a-aggregate, r-redist, I-injected
        Origin codes: i - IGP, e - EGP, ? - incomplete, | - multipath, & - backup

           Network            Next Hop            Metric     LocPrf     Weight Path
        *>l1.1.1.0/24         0.0.0.0                           100      32768 i
        * i                   0.0.0.0                           100      32768 i
        *>r1.3.1.0/24         0.0.0.0               4444        100      32768 ?
        *>r1.3.2.0/24         0.0.0.0               4444        100      32768 ?
        * i4.0.0.0/8          fec1::112                0        100          0 ?
        *>i                   21.0.0.2                 0        100          0 ?
        * i104.0.0.0/8        fec1::112                0        100          0 ?
        * i                   21.0.0.2                 0        100          0 ?
        *>r                   0.0.0.0               4444        100      32768 ?
        * i204.0.0.0/8        fec1::112                0        100          0 ?
        * i                   21.0.0.2                 0        100          0 ?
        *>r                   0.0.0.0               4444        100      32768 ?

        BGP routing table information for VRF default, address family IPv4 Multicast
        BGP table version is 19, Local Router ID is 21.0.101.1
        Status: s-suppressed, x-deleted, S-stale, d-dampened, h-history, *-valid, >-best
        Path type: i-internal, e-external, c-confed, l-local, a-aggregate, r-redist, I-injected
        Origin codes: i - IGP, e - EGP, ? - incomplete, | - multipath, & - backup

           Network            Next Hop            Metric     LocPrf     Weight Path
        *>r1.1.1.0/24         0.0.0.0               3333        100      32768 ?
        *>r1.2.1.0/24         0.0.0.0               3333        100      32768 ?
        *>r2.0.0.0/8          0.0.0.0               3333        100      32768 ?
        *>i4.0.0.0/8          21.0.0.2                 0        100          0 ?
        *>r102.0.0.0/8        0.0.0.0               3333        100      32768 ?
        *>i104.0.0.0/8        21.0.0.2                 0        100          0 ?
        *>r202.0.0.0/8        0.0.0.0               3333        100      32768 ?
        *>i204.0.0.0/8        21.0.0.2                 0        100          0 ?

        BGP routing table information for VRF default, address family IPv6 Unicast
        BGP table version is 7, Local Router ID is 21.0.101.1
        Status: s-suppressed, x-deleted, S-stale, d-dampened, h-history, *-valid, >-best
        Path type: i-internal, e-external, c-confed, l-local, a-aggregate, r-redist, I-injected
        Origin codes: i - IGP, e - EGP, ? - incomplete, | - multipath, & - backup

           Network            Next Hop            Metric     LocPrf     Weight Path
        *>r2001:11::1/128     0::                      0        100      32768 ?

        BGP routing table information for VRF default, address family VPNv4 Unicast
        BGP table version is 23, Local Router ID is 21.0.101.1
        Status: s-suppressed, x-deleted, S-stale, d-dampened, h-history, *-valid, >-best
        Path type: i-internal, e-external, c-confed, l-local, a-aggregate, r-redist, I-injected
        Origin codes: i - IGP, e - EGP, ? - incomplete, | - multipath, & - backup

           Network            Next Hop            Metric     LocPrf     Weight Path
        Route Distinguisher: 1:100    (VRF vpn1)
        *>l1.1.1.0/24         0.0.0.0                           100      32768 i
        *>r1.3.1.0/24         0.0.0.0               4444        100      32768 ?
        *>r1.3.2.0/24         0.0.0.0               4444        100      32768 ?
        *>i4.0.0.0/8          21.0.0.2                 0        100          0 ?
        *>r104.0.0.0/8        0.0.0.0               4444        100      32768 ?
        *>r204.0.0.0/8        0.0.0.0               4444        100      32768 ?

        Route Distinguisher: 2:100    (VRF vpn2)
        *>r1.3.1.0/24         0.0.0.0               4444        100      32768 ?
        *>r1.3.2.0/24         0.0.0.0               4444        100      32768 ?
        *>r104.0.0.0/8        0.0.0.0               4444        100      32768 ?
        *>r204.0.0.0/8        0.0.0.0               4444        100      32768 ?

        BGP routing table information for VRF default, address family VPNv6 Unicast
        BGP table version is 7, Local Router ID is 21.0.101.1
        Status: s-suppressed, x-deleted, S-stale, d-dampened, h-history, *-valid, >-best
        Path type: i-internal, e-external, c-confed, l-local, a-aggregate, r-redist, I-injected
        Origin codes: i - IGP, e - EGP, ? - incomplete, | - multipath, & - backup

           Network            Next Hop            Metric     LocPrf     Weight Path
        Route Distinguisher: 1:100    (VRF vpn1)
        *>r2001:11::1/128     0::                      0        100      32768 ?

        Route Distinguisher: 2:100    (VRF vpn2)
        *>r2001:11::1/128     0::                      0        100      32768 ?

        BGP routing table information for VRF default, address family IPv4 Label Unicast
        BGP table version is 28, Local Router ID is 21.0.101.1
        Status: s-suppressed, x-deleted, S-stale, d-dampened, h-history, *-valid, >-best
        Path type: i-internal, e-external, c-confed, l-local, a-aggregate, r-redist, I-injected
        Origin codes: i - IGP, e - EGP, ? - incomplete, | - multipath, & - backup

           Network            Next Hop            Metric     LocPrf     Weight Path
        *>l1.1.1.0/24         0.0.0.0                           100      32768 i
        *>r1.3.1.0/24         0.0.0.0               4444        100      32768 ?
        *>r1.3.2.0/24         0.0.0.0               4444        100      32768 ?
        * i4.0.0.0/8          fec1::112                0        100          0 ?
        *>i                   21.0.0.2                 0        100          0 ?
        * i104.0.0.0/8        fec1::112                0        100          0 ?
        * i                   21.0.0.2                 0        100          0 ?
        *>r                   0.0.0.0               4444        100      32768 ?
        * i204.0.0.0/8        fec1::112                0        100          0 ?
        * i                   21.0.0.2                 0        100          0 ?
        *>r                   0.0.0.0               4444        100      32768 ?

        BGP routing table information for VRF vpn1, address family IPv4 Unicast
        BGP table version is 19, Local Router ID is 11.11.11.11
        Status: s-suppressed, x-deleted, S-stale, d-dampened, h-history, *-valid, >-best
        Path type: i-internal, e-external, c-confed, l-local, a-aggregate, r-redist, I-injected
        Origin codes: i - IGP, e - EGP, ? - incomplete, | - multipath, & - backup

           Network            Next Hop            Metric     LocPrf     Weight Path
        *>l1.1.1.0/24         0.0.0.0                           100      32768 i
        *>r1.3.1.0/24         0.0.0.0               4444        100      32768 ?
        *>r1.3.2.0/24         0.0.0.0               4444        100      32768 ?
        *>i4.0.0.0/8          21.0.0.2                 0        100          0 ?
        *>r104.0.0.0/8        0.0.0.0               4444        100      32768 ?
        *>r204.0.0.0/8        0.0.0.0               4444        100      32768 ?

        BGP routing table information for VRF vpn1, address family IPv4 Multicast
        BGP table version is 6, Local Router ID is 11.11.11.11
        Status: s-suppressed, x-deleted, S-stale, d-dampened, h-history, *-valid, >-best
        Path type: i-internal, e-external, c-confed, l-local, a-aggregate, r-redist, I-injected
        Origin codes: i - IGP, e - EGP, ? - incomplete, | - multipath, & - backup

           Network            Next Hop            Metric     LocPrf     Weight Path
        *>r1.3.1.0/24         0.0.0.0                  0        100      32768 ?
        *>r1.3.2.0/24         0.0.0.0                  0        100      32768 ?
        *>r104.0.0.0/8        0.0.0.0                  0        100      32768 ?
        *>r204.0.0.0/8        0.0.0.0                  0        100      32768 ?

        BGP routing table information for VRF vpn1, address family IPv6 Unicast
        BGP table version is 6, Local Router ID is 11.11.11.11
        Status: s-suppressed, x-deleted, S-stale, d-dampened, h-history, *-valid, >-best
        Path type: i-internal, e-external, c-confed, l-local, a-aggregate, r-redist, I-injected
        Origin codes: i - IGP, e - EGP, ? - incomplete, | - multipath, & - backup

           Network            Next Hop            Metric     LocPrf     Weight Path
        *>r2001:11::1/128     0::                      0        100      32768 ?

        BGP routing table information for VRF vpn2, address family IPv4 Unicast
        BGP table version is 6, Local Router ID is 22.22.22.22
        Status: s-suppressed, x-deleted, S-stale, d-dampened, h-history, *-valid, >-best
        Path type: i-internal, e-external, c-confed, l-local, a-aggregate, r-redist, I-injected
        Origin codes: i - IGP, e - EGP, ? - incomplete, | - multipath, & - backup

           Network            Next Hop            Metric     LocPrf     Weight Path
        *>r1.3.1.0/24         0.0.0.0               4444        100      32768 ?
        *>r1.3.2.0/24         0.0.0.0               4444        100      32768 ?
        *>r104.0.0.0/8        0.0.0.0               4444        100      32768 ?
        *>r204.0.0.0/8        0.0.0.0               4444        100      32768 ?

        BGP routing table information for VRF vpn2, address family IPv6 Unicast
        BGP table version is 3, Local Router ID is 22.22.22.22
        Status: s-suppressed, x-deleted, S-stale, d-dampened, h-history, *-valid, >-best
        Path type: i-internal, e-external, c-confed, l-local, a-aggregate, r-redist, I-injected
        Origin codes: i - IGP, e - EGP, ? - incomplete, | - multipath, & - backup

           Network            Next Hop            Metric     LocPrf     Weight Path
        *>r2001:11::1/128     0::                      0        100      32768 ?

        pinxdt-n9kv-2# 
        '''}

    golden_parsed_output4 = {
        'vrf': 
            {'default': 
                {'address_family': 
                    {'ipv4 multicast': 
                        {'bgp_table_version': 175,
                        'local_router_id': '20.0.0.6',
                        'prefixes': {'1.2.1.0/24': {'index': {1: {'localprf': 100,
                                                                 'next_hop': '19.0.101.1',
                                                                 'origin_codes': 'i',
                                                                 'path': '2 '
                                                                         '3 '
                                                                         '4',
                                                                 'path_type': 'i',
                                                                 'status_codes': '*>',
                                                                 'weight': 0}}},
                                    '1.2.2.0/24': {'index': {1: {'localprf': 100,
                                                                 'next_hop': '19.0.101.1',
                                                                 'origin_codes': 'i',
                                                                 'path': '2 '
                                                                         '3 '
                                                                         '4',
                                                                 'path_type': 'i',
                                                                 'status_codes': '*>',
                                                                 'weight': 0}}},
                                    '1.4.1.0/24': {'index': {1: {'localprf': 100,
                                                                 'next_hop': '19.0.102.4',
                                                                 'origin_codes': 'i',
                                                                 'path': '2 '
                                                                         '3 '
                                                                         '4',
                                                                 'path_type': 'i',
                                                                 'status_codes': '*>',
                                                                 'weight': 0}}},
                                    '1.4.2.0/24': {'index': {1: {'localprf': 100,
                                                                 'next_hop': '19.0.102.4',
                                                                 'origin_codes': 'i',
                                                                 'path': '2 '
                                                                         '3 '
                                                                         '4',
                                                                 'path_type': 'i',
                                                                 'status_codes': '*>',
                                                                 'weight': 0}}},
                                    '2.1.0.0/24': {'index': {1: {'next_hop': '19.0.102.3',
                                                                 'origin_codes': 'i',
                                                                 'path': '888 '
                                                                         '10 '
                                                                         '20 '
                                                                         '30 '
                                                                         '40 '
                                                                         '50 '
                                                                         '60 '
                                                                         '70 '
                                                                         '80 '
                                                                         '90',
                                                                 'path_type': 'e',
                                                                 'status_codes': 'd ',
                                                                 'weight': 0}}},
                                    '2.1.1.0/24': {'index': {1: {'next_hop': '19.0.102.3',
                                                                 'origin_codes': 'i',
                                                                 'path': '888 '
                                                                         '10 '
                                                                         '20 '
                                                                         '30 '
                                                                         '40 '
                                                                         '50 '
                                                                         '60 '
                                                                         '70 '
                                                                         '80 '
                                                                         '90',
                                                                 'path_type': 'e',
                                                                 'status_codes': 'd ',
                                                                 'weight': 0}}}}},
                    'ipv4 unicast': 
                        {'bgp_table_version': 174,
                        'local_router_id': '20.0.0.6',
                        'prefixes': {'1.1.1.0/24': {'index': {1: {'localprf': 100,
                                                               'metric': 2222,
                                                               'next_hop': '19.0.101.1',
                                                               'origin_codes': 'i',
                                                               'path': '1 '
                                                                       '2 '
                                                                       '3 '
                                                                       '65000 '
                                                                       '23',
                                                               'path_type': 'i',
                                                               'status_codes': '* ',
                                                               'weight': 0},
                                                            2: {'localprf': 100,
                                                                'next_hop': '19.0.102.4',
                                                                'origin_codes': 'i',
                                                                'path': '{62112 '
                                                                        '33492 '
                                                                        '4872 '
                                                                        '41787 '
                                                                        '13166 '
                                                                        '50081 '
                                                                        '21461 '
                                                                        '58376 '
                                                                        '29755 '
                                                                        '1135}',
                                                                'path_type': 'i',
                                                                'status_codes': '*>',
                                                                'weight': 0}}},
                                    '1.1.2.0/24': {'index': {1: {'localprf': 100,
                                                               'metric': 2222,
                                                               'next_hop': '19.0.101.1',
                                                               'origin_codes': 'i',
                                                               'path': '1 '
                                                                       '2 '
                                                                       '3 '
                                                                       '65000 '
                                                                       '23',
                                                               'path_type': 'i',
                                                               'status_codes': '* ',
                                                               'weight': 0},
                                                            2: {'localprf': 100,
                                                                'next_hop': '19.0.102.4',
                                                                'origin_codes': 'i',
                                                                'path': '{62112 '
                                                                        '33492 '
                                                                        '4872 '
                                                                        '41787 '
                                                                        '13166 '
                                                                        '50081 '
                                                                        '21461 '
                                                                        '58376 '
                                                                        '29755 '
                                                                        '1135}',
                                                                'path_type': 'i',
                                                                'status_codes': '*>',
                                                               'weight': 0}}},
                                    '1.6.0.0/16': {'index': {1: {'localprf': 100,
                                                               'next_hop': '19.0.101.1',
                                                               'origin_codes': 'i',
                                                               'path': '10 '
                                                                       '20 '
                                                                       '30 '
                                                                       '40 '
                                                                       '50 '
                                                                       '60 '
                                                                       '70 '
                                                                       '80 '
                                                                       '90',
                                                               'path_type': 'i',
                                                               'status_codes': '*>',
                                                               'weight': 0}}},
                                    '2.0.0.0/24': {'index': {1: {'next_hop': '19.0.102.3',
                                                               'origin_codes': 'i',
                                                               'path': '888 '
                                                                       '10 '
                                                                       '20 '
                                                                       '30 '
                                                                       '40 '
                                                                       '50 '
                                                                       '60 '
                                                                       '70 '
                                                                       '80 '
                                                                       '90',
                                                               'path_type': 'e',
                                                               'status_codes': 'd ',
                                                               'weight': 0}}},
                                    '2.0.1.0/24': {'index': {1: {'next_hop': '19.0.102.3',
                                                               'origin_codes': 'i',
                                                               'path': '888 '
                                                                       '10 '
                                                                       '20 '
                                                                       '30 '
                                                                       '40 '
                                                                       '50 '
                                                                       '60 '
                                                                       '70 '
                                                                       '80 '
                                                                       '90',
                                                               'path_type': 'e',
                                                               'status_codes': 'd ',
                                                               'weight': 0}}}}},
                    'ipv6 multicast': {'bgp_table_version': 6,
                                                           'local_router_id': '20.0.0.6',
                                                           'prefixes': {'eeee::/113': {'index': {1: {'localprf': 100,
                                                                                                     'next_hop': 'fec0::1002',
                                                                                                     'origin_codes': 'i',
                                                                                                     'path_type': 'i',
                                                                                                     'status_codes': '*>',
                                                                                                     'weight': 0}}},
                                                                        'eeee::8000/113': {'index': {1: {'localprf': 100,
                                                                                                         'next_hop': 'fec0::1002',
                                                                                                         'origin_codes': 'i',
                                                                                                         'path_type': 'i',
                                                                                                         'status_codes': '*>',
                                                                                                         'weight': 0}}}}},
                    'ipv6 unicast': {'bgp_table_version': 173,
                                                         'local_router_id': '20.0.0.6',
                                                         'prefixes': {'2001::/112': {'index': {1: {'next_hop': 'fec0::2002',
                                                                                                   'origin_codes': 'i',
                                                                                                   'path': '888 '
                                                                                                           '10 '
                                                                                                           '20 '
                                                                                                           '30 '
                                                                                                           '40 '
                                                                                                           '50 '
                                                                                                           '60 '
                                                                                                           '70 '
                                                                                                           '80 '
                                                                                                           '90',
                                                                                                   'path_type': 'e',
                                                                                                   'status_codes': 'd ',
                                                                                                   'weight': 0}}},
                                                                      '2001::1:0/112': {'index': {1: {'next_hop': 'fec0::2002',
                                                                                                      'origin_codes': 'i',
                                                                                                      'path': '888 '
                                                                                                              '10 '
                                                                                                              '20 '
                                                                                                              '30 '
                                                                                                              '40 '
                                                                                                              '50 '
                                                                                                              '60 '
                                                                                                              '70 '
                                                                                                              '80 '
                                                                                                              '90',
                                                                                                      'path_type': 'e',
                                                                                                      'status_codes': 'd ',
                                                                                                      'weight': 0}}},
                                                                      'abcd::/112': {'index': {1: {'localprf': 100,
                                                                                                   'next_hop': 'fec0::1002',
                                                                                                   'origin_codes': 'i',
                                                                                                   'path': '3 '
                                                                                                           '10 '
                                                                                                           '20 '
                                                                                                           '30 '
                                                                                                           '40 '
                                                                                                           '50 '
                                                                                                           '60 '
                                                                                                           '70 '
                                                                                                           '80 '
                                                                                                           '90',
                                                                                                   'path_type': 'i',
                                                                                                   'status_codes': '*>',
                                                                                                   'weight': 0}}},
                                                                      'dddd::/113': {'index': {1: {'localprf': 100,
                                                                                                   'metric': 4444,
                                                                                                   'next_hop': 'fec0::1002',
                                                                                                   'origin_codes': 'i',
                                                                                                   'path': '38050 '
                                                                                                           '9430 '
                                                                                                           '46344 '
                                                                                                           '17724 '
                                                                                                           '54639',
                                                                                                   'path_type': 'i',
                                                                                                   'status_codes': '*>',
                                                                                                   'weight': 0}}},
                                                                      'dddd::8000/113': {'index': {1: {'localprf': 100,
                                                                                                       'metric': 4444,
                                                                                                       'next_hop': 'fec0::1002',
                                                                                                       'origin_codes': 'i',
                                                                                                       'path': '38050 '
                                                                                                               '9430 '
                                                                                                               '46344 '
                                                                                                               '17724 '
                                                                                                               '54639',
                                                                                                       'path_type': 'i',
                                                                                                       'status_codes': '*>',
                                                                                                       'weight': 0}}}}},
                    'link-state': {'bgp_table_version': 173,
                                                       'local_router_id': '20.0.0.6',
                                                       'prefixes': {'[2]:[77][7,0][39.39.39.39,1,656877351][39.1.1.1,22][19.0.102.3,39.0.1.30]/616': {'index': {1: {'next_hop': '19.0.102.3',
                                                                                                                                                                    'origin_codes': 'i',
                                                                                                                                                                    'path': '888 '
                                                                                                                                                                            '10 '
                                                                                                                                                                            '20 '
                                                                                                                                                                            '30 '
                                                                                                                                                                            '40 '
                                                                                                                                                                            '50 '
                                                                                                                                                                            '60 '
                                                                                                                                                                            '70 '
                                                                                                                                                                            '80 '
                                                                                                                                                                            '90',
                                                                                                                                                                    'path_type': 'e',
                                                                                                                                                                    'status_codes': 'd ',
                                                                                                                                                                    'weight': 0}}},
                                                                    '[2]:[77][7,0][39.39.39.39,2,656877351][39.1.1.1,22][19.0.102.3,39.0.1.31]/616': {'index': {1: {'next_hop': '19.0.102.3',
                                                                                                                                                                    'origin_codes': 'i',
                                                                                                                                                                    'path': '888 '
                                                                                                                                                                            '10 '
                                                                                                                                                                            '20 '
                                                                                                                                                                            '30 '
                                                                                                                                                                            '40 '
                                                                                                                                                                            '50 '
                                                                                                                                                                            '60 '
                                                                                                                                                                            '70 '
                                                                                                                                                                            '80 '
                                                                                                                                                                            '90',
                                                                                                                                                                    'path_type': 'e',
                                                                                                                                                                    'status_codes': 'd ',
                                                                                                                                                                    'weight': 0}}},
                                                                    '[2]:[77][7,0][9.9.9.9,1,151587081][29.1.1.1,22][19.0.101.1,29.0.1.30]/616': {'index': {1: {'localprf': 100,
                                                                                                                                                                'metric': 4444,
                                                                                                                                                                'next_hop': '19.0.101.1',
                                                                                                                                                                'origin_codes': 'i',
                                                                                                                                                                'path': '3 '
                                                                                                                                                                        '10 '
                                                                                                                                                                        '20 '
                                                                                                                                                                        '30 '
                                                                                                                                                                        '40 '
                                                                                                                                                                        '50 '
                                                                                                                                                                        '60 '
                                                                                                                                                                        '70 '
                                                                                                                                                                        '80 '
                                                                                                                                                                        '90',
                                                                                                                                                                'path_type': 'i',
                                                                                                                                                                'status_codes': '*>',
                                                                                                                                                                'weight': 0}}},
                                                                    '[2]:[77][7,0][9.9.9.9,2,151587081][29.1.1.1,22][19.0.101.1,29.0.1.31]/616': {'index': {1: {'localprf': 100,
                                                                                                                                                                'metric': 4444,
                                                                                                                                                                'next_hop': '19.0.101.1',
                                                                                                                                                                'origin_codes': 'i',
                                                                                                                                                                'path': '3 '
                                                                                                                                                                        '10 '
                                                                                                                                                                        '20 '
                                                                                                                                                                        '30 '
                                                                                                                                                                        '40 '
                                                                                                                                                                        '50 '
                                                                                                                                                                        '60 '
                                                                                                                                                                        '70 '
                                                                                                                                                                        '80 '
                                                                                                                                                                        '90',
                                                                                                                                                                'path_type': 'i',
                                                                                                                                                                'status_codes': '*>',
                                                                                                                                                                'weight': 0}}}}},
                    'vpnv4 unicast': 
                        {'bgp_table_version': 183,
                        'local_router_id': '20.0.0.6'},
                    'vpnv4 unicast RD 0:0': {'bgp_table_version': 183,
                                                                 'local_router_id': '20.0.0.6',
                                                                 'prefixes': {'2.3.1.0/24': {'index': {1: {'next_hop': '19.0.102.3',
                                                                                                           'origin_codes': 'i',
                                                                                                           'path': '888 '
                                                                                                                   '10 '
                                                                                                                   '20 '
                                                                                                                   '30 '
                                                                                                                   '40 '
                                                                                                                   '50 '
                                                                                                                   '60 '
                                                                                                                   '70 '
                                                                                                                   '80 '
                                                                                                                   '90',
                                                                                                           'path_type': 'e',
                                                                                                           'status_codes': 'd ',
                                                                                                           'weight': 0}}},
                                                                              '2.3.2.0/24': {'index': {1: {'next_hop': '19.0.102.3',
                                                                                                           'origin_codes': 'i',
                                                                                                           'path': '888 '
                                                                                                                   '10 '
                                                                                                                   '20 '
                                                                                                                   '30 '
                                                                                                                   '40 '
                                                                                                                   '50 '
                                                                                                                   '60 '
                                                                                                                   '70 '
                                                                                                                   '80 '
                                                                                                                   '90',
                                                                                                           'path_type': 'e',
                                                                                                           'status_codes': 'd ',
                                                                                                           'weight': 0}}}},
                                                                 'route_distinguisher': '0:0'},
                    'vpnv4 unicast RD 101:100': {'bgp_table_version': 183,
                                                                     'local_router_id': '20.0.0.6',
                                                                     'prefixes': {'1.3.1.0/24': {'index': {1: {'localprf': 100,
                                                                                                               'next_hop': '19.0.102.4',
                                                                                                               'origin_codes': 'i',
                                                                                                               'path': '3 '
                                                                                                                       '10 '
                                                                                                                       '20 '
                                                                                                                       '30 '
                                                                                                                       '40',
                                                                                                               'path_type': 'i',
                                                                                                               'status_codes': '*>',
                                                                                                               'weight': 0},
                                                                                                            2: {'localprf': 100,
                                                                                                                'metric': 4444,
                                                                                                                'next_hop': '19.0.101.1',
                                                                                                                'origin_codes': 'i',
                                                                                                                'path': '3 '
                                                                                                                        '10 '
                                                                                                                        '20 '
                                                                                                                        '4 '
                                                                                                                        '5 '
                                                                                                                        '6 '
                                                                                                                        '3 '
                                                                                                                        '10 '
                                                                                                                        '20 '
                                                                                                                        '4 '
                                                                                                                        '5 '
                                                                                                                        '6',
                                                                                                                'path_type': 'i',
                                                                                                                'status_codes': '* ',
                                                                                                               'weight': 0}}},
                                                                                  '1.3.2.0/24': {'index': {1: {'localprf': 100,
                                                                                                               'next_hop': '19.0.102.4',
                                                                                                               'origin_codes': 'i',
                                                                                                               'path': '3 '
                                                                                                                       '10 '
                                                                                                                       '20 '
                                                                                                                       '30 '
                                                                                                                       '40',
                                                                                                               'path_type': 'i',
                                                                                                               'status_codes': '*>',
                                                                                                               'weight': 0},
                                                                                                            2: {'localprf': 100,
                                                                                                                'metric': 4444,
                                                                                                                'next_hop': '19.0.101.1',
                                                                                                                'origin_codes': 'i',
                                                                                                                'path': '3 '
                                                                                                                        '10 '
                                                                                                                        '20 '
                                                                                                                        '4 '
                                                                                                                        '5 '
                                                                                                                        '6 '
                                                                                                                        '3 '
                                                                                                                        '10 '
                                                                                                                        '20 '
                                                                                                                        '4 '
                                                                                                                        '5 '
                                                                                                                        '6',
                                                                                                                'path_type': 'i',
                                                                                                                'status_codes': '* ',
                                                                                                                'weight': 0}}}},
                                                                     'route_distinguisher': '101:100'},
                    'vpnv4 unicast RD 102:100': {'bgp_table_version': 183,
                                                                     'local_router_id': '20.0.0.6',
                                                                     'prefixes': {'102.1.1.0/24': {'index': {1: {'localprf': 100,
                                                                                                                 'next_hop': '19.0.102.4',
                                                                                                                 'origin_codes': 'i',
                                                                                                                 'path': '200 '
                                                                                                                         '300 '
                                                                                                                         '400 '
                                                                                                                         '500 '
                                                                                                                         '600 '
                                                                                                                         '700',
                                                                                                                 'path_type': 'i',
                                                                                                                 'status_codes': '*>',
                                                                                                                 'weight': 0}}},
                                                                                  '102.1.2.0/24': {'index': {1: {'localprf': 100,
                                                                                                                 'next_hop': '19.0.102.4',
                                                                                                                 'origin_codes': 'i',
                                                                                                                 'path': '200 '
                                                                                                                         '300 '
                                                                                                                         '400 '
                                                                                                                         '500 '
                                                                                                                         '600 '
                                                                                                                         '700',
                                                                                                                 'path_type': 'i',
                                                                                                                 'status_codes': '*>',
                                                                                                                 'weight': 0}}}},
                                                                     'route_distinguisher': '102:100'},
                    'vpnv6 unicast': 
                        {'bgp_table_version': 13,
                        'local_router_id': '20.0.0.6'},
                    'vpnv6 unicast RD 0xbb00010000000000': {'bgp_table_version': 13,
                                                                                'local_router_id': '20.0.0.6',
                                                                                'prefixes': {'0:0:80::/41': {'index': {1: {'next_hop': '0',
                                                                                                                           'origin_codes': 'i',
                                                                                                                           'path': '10 '
                                                                                                                                   '20 '
                                                                                                                                   '30 '
                                                                                                                                   '40 '
                                                                                                                                   '50 '
                                                                                                                                   '60 '
                                                                                                                                   '70 '
                                                                                                                                   '80 '
                                                                                                                                   '90',
                                                                                                                           'path_type': 'e',
                                                                                                                           'status_codes': '*>',
                                                                                                                           'weight': 888}}},
                                                                                             '0::/41': {'index': {1: {'next_hop': '0',
                                                                                                                      'origin_codes': 'i',
                                                                                                                      'path': '10 '
                                                                                                                              '20 '
                                                                                                                              '30 '
                                                                                                                              '40 '
                                                                                                                              '50 '
                                                                                                                              '60 '
                                                                                                                              '70 '
                                                                                                                              '80 '
                                                                                                                              '90',
                                                                                                                      'path_type': 'e',
                                                                                                                      'status_codes': '*>',
                                                                                                                      'weight': 888}}}},
                                                                                'route_distinguisher': '0xbb00010000000000'},
                    'vpnv6 unicast RD 100:200': {'bgp_table_version': 13,
                                                                     'local_router_id': '20.0.0.6',
                                                                     'prefixes': {'aaaa:1::/113': {'index': {1: {'localprf': 100,
                                                                                                                 'next_hop': '4444',
                                                                                                                 'origin_codes': 'i',
                                                                                                                 'path_type': 'i',
                                                                                                                 'status_codes': '*>',
                                                                                                                 'weight': 0}}},
                                                                                  'aaaa:1::8000/113': {'index': {1: {'localprf': 100,
                                                                                                                     'next_hop': '4444',
                                                                                                                     'origin_codes': 'i',
                                                                                                                     'path_type': 'i',
                                                                                                                     'status_codes': '*>',
                                                                                                                     'weight': 0}}}},
                                                                     'route_distinguisher': '100:200'}}},
            'vpn1': 
                {'address_family': 
                    {'ipv4 unicast': {'bgp_table_version': 9,
                                                      'local_router_id': '0.0.0.0',
                                                      'prefixes': {'1.1.1.0/24': {'index': {1: {'localprf': 100,
                                                                                                'next_hop': '19.0.102.4',
                                                                                                'origin_codes': 'i',
                                                                                                'path': '{62112 '
                                                                                                        '33492 '
                                                                                                        '4872 '
                                                                                                        '41787 '
                                                                                                        '13166 '
                                                                                                        '50081 '
                                                                                                        '21461 '
                                                                                                        '58376 '
                                                                                                        '29755 '
                                                                                                        '1135}',
                                                                                                'path_type': 'i',
                                                                                                'status_codes': '*>',
                                                                                                'weight': 0}}},
                                                                   '1.1.2.0/24': {'index': {1: {'localprf': 100,
                                                                                                'next_hop': '19.0.102.4',
                                                                                                'origin_codes': 'i',
                                                                                                'path': '{62112 '
                                                                                                        '33492 '
                                                                                                        '4872 '
                                                                                                        '41787 '
                                                                                                        '13166 '
                                                                                                        '50081 '
                                                                                                        '21461 '
                                                                                                        '58376 '
                                                                                                        '29755 '
                                                                                                        '1135}',
                                                                                                'path_type': 'i',
                                                                                                'status_codes': '*>',
                                                                                                'weight': 0}}},
                                                                   '1.6.0.0/16': {'index': {1: {'localprf': 100,
                                                                                                'next_hop': '19.0.101.1',
                                                                                                'origin_codes': 'i',
                                                                                                'path': '10 '
                                                                                                        '20 '
                                                                                                        '30 '
                                                                                                        '40 '
                                                                                                        '50 '
                                                                                                        '60 '
                                                                                                        '70 '
                                                                                                        '80 '
                                                                                                        '90',
                                                                                                'path_type': 'i',
                                                                                                'status_codes': '*>',
                                                                                                'weight': 0}}}}}}},
            'vpn2': 
                {'address_family': 
                    {'ipv4 unicast': {'bgp_table_version': 7,
                                                      'local_router_id': '0.0.0.0',
                                                      'prefixes': {'1.1.1.0/24': {'index': {1: {'localprf': 100,
                                                                                                'next_hop': '19.0.102.4',
                                                                                                'origin_codes': 'i',
                                                                                                'path': '{62112 '
                                                                                                        '33492 '
                                                                                                        '4872 '
                                                                                                        '41787 '
                                                                                                        '13166 '
                                                                                                        '50081 '
                                                                                                        '21461 '
                                                                                                        '58376 '
                                                                                                        '29755 '
                                                                                                        '1135}',
                                                                                                'path_type': 'i',
                                                                                                'status_codes': '*>',
                                                                                                'weight': 0}}},
                                                                   '1.1.2.0/24': {'index': {1: {'localprf': 100,
                                                                                                'next_hop': '19.0.102.4',
                                                                                                'origin_codes': 'i',
                                                                                                'path': '{62112 '
                                                                                                        '33492 '
                                                                                                        '4872 '
                                                                                                        '41787 '
                                                                                                        '13166 '
                                                                                                        '50081 '
                                                                                                        '21461 '
                                                                                                        '58376 '
                                                                                                        '29755 '
                                                                                                        '1135}',
                                                                                                'path_type': 'i',
                                                                                                'status_codes': '*>',
                                                                                                'weight': 0}}},
                                                                   '1.6.0.0/16': {'index': {1: {'localprf': 100,
                                                                                                'next_hop': '19.0.101.1',
                                                                                                'origin_codes': 'i',
                                                                                                'path': '10 '
                                                                                                        '20 '
                                                                                                        '30 '
                                                                                                        '40 '
                                                                                                        '50 '
                                                                                                        '60 '
                                                                                                        '70 '
                                                                                                        '80 '
                                                                                                        '90',
                                                                                                'path_type': 'i',
                                                                                                'status_codes': '*>',
                                                                                                'weight': 0}}}}},
                    'ipv6 unicast': {'bgp_table_version': 7,
                                                      'local_router_id': '0.0.0.0',
                                                      'prefixes': {'abcd::/112': {'index': {1: {'localprf': 100,
                                                                                                'next_hop': 'fec0::1002',
                                                                                                'origin_codes': 'i',
                                                                                                'path': '3 '
                                                                                                        '10 '
                                                                                                        '20 '
                                                                                                        '30 '
                                                                                                        '40 '
                                                                                                        '50 '
                                                                                                        '60 '
                                                                                                        '70 '
                                                                                                        '80 '
                                                                                                        '90',
                                                                                                'path_type': 'i',
                                                                                                'status_codes': '*>',
                                                                                                'weight': 0}}},
                                                                   'dddd::/113': {'index': {1: {'localprf': 100,
                                                                                                'metric': 4444,
                                                                                                'next_hop': 'fec0::1002',
                                                                                                'origin_codes': 'i',
                                                                                                'path': '38050 '
                                                                                                        '9430 '
                                                                                                        '46344 '
                                                                                                        '17724 '
                                                                                                        '54639',
                                                                                                'path_type': 'i',
                                                                                                'status_codes': '*>',
                                                                                                'weight': 0}}},
                                                                   'dddd::8000/113': {'index': {1: {'localprf': 100,
                                                                                                    'metric': 4444,
                                                                                                    'next_hop': 'fec0::1002',
                                                                                                    'origin_codes': 'i',
                                                                                                    'path': '38050 '
                                                                                                            '9430 '
                                                                                                            '46344 '
                                                                                                            '17724 '
                                                                                                            '54639',
                                                                                                    'path_type': 'i',
                                                                                                    'status_codes': '*>',
                                                                                                    'weight': 0}}}}}}}}}

    golden_output4 = {'execute.return_value': '''
        show bgp vrf all all

        BGP routing table information for VRF default, address family IPv4 Unicast
        BGP table version is 174, Local Router ID is 20.0.0.6
        Status: s-suppressed, x-deleted, S-stale, d-dampened, h-history, *-valid, >-best
        Path type: i-internal, e-external, c-confed, l-local, a-aggregate, r-redist, I-injected
        Origin codes: i - IGP, e - EGP, ? - incomplete, | - multipath, & - backup

           Network            Next Hop            Metric     LocPrf     Weight Path
        * i1.1.1.0/24         19.0.101.1            2222        100          0 1 2 3 65000 23 i
        *>i                   19.0.102.4                        100          0 {62112 33492 4872 41787 13166 50081 21461 58376 29755 1135} i
        * i1.1.2.0/24         19.0.101.1            2222        100          0 1 2 3 65000 23 i
        *>i                   19.0.102.4                        100          0 {62112 33492 4872 41787 13166 50081 21461 58376 29755 1135} i
        *>i1.6.0.0/16         19.0.101.1                        100          0 10 20 30 40 50 60 70 80 90 i
        d e2.0.0.0/24         19.0.102.3                                     0 888 10 20 30 40 50 60 70 80 90 i
        d e2.0.1.0/24         19.0.102.3                                     0 888 10 20 30 40 50 60 70 80 90 i

        BGP routing table information for VRF default, address family IPv4 Multicast
        BGP table version is 175, Local Router ID is 20.0.0.6
        Status: s-suppressed, x-deleted, S-stale, d-dampened, h-history, *-valid, >-best
        Path type: i-internal, e-external, c-confed, l-local, a-aggregate, r-redist, I-injected
        Origin codes: i - IGP, e - EGP, ? - incomplete, | - multipath, & - backup

           Network            Next Hop            Metric     LocPrf     Weight Path
        *>i1.2.1.0/24         19.0.101.1                        100          0 2 3 4 i
        *>i1.2.2.0/24         19.0.101.1                        100          0 2 3 4 i
        *>i1.4.1.0/24         19.0.102.4                        100          0 2 3 4 i
        *>i1.4.2.0/24         19.0.102.4                        100          0 2 3 4 i
        d e2.1.0.0/24         19.0.102.3                                     0 888 10 20 30 40 50 60 70 80 90 i
        d e2.1.1.0/24         19.0.102.3                                     0 888 10 20 30 40 50 60 70 80 90 i

        BGP routing table information for VRF default, address family IPv6 Unicast
        BGP table version is 173, Local Router ID is 20.0.0.6
        Status: s-suppressed, x-deleted, S-stale, d-dampened, h-history, *-valid, >-best
        Path type: i-internal, e-external, c-confed, l-local, a-aggregate, r-redist, I-injected
        Origin codes: i - IGP, e - EGP, ? - incomplete, | - multipath, & - backup

           Network            Next Hop            Metric     LocPrf     Weight Path
        d e2001::/112         fec0::2002                                     0 888 10 20 30 40 50 60 70 80 90 i
        d e2001::1:0/112      fec0::2002                                     0 888 10 20 30 40 50 60 70 80 90 i
        *>iabcd::/112         fec0::1002                        100          0 3 10 20 30 40 50 60 70 80 90 i
        *>idddd::/113         fec0::1002            4444        100          0 38050 9430 46344 17724 54639 i
        *>idddd::8000/113     fec0::1002            4444        100          0 38050 9430 46344 17724 54639 i

        BGP routing table information for VRF default, address family IPv6 Multicast
        BGP table version is 6, Local Router ID is 20.0.0.6
        Status: s-suppressed, x-deleted, S-stale, d-dampened, h-history, *-valid, >-best
        Path type: i-internal, e-external, c-confed, l-local, a-aggregate, r-redist, I-injected
        Origin codes: i - IGP, e - EGP, ? - incomplete, | - multipath, & - backup

           Network            Next Hop            Metric     LocPrf     Weight Path
        *>ieeee::/113         fec0::1002                        100          0 i
        *>ieeee::8000/113     fec0::1002                        100          0 i

        BGP routing table information for VRF default, address family VPNv4 Unicast
        BGP table version is 183, Local Router ID is 20.0.0.6
        Status: s-suppressed, x-deleted, S-stale, d-dampened, h-history, *-valid, >-best
        Path type: i-internal, e-external, c-confed, l-local, a-aggregate, r-redist, I-injected
        Origin codes: i - IGP, e - EGP, ? - incomplete, | - multipath, & - backup

           Network            Next Hop            Metric     LocPrf     Weight Path
        Route Distinguisher: 0:0
        d e2.3.1.0/24         19.0.102.3                                     0 888 10 20 30 40 50 60 70 80 90 i
        d e2.3.2.0/24         19.0.102.3                                     0 888 10 20 30 40 50 60 70 80 90 i

        Route Distinguisher: 101:100
        *>i1.3.1.0/24         19.0.102.4                        100          0 3 10 20 30 40 i
        * i                   19.0.101.1            4444        100          0 3 10 20 4 5 6 3 10 20 4 5 6 i
        *>i1.3.2.0/24         19.0.102.4                        100          0 3 10 20 30 40 i
        * i                   19.0.101.1            4444        100          0 3 10 20 4 5 6 3 10 20 4 5 6 i

        Route Distinguisher: 102:100
        *>i102.1.1.0/24       19.0.102.4                        100          0 200 300 400 500 600 700 i
        *>i102.1.2.0/24       19.0.102.4                        100          0 200 300 400 500 600 700 i

        BGP routing table information for VRF default, address family VPNv6 Unicast
        BGP table version is 13, Local Router ID is 20.0.0.6
        Status: s-suppressed, x-deleted, S-stale, d-dampened, h-history, *-valid, >-best
        Path type: i-internal, e-external, c-confed, l-local, a-aggregate, r-redist, I-injected
        Origin codes: i - IGP, e - EGP, ? - incomplete, | - multipath, & - backup

           Network            Next Hop            Metric     LocPrf     Weight Path
        Route Distinguisher: 100:200
        *>iaaaa:1::/113       ::ffff:19.0.101.1
                                                    4444        100          0 i
        *>iaaaa:1::8000/113   ::ffff:19.0.101.1
                                                    4444        100          0 i

        Route Distinguisher: 0xbb00010000000000
        *>e0::/41             ::ffff:19.0.102.3
                                                                             0 888 10 20 30 40 50 60 70 80 90 i
        *>e0:0:80::/41        ::ffff:19.0.102.3
                                                                             0 888 10 20 30 40 50 60 70 80 90 i

        BGP routing table information for VRF default, address family Link-State
        BGP table version is 173, Local Router ID is 20.0.0.6
        Status: s-suppressed, x-deleted, S-stale, d-dampened, h-history, *-valid, >-best
        Path type: i-internal, e-external, c-confed, l-local, a-aggregate, r-redist, I-injected
        Origin codes: i - IGP, e - EGP, ? - incomplete, | - multipath, & - backup

           Network            Next Hop            Metric     LocPrf     Weight Path
        *>i[2]:[77][7,0][9.9.9.9,1,151587081][29.1.1.1,22][19.0.101.1,29.0.1.30]/616
                              19.0.101.1            4444        100          0 3 10 20 30 40 50 60 70 80 90 i
        d e[2]:[77][7,0][39.39.39.39,1,656877351][39.1.1.1,22][19.0.102.3,39.0.1.30]/616
                              19.0.102.3                                     0 888 10 20 30 40 50 60 70 80 90 i
        *>i[2]:[77][7,0][9.9.9.9,2,151587081][29.1.1.1,22][19.0.101.1,29.0.1.31]/616
                              19.0.101.1            4444        100          0 3 10 20 30 40 50 60 70 80 90 i
        d e[2]:[77][7,0][39.39.39.39,2,656877351][39.1.1.1,22][19.0.102.3,39.0.1.31]/616
                              19.0.102.3                                     0 888 10 20 30 40 50 60 70 80 90 i

        BGP routing table information for VRF vpn1, address family IPv4 Unicast
        BGP table version is 9, Local Router ID is 0.0.0.0
        Status: s-suppressed, x-deleted, S-stale, d-dampened, h-history, *-valid, >-best
        Path type: i-internal, e-external, c-confed, l-local, a-aggregate, r-redist, I-injected
        Origin codes: i - IGP, e - EGP, ? - incomplete, | - multipath, & - backup

           Network            Next Hop            Metric     LocPrf     Weight Path
        *>i1.1.1.0/24         19.0.102.4                        100          0 {62112 33492 4872 41787 13166 50081 21461 58376 29755 1135} i
        *>i1.1.2.0/24         19.0.102.4                        100          0 {62112 33492 4872 41787 13166 50081 21461 58376 29755 1135} i
        *>i1.6.0.0/16         19.0.101.1                        100          0 10 20 30 40 50 60 70 80 90 i

        BGP routing table information for VRF vpn2, address family IPv4 Unicast
        BGP table version is 7, Local Router ID is 0.0.0.0
        Status: s-suppressed, x-deleted, S-stale, d-dampened, h-history, *-valid, >-best
        Path type: i-internal, e-external, c-confed, l-local, a-aggregate, r-redist, I-injected
        Origin codes: i - IGP, e - EGP, ? - incomplete, | - multipath, & - backup

           Network            Next Hop            Metric     LocPrf     Weight Path
        *>i1.1.1.0/24         19.0.102.4                        100          0 {62112 33492 4872 41787 13166 50081 21461 58376 29755 1135} i
        *>i1.1.2.0/24         19.0.102.4                        100          0 {62112 33492 4872 41787 13166 50081 21461 58376 29755 1135} i
        *>i1.6.0.0/16         19.0.101.1                        100          0 10 20 30 40 50 60 70 80 90 i

        BGP routing table information for VRF vpn2, address family IPv6 Unicast
        BGP table version is 7, Local Router ID is 0.0.0.0
        Status: s-suppressed, x-deleted, S-stale, d-dampened, h-history, *-valid, >-best
        Path type: i-internal, e-external, c-confed, l-local, a-aggregate, r-redist, I-injected
        Origin codes: i - IGP, e - EGP, ? - incomplete, | - multipath, & - backup

           Network            Next Hop            Metric     LocPrf     Weight Path
        *>iabcd::/112         fec0::1002                        100          0 3 10 20 30 40 50 60 70 80 90 i
        *>idddd::/113         fec0::1002            4444        100          0 38050 9430 46344 17724 54639 i
        *>idddd::8000/113     fec0::1002            4444        100          0 38050 9430 46344 17724 54639 i
        '''}

    def test_show_bgp_vrf_all_all_golden1(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output1)
        obj = ShowBgpVrfAllAll(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output1)

    def test_show_bgp_vrf_all_all_golden2(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output2)
        obj = ShowBgpVrfAllAll(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output2)

    def test_show_bgp_vrf_all_all_golden3(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output3)
        obj = ShowBgpVrfAllAll(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output3)

    def test_show_bgp_vrf_all_all_golden4(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output4)
        obj = ShowBgpVrfAllAll(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output4)

    def test_show_bgp_vrf_all_all_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowBgpVrfAllAll(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

# ==================================================
#  Unit test for 'show bgp vrf <WORD> all neighbors'       
# ==================================================

class test_show_bgp_vrf_all_neighbors(unittest.TestCase):
    
    '''Unit test for show bgp vrf all all neighbors'''

    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output1 = {
        'neighbor':
            {'2.2.2.10':
                {'address_family':
                    {'ipv4 unicast':
                        {'bgp_table_version': 21,
                        'next_hop_self': False,
                        'path':
                            {'accepted_paths': 0,
                            'memory_usage': 0,
                            'total_entries': 0},
                        'neighbor_version': 0,
                        'soo': 'SOO:100:100'}},
                'bgp_negotiated_keepalive_timers':
                    {'hold_time': 180,
                    'keepalive_interval': 60,
                    'keepalive_timer': 'not '
                                       'running',
                    'last_read': 'never',
                    'last_written': 'never'},
                'bgp_neighbor_counters':
                    {'messages':
                        {'received':
                            {'bytes_in_queue': 0,
                            'capability': 0,
                            'keepalives': 0,
                            'notifications': 0,
                            'opens': 0,
                            'route_refresh': 0,
                            'total': 0,
                            'total_bytes': 0,
                            'updates': 0},
                        'sent':
                            {'bytes_in_queue': 0,
                            'capability': 0,
                            'keepalives': 0,
                            'notifications': 0,
                            'opens': 0,
                            'route_refresh': 0,
                            'total': 0,
                            'total_bytes': 0,
                            'updates': 0}}},
                'bgp_session_transport':
                    {'connection':
                        {'dropped': 0,
                        'established': 0,
                        'last_reset': 'never',
                        'reset_by': 'peer',
                        'reset_reason': 'no '
                                        'error'}},
                'bgp_version': 4,
                'link': 'unknown',
                'local_as': 'None',
                'peer_index': 1,
                'received_bytes_queue': 0,
                'received_messages': 0,
                'received_notifications': 0,
                'remote_as': 0,
                'retry_time': '0.000000',
                'router_id': '0.0.0.0',
                'sent_bytes_queue': 0,
                'sent_messages': 0,
                'sent_notifications': 0,
                'session_state': 'Idle',
                'shutdown': False,
                'up_time': '02:19:37'}}}

    golden_output1 = {'execute.return_value': '''
        N7k# show bgp vrf VRF1 all neighbors 
        BGP neighbor is 2.2.2.10,  remote AS 0, unknown link,  Peer index 1
          BGP version 4, remote router ID 0.0.0.0
          BGP state = Idle, down for 02:19:37, retry in 0.000000
          Last read never, hold time = 180, keepalive interval is 60 seconds
          Last written never, keepalive timer not running
          Received 0 messages, 0 notifications, 0 bytes in queue
          Sent 0 messages, 0 notifications, 0 bytes in queue
          Connections established 0, dropped 0
          Connection attempts 0
          Last reset by us never, due to No error
          Last reset by peer never, due to No error

          Message statistics:
                                      Sent               Rcvd
          Opens:                         0                  0  
          Notifications:                 0                  0  
          Updates:                       0                  0  
          Keepalives:                    0                  0  
          Route Refresh:                 0                  0  
          Capability:                    0                  0  
          Total:                         0                  0  
          Total bytes:                   0                  0  
          Bytes in queue:                0                  0  

          For address family: IPv4 Unicast
          BGP table version 21, neighbor version 0
          0 accepted paths consume 0 bytes of memory
          0 sent paths
          Third-party Nexthop will not be computed.
          SOO Extcommunity: SOO:100:100

          No established BGP session with peer
        '''}

    golden_parsed_output2 = {
        'neighbor':
            {'2.2.2.2':
                {'address_family':
                    {'vpnv4 unicast':
                        {'bgp_table_version': 11,
                        'maximum_prefix_max_prefix_no': 300000,
                        'next_hop_self': False,
                        'path':
                            {'accepted_paths': 1,
                            'memory_usage': 48,
                            'total_entries': 2},
                        'route_map_name_in': 'genie_redistribution',
                        'route_map_name_out': 'genie_redistribution',
                        'neighbor_version': 11,
                        'send_community': True},
                    'vpnv6 unicast':
                        {'bgp_table_version': 10,
                        'next_hop_self': False,
                        'path':
                            {'accepted_paths': 1,
                            'memory_usage': 48,
                            'total_entries': 2},
                        'neighbor_version': 10,
                        'send_community': True}},
                'bfd_live_detection': True,
                'bgp_negotiated_capabilities':
                    {'dynamic_capability': 'advertised '
                                           '(mp, '
                                           'refresh, '
                                           'gr) '
                                           'received '
                                           '(mp, '
                                           'refresh, '
                                           'gr)',
                    'dynamic_capability_old': 'advertised '
                                              'received',
                    'graceful_restart': 'advertised '
                                        'received',
                    'route_refresh': 'advertised '
                                     'received',
                    'route_refresh_old': 'advertised '
                                         'received',
                    'vpnv4_unicast': 'advertised '
                                     'received',
                    'vpnv6_unicast': 'advertised '
                                     'received'},
                'bgp_negotiated_keepalive_timers':
                    {'hold_time': 99,
                    'keepalive_interval': 33,
                    'keepalive_timer': 'expiry '
                                     'due '
                                     '00:00:19',
                    'last_read': '00:00:15',
                    'last_written': '00:00:13'},
                'bgp_neighbor_counters':
                    {'messages':
                        {'received':
                            {'bytes_in_queue': 0,
                            'capability': 0,
                            'keepalives': 256,
                            'notifications': 0,
                            'opens': 1,
                            'route_refresh': 0,
                            'total': 261,
                            'total_bytes': 5139,
                            'updates': 4},
                        'sent':
                            {'bytes_in_queue': 0,
                            'capability': 0,
                            'keepalives': 256,
                            'notifications': 0,
                            'opens': 1,
                            'route_refresh': 0,
                            'total': 263,
                            'total_bytes': 5311,
                            'updates': 6}}},
                'bgp_session_transport':
                    {'connection':
                        {'dropped': 0,
                        'established': 1,
                        'last_reset': 'never',
                        'reset_by': 'peer',
                        'reset_reason': 'no '
                                        'error'},
                    'transport':
                        {'fd': '44',
                        'foreign_host': '2.2.2.2',
                        'foreign_port': '179',
                        'local_host': '1.1.1.1',
                        'local_port': '57144'}},
                'bgp_version': 4,
                'description': 'nei_desc',
                'graceful_restart_paramters':
                    {'restart_time_advertised_by_peer_seconds': 120,
                    'restart_time_advertised_to_peer_seconds': 240,
                    'stale_time_advertised_by_peer_seconds': 600},
                'link': 'ibgp',
                'local_as': 'None',
                'nbr_local_as_cmd': 'not active',
                'peer_index': 1,
                'received_bytes_queue': 0,
                'received_messages': 261,
                'received_notifications': 0,
                'remote_as': 100,
                'retry_time': 'None',
                'router_id': '2.2.2.2',
                'sent_bytes_queue': 0,
                'sent_messages': 263,
                'sent_notifications': 0,
                'session_state': 'Established',
                'shutdown': False,
                'suppress_four_byte_as_capability': True,
                'up_time': '02:20:02',
                'update_source': 'loopback0'},
            '2.2.2.25':
                {'bgp_negotiated_keepalive_timers':
                    {'hold_time': 45,
                    'keepalive_interval': 15,
                    'keepalive_timer': 'not '
                                      'running',
                    'last_read': 'never',
                    'last_written': 'never'},
                'bgp_neighbor_counters':
                    {'messages':
                        {'received':
                            {'bytes_in_queue': 0,
                            'capability': 0,
                            'keepalives': 0,
                            'notifications': 0,
                            'opens': 0,
                            'route_refresh': 0,
                            'total': 0,
                            'total_bytes': 0,
                            'updates': 0},
                        'sent':
                            {'bytes_in_queue': 0,
                            'capability': 0,
                            'keepalives': 0,
                            'notifications': 0,
                            'opens': 0,
                            'route_refresh': 0,
                            'total': 0,
                            'total_bytes': 0,
                            'updates': 0}}},
                'bgp_session_transport':
                    {'connection':
                        {'dropped': 0,
                        'established': 0,
                        'last_reset': 'never',
                        'reset_by': 'peer',
                        'reset_reason': 'no '
                                        'error'}},
                'bgp_version': 4,
                'link': 'unknown',
                'local_as': 'None',
                'peer_index': 3,
                'received_bytes_queue': 0,
                'received_messages': 0,
                'received_notifications': 0,
                'remote_as': 0,
                'retry_time': '0.000000',
                'router_id': '0.0.0.0',
                'sent_bytes_queue': 0,
                'sent_messages': 0,
                'sent_notifications': 0,
                'session_state': 'Idle',
                'shutdown': False,
                'up_time': '02:20:08'},
            '2.2.2.5':
                {'address_family':
                    {'ipv4 unicast':
                        {'as_override': True,
                        'as_override_count': 9,
                        'bgp_table_version': 2,
                        'inherit_peer_policy':
                            {'PEER-POLICY':
                                {'inherit_peer_seq': 10},
                            'PEER-POLICY2':
                                {'inherit_peer_seq': 20}},
                        'maximum_prefix_max_prefix_no': 300,
                        'nbr_af_default_originate': True,
                        'nbr_af_default_originate_route_map': 'Default '
                                                              'information '
                                                              'originate, '
                                                              'default '
                                                              'not '
                                                              'sent',
                        'next_hop_self': True,
                        'path':
                            {'accepted_paths': 0,
                            'memory_usage': 0,
                            'total_entries': 0},
                        'route_map_name_in': 'test-map',
                        'route_map_name_out': 'test-map',
                        'neighbor_version': 0,
                        'send_community': True,
                        'soft_configuration': True}},
                'bfd_live_detection': True,
                'bgp_negotiated_keepalive_timers':
                    {'hold_time': 45,
                    'keepalive_interval': 15,
                    'keepalive_timer': 'not '
                    'running',
                    'last_read': 'never',
                    'last_written': 'never'},
                'bgp_neighbor_counters':
                    {'messages':
                        {'received':
                            {'bytes_in_queue': 0,
                            'capability': 0,
                            'keepalives': 0,
                            'notifications': 0,
                            'opens': 0,
                            'route_refresh': 0,
                            'total': 0,
                            'total_bytes': 0,
                            'updates': 0},
                        'sent':
                            {'bytes_in_queue': 0,
                            'capability': 0,
                            'keepalives': 0,
                            'notifications': 0,
                            'opens': 0,
                            'route_refresh': 0,
                            'total': 0,
                            'total_bytes': 0,
                            'updates': 0}}},
                'bgp_session_transport':
                    {'connection':
                        {'dropped': 0,
                        'established': 0,
                        'last_reset': 'never',
                        'mode': 'allowed',
                        'reset_by': 'peer',
                        'reset_reason': 'no '
                                        'error'}},
                'bgp_version': 4,
                'disable_connected_check': True,
                'description': 'PEER-SESSION',
                'inherit_peer_session': 'PEER-SESSION',
                'link': 'ebgp',
                'local_as': '333',
                'peer_index': 2,
                'ebgp_multihop': True,
                'ebgp_multihop_max_hop': 255,
                'received_bytes_queue': 0,
                'received_messages': 0,
                'received_notifications': 0,
                'remote_as': 200,
                'retry_time': 'None',
                'router_id': '0.0.0.0',
                'sent_bytes_queue': 0,
                'sent_messages': 0,
                'sent_notifications': 0,
                'session_state': 'Shut (Admin)',
                'shutdown': True,
                'tcp_md5_auth': 'enabled',
                'tcp_md5_auth_config': 'TCP MD5 authentication '
                                       'is enabled',
                'up_time': '02:20:09',
                'update_source': 'loopback0'}}}

    golden_output2 = {'execute.return_value': '''
        N7k# show bgp vrf default all neighbors 
        BGP neighbor is 2.2.2.2,  remote AS 100, ibgp link,  Peer index 1
          Description: nei_desc
          BGP version 4, remote router ID 2.2.2.2
          BGP state = Established, up for 02:20:02
          Using loopback0 as update source for this peer
          BFD live-detection is configured
          Neighbor local-as command not active
          Last read 00:00:15, hold time = 99, keepalive interval is 33 seconds
          Last written 00:00:13, keepalive timer expiry due 00:00:19
          Received 261 messages, 0 notifications, 0 bytes in queue
          Sent 263 messages, 0 notifications, 0 bytes in queue
          Connections established 1, dropped 0
          Last reset by us never, due to No error
          Last reset by peer never, due to No error

          Neighbor capabilities:
          Dynamic capability: advertised (mp, refresh, gr) received (mp, refresh, gr)
          Dynamic capability (old): advertised received
          Route refresh capability (new): advertised received 
          Route refresh capability (old): advertised received 
          4-Byte AS capability: disabled 
          Address family VPNv4 Unicast: advertised received 
          Address family VPNv6 Unicast: advertised received 
          Graceful Restart capability: advertised received

          Graceful Restart Parameters:
          Address families advertised to peer:
            VPNv4 Unicast  VPNv6 Unicast  
          Address families received from peer:
            VPNv4 Unicast  VPNv6 Unicast  
          Forwarding state preserved by peer for:
          Restart time advertised to peer: 240 seconds
          Stale time for routes advertised by peer: 600 seconds
          Restart time advertised by peer: 120 seconds

          Message statistics:
                                      Sent               Rcvd
          Opens:                         1                  1  
          Notifications:                 0                  0  
          Updates:                       6                  4  
          Keepalives:                  256                256  
          Route Refresh:                 0                  0  
          Capability:                    0                  0  
          Total:                       263                261  
          Total bytes:                5311               5139  
          Bytes in queue:                0                  0  

          For address family: VPNv4 Unicast
          BGP table version 11, neighbor version 11
          1 accepted paths consume 48 bytes of memory
          2 sent paths
          Community attribute sent to this neighbor
          Extended community attribute sent to this neighbor
          Third-party Nexthop will not be computed.
          Maximum prefixes allowed 300000
          Inbound route-map configured is genie_redistribution, handle obtained
          Outbound route-map configured is genie_redistribution, handle obtained

          For address family: VPNv6 Unicast
          BGP table version 10, neighbor version 10
          1 accepted paths consume 48 bytes of memory
          2 sent paths
          Community attribute sent to this neighbor
          Extended community attribute sent to this neighbor
          Third-party Nexthop will not be computed.

          Local host: 1.1.1.1, Local port: 57144
          Foreign host: 2.2.2.2, Foreign port: 179
          fd = 44

        BGP neighbor is 2.2.2.5,  remote AS 200, local AS 333, ebgp link,  Peer index 2
          Inherits session configuration from session-template PEER-SESSION
          Description: PEER-SESSION
          BGP version 4, remote router ID 0.0.0.0
          BGP state = Shut (Admin), down for 02:20:09
          Using loopback0 as update source for this peer
          Connected check is disabled
          BFD live-detection is configured
          External BGP peer might be upto 255 hops away
          TCP MD5 authentication is enabled
          Only passive connection setup allowed
          Last read never, hold time = 45, keepalive interval is 15 seconds
          Last written never, keepalive timer not running
          Received 0 messages, 0 notifications, 0 bytes in queue
          Sent 0 messages, 0 notifications, 0 bytes in queue
          Connections established 0, dropped 0
          Last reset by us never, due to No error
          Last reset by peer never, due to No error

          Message statistics:
                                      Sent               Rcvd
          Opens:                         0                  0  
          Notifications:                 0                  0  
          Updates:                       0                  0  
          Keepalives:                    0                  0  
          Route Refresh:                 0                  0  
          Capability:                    0                  0  
          Total:                         0                  0  
          Total bytes:                   0                  0  
          Bytes in queue:                0                  0  

          For address family: IPv4 Unicast
          BGP table version 2, neighbor version 0
          0 accepted paths consume 0 bytes of memory
          0 sent paths
          Inbound soft reconfiguration allowed
          Community attribute sent to this neighbor
          Extended community attribute sent to this neighbor
          Nexthop always set to local peering address, 0.0.0.0
          Maximum prefixes allowed 300
          Allow my ASN 9 times
          ASN override is enabled
          Inbound route-map configured is test-map, handle obtained
          Outbound route-map configured is test-map, handle obtained
          Default information originate, default not sent
          Inherited policy-templates:
            Preference    Name                
                    10    PEER-POLICY                                                 
                    20    PEER-POLICY2                                                

          No established BGP session with peer

        BGP neighbor is 2.2.2.25,  remote AS 0, unknown link,  Peer index 3
          BGP version 4, remote router ID 0.0.0.0
          BGP state = Idle, down for 02:20:08, retry in 0.000000
          No address family configured
          Last read never, hold time = 45, keepalive interval is 15 seconds
          Last written never, keepalive timer not running
          Received 0 messages, 0 notifications, 0 bytes in queue
          Sent 0 messages, 0 notifications, 0 bytes in queue
          Connections established 0, dropped 0
          Connection attempts 0
          Last reset by us never, due to No error
          Last reset by peer never, due to No error

          Message statistics:
                                      Sent               Rcvd
          Opens:                         0                  0  
          Notifications:                 0                  0  
          Updates:                       0                  0  
          Keepalives:                    0                  0  
          Route Refresh:                 0                  0  
          Capability:                    0                  0  
          Total:                         0                  0  
          Total bytes:                   0                  0  
          Bytes in queue:                0                  0  

          No established BGP session with peer
        '''}

    golden_parsed_output3 = {
        'neighbor':
            {'21.0.101.1':
                {'address_family':
                    {'ipv4 multicast':
                        {'bgp_table_version': 55,
                        'next_hop_self': False,
                        'path':
                            {'accepted_paths': 5,
                            'memory_usage': 660},
                        'route_reflector_client': True,
                        'neighbor_version': 55,
                        'send_community': True},
                    'ipv4 unicast':
                        {'bgp_table_version': 6765004,
                        'next_hop_self': False,
                        'path':
                            {'accepted_paths': 5,
                            'memory_usage': 660},
                        'route_reflector_client': True,
                        'neighbor_version': 6765004,
                        'send_community': True},
                    'ipv6 multicast':
                        {'bgp_table_version': 2,
                        'next_hop_self': False,
                        'path':
                            {'accepted_paths': 0,
                            'memory_usage': 0},
                        'route_reflector_client': True,
                        'neighbor_version': 0,
                        'send_community': True},
                    'ipv6 unicast':
                        {'bgp_table_version': 2,
                        'next_hop_self': False,
                        'path':
                            {'accepted_paths': 0,
                            'memory_usage': 0},
                        'route_reflector_client': True,
                        'neighbor_version': 0,
                        'send_community': True},
                    'vpnv4 unicast':
                        {'bgp_table_version': 12863408,
                        'next_hop_self': False,
                        'path':
                            {'accepted_paths': 0,
                            'memory_usage': 0},
                        'route_reflector_client': True,
                        'neighbor_version': 0,
                        'send_community': True},
                    'vpnv6 unicast':
                        {'bgp_table_version': 2,
                        'next_hop_self': False,
                        'path':
                            {'accepted_paths': 0,
                            'memory_usage': 0},
                        'route_reflector_client': True,
                        'neighbor_version': 0,
                        'send_community': True}},
                'bgp_negotiated_capabilities':
                    {'dynamic_capability': 'advertised '
                                           '(mp, '
                                           'refresh, '
                                           'gr) '
                                           'received '
                                           '(mp, '
                                           'refresh, '
                                           'gr)',
                    'dynamic_capability_old': 'advertised '
                                              'received',
                    'graceful_restart': 'advertised '
                                        'received',
                    'route_refresh': 'advertised '
                                     'received',
                    'route_refresh_old': 'advertised '
                                         'received',
                    'vpnv4_unicast': 'advertised',
                    'vpnv6_unicast': 'advertised'},
                'bgp_negotiated_keepalive_timers':
                    {'hold_time': 180,
                    'keepalive_interval': 60,
                    'keepalive_timer': 'expiry '
                                       'due '
                                       '00:00:14',
                    'last_read': '00:00:45',
                    'last_written': '00:00:45'},
                'bgp_neighbor_counters':
                    {'messages':
                        {'received':
                            {'bytes_in_queue': 0,
                            'capability': 17,
                            'keepalives': 17,
                            'notifications': 0,
                            'opens': 5,
                            'route_refresh': 0,
                            'total': 67,
                            'total_bytes': 2261,
                            'updates': 28},
                        'sent':
                            {'bytes_in_queue': 0,
                            'capability': 17,
                            'keepalives': 17,
                            'notifications': 0,
                            'opens': 5,
                            'route_refresh': 0,
                            'total': 50,
                            'total_bytes': 1940,
                            'updates': 23}}},
                'bgp_session_transport':
                    {'connection':
                        {'dropped': 4,
                        'established': 5,
                        'last_reset': 'never',
                        'reset_by': 'us',
                        'reset_reason': 'no '
                        'error'},
                    'transport':
                        {'fd': '81',
                        'foreign_host': '21.0.101.1',
                        'foreign_port': '179',
                        'local_host': '21.0.0.2',
                        'local_port': '55337'}},
                'bgp_version': 4,
                'graceful_restart_paramters':
                    {'restart_time_advertised_by_peer_seconds': 120,
                    'restart_time_advertised_to_peer_seconds': 120,
                    'stale_time_advertised_by_peer_seconds': 300},
                'link': 'ibgp',
                'local_as': 'None',
                'peer_index': 6,
                'received_bytes_queue': 0,
                'received_messages': 67,
                'received_notifications': 0,
                'remote_as': 333,
                'retry_time': 'None',
                'router_id': '21.0.101.1',
                'session_state': 'Established',
                'shutdown': False,
                'up_time': '00:07:46'},
            '21.0.102.1':
                {'address_family':
                    {'ipv4 multicast':
                        {'bgp_table_version': 55,
                        'next_hop_self': False,
                        'path':
                            {'accepted_paths': 0,
                            'memory_usage': 0},
                        'route_reflector_client': True,
                        'neighbor_version': 0,
                        'send_community': True},
                    'ipv4 unicast':
                        {'bgp_table_version': 6765004,
                        'next_hop_self': False,
                        'path':
                            {'accepted_paths': 0,
                            'memory_usage': 0},
                        'route_reflector_client': True,
                        'neighbor_version': 0,
                        'send_community': True},
                    'ipv6 multicast':
                        {'bgp_table_version': 2,
                        'next_hop_self': False,
                        'path':
                            {'accepted_paths': 0,
                            'memory_usage': 0},
                        'route_reflector_client': True,
                        'neighbor_version': 0,
                        'send_community': True},
                    'ipv6 unicast':
                        {'bgp_table_version': 2,
                        'next_hop_self': False,
                        'path':
                            {'accepted_paths': 0,
                            'memory_usage': 0},
                        'route_reflector_client': True,
                        'neighbor_version': 0,
                        'send_community': True},
                    'vpnv4 unicast':
                        {'bgp_table_version': 12863408,
                        'next_hop_self': False,
                        'path':
                            {'accepted_paths': 0,
                            'memory_usage': 0},
                        'neighbor_version': 0,
                        'send_community': True},
                    'vpnv6 unicast':
                        {'bgp_table_version': 2,
                        'next_hop_self': False,
                        'path':
                            {'accepted_paths': 0,
                            'memory_usage': 0},
                        'route_reflector_client': True,
                        'neighbor_version': 0,
                        'send_community': True}},
                'bgp_negotiated_keepalive_timers':
                    {'hold_time': 180,
                    'keepalive_interval': 60,
                    'keepalive_timer': 'not '
                    'running',
                    'last_read': 'never',
                    'last_written': 'never'},
                'bgp_neighbor_counters':
                    {'messages':
                        {'received':
                            {'bytes_in_queue': 0,
                            'capability': 0,
                            'keepalives': 0,
                            'notifications': 0,
                            'opens': 0,
                            'route_refresh': 0,
                            'total': 0,
                            'total_bytes': 0,
                            'updates': 0},
                        'sent':
                            {'bytes_in_queue': 0,
                            'capability': 0,
                            'keepalives': 0,
                            'notifications': 0,
                            'opens': 0,
                            'route_refresh': 0,
                            'total': 0,
                            'total_bytes': 0,
                            'updates': 0}}},
                'bgp_session_transport':
                    {'connection':
                        {'dropped': 0,
                        'established': 0,
                        'last_reset': 'never',
                        'reset_by': 'peer',
                        'reset_reason': 'no '
                        'error'}},
                'bgp_version': 4,
                'link': 'ibgp',
                'local_as': 'None',
                'peer_index': 7,
                'received_bytes_queue': 0,
                'received_messages': 0,
                'received_notifications': 0,
                'remote_as': 333,
                'retry_time': '00:00:55',
                'router_id': '0.0.0.0',
                'session_state': 'Idle',
                'shutdown': False,
                'up_time': '01:27:53'},
            '21.0.201.1':
                {'address_family':
                    {'ipv4 multicast':
                        {'bgp_table_version': 55,
                        'neighbor_version': 0,
                        'path':
                            {'accepted_paths': 0,
                            'memory_usage': 0},
                        'send_community': True},
                    'ipv4 unicast':
                        {'bgp_table_version': 6765004,
                        'neighbor_version': 0,
                        'path':
                            {'accepted_paths': 0,
                            'memory_usage': 0},
                        'send_community': True},
                    'ipv6 multicast':
                        {'bgp_table_version': 2,
                        'neighbor_version': 0,
                        'path':
                            {'accepted_paths': 0,
                            'memory_usage': 0},
                        'send_community': True},
                    'ipv6 unicast':
                        {'bgp_table_version': 2,
                        'neighbor_version': 0,
                        'path':
                            {'accepted_paths': 0,
                            'memory_usage': 0},
                        'send_community': True},
                    'vpnv4 unicast':
                        {'bgp_table_version': 12863408,
                        'neighbor_version': 0,
                        'path':
                            {'accepted_paths': 0,
                            'memory_usage': 0},
                        'send_community': True},
                    'vpnv6 unicast':
                        {'bgp_table_version': 2,
                        'neighbor_version': 0,
                        'path':
                            {'accepted_paths': 0,
                           'memory_usage': 0},
                        'send_community': True}},
                'bgp_negotiated_keepalive_timers':
                    {'hold_time': 180,
                    'keepalive_interval': 60,
                    'keepalive_timer': 'not '
                                    'running',
                    'last_read': 'never',
                    'last_written': 'never'},
                'bgp_neighbor_counters':
                    {'messages':
                        {'received':
                            {'bytes_in_queue': 0,
                            'capability': 0,
                            'keepalives': 0,
                            'notifications': 0,
                            'opens': 0,
                            'route_refresh': 0,
                            'total': 0,
                            'total_bytes': 0,
                            'updates': 0},
                        'sent':
                            {'bytes_in_queue': 0,
                            'capability': 0,
                            'keepalives': 0,
                            'notifications': 0,
                            'opens': 0,
                            'route_refresh': 0,
                            'total': 0,
                            'total_bytes': 0,
                            'updates': 0}}},
                'bgp_session_transport':
                    {'connection':
                        {'dropped': 0,
                        'established': 0,
                        'last_reset': 'never',
                        'reset_by': 'peer',
                        'reset_reason': 'no '
                                        'error'}},
                'bgp_version': 4,
                'link': 'ebgp',
                'local_as': 'None',
                'peer_index': 8,
                'received_bytes_queue': 0,
                'received_messages': 0,
                'received_notifications': 0,
                'remote_as': 888,
                'retry_time': '00:01:12',
                'router_id': '0.0.0.0',
                'session_state': 'Idle',
                'shutdown': False,
                'up_time': '01:27:52'},
            '4.4.4.4':
                {'bgp_negotiated_keepalive_timers':
                    {'hold_time': 180,
                    'keepalive_interval': 60,
                    'keepalive_timer': 'not '
                    'running',
                    'last_read': 'never',
                    'last_written': 'never'},
                'bgp_neighbor_counters':
                    {'messages':
                        {'received':
                            {'bytes_in_queue': 0,
                            'capability': 0,
                            'keepalives': 0,
                            'notifications': 0,
                            'opens': 0,
                            'route_refresh': 0,
                            'total': 0,
                            'total_bytes': 0,
                            'updates': 0},
                        'sent':
                            {'bytes_in_queue': 0,
                            'capability': 0,
                            'keepalives': 0,
                            'notifications': 0,
                            'opens': 0,
                            'route_refresh': 0,
                            'total': 0,
                            'total_bytes': 0,
                            'updates': 0}}},
                'bgp_session_transport':
                    {'connection':
                        {'dropped': 0,
                        'established': 0,
                        'last_reset': 'never',
                        'reset_by': 'peer',
                        'reset_reason': 'no '
                        'error'}},
                'bgp_version': 4,
                'link': 'unknown',
                'local_as': 'None',
                'peer_index': 5,
                'received_bytes_queue': 0,
                'received_messages': 0,
                'received_notifications': 0,
                'remote_as': 0,
                'retry_time': '0.000000',
                'router_id': '0.0.0.0',
                'session_state': 'Idle',
                'shutdown': False,
                'up_time': '01:27:54'},
            'fec1::1002':
                {'address_family':
                    {'ipv4 unicast':
                        {'bgp_table_version': 6765004,
                        'neighbor_version': 6765004,
                        'next_hop_self': False,
                        'path':
                            {'accepted_paths': 5,
                            'memory_usage': 660},
                        'route_reflector_client': True,
                        'send_community': True}},
                'bgp_negotiated_capabilities':
                    {'dynamic_capability': 'advertised '
                                            '(mp, '
                                            'refresh, '
                                            'gr) '
                                            'received '
                                            '(mp, '
                                            'refresh, '
                                            'gr)',
                    'dynamic_capability_old': 'advertised '
                                              'received',
                    'graceful_restart': 'advertised '
                                        'received',
                    'route_refresh': 'advertised '
                                     'received',
                    'route_refresh_old': 'advertised '
                                         'received'},
                'bgp_negotiated_keepalive_timers':
                    {'hold_time': 180,
                    'keepalive_interval': 60,
                    'keepalive_timer': 'expiry '
                                       'due '
                                       '00:00:20',
                    'last_read': '00:00:39',
                    'last_written': '00:00:39'},
                'bgp_neighbor_counters':
                    {'messages':
                        {'received':
                            {'bytes_in_queue': 0,
                            'capability': 6,
                            'keepalives': 17,
                            'notifications': 0,
                            'opens': 5,
                            'route_refresh': 0,
                            'total': 43,
                            'total_bytes': 1420,
                            'updates': 15},
                        'sent':
                            {'bytes_in_queue': 0,
                            'capability': 6,
                            'keepalives': 17,
                            'notifications': 0,
                            'opens': 5,
                            'route_refresh': 0,
                            'total': 33,
                            'total_bytes': 1739,
                            'updates': 20}}},
                'bgp_session_transport':
                    {'connection':
                        {'dropped': 4,
                        'established': 5,
                        'last_reset': 'never',
                        'reset_by': 'us',
                        'reset_reason': 'no '
                        'error'},
                    'transport':
                        {'fd': '88'}},
                'bgp_version': 4,
                'graceful_restart_paramters':
                    {'restart_time_advertised_by_peer_seconds': 120,
                    'restart_time_advertised_to_peer_seconds': 120,
                    'stale_time_advertised_by_peer_seconds': 300},
                'link': 'ibgp',
                'local_as': 'None',
                'peer_index': 3,
                'received_bytes_queue': 0,
                'received_messages': 43,
                'received_notifications': 0,
                'remote_as': 333,
                'retry_time': 'None',
                'router_id': '21.0.101.1',
                'session_state': 'Established',
                'shutdown': False,
                'up_time': '00:07:40'},
            'fec1::2002':
                {'address_family':
                    {'ipv4 unicast':
                        {'bgp_table_version': 6765004,
                        'neighbor_version': 0,
                        'path':
                            {'accepted_paths': 0,
                            'memory_usage': 0},
                        'send_community': True},
                    'ipv6 multicast':
                        {'bgp_table_version': 2,
                        'neighbor_version': 0,
                        'path':
                            {'accepted_paths': 0,
                            'memory_usage': 0},
                        'send_community': True},
                    'ipv6 unicast':
                        {'bgp_table_version': 2,
                        'neighbor_version': 0,
                        'path':
                            {'accepted_paths': 0,
                            'memory_usage': 0},
                        'send_community': True}},
                'bgp_negotiated_keepalive_timers':
                    {'hold_time': 180,
                    'keepalive_interval': 60,
                    'keepalive_timer': 'not '
                    'running',
                    'last_read': 'never',
                    'last_written': 'never'},
                'bgp_neighbor_counters':
                    {'messages':
                        {'received':
                            {'bytes_in_queue': 0,
                            'capability': 0,
                            'keepalives': 0,
                            'notifications': 0,
                            'opens': 0,
                            'route_refresh': 0,
                            'total': 0,
                            'total_bytes': 0,
                            'updates': 0},
                        'sent':
                            {'bytes_in_queue': 0,
                            'capability': 0,
                            'keepalives': 0,
                            'notifications': 0,
                            'opens': 0,
                            'route_refresh': 0,
                            'total': 0,
                            'total_bytes': 0,
                            'updates': 0}}},
                'bgp_session_transport':
                    {'connection':
                        {'dropped': 0,
                        'established': 0,
                        'last_reset': 'never',
                        'reset_by': 'peer',
                        'reset_reason': 'no '
                        'error'}},
                'bgp_version': 4,
                'link': 'ebgp',
                'local_as': 'None',
                'peer_index': 4,
                'received_bytes_queue': 0,
                'received_messages': 0,
                'received_notifications': 0,
                'remote_as': 888,
                'retry_time': '00:00:29',
                'router_id': '0.0.0.0',
                'session_state': 'Idle',
                'shutdown': False,
                'up_time': '01:27:55'}}}

    golden_output3 = {'execute.return_value': '''
        BGP neighbor is 4.4.4.4, remote AS 0, unknown link, Peer index 5
          BGP version 4, remote router ID 0.0.0.0
          BGP state = Idle, down for 01:27:54, retry in 0.000000
          No address family configured
          Last read never, hold time = 180, keepalive interval is 60 seconds
          Last written never, keepalive timer not running
          Received 0 messages, 0 notifications, 0 bytes in queue
          Sent 0 messages, 0 notifications, 0(0) bytes in queue
          Connections established 0, dropped 0
          Connection attempts 0
          Last reset by us never, due to No error
          Last reset by peer never, due to No error

          Message statistics:
                                      Sent               Rcvd
          Opens:                         0                  0  
          Notifications:                 0                  0  
          Updates:                       0                  0  
          Keepalives:                    0                  0  
          Route Refresh:                 0                  0  
          Capability:                    0                  0  
          Total:                         0                  0  
          Total bytes:                   0                  0  
          Bytes in queue:                0                  0  

          No established BGP session with peer

        BGP neighbor is 21.0.101.1, remote AS 333, ibgp link, Peer index 6
          BGP version 4, remote router ID 21.0.101.1
          BGP state = Established, up for 00:07:46
          Peer is directly attached, interface Ethernet1/1
          Last read 00:00:45, hold time = 180, keepalive interval is 60 seconds
          Last written 00:00:45, keepalive timer expiry due 00:00:14
          Received 67 messages, 0 notifications, 0 bytes in queue
          Sent 50 messages, 0 notifications, 0(0) bytes in queue
          Connections established 5, dropped 4
          Last reset by peer 00:12:43, due to session closed
          Last reset by us never, due to No error

          Neighbor capabilities:
          Dynamic capability: advertised (mp, refresh, gr) received (mp, refresh, gr)
          Dynamic capability (old): advertised received
          Route refresh capability (new): advertised received 
          Route refresh capability (old): advertised received 
          4-Byte AS capability: advertised received 
          Address family IPv4 Unicast: advertised received 
          Address family IPv4 Multicast: advertised received 
          Address family IPv6 Unicast: advertised 
          Address family IPv6 Multicast: advertised 
          Address family VPNv4 Unicast: advertised 
          Address family VPNv6 Unicast: advertised 
          Address family Link-State: advertised 
          Graceful Restart capability: advertised received

          Graceful Restart Parameters:
          Address families advertised to peer:
            IPv4 Unicast  IPv4 Multicast  IPv6 Unicast  IPv6 Multicast  VPNv4 Unicast  VPNv6 Unicast  Link-State  
          Address families received from peer:
            IPv4 Unicast  IPv4 Multicast  
          Forwarding state preserved by peer for:
          Restart time advertised to peer: 120 seconds
          Stale time for routes advertised by peer: 300 seconds
          Restart time advertised by peer: 120 seconds
          Extended Next Hop Encoding Capability: advertised received
          Receive IPv6 next hop encoding Capability for AF:
            IPv4 Unicast  

          Message statistics:
                                      Sent               Rcvd
          Opens:                         5                  5  
          Notifications:                 0                  0  
          Updates:                      23                 28  
          Keepalives:                   17                 17  
          Route Refresh:                 0                  0  
          Capability:                   17                 17  
          Total:                        50                 67  
          Total bytes:                1940               2261  
          Bytes in queue:                0                  0  

          For address family: IPv4 Unicast
          BGP table version 6765004, neighbor version 6765004
          5 accepted paths consume 660 bytes of memory
          Inbound soft reconfiguration allowed(always)
          Community attribute sent to this neighbor
          Extended community attribute sent to this neighbor
          Third-party Nexthop will not be computed.
          Route reflector client
          5 paths flushed from peer
          Last End-of-RIB received 00:00:01 after session start

          For address family: IPv4 Multicast
          BGP table version 55, neighbor version 55
          5 accepted paths consume 660 bytes of memory
          Inbound soft reconfiguration allowed(always)
          Community attribute sent to this neighbor
          Extended community attribute sent to this neighbor
          Third-party Nexthop will not be computed.
          Route reflector client
          5 paths flushed from peer
          Last End-of-RIB received 00:00:01 after session start

          For address family: IPv6 Unicast
          BGP table version 2, neighbor version 0
          0 accepted paths consume 0 bytes of memory
          Inbound soft reconfiguration allowed(always)
          Community attribute sent to this neighbor
          Extended community attribute sent to this neighbor
          Third-party Nexthop will not be computed.
          Route reflector client

          For address family: IPv6 Multicast
          BGP table version 2, neighbor version 0
          0 accepted paths consume 0 bytes of memory
          Inbound soft reconfiguration allowed(always)
          Community attribute sent to this neighbor
          Extended community attribute sent to this neighbor
          Third-party Nexthop will not be computed.
          Route reflector client

          For address family: VPNv4 Unicast
          BGP table version 12863408, neighbor version 0
          0 accepted paths consume 0 bytes of memory
          Community attribute sent to this neighbor
          Extended community attribute sent to this neighbor
          Third-party Nexthop will not be computed.
          Route reflector client

          For address family: VPNv6 Unicast
          BGP table version 2, neighbor version 0
          0 accepted paths consume 0 bytes of memory
          Community attribute sent to this neighbor
          Extended community attribute sent to this neighbor
          Third-party Nexthop will not be computed.
          Route reflector client

          For address family: Link-State
          BGP table version 2, neighbor version 0
          0 accepted paths consume 0 bytes of memory
          Community attribute sent to this neighbor
          Extended community attribute sent to this neighbor
          Third-party Nexthop will not be computed.
          Route reflector client

          Local host: 21.0.0.2, Local port: 55337
          Foreign host: 21.0.101.1, Foreign port: 179
          fd = 81

        BGP neighbor is 21.0.102.1, remote AS 333, ibgp link, Peer index 7
          BGP version 4, remote router ID 0.0.0.0
          BGP state = Idle, down for 01:27:53, retry in 00:00:55
          Peer is directly attached, interface Ethernet1/1
          Last read never, hold time = 180, keepalive interval is 60 seconds
          Last written never, keepalive timer not running
          Received 0 messages, 0 notifications, 0 bytes in queue
          Sent 0 messages, 0 notifications, 0(0) bytes in queue
          Connections established 0, dropped 0
          Connection attempts 69
          Last reset by us never, due to No error
          Last reset by peer never, due to No error

          Message statistics:
                                      Sent               Rcvd
          Opens:                         0                  0  
          Notifications:                 0                  0  
          Updates:                       0                  0  
          Keepalives:                    0                  0  
          Route Refresh:                 0                  0  
          Capability:                    0                  0  
          Total:                         0                  0  
          Total bytes:                   0                  0  
          Bytes in queue:                0                  0  

          For address family: IPv4 Unicast
          BGP table version 6765004, neighbor version 0
          0 accepted paths consume 0 bytes of memory
          Inbound soft reconfiguration allowed(always)
          Community attribute sent to this neighbor
          Extended community attribute sent to this neighbor
          Third-party Nexthop will not be computed.
          Route reflector client

          For address family: IPv4 Multicast
          BGP table version 55, neighbor version 0
          0 accepted paths consume 0 bytes of memory
          Inbound soft reconfiguration allowed(always)
          Community attribute sent to this neighbor
          Extended community attribute sent to this neighbor
          Third-party Nexthop will not be computed.
          Route reflector client

          For address family: IPv6 Unicast
          BGP table version 2, neighbor version 0
          0 accepted paths consume 0 bytes of memory
          Inbound soft reconfiguration allowed(always)
          Community attribute sent to this neighbor
          Extended community attribute sent to this neighbor
          Third-party Nexthop will not be computed.
          Route reflector client

          For address family: IPv6 Multicast
          BGP table version 2, neighbor version 0
          0 accepted paths consume 0 bytes of memory
          Inbound soft reconfiguration allowed(always)
          Community attribute sent to this neighbor
          Extended community attribute sent to this neighbor
          Third-party Nexthop will not be computed.
          Route reflector client

          For address family: VPNv4 Unicast
          BGP table version 12863408, neighbor version 0
          0 accepted paths consume 0 bytes of memory
          Community attribute sent to this neighbor
          Extended community attribute sent to this neighbor
          Third-party Nexthop will not be computed.

          For address family: VPNv6 Unicast
          BGP table version 2, neighbor version 0
          0 accepted paths consume 0 bytes of memory
          Community attribute sent to this neighbor
          Extended community attribute sent to this neighbor
          Third-party Nexthop will not be computed.
          Route reflector client

          For address family: Link-State
          BGP table version 2, neighbor version 0
          0 accepted paths consume 0 bytes of memory
          Community attribute sent to this neighbor
          Extended community attribute sent to this neighbor
          Third-party Nexthop will not be computed.
          Route reflector client

          No established BGP session with peer

        BGP neighbor is 21.0.201.1, remote AS 888, ebgp link, Peer index 8
          BGP version 4, remote router ID 0.0.0.0
          BGP state = Idle, down for 01:27:52, retry in 00:01:12
          Peer is directly attached, interface Ethernet1/1
          Last read never, hold time = 180, keepalive interval is 60 seconds
          Last written never, keepalive timer not running
          Received 0 messages, 0 notifications, 0 bytes in queue
          Sent 0 messages, 0 notifications, 0(0) bytes in queue
          Connections established 0, dropped 0
          Connection attempts 70
          Last reset by us never, due to No error
          Last reset by peer never, due to No error

          Message statistics:
                                      Sent               Rcvd
          Opens:                         0                  0  
          Notifications:                 0                  0  
          Updates:                       0                  0  
          Keepalives:                    0                  0  
          Route Refresh:                 0                  0  
          Capability:                    0                  0  
          Total:                         0                  0  
          Total bytes:                   0                  0  
          Bytes in queue:                0                  0  

          For address family: IPv4 Unicast
          BGP table version 6765004, neighbor version 0
          0 accepted paths consume 0 bytes of memory
          Inbound soft reconfiguration allowed(always)
          Community attribute sent to this neighbor
          Extended community attribute sent to this neighbor

          For address family: IPv4 Multicast
          BGP table version 55, neighbor version 0
          0 accepted paths consume 0 bytes of memory
          Inbound soft reconfiguration allowed(always)
          Community attribute sent to this neighbor
          Extended community attribute sent to this neighbor

          For address family: IPv6 Unicast
          BGP table version 2, neighbor version 0
          0 accepted paths consume 0 bytes of memory
          Inbound soft reconfiguration allowed(always)
          Community attribute sent to this neighbor
          Extended community attribute sent to this neighbor

          For address family: IPv6 Multicast
          BGP table version 2, neighbor version 0
          0 accepted paths consume 0 bytes of memory
          Inbound soft reconfiguration allowed(always)
          Community attribute sent to this neighbor
          Extended community attribute sent to this neighbor

          For address family: VPNv4 Unicast
          BGP table version 12863408, neighbor version 0
          0 accepted paths consume 0 bytes of memory
          Community attribute sent to this neighbor
          Extended community attribute sent to this neighbor

          For address family: VPNv6 Unicast
          BGP table version 2, neighbor version 0
          0 accepted paths consume 0 bytes of memory
          Community attribute sent to this neighbor
          Extended community attribute sent to this neighbor

          For address family: Link-State
          BGP table version 2, neighbor version 0
          0 accepted paths consume 0 bytes of memory
          Community attribute sent to this neighbor
          Extended community attribute sent to this neighbor

          No established BGP session with peer

        BGP neighbor is fec1::1002, remote AS 333, ibgp link, Peer index 3
          BGP version 4, remote router ID 21.0.101.1
          BGP state = Established, up for 00:07:40
          Peer is directly attached, interface Ethernet1/1
          Last read 00:00:39, hold time = 180, keepalive interval is 60 seconds
          Last written 00:00:39, keepalive timer expiry due 00:00:20
          Received 43 messages, 0 notifications, 0 bytes in queue
          Sent 33 messages, 0 notifications, 0(0) bytes in queue
          Connections established 5, dropped 4
          Last reset by peer 00:12:43, due to session closed
          Last reset by us never, due to No error

          Neighbor capabilities:
          Dynamic capability: advertised (mp, refresh, gr) received (mp, refresh, gr)
          Dynamic capability (old): advertised received
          Route refresh capability (new): advertised received 
          Route refresh capability (old): advertised received 
          4-Byte AS capability: advertised received 
          Address family IPv4 Unicast: advertised received 
          Graceful Restart capability: advertised received

          Graceful Restart Parameters:
          Address families advertised to peer:
            IPv4 Unicast  
          Address families received from peer:
            IPv4 Unicast  
          Forwarding state preserved by peer for:
          Restart time advertised to peer: 120 seconds
          Stale time for routes advertised by peer: 300 seconds
          Restart time advertised by peer: 120 seconds
          Extended Next Hop Encoding Capability: advertised received
          Receive IPv6 next hop encoding Capability for AF:
            IPv4 Unicast  

          Message statistics:
                                      Sent               Rcvd
          Opens:                         5                  5  
          Notifications:                 0                  0  
          Updates:                      20                 15  
          Keepalives:                   17                 17  
          Route Refresh:                 0                  0  
          Capability:                    6                  6  
          Total:                        33                 43  
          Total bytes:                1739               1420  
          Bytes in queue:                0                  0  

          For address family: IPv4 Unicast
          BGP table version 6765004, neighbor version 6765004
          5 accepted paths consume 660 bytes of memory
          Inbound soft reconfiguration allowed(always)
          Community attribute sent to this neighbor
          Extended community attribute sent to this neighbor
          Third-party Nexthop will not be computed.
          Route reflector client
          5 paths flushed from peer
          Last End-of-RIB received 00:00:01 after session start

          Local host: fec1::112, Local port: 179
          Foreign host: fec1::1002, Foreign port: 29470
          fd = 88

        BGP neighbor is fec1::2002, remote AS 888, ebgp link, Peer index 4
          BGP version 4, remote router ID 0.0.0.0
          BGP state = Idle, down for 01:27:55, retry in 00:00:29
          Peer is directly attached, interface Ethernet1/1
          Last read never, hold time = 180, keepalive interval is 60 seconds
          Last written never, keepalive timer not running
          Received 0 messages, 0 notifications, 0 bytes in queue
          Sent 0 messages, 0 notifications, 0(0) bytes in queue
          Connections established 0, dropped 0
          Connection attempts 68
          Last reset by us never, due to No error
          Last reset by peer never, due to No error

          Message statistics:
                                      Sent               Rcvd
          Opens:                         0                  0  
          Notifications:                 0                  0  
          Updates:                       0                  0  
          Keepalives:                    0                  0  
          Route Refresh:                 0                  0  
          Capability:                    0                  0  
          Total:                         0                  0  
          Total bytes:                   0                  0  
          Bytes in queue:                0                  0  

          For address family: IPv4 Unicast
          BGP table version 6765004, neighbor version 0
          0 accepted paths consume 0 bytes of memory
          Inbound soft reconfiguration allowed(always)
          Community attribute sent to this neighbor
          Extended community attribute sent to this neighbor

          For address family: IPv6 Unicast
          BGP table version 2, neighbor version 0
          0 accepted paths consume 0 bytes of memory
          Inbound soft reconfiguration allowed(always)
          Community attribute sent to this neighbor
          Extended community attribute sent to this neighbor

          For address family: IPv6 Multicast
          BGP table version 2, neighbor version 0
          0 accepted paths consume 0 bytes of memory
          Inbound soft reconfiguration allowed(always)
          Community attribute sent to this neighbor
          Extended community attribute sent to this neighbor

          For address family: Link-State
          BGP table version 2, neighbor version 0
          0 accepted paths consume 0 bytes of memory
          Community attribute sent to this neighbor
          Extended community attribute sent to this neighbor

          No established BGP session with peer
        '''}

    def test_show_bgp_vrf_VRF1_all_neighbors_golden1(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output1)
        obj = ShowBgpVrfAllNeighbors(device=self.device)
        parsed_output = obj.parse(vrf='VRF1')
        self.assertEqual(parsed_output,self.golden_parsed_output1)

    def test_show_bgp_vrf_default_all_neighbors_golden2(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output2)
        obj = ShowBgpVrfAllNeighbors(device=self.device)
        parsed_output = obj.parse(vrf='default')
        self.assertEqual(parsed_output,self.golden_parsed_output2)

    def test_show_bgp_vrf_default_all_neighbors_golden3(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output3)
        obj = ShowBgpVrfAllNeighbors(device=self.device)
        parsed_output = obj.parse(vrf='default')
        self.assertEqual(parsed_output,self.golden_parsed_output3)

    def test_show_bgp_vrf_default_all_neighbors_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowBgpVrfAllNeighbors(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse(vrf='default')

class test_show_bgp_vrf_all_neighbors_yang(unittest.TestCase):

    '''Unit test for show vrf all neighbors - YANG'''
    
    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output = {
        'neighbor': 
            {'21.0.101.1': 
                {'address_family': 
                    {'ipv4 unicast': 
                        {'enabled': True,
                        'graceful_restart': False,
                        'ipv4_unicast_send_default_route': False},
                    'ipv6 unicast': 
                        {'enabled': True,
                        'graceful_restart': False},
                    'l3vpn ipv4 unicast': 
                        {'enabled': True,
                        'graceful_restart': False},
                    'l3vpn ipv6 unicast': 
                        {'enabled': True,
                        'graceful_restart': False}},
                'allow_own_as': 0,
                'bgp_session_transport': 
                    {'transport': 
                        {'foreign_host': 'unspecified',
                        'foreign_port': '21.0.101.1',
                        'local_host': '0.0.0.0',
                        'local_port': 'unspecified',
                        'passive_mode': 'false'}},
                'description': 'None',
                'ebgp_multihop': False,
                'ebgp_multihop_max_hop': 0,
                'graceful_restart': False,
                'graceful_restart_helper_only': False,
                'graceful_restart_restart_time': 120,
                'graceful_restart_stalepath_time': 300,
                'holdtime': 180,
                'keepalive_interval': 60,
                'link': 'ebgp',
                'minimum_advertisement_interval': 0,
                'peer_group': 'None',
                'remote_as': 333,
                'remove_private_as': False,
                'route_reflector_client': True,
                'route_reflector_cluster_id': 3,
                'send_community': 'BOTH'},
            '21.0.102.1': 
                {'address_family': 
                    {'ipv4 unicast': 
                        {'enabled': True,
                        'graceful_restart': False},
                    'ipv6 unicast': 
                        {'enabled': True,
                        'graceful_restart': False},
                    'l3vpn ipv4 unicast': 
                        {'enabled': True,
                        'graceful_restart': False},
                    'l3vpn ipv6 unicast': 
                        {'enabled': True,
                        'graceful_restart': False}},
                'allow_own_as': 0,
                'bgp_session_transport': 
                    {'transport': 
                        {'foreign_host': 'unspecified',
                        'foreign_port': '21.0.102.1',
                        'local_host': '0.0.0.0',
                        'local_port': 'unspecified',
                        'passive_mode': 'false'}},
                'description': 'None',
                'ebgp_multihop': False,
                'ebgp_multihop_max_hop': 0,
                'graceful_restart': False,
                'graceful_restart_helper_only': False,
                'graceful_restart_restart_time': 120,
                'graceful_restart_stalepath_time': 300,
                'holdtime': 180,
                'keepalive_interval': 60,
                'link': 'ebgp',
                'minimum_advertisement_interval': 0,
                'peer_group': 'None',
                'remote_as': 333,
                'remove_private_as': False,
                'route_reflector_client': True,
                'route_reflector_cluster_id': 3,
                'send_community': 'BOTH'},
            '21.0.201.1': 
                {'address_family': 
                    {'ipv4 unicast': 
                        {'enabled': True,
                        'graceful_restart': False,
                        'ipv4_unicast_send_default_route': False},
                    'ipv6 unicast': 
                        {'enabled': True,
                        'graceful_restart': False,
                        'ipv6_unicast_send_default_route': False},
                    'l3vpn ipv4 unicast': 
                        {'enabled': True,
                        'graceful_restart': False},
                    'l3vpn ipv6 unicast': 
                        {'enabled': True,
                        'graceful_restart': False}},
                'allow_own_as': 0,
                'bgp_session_transport': 
                    {'transport': 
                        {'foreign_host': 'unspecified',
                        'foreign_port': '21.0.201.1',
                        'local_host': '0.0.0.0',
                        'local_port': 'unspecified',
                        'passive_mode': 'false'}},
                'description': 'None',
                'ebgp_multihop': False,
                'ebgp_multihop_max_hop': 0,
                'graceful_restart': False,
                'graceful_restart_helper_only': False,
                'graceful_restart_restart_time': 120,
                'graceful_restart_stalepath_time': 300,
                'holdtime': 180,
                'keepalive_interval': 60,
                'link': 'ebgp',
                'minimum_advertisement_interval': 0,
                'peer_group': 'None',
                'remote_as': 888,
                'remove_private_as': False,
                'route_reflector_client': False,
                'route_reflector_cluster_id': 3,
                'send_community': 'BOTH'},
            '4.4.4.4': 
                {'bgp_session_transport': 
                    {'transport': 
                        {'foreign_host': 'unspecified',
                        'foreign_port': '4.4.4.4',
                        'local_host': '0.0.0.0',
                        'local_port': 'unspecified',
                        'passive_mode': 'false'}},
                'description': 'None',
                'ebgp_multihop': False,
                'ebgp_multihop_max_hop': 0,
                'graceful_restart': False,
                'graceful_restart_helper_only': False,
                'graceful_restart_restart_time': 120,
                'graceful_restart_stalepath_time': 300,
                'holdtime': 180,
                'keepalive_interval': 60,
                'link': 'ebgp',
                'peer_group': 'None',
                'remove_private_as': False,
                'route_reflector_cluster_id': 3},
            'fec1::1002':  
                {'address_family': 
                    {'ipv4 unicast': 
                        {'enabled': True,
                        'graceful_restart': False,
                        'ipv4_unicast_send_default_route': False}},
                'allow_own_as': 0,
                'bgp_session_transport': 
                    {'transport': 
                        {'foreign_host': 'unspecified',
                        'foreign_port': 'fec1::1002',
                        'local_host': '::',
                        'local_port': 'unspecified',
                        'passive_mode': 'false'}},
                'description': 'None',
                'ebgp_multihop': False,
                'ebgp_multihop_max_hop': 0,
                'graceful_restart': False,
                'graceful_restart_helper_only': False,
                'graceful_restart_restart_time': 120,
                'graceful_restart_stalepath_time': 300,
                'holdtime': 180,
                'keepalive_interval': 60,
                'link': 'ebgp',
                'minimum_advertisement_interval': 0,
                'peer_group': 'None',
                'remote_as': 333,
                'remove_private_as': False,
                'route_reflector_client': True,
                'route_reflector_cluster_id': 3,
                'send_community': 'BOTH'},
            'fec1::2002': 
                {'address_family': 
                    {'ipv4 unicast': 
                        {'enabled': True,
                        'graceful_restart': False,
                        'ipv4_unicast_send_default_route': False},
                    'ipv6 unicast': 
                        {'enabled': True,
                        'graceful_restart': False,
                        'ipv6_unicast_send_default_route': False}},
                'allow_own_as': 0,
                'bgp_session_transport': 
                    {'transport': 
                        {'foreign_host': 'unspecified',
                        'foreign_port': 'fec1::2002',
                        'local_host': '::',
                        'local_port': 'unspecified',
                        'passive_mode': 'false'}},
                'description': 'None',
                'ebgp_multihop': False,
                'ebgp_multihop_max_hop': 0,
                'graceful_restart': False,
                'graceful_restart_helper_only': False,
                'graceful_restart_restart_time': 120,
                'graceful_restart_stalepath_time': 300,
                'holdtime': 180,
                'keepalive_interval': 60,
                'link': 'ebgp',
                'minimum_advertisement_interval': 0,
                'peer_group': 'None',
                'remote_as': 888,
                'remove_private_as': False,
                'route_reflector_client': False,
                'route_reflector_cluster_id': 3,
                'send_community': 'BOTH'}}}

    class etree_holder():
        def __init__(self):
            self.data = ET.fromstring('''
                <rpc-reply xmlns="urn:ietf:params:xml:ns:netconf:base:1.0" message-id="101">
                    <data>
                        <bgp xmlns="http://openconfig.net/yang/bgp">
                            <global>
                                <afi-safis>
                                    <afi-safi xmlns="http://openconfig.net/yang/bgp-multiprotocol">
                                        <afi-safi-name>none</afi-safi-name>
                                        <config>
                                            <afi-safi-name>none</afi-safi-name>
                                        </config>
                                        <graceful-restart>
                                            <state>
                                                <enabled>false</enabled>
                                            </state>
                                        </graceful-restart>
                                        <state>
                                            <afi-safi-name>none</afi-safi-name>
                                            <enabled>true</enabled>
                                        </state>
                                        <route-selection-options>
                                            <config>
                                                <advertise-inactive-routes>false</advertise-inactive-routes>
                                            </config>
                                            <state>
                                                <advertise-inactive-routes>false</advertise-inactive-routes>
                                            </state>
                                        </route-selection-options>
                                        <use-multiple-paths>
                                            <ebgp>
                                                <config>
                                                    <maximum-paths>1</maximum-paths>
                                                </config>
                                                <state>
                                                    <maximum-paths>1</maximum-paths>
                                                </state>
                                            </ebgp>
                                            <ibgp>
                                                <config>
                                                    <maximum-paths>1</maximum-paths>
                                                </config>
                                                <state>
                                                    <maximum-paths>1</maximum-paths>
                                                </state>
                                            </ibgp>
                                        </use-multiple-paths>
                                    </afi-safi>
                                    <afi-safi xmlns="http://openconfig.net/yang/bgp-multiprotocol">
                                        <afi-safi-name>none</afi-safi-name>
                                        <config>
                                            <afi-safi-name>none</afi-safi-name>
                                        </config>
                                        <graceful-restart>
                                            <state>
                                                <enabled>false</enabled>
                                            </state>
                                        </graceful-restart>
                                        <state>
                                            <afi-safi-name>none</afi-safi-name>
                                            <enabled>true</enabled>
                                        </state>
                                        <route-selection-options>
                                            <config>
                                                <advertise-inactive-routes>false</advertise-inactive-routes>
                                            </config>
                                            <state>
                                                <advertise-inactive-routes>false</advertise-inactive-routes>
                                            </state>
                                        </route-selection-options>
                                        <use-multiple-paths>
                                            <ebgp>
                                                <config>
                                                    <maximum-paths>1</maximum-paths>
                                                </config>
                                                <state>
                                                    <maximum-paths>1</maximum-paths>
                                                </state>
                                            </ebgp>
                                            <ibgp>
                                                <config>
                                                    <maximum-paths>1</maximum-paths>
                                                </config>
                                                <state>
                                                    <maximum-paths>1</maximum-paths>
                                                </state>
                                            </ibgp>
                                        </use-multiple-paths>
                                    </afi-safi>
                                    <afi-safi xmlns="http://openconfig.net/yang/bgp-multiprotocol">
                                        <afi-safi-name>L3VPN_IPV6_UNICAST</afi-safi-name>
                                        <config>
                                            <afi-safi-name>L3VPN_IPV6_UNICAST</afi-safi-name>
                                        </config>
                                        <graceful-restart>
                                            <state>
                                                <enabled>false</enabled>
                                            </state>
                                        </graceful-restart>
                                        <state>
                                            <afi-safi-name>L3VPN_IPV6_UNICAST</afi-safi-name>
                                            <enabled>true</enabled>
                                        </state>
                                        <route-selection-options>
                                            <config>
                                                <advertise-inactive-routes>false</advertise-inactive-routes>
                                            </config>
                                            <state>
                                                <advertise-inactive-routes>false</advertise-inactive-routes>
                                            </state>
                                        </route-selection-options>
                                        <use-multiple-paths>
                                            <ebgp>
                                                <config>
                                                    <maximum-paths>1</maximum-paths>
                                                </config>
                                                <state>
                                                    <maximum-paths>1</maximum-paths>
                                                </state>
                                            </ebgp>
                                            <ibgp>
                                                <config>
                                                    <maximum-paths>1</maximum-paths>
                                                </config>
                                                <state>
                                                    <maximum-paths>1</maximum-paths>
                                                </state>
                                            </ibgp>
                                        </use-multiple-paths>
                                    </afi-safi>
                                    <afi-safi xmlns="http://openconfig.net/yang/bgp-multiprotocol">
                                        <afi-safi-name>L3VPN_IPV4_UNICAST</afi-safi-name>
                                        <config>
                                            <afi-safi-name>L3VPN_IPV4_UNICAST</afi-safi-name>
                                        </config>
                                        <graceful-restart>
                                            <state>
                                                <enabled>false</enabled>
                                            </state>
                                        </graceful-restart>
                                        <state>
                                            <afi-safi-name>L3VPN_IPV4_UNICAST</afi-safi-name>
                                            <enabled>true</enabled>
                                        </state>
                                        <route-selection-options>
                                            <config>
                                                <advertise-inactive-routes>false</advertise-inactive-routes>
                                            </config>
                                            <state>
                                                <advertise-inactive-routes>false</advertise-inactive-routes>
                                            </state>
                                        </route-selection-options>
                                        <use-multiple-paths>
                                            <ebgp>
                                                <config>
                                                    <maximum-paths>1</maximum-paths>
                                                </config>
                                                <state>
                                                    <maximum-paths>1</maximum-paths>
                                                </state>
                                            </ebgp>
                                            <ibgp>
                                                <config>
                                                    <maximum-paths>1</maximum-paths>
                                                </config>
                                                <state>
                                                    <maximum-paths>1</maximum-paths>
                                                </state>
                                            </ibgp>
                                        </use-multiple-paths>
                                    </afi-safi>
                                    <afi-safi xmlns="http://openconfig.net/yang/bgp-multiprotocol">
                                        <afi-safi-name>IPV6_UNICAST</afi-safi-name>
                                        <config>
                                            <afi-safi-name>IPV6_UNICAST</afi-safi-name>
                                        </config>
                                        <graceful-restart>
                                            <state>
                                                <enabled>false</enabled>
                                            </state>
                                        </graceful-restart>
                                        <state>
                                            <afi-safi-name>IPV6_UNICAST</afi-safi-name>
                                            <enabled>true</enabled>
                                        </state>
                                        <route-selection-options>
                                            <config>
                                                <advertise-inactive-routes>false</advertise-inactive-routes>
                                            </config>
                                            <state>
                                                <advertise-inactive-routes>false</advertise-inactive-routes>
                                            </state>
                                        </route-selection-options>
                                        <use-multiple-paths>
                                            <ebgp>
                                                <config>
                                                    <maximum-paths>1</maximum-paths>
                                                </config>
                                                <state>
                                                    <maximum-paths>1</maximum-paths>
                                                </state>
                                            </ebgp>
                                            <ibgp>
                                                <config>
                                                    <maximum-paths>1</maximum-paths>
                                                </config>
                                                <state>
                                                    <maximum-paths>1</maximum-paths>
                                                </state>
                                            </ibgp>
                                        </use-multiple-paths>
                                    </afi-safi>
                                    <afi-safi xmlns="http://openconfig.net/yang/bgp-multiprotocol">
                                        <afi-safi-name>IPV4_UNICAST</afi-safi-name>
                                        <config>
                                            <afi-safi-name>IPV4_UNICAST</afi-safi-name>
                                        </config>
                                        <graceful-restart>
                                            <state>
                                                <enabled>false</enabled>
                                            </state>
                                        </graceful-restart>
                                        <state>
                                            <afi-safi-name>IPV4_UNICAST</afi-safi-name>
                                            <enabled>true</enabled>
                                        </state>
                                        <route-selection-options>
                                            <config>
                                                <advertise-inactive-routes>false</advertise-inactive-routes>
                                            </config>
                                            <state>
                                                <advertise-inactive-routes>false</advertise-inactive-routes>
                                            </state>
                                        </route-selection-options>
                                        <use-multiple-paths>
                                            <ebgp>
                                                <config>
                                                    <maximum-paths>1</maximum-paths>
                                                </config>
                                                <state>
                                                    <maximum-paths>1</maximum-paths>
                                                </state>
                                            </ebgp>
                                            <ibgp>
                                                <config>
                                                    <maximum-paths>1</maximum-paths>
                                                </config>
                                                <state>
                                                    <maximum-paths>1</maximum-paths>
                                                </state>
                                            </ibgp>
                                        </use-multiple-paths>
                                    </afi-safi>
                                    <afi-safi xmlns="http://openconfig.net/yang/bgp-multiprotocol">
                                        <afi-safi-name>none</afi-safi-name>
                                        <config>
                                            <afi-safi-name>none</afi-safi-name>
                                        </config>
                                        <graceful-restart>
                                            <state>
                                                <enabled>false</enabled>
                                            </state>
                                        </graceful-restart>
                                        <state>
                                            <afi-safi-name>none</afi-safi-name>
                                            <enabled>true</enabled>
                                        </state>
                                        <route-selection-options>
                                            <config>
                                                <advertise-inactive-routes>false</advertise-inactive-routes>
                                            </config>
                                            <state>
                                                <advertise-inactive-routes>false</advertise-inactive-routes>
                                            </state>
                                        </route-selection-options>
                                        <use-multiple-paths>
                                            <ebgp>
                                                <config>
                                                    <maximum-paths>1</maximum-paths>
                                                </config>
                                                <state>
                                                    <maximum-paths>1</maximum-paths>
                                                </state>
                                            </ebgp>
                                            <ibgp>
                                                <config>
                                                    <maximum-paths>1</maximum-paths>
                                                </config>
                                                <state>
                                                    <maximum-paths>1</maximum-paths>
                                                </state>
                                            </ibgp>
                                        </use-multiple-paths>
                                    </afi-safi>
                                    <afi-safi xmlns="http://openconfig.net/yang/bgp-multiprotocol">
                                        <afi-safi-name>IPV4_LABELED_UNICAST</afi-safi-name>
                                        <config>
                                            <afi-safi-name>IPV4_LABELED_UNICAST</afi-safi-name>
                                        </config>
                                        <graceful-restart>
                                            <state>
                                                <enabled>false</enabled>
                                            </state>
                                        </graceful-restart>
                                        <state>
                                            <afi-safi-name>IPV4_LABELED_UNICAST</afi-safi-name>
                                            <enabled>true</enabled>
                                        </state>
                                        <route-selection-options>
                                            <config>
                                                <advertise-inactive-routes>false</advertise-inactive-routes>
                                            </config>
                                            <state>
                                                <advertise-inactive-routes>false</advertise-inactive-routes>
                                            </state>
                                        </route-selection-options>
                                        <use-multiple-paths>
                                            <ebgp>
                                                <config>
                                                    <maximum-paths>1</maximum-paths>
                                                </config>
                                                <state>
                                                    <maximum-paths>1</maximum-paths>
                                                </state>
                                            </ebgp>
                                            <ibgp>
                                                <config>
                                                    <maximum-paths>1</maximum-paths>
                                                </config>
                                                <state>
                                                    <maximum-paths>1</maximum-paths>
                                                </state>
                                            </ibgp>
                                        </use-multiple-paths>
                                    </afi-safi>
                                </afi-safis>
                                <graceful-restart>
                                    <config>
                                        <enabled>false</enabled>
                                        <helper-only>false</helper-only>
                                        <restart-time>120</restart-time>
                                        <stale-routes-time>300</stale-routes-time>
                                    </config>
                                    <state>
                                        <enabled>false</enabled>
                                        <helper-only>false</helper-only>
                                        <restart-time>120</restart-time>
                                        <stale-routes-time>300</stale-routes-time>
                                    </state>
                                </graceful-restart>
                                <use-multiple-paths xmlns="http://openconfig.net/yang/bgp-multiprotocol">
                                    <ebgp>
                                        <config>
                                            <maximum-paths>1</maximum-paths>
                                        </config>
                                        <state>
                                            <maximum-paths>1</maximum-paths>
                                        </state>
                                    </ebgp>
                                    <ibgp>
                                        <config>
                                            <maximum-paths>1</maximum-paths>
                                        </config>
                                        <state>
                                            <maximum-paths>1</maximum-paths>
                                        </state>
                                    </ibgp>
                                </use-multiple-paths>
                                <config>
                                    <as>333</as>
                                    <router-id>0.0.0.0</router-id>
                                </config>
                                <state>
                                    <as>333</as>
                                    <router-id>0.0.0.0</router-id>
                                </state>
                            </global>
                            <neighbors>
                                <neighbor>
                                    <graceful-restart>
                                        <state>
                                            <enabled>false</enabled>
                                            <helper-only>false</helper-only>
                                            <restart-time>120</restart-time>
                                            <stale-routes-time>300</stale-routes-time>
                                        </state>
                                    </graceful-restart>
                                    <config>
                                        <description/>
                                        <peer-as/>
                                        <remove-private-as/>
                                        <peer-group/>
                                        <neighbor-address>4.4.4.4</neighbor-address>
                                    </config>
                                    <ebgp-multihop>
                                        <config>
                                            <multihop-ttl>0</multihop-ttl>
                                        </config>
                                        <state>
                                            <enabled>false</enabled>
                                            <multihop-ttl>0</multihop-ttl>
                                        </state>
                                    </ebgp-multihop>
                                    <logging-options>
                                        <config>
                                            <log-neighbor-state-changes>true</log-neighbor-state-changes>
                                        </config>
                                        <state>
                                            <log-neighbor-state-changes>true</log-neighbor-state-changes>
                                        </state>
                                    </logging-options>
                                    <route-reflector>
                                        <config>
                                            <route-reflector-cluster-id>3</route-reflector-cluster-id>
                                        </config>
                                        <state>
                                            <route-reflector-cluster-id>3</route-reflector-cluster-id>
                                        </state>
                                    </route-reflector>
                                    <state>
                                        <description/>
                                        <peer-as/>
                                        <remove-private-as/>
                                        <peer-group/>
                                        <neighbor-address>4.4.4.4</neighbor-address>
                                    </state>
                                    <timers>
                                        <config>
                                            <hold-time>180</hold-time>
                                            <keepalive-interval>60</keepalive-interval>
                                        </config>
                                        <state>
                                            <hold-time>180</hold-time>
                                            <keepalive-interval>60</keepalive-interval>
                                        </state>
                                    </timers>
                                    <transport>
                                        <config>
                                            <passive-mode>false</passive-mode>
                                        </config>
                                        <state>
                                            <local-address>0.0.0.0</local-address>
                                            <passive-mode>false</passive-mode>
                                            <local-port xmlns="http://openconfig.net/yang/bgp-operational">unspecified</local-port>
                                            <remote-address xmlns="http://openconfig.net/yang/bgp-operational">4.4.4.4</remote-address>
                                            <remote-port xmlns="http://openconfig.net/yang/bgp-operational">unspecified</remote-port>
                                        </state>
                                    </transport>
                                    <neighbor-address>4.4.4.4</neighbor-address>
                                </neighbor>
                                <neighbor>
                                    <afi-safis>
                                        <afi-safi xmlns="http://openconfig.net/yang/bgp-multiprotocol">
                                            <afi-safi-name>IPV6_UNICAST</afi-safi-name>
                                            <config>
                                                <afi-safi-name>IPV6_UNICAST</afi-safi-name>
                                            </config>
                                            <graceful-restart>
                                                <state>
                                                    <enabled>false</enabled>
                                                </state>
                                            </graceful-restart>
                                            <state>
                                                <afi-safi-name>IPV6_UNICAST</afi-safi-name>
                                                <enabled>true</enabled>
                                            </state>
                                        </afi-safi>
                                        <afi-safi xmlns="http://openconfig.net/yang/bgp-multiprotocol">
                                            <afi-safi-name>L3VPN_IPV6_UNICAST</afi-safi-name>
                                            <config>
                                                <afi-safi-name>L3VPN_IPV6_UNICAST</afi-safi-name>
                                            </config>
                                            <graceful-restart>
                                                <state>
                                                    <enabled>false</enabled>
                                                </state>
                                            </graceful-restart>
                                            <state>
                                                <afi-safi-name>L3VPN_IPV6_UNICAST</afi-safi-name>
                                                <enabled>true</enabled>
                                            </state>
                                        </afi-safi>
                                        <afi-safi xmlns="http://openconfig.net/yang/bgp-multiprotocol">
                                            <afi-safi-name>none</afi-safi-name>
                                            <config>
                                                <afi-safi-name>none</afi-safi-name>
                                            </config>
                                            <graceful-restart>
                                                <state>
                                                    <enabled>false</enabled>
                                                </state>
                                            </graceful-restart>
                                            <state>
                                                <afi-safi-name>none</afi-safi-name>
                                                <enabled>true</enabled>
                                            </state>
                                        </afi-safi>
                                        <afi-safi xmlns="http://openconfig.net/yang/bgp-multiprotocol">
                                            <afi-safi-name>none</afi-safi-name>
                                            <config>
                                                <afi-safi-name>none</afi-safi-name>
                                            </config>
                                            <graceful-restart>
                                                <state>
                                                    <enabled>false</enabled>
                                                </state>
                                            </graceful-restart>
                                            <state>
                                                <afi-safi-name>none</afi-safi-name>
                                                <enabled>true</enabled>
                                            </state>
                                        </afi-safi>
                                        <afi-safi xmlns="http://openconfig.net/yang/bgp-multiprotocol">
                                            <afi-safi-name>none</afi-safi-name>
                                            <config>
                                                <afi-safi-name>none</afi-safi-name>
                                            </config>
                                            <graceful-restart>
                                                <state>
                                                    <enabled>false</enabled>
                                                </state>
                                            </graceful-restart>
                                            <state>
                                                <afi-safi-name>none</afi-safi-name>
                                                <enabled>true</enabled>
                                            </state>
                                        </afi-safi>
                                        <afi-safi xmlns="http://openconfig.net/yang/bgp-multiprotocol">
                                            <afi-safi-name>IPV4_UNICAST</afi-safi-name>
                                            <config>
                                                <afi-safi-name>IPV4_UNICAST</afi-safi-name>
                                            </config>
                                            <graceful-restart>
                                                <state>
                                                    <enabled>false</enabled>
                                                </state>
                                            </graceful-restart>
                                            <state>
                                                <afi-safi-name>IPV4_UNICAST</afi-safi-name>
                                                <enabled>true</enabled>
                                            </state>
                                        </afi-safi>
                                        <afi-safi xmlns="http://openconfig.net/yang/bgp-multiprotocol">
                                            <afi-safi-name>L3VPN_IPV4_UNICAST</afi-safi-name>
                                            <config>
                                                <afi-safi-name>L3VPN_IPV4_UNICAST</afi-safi-name>
                                            </config>
                                            <graceful-restart>
                                                <state>
                                                    <enabled>false</enabled>
                                                </state>
                                            </graceful-restart>
                                            <state>
                                                <afi-safi-name>L3VPN_IPV4_UNICAST</afi-safi-name>
                                                <enabled>true</enabled>
                                            </state>
                                        </afi-safi>
                                    </afi-safis>
                                    <as-path-options>
                                        <config>
                                            <allow-own-as>0</allow-own-as>
                                        </config>
                                        <state>
                                            <allow-own-as>0</allow-own-as>
                                        </state>
                                    </as-path-options>
                                    <graceful-restart>
                                        <state>
                                            <enabled>false</enabled>
                                            <helper-only>false</helper-only>
                                            <restart-time>120</restart-time>
                                            <stale-routes-time>300</stale-routes-time>
                                        </state>
                                    </graceful-restart>
                                    <config>
                                        <description/>
                                        <peer-as>333</peer-as>
                                        <remove-private-as/>
                                        <send-community>BOTH</send-community>
                                        <peer-group/>
                                        <neighbor-address>21.0.102.1</neighbor-address>
                                    </config>
                                    <ebgp-multihop>
                                        <config>
                                            <multihop-ttl>0</multihop-ttl>
                                        </config>
                                        <state>
                                            <enabled>false</enabled>
                                            <multihop-ttl>0</multihop-ttl>
                                        </state>
                                    </ebgp-multihop>
                                    <logging-options>
                                        <config>
                                            <log-neighbor-state-changes>true</log-neighbor-state-changes>
                                        </config>
                                        <state>
                                            <log-neighbor-state-changes>true</log-neighbor-state-changes>
                                        </state>
                                    </logging-options>
                                    <route-reflector>
                                        <config>
                                            <route-reflector-client>true</route-reflector-client>
                                            <route-reflector-cluster-id>3</route-reflector-cluster-id>
                                        </config>
                                        <state>
                                            <route-reflector-client>true</route-reflector-client>
                                            <route-reflector-cluster-id>3</route-reflector-cluster-id>
                                        </state>
                                    </route-reflector>
                                    <state>
                                        <description/>
                                        <peer-as>333</peer-as>
                                        <remove-private-as/>
                                        <send-community>BOTH</send-community>
                                        <peer-group/>
                                        <neighbor-address>21.0.102.1</neighbor-address>
                                    </state>
                                    <timers>
                                        <config>
                                            <hold-time>180</hold-time>
                                            <keepalive-interval>60</keepalive-interval>
                                            <minimum-advertisement-interval>0</minimum-advertisement-interval>
                                        </config>
                                        <state>
                                            <hold-time>180</hold-time>
                                            <keepalive-interval>60</keepalive-interval>
                                            <minimum-advertisement-interval>0</minimum-advertisement-interval>
                                        </state>
                                    </timers>
                                    <transport>
                                        <config>
                                            <passive-mode>false</passive-mode>
                                        </config>
                                        <state>
                                            <local-address>0.0.0.0</local-address>
                                            <passive-mode>false</passive-mode>
                                            <local-port xmlns="http://openconfig.net/yang/bgp-operational">unspecified</local-port>
                                            <remote-address xmlns="http://openconfig.net/yang/bgp-operational">21.0.102.1</remote-address>
                                            <remote-port xmlns="http://openconfig.net/yang/bgp-operational">unspecified</remote-port>
                                        </state>
                                    </transport>
                                    <neighbor-address>21.0.102.1</neighbor-address>
                                </neighbor>
                                <neighbor>
                                    <afi-safis>
                                        <afi-safi xmlns="http://openconfig.net/yang/bgp-multiprotocol">
                                            <afi-safi-name>IPV6_UNICAST</afi-safi-name>
                                            <config>
                                                <afi-safi-name>IPV6_UNICAST</afi-safi-name>
                                            </config>
                                            <graceful-restart>
                                                <state>
                                                    <enabled>false</enabled>
                                                </state>
                                            </graceful-restart>
                                            <ipv6-unicast>
                                                <config>
                                                    <send-default-route>false</send-default-route>
                                                </config>
                                                <state>
                                                    <send-default-route>false</send-default-route>
                                                </state>
                                            </ipv6-unicast>
                                            <state>
                                                <afi-safi-name>IPV6_UNICAST</afi-safi-name>
                                                <enabled>true</enabled>
                                            </state>
                                        </afi-safi>
                                        <afi-safi xmlns="http://openconfig.net/yang/bgp-multiprotocol">
                                            <afi-safi-name>none</afi-safi-name>
                                            <config>
                                                <afi-safi-name>none</afi-safi-name>
                                            </config>
                                            <graceful-restart>
                                                <state>
                                                    <enabled>false</enabled>
                                                </state>
                                            </graceful-restart>
                                            <state>
                                                <afi-safi-name>none</afi-safi-name>
                                                <enabled>true</enabled>
                                            </state>
                                        </afi-safi>
                                        <afi-safi xmlns="http://openconfig.net/yang/bgp-multiprotocol">
                                            <afi-safi-name>none</afi-safi-name>
                                            <config>
                                                <afi-safi-name>none</afi-safi-name>
                                            </config>
                                            <graceful-restart>
                                                <state>
                                                    <enabled>false</enabled>
                                                </state>
                                            </graceful-restart>
                                            <state>
                                                <afi-safi-name>none</afi-safi-name>
                                                <enabled>true</enabled>
                                            </state>
                                        </afi-safi>
                                        <afi-safi xmlns="http://openconfig.net/yang/bgp-multiprotocol">
                                            <afi-safi-name>IPV4_UNICAST</afi-safi-name>
                                            <config>
                                                <afi-safi-name>IPV4_UNICAST</afi-safi-name>
                                            </config>
                                            <graceful-restart>
                                                <state>
                                                    <enabled>false</enabled>
                                                </state>
                                            </graceful-restart>
                                            <ipv4-unicast>
                                                <config>
                                                    <send-default-route>false</send-default-route>
                                                </config>
                                                <state>
                                                    <send-default-route>false</send-default-route>
                                                </state>
                                            </ipv4-unicast>
                                            <state>
                                                <afi-safi-name>IPV4_UNICAST</afi-safi-name>
                                                <enabled>true</enabled>
                                            </state>
                                        </afi-safi>
                                    </afi-safis>
                                    <as-path-options>
                                        <config>
                                            <allow-own-as>0</allow-own-as>
                                        </config>
                                        <state>
                                            <allow-own-as>0</allow-own-as>
                                        </state>
                                    </as-path-options>
                                    <graceful-restart>
                                        <state>
                                            <enabled>false</enabled>
                                            <helper-only>false</helper-only>
                                            <restart-time>120</restart-time>
                                            <stale-routes-time>300</stale-routes-time>
                                        </state>
                                    </graceful-restart>
                                    <config>
                                        <description/>
                                        <peer-as>888</peer-as>
                                        <remove-private-as/>
                                        <send-community>BOTH</send-community>
                                        <peer-group/>
                                        <neighbor-address>fec1::2002</neighbor-address>
                                    </config>
                                    <ebgp-multihop>
                                        <config>
                                            <multihop-ttl>0</multihop-ttl>
                                        </config>
                                        <state>
                                            <enabled>false</enabled>
                                            <multihop-ttl>0</multihop-ttl>
                                        </state>
                                    </ebgp-multihop>
                                    <logging-options>
                                        <config>
                                            <log-neighbor-state-changes>true</log-neighbor-state-changes>
                                        </config>
                                        <state>
                                            <log-neighbor-state-changes>true</log-neighbor-state-changes>
                                        </state>
                                    </logging-options>
                                    <route-reflector>
                                        <config>
                                            <route-reflector-client>false</route-reflector-client>
                                            <route-reflector-cluster-id>3</route-reflector-cluster-id>
                                        </config>
                                        <state>
                                            <route-reflector-client>false</route-reflector-client>
                                            <route-reflector-cluster-id>3</route-reflector-cluster-id>
                                        </state>
                                    </route-reflector>
                                    <state>
                                        <description/>
                                        <peer-as>888</peer-as>
                                        <remove-private-as/>
                                        <send-community>BOTH</send-community>
                                        <peer-group/>
                                        <neighbor-address>fec1::2002</neighbor-address>
                                    </state>
                                    <timers>
                                        <config>
                                            <hold-time>180</hold-time>
                                            <keepalive-interval>60</keepalive-interval>
                                            <minimum-advertisement-interval>0</minimum-advertisement-interval>
                                        </config>
                                        <state>
                                            <hold-time>180</hold-time>
                                            <keepalive-interval>60</keepalive-interval>
                                            <minimum-advertisement-interval>0</minimum-advertisement-interval>
                                        </state>
                                    </timers>
                                    <transport>
                                        <config>
                                            <passive-mode>false</passive-mode>
                                        </config>
                                        <state>
                                            <local-address>::</local-address>
                                            <passive-mode>false</passive-mode>
                                            <local-port xmlns="http://openconfig.net/yang/bgp-operational">unspecified</local-port>
                                            <remote-address xmlns="http://openconfig.net/yang/bgp-operational">fec1::2002</remote-address>
                                            <remote-port xmlns="http://openconfig.net/yang/bgp-operational">unspecified</remote-port>
                                        </state>
                                    </transport>
                                    <neighbor-address>fec1::2002</neighbor-address>
                                </neighbor>
                                <neighbor>
                                    <afi-safis>
                                        <afi-safi xmlns="http://openconfig.net/yang/bgp-multiprotocol">
                                            <afi-safi-name>IPV4_UNICAST</afi-safi-name>
                                            <config>
                                                <afi-safi-name>IPV4_UNICAST</afi-safi-name>
                                            </config>
                                            <graceful-restart>
                                                <state>
                                                    <enabled>false</enabled>
                                                </state>
                                            </graceful-restart>
                                            <ipv4-unicast>
                                                <config>
                                                    <send-default-route>false</send-default-route>
                                                </config>
                                                <state>
                                                    <send-default-route>false</send-default-route>
                                                </state>
                                            </ipv4-unicast>
                                            <state>
                                                <afi-safi-name>IPV4_UNICAST</afi-safi-name>
                                                <enabled>true</enabled>
                                            </state>
                                        </afi-safi>
                                    </afi-safis>
                                    <as-path-options>
                                        <config>
                                            <allow-own-as>0</allow-own-as>
                                        </config>
                                        <state>
                                            <allow-own-as>0</allow-own-as>
                                        </state>
                                    </as-path-options>
                                    <graceful-restart>
                                        <state>
                                            <enabled>false</enabled>
                                            <helper-only>false</helper-only>
                                            <restart-time>120</restart-time>
                                            <stale-routes-time>300</stale-routes-time>
                                        </state>
                                    </graceful-restart>
                                    <config>
                                        <description/>
                                        <peer-as>333</peer-as>
                                        <remove-private-as/>
                                        <send-community>BOTH</send-community>
                                        <peer-group/>
                                        <neighbor-address>fec1::1002</neighbor-address>
                                    </config>
                                    <ebgp-multihop>
                                        <config>
                                            <multihop-ttl>0</multihop-ttl>
                                        </config>
                                        <state>
                                            <enabled>false</enabled>
                                            <multihop-ttl>0</multihop-ttl>
                                        </state>
                                    </ebgp-multihop>
                                    <logging-options>
                                        <config>
                                            <log-neighbor-state-changes>true</log-neighbor-state-changes>
                                        </config>
                                        <state>
                                            <log-neighbor-state-changes>true</log-neighbor-state-changes>
                                        </state>
                                    </logging-options>
                                    <route-reflector>
                                        <config>
                                            <route-reflector-client>true</route-reflector-client>
                                            <route-reflector-cluster-id>3</route-reflector-cluster-id>
                                        </config>
                                        <state>
                                            <route-reflector-client>true</route-reflector-client>
                                            <route-reflector-cluster-id>3</route-reflector-cluster-id>
                                        </state>
                                    </route-reflector>
                                    <state>
                                        <description/>
                                        <peer-as>333</peer-as>
                                        <remove-private-as/>
                                        <send-community>BOTH</send-community>
                                        <peer-group/>
                                        <neighbor-address>fec1::1002</neighbor-address>
                                    </state>
                                    <timers>
                                        <config>
                                            <hold-time>180</hold-time>
                                            <keepalive-interval>60</keepalive-interval>
                                            <minimum-advertisement-interval>0</minimum-advertisement-interval>
                                        </config>
                                        <state>
                                            <hold-time>180</hold-time>
                                            <keepalive-interval>60</keepalive-interval>
                                            <minimum-advertisement-interval>0</minimum-advertisement-interval>
                                        </state>
                                    </timers>
                                    <transport>
                                        <config>
                                            <passive-mode>false</passive-mode>
                                        </config>
                                        <state>
                                            <local-address>::</local-address>
                                            <passive-mode>false</passive-mode>
                                            <local-port xmlns="http://openconfig.net/yang/bgp-operational">unspecified</local-port>
                                            <remote-address xmlns="http://openconfig.net/yang/bgp-operational">fec1::1002</remote-address>
                                            <remote-port xmlns="http://openconfig.net/yang/bgp-operational">unspecified</remote-port>
                                        </state>
                                    </transport>
                                    <neighbor-address>fec1::1002</neighbor-address>
                                </neighbor>
                                <neighbor>
                                    <afi-safis>
                                        <afi-safi xmlns="http://openconfig.net/yang/bgp-multiprotocol">
                                            <afi-safi-name>IPV6_UNICAST</afi-safi-name>
                                            <config>
                                                <afi-safi-name>IPV6_UNICAST</afi-safi-name>
                                            </config>
                                            <graceful-restart>
                                                <state>
                                                    <enabled>false</enabled>
                                                </state>
                                            </graceful-restart>
                                            <state>
                                                <afi-safi-name>IPV6_UNICAST</afi-safi-name>
                                                <enabled>true</enabled>
                                            </state>
                                        </afi-safi>
                                        <afi-safi xmlns="http://openconfig.net/yang/bgp-multiprotocol">
                                            <afi-safi-name>L3VPN_IPV6_UNICAST</afi-safi-name>
                                            <config>
                                                <afi-safi-name>L3VPN_IPV6_UNICAST</afi-safi-name>
                                            </config>
                                            <graceful-restart>
                                                <state>
                                                    <enabled>false</enabled>
                                                </state>
                                            </graceful-restart>
                                            <state>
                                                <afi-safi-name>L3VPN_IPV6_UNICAST</afi-safi-name>
                                                <enabled>true</enabled>
                                            </state>
                                        </afi-safi>
                                        <afi-safi xmlns="http://openconfig.net/yang/bgp-multiprotocol">
                                            <afi-safi-name>none</afi-safi-name>
                                            <config>
                                                <afi-safi-name>none</afi-safi-name>
                                            </config>
                                            <graceful-restart>
                                                <state>
                                                    <enabled>false</enabled>
                                                </state>
                                            </graceful-restart>
                                            <state>
                                                <afi-safi-name>none</afi-safi-name>
                                                <enabled>true</enabled>
                                            </state>
                                        </afi-safi>
                                        <afi-safi xmlns="http://openconfig.net/yang/bgp-multiprotocol">
                                            <afi-safi-name>none</afi-safi-name>
                                            <config>
                                                <afi-safi-name>none</afi-safi-name>
                                            </config>
                                            <graceful-restart>
                                                <state>
                                                    <enabled>false</enabled>
                                                </state>
                                            </graceful-restart>
                                            <state>
                                                <afi-safi-name>none</afi-safi-name>
                                                <enabled>true</enabled>
                                            </state>
                                        </afi-safi>
                                        <afi-safi xmlns="http://openconfig.net/yang/bgp-multiprotocol">
                                            <afi-safi-name>none</afi-safi-name>
                                            <config>
                                                <afi-safi-name>none</afi-safi-name>
                                            </config>
                                            <graceful-restart>
                                                <state>
                                                    <enabled>false</enabled>
                                                </state>
                                            </graceful-restart>
                                            <state>
                                                <afi-safi-name>none</afi-safi-name>
                                                <enabled>true</enabled>
                                            </state>
                                        </afi-safi>
                                        <afi-safi xmlns="http://openconfig.net/yang/bgp-multiprotocol">
                                            <afi-safi-name>IPV4_UNICAST</afi-safi-name>
                                            <config>
                                                <afi-safi-name>IPV4_UNICAST</afi-safi-name>
                                            </config>
                                            <graceful-restart>
                                                <state>
                                                    <enabled>false</enabled>
                                                </state>
                                            </graceful-restart>
                                            <ipv4-unicast>
                                                <config>
                                                    <send-default-route>false</send-default-route>
                                                </config>
                                                <state>
                                                    <send-default-route>false</send-default-route>
                                                </state>
                                            </ipv4-unicast>
                                            <state>
                                                <afi-safi-name>IPV4_UNICAST</afi-safi-name>
                                                <enabled>true</enabled>
                                            </state>
                                        </afi-safi>
                                        <afi-safi xmlns="http://openconfig.net/yang/bgp-multiprotocol">
                                            <afi-safi-name>L3VPN_IPV4_UNICAST</afi-safi-name>
                                            <config>
                                                <afi-safi-name>L3VPN_IPV4_UNICAST</afi-safi-name>
                                            </config>
                                            <graceful-restart>
                                                <state>
                                                    <enabled>false</enabled>
                                                </state>
                                            </graceful-restart>
                                            <state>
                                                <afi-safi-name>L3VPN_IPV4_UNICAST</afi-safi-name>
                                                <enabled>true</enabled>
                                            </state>
                                        </afi-safi>
                                    </afi-safis>
                                    <as-path-options>
                                        <config>
                                            <allow-own-as>0</allow-own-as>
                                        </config>
                                        <state>
                                            <allow-own-as>0</allow-own-as>
                                        </state>
                                    </as-path-options>
                                    <graceful-restart>
                                        <state>
                                            <enabled>false</enabled>
                                            <helper-only>false</helper-only>
                                            <restart-time>120</restart-time>
                                            <stale-routes-time>300</stale-routes-time>
                                        </state>
                                    </graceful-restart>
                                    <config>
                                        <description/>
                                        <peer-as>333</peer-as>
                                        <remove-private-as/>
                                        <send-community>BOTH</send-community>
                                        <peer-group/>
                                        <neighbor-address>21.0.101.1</neighbor-address>
                                    </config>
                                    <ebgp-multihop>
                                        <config>
                                            <multihop-ttl>0</multihop-ttl>
                                        </config>
                                        <state>
                                            <enabled>false</enabled>
                                            <multihop-ttl>0</multihop-ttl>
                                        </state>
                                    </ebgp-multihop>
                                    <logging-options>
                                        <config>
                                            <log-neighbor-state-changes>true</log-neighbor-state-changes>
                                        </config>
                                        <state>
                                            <log-neighbor-state-changes>true</log-neighbor-state-changes>
                                        </state>
                                    </logging-options>
                                    <route-reflector>
                                        <config>
                                            <route-reflector-client>true</route-reflector-client>
                                            <route-reflector-cluster-id>3</route-reflector-cluster-id>
                                        </config>
                                        <state>
                                            <route-reflector-client>true</route-reflector-client>
                                            <route-reflector-cluster-id>3</route-reflector-cluster-id>
                                        </state>
                                    </route-reflector>
                                    <state>
                                        <description/>
                                        <peer-as>333</peer-as>
                                        <remove-private-as/>
                                        <send-community>BOTH</send-community>
                                        <peer-group/>
                                        <neighbor-address>21.0.101.1</neighbor-address>
                                    </state>
                                    <timers>
                                        <config>
                                            <hold-time>180</hold-time>
                                            <keepalive-interval>60</keepalive-interval>
                                            <minimum-advertisement-interval>0</minimum-advertisement-interval>
                                        </config>
                                        <state>
                                            <hold-time>180</hold-time>
                                            <keepalive-interval>60</keepalive-interval>
                                            <minimum-advertisement-interval>0</minimum-advertisement-interval>
                                        </state>
                                    </timers>
                                    <transport>
                                        <config>
                                            <passive-mode>false</passive-mode>
                                        </config>
                                        <state>
                                            <local-address>0.0.0.0</local-address>
                                            <passive-mode>false</passive-mode>
                                            <local-port xmlns="http://openconfig.net/yang/bgp-operational">unspecified</local-port>
                                            <remote-address xmlns="http://openconfig.net/yang/bgp-operational">21.0.101.1</remote-address>
                                            <remote-port xmlns="http://openconfig.net/yang/bgp-operational">unspecified</remote-port>
                                        </state>
                                    </transport>
                                    <neighbor-address>21.0.101.1</neighbor-address>
                                </neighbor>
                                <neighbor>
                                    <afi-safis>
                                        <afi-safi xmlns="http://openconfig.net/yang/bgp-multiprotocol">
                                            <afi-safi-name>IPV6_UNICAST</afi-safi-name>
                                            <config>
                                                <afi-safi-name>IPV6_UNICAST</afi-safi-name>
                                            </config>
                                            <graceful-restart>
                                                <state>
                                                    <enabled>false</enabled>
                                                </state>
                                            </graceful-restart>
                                            <ipv6-unicast>
                                                <config>
                                                    <send-default-route>false</send-default-route>
                                                </config>
                                                <state>
                                                    <send-default-route>false</send-default-route>
                                                </state>
                                            </ipv6-unicast>
                                            <state>
                                                <afi-safi-name>IPV6_UNICAST</afi-safi-name>
                                                <enabled>true</enabled>
                                            </state>
                                        </afi-safi>
                                        <afi-safi xmlns="http://openconfig.net/yang/bgp-multiprotocol">
                                            <afi-safi-name>L3VPN_IPV6_UNICAST</afi-safi-name>
                                            <config>
                                                <afi-safi-name>L3VPN_IPV6_UNICAST</afi-safi-name>
                                            </config>
                                            <graceful-restart>
                                                <state>
                                                    <enabled>false</enabled>
                                                </state>
                                            </graceful-restart>
                                            <state>
                                                <afi-safi-name>L3VPN_IPV6_UNICAST</afi-safi-name>
                                                <enabled>true</enabled>
                                            </state>
                                        </afi-safi>
                                        <afi-safi xmlns="http://openconfig.net/yang/bgp-multiprotocol">
                                            <afi-safi-name>none</afi-safi-name>
                                            <config>
                                                <afi-safi-name>none</afi-safi-name>
                                            </config>
                                            <graceful-restart>
                                                <state>
                                                    <enabled>false</enabled>
                                                </state>
                                            </graceful-restart>
                                            <state>
                                                <afi-safi-name>none</afi-safi-name>
                                                <enabled>true</enabled>
                                            </state>
                                        </afi-safi>
                                        <afi-safi xmlns="http://openconfig.net/yang/bgp-multiprotocol">
                                            <afi-safi-name>none</afi-safi-name>
                                            <config>
                                                <afi-safi-name>none</afi-safi-name>
                                            </config>
                                            <graceful-restart>
                                                <state>
                                                    <enabled>false</enabled>
                                                </state>
                                            </graceful-restart>
                                            <state>
                                                <afi-safi-name>none</afi-safi-name>
                                                <enabled>true</enabled>
                                            </state>
                                        </afi-safi>
                                        <afi-safi xmlns="http://openconfig.net/yang/bgp-multiprotocol">
                                            <afi-safi-name>none</afi-safi-name>
                                            <config>
                                                <afi-safi-name>none</afi-safi-name>
                                            </config>
                                            <graceful-restart>
                                                <state>
                                                    <enabled>false</enabled>
                                                </state>
                                            </graceful-restart>
                                            <state>
                                                <afi-safi-name>none</afi-safi-name>
                                                <enabled>true</enabled>
                                            </state>
                                        </afi-safi>
                                        <afi-safi xmlns="http://openconfig.net/yang/bgp-multiprotocol">
                                            <afi-safi-name>IPV4_UNICAST</afi-safi-name>
                                            <config>
                                                <afi-safi-name>IPV4_UNICAST</afi-safi-name>
                                            </config>
                                            <graceful-restart>
                                                <state>
                                                    <enabled>false</enabled>
                                                </state>
                                            </graceful-restart>
                                            <ipv4-unicast>
                                                <config>
                                                    <send-default-route>false</send-default-route>
                                                </config>
                                                <state>
                                                    <send-default-route>false</send-default-route>
                                                </state>
                                            </ipv4-unicast>
                                            <state>
                                                <afi-safi-name>IPV4_UNICAST</afi-safi-name>
                                                <enabled>true</enabled>
                                            </state>
                                        </afi-safi>
                                        <afi-safi xmlns="http://openconfig.net/yang/bgp-multiprotocol">
                                            <afi-safi-name>L3VPN_IPV4_UNICAST</afi-safi-name>
                                            <config>
                                                <afi-safi-name>L3VPN_IPV4_UNICAST</afi-safi-name>
                                            </config>
                                            <graceful-restart>
                                                <state>
                                                    <enabled>false</enabled>
                                                </state>
                                            </graceful-restart>
                                            <state>
                                                <afi-safi-name>L3VPN_IPV4_UNICAST</afi-safi-name>
                                                <enabled>true</enabled>
                                            </state>
                                        </afi-safi>
                                    </afi-safis>
                                    <as-path-options>
                                        <config>
                                            <allow-own-as>0</allow-own-as>
                                        </config>
                                        <state>
                                            <allow-own-as>0</allow-own-as>
                                        </state>
                                    </as-path-options>
                                    <graceful-restart>
                                        <state>
                                            <enabled>false</enabled>
                                            <helper-only>false</helper-only>
                                            <restart-time>120</restart-time>
                                            <stale-routes-time>300</stale-routes-time>
                                        </state>
                                    </graceful-restart>
                                    <config>
                                        <description/>
                                        <peer-as>888</peer-as>
                                        <remove-private-as/>
                                        <send-community>BOTH</send-community>
                                        <peer-group/>
                                        <neighbor-address>21.0.201.1</neighbor-address>
                                    </config>
                                    <ebgp-multihop>
                                        <config>
                                            <multihop-ttl>0</multihop-ttl>
                                        </config>
                                        <state>
                                            <enabled>false</enabled>
                                            <multihop-ttl>0</multihop-ttl>
                                        </state>
                                    </ebgp-multihop>
                                    <logging-options>
                                        <config>
                                            <log-neighbor-state-changes>true</log-neighbor-state-changes>
                                        </config>
                                        <state>
                                            <log-neighbor-state-changes>true</log-neighbor-state-changes>
                                        </state>
                                    </logging-options>
                                    <route-reflector>
                                        <config>
                                            <route-reflector-client>false</route-reflector-client>
                                            <route-reflector-cluster-id>3</route-reflector-cluster-id>
                                        </config>
                                        <state>
                                            <route-reflector-client>false</route-reflector-client>
                                            <route-reflector-cluster-id>3</route-reflector-cluster-id>
                                        </state>
                                    </route-reflector>
                                    <state>
                                        <description/>
                                        <peer-as>888</peer-as>
                                        <remove-private-as/>
                                        <send-community>BOTH</send-community>
                                        <peer-group/>
                                        <neighbor-address>21.0.201.1</neighbor-address>
                                    </state>
                                    <timers>
                                        <config>
                                            <hold-time>180</hold-time>
                                            <keepalive-interval>60</keepalive-interval>
                                            <minimum-advertisement-interval>0</minimum-advertisement-interval>
                                        </config>
                                        <state>
                                            <hold-time>180</hold-time>
                                            <keepalive-interval>60</keepalive-interval>
                                            <minimum-advertisement-interval>0</minimum-advertisement-interval>
                                        </state>
                                    </timers>
                                    <transport>
                                        <config>
                                            <passive-mode>false</passive-mode>
                                        </config>
                                        <state>
                                            <local-address>0.0.0.0</local-address>
                                            <passive-mode>false</passive-mode>
                                            <local-port xmlns="http://openconfig.net/yang/bgp-operational">unspecified</local-port>
                                            <remote-address xmlns="http://openconfig.net/yang/bgp-operational">21.0.201.1</remote-address>
                                            <remote-port xmlns="http://openconfig.net/yang/bgp-operational">unspecified</remote-port>
                                        </state>
                                    </transport>
                                    <neighbor-address>21.0.201.1</neighbor-address>
                                </neighbor>
                            </neighbors>
                        </bgp>
                    </data>
                </rpc-reply>
            ''')

    yang_output = {'get.return_value': etree_holder()}

    # def test_show_bgp_vrf_all_neighbors_golden_yang(self):
    #     self.maxDiff = None
    #     self.device = Mock(**self.yang_output)
    #     obj = ShowBgpVrfAllNeighbors(device=self.device, context='yang')
    #     try:
    #         parsed_output = obj.parse(vrf='default')
    #         self.assertEqual(parsed_output,self.golden_parsed_output)
    #     except SchemaMissingKeyError:
    #         pass


# ======================================================
#  Unit test for 'show bgp vrf all all nexthop-database'       
# ======================================================

class test_show_bgp_vrf_all_all_nexthop_database(unittest.TestCase):
    
    '''Unit test for show bgp vrf all all nexthop-database'''

    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output = {
        'vrf':
            {'VRF1':
                {'address_family':
                    {'ipv4 unicast':
                        {'af_nexthop_trigger_enable': True,
                        'igp_cost': 0,
                        'igp_preference': 0,
                        'igp_route_type': 0,
                        'metric_next_advertise': 'never',
                        'next_hop': '0.0.0.0',
                        'nexthop_last_resolved': 'never',
                        'nexthop_resolved_using': '0.0.0.0/0',
                        'nexthop_trigger_delay_critical': 2222,
                        'nexthop_trigger_delay_non_critical': 3333,
                        'nexthop_type': 'not-attached '
                                        'local '
                                        'unreachable '
                                        'not-labeled',
                        'refcount': 4,
                        'rnh_epoch': 0},
                    'ipv6 unicast':
                        {'af_nexthop_trigger_enable': True,
                        'igp_cost': 0,
                        'igp_preference': 0,
                        'igp_route_type': 0,
                        'metric_next_advertise': 'never',
                        'next_hop': '0::',
                        'nexthop_trigger_delay_critical': 3000,
                        'nexthop_trigger_delay_non_critical': 10000,
                        'nexthop_type': 'not-attached '
                                        'local '
                                        'unreachable '
                                        'not-labeled',
                        'refcount': 3,
                        'rnh_epoch': 0}}},
            'default':
                {'address_family':
                    {'ipv4 unicast':
                        {'af_nexthop_trigger_enable': True,
                        'nexthop_trigger_delay_critical': 3000,
                        'nexthop_trigger_delay_non_critical': 10000},
                    'ipv6 label unicast':
                        {'af_nexthop_trigger_enable': True,
                        'nexthop_trigger_delay_critical': 3000,
                        'nexthop_trigger_delay_non_critical': 10000},
                    'ipv6 unicast':
                        {'af_nexthop_trigger_enable': True,
                        'nexthop_trigger_delay_critical': 3000,
                        'nexthop_trigger_delay_non_critical': 10000},
                    'vpnv4 unicast':
                        {'af_nexthop_trigger_enable': True,
                        'attached_nexthop': '10.1.3.3',
                        'attached_nexthop_interface': 'Ethernet4/2',
                        'igp_cost': 41,
                        'igp_preference': 110,
                        'igp_route_type': 0,
                        'metric_next_advertise': 'never',
                        'next_hop': '3.3.3.3',
                        'nexthop_last_resolved': '5w0d',
                        'nexthop_resolved_using': '3.3.3.3/32',
                        'nexthop_trigger_delay_critical': 3000,
                        'nexthop_trigger_delay_non_critical': 10000,
                        'nexthop_type': 'not-attached '
                                        'not-local '
                                        'reachable '
                                        'labeled',
                        'refcount': 1,
                        'rnh_epoch': 1},
                    'vpnv6 unicast':
                        {'af_nexthop_trigger_enable': True,
                        'attached_nexthop': '10.1.3.3',
                        'attached_nexthop_interface': 'Ethernet4/2',
                        'igp_cost': 41,
                        'igp_preference': 110,
                        'igp_route_type': 0,
                        'metric_next_advertise': 'never',
                        'next_hop': '::ffff:3.3.3.3',
                        'nexthop_last_resolved': '5w0d',
                        'nexthop_resolved_using': '3.3.3.3/32',
                        'nexthop_trigger_delay_critical': 3000,
                        'nexthop_trigger_delay_non_critical': 10000,
                        'nexthop_type': 'not-attached '
                                        'not-local '
                                        'reachable '
                                        'labeled',
                        'refcount': 1,
                        'rnh_epoch': 1}}}}}

    golden_output = {'execute.return_value': '''
        Next Hop table for VRF VRF1, address family IPv4 Unicast:
        Next-hop trigger-delay(miliseconds)
          Critical: 2222 Non-critical: 3333

        Nexthop: 0.0.0.0, Refcount: 4, IGP cost: 0
        IGP Route type: 0, IGP preference: 0
        Nexthop is not-attached local unreachable not-labeled
        Nexthop last resolved: never, using 0.0.0.0/0
        Metric next advertise: Never
        RNH epoch: 0

        Next Hop table for VRF VRF1, address family IPv6 Unicast:
        Next-hop trigger-delay(miliseconds)
          Critical: 3000 Non-critical: 10000

        Nexthop: 0::, Refcount: 3, IGP cost: 0
        IGP Route type: 0, IGP preference: 0
        Nexthop is not-attached local unreachable not-labeled
        Nexthop last resolved: never, using 0::/0
        Metric next advertise: Never
        RNH epoch: 0

        Next Hop table for VRF default, address family IPv4 Unicast:
        Next-hop trigger-delay(miliseconds)
          Critical: 3000 Non-critical: 10000

        Next Hop table for VRF default, address family IPv6 Unicast:
        Next-hop trigger-delay(miliseconds)
          Critical: 3000 Non-critical: 10000

        Next Hop table for VRF default, address family VPNv4 Unicast:
        Next-hop trigger-delay(miliseconds)
          Critical: 3000 Non-critical: 10000

        Nexthop: 3.3.3.3, Refcount: 1, IGP cost: 41
        IGP Route type: 0, IGP preference: 110
        Attached nexthop: 10.1.3.3, Interface: Ethernet4/2
        Nexthop is not-attached not-local reachable labeled
        Nexthop last resolved: 5w0d, using 3.3.3.3/32
        Metric next advertise: Never
        RNH epoch: 1

        Next Hop table for VRF default, address family VPNv6 Unicast:
        Next-hop trigger-delay(miliseconds)
          Critical: 3000 Non-critical: 10000

        Nexthop: ::ffff:3.3.3.3, Refcount: 1, IGP cost: 41
        IGP Route type: 0, IGP preference: 110
        Attached nexthop: 10.1.3.3, Interface: Ethernet4/2
        Nexthop is not-attached not-local reachable labeled
        Nexthop last resolved: 5w0d, using 3.3.3.3/32
        Metric next advertise: Never
        RNH epoch: 1

        Next Hop table for VRF default, address family IPv6 Label Unicast:
        Next-hop trigger-delay(miliseconds)
          Critical: 3000 Non-critical: 10000
        '''}

    def test_show_bgp_vrf_all_all_nexthop_database_golden(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output)
        obj = ShowBgpVrfAllAllNextHopDatabase(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output)

    def test_show_bgp_vrf_all_all_nexthop_database_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowBgpVrfAllAllNextHopDatabase(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()


# =============================================
#  Unit test for 'show bgp vrf all all summary'
# =============================================

class test_show_bgp_vrf_all_all_summary(unittest.TestCase):
    
    '''Unit test for 'show bgp vrf all all summary'''

    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output1 = {
        'vrf':
            {'VRF1':
                {'neighbor':
                    {'2.2.2.10':
                        {'address_family':
                            {'ipv4 unicast':
                                {'as': 0,
                                'as_path_entries': '[0/0]',
                                'attribute_entries': '[3/384]',
                                'bgp_table_version': 40,
                                'capable_peers': 0,
                                'clusterlist_entries': '[1/4]',
                                'community_entries': '[0/0]',
                                'config_peers': 1,
                                'dampened_paths': 0,
                                'dampening': True,
                                'history_paths': 0,
                                'inq': 0,
                                'local_as': 100,
                                'msg_rcvd': 0,
                                'msg_sent': 0,
                                'outq': 0,
                                'path': {'memory_usage': 620,
                                        'total_entries': 5},
                                'prefixes':
                                    {'memory_usage': 620,
                                    'total_entries': 5},
                                'route_identifier': '4.4.4.4',
                                'state_pfxrcd': 'Idle',
                                'tbl_ver': 0,
                                'up_down': '5w6d',
                                'v': 4}}}}},
            'default':
                {'neighbor':
                    {'2.2.2.2':
                        {'address_family':
                            {'vpnv4 unicast':
                                {'as': 100,
                                'as_path_entries': '[0/0]',
                                'attribute_entries': '[1/128]',
                                'bgp_table_version': 53,
                                'capable_peers': 1,
                                'clusterlist_entries': '[1/4]',
                                'community_entries': '[0/0]',
                                'config_peers': 1,
                                'inq': 0,
                                'local_as': 100,
                                'msg_rcvd': 108554,
                                'msg_sent': 108566,
                                'outq': 0,
                                'path': {'memory_usage': 620,
                                        'total_entries': 5},
                                'prefixes':
                                    {'memory_usage': 620,
                                    'total_entries': 5},
                                'route_identifier': '1.1.1.1',
                                'state_pfxrcd': '1',
                                'tbl_ver': 53,
                                'up_down': '5w6d',
                                'v': 4},
                            'vpnv6 unicast':
                                {'as': 100,
                                'as_path_entries': '[0/0]',
                                'attribute_entries': '[1/128]',
                                'bgp_table_version': 45,
                                'capable_peers': 1,
                                'clusterlist_entries': '[1/4]',
                                'community_entries': '[0/0]',
                                'config_peers': 1,
                                'inq': 0,
                                'local_as': 100,
                                'msg_rcvd': 108554,
                                'msg_sent': 108566,
                                'outq': 0,
                                'path': {'memory_usage': 544,
                                        'total_entries': 4},
                                'prefixes':
                                    {'memory_usage': 544,
                                    'total_entries': 4},
                                'route_identifier': '1.1.1.1',
                                'state_pfxrcd': '1',
                                'tbl_ver': 45,
                                'up_down': '5w6d',
                                'v': 4}}},
                    '2.2.2.5':
                        {'address_family':
                            {'ipv4 unicast':
                                {'as': 200,
                                'as_path_entries': '[0/0]',
                                'attribute_entries': '[0/0]',
                                'bgp_table_version': 2,
                                'capable_peers': 0,
                                'clusterlist_entries': '[1/4]',
                                'community_entries': '[0/0]',
                                'config_peers': 1,
                                'dampened_paths': 0,
                                'dampening': True,
                                'history_paths': 0,
                                'inq': 0,
                                'local_as': 100,
                                'msg_rcvd': 0,
                                'msg_sent': 0,
                                'outq': 0,
                                'route_identifier': '1.1.1.1',
                                'state_pfxrcd': 'Shut '
                                '(Admin)',
                                'tbl_ver': 0,
                                'up_down': '5w6d',
                                'v': 4}}}}}}}

    golden_output1 = {'execute.return_value': '''
        BGP summary information for VRF VRF1, address family IPv4 Unicast
        BGP router identifier 4.4.4.4, local AS number 100
        BGP table version is 40, IPv4 Unicast config peers 1, capable peers 0
        5 network entries and 5 paths using 620 bytes of memory
        BGP attribute entries [3/384], BGP AS path entries [0/0]
        BGP community entries [0/0], BGP clusterlist entries [1/4]
        Dampening configured, 0 history paths, 0 dampened paths

        Neighbor        V    AS MsgRcvd MsgSent   TblVer  InQ OutQ Up/Down  State/PfxRcd
        2.2.2.10        4     0       0       0        0    0    0     5w6d Idle     

        BGP summary information for VRF VRF1, address family IPv6 Unicast

        BGP summary information for VRF default, address family IPv4 Unicast
        BGP router identifier 1.1.1.1, local AS number 100
        BGP table version is 2, IPv4 Unicast config peers 1, capable peers 0
        0 network entries and 0 paths using 0 bytes of memory
        BGP attribute entries [0/0], BGP AS path entries [0/0]
        BGP community entries [0/0], BGP clusterlist entries [1/4]
        Dampening configured, 0 history paths, 0 dampened paths

        Neighbor        V    AS MsgRcvd MsgSent   TblVer  InQ OutQ Up/Down  State/PfxRcd
        2.2.2.5         4   200       0       0        0    0    0     5w6d Shut (Admin)

        BGP summary information for VRF default, address family IPv6 Unicast

        BGP summary information for VRF default, address family VPNv4 Unicast
        BGP router identifier 1.1.1.1, local AS number 100
        BGP table version is 53, VPNv4 Unicast config peers 1, capable peers 1
        5 network entries and 5 paths using 620 bytes of memory
        BGP attribute entries [1/128], BGP AS path entries [0/0]
        BGP community entries [0/0], BGP clusterlist entries [1/4]

        Neighbor        V    AS MsgRcvd MsgSent   TblVer  InQ OutQ Up/Down  State/PfxRcd
        2.2.2.2         4   100  108554  108566       53    0    0     5w6d 1         

        BGP summary information for VRF default, address family VPNv6 Unicast
        BGP router identifier 1.1.1.1, local AS number 100
        BGP table version is 45, VPNv6 Unicast config peers 1, capable peers 1
        4 network entries and 4 paths using 544 bytes of memory
        BGP attribute entries [1/128], BGP AS path entries [0/0]
        BGP community entries [0/0], BGP clusterlist entries [1/4]

        Neighbor        V    AS MsgRcvd MsgSent   TblVer  InQ OutQ Up/Down  State/PfxRcd
        2.2.2.2         4   100  108554  108566       45    0    0     5w6d 1         

        BGP summary information for VRF default, address family IPv6 Label Unicast
        '''}

    golden_parsed_output2 = {
        'vrf':
            {'default':
                {'neighbor':
                    {'21.0.0.2':
                        {'address_family':
                            {'ipv4 multicast':
                                {'as': 333,
                                'as_path_entries': '[0/0]',
                                'attribute_entries': '[2/312]',
                                'bgp_table_version': 19,
                                'capable_peers': 1,
                                'clusterlist_entries': '[0/0]',
                                'community_entries': '[1/32]',
                                'config_peers': 1,
                                'inq': 0,
                                'local_as': 333,
                                'msg_rcvd': 17,
                                'msg_sent': 15,
                                'outq': 0,
                                'path':
                                    {'memory_usage': 1856,
                                    'total_entries': 8},
                                'prefixes':
                                    {'memory_usage': 1856,
                                    'total_entries': 8},
                                'route_identifier': '21.0.101.1',
                                'state_pfxrcd': '3',
                                'tbl_ver': 19,
                                'up_down': '00:08:22',
                                'v': 4},
                            'ipv4 unicast':
                                {'as': 333,
                                'as_path_entries': '[0/0]',
                                'attribute_entries': '[3/468]',
                                'bgp_table_version': 25,
                                'capable_peers': 2,
                                'clusterlist_entries': '[0/0]',
                                'community_entries': '[1/32]',
                                'config_peers': 2,
                                'inq': 0,
                                'local_as': 333,
                                'msg_rcvd': 17,
                                'msg_sent': 15,
                                'outq': 0,
                                'path':
                                    {'memory_usage': 1524,
                                    'total_entries': 6},
                                'prefixes':
                                    {'memory_usage': 1524,
                                    'total_entries': 6},
                                'route_identifier': '21.0.101.1',
                                'state_pfxrcd': '3',
                                'tbl_ver': 25,
                                'up_down': '00:08:22',
                                'v': 4}}}}}}}

    golden_output2 = {'execute.return_value': '''
        pinxdt-n9kv-2# show bgp vrf all all summary 
        BGP summary information for VRF ac, address family IPv4 Unicast

        BGP summary information for VRF ac, address family IPv6 Unicast

        BGP summary information for VRF default, address family IPv4 Unicast
        BGP router identifier 21.0.101.1, local AS number 333
        BGP table version is 25, IPv4 Unicast config peers 2, capable peers 2
        6 network entries and 11 paths using 1524 bytes of memory
        BGP attribute entries [3/468], BGP AS path entries [0/0]
        BGP community entries [1/32], BGP clusterlist entries [0/0]
        3 received paths for inbound soft reconfiguration
        3 identical, 0 modified, 0 filtered received paths using 0 bytes

        Neighbor        V    AS MsgRcvd MsgSent   TblVer  InQ OutQ Up/Down  State/PfxRcd
        21.0.0.2        4   333      17      15       25    0    0 00:08:22 3         
        fec1::112       4   333      16      13       25    0    0 00:08:17 3         

        BGP summary information for VRF default, address family IPv4 Multicast
        BGP router identifier 21.0.101.1, local AS number 333
        BGP table version is 19, IPv4 Multicast config peers 1, capable peers 1
        8 network entries and 8 paths using 1856 bytes of memory
        BGP attribute entries [2/312], BGP AS path entries [0/0]
        BGP community entries [1/32], BGP clusterlist entries [0/0]
        3 received paths for inbound soft reconfiguration
        3 identical, 0 modified, 0 filtered received paths using 0 bytes

        Neighbor        V    AS MsgRcvd MsgSent   TblVer  InQ OutQ Up/Down  State/PfxRcd
        21.0.0.2        4   333      17      15       19    0    0 00:08:22 3         

        BGP summary information for VRF default, address family IPv6 Unicast

        BGP summary information for VRF default, address family IPv6 Multicast

        BGP summary information for VRF default, address family VPNv4 Unicast

        BGP summary information for VRF default, address family VPNv6 Unicast

        BGP summary information for VRF default, address family IPv4 MVPN

        BGP summary information for VRF default, address family IPv6 MVPN

        BGP summary information for VRF default, address family IPv4 Label Unicast

        BGP summary information for VRF default, address family Link-State

        BGP summary information for VRF vpn1, address family IPv4 Unicast

        BGP summary information for VRF vpn1, address family IPv4 Multicast

        BGP summary information for VRF vpn1, address family IPv6 Unicast

        BGP summary information for VRF vpn1, address family IPv6 Multicast

        BGP summary information for VRF vpn2, address family IPv4 Unicast

        BGP summary information for VRF vpn2, address family IPv6 Unicast
        pinxdt-n9kv-2# 
        '''}

    golden_parsed_output3 = {
        'vrf': 
            {'default': 
                {'neighbor': 
                    {'19.0.101.1': 
                        {'address_family': 
                            {'ipv4 unicast': 
                                {'as': 333,
                                'as_path_entries': '[4/144]',
                                'attribute_entries': '[4/640]',
                                'bgp_table_version': 174,
                                'capable_peers': 3,
                                'clusterlist_entries': '[7/28]',
                                'community_entries': '[2/96]',
                                'config_peers': 3,
                                'dampened_paths': 2,
                                'dampening': True,
                                'history_paths': 0,
                                'inq': 0,
                                'local_as': 333,
                                'msg_rcvd': 29,
                                'msg_sent': 31,
                                'outq': 0,
                                'path': {'memory_usage': 1424,
                                      'total_entries': 5},
                                'prefixes': {'memory_usage': 1424,
                                          'total_entries': 5},
                                'route_identifier': '20.0.0.6',
                                'state_pfxrcd': '3',
                                'tbl_ver': 174,
                                'up_down': '00:20:33',
                                'v': 4}}},
                    '19.0.102.3': 
                        {'address_family': 
                            {'ipv4 unicast': 
                                {'as': 888,
                                'inq': 0,
                                'msg_rcvd': 841,
                                'msg_sent': 28,
                                'outq': 0,
                                'path': {'memory_usage': 1424,
                                'total_entries': 5},
                                'prefixes': {'memory_usage': 1424,
                                  'total_entries': 5},
                                'state_pfxrcd': '2',
                                'tbl_ver': 174,
                                'up_down': '00:20:33',
                                'v': 4}}},
                    '19.0.102.4': 
                        {'address_family': 
                            {'ipv4 multicast': 
                                {'as': 333,
                                'as_path_entries': '[2/56]',
                                'attribute_entries': '[3/480]',
                                'bgp_table_version': 175,
                                'capable_peers': 3,
                                'clusterlist_entries': '[7/28]',
                                'community_entries': '[2/96]',
                                'config_peers': 3,
                                'dampened_paths': 2,
                                'dampening': True,
                                'history_paths': 0,
                                'inq': 0,
                                'local_as': 333,
                                'msg_rcvd': 27,
                                'msg_sent': 31,
                                'outq': 0,
                                'path': {'memory_usage': 1392,
                                        'total_entries': 6},
                                'prefixes': {'memory_usage': 1392,
                                            'total_entries': 6},
                                'route_identifier': '20.0.0.6',
                                'state_pfxrcd': '2',
                                'tbl_ver': 175,
                                'up_down': '00:20:33',
                                'v': 4},
                            'ipv4 unicast': {'as': 333,
                                             'inq': 0,
                                             'msg_rcvd': 27,
                                             'msg_sent': 31,
                                             'outq': 0,
                                             'path': {'memory_usage': 1424,
                                                      'total_entries': 5},
                                             'prefixes': {'memory_usage': 1424,
                                                          'total_entries': 5},
                                             'state_pfxrcd': '2',
                                             'tbl_ver': 174,
                                             'up_down': '00:20:33',
                                             'v': 4},
                            'ipv6 multicast': {'as': 333,
                                               'as_path_entries': '[0/0]',
                                               'attribute_entries': '[1/160]',
                                               'bgp_table_version': 6,
                                               'capable_peers': 2,
                                               'clusterlist_entries': '[7/28]',
                                               'community_entries': '[2/96]',
                                               'config_peers': 5,
                                               'dampened_paths': 0,
                                               'dampening': True,
                                               'history_paths': 0,
                                               'inq': 0,
                                               'local_as': 333,
                                               'msg_rcvd': 27,
                                               'msg_sent': 31,
                                               'outq': 0,
                                               'path': {'memory_usage': 488,
                                                        'total_entries': 2},
                                               'prefixes': {'memory_usage': 488,
                                                            'total_entries': 2},
                                               'route_identifier': '20.0.0.6',
                                               'state_pfxrcd': '0 '
                                                               '(No '
                                                               'Cap)',
                                               'tbl_ver': 0,
                                               'up_down': '00:20:33',
                                               'v': 4},
                            'ipv6 unicast': {'as': 333,
                                             'as_path_entries': '[3/106]',
                                             'attribute_entries': '[3/480]',
                                             'bgp_table_version': 173,
                                             'capable_peers': 2,
                                             'clusterlist_entries': '[7/28]',
                                             'community_entries': '[2/96]',
                                             'config_peers': 5,
                                             'dampened_paths': 2,
                                             'dampening': True,
                                             'history_paths': 0,
                                             'inq': 0,
                                             'local_as': 333,
                                             'msg_rcvd': 27,
                                             'msg_sent': 31,
                                             'outq': 0,
                                             'path': {'memory_usage': 1220,
                                                      'total_entries': 5},
                                             'prefixes': {'memory_usage': 1220,
                                                          'total_entries': 5},
                                             'route_identifier': '20.0.0.6',
                                             'state_pfxrcd': '0 '
                                                             '(No '
                                                             'Cap)',
                                             'tbl_ver': 0,
                                             'up_down': '00:20:33',
                                             'v': 4},
                            'vpnv4 unicast': {'as': 333,
                                              'as_path_entries': '[4/140]',
                                              'attribute_entries': '[4/640]',
                                              'bgp_table_version': 183,
                                              'capable_peers': 3,
                                              'clusterlist_entries': '[7/28]',
                                              'community_entries': '[2/96]',
                                              'config_peers': 3,
                                              'dampened_paths': 2,
                                              'dampening': True,
                                              'history_paths': 0,
                                              'inq': 0,
                                              'local_as': 333,
                                              'msg_rcvd': 27,
                                              'msg_sent': 31,
                                              'outq': 0,
                                              'path': {'memory_usage': 1656,
                                                       'total_entries': 6},
                                              'prefixes': {'memory_usage': 1656,
                                                           'total_entries': 6},
                                              'route_identifier': '20.0.0.6',
                                              'state_pfxrcd': '4',
                                              'tbl_ver': 183,
                                              'up_down': '00:20:33',
                                              'v': 4},
                            'vpnv6 unicast': {'as': 333,
                                              'as_path_entries': '[1/42]',
                                              'attribute_entries': '[2/320]',
                                              'bgp_table_version': 13,
                                              'capable_peers': 3,
                                              'clusterlist_entries': '[7/28]',
                                              'community_entries': '[2/96]',
                                              'config_peers': 3,
                                              'dampened_paths': 0,
                                              'dampening': True,
                                              'history_paths': 0,
                                              'inq': 0,
                                              'local_as': 333,
                                              'msg_rcvd': 27,
                                              'msg_sent': 31,
                                              'outq': 0,
                                              'path': {'memory_usage': 928,
                                                       'total_entries': 4},
                                              'prefixes': {'memory_usage': 928,
                                                           'total_entries': 4},
                                              'route_identifier': '20.0.0.6',
                                              'state_pfxrcd': '0',
                                              'tbl_ver': 173,
                                              'up_down': '00:20:33',
                                              'v': 4}}}}},
            'vpn1': 
                {'neighbor': 
                    {'19.0.103.1': 
                        {'address_family': 
                            {'ipv4 multicast': {'as': 333,
                                            'as_path_entries': '[0/0]',
                                            'attribute_entries': '[0/0]',
                                            'bgp_table_version': 2,
                                            'capable_peers': 0,
                                            'clusterlist_entries': '[7/28]',
                                            'community_entries': '[2/96]',
                                            'config_peers': 1,
                                            'inq': 0,
                                            'local_as': 333,
                                            'msg_rcvd': 0,
                                            'msg_sent': 0,
                                            'outq': 0,
                                            'route_identifier': '0.0.0.0',
                                            'state_pfxrcd': 'Idle',
                                            'tbl_ver': 0,
                                            'up_down': '00:20:35',
                                            'v': 4},
                            'ipv4 unicast': {'as': 333,
                                          'as_path_entries': '[2/80]',
                                          'attribute_entries': '[2/320]',
                                          'bgp_table_version': 9,
                                          'capable_peers': 0,
                                          'clusterlist_entries': '[7/28]',
                                          'community_entries': '[2/96]',
                                          'config_peers': 1,
                                          'dampened_paths': 2,
                                          'dampening': True,
                                          'history_paths': 0,
                                          'inq': 0,
                                          'local_as': 333,
                                          'msg_rcvd': 0,
                                          'msg_sent': 0,
                                          'outq': 0,
                                          'path': {'memory_usage': 300,
                                                   'total_entries': 3},
                                          'prefixes': {'memory_usage': 300,
                                                       'total_entries': 3},
                                          'route_identifier': '0.0.0.0',
                                          'state_pfxrcd': 'Idle',
                                          'tbl_ver': 0,
                                          'up_down': '00:20:35',
                                          'v': 4},
                            'ipv6 multicast': {'as': 333,
                                            'as_path_entries': '[0/0]',
                                            'attribute_entries': '[0/0]',
                                            'bgp_table_version': 2,
                                            'capable_peers': 0,
                                            'clusterlist_entries': '[7/28]',
                                            'community_entries': '[2/96]',
                                            'config_peers': 1,
                                            'inq': 0,
                                            'local_as': 333,
                                            'msg_rcvd': 0,
                                            'msg_sent': 0,
                                            'outq': 0,
                                            'route_identifier': '0.0.0.0',
                                            'state_pfxrcd': 'Idle',
                                            'tbl_ver': 0,
                                            'up_down': '00:20:35',
                                            'v': 4},
                            'ipv6 unicast': {'as': 333,
                                          'as_path_entries': '[0/0]',
                                          'attribute_entries': '[0/0]',
                                          'bgp_table_version': 2,
                                          'capable_peers': 0,
                                          'clusterlist_entries': '[7/28]',
                                          'community_entries': '[2/96]',
                                          'config_peers': 1,
                                          'inq': 0,
                                          'local_as': 333,
                                          'msg_rcvd': 0,
                                          'msg_sent': 0,
                                          'outq': 0,
                                          'route_identifier': '0.0.0.0',
                                          'state_pfxrcd': 'Idle',
                                          'tbl_ver': 0,
                                          'up_down': '00:20:35',
                                          'v': 4}}}}}}}

    golden_output3 = {'execute.return_value': '''
        show bgp vrf all all summary

        BGP summary information for VRF default, address family IPv4 Unicast
        BGP router identifier 20.0.0.6, local AS number 333
        BGP table version is 174, IPv4 Unicast config peers 3, capable peers 3
        5 network entries and 7 paths using 1424 bytes of memory
        BGP attribute entries [4/640], BGP AS path entries [4/144]
        BGP community entries [2/96], BGP clusterlist entries [7/28]
        Dampening configured, 0 history paths, 2 dampened paths

        Neighbor        V    AS MsgRcvd MsgSent   TblVer  InQ OutQ Up/Down  State/PfxRcd
        19.0.101.1      4   333      29      31      174    0    0 00:20:33 3         
        19.0.102.3      4   888     841      28      174    0    0 00:20:33 2         
        19.0.102.4      4   333      27      31      174    0    0 00:20:33 2         

        BGP summary information for VRF default, address family IPv4 Multicast
        BGP router identifier 20.0.0.6, local AS number 333
        BGP table version is 175, IPv4 Multicast config peers 3, capable peers 3
        6 network entries and 6 paths using 1392 bytes of memory
        BGP attribute entries [3/480], BGP AS path entries [2/56]
        BGP community entries [2/96], BGP clusterlist entries [7/28]
        Dampening configured, 0 history paths, 2 dampened paths

        Neighbor        V    AS MsgRcvd MsgSent   TblVer  InQ OutQ Up/Down  State/PfxRcd
        19.0.101.1      4   333      29      31      175    0    0 00:20:33 2         
        19.0.102.3      4   888     841      28      175    0    0 00:20:33 2         
        19.0.102.4      4   333      27      31      175    0    0 00:20:33 2         

        BGP summary information for VRF default, address family IPv6 Unicast
        BGP router identifier 20.0.0.6, local AS number 333
        BGP table version is 173, IPv6 Unicast config peers 5, capable peers 2
        5 network entries and 5 paths using 1220 bytes of memory
        BGP attribute entries [3/480], BGP AS path entries [3/106]
        BGP community entries [2/96], BGP clusterlist entries [7/28]
        Dampening configured, 0 history paths, 2 dampened paths

        Neighbor        V    AS MsgRcvd MsgSent   TblVer  InQ OutQ Up/Down  State/PfxRcd
        19.0.101.1      4   333      29      31        0    0    0 00:20:33 0 (No Cap)
        19.0.102.3      4   888     841      28        0    0    0 00:20:33 0 (No Cap)
        19.0.102.4      4   333      27      31        0    0    0 00:20:33 0 (No Cap)
        fec0::1002      4   333      26      26      173    0    0 00:20:33 3         
        fec0::2002      4   888     187      25      173    0    0 00:20:33 2         

        BGP summary information for VRF default, address family IPv6 Multicast
        BGP router identifier 20.0.0.6, local AS number 333
        BGP table version is 6, IPv6 Multicast config peers 5, capable peers 2
        2 network entries and 2 paths using 488 bytes of memory
        BGP attribute entries [1/160], BGP AS path entries [0/0]
        BGP community entries [2/96], BGP clusterlist entries [7/28]
        Dampening configured, 0 history paths, 0 dampened paths

        Neighbor        V    AS MsgRcvd MsgSent   TblVer  InQ OutQ Up/Down  State/PfxRcd
        19.0.101.1      4   333      29      31        0    0    0 00:20:33 0 (No Cap)
        19.0.102.3      4   888     841      28        0    0    0 00:20:33 0 (No Cap)
        19.0.102.4      4   333      27      31        0    0    0 00:20:33 0 (No Cap)
        fec0::1002      4   333      26      26        6    0    0 00:20:33 2         
        fec0::2002      4   888     187      25        6    0    0 00:20:33 0         

        BGP summary information for VRF default, address family VPNv4 Unicast
        BGP router identifier 20.0.0.6, local AS number 333
        BGP table version is 183, VPNv4 Unicast config peers 3, capable peers 3
        6 network entries and 8 paths using 1656 bytes of memory
        BGP attribute entries [4/640], BGP AS path entries [4/140]
        BGP community entries [2/96], BGP clusterlist entries [7/28]
        Dampening configured, 0 history paths, 2 dampened paths

        Neighbor        V    AS MsgRcvd MsgSent   TblVer  InQ OutQ Up/Down  State/PfxRcd
        19.0.101.1      4   333      29      31      183    0    0 00:20:33 2         
        19.0.102.3      4   888     841      28      183    0    0 00:20:33 2         
        19.0.102.4      4   333      27      31      183    0    0 00:20:33 4         

        BGP summary information for VRF default, address family VPNv6 Unicast
        BGP router identifier 20.0.0.6, local AS number 333
        BGP table version is 13, VPNv6 Unicast config peers 3, capable peers 3
        4 network entries and 4 paths using 976 bytes of memory
        BGP attribute entries [2/320], BGP AS path entries [1/42]
        BGP community entries [2/96], BGP clusterlist entries [7/28]
        Dampening configured, 0 history paths, 0 dampened paths

        Neighbor        V    AS MsgRcvd MsgSent   TblVer  InQ OutQ Up/Down  State/PfxRcd
        19.0.101.1      4   333      29      31       13    0    0 00:20:33 2         
        19.0.102.3      4   888     841      28       13    0    0 00:20:33 2         
        19.0.102.4      4   333      27      31       13    0    0 00:20:33 0         

        BGP summary information for VRF default, address family Link-State
        BGP router identifier 20.0.0.6, local AS number 333
        BGP table version is 173, Link-State config peers 5, capable peers 3
        4 network entries and 4 paths using 928 bytes of memory
        BGP attribute entries [2/320], BGP AS path entries [2/84]
        BGP community entries [2/96], BGP clusterlist entries [7/28]
        Dampening configured, 0 history paths, 2 dampened paths

        Neighbor        V    AS MsgRcvd MsgSent   TblVer  InQ OutQ Up/Down  State/PfxRcd
        19.0.101.1      4   333      29      31      173    0    0 00:20:33 2         
        19.0.102.3      4   888     841      28      173    0    0 00:20:33 2         
        19.0.102.4      4   333      27      31      173    0    0 00:20:33 0         
        fec0::1002      4   333      26      26        0    0    0 00:20:33 0 (No Cap)
        fec0::2002      4   888     187      25        0    0    0 00:20:33 0 (No Cap)

        BGP summary information for VRF vpn1, address family IPv4 Unicast
        BGP router identifier 0.0.0.0, local AS number 333
        BGP table version is 9, IPv4 Unicast config peers 1, capable peers 0
        3 network entries and 3 paths using 300 bytes of memory
        BGP attribute entries [2/320], BGP AS path entries [2/80]
        BGP community entries [2/96], BGP clusterlist entries [7/28]

        Neighbor        V    AS MsgRcvd MsgSent   TblVer  InQ OutQ Up/Down  State/PfxRcd
        19.0.103.1      4   333       0       0        0    0    0 00:20:35 Idle     

        BGP summary information for VRF vpn1, address family IPv4 Multicast
        BGP router identifier 0.0.0.0, local AS number 333
        BGP table version is 2, IPv4 Multicast config peers 1, capable peers 0
        0 network entries and 0 paths using 0 bytes of memory
        BGP attribute entries [0/0], BGP AS path entries [0/0]
        BGP community entries [2/96], BGP clusterlist entries [7/28]

        Neighbor        V    AS MsgRcvd MsgSent   TblVer  InQ OutQ Up/Down  State/PfxRcd
        19.0.103.1      4   333       0       0        0    0    0 00:20:35 Idle     

        BGP summary information for VRF vpn1, address family IPv6 Unicast
        BGP router identifier 0.0.0.0, local AS number 333
        BGP table version is 2, IPv6 Unicast config peers 1, capable peers 0
        0 network entries and 0 paths using 0 bytes of memory
        BGP attribute entries [0/0], BGP AS path entries [0/0]
        BGP community entries [2/96], BGP clusterlist entries [7/28]

        Neighbor        V    AS MsgRcvd MsgSent   TblVer  InQ OutQ Up/Down  State/PfxRcd
        19.0.103.1      4   333       0       0        0    0    0 00:20:35 Idle     

        BGP summary information for VRF vpn1, address family IPv6 Multicast
        BGP router identifier 0.0.0.0, local AS number 333
        BGP table version is 2, IPv6 Multicast config peers 1, capable peers 0
        0 network entries and 0 paths using 0 bytes of memory
        BGP attribute entries [0/0], BGP AS path entries [0/0]
        BGP community entries [2/96], BGP clusterlist entries [7/28]

        Neighbor        V    AS MsgRcvd MsgSent   TblVer  InQ OutQ Up/Down  State/PfxRcd
        19.0.103.1      4   333       0       0        0    0    0 00:20:35 Idle     

        BGP summary information for VRF vpn2, address family IPv4 Unicast

        BGP summary information for VRF vpn2, address family IPv6 Unicast
        '''}

    def test_show_bgp_vrf_all_all_summary_golden1(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output1)
        obj = ShowBgpVrfAllAllSummary(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output1)

    def test_show_bgp_vrf_all_all_summary_golden2(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output2)
        obj = ShowBgpVrfAllAllSummary(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output2)

    def test_show_bgp_vrf_all_all_summary_golden3(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output3)
        obj = ShowBgpVrfAllAllSummary(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output3)

    def test_show_bgp_vrf_all_all_summary_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowBgpVrfAllAllSummary(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()


# ==================================================================
#  Unit test for 'show bgp process vrf all all dampening parameters'
# ==================================================================

class TestShowBgpVrfAllAllDampeningParameters(unittest.TestCase):
    ''' unittest for "show bgp vrf all all dampening parameters"
    '''
    device = Device(name='aDevice')
    device1 = Device(name='bDevice')
    empty_output = {'execute.return_value': ''}
    golden_parsed_output = {'vrf':
                            {'VRF1':
                             {'address_family':
                              {'ipv4 unicast':
                               {'dampening': 'True',
                                'dampening_route_map': 'dampening1',
                                'dampening_half_life_time': '45',
                                'dampening_reuse_time': '10000',
                                'dampening_suppress_time': '20000',
                                'dampening_max_suppress_time': '255',
                                'dampening_max_suppress_penalty': '507968'},
                               'ipv6 unicast':
                               {'dampening': 'True',
                                'dampening_route_map': 'dampening2',
                                'dampening_half_life_time': '45',
                                'dampening_reuse_time': '9999',
                                'dampening_suppress_time': '19999',
                                'dampening_max_suppress_time': '255',
                                'dampening_max_suppress_penalty': '507917'}}},
                             'default':
                             {'address_family':
                              {'ipv4 unicast':
                               {'dampening': 'True',
                                'dampening_half_life_time': '45',
                                'dampening_reuse_time': '1111',
                                'dampening_suppress_time': '2222',
                                'dampening_max_suppress_time': '255',
                                'dampening_max_suppress_penalty': '56435'},
                              'vpnv4 unicast':
                               {'dampening': 'True',
                                'route_distinguisher':
                                 {'1:100':
                                  {'rd_vrf': 'vpn1',
                                   'dampening_half_life_time': '1 mins',
                                   'dampening_reuse_time': '10',
                                   'dampening_suppress_time': '30',
                                   'dampening_max_suppress_time': '2 mins',
                                   'dampening_max_suppress_penalty': '40'}}}}}}}

    golden_output = {'execute.return_value': '''
        Route Flap Dampening Parameters for VRF VRF1 Address family IPv4 Unicast:

        Dampening policy configured: dampening1

        Half-life time                 : 45
        Suppress penalty               : 20000
        Reuse penalty                  : 10000
        Max suppress time              : 255
        Max suppress penalty           : 507968

        Route Flap Dampening Parameters for VRF VRF1 Address family IPv6 Unicast:

        Dampening policy configured: dampening2

        Half-life time                 : 45
        Suppress penalty               : 19999
        Reuse penalty                  : 9999
        Max suppress time              : 255
        Max suppress penalty           : 507917

        Route Flap Dampening Parameters for VRF default Address family IPv4 Unicast:

        Configured values in use:

        Half-life time                 : 45
        Suppress penalty               : 2222
        Reuse penalty                  : 1111
        Max suppress time              : 255
        Max suppress penalty           : 56435

        Route Flap Dampening Parameters for VRF default Address family VPNv4 Unicast:
        Route Distinguisher: 1:100    (VRF vpn1)

        Configured values in use:

        Half-life time                 : 1 mins
        Suppress penalty               : 30
        Reuse penalty                  : 10
        Max suppress time              : 2 mins
        Max suppress penalty           : 40
        '''}

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        bgp_obj = ShowBgpVrfAllAllDampeningParameters(device=self.device)
        parsed_output = bgp_obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)

    def test_empty(self):
        self.device1 = Mock(**self.empty_output)
        bgp_obj = ShowBgpVrfAllAllDampeningParameters(device=self.device1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = bgp_obj.parse()


# ==========================================================================
# Unit test for 'show bgp vrf <WORD> all neighbors <WORD> advertised-routes'
# ==========================================================================

class test_show_bgp_vrf_all_neighbors_advertised_routes(unittest.TestCase):
    
    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output = {
        'vrf':
            {'default':
                {'neighbor':
                    {'2.2.2.10':
                        {'address_family':
                            {'ipv4 label unicast': 
                                {'bgp_table_version': 28,
                                'local_router_id': '21.0.101.1'},
                            'ipv4 multicast':
                                {'advertised':
                                    {'1.1.1.0/24':
                                        {'index':
                                            {1:
                                                {'next_hop': '0.0.0.0',
                                                'localprf': 100,
                                                'metric': 3333,
                                                'origin_codes': '?',
                                                'path_type': 'r',
                                                'status_codes': '*>',
                                                'weight': 32768}}},
                                    '1.2.1.0/24':
                                        {'index':
                                            {1:
                                                {'next_hop': '0.0.0.0',
                                                'localprf': 100,
                                                'metric': 3333,
                                                'origin_codes': '?',
                                                'path_type': 'r',
                                                'status_codes': '*>',
                                                'weight': 32768}}},
                                    '102.0.0.0/8':
                                        {'index':
                                            {1:
                                                {'next_hop': '0.0.0.0',
                                                'localprf': 100,
                                                'metric': 3333,
                                                'origin_codes': '?',
                                                'path_type': 'r',
                                                'status_codes': '*>',
                                                'weight': 32768}}},
                                    '2.0.0.0/8':
                                        {'index':
                                            {1:
                                                {'next_hop': '0.0.0.0',
                                                'localprf': 100,
                                                'metric': 3333,
                                                'origin_codes': '?',
                                                'path_type': 'r',
                                                'status_codes': '*>',
                                                'weight': 32768}}},
                                    '202.0.0.0/8':
                                        {'index':
                                            {1:
                                                {'next_hop': '0.0.0.0',
                                                'localprf': 100,
                                                'metric': 3333,
                                                'origin_codes': '?',
                                                'path_type': 'r',
                                                'status_codes': '*>',
                                                'weight': 32768}}}},
                                'bgp_table_version': 19,
                                'local_router_id': '21.0.101.1'},
                            'ipv4 mvpn': 
                                {'bgp_table_version': 2,
                                'local_router_id': '21.0.101.1'},
                            'ipv4 unicast':
                                {'advertised':
                                    {'1.1.1.0/24':
                                        {'index':
                                            {1:
                                                {'next_hop': '0.0.0.0',
                                                'localprf': 100,
                                                'origin_codes': 'i',
                                                'path_type': 'l',
                                                'status_codes': '*>',
                                                'weight': 32768}}},
                                    '1.3.1.0/24':
                                        {'index':
                                            {1:
                                                {'next_hop': '0.0.0.0',
                                                'localprf': 100,
                                                'metric': 4444,
                                                'origin_codes': '?',
                                                'path_type': 'r',
                                                'status_codes': '*>',
                                                'weight': 32768}}},
                                    '1.3.2.0/24':
                                        {'index':
                                            {1:
                                                {'next_hop': '0.0.0.0',
                                                'localprf': 100,
                                                'metric': 4444,
                                                'origin_codes': '?',
                                                'path_type': 'r',
                                                'status_codes': '*>',
                                                'weight': 32768}}},
                                    '104.0.0.0/8':
                                        {'index':
                                            {1:
                                                {'next_hop': '0.0.0.0',
                                                'localprf': 100,
                                                'metric': 4444,
                                                'origin_codes': '?',
                                                'path_type': 'r',
                                                'status_codes': '*>',
                                                'weight': 32768}}},
                                    '204.0.0.0/8':
                                        {'index':
                                            {1:
                                                {'next_hop': '0.0.0.0',
                                                'localprf': 100,
                                                'metric': 4444,
                                                'origin_codes': '?',
                                                'path_type': 'r',
                                                'status_codes': '*>',
                                                'weight': 32768}}}},
                                'bgp_table_version': 25,
                                'local_router_id': '21.0.101.1'},
                            'ipv6 multicast': 
                                {'bgp_table_version': 2,
                                'local_router_id': '21.0.101.1'},
                            'ipv6 mvpn': 
                                {'bgp_table_version': 2,
                                'local_router_id': '21.0.101.1'},
                            'ipv6 unicast': 
                                {'bgp_table_version': 7,
                                'local_router_id': '21.0.101.1'},
                            'link-state': 
                                {'bgp_table_version': 2,
                                'local_router_id': '21.0.101.1'},
                            'vpnv4 unicast': 
                                {'bgp_table_version': 23,
                                'local_router_id': '21.0.101.1'},
                            'vpnv4 unicast RD 1:100': {
                                'bgp_table_version': 23,
                                'default_vrf': 'vpn1',
                                'local_router_id': '21.0.101.1',
                                'route_distinguisher': '1:100',
                                'advertised': {
                                    '1.1.1.0/24':{
                                        'index': {
                                            1: {
                                                'next_hop': '0.0.0.0',
                                                'localprf': 100,
                                                'metric': 3333,
                                                'origin_codes': '?',
                                                'path_type': 'r',
                                                'status_codes': '*>',
                                                'weight': 32768}}},
                                    '1.2.1.0/24':{
                                        'index': {
                                            1: {
                                                'next_hop': '0.0.0.0',
                                                'localprf': 100,
                                                'metric': 3333,
                                                'origin_codes': '?',
                                                'path_type': 'r',
                                                'status_codes': '*>',
                                                'weight': 32768}}}}},
                            'vpnv4 unicast RD 2:100': {
                                'bgp_table_version': 23,
                                'default_vrf': 'vpn2',
                                'local_router_id': '21.0.101.1',
                                'route_distinguisher': '2:100',
                                'advertised': {
                                    '1.1.1.0/24':{
                                        'index': {
                                            1: {
                                                'next_hop': '0.0.0.0',
                                                'localprf': 100,
                                                'metric': 3333,
                                                'origin_codes': '?',
                                                'path_type': 'r',
                                                'status_codes': '*>',
                                                'weight': 32768}}},
                                    '1.2.1.0/24':{
                                        'index': {
                                            1: {
                                                'next_hop': '0.0.0.0',
                                                'localprf': 100,
                                                'metric': 3333,
                                                'origin_codes': '?',
                                                'path_type': 'r',
                                                'status_codes': '*>',
                                                'weight': 32768}}}}},
                            'vpnv6 unicast': 
                                {'bgp_table_version': 7,
                                'local_router_id': '21.0.101.1'},
                            'vpnv6 unicast RD 1:100': 
                                {'bgp_table_version': 7,
                                'default_vrf': 'vpn1',
                                'local_router_id': '21.0.101.1',
                                'route_distinguisher': '1:100'},
                            'vpnv6 unicast RD 2:100': 
                                {'bgp_table_version': 7,
                                'default_vrf': 'vpn2',
                                'local_router_id': '21.0.101.1',
                                'route_distinguisher': '2:100'}}}}}}}

    golden_output = {'execute.return_value': '''
        pinxdt-n9kv-2# show bgp vrf default all neighbors 2.2.2.10 advertised-routes 
        Can't find neighbor 2.2.2.10

        Peer 2.2.2.10 routes for address family IPv4 Unicast:
        BGP table version is 25, Local Router ID is 21.0.101.1
        Status: s-suppressed, x-deleted, S-stale, d-dampened, h-history, *-valid, >-best
        Path type: i-internal, e-external, c-confed, l-local, a-aggregate, r-redist, I-injected
        Origin codes: i - IGP, e - EGP, ? - incomplete, | - multipath, & - backup

           Network            Next Hop            Metric     LocPrf     Weight Path
        *>l1.1.1.0/24         0.0.0.0                           100      32768 i
        *>r1.3.1.0/24         0.0.0.0               4444        100      32768 ?
        *>r1.3.2.0/24         0.0.0.0               4444        100      32768 ?
        *>r104.0.0.0/8        0.0.0.0               4444        100      32768 ?
        *>r204.0.0.0/8        0.0.0.0               4444        100      32768 ?


        Peer 2.2.2.10 routes for address family IPv4 Multicast:
        BGP table version is 19, Local Router ID is 21.0.101.1
        Status: s-suppressed, x-deleted, S-stale, d-dampened, h-history, *-valid, >-best
        Path type: i-internal, e-external, c-confed, l-local, a-aggregate, r-redist, I-injected
        Origin codes: i - IGP, e - EGP, ? - incomplete, | - multipath, & - backup

           Network            Next Hop            Metric     LocPrf     Weight Path
        *>r1.1.1.0/24         0.0.0.0               3333        100      32768 ?
        *>r1.2.1.0/24         0.0.0.0               3333        100      32768 ?
        *>r2.0.0.0/8          0.0.0.0               3333        100      32768 ?
        *>r102.0.0.0/8        0.0.0.0               3333        100      32768 ?
        *>r202.0.0.0/8        0.0.0.0               3333        100      32768 ?


        Peer 2.2.2.10 routes for address family IPv6 Unicast:
        BGP table version is 7, Local Router ID is 21.0.101.1
        Status: s-suppressed, x-deleted, S-stale, d-dampened, h-history, *-valid, >-best
        Path type: i-internal, e-external, c-confed, l-local, a-aggregate, r-redist, I-injected
        Origin codes: i - IGP, e - EGP, ? - incomplete, | - multipath, & - backup

           Network            Next Hop            Metric     LocPrf     Weight Path


        Peer 2.2.2.10 routes for address family IPv6 Multicast:
        BGP table version is 2, Local Router ID is 21.0.101.1
        Status: s-suppressed, x-deleted, S-stale, d-dampened, h-history, *-valid, >-best
        Path type: i-internal, e-external, c-confed, l-local, a-aggregate, r-redist, I-injected
        Origin codes: i - IGP, e - EGP, ? - incomplete, | - multipath, & - backup

           Network            Next Hop            Metric     LocPrf     Weight Path

        Peer 2.2.2.10 routes for address family VPNv4 Unicast:
        BGP table version is 23, Local Router ID is 21.0.101.1
        Status: s-suppressed, x-deleted, S-stale, d-dampened, h-history, *-valid, >-best
        Path type: i-internal, e-external, c-confed, l-local, a-aggregate, r-redist, I-injected
        Origin codes: i - IGP, e - EGP, ? - incomplete, | - multipath, & - backup

           Network            Next Hop            Metric     LocPrf     Weight Path
        Route Distinguisher: 1:100    (VRF vpn1)
        *>r1.1.1.0/24         0.0.0.0               3333        100      32768 ?
        *>r1.2.1.0/24         0.0.0.0               3333        100      32768 ?

        Route Distinguisher: 2:100    (VRF vpn2)
        *>r1.1.1.0/24         0.0.0.0               3333        100      32768 ?
        *>r1.2.1.0/24         0.0.0.0               3333        100      32768 ?


        Peer 2.2.2.10 routes for address family VPNv6 Unicast:
        BGP table version is 7, Local Router ID is 21.0.101.1
        Status: s-suppressed, x-deleted, S-stale, d-dampened, h-history, *-valid, >-best
        Path type: i-internal, e-external, c-confed, l-local, a-aggregate, r-redist, I-injected
        Origin codes: i - IGP, e - EGP, ? - incomplete, | - multipath, & - backup

           Network            Next Hop            Metric     LocPrf     Weight Path
        Route Distinguisher: 1:100    (VRF vpn1)

        Route Distinguisher: 2:100    (VRF vpn2)


        Peer 2.2.2.10 routes for address family IPv4 MVPN:
        BGP table version is 2, Local Router ID is 21.0.101.1
        Status: s-suppressed, x-deleted, S-stale, d-dampened, h-history, *-valid, >-best
        Path type: i-internal, e-external, c-confed, l-local, a-aggregate, r-redist, I-injected
        Origin codes: i - IGP, e - EGP, ? - incomplete, | - multipath, & - backup

           Network            Next Hop            Metric     LocPrf     Weight Path

        Peer 2.2.2.10 routes for address family IPv6 MVPN:
        BGP table version is 2, Local Router ID is 21.0.101.1
        Status: s-suppressed, x-deleted, S-stale, d-dampened, h-history, *-valid, >-best
        Path type: i-internal, e-external, c-confed, l-local, a-aggregate, r-redist, I-injected
        Origin codes: i - IGP, e - EGP, ? - incomplete, | - multipath, & - backup

           Network            Next Hop            Metric     LocPrf     Weight Path

        Peer 2.2.2.10 routes for address family IPv4 Label Unicast:
        BGP table version is 28, Local Router ID is 21.0.101.1
        Status: s-suppressed, x-deleted, S-stale, d-dampened, h-history, *-valid, >-best
        Path type: i-internal, e-external, c-confed, l-local, a-aggregate, r-redist, I-injected
        Origin codes: i - IGP, e - EGP, ? - incomplete, | - multipath, & - backup

           Network            Next Hop            Metric     LocPrf     Weight Path


        Peer 2.2.2.10 routes for address family Link-State:
        BGP table version is 2, Local Router ID is 21.0.101.1
        Status: s-suppressed, x-deleted, S-stale, d-dampened, h-history, *-valid, >-best
        Path type: i-internal, e-external, c-confed, l-local, a-aggregate, r-redist, I-injected
        Origin codes: i - IGP, e - EGP, ? - incomplete, | - multipath, & - backup

           Network            Next Hop            Metric     LocPrf     Weight Path
        Can't find neighbor 21.0.0.2
        Can't find neighbor 21.0.0.2
        pinxdt-n9kv-2# 
        '''}

    golden_parsed_output2 = {
        'vrf': 
            {'default': 
                {'neighbor': 
                    {'19.0.102.3': 
                        {'address_family': 
                            {'ipv4 multicast': 
                                {'advertised': 
                                    {'1.2.1.0/24': {'index': {1: {'localprf': 100,
                                                               'next_hop': '19.0.101.1',
                                                               'origin_codes': 'i',
                                                               'path': '2 '
                                                                       '3 '
                                                                       '4',
                                                               'path_type': 'i',
                                                               'status_codes': '*>',
                                                               'weight': 0}}},
                                    '1.2.2.0/24': {'index': {1: {'localprf': 100,
                                                               'next_hop': '19.0.101.1',
                                                               'origin_codes': 'i',
                                                               'path': '2 '
                                                                       '3 '
                                                                       '4',
                                                               'path_type': 'i',
                                                               'status_codes': '*>',
                                                               'weight': 0}}},
                                    '1.4.1.0/24': {'index': {1: {'localprf': 100,
                                                               'next_hop': '19.0.102.4',
                                                               'origin_codes': 'i',
                                                               'path': '2 '
                                                                       '3 '
                                                                       '4',
                                                               'path_type': 'i',
                                                               'status_codes': '*>',
                                                               'weight': 0}}},
                                    '1.4.2.0/24': {'index': {1: {'localprf': 100,
                                                               'next_hop': '19.0.102.4',
                                                               'origin_codes': 'i',
                                                               'path': '2 '
                                                                       '3 '
                                                                       '4',
                                                               'path_type': 'i',
                                                               'status_codes': '*>',
                                                               'weight': 0}}},
                                    '1.5.2.0/24': {'index': {1: {'localprf': 500,
                                                               'metric': 5555,
                                                               'next_hop': '19.0.102.4',
                                                               'origin_codes': 'i',
                                                               'path': '2 '
                                                                       '3 '
                                                                       '4 '
                                                                       '5 '
                                                                       '6 '
                                                                       '7 '
                                                                       '8 '
                                                                       '9 '
                                                                       '10 '
                                                                       '11 '
                                                                       '12',
                                                               'path_type': 'i',
                                                               'status_codes': '*>',
                                                               'weight': 32788}}}},
                                'bgp_table_version': 175,
                                'local_router_id': '20.0.0.6'},
                            'ipv4 unicast': 
                                {'advertised': 
                                    {'1.1.1.0/24': {'index': {1: {'localprf': 100,
                                                                 'next_hop': '19.0.102.4',
                                                                 'origin_codes': 'i',
                                                                 'path': '{62112 '
                                                                         '33492 '
                                                                         '4872 '
                                                                         '41787 '
                                                                         '13166 '
                                                                         '50081 '
                                                                         '21461 '
                                                                         '58376 '
                                                                         '29755 '
                                                                         '1135}',
                                                                 'path_type': 'i',
                                                                 'status_codes': '*>',
                                                                 'weight': 0}}},
                                    '1.1.2.0/24': {'index': {1: {'localprf': 100,
                                                                 'next_hop': '19.0.102.4',
                                                                 'origin_codes': 'i',
                                                                 'path': '{62112 '
                                                                         '33492 '
                                                                         '4872 '
                                                                         '41787 '
                                                                         '13166 '
                                                                         '50081 '
                                                                         '21461 '
                                                                         '58376 '
                                                                         '29755 '
                                                                         '1135}',
                                                                 'path_type': 'i',
                                                                 'status_codes': '*>',
                                                                 'weight': 0}}},
                                    '1.5.0.0/24': {'index': {1: {'metric': 100,
                                                                 'next_hop': '19.0.102.3',
                                                                 'origin_codes': 'i',
                                                                 'path': '10 '
                                                                         '20 '
                                                                         '30 '
                                                                         '40 '
                                                                         '50 '
                                                                         '60 '
                                                                         '70 '
                                                                         '80 '
                                                                         '90',
                                                                 'path_type': 'i',
                                                                 'status_codes': '*>',
                                                                 'weight': 0}}},
                                    '1.6.0.0/16': {'index': {1: {'localprf': 100,
                                                                 'next_hop': '19.0.101.1',
                                                                 'origin_codes': 'i',
                                                                 'path': '10 '
                                                                         '20 '
                                                                         '30 '
                                                                         '40 '
                                                                         '50 '
                                                                         '60 '
                                                                         '70 '
                                                                         '80 '
                                                                         '90',
                                                                 'path_type': 'i',
                                                                 'status_codes': '*>',
                                                                 'weight': 0}}}},
                                'bgp_table_version': 174,
                                'local_router_id': '20.0.0.6'},
                            'ipv6 multicast': 
                                {'bgp_table_version': 6,
                                'local_router_id': '20.0.0.6'},
                            'ipv6 unicast': 
                                {'bgp_table_version': 173,
                                'local_router_id': '20.0.0.6'},
                            'link-state': 
                                {'advertised': 
                                    {'[2]:[77][7,0][9.9.9.9,1,151587081][29.1.1.1,22][19.0.101.1,29.0.1.30]/616': 
                                        {'index': 
                                            {1: 
                                                {'localprf': 100,
                                                'metric': 4444,
                                                'next_hop': '19.0.101.1',
                                                'origin_codes': 'i',
                                                'path': '3 '
                                                        '10 '
                                                        '20 '
                                                        '30 '
                                                        '40 '
                                                        '50 '
                                                        '60 '
                                                        '70 '
                                                        '80 '
                                                        '90',
                                                'path_type': 'i',
                                                'status_codes': '*>',
                                                'weight': 0},
                                            2: 
                                                {'localprf': 100,
                                                'metric': 4444,
                                                'next_hop': '19.0.102.3',
                                                'origin_codes': 'i',
                                                'path': '3 '
                                                        '10 '
                                                        '20 '
                                                        '30 '
                                                        '40 '
                                                        '50 '
                                                        '60 '
                                                        '70 '
                                                        '80 '
                                                        '90',
                                                'path_type': 'i',
                                                'status_codes': '*>',
                                                'weight': 0}}},
                                    '[2]:[77][7,0][9.9.9.9,2,151587081][29.1.1.1,22][19.0.101.1,29.0.1.31]/616': 
                                        {'index': 
                                            {1: 
                                                {'localprf': 200,
                                                'metric': 555,
                                                'next_hop': '19.0.103.2',
                                                'origin_codes': 'i',
                                                'path': '3 '
                                                        '10 '
                                                        '20 '
                                                        '30 '
                                                        '40 '
                                                        '50 '
                                                        '60 '
                                                        '70 '
                                                        '80 '
                                                        '90',
                                                'path_type': 'i',
                                                'status_codes': '*>',
                                                'weight': 0}}}},
                                'bgp_table_version': 173,
                                'local_router_id': '20.0.0.6'},
                            'vpnv4 unicast': 
                                {'bgp_table_version': 183,
                                'local_router_id': '20.0.0.6'},
                            'vpnv4 unicast RD 0:0': 
                                {'bgp_table_version': 183,
                                'local_router_id': '20.0.0.6',
                                'route_distinguisher': '0:0'},
                            'vpnv4 unicast RD 101:100': 
                                {'bgp_table_version': 183,
                                'local_router_id': '20.0.0.6',
                                'route_distinguisher': '101:100'},
                            'vpnv4 unicast RD 102:100': 
                                {'bgp_table_version': 183,
                                'local_router_id': '20.0.0.6',
                                'route_distinguisher': '102:100'},
                            'vpnv6 unicast': 
                                {'bgp_table_version': 13,
                                'local_router_id': '20.0.0.6'},
                            'vpnv6 unicast RD 0xbb00010000000000': 
                                {'bgp_table_version': 13,
                                'local_router_id': '20.0.0.6',
                                'route_distinguisher': '0xbb00010000000000'},
                            'vpnv6 unicast RD 100:200': 
                                {'bgp_table_version': 13,
                                'local_router_id': '20.0.0.6',
                                'route_distinguisher': '100:200'}}}}}}}

    golden_output2 = {'execute.return_value': '''
        show bgp vrf default all neighbors 19.0.102.3 advertised-routes


        Peer 19.0.102.3 routes for address family IPv4 Unicast:
        BGP table version is 174, Local Router ID is 20.0.0.6
        Status: s-suppressed, x-deleted, S-stale, d-dampened, h-history, *-valid, >-best
        Path type: i-internal, e-external, c-confed, l-local, a-aggregate, r-redist, I-injected
        Origin codes: i - IGP, e - EGP, ? - incomplete, | - multipath, & - backup

           Network            Next Hop            Metric     LocPrf     Weight Path
        *>i1.1.1.0/24         19.0.102.4                        100          0 {62112 33492 4872 41787 13166 50081 21461 58376 29755 1135} i
        *>i1.1.2.0/24         19.0.102.4                        100          0 {62112 33492 4872 41787 13166 50081 21461 58376 29755 1135} i
        *>i1.6.0.0/16         19.0.101.1                        100          0 10 20 30 40 50 60 70 80 90 i
        *>i1.5.0.0/24         19.0.102.3             100                     0 10 20 30 40 50 60 70 80 90 i


        Peer 19.0.102.3 routes for address family IPv4 Multicast:
        BGP table version is 175, Local Router ID is 20.0.0.6
        Status: s-suppressed, x-deleted, S-stale, d-dampened, h-history, *-valid, >-best
        Path type: i-internal, e-external, c-confed, l-local, a-aggregate, r-redist, I-injected
        Origin codes: i - IGP, e - EGP, ? - incomplete, | - multipath, & - backup

           Network            Next Hop            Metric     LocPrf     Weight Path
        *>i1.2.1.0/24         19.0.101.1                        100          0 2 3 4 i
        *>i1.2.2.0/24         19.0.101.1                        100          0 2 3 4 i
        *>i1.4.1.0/24         19.0.102.4                        100          0 2 3 4 i
        *>i1.4.2.0/24         19.0.102.4                        100          0 2 3 4 i
        *>i1.5.2.0/24         19.0.102.4            5555        500      32788 2 3 4 5 6 7 8 9 10 11 12 i


        Peer 19.0.102.3 routes for address family IPv6 Unicast:
        BGP table version is 173, Local Router ID is 20.0.0.6
        Status: s-suppressed, x-deleted, S-stale, d-dampened, h-history, *-valid, >-best
        Path type: i-internal, e-external, c-confed, l-local, a-aggregate, r-redist, I-injected
        Origin codes: i - IGP, e - EGP, ? - incomplete, | - multipath, & - backup

           Network            Next Hop            Metric     LocPrf     Weight Path


        Peer 19.0.102.3 routes for address family IPv6 Multicast:
        BGP table version is 6, Local Router ID is 20.0.0.6
        Status: s-suppressed, x-deleted, S-stale, d-dampened, h-history, *-valid, >-best
        Path type: i-internal, e-external, c-confed, l-local, a-aggregate, r-redist, I-injected
        Origin codes: i - IGP, e - EGP, ? - incomplete, | - multipath, & - backup

           Network            Next Hop            Metric     LocPrf     Weight Path


        Peer 19.0.102.3 routes for address family VPNv4 Unicast:
        BGP table version is 183, Local Router ID is 20.0.0.6
        Status: s-suppressed, x-deleted, S-stale, d-dampened, h-history, *-valid, >-best
        Path type: i-internal, e-external, c-confed, l-local, a-aggregate, r-redist, I-injected
        Origin codes: i - IGP, e - EGP, ? - incomplete, | - multipath, & - backup

           Network            Next Hop            Metric     LocPrf     Weight Path
        Route Distinguisher: 0:0

        Route Distinguisher: 101:100

        Route Distinguisher: 102:100


        Peer 19.0.102.3 routes for address family VPNv6 Unicast:
        BGP table version is 13, Local Router ID is 20.0.0.6
        Status: s-suppressed, x-deleted, S-stale, d-dampened, h-history, *-valid, >-best
        Path type: i-internal, e-external, c-confed, l-local, a-aggregate, r-redist, I-injected
        Origin codes: i - IGP, e - EGP, ? - incomplete, | - multipath, & - backup

           Network            Next Hop            Metric     LocPrf     Weight Path
        Route Distinguisher: 100:200

        Route Distinguisher: 0xbb00010000000000


        Peer 19.0.102.3 routes for address family Link-State:
        BGP table version is 173, Local Router ID is 20.0.0.6
        Status: s-suppressed, x-deleted, S-stale, d-dampened, h-history, *-valid, >-best
        Path type: i-internal, e-external, c-confed, l-local, a-aggregate, r-redist, I-injected
        Origin codes: i - IGP, e - EGP, ? - incomplete, | - multipath, & - backup

           Network            Next Hop            Metric     LocPrf     Weight Path
        *>i[2]:[77][7,0][9.9.9.9,1,151587081][29.1.1.1,22][19.0.101.1,29.0.1.30]/616
                              19.0.101.1            4444        100          0 3 10 20 30 40 50 60 70 80 90 i
                              19.0.102.3            4444        100          0 3 10 20 30 40 50 60 70 80 90 i
        *>i[2]:[77][7,0][9.9.9.9,2,151587081][29.1.1.1,22][19.0.101.1,29.0.1.31]/616
                              19.0.103.2            555        200          0 3 10 20 30 40 50 60 70 80 90 i
        '''}

    def test_show_bgp_vrf_all_neighbors_advertised_routes_golden(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output)
        obj = ShowBgpVrfAllNeighborsAdvertisedRoutes(device=self.device)
        parsed_output = obj.parse(vrf='default', neighbor='21.0.0.2')
        self.assertEqual(parsed_output,self.golden_parsed_output)

    def test_show_bgp_vrf_all_neighbors_advertised_routes_golden2(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output2)
        obj = ShowBgpVrfAllNeighborsAdvertisedRoutes(device=self.device)
        parsed_output = obj.parse(vrf='default', neighbor='19.0.102.3')
        self.assertEqual(parsed_output,self.golden_parsed_output2)

    def test_show_bgp_vrf_all_neighbors_advertised_routes_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowBgpVrfAllNeighborsAdvertisedRoutes(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse(vrf='all', neighbor='21.0.0.2')

# ===============================================================
# Unit test for 'show bgp vrf <WORD> all neighbors <WORD> routes'
# ===============================================================

class test_show_bgp_vrf_all_neighbors_routes(unittest.TestCase):
    
    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output = {
        'vrf':
            {'default':
                {'neighbor':
                    {'21.0.0.2':
                        {'address_family':
                            {'ipv4 label unicast':
                                {'bgp_table_version': 28,
                                'local_router_id': '21.0.101.1',
                                'routes':
                                    {'104.0.0.0/8':
                                        {'index':
                                            {1:
                                                {'next_hop': '21.0.0.2',
                                                'localprf': 100,
                                                'metric': 0,
                                                'origin_codes': '?',
                                                'path_type': 'i',
                                                'status_codes': '* ',
                                                'weight': 0}}},
                                    '204.0.0.0/8':
                                        {'index':
                                            {1:
                                                {'next_hop': '21.0.0.2',
                                                'localprf': 100,
                                                'metric': 0,
                                                'origin_codes': '?',
                                                'path_type': 'i',
                                                'status_codes': '* ',
                                                'weight': 0}}},
                                            '4.0.0.0/8':
                                                {'index':
                                                    {1:
                                                        {'next_hop': '21.0.0.2',
                                                        'localprf': 100,
                                                        'metric': 0,
                                                        'origin_codes': '?',
                                                        'path_type': 'i',
                                                        'status_codes': '*>',
                                                        'weight': 0}}}}},
                            'ipv4 multicast':
                                {'bgp_table_version': 19,
                                'local_router_id': '21.0.101.1',
                                'routes':
                                    {'104.0.0.0/8':
                                        {'index':
                                            {1:
                                                {'next_hop': '21.0.0.2',
                                                'localprf': 100,
                                                'metric': 0,
                                                'origin_codes': '?',
                                                'path_type': 'i',
                                                'status_codes': '*>',
                                                'weight': 0}}},
                                    '204.0.0.0/8':
                                        {'index':
                                            {1:
                                                {'next_hop': '21.0.0.2',
                                                'localprf': 100,
                                                'metric': 0,
                                                'origin_codes': '?',
                                                'path_type': 'i',
                                                'status_codes': '*>',
                                                'weight': 0}}},
                                    '4.0.0.0/8':
                                        {'index':
                                            {1:
                                                {'next_hop': '21.0.0.2',
                                                'localprf': 100,
                                                'metric': 0,
                                                'origin_codes': '?',
                                                'path_type': 'i',
                                                'status_codes': '*>',
                                                'weight': 0}}}}},
                            'ipv4 mvpn': 
                                {'bgp_table_version': 2,
                                'local_router_id': '21.0.101.1'},
                            'ipv4 unicast':
                                {'bgp_table_version': 25,
                                'local_router_id': '21.0.101.1',
                                'routes':
                                    {'104.0.0.0/8':
                                        {'index':
                                            {1:
                                                {'next_hop': '21.0.0.2',
                                                'localprf': 100,
                                                'metric': 0,
                                                'origin_codes': '?',
                                                'path_type': 'i',
                                                'status_codes': '* ',
                                                'weight': 0}}},
                                    '204.0.0.0/8':
                                        {'index':
                                            {1:
                                                {'next_hop': '21.0.0.2',
                                                'localprf': 100,
                                                'metric': 0,
                                                'origin_codes': '?',
                                                'path_type': 'i',
                                                'status_codes': '* ',
                                                'weight': 0}}},
                                    '4.0.0.0/8':
                                        {'index':
                                            {1:
                                                {'next_hop': '21.0.0.2',
                                                'localprf': 100,
                                                'metric': 0,
                                                'origin_codes': '?',
                                                'path_type': 'i',
                                                'status_codes': '*>',
                                                'weight': 0}}}}},
                            'ipv6 multicast': 
                                {'bgp_table_version': 2,
                                'local_router_id': '21.0.101.1'},
                            'ipv6 mvpn': 
                                {'bgp_table_version': 2,
                                'local_router_id': '21.0.101.1'},
                            'ipv6 unicast': 
                                {'bgp_table_version': 7,
                                'local_router_id': '21.0.101.1'},
                            'link-state': 
                                {'bgp_table_version': 2,
                                'local_router_id': '21.0.101.1'},
                            'vpnv4 unicast': 
                                {'bgp_table_version': 23,
                                'local_router_id': '21.0.101.1'},
                            'vpnv4 unicast RD 2:100':
                                {'bgp_table_version': 23,
                                'default_vrf': 'vpn2',
                                'local_router_id': '21.0.101.1',
                                'route_distinguisher': '2:100',
                                'routes':
                                    {'4.0.0.0/8':
                                        {'index':
                                            {1:
                                                {'next_hop': '21.0.0.2',
                                                'localprf': 100,
                                                'metric': 0,
                                                'origin_codes': '?',
                                                'path_type': 'i',
                                                'status_codes': '*>',
                                                'weight': 0}}}}},
                            'vpnv4 unicast RD 1:100':
                                {'bgp_table_version': 23,
                                'default_vrf': 'vpn1',
                                'local_router_id': '21.0.101.1',
                                'route_distinguisher': '1:100',
                                'routes':
                                    {'4.0.0.0/8':
                                        {'index':
                                            {1:
                                                {'next_hop': '21.0.0.2',
                                                'localprf': 100,
                                                'metric': 0,
                                                'origin_codes': '?',
                                                'path_type': 'i',
                                                'status_codes': '*>',
                                                'weight': 0}}}}},
                            'vpnv6 unicast': 
                                {'bgp_table_version': 7,
                                'local_router_id': '21.0.101.1'},
                            'vpnv6 unicast RD 1:100': 
                                {'bgp_table_version': 7,
                                'default_vrf': 'vpn1',
                                'local_router_id': '21.0.101.1',
                                'route_distinguisher': '1:100'},
                            'vpnv6 unicast RD 2:100': 
                                {'bgp_table_version': 7,
                                'default_vrf': 'vpn2',
                                'local_router_id': '21.0.101.1',
                                'route_distinguisher': '2:100'}}}}}}}

    golden_output = {'execute.return_value': '''
        pinxdt-n9kv-2# show bgp vrf default all neighbors 21.0.0.2 routes 
        Can't find neighbor 21.0.0.2

        Peer 21.0.0.2 routes for address family IPv4 Unicast:
        BGP table version is 25, Local Router ID is 21.0.101.1
        Status: s-suppressed, x-deleted, S-stale, d-dampened, h-history, *-valid, >-best
        Path type: i-internal, e-external, c-confed, l-local, a-aggregate, r-redist, I-injected
        Origin codes: i - IGP, e - EGP, ? - incomplete, | - multipath, & - backup

           Network            Next Hop            Metric     LocPrf     Weight Path
        *>i4.0.0.0/8          21.0.0.2                 0        100          0 ?
        * i104.0.0.0/8        21.0.0.2                 0        100          0 ?
        * i204.0.0.0/8        21.0.0.2                 0        100          0 ?


        Peer 21.0.0.2 routes for address family IPv4 Multicast:
        BGP table version is 19, Local Router ID is 21.0.101.1
        Status: s-suppressed, x-deleted, S-stale, d-dampened, h-history, *-valid, >-best
        Path type: i-internal, e-external, c-confed, l-local, a-aggregate, r-redist, I-injected
        Origin codes: i - IGP, e - EGP, ? - incomplete, | - multipath, & - backup

           Network            Next Hop            Metric     LocPrf     Weight Path
        *>i4.0.0.0/8          21.0.0.2                 0        100          0 ?
        *>i104.0.0.0/8        21.0.0.2                 0        100          0 ?
        *>i204.0.0.0/8        21.0.0.2                 0        100          0 ?


        Peer 21.0.0.2 routes for address family IPv6 Unicast:
        BGP table version is 7, Local Router ID is 21.0.101.1
        Status: s-suppressed, x-deleted, S-stale, d-dampened, h-history, *-valid, >-best
        Path type: i-internal, e-external, c-confed, l-local, a-aggregate, r-redist, I-injected
        Origin codes: i - IGP, e - EGP, ? - incomplete, | - multipath, & - backup

           Network            Next Hop            Metric     LocPrf     Weight Path


        Peer 21.0.0.2 routes for address family IPv6 Multicast:
        BGP table version is 2, Local Router ID is 21.0.101.1
        Status: s-suppressed, x-deleted, S-stale, d-dampened, h-history, *-valid, >-best
        Path type: i-internal, e-external, c-confed, l-local, a-aggregate, r-redist, I-injected
        Origin codes: i - IGP, e - EGP, ? - incomplete, | - multipath, & - backup

           Network            Next Hop            Metric     LocPrf     Weight Path

        Peer 21.0.0.2 routes for address family VPNv4 Unicast:
        BGP table version is 23, Local Router ID is 21.0.101.1
        Status: s-suppressed, x-deleted, S-stale, d-dampened, h-history, *-valid, >-best
        Path type: i-internal, e-external, c-confed, l-local, a-aggregate, r-redist, I-injected
        Origin codes: i - IGP, e - EGP, ? - incomplete, | - multipath, & - backup

           Network            Next Hop            Metric     LocPrf     Weight Path
        Route Distinguisher: 1:100    (VRF vpn1)
        *>i4.0.0.0/8          21.0.0.2                 0        100          0 ?

        Route Distinguisher: 2:100    (VRF vpn2)
        *>i4.0.0.0/8          21.0.0.2                 0        100          0 ?

        Peer 21.0.0.2 routes for address family VPNv6 Unicast:
        BGP table version is 7, Local Router ID is 21.0.101.1
        Status: s-suppressed, x-deleted, S-stale, d-dampened, h-history, *-valid, >-best
        Path type: i-internal, e-external, c-confed, l-local, a-aggregate, r-redist, I-injected
        Origin codes: i - IGP, e - EGP, ? - incomplete, | - multipath, & - backup

           Network            Next Hop            Metric     LocPrf     Weight Path
        Route Distinguisher: 1:100    (VRF vpn1)

        Route Distinguisher: 2:100    (VRF vpn2)


        Peer 21.0.0.2 routes for address family IPv4 MVPN:
        BGP table version is 2, Local Router ID is 21.0.101.1
        Status: s-suppressed, x-deleted, S-stale, d-dampened, h-history, *-valid, >-best
        Path type: i-internal, e-external, c-confed, l-local, a-aggregate, r-redist, I-injected
        Origin codes: i - IGP, e - EGP, ? - incomplete, | - multipath, & - backup

           Network            Next Hop            Metric     LocPrf     Weight Path

        Peer 21.0.0.2 routes for address family IPv6 MVPN:
        BGP table version is 2, Local Router ID is 21.0.101.1
        Status: s-suppressed, x-deleted, S-stale, d-dampened, h-history, *-valid, >-best
        Path type: i-internal, e-external, c-confed, l-local, a-aggregate, r-redist, I-injected
        Origin codes: i - IGP, e - EGP, ? - incomplete, | - multipath, & - backup

           Network            Next Hop            Metric     LocPrf     Weight Path

        Peer 21.0.0.2 routes for address family IPv4 Label Unicast:
        BGP table version is 28, Local Router ID is 21.0.101.1
        Status: s-suppressed, x-deleted, S-stale, d-dampened, h-history, *-valid, >-best
        Path type: i-internal, e-external, c-confed, l-local, a-aggregate, r-redist, I-injected
        Origin codes: i - IGP, e - EGP, ? - incomplete, | - multipath, & - backup

           Network            Next Hop            Metric     LocPrf     Weight Path
        *>i4.0.0.0/8          21.0.0.2                 0        100          0 ?
        * i104.0.0.0/8        21.0.0.2                 0        100          0 ?
        * i204.0.0.0/8        21.0.0.2                 0        100          0 ?


        Peer 21.0.0.2 routes for address family Link-State:
        BGP table version is 2, Local Router ID is 21.0.101.1
        Status: s-suppressed, x-deleted, S-stale, d-dampened, h-history, *-valid, >-best
        Path type: i-internal, e-external, c-confed, l-local, a-aggregate, r-redist, I-injected
        Origin codes: i - IGP, e - EGP, ? - incomplete, | - multipath, & - backup

           Network            Next Hop            Metric     LocPrf     Weight Path
        Can't find neighbor 21.0.0.2
        Can't find neighbor 21.0.0.2
        '''}

    golden_parsed_output2 = {
        'vrf': 
            {'default': 
                {'neighbor': 
                    {'19.0.101.1': 
                        {'address_family': 
                            {'ipv4 multicast': 
                                {'bgp_table_version': 175,
                                'local_router_id': '20.0.0.6',
                                'routes': 
                                    {'1.2.1.0/24': 
                                        {'index': 
                                            {1: 
                                                {'localprf': 100,
                                                'next_hop': '19.0.101.1',
                                                'origin_codes': 'i',
                                                'path': '2 '
                                                        '3 '
                                                        '4',
                                                'path_type': 'i',
                                                'status_codes': '*>',
                                                'weight': 0}}},
                                    '1.2.2.0/24': 
                                        {'index': 
                                            {1: 
                                                {'localprf': 100,
                                                'next_hop': '19.0.101.1',
                                                'origin_codes': 'i',
                                                'path': '2 '
                                                        '3 '
                                                        '4',
                                                'path_type': 'i',
                                                'status_codes': '*>',
                                                'weight': 0}}}}},
                            'ipv4 unicast': 
                                {'bgp_table_version': 174,
                                'local_router_id': '20.0.0.6',
                                'routes': 
                                    {'1.1.1.0/24': 
                                        {'index': 
                                            {1: 
                                                {'localprf': 100,
                                                'metric': 2222,
                                                'next_hop': '19.0.101.1',
                                                'origin_codes': 'i',
                                                'path': '1 '
                                                        '2 '
                                                        '3 '
                                                        '65000 '
                                                        '23',
                                                'path_type': 'i',
                                                'status_codes': '* ',
                                                'weight': 0}}},
                                    '1.1.2.0/24': 
                                        {'index': 
                                            {1: 
                                                {'localprf': 100,
                                                'metric': 2222,
                                                'next_hop': '19.0.101.1',
                                                'origin_codes': 'i',
                                                'path': '1 '
                                                        '2 '
                                                        '3 '
                                                        '65000 '
                                                        '23',
                                                'path_type': 'i',
                                                'status_codes': '* ',
                                                'weight': 0}}},
                                    '1.6.0.0/16': 
                                        {'index': 
                                            {1: 
                                                {'localprf': 100,
                                                'next_hop': '19.0.101.1',
                                                'origin_codes': 'i',
                                                'path': '10 '
                                                        '20 '
                                                        '30 '
                                                        '40 '
                                                        '50 '
                                                        '60 '
                                                        '70 '
                                                        '80 '
                                                        '90',
                                                'path_type': 'i',
                                                'status_codes': '*>',
                                                'weight': 0}}}}},
                            'ipv6 multicast': 
                                {'bgp_table_version': 6,
                                'local_router_id': '20.0.0.6'},
                            'ipv6 unicast': 
                                {'bgp_table_version': 173,
                                'local_router_id': '20.0.0.6'},
                            'link-state': 
                                {'bgp_table_version': 173,
                                'local_router_id': '20.0.0.6',
                                'routes': 
                                    {'[2]:[77][7,0][9.9.9.9,1,151587081][29.1.1.1,22][19.0.101.1,29.0.1.30]/616': 
                                        {'index': 
                                            {1: 
                                                {'localprf': 100,
                                                'metric': 4444,
                                                'next_hop': '19.0.101.1',
                                                'origin_codes': 'i',
                                                'path': '3 '
                                                      '10 '
                                                      '20 '
                                                      '30 '
                                                      '40 '
                                                      '50 '
                                                      '60 '
                                                      '70 '
                                                      '80 '
                                                      '90',
                                                'path_type': 'i',
                                                'status_codes': '*>',
                                                'weight': 0}}},
                                    '[2]:[77][7,0][9.9.9.9,2,151587081][29.1.1.1,22][19.0.101.1,29.0.1.31]/616': 
                                        {'index': 
                                            {1: 
                                                {'localprf': 100,
                                                'metric': 4444,
                                                'next_hop': '19.0.101.1',
                                                'origin_codes': 'i',
                                                'path': '3 '
                                                      '10 '
                                                      '20 '
                                                      '30 '
                                                      '40 '
                                                      '50 '
                                                      '60 '
                                                      '70 '
                                                      '80 '
                                                      '90',
                                                'path_type': 'i',
                                                'status_codes': '*>',
                                                'weight': 0}}}}},
                            'vpnv4 unicast': 
                                {'bgp_table_version': 183,
                                'local_router_id': '20.0.0.6'},
                            'vpnv4 unicast RD 0:0': 
                                {'bgp_table_version': 183,
                                'local_router_id': '20.0.0.6',
                                'route_distinguisher': '0:0'},
                            'vpnv4 unicast RD 101:100': 
                                {'bgp_table_version': 183,
                                'local_router_id': '20.0.0.6',
                                'route_distinguisher': '101:100',
                                'routes': 
                                    {'1.3.1.0/24': 
                                        {'index': 
                                            {1: 
                                                {'localprf': 100,
                                                'metric': 4444,
                                                'next_hop': '19.0.101.1',
                                                'origin_codes': 'i',
                                                'path': '3 '
                                                        '10 '
                                                        '20 '
                                                        '4 '
                                                        '5 '
                                                        '6 '
                                                        '3 '
                                                        '10 '
                                                        '20 '
                                                        '4 '
                                                        '5 '
                                                        '6',
                                                'path_type': 'i',
                                                'status_codes': '* ',
                                                'weight': 0}}},
                                    '1.3.2.0/24': 
                                        {'index': 
                                            {1: 
                                                {'localprf': 100,
                                                'metric': 4444,
                                                'next_hop': '19.0.101.1',
                                                'origin_codes': 'i',
                                                'path': '3 '
                                                     '10 '
                                                     '20 '
                                                     '4 '
                                                     '5 '
                                                     '6 '
                                                     '3 '
                                                     '10 '
                                                     '20 '
                                                     '4 '
                                                     '5 '
                                                     '6',
                                                'path_type': 'i',
                                                'status_codes': '* ',
                                                'weight': 0}}}}},
                            'vpnv4 unicast RD 102:100': 
                                {'bgp_table_version': 183,
                                'local_router_id': '20.0.0.6',
                                'route_distinguisher': '102:100'},
                            'vpnv6 unicast': 
                                {'bgp_table_version': 13,
                                'local_router_id': '20.0.0.6'},
                            'vpnv6 unicast RD 0xbb00010000000000': 
                                {'bgp_table_version': 13,
                                'local_router_id': '20.0.0.6',
                                'route_distinguisher': '0xbb00010000000000'},
                            'vpnv6 unicast RD 100:200': 
                                {'bgp_table_version': 13,
                                'local_router_id': '20.0.0.6',
                                'route_distinguisher': '100:200',
                                'routes': 
                                    {'aaaa:1::/113': 
                                        {'index': 
                                            {1: 
                                                {'localprf': 100,
                                                'next_hop': '4444',
                                                'origin_codes': 'i',
                                                'path_type': 'i',
                                                'status_codes': '*>',
                                                'weight': 0}}},
                                    'aaaa:1::8000/113': 
                                        {'index': 
                                            {1: 
                                                {'localprf': 100,
                                                'next_hop': '4444',
                                                'origin_codes': 'i',
                                                'path_type': 'i',
                                                'status_codes': '*>',
                                                'weight': 0}}}}}}}}}}}

    golden_output2 = {'execute.return_value': '''

        Peer 19.0.101.1 routes for address family IPv4 Unicast:
        BGP table version is 174, Local Router ID is 20.0.0.6
        Status: s-suppressed, x-deleted, S-stale, d-dampened, h-history, *-valid, >-best
        Path type: i-internal, e-external, c-confed, l-local, a-aggregate, r-redist, I-injected
        Origin codes: i - IGP, e - EGP, ? - incomplete, | - multipath, & - backup

           Network            Next Hop            Metric     LocPrf     Weight Path
        * i1.1.1.0/24         19.0.101.1            2222        100          0 1 2 3 65000 23 i
        * i1.1.2.0/24         19.0.101.1            2222        100          0 1 2 3 65000 23 i
        *>i1.6.0.0/16         19.0.101.1                        100          0 10 20 30 40 50 60 70 80 90 i


        Peer 19.0.101.1 routes for address family IPv4 Multicast:
        BGP table version is 175, Local Router ID is 20.0.0.6
        Status: s-suppressed, x-deleted, S-stale, d-dampened, h-history, *-valid, >-best
        Path type: i-internal, e-external, c-confed, l-local, a-aggregate, r-redist, I-injected
        Origin codes: i - IGP, e - EGP, ? - incomplete, | - multipath, & - backup

           Network            Next Hop            Metric     LocPrf     Weight Path
        *>i1.2.1.0/24         19.0.101.1                        100          0 2 3 4 i
        *>i1.2.2.0/24         19.0.101.1                        100          0 2 3 4 i


        Peer 19.0.101.1 routes for address family IPv6 Unicast:
        BGP table version is 173, Local Router ID is 20.0.0.6
        Status: s-suppressed, x-deleted, S-stale, d-dampened, h-history, *-valid, >-best
        Path type: i-internal, e-external, c-confed, l-local, a-aggregate, r-redist, I-injected
        Origin codes: i - IGP, e - EGP, ? - incomplete, | - multipath, & - backup

           Network            Next Hop            Metric     LocPrf     Weight Path


        Peer 19.0.101.1 routes for address family IPv6 Multicast:
        BGP table version is 6, Local Router ID is 20.0.0.6
        Status: s-suppressed, x-deleted, S-stale, d-dampened, h-history, *-valid, >-best
        Path type: i-internal, e-external, c-confed, l-local, a-aggregate, r-redist, I-injected
        Origin codes: i - IGP, e - EGP, ? - incomplete, | - multipath, & - backup

           Network            Next Hop            Metric     LocPrf     Weight Path


        Peer 19.0.101.1 routes for address family VPNv4 Unicast:
        BGP table version is 183, Local Router ID is 20.0.0.6
        Status: s-suppressed, x-deleted, S-stale, d-dampened, h-history, *-valid, >-best
        Path type: i-internal, e-external, c-confed, l-local, a-aggregate, r-redist, I-injected
        Origin codes: i - IGP, e - EGP, ? - incomplete, | - multipath, & - backup

           Network            Next Hop            Metric     LocPrf     Weight Path
        Route Distinguisher: 0:0

        Route Distinguisher: 101:100
        * i1.3.1.0/24         19.0.101.1            4444        100          0 3 10 20 4 5 6 3 10 20 4 5 6 i
        * i1.3.2.0/24         19.0.101.1            4444        100          0 3 10 20 4 5 6 3 10 20 4 5 6 i

        Route Distinguisher: 102:100


        Peer 19.0.101.1 routes for address family VPNv6 Unicast:
        BGP table version is 13, Local Router ID is 20.0.0.6
        Status: s-suppressed, x-deleted, S-stale, d-dampened, h-history, *-valid, >-best
        Path type: i-internal, e-external, c-confed, l-local, a-aggregate, r-redist, I-injected
        Origin codes: i - IGP, e - EGP, ? - incomplete, | - multipath, & - backup

           Network            Next Hop            Metric     LocPrf     Weight Path
        Route Distinguisher: 100:200
        *>iaaaa:1::/113       ::ffff:19.0.101.1
                                                    4444        100          0 i
        *>iaaaa:1::8000/113   ::ffff:19.0.101.1
                                                    4444        100          0 i

        Route Distinguisher: 0xbb00010000000000


        Peer 19.0.101.1 routes for address family Link-State:
        BGP table version is 173, Local Router ID is 20.0.0.6
        Status: s-suppressed, x-deleted, S-stale, d-dampened, h-history, *-valid, >-best
        Path type: i-internal, e-external, c-confed, l-local, a-aggregate, r-redist, I-injected
        Origin codes: i - IGP, e - EGP, ? - incomplete, | - multipath, & - backup

           Network            Next Hop            Metric     LocPrf     Weight Path
        *>i[2]:[77][7,0][9.9.9.9,1,151587081][29.1.1.1,22][19.0.101.1,29.0.1.30]/616
                              19.0.101.1            4444        100          0 3 10 20 30 40 50 60 70 80 90 i
        *>i[2]:[77][7,0][9.9.9.9,2,151587081][29.1.1.1,22][19.0.101.1,29.0.1.31]/616
                              19.0.101.1            4444        100          0 3 10 20 30 40 50 60 70 80 90 i
        '''}

    def test_show_bgp_vrf_all_neighbors_routes_golden(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output)
        obj = ShowBgpVrfAllNeighborsRoutes(device=self.device)
        parsed_output = obj.parse(vrf='default', neighbor='21.0.0.2')
        self.assertEqual(parsed_output,self.golden_parsed_output)

    def test_show_bgp_vrf_all_neighbors_routes_golden2(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output2)
        obj = ShowBgpVrfAllNeighborsRoutes(device=self.device)
        parsed_output = obj.parse(vrf='default', neighbor='19.0.101.1')
        self.assertEqual(parsed_output,self.golden_parsed_output2)

    def test_show_bgp_vrf_all_neighbors_routes_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowBgpVrfAllNeighborsRoutes(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse(vrf='default', neighbor='21.0.0.2')


# ========================================================================
# Unit test for 'show bgp vrf <WORD> all neighbors <WORD> received-routes'
# ========================================================================

class test_show_bgp_vrf_all_neighbors_received_routes(unittest.TestCase):
    
    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output = {
        'vrf': {
            'default': {
                'neighbor': {
                    '21.0.0.2': {
                        'address_family': {
                            'ipv4 multicast': {
                                'bgp_table_version': 19,
                                'local_router_id': '21.0.101.1',
                                'received_routes': {
                                    '104.0.0.0/8': {
                                        'index': {
                                            1: {
                                                'next_hop': '21.0.0.2',
                                                'localprf': 100,
                                                'metric': 0,
                                                'origin_codes': '?',
                                                'path_type': 'i',
                                                'status_codes': '*>',
                                                'weight': 0}}},
                                    '204.0.0.0/8': {
                                        'index': {
                                            1: {
                                                'next_hop': '21.0.0.2',
                                                'localprf': 100,
                                                'metric': 0,
                                                'origin_codes': '?',
                                                'path_type': 'i',
                                                'status_codes': '*>',
                                                'weight': 0}}},
                                    '4.0.0.0/8': {
                                        'index': {
                                            1: {
                                                'next_hop': '21.0.0.2',
                                                'localprf': 100,
                                                'metric': 0,
                                                'origin_codes': '?',
                                                'path_type': 'i',
                                                'status_codes': '*>',
                                                'weight': 0}}}}},
                            'vpnv4 unicast': 
                                {'bgp_table_version': 23,
                                'local_router_id': '21.0.101.1'},
                            'vpnv4 unicast RD 1:100': {
                                'bgp_table_version': 23,
                                'local_router_id': '21.0.101.1',
                                'route_distinguisher': '1:100',
                                'default_vrf': 'vpn1',
                                'received_routes': {
                                    '1.1.1.0/24': {
                                        'index': {
                                            1: {
                                                'next_hop': '0.0.0.0',
                                                'localprf': 100,
                                                'metric': 3333,
                                                'origin_codes': '?',
                                                'path_type': 'r',
                                                'status_codes': '*>',
                                                'weight': 32768}}},
                                    '1.2.1.0/24': {
                                        'index': {
                                            1: {
                                                'next_hop': '0.0.0.0',
                                                'localprf': 100,
                                                'metric': 3333,
                                                'origin_codes': '?',
                                                'path_type': 'r',
                                                'status_codes': '*>',
                                                'weight': 32768}}}}},
                            'vpnv4 unicast RD 2:100': {
                                'bgp_table_version': 23,
                                'local_router_id': '21.0.101.1',
                                'route_distinguisher': '2:100',
                                'default_vrf': 'vpn2',
                                'received_routes': {
                                    '1.1.1.0/24': {
                                        'index': {
                                            1: {
                                                'next_hop': '0.0.0.0',
                                                'localprf': 100,
                                                'metric': 3333,
                                                'origin_codes': '?',
                                                'path_type': 'r',
                                                'status_codes': '*>',
                                                'weight': 32768}}},
                                    '1.2.1.0/24': {
                                        'index': {
                                            1: {
                                                'next_hop': '0.0.0.0',
                                                'localprf': 100,
                                                'metric': 3333,
                                                'origin_codes': '?',
                                                'path_type': 'r',
                                                'status_codes': '*>',
                                                'weight': 32768}}}}}}}}}}}

    golden_output = {'execute.return_value': '''
        pinxdt-n9kv-2# show bgp vrf default all neighbors 21.0.0.2 received-routes 
        Can't find neighbor 21.0.0.2

        Inbound soft reconfiguration for IPv4 Unicast not performed on 21.0.0.2

        Peer 21.0.0.2 routes for address family IPv4 Multicast:
        BGP table version is 19, Local Router ID is 21.0.101.1
        Status: s-suppressed, x-deleted, S-stale, d-dampened, h-history, *-valid, >-best
        Path type: i-internal, e-external, c-confed, l-local, a-aggregate, r-redist, I-injected
        Origin codes: i - IGP, e - EGP, ? - incomplete, | - multipath, & - backup

           Network            Next Hop            Metric     LocPrf     Weight Path
        *>i4.0.0.0/8          21.0.0.2                 0        100          0 ?
        *>i104.0.0.0/8        21.0.0.2                 0        100          0 ?
        *>i204.0.0.0/8        21.0.0.2                 0        100          0 ?


        Inbound soft reconfiguration for IPv6 Unicast not performed on 21.0.0.2

        Inbound soft reconfiguration for IPv6 Multicast not performed on 21.0.0.2

        Inbound soft reconfiguration for VPNv4 Unicast not performed on 21.0.0.2

        Peer 21.0.0.2 routes for address family VPNv4 Unicast:
        BGP table version is 23, Local Router ID is 21.0.101.1
        Status: s-suppressed, x-deleted, S-stale, d-dampened, h-history, *-valid, >-best
        Path type: i-internal, e-external, c-confed, l-local, a-aggregate, r-redist, I-injected
        Origin codes: i - IGP, e - EGP, ? - incomplete, | - multipath, & - backup

           Network            Next Hop            Metric     LocPrf     Weight Path
        Route Distinguisher: 1:100    (VRF vpn1)
        *>r1.1.1.0/24         0.0.0.0               3333        100      32768 ?
        *>r1.2.1.0/24         0.0.0.0               3333        100      32768 ?

        Route Distinguisher: 2:100    (VRF vpn2)
        *>r1.1.1.0/24         0.0.0.0               3333        100      32768 ?
        *>r1.2.1.0/24         0.0.0.0               3333        100      32768 ?     

        Inbound soft reconfiguration for VPNv6 Unicast not performed on 21.0.0.2

        Inbound soft reconfiguration for IPv4 MVPN not performed on 21.0.0.2

        Inbound soft reconfiguration for IPv6 MVPN not performed on 21.0.0.2

        Inbound soft reconfiguration for IPv4 Label Unicast not performed on 21.0.0.2

        Inbound soft reconfiguration for Link-State not performed on 21.0.0.2
        Can't find neighbor 21.0.0.2
        Can't find neighbor 21.0.0.2
        pinxdt-n9kv-2# 
        '''}

    golden_parsed_output2 = {
        'vrf': 
            {'default': 
                {'neighbor': 
                    {'19.0.101.1': 
                        {'address_family': 
                            {'ipv4 multicast': 
                                {'bgp_table_version': 175,
                                'local_router_id': '20.0.0.6',
                                'received_routes': 
                                    {'1.2.1.0/24': 
                                        {'index': 
                                            {1: 
                                                {'localprf': 100,
                                                'next_hop': '19.0.101.1',
                                                'origin_codes': 'i',
                                                'path': '2 '
                                                        '3 '
                                                        '4',
                                                'path_type': 'i',
                                                'status_codes': '*>',
                                                'weight': 0}}},
                                    '1.2.2.0/24': 
                                        {'index': 
                                            {1: 
                                                {'localprf': 100,
                                                'next_hop': '19.0.101.1',
                                                'origin_codes': 'i',
                                                'path': '2 '
                                                        '3 '
                                                        '4',
                                                'path_type': 'i',
                                                'status_codes': '*>',
                                                'weight': 0}}}}},
                            'ipv4 unicast': 
                                {'bgp_table_version': 174,
                                'local_router_id': '20.0.0.6',
                                'received_routes': 
                                    {'1.1.1.0/24': 
                                        {'index': 
                                            {1: 
                                                {'localprf': 100,
                                                'metric': 2222,
                                                'next_hop': '19.0.101.1',
                                                'origin_codes': 'i',
                                                'path': '1 '
                                                        '2 '
                                                        '3 '
                                                        '65000 '
                                                        '23',
                                                'path_type': 'i',
                                                'status_codes': '* ',
                                                'weight': 0}}},
                                    '1.1.2.0/24': 
                                        {'index': 
                                            {1: 
                                                {'localprf': 100,
                                                'metric': 2222,
                                                'next_hop': '19.0.101.1',
                                                'origin_codes': 'i',
                                                'path': '1 '
                                                        '2 '
                                                        '3 '
                                                        '65000 '
                                                        '23',
                                                'path_type': 'i',
                                                'status_codes': '* ',
                                                'weight': 0}}},
                                    '1.6.0.0/16': 
                                        {'index': 
                                            {1: 
                                                {'localprf': 100,
                                                'next_hop': '19.0.101.1',
                                                'origin_codes': 'i',
                                                'path': '10 '
                                                        '20 '
                                                        '30 '
                                                        '40 '
                                                        '50 '
                                                        '60 '
                                                        '70 '
                                                        '80 '
                                                        '90',
                                                'path_type': 'i',
                                                'status_codes': '*>',
                                                'weight': 0}}}}},
                            'ipv6 multicast': 
                                {'bgp_table_version': 6,
                                'local_router_id': '20.0.0.6'},
                            'ipv6 unicast': 
                                {'bgp_table_version': 173,
                                'local_router_id': '20.0.0.6'},
                            'link-state': 
                                {'bgp_table_version': 173,
                                'local_router_id': '20.0.0.6',
                                'received_routes': 
                                    {'[2]:[77][7,0][9.9.9.9,1,151587081][29.1.1.1,22][19.0.101.1,29.0.1.30]/616': 
                                        {'index': 
                                            {1: 
                                                {'localprf': 100,
                                                'metric': 4444,
                                                'next_hop': '19.0.101.1',
                                                'origin_codes': 'i',
                                                'path': '3 '
                                                      '10 '
                                                      '20 '
                                                      '30 '
                                                      '40 '
                                                      '50 '
                                                      '60 '
                                                      '70 '
                                                      '80 '
                                                      '90',
                                                'path_type': 'i',
                                                'status_codes': '*>',
                                                'weight': 0}}},
                                    '[2]:[77][7,0][9.9.9.9,2,151587081][29.1.1.1,22][19.0.101.1,29.0.1.31]/616': 
                                        {'index': 
                                            {1: 
                                                {'localprf': 100,
                                                'metric': 4444,
                                                'next_hop': '19.0.101.1',
                                                'origin_codes': 'i',
                                                'path': '3 '
                                                      '10 '
                                                      '20 '
                                                      '30 '
                                                      '40 '
                                                      '50 '
                                                      '60 '
                                                      '70 '
                                                      '80 '
                                                      '90',
                                                'path_type': 'i',
                                                'status_codes': '*>',
                                                'weight': 0}}}}},
                            'vpnv4 unicast': 
                                {'bgp_table_version': 183,
                                'local_router_id': '20.0.0.6'},
                            'vpnv4 unicast RD 0:0': 
                                {'bgp_table_version': 183,
                                'local_router_id': '20.0.0.6',
                                'route_distinguisher': '0:0'},
                            'vpnv4 unicast RD 101:100': 
                                {'bgp_table_version': 183,
                                'local_router_id': '20.0.0.6',
                                'route_distinguisher': '101:100',
                                'received_routes': 
                                    {'1.3.1.0/24': 
                                        {'index': 
                                            {1: 
                                                {'localprf': 100,
                                                'metric': 4444,
                                                'next_hop': '19.0.101.1',
                                                'origin_codes': 'i',
                                                'path': '3 '
                                                        '10 '
                                                        '20 '
                                                        '4 '
                                                        '5 '
                                                        '6 '
                                                        '3 '
                                                        '10 '
                                                        '20 '
                                                        '4 '
                                                        '5 '
                                                        '6',
                                                'path_type': 'i',
                                                'status_codes': '* ',
                                                'weight': 0}}},
                                    '1.3.2.0/24': 
                                        {'index': 
                                            {1: 
                                                {'localprf': 100,
                                                'metric': 4444,
                                                'next_hop': '19.0.101.1',
                                                'origin_codes': 'i',
                                                'path': '3 '
                                                     '10 '
                                                     '20 '
                                                     '4 '
                                                     '5 '
                                                     '6 '
                                                     '3 '
                                                     '10 '
                                                     '20 '
                                                     '4 '
                                                     '5 '
                                                     '6',
                                                'path_type': 'i',
                                                'status_codes': '* ',
                                                'weight': 0}}}}},
                            'vpnv4 unicast RD 102:100': 
                                {'bgp_table_version': 183,
                                'local_router_id': '20.0.0.6',
                                'route_distinguisher': '102:100'},
                            'vpnv6 unicast': 
                                {'bgp_table_version': 13,
                                'local_router_id': '20.0.0.6'},
                            'vpnv6 unicast RD 0xbb00010000000000': 
                                {'bgp_table_version': 13,
                                'local_router_id': '20.0.0.6',
                                'route_distinguisher': '0xbb00010000000000'},
                            'vpnv6 unicast RD 100:200': 
                                {'bgp_table_version': 13,
                                'local_router_id': '20.0.0.6',
                                'route_distinguisher': '100:200',
                                'received_routes': 
                                    {'aaaa:1::/113': 
                                        {'index': 
                                            {1: 
                                                {'localprf': 100,
                                                'next_hop': '4444',
                                                'origin_codes': 'i',
                                                'path_type': 'i',
                                                'status_codes': '*>',
                                                'weight': 0}}},
                                    'aaaa:1::8000/113': 
                                        {'index': 
                                            {1: 
                                                {'localprf': 100,
                                                'next_hop': '4444',
                                                'origin_codes': 'i',
                                                'path_type': 'i',
                                                'status_codes': '*>',
                                                'weight': 0}}}}}}}}}}}

    golden_output2 = {'execute.return_value': '''
        Peer 19.0.101.1 routes for address family IPv4 Unicast:
        BGP table version is 174, Local Router ID is 20.0.0.6
        Status: s-suppressed, x-deleted, S-stale, d-dampened, h-history, *-valid, >-best
        Path type: i-internal, e-external, c-confed, l-local, a-aggregate, r-redist, I-injected
        Origin codes: i - IGP, e - EGP, ? - incomplete, | - multipath, & - backup

           Network            Next Hop            Metric     LocPrf     Weight Path
        * i1.1.1.0/24         19.0.101.1            2222        100          0 1 2 3 65000 23 i
        * i1.1.2.0/24         19.0.101.1            2222        100          0 1 2 3 65000 23 i
        *>i1.6.0.0/16         19.0.101.1                        100          0 10 20 30 40 50 60 70 80 90 i


        Peer 19.0.101.1 routes for address family IPv4 Multicast:
        BGP table version is 175, Local Router ID is 20.0.0.6
        Status: s-suppressed, x-deleted, S-stale, d-dampened, h-history, *-valid, >-best
        Path type: i-internal, e-external, c-confed, l-local, a-aggregate, r-redist, I-injected
        Origin codes: i - IGP, e - EGP, ? - incomplete, | - multipath, & - backup

           Network            Next Hop            Metric     LocPrf     Weight Path
        *>i1.2.1.0/24         19.0.101.1                        100          0 2 3 4 i
        *>i1.2.2.0/24         19.0.101.1                        100          0 2 3 4 i


        Peer 19.0.101.1 routes for address family IPv6 Unicast:
        BGP table version is 173, Local Router ID is 20.0.0.6
        Status: s-suppressed, x-deleted, S-stale, d-dampened, h-history, *-valid, >-best
        Path type: i-internal, e-external, c-confed, l-local, a-aggregate, r-redist, I-injected
        Origin codes: i - IGP, e - EGP, ? - incomplete, | - multipath, & - backup

           Network            Next Hop            Metric     LocPrf     Weight Path


        Peer 19.0.101.1 routes for address family IPv6 Multicast:
        BGP table version is 6, Local Router ID is 20.0.0.6
        Status: s-suppressed, x-deleted, S-stale, d-dampened, h-history, *-valid, >-best
        Path type: i-internal, e-external, c-confed, l-local, a-aggregate, r-redist, I-injected
        Origin codes: i - IGP, e - EGP, ? - incomplete, | - multipath, & - backup

           Network            Next Hop            Metric     LocPrf     Weight Path


        Peer 19.0.101.1 routes for address family VPNv4 Unicast:
        BGP table version is 183, Local Router ID is 20.0.0.6
        Status: s-suppressed, x-deleted, S-stale, d-dampened, h-history, *-valid, >-best
        Path type: i-internal, e-external, c-confed, l-local, a-aggregate, r-redist, I-injected
        Origin codes: i - IGP, e - EGP, ? - incomplete, | - multipath, & - backup

           Network            Next Hop            Metric     LocPrf     Weight Path
        Route Distinguisher: 0:0

        Route Distinguisher: 101:100
        * i1.3.1.0/24         19.0.101.1            4444        100          0 3 10 20 4 5 6 3 10 20 4 5 6 i
        * i1.3.2.0/24         19.0.101.1            4444        100          0 3 10 20 4 5 6 3 10 20 4 5 6 i

        Route Distinguisher: 102:100


        Peer 19.0.101.1 routes for address family VPNv6 Unicast:
        BGP table version is 13, Local Router ID is 20.0.0.6
        Status: s-suppressed, x-deleted, S-stale, d-dampened, h-history, *-valid, >-best
        Path type: i-internal, e-external, c-confed, l-local, a-aggregate, r-redist, I-injected
        Origin codes: i - IGP, e - EGP, ? - incomplete, | - multipath, & - backup

           Network            Next Hop            Metric     LocPrf     Weight Path
        Route Distinguisher: 100:200
        *>iaaaa:1::/113       ::ffff:19.0.101.1
                                                    4444        100          0 i
        *>iaaaa:1::8000/113   ::ffff:19.0.101.1
                                                    4444        100          0 i

        Route Distinguisher: 0xbb00010000000000


        Peer 19.0.101.1 routes for address family Link-State:
        BGP table version is 173, Local Router ID is 20.0.0.6
        Status: s-suppressed, x-deleted, S-stale, d-dampened, h-history, *-valid, >-best
        Path type: i-internal, e-external, c-confed, l-local, a-aggregate, r-redist, I-injected
        Origin codes: i - IGP, e - EGP, ? - incomplete, | - multipath, & - backup

           Network            Next Hop            Metric     LocPrf     Weight Path
        *>i[2]:[77][7,0][9.9.9.9,1,151587081][29.1.1.1,22][19.0.101.1,29.0.1.30]/616
                              19.0.101.1            4444        100          0 3 10 20 30 40 50 60 70 80 90 i
        *>i[2]:[77][7,0][9.9.9.9,2,151587081][29.1.1.1,22][19.0.101.1,29.0.1.31]/616
                              19.0.101.1            4444        100          0 3 10 20 30 40 50 60 70 80 90 i
        '''}

    def test_show_bgp_vrf_all_neighbors_received_routes_golden(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output)
        obj = ShowBgpVrfAllNeighborsReceivedRoutes(device=self.device)
        parsed_output = obj.parse(vrf='default', neighbor='21.0.0.2')
        self.assertEqual(parsed_output,self.golden_parsed_output)

    def test_show_bgp_vrf_all_neighbors_received_routes_golden2(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output2)
        obj = ShowBgpVrfAllNeighborsReceivedRoutes(device=self.device)
        parsed_output = obj.parse(vrf='default', neighbor='19.0.101.1')
        self.assertEqual(parsed_output,self.golden_parsed_output2)

    def test_show_bgp_vrf_all_neighbors_received_routes_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowBgpVrfAllNeighborsReceivedRoutes(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse(vrf='default', neighbor='21.0.0.2')


# ========================================================================
# Unit test for 'show running-config bgp'
# ========================================================================

class test_show_running_config_bgp(unittest.TestCase):

    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output = {
        "bgp": {
            "bgp_id": 333,
            "protocol_shutdown": True,
            "vrf": {
              "management": {
                "graceful_restart": True,
                "log_neighbor_changes": False,
                "neighbor_id": {
                  "5.5.5.5": {'nbr_disable_connected_check': False,
                              'nbr_ebgp_multihop': False,
                              'nbr_fall_over_bfd': False,
                              'nbr_local_as_dual_as': False,
                              'nbr_local_as_no_prepend': False,
                              'nbr_local_as_replace_as': False,
                              'nbr_password_text': '3 '
                                                   '386c0565965f89de',
                              'nbr_remove_private_as': False,
                              'nbr_shutdown': False,
                              'nbr_suppress_four_byte_as_capability': False}
                },
                "enforce_first_as": True,
                "flush_routes": False,
                "fast_external_fallover": True,
                "isolate": False
              },
              "ac": {
                "log_neighbor_changes": False,
                "bestpath_cost_community_ignore": False,
                "bestpath_med_missing_at_worst": False,
                "enforce_first_as": True,
                "flush_routes": False,
                "always_compare_med": True,
                "graceful_restart": True,
                "bestpath_compare_routerid": False,
                "af_name": {
                  "ipv4 unicast": {
                    "af_client_to_client_reflection": True
                  }
                },
                "neighbor_id": {
                  "2.2.2.2": {
                    "nbr_disable_connected_check": True,
                    "nbr_local_as_replace_as": False,
                    "nbr_local_as_no_prepend": False,
                    "nbr_description": "ja",
                    "nbr_af_name": {
                      "ipv4 unicast": {
                        "nbr_af_allowas_in_as_number": 3,
                        "nbr_af_route_reflector_client": False,
                        "nbr_af_send_community": "both",
                        "nbr_af_allowas_in": True,
                        "nbr_af_maximum_prefix_max_prefix_no": 2
                      }
                    },
                    "nbr_shutdown": False,
                    "nbr_remove_private_as": True,
                    "nbr_local_as_dual_as": False,
                    "nbr_ebgp_multihop": False,
                    "nbr_suppress_four_byte_as_capability": True,
                    "nbr_fall_over_bfd": True,
                    "nbr_local_as_as_no": "222"
                  }
                },
                "fast_external_fallover": True,
                "isolate": False
              },
              "vpn1": {
                "graceful_restart": True,
                "log_neighbor_changes": False,
                "af_name": {
                  "ipv4 unicast": {
                    "af_dampening_reuse_time": 10,
                    "af_client_to_client_reflection": True,
                    "af_redist_static_route_policy": "PERMIT_ALL_RM",
                    "af_dampening_suppress_time": 30,
                    "af_dampening": True,
                    "af_redist_static": True,
                    "af_dampening_max_suppress_time": 2,
                    "af_dampening_half_life_time": 1
                  },
                  "ipv6 unicast": {
                    "af_dampening_reuse_time": 10,
                    "af_client_to_client_reflection": True,
                    "af_redist_static_route_policy": "PERMIT_ALL_RM",
                    "af_dampening_suppress_time": 30,
                    "af_dampening": True,
                    "af_redist_static": True,
                    "af_dampening_max_suppress_time": 2,
                    "af_dampening_half_life_time": 1
                  },
                  "ipv6 multicast": {
                    "af_dampening_reuse_time": 10,
                    "af_client_to_client_reflection": True,
                    "af_redist_static_route_policy": "PERMIT_ALL_RM",
                    "af_dampening_suppress_time": 30,
                    "af_dampening": True,
                    "af_redist_static": True,
                    "af_dampening_max_suppress_time": 2,
                    "af_dampening_half_life_time": 1
                  },
                  "ipv4 multicast": {
                    "af_client_to_client_reflection": True,
                    "af_redist_static_route_policy": "PERMIT_ALL_RM",
                    "af_redist_static": True
                  }
                },
                "enforce_first_as": True,
                "flush_routes": False,
                "fast_external_fallover": True,
                "isolate": False
              },
              "default": {
                "dynamic_med_interval": 70,
                "graceful_restart": False,
                "log_neighbor_changes": False,
                "af_name": {
                  "ipv4 unicast": {
                    "af_dampening_reuse_time": 10,
                    "af_aggregate_address_ipv4_address": "1.1.1.0",
                    "af_redist_static": True,
                    "af_v6_network_number": "1.1.1.0/24",
                    "af_redist_static_route_policy": "ADD_RT_400_400",
                    "af_dampening": True,
                    "af_client_to_client_reflection": True,
                    "af_aggregate_address_ipv4_mask": 24,
                    "af_dampening_suppress_time": 30,
                    "af_dampening_max_suppress_time": 2,
                    "af_v6_allocate_label_all": True,
                    "af_dampening_half_life_time": 1
                  },
                  "link-state": {
                    "af_dampening_reuse_time": 10,
                    "af_client_to_client_reflection": True,
                    "af_dampening_suppress_time": 30,
                    "af_dampening": True,
                    "af_dampening_max_suppress_time": 2,
                    "af_dampening_half_life_time": 1
                  },
                  "ipv4 multicast": {
                    "af_dampening_reuse_time": 10,
                    "af_client_to_client_reflection": True,
                    "af_redist_static_route_policy": "PERMIT_ALL_RM",
                    "af_dampening_suppress_time": 30,
                    "af_dampening": True,
                    "af_redist_static": True,
                    "af_dampening_max_suppress_time": 2,
                    "af_dampening_half_life_time": 1
                  },
                  "ipv6 unicast": {
                    "af_dampening_reuse_time": 10,
                    "af_client_to_client_reflection": True,
                    "af_redist_static_route_policy": "PERMIT_ALL_RM",
                    "af_dampening_suppress_time": 30,
                    "af_dampening": True,
                    "af_redist_static": True,
                    "af_dampening_max_suppress_time": 2,
                    "af_dampening_half_life_time": 1
                  },
                  "vpnv6 unicast": {
                    "af_dampening_reuse_time": 10,
                    "af_dampening_suppress_time": 30,
                    "af_dampening": True,
                    "af_dampening_max_suppress_time": 2,
                    "af_dampening_half_life_time": 1
                  },
                  "vpnv4 unicast": {
                    "af_dampening_route_map": "PASS-ALL",
                    "af_dampening": True,
                    "af_nexthop_trigger_enable": True,
                    "af_nexthop_trigger_delay_critical": 4,
                    "af_nexthop_trigger_delay_non_critical": 5
                  },
                  "ipv6 multicast": {
                    "af_dampening_reuse_time": 10,
                    "af_client_to_client_reflection": True,
                    "af_redist_static_route_policy": "PERMIT_ALL_RM",
                    "af_dampening_suppress_time": 30,
                    "af_dampening": True,
                    "af_redist_static": True,
                    "af_dampening_max_suppress_time": 2,
                    "af_dampening_half_life_time": 1
                  },
                  "ipv4 labeled-unicast": {}
                },
                "neighbor_id": {
                  "fec1::2002": {
                    "nbr_local_as_replace_as": False,
                    "nbr_af_name": {
                      "ipv4 unicast": {
                        "nbr_af_soft_reconfiguration": True,
                        "nbr_af_route_reflector_client": False,
                        "nbr_af_send_community": "both",
                        "nbr_af_allowas_in": False
                      },
                      "link-state": {
                        "nbr_af_route_reflector_client": False,
                        "nbr_af_send_community": "both",
                        "nbr_af_allowas_in": False
                      },
                      "ipv6 multicast": {
                        "nbr_af_soft_reconfiguration": True,
                        "nbr_af_route_reflector_client": False,
                        "nbr_af_send_community": "both",
                        "nbr_af_allowas_in": False
                      },
                      "ipv6 unicast": {
                        "nbr_af_soft_reconfiguration": True,
                        "nbr_af_route_reflector_client": False,
                        "nbr_af_send_community": "both",
                        "nbr_af_allowas_in": False
                      }
                    },
                    "nbr_disable_connected_check": False,
                    "nbr_remove_private_as": False,
                    "nbr_local_as_dual_as": False,
                    "nbr_ebgp_multihop": False,
                    "nbr_local_as_no_prepend": False,
                    "nbr_shutdown": False,
                    "nbr_suppress_four_byte_as_capability": False,
                    "nbr_fall_over_bfd": False,
                    "nbr_remote_as": 888
                  },
                  "21.0.102.1": {
                    "nbr_local_as_replace_as": False,
                    "nbr_af_name": {
                      "ipv4 unicast": {
                        "nbr_af_soft_reconfiguration": True,
                        "nbr_af_route_reflector_client": True,
                        "nbr_af_send_community": "both",
                        "nbr_af_allowas_in": False
                      },
                      "link-state": {
                        "nbr_af_route_reflector_client": True,
                        "nbr_af_send_community": "both",
                        "nbr_af_allowas_in": False
                      },
                      "ipv4 multicast": {
                        "nbr_af_soft_reconfiguration": True,
                        "nbr_af_route_reflector_client": True,
                        "nbr_af_send_community": "both",
                        "nbr_af_allowas_in": False
                      },
                      "ipv6 unicast": {
                        "nbr_af_soft_reconfiguration": True,
                        "nbr_af_route_reflector_client": True,
                        "nbr_af_send_community": "both",
                        "nbr_af_allowas_in": False
                      },
                      "vpnv6 unicast": {
                        "nbr_af_route_reflector_client": True,
                        "nbr_af_send_community": "both",
                        "nbr_af_allowas_in": False
                      },
                      "vpnv4 unicast": {
                        "nbr_af_route_reflector_client": False,
                        "nbr_af_send_community": "both",
                        "nbr_af_allowas_in": False
                      },
                      "ipv6 multicast": {
                        "nbr_af_soft_reconfiguration": True,
                        "nbr_af_route_reflector_client": True,
                        "nbr_af_send_community": "both",
                        "nbr_af_allowas_in": False
                      }
                    },
                    "nbr_disable_connected_check": False,
                    "nbr_remove_private_as": False,
                    "nbr_local_as_dual_as": False,
                    "nbr_ebgp_multihop": False,
                    "nbr_local_as_no_prepend": False,
                    "nbr_shutdown": False,
                    "nbr_suppress_four_byte_as_capability": False,
                    "nbr_fall_over_bfd": False,
                    "nbr_remote_as": 333
                  },
                  "21.0.201.1": {
                    "nbr_local_as_replace_as": False,
                    "nbr_af_name": {
                      "ipv4 unicast": {
                        "nbr_af_soft_reconfiguration": True,
                        "nbr_af_route_reflector_client": False,
                        "nbr_af_send_community": "both",
                        "nbr_af_allowas_in": False
                      },
                      "link-state": {
                        "nbr_af_route_reflector_client": False,
                        "nbr_af_send_community": "both",
                        "nbr_af_allowas_in": False
                      },
                      "ipv4 multicast": {
                        "nbr_af_soft_reconfiguration": True,
                        "nbr_af_route_reflector_client": False,
                        "nbr_af_send_community": "both",
                        "nbr_af_allowas_in": False
                      },
                      "ipv6 unicast": {
                        "nbr_af_soft_reconfiguration": True,
                        "nbr_af_route_reflector_client": False,
                        "nbr_af_send_community": "both",
                        "nbr_af_allowas_in": False
                      },
                      "vpnv6 unicast": {
                        "nbr_af_route_reflector_client": False,
                        "nbr_af_send_community": "both",
                        "nbr_af_allowas_in": False
                      },
                      "vpnv4 unicast": {
                        "nbr_af_route_reflector_client": False,
                        "nbr_af_send_community": "both",
                        "nbr_af_allowas_in": False
                      },
                      "ipv6 multicast": {
                        "nbr_af_soft_reconfiguration": True,
                        "nbr_af_route_reflector_client": False,
                        "nbr_af_send_community": "both",
                        "nbr_af_allowas_in": False
                      }
                    },
                    "nbr_disable_connected_check": False,
                    "nbr_remove_private_as": False,
                    "nbr_local_as_dual_as": False,
                    "nbr_ebgp_multihop": False,
                    "nbr_local_as_no_prepend": False,
                    "nbr_shutdown": False,
                    "nbr_suppress_four_byte_as_capability": False,
                    "nbr_fall_over_bfd": False,
                    "nbr_remote_as": 888
                  },
                  "21.0.101.1": {
                    "nbr_local_as_replace_as": False,
                    "nbr_af_name": {
                      "ipv4 unicast": {
                        "nbr_af_soft_reconfiguration": True,
                        "nbr_af_route_reflector_client": True,
                        "nbr_af_send_community": "both",
                        "nbr_af_allowas_in": False
                      },
                      "link-state": {
                        "nbr_af_route_reflector_client": True,
                        "nbr_af_send_community": "both",
                        "nbr_af_allowas_in": False
                      },
                      "ipv4 multicast": {
                        "nbr_af_soft_reconfiguration": True,
                        "nbr_af_route_reflector_client": True,
                        "nbr_af_send_community": "both",
                        "nbr_af_allowas_in": False
                      },
                      "ipv6 unicast": {
                        "nbr_af_soft_reconfiguration": True,
                        "nbr_af_route_reflector_client": True,
                        "nbr_af_send_community": "both",
                        "nbr_af_allowas_in": False
                      },
                      "vpnv6 unicast": {
                        "nbr_af_route_reflector_client": True,
                        "nbr_af_send_community": "both",
                        "nbr_af_allowas_in": False
                      },
                      "vpnv4 unicast": {
                        "nbr_af_route_reflector_client": True,
                        "nbr_af_send_community": "both",
                        "nbr_af_allowas_in": False
                      },
                      "ipv6 multicast": {
                        "nbr_af_soft_reconfiguration": True,
                        "nbr_af_route_reflector_client": True,
                        "nbr_af_send_community": "both",
                        "nbr_af_allowas_in": False
                      }
                    },
                    "nbr_disable_connected_check": False,
                    "nbr_remove_private_as": False,
                    "nbr_local_as_dual_as": False,
                    "nbr_ebgp_multihop": False,
                    "nbr_local_as_no_prepend": False,
                    "nbr_shutdown": False,
                    "nbr_suppress_four_byte_as_capability": False,
                    "nbr_fall_over_bfd": False,
                    "nbr_remote_as": 333
                  },
                  "fec1::1002": {
                    "nbr_local_as_replace_as": False,
                    "nbr_af_name": {
                      "ipv4 unicast": {
                        "nbr_af_soft_reconfiguration": True,
                        "nbr_af_route_reflector_client": True,
                        "nbr_af_send_community": "both",
                        "nbr_af_allowas_in": False
                      }
                    },
                    "nbr_disable_connected_check": False,
                    "nbr_remove_private_as": False,
                    "nbr_local_as_dual_as": False,
                    "nbr_ebgp_multihop": False,
                    "nbr_local_as_no_prepend": False,
                    "nbr_shutdown": False,
                    "nbr_suppress_four_byte_as_capability": False,
                    "nbr_fall_over_bfd": False,
                    "nbr_remote_as": 333
                  },
                  "4.4.4.4": {}
                },
                "disable_policy_batching_ipv4": "s",
                "cluster_id": "3",
                "enforce_first_as": False,
                "flush_routes": True,
                "fast_external_fallover": True,
                "isolate": True
              }
            },
            "ps_name": {
              "PEER-SESSION": {
                "ps_ebgp_multihop": True,
                "ps_fall_over_bfd": False,
                "ps_shutdown": False,
                "ps_local_as_dual_as": False,
                "ps_local_as_replace_as": False,
                "ps_ebgp_multihop_max_hop": 3,
                "ps_suppress_four_byte_as_capability": False,
                "ps_local_as_no_prepend": False,
                "ps_disable_connected_check": False
                }
            }
        }
    }


    golden_output = {'execute.return_value': '''
        pinxdt-n9kv-3# show run bgp

        !Command: show running-config bgp
        !Time: Wed Jun 28 06:23:27 2017

        version 7.0(3)I7(1)
        feature bgp

        router bgp 333
          dynamic-med-interval 70
          shutdown
          cluster-id 3
          no graceful-restart
          flush-routes
          isolate
          disable-policy-batching ipv4 prefix-list s
          no enforce-first-as
          event-history objstore size large
          address-family ipv4 multicast
            dampening 1 10 30 2
            redistribute static route-map PERMIT_ALL_RM
          address-family ipv4 unicast
            dampening 1 10 30 2
            network 1.1.1.0/24
            redistribute static route-map ADD_RT_400_400
            aggregate-address 1.1.1.0/24
            inject-map ORIGINATE_IPV4 exist-map INJECTED_IPV4 copy-attributes
            allocate-label all
          address-family ipv6 multicast
            dampening 1 10 30 2
            redistribute static route-map PERMIT_ALL_RM
          address-family ipv6 unicast
            dampening 1 10 30 2
            redistribute static route-map PERMIT_ALL_RM
            inject-map ORIGINATE_IPV6 exist-map INJECTED_IPV6 copy-attributes
          address-family vpnv4 unicast
            dampening route-map PASS-ALL
            nexthop trigger-delay critical 4 non-critical 5
          address-family vpnv6 unicast
            dampening 1 10 30 2
          address-family ipv4 labeled-unicast
          address-family link-state
            dampening 1 10 30 2
          template peer-session PEER-SESSION
            ebgp-multihop 3
          neighbor fec1::1002
            remote-as 333
            address-family ipv4 unicast
              send-community
              send-community extended
              route-reflector-client
              soft-reconfiguration inbound always
          neighbor fec1::2002
            remote-as 888
            address-family ipv4 unicast
              send-community
              send-community extended
              soft-reconfiguration inbound always
            address-family ipv6 multicast
              send-community
              send-community extended
              soft-reconfiguration inbound always
            address-family ipv6 unicast
              send-community
              send-community extended
              soft-reconfiguration inbound always
            address-family link-state
              send-community
              send-community extended
          neighbor 4.4.4.4
          neighbor 21.0.101.1
            remote-as 333
            address-family ipv4 multicast
              send-community
              send-community extended
              route-reflector-client
              soft-reconfiguration inbound always
            address-family ipv4 unicast
              send-community
              send-community extended
              route-reflector-client
              soft-reconfiguration inbound always
            address-family ipv6 multicast
              send-community
              send-community extended
              route-reflector-client
              soft-reconfiguration inbound always
            address-family ipv6 unicast
              send-community
              send-community extended
              route-reflector-client
              soft-reconfiguration inbound always
            address-family vpnv4 unicast
              send-community
              send-community extended
              route-reflector-client
            address-family vpnv6 unicast
              send-community
              send-community extended
              route-reflector-client
            address-family link-state
              send-community
              send-community extended
              route-reflector-client
          neighbor 21.0.102.1
            remote-as 333
            address-family ipv4 multicast
              send-community
              send-community extended
              route-reflector-client
              soft-reconfiguration inbound always
            address-family ipv4 unicast
              send-community
              send-community extended
              route-reflector-client
              soft-reconfiguration inbound always
            address-family ipv6 multicast
              send-community
              send-community extended
              route-reflector-client
              soft-reconfiguration inbound always
            address-family ipv6 unicast
              send-community
              send-community extended
              route-reflector-client
              soft-reconfiguration inbound always
            address-family vpnv4 unicast
              send-community
              send-community extended
            address-family vpnv6 unicast
              send-community
              send-community extended
              route-reflector-client
            address-family link-state
              send-community
              send-community extended
              route-reflector-client
          neighbor 21.0.201.1
            remote-as 888
            address-family ipv4 multicast
              send-community
              send-community extended
              soft-reconfiguration inbound always
            address-family ipv4 unicast
              send-community
              send-community extended
              soft-reconfiguration inbound always
            address-family ipv6 multicast
              send-community
              send-community extended
              soft-reconfiguration inbound always
            address-family ipv6 unicast
              send-community
              send-community extended
              soft-reconfiguration inbound always
            address-family vpnv4 unicast
              send-community
              send-community extended
            address-family vpnv6 unicast
              send-community
              send-community extended
            address-family link-state
              send-community
              send-community extended
          vrf ac
            bestpath always-compare-med
            address-family ipv4 unicast
            neighbor 2.2.2.2
              bfd
              local-as 222
              description ja
              remove-private-as
              disable-connected-check
              capability suppress 4-byte-as
              address-family ipv4 unicast
                allowas-in 3
                send-community
                send-community extended
                maximum-prefix 2
          vrf management
            neighbor 5.5.5.5
              password 3 386c0565965f89de
          vrf vpn1
            address-family ipv4 multicast
              redistribute static route-map PERMIT_ALL_RM
            address-family ipv4 unicast
              dampening 1 10 30 2
              redistribute static route-map PERMIT_ALL_RM
            address-family ipv6 multicast
              dampening 1 10 30 2
              redistribute static route-map PERMIT_ALL_RM
            address-family ipv6 unicast
              dampening 1 10 30 2
              redistribute static route-map PERMIT_ALL_RM
        vrf context vpn1
          rd 1:100
          address-family ipv4 unicast
            route-target import 100:1
            route-target export 100:1
            route-target export 400:400
            export map PERMIT_ALL_RM
            import map PERMIT_ALL_RM
            import vrf default map PERMIT_ALL_RM
            export vrf default map PERMIT_ALL_RM
          address-family ipv6 unicast
            route-target import 1:100
            route-target export 1:100
            route-target export 600:600
            export map PERMIT_ALL_RM
            import map PERMIT_ALL_RM
            import vrf default map PERMIT_ALL_RM
            export vrf default map PERMIT_ALL_RM
        vrf context vpn2
          rd 2:100
          address-family ipv4 unicast
            route-target import 400:400
          address-family ipv6 unicast
            route-target import 600:600
        '''}

    def test_golden(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output)
        obj = ShowRunningConfigBgp(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output)


    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowRunningConfigBgp(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()


if __name__ == '__main__':
    unittest.main()
