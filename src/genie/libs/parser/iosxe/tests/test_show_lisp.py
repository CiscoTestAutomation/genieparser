
# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError, SchemaMissingKeyError

# iosxe show_lisp
from genie.libs.parser.iosxe.show_lisp import ShowLispSession,\
                                              ShowLispPlatform,\
                                              ShowLispExtranet,\
                                              ShowLispDynamicEidDetail,\
                                              ShowLispService,\
                                              ShowLispServiceMapCache



# =================================
# Unit test for 'show lisp session'
# =================================
class test_show_lisp_session(unittest.TestCase):

    '''Unit test for "show lisp session"'''

    device = Device(name='aDevice')
    
    empty_output = {'execute.return_value': ''}

    golden_parsed_output1 = {
        'vrf':
            {'default': 
                {'sessions':
                    {'established': 3,
                    'peers':
                        {'2.2.2.2':
                            {'state': 'up',
                            'time': '00:51:38',
                            'total_in': 8,
                            'total_out': 13,
                            'users': 3},
                        '6.6.6.6':
                            {'state': 'up',
                            'time': '00:51:53',
                            'total_in': 3,
                            'total_out': 10,
                            'users': 1},
                        '8.8.8.8':
                            {'state': 'up',
                            'time': '00:52:15',
                            'total_in': 8,
                            'total_out': 13,
                            'users': 3}},
                    'total': 3},
                },
            },
        }

    golden_output1 = {'execute.return_value': '''
        204-MSMR#show lisp session
        Sessions for VRF default, total: 3, established: 3
        Peer                           State      Up/Down        In/Out    Users
        2.2.2.2                        Up         00:51:38        8/13     3
        6.6.6.6                        Up         00:51:53        3/10     1
        8.8.8.8                        Up         00:52:15        8/13     3
        '''}

    def test_show_lisp_session_full1(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output1)
        obj = ShowLispSession(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output1)

    def test_show_lisp_session_empty(self):
        self.maxDiff = None
        self.device = Mock(**self.empty_output)
        obj = ShowLispSession(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()


# ==================================
# Unit test for 'show lisp platform'
# ==================================
class test_show_lisp_platform(unittest.TestCase):

    '''Unit test for "show lisp platform"'''

    device = Device(name='aDevice')

    empty_output = {'execute.return_value': ''}

    golden_parsed_output1 = {
        'current_config_style': 'service and instance',
        'latest_supported_config_style': 'service and instance',
        'parallel_lisp_instance_limit': 2000,
        'rloc_forwarding_support':
            {'local':
                {'ipv4': 'ok',
                'ipv6': 'ok',
                'mac': 'unsupported'},
            'remote':
                {'ipv4': 'ok',
                'ipv6': 'ok',
                'mac':'unsupported'}}}

    golden_output1 = {'execute.return_value': '''
        202-XTR#show lisp platform
        Parallel LISP instance limit:      2000
        RLOC forwarding support:
        IPv4 RLOC, local:                 OK
        IPv6 RLOC, local:                 OK
        MAC RLOC, local:                  Unsupported
        IPv4 RLOC, remote:                OK
        IPv6 RLOC, remote:                OK
        MAC RLOC, remote:                 Unsupported
        Latest supported config style:     Service and instance
        Current config style:              Service and instance
        '''}

    def test_show_lisp_platform_full1(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output1)
        obj = ShowLispPlatform(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output1)

    def test_show_lisp_platform_empty(self):
        self.maxDiff = None
        self.device = Mock(**self.empty_output)
        obj = ShowLispPlatform(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()


# ===========================================================================
# Unit test for 'show lisp all extranet <extranet> instance-id <instance_id>'
# ===========================================================================
class test_show_lisp_extranet(unittest.TestCase):

    '''Unit test for "show lisp all extranet <extranet> instance-id <instance_id>"'''

    device = Device(name='aDevice')

    empty_output = {'execute.return_value': ''}

    golden_parsed_output1 = {
        'lisp_router_instances':
            {0:
                {'service':
                    {'ipv4':
                        {'map_server':
                            {'virtual_network_ids':
                                {'101':
                                    {'extranets':
                                        {'ext1':
                                            {'extranet': 'ext1',
                                            'home_instance_id': 103,
                                            'subscriber':
                                                {'192.168.0.0/24':
                                                    {'bidirectional': True,
                                                    'eid_record': '192.168.0.0/24'},
                                                '192.168.9.0/24':
                                                    {'bidirectional': True,
                                                    'eid_record': '192.168.9.0/24'}}}},
                                    'vni': '101'},
                                '102':
                                    {'extranets':
                                        {'ext1':
                                            {'extranet': 'ext1',
                                            'home_instance_id': 103,
                                            'subscriber':
                                                {'172.168.1.0/24':
                                                    {'bidirectional': True,
                                                    'eid_record': '172.168.1.0/24'}}}},
                                    'vni': '102'},
                                '103':
                                    {'extranets':
                                        {'ext1':
                                            {'extranet': 'ext1',
                                            'home_instance_id': 103,
                                            'provider':
                                                {'100.100.100.0/24':
                                                    {'bidirectional': True,
                                                    'eid_record': '100.100.100.0/24'},
                                                '200.200.200.0/24':
                                                    {'bidirectional': True,
                                                    'eid_record': '200.200.200.0/24'},
                                                '88.88.88.0/24':
                                                    {'bidirectional': True,
                                                    'eid_record': '88.88.88.0/24'}}}},
                                    'vni': '103'},
                            'total_extranet_entries': 6}}}}}}}

    golden_output1 = {'execute.return_value': '''
        204-MSMR#show lisp all extranet ext1 instance-id 103
        Output for router lisp 0

        -----------------------------------------------------
        LISP Extranet table
        Home Instance ID: 103
        Total entries: 6
        Provider/Subscriber  Inst ID    EID prefix
        Provider             103        88.88.88.0/24
        Provider             103        100.100.100.0/24
        Provider             103        200.200.200.0/24
        Subscriber           102        172.168.1.0/24
        Subscriber           101        192.168.0.0/24
        Subscriber           101        192.168.9.0/24
        '''}

    def test_show_lisp_extranet_full1(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output1)
        obj = ShowLispExtranet(device=self.device)
        parsed_output = obj.parse(extranet='ext1', instance_id='103')
        self.assertEqual(parsed_output, self.golden_parsed_output1)

    def test_show_lisp_extranet_empty(self):
        self.maxDiff = None
        self.device = Mock(**self.empty_output)
        obj = ShowLispExtranet(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse(extranet='ext1', instance_id='103')


# ==========================================================================
# Unit test for 'show lisp all instance-id <instance_id> dynamic-eid detail'
# ==========================================================================
class test_show_lisp_dynamic_eid_detail(unittest.TestCase):

    '''Unit test for "show lisp all instance-id <instance_id> dynamic-eid detail"'''

    device = Device(name='aDevice')

    empty_output = {'execute.return_value': ''}

    golden_parsed_output1 = {
        'lisp_router_instances': 
            {0: 
                {'service': 
                    {'ipv4': 
                        {'etr': 
                            {'local_eids': 
                                {101: 
                                    {'dynamic_eids': 
                                        {'192.168.0.0/24': 
                                            {'dynamic_eid_name': '192',
                                            'eid_address': 
                                                {'virtual_network_id': 'red'},
                                            'global_map_server': True,
                                            'id': '192.168.0.0/24',
                                            'last_dynamic_eid': 
                                                {'192.168.0.1': 
                                                    {'eids': 
                                                        {'192.168.0.1': 
                                                            {'discovered_by': 'packet reception',
                                                            'interface': 'GigabitEthernet5',
                                                            'last_activity': '00:00:23',
                                                            'uptime': '01:17:25'}},
                                                    'last_dynamic_eid_discovery_elaps_time': '01:17:25'}},
                                                    'num_of_roaming_dynamic_eid': 1,
                                                    'registering_more_specific': True,
                                                    'rlocs': 'RLOC',
                                                    'site_based_multicast_map_nofity_group': 'none configured'}}}}}}}}}}

    golden_output1 = {'execute.return_value': '''
        202-XTR#show lisp all instance-id 101 dynamic-eid detail
        Output for router lisp 0

        -----------------------------------------------------
        LISP Dynamic EID Information for VRF "red"

        Dynamic-EID name: 192
          Database-mapping EID-prefix: 192.168.0.0/24, locator-set RLOC
          Registering more-specific dynamic-EIDs
          Map-Server(s): none configured, use global Map-Server
          Site-based multicast Map-Notify group: none configured
          Number of roaming dynamic-EIDs discovered: 1
          Last dynamic-EID discovered: 192.168.0.1, 01:17:25 ago
            192.168.0.1, GigabitEthernet5, uptime: 01:17:25
              last activity: 00:00:23, discovered by: Packet Reception
        '''}

    golden_parsed_output2 = {
        'lisp_router_instances': 
            {0: 
                {'service': 
                    {'ipv4': 
                        {'etr': 
                            {'local_eids': 
                                {101: 
                                    {'dynamic_eids': 
                                        {'10.10.10.0/24': 
                                            {'dynamic_eid_name': 'CC-CA01-C-603',
                                            'eid_address': 
                                                {'virtual_network_id': 'blue'},
                                             'global_map_server': True,
                                             'id': '10.10.10.0/24',
                                             'last_dynamic_eid': 
                                                {'10.10.10.85': 
                                                    {'eids': 
                                                        {'10.10.10.83': 
                                                            {'discovered_by': 'packet reception',
                                                            'interface': 'Port-channel1.125',
                                                            'last_activity': '00:00:29',
                                                            'uptime': '03:28:27'},
                                                        '10.10.10.84': 
                                                            {'discovered_by': 'packet '
                                                            'reception',
                                                            'interface': 'Port-channel1.125',
                                                            'last_activity': '00:00:14',
                                                            'uptime': '00:14:10'},
                                                        '10.10.10.86': 
                                                            {'discovered_by': 'packet '
                                                            'reception',
                                                            'interface': 'Port-channel1.125',
                                                            'last_activity': '00:00:07',
                                                            'uptime': '03:40:08'}},
                                                    'last_dynamic_eid_discovery_elaps_time': '00:00:40'}},
                                            'num_of_roaming_dynamic_eid': 3,
                                            'registering_more_specific': True,
                                            'rlocs': 'CC-CA04-C',
                                            'site_based_multicast_map_nofity_group': 'none configured'}}}}}}}}}}

    golden_output2 = {'execute.return_value': '''
        202-XTR#show lisp all instance-id 101 dynamic-eid detail
        Output for router lisp 0

        -----------------------------------------------------
        LISP Dynamic EID Information for VRF "blue"

        Dynamic-EID name: CC-CA01-C-603
         Database-mapping EID-prefix: 10.10.10.0/24, locator-set CC-CA04-C
         Registering more-specific dynamic-EIDs
         Map-Server(s): none configured, use global Map-Server
         Site-based multicast Map-Notify group: none configured
         Number of roaming dynamic-EIDs discovered: 3
         Last dynamic-EID discovered: 10.10.10.85, 00:00:40 ago
           10.10.10.83, Port-channel1.125, uptime: 03:28:27
             last activity: 00:00:29, discovered by: Packet Reception
           10.10.10.84, Port-channel1.125, uptime: 00:14:10
             last activity: 00:00:14, discovered by: Packet Reception
           10.10.10.86, Port-channel1.125, uptime: 03:40:08
             last activity: 00:00:07, discovered by: Packet Reception
        '''}

    golden_parsed_output3 = {
        'lisp_router_instances': 
            {0: 
                {'service': 
                    {'ipv4': 
                        {'etr': 
                            {'local_eids': 
                                {101: 
                                    {'dynamic_eids': 
                                        {'192.168.0.0/24': 
                                            {'dynamic_eid_name': '192',
                                            'eid_address': {'virtual_network_id': 'green'},
                                            'id': '192.168.0.0/24',
                                            'last_dynamic_eid': 
                                                {'192.168.0.1': 
                                                    {'eids': 
                                                        {'192.168.0.1': 
                                                            {'discovered_by': 'packet reception',
                                                            'interface': 'GigabitEthernet5',
                                                            'last_activity': '00:00:15',
                                                            'uptime': '11:56:56'}},
                                                    'last_dynamic_eid_discovery_elaps_time': '11:56:56'}},
                                            'mapping_servers': 
                                                {'4.4.4.4': 
                                                    {'proxy_reply': True},
                                                '6.6.6.6': 
                                                    {}},
                                            'num_of_roaming_dynamic_eid': 1,
                                            'registering_more_specific': True,
                                            'rlocs': 'RLOC'}}}}}}}}}}

    golden_output3 = {'execute.return_value': '''
        202-XTR#show lisp all instance-id 101 dynamic-eid detail
        Output for router lisp 0

        -----------------------------------------------------
        LISP Dynamic EID Information for VRF "green"

        Dynamic-EID name: 192
          Database-mapping EID-prefix: 192.168.0.0/24, locator-set RLOC
          Registering more-specific dynamic-EIDs
          Map-Server(s): 4.4.4.4  (proxy-replying)
          Map-Server(s): 6.6.6.6
          Site-based multicast Map-Notify group: 225.1.1.2
          Number of roaming dynamic-EIDs discovered: 1
          Last dynamic-EID discovered: 192.168.0.1, 11:56:56 ago
            192.168.0.1, GigabitEthernet5, uptime: 11:56:56
              last activity: 00:00:15, discovered by: Packet Reception
        '''}

    def test_show_lisp_dynamic_eid_detail_full1(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output1)
        obj = ShowLispDynamicEidDetail(device=self.device)
        parsed_output = obj.parse(instance_id=101)
        self.assertEqual(parsed_output, self.golden_parsed_output1)

    def test_show_lisp_dynamic_eid_detail_full2(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output2)
        obj = ShowLispDynamicEidDetail(device=self.device)
        parsed_output = obj.parse(instance_id=101)
        self.assertEqual(parsed_output, self.golden_parsed_output2)

    def test_show_lisp_dynamic_eid_detail_full3(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output3)
        obj = ShowLispDynamicEidDetail(device=self.device)
        parsed_output = obj.parse(instance_id=101)
        self.assertEqual(parsed_output, self.golden_parsed_output3)

    def test_show_lisp_dynamic_eid_detail_empty(self):
        self.maxDiff = None
        self.device = Mock(**self.empty_output)
        obj = ShowLispDynamicEidDetail(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse(instance_id=101)


# =================================================================
# Unit test for 'show lisp all instance-id <instance_id> <service>'
# =================================================================
class test_show_lisp_instance_id_service(unittest.TestCase):

    '''Unit test for "show lisp all instance-id <instance_id> <service>"'''

    device = Device(name='aDevice')

    empty_output = {'execute.return_value': ''}

    golden_parsed_output1 = {
        'lisp_router_instances': 
            {0: 
                {'lisp_router_id': 
                    {'site_id': 'unspecified',
                    'xtr_id': '0x730E0861-0x12996F6D-0xEFEA2114-0xE1C951F7'},
                'lisp_router_instance_id': 0,
                'service': 
                    {'ipv4': 
                        {'database': 
                            {'dynamic_database_limit': 65535,
                            'dynamic_database_size': 0,
                            'inactive_deconfig_away_size': 0,
                            'route_import_database_limit': 1000,
                            'route_import_database_size': 0,
                            'static_database_limit': 65535,
                            'static_database_size': 1,
                            'total_database_mapping_size': 1},
                        'delegated_database_tree': False,
                        'eid_table': 'vrf red',
                        'etr': 
                            {'accept_mapping_data': 'disabled, verify disabled',
                            'enabled': True,
                            'encapsulation': 'lisp',
                            'map_cache_ttl': '1d00h',
                            'mapping_servers': 
                                {'13.13.13.13 (00:00:35)': 
                                    {'ms_address': '13.13.13.13 (00:00:35)'},
                                '4.4.4.4 (17:49:58)': 
                                    {'ms_address': '4.4.4.4 (17:49:58)'}},
                            'proxy_etr_router': False},
                        'itr': 
                            {'enabled': True,
                            'local_rloc_last_resort': '2.2.2.2',
                            'map_resolvers': 
                                {'13.13.13.13': 
                                    {'map_resolver': '13.13.13.13'},
                                '4.4.4.4': 
                                    {'map_resolver': '4.4.4.4'}},
                            'max_smr_per_map_cache_entry': '8 more specifics',
                            'multiple_smr_suppression_time': '20 secs',
                            'proxy_itr_router': False,
                            'solicit_map_request': 'accept and process',
                            'use_proxy_etr_rloc': '10.10.10.10'},
                        'locator_status_algorithms': 
                            {'ipv4_rloc_min_mask_len': 0,
                            'ipv6_rloc_min_mask_len': 0,
                            'lsb_reports': 'process',
                            'rloc_probe_algorithm': False,
                            'rloc_probe_on_member_change': False,
                            'rloc_probe_on_route_change': 'N/A (periodic probing disabled)'},
                        'locator_table': 'default',
                        'map_cache': 
                            {'imported_route_count': 0,
                            'imported_route_limit': 1000,
                            'map_cache_activity_check_period': '60 secs',
                            'map_cache_fib_updates': 'established',
                            'map_cache_limit': 1000,
                            'map_cache_size': 2,
                            'persistent_map_cache': False,
                            'static_mappings_configured': 0},
                        'map_request_source': 'derived from EID destination',
                        'map_resolver': 
                            {'enabled': False},
                        'map_server': 
                            {'enabled': False,
                            'virtual_network_ids': 
                                {'101': 
                                    {'vni': '101'}}},
                        'mobility_first_hop_router': False,
                        'nat_traversal_router': False,
                        'service': 'ipv4',
                        'site_registration_limit': 0}}}}}

    golden_output1 = {'execute.return_value': '''
        202-XTR#show lisp all instance-id 101 ipv4

        =================================================
        Output for router lisp 0
        =================================================
          Instance ID:                         101
          Router-lisp ID:                      0
          Locator table:                       default
          EID table:                           vrf red
          Ingress Tunnel Router (ITR):         enabled
          Egress Tunnel Router (ETR):          enabled
          Proxy-ITR Router (PITR):             disabled
          Proxy-ETR Router (PETR):             disabled
          NAT-traversal Router (NAT-RTR):      disabled
          Mobility First-Hop Router:           disabled
          Map Server (MS):                     disabled
          Map Resolver (MR):                   disabled
          Delegated Database Tree (DDT):       disabled
          Site Registration Limit:             0
          Map-Request source:                  derived from EID destination
          ITR Map-Resolver(s):                 4.4.4.4, 13.13.13.13
          ETR Map-Server(s):                   4.4.4.4 (17:49:58), 13.13.13.13 (00:00:35)
          xTR-ID:                              0x730E0861-0x12996F6D-0xEFEA2114-0xE1C951F7
          site-ID:                             unspecified
          ITR local RLOC (last resort):        2.2.2.2
          ITR use proxy ETR RLOC(s):           10.10.10.10
          ITR Solicit Map Request (SMR):       accept and process
            Max SMRs per map-cache entry:      8 more specifics
            Multiple SMR suppression time:     20 secs
          ETR accept mapping data:             disabled, verify disabled
          ETR map-cache TTL:                   1d00h
          Locator Status Algorithms:
            RLOC-probe algorithm:              disabled
            RLOC-probe on route change:        N/A (periodic probing disabled)
            RLOC-probe on member change:       disabled
            LSB reports:                       process
            IPv4 RLOC minimum mask length:     /0
            IPv6 RLOC minimum mask length:     /0
          Map-cache:                           
            Static mappings configured:        0
            Map-cache size/limit:              2/1000
            Imported route count/limit:        0/1000
            Map-cache activity check period:   60 secs
            Map-cache FIB updates:             established
            Persistent map-cache:              disabled
          Database:                            
            Total database mapping size:       1
            static database size/limit:        1/65535
            dynamic database size/limit:       0/65535
            route-import database size/limit:  0/1000
            Inactive (deconfig/away) size:     0
          Encapsulation type:                  lisp
        '''}

    golden_parsed_output2 = {
        'lisp_router_instances': 
            {0: 
                {'lisp_router_id': 
                    {'site_id': 'unspecified',
                    'xtr_id': '0x730E0861-0x12996F6D-0xEFEA2114-0xE1C951F7'},
                'lisp_router_instance_id': 0,
                'service': 
                    {'ipv6': 
                        {'database': 
                            {'dynamic_database_limit': 65535,
                            'dynamic_database_size': 0,
                            'inactive_deconfig_away_size': 0,
                            'route_import_database_limit': 1000,
                            'route_import_database_size': 0,
                            'static_database_limit': 65535,
                            'static_database_size': 1,
                            'total_database_mapping_size': 1},
                        'delegated_database_tree': False,
                        'eid_table': 'vrf red',
                        'etr': 
                            {'accept_mapping_data': 'disabled, verify disabled',
                            'enabled': True,
                            'encapsulation': 'lisp',
                            'map_cache_ttl': '1d00h',
                            'mapping_servers': 
                                {'13.13.13.13 (00:00:35)': 
                                    {'ms_address': '13.13.13.13 (00:00:35)'},
                                '4.4.4.4 (17:49:58)': 
                                    {'ms_address': '4.4.4.4 (17:49:58)'}},
                            'proxy_etr_router': False},
                        'itr': 
                            {'enabled': True,
                            'local_rloc_last_resort': '2.2.2.2',
                            'map_resolvers': 
                                {'13.13.13.13': 
                                    {'map_resolver': '13.13.13.13'},
                                '4.4.4.4': 
                                    {'map_resolver': '4.4.4.4'}},
                            'max_smr_per_map_cache_entry': '8 more specifics',
                            'multiple_smr_suppression_time': '20 secs',
                            'proxy_itr_router': False,
                            'solicit_map_request': 'accept and process',
                            'use_proxy_etr_rloc': '10.10.10.10'},
                        'locator_status_algorithms': 
                            {'ipv4_rloc_min_mask_len': 0,
                            'ipv6_rloc_min_mask_len': 0,
                            'lsb_reports': 'process',
                            'rloc_probe_algorithm': False,
                            'rloc_probe_on_member_change': False,
                            'rloc_probe_on_route_change': 'N/A (periodic probing disabled)'},
                        'locator_table': 'default',
                        'map_cache': 
                            {'imported_route_count': 0,
                            'imported_route_limit': 1000,
                            'map_cache_activity_check_period': '60 secs',
                            'map_cache_fib_updates': 'established',
                            'map_cache_limit': 1000,
                            'map_cache_size': 2,
                            'persistent_map_cache': False,
                            'static_mappings_configured': 0},
                        'map_request_source': 'derived from EID destination',
                        'map_resolver': 
                            {'enabled': False},
                        'map_server': 
                            {'enabled': False,
                            'virtual_network_ids': 
                                {'101': 
                                    {'vni': '101'}}},
                        'mobility_first_hop_router': False,
                        'nat_traversal_router': False,
                        'service': 'ipv6',
                        'site_registration_limit': 0}}}}}

    golden_output2 = {'execute.return_value': '''
        202-XTR#show lisp all instance-id 101 ipv4

        =================================================
        Output for router lisp 0
        =================================================
          Instance ID:                         101
          Router-lisp ID:                      0
          Locator table:                       default
          EID table:                           vrf red
          Ingress Tunnel Router (ITR):         enabled
          Egress Tunnel Router (ETR):          enabled
          Proxy-ITR Router (PITR):             disabled
          Proxy-ETR Router (PETR):             disabled
          NAT-traversal Router (NAT-RTR):      disabled
          Mobility First-Hop Router:           disabled
          Map Server (MS):                     disabled
          Map Resolver (MR):                   disabled
          Delegated Database Tree (DDT):       disabled
          Site Registration Limit:             0
          Map-Request source:                  derived from EID destination
          ITR Map-Resolver(s):                 4.4.4.4, 13.13.13.13
          ETR Map-Server(s):                   4.4.4.4 (17:49:58), 13.13.13.13 (00:00:35)
          xTR-ID:                              0x730E0861-0x12996F6D-0xEFEA2114-0xE1C951F7
          site-ID:                             unspecified
          ITR local RLOC (last resort):        2.2.2.2
          ITR use proxy ETR RLOC(s):           10.10.10.10
          ITR Solicit Map Request (SMR):       accept and process
            Max SMRs per map-cache entry:      8 more specifics
            Multiple SMR suppression time:     20 secs
          ETR accept mapping data:             disabled, verify disabled
          ETR map-cache TTL:                   1d00h
          Locator Status Algorithms:
            RLOC-probe algorithm:              disabled
            RLOC-probe on route change:        N/A (periodic probing disabled)
            RLOC-probe on member change:       disabled
            LSB reports:                       process
            IPv4 RLOC minimum mask length:     /0
            IPv6 RLOC minimum mask length:     /0
          Map-cache:                           
            Static mappings configured:        0
            Map-cache size/limit:              2/1000
            Imported route count/limit:        0/1000
            Map-cache activity check period:   60 secs
            Map-cache FIB updates:             established
            Persistent map-cache:              disabled
          Database:                            
            Total database mapping size:       1
            static database size/limit:        1/65535
            dynamic database size/limit:       0/65535
            route-import database size/limit:  0/1000
            Inactive (deconfig/away) size:     0
          Encapsulation type:                  lisp
        '''}

    golden_parsed_output3 = {
        'lisp_router_instances': 
            {0: 
                {'lisp_router_id': 
                    {'site_id': 'unspecified',
                    'xtr_id': '0xA5EABB49-0x6C6CE939-0x530E699E-0x09187DFC'},
                'lisp_router_instance_id': 0,
                'service': 
                    {'ethernet': 
                        {'database': 
                            {'dynamic_database_limit': 65535,
                            'dynamic_database_size': 2,
                            'import_site_db_limit': 65535,
                            'import_site_db_size': 0,
                            'inactive_deconfig_away_size': 0,
                            'proxy_db_size': 0,
                            'route_import_database_limit': 5000,
                            'route_import_database_size': 0,
                            'static_database_limit': 65535,
                            'static_database_size': 0,
                            'total_database_mapping_size': 2},
                        'delegated_database_tree': False,
                        'eid_table': 'Vlan 102',
                        'etr': 
                            {'accept_mapping_data': 'disabled, verify disabled',
                            'enabled': True,
                            'encapsulation': 'vxlan',
                            'map_cache_ttl': '1d00h',
                            'mapping_servers': 
                                {'44.44.44.44 (00:00:45)': 
                                    {'ms_address': '44.44.44.44 (00:00:45)'},
                                '44.44.44.44 (00:00:50)': 
                                    {'ms_address': '44.44.44.44 (00:00:50)'}},
                            'proxy_etr_router': False},
                        'itr': 
                            {'enabled': True,
                            'local_rloc_last_resort': '11.11.11.1',
                            'map_resolvers': 
                                {'44.44.44.44': 
                                    {'map_resolver': '44.44.44.44'}},
                            'max_smr_per_map_cache_entry': '8 more specifics',
                            'multiple_smr_suppression_time': '20 secs',
                            'proxy_itr_router': False,
                            'solicit_map_request': 'accept and process'},
                        'locator_status_algorithms': 
                            {'ipv4_rloc_min_mask_len': 0,
                            'ipv6_rloc_min_mask_len': 0,
                            'lsb_reports': 'process',
                            'rloc_probe_algorithm': False,
                            'rloc_probe_on_member_change': False,
                            'rloc_probe_on_route_change': 'N/A (periodic probing disabled)'},
                        'locator_table': 'default',
                        'map_cache': 
                            {'imported_route_count': 0,
                            'imported_route_limit': 5000,
                            'map_cache_activity_check_period': '60 secs',
                            'map_cache_fib_updates': 'established',
                            'map_cache_limit': 5120,
                            'map_cache_size': 0,
                            'persistent_map_cache': False,
                            'static_mappings_configured': 0},
                        'map_request_source': 'derived from EID destination',
                        'map_resolver': 
                            {'enabled': False},
                            'map_server': 
                                {'enabled': False,
                                'virtual_network_ids': 
                                    {'0': {'vni': '0'},
                                    '1': {'vni': '1'},
                                    '102': {'vni': '102'},
                                    '131': {'vni': '131'},
                                    '132': {'vni': '132'},
                                    '133': {'vni': '133'},
                                    '134': {'vni': '134'},
                                    '135': {'vni': '135'},
                                    '136': {'vni': '136'},
                                    '137': {'vni': '137'},
                                    '138': {'vni': '138'},
                                    '139': {'vni': '139'},
                                    '140': {'vni': '140'},
                                    '141': {'vni': '141'},
                                    '142': {'vni': '142'},
                                    '143': {'vni': '143'},
                                    '144': {'vni': '144'},
                                    '145': {'vni': '145'},
                                    '146': {'vni': '146'},
                                    '147': {'vni': '147'},
                                    '148': {'vni': '148'},
                                    '149': {'vni': '149'},
                                    '150': {'vni': '150'},
                                    '151': {'vni': '151'},
                                    '152': {'vni': '152'},
                                    '153': {'vni': '153'},
                                    '154': {'vni': '154'},
                                    '155': {'vni': '155'},
                                    '156': {'vni': '156'},
                                    '157': {'vni': '157'},
                                    '158': {'vni': '158'},
                                    '159': {'vni': '159'},
                                    '160': {'vni': '160'},
                                    '161': {'vni': '161'},
                                    '162': {'vni': '162'},
                                    '163': {'vni': '163'},
                                    '164': {'vni': '164'},
                                    '165': {'vni': '165'},
                                    '166': {'vni': '166'},
                                    '167': {'vni': '167'},
                                    '168': {'vni': '168'},
                                    '169': {'vni': '169'},
                                    '170': {'vni': '170'},
                                    '171': {'vni': '171'},
                                    '172': {'vni': '172'},
                                    '173': {'vni': '173'},
                                    '174': {'vni': '174'},
                                    '175': {'vni': '175'},
                                    '176': {'vni': '176'},
                                    '177': {'vni': '177'},
                                    '178': {'vni': '178'},
                                    '179': {'vni': '179'},
                                    '180': {'vni': '180'},
                                    '181': {'vni': '181'},
                                    '182': {'vni': '182'},
                                    '183': {'vni': '183'},
                                    '184': {'vni': '184'},
                                    '185': {'vni': '185'},
                                    '186': {'vni': '186'},
                                    '187': {'vni': '187'},
                                    '188': {'vni': '188'},
                                    '189': {'vni': '189'},
                                    '190': {'vni': '190'},
                                    '191': {'vni': '191'},
                                    '192': {'vni': '192'},
                                    '193': {'vni': '193'},
                                    '194': {'vni': '194'},
                                    '195': {'vni': '195'},
                                    '2': {'vni': '2'}}},
                        'mobility_first_hop_router': False,
                        'nat_traversal_router': False,
                        'service': 'ethernet',
                        'site_registration_limit': 0,
                        'source_locator_configuration': 
                            {'vlans': 
                                {'vlan100': 
                                    {'address': '11.11.11.1',
                                    'interface': 'Loopback0'},
                                'vlan101': 
                                    {'address': '11.11.11.1',
                                    'interface': 'Loopback0'}}}}}}}}

    golden_output3 = {'execute.return_value': '''
        OTT-LISP-C3K-3-xTR1#show lisp all instance-id * ethernet

        =================================================
        Output for router lisp 0 instance-id 0
        =================================================
        % EID table not enabled for MAC.

        =================================================
        Output for router lisp 0 instance-id 1
        =================================================
          Instance ID:                         1
          Router-lisp ID:                      0
          Locator table:                       default
          EID table:                           Vlan 101
          Ingress Tunnel Router (ITR):         enabled
          Egress Tunnel Router (ETR):          enabled
          Proxy-ITR Router (PITR):             disabled
          Proxy-ETR Router (PETR):             disabled
          NAT-traversal Router (NAT-RTR):      disabled
          Mobility First-Hop Router:           disabled
          Map Server (MS):                     disabled
          Map Resolver (MR):                   disabled
          Mr-use-petr:                         disabled
          Delegated Database Tree (DDT):       disabled
          Site Registration Limit:             0
          Map-Request source:                  derived from EID destination
          ITR Map-Resolver(s):                 44.44.44.44
                                               66.66.66.66 *** not reachable ***
          ETR Map-Server(s):                   44.44.44.44 (00:00:45)
                                               66.66.66.66 (never)
          xTR-ID:                              0xA5EABB49-0x6C6CE939-0x530E699E-0x09187DFC
          site-ID:                             unspecified
          ITR local RLOC (last resort):        11.11.11.1
          ITR Solicit Map Request (SMR):       accept and process
            Max SMRs per map-cache entry:      8 more specifics
            Multiple SMR suppression time:     20 secs
          ETR accept mapping data:             disabled, verify disabled
          ETR map-cache TTL:                   1d00h
          Locator Status Algorithms:
            RLOC-probe algorithm:              disabled
            RLOC-probe on route change:        N/A (periodic probing disabled)
            RLOC-probe on member change:       disabled
            LSB reports:                       process
            IPv4 RLOC minimum mask length:     /0
            IPv6 RLOC minimum mask length:     /0
          Map-cache:
            Static mappings configured:        0
            Map-cache size/limit:              4/5120
            Imported route count/limit:        0/5000
            Map-cache activity check period:   60 secs
            Map-cache FIB updates:             established
            Persistent map-cache:              disabled
          Source locator configuration:
            Vlan100: 11.11.11.1 (Loopback0)
            Vlan101: 11.11.11.1 (Loopback0)
          Database:
            Total database mapping size:       2
            static database size/limit:        0/65535
            dynamic database size/limit:       2/65535
            route-import database size/limit:  0/5000
            import-site-reg database size/limit0/65535
            proxy database size:               0
            Inactive (deconfig/away) size:     0
          Encapsulation type:                  vxlan

        =================================================
        Output for router lisp 0 instance-id 2
        =================================================
          Instance ID:                         2
          Router-lisp ID:                      0
          Locator table:                       default
          EID table:                           Vlan 102
          Ingress Tunnel Router (ITR):         enabled
          Egress Tunnel Router (ETR):          enabled
          Proxy-ITR Router (PITR):             disabled
          Proxy-ETR Router (PETR):             disabled
          NAT-traversal Router (NAT-RTR):      disabled
          Mobility First-Hop Router:           disabled
          Map Server (MS):                     disabled
          Map Resolver (MR):                   disabled
          Mr-use-petr:                         disabled
          Delegated Database Tree (DDT):       disabled
          Site Registration Limit:             0
          Map-Request source:                  derived from EID destination
          ITR Map-Resolver(s):                 44.44.44.44
                                               66.66.66.66 *** not reachable ***
          ETR Map-Server(s):                   44.44.44.44 (00:00:50)
                                               66.66.66.66 (never)
          xTR-ID:                              0xA5EABB49-0x6C6CE939-0x530E699E-0x09187DFC
          site-ID:                             unspecified
          ITR local RLOC (last resort):        11.11.11.1
          ITR Solicit Map Request (SMR):       accept and process
            Max SMRs per map-cache entry:      8 more specifics
            Multiple SMR suppression time:     20 secs
          ETR accept mapping data:             disabled, verify disabled
          ETR map-cache TTL:                   1d00h
          Locator Status Algorithms:
            RLOC-probe algorithm:              disabled
            RLOC-probe on route change:        N/A (periodic probing disabled)
            RLOC-probe on member change:       disabled
            LSB reports:                       process
            IPv4 RLOC minimum mask length:     /0
            IPv6 RLOC minimum mask length:     /0
          Map-cache:
            Static mappings configured:        0
            Map-cache size/limit:              0/5120
            Imported route count/limit:        0/5000
            Map-cache activity check period:   60 secs
            Map-cache FIB updates:             established
            Persistent map-cache:              disabled
          Source locator configuration:
            Vlan100: 11.11.11.1 (Loopback0)
            Vlan101: 11.11.11.1 (Loopback0)
          Database:
            Total database mapping size:       2
            static database size/limit:        0/65535
            dynamic database size/limit:       2/65535
            route-import database size/limit:  0/5000
            import-site-reg database size/limit0/65535
            proxy database size:               0
            Inactive (deconfig/away) size:     0
          Encapsulation type:                  vxlan

        =================================================
        Output for router lisp 0 instance-id 102
        =================================================
        % EID table not enabled for MAC.

        =================================================
        Output for router lisp 0 instance-id 131
        =================================================
        % EID table not enabled for MAC.

        =================================================
        Output for router lisp 0 instance-id 132
        =================================================
        % EID table not enabled for MAC.

        =================================================
        Output for router lisp 0 instance-id 133
        =================================================
        % EID table not enabled for MAC.

        =================================================
        Output for router lisp 0 instance-id 134
        =================================================
        % EID table not enabled for MAC.

        =================================================
        Output for router lisp 0 instance-id 135
        =================================================
        % EID table not enabled for MAC.

        =================================================
        Output for router lisp 0 instance-id 136
        =================================================
        % EID table not enabled for MAC.

        =================================================
        Output for router lisp 0 instance-id 137
        =================================================
        % EID table not enabled for MAC.

        =================================================
        Output for router lisp 0 instance-id 138
        =================================================
        % EID table not enabled for MAC.

        =================================================
        Output for router lisp 0 instance-id 139
        =================================================
        % EID table not enabled for MAC.

        =================================================
        Output for router lisp 0 instance-id 140
        =================================================
        % EID table not enabled for MAC.

        =================================================
        Output for router lisp 0 instance-id 141
        =================================================
        % EID table not enabled for MAC.

        =================================================
        Output for router lisp 0 instance-id 142
        =================================================
        % EID table not enabled for MAC.

        =================================================
        Output for router lisp 0 instance-id 143
        =================================================
        % EID table not enabled for MAC.

        =================================================
        Output for router lisp 0 instance-id 144
        =================================================
        % EID table not enabled for MAC.

        =================================================
        Output for router lisp 0 instance-id 145
        =================================================
        % EID table not enabled for MAC.

        =================================================
        Output for router lisp 0 instance-id 146
        =================================================
        % EID table not enabled for MAC.

        =================================================
        Output for router lisp 0 instance-id 147
        =================================================
        % EID table not enabled for MAC.

        =================================================
        Output for router lisp 0 instance-id 148
        =================================================
        % EID table not enabled for MAC.

        =================================================
        Output for router lisp 0 instance-id 149
        =================================================
        % EID table not enabled for MAC.

        =================================================
        Output for router lisp 0 instance-id 150
        =================================================
        % EID table not enabled for MAC.

        =================================================
        Output for router lisp 0 instance-id 151
        =================================================
        % EID table not enabled for MAC.

        =================================================
        Output for router lisp 0 instance-id 152
        =================================================
        % EID table not enabled for MAC.

        =================================================
        Output for router lisp 0 instance-id 153
        =================================================
        % EID table not enabled for MAC.

        =================================================
        Output for router lisp 0 instance-id 154
        =================================================
        % EID table not enabled for MAC.

        =================================================
        Output for router lisp 0 instance-id 155
        =================================================
        % EID table not enabled for MAC.

        =================================================
        Output for router lisp 0 instance-id 156
        =================================================
        % EID table not enabled for MAC.

        =================================================
        Output for router lisp 0 instance-id 157
        =================================================
        % EID table not enabled for MAC.

        =================================================
        Output for router lisp 0 instance-id 158
        =================================================
        % EID table not enabled for MAC.

        =================================================
        Output for router lisp 0 instance-id 159
        =================================================
        % EID table not enabled for MAC.

        =================================================
        Output for router lisp 0 instance-id 160
        =================================================
        % EID table not enabled for MAC.

        =================================================
        Output for router lisp 0 instance-id 161
        =================================================
        % EID table not enabled for MAC.

        =================================================
        Output for router lisp 0 instance-id 162
        =================================================
        % EID table not enabled for MAC.

        =================================================
        Output for router lisp 0 instance-id 163
        =================================================
        % EID table not enabled for MAC.

        =================================================
        Output for router lisp 0 instance-id 164
        =================================================
        % EID table not enabled for MAC.

        =================================================
        Output for router lisp 0 instance-id 165
        =================================================
        % EID table not enabled for MAC.

        =================================================
        Output for router lisp 0 instance-id 166
        =================================================
        % EID table not enabled for MAC.

        =================================================
        Output for router lisp 0 instance-id 167
        =================================================
        % EID table not enabled for MAC.

        =================================================
        Output for router lisp 0 instance-id 168
        =================================================
        % EID table not enabled for MAC.

        =================================================
        Output for router lisp 0 instance-id 169
        =================================================
        % EID table not enabled for MAC.

        =================================================
        Output for router lisp 0 instance-id 170
        =================================================
        % EID table not enabled for MAC.

        =================================================
        Output for router lisp 0 instance-id 171
        =================================================
        % EID table not enabled for MAC.

        =================================================
        Output for router lisp 0 instance-id 172
        =================================================
        % EID table not enabled for MAC.

        =================================================
        Output for router lisp 0 instance-id 173
        =================================================
        % EID table not enabled for MAC.

        =================================================
        Output for router lisp 0 instance-id 174
        =================================================
        % EID table not enabled for MAC.

        =================================================
        Output for router lisp 0 instance-id 175
        =================================================
        % EID table not enabled for MAC.

        =================================================
        Output for router lisp 0 instance-id 176
        =================================================
        % EID table not enabled for MAC.

        =================================================
        Output for router lisp 0 instance-id 177
        =================================================
        % EID table not enabled for MAC.

        =================================================
        Output for router lisp 0 instance-id 178
        =================================================
        % EID table not enabled for MAC.

        =================================================
        Output for router lisp 0 instance-id 179
        =================================================
        % EID table not enabled for MAC.

        =================================================
        Output for router lisp 0 instance-id 180
        =================================================
        % EID table not enabled for MAC.

        =================================================
        Output for router lisp 0 instance-id 181
        =================================================
        % EID table not enabled for MAC.

        =================================================
        Output for router lisp 0 instance-id 182
        =================================================
        % EID table not enabled for MAC.

        =================================================
        Output for router lisp 0 instance-id 183
        =================================================
        % EID table not enabled for MAC.

        =================================================
        Output for router lisp 0 instance-id 184
        =================================================
        % EID table not enabled for MAC.

        =================================================
        Output for router lisp 0 instance-id 185
        =================================================
        % EID table not enabled for MAC.

        =================================================
        Output for router lisp 0 instance-id 186
        =================================================
        % EID table not enabled for MAC.

        =================================================
        Output for router lisp 0 instance-id 187
        =================================================
        % EID table not enabled for MAC.

        =================================================
        Output for router lisp 0 instance-id 188
        =================================================
        % EID table not enabled for MAC.

        =================================================
        Output for router lisp 0 instance-id 189
        =================================================
        % EID table not enabled for MAC.

        =================================================
        Output for router lisp 0 instance-id 190
        =================================================
        % EID table not enabled for MAC.

        =================================================
        Output for router lisp 0 instance-id 191
        =================================================
        % EID table not enabled for MAC.

        =================================================
        Output for router lisp 0 instance-id 192
        =================================================
        % EID table not enabled for MAC.

        =================================================
        Output for router lisp 0 instance-id 193
        =================================================
        % EID table not enabled for MAC.

        =================================================
        Output for router lisp 0 instance-id 194
        =================================================
        % EID table not enabled for MAC.

        =================================================
        Output for router lisp 0 instance-id 195
        =================================================
        % EID table not enabled for MAC.
        '''}

    golden_parsed_output4 = {
        'lisp_router_instances': 
            {0: 
                {'lisp_router_id': 
                    {'site_id': 'unspecified',
                    'xtr_id': '0x730E0861-0x12996F6D-0xEFEA2114-0xE1C951F7'},
                'lisp_router_instance_id': 0,
                'service': 
                    {'ethernet': 
                        {'database': 
                            {'dynamic_database_mapping_limit': 1000},
                            'delegated_database_tree': False,
                            'etr': 
                                {'accept_mapping_data': 'disabled, verify disabled',
                                'enabled': True,
                                'map_cache_ttl': '1d00h',
                                'mapping_servers': 
                                    {'13.13.13.13': 
                                        {'ms_address': '13.13.13.13'},
                                    '4.4.4.4': 
                                        {'ms_address': '4.4.4.4'}},
                                'proxy_etr_router': False},
                            'itr': 
                                {'enabled': True,
                                'local_rloc_last_resort': '*** NOT FOUND ***',
                                'map_resolvers': 
                                    {'13.13.13.13': 
                                        {'map_resolver': '13.13.13.13'},
                                    '4.4.4.4': 
                                        {'map_resolver': '4.4.4.4'}},
                                'max_smr_per_map_cache_entry': '8 more specifics',
                                'multiple_smr_suppression_time': '20 secs',
                                'proxy_itr_router': False,
                                'solicit_map_request': 'accept and process'},
                            'locator_status_algorithms': 
                                {'ipv4_rloc_min_mask_len': 0,
                                'ipv6_rloc_min_mask_len': 0,
                                'lsb_reports': 'process',
                                'rloc_probe_algorithm': False,
                                'rloc_probe_on_member_change': False,
                                'rloc_probe_on_route_change': 'N/A (periodic probing disabled)'},
                            'locator_table': 'default',
                            'map_cache': 
                                {'map_cache_activity_check_period': '60 secs',
                                'map_cache_limit': 1000,
                                'persistent_map_cache': False},
                            'map_resolver': 
                                {'enabled': False},
                            'map_server': 
                                {'enabled': False},
                            'mobility_first_hop_router': False,
                            'nat_traversal_router': False,
                            'service': 'ethernet'}}}}}

    golden_output4 =  {'execute.return_value': '''
        202-XTR#show lisp all service ipv4
        =================================================
        Output for router lisp 0
        =================================================
          Router-lisp ID:                      0
          Locator table:                       default
          Ingress Tunnel Router (ITR):         enabled
          Egress Tunnel Router (ETR):          enabled
          Proxy-ITR Router (PITR):             disabled
          Proxy-ETR Router (PETR):             disabled
          NAT-traversal Router (NAT-RTR):      disabled
          Mobility First-Hop Router:           disabled
          Map Server (MS):                     disabled
          Map Resolver (MR):                   disabled
          Delegated Database Tree (DDT):       disabled
          ITR Map-Resolver(s):                 4.4.4.4, 13.13.13.13
          ETR Map-Server(s):                   4.4.4.4, 13.13.13.13
          xTR-ID:                              0x730E0861-0x12996F6D-0xEFEA2114-0xE1C951F7
          site-ID:                             unspecified
          ITR local RLOC (last resort):        *** NOT FOUND ***
          ITR Solicit Map Request (SMR):       accept and process
            Max SMRs per map-cache entry:      8 more specifics
            Multiple SMR suppression time:     20 secs
          ETR accept mapping data:             disabled, verify disabled
          ETR map-cache TTL:                   1d00h
          Locator Status Algorithms:
            RLOC-probe algorithm:              disabled
            RLOC-probe on route change:        N/A (periodic probing disabled)
            RLOC-probe on member change:       disabled
            LSB reports:                       process
            IPv4 RLOC minimum mask length:     /0
            IPv6 RLOC minimum mask length:     /0
          Map-cache:                           
            Map-cache limit:                   1000
            Map-cache activity check period:   60 secs
            Persistent map-cache:              disabled
          Database:                            
            Dynamic database mapping limit:    1000
        '''}

    golden_parsed_output5 = {
        'lisp_router_instances': 
            {0: 
                {'lisp_router_id': 
                    {'site_id': 'unspecified',
                    'xtr_id': '0x5B6A0468-0x55E69768-0xD1AE2E61-0x4A082FD5'},
                'lisp_router_instance_id': 0,
                'service': 
                    {'ethernet': 
                        {'database': 
                            {'dynamic_database_mapping_limit': 1000},
                            'delegated_database_tree': False,
                        'etr': 
                            {'accept_mapping_data': 'disabled, verify disabled',
                            'enabled': True,
                            'map_cache_ttl': '1d00h',
                            'mapping_servers': 
                                {'13.13.13.13': 
                                    {'ms_address': '13.13.13.13'},
                                '4.4.4.4': 
                                    {'ms_address': '4.4.4.4'}},
                            'proxy_etr_router': False},
                        'itr': 
                            {'enabled': True,
                            'local_rloc_last_resort': '*** NOT FOUND ***',
                            'map_resolvers': 
                                {'13.13.13.13': 
                                    {'map_resolver': '13.13.13.13'},
                                '4.4.4.4': 
                                    {'map_resolver': '4.4.4.4'}},
                            'max_smr_per_map_cache_entry': '8 more specifics',
                            'multiple_smr_suppression_time': '20 secs',
                            'proxy_itr_router': False,
                            'solicit_map_request': 'accept and process'},
                        'locator_status_algorithms': 
                            {'ipv4_rloc_min_mask_len': 0,
                            'ipv6_rloc_min_mask_len': 0,
                            'lsb_reports': 'process',
                            'rloc_probe_algorithm': False,
                            'rloc_probe_on_member_change': False,
                            'rloc_probe_on_route_change': 'N/A (periodic probing disabled)'},
                        'locator_table': 'default',
                        'map_cache': 
                            {'map_cache_activity_check_period': '60 secs',
                            'map_cache_limit': 1000,
                            'persistent_map_cache': False},
                        'map_resolver': 
                            {'enabled': False},
                        'map_server': 
                            {'enabled': False},
                        'mobility_first_hop_router': False,
                        'nat_traversal_router': False,
                        'service': 'ethernet'}}}}}

    golden_output5 = {'execute.return_value': '''
        202-XTR#show lisp all service ipv6
        =================================================
        Output for router lisp 0
        =================================================
          Router-lisp ID:                      0
          Locator table:                       default
          Ingress Tunnel Router (ITR):         enabled
          Egress Tunnel Router (ETR):          enabled
          Proxy-ITR Router (PITR):             disabled
          Proxy-ETR Router (PETR):             disabled
          NAT-traversal Router (NAT-RTR):      disabled
          Mobility First-Hop Router:           disabled
          Map Server (MS):                     disabled
          Map Resolver (MR):                   disabled
          Delegated Database Tree (DDT):       disabled
          ITR Map-Resolver(s):                 4.4.4.4, 13.13.13.13
          ETR Map-Server(s):                   4.4.4.4, 13.13.13.13
          xTR-ID:                              0x5B6A0468-0x55E69768-0xD1AE2E61-0x4A082FD5
          site-ID:                             unspecified
          ITR local RLOC (last resort):        *** NOT FOUND ***
          ITR Solicit Map Request (SMR):       accept and process
            Max SMRs per map-cache entry:      8 more specifics
            Multiple SMR suppression time:     20 secs
          ETR accept mapping data:             disabled, verify disabled
          ETR map-cache TTL:                   1d00h
          Locator Status Algorithms:
            RLOC-probe algorithm:              disabled
            RLOC-probe on route change:        N/A (periodic probing disabled)
            RLOC-probe on member change:       disabled
            LSB reports:                       process
            IPv4 RLOC minimum mask length:     /0
            IPv6 RLOC minimum mask length:     /0
          Map-cache:                           
            Map-cache limit:                   1000
            Map-cache activity check period:   60 secs
            Persistent map-cache:              disabled
          Database:                            
            Dynamic database mapping limit:    1000
        '''}

    golden_parsed_output6 = {
        'lisp_router_instances': 
            {0: 
                {'lisp_router_id': 
                    {'site_id': 'unspecified',
                    'xtr_id': '0xA5EABB49-0x6C6CE939-0x530E699E-0x09187DFC'},
                'lisp_router_instance_id': 0,
                'service': 
                    {'ethernet': 
                        {'database': 
                            {'dynamic_database_mapping_limit': 5120},
                            'delegated_database_tree': False,
                        'etr': 
                            {'accept_mapping_data': 'disabled, verify disabled',
                            'enabled': True,
                            'map_cache_ttl': '1d00h',
                            'mapping_servers': 
                                {'44.44.44.44': 
                                    {'ms_address': '44.44.44.44'}},
                            'proxy_etr_router': False},
                        'itr': 
                            {'enabled': True,
                            'local_rloc_last_resort': '*** NOT FOUND ***',
                            'map_resolvers': 
                                {'44.44.44.44': 
                                    {'map_resolver': '44.44.44.44'}},
                            'max_smr_per_map_cache_entry': '8 more specifics',
                            'multiple_smr_suppression_time': '20 secs',
                            'proxy_itr_router': False,
                            'solicit_map_request': 'accept and process'},
                        'locator_status_algorithms':
                            {'ipv4_rloc_min_mask_len': 0,
                            'ipv6_rloc_min_mask_len': 0,
                            'lsb_reports': 'process',
                            'rloc_probe_algorithm': False,
                            'rloc_probe_on_member_change': False,
                            'rloc_probe_on_route_change': 'N/A (periodic probing disabled)'},
                        'locator_table': 'default',
                        'map_cache': 
                            {'map_cache_activity_check_period': '60 secs',
                            'map_cache_limit': 5120,
                            'persistent_map_cache': False},
                        'map_resolver': 
                            {'enabled': False},
                        'map_server': 
                            {'enabled': False},
                        'mobility_first_hop_router': False,
                        'nat_traversal_router': False,
                        'service': 'ethernet',
                        'source_locator_configuration': 
                            {'vlans': 
                                {'vlan100': 
                                    {'address': '11.11.11.1',
                                    'interface': 'Loopback0'},
                                'vlan101': 
                                    {'address': '11.11.11.1',
                                    'interface': 'Loopback0'}}}}}}}}

    golden_output6 = {'execute.return_value': '''
        OTT-LISP-C3K-3-xTR1#show lisp all service ethernet

        =================================================
        Output for router lisp 0
        =================================================
          Router-lisp ID:                      0
          Locator table:                       default
          Ingress Tunnel Router (ITR):         enabled
          Egress Tunnel Router (ETR):          enabled
          Proxy-ITR Router (PITR):             disabled
          Proxy-ETR Router (PETR):             disabled
          NAT-traversal Router (NAT-RTR):      disabled
          Mobility First-Hop Router:           disabled
          Map Server (MS):                     disabled
          Map Resolver (MR):                   disabled
          Mr-use-petr:                         disabled
          Delegated Database Tree (DDT):       disabled
          ITR Map-Resolver(s):                 44.44.44.44
                                               66.66.66.66
          ETR Map-Server(s):                   44.44.44.44
                                               66.66.66.66
          xTR-ID:                              0xA5EABB49-0x6C6CE939-0x530E699E-0x09187DFC
          site-ID:                             unspecified
          ITR local RLOC (last resort):        *** NOT FOUND ***
          ITR Solicit Map Request (SMR):       accept and process
            Max SMRs per map-cache entry:      8 more specifics
            Multiple SMR suppression time:     20 secs
          ETR accept mapping data:             disabled, verify disabled
          ETR map-cache TTL:                   1d00h
          Locator Status Algorithms:
            RLOC-probe algorithm:              disabled
            RLOC-probe on route change:        N/A (periodic probing disabled)
            RLOC-probe on member change:       disabled
            LSB reports:                       process
            IPv4 RLOC minimum mask length:     /0
            IPv6 RLOC minimum mask length:     /0
          Map-cache:
            Map-cache limit:                   5120
            Map-cache activity check period:   60 secs
            Persistent map-cache:              disabled
          Source locator configuration:
            Vlan100: 11.11.11.1 (Loopback0)
            Vlan101: 11.11.11.1 (Loopback0)
          Database:
            Dynamic database mapping limit:    5120
        '''}

    def test_show_lisp_instance_id_service_full1(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output1)
        obj = ShowLispService(device=self.device)
        parsed_output = obj.parse(instance_id=101, service='ipv4')
        self.assertEqual(parsed_output, self.golden_parsed_output1)

    def test_show_lisp_instance_id_service_full2(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output2)
        obj = ShowLispService(device=self.device)
        parsed_output = obj.parse(instance_id=101, service='ipv6')
        self.assertEqual(parsed_output, self.golden_parsed_output2)

    def test_show_lisp_instance_id_service_full3(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output3)
        obj = ShowLispService(device=self.device)
        parsed_output = obj.parse(instance_id='*', service='ethernet')
        self.assertEqual(parsed_output, self.golden_parsed_output3)

    def test_show_lisp_instance_id_service_full4(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output4)
        obj = ShowLispService(device=self.device)
        parsed_output = obj.parse(instance_id='*', service='ethernet')
        self.assertEqual(parsed_output, self.golden_parsed_output4)

    def test_show_lisp_instance_id_service_full5(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output5)
        obj = ShowLispService(device=self.device)
        parsed_output = obj.parse(instance_id='*', service='ethernet')
        self.assertEqual(parsed_output, self.golden_parsed_output5)

    def test_show_lisp_instance_id_service_full6(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output6)
        obj = ShowLispService(device=self.device)
        parsed_output = obj.parse(instance_id='*', service='ethernet')
        self.assertEqual(parsed_output, self.golden_parsed_output6)

    def test_show_lisp_instance_id_service_empty(self):
        self.maxDiff = None
        self.device = Mock(**self.empty_output)
        obj = ShowLispService(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse(instance_id='*', service='ipv4')



# ===========================================================================
# Unit test for 'show lisp all instance-id <instance_id> <service> map-cache'
# ===========================================================================
class test_show_lisp_instance_id_service_map_cache(unittest.TestCase):

    '''Unit test for "show lisp all instance-id <instance_id> <service> map-cache"'''

    device = Device(name='aDevice')

    empty_output = {'execute.return_value': ''}

    golden_parsed_output1 = {
        'lisp_router_instances': 
            {0: 
                {'lisp_router_instance_id': 0,
                'service': 
                    {'ipv4': 
                        {'service': 'ipv4',
                        'itr': 
                            {'map_cache': 
                                {101: 
                                    {'vni': '101',
                                    'iid': 101,
                                    'entries': 2,
                                    'mappings': 
                                        {'0.0.0.0/0': 
                                            {'id': '0.0.0.0/0',
                                            'uptime': '15:23:50',
                                            'expires': 'never',
                                            'via': 'static-send-map-request',
                                            'eid': 
                                                {'address_type': 'ipv4-afi',
                                                'virtual_network_id': 'vrf red',
                                                'ipv4': 
                                                    {'ipv4': '0.0.0.0/0'}},
                                            'negative_mapping': {'map_reply_action': 'send-map-request'}},
                                        '192.168.9.0/24': 
                                            {'id': '192.168.9.0/24',
                                            'uptime': '00:04:02',
                                            'expires': '23:55:57',
                                            'via': 'map-reply, complete',
                                            'eid': 
                                                {'address_type': 'ipv4-afi',
                                                'virtual_network_id': 'vrf red',
                                                'ipv4': 
                                                    {'ipv4': '192.168.9.0/24'}},
                                            'positive_mapping': 
                                                {'rlocs': 
                                                    {1: 
                                                        {'id': '1',
                                                        'locator_address': 
                                                            {'address_type': 'ipv4-afi',
                                                            'encap_iid': '-',
                                                            'ipv4': 
                                                                {'ipv4': '8.8.8.8'},
                                                            'priority': 50,
                                                            'state': 'up',
                                                            'uptime': '00:04:02',
                                                            'virtual_network_id': '101',
                                                            'weight': 50}}}}}}}}}}}}}}

    golden_output1 = {'execute.return_value': '''
        202-XTR#show lisp all instance-id 101 ipv4 map-cache 
        =====================================================
        Output for router lisp 0
        =====================================================
        LISP IPv4 Mapping Cache for EID-table vrf red (IID 101), 2 entries

        0.0.0.0/0, uptime: 15:23:50, expires: never, via static-send-map-request
          Negative cache entry, action: send-map-request
        192.168.9.0/24, uptime: 00:04:02, expires: 23:55:57, via map-reply, complete
          Locator  Uptime    State      Pri/Wgt     Encap-IID
          8.8.8.8  00:04:02  up          50/50        -
        '''}

    golden_parsed_output2 = {
        'lisp_router_instances': 
            {0: 
                {'lisp_router_instance_id': 0,
                'service': 
                    {'ipv6': 
                        {'service': 'ipv6',
                        'itr': 
                            {'map_cache': 
                                {101: 
                                    {'vni': '101',
                                    'entries': 2,
                                    'iid': 101,
                                    'mappings': 
                                        {'172.16.10.0/24': 
                                            {'eid': 
                                                {'address_type': 'ipv6-afi',
                                                'ipv4': 
                                                    {'ipv4': '172.16.10.0/24'},
                                                'virtual_network_id': 'vrf red'},
                                            'expires': '23:59:59',
                                            'id': '172.16.10.0/24',
                                            'positive_mapping': 
                                                {'rlocs': 
                                                    {1: 
                                                        {'id': '1',
                                                        'locator_address': 
                                                            {'address_type': 'ipv6-afi',
                                                            'ipv4': {'ipv4': '172.16.156.134'},
                                                            'priority': 1,
                                                            'state': 'up',
                                                            'uptime': '00:00:00',
                                                            'virtual_network_id': '101',
                                                            'weight': 50}},
                                                    2: 
                                                        {'id': '2',
                                                        'locator_address': 
                                                            {'address_type': 'ipv6-afi',
                                                            'ipv4': 
                                                                {'ipv4': '192.168.65.94'},
                                                            'priority': 1,
                                                            'state': 'up',
                                                            'uptime': '00:00:00',
                                                            'virtual_network_id': '101',
                                                            'weight': 50}},
                                                    3: 
                                                        {'id': '3',
                                                        'locator_address': 
                                                            {'address_type': 'ipv6-afi',
                                                            'ipv6': 
                                                                {'ipv6': '2001:468:D01:9C::80DF:9C86'},
                                                            'priority': 2,
                                                            'state': 'up',
                                                            'uptime': '00:00:00',
                                                            'virtual_network_id': '101',
                                                            'weight': 100}}}},
                                            'uptime': '00:00:00',
                                            'via': 'map-reply, complete'},
                                        '2001:192:168:9::/64': 
                                            {'eid': 
                                                {'address_type': 'ipv6-afi',
                                                'ipv6': 
                                                    {'ipv6': '2001:192:168:9::/64'},
                                                'virtual_network_id': 'vrf red'},
                                            'expires': '23:53:08',
                                            'id': '2001:192:168:9::/64',
                                            'positive_mapping': 
                                                {'rlocs': 
                                                    {1: 
                                                        {'id': '1',
                                                        'locator_address': 
                                                            {'address_type': 'ipv6-afi',
                                                            'encap_iid': '-',
                                                            'ipv4': 
                                                                {'ipv4': '8.8.8.8'},
                                                            'priority': 50,
                                                            'state': 'up',
                                                            'uptime': '00:06:51',
                                                            'virtual_network_id': '101',
                                                            'weight': 50}}}},
                                            'uptime': '00:06:51',
                                            'via': 'map-reply, complete'},
                                        '::/0': 
                                            {'eid': 
                                                {'address_type': 'ipv6-afi',
                                                'ipv6': 
                                                    {'ipv6': '::/0'},
                                                'virtual_network_id': 'vrf red'},
                                            'expires': 'never',
                                            'id': '::/0',
                                            'negative_mapping': 
                                                {'map_reply_action': 'send-map-request'},
                                            'uptime': '00:11:28',
                                            'via': 'static-send-map-request'}}}}}}}}}}

    golden_output2 = {'execute.return_value': '''
        202-XTR#show lisp all instance-id 101 ipv6 map-cache 

        =====================================================
        Output for router lisp 0
        =====================================================
        LISP IPv6 Mapping Cache for EID-table vrf red (IID 101), 2 entries

        ::/0, uptime: 00:11:28, expires: never, via static-send-map-request
          Negative cache entry, action: send-map-request
        2001:192:168:9::/64, uptime: 00:06:51, expires: 23:53:08, via map-reply, complete
          Locator  Uptime    State      Pri/Wgt     Encap-IID
          8.8.8.8  00:06:51  up          50/50        -
        172.16.10.0/24, uptime: 00:00:00, expires: 23:59:59, via map-reply, complete
          Locator                     Uptime    State      Pri/Wgt
          172.16.156.134             00:00:00  up           1/50
          192.168.65.94                00:00:00  up           1/50
          2001:468:D01:9C::80DF:9C86  00:00:00  up           2/100
        '''}

    golden_parsed_output3 = {
        'lisp_router_instances': 
            {0: 
                {'lisp_router_instance_id': 0,
                'service': 
                    {'ethernet': 
                        {'service': 'ethernet',
                        'itr': 
                            {'map_cache': 
                                {'193': 
                                    {'vni': '193',
                                    'entries': 4,
                                    'iid': 1,
                                    'mappings': 
                                        {'b827.eb51.f5ce/48': 
                                            {'eid': 
                                                {'address_type': 'mac-afi',
                                                'ipv4': 
                                                    {'ipv4': 'b827.eb51.f5ce/48'},
                                                'virtual_network_id': 'Vlan 101'},
                                            'expires': '01:10:17',
                                            'id': 'b827.eb51.f5ce/48',
                                            'positive_mapping': 
                                                {'rlocs': 
                                                    {1: 
                                                        {'id': '1',
                                                        'locator_address': 
                                                            {'address_type': 'mac-afi',
                                                            'encap_iid': '-',
                                                            'ipv4': 
                                                                {'ipv4': '22.22.22.1'},
                                                            'priority': 0,
                                                            'state': 'up',
                                                            'uptime': '22:49:42',
                                                            'virtual_network_id': '193',
                                                            'weight': 0}}}},
                                            'uptime': '22:49:42',
                                            'via': 'WLC Map-Notify, complete'},
                                        'b827.eb73.159c/48': 
                                            {'eid': 
                                                {'address_type': 'mac-afi',
                                                'ipv4': 
                                                    {'ipv4': 'b827.eb73.159c/48'},
                                                'virtual_network_id': 'Vlan 101'},
                                            'expires': '08:57:24',
                                            'id': 'b827.eb73.159c/48',
                                            'positive_mapping': 
                                                {'rlocs': 
                                                    {1: 
                                                        {'id': '1',
                                                        'locator_address': 
                                                            {'address_type': 'mac-afi',
                                                            'encap_iid': '-',
                                                            'ipv4': 
                                                                {'ipv4': '22.22.22.1'},
                                                            'priority': 0,
                                                            'state': 'up',
                                                            'uptime': '15:02:35',
                                                            'virtual_network_id': '193',
                                                            'weight': 0}}}},
                                            'uptime': '15:02:35',
                                            'via': 'WLC Map-Notify, complete'},
                                        'b827.ebd0.acc6/48': 
                                            {'eid': 
                                                {'address_type': 'mac-afi',
                                                'ipv4': 
                                                    {'ipv4': 'b827.ebd0.acc6/48'},
                                                'virtual_network_id': 'Vlan 101'},
                                            'expires': '08:57:25',
                                            'id': 'b827.ebd0.acc6/48',
                                            'positive_mapping': 
                                                {'rlocs': 
                                                    {1: 
                                                        {'id': '1',
                                                        'locator_address': 
                                                            {'address_type': 'mac-afi',
                                                            'encap_iid': '-',
                                                            'ipv4': 
                                                                {'ipv4': '22.22.22.1'},
                                                            'priority': 0,
                                                            'state': 'up',
                                                            'uptime': '15:02:34',
                                                            'virtual_network_id': '193',
                                                            'weight': 0}}}},
                                            'uptime': '15:02:34',
                                            'via': 'WLC Map-Notify, complete'},
                                        'b827.ebd6.0c63/48': 
                                            {'eid': 
                                                {'address_type': 'mac-afi',
                                                'ipv4': 
                                                    {'ipv4': 'b827.ebd6.0c63/48'},
                                                'virtual_network_id': 'Vlan 101'},
                                            'expires': '09:02:44',
                                            'id': 'b827.ebd6.0c63/48',
                                            'positive_mapping': 
                                                {'rlocs': 
                                                    {1: 
                                                        {'id': '1',
                                                        'locator_address': 
                                                            {'address_type': 'mac-afi',
                                                        'encap_iid': '-',
                                                        'ipv4': {'ipv4': '22.22.22.1'},
                                                        'priority': 0,
                                                        'state': 'up',
                                                        'uptime': '14:57:15',
                                                        'virtual_network_id': '193',
                                                        'weight': 0}}}},
                                            'uptime': '14:57:15',
                                            'via': 'WLC Map-Notify, complete'}}}}}}}}}}

    golden_output3 = {'execute.return_value': '''
        OTT-LISP-C3K-3-xTR1#show lisp all instance-id * ethernet map-cache
        =================================================
        Output for router lisp 0 instance-id 0
        =================================================
        % EID table not enabled for MAC.

        =================================================
        Output for router lisp 0 instance-id 193
        =================================================
        LISP MAC Mapping Cache for EID-table Vlan 101 (IID 1), 4 entries

        b827.eb51.f5ce/48, uptime: 22:49:42, expires: 01:10:17, via WLC Map-Notify, complete
          Locator     Uptime    State      Pri/Wgt     Encap-IID
          22.22.22.1  22:49:42  up           0/0         -
        b827.eb73.159c/48, uptime: 15:02:35, expires: 08:57:24, via WLC Map-Notify, complete
          Locator     Uptime    State      Pri/Wgt     Encap-IID
          22.22.22.1  15:02:35  up           0/0         -
        b827.ebd0.acc6/48, uptime: 15:02:34, expires: 08:57:25, via WLC Map-Notify, complete
          Locator     Uptime    State      Pri/Wgt     Encap-IID
          22.22.22.1  15:02:34  up           0/0         -
        b827.ebd6.0c63/48, uptime: 14:57:15, expires: 09:02:44, via WLC Map-Notify, complete
          Locator     Uptime    State      Pri/Wgt     Encap-IID
          22.22.22.1  14:57:15  up           0/0         -

        =================================================
        Output for router lisp 0 instance-id 2
        =================================================

        =================================================
        Output for router lisp 0 instance-id 102
        =================================================
        % EID table not enabled for MAC.

        =================================================
        Output for router lisp 0 instance-id 131
        =================================================
        % EID table not enabled for MAC.

        =================================================
        Output for router lisp 0 instance-id 132
        =================================================
        % EID table not enabled for MAC.

        =================================================
        Output for router lisp 0 instance-id 133
        =================================================
        % EID table not enabled for MAC.

        =================================================
        Output for router lisp 0 instance-id 134
        =================================================
        % EID table not enabled for MAC.

        =================================================
        Output for router lisp 0 instance-id 135
        =================================================
        % EID table not enabled for MAC.

        =================================================
        Output for router lisp 0 instance-id 136
        =================================================
        % EID table not enabled for MAC.

        =================================================
        Output for router lisp 0 instance-id 137
        =================================================
        % EID table not enabled for MAC.

        =================================================
        Output for router lisp 0 instance-id 138
        =================================================
        % EID table not enabled for MAC.

        =================================================
        Output for router lisp 0 instance-id 139
        =================================================
        % EID table not enabled for MAC.

        =================================================
        Output for router lisp 0 instance-id 140
        =================================================
        % EID table not enabled for MAC.

        =================================================
        Output for router lisp 0 instance-id 141
        =================================================
        % EID table not enabled for MAC.

        =================================================
        Output for router lisp 0 instance-id 142
        =================================================
        % EID table not enabled for MAC.

        =================================================
        Output for router lisp 0 instance-id 143
        =================================================
        % EID table not enabled for MAC.

        =================================================
        Output for router lisp 0 instance-id 144
        =================================================
        % EID table not enabled for MAC.

        =================================================
        Output for router lisp 0 instance-id 145
        =================================================
        % EID table not enabled for MAC.

        =================================================
        Output for router lisp 0 instance-id 146
        =================================================
        % EID table not enabled for MAC.

        =================================================
        Output for router lisp 0 instance-id 147
        =================================================
        % EID table not enabled for MAC.

        =================================================
        Output for router lisp 0 instance-id 148
        =================================================
        % EID table not enabled for MAC.

        =================================================
        Output for router lisp 0 instance-id 149
        =================================================
        % EID table not enabled for MAC.

        =================================================
        Output for router lisp 0 instance-id 150
        =================================================
        % EID table not enabled for MAC.

        =================================================
        Output for router lisp 0 instance-id 151
        =================================================
        % EID table not enabled for MAC.

        =================================================
        Output for router lisp 0 instance-id 152
        =================================================
        % EID table not enabled for MAC.

        =================================================
        Output for router lisp 0 instance-id 153
        =================================================
        % EID table not enabled for MAC.

        =================================================
        Output for router lisp 0 instance-id 154
        =================================================
        % EID table not enabled for MAC.

        =================================================
        Output for router lisp 0 instance-id 155
        =================================================
        % EID table not enabled for MAC.

        =================================================
        Output for router lisp 0 instance-id 156
        =================================================
        % EID table not enabled for MAC.

        =================================================
        Output for router lisp 0 instance-id 157
        =================================================
        % EID table not enabled for MAC.

        =================================================
        Output for router lisp 0 instance-id 158
        =================================================
        % EID table not enabled for MAC.

        =================================================
        Output for router lisp 0 instance-id 159
        =================================================
        % EID table not enabled for MAC.

        =================================================
        Output for router lisp 0 instance-id 160
        =================================================
        % EID table not enabled for MAC.

        =================================================
        Output for router lisp 0 instance-id 161
        =================================================
        % EID table not enabled for MAC.

        =================================================
        Output for router lisp 0 instance-id 162
        =================================================
        % EID table not enabled for MAC.

        =================================================
        Output for router lisp 0 instance-id 163
        =================================================
        % EID table not enabled for MAC.

        =================================================
        Output for router lisp 0 instance-id 164
        =================================================
        % EID table not enabled for MAC.

        =================================================
        Output for router lisp 0 instance-id 165
        =================================================
        % EID table not enabled for MAC.

        =================================================
        Output for router lisp 0 instance-id 166
        =================================================
        % EID table not enabled for MAC.

        =================================================
        Output for router lisp 0 instance-id 167
        =================================================
        % EID table not enabled for MAC.

        =================================================
        Output for router lisp 0 instance-id 168
        =================================================
        % EID table not enabled for MAC.

        =================================================
        Output for router lisp 0 instance-id 169
        =================================================
        % EID table not enabled for MAC.

        =================================================
        Output for router lisp 0 instance-id 170
        =================================================
        % EID table not enabled for MAC.

        =================================================
        Output for router lisp 0 instance-id 171
        =================================================
        % EID table not enabled for MAC.

        =================================================
        Output for router lisp 0 instance-id 172
        =================================================
        % EID table not enabled for MAC.

        =================================================
        Output for router lisp 0 instance-id 173
        =================================================
        % EID table not enabled for MAC.

        =================================================
        Output for router lisp 0 instance-id 174
        =================================================
        % EID table not enabled for MAC.

        =================================================
        Output for router lisp 0 instance-id 175
        =================================================
        % EID table not enabled for MAC.

        =================================================
        Output for router lisp 0 instance-id 176
        =================================================
        % EID table not enabled for MAC.

        =================================================
        Output for router lisp 0 instance-id 177
        =================================================
        % EID table not enabled for MAC.

        =================================================
        Output for router lisp 0 instance-id 178
        =================================================
        % EID table not enabled for MAC.

        =================================================
        Output for router lisp 0 instance-id 179
        =================================================
        % EID table not enabled for MAC.

        =================================================
        Output for router lisp 0 instance-id 180
        =================================================
        % EID table not enabled for MAC.

        =================================================
        Output for router lisp 0 instance-id 181
        =================================================
        % EID table not enabled for MAC.

        =================================================
        Output for router lisp 0 instance-id 182
        =================================================
        % EID table not enabled for MAC.

        =================================================
        Output for router lisp 0 instance-id 183
        =================================================
        % EID table not enabled for MAC.

        =================================================
        Output for router lisp 0 instance-id 184
        =================================================
        % EID table not enabled for MAC.

        =================================================
        Output for router lisp 0 instance-id 185
        =================================================
        % EID table not enabled for MAC.

        =================================================
        Output for router lisp 0 instance-id 186
        =================================================
        % EID table not enabled for MAC.

        =================================================
        Output for router lisp 0 instance-id 187
        =================================================
        % EID table not enabled for MAC.

        =================================================
        Output for router lisp 0 instance-id 188
        =================================================
        % EID table not enabled for MAC.

        =================================================
        Output for router lisp 0 instance-id 189
        =================================================
        % EID table not enabled for MAC.

        =================================================
        Output for router lisp 0 instance-id 190
        =================================================
        % EID table not enabled for MAC.

        =================================================
        Output for router lisp 0 instance-id 191
        =================================================
        % EID table not enabled for MAC.

        =================================================
        Output for router lisp 0 instance-id 192
        =================================================
        % EID table not enabled for MAC.

        =================================================
        Output for router lisp 0 instance-id 194
        =================================================
        % EID table not enabled for MAC.

        =================================================
        Output for router lisp 0 instance-id 195
        =================================================
        % EID table not enabled for MAC.
        '''}

    def test_show_lisp_instance_id_service_map_cache_full1(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output1)
        obj = ShowLispServiceMapCache(device=self.device)
        parsed_output = obj.parse(instance_id=101, service='ipv4')
        self.assertEqual(parsed_output, self.golden_parsed_output1)

    def test_show_lisp_instance_id_service_map_cache_full2(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output2)
        obj = ShowLispServiceMapCache(device=self.device)
        parsed_output = obj.parse(instance_id=101, service='ipv6')
        self.assertEqual(parsed_output, self.golden_parsed_output2)

    def test_show_lisp_instance_id_service_map_cache_full3(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output3)
        obj = ShowLispServiceMapCache(device=self.device)
        parsed_output = obj.parse(instance_id='*', service='ethernet')
        self.assertEqual(parsed_output, self.golden_parsed_output3)


    def test_show_lisp_instance_id_service_map_cache_empty(self):
        self.maxDiff = None
        self.device = Mock(**self.empty_output)
        obj = ShowLispServiceMapCache(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse(instance_id='*', service='ipv4')



if __name__ == '__main__':
    unittest.main()
