
# Python
import unittest
from unittest.mock import Mock
import xml.etree.ElementTree as ET

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from metaparser.util.exceptions import SchemaEmptyParserError, SchemaMissingKeyError

# iosxr show_bgp
from parser.iosxr.show_bgp import ShowPlacementProgramAll,\
                                  ShowBgpInstanceAfGroupConfiguration,\
                                  ShowBgpInstanceSessionGroupConfiguration,\
                                  ShowBgpInstanceProcessDetail,\
                                  ShowBgpInstanceNeighborsDetail,\
                                  ShowBgpInstanceNeighborsAdvertisedRoutes,\
                                  ShowBgpInstanceNeighborsReceivedRoutes,\
                                  ShowBgpInstanceNeighborsRoutes


# ==========================================
# Unit test for 'show placement program all'
# ==========================================

class test_show_placement_program_all(unittest.TestCase):
    
    device = Device(name='aDevice')
    device0 = Device(name='bDevice')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output = {
        'program': 
            {'rcp_fs':
                {'instance':
                    {'default':
                        {'active': '0/0/CPU0',
                        'active_state': 'RUNNING',
                        'group': 'central-services',
                        'jid': '1168',
                        'standby': 'NONE',
                        'standby_state': 'NOT_SPAWNED'}}},
            'ospf': 
                {'instance':
                    {'1':
                        {'active': '0/0/CPU0',
                        'active_state': 'RUNNING',
                        'group': 'v4-routing',
                        'jid': '1018',
                        'standby': 'NONE',
                        'standby_state': 'NOT_SPAWNED'}}},
            'bgp': 
                {'instance':
                    {'default':
                        {'active': '0/0/CPU0',
                        'active_state': 'RUNNING',
                        'group': 'v4-routing',
                        'jid': '1018',
                        'standby': 'NONE',
                        'standby_state': 'NOT_SPAWNED'}}},
            'statsd_manager_g': 
                {'instance':
                    {'default':
                        {'active': '0/0/CPU0',
                        'active_state': 'RUNNING',
                        'group': 'netmgmt',
                        'jid': '1141',
                        'standby': 'NONE',
                        'standby_state': 'NOT_SPAWNED'}}},
            'pim': 
                {'instance':
                    {'default':
                        {'active': '0/0/CPU0',
                        'active_state': 'RUNNING',
                        'group': 'mcast-routing',
                        'jid': '1158',
                        'standby': 'NONE',
                        'standby_state': 'NOT_SPAWNED'}}},
            'ipv6_local': 
                {'instance':
                    {'default':
                        {'active': '0/0/CPU0',
                        'active_state': 'RUNNING',
                        'group': 'v6-routing',
                        'jid': '1156',
                        'standby': 'NONE',
                        'standby_state': 'NOT_SPAWNED'}}}
            },
        }
    
    golden_output = {'execute.return_value': '''
        Display program related information. This is the program information corresponding to this LR as
        perceived by the placement daemon.
        ------------------------------------------------------------------------------------------------------------------------------------------
                           Process Information
        ------------------------------------------------------------------------------------------------------------------------------------------
        Program                                 Group               jid  Active         Active-state             Standby        Standby-state  
        ------------------------------------------------------------------------------------------------------------------------------------------
        rcp_fs                                  central-services    1168 0/0/CPU0       RUNNING                  NONE           NOT_SPAWNED    
        ospf(1)                                 v4-routing          1018 0/0/CPU0       RUNNING                  NONE           NOT_SPAWNED    
        bgp(default)                            v4-routing          1018 0/0/CPU0       RUNNING                  NONE           NOT_SPAWNED
        statsd_manager_g                        netmgmt             1141 0/0/CPU0       RUNNING                  NONE           NOT_SPAWNED    
        pim                                     mcast-routing       1158 0/0/CPU0       RUNNING                  NONE           NOT_SPAWNED    
        ipv6_local                              v6-routing          1156 0/0/CPU0       RUNNING                  NONE           NOT_SPAWNED    
      '''}


    def test_empty(self):
        self.device1 = Mock(**self.empty_output)
        placement_program_all_obj = ShowPlacementProgramAll(device=self.device1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = placement_program_all_obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        placement_program_all_obj = ShowPlacementProgramAll(device=self.device)
        parsed_output = placement_program_all_obj.parse()
        self.maxDiff = None
        self.assertEqual(parsed_output,self.golden_parsed_output)


# ========================================================
# Unit test for 'show bgp instance af-group configuration'
# ========================================================

class test_show_bgp_instance_af_group_configuration(unittest.TestCase):
    
    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}
    golden_parsed_output = {
        "instance": {
            "default": {
                "pp_name": {
                    "af_group": {
                        "address_family": "ipv4 unicast",
                        "default_originate": True,
                        "default_originate_route_map": "allpass",
                        "max_prefix_no": 429,
                        "max_prefix_threshold": 75,
                        "max_prefix_restart": 35,
                        "next_hop_self": True,
                        "route_map_name_in": "allpass",
                        "route_map_name_out": "allpass",
                        "route_reflector_client": True,
                        "send_community": "both",
                        "send_comm_ebgp": True,
                        "send_ext_comm_ebgp": True,
                        "soo": "100:1",
                        "soft_reconfiguration": "inbound always",
                        "allowas_in_as_number": 10,
                        "allowas_in": True,
                        "as_override": True
                    }
                }
            }
        }

    }

    golden_output = {'execute.return_value': '''
        Fri Jul 14 16:30:21.081 EDT
        Building configuration...    
        router bgp 100 af-group af_group address-family ipv4 unicast 

            Wed Jul 12 15:42:07.027 EDT
        af-group af_group address-family IPv4 Unicast
          default-originate policy allpass            []
          maximum-prefix 429 75 35                    []
          next-hop-self                               []
          policy allpass in                           []
          policy allpass out                          []
          route-reflector-client                      []
          send-community-ebgp                         []
          send-extended-community-ebgp                []
          site-of-origin 100:1                        []
          soft-reconfiguration inbound always         []
          allowas-in 10                               []
          as-override                                 []
        '''}

    def test_empty(self):
        self.device1 = Mock(**self.empty_output)
        obj = ShowBgpInstanceAfGroupConfiguration(device=self.device1)
        self.maxDiff = None
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = ShowBgpInstanceAfGroupConfiguration(device=self.device)
        parsed_output = obj.parse()
        self.maxDiff = None
        self.assertEqual(parsed_output,self.golden_parsed_output)


# =============================================================
# Unit test for 'show bgp instance session group configuration'
# =============================================================

class test_show_bgp_instance_session_group_configuration(unittest.TestCase):
    
    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}
    golden_parsed_output = {
        "instance": {
            "default": {
                "peer_session": {
                    "SG": {
                        "remote_as": 333,
                        "fall_over_bfd": True,
                        "password_text": "094F471A1A0A464058",
                        "holdtime": 30,
                        "transport_connection_mode": "active-only",
                        "ebgp_multihop_max_hop": 254,
                        "local_replace_as": True,
                        "ps_minimum_holdtime": 3,
                        "keepalive_interval": 10,
                        "shutdown": True,
                        "local_dual_as": True,
                        "local_no_prepend": True,
                        "ebgp_multihop_enable": True,
                        "suppress_four_byte_as_capability": True,
                        "local_as_as_no": 200,
                        "description": "SG_group",
                        "update_source": 'loopback0',
                        "disable_connected_check": True
                    }
                }
            }
        }
    }

    golden_output = {'execute.return_value': '''
        Fri Jul 14 17:50:40.461 EDT
        Building configuration...
        router bgp 100 session-group SG 

        Thu Jul 13 12:28:48.673 EDT
        session-group SG
         remote-as 333                              []
         description SG_group                       []
         ebgp-multihop 254                          []
         local-as 200 no-prepend replace-as dual-as []
         password encrypted 094F471A1A0A464058      []
         shutdown                                   []
         timers 10 30 3                             []
         update-source Loopback0                    []
         suppress-4byteas                           []
         session-open-mode active-only              []
         bfd fast-detect                            []
         ignore-connected                           []
        '''}

    def test_empty(self):
        self.device1 = Mock(**self.empty_output)
        obj = ShowBgpInstanceSessionGroupConfiguration(device=self.device1)
        self.maxDiff = None
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = ShowBgpInstanceSessionGroupConfiguration(device=self.device)
        parsed_output = obj.parse()
        self.maxDiff = None
        self.assertEqual(parsed_output,self.golden_parsed_output)


