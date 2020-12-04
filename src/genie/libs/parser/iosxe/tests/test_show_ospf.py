
# Python
import unittest
from unittest.mock import Mock

# ATS
from pyats.topology import Device
from pyats.topology import loader

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
                                               ShowIpOspfMplsTrafficEngLink2,
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
                                               ShowIpOspfDatabaseOpaqueAreaAdvRouter,
                                               ShowIpOspfNeighborDetail2)

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
        self.outputs['show ip ospf interface GigabitEthernet2'] = raw2_1
        self.outputs['show ip ospf interface GigabitEthernet1'] = raw2_2
        self.outputs['show ip ospf interface OSPF_SL1'] = raw2_3
        self.outputs['show ip ospf interface GigabitEthernet3'] = raw2_4
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
        self.outputs['show ip ospf interface OSPF_VL1'] = raw2_1
        self.outputs['show ip ospf interface GigabitEthernet0/1'] = raw2_2
        self.outputs['show ip ospf interface GigabitEthernet0/0'] = raw2_3

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
        self.outputs['show ip ospf interface TenGigabitEthernet3/1/1'] = raw2_1
        self.outputs['show ip ospf interface TenGigabitEthernet3/1/2'] = raw2_2
        self.outputs['show ip ospf interface TenGigabitEthernet3/1/3'] = raw2_3
        self.outputs['show ip ospf interface TenGigabitEthernet3/1/4'] = raw2_4
        self.outputs['show ip ospf interface TenGigabitEthernet3/1/5'] = raw2_5

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
        self.outputs['show ip ospf interface GigabitEthernet5'] = raw2_1
        self.outputs['show ip ospf interface GigabitEthernet4'] = raw2_2
        self.outputs['show ip ospf interface GigabitEthernet3'] = raw2_3
        self.outputs['show ip ospf interface GigabitEthernet2'] = raw2_4

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
    
    golden_parsed_output5 = {
        'vrf': {
            'default': {
                'address_family': {
                    'ipv4': {
                        'instance': {
                            '1668': {
                                'areas': {
                                    '0.0.0.0': {
                                        'interfaces': {
                                            'TenGigabitEthernet3/1/1': {
                                                'neighbors': {
                                                    '10.25.0.102': {
                                                        'address': '10.16.255.210',
                                                        'bdr_ip_addr': '0.0.0.0',
                                                        'dead_timer': '00:00:07',
                                                        'dr_ip_addr': '0.0.0.0',
                                                        'first': '0x0(0)/0x0(0)',
                                                        'index': '8/9,',
                                                        'bfd_state': 'enabled',
                                                        'interface': 'TenGigabitEthernet3/1/1',
                                                        'neighbor_router_id': '10.25.0.102',
                                                        'next': '0x0(0)/0x0(0)',
                                                        'priority': 0,
                                                        'state': 'full',
                                                        'statistics': {
                                                            'last_retrans_max_scan_length': 6,
                                                            'last_retrans_max_scan_time_msec': 4,
                                                            'last_retrans_scan_length': 0,
                                                            'last_retrans_scan_time_msec': 0,
                                                            'nbr_event_count': 6,
                                                            'nbr_retrans_qlen': 0,
                                                            'total_retransmission': 383,
                                                        },
                                                        'uptime': '8w0d',
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
    def test_show_ip_ospf_neighbor_detail_full5(self):

        self.maxDiff = None

        def mapper(key):
            return self.outputs[key]
        
        raw1 = '''\
            nhq-choke-VSS#sh ip ospf neighbor detail
            show ip ospf neighbor detail
            Neighbor 10.25.0.102, interface address 10.16.255.210
                In the area 0 via interface TenGigabitEthernet3/1/1, BFD enabled
                Neighbor priority is 0, State is FULL, 6 state changes
                DR is 0.0.0.0 BDR is 0.0.0.0
                Options is 0x12 in Hello (E-bit, L-bit)
                Options is 0x52 in DBD (E-bit, L-bit, O-bit)
                LLS Options is 0x1 (LR)
                Dead timer due in 00:00:07
                Neighbor is up for 8w0d    
                Index 8/9, retransmission queue length 0, number of retransmission 383
                First 0x0(0)/0x0(0) Next 0x0(0)/0x0(0)
                Last retransmission scan length is 0, maximum is 6
                Last retransmission scan time is 0 msec, maximum is 4 msec'''
        raw2_1 = '''\
            nhq-choke-VSS#show ip ospf interface | section TenGigabitEthernet3/1/1
            TenGigabitEthernet3/1/1 is up, line protocol is up (connected) 
                Internet Address 10.16.255.209/30, Area 0, Attached via Interface Enable
                Process ID 1668, Router ID 10.31.208.123, Network Type POINT_TO_POINT, Cost: 100
                Topology-MTID    Cost    Disabled    Shutdown      Topology Name
                        0           100       no          no            Base
                Enabled by interface config, including secondary ip addresses
                Transmit Delay is 1 sec, State POINT_TO_POINT, BFD enabled
                Timer intervals configured, Hello 2, Dead 6, Wait 6, Retransmit 5
                    oob-resync timeout 40
                    Hello due in 00:00:01
                Supports Link-local Signaling (LLS)
                Cisco NSF helper support enabled
                IETF NSF helper support enabled
                Can be protected by per-prefix Loop-Free FastReroute
                Can be used for per-prefix Loop-Free FastReroute repair paths
                Index 3/3, flood queue length 0
                Next 0x0(0)/0x0(0)
                Last flood scan length is 1, maximum is 51
                Last flood scan time is 0 msec, maximum is 4 msec
                Neighbor Count is 1, Adjacent neighbor count is 1 
                    Adjacent with neighbor 10.25.0.102
                Suppress hello for 0 neighbor(s)
            '''
        raw3_2 = '''\
            R1_ospf_xe#show running-config | section router ospf 1668
            show running-config | section router ospf 1668
                router ospf 1668
                router-id 10.31.208.123
                default-information originate
            '''
        self.outputs = {}
        self.outputs['show ip ospf interface TenGigabitEthernet3/1/1'] = raw2_1
        self.outputs['show ip ospf neighbor detail'] = raw1
        self.outputs['show running-config | section router ospf 1668'] = raw3_2
        self.device.execute = Mock()
        self.device.execute.side_effect = mapper
        obj = ShowIpOspfNeighborDetail(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output5)



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
    golden_parsed_output2 = {
       "vrf":{
          "default":{
             "address_family":{
                "ipv4":{
                   "areas":{
                      "0.0.0.1":{
                         "sham_links":{
                            "10.229.11.11 10.151.22.22":{
                               "transit_area_id":"0.0.0.1",
                               "local_id":"10.229.11.11",
                               "demand_circuit":True,
                               "name":"SL0",
                               "remote_id":"10.151.22.22",
                               "link_state":"up",
                               "dcbitless_lsa_count":1,
                               "donotage_lsa":"not allowed",
                               "cost":111,
                               "state":"point_to_point,",
                               "hello_interval":10,
                               "dead_interval":40,
                               "wait_interval":40,
                               "ttl_security":{
                                  "enable":True,
                                  "hops":3
                               },
                               "hello_timer":"00:00:00",
                               "adjacency_state":"full",
                               "index":"1/2/2",
                               "retrans_qlen":0,
                               "total_retransmission":2,
                               "first":"0x0(0)/0x0(0)/0x0(0)",
                               "next":"0x0(0)/0x0(0)/0x0(0)",
                               "last_retransmission_scan_length":1,
                               "last_retransmission_max_length":1,
                               "last_retransmission_scan_time":0,
                               "last_retransmission_max_scan":0
                            }
                         }
                      }
                   }
                }
             }
          }
       }
    }
                                                
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
        self.outputs['show ip ospf interface OSPF_SL0'] = raw2
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

    golden_parsed_output2 = \
    {
       "vrf":{
          "default":{
             "address_family":{
                "ipv4":{
                   "areas":{
                      "0.0.0.1":{
                         "virtual_links":{
                            "0.0.0.1 10.36.3.3":{
                               "transit_area_id":"0.0.0.1",
                               "demand_circuit":True,
                               "interface":"GigabitEthernet0/1",
                               "name":"VL0",
                               "router_id":"10.36.3.3",
                               "dcbitless_lsa_count":7,
                               "donotage_lsa":"not allowed",
                               "link_state":"up",
                               "topology":{
                                  0:{
                                     "cost":1,
                                     "name":"Base",
                                     "disabled":False,
                                     "shutdown":False
                                  }
                               },
                               "transmit_delay":1,
                               "state":"point-to-point,",
                               "hello_interval":10,
                               "dead_interval":40,
                               "wait_interval":40,
                               "retransmit_interval":5,
                               "hello_timer":"00:00:08",
                               "adjacency_state":"full",
                               "index":"1/3",
                               "retrans_qlen":0,
                               "total_retransmission":0,
                               "first":"0x0(0)/0x0(0)",
                               "next":"0x0(0)/0x0(0)",
                               "last_retransmission_scan_length":0,
                               "last_retransmission_max_length":0,
                               "last_retransmission_scan_time":0,
                               "last_retransmission_max_scan":0
                            }
                         }
                      }
                   }
                }
             }
          }
       }
    }

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
        self.outputs['show ip ospf interface OSPF_VL0'] = raw2
        self.outputs['show running-config | section router ospf 2'] = raw3

        self.device.execute = Mock()
        self.device.execute.side_effect = mapper
        
        obj = ShowIpOspfVirtualLinks(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output1)

    def test_show_ip_ospf_virtual_links_empty(self):
        self.maxDiff = None
        self.device = Mock(**self.empty_output)
        obj = ShowIpOspfVirtualLinks(device=self.device)
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

class test_show_ip_ospf_neighbor_detail_2(unittest.TestCase):


    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_output1 = \
        """
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
        """
    golden_parsed_output1 = \
    {
        "address-family":{
            "ipv4":{
               "areas":{
                  "0.0.0.8":{
                     "interfaces":{
                        "GigabitEthernet0/1/2":{
                           "neighbors":{
                              "10.16.2.2":{
                                 "neighbor_router_id":"10.16.2.2",
                                 "interface":"GigabitEthernet0/1/2",
                                 "address":"192.168.154.2",
                                 "interface_id":"24",
                                 "priority":0,
                                 "state":"full",
                                 "statistics":{
                                    "nbr_event_count":6,
                                    "nbr_retrans_qlen":0,
                                    "total_retransmission":0,
                                    "last_retrans_scan_length":0,
                                    "last_retrans_max_scan_length":0,
                                    "last_retrans_scan_time_msec":0,
                                    "last_retrans_max_scan_time_msec":0
                                 },
                                 "dr_ip_addr":"0.0.0.0",
                                 "bdr_ip_addr":"0.0.0.0",
                                 "sr_adj_label":"16",
                                 "dead_timer":"00:00:38",
                                 "uptime":"3d16h",
                                 "index":"1/3/3,",
                                 "first":"0x0(0)/0x0(0)/0x0(0)",
                                 "next":"0x0(0)/0x0(0)/0x0(0)"
                              }
                           }
                        },
                        "GigabitEthernet0/1/1":{
                           "neighbors":{
                              "10.16.2.2":{
                                 "neighbor_router_id":"10.16.2.2",
                                 "interface":"GigabitEthernet0/1/1",
                                 "address":"192.168.4.2",
                                 "interface_id":"23",
                                 "priority":0,
                                 "state":"full",
                                 "statistics":{
                                    "nbr_event_count":6,
                                    "nbr_retrans_qlen":0,
                                    "total_retransmission":2,
                                    "last_retrans_scan_length":1,
                                    "last_retrans_max_scan_length":1,
                                    "last_retrans_scan_time_msec":0,
                                    "last_retrans_max_scan_time_msec":0
                                 },
                                 "dr_ip_addr":"0.0.0.0",
                                 "bdr_ip_addr":"0.0.0.0",
                                 "sr_adj_label":"17",
                                 "dead_timer":"00:00:35",
                                 "uptime":"1w0d",
                                 "index":"1/4/4,",
                                 "first":"0x0(0)/0x0(0)/0x0(0)",
                                 "next":"0x0(0)/0x0(0)/0x0(0)"
                                }
                                }
                            }
                        }
                    }
                }
            }
        }
    }    

    golden_output2 = '''\
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
    #     '''
    golden_parsed_output2 = \
        {
           "address-family":{
              "ipv4":{
                 "areas":{
                    "0.0.0.0":{
                       "virtual_links":{
                          "OSPF_VL1":{
                             "neighbors":{
                                "10.36.3.3":{
                                   "neighbor_router_id":"10.36.3.3",
                                   "interface":"OSPF_VL1",
                                   "address":"10.229.3.3",
                                   "priority":0,
                                   "state":"full",
                                   "statistics":{
                                      "nbr_event_count":12,
                                      "nbr_retrans_qlen":0,
                                      "total_retransmission":3,
                                      "last_retrans_scan_length":1,
                                      "last_retrans_max_scan_length":1,
                                      "last_retrans_scan_time_msec":0,
                                      "last_retrans_max_scan_time_msec":0
                                   },
                                   "dr_ip_addr":"0.0.0.0",
                                   "bdr_ip_addr":"0.0.0.0",
                                   "hello_options":"0x2",
                                   "dbd_options":"0x42",
                                   "dead_timer":"00:00:41",
                                   "uptime":"05:07:21",
                                   "index":"1/3,",
                                   "first":"0x0(0)/0x0(0)",
                                   "next":"0x0(0)/0x0(0)"
                                }
                             }
                          }
                       }
                    },
                    "0.0.0.1":{
                       "interfaces":{
                          "GigabitEthernet0/1":{
                             "neighbors":{
                                "10.36.3.3":{
                                   "neighbor_router_id":"10.36.3.3",
                                   "interface":"GigabitEthernet0/1",
                                   "address":"10.19.4.3",
                                   "priority":1,
                                   "state":"full",
                                   "statistics":{
                                      "nbr_event_count":6,
                                      "nbr_retrans_qlen":0,
                                      "total_retransmission":2,
                                      "last_retrans_scan_length":1,
                                      "last_retrans_max_scan_length":1,
                                      "last_retrans_scan_time_msec":0,
                                      "last_retrans_max_scan_time_msec":0
                                   },
                                   "dr_ip_addr":"10.19.4.4",
                                   "bdr_ip_addr":"10.19.4.3",
                                   "hello_options":"0x2",
                                   "dbd_options":"0x42",
                                   "dead_timer":"00:00:33",
                                   "uptime":"16:31:06",
                                   "index":"2/2,",
                                   "first":"0x0(0)/0x0(0)",
                                   "next":"0x0(0)/0x0(0)"
                                }
                             }
                          },
                          "GigabitEthernet0/0":{
                             "neighbors":{
                                "10.16.2.2":{
                                   "neighbor_router_id":"10.16.2.2",
                                   "interface":"GigabitEthernet0/0",
                                   "address":"10.229.4.2",
                                   "priority":1,
                                   "state":"full",
                                   "statistics":{
                                      "nbr_event_count":6,
                                      "nbr_retrans_qlen":0,
                                      "total_retransmission":1,
                                      "last_retrans_scan_length":1,
                                      "last_retrans_max_scan_length":1,
                                      "last_retrans_scan_time_msec":0,
                                      "last_retrans_max_scan_time_msec":0
                                   },
                                   "dr_ip_addr":"10.229.4.4",
                                   "bdr_ip_addr":"10.229.4.2",
                                   "dead_timer":"00:00:34",
                                   "uptime":"05:07:40",
                                   "index":"1/1,",
                                   "first":"0x0(0)/0x0(0)",
                                   "next":"0x0(0)/0x0(0)"
                                }
                             }
                          }
                       }
                    }
                 }
              }
           }
        }
    
    golden_output3 = '''
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

    golden_parsed_output3 = {
        "address-family":{
           "ipv4":{
              "areas":{
                 "0.0.0.0":{
                    "interfaces":{
                       "GigabitEthernet2":{
                          "neighbors":{
                             "10.16.2.2":{
                                "neighbor_router_id":"10.16.2.2",
                                "interface":"GigabitEthernet2",
                                "address":"10.1.2.2",
                                "interface_id":"unknown",
                                "priority":1,
                                "state":"full",
                                "statistics":{
                                   "nbr_event_count":6,
                                   "nbr_retrans_qlen":0,
                                   "total_retransmission":0,
                                   "last_retrans_scan_length":0,
                                   "last_retrans_max_scan_length":0,
                                   "last_retrans_scan_time_msec":0,
                                   "last_retrans_max_scan_time_msec":0
                                },
                                "dr_ip_addr":"10.1.2.1",
                                "bdr_ip_addr":"10.1.2.2",
                                "hello_options":"0x2",
                                "dbd_options":"0x42",
                                "dead_timer":"00:00:33",
                                "uptime":"08:04:20",
                                "index":"1/2/2,",
                                "first":"0x0(0)/0x0(0)/0x0(0)",
                                "next":"0x0(0)/0x0(0)/0x0(0)"
                             }
                          }
                       },
                       "GigabitEthernet1":{
                          "neighbors":{
                             "10.64.4.4":{
                                "neighbor_router_id":"10.64.4.4",
                                "interface":"GigabitEthernet1",
                                "address":"10.1.4.4",
                                "priority":1,
                                "state":"full",
                                "statistics":{
                                   "nbr_event_count":6,
                                   "nbr_retrans_qlen":0,
                                   "total_retransmission":1,
                                   "last_retrans_scan_length":0,
                                   "last_retrans_max_scan_length":1,
                                   "last_retrans_scan_time_msec":0,
                                   "last_retrans_max_scan_time_msec":0
                                },
                                "dr_ip_addr":"10.1.4.4",
                                "bdr_ip_addr":"10.1.4.1",
                                "dead_timer":"00:00:35",
                                "uptime":"1d01h",
                                "index":"1/1/1,",
                                "first":"0x0(0)/0x0(0)/0x0(0)",
                                "next":"0x0(0)/0x0(0)/0x0(0)"
                             }
                          }
                       }
                    }
                 },
                 "0.0.0.1":{
                    "sham_links":{
                       "OSPF_SL1":{
                          "neighbors":{
                             "10.151.22.22":{
                                "neighbor_router_id":"10.151.22.22",
                                "interface":"OSPF_SL1",
                                "address":"10.151.22.22",
                                "priority":0,
                                "state":"full",
                                "statistics":{
                                   "nbr_event_count":6,
                                   "nbr_retrans_qlen":0,
                                   "total_retransmission":2,
                                   "last_retrans_scan_length":1,
                                   "last_retrans_max_scan_length":1,
                                   "last_retrans_scan_time_msec":0,
                                   "last_retrans_max_scan_time_msec":0
                                },
                                "dr_ip_addr":"0.0.0.0",
                                "bdr_ip_addr":"0.0.0.0",
                                "hello_options":"0x2",
                                "dbd_options":"0x42",
                                "dead_timer":"00:00:35",
                                "uptime":"07:41:59",
                                "index":"1/2/2,",
                                "first":"0x0(0)/0x0(0)/0x0(0)",
                                "next":"0x0(0)/0x0(0)/0x0(0)"
                             }
                          }
                       }
                    },
                    "interfaces":{
                       "GigabitEthernet3":{
                          "neighbors":{
                             "10.115.55.55":{
                                "neighbor_router_id":"10.115.55.55",
                                "interface":"GigabitEthernet3",
                                "address":"10.186.5.5",
                                "priority":1,
                                "state":"full",
                                "statistics":{
                                   "nbr_event_count":6,
                                   "nbr_retrans_qlen":0,
                                   "total_retransmission":6,
                                   "last_retrans_scan_length":1,
                                   "last_retrans_max_scan_length":6,
                                   "last_retrans_scan_time_msec":0,
                                   "last_retrans_max_scan_time_msec":0
                                },
                                "dr_ip_addr":"10.186.5.1",
                                "bdr_ip_addr":"10.186.5.5",
                                "dead_timer":"00:00:34",
                                "uptime":"15:47:14",
                                "index":"1/1/1,",
                                "first":"0x0(0)/0x0(0)/0x0(0)",
                                "next":"0x0(0)/0x0(0)/0x0(0)"
                             }
                          }
                       }
                    }
                 }
              }
           }
        }
    }       

    def test_show_ip_ospf_neighbor_detail_2_empty_output(self):
        self.maxDiff = None
        self.device = Mock(**self.empty_output)
        obj = ShowIpOspfNeighborDetail2(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse(output='')

    def test_show_ip_ospf_neighbor_detail_2_golden_1_output(self):

        self.maxDiff = None
        obj = ShowIpOspfNeighborDetail2(device=self.device)
        parsed_output = obj.parse(output=self.golden_output1)
        self.assertEqual(parsed_output, self.golden_parsed_output1)

    def test_show_ip_ospf_neighbor_detail_2_golden_2_output(self):

        self.maxDiff = None
        obj = ShowIpOspfNeighborDetail2(device=self.device)
        parsed_output = obj.parse(output=self.golden_output2)
        self.assertEqual(parsed_output, self.golden_parsed_output2)

    def test_show_ip_ospf_neighbor_detail_2_golden_3_output(self):

        self.maxDiff = None
        obj = ShowIpOspfNeighborDetail2(device=self.device)
        parsed_output = obj.parse(output=self.golden_output3)
        self.assertEqual(parsed_output, self.golden_parsed_output3)

if __name__ == '__main__':
    unittest.main()