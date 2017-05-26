
# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device

# Metaparser
from metaparser.util.exceptions import SchemaEmptyParserError

# nxos show_bgp
from parser.nxos.show_bgp import ShowBgpProcessVrfAll, ShowBgpPeerSession,\
                                 ShowBgpPeerPolicy, ShowBgpPeerTemplate,\
                                 ShowBgpVrfAllAll,\
                                 ShowBgpVrfAllNeighbors,\
                                 ShowBgpVrfAllAllNextHopDatabase,\
                                 ShowBgpVrfAllAllSummary,\
                                 ShowBgpVrfAllAllDampeningParameters


# =========================================
#  Unit test for 'show bgp process vrf all'
# =========================================

class test_show_bgp_process_vrf_all(unittest.TestCase):

    '''Unit test for show bgp process vrf all'''
    
    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output = {
        'bgp_as_path_entries': 0,
        'bgp_memory_state': 'ok',
        'bgp_paths_per_hwm_attr': 1,
        'bgp_pid': 29474,
        'bgp_protocol_state': 'running',
        'bgp_protocol_status': 'started',
        'bgp_protocol_status_reason': 'configuration',
        'bgp_tag': '100',
        'bytes_used': 368,
        'bytes_used_as_path_entries': 0,
        'entries_pending_delete': 0,
        'hwm_attr_entries': 5,
        'hwm_entries_pending_delete': 0,
        'num_attr_entries': 4,
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
                        'table_id': '10',
                        'table_state': 'up'},
                    'ipv6 unicast': {
                        'aggregate_label': '492288',
                        'export_rt_list': '100:100',
                        'import_rt_list': '100:100',
                        'label_mode': 'per-prefix',
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
                         'table_id': '1',
                         'table_state': 'up'},
                    'ipv6 label unicast': 
                        {'peers': 
                            {0: 
                                {'active_peers': 0,
                                 'aggregates': 0,
                                 'networks': 0,
                                 'paths': 0,
                                 'routes': 0}},
                         'table_id': '80000001',
                         'table_state': 'up'},
                    'ipv6 unicast': 
                        {'peers': 
                            {0: 
                                {'active_peers': 0,
                                'aggregates': 0,
                                'networks': 0,
                                'paths': 0,
                                'routes': 0}},
                         'table_id': '80000001',
                         'table_state': 'up'},
                    'vpnv4 unicast': 
                        {'peers': 
                            {1: 
                                {'active_peers': 1,
                                 'aggregates': 0,
                                 'networks': 0,
                                 'paths': 5,
                                 'routes': 5}},
                         'table_id': '1',
                         'table_state': 'up'},
                    'vpnv6 unicast': 
                        {'peers': 
                            {1: 
                                {'active_peers': 1,
                                'aggregates': 0,
                                 'networks': 0,
                                 'paths': 4,
                                 'routes': 4}},
                         'table_id': '80000001',
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

    golden_output = {'execute.return_value': '''
        BGP Process Information
        BGP Process ID                 : 29474
        BGP Protocol Started, reason:  : configuration
        BGP Protocol Tag               : 100
        BGP Protocol State             : Running
        BGP Memory State               : OK

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

    def test_show_version_golden1(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output)
        obj = ShowBgpProcessVrfAll(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output)

    def test_show_version_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowBgpProcessVrfAll(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

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
                                {'next_hop':
                                    {'0.0.0.0':
                                        {'localpref': '100',
                                        'metric': 'None',
                                        'origin_codes': 'i',
                                        'path_type': 'a',
                                        'status_codes': '*>',
                                        'weight': '32768'},
                                    '4.4.4.4':
                                        {'localpref': '100',
                                        'metric': '0',
                                        'origin_codes': 'e',
                                        'weight': '32768'},
                                    '6.6.6.6':
                                        {'localpref': '100',
                                        'metric': '0',
                                        'origin_codes': 'e',
                                        'weight': '32768'}}},
                                    '11.11.11.11/32':
                                        {'next_hop':
                                            {'0.0.0.0':
                                            {'localpref': '100',
                                            'metric': '0',
                                            'origin_codes': '?',
                                            'path_type': 'r',
                                            'status_codes': '*>',
                                            'weight': '32768'}}},
                            '123.0.0.0/8':
                                {'next_hop':
                                    {'0.0.0.0':
                                        {'localpref': '100',
                                        'metric': 'None',
                                        'origin_codes': 'i',
                                        'path_type': 'a',
                                        'status_codes': 'None',
                                        'weight': '32768'}}},
                            '33.33.33.33/32':
                                {'next_hop':
                                    {'3.3.3.3':
                                        {'localpref': '100',
                                        'metric': '0',
                                        'origin_codes': '?',
                                        'path_type': 'i',
                                        'status_codes': '*>',
                                        'weight': '0'}}},
                            '34.34.34.0/24':
                                {'next_hop':
                                    {'0.0.0.0':
                                        {'localpref': '100',
                                        'metric': 'None',
                                        'origin_codes': 'i',
                                        'path_type': 'l',
                                        'status_codes': 'None',
                                        'weight': '32768'}}}}},
                    'ipv6 unicast':
                        {'bgp_table_version': 28,
                        'local_router_id': '11.11.11.11',
                        'prefixes':
                            {'2000::/8':
                                {'next_hop':
                                    {'0::':
                                        {'localpref': '100',
                                        'metric': 'None',
                                        'origin_codes': 'i',
                                        'path_type': 'a',
                                        'status_codes': '*>',
                                        'weight': '32768'}}},
                            '2001:111:222::/64':
                                {'next_hop':
                                    {'0::':
                                        {'localpref': '100',
                                        'metric': 'None',
                                        'origin_codes': 'i',
                                        'path_type': 'l',
                                        'status_codes': 'None',
                                        'weight': '32768'}}},
                            '2001::11/128':
                                {'next_hop':
                                    {'0::':
                                        {'localpref': '100',
                                        'metric': '0',
                                        'origin_codes': '?',
                                        'path_type': 'r',
                                        'status_codes': '*>',
                                        'weight': '32768'}}},
                            '2001::33/128':
                                {'next_hop':
                                    {'::ffff:3.3.3.3':
                                        {'localpref': '100',
                                        'metric': '0',
                                        'origin_codes': '?',
                                        'path_type': 'i',
                                        'status_codes': '*>',
                                        'weight': '0'}}}},
                        'v6_aggregate_address_as_set': True,
                        'v6_aggregate_address_ipv6_address': '2000::/8',
                        'v6_aggregate_address_summary_only': True}}},
            'default':
                {'address_family':
                    {'vpnv4 unicast':
                        {'aggregate_address_as_set': True,
                        'aggregate_address_ipv4_address': '11.0.0.0',
                        'aggregate_address_ipv4_mask': '8',
                        'aggregate_address_summary_only': True,
                        'bgp_table_version': 48,
                        'default_vrf': 'VRF1',
                        'local_router_id': '1.1.1.1',
                        'prefixes':
                            {'11.0.0.0/8':
                                {'next_hop':
                                    {'0.0.0.0':
                                        {'localpref': '100',
                                        'metric': 'None',
                                        'origin_codes': 'i',
                                        'path_type': 'a',
                                        'status_codes': '*>',
                                        'weight': '32768'}}},
                            '11.11.11.11/32':
                                {'next_hop':
                                    {'0.0.0.0':
                                        {'localpref': '100',
                                        'metric': '0',
                                        'origin_codes': '?',
                                        'path_type': 'r',
                                        'status_codes': '*>',
                                        'weight': '32768'}}},
                            '123.0.0.0/8':
                                {'next_hop':
                                    {'0.0.0.0':
                                        {'localpref': '100',
                                        'metric': 'None',
                                        'origin_codes': 'i',
                                        'path_type': 'a',
                                        'status_codes': 'None',
                                        'weight': '32768'}}},
                            '33.33.33.33/32':
                                {'next_hop':
                                    {'3.3.3.3':
                                        {'localpref': '100',
                                        'metric': '0',
                                        'origin_codes': '?',
                                        'path_type': 'i',
                                        'status_codes': '*>',
                                        'weight': '0'}}},
                            '34.34.34.0/24':
                                {'next_hop':
                                    {'0.0.0.0':
                                        {'localpref': '100',
                                        'metric': 'None',
                                        'origin_codes': 'i',
                                        'path_type': 'l',
                                        'status_codes': 'None',
                                        'weight': '32768'}}}},
                        'route_distinguisher': '100:100'},
                    'vpnv6 unicast':
                        {'bgp_table_version': 41,
                        'default_vrf': 'VRF1',
                        'local_router_id': '1.1.1.1',
                        'prefixes':
                            {'2000::/8':
                                {'next_hop':
                                    {'0::':
                                        {'localpref': '100',
                                        'metric': 'None',
                                        'origin_codes': 'i',
                                        'path_type': 'a',
                                        'status_codes': '*>',
                                        'weight': '32768'}}},
                            '2001:111:222::/64':
                                {'next_hop':
                                    {'0::':
                                        {'localpref': '100',
                                        'metric': 'None',
                                        'origin_codes': 'i',
                                        'path_type': 'l',
                                        'status_codes': 'None',
                                        'weight': '32768'}}},
                            '2001::11/128':
                                {'next_hop':
                                    {'0::':
                                        {'localpref': '100',
                                        'metric': '0',
                                        'origin_codes': '?',
                                        'path_type': 'r',
                                        'status_codes': '*>',
                                        'weight': '32768'}}},
                            '2001::33/128':
                                {'next_hop':
                                    {'::ffff:3.3.3.3':
                                        {'localpref': '100',
                                        'metric': '0',
                                        'origin_codes': '?',
                                        'path_type': 'i',
                                        'status_codes': '*>',
                                        'weight': '0'}}}},
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
                                {'next_hop':
                                    {'1.2.1.1':
                                        {'localpref': '100',
                                        'metric': '',
                                        'origin_codes': 'i',
                                        'path_type': 'l',
                                        'status_codes': '*>',
                                        'weight': '32768'}}},
                            '[2]:[0]:[0]:[48]:[0000.1986.6d99]:[128]:[2004:ab4:123:20::44]/368':
                                {'next_hop':
                                    {'1.2.1.1':
                                        {'localpref': '100',
                                        'metric': '',
                                        'origin_codes': 'i',
                                        'path_type': 'l',
                                        'status_codes': '*>',
                                        'weight': '32768'}}},
                            '[2]:[0]:[0]:[48]:[0000.1986.6d99]:[32]:[100.100.20.44]/272':
                                {'next_hop':
                                    {'1.2.1.1':
                                        {'localpref': '100',
                                        'metric': '',
                                        'origin_codes': 'i',
                                        'path_type': 'l',
                                        'status_codes': '*>',
                                        'weight': '32768'}}}}}}}}}

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
                        'routing_table_version': 0,
                        'soo': 'SOO:100:100'}},
                'bgp_negotiated_keepalive_timers':
                    {'hold_time': '180',
                    'keepalive_interval': '60',
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
                'remote_as': '0',
                'retry_time': '0.000000',
                'router_id': '0.0.0.0',
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
                        'routing_table_version': 11,
                        'send_community': True},
                    'vpnv6 unicast':
                        {'bgp_table_version': 10,
                        'next_hop_self': False,
                        'path':
                            {'accepted_paths': 1,
                            'memory_usage': 48,
                            'total_entries': 2},
                        'routing_table_version': 10,
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
                    {'hold_time': '99',
                    'keepalive_interval': '33',
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
                'remote_as': '100',
                'retry_time': 'None',
                'router_id': '2.2.2.2',
                'session_state': 'Established',
                'shutdown': False,
                'suppress_four_byte_as_capability': True,
                'up_time': '02:20:02',
                'update_source': 'loopback0'},
            '2.2.2.25':
                {'bgp_negotiated_keepalive_timers':
                    {'hold_time': '45',
                    'keepalive_interval': '15',
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
                'remote_as': '0',
                'retry_time': '0.000000',
                'router_id': '0.0.0.0',
                'session_state': 'Idle',
                'shutdown': False,
                'up_time': '02:20:08'},
            '2.2.2.5':
                {'address_family':
                    {'ipv4 unicast':
                        {'as_override': True,
                        'as_override_count': 9,
                        'bgp_table_version': 2,
                        'inherited_peer_policy_names':
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
                        'routing_table_version': 0,
                        'send_community': True,
                        'soft_configuration': True}},
                'bfd_live_detection': True,
                'bgp_negotiated_keepalive_timers':
                    {'hold_time': '45',
                    'keepalive_interval': '15',
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
                'remote_as': '200',
                'retry_time': 'None',
                'router_id': '0.0.0.0',
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

    def test_show_bgp_vrf_VRF1_all_neighbors_golden(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output1)
        obj = ShowBgpVrfAllNeighbors(device=self.device)
        parsed_output = obj.parse(vrf='VRF1')
        self.assertEqual(parsed_output,self.golden_parsed_output1)

    def test_show_bgp_vrf_default_all_neighbors_golden(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output2)
        obj = ShowBgpVrfAllNeighbors(device=self.device, )
        parsed_output = obj.parse(vrf='default')
        self.assertEqual(parsed_output,self.golden_parsed_output2)

    def test_show_bgp_vrf_default_all_neighbors_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowBgpVrfAllNeighbors(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse(vrf='default')


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

    golden_parsed_output = {
        'vrf':
            {'VRF1':
                {'address_family':
                    {'ipv4 unicast':
                        {'as_path_entries': '[0/0]',
                        'attribute_entries': '[3/384]',
                        'bgp_table_version': 40,
                        'capable_peers': 0,
                        'clusterlist_entries': '[1/4]',
                        'community_entries': '[0/0]',
                        'config_peers': 1,
                        'dampened_paths': '0',
                        'dampening': 'configured',
                        'history_paths': '0',
                        'local_as': 100,
                        'neighbor':
                            {'2.2.2.10':
                                {'as': 0,
                                'inq': 0,
                                'msg_rcvd': 0,
                                'msg_sent': 0,
                                'outq': 0,
                                'state': 'Idle',
                                'tbl_ver': 0,
                                'up_down': '5w6d',
                                'v': 4}},
                        'path':
                            {'memory_usage': 620,
                            'total_entries': 5},
                        'prefixes':
                            {'memory_usage': 620,
                            'total_entries': 5},
                        'route_identifier': '4.4.4.4'},
                    'ipv6 unicast': {}}},
            'default':
                {'address_family':
                    {'ipv4 unicast':
                        {'as_path_entries': '[0/0]',
                        'attribute_entries': '[0/0]',
                        'bgp_table_version': 2,
                        'capable_peers': 0,
                        'clusterlist_entries': '[1/4]',
                        'community_entries': '[0/0]',
                        'config_peers': 1,
                        'dampened_paths': '0',
                        'dampening': 'configured',
                        'history_paths': '0',
                        'local_as': 100,
                        'path':
                            {'memory_usage': 0,
                            'total_entries': 0},
                        'prefixes':
                            {'memory_usage': 0,
                            'total_entries': 0},
                        'route_identifier': '1.1.1.1'},
                    'ipv6 label unicast': {},
                    'ipv6 unicast': {},
                    'vpnv4 unicast':
                        {'as_path_entries': '[0/0]',
                        'attribute_entries': '[1/128]',
                        'bgp_table_version': 53,
                        'capable_peers': 1,
                        'clusterlist_entries': '[1/4]',
                        'community_entries': '[0/0]',
                        'config_peers': 1,
                        'local_as': 100,
                        'neighbor':
                            {'2.2.2.2':
                                {'as': 100,
                               'inq': 0,
                               'msg_rcvd': 108554,
                               'msg_sent': 108566,
                               'outq': 0,
                               'state': '1',
                               'tbl_ver': 53,
                               'up_down': '5w6d',
                               'v': 4}},
                        'path':
                            {'memory_usage': 620,
                            'total_entries': 5},
                        'prefixes':
                            {'memory_usage': 620,
                            'total_entries': 5},
                        'route_identifier': '1.1.1.1'},
                    'vpnv6 unicast':
                        {'as_path_entries': '[0/0]',
                        'attribute_entries': '[1/128]',
                        'bgp_table_version': 45,
                        'capable_peers': 1,
                        'clusterlist_entries': '[1/4]',
                        'community_entries': '[0/0]',
                        'config_peers': 1,
                        'local_as': 100,
                        'neighbor':
                            {'2.2.2.2':
                                {'as': 100,
                               'inq': 0,
                               'msg_rcvd': 108554,
                               'msg_sent': 108566,
                               'outq': 0,
                               'state': '1',
                               'tbl_ver': 45,
                               'up_down': '5w6d',
                               'v': 4}},
                        'path':
                            {'memory_usage': 544,
                            'total_entries': 4},
                        'prefixes':
                            {'memory_usage': 544,
                            'total_entries': 4},
                        'route_identifier': '1.1.1.1'}}}}}

    golden_output = {'execute.return_value': '''
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

    def test_show_bgp_vrf_all_all_summary_golden(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output)
        obj = ShowBgpVrfAllAllSummary(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output)

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


if __name__ == '__main__':
    unittest.main()


# vim: ft=python et sw=4
