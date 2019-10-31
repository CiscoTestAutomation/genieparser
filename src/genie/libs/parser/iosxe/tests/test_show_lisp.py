
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
                                              ShowLispServiceMapCache,\
                                              ShowLispServiceRlocMembers,\
                                              ShowLispServiceSmr,\
                                              ShowLispServiceSummary,\
                                              ShowLispServiceDatabase,\
                                              ShowLispServiceServerSummary,\
                                              ShowLispServiceServerDetailInternal,\
                                              ShowLispServiceStatistics



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
                        {'10.16.2.2':
                            {'state': 'up',
                            'time': '00:51:38',
                            'total_in': 8,
                            'total_out': 13,
                            'users': 3},
                        '10.144.6.6':
                            {'state': 'up',
                            'time': '00:51:53',
                            'total_in': 3,
                            'total_out': 10,
                            'users': 1},
                        '10.1.8.8':
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
        10.16.2.2                      Up         00:51:38        8/13     3
        10.144.6.6                     Up         00:51:53        3/10     1
        10.1.8.8                       Up         00:52:15        8/13     3
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
                                                {'172.16.1.0/24':
                                                    {'bidirectional': True,
                                                    'eid_record': '172.16.1.0/24'}}}},
                                    'vni': '102'},
                                '103':
                                    {'extranets':
                                        {'ext1':
                                            {'extranet': 'ext1',
                                            'home_instance_id': 103,
                                            'provider':
                                                {'10.220.100.0/24':
                                                    {'bidirectional': True,
                                                    'eid_record': '10.220.100.0/24'},
                                                '192.168.195.0/24':
                                                    {'bidirectional': True,
                                                    'eid_record': '192.168.195.0/24'},
                                                '10.121.88.0/24':
                                                    {'bidirectional': True,
                                                    'eid_record': '10.121.88.0/24'}}}},
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
        Provider             103        10.121.88.0/24
        Provider             103        10.220.100.0/24
        Provider             103        192.168.195.0/24
        Subscriber           102        172.16.1.0/24
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
                                                    'site_based_multicast_map_notify_group': 'none configured'}}}}}}}}}}

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
                                            'site_based_multicast_map_notify_group': 'none configured'}}}}}}}}}}

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
                                                {'10.64.4.4': 
                                                    {'proxy_reply': True},
                                                '10.144.6.6': 
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
          Map-Server(s): 10.64.4.4  (proxy-replying)
          Map-Server(s): 10.144.6.6
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
class test_show_lisp_service(unittest.TestCase):

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
                        {'delegated_database_tree': False,
                        'etr': 
                            {'accept_mapping_data': 'disabled, verify disabled',
                            'enabled': True,
                            'encapsulation': 'lisp',
                            'map_cache_ttl': '1d00h',
                            'use_petrs':
                                {'10.10.10.10':
                                    {'use_petr': '10.10.10.10',
                                    },
                                },
                            'mapping_servers': 
                                {'10.166.13.13': 
                                    {'ms_address': '10.166.13.13',
                                    'uptime': '00:00:35'},
                                '10.64.4.4': 
                                    {'ms_address': '10.64.4.4',
                                    'uptime': '17:49:58'}},
                            'proxy_etr_router': False},
                        'instance_id': 
                            {'101': 
                                {'database': 
                                    {'dynamic_database_limit': 65535,
                                    'dynamic_database_size': 0,
                                    'inactive_deconfig_away_size': 0,
                                    'route_import_database_limit': 1000,
                                    'route_import_database_size': 0,
                                    'static_database_limit': 65535,
                                    'static_database_size': 1,
                                    'total_database_mapping_size': 1},
                                'eid_table': 'vrf red',
                                'itr': 
                                    {'local_rloc_last_resort': '10.16.2.2',
                                    'use_proxy_etr_rloc': '10.10.10.10'},
                                'map_cache': 
                                    {'imported_route_count': 0,
                                    'imported_route_limit': 1000,
                                    'map_cache_size': 2,
                                    'persistent_map_cache': False,
                                    'static_mappings_configured': 0},
                                'map_request_source': 'derived from EID destination',
                                'mapping_servers': 
                                    {'10.166.13.13': 
                                        {'ms_address': '10.166.13.13',
                                        'uptime': '00:00:35'},
                                    '10.64.4.4': 
                                        {'ms_address': '10.64.4.4',
                                        'uptime': '17:49:58'}},
                                'site_registration_limit': 0}},
                        'itr': 
                            {'enabled': True,
                            'map_resolvers': 
                                {'10.166.13.13': 
                                    {'map_resolver': '10.166.13.13'},
                                '10.64.4.4': 
                                    {'map_resolver': '10.64.4.4'}},
                            'max_smr_per_map_cache_entry': '8 more specifics',
                            'multiple_smr_suppression_time': 20,
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
                            {'map_cache_activity_check_period': 60,
                            'map_cache_fib_updates': 'established',
                            'map_cache_limit': 1000},
                        'map_resolver': 
                            {'enabled': False},
                        'map_server': 
                            {'enabled': False},
                        'mobility_first_hop_router': False,
                        'nat_traversal_router': False,
                        'service': 'ipv4'}}}}}

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
          ITR Map-Resolver(s):                 10.64.4.4, 10.166.13.13
          ETR Map-Server(s):                   10.64.4.4 (17:49:58), 10.166.13.13 (00:00:35)
          xTR-ID:                              0x730E0861-0x12996F6D-0xEFEA2114-0xE1C951F7
          site-ID:                             unspecified
          ITR local RLOC (last resort):        10.16.2.2
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
                        {'delegated_database_tree': False,
                        'etr': 
                            {'accept_mapping_data': 'disabled, verify disabled',
                            'enabled': True,
                            'encapsulation': 'lisp',
                            'map_cache_ttl': '1d00h',
                            'use_petrs':
                                {'10.10.10.10':
                                    {'use_petr': '10.10.10.10',
                                    },
                                },
                            'mapping_servers': 
                                {'10.166.13.13': 
                                    {'ms_address': '10.166.13.13',
                                    'uptime': '00:00:35'},
                                '10.64.4.4': 
                                    {'ms_address': '10.64.4.4',
                                    'uptime': '17:49:58'}},
                            'proxy_etr_router': False},
                        'instance_id': 
                            {'101': 
                                {'database': 
                                    {'dynamic_database_limit': 65535,
                                    'dynamic_database_size': 0,
                                    'inactive_deconfig_away_size': 0,
                                    'route_import_database_limit': 1000,
                                    'route_import_database_size': 0,
                                    'static_database_limit': 65535,
                                    'static_database_size': 1,
                                    'total_database_mapping_size': 1},
                                'eid_table': 'vrf red',
                                'itr': 
                                    {'local_rloc_last_resort': '10.16.2.2',
                                    'use_proxy_etr_rloc': '10.10.10.10'},
                                'map_cache': 
                                    {'imported_route_count': 0,
                                    'imported_route_limit': 1000,
                                    'map_cache_size': 2,
                                    'persistent_map_cache': False,
                                    'static_mappings_configured': 0},
                                'map_request_source': 'derived from EID destination',
                                'mapping_servers': 
                                    {'10.166.13.13': 
                                        {'ms_address': '10.166.13.13',
                                        'uptime': '00:00:35'},
                                    '10.64.4.4': 
                                        {'ms_address': '10.64.4.4',
                                        'uptime': '17:49:58'}},
                                'site_registration_limit': 0}},
                        'itr': 
                            {'enabled': True,
                            'map_resolvers': 
                                {'10.166.13.13': 
                                    {'map_resolver': '10.166.13.13'},
                                '10.64.4.4': 
                                    {'map_resolver': '10.64.4.4'}},
                            'max_smr_per_map_cache_entry': '8 more specifics',
                            'multiple_smr_suppression_time': 20,
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
                            {'map_cache_activity_check_period': 60,
                            'map_cache_fib_updates': 'established',
                            'map_cache_limit': 1000},
                        'map_resolver': 
                            {'enabled': False},
                        'map_server': 
                            {'enabled': False},
                        'mobility_first_hop_router': False,
                        'nat_traversal_router': False,
                        'service': 'ipv6'}}}}}

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
          ITR Map-Resolver(s):                 10.64.4.4, 10.166.13.13
          ETR Map-Server(s):                   10.64.4.4 (17:49:58), 10.166.13.13 (00:00:35)
          xTR-ID:                              0x730E0861-0x12996F6D-0xEFEA2114-0xE1C951F7
          site-ID:                             unspecified
          ITR local RLOC (last resort):        10.16.2.2
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
                        {'delegated_database_tree': False,
                        'etr': 
                            {'accept_mapping_data': 'disabled, verify disabled',
                            'enabled': True,
                            'encapsulation': 'vxlan',
                            'map_cache_ttl': '1d00h',
                            'mapping_servers': 
                                {'10.94.44.44': 
                                    {'ms_address': '10.94.44.44',
                                    'uptime': '00:00:50'},
                                '10.84.66.66': 
                                    {'ms_address': '10.84.66.66',
                                    'uptime': 'never'}},
                            'proxy_etr_router': False},
                        'instance_id': 
                            {'1': 
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
                                'eid_table': 'Vlan 101',
                                'itr': 
                                    {'local_rloc_last_resort': '10.229.11.1'},
                                'map_cache': 
                                    {'imported_route_count': 0,
                                    'imported_route_limit': 5000,
                                    'map_cache_size': 4,
                                    'persistent_map_cache': False,
                                    'static_mappings_configured': 0},
                                'map_request_source': 'derived from EID destination',
                                'mapping_servers': 
                                    {'10.94.44.44': 
                                        {'ms_address': '10.94.44.44',
                                        'uptime': '00:00:45'},
                                    '10.84.66.66': 
                                        {'ms_address': '10.84.66.66',
                                        'uptime': 'never'}},
                                'site_registration_limit': 0},
                            '2': 
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
                                'eid_table': 'Vlan 102',
                                'itr': 
                                    {'local_rloc_last_resort': '10.229.11.1'},
                                'map_cache': 
                                    {'imported_route_count': 0,
                                    'imported_route_limit': 5000,
                                    'map_cache_size': 0,
                                    'persistent_map_cache': False,
                                    'static_mappings_configured': 0},
                                'map_request_source': 'derived from EID destination',
                                'mapping_servers': 
                                    {'10.94.44.44': 
                                        {'ms_address': '10.94.44.44',
                                        'uptime': '00:00:50'},
                                    '10.84.66.66': 
                                        {'ms_address': '10.84.66.66',
                                        'uptime': 'never'}},
                                'site_registration_limit': 0}},
                        'itr': 
                            {'enabled': True,
                            'map_resolvers': 
                                {'10.94.44.44': 
                                    {'map_resolver': '10.94.44.44'},
                                '10.84.66.66': 
                                    {'map_resolver': '10.84.66.66'}},
                            'max_smr_per_map_cache_entry': '8 more specifics',
                            'multiple_smr_suppression_time': 20,
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
                            {'map_cache_activity_check_period': 60,
                            'map_cache_fib_updates': 'established',
                            'map_cache_limit': 5120},
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
                                    {'address': '10.229.11.1',
                                    'interface': 'Loopback0'},
                                'vlan101': 
                                    {'address': '10.229.11.1',
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
          ITR Map-Resolver(s):                 10.94.44.44
                                               10.84.66.66 *** not reachable ***
          ETR Map-Server(s):                   10.94.44.44 (00:00:45)
                                               10.84.66.66 (never)
          xTR-ID:                              0xA5EABB49-0x6C6CE939-0x530E699E-0x09187DFC
          site-ID:                             unspecified
          ITR local RLOC (last resort):        10.229.11.1
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
            Vlan100: 10.229.11.1 (Loopback0)
            Vlan101: 10.229.11.1 (Loopback0)
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
          ITR Map-Resolver(s):                 10.94.44.44
                                               10.84.66.66 *** not reachable ***
          ETR Map-Server(s):                   10.94.44.44 (00:00:50)
                                               10.84.66.66 (never)
          xTR-ID:                              0xA5EABB49-0x6C6CE939-0x530E699E-0x09187DFC
          site-ID:                             unspecified
          ITR local RLOC (last resort):        10.229.11.1
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
            Vlan100: 10.229.11.1 (Loopback0)
            Vlan101: 10.229.11.1 (Loopback0)
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
                    {'ipv4': 
                        {'delegated_database_tree': False,
                        'etr': 
                            {'accept_mapping_data': 'disabled, verify disabled',
                            'enabled': True,
                            'map_cache_ttl': '1d00h',
                            'mapping_servers': 
                                {'10.166.13.13': 
                                    {'ms_address': '10.166.13.13'},
                                '10.64.4.4': 
                                    {'ms_address': '10.64.4.4'}},
                            'proxy_etr_router': False},
                        'instance_id': 
                            {'*': 
                                {'database': 
                                    {'dynamic_database_mapping_limit': 1000},
                                'itr': 
                                    {'local_rloc_last_resort': '*** NOT FOUND ***'},
                                'map_cache': 
                                    {'persistent_map_cache': False},
                                'mapping_servers': 
                                    {'10.166.13.13': 
                                        {'ms_address': '10.166.13.13'},
                                    '10.64.4.4': 
                                        {'ms_address': '10.64.4.4'}}}},
                        'itr': 
                            {'enabled': True,
                            'map_resolvers': 
                                {'10.166.13.13': 
                                    {'map_resolver': '10.166.13.13'},
                                '10.64.4.4': 
                                    {'map_resolver': '10.64.4.4'}},
                            'max_smr_per_map_cache_entry': '8 more specifics',
                            'multiple_smr_suppression_time': 20,
                            'proxy_itr_router': True,
                            'proxy_itrs': 
                                {'10.10.10.10': 
                                    {'proxy_etr_address': '10.10.10.10'}},
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
                            {'map_cache_activity_check_period': 60,
                            'map_cache_limit': 1000},
                        'map_resolver': 
                            {'enabled': False},
                        'map_server': 
                            {'enabled': False},
                        'mobility_first_hop_router': False,
                        'nat_traversal_router': False,
                        'service': 'ipv4'}}}}}

    golden_output4 =  {'execute.return_value': '''
        202-XTR#show lisp all service ipv4
        =================================================
        Output for router lisp 0
        =================================================
          Router-lisp ID:                      0
          Locator table:                       default
          Ingress Tunnel Router (ITR):         enabled
          Egress Tunnel Router (ETR):          enabled
          Proxy-ITR Router (PITR):             enabled RLOCs: 10.10.10.10
          Proxy-ETR Router (PETR):             disabled
          NAT-traversal Router (NAT-RTR):      disabled
          Mobility First-Hop Router:           disabled
          Map Server (MS):                     disabled
          Map Resolver (MR):                   disabled
          Delegated Database Tree (DDT):       disabled
          ITR Map-Resolver(s):                 10.64.4.4, 10.166.13.13
          ETR Map-Server(s):                   10.64.4.4, 10.166.13.13
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
                    {'ipv6': 
                        {'delegated_database_tree': False,
                        'etr': 
                            {'accept_mapping_data': 'disabled, verify disabled',
                            'enabled': True,
                            'map_cache_ttl': '1d00h',
                            'mapping_servers': 
                                {'10.166.13.13': 
                                    {'ms_address': '10.166.13.13'},
                                '10.64.4.4': 
                                    {'ms_address': '10.64.4.4'}},
                            'proxy_etr_router': False},
                        'instance_id': 
                            {'*': 
                                {'database': 
                                    {'dynamic_database_mapping_limit': 1000},
                                'itr': 
                                    {'local_rloc_last_resort': '*** NOT FOUND ***'},
                                'map_cache': 
                                    {'persistent_map_cache': False},
                                'mapping_servers': 
                                    {'10.166.13.13': 
                                        {'ms_address': '10.166.13.13'},
                                    '10.64.4.4': 
                                        {'ms_address': '10.64.4.4'}}}},
                        'itr': 
                            {'enabled': True,
                            'map_resolvers': 
                                {'10.166.13.13': 
                                    {'map_resolver': '10.166.13.13'},
                                '10.64.4.4': 
                                    {'map_resolver': '10.64.4.4'}},
                            'max_smr_per_map_cache_entry': '8 more specifics',
                            'multiple_smr_suppression_time': 20,
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
                            {'map_cache_activity_check_period': 60,
                            'map_cache_limit': 1000},
                        'map_resolver': 
                            {'enabled': False},
                        'map_server': 
                            {'enabled': False},
                        'mobility_first_hop_router': False,
                        'nat_traversal_router': False,
                        'service': 'ipv6'}}}}}

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
          ITR Map-Resolver(s):                 10.64.4.4, 10.166.13.13
          ETR Map-Server(s):                   10.64.4.4, 10.166.13.13
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
                        {'delegated_database_tree': False,
                        'etr': 
                            {'accept_mapping_data': 'disabled, verify disabled',
                            'enabled': True,
                            'map_cache_ttl': '1d00h',
                            'mapping_servers': 
                                {'10.94.44.44': 
                                    {'ms_address': '10.94.44.44'}},
                            'proxy_etr_router': False},
                        'instance_id': 
                            {'*': 
                                {'database': 
                                    {'dynamic_database_mapping_limit': 5120},
                                'itr': 
                                    {'local_rloc_last_resort': '*** NOT FOUND ***'},
                                'map_cache': 
                                    {'persistent_map_cache': False},
                                'mapping_servers': 
                                    {'10.94.44.44': 
                                        {'ms_address': '10.94.44.44'}}}},
                        'itr': 
                            {'enabled': True,
                            'map_resolvers': 
                                {'10.94.44.44': 
                                    {'map_resolver': '10.94.44.44'},
                                '10.84.66.66': 
                                    {'map_resolver': '10.84.66.66'}},
                            'max_smr_per_map_cache_entry': '8 more specifics',
                            'multiple_smr_suppression_time': 20,
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
                            {'map_cache_activity_check_period': 60,
                            'map_cache_limit': 5120},
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
                                    {'address': '10.229.11.1',
                                    'interface': 'Loopback0'},
                                'vlan101': 
                                    {'address': '10.229.11.1',
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
          ITR Map-Resolver(s):                 10.94.44.44
                                               10.84.66.66
          ETR Map-Server(s):                   10.94.44.44
                                               10.84.66.66
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
            Vlan100: 10.229.11.1 (Loopback0)
            Vlan101: 10.229.11.1 (Loopback0)
          Database:
            Dynamic database mapping limit:    5120
        '''}

    def test_show_lisp_service_full1(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output1)
        obj = ShowLispService(device=self.device)
        parsed_output = obj.parse(instance_id=101, service='ipv4')
        self.assertEqual(parsed_output, self.golden_parsed_output1)

    def test_show_lisp_service_full2(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output2)
        obj = ShowLispService(device=self.device)
        parsed_output = obj.parse(instance_id=101, service='ipv6')
        self.assertEqual(parsed_output, self.golden_parsed_output2)

    def test_show_lisp_service_full3(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output3)
        obj = ShowLispService(device=self.device)
        parsed_output = obj.parse(instance_id='*', service='ethernet')
        self.assertEqual(parsed_output, self.golden_parsed_output3)

    def test_show_lisp_service_full4(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output4)
        obj = ShowLispService(device=self.device)
        parsed_output = obj.parse(instance_id='*', service='ipv4')
        self.assertEqual(parsed_output, self.golden_parsed_output4)

    def test_show_lisp_service_full5(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output5)
        obj = ShowLispService(device=self.device)
        parsed_output = obj.parse(instance_id='*', service='ipv6')
        self.assertEqual(parsed_output, self.golden_parsed_output5)

    def test_show_lisp_service_full6(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output6)
        obj = ShowLispService(device=self.device)
        parsed_output = obj.parse(instance_id='*', service='ethernet')
        self.assertEqual(parsed_output, self.golden_parsed_output6)

    def test_show_lisp_service_empty(self):
        self.maxDiff = None
        self.device = Mock(**self.empty_output)
        obj = ShowLispService(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse(instance_id='*', service='ipv4')


# ===========================================================================
# Unit test for 'show lisp all instance-id <instance_id> <service> map-cache'
# ===========================================================================
class test_show_lisp_service_map_cache(unittest.TestCase):

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
                                    'entries': 2,
                                    'mappings': 
                                        {'0.0.0.0/0': 
                                            {'id': '0.0.0.0/0',
                                            'creation_time': '15:23:50',
                                            'time_to_live': 'never',
                                            'via': 'static-send-map-request',
                                            'eid': 
                                                {'address_type': 'ipv4-afi',
                                                'vrf': 'red',
                                                'ipv4': 
                                                    {'ipv4': '0.0.0.0/0'}},
                                            'negative_mapping': {'map_reply_action': 'send-map-request'}},
                                        '192.168.9.0/24': 
                                            {'id': '192.168.9.0/24',
                                            'creation_time': '00:04:02',
                                            'time_to_live': '23:55:57',
                                            'via': 'map-reply, complete',
                                            'eid': 
                                                {'address_type': 'ipv4-afi',
                                                'vrf': 'red',
                                                'ipv4': 
                                                    {'ipv4': '192.168.9.0/24'}},
                                            'positive_mapping': 
                                                {'rlocs': 
                                                    {1: 
                                                        {'id': '1',
                                                        'encap_iid': '-',
                                                        'priority': 50,
                                                        'state': 'up',
                                                        'uptime': '00:04:02',
                                                        'weight': 50,
                                                        'locator_address': 
                                                            {'address_type': 'ipv4-afi',
                                                            'virtual_network_id': '101',
                                                            'ipv4': 
                                                                {'ipv4': '10.1.8.8'}}}}}}}}}}}}}}}

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
          10.1.8.8 00:04:02  up          50/50        -
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
                                    'mappings': 
                                        {'172.16.10.0/24': 
                                            {'eid': 
                                                {'address_type': 'ipv4-afi',
                                                'ipv4': 
                                                    {'ipv4': '172.16.10.0/24'},
                                                'vrf': 'red'},
                                            'time_to_live': '23:59:59',
                                            'id': '172.16.10.0/24',
                                            'positive_mapping': 
                                                {'rlocs': 
                                                    {1: 
                                                        {'id': '1',
                                                        'priority': 1,
                                                        'state': 'up',
                                                        'uptime': '00:00:00',
                                                        'weight': 50,
                                                        'locator_address': 
                                                            {'address_type': 'ipv4-afi',
                                                            'ipv4': 
                                                                {'ipv4': '172.16.156.134'},
                                                            'virtual_network_id': '101'}},
                                                    2: 
                                                        {'id': '2',
                                                        'priority': 1,
                                                        'state': 'up',
                                                        'uptime': '00:00:00',
                                                        'weight': 50,
                                                        'locator_address': 
                                                            {'address_type': 'ipv4-afi',
                                                            'ipv4': 
                                                                {'ipv4': '192.168.65.94'},
                                                            'virtual_network_id': '101'}},
                                                    3: 
                                                        {'id': '3',
                                                        'priority': 2,
                                                        'state': 'up',
                                                        'uptime': '00:00:00',
                                                        'weight': 100,
                                                        'locator_address': 
                                                            {'address_type': 'ipv6-afi',
                                                            'ipv6': 
                                                                {'ipv6': '2001:DB8:BBED:2829::80DF:9C86'},
                                                            'virtual_network_id': '101'}}}},
                                            'creation_time': '00:00:00',
                                            'via': 'map-reply, complete'},
                                        '2001:192:168:9::/64': 
                                            {'eid': 
                                                {'address_type': 'ipv6-afi',
                                                'ipv6': 
                                                    {'ipv6': '2001:192:168:9::/64'},
                                                'vrf': 'red'},
                                            'time_to_live': '23:53:08',
                                            'id': '2001:192:168:9::/64',
                                            'positive_mapping': 
                                                {'rlocs': 
                                                    {1: 
                                                        {'id': '1',
                                                        'encap_iid': '-',
                                                        'priority': 50,
                                                        'state': 'up',
                                                        'uptime': '00:06:51',
                                                        'weight': 50,
                                                        'locator_address': 
                                                            {'address_type': 'ipv4-afi',
                                                            'ipv4': 
                                                                {'ipv4': '10.1.8.8'},
                                                            'virtual_network_id': '101'}}}},
                                            'creation_time': '00:06:51',
                                            'via': 'map-reply, complete'},
                                        '::/0': 
                                            {'eid': 
                                                {'address_type': 'ipv6-afi',
                                                'ipv6': 
                                                    {'ipv6': '::/0'},
                                                'vrf': 'red'},
                                            'time_to_live': 'never',
                                            'id': '::/0',
                                            'negative_mapping': 
                                                {'map_reply_action': 'send-map-request'},
                                            'creation_time': '00:11:28',
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
          10.1.8.8 00:06:51  up          50/50        -
        172.16.10.0/24, uptime: 00:00:00, expires: 23:59:59, via map-reply, complete
          Locator                     Uptime    State      Pri/Wgt
          172.16.156.134              00:00:00  up           1/50
          192.168.65.94               00:00:00  up           1/50
          2001:DB8:BBED:2829::80DF:9C86  00:00:00  up           2/100
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
                                    'mappings': 
                                        {'b827.eb51.f5ce/48': 
                                            {'eid': 
                                                {'address_type': 'ipv4-afi',
                                                'ipv4': 
                                                    {'ipv4': 'b827.eb51.f5ce/48'},
                                                'vrf': '101'},
                                            'time_to_live': '01:10:17',
                                            'id': 'b827.eb51.f5ce/48',
                                            'positive_mapping': 
                                                {'rlocs': 
                                                    {1: 
                                                        {'id': '1',
                                                        'priority': 0,
                                                        'state': 'up',
                                                        'uptime': '22:49:42',
                                                        'encap_iid': '-',
                                                        'weight': 0,
                                                        'locator_address': 
                                                            {'address_type': 'ipv4-afi',
                                                            'ipv4': 
                                                                {'ipv4': '10.151.22.1'},
                                                            'virtual_network_id': '193'}}}},
                                            'creation_time': '22:49:42',
                                            'via': 'WLC Map-Notify, complete'},
                                        'b827.eb73.159c/48': 
                                            {'eid': 
                                                {'address_type': 'ipv4-afi',
                                                'ipv4': 
                                                    {'ipv4': 'b827.eb73.159c/48'},
                                                'vrf': '101'},
                                            'time_to_live': '08:57:24',
                                            'id': 'b827.eb73.159c/48',
                                            'positive_mapping': 
                                                {'rlocs': 
                                                    {1: 
                                                        {'id': '1',
                                                        'encap_iid': '-',
                                                        'priority': 0,
                                                        'state': 'up',
                                                        'uptime': '15:02:35',
                                                        'weight': 0,
                                                        'locator_address': 
                                                            {'address_type': 'ipv4-afi',
                                                            'ipv4': 
                                                                {'ipv4': '10.151.22.1'},
                                                            'virtual_network_id': '193',
                                                            }}}},
                                            'creation_time': '15:02:35',
                                            'via': 'WLC Map-Notify, complete'},
                                        'b827.ebd0.acc6/48': 
                                            {'eid': 
                                                {'address_type': 'ipv4-afi',
                                                'ipv4': 
                                                    {'ipv4': 'b827.ebd0.acc6/48'},
                                                'vrf': '101'},
                                            'time_to_live': '08:57:25',
                                            'id': 'b827.ebd0.acc6/48',
                                            'positive_mapping': 
                                                {'rlocs': 
                                                    {1: 
                                                        {'id': '1',
                                                        'encap_iid': '-',
                                                        'priority': 0,
                                                        'state': 'up',
                                                        'uptime': '15:02:34',
                                                        'weight': 0,
                                                        'locator_address': 
                                                            {'address_type': 'ipv4-afi',
                                                            'ipv4': 
                                                                {'ipv4': '10.151.22.1'},
                                                            'virtual_network_id': '193'}}}},
                                            'creation_time': '15:02:34',
                                            'via': 'WLC Map-Notify, complete'},
                                        'b827.ebd6.0c63/48': 
                                            {'eid': 
                                                {'address_type': 'ipv4-afi',
                                                'ipv4': 
                                                    {'ipv4': 'b827.ebd6.0c63/48'},
                                                'vrf': '101'},
                                            'time_to_live': '09:02:44',
                                            'id': 'b827.ebd6.0c63/48',
                                            'positive_mapping': 
                                                {'rlocs': 
                                                    {1: 
                                                        {'id': '1',
                                                        'encap_iid': '-',
                                                        'priority': 0,
                                                        'state': 'up',
                                                        'uptime': '14:57:15',
                                                        'weight': 0,
                                                        'locator_address': 
                                                            {'address_type': 'ipv4-afi',
                                                            'ipv4': 
                                                                {'ipv4': '10.151.22.1'},
                                                            'virtual_network_id': '193'}}}},
                                            'creation_time': '14:57:15',
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
          10.151.22.1 22:49:42  up           0/0         -
        b827.eb73.159c/48, uptime: 15:02:35, expires: 08:57:24, via WLC Map-Notify, complete
          Locator     Uptime    State      Pri/Wgt     Encap-IID
          10.151.22.1 15:02:35  up           0/0         -
        b827.ebd0.acc6/48, uptime: 15:02:34, expires: 08:57:25, via WLC Map-Notify, complete
          Locator     Uptime    State      Pri/Wgt     Encap-IID
          10.151.22.1 15:02:34  up           0/0         -
        b827.ebd6.0c63/48, uptime: 14:57:15, expires: 09:02:44, via WLC Map-Notify, complete
          Locator     Uptime    State      Pri/Wgt     Encap-IID
          10.151.22.1 14:57:15  up           0/0         -

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

    def test_show_lisp_service_map_cache_full1(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output1)
        obj = ShowLispServiceMapCache(device=self.device)
        parsed_output = obj.parse(instance_id=101, service='ipv4')
        self.assertEqual(parsed_output, self.golden_parsed_output1)

    def test_show_lisp_service_map_cache_full2(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output2)
        obj = ShowLispServiceMapCache(device=self.device)
        parsed_output = obj.parse(instance_id=101, service='ipv6')
        self.assertEqual(parsed_output, self.golden_parsed_output2)

    def test_show_lisp_service_map_cache_full3(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output3)
        obj = ShowLispServiceMapCache(device=self.device)
        parsed_output = obj.parse(instance_id='*', service='ethernet')
        self.assertEqual(parsed_output, self.golden_parsed_output3)

    def test_show_lisp_service_map_cache_empty(self):
        self.maxDiff = None
        self.device = Mock(**self.empty_output)
        obj = ShowLispServiceMapCache(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse(instance_id='*', service='ipv4')


# ==============================================================================
# Unit test for 'show lisp all instance-id <instance_id> <service> rloc members'
# ==============================================================================
class test_show_lisp_service_rloc_members(unittest.TestCase):

    '''Unit test for "show lisp all instance-id <instance_id> <service> rloc members"'''

    device = Device(name='aDevice')

    empty_output = {'execute.return_value': ''}

    golden_parsed_output1 = {
        'lisp_router_instances': 
            {0: 
                {'lisp_router_instance_id': 0,
                'service': 
                    {'ipv4': 
                        {'instance_id':
                            {'101':
                                {'rloc': 
                                    {'distribution': False,
                                    'total_entries': 2,
                                    'valid_entries': 2,
                                    'members': 
                                        {'10.16.2.2': 
                                            {'origin': 'registration',
                                            'valid': 'yes'},
                                        '10.1.8.8': 
                                            {'origin': 'registration',
                                            'valid': 'yes'}}}}}}}}}}

    golden_output1 = {'execute.return_value': '''
        204-MSMR#show lisp all instance-id 101 ipv4 server rloc members 

        =====================================================
        Output for router lisp 0
        =====================================================
        LISP RLOC Membership for router lisp 0 IID 101
        Entries: 2 valid / 2 total, Distribution disabled

        RLOC                                    Origin                       Valid
        10.16.2.2                               Registration                 Yes
        10.1.8.8                                Registration                 Yes
        '''}

    golden_parsed_output2 = {
        'lisp_router_instances': 
            {0: 
                {'lisp_router_instance_id': 0,
                'service': 
                    {'ipv6': 
                        {'instance_id':
                            {'101':
                                {'rloc': 
                                    {'distribution': False,
                                    'total_entries': 2,
                                    'valid_entries': 2,
                                    'members': 
                                        {'10.16.2.2': 
                                            {'origin': 'registration',
                                            'valid': 'yes'},
                                        '10.1.8.8': 
                                            {'origin': 'registration',
                                            'valid': 'yes'}}}}}}}}}}

    golden_output2 = {'execute.return_value': '''
        04-MSMR#show lisp all instance-id 101 ipv6 server rloc members 

        =====================================================
        Output for router lisp 0
        =====================================================
        LISP RLOC Membership for router lisp 0 IID 101
        Entries: 2 valid / 2 total, Distribution disabled

        RLOC                                    Origin                       Valid
        10.16.2.2                               Registration                 Yes
        10.1.8.8                                Registration                 Yes
        '''}

    golden_parsed_output3 = {
        'lisp_router_instances': 
            {2: 
                {'lisp_router_instance_id': 2,
                'service': 
                    {'ethernet': 
                        {'instance_id': 
                            {'101': {},
                            '102': {},
                            '103': {},
                            '104': {},
                            '107': {},
                            '108': {},
                            '109': {}}}}}}}

    golden_output3 = {'execute.return_value': '''
        OTT-LISP-C9K-20-MSMR#show lisp all instance-id * ethernet server rloc members

        =================================================
        Output for router lisp 2 instance-id 101
        =================================================
        % EID table not enabled for MAC.

        =================================================
        Output for router lisp 2 instance-id 102
        =================================================
        % EID table not enabled for MAC.

        =================================================
        Output for router lisp 2 instance-id 103
        =================================================
        % EID table not enabled for MAC.

        =================================================
        Output for router lisp 2 instance-id 104
        =================================================
        % EID table not enabled for MAC.

        =================================================
        Output for router lisp 2 instance-id 107
        =================================================
        % EID table not enabled for MAC.

        =================================================
        Output for router lisp 2 instance-id 108
        =================================================
        % EID table not enabled for MAC.

        =================================================
        Output for router lisp 2 instance-id 109
        =================================================
        % EID table not enabled for MAC.

        '''}

    def test_show_lisp_service_rloc_members_full1(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output1)
        obj = ShowLispServiceRlocMembers(device=self.device)
        parsed_output = obj.parse(instance_id=101, service='ipv4')
        self.assertEqual(parsed_output, self.golden_parsed_output1)

    def test_show_lisp_service_rloc_members_full2(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output2)
        obj = ShowLispServiceRlocMembers(device=self.device)
        parsed_output = obj.parse(instance_id=101, service='ipv6')
        self.assertEqual(parsed_output, self.golden_parsed_output2)

    def test_show_lisp_service_rloc_members_full3(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output3)
        obj = ShowLispServiceRlocMembers(device=self.device)
        parsed_output = obj.parse(instance_id='*', service='ethernet')
        self.assertEqual(parsed_output, self.golden_parsed_output3)

    def test_show_lisp_service_rloc_members_empty(self):
        self.maxDiff = None
        self.device = Mock(**self.empty_output)
        obj = ShowLispServiceRlocMembers(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse(instance_id='*', service='ipv4')


# =====================================================================
# Unit test for 'show lisp all instance-id <instance_id> <service> smr'
# =====================================================================
class test_show_lisp_service_smr(unittest.TestCase):

    '''Unit test for "show lisp all instance-id <instance_id> <service> smr"'''

    device = Device(name='aDevice')

    empty_output = {'execute.return_value': ''}

    golden_parsed_output1 = {
        'lisp_router_instances': 
            {0: 
                {'lisp_router_instance_id': 0,
                'service': 
                    {'ipv4': 
                        {'instance_id': 
                            {'101': 
                                {'smr': 
                                    {'entries': 1,
                                    'prefixes': 
                                        {'192.168.0.0/24': 
                                            {'producer': 'local EID'}},
                                    'vrf': 'red'}}}}}}}}

    golden_output1 = {'execute.return_value': '''
        202-XTR#show lisp all instance-id 101 ipv4 smr
        =====================================================
        Output for router lisp 0
        =====================================================
        LISP SMR Table for router lisp 0 (red) IID 101
        Entries: 1

        Prefix                                  Producer
        192.168.0.0/24                          local EID
        '''}

    golden_parsed_output2 = {
        'lisp_router_instances': 
            {0: 
                {'lisp_router_instance_id': 0,
                'service': 
                    {'ipv6': 
                        {'instance_id': 
                            {'101': 
                                {'smr': 
                                    {'entries': 1,
                                    'prefixes': 
                                        {'2001:192:168::/64': 
                                            {'producer': 'local EID'}},
                                    'vrf': 'red'}}}}}}}}

    golden_output2 = {'execute.return_value': '''
        202-XTR#show lisp all instance-id 101 ipv6 smr
        =====================================================
        Output for router lisp 0
        =====================================================
        LISP SMR Table for router lisp 0 (red) IID 101
        Entries: 1

        Prefix                                  Producer
        2001:192:168::/64                       local EID
        '''}

    def test_show_lisp_service_smr_full1(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output1)
        obj = ShowLispServiceSmr(device=self.device)
        parsed_output = obj.parse(instance_id=101, service='ipv4')
        self.assertEqual(parsed_output, self.golden_parsed_output1)

    def test_show_lisp_service_smr_full2(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output2)
        obj = ShowLispServiceSmr(device=self.device)
        parsed_output = obj.parse(instance_id=101, service='ipv6')
        self.assertEqual(parsed_output, self.golden_parsed_output2)

    def test_show_lisp_service_smr_empty(self):
        self.maxDiff = None
        self.device = Mock(**self.empty_output)
        obj = ShowLispServiceSmr(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse(instance_id='*', service='ipv4')


# =======================================================
# Unit test for 'show lisp all service <service> summary'
# =======================================================
class test_show_lisp_service_summary(unittest.TestCase):

    '''Unit test for "show lisp all service <service> summary"'''

    device = Device(name='aDevice')

    empty_output = {'execute.return_value': ''}

    golden_parsed_output1 = {
        'lisp_router_instances': 
            {0: 
                {'lisp_router_instance_id': 0,
                'service': 
                    {'ipv4': 
                        {'virtual_network_ids':
                            {'102':
                                {'cache_idle': '0%',
                                'cache_size': 1,
                                'db_no_route': 0,
                                'db_size': 1,
                                'incomplete': '0.0%',
                                'vrf': 'blue',
                                'interface': 'LISP0.102',
                                'lisp_role':
                                    {'itr-etr':
                                        {'lisp_role_type': 'itr-etr',
                                        },
                                    },
                                },
                            '101':
                                {'cache_idle': '0.0%',
                                'cache_size': 2,
                                'db_no_route': 0,
                                'db_size': 1,
                                'incomplete': '0.0%',
                                'vrf': 'red',
                                'interface': 'LISP0.101',
                                'lisp_role':
                                    {'itr-etr':
                                        {'lisp_role_type': 'itr-etr',
                                        },
                                    },
                                },
                            },
                        'etr':
                            {'summary': 
                                {'eid_tables_incomplete_map_cache_entries': 0,
                                'eid_tables_inconsistent_locators': 0,
                                'eid_tables_pending_map_cache_update_to_fib': 0,
                                'instance_count': 2,
                                'total_db_entries': 2,
                                'total_db_entries_inactive': 0,
                                'total_eid_tables': 2,
                                'total_map_cache_entries': 3}}}}}}}

    golden_output1 = {'execute.return_value': '''
        202-XTR#show lisp all service ipv4 summary 

        =====================================================
        Output for router lisp 0
        =====================================================
        Router-lisp ID:   0
        Instance count:   2
        Key: DB - Local EID Database entry count (@ - RLOC check pending
                                                  * - RLOC consistency problem),
             DB no route - Local EID DB entries with no matching RIB route,
             Cache - Remote EID mapping cache size, IID - Instance ID,
             Role - Configured Role

                              Interface    DB  DB no  Cache Incom Cache 
        EID VRF name             (.IID)  size  route   size plete  Idle Role
        red                   LISP0.101     1      0      2  0.0%  0.0% ITR-ETR
        blue                  LISP0.102     1      0      1  0.0%    0% ITR-ETR

        Number of eid-tables:                                 2
        Total number of database entries:                     2 (inactive 0)
        EID-tables with inconsistent locators:                0
        Total number of map-cache entries:                    3
        EID-tables with incomplete map-cache entries:         0
        EID-tables pending map-cache update to FIB:           0
        '''}

    golden_parsed_output2 = {
        'lisp_router_instances': 
            {0:
                {'lisp_router_instance_id': 0,
                'service': 
                    {'ipv6': 
                        {'virtual_network_ids':
                            {'101':
                                {'cache_idle': '0.0%',
                                'cache_size': 2,
                                'db_no_route': 0,
                                'db_size': 1,
                                'incomplete': '0.0%',
                                'vrf': 'red',
                                'interface': 'LISP0.101',
                                'lisp_role':
                                    {'itr-etr':
                                        {'lisp_role_type': 'itr-etr',
                                        },
                                    },
                                },
                            },
                        'etr':
                            {'summary': 
                                {'eid_tables_incomplete_map_cache_entries': 0,
                                'eid_tables_inconsistent_locators': 0,
                                'eid_tables_pending_map_cache_update_to_fib': 0,
                                'instance_count': 2,
                                'total_db_entries': 1,
                                'total_db_entries_inactive': 0,
                                'total_eid_tables': 1,
                                'total_map_cache_entries': 2}}}}}}}

    golden_output2 = {'execute.return_value': '''
        202-XTR#show lisp all service ipv6 summary 
        =====================================================
        Output for router lisp 0
        =====================================================
        Router-lisp ID:   0
        Instance count:   2
        Key: DB - Local EID Database entry count (@ - RLOC check pending
                                                  * - RLOC consistency problem),
             DB no route - Local EID DB entries with no matching RIB route,
             Cache - Remote EID mapping cache size, IID - Instance ID,
             Role - Configured Role

                              Interface    DB  DB no  Cache Incom Cache 
        EID VRF name             (.IID)  size  route   size plete  Idle Role
        red                   LISP0.101     1      0      2  0.0%  0.0% ITR-ETR

        Number of eid-tables:                                 1
        Total number of database entries:                     1 (inactive 0)
        EID-tables with inconsistent locators:                0
        Total number of map-cache entries:                    2
        EID-tables with incomplete map-cache entries:         0
        EID-tables pending map-cache update to FIB:           0
        '''}

    golden_parsed_output3 = {
        'lisp_router_instances': 
            {0: 
                {'lisp_router_instance_id': 0,
                'service': 
                    {'ethernet': 
                        {'virtual_network_ids':
                            {'1':
                                {'cache_idle': '100%',
                                'cache_size': 4,
                                'db_no_route': 0,
                                'db_size': 2,
                                'incomplete': '0.0%',
                                'interface': 'LISP0.1',
                                'lisp_role':
                                    {'none':
                                        {'lisp_role_type': 'none',
                                        },
                                    },
                                },
                            '2':
                                {'cache_idle': '0%',
                                'cache_size': 0,
                                'db_no_route': 0,
                                'db_size': 2,
                                'incomplete': '0%',
                                'interface': 'LISP0.2',
                                'lisp_role':
                                    {'none':
                                        {'lisp_role_type': 'none',
                                        },
                                    },
                                },
                            },
                        'etr':
                            {'summary': 
                                {'eid_tables_incomplete_map_cache_entries': 0,
                                'eid_tables_inconsistent_locators': 0,
                                'eid_tables_pending_map_cache_update_to_fib': 0,
                                'instance_count': 69,
                                'total_db_entries': 4,
                                'total_db_entries_inactive': 0,
                                'total_eid_tables': 2,
                                'total_map_cache_entries': 4}}}}}}}

    golden_output3 = {'execute.return_value': '''
        OTT-LISP-C3K-3-xTR1#show lisp all service ethernet summary
        =================================================
        Output for router lisp 0
        =================================================
        Router-lisp ID:   0
        Instance count:   69
        Key: DB - Local EID Database entry count (@ - RLOC check pending
                                                  * - RLOC consistency problem),
             DB no route - Local EID DB entries with no matching RIB route,
             Cache - Remote EID mapping cache size, IID - Instance ID,
             Role - Configured Role

                              Interface    DB  DB no  Cache Incom Cache
        EID VRF name             (.IID)  size  route   size plete  Idle Role
                                LISP0.1     2      0      4  0.0%  100% NONE
                                LISP0.2     2      0      0    0%    0% NONE

        Number of eid-tables:                                 2
        Total number of database entries:                     4 (inactive 0)
        Maximum database entries:                          5120
        EID-tables with inconsistent locators:                0
        Total number of map-cache entries:                    4
        Maximum map-cache entries:                         5120
        EID-tables with incomplete map-cache entries:         0
        EID-tables pending map-cache update to FIB:           0
        '''}

    def test_show_lisp_service_summary_full1(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output1)
        obj = ShowLispServiceSummary(device=self.device)
        parsed_output = obj.parse(service='ipv4')
        self.assertEqual(parsed_output, self.golden_parsed_output1)

    def test_show_lisp_service_summary_full2(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output2)
        obj = ShowLispServiceSummary(device=self.device)
        parsed_output = obj.parse(service='ipv6')
        self.assertEqual(parsed_output, self.golden_parsed_output2)

    def test_show_lisp_service_summary_full3(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output3)
        obj = ShowLispServiceSummary(device=self.device)
        parsed_output = obj.parse(service='ethernet')
        self.assertEqual(parsed_output, self.golden_parsed_output3)

    def test_show_lisp_service_summary_empty(self):
        self.maxDiff = None
        self.device = Mock(**self.empty_output)
        obj = ShowLispServiceSummary(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse(service='ipv4')


# ==========================================================================
# Unit test for 'show lisp all instance-id <instance_id> <service> dabatase'
# ==========================================================================
class test_show_lisp_service_database(unittest.TestCase):

    '''Unit test for "show lisp all instance-id <instance_id> <service> dabatase"'''

    device = Device(name='aDevice')

    empty_output = {'execute.return_value': ''}

    golden_parsed_output1 = {
        'lisp_router_instances': 
            {0: 
                {'lisp_router_instance_id': 0,
                'locator_sets': 
                    {'RLOC': 
                        {'locator_set_name': 'RLOC'}},
                'service': 
                    {'ipv4': 
                        {'etr': 
                            {'local_eids': 
                                {'101': 
                                    {'vni': '101',
                                    'total_eid_entries': 1,
                                    'no_route_eid_entries': 0,
                                    'inactive_eid_entries': 0,
                                    'eids': 
                                        {'192.168.0.0/24': 
                                            {'eid_address': 
                                                {'address_type': 'ipv4',
                                                'vrf': 'red'},
                                            'id': '192.168.0.0/24',
                                            'loopback_address': '10.16.2.2',
                                            'priority': 50,
                                            'rlocs': 'RLOC',
                                            'source': 'cfg-intf',
                                            'state': 'site-self, reachable',
                                            'weight': 50}}}}}}}}}}

    golden_output1 = {'execute.return_value': '''
        202-XTR#show lisp all instance-id 101 ipv4 database  
        =====================================================
        Output for router lisp 0
        =====================================================
        LISP ETR IPv4 Mapping Database for EID-table vrf red (IID 101), LSBs: 0x1
        Entries total 1, no-route 0, inactive 0

        192.168.0.0/24, locator-set RLOC
          Locator  Pri/Wgt  Source     State
          10.16.2.2 50/50   cfg-intf   site-self, reachable
        '''}

    golden_parsed_output2 = {
        'lisp_router_instances': 
            {0: 
                {'lisp_router_instance_id': 0,
                'locator_sets': 
                    {'RLOC': 
                        {'locator_set_name': 'RLOC'}},
                'service': 
                    {'ipv6': 
                        {'etr': 
                            {'local_eids': 
                                {'101': 
                                    {'vni': '101',
                                    'total_eid_entries': 1,
                                    'no_route_eid_entries': 0,
                                    'inactive_eid_entries': 0,
                                    'eids': 
                                        {'2001:192:168::/64': 
                                            {'eid_address': 
                                                {'address_type': 'ipv6',
                                                'vrf': 'red'},
                                            'id': '2001:192:168::/64',
                                            'loopback_address': '10.16.2.2',
                                            'priority': 50,
                                            'rlocs': 'RLOC',
                                            'source': 'cfg-intf',
                                            'state': 'site-self, reachable',
                                            'weight': 50}}}}}}}}}}

    golden_output2 = {'execute.return_value': '''
        202-XTR#show lisp all instance-id 101 ipv6 database 
        =====================================================
        Output for router lisp 0
        =====================================================
        LISP ETR IPv6 Mapping Database for EID-table vrf red (IID 101), LSBs: 0x1
        Entries total 1, no-route 0, inactive 0

        2001:192:168::/64, locator-set RLOC
          Locator  Pri/Wgt  Source     State
          10.16.2.2 50/50   cfg-intf   site-self, reachable
        '''}

    golden_parsed_output3 = {
        'lisp_router_instances': 
            {0: 
                {'lisp_router_instance_id': 0,
                'locator_sets': 
                    {'RLOC': 
                        {'locator_set_name': 'RLOC'}},
                'service': 
                    {'ethernet': 
                        {'etr': 
                            {'local_eids': 
                                {'1': 
                                    {'vni': '1',
                                    'total_eid_entries': 2,
                                    'no_route_eid_entries': 0,
                                    'inactive_eid_entries': 0,
                                    'dynamic_eids': 
                                        {'0050.56b0.6a0e/48': 
                                            {'dynamic_eid': 'Auto-L2-group-1',
                                            'eid_address': 
                                                {'address_type': 'ethernet',
                                                'vrf': '101'},
                                            'id': '0050.56b0.6a0e/48',
                                            'loopback_address': '10.229.11.1',
                                            'priority': 1,
                                            'rlocs': 'RLOC',
                                            'source': 'cfg-intf',
                                            'state': 'site-self, reachable',
                                            'weight': 100},
                                      'cafe.cafe.cafe/48': 
                                        {'dynamic_eid': 'Auto-L2-group-1',
                                        'eid_address': 
                                            {'address_type': 'ethernet',
                                            'vrf': '101'},
                                        'id': 'cafe.cafe.cafe/48',
                                        'loopback_address': '10.229.11.1',
                                        'priority': 1,
                                        'rlocs': 'RLOC',
                                        'source': 'cfg-intf',
                                        'state': 'site-self, reachable',
                                        'weight': 100}}},
                                '2': 
                                    {'vni': '2',
                                    'total_eid_entries': 2,
                                    'no_route_eid_entries': 0,
                                    'inactive_eid_entries': 0,
                                    'dynamic_eids': 
                                        {'0050.56b0.60de/48': 
                                            {'dynamic_eid': 'Auto-L2-group-2',
                                            'eid_address': 
                                                {'address_type': 'ethernet',
                                                'vrf': '102'},
                                            'id': '0050.56b0.60de/48',
                                            'loopback_address': '10.229.11.1',
                                            'priority': 1,
                                            'rlocs': 'RLOC',
                                            'source': 'cfg-intf',
                                            'state': 'site-self, reachable',
                                            'weight': 100},
                                        'face.0171.0001/48': 
                                            {'dynamic_eid': 'Auto-L2-group-2',
                                            'eid_address': 
                                                {'address_type': 'ethernet',
                                                'vrf': '102'},
                                            'id': 'face.0171.0001/48',
                                            'loopback_address': '10.229.11.1',
                                            'priority': 1,
                                            'rlocs': 'RLOC',
                                            'source': 'cfg-intf',
                                            'state': 'site-self, reachable',
                                            'weight': 100}}}}}}}}}}

    golden_output3 = {'execute.return_value': '''
        OTT-LISP-C3K-3-xTR1#show lisp all instance-id * ethernet database
        =================================================
        Output for router lisp 0 instance-id 0
        =================================================
        % EID table not enabled for MAC.

        =================================================
        Output for router lisp 0 instance-id 1
        =================================================
        LISP ETR MAC Mapping Database for EID-table Vlan 101 (IID 1), LSBs: 0x1
        Entries total 2, no-route 0, inactive 0

        0050.56b0.6a0e/48, dynamic-eid Auto-L2-group-1, inherited from default locator-set RLOC
          Locator     Pri/Wgt  Source     State
          10.229.11.1   1/100  cfg-intf   site-self, reachable
        cafe.cafe.cafe/48, dynamic-eid Auto-L2-group-1, inherited from default locator-set RLOC
          Locator     Pri/Wgt  Source     State
          10.229.11.1   1/100  cfg-intf   site-self, reachable

        =================================================
        Output for router lisp 0 instance-id 2
        =================================================
        LISP ETR MAC Mapping Database for EID-table Vlan 102 (IID 2), LSBs: 0x1
        Entries total 2, no-route 0, inactive 0

        0050.56b0.60de/48, dynamic-eid Auto-L2-group-2, inherited from default locator-set RLOC
          Locator     Pri/Wgt  Source     State
          10.229.11.1    1/100  cfg-intf   site-self, reachable
        face.0171.0001/48, dynamic-eid Auto-L2-group-2, inherited from default locator-set RLOC
          Locator     Pri/Wgt  Source     State
          10.229.11.1    1/100  cfg-intf   site-self, reachable

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

    def test_show_lisp_service_database_full1(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output1)
        obj = ShowLispServiceDatabase(device=self.device)
        parsed_output = obj.parse(service='ipv4', instance_id='101')
        self.assertEqual(parsed_output, self.golden_parsed_output1)

    def test_show_lisp_service_database_full2(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output2)
        obj = ShowLispServiceDatabase(device=self.device)
        parsed_output = obj.parse(service='ipv6', instance_id='101')
        self.assertEqual(parsed_output, self.golden_parsed_output2)

    def test_show_lisp_service_database_full3(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output3)
        obj = ShowLispServiceDatabase(device=self.device)
        parsed_output = obj.parse(service='ethernet', instance_id='*')
        self.assertEqual(parsed_output, self.golden_parsed_output3)

    def test_show_lisp_service_database_empty(self):
        self.maxDiff = None
        self.device = Mock(**self.empty_output)
        obj = ShowLispServiceDatabase(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse(service='ipv4', instance_id='*')


# ================================================================================
# Unit test for 'show lisp all instance-id <instance_id> <service> server summary'
# ================================================================================
class test_show_lisp_service_server_summary(unittest.TestCase):

    '''Unit test for "show lisp all instance-id <instance_id> <service> server summary"'''

    device = Device(name='aDevice')

    empty_output = {'execute.return_value': ''}

    golden_parsed_output1 = {
        'lisp_router_instances': 
            {0: 
                {'lisp_router_instance_id': 0,
                'service': 
                    {'ipv4': 
                        {'instance_id':
                            {'101':
                                {'map_server': 
                                    {'summary': 
                                        {'number_registered_sites': 2,
                                        'number_configured_sites': 2,
                                        'af_datum': 
                                            {'ipv4-afi':
                                                {'address_type': 'ipv4-afi',
                                                'number_registered_eids': 2,
                                                'number_configured_eids': 2,
                                                },
                                            },
                                        'sites_with_inconsistent_registrations': 0},
                                    'sites': 
                                        {'xtr1_1': 
                                            {'configured': 1,
                                            'inconsistent': 0,
                                            'registered': 1,
                                            'site_id': 'xtr1_1'},
                                        'xtr2': 
                                            {'configured': 1,
                                            'inconsistent': 0,
                                            'registered': 1,
                                            'site_id': 'xtr2'}}}}}}}}}}

    golden_output1 = {'execute.return_value': '''
        204-MSMR#show lisp all instance-id 101 ipv4 server summary 
        =====================================================
        Output for router lisp 0
        =====================================================
                             -----------  IPv4 ----------- 
         Site name            Configured Registered Incons
        xtr1_1                        1          1      0
        xtr2                          1          1      0

        Number of configured sites:                     2
        Number of registered sites:                     2
        Sites with inconsistent registrations:          0
        IPv4
          Number of configured EID prefixes:            2
          Number of registered EID prefixes:            2
        '''}

    golden_parsed_output2 = {
        'lisp_router_instances': 
            {0: 
                {'lisp_router_instance_id': 0,
                'service': 
                    {'ipv6': 
                        {'instance_id':
                            {'101':
                                {'map_server': 
                                    {'summary': 
                                        {'number_configured_sites': 2,
                                        'number_registered_sites': 2,
                                        'af_datum':
                                            {'ipv6-afi':
                                                {'address_type': 'ipv6-afi',
                                                'number_configured_eids': 2,
                                                'number_registered_eids': 2,
                                                },
                                            },
                                        'sites_with_inconsistent_registrations': 0},
                                    'sites': 
                                        {'xtr1_1': 
                                            {'configured': 1,
                                            'inconsistent': 0,
                                            'registered': 1,
                                            'site_id': 'xtr1_1'},
                                        'xtr2': 
                                            {'configured': 1,
                                            'inconsistent': 0,
                                            'registered': 1,
                                            'site_id': 'xtr2'}}}}}}}}}}

    golden_output2 = {'execute.return_value': '''
        204-MSMR#show lisp all instance-id 101 ipv6 server summary 
        =====================================================
        Output for router lisp 0
        =====================================================
                             -----------  IPv6 ----------- 
         Site name            Configured Registered Incons
        xtr1_1                        1          1      0
        xtr2                          1          1      0

        Number of configured sites:                     2
        Number of registered sites:                     2
        Sites with inconsistent registrations:          0
        IPv6
          Number of configured EID prefixes:            2
          Number of registered EID prefixes:            2
        '''}

    golden_parsed_output3 = {
        'lisp_router_instances': 
            {2: 
                {'lisp_router_instance_id': 2,
                'service': 
                    {'ethernet': 
                        {'instance_id': 
                            {'101': 
                                {'map_server': 
                                    {'summary': 
                                        {'number_configured_sites': 1,
                                        'number_registered_sites': 0,
                                        'site_registration_count': 0,
                                        'site_registration_limit': 0,
                                        'sites_with_inconsistent_registrations': 0},
                                    'sites': 
                                        {'xtr1_1': 
                                            {'configured': 0,
                                            'inconsistent': 0,
                                            'registered': 0,
                                            'site_id': 'xtr1_1'}}}},
                            '102': 
                                {'map_server': 
                                    {'summary': 
                                        {'number_configured_sites': 1,
                                        'number_registered_sites': 0,
                                        'site_registration_count': 0,
                                        'site_registration_limit': 0,
                                        'sites_with_inconsistent_registrations': 0},
                                    'sites': 
                                        {'xtr1_2': 
                                            {'configured': 0,
                                            'inconsistent': 0,
                                            'registered': 0,
                                            'site_id': 'xtr1_2'}}}},
                            '103': 
                                {'map_server': 
                                    {'summary': 
                                        {'number_configured_sites': 1,
                                        'number_registered_sites': 0,
                                        'site_registration_count': 0,
                                        'site_registration_limit': 0,
                                        'sites_with_inconsistent_registrations': 0},
                                    'sites': 
                                        {'provider': 
                                            {'configured': 0,
                                            'inconsistent': 0,
                                            'registered': 0,
                                            'site_id': 'provider'}}}},
                            '104': 
                                {'map_server': 
                                    {'summary': 
                                        {'number_configured_sites': 1,
                                        'number_registered_sites': 0,
                                        'site_registration_count': 0,
                                        'site_registration_limit': 0,
                                        'sites_with_inconsistent_registrations': 0},
                                    'sites': 
                                        {'xtr1_3': 
                                            {'configured': 0,
                                            'inconsistent': 0,
                                            'registered': 0,
                                            'site_id': 'xtr1_3'}}}},
                            '107': 
                                {'map_server': 
                                    {'summary': 
                                        {'number_configured_sites': 1,
                                        'number_registered_sites': 0,
                                        'site_registration_count': 0,
                                        'site_registration_limit': 0,
                                        'sites_with_inconsistent_registrations': 0},
                                    'sites': 
                                        {'prov1': 
                                            {'configured': 0,
                                            'inconsistent': 0,
                                            'registered': 0,
                                            'site_id': 'prov1'}}}},
                            '108': 
                                {'map_server': 
                                    {'summary': 
                                        {'number_configured_sites': 1,
                                        'number_registered_sites': 0,
                                        'site_registration_count': 0,
                                        'site_registration_limit': 0,
                                        'sites_with_inconsistent_registrations': 0},
                                    'sites': 
                                        {'prov2': 
                                            {'configured': 0,
                                            'inconsistent': 0,
                                            'registered': 0,
                                            'site_id': 'prov2'}}}},
                            '109': 
                                {'map_server': 
                                    {'summary': 
                                        {'number_configured_sites': 1,
                                        'number_registered_sites': 0,
                                        'site_registration_count': 0,
                                        'site_registration_limit': 0,
                                        'sites_with_inconsistent_registrations': 0},
                                    'sites': 
                                        {'prov3': 
                                            {'configured': 0,
                                            'inconsistent': 0,
                                            'registered': 0,
                                            'site_id': 'prov3'}}}}}}}}}}

    golden_output3 = {'execute.return_value': '''
        OTT-LISP-C9K-20-MSMR#show lisp all instance-id * ethernet server summary
        =================================================
        Output for router lisp 2 instance-id 101
        =================================================
        *********************************
        ** NO LOCATOR-TABLE CONFIGURED **
        *********************************

                             -----------  MAC  -----------
         Site name            Configured Registered Incons
        xtr1_1                        0          0      0

        Site-registration limit for router lisp 2:            0
        Site-registration count for router lisp 2:            0
        Number of configured sites:                           1
        Number of registered sites:                           0
        Sites with inconsistent registrations:                0

        =================================================
        Output for router lisp 2 instance-id 102
        =================================================
        *********************************
        ** NO LOCATOR-TABLE CONFIGURED **
        *********************************

                             -----------  MAC  -----------
         Site name            Configured Registered Incons
        xtr1_2                        0          0      0

        Site-registration limit for router lisp 2:            0
        Site-registration count for router lisp 2:            0
        Number of configured sites:                           1
        Number of registered sites:                           0
        Sites with inconsistent registrations:                0

        =================================================
        Output for router lisp 2 instance-id 103
        =================================================
        *********************************
        ** NO LOCATOR-TABLE CONFIGURED **
        *********************************

                             -----------  MAC  -----------
         Site name            Configured Registered Incons
        provider                      0          0      0

        Site-registration limit for router lisp 2:            0
        Site-registration count for router lisp 2:            0
        Number of configured sites:                           1
        Number of registered sites:                           0
        Sites with inconsistent registrations:                0

        =================================================
        Output for router lisp 2 instance-id 104
        =================================================
        *********************************
        ** NO LOCATOR-TABLE CONFIGURED **
        *********************************

                             -----------  MAC  -----------
         Site name            Configured Registered Incons
        xtr1_3                        0          0      0

        Site-registration limit for router lisp 2:            0
        Site-registration count for router lisp 2:            0
        Number of configured sites:                           1
        Number of registered sites:                           0
        Sites with inconsistent registrations:                0

        =================================================
        Output for router lisp 2 instance-id 107
        =================================================
        *********************************
        ** NO LOCATOR-TABLE CONFIGURED **
        *********************************

                             -----------  MAC  -----------
         Site name            Configured Registered Incons
        prov1                         0          0      0

        Site-registration limit for router lisp 2:            0
        Site-registration count for router lisp 2:            0
        Number of configured sites:                           1
        Number of registered sites:                           0
        Sites with inconsistent registrations:                0

        =================================================
        Output for router lisp 2 instance-id 108
        =================================================
        *********************************
        ** NO LOCATOR-TABLE CONFIGURED **
        *********************************

                             -----------  MAC  -----------
         Site name            Configured Registered Incons
        prov2                         0          0      0

        Site-registration limit for router lisp 2:            0
        Site-registration count for router lisp 2:            0
        Number of configured sites:                           1
        Number of registered sites:                           0
        Sites with inconsistent registrations:                0

        =================================================
        Output for router lisp 2 instance-id 109
        =================================================
        *********************************
        ** NO LOCATOR-TABLE CONFIGURED **
        *********************************

                             -----------  MAC  -----------
         Site name            Configured Registered Incons
        prov3                         0          0      0

        Site-registration limit for router lisp 2:            0
        Site-registration count for router lisp 2:            0
        Number of configured sites:                           1
        Number of registered sites:                           0
        Sites with inconsistent registrations:                0

        '''}

    def test_show_lisp_service_server_summary_full1(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output1)
        obj = ShowLispServiceServerSummary(device=self.device)
        parsed_output = obj.parse(service='ipv4', instance_id='101')
        self.assertEqual(parsed_output, self.golden_parsed_output1)

    def test_show_lisp_service_server_summary_full2(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output2)
        obj = ShowLispServiceServerSummary(device=self.device)
        parsed_output = obj.parse(service='ipv6', instance_id='101')
        self.assertEqual(parsed_output, self.golden_parsed_output2)

    def test_show_lisp_service_server_summary_full3(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output3)
        obj = ShowLispServiceServerSummary(device=self.device)
        parsed_output = obj.parse(service='ethernet', instance_id='*')
        self.assertEqual(parsed_output, self.golden_parsed_output3)

    def test_show_lisp_service_server_summary_empty(self):
        self.maxDiff = None
        self.device = Mock(**self.empty_output)
        obj = ShowLispServiceServerSummary(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse(service='ipv4', instance_id='*')


# ========================================================================================
# Unit test for 'show lisp all instance-id <instance_id> <service> server detail internal'
# ========================================================================================
class test_show_lisp_service_server_detail_internal(unittest.TestCase):

    '''Unit test for "show lisp all instance-id <instance_id> <service> server detail internal"'''

    device = Device(name='aDevice')

    empty_output = {'execute.return_value': ''}

    golden_parsed_output1 = {
        'lisp_router_instances': 
            {0: 
                {'service': 
                    {'ipv4': 
                        {'map_server': 
                            {'sites': 
                                {'provider': 
                                    {'allowed_configured_locators': 'any',
                                    'site_id': 'provider'},
                                'xtr1_1': 
                                    {'allowed_configured_locators': 'any',
                                    'site_id': 'xtr1_1'},
                                'xtr1_2': 
                                    {'allowed_configured_locators': 'any',
                                    'site_id': 'xtr1_2'},
                                'xtr2': 
                                    {'allowed_configured_locators': 'any',
                                    'site_id': 'xtr2'}},
                            'virtual_network_ids': 
                                {'101': 
                                    {'mappings': 
                                        {'192.168.0.0/24': 
                                            {'eid_id': '192.168.0.0/24',
                                            'first_registered': '1w4d',
                                            'eid_address':
                                                {'address_type': 'ipv4-afi',
                                                'ipv4': 
                                                    {'ipv4': '192.168.0.0/24'},
                                                'virtual_network_id': '101',
                                                },
                                            'last_registered': '02:41:22',
                                            'merge_active': False,
                                            'more_specifics_accepted': True,
                                            'origin': 'Configuration',
                                            'proxy_reply': False,
                                            'registration_errors': 
                                                {'allowed_locators_mismatch': 0,
                                                'authentication_failures': 0},
                                            'routing_table_tag': 0,
                                            'site_id': 'xtr1_1',
                                            'state': 'unknown',
                                            'ttl': '00:00:00'},
                                        '192.168.0.1/32': 
                                            {'eid_id': '192.168.0.1/32',
                                            'first_registered': '01:12:41',
                                            'eid_address':
                                                {'address_type': 'ipv4-afi',
                                                'ipv4': 
                                                    {'ipv4': '192.168.0.1/32'},
                                                'virtual_network_id': '101',
                                                },
                                            'last_registered': '01:12:41',
                                            'mapping_records': 
                                                {'0x21EDD25F-0x7598784C-0x769C8E4E-0xC04926EC': 
                                                    {'eid': 
                                                        {'address_type': 'ipv4-afi',
                                                        'ipv4': 
                                                            {'ipv4': '192.168.0.1/32'},
                                                        'virtual_network_id': '101',
                                                        },
                                                    'etr': '10.16.2.2',
                                                    'map_notify': True,
                                                    'merge': False,
                                                    'nonce': '0x70D18EF4-0x3A605D67',
                                                    'proxy_reply': True,
                                                    'security_capability': False,
                                                    'sourced_by': 'reliable transport',
                                                    'state': 'complete',
                                                    'time_to_live': 86400,
                                                    'ttl': '1d00h',
                                                    'creation_time': '01:12:41',
                                                    'hash_function': 'sha1,',
                                                    'locator': 
                                                        {'10.16.2.2': 
                                                            {'local': True,
                                                            'priority': 50,
                                                            'scope': 'IPv4 none',
                                                            'state': 'up',
                                                            'weight': 50}},
                                                    'site_id': 'unspecified',
                                                    'xtr_id': '0x21EDD25F-0x7598784C-0x769C8E4E-0xC04926EC'}},
                                            'merge_active': False,
                                            'origin': 'Dynamic',
                                            'proxy_reply': True,
                                            'registration_errors': 
                                                {'allowed_locators_mismatch': 0,
                                                'authentication_failures': 0},
                                            'routing_table_tag': 0,
                                            'site_id': 'xtr1_1',
                                            'state': 'complete',
                                            'ttl': '1d00h'},
                                        '192.168.9.0/24': 
                                            {'eid_id': '192.168.9.0/24',
                                            'first_registered': '01:55:47',
                                            'eid_address':
                                                {'address_type': 'ipv4-afi',
                                                'ipv4': 
                                                    {'ipv4': '192.168.9.0/24'},
                                                'virtual_network_id': '101',
                                                },
                                            'last_registered': '01:55:47',
                                            'mapping_records': 
                                                {'0x77200484-0xD134DC48-0x0FBAD9DC-0x4A46CA5D': 
                                                    {'eid': 
                                                        {'address_type': 'ipv4-afi',
                                                        'ipv4': 
                                                            {'ipv4': '192.168.9.0/24'},
                                                        'virtual_network_id': '101',
                                                        },
                                                    'etr': '10.1.8.8',
                                                    'creation_time': '01:55:47',
                                                    'hash_function': 'sha1,',
                                                    'map_notify': True,
                                                    'merge': False,
                                                    'nonce': '0xB06AE31D-0x6ADB0BA5',
                                                    'proxy_reply': True,
                                                    'security_capability': False,
                                                    'sourced_by': 'reliable transport',
                                                    'state': 'complete',
                                                    'time_to_live': 86400,
                                                    'ttl': '1d00h',
                                                    'locator': 
                                                        {'10.1.8.8': 
                                                            {'local': True,
                                                            'priority': 50,
                                                            'scope': 'IPv4 none',
                                                            'state': 'up',
                                                            'weight': 50}},
                                                    'site_id': 'unspecified',
                                                    'xtr_id': '0x77200484-0xD134DC48-0x0FBAD9DC-0x4A46CA5D'}},
                                            'merge_active': False,
                                            'origin': 'Configuration',
                                            'proxy_reply': True,
                                            'registration_errors': {'allowed_locators_mismatch': 0,
                                                               'authentication_failures': 0},
                                            'routing_table_tag': 0,
                                            'site_id': 'xtr2',
                                            'state': 'complete',
                                            'ttl': '1d00h'}},
                                    'vni': '101'}}}}}}}}

    golden_output1 = {'execute.return_value': '''
        204-MSMR#show lisp all instance-id 101 ipv4 server detail internal
        =====================================================
        Output for router lisp 0
        =====================================================
        LISP Site Registration Information

        Site name: provider
        Allowed configured locators: any
        Allowed EID-prefixes:

        Site name: xtr1_1
        Allowed configured locators: any
        Allowed EID-prefixes:

          EID-prefix: 192.168.0.0/24 instance-id 101
            First registered:     1w4d
            Last registered:      02:41:22
            Routing table tag:    0
            Origin:               Configuration, accepting more specifics
            Merge active:         No
            Proxy reply:          No
            TTL:                  00:00:00
            State:                unknown
            Registration errors:
              Authentication failures:   0
              Allowed locators mismatch: 0
            No registrations.

          EID-prefix: 192.168.0.1/32 instance-id 101
            First registered:     01:12:41
            Last registered:      01:12:41
            Routing table tag:    0
            Origin:               Dynamic, more specific of 192.168.0.0/24
            Merge active:         No
            Proxy reply:          Yes
            TTL:                  1d00h
            State:                complete
            Registration errors:
              Authentication failures:   0
              Allowed locators mismatch: 0
            ETR 10.16.2.2, last registered 01:12:41, proxy-reply, map-notify
                         TTL 1d00h, no merge, hash-function sha1, nonce 0x70D18EF4-0x3A605D67
                         state complete, no security-capability
                         xTR-ID 0x21EDD25F-0x7598784C-0x769C8E4E-0xC04926EC
                         site-ID unspecified
                         sourced by reliable transport
              Locator  Local  State      Pri/Wgt  Scope
              10.16.2.2 yes    up          50/50   IPv4 none

        Site name: xtr1_2
        Allowed configured locators: any
        Allowed EID-prefixes:

        Site name: xtr2
        Allowed configured locators: any
        Allowed EID-prefixes:

          EID-prefix: 192.168.9.0/24 instance-id 101
            First registered:     01:55:47
            Last registered:      01:55:47
            Routing table tag:    0
            Origin:               Configuration
            Merge active:         No
            Proxy reply:          Yes
            TTL:                  1d00h
            State:                complete
            Registration errors:
              Authentication failures:   0
              Allowed locators mismatch: 0
            ETR 10.1.8.8, last registered 01:55:47, proxy-reply, map-notify
                         TTL 1d00h, no merge, hash-function sha1, nonce 0xB06AE31D-0x6ADB0BA5
                         state complete, no security-capability
                         xTR-ID 0x77200484-0xD134DC48-0x0FBAD9DC-0x4A46CA5D
                         site-ID unspecified
                         sourced by reliable transport
              Locator  Local  State      Pri/Wgt  Scope
              10.1.8.8  yes    up          50/50   IPv4 none
        '''}

    golden_parsed_output2 = {
        'lisp_router_instances': 
            {0: 
                {'service': 
                    {'ipv6': 
                        {'map_server': 
                            {'sites': 
                                {'provider': 
                                    {'allowed_configured_locators': 'any',
                                    'site_id': 'provider'},
                                'xtr1_1': 
                                    {'allowed_configured_locators': 'any',
                                    'site_id': 'xtr1_1'},
                                'xtr1_2': 
                                    {'allowed_configured_locators': 'any',
                                    'site_id': 'xtr1_2'},
                                'xtr2': 
                                    {'allowed_configured_locators': 'any',
                                    'site_id': 'xtr2'}},
                            'virtual_network_ids': 
                                {'101': 
                                    {'mappings': 
                                        {'2001:192:168:9::/64': 
                                            {'eid_id': '2001:192:168:9::/64',
                                            'first_registered': '00:13:19',
                                            'eid_address':
                                                {'address_type': 'ipv6-afi',
                                                'ipv6': 
                                                    {'ipv6': '2001:192:168:9::/64'},
                                                'virtual_network_id': '101',
                                                },
                                            'last_registered': '00:13:19',
                                            'mapping_records': 
                                                {'0x6BE732BF-0xD9530F52-0xF9162AA3-0x6283920A': 
                                                    {'eid': 
                                                        {'address_type': 'ipv6-afi',
                                                        'ipv6': 
                                                            {'ipv6': '2001:192:168:9::/64'},
                                                        'virtual_network_id': '101',
                                                        },
                                                    'etr': '10.1.8.8',
                                                    'creation_time': '00:13:19',
                                                    'hash_function': 'sha1,',
                                                    'map_notify': True,
                                                    'merge': False,
                                                    'nonce': '0x90004FBE-0x03D2420E',
                                                    'proxy_reply': True,
                                                    'security_capability': False,
                                                    'sourced_by': 'reliable transport',
                                                    'state': 'complete',
                                                    'time_to_live': 86400,
                                                    'ttl': '1d00h',
                                                    'locator': 
                                                        {'10.1.8.8': 
                                                            {'local': True,
                                                            'priority': 50,
                                                            'scope': 'IPv4 none',
                                                            'state': 'up',
                                                            'weight': 50}},
                                                    'site_id': 'unspecified',
                                                    'xtr_id': '0x6BE732BF-0xD9530F52-0xF9162AA3-0x6283920A'}},
                                            'merge_active': False,
                                            'origin': 'Configuration',
                                            'proxy_reply': True,
                                            'registration_errors': 
                                                {'allowed_locators_mismatch': 0,
                                                'authentication_failures': 0},
                                            'routing_table_tag': 0,
                                            'site_id': 'xtr2',
                                            'state': 'complete',
                                            'ttl': '1d00h'},
                                        '2001:192:168::/64': 
                                            {'eid_id': '2001:192:168::/64',
                                            'first_registered': '00:13:19',
                                            'eid_address':
                                                {'address_type': 'ipv6-afi',
                                                'ipv6': 
                                                    {'ipv6': '2001:192:168::/64'},
                                                'virtual_network_id': '101',
                                                },
                                            'last_registered': '00:13:19',
                                            'mapping_records': 
                                                {'0x5B6A0468-0x55E69768-0xD1AE2E61-0x4A082FD5': 
                                                    {'eid': 
                                                        {'address_type': 'ipv6-afi',
                                                        'ipv6': 
                                                            {'ipv6': '2001:192:168::/64'},
                                                        'virtual_network_id': '101',
                                                        },
                                                    'etr': '10.16.2.2',
                                                    'creation_time': '00:13:19',
                                                    'hash_function': 'sha1,',
                                                    'map_notify': True,
                                                    'merge': False,
                                                    'nonce': '0xF8845AAB-0x44B8B869',
                                                    'proxy_reply': True,
                                                    'security_capability': False,
                                                    'sourced_by': 'reliable transport',
                                                    'state': 'complete',
                                                    'time_to_live': 86400,
                                                    'ttl': '1d00h',
                                                    'locator': 
                                                        {'10.16.2.2': 
                                                            {'local': True,
                                                            'priority': 50,
                                                            'scope': 'IPv4 none',
                                                            'state': 'up',
                                                            'weight': 50}},
                                                    'site_id': 'unspecified',
                                                    'xtr_id': '0x5B6A0468-0x55E69768-0xD1AE2E61-0x4A082FD5'}},
                                            'merge_active': False,
                                            'origin': 'Configuration',
                                            'proxy_reply': True,
                                            'registration_errors': 
                                                {'allowed_locators_mismatch': 0,
                                                'authentication_failures': 0},
                                            'routing_table_tag': 0,
                                            'site_id': 'xtr1_1',
                                            'state': 'complete',
                                            'ttl': '1d00h'}},
                                    'vni': '101'}}}}}}}}

    golden_output2 = {'execute.return_value': '''
        204-MSMR#show lisp all instance-id 101 ipv6 server detail internal 
        =====================================================
        Output for router lisp 0
        =====================================================
        LISP Site Registration Information

        Site name: provider
        Allowed configured locators: any
        Allowed EID-prefixes:
        Site name: xtr1_1
        Allowed configured locators: any
        Allowed EID-prefixes:

          EID-prefix: 2001:192:168::/64 instance-id 101 
            First registered:     00:13:19
            Last registered:      00:13:19
            Routing table tag:    0
            Origin:               Configuration
            Merge active:         No
            Proxy reply:          Yes
            TTL:                  1d00h
            State:                complete
            Registration errors:  
              Authentication failures:   0
              Allowed locators mismatch: 0
            ETR 10.16.2.2, last registered 00:13:19, proxy-reply, map-notify
                         TTL 1d00h, no merge, hash-function sha1, nonce 0xF8845AAB-0x44B8B869
                         state complete, no security-capability
                         xTR-ID 0x5B6A0468-0x55E69768-0xD1AE2E61-0x4A082FD5
                         site-ID unspecified
                         sourced by reliable transport
              Locator  Local  State      Pri/Wgt  Scope
              10.16.2.2 yes   up          50/50   IPv4 none
        Site name: xtr1_2
        Allowed configured locators: any
        Allowed EID-prefixes:
        Site name: xtr2
        Allowed configured locators: any
        Allowed EID-prefixes:

          EID-prefix: 2001:192:168:9::/64 instance-id 101 
            First registered:     00:13:19
            Last registered:      00:13:19
            Routing table tag:    0
            Origin:               Configuration
            Merge active:         No
            Proxy reply:          Yes
            TTL:                  1d00h
            State:                complete
            Registration errors:  
              Authentication failures:   0
              Allowed locators mismatch: 0
            ETR 10.1.8.8, last registered 00:13:19, proxy-reply, map-notify
                         TTL 1d00h, no merge, hash-function sha1, nonce 0x90004FBE-0x03D2420E
                         state complete, no security-capability
                         xTR-ID 0x6BE732BF-0xD9530F52-0xF9162AA3-0x6283920A
                         site-ID unspecified
                         sourced by reliable transport
              Locator  Local  State      Pri/Wgt  Scope
              10.1.8.8 yes    up          50/50   IPv4 none
        '''}

    golden_parsed_output3 = {
        'lisp_router_instances': 
            {2: 
                {'service': 
                    {'ethernet': 
                        {'map_server': 
                            {'sites': 
                                {'prov1': 
                                    {'allowed_configured_locators': 'any',
                                    'site_id': 'prov1'},
                                'prov2': 
                                    {'allowed_configured_locators': 'any',
                                    'site_id': 'prov2'},
                                'prov3': 
                                    {'allowed_configured_locators': 'any',
                                    'site_id': 'prov3'},
                                'provider': 
                                    {'allowed_configured_locators': 'any',
                                    'site_id': 'provider'},
                                'xtr1_1': 
                                    {'allowed_configured_locators': 'any',
                                    'site_id': 'xtr1_1'},
                                'xtr1_2': 
                                    {'allowed_configured_locators': 'any',
                                    'site_id': 'xtr1_2'},
                                'xtr1_3': 
                                    {'allowed_configured_locators': 'any',
                                    'site_id': 'xtr1_3'}}}}}}}}

    golden_output3 = {'execute.return_value': '''
        OTT-LISP-C9K-20-MSMR#show lisp all instance-id * ethernet server detail internal
        =================================================
        Output for router lisp 2 instance-id 101
        =================================================
        *********************************
        ** NO LOCATOR-TABLE CONFIGURED **
        *********************************

        LISP Site Registration Information

        Site name: prov1
        Allowed configured locators: any
        Allowed EID-prefixes:
        Site name: prov2
        Allowed configured locators: any
        Allowed EID-prefixes:
        Site name: prov3
        Allowed configured locators: any
        Allowed EID-prefixes:
        Site name: provider
        Allowed configured locators: any
        Allowed EID-prefixes:
        Site name: xtr1_1
        Allowed configured locators: any
        Allowed EID-prefixes:
        Site name: xtr1_2
        Allowed configured locators: any
        Allowed EID-prefixes:
        Site name: xtr1_3
        Allowed configured locators: any
        Allowed EID-prefixes:

        =================================================
        Output for router lisp 2 instance-id 102
        =================================================
        *********************************
        ** NO LOCATOR-TABLE CONFIGURED **
        *********************************

        LISP Site Registration Information

        Site name: prov1
        Allowed configured locators: any
        Allowed EID-prefixes:
        Site name: prov2
        Allowed configured locators: any
        Allowed EID-prefixes:
        Site name: prov3
        Allowed configured locators: any
        Allowed EID-prefixes:
        Site name: provider
        Allowed configured locators: any
        Allowed EID-prefixes:
        Site name: xtr1_1
        Allowed configured locators: any
        Allowed EID-prefixes:
        Site name: xtr1_2
        Allowed configured locators: any
        Allowed EID-prefixes:
        Site name: xtr1_3
        Allowed configured locators: any
        Allowed EID-prefixes:

        =================================================
        Output for router lisp 2 instance-id 103
        =================================================
        *********************************
        ** NO LOCATOR-TABLE CONFIGURED **
        *********************************

        LISP Site Registration Information

        Site name: prov1
        Allowed configured locators: any
        Allowed EID-prefixes:
        Site name: prov2
        Allowed configured locators: any
        Allowed EID-prefixes:
        Site name: prov3
        Allowed configured locators: any
        Allowed EID-prefixes:
        Site name: provider
        Allowed configured locators: any
        Allowed EID-prefixes:
        Site name: xtr1_1
        Allowed configured locators: any
        Allowed EID-prefixes:
        Site name: xtr1_2
        Allowed configured locators: any
        Allowed EID-prefixes:
        Site name: xtr1_3
        Allowed configured locators: any
        Allowed EID-prefixes:

        =================================================
        Output for router lisp 2 instance-id 104
        =================================================
        *********************************
        ** NO LOCATOR-TABLE CONFIGURED **
        *********************************

        LISP Site Registration Information

        Site name: prov1
        Allowed configured locators: any
        Allowed EID-prefixes:
        Site name: prov2
        Allowed configured locators: any
        Allowed EID-prefixes:
        Site name: prov3
        Allowed configured locators: any
        Allowed EID-prefixes:
        Site name: provider
        Allowed configured locators: any
        Allowed EID-prefixes:
        Site name: xtr1_1
        Allowed configured locators: any
        Allowed EID-prefixes:
        Site name: xtr1_2
        Allowed configured locators: any
        Allowed EID-prefixes:
        Site name: xtr1_3
        Allowed configured locators: any
        Allowed EID-prefixes:

        =================================================
        Output for router lisp 2 instance-id 107
        =================================================
        *********************************
        ** NO LOCATOR-TABLE CONFIGURED **
        *********************************

        LISP Site Registration Information

        Site name: prov1
        Allowed configured locators: any
        Allowed EID-prefixes:
        Site name: prov2
        Allowed configured locators: any
        Allowed EID-prefixes:
        Site name: prov3
        Allowed configured locators: any
        Allowed EID-prefixes:
        Site name: provider
        Allowed configured locators: any
        Allowed EID-prefixes:
        Site name: xtr1_1
        Allowed configured locators: any
        Allowed EID-prefixes:
        Site name: xtr1_2
        Allowed configured locators: any
        Allowed EID-prefixes:
        Site name: xtr1_3
        Allowed configured locators: any
        Allowed EID-prefixes:

        =================================================
        Output for router lisp 2 instance-id 108
        =================================================
        *********************************
        ** NO LOCATOR-TABLE CONFIGURED **
        *********************************

        LISP Site Registration Information

        Site name: prov1
        Allowed configured locators: any
        Allowed EID-prefixes:
        Site name: prov2
        Allowed configured locators: any
        Allowed EID-prefixes:
        Site name: prov3
        Allowed configured locators: any
        Allowed EID-prefixes:
        Site name: provider
        Allowed configured locators: any
        Allowed EID-prefixes:
        Site name: xtr1_1
        Allowed configured locators: any
        Allowed EID-prefixes:
        Site name: xtr1_2
        Allowed configured locators: any
        Allowed EID-prefixes:
        Site name: xtr1_3
        Allowed configured locators: any
        Allowed EID-prefixes:

        =================================================
        Output for router lisp 2 instance-id 109
        =================================================
        *********************************
        ** NO LOCATOR-TABLE CONFIGURED **
        *********************************

        LISP Site Registration Information

        Site name: prov1
        Allowed configured locators: any
        Allowed EID-prefixes:
        Site name: prov2
        Allowed configured locators: any
        Allowed EID-prefixes:
        Site name: prov3
        Allowed configured locators: any
        Allowed EID-prefixes:
        Site name: provider
        Allowed configured locators: any
        Allowed EID-prefixes:
        Site name: xtr1_1
        Allowed configured locators: any
        Allowed EID-prefixes:
        Site name: xtr1_2
        Allowed configured locators: any
        Allowed EID-prefixes:
        Site name: xtr1_3
        Allowed configured locators: any
        Allowed EID-prefixes:

        '''}

    def test_show_lisp_service_server_detail_internal_full1(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output1)
        obj = ShowLispServiceServerDetailInternal(device=self.device)
        parsed_output = obj.parse(service='ipv4', instance_id='101')
        self.assertEqual(parsed_output, self.golden_parsed_output1)

    def test_show_lisp_service_server_detail_internal_full2(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output2)
        obj = ShowLispServiceServerDetailInternal(device=self.device)
        parsed_output = obj.parse(service='ipv6', instance_id='101')
        self.assertEqual(parsed_output, self.golden_parsed_output2)

    def test_show_lisp_service_server_detail_internal_full3(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output3)
        obj = ShowLispServiceServerDetailInternal(device=self.device)
        parsed_output = obj.parse(service='ethernet', instance_id='*')
        self.assertEqual(parsed_output, self.golden_parsed_output3)

    def test_show_lisp_service_server_detail_internal_empty(self):
        self.maxDiff = None
        self.device = Mock(**self.empty_output)
        obj = ShowLispServiceServerDetailInternal(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse(service='ipv4', instance_id='*')


# ============================================================================
# Unit test for 'show lisp all instance-id <instance_id> <service> statistics'
# ============================================================================
class test_show_lisp_service_statistics(unittest.TestCase):

    '''Unit test for "show lisp all instance-id <instance_id> <service> statistics"'''

    device = Device(name='aDevice')

    empty_output = {'execute.return_value': ''}

    golden_parsed_output1 = {
        'lisp_router_instances': 
            {0: 
                {'service': 
                    {'ipv4': 
                        {'statistics': 
                            {'EID': 
                                {'control': 
                                    {'authoritative_records_in': '1',
                                    'authoritative_records_out': '1',
                                    'ddt_referral_deferred': '0',
                                    'ddt_referral_dropped': '0',
                                    'ddt_request_deferred': '0',
                                    'ddt_request_dropped': '0',
                                    'deferred_packet_transmission': '0/0',
                                    'dropped_control_packets_in_input_queue': '0',
                                    'encapsulated_map_requests_in': '0',
                                    'encapsulated_map_requests_out': '3',
                                    'etr_info_request_deferred': '0',
                                    'etr_info_request_dropped': '0',
                                    'map_notify_records_in': '4',
                                    'map_notify_records_out': '0',
                                    'map_notify_auth_failures': '0',
                                    'map_register_records_in': '0',
                                    'map_register_records_out': '2857',
                                    'map_reply_deferred': '0',
                                    'map_reply_dropped': '0',
                                    'map_reply_records_in': '2',
                                    'map_reply_records_out': '1',
                                    'map_requests_expired_no-reply': '0',
                                    'map_requests_expired_on-queue': '0',
                                    'map_requests_in': '0',
                                    'map_requests_out': '4',
                                    'map_resolver_map_requests_forwarded': '0',
                                    'map_server_af_disabled': '0',
                                    'map_registers_in_auth_failed': '0',
                                    'map_server_map_requests_forwarded': '0',
                                    'map_server_proxy_reply_records_out': '0',
                                    'map_subscribe_failures_in': '0',
                                    'map_subscribe_failures_out': '0',
                                    'map_unsubscribe_failures_in': '0',
                                    'map_unsubscribe_failures_out': '0',
                                    'mr_map_request_fwd_deferred': '0',
                                    'mr_map_request_fwd_dropped': '0',
                                    'mr_negative_map_reply_deferred': '0',
                                    'mr_negative_map_reply_dropped': '0',
                                    'ms_info_reply_deferred': '0',
                                    'ms_info_reply_dropped': '0',
                                    'ms_map_request_fwd_deferred': '0',
                                    'ms_map_request_fwd_dropped': '0',
                                    'ms_proxy_map_reply_deferred': '0',
                                    'ms_proxy_map_reply_dropped': '0',
                                    'negative_records_in': '0',
                                    'negative_records_out': '0',
                                    'non_authoritative_records_in': '1',
                                    'non_authoritative_records_out': '0',
                                    'rloc_probe_map_requests_in': '0',
                                    'rloc_probe_map_requests_out': '1',
                                    'rloc_probe_records_in': '1',
                                    'rloc_probe_records_out': '1',
                                    'rtr_map_notify_fwd_deferred': '0',
                                    'rtr_map_notify_fwd_dropped': '0',
                                    'rtr_map_register_fwd_deferred': '0',
                                    'rtr_map_register_fwd_dropped': '0',
                                    'smr_based_map_requests_in': '0',
                                    'smr_based_map_requests_out': '0',
                                    'wlc_ap_map_notify_in': '0',
                                    'wlc_ap_map_notify_out': '0',
                                    'wlc_ap_map_register_in': '0',
                                    'wlc_ap_map_register_out': '0',
                                    'wlc_client_map_notify_in': '0',
                                    'wlc_client_map_notify_out': '0',
                                    'wlc_client_map_register_in': '0',
                                    'wlc_client_map_register_out': '0',
                                    'wlc_map_notify_failures_in': '0',
                                    'wlc_map_notify_failures_out': '0',
                                    'wlc_map_notify_records_in': '0',
                                    'wlc_map_notify_records_out': '0',
                                    'wlc_map_register_failures_in': '0',
                                    'wlc_map_register_failures_out': '0',
                                    'wlc_map_register_records_in': '0',
                                    'wlc_map_register_records_out': '0',
                                    'wlc_map_subscribe_records_in': '0',
                                    'wlc_map_subscribe_records_out': '1',
                                    'wlc_map_unsubscribe_records_in': '0',
                                    'wlc_map_unsubscribe_records_out': '0',
                                    'xtr_mcast_map_notify_deferred': '0',
                                    'xtr_mcast_map_notify_dropped': '0'},
                                'errors': 
                                    {'average_rlocs_per_eid_prefix': '1',
                                    'cache_entries_created': '3',
                                    'cache_entries_deleted': '1',
                                    'ddt_itr_map_requests_dropped': '0 (nonce-collision: 0, bad-xTR-nonce: 0)',
                                    'map_register_invalid_source_rloc_drops': '0',
                                    'map_request_invalid_source_rloc_drops': '0',
                                    'map_rseolvers': 
                                        {'10.166.13.13': 
                                            {'last_reply': '03:13:58',
                                            'metric': '26',
                                            'negative': 0,
                                            'no_reply': 1,
                                            'positive': 0,
                                            'reqs_sent': 2},
                                        '10.64.4.4': 
                                            {'last_reply': '03:13:58',
                                            'metric': '4',
                                            'negative': 0,
                                            'no_reply': 0,
                                            'positive': 1,
                                            'reqs_sent': 1}},
                                    'number_of_data_signals_processed': '1 (+ dropped 0)',
                                    'number_of_eid_prefixes_in_map_cache': '2',
                                    'number_of_negative_entries_in_map_cache': '1',
                                    'number_of_reachability_reports': '0 (+ dropped 0)',
                                    'total_number_of_rlocs_in_map_cache': '1'},
                                'last_cleared': 'never'},
                            'Miscellaneous': 
                                {'errors': 
                                    {'invalid_ip_header_drops': '0',
                                    'invalid_ip_proto_field_drops': '0',
                                    'invalid_ip_version_drops': '0',
                                    'invalid_lisp_checksum_drops': '0',
                                    'invalid_lisp_control_port_drops': '0',
                                    'invalid_packet_size_dropss': '0',
                                    'unknown_packet_drops': '0',
                                    'unsupported_lisp_packet_type_drops': '0'},
                                'last_cleared': 'never'},
                            'RLOC': 
                                {'control': 
                                    {'ddt_map_referrals_in': '0',
                                    'ddt_map_referrals_out': '0',
                                    'ddt_map_requests_in': '0',
                                    'ddt_map_requests_out': '0',
                                    'rtr_map_notifies_forwarded': '0',
                                    'rtr_map_requests_forwarded': '0'},
                                'errors': 
                                    {'ddt_requests_failed': '0',
                                    'map_referral_format_errors': '0',
                                    'map_reply_format_errors': '0',
                                    'map_request_format_errors': '0',
                                    'mapping_record_ttl_alerts': '0'},
                                'last_cleared': 'never'}}}}}}}

    golden_output1 = {'execute.return_value': '''
        202-XTR#show lisp all instance-id 101 ipv4 statistics 
        =====================================================
        Output for router lisp 0
        =====================================================
        LISP EID Statistics for instance ID 101 - last cleared: never
        Control Packets:
          Map-Requests in/out:                      0/4
            Encapsulated Map-Requests in/out:       0/3
            RLOC-probe Map-Requests in/out:         0/1
            SMR-based Map-Requests in/out:          0/0
            Map-Requests expired on-queue/no-reply:  0/0
            Map-Resolver Map-Requests forwarded:    0
            Map-Server Map-Requests forwarded:      0
          Map-Reply records in/out:                 2/1
            Authoritative records in/out:           1/1
            Non-authoritative records in/out:       1/0
            Negative records in/out:                0/0
            RLOC-probe records in/out:              1/1
            Map-Server Proxy-Reply records out:     0
          WLC Map-Subscribe records in/out:         0/1
            Map-Subscribe failures in/out:          0/0
          WLC Map-Unsubscribe records in/out:       0/0
            Map-Unsubscribe failures in/out:        0/0
          Map-Register records in/out:              0/2857
            Map-Server AF disabled:                 0
            Authentication failures:                0
          WLC Map-Register records in/out:          0/0
            WLC AP Map-Register in/out:             0/0
            WLC Client Map-Register in/out:         0/0
            WLC Map-Register failures in/out:       0/0
          Map-Notify records in/out:                4/0
            Authentication failures:                0
          WLC Map-Notify records in/out:            0/0
            WLC AP Map-Notify in/out:               0/0
            WLC Client Map-Notify in/out:           0/0
            WLC Map-Notify failures in/out:         0/0
          Dropped control packets in input queue:   0
          Deferred packet transmission:             0/0
            DDT referral deferred/dropped:          0/0
            DDT request deferred/dropped:           0/0
            Map-Reply deferred/dropped:             0/0
            MR negative Map-Reply deferred/dropped: 0/0
            MR Map-Request fwd deferred/dropped:    0/0
            MS Map-Request fwd deferred/dropped:    0/0
            MS proxy Map-Reply deferred/dropped:    0/0
            xTR mcast Map-Notify deferred/dropped:  0/0
            MS Info-Reply deferred/dropped:         0/0
            RTR Map-Register fwd deferred/dropped:  0/0
            RTR Map-Notify fwd deferred/dropped:    0/0
            ETR Info-Request deferred/dropped:      0/0
        Errors:
          Map-Request invalid source rloc drops:    0
          Map-Register invalid source rloc drops:   0
          DDT ITR Map-Requests dropped:             0 (nonce-collision: 0, bad-xTR-nonce: 0)
        Cache Related:
          Cache entries created/deleted:            3/1
          NSF CEF replay entry count                0
          Number of EID-prefixes in map-cache:      2
          Number of negative entries in map-cache:  1
          Total number of RLOCs in map-cache:       1
          Average RLOCs per EID-prefix:             1
        Forwarding:
          Number of data signals processed:         1 (+ dropped 0)
          Number of reachability reports:           0 (+ dropped 0)
        ITR Map-Resolvers:
          Map-Resolver         LastReply  Metric ReqsSent Positive Negative No-Reply
          10.64.4.4            03:13:58        4        1        1        0        0
          10.166.13.13         03:13:58       26        2        0        0        1
        LISP RLOC Statistics - last cleared: never
        Control Packets:
            RTR Map-Requests forwarded:             0
            RTR Map-Notifies forwarded:             0
          DDT-Map-Requests in/out:                  0/0
          DDT-Map-Referrals in/out:                 0/0
        Errors:
          Map-Request format errors:                0
          Map-Reply format errors:                  0
          Map-Referral format errors:               0
          Mapping record TTL alerts:                0
          DDT Requests failed:                      0
        LISP Miscellaneous Statistics - last cleared: never
        Errors:
          Invalid IP version drops:                 0
          Invalid IP header drops:                  0
          Invalid IP proto field drops:             0
          Invalid packet size dropss:               0
          Invalid LISP control port drops:          0
          Invalid LISP checksum drops:              0
          Unsupported LISP packet type drops:       0
          Unknown packet drops:                     0
        '''}

    golden_parsed_output2 = {
        'lisp_router_instances': 
            {0: 
                {'service': 
                    {'ipv6': 
                        {'statistics': 
                            {'EID': 
                                {'control': 
                                    {'authoritative_records_in': '1',
                                    'authoritative_records_out': '1',
                                    'ddt_referral_deferred': '0',
                                    'ddt_referral_dropped': '0',
                                    'ddt_request_deferred': '0',
                                    'ddt_request_dropped': '0',
                                    'deferred_packet_transmission': '0/0',
                                    'dropped_control_packets_in_input_queue': '0',
                                    'encapsulated_map_requests_in': '0',
                                    'encapsulated_map_requests_out': '5',
                                    'etr_info_request_deferred': '0',
                                    'etr_info_request_dropped': '0',
                                    'map_notify_records_in': '2',
                                    'map_notify_records_out': '0',
                                    'map_notify_auth_failures': '0',
                                    'map_register_records_in': '0',
                                    'map_register_records_out': '52',
                                    'map_reply_deferred': '0',
                                    'map_reply_dropped': '0',
                                    'map_reply_records_in': '2',
                                    'map_reply_records_out': '1',
                                    'map_requests_in': '0',
                                    'map_requests_out': '6',
                                    'map_resolver_map_requests_forwarded': '0',
                                    'map_server_af_disabled': '0',
                                    'map_registers_in_auth_failed': '0',
                                    'map_server_map_requests_forwarded': '0',
                                    'map_server_proxy_reply_records_out': '0',
                                    'map_subscribe_failures_in': '0',
                                    'map_subscribe_failures_out': '0',
                                    'map_unsubscribe_failures_in': '0',
                                    'map_unsubscribe_failures_out': '0',
                                    'mr_map_request_fwd_deferred': '0',
                                    'mr_map_request_fwd_dropped': '0',
                                    'mr_negative_map_reply_deferred': '0',
                                    'mr_negative_map_reply_dropped': '0',
                                    'ms_info_reply_deferred': '0',
                                    'ms_info_reply_dropped': '0',
                                    'ms_map_request_fwd_deferred': '0',
                                    'ms_map_request_fwd_dropped': '0',
                                    'ms_proxy_map_reply_deferred': '0',
                                    'ms_proxy_map_reply_dropped': '0',
                                    'negative_records_in': '0',
                                    'negative_records_out': '0',
                                    'non_authoritative_records_in': '1',
                                    'non_authoritative_records_out': '0',
                                    'rloc_probe_map_requests_in': '0',
                                    'rloc_probe_map_requests_out': '1',
                                    'rloc_probe_records_in': '1',
                                    'rloc_probe_records_out': '1',
                                    'rtr_map_notify_fwd_deferred': '0',
                                    'rtr_map_notify_fwd_dropped': '0',
                                    'rtr_map_register_fwd_deferred': '0',
                                    'rtr_map_register_fwd_dropped': '0',
                                    'smr_based_map_requests_in': '0',
                                    'smr_based_map_requests_out': '0',
                                    'wlc_ap_map_notify_in': '0',
                                    'wlc_ap_map_notify_out': '0',
                                    'wlc_ap_map_register_in': '0',
                                    'wlc_ap_map_register_out': '0',
                                    'wlc_client_map_notify_in': '0',
                                    'wlc_client_map_notify_out': '0',
                                    'wlc_client_map_register_in': '0',
                                    'wlc_client_map_register_out': '0',
                                    'wlc_map_notify_failures_in': '0',
                                    'wlc_map_notify_failures_out': '0',
                                    'wlc_map_notify_records_in': '0',
                                    'wlc_map_notify_records_out': '0',
                                    'wlc_map_register_failures_in': '0',
                                    'wlc_map_register_failures_out': '0',
                                    'wlc_map_register_records_in': '0',
                                    'wlc_map_register_records_out': '0',
                                    'wlc_map_subscribe_records_in': '0',
                                    'wlc_map_subscribe_records_out': '2',
                                    'wlc_map_unsubscribe_records_in': '0',
                                    'wlc_map_unsubscribe_records_out': '0',
                                    'xtr_mcast_map_notify_deferred': '0',
                                    'xtr_mcast_map_notify_dropped': '0'},
                                'errors': 
                                    {'average_rlocs_per_eid_prefix': '1',
                                    'cache_entries_created': '4',
                                    'cache_entries_deleted': '2',
                                    'ddt_itr_map_requests_dropped': '0 (nonce-collision: 0, bad-xTR-nonce: 0)',
                                    'map_register_invalid_source_rloc_drops': '0',
                                    'map_request_invalid_source_rloc_drops': '0',
                                    'map_rseolvers': 
                                        {'10.166.13.13': 
                                            {'last_reply': '00:17:11',
                                            'metric': '31',
                                            'negative': 0,
                                            'no_reply': 2,
                                            'positive': 0,
                                            'reqs_sent': 3},
                                        '10.64.4.4': 
                                            {'last_reply': '00:15:36',
                                            'metric': '19',
                                            'negative': 0,
                                            'no_reply': 1,
                                            'positive': 1,
                                            'reqs_sent': 2}},
                                    'number_of_data_signals_processed': '2 (+ dropped 0)',
                                    'number_of_eid_prefixes_in_map_cache': '2',
                                    'number_of_negative_entries_in_map_cache': '1',
                                    'number_of_reachability_reports': '0 (+ dropped 0)',
                                    'total_number_of_rlocs_in_map_cache': '1'},
                                'last_cleared': 'never'},
                                'Miscellaneous':
                                    {'errors': 
                                        {'invalid_ip_header_drops': '0',
                                        'invalid_ip_proto_field_drops': '0',
                                        'invalid_ip_version_drops': '0',
                                        'invalid_lisp_checksum_drops': '0',
                                        'invalid_lisp_control_port_drops': '0',
                                        'invalid_packet_size_dropss': '0',
                                        'unknown_packet_drops': '0',
                                        'unsupported_lisp_packet_type_drops': '0'},
                                    'last_cleared': 'never'},
                                'RLOC': 
                                    {'control': 
                                        {'ddt_map_referrals_in': '0',
                                        'ddt_map_referrals_out': '0',
                                        'ddt_map_requests_in': '0',
                                        'ddt_map_requests_out': '0',
                                        'rtr_map_notifies_forwarded': '0',
                                        'rtr_map_requests_forwarded': '0'},
                                    'errors': 
                                        {'ddt_requests_failed': '0',
                                        'map_referral_format_errors': '0',
                                        'map_reply_format_errors': '0',
                                        'map_request_format_errors': '0',
                                        'mapping_record_ttl_alerts': '0'},
                                    'last_cleared': 'never'}}}}}}}

    golden_output2 = {'execute.return_value': '''
        202-XTR#show lisp all instance-id 101 ipv6 statistics 
        =====================================================
        Output for router lisp 0
        =====================================================
        LISP EID Statistics for instance ID 101 - last cleared: never
        Control Packets:
          Map-Requests in/out:                      0/6
            Encapsulated Map-Requests in/out:       0/5
            RLOC-probe Map-Requests in/out:         0/1
            SMR-based Map-Requests in/out:          0/0
            Map-Requests expired on-queue/no-reply  0/1
            Map-Resolver Map-Requests forwarded:    0
            Map-Server Map-Requests forwarded:      0
          Map-Reply records in/out:                 2/1
            Authoritative records in/out:           1/1
            Non-authoritative records in/out:       1/0
            Negative records in/out:                0/0
            RLOC-probe records in/out:              1/1
            Map-Server Proxy-Reply records out:     0
          WLC Map-Subscribe records in/out:         0/2
            Map-Subscribe failures in/out:          0/0
          WLC Map-Unsubscribe records in/out:       0/0
            Map-Unsubscribe failures in/out:        0/0
          Map-Register records in/out:              0/52
            Map-Server AF disabled:                 0
            Authentication failures:                0
          WLC Map-Register records in/out:          0/0
            WLC AP Map-Register in/out:             0/0
            WLC Client Map-Register in/out:         0/0
            WLC Map-Register failures in/out:       0/0
          Map-Notify records in/out:                2/0
            Authentication failures:                0
          WLC Map-Notify records in/out:            0/0
            WLC AP Map-Notify in/out:               0/0
            WLC Client Map-Notify in/out:           0/0
            WLC Map-Notify failures in/out:         0/0
          Dropped control packets in input queue:   0
          Deferred packet transmission:             0/0
            DDT referral deferred/dropped:          0/0
            DDT request deferred/dropped:           0/0
            Map-Reply deferred/dropped:             0/0
            MR negative Map-Reply deferred/dropped: 0/0
            MR Map-Request fwd deferred/dropped:    0/0
            MS Map-Request fwd deferred/dropped:    0/0
            MS proxy Map-Reply deferred/dropped:    0/0
            xTR mcast Map-Notify deferred/dropped:  0/0
            MS Info-Reply deferred/dropped:         0/0
            RTR Map-Register fwd deferred/dropped:  0/0
            RTR Map-Notify fwd deferred/dropped:    0/0
            ETR Info-Request deferred/dropped:      0/0
        Errors:
          Map-Request invalid source rloc drops:    0
          Map-Register invalid source rloc drops:   0
          DDT ITR Map-Requests dropped:             0 (nonce-collision: 0, bad-xTR-nonce: 0)
        Cache Related:
          Cache entries created/deleted:            4/2
          NSF CEF replay entry count                0
          Number of EID-prefixes in map-cache:      2
          Number of negative entries in map-cache:  1
          Total number of RLOCs in map-cache:       1
          Average RLOCs per EID-prefix:             1
        Forwarding:
          Number of data signals processed:         2 (+ dropped 0)
          Number of reachability reports:           0 (+ dropped 0)
        ITR Map-Resolvers:
          Map-Resolver         LastReply  Metric ReqsSent Positive Negative No-Reply
          10.64.4.4            00:15:36       19        2        1        0        1
          10.166.13.13         00:17:11       31        3        0        0        2
        LISP RLOC Statistics - last cleared: never
        Control Packets:
            RTR Map-Requests forwarded:             0
            RTR Map-Notifies forwarded:             0
          DDT-Map-Requests in/out:                  0/0
          DDT-Map-Referrals in/out:                 0/0
        Errors:
          Map-Request format errors:                0
          Map-Reply format errors:                  0
          Map-Referral format errors:               0
          Mapping record TTL alerts:                0
          DDT Requests failed:                      0
        LISP Miscellaneous Statistics - last cleared: never
        Errors:
          Invalid IP version drops:                 0
          Invalid IP header drops:                  0
          Invalid IP proto field drops:             0
          Invalid packet size dropss:               0
          Invalid LISP control port drops:          0
          Invalid LISP checksum drops:              0
          Unsupported LISP packet type drops:       0
          Unknown packet drops:                     0
        '''}

    golden_parsed_output3 = {
        'lisp_router_instances': 
            {0: 
                {'service': 
                    {'ethernet': 
                        {'statistics': 
                            {'EID': 
                                {'control': 
                                    {'authoritative_records_in': '0',
                                    'authoritative_records_out': '0',
                                    'encapsulated_map_requests_in': '0',
                                    'encapsulated_map_requests_out': '0',
                                    'extranet_smr_cross_iid_map_requests_in': '0',
                                    'map_notify_records_in': '372',
                                    'map_notify_records_out': '0',
                                    'map_notify_auth_failures': '0',
                                    'map_register_records_in': '0',
                                    'map_register_records_out': '6460',
                                    'map_reply_records_in': '0',
                                    'map_reply_records_out': '0',
                                    'map_requests_in': '0',
                                    'map_requests_out': '0',
                                    'map_resolver_map_requests_forwarded': '0',
                                    'map_server_af_disabled': '0',
                                    'map_registers_in_auth_failed': '0',
                                    'map_server_map_requests_forwarded': '0',
                                    'map_server_proxy_reply_records_out': '0',
                                    'map_subscribe_failures_in': '0',
                                    'map_subscribe_failures_out': '0',
                                    'map_unsubscribe_failures_in': '0',
                                    'map_unsubscribe_failures_out': '0',
                                    'negative_records_in': '0',
                                    'negative_records_out': '0',
                                    'non_authoritative_records_in': '0',
                                    'non_authoritative_records_out': '0',
                                    'rloc_probe_map_requests_in': '0',
                                    'rloc_probe_map_requests_out': '0',
                                    'rloc_probe_records_in': '0',
                                    'rloc_probe_records_out': '0',
                                    'smr_based_map_requests_in': '0',
                                    'smr_based_map_requests_out': '0',
                                    'wlc_ap_map_notify_in': '0',
                                    'wlc_ap_map_notify_out': '0',
                                    'wlc_ap_map_register_in': '0',
                                    'wlc_ap_map_register_out': '0',
                                    'wlc_client_map_notify_in': '30',
                                    'wlc_client_map_notify_out': '0',
                                    'wlc_client_map_register_in': '0',
                                    'wlc_client_map_register_out': '0',
                                    'wlc_map_notify_failures_in': '0',
                                    'wlc_map_notify_failures_out': '0',
                                    'wlc_map_notify_records_in': '30',
                                    'wlc_map_notify_records_out': '0',
                                    'wlc_map_register_failures_in': '0',
                                    'wlc_map_register_failures_out': '0',
                                    'wlc_map_register_records_in': '0',
                                    'wlc_map_register_records_out': '0',
                                    'wlc_map_subscribe_records_in': '0',
                                    'wlc_map_subscribe_records_out': '15',
                                    'wlc_map_unsubscribe_records_in': '0',
                                    'wlc_map_unsubscribe_records_out': '0'},
                                'errors': 
                                    {'average_rlocs_per_eid_prefix': '0',
                                    'cache_entries_created': '2',
                                    'cache_entries_deleted': '2',
                                    'ddt_itr_map_requests_dropped': '0 (nonce-collision: 0, bad-xTR-nonce: 0)',
                                    'map_register_invalid_source_rloc_drops': '0',
                                    'map_request_invalid_source_rloc_drops': '0',
                                    'map_rseolvers': 
                                        {'10.94.44.44': 
                                            {'last_reply': 'never',
                                            'metric': '1',
                                            'negative': 0,
                                            'no_reply': 1,
                                            'positive': 1,
                                            'reqs_sent': 6},
                                        '10.84.66.66': 
                                            {'last_reply': 'never',
                                            'metric': 'Unreach',
                                            'negative': 0,
                                            'no_reply': 0,
                                            'positive': 0,
                                            'reqs_sent': 0}},
                                    'number_of_data_signals_processed': '0 (+ dropped 0)',
                                    'number_of_eid_prefixes_in_map_cache': '0',
                                    'number_of_negative_entries_in_map_cache': '0',
                                    'number_of_reachability_reports': '0 (+ dropped 0)',
                                    'number_of_rejected_eid_prefixes_due_to_limit_': '0',
                                    'number_of_smr_signals_dropped': '0',
                                    'total_number_of_rlocs_in_map_cache': '0'},
                                'last_cleared': 'never'},
                            'Miscellaneous': 
                                {'errors': 
                                    {'invalid_ip_header_drops': '0',
                                    'invalid_ip_proto_field_drops': '0',
                                    'invalid_ip_version_drops': '0',
                                    'invalid_lisp_checksum_drops': '0',
                                    'invalid_lisp_control_port_drops': '0',
                                    'invalid_packet_size_dropss': '0',
                                    'unknown_packet_drops': '0',
                                    'unsupported_lisp_packet_type_drops': '0'},
                                'last_cleared': 'never'},
                            'RLOC': 
                                {'control': 
                                    {'ddt_map_referrals_in': '0',
                                    'ddt_map_referrals_out': '0',
                                    'ddt_map_requests_in': '0',
                                    'ddt_map_requests_out': '0',
                                    'rtr_map_notifies_forwarded': '0',
                                    'rtr_map_requests_forwarded': '0'},
                                'errors': 
                                    {'ddt_requests_failed': '0',
                                    'map_referral_format_errors': '0',
                                    'map_reply_format_errors': '0',
                                    'map_request_format_errors': '0',
                                    'mapping_record_ttl_alerts': '0'},
                                'last_cleared': 'never'}}}}}}}

    golden_output3 = {'execute.return_value': '''
        OTT-LISP-C3K-3-xTR1#show lisp all instance-id * ethernet statistics

        =================================================
        Output for router lisp 0 instance-id 0
        =================================================
        % EID table not enabled for MAC.

        =================================================
        Output for router lisp 0 instance-id 1
        =================================================
        LISP EID Statistics for instance ID 1 - last cleared: never
        Control Packets:
          Map-Requests in/out:                              8/40
            Encapsulated Map-Requests in/out:               8/36
            RLOC-probe Map-Requests in/out:                 0/4
            SMR-based Map-Requests in/out:                  0/4
            Extranet SMR cross-IID Map-Requests in:         0
            Map-Requests expired on-queue/no-reply          0/13
            Map-Resolver Map-Requests forwarded:            0
            Map-Server Map-Requests forwarded:              0
          Map-Reply records in/out:                         0/0
            Authoritative records in/out:                   0/0
            Non-authoritative records in/out:               0/0
            Negative records in/out:                        0/0
            RLOC-probe records in/out:                      0/0
            Map-Server Proxy-Reply records out:             0
          WLC Map-Subscribe records in/out:                 0/15
            Map-Subscribe failures in/out:                  0/0
          WLC Map-Unsubscribe records in/out:               0/0
            Map-Unsubscribe failures in/out:                0/0
          Map-Register records in/out:                      0/15516
            Map-Server AF disabled:                         0
            Authentication failures:                        0
          WLC Map-Register records in/out:                  0/0
            WLC AP Map-Register in/out:                     0/0
            WLC Client Map-Register in/out:                 0/0
            WLC Map-Register failures in/out:               0/0
          Map-Notify records in/out:                        2014/0
            Authentication failures:                        0
          WLC Map-Notify records in/out:                    453/0
            WLC AP Map-Notify in/out:                       12/0
            WLC Client Map-Notify in/out:                   441/0
            WLC Map-Notify failures in/out:                 0/0
        Errors:
          Map-Request invalid source rloc drops:            0
          Map-Register invalid source rloc drops:           0
          DDT ITR Map-Requests dropped:                     0 (nonce-collision: 0, bad-xTR-nonce: 0)
        Cache Related:
          Cache entries created/deleted:                    166/162
          NSF CEF replay entry count                        0
          Number of EID-prefixes in map-cache:              4
          Number of rejected EID-prefixes due to limit :    0
          Number of negative entries in map-cache:          0
          Total number of RLOCs in map-cache:               4
          Average RLOCs per EID-prefix:                     1
        Forwarding:
          Number of data signals processed:                 0 (+ dropped 40)
          Number of reachability reports:                   0 (+ dropped 0)
          Number of SMR signals dropped:                    0
        ITR Map-Resolvers:
          Map-Resolver         LastReply  Metric ReqsSent Positive Negative No-Reply
          10.94.44.44          never           1      306       18        0       66
          10.84.66.66          never     Unreach        0        0        0        0
        LISP RLOC Statistics - last cleared: never
        Control Packets:
            RTR Map-Requests forwarded:                     0
            RTR Map-Notifies forwarded:                     0
          DDT-Map-Requests in/out:                          0/0
          DDT-Map-Referrals in/out:                         0/0
        Errors:
          Map-Request format errors:                        0
          Map-Reply format errors:                          0
          Map-Referral format errors:                       0
          Mapping record TTL alerts:                        0
          DDT Requests failed:                              0
        LISP Miscellaneous Statistics - last cleared: never
        Errors:
          Invalid IP version drops:                         0
          Invalid IP header drops:                          0
          Invalid IP proto field drops:                     0
          Invalid packet size dropss:                       0
          Invalid LISP control port drops:                  0
          Invalid LISP checksum drops:                      0
          Unsupported LISP packet type drops:               0
          Unknown packet drops:                             0

        =================================================
        Output for router lisp 0 instance-id 2
        =================================================
        LISP EID Statistics for instance ID 2 - last cleared: never
        Control Packets:
          Map-Requests in/out:                              0/0
            Encapsulated Map-Requests in/out:               0/0
            RLOC-probe Map-Requests in/out:                 0/0
            SMR-based Map-Requests in/out:                  0/0
            Extranet SMR cross-IID Map-Requests in:         0
            Map-Requests expired on-queue/no-reply          0/0
            Map-Resolver Map-Requests forwarded:            0
            Map-Server Map-Requests forwarded:              0
          Map-Reply records in/out:                         0/0
            Authoritative records in/out:                   0/0
            Non-authoritative records in/out:               0/0
            Negative records in/out:                        0/0
            RLOC-probe records in/out:                      0/0
            Map-Server Proxy-Reply records out:             0
          WLC Map-Subscribe records in/out:                 0/15
            Map-Subscribe failures in/out:                  0/0
          WLC Map-Unsubscribe records in/out:               0/0
            Map-Unsubscribe failures in/out:                0/0
          Map-Register records in/out:                      0/6460
            Map-Server AF disabled:                         0
            Authentication failures:                        0
          WLC Map-Register records in/out:                  0/0
            WLC AP Map-Register in/out:                     0/0
            WLC Client Map-Register in/out:                 0/0
            WLC Map-Register failures in/out:               0/0
          Map-Notify records in/out:                        372/0
            Authentication failures:                        0
          WLC Map-Notify records in/out:                    30/0
            WLC AP Map-Notify in/out:                       0/0
            WLC Client Map-Notify in/out:                   30/0
            WLC Map-Notify failures in/out:                 0/0
        Errors:
          Map-Request invalid source rloc drops:            0
          Map-Register invalid source rloc drops:           0
          DDT ITR Map-Requests dropped:                     0 (nonce-collision: 0, bad-xTR-nonce: 0)
        Cache Related:
          Cache entries created/deleted:                    2/2
          NSF CEF replay entry count                        0
          Number of EID-prefixes in map-cache:              0
          Number of rejected EID-prefixes due to limit :    0
          Number of negative entries in map-cache:          0
          Total number of RLOCs in map-cache:               0
          Average RLOCs per EID-prefix:                     0
        Forwarding:
          Number of data signals processed:                 0 (+ dropped 0)
          Number of reachability reports:                   0 (+ dropped 0)
          Number of SMR signals dropped:                    0
        ITR Map-Resolvers:
          Map-Resolver         LastReply  Metric ReqsSent Positive Negative No-Reply
          10.94.44.44          never           1        6        1        0        1
          10.84.66.66          never     Unreach        0        0        0        0
        LISP RLOC Statistics - last cleared: never
        Control Packets:
            RTR Map-Requests forwarded:                     0
            RTR Map-Notifies forwarded:                     0
          DDT-Map-Requests in/out:                          0/0
          DDT-Map-Referrals in/out:                         0/0
        Errors:
          Map-Request format errors:                        0
          Map-Reply format errors:                          0
          Map-Referral format errors:                       0
          Mapping record TTL alerts:                        0
          DDT Requests failed:                              0
        LISP Miscellaneous Statistics - last cleared: never
        Errors:
          Invalid IP version drops:                         0
          Invalid IP header drops:                          0
          Invalid IP proto field drops:                     0
          Invalid packet size dropss:                       0
          Invalid LISP control port drops:                  0
          Invalid LISP checksum drops:                      0
          Unsupported LISP packet type drops:               0
          Unknown packet drops:                             0

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

    def test_show_lisp_service_statistics_full1(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output1)
        obj = ShowLispServiceStatistics(device=self.device)
        parsed_output = obj.parse(service='ipv4', instance_id='101')
        self.assertEqual(parsed_output, self.golden_parsed_output1)

    def test_show_lisp_service_statistics_full2(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output2)
        obj = ShowLispServiceStatistics(device=self.device)
        parsed_output = obj.parse(service='ipv6', instance_id='101')
        self.assertEqual(parsed_output, self.golden_parsed_output2)

    def test_show_lisp_service_statistics_full3(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output3)
        obj = ShowLispServiceStatistics(device=self.device)
        parsed_output = obj.parse(service='ethernet', instance_id='*')
        self.assertEqual(parsed_output, self.golden_parsed_output3)

    def test_show_lisp_service_statistics_empty(self):
        self.maxDiff = None
        self.device = Mock(**self.empty_output)
        obj = ShowLispServiceStatistics(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse(service='ipv4', instance_id='*')



if __name__ == '__main__':
    unittest.main()