# ===========================================================
# Unit test for 'show bgp instance all vrf all process detail
# ===========================================================
class test_show_bgp_instance_all_vrf_all_process_detail(unittest.TestCase):
    
    device = Device(name='aDevice')
    device0 = Device(name='bDevice')
    empty_output = {'execute.return_value': ''}
    
    golden_parsed_output = {'instance': 
        {'default': 
            {'vrf': 
                {'default': 
                    {'active_cluster_id': '1.1.1.1',
                        'address_family': 
                            {'vpnv4 unicast': 
                                {'attribute_download': 'Disabled',
                                'bgp_table_version': '43',
                                'chunk_elememt_size': '3',
                                'client_reflection': True,
                                'dampening': False,
                                'dynamic_med': True,
                                'dynamic_med_int': '10 '
                                                   'minutes',
                                'dynamic_med_periodic_timer': 'Not '
                                                              'Running',
                                'dynamic_med_timer': 'Not '
                                                     'Running',
                                'label_retention_timer_value': '5 '
                                                               'mins',
                                'main_table_version': '43',
                                'nexthop_resolution_minimum_prefix_length': '0 '
                                                                            '(not '
                                                                            'configured)',
                                                                                   'num_of_scan_segments': '1',
                                                                                    'permanent_network': 'unconfigured',
                                                                                    'prefix_scanned_per_segment': '100000',
                                                                                    'prefixes_path': {'remote prefixes': {'mem_used': 920,
                                                                                                                          'number': 10}},
                                                                                    'remote_local': {'remote prefixes': {'allocated': 10,
                                                                                                                         'freed': 0}},
                                                                                    'rib_has_not_converged': 'version '
                                                                                                             '0',
                                                                                    'rib_table_prefix_limit_reached': 'no',
                                                                                    'rib_table_prefix_limit_ver': '0',
                                                                                    'scan_interval': '60',
                                                                                    'soft_reconfig_entries': '0',
                                                                                    'state': 'normal '
                                                                                             'mode',
                                                                                    'table_bit_field_size': '1 ',
                                                                                    'table_version_acked_by_rib': '0',
                                                                                    'table_version_synced_to_rib': '43',
                                                                                    'thread': {'import thread': {'triggers': {'Jun 28 19:10:16.427': {'tbl_ver': 43,
                                                                                                                                                      'trig_tid': 3,
                                                                                                                                                      'ver': 43}}},
                                                                                               'label thread': {'triggers': {'Jun 28 19:10:16.427': {'tbl_ver': 43,
                                                                                                                                                     'trig_tid': 3,
                                                                                                                                                     'ver': 43}}},
                                                                                               'rib thread': {'triggers': {'Jun 28 18:29:29.595': {'tbl_ver': 43,
                                                                                                                                                   'trig_tid': 8,
                                                                                                                                                   'ver': 33}}},
                                                                                               'update thread': {'triggers': {'Jun 28 19:10:16.427': {'tbl_ver': 43,
                                                                                                                                                      'trig_tid': 8,
                                                                                                                                                      'ver': 43}}}},
                                                                                    'total_prefixes_scanned': '40'},
                                                                  'vpnv6 unicast': {'attribute_download': 'Disabled',
                                                                                    'bgp_table_version': '43',
                                                                                    'chunk_elememt_size': '3',
                                                                                    'client_reflection': True,
                                                                                    'dampening': False,
                                                                                   'dynamic_med': True,
                                                                                    'dynamic_med_int': '10 '
                                                                                                      'minutes',
                                                                                    'dynamic_med_periodic_timer': 'Not '
                                                                                                                  'Running',
                                                                                    'dynamic_med_timer': 'Not '
                                                                                                         'Running',
                                                                                    'label_retention_timer_value': '5 '
                                                                                                                   'mins',
                                                                                    'main_table_version': '43',
                                                                                    'nexthop_resolution_minimum_prefix_length': '0 '
                                                                                                                                '(not '
                                                                                                                                'configured)',
                                                                                    'num_of_scan_segments': '1',
                                                                                    'permanent_network': 'unconfigured',
                                                                                    'prefix_scanned_per_segment': '100000',
                                                                                    'prefixes_path': {'remote prefixes': {'mem_used': 1040,
                                                                                                                          'number': 10}},
                                                                                    'remote_local': {'remote prefixes': {'allocated': 10,
                                                                                                                         'freed': 0}},
                                                                                    'rib_has_not_converged': 'version '
                                                                                                             '0',
                                                                                    'rib_table_prefix_limit_reached': 'no',
                                                                                    'rib_table_prefix_limit_ver': '0',
                                                                                    'scan_interval': '60',
                                                                                    'soft_reconfig_entries': '0',
                                                                                    'state': 'normal '
                                                                                             'mode',
                                                                                    'table_bit_field_size': '1 ',
                                                                                    'table_version_acked_by_rib': '0',
                                                                                    'table_version_synced_to_rib': '43',
                                                                                    'thread': {'import thread': {'triggers': {'Jun 28 19:10:16.427': {'tbl_ver': 43,
                                                                                                                                                      'trig_tid': 3,
                                                                                                                                                      'ver': 43}}},
                                                                                               'label thread': {'triggers': {'Jun 28 19:10:16.427': {'tbl_ver': 43,
                                                                                                                                                     'trig_tid': 3,
                                                                                                                                                     'ver': 43}}},
                                                                                               'rib thread': {'triggers': {'Jun 28 18:29:34.604': {'tbl_ver': 43,
                                                                                                                                                   'trig_tid': 8,
                                                                                                                                                   'ver': 33}}},
                                                                                               'update thread': {'triggers': {'Jun 28 19:10:16.427': {'tbl_ver': 43,
                                                                                                                                                      'trig_tid': 8,
                                                                                                                                                      'ver': 43}}}},
                                                                                    'total_prefixes_scanned': '40'}},
                                               'as_number': 100,
                                               'as_system_number_format': 'ASPLAIN',
                                               'att': {'as_paths': {'memory_used': 480,
                                                                    'number': 6},
                                                       'attributes': {'memory_used': 912,
                                                                      'number': 6},
                                                       'communities': {'memory_used': 0,
                                                                       'number': 0},
                                                       'extended_communities': {'memory_used': 480,
                                                                                'number': 6},
                                                       'imported_paths': {'memory_used': 2200,
                                                                          'number': 25},
                                                       'local_paths': {'memory_used': 2640,
                                                                       'number': 30},
                                                       'local_prefixes': {'memory_used': 3210,
                                                                          'number': 30},
                                                       'local_rds': {'memory_used': 160,
                                                                     'number': 2},
                                                       'nexthop_entries': {'memory_used': 12800,
                                                                           'number': 32},
                                                       'pe_distinguisher_labels': {'memory_used': 0,
                                                                                   'number': 0},
                                                       'pmsi_tunnel_attr': {'memory_used': 0,
                                                                            'number': 0},
                                                       'ppmp_attr': {'memory_used': 0,
                                                                     'number': 0},
                                                       'remote_paths': {'memory_used': 1760,
                                                                        'number': 20},
                                                       'remote_rds': {'memory_used': 160,
                                                                      'number': 2},
                                                       'ribrnh_tunnel_attr': {'memory_used': 0,
                                                                              'number': 0},
                                                       'route_reflector_entries': {'memory_used': 320,
                                                                                   'number': 4},
                                                       'total_paths': {'memory_used': 4400,
                                                                       'number': 50},
                                                       'total_prefixes': {'memory_used': 4280,
                                                                          'number': 40},
                                                       'total_rds': {'memory_used': 320,
                                                                     'number': 4},
                                                       'tunnel_encap_attr': {'memory_used': 0,
                                                                             'number': 0}},
                                               'bgp_speaker_process': 0,
                                               'bmp_pool_summary': {'100': {'alloc': 0,
                                                                            'free': 0},
                                                                   '1200': {'alloc': 0,
                                                                             'free': 0},
                                                                    '20000': {'alloc': 0,
                                                                              'free': 0}},
                                               'current_limit_for_bmp_buffer_size': 307,
                                               'current_utilization_of_bmp_buffer_limit': 0,
                                               'default_cluster_id': '1.1.1.1',
                                               'default_keepalive': 60,
                                               'default_local_preference': 100,
                                               'default_value_for_bmp_buffer_size': 307,
                                               'enforce_first_as_enabled': True,
                                               'fast_external_fallover': True,
                                               'generic_scan_interval': 60,
                                               'max_limit_for_bmp_buffer_size': 409,
                                               'message_logging_pool_summary': {'4500': {'alloc': 0,
                                                                                         'free': 0}},
                                               'neighbor_logging': True,
                                               'node': 'node0_0_CPU0',
                                               'non_stop_routing': True,
                                               'operation_mode': 'STANDALONE',
                                               'platform_rlimit_max': 2147483648,
                                               'pool': {'1200': {'alloc': 0,
                                                                 'free': 0},
                                                        '200': {'alloc': 0,
                                                                'free': 0},
                                                        '20000': {'alloc': 0,
                                                                  'free': 0},
                                                        '2200': {'alloc': 0,
                                                                 'free': 0},
                                                        '300': {'alloc': 311,
                                                                'free': 310},
                                                        '3300': {'alloc': 0,
                                                                 'free': 0},
                                                        '400': {'alloc': 6,
                                                                'free': 6},
                                                        '4000': {'alloc': 0,
                                                                 'free': 0},
                                                        '4500': {'alloc': 0,
                                                                 'free': 0},
                                                        '500': {'alloc': 20,
                                                                'free': 20},
                                                        '5000': {'alloc': 0,
                                                                 'free': 0},
                                                        '600': {'alloc': 12,
                                                                'free': 12},
                                                        '700': {'alloc': 2,
                                                                'free': 2},
                                                        '800': {'alloc': 0,
                                                                'free': 0},
                                                        '900': {'alloc': 0,
                                                                'free': 0}},
                                               'received_notifications': 0,
                                               'received_updates': 24,
                                               'restart_count': 1,
                                               'router_id': '1.1.1.1',
                                               'sent_notifications': 1,
                                               'sent_updates': 14,
                                               'update_delay': 120,
                                               'vrf_info': {'default': {'cfg': 2,
                                                                        'nbrs_estab': 2,
                                                                        'total': 1},
                                                            'non-default': {'cfg': 4,
                                                                            'nbrs_estab': 4,
                                                                            'total': 2}}}}}}}

    golden_output = {'execute.return_value': '''

        BGP instance 0: 'default'
        =========================

        BGP Process Information: 
        BGP is operating in STANDALONE mode
        Autonomous System number format: ASPLAIN
        Autonomous System: 100
        Router ID: 1.1.1.1 (manually configured)
        Default Cluster ID: 1.1.1.1
        Active Cluster IDs:  1.1.1.1
        Fast external fallover enabled
        Platform RLIMIT max: 2147483648 bytes
        Maximum limit for BMP buffer size: 409 MB
        Default value for BMP buffer size: 307 MB
        Current limit for BMP buffer size: 307 MB
        Current utilization of BMP buffer limit: 0 B
        Neighbor logging is enabled
        Enforce first AS enabled
        Default local preference: 100
        Default keepalive: 60
        Non-stop routing is enabled
        Update delay: 120
        Generic scan interval: 60

        BGP Speaker process: 0, Node: node0_0_CPU0
        Restart count: 1
                                   Total           Nbrs Estab/Cfg
        Default VRFs:              1               2/2
        Non-Default VRFs:          2               4/4

                                   Sent            Received
        Updates:                   14              24              
        Notifications:             1               0               

                                   Number          Memory Used
        Attributes:                6               912             
        AS Paths:                  6               480             
        Communities:               0               0               
        Extended communities:      6               480             
        PMSI Tunnel attr:          0               0               
        RIBRNH Tunnel attr:        0               0               
        PPMP attr:                 0               0               
        Tunnel Encap attr:         0               0               
        PE distinguisher labels:   0               0               
        Route Reflector Entries:   4               320             
        Nexthop Entries:           32              12800           

                                   Alloc           Free          
        Pool 200:                  0               0             
        Pool 300:                  311             310           
        Pool 400:                  6               6             
        Pool 500:                  20              20            
        Pool 600:                  12              12            
        Pool 700:                  2               2             
        Pool 800:                  0               0             
        Pool 900:                  0               0             
        Pool 1200:                 0               0             
        Pool 2200:                 0               0             
        Pool 3300:                 0               0             
        Pool 4000:                 0               0             
        Pool 4500:                 0               0             
        Pool 5000:                 0               0             
        Pool 20000:                0               0             

        Message logging pool summary:
                                   Alloc           Free          
        Pool 100:                  19              10            
        Pool 200:                  11              1             
        Pool 500:                  19              12            
        Pool 2200:                 0               0             
        Pool 4500:                 0               0             

        BMP pool summary:
                                   Alloc           Free          
        Pool 100:                  0               0           
        Pool 1200:                 0               0           
        Pool 20000:                0               0             

        Address family: VPNv4 Unicast
        Dampening is not enabled
        Client reflection is enabled in global config
        Dynamic MED is Disabled
        Dynamic MED interval : 10 minutes
        Dynamic MED Timer : Not Running
        Dynamic MED Periodic Timer : Not Running
        Scan interval: 60
        Total prefixes scanned: 40
        Prefixes scanned per segment: 100000
        Number of scan segments: 1
        Nexthop resolution minimum prefix-length: 0 (not configured)
        Main Table Version: 43
        Table version synced to RIB: 43
        Table version acked by RIB: 0
        RIB has not converged: version 0
        RIB table prefix-limit reached ?  [No], version 0
        Permanent Network Unconfigured

        State: Normal mode.
        BGP Table Version: 43
        Attribute download: Disabled
        Label retention timer value 5 mins
        Soft Reconfig Entries: 0
        Table bit-field size : 1 Chunk element size : 3

                           Last 8 Triggers       Ver         Tbl Ver     Trig TID  

        Label Thread       Jun 28 19:10:16.427   43          43          3         
                           Jun 28 19:10:16.417   43          43          3         
                           Jun 28 19:09:29.680   43          43          3         
                           Jun 28 19:09:29.670   43          43          3         
                           Jun 28 18:29:34.604   43          43          3         
                           Jun 28 18:29:29.595   33          43          4         
                           Jun 28 18:29:29.595   33          38          3         
                           Jun 28 18:24:52.694   33          33          3         
                           Total triggers: 15

        Import Thread      Jun 28 19:10:16.427   43          43          3         
                           Jun 28 19:10:16.417   43          43          3         
                           Jun 28 19:09:29.680   43          43          3         
                           Jun 28 19:09:29.670   43          43          3         
                           Jun 28 18:29:34.604   43          43          3         
                           Jun 28 18:29:29.595   43          43          8         
                           Jun 28 18:29:29.595   38          43          4         
                           Jun 28 18:29:29.595   33          38          3         
                           Total triggers: 16

        RIB Thread         Jun 28 18:29:29.595   33          43          8         
                           Jun 28 18:29:29.595   33          43          4         
                           Jun 28 18:24:26.135   13          33          4         
                           Jun 28 18:24:26.135   13          33          8         
                           Jun 28 18:24:26.135   13          33          4         
                           Jun 28 18:24:21.656   11          13          4         
                           Jun 28 18:21:26.418   1           11          8         
                           Jun 28 18:21:26.418   1           11          6         
                           Total triggers: 8

        Update Thread      Jun 28 19:10:16.427   43          43          8         
                           Jun 28 19:10:16.417   43          43          8         
                           Jun 28 19:09:29.680   43          43          8         
                           Jun 28 19:09:29.670   43          43          8         
                           Jun 28 18:29:34.604   43          43          8         
                           Jun 28 18:29:29.605   43          43          18        
                           Jun 28 18:29:29.595   33          43          8         
                           Jun 28 18:24:52.694   33          33          8         
                           Total triggers: 17

                              Allocated       Freed         
        Remote Prefixes:      10              0             
        Remote Paths:         20              0             
        Remote Path-elems:    10              0             

        Local Prefixes:       30              0             
        Local Paths:          30              0             

                              Number          Mem Used      
        Remote Prefixes:      10              920           
        Remote Paths:         20              1760          
        Remote Path-elems:    10              630           
        Remote RDs:           2               160           

        Local Prefixes:       30              2850          
        Local Paths:          30              2640          
        Local RDs:            2               160           

        Total Prefixes:       40              3800          
        Total Paths:          50              4400          
        Total Path-elems:     40              4400          
        Imported Paths:       25              2200          
        Total RDs:            4               320           


        Address family: VPNv6 Unicast
        Dampening is not enabled
        Client reflection is enabled in global config
        Dynamic MED is Disabled
        Dynamic MED interval : 10 minutes
        Dynamic MED Timer : Not Running
        Dynamic MED Periodic Timer : Not Running
        Scan interval: 60
        Total prefixes scanned: 40
        Prefixes scanned per segment: 100000
        Number of scan segments: 1
        Nexthop resolution minimum prefix-length: 0 (not configured)
        Main Table Version: 43
        Table version synced to RIB: 43
        Table version acked by RIB: 0
        RIB has not converged: version 0
        RIB table prefix-limit reached ?  [No], version 0
        Permanent Network Unconfigured

        State: Normal mode.
        BGP Table Version: 43
        Attribute download: Disabled
        Label retention timer value 5 mins
        Soft Reconfig Entries: 0
        Table bit-field size : 1 Chunk element size : 3

                           Last 8 Triggers       Ver         Tbl Ver     Trig TID  

        Label Thread       Jun 28 19:10:16.427   43          43          3         
                           Jun 28 19:10:16.417   43          43          3         
                           Jun 28 19:09:29.680   43          43          3         
                           Jun 28 19:09:29.670   43          43          3         
                           Jun 28 18:29:34.604   33          43          4         
                           Jun 28 18:29:34.604   33          38          3         
                           Jun 28 18:29:29.595   33          33          3         
                           Jun 28 18:24:52.694   33          33          3         
                           Total triggers: 15

        Import Thread      Jun 28 19:10:16.427   43          43          3         
                           Jun 28 19:10:16.417   43          43          3         
                           Jun 28 19:09:29.680   43          43          3         
                           Jun 28 19:09:29.670   43          43          3         
                           Jun 28 18:29:34.604   43          43          8         
                           Jun 28 18:29:34.604   38          43          4         
                           Jun 28 18:29:34.604   33          38          3         
                           Jun 28 18:29:29.595   33          33          3         
                           Total triggers: 16

        RIB Thread         Jun 28 18:29:34.604   33          43          8         
                           Jun 28 18:29:34.604   33          43          4         
                           Jun 28 18:24:26.135   13          33          4         
                           Jun 28 18:24:26.135   13          33          4         
                           Jun 28 18:24:21.656   11          13          8         
                           Jun 28 18:21:26.428   1           11          8         
                           Jun 28 18:21:26.418   1           11          6         
                           Total triggers: 7

        Update Thread      Jun 28 19:10:16.427   43          43          8         
                           Jun 28 19:10:16.417   43          43          8         
                           Jun 28 19:09:29.680   43          43          8         
                           Jun 28 19:09:29.670   43          43          8         
                           Jun 28 18:29:34.604   43          43          19        
                           Jun 28 18:29:34.604   33          43          8         
                           Jun 28 18:29:29.595   33          33          8         
                           Jun 28 18:24:52.694   33          33          8         
                           Total triggers: 17

                              Allocated       Freed         
        Remote Prefixes:      10              0             
        Remote Paths:         20              0             
        Remote Path-elems:    10              0             

        Local Prefixes:       30              0             
        Local Paths:          30              0             

                              Number          Mem Used      
        Remote Prefixes:      10              1040          
        Remote Paths:         20              1760          
        Remote Path-elems:    10              630           
        Remote RDs:           2               160           

        Local Prefixes:       30              3210          
        Local Paths:          30              2640          
        Local RDs:            2               160           

        Total Prefixes:       40              4280          
        Total Paths:          50              4400          
        Total Path-elems:     40              4400          
        Imported Paths:       25              2200          
        Total RDs:            4               320           
    '''}

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowBgpInstanceProcessDetail(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse(vrf_type='vrf')

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = ShowBgpInstanceProcessDetail(device=self.device)
        parsed_output = obj.parse(vrf_type='vrf')
        self.maxDiff = None
        self.assertEqual(parsed_output,self.golden_parsed_output)


# =============================================================
# Unit test for 'show bgp instance all vrf all neighbors detail
# =============================================================

class test_show_bgp_instance_all_vrf_all_neighbors_detail(unittest.TestCase):

    device = Device(name='aDevice')
    device0 = Device(name='bDevice')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output = {
        "instance": {
          "default": {
               "vrf": {
                    "default": {
                         "neighbor": {
                              "2.2.2.2": {
                                   "link_state": "internal link",
                                   "last_ka_expiry_before_second_last": "00:00:00",
                                   "inbound_message": "3",
                                   "bgp_session_transport": {
                                        "connection": {
                                             "last_reset": "00:00:00",
                                             "state": "established",
                                             "connections_established": 1,
                                             "connections_dropped": 0
                                        },
                                        "transport": {
                                             "local_host": "1.1.1.1",
                                             "if_handle": "0x00000000",
                                             "foreign_port": 179,
                                             "foreign_host": "2.2.2.2",
                                             "local_port": 46663
                                        }
                                   },
                                   "last_ka_error_ka_not_sent": "00:00:00",
                                   "min_acceptable_hold_time": 3,
                                   "router_id": "2.2.2.2",
                                   "last_write_written": 0,
                                   "second_last_write_before_attempted": 0,
                                   "last_ka_start_before_second_last": "00:00:00",
                                   "remote_as": 100,
                                   "bgp_negotiated_keepalive_timers": {
                                        "keepalive_interval": 60,
                                        "hold_time": 180
                                   },
                                   "last_write_pulse_rcvd": "Jun 28 19:03:35.294 ",
                                   "written": 19,
                                   "message_stats_output_queue": 0,
                                   "second_attempted": 19,
                                   "message_stats_input_queue": 0,
                                   "last_ka_expiry_before_reset": "00:00:00",
                                   "last_write_pulse_rcvd_before_reset": "00:00:00",
                                   "second_written": 19,
                                   "last_write_before_reset": "00:00:00",
                                   "attempted": 19,
                                   "second_last_write": "00:01:23",
                                   "last_ka_error_before_reset": "00:00:00",
                                   "bgp_neighbor_counters": {
                                        "messages": {
                                             "sent": {
                                                  "keepalives": "43",
                                                  "opens": "1",
                                                  "updates": "4",
                                                  "notifications": "0"
                                             },
                                             "received": {
                                                  "keepalives": "44",
                                                  "opens": "1",
                                                  "updates": "6",
                                                  "notifications": "0"
                                             }
                                        }
                                   },
                                   "last_write_thread_event_before_reset": "00:00:00",
                                   "last_write_attempted": 0,
                                   "precedence": "internet",
                                   "configured_hold_time": 180,
                                   "keepalive": 60,
                                   "local_as_as_no": 100,
                                   "last_read": "00:00:32",
                                   "second_last_write_before_written": 0,
                                   "minimum_time_between_adv_runs": 0,
                                   "multiprotocol_capability": "received",
                                   "address_family": {
                                        "vpnv4 unicast": {
                                             "last_synced_ack_version": 0,
                                             "last_ack_version": 43,
                                             "cummulative_no_prefixes_denied": 0,
                                             "refresh_request_status": "No Refresh request being processed",
                                             "prefix_suppressed": 0,
                                             "route_refresh_request_received": 0,
                                             "maximum_prefixes_allowed": 2097152,
                                             "neighbor_version": 43,
                                             "maximum_prefix_restart": 0,
                                             "eor_status": "was received during read-only mode",
                                             "best_paths": 10,
                                             "outstanding_version_objects_max": 1,
                                             "exact_no_prefixes_denied": 0,
                                             "prefix_withdrawn": 0,
                                             "outstanding_version_objects_current": 0,
                                             "route_refresh_request_sent": 0,
                                             "accepted_prefixes": 10,
                                             "maximum_prefix_threshold": "75%",
                                             "filter_group": "0.2",
                                             "maximum_prefix_warning_only": True,
                                             "update_group": "0.2",
                                             "additional_paths_operation": "None",
                                             "prefix_advertised": 5
                                        },
                                        "vpnv6 unicast": {
                                             "last_synced_ack_version": 0,
                                             "last_ack_version": 43,
                                             "cummulative_no_prefixes_denied": 0,
                                             "refresh_request_status": "No Refresh request being processed",
                                             "prefix_suppressed": 0,
                                             "route_refresh_request_received": 0,
                                             "maximum_prefixes_allowed": 1048576,
                                             "neighbor_version": 43,
                                             "maximum_prefix_restart": 0,
                                             "eor_status": "was received during read-only mode",
                                             "best_paths": 10,
                                             "outstanding_version_objects_max": 1,
                                             "exact_no_prefixes_denied": 0,
                                             "prefix_withdrawn": 0,
                                             "outstanding_version_objects_current": 0,
                                             "route_refresh_request_sent": 0,
                                             "accepted_prefixes": 10,
                                             "maximum_prefix_threshold": "75%",
                                             "filter_group": "0.2",
                                             "maximum_prefix_warning_only": True,
                                             "update_group": "0.2",
                                             "additional_paths_operation": "None",
                                             "prefix_advertised": 5
                                        }
                                   },
                                   "non_stop_routing": "enabled",
                                   "last_write": "00:00:23",
                                   "nsr_state": "None",
                                   "tcp_initial_sync_done": "---",
                                   "last_full_not_set_pulse_count": 93,
                                   "tcp_initial_sync": "---",
                                   "outbound_message": "3",
                                   "bgp_negotiated_capabilities": {
                                        "four_octets_asn": "advertised received",
                                        "vpnv6_unicast": "advertised received",
                                        "route_refresh": "advertised received",
                                        "vpnv4_unicast": "advertised received"
                                   },
                                   "last_write_thread_event_second_last": "00:00:00",
                                   "second_last_write_before_reset": "00:00:00",
                                   "last_ka_start_before_reset": "00:00:00",
                                   "last_read_before_reset": "00:00:00"
                              },
                              "3.3.3.3": {
                                   "link_state": "internal link",
                                   "last_ka_expiry_before_second_last": "00:00:00",
                                   "inbound_message": "3",
                                   "bgp_session_transport": {
                                        "connection": {
                                             "last_reset": "00:00:00",
                                             "state": "established",
                                             "connections_established": 1,
                                             "connections_dropped": 0
                                        },
                                        "transport": {
                                             "local_host": "1.1.1.1",
                                             "if_handle": "0x00000000",
                                             "foreign_port": 179,
                                             "foreign_host": "3.3.3.3",
                                             "local_port": 54707
                                        }
                                   },
                                   "last_ka_error_ka_not_sent": "00:00:00",
                                   "min_acceptable_hold_time": 3,
                                   "router_id": "3.3.3.3",
                                   "last_write_written": 0,
                                   "second_last_write_before_attempted": 0,
                                   "last_ka_start_before_second_last": "00:00:00",
                                   "remote_as": 100,
                                   "bgp_negotiated_keepalive_timers": {
                                        "keepalive_interval": 60,
                                        "hold_time": 180
                                   },
                                   "last_write_pulse_rcvd": "Jun 28 19:03:52.763 ",
                                   "written": 19,
                                   "message_stats_output_queue": 0,
                                   "second_attempted": 19,
                                   "message_stats_input_queue": 0,
                                   "last_ka_expiry_before_reset": "00:00:00",
                                   "last_write_pulse_rcvd_before_reset": "00:00:00",
                                   "second_written": 19,
                                   "last_write_before_reset": "00:00:00",
                                   "attempted": 19,
                                   "second_last_write": "00:01:23",
                                   "last_ka_error_before_reset": "00:00:00",
                                   "bgp_neighbor_counters": {
                                        "messages": {
                                             "sent": {
                                                  "keepalives": "40",
                                                  "opens": "1",
                                                  "updates": "4",
                                                  "notifications": "0"
                                             },
                                             "received": {
                                                  "keepalives": "41",
                                                  "opens": "1",
                                                  "updates": "6",
                                                  "notifications": "0"
                                             }
                                        }
                                   },
                                   "last_write_thread_event_before_reset": "00:00:00",
                                   "last_write_attempted": 0,
                                   "precedence": "internet",
                                   "configured_hold_time": 180,
                                   "keepalive": 60,
                                   "local_as_as_no": 100,
                                   "last_read": "00:00:06",
                                   "second_last_write_before_written": 0,
                                   "minimum_time_between_adv_runs": 0,
                                   "multiprotocol_capability": "received",
                                   "address_family": {
                                        "vpnv4 unicast": {
                                             "last_synced_ack_version": 0,
                                             "last_ack_version": 43,
                                             "cummulative_no_prefixes_denied": 0,
                                             "refresh_request_status": "No Refresh request being processed",
                                             "prefix_suppressed": 0,
                                             "route_refresh_request_received": 0,
                                             "maximum_prefixes_allowed": 2097152,
                                             "neighbor_version": 43,
                                             "maximum_prefix_restart": 0,
                                             "eor_status": "was not received during read-only mode",
                                             "best_paths": 0,
                                             "outstanding_version_objects_max": 1,
                                             "exact_no_prefixes_denied": 0,
                                             "prefix_withdrawn": 0,
                                             "outstanding_version_objects_current": 0,
                                             "route_refresh_request_sent": 0,
                                             "accepted_prefixes": 10,
                                             "maximum_prefix_threshold": "75%",
                                             "filter_group": "0.2",
                                             "maximum_prefix_warning_only": True,
                                             "update_group": "0.2",
                                             "additional_paths_operation": "None",
                                             "prefix_advertised": 5
                                        },
                                        "vpnv6 unicast": {
                                             "last_synced_ack_version": 0,
                                             "last_ack_version": 43,
                                             "cummulative_no_prefixes_denied": 0,
                                             "refresh_request_status": "No Refresh request being processed",
                                             "prefix_suppressed": 0,
                                             "route_refresh_request_received": 0,
                                             "maximum_prefixes_allowed": 1048576,
                                             "neighbor_version": 43,
                                             "maximum_prefix_restart": 0,
                                             "eor_status": "was not received during read-only mode",
                                             "best_paths": 0,
                                             "outstanding_version_objects_max": 1,
                                             "exact_no_prefixes_denied": 0,
                                             "prefix_withdrawn": 0,
                                             "outstanding_version_objects_current": 0,
                                             "route_refresh_request_sent": 0,
                                             "accepted_prefixes": 10,
                                             "maximum_prefix_threshold": "75%",
                                             "filter_group": "0.2",
                                             "maximum_prefix_warning_only": True,
                                             "update_group": "0.2",
                                             "additional_paths_operation": "None",
                                             "prefix_advertised": 5
                                        }
                                   },
                                   "non_stop_routing": "enabled",
                                   "last_write": "00:00:23",
                                   "nsr_state": "None",
                                   "tcp_initial_sync_done": "---",
                                   "last_full_not_set_pulse_count": 88,
                                   "tcp_initial_sync": "---",
                                   "outbound_message": "3",
                                   "bgp_negotiated_capabilities": {
                                        "four_octets_asn": "advertised received",
                                        "vpnv6_unicast": "advertised received",
                                        "route_refresh": "advertised received",
                                        "vpnv4_unicast": "advertised received"
                                   },
                                   "last_write_thread_event_second_last": "00:00:00",
                                   "second_last_write_before_reset": "00:00:00",
                                   "last_ka_start_before_reset": "00:00:00",
                                   "last_read_before_reset": "00:00:00"
                                }
                            }
                        }
                    }
                }
            }
        }

    golden_output = {'execute.return_value': '''
           
        BGP instance 0: 'default'
        =========================

        BGP neighbor is 2.2.2.2
         Remote AS 100, local AS 100, internal link
         Remote router ID 2.2.2.2
          BGP state = Established, up for 00:42:33
          NSR State: None
          Last read 00:00:32, Last read before reset 00:00:00
          Hold time is 180, keepalive interval is 60 seconds
          Configured hold time: 180, keepalive: 60, min acceptable hold time: 3
          Last write 00:00:23, attempted 19, written 19
          Second last write 00:01:23, attempted 19, written 19
          Last write before reset 00:00:00, attempted 0, written 0
          Second last write before reset 00:00:00, attempted 0, written 0
          Last write pulse rcvd  Jun 28 19:03:35.294 last full not set pulse count 93
          Last write pulse rcvd before reset 00:00:00
          Socket not armed for io, armed for read, armed for write
          Last write thread event before reset 00:00:00, second last 00:00:00
          Last KA expiry before reset 00:00:00, second last 00:00:00
          Last KA error before reset 00:00:00, KA not sent 00:00:00
          Last KA start before reset 00:00:00, second last 00:00:00
          Precedence: internet
          Non-stop routing is enabled
          Entered Neighbor NSR TCP mode:
            TCP Initial Sync :              ---                
            TCP Initial Sync Phase Two :    ---                
            TCP Initial Sync Done :         ---                
          Multi-protocol capability received
          Neighbor capabilities:            Adv         Rcvd
            Route refresh:                  Yes         Yes
            4-byte AS:                      Yes         Yes
            Address family VPNv4 Unicast:   Yes         Yes
            Address family VPNv6 Unicast:   Yes         Yes
          Message stats:
            InQ depth: 0, OutQ depth: 0
                            Last_Sent               Sent  Last_Rcvd               Rcvd
            Open:           Jun 28 18:21:24.198        1  Jun 28 18:21:24.208        1
            Notification:   ---                        0  ---                        0
            Update:         Jun 28 18:29:34.624        4  Jun 28 18:21:26.218        6
            Keepalive:      Jun 28 19:03:35.164       43  Jun 28 19:03:26.445       44
            Route_Refresh:  ---                        0  ---                        0
            Total:                                    48                            51
          Minimum time between advertisement runs is 0 secs
          Inbound message logging enabled, 3 messages buffered
          Outbound message logging enabled, 3 messages buffered

         For Address Family: VPNv4 Unicast
          BGP neighbor version 43
          Update group: 0.2 Filter-group: 0.2  No Refresh request being processed
            Graceful Restart capability received
              Remote Restart time is 120 seconds
              Neighbor did not preserve the forwarding state during latest restart
          Route refresh request: received 0, sent 0
          10 accepted prefixes, 10 are bestpaths
          Exact no. of prefixes denied : 0.
          Cumulative no. of prefixes denied: 0. 
          Prefix advertised 5, suppressed 0, withdrawn 0
          Maximum prefixes allowed 2097152
          Threshold for warning message 75%, restart interval 0 min
          AIGP is enabled
          An EoR was received during read-only mode
          Last ack version 43, Last synced ack version 0
          Outstanding version objects: current 0, max 1
          Additional-paths operation: None
          Send Multicast Attributes

         For Address Family: VPNv6 Unicast
          BGP neighbor version 43
          Update group: 0.2 Filter-group: 0.2  No Refresh request being processed
            Graceful Restart capability received
              Remote Restart time is 120 seconds
              Neighbor did not preserve the forwarding state during latest restart
          Route refresh request: received 0, sent 0
          10 accepted prefixes, 10 are bestpaths
          Exact no. of prefixes denied : 0.
          Cumulative no. of prefixes denied: 0. 
          Prefix advertised 5, suppressed 0, withdrawn 0
          Maximum prefixes allowed 1048576
          Threshold for warning message 75%, restart interval 0 min
          AIGP is enabled
          An EoR was received during read-only mode
          Last ack version 43, Last synced ack version 0
          Outstanding version objects: current 0, max 1
          Additional-paths operation: None
          Send Multicast Attributes

          Connections established 1; dropped 0
          Local host: 1.1.1.1, Local port: 46663, IF Handle: 0x00000000
          Foreign host: 2.2.2.2, Foreign port: 179
          Last reset 00:00:00

        BGP neighbor is 3.3.3.3
         Remote AS 100, local AS 100, internal link
         Remote router ID 3.3.3.3
          BGP state = Established, up for 00:39:07
          NSR State: None
          Last read 00:00:06, Last read before reset 00:00:00
          Hold time is 180, keepalive interval is 60 seconds
          Configured hold time: 180, keepalive: 60, min acceptable hold time: 3
          Last write 00:00:23, attempted 19, written 19
          Second last write 00:01:23, attempted 19, written 19
          Last write before reset 00:00:00, attempted 0, written 0
          Second last write before reset 00:00:00, attempted 0, written 0
          Last write pulse rcvd  Jun 28 19:03:52.763 last full not set pulse count 88
          Last write pulse rcvd before reset 00:00:00
          Socket not armed for io, armed for read, armed for write
          Last write thread event before reset 00:00:00, second last 00:00:00
          Last KA expiry before reset 00:00:00, second last 00:00:00
          Last KA error before reset 00:00:00, KA not sent 00:00:00
          Last KA start before reset 00:00:00, second last 00:00:00
          Precedence: internet
          Non-stop routing is enabled
          Entered Neighbor NSR TCP mode:
            TCP Initial Sync :              ---                
            TCP Initial Sync Phase Two :    ---                
            TCP Initial Sync Done :         ---                
          Multi-protocol capability received
          Neighbor capabilities:            Adv         Rcvd
            Route refresh:                  Yes         Yes
            4-byte AS:                      Yes         Yes
            Address family VPNv4 Unicast:   Yes         Yes
            Address family VPNv6 Unicast:   Yes         Yes
          Message stats:
            InQ depth: 0, OutQ depth: 0
                            Last_Sent               Sent  Last_Rcvd               Rcvd
            Open:           Jun 28 18:24:51.194        1  Jun 28 18:24:51.204        1
            Notification:   ---                        0  ---                        0
            Update:         Jun 28 18:29:34.624        4  Jun 28 18:24:52.664        6
            Keepalive:      Jun 28 19:03:35.164       40  Jun 28 19:03:52.763       41
            Route_Refresh:  ---                        0  ---                        0
            Total:                                    45                            48
          Minimum time between advertisement runs is 0 secs
          Inbound message logging enabled, 3 messages buffered
          Outbound message logging enabled, 3 messages buffered

         For Address Family: VPNv4 Unicast
          BGP neighbor version 43
          Update group: 0.2 Filter-group: 0.2  No Refresh request being processed
            Graceful Restart capability received
              Remote Restart time is 120 seconds
              Neighbor did not preserve the forwarding state during latest restart
          Route refresh request: received 0, sent 0
          10 accepted prefixes, 0 are bestpaths
          Exact no. of prefixes denied : 0.
          Cumulative no. of prefixes denied: 0. 
          Prefix advertised 5, suppressed 0, withdrawn 0
          Maximum prefixes allowed 2097152
          Threshold for warning message 75%, restart interval 0 min
          AIGP is enabled
          An EoR was not received during read-only mode
          Last ack version 43, Last synced ack version 0
          Outstanding version objects: current 0, max 1
          Additional-paths operation: None
          Send Multicast Attributes

         For Address Family: VPNv6 Unicast
          BGP neighbor version 43
          Update group: 0.2 Filter-group: 0.2  No Refresh request being processed
            Graceful Restart capability received
              Remote Restart time is 120 seconds
              Neighbor did not preserve the forwarding state during latest restart
          Route refresh request: received 0, sent 0
          10 accepted prefixes, 0 are bestpaths
          Exact no. of prefixes denied : 0.
          Cumulative no. of prefixes denied: 0. 
          Prefix advertised 5, suppressed 0, withdrawn 0
          Maximum prefixes allowed 1048576
          Threshold for warning message 75%, restart interval 0 min
          AIGP is enabled
          An EoR was not received during read-only mode
          Last ack version 43, Last synced ack version 0
          Outstanding version objects: current 0, max 1
          Additional-paths operation: None
          Send Multicast Attributes

          Connections established 1; dropped 0
          Local host: 1.1.1.1, Local port: 54707, IF Handle: 0x00000000
          Foreign host: 3.3.3.3, Foreign port: 179
          Last reset 00:00:00
            '''}


    def test_empty(self):
        self.device1 = Mock(**self.empty_output)
        bgp_instance_neighbors_detail_obj = ShowBgpInstanceNeighborsDetail(device=self.device1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = bgp_instance_neighbors_detail_obj.parse(vrf_type='all')

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        bgp_instance_neighbors_detail_obj = ShowBgpInstanceNeighborsDetail(device=self.device)
        parsed_output = bgp_instance_neighbors_detail_obj.parse(vrf_type='all')
        self.maxDiff = None
        self.assertEqual(parsed_output,self.golden_parsed_output)


# ================================================================================
# Unit test for 'show bgp instance all vrf all neighbors <WORD> advertised-routes'
# ================================================================================

class test_show_bgp_instance_all_vrf_all_neighbors_advertised_routes(unittest.TestCase):
        
    device = Device(name='aDevice')
    device0 = Device(name='bDevice')
    empty_output = {'execute.return_value': ''}
    golden_parsed_output =  {
        "instance": {
            "default": {
                "vrf": {
                    "VRF2": {
                        "address_family": {
                            "ipv4 unicast RD 200:2": {
                                "advertised": {
                                    "prefix": {
                                        "46.2.2.0/24": {
                                            "index": {
                                                1: {
                                                    "froms": "2.2.2.2",
                                                    "next_hop": "20.1.5.1",
                                                    "asn": 100,
                                                    "origin_code": "e",
                                                    "path": "400 33299 51178 47751 {27016}"}}},
                                        "46.1.1.0/24": {
                                            "index": {
                                                1: {
                                                    "froms": "2.2.2.2",
                                                    "next_hop": "20.1.5.1",
                                                    "asn": 100,
                                                    "origin_code": "e",
                                                    "path": "300 33299 51178 47751 {27016}"}}},
                                        "46.1.5.0/24": {
                                            "index": {
                                                1: {
                                                    "froms": "2.2.2.2",
                                                    "next_hop": "20.1.5.1",
                                                    "asn": 100,
                                                    "origin_code": "e",
                                                    "path": "300 33299 51178 47751 {27016}"}}},
                                        "46.1.4.0/24": {
                                            "index": {
                                                1: {
                                                    "froms": "2.2.2.2",
                                                    "next_hop": "20.1.5.1",
                                                    "asn": 100,
                                                    "origin_code": "e",
                                                    "path": "300 33299 51178 47751 {27016}"
                                        }}}}},
                                "processed_prefixes": "4",
                                "route_distinguisher": "200:2",
                                "processed_paths": "4",
                                "default_vrf": "VRF2"}}},
                    "VRF1": {}
                    }
                }
            }
        }



    golden_output = {'execute.return_value': '''
    
        Neighbor not found

        BGP instance 0: 'default'
        =========================

        VRF: VRF1
        ---------

        VRF: VRF2
        ---------
        Network            Next Hop        From            AS Path
        Route Distinguisher: 200:2 (default for vrf VRF2)
        46.1.1.0/24        20.1.5.1        2.2.2.2         100 300 33299 51178 47751 {27016}e
        46.1.4.0/24        20.1.5.1        2.2.2.2         100 300 33299 51178 47751 {27016}e
        46.1.5.0/24        20.1.5.1        2.2.2.2         100 300 33299 51178 47751 {27016}e
        46.2.2.0/24        20.1.5.1        2.2.2.2         100 400 33299 51178 47751 {27016}e

        Processed 4 prefixes, 4 paths
        '''}

    def test_empty(self):
        self.device1 = Mock(**self.empty_output)
        bgp_instance_all_vrf_all_neighbors_advertised_routes_obj = ShowBgpInstanceNeighborsAdvertisedRoutes(device=self.device1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = bgp_instance_all_vrf_all_neighbors_advertised_routes_obj.parse(neighbor='20.1.5.5', vrf='vrf')

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        bgp_instance_all_vrf_all_neighbors_advertised_routes_obj = ShowBgpInstanceNeighborsAdvertisedRoutes(device=self.device)
        parsed_output = bgp_instance_all_vrf_all_neighbors_advertised_routes_obj.parse(neighbor='20.1.5.5', vrf='vrf')
        self.maxDiff = None
        self.assertEqual(parsed_output,self.golden_parsed_output)


# ================================================================================
# Unit test for 'show bgp instance all all all neighbors <WORD> advertised-routes'
# ================================================================================

class test_show_bgp_instance_all_all_all_neighbors_advertised_routes(unittest.TestCase):
        
    device = Device(name='aDevice')
    device0 = Device(name='bDevice')
    empty_output = {'execute.return_value': ''}
    golden_parsed_output =  {
        "instance": {
            "default": {
                "vrf": {
                    "default": {
                        "address_family": {
                            "vpnv4 unicast RD 200:2": {
                                "processed_paths": "2",
                                "processed_prefixes": "2",
                                "advertised": {
                                    "prefix": {
                                        "15.1.2.0/24": {
                                            "index": {
                                                1: {
                                                    "froms": "20.1.5.5",
                                                    "path": "33299 51178 47751 {27016}",
                                                    "asn": 200,
                                                    "next_hop": "1.1.1.1",
                                                    "origin_code": "e"
                                                }
                                            }
                                        },
                                        "15.1.1.0/24": {
                                            "index": {
                                                1: {
                                                    "froms": "20.1.5.5",
                                                    "path": "33299 51178 47751 {27016}",
                                                    "asn": 200,
                                                    "next_hop": "1.1.1.1",
                                                    "origin_code": "e"
                                                }
                                            }
                                        }
                                    }
                                },
                                "default_vrf": "default",
                                "route_distinguisher": "200:2"
                            },
                            "vpnv6 unicast RD 200:2": {
                                "processed_paths": "2",
                                "processed_prefixes": "2",
                                "advertised": {
                                    "prefix": {
                                        "615:11:11::/64": {
                                            "index": {
                                                1: {
                                                    "froms": "2001:db8:20:1:5::5",
                                                    "path": "33299 51178 47751 {27017}",
                                                    "asn": 200,
                                                    "next_hop": "1.1.1.1",
                                                    "origin_code": "e"
                                                }
                                            }
                                        },
                                        "615:11:11:1::/64": {
                                            "index": {
                                                1: {
                                                    "froms": "2001:db8:20:1:5::5",
                                                    "path": "33299 51178 47751 {27016}",
                                                    "asn": 200,
                                                    "next_hop": "1.1.1.1",
                                                    "origin_code": "e"
                                                }
                                            }
                                        }
                                    }
                                },
                                "default_vrf": "default",
                                "route_distinguisher": "200:2"
                            }
                        }
                    }
                }
            }
        }
    }

    golden_output = {'execute.return_value': '''

        BGP instance 0: 'default'
        =========================

        Address Family: VPNv4 Unicast
        -----------------------------

        Network            Next Hop        From            AS  Path
        Route Distinguisher: 200:2
        15.1.1.0/24        1.1.1.1         20.1.5.5        200 33299 51178 47751 {27016}e
        15.1.2.0/24        1.1.1.1         20.1.5.5        200 33299 51178 47751 {27016}e

        Processed 2 prefixes, 2 paths

        Address Family: VPNv6 Unicast
        -----------------------------

        Network            Next Hop        From            AS  Path
        Route Distinguisher: 200:2
        615:11:11::/64     1.1.1.1         2001:db8:20:1:5::5
                                                           200 33299 51178 47751 {27017}e
        615:11:11:1::/64   1.1.1.1         2001:db8:20:1:5::5
                                                           200 33299 51178 47751 {27016}e

        Processed 2 prefixes, 2 paths
        '''}
    
    def test_empty(self):
        self.device1 = Mock(**self.empty_output)
        obj = ShowBgpInstanceNeighborsAdvertisedRoutes(device=self.device1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse(neighbor='3.3.3.3', vrf='all')

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = ShowBgpInstanceNeighborsAdvertisedRoutes(device=self.device)
        parsed_output = obj.parse(neighbor='3.3.3.3', vrf='all')
        self.maxDiff = None
        self.assertEqual(parsed_output,self.golden_parsed_output)


# ==============================================================================
# Unit test for 'show bgp instance all vrf all neighbors <WORD> received-routes'
# ==============================================================================

class test_show_bgp_instance_all_vrf_all_neighbors_received_routes(unittest.TestCase):
    device = Device(name='aDevice')
    device0 = Device(name='bDevice')
    empty_output = {'execute.return_value': ''}
    golden_parsed_output =   {
        "instance": {
           "default": {
                "vrf": {
                    "vrf2": {
                        "address_family": {
                            "ipv4 unicast RD 200:2": {
                                "non_stop_routing": True,
                                "vrf_id": "0x60000002",
                                "processed_prefixes": 2,
                                "table_state": "Active",
                                "state": "Active",
                                "processed_paths": 2,
                                "table_id": "0xe0000011",
                                "nsr_initial_initsync_version": "11 (Reached)",
                                "tbl_ver": 63,
                                "received": {
                                    "prefix": {
                                        "15.1.1.0/24": {
                                            "index": {
                                                1: {
                                                    "next_hop": "20.1.5.5",
                                                    "origin_codes": "e",
                                                    "metric": "2219",
                                                    "path": "200 33299 51178 47751 {27016}",
                                                    "weight": "0",
                                                    "status_codes": "*"
                                                }
                                            }
                                        },
                                        "15.1.2.0/24": {
                                            "index": {
                                                1: {
                                                    "next_hop": "20.1.5.5",
                                                    "origin_codes": "e",
                                                    "metric": "2219",
                                                    "path": "200 33299 51178 47751 {27016}",
                                                    "weight": "0",
                                                    "status_codes": "*"
                                                }}}}},
                               "local_as": 100,
                               "route_identifier": "11.11.11.11",
                               "rd_version": 63,
                               "nsr_issu_sync_group_versions": "0/0"
                            }}}}}}}



    golden_output = {'execute.return_value': '''
        Wed Jun 28 19:20:50.783 UTC
        % Neighbor not found

        BGP instance 0: 'default'
        =========================

        VRF: VRF1
        ---------

        VRF: VRF2
        ---------
        BGP VRF VRF2, state: Active
        BGP Route Distinguisher: 200:2
        VRF ID: 0x60000002
        BGP router identifier 11.11.11.11, local AS number 100
        Non-stop routing is enabled
        BGP table state: Active
        Table ID: 0xe0000011   RD version: 63
        BGP main routing table version 63
        BGP NSR Initial initsync version 11 (Reached)
        BGP NSR/ISSU Sync-Group versions 0/0

        Status codes: s suppressed, d damped, h history, * valid, > best
                      i - internal, r RIB-failure, S stale, N Nexthop-discard
        Origin codes: i - IGP, e - EGP, ? - incomplete
           Network            Next Hop            Metric LocPrf Weight Path
        Route Distinguisher: 200:2 (default for vrf VRF2)
        *  15.1.1.0/24        20.1.5.5              2219             0 200 33299 51178 47751 {27016} e
        *  15.1.2.0/24        20.1.5.5              2219             0 200 33299 51178 47751 {27016} e

        Processed 2 prefixes, 2 paths
        '''}

    def test_empty(self):
        self.device1 = Mock(**self.empty_output)
        obj = ShowBgpInstanceNeighborsReceivedRoutes(device=self.device1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse(vrf='vrf',neighbor='20.1.5.5')

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = ShowBgpInstanceNeighborsReceivedRoutes(device=self.device)
        parsed_output = obj.parse(vrf='vrf',neighbor='20.1.5.5')
        self.maxDiff = None
        self.assertEqual(parsed_output,self.golden_parsed_output)


# ==============================================================================
# Unit test for 'show bgp instance all all all neighbors <WORD> received-routes'
# ==============================================================================

class test_show_bgp_instance_all_all_all_neighbors_received_routes(unittest.TestCase):
    device = Device(name='aDevice')
    device0 = Device(name='bDevice')
    empty_output = {'execute.return_value': ''}
    golden_parsed_output =  {
        "instance": {
            "default": {
                "vrf": {
                    "default": {
                        "address_family": {
                            "vpnv4 unicast RD 300:1": {
                                "nsr_initial_initsync_version": "11 (Reached)",
                                "route_identifier": "1.1.1.1",
                                "non_stop_routing": True,
                                "nsr_issu_sync_group_versions": "0/0",
                                "received": {
                                    "prefix": {
                                        "46.1.1.0/24": {
                                            "index": {
                                                1: {
                                                    "metric": "2219",
                                                    "locprf": "100",
                                                    "path": "300 33299 51178 47751 {27016}",
                                                    "weight": "0",
                                                    "origin_codes": "e",
                                                    "status_codes": "*i",
                                                    "next_hop": "4.4.4.4"
                                                }}}}},
                                "generic_scan_interval": 60,
                                "local_as": 100,
                                "rd_version": 0,
                                "tbl_ver": 43,
                                "table_id": "0x0",
                                "table_state": "Active",
                                "scan_interval": 60
                            },
                            "vpnv6 unicast RD 300:1": {
                                "nsr_initial_initsync_version": "11 (Reached)",
                                "route_identifier": "1.1.1.1",
                                "non_stop_routing": True,
                                "nsr_issu_sync_group_versions": "0/0",
                                "received": {
                                    "prefix": {
                                        "646:11:11::/64": {
                                            "index": {
                                                1: {
                                                    "metric": "2219",
                                                    "locprf": "100",
                                                    "path": "300 33299 51178 47751 {27016}",
                                                    "weight": "0",
                                                    "origin_codes": "e",
                                                    "status_codes": "*i",
                                                    "next_hop": "4.4.4.4"
                                                   }
                                              }
                                        },
                                        "646:11:11:4::/64": {
                                            "index": {
                                                1: {
                                                    "metric": "2219",
                                                    "locprf": "100",
                                                    "path": "300 33299 51178 47751 {27016}",
                                                    "weight": "0",
                                                    "origin_codes": "e",
                                                    "status_codes": "*i",
                                                    "next_hop": "4.4.4.4"
                                                   }}}}},
                                "generic_scan_interval": 60,
                                "local_as": 100,
                                "rd_version": 0,
                                "tbl_ver": 43,
                                "table_id": "0x0",
                                "table_state": "Active",
                                "scan_interval": 60
                            },
                            "vpnv6 unicast RD 400:1": {
                                "nsr_initial_initsync_version": "11 (Reached)",
                                "route_identifier": "1.1.1.1",
                                "non_stop_routing": True,
                                "nsr_issu_sync_group_versions": "0/0",
                                "received": {
                                    "prefix": {
                                        "646:22:22:1::/64": {
                                            "index": {
                                                1: {
                                                    "metric": "2219",
                                                    "locprf": "100",
                                                    "path": "400 33299 51178 47751 {27016}",
                                                    "weight": "0",
                                                    "origin_codes": "e",
                                                    "status_codes": "*i",
                                                    "next_hop": "4.4.4.4"}}},
                                        "646:22:22::/64": {
                                            "index": {
                                                1: {
                                                    "metric": "2219",
                                                    "locprf": "100",
                                                    "path": "400 33299 51178 47751 {27016}",
                                                    "weight": "0",
                                                    "origin_codes": "e",
                                                    "status_codes": "*i",
                                                    "next_hop": "4.4.4.4"
                                                   }}}}},
                                "generic_scan_interval": 60,
                                "processed_paths": 10,
                                "rd_version": 0,
                                "tbl_ver": 43,
                                "table_id": "0x0",
                                "table_state": "Active",
                                "processed_prefixes": 10,
                                "local_as": 100,
                                "scan_interval": 60
                            },
                            "vpnv4 unicast RD 400:1": {
                                "nsr_initial_initsync_version": "11 (Reached)",
                                "route_identifier": "1.1.1.1",
                                "non_stop_routing": True,
                                "nsr_issu_sync_group_versions": "0/0",
                                "received": {
                                    "prefix": {
                                        "46.2.2.0/24": {
                                            "index": {
                                                1: {
                                                    "metric": "2219",
                                                    "locprf": "100",
                                                    "path": "400 33299 51178 47751 {27016}",
                                                    "weight": "0",
                                                    "origin_codes": "e",
                                                    "status_codes": "*i",
                                                    "next_hop": "4.4.4.4"}}}}},
                                "generic_scan_interval": 60,
                                "processed_paths": 10,
                                "rd_version": 0,
                                "tbl_ver": 43,
                                "table_id": "0x0",
                                "table_state": "Active",
                                "processed_prefixes": 10,
                                "local_as": 100,
                                "scan_interval": 60}}}}}}}



    golden_output = {'execute.return_value': '''
        BGP instance 0: 'default'
        =========================

        Address Family: VPNv4 Unicast
        -----------------------------

        BGP router identifier 1.1.1.1, local AS number 100
        BGP generic scan interval 60 secs
        Non-stop routing is enabled
        BGP table state: Active
        Table ID: 0x0   RD version: 0
        BGP main routing table version 43
        BGP NSR Initial initsync version 11 (Reached)
        BGP NSR/ISSU Sync-Group versions 0/0
        BGP scan interval 60 secs

        Status codes: s suppressed, d damped, h history, * valid, > best
                      i - internal, r RIB-failure, S stale, N Nexthop-discard
        Origin codes: i - IGP, e - EGP, ? - incomplete
           Network            Next Hop            Metric LocPrf Weight Path
        Route Distinguisher: 300:1
        * i46.1.1.0/24        4.4.4.4               2219    100      0 300 33299 51178 47751 {27016} e
        Route Distinguisher: 400:1
        * i46.2.2.0/24        4.4.4.4               2219    100      0 400 33299 51178 47751 {27016} e

        Processed 10 prefixes, 10 paths

        Address Family: VPNv6 Unicast
        -----------------------------

        BGP router identifier 1.1.1.1, local AS number 100
        BGP generic scan interval 60 secs
        Non-stop routing is enabled
        BGP table state: Active
        Table ID: 0x0   RD version: 0
        BGP main routing table version 43
        BGP NSR Initial initsync version 11 (Reached)
        BGP NSR/ISSU Sync-Group versions 0/0
        BGP scan interval 60 secs

        Status codes: s suppressed, d damped, h history, * valid, > best
                      i - internal, r RIB-failure, S stale, N Nexthop-discard
        Origin codes: i - IGP, e - EGP, ? - incomplete
           Network            Next Hop            Metric LocPrf Weight Path
        Route Distinguisher: 300:1
        * i646:11:11::/64     4.4.4.4               2219    100      0 300 33299 51178 47751 {27016} e
        * i646:11:11:4::/64   4.4.4.4               2219    100      0 300 33299 51178 47751 {27016} e
        Route Distinguisher: 400:1
        * i646:22:22::/64     4.4.4.4               2219    100      0 400 33299 51178 47751 {27016} e
        * i646:22:22:1::/64   4.4.4.4               2219    100      0 400 33299 51178 47751 {27016} e

        Processed 10 prefixes, 10 paths
        '''}

    def test_empty(self):
        self.device1 = Mock(**self.empty_output)
        obj = ShowBgpInstanceNeighborsReceivedRoutes(device=self.device1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse(vrf='all',neighbor='20.1.5.5')

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = ShowBgpInstanceNeighborsReceivedRoutes(device=self.device)
        parsed_output = obj.parse(vrf='all',neighbor='20.1.5.5')
        self.maxDiff = None
        self.assertEqual(parsed_output,self.golden_parsed_output)


# =====================================================================
# Unit test for 'show bgp instance all vrf all neighbors <WORD> routes'
# =====================================================================

class test_show_bgp_instance_all_vrf_all_neighbors_routes(unittest.TestCase):
    
    device = Device(name='aDevice')
    device0 = Device(name='bDevice')
    empty_output = {'execute.return_value': ''}
    golden_parsed_output = {
        "instance": {
            "default": {
                "vrf": {
                    "vrf2": {
                        "address_family": {
                            "ipv4 unicast RD 200:2": {
                                "nsr_initial_initsync_version": "11 (Reached)",
                                "route_identifier": "11.11.11.11",
                                "non_stop_routing": True,
                                "processed_prefixes": 2,
                                "vrf_id": "0x60000002",
                                "table_id": "0xe0000011",
                                "local_as": 100,
                                "tbl_ver": 63,
                                "processed_paths": 2,
                                "nsr_issu_sync_group_versions": "0/0",
                                "table_state": "Active",
                                "routes": {
                                    "prefix": {
                                        "15.1.1.0/24": {
                                            "index": {
                                                1: {
                                                    "path": "200 33299 51178 47751 {27016}",
                                                    "next_hop": "20.1.5.5",
                                                    "status_codes": "*>",
                                                    "weight": "0",
                                                    "metric": "2219",
                                                    "origin_codes": "e"
                                                }
                                            }
                                        },
                                        "15.1.2.0/24": {
                                            "index": {
                                                1: {
                                                    "path": "200 33299 51178 47751 {27016}",
                                                    "next_hop": "20.1.5.5",
                                                    "status_codes": "*>",
                                                    "weight": "0",
                                                    "metric": "2219",
                                                    "origin_codes": "e"
                                                }
                                            }
                                        }
                                    }
                                },
                                "state": "Active",
                                "rd_version": 63}}}}}}}

    golden_output = {'execute.return_value': '''
    
     Neighbor not found

    BGP instance 0: 'default'
    =========================

    VRF: VRF1
    ---------

    VRF: VRF2
    ---------
    BGP VRF VRF2, state: Active
    BGP Route Distinguisher: 200:2
    VRF ID: 0x60000002
    BGP router identifier 11.11.11.11, local AS number 100
    Non-stop routing is enabled
    BGP table state: Active
    Table ID: 0xe0000011   RD version: 63
    BGP main routing table version 63
    BGP NSR Initial initsync version 11 (Reached)
    BGP NSR/ISSU Sync-Group versions 0/0

    Status codes: s suppressed, d damped, h history, * valid, > best
                  i - internal, r RIB-failure, S stale, N Nexthop-discard
    Origin codes: i - IGP, e - EGP, ? - incomplete
       Network            Next Hop            Metric LocPrf Weight Path
    Route Distinguisher: 200:2 (default for vrf VRF2)
    *> 15.1.1.0/24        20.1.5.5              2219             0 200 33299 51178 47751 {27016} e
    *> 15.1.2.0/24        20.1.5.5              2219             0 200 33299 51178 47751 {27016} e
    
    Processed 2 prefixes, 2 paths
        '''}

    def test_empty(self):
        self.device1 = Mock(**self.empty_output)
        obj = ShowBgpInstanceNeighborsRoutes(device=self.device1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse(neighbor='20.1.5.5', vrf='vrf')

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = ShowBgpInstanceNeighborsRoutes(device=self.device)
        parsed_output = obj.parse(neighbor='20.1.5.5', vrf='vrf')
        self.maxDiff = None
        self.assertEqual(parsed_output,self.golden_parsed_output)


# =====================================================================
# Unit test for 'show bgp instance all all all neighbors <WORD> routes'
# =====================================================================

class test_show_bgp_instance_all_all_all_neighbors_routes(unittest.TestCase):
    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}
    golden_parsed_output = {
       "instance": {
          "default": {
               "vrf": {
                    "default": {
                         "address_family": {
                              "vpnv4 unicast RD 400:1": {
                                   "rd_version": 0,
                                   "route_identifier": "1.1.1.1",
                                   "routes": {
                                        "prefix": {
                                             "46.2.2.0/24": {
                                                  "index": {
                                                       1: {
                                                            "path": "400 33299 51178 47751 {27016}",
                                                            "status_codes": "*i",
                                                            "locprf": "100",
                                                            "weight": "0",
                                                            "next_hop": "4.4.4.4",
                                                            "metric": "2219",
                                                            "origin_codes": "e"
                                                       }
                                                  }
                                             }
                                        }
                                   },
                                   "non_stop_routing": True,
                                   "scan_interval": 60,
                                   "tbl_ver": 43,
                                   "nsr_issu_sync_group_versions": "0/0",
                                   "local_as": 100,
                                   "nsr_initial_initsync_version": "11 (Reached)",
                                   "table_id": "0x0",
                                   "table_state": "Active",
                                   "processed_prefixes": 2,
                                   "generic_scan_interval": 60,
                                   "processed_paths": 2
                              },
                              "vpnv6 unicast RD 400:1": {
                                   "rd_version": 0,
                                   "route_identifier": "1.1.1.1",
                                   "routes": {
                                        "prefix": {
                                             "646:22:22::/64": {
                                                  "index": {
                                                       1: {
                                                            "path": "400 33299 51178 47751 {27016}",
                                                            "status_codes": "*i",
                                                            "locprf": "100",
                                                            "weight": "0",
                                                            "next_hop": "4.4.4.4",
                                                            "metric": "2219",
                                                            "origin_codes": "e"
                                                       }
                                                  }
                                             }
                                        }
                                   },
                                   "non_stop_routing": True,
                                   "scan_interval": 60,
                                   "tbl_ver": 43,
                                   "nsr_issu_sync_group_versions": "0/0",
                                   "local_as": 100,
                                   "nsr_initial_initsync_version": "11 (Reached)",
                                   "table_id": "0x0",
                                   "table_state": "Active",
                                   "processed_prefixes": 3,
                                   "generic_scan_interval": 60,
                                   "processed_paths": 3
                              },
                              "vpnv4 unicast RD 300:1": {
                                   "rd_version": 0,
                                   "route_identifier": "1.1.1.1",
                                   "routes": {
                                        "prefix": {
                                             "46.1.1.0/24": {
                                                  "index": {
                                                       1: {
                                                            "path": "300 33299 51178 47751 {27016}",
                                                            "status_codes": "*i",
                                                            "locprf": "100",
                                                            "weight": "0",
                                                            "next_hop": "4.4.4.4",
                                                            "metric": "2219",
                                                            "origin_codes": "e"
                                                       }
                                                  }
                                             }
                                        }
                                   },
                                   "non_stop_routing": True,
                                   "scan_interval": 60,
                                   "tbl_ver": 43,
                                   "nsr_issu_sync_group_versions": "0/0",
                                   "local_as": 100,
                                   "nsr_initial_initsync_version": "11 (Reached)",
                                   "table_id": "0x0",
                                   "table_state": "Active",
                                   "generic_scan_interval": 60
                              },
                              "vpnv6 unicast RD 300:1": {
                                   "rd_version": 0,
                                   "route_identifier": "1.1.1.1",
                                   "routes": {
                                        "prefix": {
                                             "646:11:11::/64": {
                                                  "index": {
                                                       1: {
                                                            "path": "300 33299 51178 47751 {27016}",
                                                            "status_codes": "*i",
                                                            "locprf": "100",
                                                            "weight": "0",
                                                            "next_hop": "4.4.4.4",
                                                            "metric": "2219",
                                                            "origin_codes": "e"
                                                       }
                                                  }
                                             },
                                             "646:11:11:1::/64": {
                                                  "index": {
                                                       1: {
                                                            "path": "300 33299 51178 47751 {27016}",
                                                            "status_codes": "*i",
                                                            "locprf": "100",
                                                            "weight": "0",
                                                            "next_hop": "4.4.4.4",
                                                            "metric": "2219",
                                                            "origin_codes": "e"
                                                       }
                                                  }
                                             }
                                        }
                                   },
                                   "non_stop_routing": True,
                                   "scan_interval": 60,
                                   "tbl_ver": 43,
                                   "nsr_issu_sync_group_versions": "0/0",
                                   "local_as": 100,
                                   "nsr_initial_initsync_version": "11 (Reached)",
                                   "table_id": "0x0",
                                   "table_state": "Active",
                                   "generic_scan_interval": 60
                                }
                            }
                        }
                    }
                }
            }
        }

    golden_output = {'execute.return_value': '''
        BGP instance 0: 'default'
        =========================

        Address Family: VPNv4 Unicast
        -----------------------------

        BGP router identifier 1.1.1.1, local AS number 100
        BGP generic scan interval 60 secs
        Non-stop routing is enabled
        BGP table state: Active
        Table ID: 0x0   RD version: 0
        BGP main routing table version 43
        BGP NSR Initial initsync version 11 (Reached)
        BGP NSR/ISSU Sync-Group versions 0/0
        BGP scan interval 60 secs

        Status codes: s suppressed, d damped, h history, * valid, > best
                      i - internal, r RIB-failure, S stale, N Nexthop-discard
        Origin codes: i - IGP, e - EGP, ? - incomplete
           Network            Next Hop            Metric LocPrf Weight Path
        Route Distinguisher: 300:1
        * i46.1.1.0/24        4.4.4.4               2219    100      0 300 33299 51178 47751 {27016} e
        
        Route Distinguisher: 400:1
        * i46.2.2.0/24        4.4.4.4               2219    100      0 400 33299 51178 47751 {27016} e
        

        Processed 2 prefixes, 2 paths

        Address Family: VPNv6 Unicast
        -----------------------------

        BGP router identifier 1.1.1.1, local AS number 100
        BGP generic scan interval 60 secs
        Non-stop routing is enabled
        BGP table state: Active
        Table ID: 0x0   RD version: 0
        BGP main routing table version 43
        BGP NSR Initial initsync version 11 (Reached)
        BGP NSR/ISSU Sync-Group versions 0/0
        BGP scan interval 60 secs

        Status codes: s suppressed, d damped, h history, * valid, > best
                      i - internal, r RIB-failure, S stale, N Nexthop-discard
        Origin codes: i - IGP, e - EGP, ? - incomplete
           Network            Next Hop            Metric LocPrf Weight Path
        Route Distinguisher: 300:1
        * i646:11:11::/64     4.4.4.4               2219    100      0 300 33299 51178 47751 {27016} e
        * i646:11:11:1::/64   4.4.4.4               2219    100      0 300 33299 51178 47751 {27016} e
        Route Distinguisher: 400:1
        * i646:22:22::/64     4.4.4.4               2219    100      0 400 33299 51178 47751 {27016} e
        

        Processed 3 prefixes, 3 paths
        '''}

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowBgpInstanceNeighborsRoutes(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse(neighbor='3.3.3.3', vrf='all')

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = ShowBgpInstanceNeighborsRoutes(device=self.device)
        parsed_output = obj.parse(neighbor='3.3.3.3', vrf='all')
        self.maxDiff = None
        self.assertEqual(parsed_output,self.golden_parsed_output)


if __name__ == '__main__':
    unittest.main()
