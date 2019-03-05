
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
from genie.libs.parser.iosxe.show_ospf import ShowIpOspf,\
                                   ShowIpOspfInterface,\
                                   ShowIpOspfNeighborDetail,\
                                   ShowIpOspfShamLinks,\
                                   ShowIpOspfVirtualLinks,\
                                   ShowIpOspfDatabase,\
                                   ShowIpOspfDatabaseRouter,\
                                   ShowIpOspfDatabaseExternal,\
                                   ShowIpOspfDatabaseNetwork,\
                                   ShowIpOspfDatabaseSummary,\
                                   ShowIpOspfDatabaseOpaqueArea,\
                                   ShowIpOspfMplsLdpInterface,\
                                   ShowIpOspfMplsTrafficEngLink


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
                                            {'1.1.0.0/16': 
                                                {'advertise': True,
                                                'cost': 10,
                                                'prefix': '1.1.0.0/16'}},
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
                                'router_id': '1.1.1.1',
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
                                            {'1.1.1.0/24': 
                                                {'advertise': True,
                                                'prefix': '1.1.1.0/24'}},
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
                                'router_id': '11.11.11.11',
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
         Routing Process "ospf 1" with ID 1.1.1.1
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
                 1.1.0.0/16 Active(10 - configured) Advertise
                Number of LSA 19. Checksum Sum 0x07CF20
                Number of opaque link LSA 0. Checksum Sum 0x000000
                Number of DCbitless LSA 5
                Number of indication LSA 0
                Number of DoNotAge LSA 0
                Flood list length 0

         Routing Process "ospf 2" with ID 11.11.11.11
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
                 1.1.1.0/24 Passive Advertise
                Number of LSA 11. Checksum Sum 0x053FED
                Number of opaque link LSA 0. Checksum Sum 0x000000
                Number of DCbitless LSA 1
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

    def test_show_ip_ospf_empty(self):
        self.maxDiff = None
        self.device = Mock(**self.empty_output)
        obj = ShowIpOspf(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()


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
                                                'bdr_ip_addr': '20.1.5.5',
                                                'bdr_router_id': '55.55.55.55',
                                                'bfd': 
                                                    {'enable': False},
                                                'cost': 1,
                                                'dead_interval': 40,
                                                'demand_circuit': False,
                                                'dr_ip_addr': '20.1.5.1',
                                                'dr_router_id': '11.11.11.11',
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
                                                'ip_address': '20.1.5.1/24',
                                                'last_flood_scan_length': 0,
                                                'last_flood_scan_time_msec': 0,
                                                'line_protocol': True,
                                                'max_flood_scan_length': 7,
                                                'max_flood_scan_time_msec': 1,
                                                'name': 'GigabitEthernet3',
                                                'neighbors': 
                                                    {'55.55.55.55': 
                                                        {'bdr_router_id': '55.55.55.55'}},
                                                'next': '0x0(0)/0x0(0)/0x0(0)',
                                                'passive': False,
                                                'priority': 1,
                                                'retransmit_interval': 5,
                                                'router_id': '11.11.11.11',
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
                                            {'11.11.11.11 22.22.22.22': 
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
                                                'router_id': '11.11.11.11',
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
                                                'bdr_router_id': '1.1.1.1',
                                                'bfd': 
                                                    {'enable': False},
                                                'cost': 1,
                                                'dead_interval': 40,
                                                'demand_circuit': False,
                                                'dr_ip_addr': '10.1.4.4',
                                                'dr_router_id': '4.4.4.4',
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
                                                    {'4.4.4.4': 
                                                        {'dr_router_id': '4.4.4.4'}},
                                                'next': '0x0(0)/0x0(0)/0x0(0)',
                                                'passive': False,
                                                'priority': 1,
                                                'retransmit_interval': 5,
                                                'router_id': '1.1.1.1',
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
                                                'bdr_router_id': '2.2.2.2',
                                                'bfd': 
                                                    {'enable': False},
                                                'cost': 1,
                                                'dead_interval': 40,
                                                'demand_circuit': False,
                                                'dr_ip_addr': '10.1.2.1',
                                                'dr_router_id': '1.1.1.1',
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
                                                    {'2.2.2.2': 
                                                        {'bdr_router_id': '2.2.2.2'}},
                                                'next': '0x0(0)/0x0(0)/0x0(0)',
                                                'passive': False,
                                                'prefix_suppression': True,
                                                'priority': 1,
                                                'retransmit_interval': 5,
                                                'router_id': '1.1.1.1',
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
                                                'ip_address': '1.1.1.1/32',
                                                'line_protocol': True,
                                                'name': 'Loopback0',
                                                'router_id': '1.1.1.1',
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
                                                'ip_address': '44.44.44.44/32',
                                                'line_protocol': True,
                                                'name': 'Loopback1',
                                                'router_id': '4.4.4.4',
                                                'stub_host': True,
                                                'topology': 
                                                    {0: 
                                                        {'cost': 1,
                                                        'disabled': False,
                                                        'name': 'Base',
                                                        'shutdown': False}}}},
                                        'virtual_links': 
                                            {'0.0.0.1 4.4.4.4': 
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
                                                'ip_address': '20.3.4.4/24',
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
                                                'router_id': '4.4.4.4',
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
                                                'bdr_ip_addr': '20.2.4.2',
                                                'bdr_router_id': '2.2.2.2',
                                                'bfd': 
                                                    {'enable': False},
                                                'cost': 1,
                                                'dead_interval': 40,
                                                'demand_circuit': False,
                                                'dr_ip_addr': '20.2.4.4',
                                                'dr_router_id': '4.4.4.4',
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
                                                'ip_address': '20.2.4.4/24',
                                                'last_flood_scan_length': 1,
                                                'last_flood_scan_time_msec': 0,
                                                'line_protocol': True,
                                                'lls': True,
                                                'max_flood_scan_length': 10,
                                                'max_flood_scan_time_msec': 10,
                                                'name': 'GigabitEthernet0/0',
                                                'neighbors': 
                                                    {'2.2.2.2': 
                                                        {'bdr_router_id': '2.2.2.2'}},
                                                'next': '0x0(0)/0x0(0)',
                                                'oob_resync_timeout': 40,
                                                'passive': False,
                                                'priority': 1,
                                                'retransmit_interval': 5,
                                                'router_id': '4.4.4.4',
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
                                                'bdr_ip_addr': '20.3.4.3',
                                                'bdr_router_id': '3.3.3.3',
                                                'bfd': 
                                                    {'enable': False},
                                                'cost': 1,
                                                'dead_interval': 40,
                                                'demand_circuit': False,
                                                'dr_ip_addr': '20.3.4.4',
                                                'dr_router_id': '4.4.4.4',
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
                                                'ip_address': '20.3.4.4/24',
                                                'last_flood_scan_length': 0,
                                                'last_flood_scan_time_msec': 0,
                                                'line_protocol': True,
                                                'lls': True,
                                                'max_flood_scan_length': 11,
                                                'max_flood_scan_time_msec': 1,
                                                'name': 'GigabitEthernet0/1',
                                                'neighbors': 
                                                    {'3.3.3.3': 
                                                        {'bdr_router_id': '3.3.3.3'}},
                                                'next': '0x0(0)/0x0(0)',
                                                'oob_resync_timeout': 40,
                                                'passive': False,
                                                'priority': 1,
                                                'retransmit_interval': 5,
                                                'router_id': '4.4.4.4',
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
                                                    'ip_address': '4.4.4.4/32',
                                                    'line_protocol': True,
                                                    'name': 'Loopback0',
                                                    'router_id': '4.4.4.4',
                                                    'stub_host': True,
                                                    'topology': 
                                                        {0: 
                                                            {'cost': 1,
                                                            'disabled': False,
                                                            'name': 'Base',
                                                            'shutdown': False}}}}}}}}}}}}}

    def test_show_ip_ospf_interface_full1(self):
        
        self.maxDiff = None

        def mapper(key):
            return self.outputs[key]

        raw1 = '''\
            R1_ospf_xe#show ip ospf interface
            Loopback0 is up, line protocol is up 
              Internet Address 1.1.1.1/32, Interface ID 11, Area 0
              Attached via Interface Enable
              Process ID 1, Router ID 1.1.1.1, Network Type LOOPBACK, Cost: 1
              Topology-MTID    Cost    Disabled    Shutdown      Topology Name
                    0           1         no          no            Base
              Enabled by interface config, including secondary ip addresses
              Loopback interface is treated as a stub Host
            GigabitEthernet2 is up, line protocol is up (connected)
              Internet Address 10.1.2.1/24, Interface ID 8, Area 0
              Attached via Interface Enable
              Process ID 1, Router ID 1.1.1.1, Network Type BROADCAST, Cost: 1
              Topology-MTID    Cost    Disabled    Shutdown      Topology Name
                    0           1         no          no            Base
              Enabled by interface config, including secondary ip addresses
              Transmit Delay is 1 sec, State DR, Priority 1
              Designated Router (ID) 1.1.1.1, Interface address 10.1.2.1
              Backup Designated router (ID) 2.2.2.2, Interface address 10.1.2.2
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
                Adjacent with neighbor 2.2.2.2  (Backup Designated Router)
              Suppress hello for 0 neighbor(s)
            GigabitEthernet1 is up, line protocol is up 
              Internet Address 10.1.4.1/24, Interface ID 7, Area 0
              Attached via Interface Enable
              Process ID 1, Router ID 1.1.1.1, Network Type BROADCAST, Cost: 1
              Topology-MTID    Cost    Disabled    Shutdown      Topology Name
                    0           1         no          no            Base
              Enabled by interface config, including secondary ip addresses
              Transmit Delay is 1 sec, State BDR, Priority 1
              Designated Router (ID) 4.4.4.4, Interface address 10.1.4.4
              Backup Designated router (ID) 1.1.1.1, Interface address 10.1.4.1
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
                Adjacent with neighbor 4.4.4.4  (Designated Router)
              Suppress hello for 0 neighbor(s)
            OSPF_SL1 is up, line protocol is up 
              Internet Address 0.0.0.0/0, Interface ID 14, Area 1
              Attached via Not Attached
              Process ID 2, Router ID 11.11.11.11, Network Type SHAM_LINK, Cost: 111
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
                Adjacent with neighbor 22.22.22.22
              Suppress hello for 0 neighbor(s)
            GigabitEthernet3 is up, line protocol is up 
              Internet Address 20.1.5.1/24, Interface ID 9, Area 1
              Attached via Interface Enable
              Process ID 2, Router ID 11.11.11.11, Network Type BROADCAST, Cost: 1
              Topology-MTID    Cost    Disabled    Shutdown      Topology Name
                    0           1         no          no            Base
              Enabled by interface config, including secondary ip addresses
              Transmit Delay is 1 sec, State DR, Priority 1
              Designated Router (ID) 11.11.11.11, Interface address 20.1.5.1
              Backup Designated router (ID) 55.55.55.55, Interface address 20.1.5.5
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
                Adjacent with neighbor 55.55.55.55  (Backup Designated Router)
              Suppress hello for 0 neighbor(s)
            '''

        raw2 = '''\
            R1_ospf_xe#show ip ospf sham-links | i OSPF_SL1
              Sham Link OSPF_SL1 to address 22.22.22.22 is up
            '''

        raw3 = '''\
            R1_ospf_xe#show running-config | i sham-link | i 22.22.22.22
              area 1 sham-link 11.11.11.11 22.22.22.22 cost 111 ttl-security hops 3
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
                area 1 virtual-link 5.5.5.5
                area 1 sham-link 11.11.11.11 22.22.22.22 cost 111 ttl-security hops 3
                redistribute bgp
            '''

        self.outputs = {}
        self.outputs['show ip ospf interface'] = raw1
        self.outputs['show ip ospf sham-links | i OSPF_SL1'] = raw2
        self.outputs['show running-config | i sham-link | i 22.22.22.22'] = raw3
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
              Internet Address 20.3.4.4/24, Area 1, Attached via Not Attached
              Process ID 2, Router ID 4.4.4.4, Network Type VIRTUAL_LINK, Cost: 1
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
                Adjacent with neighbor 3.3.3.3
              Suppress hello for 0 neighbor(s)
            Loopback0 is up, line protocol is up 
              Internet Address 4.4.4.4/32, Area 1, Attached via Interface Enable
              Process ID 1, Router ID 4.4.4.4, Network Type LOOPBACK, Cost: 1
              Topology-MTID    Cost    Disabled    Shutdown      Topology Name
                    0           1         no          no            Base
              Enabled by interface config, including secondary ip addresses
              Loopback interface is treated as a stub Host
            GigabitEthernet0/1 is up, line protocol is up 
              Internet Address 20.3.4.4/24, Area 1, Attached via Interface Enable
              Process ID 1, Router ID 4.4.4.4, Network Type BROADCAST, Cost: 1
              Topology-MTID    Cost    Disabled    Shutdown      Topology Name
                    0           1         no          no            Base
              Enabled by interface config, including secondary ip addresses
              Transmit Delay is 1 sec, State DR, Priority 1
              Designated Router (ID) 4.4.4.4, Interface address 20.3.4.4
              Backup Designated router (ID) 3.3.3.3, Interface address 20.3.4.3
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
                Adjacent with neighbor 3.3.3.3  (Backup Designated Router)
              Suppress hello for 0 neighbor(s)
            GigabitEthernet0/0 is up, line protocol is up 
              Internet Address 20.2.4.4/24, Area 1, Attached via Interface Enable
              Process ID 1, Router ID 4.4.4.4, Network Type BROADCAST, Cost: 1
              Topology-MTID    Cost    Disabled    Shutdown      Topology Name
                    0           1         no          no            Base
              Enabled by interface config, including secondary ip addresses
              Transmit Delay is 1 sec, State DR, Priority 1
              Designated Router (ID) 4.4.4.4, Interface address 20.2.4.4
              Backup Designated router (ID) 2.2.2.2, Interface address 20.2.4.2
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
                Adjacent with neighbor 2.2.2.2  (Backup Designated Router)
              Suppress hello for 0 neighbor(s)
            Loopback1 is up, line protocol is up 
              Internet Address 44.44.44.44/32, Area 1, Attached via Interface Enable
              Process ID 2, Router ID 4.4.4.4, Network Type LOOPBACK, Cost: 1
              Topology-MTID    Cost    Disabled    Shutdown      Topology Name
                    0           1         no          no            Base
              Enabled by interface config, including secondary ip addresses
              Loopback interface is treated as a stub Host
            '''

        raw2 = '''\
            R1_ospf_xe#show ip ospf virtual-links | i OSPF_VL1
              Virtual Link OSPF_VL1 to router 5.5.5.5 is down
            '''

        raw3 = '''\
            R1_ospf_xe#show running-config | i virtual-link | i 5.5.5.5
              area 1 virtual-link 5.5.5.5
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
                area 1 virtual-link 5.5.5.5
                area 1 sham-link 11.11.11.11 22.22.22.22 cost 111 ttl-security hops 3
                redistribute bgp
            '''

        self.outputs = {}
        self.outputs['show ip ospf interface'] = raw1
        self.outputs['show ip ospf virtual-links | i OSPF_VL1'] = raw2
        self.outputs['show running-config | i virtual-link | i 5.5.5.5'] = raw3
        self.outputs['show running-config | section router ospf 1'] = raw4
        self.outputs['show running-config | section router ospf 2'] = raw5

        self.device.execute = Mock()
        self.device.execute.side_effect = mapper
        
        obj = ShowIpOspfInterface(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output2)

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
                                                    {'55.55.55.55': 
                                                        {'address': '20.1.5.5',
                                                        'bdr_ip_addr': '20.1.5.5',
                                                        'dead_timer': '00:00:34',
                                                        'dr_ip_addr': '20.1.5.1',
                                                        'first': '0x0(0)/0x0(0)/0x0(0)',
                                                        'index': '1/1/1,',
                                                        'interface': 'GigabitEthernet3',
                                                        'neighbor_router_id': '55.55.55.55',
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
                                            {'11.11.11.11 22.22.22.22': 
                                                {'neighbors': 
                                                    {'22.22.22.22': 
                                                        {'address': '22.22.22.22',
                                                        'bdr_ip_addr': '0.0.0.0',
                                                        'dead_timer': '00:00:35',
                                                        'dr_ip_addr': '0.0.0.0',
                                                        'first': '0x0(0)/0x0(0)/0x0(0)',
                                                        'hello_options': '0x2',
                                                        'dbd_options': '0x42',
                                                        'index': '1/2/2,',
                                                        'interface': 'OSPF_SL1',
                                                        'neighbor_router_id': '22.22.22.22',
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
                                                    {'4.4.4.4': 
                                                        {'address': '10.1.4.4',
                                                        'bdr_ip_addr': '10.1.4.1',
                                                        'dead_timer': '00:00:35',
                                                        'dr_ip_addr': '10.1.4.4',
                                                        'first': '0x0(0)/0x0(0)/0x0(0)',
                                                        'index': '1/1/1,',
                                                        'interface': 'GigabitEthernet1',
                                                        'neighbor_router_id': '4.4.4.4',
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
                                                    {'2.2.2.2': 
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
                                                        'neighbor_router_id': '2.2.2.2',
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
                                                    {'2.2.2.2': 
                                                        {'address': '20.2.4.2',
                                                        'bdr_ip_addr': '20.2.4.2',
                                                        'dead_timer': '00:00:34',
                                                        'dr_ip_addr': '20.2.4.4',
                                                        'first': '0x0(0)/0x0(0)',
                                                        'index': '1/1,',
                                                        'interface': 'GigabitEthernet0/0',
                                                        'neighbor_router_id': '2.2.2.2',
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
                                                    {'3.3.3.3': 
                                                        {'address': '20.3.4.3',
                                                        'bdr_ip_addr': '20.3.4.3',
                                                        'dead_timer': '00:00:33',
                                                        'dr_ip_addr': '20.3.4.4',
                                                        'first': '0x0(0)/0x0(0)',
                                                        'hello_options': '0x2',
                                                        'dbd_options': '0x42',
                                                        'index': '2/2,',
                                                        'interface': 'GigabitEthernet0/1',
                                                        'neighbor_router_id': '3.3.3.3',
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
                                            {'0.0.0.1 4.4.4.4,': 
                                                {'neighbors': 
                                                    {'3.3.3.3': 
                                                        {'address': '20.2.3.3',
                                                        'bdr_ip_addr': '0.0.0.0',
                                                        'dead_timer': '00:00:41',
                                                        'dr_ip_addr': '0.0.0.0',
                                                        'first': '0x0(0)/0x0(0)',
                                                        'hello_options': '0x2',
                                                        'dbd_options': '0x42',
                                                        'index': '1/3,',
                                                        'interface': 'OSPF_VL1',
                                                        'neighbor_router_id': '3.3.3.3',
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
                                                    {'20.51.55.33': 
                                                        {'address': '20.51.55.33',
                                                        'bdr_ip_addr': '0.0.0.0',
                                                        'dead_timer': '00:00:03',
                                                        'dr_ip_addr': '20.51.55.38',
                                                        'first': '0x0(0)/0x625F62BC(13775196)',
                                                        'hello_options': '0x2',
                                                        'index': '2/2,',
                                                        'interface': 'TenGigabitEthernet3/1/1',
                                                        'neighbor_router_id': '20.51.55.33',
                                                        'next': '0x0(0)/0x625F62BC(13775196)',
                                                        'priority': 0,
                                                        'state': 'full',
                                                        'statistics': {'last_retrans_max_scan_length': 2,
                                                                     'last_retrans_max_scan_time_msec': 4,
                                                                     'last_retrans_scan_length': 0,
                                                                     'last_retrans_scan_time_msec': 0,
                                                                     'nbr_event_count': 12,
                                                                     'nbr_retrans_qlen': 3,
                                                                     'total_retransmission': 5},
                                                        'uptime': '3d21h'}}},
                                            'TenGigabitEthernet3/1/2': 
                                                {'neighbors': 
                                                    {'20.51.55.41': 
                                                        {'address': '20.51.55.41',
                                                        'bdr_ip_addr': '0.0.0.0',
                                                        'dead_timer': '00:00:03',
                                                        'dr_ip_addr': '20.51.55.46',
                                                        'first': '0x0(0)/0x0(0)',
                                                        'hello_options': '0x2',
                                                        'index': '1/1,',
                                                        'interface': 'TenGigabitEthernet3/1/2',
                                                        'neighbor_router_id': '20.51.55.41',
                                                        'next': '0x0(0)/0x0(0)',
                                                        'priority': 0,
                                                        'state': 'full',
                                                        'statistics': {'last_retrans_max_scan_length': 1,
                                                                     'last_retrans_max_scan_time_msec': 0,
                                                                     'last_retrans_scan_length': 0,
                                                                     'last_retrans_scan_time_msec': 0,
                                                                     'nbr_event_count': 22,
                                                                     'nbr_retrans_qlen': 0,
                                                                     'total_retransmission': 1},
                                                        'uptime': '3d00h'}}},
                                            'TenGigabitEthernet3/1/5': 
                                                {'neighbors': 
                                                    {'20.51.55.49': 
                                                        {'address': '20.51.55.49',
                                                        'bdr_ip_addr': '0.0.0.0',
                                                        'dead_timer': '00:00:03',
                                                        'dr_ip_addr': '20.51.55.54',
                                                        'first': '0x0(0)/0x625F6304(13775194)',
                                                        'hello_options': '0x2',
                                                        'index': '3/3,',
                                                        'interface': 'TenGigabitEthernet3/1/5',
                                                        'neighbor_router_id': '20.51.55.49',
                                                        'next': '0x0(0)/0x625F6304(13775194)',
                                                        'priority': 0,
                                                        'state': 'full',
                                                        'statistics': {'last_retrans_max_scan_length': 3,
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
                                                    {'20.51.55.21': 
                                                        {'address': '20.51.55.21',
                                                        'bdr_ip_addr': '0.0.0.0',
                                                        'dead_timer': '00:00:03',
                                                        'dr_ip_addr': '20.51.55.26',
                                                        'first': '0x0(0)/0x0(0)',
                                                        'hello_options': '0x2',
                                                        'index': '1/1,',
                                                        'interface': 'TenGigabitEthernet3/1/3',
                                                        'neighbor_router_id': '20.51.55.21',
                                                        'next': '0x0(0)/0x0(0)',
                                                        'priority': 0,
                                                        'state': 'full',
                                                        'statistics': {'last_retrans_max_scan_length': 0,
                                                                      'last_retrans_max_scan_time_msec': 0,
                                                                      'last_retrans_scan_length': 0,
                                                                      'last_retrans_scan_time_msec': 0,
                                                                      'nbr_event_count': 12,
                                                                      'nbr_retrans_qlen': 0,
                                                                      'total_retransmission': 0},
                                                        'uptime': '3d00h'}}},
                                            'TenGigabitEthernet3/1/4': 
                                                {'neighbors': 
                                                    {'20.51.55.93': 
                                                        {'address': '20.51.55.93',
                                                        'bdr_ip_addr': '0.0.0.0',
                                                        'dead_timer': '00:00:03',
                                                        'dr_ip_addr': '20.51.55.98',
                                                        'first': '0x0(0)/0x0(0)',
                                                        'hello_options': '0x2',
                                                        'index': '2/2,',
                                                        'interface': 'TenGigabitEthernet3/1/4',
                                                        'neighbor_router_id': '20.51.55.93',
                                                        'next': '0x0(0)/0x0(0)',
                                                        'priority': 0,
                                                        'state': 'full',
                                                        'statistics': {'last_retrans_max_scan_length': 0,
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
            Neighbor 2.2.2.2, interface address 10.1.2.2, interface-id unknown
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
            Neighbor 4.4.4.4, interface address 10.1.4.4
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
            Neighbor 22.22.22.22, interface address 22.22.22.22
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
            Neighbor 55.55.55.55, interface address 20.1.5.5
                In the area 1 via interface GigabitEthernet3
                Neighbor priority is 1, State is FULL, 6 state changes
                DR is 20.1.5.1 BDR is 20.1.5.5
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
              Process ID 1, Router ID 1.1.1.1, Network Type BROADCAST, Cost: 1
              Topology-MTID    Cost    Disabled    Shutdown      Topology Name
                    0           1         no          no            Base
              Enabled by interface config, including secondary ip addresses
              Transmit Delay is 1 sec, State DR, Priority 1
              Designated Router (ID) 1.1.1.1, Interface address 10.1.2.1
              Backup Designated router (ID) 2.2.2.2, Interface address 10.1.2.2
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
                Adjacent with neighbor 2.2.2.2  (Backup Designated Router)
              Suppress hello for 0 neighbor(s)
            '''

        raw2_2 = '''\
            R1_ospf_xe#show ip ospf interface | i GigabitEthernet1
            GigabitEthernet1 is up, line protocol is up 
              Internet Address 10.1.4.1/24, Interface ID 7, Area 0
              Attached via Interface Enable
              Process ID 1, Router ID 1.1.1.1, Network Type BROADCAST, Cost: 1
              Topology-MTID    Cost    Disabled    Shutdown      Topology Name
                    0           1         no          no            Base
              Enabled by interface config, including secondary ip addresses
              Transmit Delay is 1 sec, State BDR, Priority 1
              Designated Router (ID) 4.4.4.4, Interface address 10.1.4.4
              Backup Designated router (ID) 1.1.1.1, Interface address 10.1.4.1
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
                Adjacent with neighbor 4.4.4.4  (Designated Router)
              Suppress hello for 0 neighbor(s)
            '''

        raw2_3 = '''
            R1_ospf_xe#show ip ospf interface | i OSPF_SL1
            OSPF_SL1 is up, line protocol is up 
              Internet Address 0.0.0.0/0, Interface ID 14, Area 1
              Attached via Not Attached
              Process ID 2, Router ID 11.11.11.11, Network Type SHAM_LINK, Cost: 111
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
                Adjacent with neighbor 22.22.22.22
              Suppress hello for 0 neighbor(s)
            '''

        raw2_4 = '''
            R1_ospf_xe#show ip ospf interface | i GigabitEthernet3
            GigabitEthernet3 is up, line protocol is up 
              Internet Address 20.1.5.1/24, Interface ID 9, Area 1
              Attached via Interface Enable
              Process ID 2, Router ID 11.11.11.11, Network Type BROADCAST, Cost: 1
              Topology-MTID    Cost    Disabled    Shutdown      Topology Name
                    0           1         no          no            Base
              Enabled by interface config, including secondary ip addresses
              Transmit Delay is 1 sec, State DR, Priority 1
              Designated Router (ID) 11.11.11.11, Interface address 20.1.5.1
              Backup Designated router (ID) 55.55.55.55, Interface address 20.1.5.5
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
                Adjacent with neighbor 55.55.55.55  (Backup Designated Router)
              Suppress hello for 0 neighbor(s)
            '''

        raw3_1 = '''\
            R1_ospf_xe#show ip ospf sham-links | i OSPF_SL1
              Sham Link OSPF_SL1 to address 22.22.22.22 is up
            '''

        raw3_2 = '''\
            R1_ospf_xe#show running-config | i sham-link | i 22.22.22.22
              area 1 sham-link 11.11.11.11 22.22.22.22 cost 111 ttl-security hops 3
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
                area 1 virtual-link 5.5.5.5
                area 1 sham-link 11.11.11.11 22.22.22.22 cost 111 ttl-security hops 3
                redistribute bgp
            '''

        self.outputs = {}
        self.outputs['show ip ospf neighbor detail'] = raw1
        self.outputs['show ip ospf interface | section GigabitEthernet2'] = raw2_1
        self.outputs['show ip ospf interface | section GigabitEthernet1'] = raw2_2
        self.outputs['show ip ospf interface | section OSPF_SL1'] = raw2_3
        self.outputs['show ip ospf interface | section GigabitEthernet3'] = raw2_4
        self.outputs['show ip ospf sham-links | i OSPF_SL1'] = raw3_1
        self.outputs['show running-config | i sham-link | i 22.22.22.22'] = raw3_2
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
            Neighbor 3.3.3.3, interface address 20.2.3.3
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
            Neighbor 3.3.3.3, interface address 20.3.4.3
                In the area 1 via interface GigabitEthernet0/1
                Neighbor priority is 1, State is FULL, 6 state changes
                DR is 20.3.4.4 BDR is 20.3.4.3
                Options is 0x2 in Hello (E-bit)
                Options is 0x42 in DBD (E-bit, O-bit)
                Dead timer due in 00:00:33
                Neighbor is up for 16:31:06
                Index 2/2, retransmission queue length 0, number of retransmission 2
                First 0x0(0)/0x0(0) Next 0x0(0)/0x0(0)
                Last retransmission scan length is 1, maximum is 1
                Last retransmission scan time is 0 msec, maximum is 0 msec
            Neighbor 2.2.2.2, interface address 20.2.4.2
                In the area 1 via interface GigabitEthernet0/0
                Neighbor priority is 1, State is FULL, 6 state changes
                DR is 20.2.4.4 BDR is 20.2.4.2
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
                Internet Address 20.3.4.4/24, Area 0, Attached via Not Attached
                Process ID 1, Router ID 4.4.4.4, Network Type VIRTUAL_LINK, Cost: 1
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
                Adjacent with neighbor 3.3.3.3
                Suppress hello for 0 neighbor(s)
            '''

        raw2_2 = '''\
            R4_ospf_iosv#show ip ospf interface | section GigabitEthernet0/1
            GigabitEthernet0/1 is up, line protocol is up 
                Internet Address 20.3.4.4/24, Area 1, Attached via Interface Enable
                Process ID 1, Router ID 4.4.4.4, Network Type BROADCAST, Cost: 1
                Topology-MTID    Cost    Disabled    Shutdown      Topology Name
                    0           1         no          no            Base
                Enabled by interface config, including secondary ip addresses
                Transmit Delay is 1 sec, State DR, Priority 1
                Designated Router (ID) 4.4.4.4, Interface address 20.3.4.4
                Backup Designated router (ID) 3.3.3.3, Interface address 20.3.4.3
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
                Adjacent with neighbor 3.3.3.3  (Backup Designated Router)
                Suppress hello for 0 neighbor(s)
            '''

        raw2_3 = '''\
            R4_ospf_iosv#show ip ospf interface | section GigabitEthernet0/0
            GigabitEthernet0/0 is up, line protocol is up 
                Internet Address 20.2.4.4/24, Area 1, Attached via Interface Enable
                Process ID 1, Router ID 4.4.4.4, Network Type BROADCAST, Cost: 1
                Topology-MTID    Cost    Disabled    Shutdown      Topology Name
                    0           1         no          no            Base
                Enabled by interface config, including secondary ip addresses
                Transmit Delay is 1 sec, State DR, Priority 1
                Designated Router (ID) 4.4.4.4, Interface address 20.2.4.4
                Backup Designated router (ID) 2.2.2.2, Interface address 20.2.4.2
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
                Adjacent with neighbor 2.2.2.2  (Backup Designated Router)
                Suppress hello for 0 neighbor(s)
            '''

        raw3_1 = '''\
            R1_ospf_xe#show ip ospf virtual-links | i OSPF_VL1
              Virtual Link OSPF_VL1 to router 5.5.5.5 is down
            '''

        raw3_2 = '''\
            R1_ospf_xe#show running-config | i virtual-link | i 5.5.5.5
              area 1 virtual-link 5.5.5.5
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
                area 1 virtual-link 5.5.5.5
                area 1 sham-link 11.11.11.11 22.22.22.22 cost 111 ttl-security hops 3
                redistribute bgp
            '''

        self.outputs = {}
        self.outputs['show ip ospf neighbor detail'] = raw1
        self.outputs['show ip ospf interface | section OSPF_VL1'] = raw2_1
        self.outputs['show ip ospf interface | section GigabitEthernet0/1'] = raw2_2
        self.outputs['show ip ospf interface | section GigabitEthernet0/0'] = raw2_3

        self.outputs['show ip ospf virtual-links | i OSPF_VL1'] = raw3_1
        self.outputs['show running-config | i virtual-link | i 5.5.5.5'] = raw3_2
        
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
            Neighbor 20.51.55.49, interface address 20.51.55.49
                In the area 0 via interface TenGigabitEthernet3/1/5
                Neighbor priority is 0, State is FULL, 12 state changes
                DR is 20.51.55.54 BDR is 0.0.0.0
                Options is 0x2 in Hello (E-bit)
                Options is 0x2 in DBD (E-bit)
                Dead timer due in 00:00:03
                Neighbor is up for 3d00h
                Index 3/3, retransmission queue length 5, number of retransmission 6
                First 0x0(0)/0x625F6304(13775194) Next 0x0(0)/0x625F6304(13775194)
                Last retransmission scan length is 0, maximum is 3
                Last retransmission scan time is 0 msec, maximum is 4 msec
                Link State retransmission due in 2344 msec
            Neighbor 20.51.55.41, interface address 20.51.55.41
                In the area 0 via interface TenGigabitEthernet3/1/2
                Neighbor priority is 0, State is FULL, 22 state changes
                DR is 20.51.55.46 BDR is 0.0.0.0
                Options is 0x2 in Hello (E-bit)
                Options is 0x2 in DBD (E-bit)
                Dead timer due in 00:00:03
                Neighbor is up for 3d00h
                Index 1/1, retransmission queue length 0, number of retransmission 1
                First 0x0(0)/0x0(0) Next 0x0(0)/0x0(0)
                Last retransmission scan length is 0, maximum is 1
                Last retransmission scan time is 0 msec, maximum is 0 msec
            Neighbor 20.51.55.33, interface address 20.51.55.33
                In the area 0 via interface TenGigabitEthernet3/1/1
                Neighbor priority is 0, State is FULL, 12 state changes
                DR is 20.51.55.38 BDR is 0.0.0.0
                Options is 0x2 in Hello (E-bit)
                Options is 0x2 in DBD (E-bit)
                Dead timer due in 00:00:03
                Neighbor is up for 3d21h
                Index 2/2, retransmission queue length 3, number of retransmission 5
                First 0x0(0)/0x625F62BC(13775196) Next 0x0(0)/0x625F62BC(13775196)
                Last retransmission scan length is 0, maximum is 2
                Last retransmission scan time is 0 msec, maximum is 4 msec
                Link State retransmission due in 4356 msec
            Neighbor 20.51.55.93, interface address 20.51.55.93
                In the area 1666 via interface TenGigabitEthernet3/1/4
                Neighbor priority is 0, State is FULL, 18 state changes
                DR is 20.51.55.98 BDR is 0.0.0.0
                Options is 0x2 in Hello (E-bit)
                Options is 0x2 in DBD (E-bit)
                Dead timer due in 00:00:03
                Neighbor is up for 3d00h
                Index 2/2, retransmission queue length 0, number of retransmission 0
                First 0x0(0)/0x0(0) Next 0x0(0)/0x0(0)
                Last retransmission scan length is 0, maximum is 0
                Last retransmission scan time is 0 msec, maximum is 0 msec
            Neighbor 20.51.55.21, interface address 20.51.55.21
                In the area 1666 via interface TenGigabitEthernet3/1/3
                Neighbor priority is 0, State is FULL, 12 state changes
                DR is 20.51.55.26 BDR is 0.0.0.0
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
              Internet Address 20.51.55.38/29, Area 0, Attached via Interface Enable
              Process ID 1668, Router ID 20.46.52.10, Network Type BROADCAST, Cost: 1
              Topology-MTID    Cost    Disabled    Shutdown      Topology Name
                    0           1         no          no            Base
              Enabled by interface config, including secondary ip addresses
              Transmit Delay is 1 sec, State DR, Priority 1
              Designated Router (ID) 20.46.52.10, Interface address 20.51.55.38
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
                Adjacent with neighbor 20.51.55.33
              Suppress hello for 0 neighbor(s)
              Cryptographic authentication enabled
                Youngest key id is 1
            '''

        raw2_2 = '''\
            nhq-choke-VSS#show ip ospf interface | section TenGigabitEthernet3/1/2
            TenGigabitEthernet3/1/2 is up, line protocol is up (connected) 
              Internet Address 20.51.55.46/29, Area 0, Attached via Interface Enable
              Process ID 1668, Router ID 20.46.52.10, Network Type BROADCAST, Cost: 1
              Topology-MTID    Cost    Disabled    Shutdown      Topology Name
                    0           1         no          no            Base
              Enabled by interface config, including secondary ip addresses
              Transmit Delay is 1 sec, State DR, Priority 1
              Designated Router (ID) 20.46.52.10, Interface address 20.51.55.46
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
                Adjacent with neighbor 20.51.55.41
              Suppress hello for 0 neighbor(s)
              Cryptographic authentication enabled
                Youngest key id is 1
            '''

        raw2_3 = '''\
            nhq-choke-VSS#show ip ospf interface | section TenGigabitEthernet3/1/3
            TenGigabitEthernet3/1/3 is up, line protocol is up (connected) 
              Internet Address 20.51.55.26/29, Area 1666, Attached via Interface Enable
              Process ID 1666, Router ID 20.55.21.9, Network Type BROADCAST, Cost: 1000
              Topology-MTID    Cost    Disabled    Shutdown      Topology Name
                    0           1000      no          no            Base
              Enabled by interface config, including secondary ip addresses
              Transmit Delay is 1 sec, State DR, Priority 1
              Designated Router (ID) 20.55.21.9, Interface address 20.51.55.26
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
                Adjacent with neighbor 20.51.55.21
              Suppress hello for 0 neighbor(s)
            '''

        raw2_4 = '''\
            nhq-choke-VSS#show ip ospf interface | section TenGigabitEthernet3/1/4
            TenGigabitEthernet3/1/4 is up, line protocol is up (connected) 
              Internet Address 20.51.55.98/29, Area 1666, Attached via Interface Enable
              Process ID 1666, Router ID 20.55.21.9, Network Type BROADCAST, Cost: 1
              Topology-MTID    Cost    Disabled    Shutdown      Topology Name
                    0           1         no          no            Base
              Enabled by interface config, including secondary ip addresses
              Transmit Delay is 1 sec, State DR, Priority 1
              Designated Router (ID) 20.55.21.9, Interface address 20.51.55.98
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
                Adjacent with neighbor 20.51.55.93
              Suppress hello for 0 neighbor(s)
            '''

        raw2_5 = '''\
            nhq-choke-VSS#show ip ospf interface | section TenGigabitEthernet3/1/5
            TenGigabitEthernet3/1/5 is up, line protocol is up (connected) 
              Internet Address 20.51.55.54/29, Area 0, Attached via Interface Enable
              Process ID 1668, Router ID 20.46.52.10, Network Type BROADCAST, Cost: 100
              Topology-MTID    Cost    Disabled    Shutdown      Topology Name
                    0           100       no          no            Base
              Enabled by interface config, including secondary ip addresses
              Transmit Delay is 1 sec, State DR, Priority 1
              Designated Router (ID) 20.46.52.10, Interface address 20.51.55.54
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
                Adjacent with neighbor 20.51.55.49
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
              router-id 20.46.52.10
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
                                            {'11.11.11.11 22.22.22.22': 
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
                                                'local_id': '11.11.11.11',
                                                'name': 'SL0',
                                                'next': '0x0(0)/0x0(0)/0x0(0)',
                                                'remote_id': '22.22.22.22',
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
            Sham Link OSPF_SL0 to address 22.22.22.22 is up
            Area 1 source address 11.11.11.11
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
              Process ID 2, Router ID 11.11.11.11, Network Type SHAM_LINK, Cost: 111
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
                area 1 virtual-link 5.5.5.5
                area 1 sham-link 11.11.11.11 22.22.22.22 cost 111 ttl-security hops 3
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
                                            {'0.0.0.1 3.3.3.3': 
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
                                                'router_id': '3.3.3.3',
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
            Virtual Link OSPF_VL0 to router 3.3.3.3 is up
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
              Process ID 2, Router ID 11.11.11.11, Network Type VIRTUAL_LINK, Cost: 65535
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
                area 1 virtual-link 5.5.5.5
                area 1 sham-link 11.11.11.11 22.22.22.22 cost 111 ttl-security hops 3
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
                                    {'0.0.0.9': 
                                        {'database': 
                                            {'lsa_types': 
                                                {1: 
                                                    {'lsa_type': 1,
                                                    'lsas': 
                                                        {'1.1.1.1': 
                                                            {'adv_router': '1.1.1.1',
                                                            'lsa_id': '1.1.1.1',
                                                            'ospfv2': 
                                                                {'header': 
                                                                    {'adv_router': '1.1.1.1',
                                                                    'age': 167,
                                                                    'checksum': '0x00D8C6',
                                                                    'link_count': 1,
                                                                    'lsa_id': '1.1.1.1',
                                                                    'seq_num': '0x8000000D'}}}}}}}}}},
                            '9996': 
                                {'areas': 
                                    {'0.0.0.0': 
                                        {'database': 
                                            {'lsa_types': 
                                                {1: 
                                                    {'lsa_type': 1,
                                                    'lsas': 
                                                        {'203.131.197.252': 
                                                            {'adv_router': '203.131.197.252',
                                                            'lsa_id': '203.131.197.252',
                                                            'ospfv2': 
                                                                {'header': 
                                                                    {'adv_router': '203.131.197.252',
                                                                    'age': 1802,
                                                                    'checksum': '0x007F23',
                                                                    'link_count': 5,
                                                                    'lsa_id': '203.131.197.252',
                                                                    'seq_num': '0x80000161'}}},
                                                        '203.131.197.253': 
                                                            {'adv_router': '203.131.197.253',
                                                            'lsa_id': '203.131.197.253',
                                                            'ospfv2': 
                                                                {'header': 
                                                                    {'adv_router': '203.131.197.253',
                                                                    'age': 1784,
                                                                    'checksum': '0x00CC34',
                                                                    'link_count': 8,
                                                                    'lsa_id': '203.131.197.253',
                                                                    'seq_num': '0x80000103'}}},
                                                        '203.131.197.254': 
                                                            {'adv_router': '203.131.197.254',
                                                            'lsa_id': '203.131.197.254',
                                                            'ospfv2': 
                                                                {'header': 
                                                                    {'adv_router': '203.131.197.254',
                                                                    'age': 1675,
                                                                    'checksum': '0x007A61',
                                                                    'link_count': 3,
                                                                    'lsa_id': '203.131.197.254',
                                                                    'seq_num': '0x8000000C'}}},
                                                        '121.121.121.2': 
                                                            {'adv_router': '121.121.121.2',
                                                            'lsa_id': '121.121.121.2',
                                                            'ospfv2': 
                                                                {'header': 
                                                                    {'adv_router': '121.121.121.2',
                                                                    'age': 226,
                                                                    'checksum': '0x006975',
                                                                    'link_count': 501,
                                                                    'lsa_id': '121.121.121.2',
                                                                    'seq_num': '0x80000069'}}},
                                                        '102.138.165.119': 
                                                            {'adv_router': '102.138.165.119',
                                                            'lsa_id': '102.138.165.119',
                                                            'ospfv2': 
                                                                {'header': 
                                                                    {'adv_router': '102.138.165.119',
                                                                    'age': 1089,
                                                                    'checksum': '0x0080E0',
                                                                    'link_count': 2,
                                                                    'lsa_id': '102.138.165.119',
                                                                    'seq_num': '0x80000029'}}},
                                                        '102.138.165.120': 
                                                            {'adv_router': '102.138.165.120',
                                                            'lsa_id': '102.138.165.120',
                                                            'ospfv2': 
                                                                {'header': 
                                                                    {'adv_router': '102.138.165.120',
                                                                    'age': 1482,
                                                                    'checksum': '0x0063CB',
                                                                    'link_count': 2,
                                                                    'lsa_id': '102.138.165.120',
                                                                    'seq_num': '0x80000033'}}},
                                                        '102.138.165.220': 
                                                            {'adv_router': '102.138.165.220',
                                                            'lsa_id': '102.138.165.220',
                                                            'ospfv2': 
                                                                {'header': 
                                                                    {'adv_router': '102.138.165.220',
                                                                    'age': 525,
                                                                    'checksum': '0x004E8E',
                                                                    'link_count': 3,
                                                                    'lsa_id': '102.138.165.220',
                                                                    'seq_num': '0x800000DE'}}},
                                                        '17.83.102.64': 
                                                            {'adv_router': '17.83.102.64',
                                                            'lsa_id': '17.83.102.64',
                                                            'ospfv2': 
                                                                {'header': 
                                                                    {'adv_router': '17.83.102.64',
                                                                    'age': 2794,
                                                                    'checksum': '0x002254',
                                                                    'link_count': 3,
                                                                    'lsa_id': '17.83.102.64',
                                                                    'seq_num': '0x80000043'}}}}},
                                                2: 
                                                    {'lsa_type': 2,
                                                    'lsas': 
                                                        {'203.131.197.102': 
                                                            {'adv_router': '102.138.165.220',
                                                            'lsa_id': '203.131.197.102',
                                                            'ospfv2': 
                                                                {'header': 
                                                                    {'adv_router': '102.138.165.220',
                                                                    'age': 525,
                                                                    'checksum': '0x0094CD',
                                                                    'lsa_id': '203.131.197.102',
                                                                    'seq_num': '0x80000058'}}},
                                                        '203.131.197.93': 
                                                            {'adv_router': '203.131.197.252',
                                                            'lsa_id': '203.131.197.93',
                                                            'ospfv2': 
                                                                {'header': 
                                                                    {'adv_router': '203.131.197.252',
                                                                    'age': 1802,
                                                                    'checksum': '0x002D67',
                                                                    'lsa_id': '203.131.197.93',
                                                                    'seq_num': '0x80000008'}}},
                                                        '203.131.197.97': 
                                                            {'adv_router': '203.131.197.253',
                                                            'lsa_id': '203.131.197.97',
                                                            'ospfv2': 
                                                                {'header': 
                                                                    {'adv_router': '203.131.197.253',
                                                                    'age': 1356,
                                                                    'checksum': '0x000D83',
                                                                    'lsa_id': '203.131.197.97',
                                                                    'seq_num': '0x80000006'}}},
                                                        '121.121.121.2': 
                                                            {'adv_router': '203.131.197.253',
                                                            'lsa_id': '121.121.121.2',
                                                            'ospfv2': 
                                                                {'header': 
                                                                    {'adv_router': '203.131.197.253',
                                                                    'age': 2213,
                                                                    'checksum': '0x00D374',
                                                                    'lsa_id': '121.121.121.2',
                                                                    'seq_num': '0x80000BA8'}}},
                                                        '20.1.1.2': 
                                                            {'adv_router': '203.131.197.253',
                                                            'lsa_id': '20.1.1.2',
                                                            'ospfv2': 
                                                                {'header': 
                                                                    {'adv_router': '203.131.197.253',
                                                                    'age': 70,
                                                                    'checksum': '0x0015EF',
                                                                    'lsa_id': '20.1.1.2',
                                                                     'seq_num': '0x8000003F'}}},
                                                        '102.138.165.49': 
                                                            {'adv_router': '203.131.197.253',
                                                            'lsa_id': '102.138.165.49',
                                                            'ospfv2': 
                                                                {'header': 
                                                                    {'adv_router': '203.131.197.253',
                                                                    'age': 499,
                                                                    'checksum': '0x005CBC',
                                                                    'lsa_id': '102.138.165.49',
                                                                     'seq_num': '0x8000001A'}}},
                                                        '102.138.165.57': 
                                                            {'adv_router': '203.131.197.253',
                                                            'lsa_id': '102.138.165.57',
                                                            'ospfv2': 
                                                                {'header': 
                                                                    {'adv_router': '203.131.197.253',
                                                                    'age': 927,
                                                                    'checksum': '0x0008FE',
                                                                    'lsa_id': '102.138.165.57',
                                                                    'seq_num': '0x80000023'}}},
                                                        '17.83.102.49': 
                                                            {'adv_router': '203.131.197.252',
                                                            'lsa_id': '17.83.102.49',
                                                            'ospfv2': 
                                                                {'header': 
                                                                    {'adv_router': '203.131.197.252',
                                                                    'age': 289,
                                                                    'checksum': '0x007AD0',
                                                                    'lsa_id': '17.83.102.49',
                                                                    'seq_num': '0x8000005B'}}},
                                                        '17.83.102.57': 
                                                            {'adv_router': '203.131.197.253',
                                                            'lsa_id': '17.83.102.57',
                                                            'ospfv2': 
                                                                {'header': 
                                                                    {'adv_router': '203.131.197.253',
                                                                    'age': 2641,
                                                                    'checksum': '0x0062F8',
                                                                    'lsa_id': '17.83.102.57',
                                                                    'seq_num': '0x80000041'}}}}}}}}}}}}}}}}

    golden_output1 = {'execute.return_value': '''
        Router#show ip ospf database
        Load for five secs: 71%/0%; one minute: 11%; five minutes: 9%
        Time source is NTP, 20:29:26.348 JST Fri Nov 11 2016


                    OSPF Router with ID (203.131.197.254) (Process ID 9996)

                Router Link States (Area 0)

        Link ID         ADV Router      Age         Seq#       Checksum Link count
        17.83.102.64    17.83.102.64    2794        0x80000043 0x002254 3
        203.131.197.252 203.131.197.252 1802        0x80000161 0x007F23 5
        203.131.197.253 203.131.197.253 1784        0x80000103 0x00CC34 8
        203.131.197.254 203.131.197.254 1675        0x8000000C 0x007A61 3
        121.121.121.2   121.121.121.2   226         0x80000069 0x006975 501
        102.138.165.119 102.138.165.119 1089        0x80000029 0x0080E0 2
        102.138.165.120 102.138.165.120 1482        0x80000033 0x0063CB 2
        102.138.165.220 102.138.165.220 525         0x800000DE 0x004E8E 3

                Net Link States (Area 0)

        Link ID         ADV Router      Age         Seq#       Checksum
        20.1.1.2        203.131.197.253 70          0x8000003F 0x0015EF
        17.83.102.49    203.131.197.252 289         0x8000005B 0x007AD0
        17.83.102.57    203.131.197.253 2641        0x80000041 0x0062F8
        203.131.197.93  203.131.197.252 1802        0x80000008 0x002D67
        203.131.197.97  203.131.197.253 1356        0x80000006 0x000D83
        203.131.197.102 102.138.165.220 525         0x80000058 0x0094CD
        121.121.121.2   203.131.197.253 2213        0x80000BA8 0x00D374
        102.138.165.49  203.131.197.253 499         0x8000001A 0x005CBC
        102.138.165.57  203.131.197.253 927         0x80000023 0x0008FE

                    OSPF Router with ID (1.1.1.1) (Process ID 1)

                Router Link States (Area 9)

        Link ID         ADV Router      Age         Seq#       Checksum Link count
        1.1.1.1         1.1.1.1         167         0x8000000D 0x00D8C6 1
        Router#
        '''}

    golden_parsed_output2 = {}

    golden_output2 = {'execute.return_value': '''
        Router#show ip ospf database
        Load for five secs: 1%/0%; one minute: 4%; five minutes: 6%
        Time source is NTP, 15:40:22.269 JST Sun Nov 6 2016


                    OSPF Router with ID (203.131.197.254) (Process ID 9996)

                Router Link States (Area 8)

        Link ID         ADV Router      Age         Seq#       Checksum Link count
        17.83.102.64    17.83.102.64    2220        0x800003EC 0x008BD8 3
        203.131.197.252 203.131.197.252 1272        0x80000DBD 0x00B9E5 6
        203.131.197.253 203.131.197.253 663         0x8000009D 0x00FFD8 4
        203.131.197.254 203.131.197.254 1900        0x800000D9 0x00D029 3
        121.121.121.2   121.121.121.2   1407        0x800007BC 0x00ADD6 501
        102.138.165.220 102.138.165.220 113         0x800006E3 0x007C93 2

                Net Link States (Area 8)

        Link ID         ADV Router      Age         Seq#       Checksum
        17.83.102.50    17.83.102.64    220         0x800000AD 0x003A0A
        17.83.102.58    17.83.102.64    1220        0x80000038 0x00E2CD
        203.131.197.94  203.131.197.254 911         0x80000052 0x007ACC
        203.131.197.97  203.131.197.253 663         0x80000037 0x00AAB4
        203.131.197.102 102.138.165.220 113         0x80000055 0x009ACA
        121.121.121.2   203.131.197.252 26          0x800000D1 0x009E8D

                Summary Net Link States (Area 8)

        Link ID         ADV Router      Age         Seq#       Checksum
        102.138.165.48  203.131.197.252 26          0x800003DF 0x0006F6
        102.138.165.56  203.131.197.252 1779        0x800000D4 0x00D42E
        102.138.165.119 203.131.197.252 1030        0x800000D4 0x007847
        102.138.165.120 203.131.197.252 26          0x800003DE 0x005160

                Summary ASB Link States (Area 8)

        Link ID         ADV Router      Age         Seq#       Checksum
        102.138.165.119 203.131.197.252 1030        0x800000D4 0x00605F
        102.138.165.120 203.131.197.252 26          0x800003DE 0x003978
        Router#
        '''}

    golden_parsed_output3 = {
        'vrf': 
            {'default': 
                {'address_family': 
                    {'ipv4': 
                        {'instance': 
                            {'9996': 
                                {'areas': 
                                    {'0.0.0.0': 
                                        {'database': 
                                            {'lsa_types': 
                                                {1: 
                                                    {'lsa_type': 1,
                                                    'lsas': 
                                                        {'101.101.101.2': 
                                                            {'adv_router': '101.101.101.2',
                                                            'lsa_id': '101.101.101.2',
                                                            'ospfv2': 
                                                                {'header': 
                                                                    {'adv_router': '101.101.101.2',
                                                                    'age': 1548,
                                                                    'checksum': '0x007D6B',
                                                                    'link_count': 501,
                                                                    'lsa_id': '101.101.101.2',
                                                                     'seq_num': '0x8000005F'}}},
                                                        '102.138.135.119': 
                                                            {'adv_router': '102.138.135.119',
                                                            'lsa_id': '102.138.135.119',
                                                            'ospfv2': 
                                                                {'header': 
                                                                    {'adv_router': '102.138.135.119',
                                                                    'age': 533,
                                                                    'checksum': '0x0090D8',
                                                                    'link_count': 2,
                                                                    'lsa_id': '102.138.135.119',
                                                                    'seq_num': '0x80000021'}}},
                                                        '102.138.135.120': 
                                                            {'adv_router': '102.138.135.120',
                                                            'lsa_id': '102.138.135.120',
                                                            'ospfv2': 
                                                                {'header': 
                                                                    {'adv_router': '102.138.135.120',
                                                                    'age': 919,
                                                                    'checksum': '0x0073C3',
                                                                    'link_count': 2,
                                                                    'lsa_id': '102.138.135.120',
                                                                    'seq_num': '0x8000002B'}}},
                                                        '102.138.135.220': 
                                                            {'adv_router': '102.138.135.220',
                                                            'lsa_id': '102.138.135.220',
                                                            'ospfv2': 
                                                                {'header': 
                                                                    {'adv_router': '102.138.135.220',
                                                                    'age': 2014,
                                                                    'checksum': '0x006085',
                                                                    'link_count': 3,
                                                                    'lsa_id': '102.138.135.220',
                                                                    'seq_num': '0x800000D5'}}},
                                                        '17.83.102.64': 
                                                            {'adv_router': '17.83.102.64',
                                                            'lsa_id': '17.83.102.64',
                                                            'ospfv2': 
                                                                {'header': 
                                                                    {'adv_router': '17.83.102.64',
                                                                    'age': 1111,
                                                                    'checksum': '0x002C4F',
                                                                    'link_count': 3,
                                                                    'lsa_id': '17.83.102.64',
                                                                    'seq_num': '0x8000003E'}}},
                                                        '206.152.198.252': 
                                                            {'adv_router': '206.152.198.252',
                                                            'lsa_id': '206.152.198.252',
                                                            'ospfv2': 
                                                                {'header': 
                                                                    {'adv_router': '206.152.198.252',
                                                                    'age': 768,
                                                                    'checksum': '0x00C5E7',
                                                                    'link_count': 5,
                                                                    'lsa_id': '206.152.198.252',
                                                                    'seq_num': '0x80000155'}}},
                                                        '206.152.198.253': 
                                                            {'adv_router': '206.152.198.253',
                                                            'lsa_id': '206.152.198.253',
                                                            'ospfv2': 
                                                                {'header': 
                                                                    {'adv_router': '206.152.198.253',
                                                                    'age': 657,
                                                                    'checksum': '0x00E328',
                                                                    'link_count': 8,
                                                                    'lsa_id': '206.152.198.253',
                                                                    'seq_num': '0x800000F8'}}},
                                                        '206.152.198.254': 
                                                            {'adv_router': '206.152.198.254',
                                                            'lsa_id': '206.152.198.254',
                                                            'ospfv2': 
                                                                {'header': 
                                                                    {'adv_router': '206.152.198.254',
                                                                    'age': 656,
                                                                    'checksum': '0x007A2A',
                                                                    'link_count': 3,
                                                                    'lsa_id': '206.152.198.254',
                                                                    'seq_num': '0x8000002F'}}}}},
                                                2: 
                                                    {'lsa_type': 2,
                                                    'lsas': 
                                                        {'101.101.101.2': 
                                                            {'adv_router': '206.152.198.253',
                                                            'lsa_id': '101.101.101.2',
                                                            'ospfv2': 
                                                                {'header': 
                                                                    {'adv_router': '206.152.198.253',
                                                                    'age': 2501,
                                                                    'checksum': '0x00DF6E',
                                                                    'lsa_id': '101.101.101.2',
                                                                    'seq_num': '0x80000BA2'}}},
                                                        '102.138.135.49': 
                                                            {'adv_router': '206.152.198.253',
                                                            'lsa_id': '102.138.135.49',
                                                            'ospfv2': 
                                                                {'header': 
                                                                    {'adv_router': '206.152.198.253',
                                                                    'age': 1006,
                                                                    'checksum': '0x0068B6',
                                                                    'lsa_id': '102.138.135.49',
                                                                    'seq_num': '0x80000014'}}},
                                                        '102.138.135.57': 
                                                            {'adv_router': '206.152.198.253',
                                                            'lsa_id': '102.138.135.57',
                                                            'ospfv2': 
                                                                {'header': 
                                                                    {'adv_router': '206.152.198.253',
                                                                    'age': 2072,
                                                                    'checksum': '0x0014F8',
                                                                    'lsa_id': '102.138.135.57',
                                                                    'seq_num': '0x8000001D'}}},
                                                        '17.83.102.49': 
                                                            {'adv_router': '206.152.198.252',
                                                            'lsa_id': '17.83.102.49',
                                                            'ospfv2': 
                                                                {'header': 
                                                                    {'adv_router': '206.152.198.252',
                                                                    'age': 1763,
                                                                    'checksum': '0x008CC7',
                                                                    'lsa_id': '17.83.102.49',
                                                                    'seq_num': '0x80000052'}}},
                                                        '17.83.102.57': 
                                                            {'adv_router': '206.152.198.253',
                                                            'lsa_id': '17.83.102.57',
                                                            'ospfv2': 
                                                                {'header': 
                                                                    {'adv_router': '206.152.198.253',
                                                                    'age': 89,
                                                                    'checksum': '0x006CF3',
                                                                    'lsa_id': '17.83.102.57',
                                                                    'seq_num': '0x8000003C'}}},
                                                        '20.1.1.2': 
                                                            {'adv_router': '206.152.198.253',
                                                            'lsa_id': '20.1.1.2',
                                                            'ospfv2': 
                                                                {'header': 
                                                                    {'adv_router': '206.152.198.253',
                                                                    'age': 547,
                                                                    'checksum': '0x0021E9',
                                                                    'lsa_id': '20.1.1.2',
                                                                    'seq_num': '0x80000039'}}},
                                                        '206.152.198.102': 
                                                            {'adv_router': '102.138.135.220',
                                                            'lsa_id': '206.152.198.102',
                                                            'ospfv2': 
                                                                {'header': 
                                                                    {'adv_router': '102.138.135.220',
                                                                    'age': 2014,
                                                                    'checksum': '0x00A6C4',
                                                                    'lsa_id': '206.152.198.102',
                                                                    'seq_num': '0x8000004F'}}},
                                                        '206.152.198.94': 
                                                            {'adv_router': '206.152.198.254',
                                                            'lsa_id': '206.152.198.94',
                                                            'ospfv2': 
                                                                {'header': 
                                                                    {'adv_router': '206.152.198.254',
                                                                    'age': 639,
                                                                    'checksum': '0x001B7C',
                                                                    'lsa_id': '206.152.198.94',
                                                                    'seq_num': '0x80000002'}}},
                                                        '206.152.198.97': 
                                                            {'adv_router': '206.152.198.253',
                                                            'lsa_id': '206.152.198.97',
                                                            'ospfv2': 
                                                                {'header': 
                                                                    {'adv_router': '206.152.198.253',
                                                                    'age': 657,
                                                                    'checksum': '0x00177E',
                                                                    'lsa_id': '206.152.198.97',
                                                                    'seq_num': '0x80000001'}}}}}}}}}}}}}}}}

    golden_output3 = {'execute.return_value': '''
        1006#show ip ospf database
        Load for five secs: 0%/0%; one minute: 0%; five minutes: 0%
        Time source is NTP, 15:51:24.610 JST Fri Nov 11 2016


                    OSPF Router with ID (206.152.198.252) (Process ID 9996)

                Router Link States (Area 0)

        Link ID         ADV Router      Age         Seq#       Checksum Link count
        17.83.102.64    17.83.102.64    1111        0x8000003E 0x002C4F 3
        206.152.198.252 206.152.198.252 768         0x80000155 0x00C5E7 5
        206.152.198.253 206.152.198.253 657         0x800000F8 0x00E328 8
        206.152.198.254 206.152.198.254 656         0x8000002F 0x007A2A 3
        101.101.101.2   101.101.101.2   1548        0x8000005F 0x007D6B 501
        102.138.135.119 102.138.135.119 533         0x80000021 0x0090D8 2
        102.138.135.120 102.138.135.120 919         0x8000002B 0x0073C3 2
        102.138.135.220 102.138.135.220 2014        0x800000D5 0x006085 3

                Net Link States (Area 0)

        Link ID         ADV Router      Age         Seq#       Checksum
        20.1.1.2        206.152.198.253 547         0x80000039 0x0021E9
        17.83.102.49    206.152.198.252 1763        0x80000052 0x008CC7
        17.83.102.57    206.152.198.253 89          0x8000003C 0x006CF3
        206.152.198.94  206.152.198.254 639         0x80000002 0x001B7C
        206.152.198.97  206.152.198.253 657         0x80000001 0x00177E
        206.152.198.102 102.138.135.220 2014        0x8000004F 0x00A6C4
        101.101.101.2   206.152.198.253 2501        0x80000BA2 0x00DF6E
        102.138.135.49  206.152.198.253 1006        0x80000014 0x0068B6
        102.138.135.57  206.152.198.253 2072        0x8000001D 0x0014F8
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
        import pdb ; pdb.set_trace()
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
                                                        {'1.1.1.1 1.1.1.1': 
                                                            {'adv_router': '1.1.1.1',
                                                            'lsa_id': '1.1.1.1',
                                                            'ospfv2': 
                                                                {'body': 
                                                                    {'router': 
                                                                        {'links': 
                                                                            {'1.1.1.1': 
                                                                                {'link_data': '255.255.255.255',
                                                                                'link_id': '1.1.1.1',
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
                                                                    {'adv_router': '1.1.1.1',
                                                                    'age': 742,
                                                                    'checksum': '0x6228',
                                                                    'length': 60,
                                                                    'lsa_id': '1.1.1.1',
                                                                    'option': 'None',
                                                                    'option_desc': 'No TOS-capability, DC',
                                                                    'seq_num': '8000003D',
                                                                    'type': 1}}},
                                                        '2.2.2.2 2.2.2.2': 
                                                            {'adv_router': '2.2.2.2',
                                                            'lsa_id': '2.2.2.2',
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
                                                                            '2.2.2.2': 
                                                                                {'link_data': '255.255.255.255',
                                                                                'link_id': '2.2.2.2',
                                                                                'num_mtid_metrics': 0,
                                                                                'topologies': 
                                                                                    {0: 
                                                                                        {'metric': 1,
                                                                                        'mt_id': 0,
                                                                                        'tos': 0}},
                                                                                'type': 'stub network'}},
                                                                        'num_of_links': 4}},
                                                                'header': 
                                                                    {'adv_router': '2.2.2.2',
                                                                    'age': 1520,
                                                                    'checksum': '0x672A',
                                                                    'length': 72,
                                                                    'lsa_id': '2.2.2.2',
                                                                    'option': 'None',
                                                                    'option_desc': 'No TOS-capability, No DC',
                                                                    'seq_num': '80000013',
                                                                    'type': 1}}},
                                                        '3.3.3.3 3.3.3.3': 
                                                            {'adv_router': '3.3.3.3',
                                                            'lsa_id': '3.3.3.3',
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
                                                                            '3.3.3.3': 
                                                                                {'link_data': '255.255.255.255',
                                                                                'link_id': '3.3.3.3',
                                                                                'num_mtid_metrics': 0,
                                                                                'topologies': 
                                                                                    {0: 
                                                                                        {'metric': 1,
                                                                                        'mt_id': 0,
                                                                                        'tos': 0}},
                                                                                'type': 'stub network'}},
                                                                        'num_of_links': 3}},
                                                                'header': 
                                                                    {'adv_router': '3.3.3.3',
                                                                    'age': 235,
                                                                    'checksum': '0x75F8',
                                                                    'length': 60,
                                                                    'lsa_id': '3.3.3.3',
                                                                    'option': 'None',
                                                                    'option_desc': 'No TOS-capability, DC',
                                                                    'seq_num': '80000033',
                                                                    'type': 1}}},
                                                        '4.4.4.4 4.4.4.4': 
                                                            {'adv_router': '4.4.4.4',
                                                            'lsa_id': '4.4.4.4',
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
                                                                            '4.4.4.4': 
                                                                                {'link_data': '255.255.255.255',
                                                                                'link_id': '4.4.4.4',
                                                                                'num_mtid_metrics': 0,
                                                                                'topologies': 
                                                                                    {0: 
                                                                                        {'metric': 1,
                                                                                        'mt_id': 0,
                                                                                        'tos': 0}},
                                                                                'type': 'stub network'}},
                                                                        'num_of_links': 4}},
                                                                'header': 
                                                                    {'adv_router': '4.4.4.4',
                                                                    'age': 1486,
                                                                    'as_boundary_router': True,
                                                                    'checksum': '0xA57C',
                                                                    'length': 72,
                                                                    'lsa_id': '4.4.4.4',
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
                                                        {'11.11.11.11 11.11.11.11': 
                                                            {'adv_router': '11.11.11.11',
                                                            'lsa_id': '11.11.11.11',
                                                            'ospfv2': 
                                                                {'body': 
                                                                    {'router': 
                                                                        {'links': 
                                                                            {'20.1.5.1': 
                                                                                {'link_data': '20.1.5.1',
                                                                                'link_id': '20.1.5.1',
                                                                                'num_mtid_metrics': 0,
                                                                                'topologies': 
                                                                                    {0: 
                                                                                        {'metric': 1,
                                                                                        'mt_id': 0,
                                                                                        'tos': 0}},
                                                                                'type': 'transit network'},
                                                                            '22.22.22.22': 
                                                                                {'link_data': '0.0.0.14',
                                                                                'link_id': '22.22.22.22',
                                                                                'num_mtid_metrics': 0,
                                                                                'topologies': 
                                                                                    {0: 
                                                                                        {'metric': 111,
                                                                                        'mt_id': 0,
                                                                                        'tos': 0}},
                                                                                'type': 'another router (point-to-point)'}},
                                                                        'num_of_links': 2}},
                                                                'header': 
                                                                    {'adv_router': '11.11.11.11',
                                                                    'age': 651,
                                                                    'area_border_router': True,
                                                                    'as_boundary_router': True,
                                                                    'checksum': '0x9CE3',
                                                                    'length': 48,
                                                                    'lsa_id': '11.11.11.11',
                                                                    'option': 'None',
                                                                    'option_desc': 'No TOS-capability, DC',
                                                                    'seq_num': '8000003E',
                                                                    'type': 1}}},
                                                        '22.22.22.22 22.22.22.22': 
                                                            {'adv_router': '22.22.22.22',
                                                            'lsa_id': '22.22.22.22',
                                                            'ospfv2': 
                                                                {'body': 
                                                                    {'router': 
                                                                        {'links': 
                                                                            {'11.11.11.11': 
                                                                                {'link_data': '0.0.0.6',
                                                                                'link_id': '11.11.11.11',
                                                                                'num_mtid_metrics': 0,
                                                                                'topologies': 
                                                                                    {0: 
                                                                                        {'metric': 1,
                                                                                        'mt_id': 0,
                                                                                        'tos': 0}},
                                                                                'type': 'another router (point-to-point)'},
                                                                            '20.2.6.6': 
                                                                                {'link_data': '20.2.6.2',
                                                                                'link_id': '20.2.6.6',
                                                                                'num_mtid_metrics': 0,
                                                                                'topologies': 
                                                                                    {0: 
                                                                                        {'metric': 40,
                                                                                        'mt_id': 0,
                                                                                        'tos': 0}},
                                                                                'type': 'transit network'}},
                                                                        'num_of_links': 2}},
                                                                'header': 
                                                                    {'adv_router': '22.22.22.22',
                                                                    'age': 480,
                                                                    'area_border_router': True,
                                                                    'as_boundary_router': True,
                                                                    'checksum': '0xC41A',
                                                                    'length': 48,
                                                                    'lsa_id': '22.22.22.22',
                                                                    'option': 'None',
                                                                    'option_desc': 'No '
                                                                               'TOS-capability, '
                                                                               'No '
                                                                               'DC',
                                                                    'seq_num': '80000019',
                                                                    'type': 1}}},
                                                        '3.3.3.3 3.3.3.3': 
                                                            {'adv_router': '3.3.3.3',
                                                            'lsa_id': '3.3.3.3',
                                                            'ospfv2': 
                                                                {'body': 
                                                                    {'router': 
                                                                        {'links': 
                                                                            {'20.3.7.7': 
                                                                                {'link_data': '20.3.7.3',
                                                                                'link_id': '20.3.7.7',
                                                                                'num_mtid_metrics': 0,
                                                                                'topologies': 
                                                                                    {0: 
                                                                                        {'metric': 1,
                                                                                        'mt_id': 0,
                                                                                        'tos': 0}},
                                                                                'type': 'transit network'}},
                                                                        'num_of_links': 1}},
                                                                'header': 
                                                                    {'adv_router': '3.3.3.3',
                                                                    'age': 1128,
                                                                    'area_border_router': True,
                                                                    'as_boundary_router': True,
                                                                    'checksum': '0x5845',
                                                                    'length': 36,
                                                                    'lsa_id': '3.3.3.3',
                                                                    'option': 'None',
                                                                    'option_desc': 'No TOS-capability, DC',
                                                                    'seq_num': '80000035',
                                                                    'type': 1}}},
                                                        '55.55.55.55 55.55.55.55': 
                                                            {'adv_router': '55.55.55.55',
                                                            'lsa_id': '55.55.55.55',
                                                            'ospfv2': 
                                                                {'body': 
                                                                    {'router': 
                                                                        {'links': 
                                                                            {'20.1.5.1': 
                                                                                {'link_data': '20.1.5.5',
                                                                                'link_id': '20.1.5.1',
                                                                                'num_mtid_metrics': 0,
                                                                                'topologies': 
                                                                                    {0: 
                                                                                        {'metric': 1,
                                                                                        'mt_id': 0,
                                                                                        'tos': 0}},
                                                                                'type': 'transit network'},
                                                                            '20.5.6.6': 
                                                                                {'link_data': '20.5.6.5',
                                                                                'link_id': '20.5.6.6',
                                                                                'num_mtid_metrics': 0,
                                                                                'topologies': 
                                                                                    {0: 
                                                                                        {'metric': 30,
                                                                                        'mt_id': 0,
                                                                                        'tos': 0}},
                                                                                'type': 'transit network'},
                                                                            '55.55.55.55': 
                                                                                {'link_data': '255.255.255.255',
                                                                                'link_id': '55.55.55.55',
                                                                                'num_mtid_metrics': 0,
                                                                                'topologies': 
                                                                                    {0: 
                                                                                        {'metric': 1,
                                                                                        'mt_id': 0,
                                                                                        'tos': 0}},
                                                                                'type': 'stub network'}},
                                                                        'num_of_links': 3}},
                                                                'header': 
                                                                    {'adv_router': '55.55.55.55',
                                                                    'age': 318,
                                                                    'checksum': '0xE7BC',
                                                                    'length': 60,
                                                                    'lsa_id': '55.55.55.55',
                                                                    'option': 'None',
                                                                    'option_desc': 'No TOS-capability, DC',
                                                                    'seq_num': '80000037',
                                                                    'type': 1}}},
                                                        '66.66.66.66 66.66.66.66': 
                                                            {'adv_router': '66.66.66.66',
                                                            'lsa_id': '66.66.66.66',
                                                            'ospfv2': 
                                                                {'body': 
                                                                    {'router': 
                                                                        {'links': 
                                                                            {'20.2.6.6': 
                                                                                {'link_data': '20.2.6.6',
                                                                                'link_id': '20.2.6.6',
                                                                                'num_mtid_metrics': 0,
                                                                                'topologies': 
                                                                                    {0: 
                                                                                        {'metric': 1,
                                                                                        'mt_id': 0,
                                                                                        'tos': 0}},
                                                                                'type': 'transit network'},
                                                                            '20.5.6.6': 
                                                                                {'link_data': '20.5.6.6',
                                                                                'link_id': '20.5.6.6',
                                                                                'num_mtid_metrics': 0,
                                                                                'topologies': 
                                                                                    {0: 
                                                                                        {'metric': 30,
                                                                                        'mt_id': 0,
                                                                                        'tos': 0}},
                                                                                'type': 'transit network'},
                                                                            '20.6.7.6': 
                                                                                {'link_data': '20.6.7.6',
                                                                                'link_id': '20.6.7.6',
                                                                                'num_mtid_metrics': 0,
                                                                                'topologies': {0: {'metric': 30,
                                                                                               'mt_id': 0,
                                                                                               'tos': 0}},
                                                                                'type': 'transit '
                                                                                    'network'},
                                                                                '66.66.66.66': {'link_data': '255.255.255.255',
                                                                                'link_id': '66.66.66.66',
                                                                                'num_mtid_metrics': 0,
                                                                                'topologies': {0: {'metric': 1,
                                                                                                  'mt_id': 0,
                                                                                                  'tos': 0}},
                                                                                'type': 'stub network'}},
                                                                        'num_of_links': 4}},
                                                                'header': 
                                                                    {'adv_router': '66.66.66.66',
                                                                    'age': 520,
                                                                    'checksum': '0x1282',
                                                                    'length': 72,
                                                                    'lsa_id': '66.66.66.66',
                                                                    'option': 'None',
                                                                    'option_desc': 'No '
                                                                               'TOS-capability, '
                                                                               'DC',
                                                                    'seq_num': '8000003C',
                                                                    'type': 1}}},
                                                        '77.77.77.77 77.77.77.77': 
                                                            {'adv_router': '77.77.77.77',
                                                            'lsa_id': '77.77.77.77',
                                                            'ospfv2': 
                                                                {'body': 
                                                                    {'router': 
                                                                        {'links': 
                                                                            {'20.3.7.7': 
                                                                                {'link_data': '20.3.7.7',
                                                                                'link_id': '20.3.7.7',
                                                                                'num_mtid_metrics': 0,
                                                                                'topologies': 
                                                                                    {0: 
                                                                                        {'metric': 1,
                                                                                        'mt_id': 0,
                                                                                        'tos': 0}},
                                                                                'type': 'transit network'},
                                                                            '20.6.7.6': 
                                                                                {'link_data': '20.6.7.7',
                                                                                'link_id': '20.6.7.6',
                                                                                'num_mtid_metrics': 0,
                                                                                'topologies': 
                                                                                    {0: 
                                                                                        {'metric': 30,
                                                                                        'mt_id': 0,
                                                                                        'tos': 0}},
                                                                                'type': 'transit network'},
                                                                            '77.77.77.77': 
                                                                                {'link_data': '255.255.255.255',
                                                                                'link_id': '77.77.77.77',
                                                                                'num_mtid_metrics': 0,
                                                                                'topologies': 
                                                                                    {0: 
                                                                                        {'metric': 1,
                                                                                        'mt_id': 0,
                                                                                        'tos': 0}},
                                                                                'type': 'stub network'}},
                                                                        'num_of_links': 3}},
                                                                'header': 
                                                                    {'adv_router': '77.77.77.77',
                                                                    'age': 288,
                                                                    'checksum': '0x1379',
                                                                    'length': 60,
                                                                    'lsa_id': '77.77.77.77',
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
                                                        {'55.55.11.11 55.55.11.11':
                                                            {'adv_router': '55.55.11.11',
                                                            'lsa_id': '55.55.11.11',
                                                            'ospfv2':
                                                                {'body':
                                                                    {'router':
                                                                        {'links':
                                                                            {'55.55.11.11':
                                                                                {'link_data': '255.255.255.255',
                                                                                'link_id': '55.55.11.11',
                                                                                'num_mtid_metrics': 0,
                                                                                'topologies':
                                                                                    {0:
                                                                                        {'metric': 1,
                                                                                        'mt_id': 0,
                                                                                        'tos': 0}},
                                                                                'type': 'stub network'}},
                                                                        'num_of_links': 1}},
                                                                'header':
                                                                    {'adv_router': '55.55.11.11',
                                                                    'age': 50,
                                                                    'as_boundary_router': True,
                                                                    'checksum': '0x881A',
                                                                    'length': 36,
                                                                    'lsa_id': '55.55.11.11',
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
                                                        {'55.55.11.11 55.55.11.11':
                                                            {'adv_router': '55.55.11.11',
                                                            'lsa_id': '55.55.11.11',
                                                            'ospfv2':
                                                                {'body':
                                                                    {'router':
                                                                        {'num_of_links': 0}},
                                                                'header':
                                                                    {'adv_router': '55.55.11.11',
                                                                    'age': 8,
                                                                    'as_boundary_router': True,
                                                                    'checksum': '0x1D1B',
                                                                    'length': 24,
                                                                    'lsa_id': '55.55.11.11',
                                                                    'option': 'None',
                                                                    'option_desc': 'No TOS-capability, DC',
                                                                    'seq_num': '80000001',
                                                                    'type': 1}}}}}}}}}}}}}}}}

    golden_output1 = {'execute.return_value': '''
        R1_ospf_xe#show ip ospf database router 

            OSPF Router with ID (1.1.1.1) (Process ID 1)

                Router Link States (Area 0)

          LS age: 742
          Options: (No TOS-capability, DC)
          LS Type: Router Links
          Link State ID: 1.1.1.1
          Advertising Router: 1.1.1.1
          LS Seq Number: 8000003D
          Checksum: 0x6228
          Length: 60
          Number of Links: 3

            Link connected to: a Stub Network
             (Link ID) Network/subnet number: 1.1.1.1
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
          Link State ID: 2.2.2.2
          Advertising Router: 2.2.2.2
          LS Seq Number: 80000013
          Checksum: 0x672A
          Length: 72
          Number of Links: 4

            Link connected to: a Stub Network
             (Link ID) Network/subnet number: 2.2.2.2
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
          Link State ID: 3.3.3.3
          Advertising Router: 3.3.3.3
          LS Seq Number: 80000033
          Checksum: 0x75F8
          Length: 60
          Number of Links: 3

            Link connected to: a Stub Network
             (Link ID) Network/subnet number: 3.3.3.3
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
          Link State ID: 4.4.4.4
          Advertising Router: 4.4.4.4
          LS Seq Number: 80000036
          Checksum: 0xA57C
          Length: 72
          AS Boundary Router
          Number of Links: 4

            Link connected to: a Stub Network
             (Link ID) Network/subnet number: 4.4.4.4
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



                    OSPF Router with ID (11.11.11.11) (Process ID 2)

                        Router Link States (Area 1)
                  
          LS age: 1128
          Options: (No TOS-capability, DC)
          LS Type: Router Links
          Link State ID: 3.3.3.3
          Advertising Router: 3.3.3.3
          LS Seq Number: 80000035
          Checksum: 0x5845
          Length: 36
          Area Border Router
          AS Boundary Router
          Number of Links: 1

            Link connected to: a Transit Network
             (Link ID) Designated Router address: 20.3.7.7
             (Link Data) Router Interface address: 20.3.7.3
              Number of MTID metrics: 0
               TOS 0 Metrics: 1


          LS age: 651
          Options: (No TOS-capability, DC)
          LS Type: Router Links
          Link State ID: 11.11.11.11
          Advertising Router: 11.11.11.11
          LS Seq Number: 8000003E
          Checksum: 0x9CE3
          Length: 48
          Area Border Router
          AS Boundary Router
          Number of Links: 2

            Link connected to: another Router (point-to-point)
             (Link ID) Neighboring Router ID: 22.22.22.22
             (Link Data) Router Interface address: 0.0.0.14
              Number of MTID metrics: 0
               TOS 0 Metrics: 111

            Link connected to: a Transit Network
             (Link ID) Designated Router address: 20.1.5.1
             (Link Data) Router Interface address: 20.1.5.1
              Number of MTID metrics: 0
               TOS 0 Metrics: 1


          LS age: 480
          Options: (No TOS-capability, No DC)
          LS Type: Router Links
          Link State ID: 22.22.22.22
          Advertising Router: 22.22.22.22
          LS Seq Number: 80000019
          Checksum: 0xC41A
          Length: 48
          Area Border Router
          AS Boundary Router
          Number of Links: 2

            Link connected to: a Transit Network
             (Link ID) Designated Router address: 20.2.6.6
             (Link Data) Router Interface address: 20.2.6.2
              Number of MTID metrics: 0
               TOS 0 Metrics: 40

            Link connected to: another Router (point-to-point)
             (Link ID) Neighboring Router ID: 11.11.11.11
             (Link Data) Router Interface address: 0.0.0.6
              Number of MTID metrics: 0
               TOS 0 Metrics: 1

                  
          LS age: 318
          Options: (No TOS-capability, DC)
          LS Type: Router Links
          Link State ID: 55.55.55.55
          Advertising Router: 55.55.55.55
          LS Seq Number: 80000037
          Checksum: 0xE7BC
          Length: 60
          Number of Links: 3

            Link connected to: a Stub Network
             (Link ID) Network/subnet number: 55.55.55.55
             (Link Data) Network Mask: 255.255.255.255
              Number of MTID metrics: 0
               TOS 0 Metrics: 1

            Link connected to: a Transit Network
             (Link ID) Designated Router address: 20.5.6.6
             (Link Data) Router Interface address: 20.5.6.5
              Number of MTID metrics: 0
               TOS 0 Metrics: 30

            Link connected to: a Transit Network
             (Link ID) Designated Router address: 20.1.5.1
             (Link Data) Router Interface address: 20.1.5.5
              Number of MTID metrics: 0
               TOS 0 Metrics: 1


          LS age: 520
          Options: (No TOS-capability, DC)
          LS Type: Router Links
          Link State ID: 66.66.66.66
          Advertising Router: 66.66.66.66
          LS Seq Number: 8000003C
          Checksum: 0x1282
          Length: 72
          Number of Links: 4

            Link connected to: a Stub Network
             (Link ID) Network/subnet number: 66.66.66.66
             (Link Data) Network Mask: 255.255.255.255
              Number of MTID metrics: 0
               TOS 0 Metrics: 1

            Link connected to: a Transit Network
             (Link ID) Designated Router address: 20.6.7.6
             (Link Data) Router Interface address: 20.6.7.6
              Number of MTID metrics: 0
               TOS 0 Metrics: 30

            Link connected to: a Transit Network
             (Link ID) Designated Router address: 20.2.6.6
             (Link Data) Router Interface address: 20.2.6.6
              Number of MTID metrics: 0
               TOS 0 Metrics: 1

            Link connected to: a Transit Network
             (Link ID) Designated Router address: 20.5.6.6
             (Link Data) Router Interface address: 20.5.6.6
              Number of MTID metrics: 0
               TOS 0 Metrics: 30


          LS age: 288
          Options: (No TOS-capability, DC)
          LS Type: Router Links
          Link State ID: 77.77.77.77
          Advertising Router: 77.77.77.77
          LS Seq Number: 80000030
          Checksum: 0x1379
          Length: 60
          Number of Links: 3

            Link connected to: a Stub Network
             (Link ID) Network/subnet number: 77.77.77.77
             (Link Data) Network Mask: 255.255.255.255
              Number of MTID metrics: 0
               TOS 0 Metrics: 1

            Link connected to: a Transit Network
             (Link ID) Designated Router address: 20.6.7.6
             (Link Data) Router Interface address: 20.6.7.7
              Number of MTID metrics: 0
               TOS 0 Metrics: 30

            Link connected to: a Transit Network
             (Link ID) Designated Router address: 20.3.7.7
             (Link Data) Router Interface address: 20.3.7.7
              Number of MTID metrics: 0
               TOS 0 Metrics: 1



                    OSPF Router with ID (55.55.11.11) (Process ID 3)

                        Router Link States (Area 0)

          LS age: 50
          Options: (No TOS-capability, DC)
          LS Type: Router Links
          Link State ID: 55.55.11.11
          Advertising Router: 55.55.11.11
          LS Seq Number: 80000001
          Checksum: 0x881A
          Length: 36
          AS Boundary Router
          Number of Links: 1

            Link connected to: a Stub Network
             (Link ID) Network/subnet number: 55.55.11.11
             (Link Data) Network Mask: 255.255.255.255
              Number of MTID metrics: 0
               TOS 0 Metrics: 1



                        Router Link States (Area 11)

          LS age: 8
          Options: (No TOS-capability, DC)
          LS Type: Router Links
          Link State ID: 55.55.11.11
          Advertising Router: 55.55.11.11
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
                                                        {'44.44.44.44 4.4.4.4': 
                                                            {'adv_router': '4.4.4.4',
                                                            'lsa_id': '44.44.44.44',
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
                                                                    {'adv_router': '4.4.4.4',
                                                                    'age': 1595,
                                                                    'checksum': '0x7F60',
                                                                    'length': 36,
                                                                    'lsa_id': '44.44.44.44',
                                                                    'option': 'None',
                                                                    'option_desc': 'No TOS-capability, DC, Upward',
                                                                        'seq_num': '80000001',
                                                                        'type': 5}}}}}}}}}},
                            '2': {}}}}}}}


    golden_output1 = {'execute.return_value': '''
        R1_ospf_xe#show ip ospf database external 

            OSPF Router with ID (1.1.1.1) (Process ID 1)

                Type-5 AS External Link States

          LS age: 1595
          Options: (No TOS-capability, DC, Upward)
          LS Type: AS External Link
          Link State ID: 44.44.44.44 (External Network Number )
          Advertising Router: 4.4.4.4
          LS Seq Number: 80000001
          Checksum: 0x7F60
          Length: 36
          Network Mask: /32
                Metric Type: 2 (Larger than any link state path)
                MTID: 0 
                Metric: 20 
                Forward Address: 0.0.0.0
                External Route Tag: 0


                    OSPF Router with ID (11.11.11.11) (Process ID 2)
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
                                                        {'10.1.2.1 1.1.1.1': 
                                                            {'adv_router': '1.1.1.1',
                                                            'lsa_id': '10.1.2.1',
                                                            'ospfv2': 
                                                                {'body': 
                                                                    {'network': 
                                                                        {'attached_routers': 
                                                                            {'1.1.1.1': {},
                                                                            '2.2.2.2': {}},
                                                                        'network_mask': '255.255.255.0'}},
                                                                'header': 
                                                                    {'adv_router': '1.1.1.1',
                                                                    'age': 786,
                                                                    'checksum': '0x3DD0',
                                                                    'length': 32,
                                                                    'lsa_id': '10.1.2.1',
                                                                    'option': 'None',
                                                                    'option_desc': 'No TOS-capability, DC',
                                                                    'seq_num': '8000000F',
                                                                    'type': 2}}},
                                                        '10.1.4.4 4.4.4.4': 
                                                            {'adv_router': '4.4.4.4',
                                                            'lsa_id': '10.1.4.4',
                                                            'ospfv2': 
                                                                {'body': 
                                                                    {'network': 
                                                                        {'attached_routers': 
                                                                            {'1.1.1.1': {},
                                                                            '4.4.4.4': {}},
                                                                        'network_mask': '255.255.255.0'}},
                                                                'header': 
                                                                    {'adv_router': '4.4.4.4',
                                                                    'age': 1496,
                                                                    'checksum': '0xA431',
                                                                    'length': 32,
                                                                    'lsa_id': '10.1.4.4',
                                                                    'option': 'None',
                                                                    'option_desc': 'No TOS-capability, DC',
                                                                    'seq_num': '8000002E',
                                                                    'type': 2}}},
                                                        '10.2.3.3 3.3.3.3': 
                                                            {'adv_router': '3.3.3.3',
                                                            'lsa_id': '10.2.3.3',
                                                            'ospfv2': 
                                                                {'body': 
                                                                    {'network': 
                                                                        {'attached_routers': 
                                                                            {'2.2.2.2': {},
                                                                            '3.3.3.3': {}},
                                                                        'network_mask': '255.255.255.0'}},
                                                                'header': 
                                                                    {'adv_router': '3.3.3.3',
                                                                    'age': 774,
                                                                    'checksum': '0x2ACF',
                                                                    'length': 32,
                                                                    'lsa_id': '10.2.3.3',
                                                                    'option': 'None',
                                                                    'option_desc': 'No TOS-capability, DC',
                                                                    'seq_num': '8000000F',
                                                                    'type': 2}}},
                                                        '10.2.4.4 4.4.4.4': 
                                                            {'adv_router': '4.4.4.4',
                                                            'lsa_id': '10.2.4.4',
                                                            'ospfv2': 
                                                                {'body': 
                                                                    {'network': 
                                                                        {'attached_routers': 
                                                                            {'2.2.2.2': {},
                                                                            '4.4.4.4': {}},
                                                                        'network_mask': '255.255.255.0'}},
                                                                'header': 
                                                                    {'adv_router': '4.4.4.4',
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
                                                        '10.3.4.4 4.4.4.4': 
                                                            {'adv_router': '4.4.4.4',
                                                            'lsa_id': '10.3.4.4',
                                                            'ospfv2': 
                                                                {'body': 
                                                                    {'network': 
                                                                        {'attached_routers': 
                                                                            {'3.3.3.3': {},
                                                                            '4.4.4.4': {}},
                                                                        'network_mask': '255.255.255.0'}},
                                                                'header': 
                                                                    {'adv_router': '4.4.4.4',
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
                                                    {'20.1.5.1 11.11.11.11': 
                                                        {'adv_router': '11.11.11.11',
                                                        'lsa_id': '20.1.5.1',
                                                        'ospfv2': 
                                                            {'body': 
                                                                {'network': 
                                                                    {'attached_routers': 
                                                                        {'11.11.11.11': {},
                                                                        '55.55.55.55': {}},
                                                                    'network_mask': '255.255.255.0'}},
                                                            'header': 
                                                                {'adv_router': '11.11.11.11',
                                                                'age': 1445,
                                                                'checksum': '0xDFD8',
                                                                'length': 32,
                                                                'lsa_id': '20.1.5.1',
                                                                'option': 'None',
                                                                'option_desc': 'No TOS-capability, DC',
                                                                'seq_num': '80000032',
                                                                'type': 2}}},
                                                    '20.2.6.6 66.66.66.66': 
                                                        {'adv_router': '66.66.66.66',
                                                        'lsa_id': '20.2.6.6',
                                                        'ospfv2': 
                                                            {'body': 
                                                                {'network': 
                                                                    {'attached_routers': 
                                                                        {'22.22.22.22': {},
                                                                        '66.66.66.66': {}},
                                                                    'network_mask': '255.255.255.0'}},
                                                            'header': 
                                                                {'adv_router': '66.66.66.66',
                                                                'age': 1073,
                                                                'checksum': '0x415E',
                                                                'length': 32,
                                                                'lsa_id': '20.2.6.6',
                                                                'option': 'None',
                                                                'option_desc': 'No TOS-capability, DC',
                                                                'seq_num': '8000000F',
                                                                'type': 2}}},
                                                    '20.3.7.7 77.77.77.77': 
                                                        {'adv_router': '77.77.77.77',
                                                        'lsa_id': '20.3.7.7',
                                                        'ospfv2': 
                                                            {'body': 
                                                                {'network': 
                                                                    {'attached_routers': 
                                                                        {'3.3.3.3': {},
                                                                        '77.77.77.77': {}},
                                                                    'network_mask': '255.255.255.0'}},
                                                            'header': 
                                                                {'adv_router': '77.77.77.77',
                                                                'age': 849,
                                                                'checksum': '0x5C19',
                                                                'length': 32,
                                                                'lsa_id': '20.3.7.7',
                                                                'option': 'None',
                                                                'option_desc': 'No TOS-capability, DC',
                                                                'seq_num': '8000002A',
                                                                'type': 2}}},
                                                    '20.5.6.6 66.66.66.66': 
                                                        {'adv_router': '66.66.66.66',
                                                        'lsa_id': '20.5.6.6',
                                                        'ospfv2': 
                                                            {'body': 
                                                                {'network': 
                                                                    {'attached_routers': 
                                                                        {'55.55.55.55': {},
                                                                        '66.66.66.66': {}},
                                                                    'network_mask': '255.255.255.0'}},
                                                            'header': 
                                                                {'adv_router': '66.66.66.66',
                                                                'age': 564,
                                                                'checksum': '0x619C',
                                                                'length': 32,
                                                                'lsa_id': '20.5.6.6',
                                                                'option': 'None',
                                                                'option_desc': 'No '
                                                                'TOS-capability, '
                                                                'DC',
                                                                'seq_num': '80000029',
                                                                'type': 2}}},
                                                    '20.6.7.6 66.66.66.66': 
                                                        {'adv_router': '66.66.66.66',
                                                        'lsa_id': '20.6.7.6',
                                                        'ospfv2': 
                                                            {'body': 
                                                                {'network': 
                                                                    {'attached_routers': 
                                                                        {'66.66.66.66': {},
                                                                        '77.77.77.77': {}},
                                                                    'network_mask': '255.255.255.0'}},
                                                            'header': 
                                                                {'adv_router': '66.66.66.66',
                                                                'age': 1845,
                                                                'checksum': '0x980A',
                                                                'length': 32,
                                                                'lsa_id': '20.6.7.6',
                                                                'option': 'None',
                                                                'option_desc': 'No TOS-capability, DC',
                                                                'seq_num': '8000002A',
                                                                'type': 2}}}}}}}}}}}}}}}}

    golden_output1 = {'execute.return_value': '''
        R1_ospf_xe#show ip ospf database network 

            OSPF Router with ID (1.1.1.1) (Process ID 1)

                Net Link States (Area 0)

          LS age: 786
          Options: (No TOS-capability, DC)
          LS Type: Network Links
          Link State ID: 10.1.2.1 (address of Designated Router)
          Advertising Router: 1.1.1.1
          LS Seq Number: 8000000F
          Checksum: 0x3DD0
          Length: 32
          Network Mask: /24
                Attached Router: 1.1.1.1
                Attached Router: 2.2.2.2

          LS age: 1496
          Options: (No TOS-capability, DC)
          LS Type: Network Links
          Link State ID: 10.1.4.4 (address of Designated Router)
          Advertising Router: 4.4.4.4
          LS Seq Number: 8000002E
          Checksum: 0xA431
          Length: 32
          Network Mask: /24
                Attached Router: 4.4.4.4
                Attached Router: 1.1.1.1

          LS age: 774
          Options: (No TOS-capability, DC)
          LS Type: Network Links
          Link State ID: 10.2.3.3 (address of Designated Router)
          Advertising Router: 3.3.3.3
          LS Seq Number: 8000000F
          Checksum: 0x2ACF
          Length: 32
          Network Mask: /24
                Attached Router: 2.2.2.2
                Attached Router: 3.3.3.3

          LS age: 747
          Options: (No TOS-capability, DC)
          LS Type: Network Links
          Link State ID: 10.2.4.4 (address of Designated Router)
          Advertising Router: 4.4.4.4
          LS Seq Number: 8000000F
          Checksum: 0x9E6
          Length: 32
          Network Mask: /24
                Attached Router: 4.4.4.4
                Attached Router: 2.2.2.2

          LS age: 992
          Options: (No TOS-capability, DC)
          LS Type: Network Links
          Link State ID: 10.3.4.4 (address of Designated Router)
          Advertising Router: 4.4.4.4
          LS Seq Number: 8000002E
          Checksum: 0xF0DA
          Length: 32
          Network Mask: /24
                Attached Router: 4.4.4.4
                Attached Router: 3.3.3.3


                    OSPF Router with ID (11.11.11.11) (Process ID 2)

                        Net Link States (Area 1)
                  
          LS age: 1445
          Options: (No TOS-capability, DC)
          LS Type: Network Links
          Link State ID: 20.1.5.1 (address of Designated Router)
          Advertising Router: 11.11.11.11
          LS Seq Number: 80000032
          Checksum: 0xDFD8
          Length: 32
          Network Mask: /24
                Attached Router: 11.11.11.11
                Attached Router: 55.55.55.55

          LS age: 1073
          Options: (No TOS-capability, DC)
          LS Type: Network Links
          Link State ID: 20.2.6.6 (address of Designated Router)
          Advertising Router: 66.66.66.66
          LS Seq Number: 8000000F
          Checksum: 0x415E
          Length: 32
          Network Mask: /24
                Attached Router: 66.66.66.66
                Attached Router: 22.22.22.22

          LS age: 849
          Options: (No TOS-capability, DC)
          LS Type: Network Links
          Link State ID: 20.3.7.7 (address of Designated Router)
          Advertising Router: 77.77.77.77
          LS Seq Number: 8000002A
          Checksum: 0x5C19
          Length: 32
          Network Mask: /24
                Attached Router: 77.77.77.77
                Attached Router: 3.3.3.3

          LS age: 564
          Options: (No TOS-capability, DC)
          LS Type: Network Links
          Link State ID: 20.5.6.6 (address of Designated Router)
          Advertising Router: 66.66.66.66
          LS Seq Number: 80000029
          Checksum: 0x619C
          Length: 32
          Network Mask: /24
                Attached Router: 66.66.66.66
                Attached Router: 55.55.55.55

          LS age: 1845
          Options: (No TOS-capability, DC)
          LS Type: Network Links
          Link State ID: 20.6.7.6 (address of Designated Router)
          Advertising Router: 66.66.66.66
          LS Seq Number: 8000002A
          Checksum: 0x980A
          Length: 32
          Network Mask: /24
                Attached Router: 66.66.66.66
                Attached Router: 77.77.77.77
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
                                                        {'20.1.3.0 1.1.1.1': 
                                                            {'adv_router': '1.1.1.1',
                                                            'lsa_id': '20.1.3.0',
                                                            'ospfv2': 
                                                                {'body': 
                                                                    {'summary': 
                                                                        {'network_mask': '255.255.255.0',
                                                                        'topologies': 
                                                                            {0: 
                                                                                {'metric': 1,
                                                                                'mt_id': 0}}}},
                                                                'header': 
                                                                    {'adv_router': '1.1.1.1',
                                                                    'age': 422,
                                                                    'checksum': '0x43DC',
                                                                    'length': 28,
                                                                    'lsa_id': '20.1.3.0',
                                                                    'option': 'None',
                                                                    'option_desc': 'No TOS-capability, DC, Upward',
                                                                    'seq_num': '80000001',
                                                                    'type': 3}}},
                                                        '20.1.3.0 3.3.3.3': 
                                                            {'adv_router': '3.3.3.3',
                                                            'lsa_id': '20.1.3.0',
                                                            'ospfv2': 
                                                                {'body': 
                                                                    {'summary': 
                                                                        {'network_mask': '255.255.255.0',
                                                                        'topologies': 
                                                                            {0: 
                                                                                {'metric': 40,
                                                                                'mt_id': 0}}}},
                                                                'header': 
                                                                    {'adv_router': '3.3.3.3',
                                                                    'age': 372,
                                                                    'checksum': '0x6EA1',
                                                                    'length': 28,
                                                                    'lsa_id': '20.1.3.0',
                                                                    'option': 'None',
                                                                    'option_desc': 'No TOS-capability, No DC, Upward',
                                                                    'seq_num': '80000002',
                                                                    'type': 3}}},
                                                        '20.2.3.0 3.3.3.3': 
                                                            {'adv_router': '3.3.3.3',
                                                            'lsa_id': '20.2.3.0',
                                                            'ospfv2': 
                                                                {'body': 
                                                                    {'summary': 
                                                                        {'network_mask': '255.255.255.0',
                                                                        'topologies': 
                                                                            {0: 
                                                                                {'metric': 40,
                                                                                'mt_id': 0}}}},
                                                                'header': 
                                                                    {'adv_router': '3.3.3.3',
                                                                    'age': 372,
                                                                    'checksum': '0x62AC',
                                                                    'length': 28,
                                                                    'lsa_id': '20.2.3.0',
                                                                    'option': 'None',
                                                                    'option_desc': 'No TOS-capability, No DC, Upward',
                                                                    'seq_num': '80000002',
                                                                    'type': 3}}},
                                                        '20.2.4.0 3.3.3.3': 
                                                            {'adv_router': '3.3.3.3',
                                                            'lsa_id': '20.2.4.0',
                                                            'ospfv2': 
                                                                {'body': 
                                                                    {'summary': 
                                                                        {'network_mask': '255.255.255.0',
                                                                        'topologies': 
                                                                            {0: 
                                                                                {'metric': 41,
                                                                                'mt_id': 0}}}},
                                                                'header': 
                                                                    {'adv_router': '3.3.3.3',
                                                                    'age': 131,
                                                                    'checksum': '0x5DAD',
                                                                    'length': 28,
                                                                    'lsa_id': '20.2.4.0',
                                                                    'option': 'None',
                                                                    'option_desc': 'No TOS-capability, No DC, Upward',
                                                                    'seq_num': '80000004',
                                                                    'type': 3}}},
                                                        '20.3.4.0 3.3.3.3': 
                                                            {'adv_router': '3.3.3.3',
                                                            'lsa_id': '20.3.4.0',
                                                            'ospfv2': 
                                                                {'body': 
                                                                    {'summary': 
                                                                        {'network_mask': '255.255.255.0',
                                                                        'topologies': 
                                                                            {0: 
                                                                                {'metric': 40,
                                                                                'mt_id': 0}}}},
                                                                'header': 
                                                                    {'adv_router': '3.3.3.3',
                                                                    'age': 372,
                                                                    'checksum': '0x4BC1',
                                                                    'length': 28,
                                                                    'lsa_id': '20.3.4.0',
                                                                    'option': 'None',
                                                                    'option_desc': 'No TOS-capability, No DC, Upward',
                                                                    'seq_num': '80000002',
                                                                    'type': 3}}},
                                                        '4.4.4.4 3.3.3.3': 
                                                            {'adv_router': '3.3.3.3',
                                                            'lsa_id': '4.4.4.4',
                                                            'ospfv2': 
                                                                {'body': 
                                                                    {'summary': 
                                                                        {'network_mask': '255.255.255.255',
                                                                        'topologies': 
                                                                            {0: 
                                                                                {'metric': 41,
                                                                                'mt_id': 0}}}},
                                                                'header': 
                                                                    {'adv_router': '3.3.3.3',
                                                                    'age': 131,
                                                                    'checksum': '0xEF26',
                                                                    'length': 28,
                                                                    'lsa_id': '4.4.4.4',
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
                                                        {'1.1.0.0 1.1.1.1': 
                                                            {'adv_router': '1.1.1.1',
                                                            'lsa_id': '1.1.0.0',
                                                            'ospfv2': 
                                                                {'body': 
                                                                    {'summary': 
                                                                        {'network_mask': '255.255.0.0',
                                                                        'topologies': 
                                                                            {0: 
                                                                                {'metric': 10,
                                                                                'mt_id': 0}}}},
                                                                'header': 
                                                                    {'adv_router': '1.1.1.1',
                                                                    'age': 424,
                                                                    'checksum': '0x5CCA',
                                                                    'length': 28,
                                                                    'lsa_id': '1.1.0.0',
                                                                    'option': 'None',
                                                                    'option_desc': 'No TOS-capability, DC, Upward',
                                                                    'seq_num': '80000001',
                                                                    'type': 3}}},
                                                        '10.1.2.0 1.1.1.1': 
                                                            {'adv_router': '1.1.1.1',
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
                                                                    {'adv_router': '1.1.1.1',
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
                                                        '10.1.3.0 1.1.1.1': 
                                                            {'adv_router': '1.1.1.1',
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
                                                                    {'adv_router': '1.1.1.1',
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
                                                        '10.2.3.0 1.1.1.1': 
                                                            {'adv_router': '1.1.1.1',
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
                                                                    {'adv_router': '1.1.1.1',
                                                                    'age': 365,
                                                                    'checksum': '0x6174',
                                                                    'length': 28,
                                                                    'lsa_id': '10.2.3.0',
                                                                    'option': 'None',
                                                                    'option_desc': 'No TOS-capability, DC, Upward',
                                                                    'seq_num': '80000001',
                                                                    'type': 3}}},
                                                        '20.2.3.0 1.1.1.1': 
                                                            {'adv_router': '1.1.1.1',
                                                            'lsa_id': '20.2.3.0',
                                                            'ospfv2': 
                                                                {'body': 
                                                                    {'summary': 
                                                                        {'network_mask': '255.255.255.0',
                                                                        'topologies': 
                                                                            {0: 
                                                                                {'metric': 65575,
                                                                                'mt_id': 0}}}},
                                                                'header': 
                                                                    {'adv_router': '1.1.1.1',
                                                                    'age': 365,
                                                                    'checksum': '0x628F',
                                                                    'length': 28,
                                                                    'lsa_id': '20.2.3.0',
                                                                    'option': 'None',
                                                                    'option_desc': 'No TOS-capability, DC, Upward',
                                                                    'seq_num': '80000001',
                                                                    'type': 3}}},
                                                        '20.2.4.0 1.1.1.1': 
                                                            {'adv_router': '1.1.1.1',
                                                            'lsa_id': '20.2.4.0',
                                                            'ospfv2': 
                                                                {'body': 
                                                                    {'summary': 
                                                                        {'network_mask': '255.255.255.0',
                                                                        'topologies': 
                                                                            {0: 
                                                                                {'metric': 65576,
                                                                                'mt_id': 0}}}},
                                                                'header': 
                                                                    {'adv_router': '1.1.1.1',
                                                                    'age': 130,
                                                                    'checksum': '0x5D90',
                                                                    'length': 28,
                                                                    'lsa_id': '20.2.4.0',
                                                                    'option': 'None',
                                                                    'option_desc': 'No TOS-capability, DC, Upward',
                                                                    'seq_num': '80000003',
                                                                    'type': 3}}},
                                                        '20.3.4.0 1.1.1.1': 
                                                            {'adv_router': '1.1.1.1',
                                                            'lsa_id': '20.3.4.0',
                                                            'ospfv2': 
                                                                {'body': 
                                                                    {'summary': 
                                                                        {'network_mask': '255.255.255.0',
                                                                        'topologies': 
                                                                            {0: 
                                                                                {'metric': 65575,
                                                                                'mt_id': 0}}}},
                                                                'header': 
                                                                    {'adv_router': '1.1.1.1',
                                                                    'age': 365,
                                                                    'checksum': '0x4BA4',
                                                                    'length': 28,
                                                                    'lsa_id': '20.3.4.0',
                                                                    'option': 'None',
                                                                    'option_desc': 'No TOS-capability, DC, Upward',
                                                                    'seq_num': '80000001',
                                                                    'type': 3}}},
                                                        '3.3.3.3 1.1.1.1': 
                                                            {'adv_router': '1.1.1.1',
                                                            'lsa_id': '3.3.3.3',
                                                            'ospfv2': 
                                                                {'body': 
                                                                    {'summary': 
                                                                        {'network_mask': '255.255.255.255',
                                                                        'topologies': 
                                                                            {0: 
                                                                                {'metric': 65536,
                                                                                'mt_id': 0}}}},
                                                                'header': 
                                                                    {'adv_router': '1.1.1.1',
                                                                    'age': 365,
                                                                    'checksum': '0x8E97',
                                                                    'length': 28,
                                                                    'lsa_id': '3.3.3.3',
                                                                    'option': 'None',
                                                                    'option_desc': 'No TOS-capability, DC, Upward',
                                                                    'seq_num': '80000001',
                                                                    'type': 3}}},
                                                        '4.4.4.4 1.1.1.1': 
                                                            {'adv_router': '1.1.1.1',
                                                            'lsa_id': '4.4.4.4',
                                                            'ospfv2': 
                                                                {'body': 
                                                                    {'summary': 
                                                                        {'network_mask': '255.255.255.255',
                                                                        'topologies': 
                                                                            {0: 
                                                                                {'metric': 65576,
                                                                                'mt_id': 0}}}},
                                                                'header': 
                                                                    {'adv_router': '1.1.1.1',
                                                                    'age': 130,
                                                                    'checksum': '0xEF09',
                                                                    'length': 28,
                                                                    'lsa_id': '4.4.4.4',
                                                                    'option': 'None',
                                                                    'option_desc': 'No TOS-capability, DC, Upward',
                                                                    'seq_num': '80000002',
                                                                    'type': 3}}}}}}}}}}}}}}}}

    golden_output1 = {'execute.return_value': '''
        R1_ospf_xe#show ip ospf database summary 

            OSPF Router with ID (1.1.1.1) (Process ID 1)

                Summary Net Link States (Area 0)

          LS age: 131
          Options: (No TOS-capability, No DC, Upward)
          LS Type: Summary Links(Network)
          Link State ID: 4.4.4.4 (summary Network Number)
          Advertising Router: 3.3.3.3
          LS Seq Number: 80000003
          Checksum: 0xEF26
          Length: 28
          Network Mask: /32
                MTID: 0         Metric: 41 

          LS age: 422
          Options: (No TOS-capability, DC, Upward)
          LS Type: Summary Links(Network)
          Link State ID: 20.1.3.0 (summary Network Number)
          Advertising Router: 1.1.1.1
          LS Seq Number: 80000001
          Checksum: 0x43DC
          Length: 28
          Network Mask: /24
                MTID: 0         Metric: 1 

          LS age: 372
          Options: (No TOS-capability, No DC, Upward)
          LS Type: Summary Links(Network)
          Link State ID: 20.1.3.0 (summary Network Number)
          Advertising Router: 3.3.3.3
          LS Seq Number: 80000002
          Checksum: 0x6EA1
          Length: 28
          Network Mask: /24
                MTID: 0         Metric: 40 

          LS age: 372
          Options: (No TOS-capability, No DC, Upward)
          LS Type: Summary Links(Network)
          Link State ID: 20.2.3.0 (summary Network Number)
          Advertising Router: 3.3.3.3
          LS Seq Number: 80000002
          Checksum: 0x62AC
          Length: 28
          Network Mask: /24
                MTID: 0         Metric: 40 

          LS age: 131
          Options: (No TOS-capability, No DC, Upward)
          LS Type: Summary Links(Network)
          Link State ID: 20.2.4.0 (summary Network Number)
          Advertising Router: 3.3.3.3
          LS Seq Number: 80000004
          Checksum: 0x5DAD
          Length: 28
          Network Mask: /24
                MTID: 0         Metric: 41 

          LS age: 372
          Options: (No TOS-capability, No DC, Upward)
          LS Type: Summary Links(Network)
          Link State ID: 20.3.4.0 (summary Network Number)
          Advertising Router: 3.3.3.3
          LS Seq Number: 80000002
          Checksum: 0x4BC1
          Length: 28
          Network Mask: /24
                MTID: 0         Metric: 40 


                        Summary Net Link States (Area 1)

          LS age: 424
          Options: (No TOS-capability, DC, Upward)
          LS Type: Summary Links(Network)
          Link State ID: 1.1.0.0 (summary Network Number)
          Advertising Router: 1.1.1.1
          LS Seq Number: 80000001
          Checksum: 0x5CCA
          Length: 28
          Network Mask: /16
                MTID: 0         Metric: 10 

          LS age: 365
          Options: (No TOS-capability, DC, Upward)
          LS Type: Summary Links(Network)
          Link State ID: 3.3.3.3 (summary Network Number)
          Advertising Router: 1.1.1.1
          LS Seq Number: 80000001
          Checksum: 0x8E97
          Length: 28
          Network Mask: /32
                MTID: 0         Metric: 65536 

          LS age: 130
          Options: (No TOS-capability, DC, Upward)
          LS Type: Summary Links(Network)
          Link State ID: 4.4.4.4 (summary Network Number)
          Advertising Router: 1.1.1.1
          LS Seq Number: 80000002
          Checksum: 0xEF09
          Length: 28
          Network Mask: /32
                MTID: 0         Metric: 65576 

          LS age: 422
          Options: (No TOS-capability, DC, Upward)
          LS Type: Summary Links(Network)
          Link State ID: 10.1.2.0 (summary Network Number)
          Advertising Router: 1.1.1.1
          LS Seq Number: 80000001
          Checksum: 0xC6EF
          Length: 28
          Network Mask: /24
                MTID: 0         Metric: 111 

          LS age: 364
          Options: (No TOS-capability, DC, Upward)
          LS Type: Summary Links(Network)
          Link State ID: 10.1.3.0 (summary Network Number)
          Advertising Router: 1.1.1.1
          LS Seq Number: 80000002
          Checksum: 0x5FC4
          Length: 28
          Network Mask: /24
                MTID: 0         Metric: 65535 

          LS age: 365
          Options: (No TOS-capability, DC, Upward)
          LS Type: Summary Links(Network)
          Link State ID: 10.2.3.0 (summary Network Number)
          Advertising Router: 1.1.1.1
          LS Seq Number: 80000001
          Checksum: 0x6174
          Length: 28
          Network Mask: /24
                MTID: 0         Metric: 65868 

          LS age: 365
          Options: (No TOS-capability, DC, Upward)
          LS Type: Summary Links(Network)
          Link State ID: 20.2.3.0 (summary Network Number)
          Advertising Router: 1.1.1.1
          LS Seq Number: 80000001
          Checksum: 0x628F
          Length: 28
          Network Mask: /24
                MTID: 0         Metric: 65575 

          LS age: 130
          Options: (No TOS-capability, DC, Upward)
          LS Type: Summary Links(Network)
          Link State ID: 20.2.4.0 (summary Network Number)
          Advertising Router: 1.1.1.1
          LS Seq Number: 80000003
          Checksum: 0x5D90
          Length: 28
          Network Mask: /24
                MTID: 0         Metric: 65576 
                  
          LS age: 365
          Options: (No TOS-capability, DC, Upward)
          LS Type: Summary Links(Network)
          Link State ID: 20.3.4.0 (summary Network Number)
          Advertising Router: 1.1.1.1
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
                                                {10: 
                                                    {'lsa_type': 10,
                                                    'lsas': 
                                                        {'1.0.0.0 1.1.1.1': 
                                                            {'adv_router': '1.1.1.1',
                                                            'lsa_id': '1.0.0.0',
                                                            'ospfv2': 
                                                                {'body': 
                                                                    {'opaque': 
                                                                        {'num_of_links': 0}},
                                                                'header': 
                                                                    {'adv_router': '1.1.1.1',
                                                                    'age': 370,
                                                                    'checksum': '0x56D2',
                                                                    'fragment_number': 0,
                                                                    'length': 28,
                                                                    'lsa_id': '1.0.0.0',
                                                                    'mpls_te_router_id': '1.1.1.1',
                                                                    'opaque_id': 0,
                                                                    'opaque_type': 1,
                                                                    'option': 'None',
                                                                    'option_desc': 'No '
                                                                                'TOS-capability, '
                                                                                'DC',
                                                                    'seq_num': '80000002',
                                                                    'type': 10}}},
                                                        '1.0.0.0 2.2.2.2': 
                                                            {'adv_router': '2.2.2.2',
                                                            'lsa_id': '1.0.0.0',
                                                            'ospfv2': 
                                                                {'body': 
                                                                    {'opaque': 
                                                                        {'num_of_links': 0}},
                                                                'header': 
                                                                    {'adv_router': '2.2.2.2',
                                                                    'age': 1420,
                                                                    'checksum': '0x1E21',
                                                                    'fragment_number': 0,
                                                                    'length': 28,
                                                                    'lsa_id': '1.0.0.0',
                                                                    'mpls_te_router_id': '2.2.2.2',
                                                                    'opaque_id': 0,
                                                                    'opaque_type': 1,
                                                                    'option': 'None',
                                                                    'option_desc': 'No '
                                                                                'TOS-capability, '
                                                                                'No '
                                                                                'DC',
                                                                    'seq_num': '80000002',
                                                                    'type': 10}}},
                                                        '1.0.0.0 3.3.3.3': 
                                                            {'adv_router': '3.3.3.3',
                                                            'lsa_id': '1.0.0.0',
                                                            'ospfv2': 
                                                                {'body': 
                                                                    {'opaque': 
                                                                        {'num_of_links': 0}},
                                                                'header': 
                                                                    {'adv_router': '3.3.3.3',
                                                                    'age': 123,
                                                                    'checksum': '0x5EBA',
                                                                    'fragment_number': 0,
                                                                    'length': 28,
                                                                    'lsa_id': '1.0.0.0',
                                                                    'mpls_te_router_id': '3.3.3.3',
                                                                    'opaque_id': 0,
                                                                    'opaque_type': 1,
                                                                    'option': 'None',
                                                                    'option_desc': 'No '
                                                                                'TOS-capability, '
                                                                                'DC',
                                                                    'seq_num': '80000002',
                                                                    'type': 10}}},
                                                        '1.0.0.1 1.1.1.1': 
                                                            {'adv_router': '1.1.1.1',
                                                            'lsa_id': '1.0.0.1',
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
                                                                    {'adv_router': '1.1.1.1',
                                                                    'age': 370,
                                                                    'checksum': '0x6586',
                                                                    'fragment_number': 1,
                                                                    'length': 124,
                                                                    'lsa_id': '1.0.0.1',
                                                                    'opaque_id': 1,
                                                                    'opaque_type': 1,
                                                                    'option': 'None',
                                                                    'option_desc': 'No TOS-capability, DC',
                                                                    'seq_num': '80000002',
                                                                    'type': 10}}},
                                                        '1.0.0.2 1.1.1.1': 
                                                            {'adv_router': '1.1.1.1',
                                                            'lsa_id': '1.0.0.2',
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
                                                                    {'adv_router': '1.1.1.1',
                                                                    'age': 370,
                                                                    'checksum': '0xB43D',
                                                                    'fragment_number': 2,
                                                                    'length': 124,
                                                                    'lsa_id': '1.0.0.2',
                                                                    'opaque_id': 2,
                                                                    'opaque_type': 1,
                                                                    'option': 'None',
                                                                    'option_desc': 'No TOS-capability, DC',
                                                                    'seq_num': '80000002',
                                                                    'type': 10}}},
                                                        '1.0.0.37 2.2.2.2': 
                                                            {'adv_router': '2.2.2.2',
                                                            'lsa_id': '1.0.0.37',
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
                                                                    {'adv_router': '2.2.2.2',
                                                                    'age': 1010,
                                                                    'checksum': '0xE691',
                                                                    'fragment_number': 37,
                                                                    'length': 116,
                                                                    'lsa_id': '1.0.0.37',
                                                                    'opaque_id': 37,
                                                                    'opaque_type': 1,
                                                                    'option': 'None',
                                                                    'option_desc': 'No TOS-capability, No DC',
                                                                    'seq_num': '80000003',
                                                                    'type': 10}}},
                                                        '1.0.0.38 2.2.2.2': 
                                                            {'adv_router': '2.2.2.2',
                                                            'lsa_id': '1.0.0.38',
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
                                                                    {'adv_router': '2.2.2.2',
                                                                    'age': 1000,
                                                                    'checksum': '0x254F',
                                                                    'fragment_number': 38,
                                                                    'length': 116,
                                                                    'lsa_id': '1.0.0.38',
                                                                    'opaque_id': 38,
                                                                    'opaque_type': 1,
                                                                    'option': 'None',
                                                                    'option_desc': 'No TOS-capability, No DC',
                                                                    'seq_num': '80000003',
                                                                    'type': 10}}},
                                                        '1.0.0.39 2.2.2.2': 
                                                            {'adv_router': '2.2.2.2',
                                                            'lsa_id': '1.0.0.39',
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
                                                                    {'adv_router': '2.2.2.2',
                                                                    'age': 1000,
                                                                    'checksum': '0x4438',
                                                                    'fragment_number': 39,
                                                                    'length': 116,
                                                                    'lsa_id': '1.0.0.39',
                                                                    'opaque_id': 39,
                                                                    'opaque_type': 1,
                                                                    'option': 'None',
                                                                    'option_desc': 'No TOS-capability, No DC',
                                                                    'seq_num': '80000003',
                                                                    'type': 10}}},
                                                        '1.0.0.4 3.3.3.3': 
                                                            {'adv_router': '3.3.3.3',
                                                            'lsa_id': '1.0.0.4',
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
                                                                    {'adv_router': '3.3.3.3',
                                                                    'age': 123,
                                                                    'checksum': '0x915D',
                                                                    'fragment_number': 4,
                                                                    'length': 160,
                                                                    'lsa_id': '1.0.0.4',
                                                                    'opaque_id': 4,
                                                                    'opaque_type': 1,
                                                                    'option': 'None',
                                                                    'option_desc': 'No TOS-capability, DC',
                                                                    'seq_num': '80000002',
                                                                    'type': 10}}},
                                                        '1.0.0.6 3.3.3.3': 
                                                            {'adv_router': '3.3.3.3',
                                                            'lsa_id': '1.0.0.6',
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
                                                                    {'adv_router': '3.3.3.3',
                                                                    'age': 123,
                                                                    'checksum': '0x5EC',
                                                                    'fragment_number': 6,
                                                                    'length': 160,
                                                                    'lsa_id': '1.0.0.6',
                                                                    'opaque_id': 6,
                                                                    'opaque_type': 1,
                                                                    'option': 'None',
                                                                    'option_desc': 'No TOS-capability, DC',
                                                                    'seq_num': '80000002',
                                                                    'type': 10}}}}}}}}}},
                            '2': {}}}}}}}

    golden_output1 = {'execute.return_value': '''
        R1_ospf_xe#show ip ospf database opaque-area 

            OSPF Router with ID (1.1.1.1) (Process ID 1)

                Type-10 Opaque Area Link States (Area 0)

          LS age: 370
          Options: (No TOS-capability, DC)
          LS Type: Opaque Area Link
          Link State ID: 1.0.0.0
          Opaque Type: 1 (Traffic Engineering)
          Opaque ID: 0
          Advertising Router: 1.1.1.1
          LS Seq Number: 80000002
          Checksum: 0x56D2
          Length: 28
          Fragment number : 0

            MPLS TE router ID : 1.1.1.1

            Number of Links : 0

          LS age: 1420
          Options: (No TOS-capability, No DC)
          LS Type: Opaque Area Link
          Link State ID: 1.0.0.0
          Opaque Type: 1 (Traffic Engineering)
          Opaque ID: 0
          Advertising Router: 2.2.2.2
          LS Seq Number: 80000002
          Checksum: 0x1E21
          Length: 28
          Fragment number : 0

            MPLS TE router ID : 2.2.2.2

            Number of Links : 0

          LS age: 123
          Options: (No TOS-capability, DC)
          LS Type: Opaque Area Link
          Link State ID: 1.0.0.0
          Opaque Type: 1 (Traffic Engineering)
          Opaque ID: 0
          Advertising Router: 3.3.3.3
          LS Seq Number: 80000002
          Checksum: 0x5EBA
          Length: 28
          Fragment number : 0

            MPLS TE router ID : 3.3.3.3

            Number of Links : 0

          LS age: 370
          Options: (No TOS-capability, DC)
          LS Type: Opaque Area Link
          Link State ID: 1.0.0.1
          Opaque Type: 1 (Traffic Engineering)
          Opaque ID: 1
          Advertising Router: 1.1.1.1
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
          Link State ID: 1.0.0.2
          Opaque Type: 1 (Traffic Engineering)
          Opaque ID: 2
          Advertising Router: 1.1.1.1
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
          Link State ID: 1.0.0.4
          Opaque Type: 1 (Traffic Engineering)
          Opaque ID: 4
          Advertising Router: 3.3.3.3
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
          Link State ID: 1.0.0.6
          Opaque Type: 1 (Traffic Engineering)
          Opaque ID: 6
          Advertising Router: 3.3.3.3
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
          Link State ID: 1.0.0.37
          Opaque Type: 1 (Traffic Engineering)
          Opaque ID: 37
          Advertising Router: 2.2.2.2
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
          Link State ID: 1.0.0.38
          Opaque Type: 1 (Traffic Engineering)
          Opaque ID: 38
          Advertising Router: 2.2.2.2
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
          Link State ID: 1.0.0.39
          Opaque Type: 1 (Traffic Engineering)
          Opaque ID: 39
          Advertising Router: 2.2.2.2
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


            OSPF Router with ID (11.11.11.11) (Process ID 2)
        '''}

    def test_show_ip_ospf_database_opaque_area_full1(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output1)
        obj = ShowIpOspfDatabaseOpaqueArea(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output1)

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
                                                        'state': 'up'}}},
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
                                        'autoconfig_area_id': '0.0.0.1',
                                        'igp_sync': False}}}}}}},
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
                                        'autoconfig_area_id': '0.0.0.0',
                                        'igp_sync': False}}}}}}}}}

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
          Interface is up 
        TenGigabitEthernet3/0/1
          Process ID 1, Area 0
          LDP is not configured through LDP autoconfig
          LDP-IGP Synchronization : Not required
          Holddown timer is disabled
          Interface is down
        '''}

    def test_show_ip_ospf_mpls_ldp_interface_full1(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output1)
        obj = ShowIpOspfMplsLdpInterface(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output1)

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
                                        {'router_id': '11.11.11.11'}}}}}}},
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
                                        {'router_id': '1.1.1.1'}}}}}}}}}
    
    def test_show_ip_ospf_mpls_traffic_eng_link_full1(self):
        
        self.maxDiff = None

        def mapper(key):
            return self.outputs[key]
        
        raw1 = '''\
            R1_ospf_xe#show ip ospf mpls traffic-eng link 

            OSPF Router with ID (1.1.1.1) (Process ID 1)

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

                OSPF Router with ID (11.11.11.11) (Process ID 2)

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


if __name__ == '__main__':
    unittest.main()
