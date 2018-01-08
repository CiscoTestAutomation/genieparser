
# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from metaparser.util.exceptions import SchemaEmptyParserError, SchemaMissingKeyError

# iosxr show_ospf
from parser.iosxr.show_ospf_new import ShowOspfVrfAllInclusiveInterface,\
                                       ShowOspfVrfAllInclusiveNeighborDetail,\
                                       ShowOspfVrfAllInclusive,\
                                       ShowOspfVrfAllInclusiveShamLinks,\
                                       ShowOspfVrfAllInclusiveVirtualLinks,\
                                       ShowOspfMplsTrafficEngLinks,\
                                       ShowOspfVrfAllInclusiveDatabaseRouter,\
                                       ShowOspfVrfAllInclusiveDatabaseExternal,\
                                       ShowOspfVrfAllInclusiveDatabaseNetwork,\
                                       ShowOspfVrfAllInclusiveDatabaseSummary,\
                                       ShowOspfVrfAllInclusiveDatabaseOpaqueArea


# ======================================================
#  Unit test for 'show ospf vrf all-inclusive interface'
# ======================================================
class test_show_ospf_vrf_all_inclusive_interface(unittest.TestCase):

    '''Unit test for "show ospf vrf all-inclusive interface" '''

    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output1 = {
        'vrf': 
            {'VRF1': 
                {'address_family': 
                    {'ipv4': 
                        {'instance': 
                            {'1': 
                                {'areas': 
                                    {'0.0.0.1': 
                                        {'interfaces': 
                                            {'GigabitEthernet0/0/0/1': 
                                                {'adj_nbr': '77.77.77.77',
                                                'adj_nbr_count': 1,
                                                'bfd': 
                                                    {'enable': True,
                                                    'interval': 12345,
                                                    'mode': 'Default',
                                                    'multiplier': 50},
                                                'cost': 1,
                                                'dead_interval': 40,
                                                'demand_circuit': False,
                                                'dr_ip_addr': '20.3.7.7',
                                                'dr_router_id': '77.77.77.77',
                                                'enable': True,
                                                'flood_queue_length': 0,
                                                'hello_due_in': '00:00:03:040',
                                                'hello_interval': 10,
                                                'index': '1/1',
                                                'interface_type': 'broadcast',
                                                'ip_address': '20.3.7.3/24',
                                                'last_flood_scan_length': 1,
                                                'last_flood_scan_time_msec': 0,
                                                'line_protocol': True,
                                                'ls_ack_list': 'current',
                                                'ls_ack_list_length': 0,
                                                'high_water_mark': 11,
                                                'max_flood_scan_length': 5,
                                                'max_flood_scan_time_msec': 0,
                                                'max_pkt_sz': 1500,
                                                'mtu': 1500,
                                                'multi_area_intf_count': 0,
                                                'name': 'GigabitEthernet0/0/0/1',
                                                'nbr_count': 1,
                                                'next': '0(0)/0(0)',
                                                'num_nbrs_suppress_hello': 0,
                                                'passive': False,
                                                'priority': 1,
                                                'process_id': '1',
                                                'retransmit_interval': 5,
                                                'router_id': '3.3.3.3',
                                                'state': 'bdr',
                                                'transmit_delay': 1,
                                                'wait_interval': 40}},
                                        'sham_links': 
                                            {'1 3.3.3.3': 
                                                {'adj_nbr_count': 0,
                                                'bfd': 
                                                    {'enable': False},
                                                'cost': 111,
                                                'dead_interval': 13,
                                                'demand_circuit': True,
                                                'enable': False,
                                                'flood_queue_length': 0,
                                                'hello_due_in': '00:00:00:864',
                                                'hello_interval': 3,
                                                'high_water_mark': 9,
                                                'index': '2/2',
                                                'interface_type': 'sham-link',
                                                'ip_address': '0.0.0.0/0',
                                                'last_flood_scan_length': 1,
                                                'last_flood_scan_time_msec': 0,
                                                'line_protocol': True,
                                                'ls_ack_list': 'current',
                                                'ls_ack_list_length': 0,
                                                'max_flood_scan_length': 7,
                                                'max_flood_scan_time_msec': 0,
                                                'max_pkt_sz': 1500,
                                                'mtu': 0,
                                                'multi_area_intf_count': 0,
                                                'name': 'SL0',
                                                'nbr_count': 0,
                                                'next': '0(0)/0(0)',
                                                'num_nbrs_suppress_hello': 0,
                                                'passive': False,
                                                'process_id': '1',
                                                'retransmit_interval': 5,
                                                'router_id': '3.3.3.3',
                                                'state': 'point-to-point',
                                                'transmit_delay': 7,
                                                'wait_interval': 13}}}}}}}}},
            'default': 
                {'address_family': 
                    {'ipv4': 
                        {'instance': 
                            {'1': 
                                {'areas': 
                                    {'0.0.0.0': 
                                        {'interfaces': 
                                            {'GigabitEthernet0/0/0/0': 
                                                {'adj_nbr': '4.4.4.4',
                                                'adj_nbr_count': 1,
                                                'bfd': 
                                                    {'enable': False},
                                                'cost': 1,
                                                'dead_interval': 40,
                                                'demand_circuit': False,
                                                'dr_ip_addr': '10.3.4.4',
                                                'dr_router_id': '4.4.4.4',
                                                'enable': True,
                                                'flood_queue_length': 0,
                                                'hello_due_in': '00:00:07:171',
                                                'hello_interval': 10,
                                                'index': '1/1',
                                                'interface_type': 'broadcast',
                                                'ip_address': '10.3.4.3/24',
                                                'last_flood_scan_length': 1,
                                                'last_flood_scan_time_msec': 0,
                                                'line_protocol': True,
                                                'ls_ack_list': 'current',
                                                'ls_ack_list_length': 0,
                                                'high_water_mark': 5,
                                                'max_flood_scan_length': 3,
                                                'max_flood_scan_time_msec': 0,
                                                'max_pkt_sz': 1500,
                                                'mtu': 1500,
                                                'multi_area_intf_count': 0,
                                                'name': 'GigabitEthernet0/0/0/0',
                                                'nbr_count': 1,
                                                'next': '0(0)/0(0)',
                                                'num_nbrs_suppress_hello': 0,
                                                'passive': False,
                                                'priority': 1,
                                                'process_id': '1',
                                                'retransmit_interval': 5,
                                                'router_id': '3.3.3.3',
                                                'state': 'bdr',
                                                'transmit_delay': 1,
                                                'wait_interval': 40},
                                            'GigabitEthernet0/0/0/2': 
                                                {'adj_nbr': '2.2.2.2',
                                                'adj_nbr_count': 1,
                                                'bfd': 
                                                    {'enable': False},
                                                'cost': 1,
                                                'dead_interval': 40,
                                                'demand_circuit': False,
                                                'dr_ip_addr': '10.2.3.3',
                                                'dr_router_id': '3.3.3.3',
                                                'enable': True,
                                                'flood_queue_length': 0,
                                                'hello_due_in': '00:00:07:587',
                                                'hello_interval': 10,
                                                'index': '2/2',
                                                'interface_type': 'broadcast',
                                                'ip_address': '10.2.3.3/24',
                                                'last_flood_scan_length': 1,
                                                'last_flood_scan_time_msec': 0,
                                                'line_protocol': True,
                                                'ls_ack_list': 'current',
                                                'ls_ack_list_length': 0,
                                                'high_water_mark': 7,
                                                'max_flood_scan_length': 3,
                                                'max_flood_scan_time_msec': 0,
                                                'max_pkt_sz': 1500,
                                                'mtu': 1500,
                                                'multi_area_intf_count': 0,
                                                'name': 'GigabitEthernet0/0/0/2',
                                                'nbr_count': 1,
                                                'next': '0(0)/0(0)',
                                                'num_nbrs_suppress_hello': 0,
                                                'passive': False,
                                                'priority': 1,
                                                'process_id': '1',
                                                'retransmit_interval': 5,
                                                'router_id': '3.3.3.3',
                                                'state': 'dr',
                                                'transmit_delay': 1,
                                                'wait_interval': 40},
                                            'Loopback0': 
                                                {'bfd': 
                                                    {'enable': False},
                                                'cost': 1,
                                                'demand_circuit': False,
                                                'enable': True,
                                                'interface_type': 'loopback',
                                                'ip_address': '3.3.3.3/32',
                                                'line_protocol': True,
                                                'name': 'Loopback0',
                                                'process_id': '1',
                                                'router_id': '3.3.3.3'},
                                            'tunnel-te31': 
                                                {'adj_nbr_count': 0,
                                                'bfd': 
                                                    {'enable': False},
                                                'dead_interval': 40,
                                                'demand_circuit': False,
                                                'enable': True,
                                                'flood_queue_length': 0,
                                                'hello_interval': 10,
                                                'index': '0/0',
                                                'interface_type': 'point-to-point',
                                                'ip_address': '0.0.0.0/0',
                                                'last_flood_scan_length': 0,
                                                'last_flood_scan_time_msec': 0,
                                                'line_protocol': True,
                                                'ls_ack_list': 'current',
                                                'ls_ack_list_length': 0,
                                                'high_water_mark': 0,
                                                'max_flood_scan_length': 0,
                                                'max_flood_scan_time_msec': 0,
                                                'max_pkt_sz': 576,
                                                'mtu': 0,
                                                'multi_area_intf_count': 0,
                                                'name': 'tunnel-te31',
                                                'nbr_count': 0,
                                                'next': '0(0)/0(0)',
                                                'num_nbrs_suppress_hello': 0,
                                                'passive': True,
                                                'process_id': '1',
                                                'retransmit_interval': 5,
                                                'router_id': '3.3.3.3',
                                                'state': 'point-to-point',
                                                'transmit_delay': 1,
                                                'wait_interval': 0}}}}}}}}}}}

    golden_output1 = {'execute.return_value': '''
        RP/0/0/CPU0:R3_ospf_xr#show ospf vrf all-inclusive interface 
        Thu Nov  2 21:23:40.587 UTC

        Interfaces for OSPF 1

        Loopback0 is up, line protocol is up 
          Internet Address 3.3.3.3/32, Area 0
          Process ID 1, Router ID 3.3.3.3, Network Type LOOPBACK, Cost: 1
          Loopback interface is treated as a stub Host
        GigabitEthernet0/0/0/0 is up, line protocol is up 
          Internet Address 10.3.4.3/24, Area 0
          Process ID 1, Router ID 3.3.3.3, Network Type BROADCAST, Cost: 1
          Transmit Delay is 1 sec, State BDR, Priority 1, MTU 1500, MaxPktSz 1500
          Designated Router (ID) 4.4.4.4, Interface address 10.3.4.4
          Backup Designated router (ID) 3.3.3.3, Interface address 10.3.4.3
          Timer intervals configured, Hello 10, Dead 40, Wait 40, Retransmit 5
            Hello due in 00:00:07:171
          Index 1/1, flood queue length 0
          Next 0(0)/0(0)
          Last flood scan length is 1, maximum is 3
          Last flood scan time is 0 msec, maximum is 0 msec
          LS Ack List: current length 0, high water mark 5
          Neighbor Count is 1, Adjacent neighbor count is 1
            Adjacent with neighbor 4.4.4.4  (Designated Router)
          Suppress hello for 0 neighbor(s)
          Multi-area interface Count is 0
        GigabitEthernet0/0/0/2 is up, line protocol is up 
          Internet Address 10.2.3.3/24, Area 0
          Process ID 1, Router ID 3.3.3.3, Network Type BROADCAST, Cost: 1
          Transmit Delay is 1 sec, State DR, Priority 1, MTU 1500, MaxPktSz 1500
          Designated Router (ID) 3.3.3.3, Interface address 10.2.3.3
          Backup Designated router (ID) 2.2.2.2, Interface address 10.2.3.2
          Timer intervals configured, Hello 10, Dead 40, Wait 40, Retransmit 5
            Hello due in 00:00:07:587
          Index 2/2, flood queue length 0
          Next 0(0)/0(0)
          Last flood scan length is 1, maximum is 3
          Last flood scan time is 0 msec, maximum is 0 msec
          LS Ack List: current length 0, high water mark 7
          Neighbor Count is 1, Adjacent neighbor count is 1
            Adjacent with neighbor 2.2.2.2  (Backup Designated Router)
          Suppress hello for 0 neighbor(s)
          Multi-area interface Count is 0
        tunnel-te31 is up, line protocol is up 
          Internet Address 0.0.0.0/0, Area 0
          Process ID 1, Router ID 3.3.3.3, Network Type POINT_TO_POINT
          Interface is a tunnel igp-shortcut
          Transmit Delay is 1 sec, State POINT_TO_POINT, MTU 0, MaxPktSz 576
          Timer intervals configured, Hello 10, Dead 40, Wait 0, Retransmit 5
            No Hellos (Passive interface) 
          Index 0/0, flood queue length 0
          Next 0(0)/0(0)
          Last flood scan length is 0, maximum is 0
          Last flood scan time is 0 msec, maximum is 0 msec
          LS Ack List: current length 0, high water mark 0
          Neighbor Count is 0, Adjacent neighbor count is 0
          Suppress hello for 0 neighbor(s)
          Multi-area interface Count is 0


        Interfaces for OSPF 1, VRF VRF1

        OSPF_SL0 is unknown, line protocol is up 
          Internet Address 0.0.0.0/0, Area 1
          Process ID 1, VRF VRF1, Router ID 3.3.3.3, Network Type SHAM_LINK, Cost: 111
          Configured as demand circuit.
          Run as demand circuit.
          DoNotAge LSA not allowed (Number of DCbitless LSA is 1).
          Transmit Delay is 7 sec, State POINT_TO_POINT, MTU 0, MaxPktSz 1500
          Timer intervals configured, Hello 3, Dead 13, Wait 13, Retransmit 5
            Hello due in 00:00:00:864
          Index 2/2, flood queue length 0
          Next 0(0)/0(0)
          Last flood scan length is 1, maximum is 7
          Last flood scan time is 0 msec, maximum is 0 msec
          LS Ack List: current length 0, high water mark 9
          Neighbor Count is 0, Adjacent neighbor count is 0
          Suppress hello for 0 neighbor(s)
          Multi-area interface Count is 0
        GigabitEthernet0/0/0/1 is up, line protocol is up 
          Internet Address 20.3.7.3/24, Area 1
          Process ID 1, VRF VRF1, Router ID 3.3.3.3, Network Type BROADCAST, Cost: 1
          BFD enabled, BFD interval 12345 msec, BFD multiplier 50, Mode: Default
          Transmit Delay is 1 sec, State BDR, Priority 1, MTU 1500, MaxPktSz 1500
          Designated Router (ID) 77.77.77.77, Interface address 20.3.7.7
          Backup Designated router (ID) 3.3.3.3, Interface address 20.3.7.3
          Timer intervals configured, Hello 10, Dead 40, Wait 40, Retransmit 5
            Hello due in 00:00:03:040
          Index 1/1, flood queue length 0
          Next 0(0)/0(0)
          Last flood scan length is 1, maximum is 5
          Last flood scan time is 0 msec, maximum is 0 msec
          LS Ack List: current length 0, high water mark 11
          Neighbor Count is 1, Adjacent neighbor count is 1
            Adjacent with neighbor 77.77.77.77  (Designated Router)
          Suppress hello for 0 neighbor(s)
          Multi-area interface Count is 0
        '''}

    golden_parsed_output2 = {
        'vrf': 
            {'default': 
                {'address_family': 
                    {'ipv4': 
                        {'instance': 
                            {'1': 
                                {'areas': 
                                    {'0.0.0.0': 
                                        {'interfaces': 
                                            {'GigabitEthernet0/0/0/0': 
                                                {'adj_nbr_count': 0,
                                                'bfd': 
                                                    {'enable': False},
                                                'cost': 1,
                                                'dead_interval': 40,
                                                'demand_circuit': False,
                                                'dr_ip_addr': '10.2.3.2',
                                                'dr_router_id': '2.2.2.2',
                                                'enable': True,
                                                'flood_queue_length': 0,
                                                'hello_due_in': '00:00:09:266',
                                                'hello_interval': 10,
                                                'high_water_mark': 0,
                                                'index': '2/3',
                                                'interface_type': 'broadcast',
                                                'ip_address': '10.2.3.2/24',
                                                'last_flood_scan_length': 0,
                                                'last_flood_scan_time_msec': 0,
                                                'line_protocol': True,
                                                'ls_ack_list': 'current',
                                                'ls_ack_list_length': 0,
                                                'max_flood_scan_length': 0,
                                                'max_flood_scan_time_msec': 0,
                                                'max_pkt_sz': 1500,
                                                'mtu': 1500,
                                                'multi_area_intf_count': 0,
                                                'name': 'GigabitEthernet0/0/0/0',
                                                'nbr_count': 0,
                                                'next': '0(0)/0(0)',
                                                'num_nbrs_suppress_hello': 0,
                                                'passive': False,
                                                'priority': 1,
                                                'process_id': '1',
                                                'retransmit_interval': 5,
                                                'router_id': '2.2.2.2',
                                                'state': 'dr',
                                                'transmit_delay': 1,
                                                'wait_interval': 40},
                                            'GigabitEthernet0/0/0/2': 
                                                {'adj_nbr_count': 0,
                                                'bfd': 
                                                    {'enable': False},
                                                'cost': 1,
                                                'dead_interval': 40,
                                                'demand_circuit': False,
                                                'dr_ip_addr': '10.1.2.2',
                                                'dr_router_id': '2.2.2.2',
                                                'enable': True,
                                                'flood_queue_length': 0,
                                                'hello_due_in': '00:00:08:733',
                                                'hello_interval': 10,
                                                'high_water_mark': 0,
                                                'index': '3/4',
                                                'interface_type': 'broadcast',
                                                'ip_address': '10.1.2.2/24',
                                                'last_flood_scan_length': 0,
                                                'last_flood_scan_time_msec': 0,
                                                'line_protocol': True,
                                                'ls_ack_list': 'current',
                                                'ls_ack_list_length': 0,
                                                'max_flood_scan_length': 0,
                                                'max_flood_scan_time_msec': 0,
                                                'max_pkt_sz': 1500,
                                                'mtu': 1500,
                                                'multi_area_intf_count': 0,
                                                'name': 'GigabitEthernet0/0/0/2',
                                                'nbr_count': 0,
                                                'next': '0(0)/0(0)',
                                                'num_nbrs_suppress_hello': 0,
                                                'passive': False,
                                                'priority': 1,
                                                'process_id': '1',
                                                'retransmit_interval': 5,
                                                'router_id': '2.2.2.2',
                                                'state': 'dr',
                                                'transmit_delay': 1,
                                                'wait_interval': 40},
                                            'Loopback0': 
                                                {'bfd': 
                                                    {'enable': False},
                                                'cost': 1,
                                                'demand_circuit': False,
                                                'enable': True,
                                                'interface_type': 'loopback',
                                                'ip_address': '2.2.2.2/32',
                                                'line_protocol': True,
                                                'name': 'Loopback0',
                                                'process_id': '1',
                                                'router_id': '2.2.2.2'}},
                                        'virtual_links': 
                                            {'0.0.0.0 2.2.2.2': 
                                                {'adj_nbr': '4.4.4.4',
                                                'adj_nbr_count': 1,
                                                'bfd': 
                                                    {'enable': False},
                                                'cost': 1,
                                                'dead_interval': 40,
                                                'demand_circuit': True,
                                                'enable': False,
                                                'flood_queue_length': 0,
                                                'hello_due_in': '00:00:01:281',
                                                'hello_interval': 10,
                                                'high_water_mark': 20,
                                                'index': '4/7',
                                                'interface_type': 'virtual-link',
                                                'ip_address': '0.0.0.0/0',
                                                'last_flood_scan_length': 7,
                                                'last_flood_scan_time_msec': 0,
                                                'line_protocol': True,
                                                'ls_ack_list': 'current',
                                                'ls_ack_list_length': 0,
                                                'max_flood_scan_length': 7,
                                                'max_flood_scan_time_msec': 0,
                                                'max_pkt_sz': 1500,
                                                'mtu': 0,
                                                'multi_area_intf_count': 0,
                                                'name': 'VL0',
                                                'nbr_count': 1,
                                                'next': '0(0)/0(0)',
                                                'num_nbrs_suppress_hello': 1,
                                                'passive': False,
                                                'process_id': '1',
                                                'retransmit_interval': 5,
                                                'router_id': '2.2.2.2',
                                                'state': 'point-to-point',
                                                'transmit_delay': 1,
                                                'wait_interval': 40}}},
                                    '0.0.0.1': 
                                        {'interfaces': 
                                            {'GigabitEthernet0/0/0/1': 
                                                {'adj_nbr': '3.3.3.3',
                                                'adj_nbr_count': 1,
                                                'bfd': 
                                                    {'enable': False},
                                                'cost': 1,
                                                'dead_interval': 40,
                                                'demand_circuit': False,
                                                'dr_ip_addr': '20.2.3.3',
                                                'dr_router_id': '3.3.3.3',
                                                'enable': True,
                                                'flood_queue_length': 0,
                                                'hello_due_in': '00:00:00:698',
                                                'hello_interval': 10,
                                                'high_water_mark': 3,
                                                'index': '2/5',
                                                'interface_type': 'broadcast',
                                                'ip_address': '20.2.3.2/24',
                                                'last_flood_scan_length': 9,
                                                'last_flood_scan_time_msec': 0,
                                                'line_protocol': True,
                                                'ls_ack_list': 'current',
                                                'ls_ack_list_length': 0,
                                                'max_flood_scan_length': 9,
                                                'max_flood_scan_time_msec': 0,
                                                'max_pkt_sz': 1500,
                                                'mtu': 1500,
                                                'multi_area_intf_count': 0,
                                                'name': 'GigabitEthernet0/0/0/1',
                                                'nbr_count': 1,
                                                'next': '0(0)/0(0)',
                                                'num_nbrs_suppress_hello': 0,
                                                'passive': False,
                                                'priority': 1,
                                                'process_id': '1',
                                                'retransmit_interval': 5,
                                                'router_id': '2.2.2.2',
                                                'state': 'bdr',
                                                'transmit_delay': 1,
                                                'wait_interval': 40},
                                            'GigabitEthernet0/0/0/3': 
                                                {'adj_nbr': '4.4.4.4',
                                                'adj_nbr_count': 1,
                                                'bfd': 
                                                    {'enable': False},
                                                'cost': 1,
                                                'dead_interval': 40,
                                                'demand_circuit': False,
                                                'dr_ip_addr': '20.2.4.4',
                                                'dr_router_id': '4.4.4.4',
                                                'enable': True,
                                                'flood_queue_length': 0,
                                                'hello_due_in': '00:00:00:840',
                                                'hello_interval': 10,
                                                'high_water_mark': 21,
                                                'index': '3/6',
                                                'interface_type': 'broadcast',
                                                'ip_address': '20.2.4.2/24',
                                                'last_flood_scan_length': 9,
                                                'last_flood_scan_time_msec': 0,
                                                'line_protocol': True,
                                                'ls_ack_list': 'current',
                                                'ls_ack_list_length': 0,
                                                'max_flood_scan_length': 9,
                                                'max_flood_scan_time_msec': 0,
                                                'max_pkt_sz': 1500,
                                                'mtu': 1500,
                                                'multi_area_intf_count': 0,
                                                'name': 'GigabitEthernet0/0/0/3',
                                                'nbr_count': 1,
                                                'next': '0(0)/0(0)',
                                                'num_nbrs_suppress_hello': 0,
                                                'passive': False,
                                                'priority': 1,
                                                'process_id': '1',
                                                'retransmit_interval': 5,
                                                'router_id': '2.2.2.2',
                                                'state': 'bdr',
                                                'transmit_delay': 1,
                                                'wait_interval': 40},
                                            'Loopback1': 
                                                {'bfd': 
                                                    {'enable': False},
                                                    'cost': 1,
                                                    'demand_circuit': False,
                                                    'enable': True,
                                                    'interface_type': 'loopback',
                                                    'ip_address': '22.22.22.22/32',
                                                    'line_protocol': True,
                                                    'name': 'Loopback1',
                                                    'process_id': '1',
                                                    'router_id': '2.2.2.2'}}}}}}}}}}}

    golden_output2 = {'execute.return_value': '''
        RP/0/0/CPU0:R2_ospf_xr#show ospf vrf all-inclusive interface
        Tue Dec 12 20:23:16.958 UTC

        Interfaces for OSPF 1

        Loopback0 is up, line protocol is up 
          Internet Address 2.2.2.2/32, Area 0
          Process ID 1, Router ID 2.2.2.2, Network Type LOOPBACK, Cost: 1
          Loopback interface is treated as a stub Host
        OSPF_VL0 is unknown, line protocol is up 
          Internet Address 0.0.0.0/0, Area 0
          Process ID 1, Router ID 2.2.2.2, Network Type VIRTUAL_LINK, Cost: 1
          Configured as demand circuit.
          Run as demand circuit.
          DoNotAge LSA not allowed (Number of DCbitless LSA is 7).
          Transmit Delay is 1 sec, State POINT_TO_POINT, MTU 0, MaxPktSz 1500
          Timer intervals configured, Hello 10, Dead 40, Wait 40, Retransmit 5
            Hello due in 00:00:01:281
          Index 4/7, flood queue length 0
          Next 0(0)/0(0)
          Last flood scan length is 7, maximum is 7
          Last flood scan time is 0 msec, maximum is 0 msec
          LS Ack List: current length 0, high water mark 20
          Neighbor Count is 1, Adjacent neighbor count is 1
            Adjacent with neighbor 4.4.4.4  (Hello suppressed)
          Suppress hello for 1 neighbor(s)
          Multi-area interface Count is 0
        GigabitEthernet0/0/0/0 is up, line protocol is up 
          Internet Address 10.2.3.2/24, Area 0
          Process ID 1, Router ID 2.2.2.2, Network Type BROADCAST, Cost: 1
          Transmit Delay is 1 sec, State DR, Priority 1, MTU 1500, MaxPktSz 1500
          Designated Router (ID) 2.2.2.2, Interface address 10.2.3.2
          No backup designated router on this network
          Timer intervals configured, Hello 10, Dead 40, Wait 40, Retransmit 5
            Hello due in 00:00:09:266
          Index 2/3, flood queue length 0
          Next 0(0)/0(0)
          Last flood scan length is 0, maximum is 0
          Last flood scan time is 0 msec, maximum is 0 msec
          LS Ack List: current length 0, high water mark 0
          Neighbor Count is 0, Adjacent neighbor count is 0
          Suppress hello for 0 neighbor(s)
          Multi-area interface Count is 0
        GigabitEthernet0/0/0/2 is up, line protocol is up 
          Internet Address 10.1.2.2/24, Area 0
          Process ID 1, Router ID 2.2.2.2, Network Type BROADCAST, Cost: 1
          Transmit Delay is 1 sec, State DR, Priority 1, MTU 1500, MaxPktSz 1500
          Designated Router (ID) 2.2.2.2, Interface address 10.1.2.2
          No backup designated router on this network
          Timer intervals configured, Hello 10, Dead 40, Wait 40, Retransmit 5
            Hello due in 00:00:08:733
          Index 3/4, flood queue length 0
          Next 0(0)/0(0)
          Last flood scan length is 0, maximum is 0
          Last flood scan time is 0 msec, maximum is 0 msec
          LS Ack List: current length 0, high water mark 0
          Neighbor Count is 0, Adjacent neighbor count is 0
          Suppress hello for 0 neighbor(s)
          Multi-area interface Count is 0
        Loopback1 is up, line protocol is up 
          Internet Address 22.22.22.22/32, Area 1
          Process ID 1, Router ID 2.2.2.2, Network Type LOOPBACK, Cost: 1
          Loopback interface is treated as a stub Host
        GigabitEthernet0/0/0/1 is up, line protocol is up 
          Internet Address 20.2.3.2/24, Area 1
          Process ID 1, Router ID 2.2.2.2, Network Type BROADCAST, Cost: 1
          Transmit Delay is 1 sec, State BDR, Priority 1, MTU 1500, MaxPktSz 1500
          Designated Router (ID) 3.3.3.3, Interface address 20.2.3.3
          Backup Designated router (ID) 2.2.2.2, Interface address 20.2.3.2
          Timer intervals configured, Hello 10, Dead 40, Wait 40, Retransmit 5
            Hello due in 00:00:00:698
          Index 2/5, flood queue length 0
          Next 0(0)/0(0)
          Last flood scan length is 9, maximum is 9
          Last flood scan time is 0 msec, maximum is 0 msec
          LS Ack List: current length 0, high water mark 3
          Neighbor Count is 1, Adjacent neighbor count is 1
            Adjacent with neighbor 3.3.3.3  (Designated Router)
          Suppress hello for 0 neighbor(s)
          Multi-area interface Count is 0
        GigabitEthernet0/0/0/3 is up, line protocol is up 
          Internet Address 20.2.4.2/24, Area 1
          Process ID 1, Router ID 2.2.2.2, Network Type BROADCAST, Cost: 1
          Transmit Delay is 1 sec, State BDR, Priority 1, MTU 1500, MaxPktSz 1500
          Designated Router (ID) 4.4.4.4, Interface address 20.2.4.4
          Backup Designated router (ID) 2.2.2.2, Interface address 20.2.4.2
          Timer intervals configured, Hello 10, Dead 40, Wait 40, Retransmit 5
            Hello due in 00:00:00:840
          Index 3/6, flood queue length 0
          Next 0(0)/0(0)
          Last flood scan length is 9, maximum is 9
          Last flood scan time is 0 msec, maximum is 0 msec
          LS Ack List: current length 0, high water mark 21
          Neighbor Count is 1, Adjacent neighbor count is 1
            Adjacent with neighbor 4.4.4.4  (Designated Router)
          Suppress hello for 0 neighbor(s)
          Multi-area interface Count is 0
        '''}

    def test_show_ospf_vrf_all_inclusive_interface_full1(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output1)
        obj = ShowOspfVrfAllInclusiveInterface(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output1)

    def test_show_ospf_vrf_all_inclusive_interface_full2(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output2)
        obj = ShowOspfVrfAllInclusiveInterface(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output2)

    def test_show_ospf_vrf_all_inclusive_interface_empty(self):
        self.maxDiff = None
        self.device = Mock(**self.empty_output)
        obj = ShowOspfVrfAllInclusiveInterface(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()


# ============================================================
#  Unit test for 'show ospf vrf all-inclusive neighbor detail'
# ============================================================
class test_show_ospf_vrf_all_inclusive_neighbor_detail(unittest.TestCase):

    '''Unit test for "show ospf vrf all-inclusive neighbor detail" '''

    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output1 = {
        'vrf': 
            {'VRF1': 
                {'address_family': 
                    {'ipv4': 
                        {'instance': 
                            {'1': 
                                {'areas': 
                                    {'0.0.0.1': 
                                        {'interfaces': 
                                            {'GigabitEthernet0/0/0/1': 
                                                {'neighbors': 
                                                    {'77.77.77.77': 
                                                        {'address': '20.3.7.7',
                                                        'bdr_ip_addr': '20.3.7.3',
                                                        'dbd_retrans': 0,
                                                        'dead_timer': '00:00:32',
                                                        'dr_ip_addr': '20.3.7.7',
                                                        'first': '0(0)/0(0)',
                                                        'high_water_mark': 0,
                                                        'index': '1/1,',
                                                        'last_retrans_max_scan_length': 3,
                                                        'last_retrans_max_scan_time_msec': 0,
                                                        'last_retrans_scan_length': 3,
                                                        'last_retrans_scan_time_msec': 0,
                                                        'lls_options': '0x1 (LR)',
                                                        'ls_ack_list': 'NSR-sync',
                                                        'ls_ack_list_pending': 0,
                                                        'neighbor_router_id': '77.77.77.77',
                                                        'neighbor_uptime': '23:24:56',
                                                        'next': '0(0)/0(0)',
                                                        'num_retransmission': 15,
                                                        'num_state_changes': 6,
                                                        'options': '0x52',
                                                        'priority': 1,
                                                        'retransmission_queue_length': 0,
                                                        'state': 'full'}}}}}},
                                'total_neighbor_count': 1}}}}},
            'default': 
                {'address_family': 
                    {'ipv4': 
                        {'instance': 
                            {'1': 
                                {'areas': 
                                    {'0.0.0.0': 
                                        {'interfaces': 
                                            {'GigabitEthernet0/0/0/0': 
                                                {'neighbors': 
                                                    {'4.4.4.4': 
                                                        {'address': '10.3.4.4',
                                                        'bdr_ip_addr': '10.3.4.3',
                                                        'dbd_retrans': 0,
                                                        'dead_timer': '00:00:30',
                                                        'dr_ip_addr': '10.3.4.4',
                                                        'first': '0(0)/0(0)',
                                                        'high_water_mark': 0,
                                                        'index': '2/2,',
                                                        'last_retrans_max_scan_length': 0,
                                                        'last_retrans_max_scan_time_msec': 0,
                                                        'last_retrans_scan_length': 0,
                                                        'last_retrans_scan_time_msec': 0,
                                                        'lls_options': '0x1 (LR)',
                                                        'ls_ack_list': 'NSR-sync',
                                                        'ls_ack_list_pending': 0,
                                                        'neighbor_router_id': '4.4.4.4',
                                                        'neighbor_uptime': '1d01h',
                                                        'next': '0(0)/0(0)',
                                                        'num_retransmission': 0,
                                                        'num_state_changes': 6,
                                                        'options': '0x52',
                                                        'priority': 1,
                                                        'retransmission_queue_length': 0,
                                                        'state': 'full'}}},
                                            'GigabitEthernet0/0/0/2': 
                                                {'neighbors': 
                                                    {'2.2.2.2': 
                                                        {'address': '10.2.3.2',
                                                        'bdr_ip_addr': '10.2.3.2',
                                                        'dbd_retrans': 0,
                                                        'dead_timer': '00:00:38',
                                                        'dr_ip_addr': '10.2.3.3',
                                                        'first': '0(0)/0(0)',
                                                        'high_water_mark': 0,
                                                        'index': '1/1,',
                                                        'last_retrans_max_scan_length': 0,
                                                        'last_retrans_max_scan_time_msec': 0,
                                                        'last_retrans_scan_length': 0,
                                                        'last_retrans_scan_time_msec': 0,
                                                        'ls_ack_list': 'NSR-sync',
                                                        'ls_ack_list_pending': 0,
                                                        'neighbor_router_id': '2.2.2.2',
                                                        'neighbor_uptime': '08:22:07',
                                                        'next': '0(0)/0(0)',
                                                        'num_retransmission': 0,
                                                        'num_state_changes': 6,
                                                        'options': '0x42',
                                                        'priority': 1,
                                                        'retransmission_queue_length': 0,
                                                        'state': 'full'}}}}}},
                                'total_neighbor_count': 2}}}}}}}

    golden_output1 = {'execute.return_value': '''
        RP/0/0/CPU0:R3_ospf_xr#show ospf vrf all-inclusive neighbor detail 
        Thu Nov  2 21:28:53.636 UTC

        * Indicates MADJ interface
        # Indicates Neighbor awaiting BFD session up

        Neighbors for OSPF 1

         Neighbor 4.4.4.4, interface address 10.3.4.4
            In the area 0 via interface GigabitEthernet0/0/0/0 
            Neighbor priority is 1, State is FULL, 6 state changes
            DR is 10.3.4.4 BDR is 10.3.4.3
            Options is 0x52  
            LLS Options is 0x1 (LR)
            Dead timer due in 00:00:30
            Neighbor is up for 1d01h
            Number of DBD retrans during last exchange 0
            Index 2/2, retransmission queue length 0, number of retransmission 0
            First 0(0)/0(0) Next 0(0)/0(0)
            Last retransmission scan length is 0, maximum is 0
            Last retransmission scan time is 0 msec, maximum is 0 msec
            LS Ack list: NSR-sync pending 0, high water mark 0

         Neighbor 2.2.2.2, interface address 10.2.3.2
            In the area 0 via interface GigabitEthernet0/0/0/2 
            Neighbor priority is 1, State is FULL, 6 state changes
            DR is 10.2.3.3 BDR is 10.2.3.2
            Options is 0x42  
            Dead timer due in 00:00:38
            Neighbor is up for 08:22:07
            Number of DBD retrans during last exchange 0
            Index 1/1, retransmission queue length 0, number of retransmission 0
            First 0(0)/0(0) Next 0(0)/0(0)
            Last retransmission scan length is 0, maximum is 0
            Last retransmission scan time is 0 msec, maximum is 0 msec
            LS Ack list: NSR-sync pending 0, high water mark 0

        Total neighbor count: 2

        * Indicates MADJ interface
        # Indicates Neighbor awaiting BFD session up

        Neighbors for OSPF 1, VRF VRF1

         Neighbor 77.77.77.77, interface address 20.3.7.7
            In the area 1 via interface GigabitEthernet0/0/0/1 
            Neighbor priority is 1, State is FULL, 6 state changes
            DR is 20.3.7.7 BDR is 20.3.7.3
            Options is 0x52  
            LLS Options is 0x1 (LR)
            Dead timer due in 00:00:32
            Neighbor is up for 23:24:56
            Number of DBD retrans during last exchange 0
            Index 1/1, retransmission queue length 0, number of retransmission 15
            First 0(0)/0(0) Next 0(0)/0(0)
            Last retransmission scan length is 3, maximum is 3
            Last retransmission scan time is 0 msec, maximum is 0 msec
            LS Ack list: NSR-sync pending 0, high water mark 0

        Total neighbor count: 1
        '''}

    golden_parsed_output2 = {
        'vrf': 
            {'default': 
                {'address_family': 
                    {'ipv4': 
                        {'instance': 
                            {'1': 
                                {'areas': 
                                    {'0.0.0.0': 
                                        {'virtual_links': 
                                            {'0.0.0.0 20.2.4.4': 
                                                {'neighbors': 
                                                    {'4.4.4.4': 
                                                        {'address': '20.2.4.4',
                                                        'bdr_ip_addr': '0.0.0.0',
                                                        'dbd_retrans': 0,
                                                        'dr_ip_addr': '0.0.0.0',
                                                        'first': '0(0)/0(0)',
                                                        'high_water_mark': 0,
                                                        'index': '1/3,',
                                                        'last_retrans_max_scan_length': 0,
                                                        'last_retrans_max_scan_time_msec': 0,
                                                        'last_retrans_scan_length': 0,
                                                        'last_retrans_scan_time_msec': 0,
                                                        'lls_options': '0x1 (LR)',
                                                        'ls_ack_list': 'NSR-sync',
                                                        'ls_ack_list_pending': 0,
                                                        'neighbor_router_id': '4.4.4.4',
                                                        'neighbor_uptime': '04:58:24',
                                                        'next': '0(0)/0(0)',
                                                        'num_retransmission': 0,
                                                        'num_state_changes': 7,
                                                        'options': '0x72',
                                                        'priority': 1,
                                                        'retransmission_queue_length': 0,
                                                        'state': 'full'}}}}},
                                    '0.0.0.1': 
                                        {'interfaces': 
                                            {'GigabitEthernet0/0/0/1': 
                                                {'neighbors': 
                                                    {'3.3.3.3': 
                                                        {'address': '20.2.3.3',
                                                        'bdr_ip_addr': '20.2.3.2',
                                                        'dbd_retrans': 0,
                                                        'dead_timer': '00:00:31',
                                                        'dr_ip_addr': '20.2.3.3',
                                                        'first': '0(0)/0(0)',
                                                        'high_water_mark': 0,
                                                        'index': '2/2,',
                                                        'last_retrans_max_scan_length': 1,
                                                        'last_retrans_max_scan_time_msec': 0,
                                                        'last_retrans_scan_length': 1,
                                                        'last_retrans_scan_time_msec': 0,
                                                        'ls_ack_list': 'NSR-sync',
                                                        'ls_ack_list_pending': 0,
                                                        'neighbor_router_id': '3.3.3.3',
                                                        'neighbor_uptime': '05:00:13',
                                                        'next': '0(0)/0(0)',
                                                        'num_retransmission': 2,
                                                        'num_state_changes': 6,
                                                        'options': '0x42',
                                                        'priority': 1,
                                                        'retransmission_queue_length': 0,
                                                        'state': 'full'}}},
                                            'GigabitEthernet0/0/0/3': 
                                                {'neighbors': 
                                                    {'4.4.4.4': 
                                                        {'address': '20.2.4.4',
                                                        'bdr_ip_addr': '20.2.4.2',
                                                        'dbd_retrans': 0,
                                                        'dead_timer': '00:00:32',
                                                        'dr_ip_addr': '20.2.4.4',
                                                        'first': '0(0)/0(0)',
                                                        'high_water_mark': 0,
                                                        'index': '1/1,',
                                                        'last_retrans_max_scan_length': 0,
                                                        'last_retrans_max_scan_time_msec': 0,
                                                        'last_retrans_scan_length': 0,
                                                        'last_retrans_scan_time_msec': 0,
                                                        'lls_options': '0x1 (LR)',
                                                        'ls_ack_list': 'NSR-sync',
                                                        'ls_ack_list_pending': 0,
                                                        'neighbor_router_id': '4.4.4.4',
                                                        'neighbor_uptime': '05:00:21',
                                                        'next': '0(0)/0(0)',
                                                        'num_retransmission': 0,
                                                        'num_state_changes': 6,
                                                        'options': '0x52',
                                                        'priority': 1,
                                                        'retransmission_queue_length': 0,
                                                        'state': 'full'}}}}}},
                                'total_neighbor_count': 3}}}}}}}

    golden_output2 = {'execute.return_value': '''
        RP/0/0/CPU0:R2_ospf_xr#show ospf vrf all-inclusive neighbor detail (including virtual-link)
        Tue Dec 12 20:21:16.846 UTC

        * Indicates MADJ interface
        # Indicates Neighbor awaiting BFD session up

        Neighbors for OSPF 1

         Neighbor 4.4.4.4, interface address 20.2.4.4
            In the area 0 via interface OSPF_VL0 
            Neighbor priority is 1, State is FULL, 7 state changes
            DR is 0.0.0.0 BDR is 0.0.0.0
            Options is 0x72  
            LLS Options is 0x1 (LR)
            Neighbor is up for 04:58:24
            Number of DBD retrans during last exchange 0
            Index 1/3, retransmission queue length 0, number of retransmission 0
            First 0(0)/0(0) Next 0(0)/0(0)
            Last retransmission scan length is 0, maximum is 0
            Last retransmission scan time is 0 msec, maximum is 0 msec
            LS Ack list: NSR-sync pending 0, high water mark 0

         Neighbor 3.3.3.3, interface address 20.2.3.3
            In the area 1 via interface GigabitEthernet0/0/0/1 
            Neighbor priority is 1, State is FULL, 6 state changes
            DR is 20.2.3.3 BDR is 20.2.3.2
            Options is 0x42  
            Dead timer due in 00:00:31
            Neighbor is up for 05:00:13
            Number of DBD retrans during last exchange 0
            Index 2/2, retransmission queue length 0, number of retransmission 2
            First 0(0)/0(0) Next 0(0)/0(0)
            Last retransmission scan length is 1, maximum is 1
            Last retransmission scan time is 0 msec, maximum is 0 msec
            LS Ack list: NSR-sync pending 0, high water mark 0

         Neighbor 4.4.4.4, interface address 20.2.4.4
            In the area 1 via interface GigabitEthernet0/0/0/3 
            Neighbor priority is 1, State is FULL, 6 state changes
            DR is 20.2.4.4 BDR is 20.2.4.2
            Options is 0x52  
            LLS Options is 0x1 (LR)
            Dead timer due in 00:00:32
            Neighbor is up for 05:00:21
            Number of DBD retrans during last exchange 0
            Index 1/1, retransmission queue length 0, number of retransmission 0
            First 0(0)/0(0) Next 0(0)/0(0)
            Last retransmission scan length is 0, maximum is 0
            Last retransmission scan time is 0 msec, maximum is 0 msec
            LS Ack list: NSR-sync pending 0, high water mark 0

        Total neighbor count: 3
        '''}

    def test_show_ospf_vrf_all_inclusive_neighbor_full1(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output1)
        obj = ShowOspfVrfAllInclusiveNeighborDetail(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output1)

    def test_show_ospf_vrf_all_inclusive_neighbor_full2(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output2)
        obj = ShowOspfVrfAllInclusiveNeighborDetail(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output2)

    def test_show_ospf_vrf_all_inclusive_neighbor_empty(self):
        self.maxDiff = None
        self.device = Mock(**self.empty_output)
        obj = ShowOspfVrfAllInclusiveNeighborDetail(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()


# ============================================
#  Unit test for 'show ospf vrf all-inclusive'
# ============================================
class test_show_ospf_vrf_all_inclusive(unittest.TestCase):

    '''Unit test for "show ospf vrf all-inclusive" '''

    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output1 = {
        'vrf': 
            {'VRF1': 
                {'address_family': 
                    {'ipv4': 
                        {'instance': 
                            {'ospf 1': 
                                {'adjacency_stagger': 
                                    {'disable': False,
                                    'initial_number': 2,
                                    'maximum_number': 64},
                                'areas': 
                                    {'0.0.0.1': 
                                        {'area_type': 'normal',
                                        'statistics': 
                                            {'area_scope_lsa_cksum_sum': '0x04f437',
                                            'area_scope_lsa_count': 11,
                                            'area_scope_opaque_lsa_cksum_sum': '00000000',
                                            'area_scope_opaque_lsa_count': 0,
                                            'dcbitless_lsa_count': 1,
                                            'donotage_lsa_count': 0,
                                            'flood_list_length': 0,
                                            'indication_lsa_count': 0,
                                            'interfaces_count': 2,
                                            'lfa_interface_count': 0,
                                            'lfa_per_prefix_interface_count': 0,
                                            'lfa_revision': 0,
                                            'nbrs_full': 1,
                                            'nbrs_staggered_mode': 0,
                                            'spf_runs_count': 79}}},
                                'database_control': 
                                    {'max_lsa': 123},
                                'external_flood_list_length': 0,
                                'flood_pacing_interval': 33,
                                'lsd_revision': 1,
                                'lsd_state': 'connected, registered, bound',
                                'nsr': 
                                    {'enable': True},
                                'numbers': 
                                    {'configured_interfaces': 1024,
                                    'dc_bitless': 0,
                                    'do_not_age': 0,
                                    'external_lsa': 0,
                                    'external_lsa_checksum': '00000000',
                                    'nbrs_forming': 0,
                                    'nbrs_full': 1,
                                    'opaque_as_lsa': 0,
                                    'opaque_as_lsa_checksum': '00000000'},
                                'retransmission_interval': 66,
                                'role': 'primary active',
                                'router_id': '3.3.3.3',
                                'segment_routing_global_block_default': '16000-23999',
                                'snmp_trap': False,
                                'spf_control': 
                                    {'throttle': 
                                        {'lsa': 
                                            {'arrival': 100,
                                            'hold': 200,
                                            'interval': 200,
                                            'maximum': 5000,
                                            'refresh_interval': 1800,
                                            'start': 50},
                                        'spf': 
                                            {'hold': 200,
                                            'maximum': 5000,
                                            'start': 50}}},
                                'strict_spf_capability': True,
                                'stub_router': 
                                    {'always': 
                                        {'always': False,
                                        'external_lsa': False,
                                        'include_stub': False,
                                        'summary_lsa': False}}}}}}},
            'default': 
                {'address_family': 
                    {'ipv4': 
                        {'instance': 
                            {'ospf 1': 
                                {'adjacency_stagger': 
                                    {'disable': False,
                                    'initial_number': 2,
                                    'maximum_number': 64},
                                'areas': 
                                    {'0.0.0.0': 
                                        {'area_type': 'normal',
                                        'rrr_enabled': True,
                                        'statistics': 
                                            {'area_scope_lsa_cksum_sum': '0x0a2fb5',
                                            'area_scope_lsa_count': 19,
                                            'area_scope_opaque_lsa_cksum_sum': '00000000',
                                            'area_scope_opaque_lsa_count': 0,
                                            'dcbitless_lsa_count': 5,
                                            'donotage_lsa_count': 0,
                                            'flood_list_length': 0,
                                            'indication_lsa_count': 0,
                                            'interfaces_count': 3,
                                            'lfa_interface_count': 0,
                                            'lfa_per_prefix_interface_count': 0,
                                            'lfa_revision': 0,
                                            'nbrs_full': 2,
                                            'nbrs_staggered_mode': 0,
                                            'spf_runs_count': 26},
                                        'topology_version': 15}},
                                'external_flood_list_length': 0,
                                'flood_pacing_interval': 33,
                                'lsd_revision': 1,
                                'lsd_state': 'connected, registered, bound',
                                'nsr': 
                                    {'enable': True},
                                'numbers': 
                                    {'configured_interfaces': 1024,
                                    'dc_bitless': 0,
                                    'do_not_age': 0,
                                    'external_lsa': 1,
                                    'external_lsa_checksum': '0x00607f',
                                    'nbrs_forming': 0,
                                    'nbrs_full': 2,
                                    'opaque_as_lsa': 0,
                                    'opaque_as_lsa_checksum': '00000000'},
                                'retransmission_interval': 66,
                                'role': 'primary active',
                                'router_id': '3.3.3.3',
                                'segment_routing_global_block_default': '16000-23999',
                                'snmp_trap': True,
                                'spf_control': 
                                    {'throttle': 
                                        {'lsa': 
                                            {'arrival': 100,
                                            'hold': 200,
                                            'interval': 200,
                                            'maximum': 5000,
                                            'refresh_interval': 1800,
                                            'start': 50},
                                        'spf': 
                                            {'hold': 200,
                                            'maximum': 5000,
                                            'start': 50}}},
                                'strict_spf_capability': True,
                                'stub_router': 
                                    {'always': 
                                        {'always': True,
                                        'external_lsa': True,
                                        'include_stub': True,
                                        'state': 'active',
                                        'summary_lsa': True},
                                    'on_startup': 
                                        {'duration': 5,
                                        'external_lsa': True,
                                        'include_stub': True,
                                        'on_startup': True,
                                        'state': 'inactive',
                                        'summary_lsa': True},
                                    'on_switchover': 
                                        {'duration': 10,
                                        'external_lsa': True,
                                        'include_stub': True,
                                        'on_switchover': True,
                                        'state': 'inactive',
                                        'summary_lsa': True}}}}}}}}}

    golden_output1 = {'execute.return_value': '''
        RP/0/0/CPU0:R3_ospf_xr#show ospf vrf all-inclusive 
        Thu Nov  2 21:14:35.895 UTC

         Routing Process "ospf 1" with ID 3.3.3.3
         Role: Primary Active
         NSR (Non-stop routing) is Enabled
         Supports only single TOS(TOS0) routes
         Supports opaque LSA
         Originating router-LSAs with maximum metric
         Condition: on switch-over for 10 seconds, State: inactive
            Advertise stub links with maximum metric in router-LSAs
            Advertise summary-LSAs with metric 16711680
            Advertise external-LSAs with metric 16711680
         Condition: on start-up for 5 seconds, State: inactive
            Advertise stub links with maximum metric in router-LSAs
            Advertise summary-LSAs with metric 16711680
            Advertise external-LSAs with metric 16711680
         Condition: always State: active
            Advertise stub links with maximum metric in router-LSAs
            Advertise summary-LSAs with metric 16711680
            Advertise external-LSAs with metric 16711680
         Initial SPF schedule delay 50 msecs
         Minimum hold time between two consecutive SPFs 200 msecs
         Maximum wait time between two consecutive SPFs 5000 msecs
         Initial LSA throttle delay 50 msecs
         Minimum hold time for LSA throttle 200 msecs
         Maximum wait time for LSA throttle 5000 msecs
         Minimum LSA interval 200 msecs. Minimum LSA arrival 100 msecs
         LSA refresh interval 1800 seconds
         Flood pacing interval 33 msecs. Retransmission pacing interval 66 msecs
         Adjacency stagger enabled; initial (per area): 2, maximum: 64
            Number of neighbors forming: 0, 2 full
         Maximum number of configured interfaces 1024
         Number of external LSA 1. Checksum Sum 0x00607f
         Number of opaque AS LSA 0. Checksum Sum 00000000
         Number of DCbitless external and opaque AS LSA 0
         Number of DoNotAge external and opaque AS LSA 0
         Number of areas in this router is 1. 1 normal 0 stub 0 nssa
         External flood list length 0
         SNMP trap is enabled
         LSD connected, registered, bound, revision 1
         Segment Routing Global Block default (16000-23999), not allocated
         Strict-SPF capability is enabled
            Area BACKBONE(0)
                Number of interfaces in this area is 3
                Area has RRR enabled, topology version 15
                SPF algorithm executed 26 times
                Number of LSA 19.  Checksum Sum 0x0a2fb5
                Number of opaque link LSA 0.  Checksum Sum 00000000
                Number of DCbitless LSA 5
                Number of indication LSA 0
                Number of DoNotAge LSA 0
                Flood list length 0
                Number of LFA enabled interfaces 0, LFA revision 0
                Number of Per Prefix LFA enabled interfaces 0
                Number of neighbors forming in staggered mode 0, 2 full


         VRF VRF1 in Routing Process "ospf 1" with ID 3.3.3.3
         Role: Primary Active
         NSR (Non-stop routing) is Enabled
         Supports only single TOS(TOS0) routes
         Supports opaque LSA
         It is an area border and autonomous system boundary router
         Redistributing External Routes from,
            bgp 100
            Maximum number of redistributed prefixes 10240
            Threshold for warning message 75%
         Router is not originating router-LSAs with maximum metric
         Initial SPF schedule delay 50 msecs
         Minimum hold time between two consecutive SPFs 200 msecs
         Maximum wait time between two consecutive SPFs 5000 msecs
         Initial LSA throttle delay 50 msecs
         Minimum hold time for LSA throttle 200 msecs
         Maximum wait time for LSA throttle 5000 msecs
         Minimum LSA interval 200 msecs. Minimum LSA arrival 100 msecs
         LSA refresh interval 1800 seconds
         Flood pacing interval 33 msecs. Retransmission pacing interval 66 msecs
         Adjacency stagger enabled; initial (per area): 2, maximum: 64
            Number of neighbors forming: 0, 1 full
         Maximum number of configured interfaces 1024
         Maximum number of non self-generated LSA allowed 123
         Number of external LSA 0. Checksum Sum 00000000
         Number of opaque AS LSA 0. Checksum Sum 00000000
         Number of DCbitless external and opaque AS LSA 0
         Number of DoNotAge external and opaque AS LSA 0
         Number of areas in this router is 1. 1 normal 0 stub 0 nssa
         External flood list length 0
         SNMP trap is disabled
         LSD connected, registered, bound, revision 1
         Segment Routing Global Block default (16000-23999), not allocated
         Strict-SPF capability is enabled
            Area 1
                Number of interfaces in this area is 2
                SPF algorithm executed 79 times
                Number of LSA 11.  Checksum Sum 0x04f437
                Number of opaque link LSA 0.  Checksum Sum 00000000
                Number of DCbitless LSA 1
                Number of indication LSA 0
                Number of DoNotAge LSA 0
                Flood list length 0
                Number of LFA enabled interfaces 0, LFA revision 0
                Number of Per Prefix LFA enabled interfaces 0
                Number of neighbors forming in staggered mode 0, 1 full
        '''}

    def test_show_ospf_vrf_all_inclusive_full(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output1)
        obj = ShowOspfVrfAllInclusive(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output1)

    def test_show_ospf_vrf_all_inclusive_empty(self):
        self.maxDiff = None
        self.device = Mock(**self.empty_output)
        obj = ShowOspfVrfAllInclusive(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()


# =======================================================
#  Unit test for 'show ospf vrf all-inclusive sham-links'
# =======================================================
class test_show_ospf_vrf_all_inclusive_sham_links(unittest.TestCase):

    '''Unit test for "show ospf vrf all-inclusive sham-links" '''

    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output1 = {
        'vrf': 
            {'VRF1': 
                {'address_family': 
                    {'ipv4': 
                        {'instance': 
                            {'OSPF 1': 
                                {'areas': 
                                    {'0.0.0.1': 
                                        {'sham_links': 
                                            {'33.33.33.33 22.22.22.22': 
                                                {'cost': 111,
                                                'dcbitless_lsa_count': 1,
                                                'dead_interval': 13,
                                                'demand_circuit': True,
                                                'hello_interval': 3,
                                                'hello_timer': '00:00:00:772',
                                                'if_index': 2,
                                                'local_id': '33.33.33.33',
                                                'name': 'SL0',
                                                'remote_id': '22.22.22.22',
                                                'retransmit_interval': 5,
                                                'state': 'point-to-point,',
                                                'transit_area_id': '0.0.0.1',
                                                'transmit_delay': 7,
                                                'wait_interval': 13}}}}}}}}}}}

    golden_output1 = {'execute.return_value': '''
        RP/0/0/CPU0:R3_ospf_xr#show ospf vrf all-inclusive sham-links 
        Thu Nov  2 21:23:03.160 UTC


        Sham Links for OSPF 1, VRF VRF1

        Sham Link OSPF_SL0 to address 22.22.22.22 is up
        Area 1, source address 33.33.33.33
        IfIndex = 2
          Run as demand circuit
          DoNotAge LSA not allowed (Number of DCbitless LSA is 1)., Cost of using 111
          Transmit Delay is 7 sec, State POINT_TO_POINT,
          Timer intervals configured, Hello 3, Dead 13, Wait 13, Retransmit 5
            Hello due in 00:00:00:772
        '''}

    def test_show_ospf_vrf_all_inclusive_sham_links_full(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output1)
        obj = ShowOspfVrfAllInclusiveShamLinks(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output1)

    def test_show_ospf_vrf_all_inclusive_sham_links_empty(self):
        self.maxDiff = None
        self.device = Mock(**self.empty_output)
        obj = ShowOspfVrfAllInclusiveShamLinks(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()


# ==========================================================
#  Unit test for 'show ospf vrf all-inclusive virtual-links'
# ==========================================================
class test_show_ospf_vrf_all_inclusive_virtual_links(unittest.TestCase):

    '''Unit test for "show ospf vrf all-inclusive virtual-links" '''

    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output1 = {
        'vrf': 
            {'default':
                {'address_family': 
                    {'ipv4': 
                        {'instance': 
                            {'OSPF 1': 
                                {'areas': 
                                    {'0.0.0.1': 
                                        {'virtual_links': 
                                            {'0.0.0.1 4.4.4.4': 
                                                {'authentication': 
                                                    {'auth_trailer_key': 
                                                        {'crypto_algorithm': 'clear text'}},
                                                'cost': 65535,
                                                'dcbitless_lsa_count': 1,
                                                'dead_interval': 16,
                                                'demand_circuit': True,
                                                'hello_interval': 4,
                                                'hello_timer': '00:00:03:179',
                                                'name': 'VL0',
                                                'nsf': 
                                                    {'enable': True,
                                                    'last_restart': '00:18:16'},
                                                'retransmit_interval': 44,
                                                'router_id': '4.4.4.4',
                                                'state': 'point-to-point,',
                                                'transit_area_id': '0.0.0.1',
                                                'transmit_delay': 5,
                                                'wait_interval': 16}}}}}}}}}}}

    golden_output1 = {'execute.return_value': '''
        RP/0/0/CPU0:R2_ospf_xr#show ospf vrf all-inclusive virtual-links 
        Fri Nov  3 01:25:44.845 UTC

        Virtual Links for OSPF 1

        Virtual Link OSPF_VL0 to router 4.4.4.4 is up
          
          DoNotAge LSA not allowed Run as demand circuit (Number of DCbitless LSA is 1).
          Transit area 1, via interface GigabitEthernet0/0/0/3, Cost of using 65535
          Transmit Delay is 5 sec, State POINT_TO_POINT,
          Non-Stop Forwarding (NSF) enabled, last NSF restart 00:18:16 ago
          Timer intervals configured, Hello 4, Dead 16, Wait 16, Retransmit 44
            Hello due in 00:00:03:179
          Clear text authentication enabled
        '''}

    def test_show_ospf_vrf_all_inclusive_virtual_links_full(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output1)
        obj = ShowOspfVrfAllInclusiveVirtualLinks(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output1)

    def test_show_ospf_vrf_all_inclusive_virtual_links_empty(self):
        self.maxDiff = None
        self.device = Mock(**self.empty_output)
        obj = ShowOspfVrfAllInclusiveVirtualLinks(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()


# =================================================
#  Unit test for 'show ospf mpls traffic-eng links'
# =================================================
class test_show_ospf_mpls_traffic_eng_links(unittest.TestCase):

    '''Unit test for "show ospf vrf all-inclusive virtual-links" '''

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
                                        {'mpls': 
                                            {'te': 
                                                {'area_instance': 2,
                                                'enable': True,
                                                'link_fragments': 
                                                    {1: 
                                                        {'affinity_bit': 0,
                                                        'extended_admin_groups': 
                                                            {0: {'value': 0},
                                                            1: {'value': 0},
                                                            2: {'value': 0},
                                                            3: {'value': 0},
                                                            4: {'value': 0},
                                                            5: {'value': 0},
                                                            6: {'value': 0},
                                                            7: {'value': 0}},
                                                        'interface_address': '10.3.4.3',
                                                        'link_id': '10.3.4.4',
                                                        'link_instance': 2,
                                                        'maximum_bandwidth': 125000000,
                                                        'maximum_reservable_bandwidth': 93750000,
                                                        'network_type': 'broadcast',
                                                        'out_interface_id': 4,
                                                        'te_admin_metric': 1,
                                                        'total_extended_admin_group': 8,
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
                                                                'unreserved_bandwidth': 93750000}}},
                                                    2: 
                                                        {'affinity_bit': 0,
                                                        'extended_admin_groups': 
                                                            {0: {'value': 0},
                                                            1: {'value': 0},
                                                            2: {'value': 0},
                                                            3: {'value': 0},
                                                            4: {'value': 0},
                                                            5: {'value': 0},
                                                            6: {'value': 0},
                                                            7: {'value': 0}},
                                                        'interface_address': '10.2.3.3',
                                                        'link_id': '10.2.3.3',
                                                        'link_instance': 2,
                                                        'maximum_bandwidth': 125000000,
                                                        'maximum_reservable_bandwidth': 93750000,
                                                        'network_type': 'broadcast',
                                                        'out_interface_id': 6,
                                                        'te_admin_metric': 1,
                                                        'total_extended_admin_group': 8,
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
                                                'total_links': 2}}},
                                    '0.0.0.1': 
                                        {'mpls': 
                                            {'te': 
                                                {'enable': False}}}},
                                'mpls': 
                                    {'te': 
                                        {'router_id': '3.3.3.3'}}}}}}}}}

    golden_output1 = {'execute.return_value': '''
        RP/0/0/CPU0:R3_ospf_xr#show ospf mpls traffic-eng link 
        Thu Nov  2 21:15:42.880 UTC

                OSPF Router with ID (3.3.3.3) (Process ID 1)

      Area 0 has 2 MPLS TE links. Area instance is 2.
        Link is associated with fragment 1. Link instance is 2
          Link connected to Broadcast network
          Link ID : 10.3.4.4
          Interface Address : 10.3.4.3
          Admin Metric : TE: 1
          (all bandwidths in bytes/sec)
          Maximum bandwidth : 125000000
          Maximum global pool reservable bandwidth : 93750000
          Number of Priority : 8
          Global pool unreserved BW 
          Priority 0 :             93750000  Priority 1 :             93750000
          Priority 2 :             93750000  Priority 3 :             93750000
          Priority 4 :             93750000  Priority 5 :             93750000
          Priority 6 :             93750000  Priority 7 :             93750000
          Out Interface ID : 4
          Affinity Bit : 0
          Extended Admin Group : 8
           EAG[0]: 0
           EAG[1]: 0
           EAG[2]: 0
           EAG[3]: 0
           EAG[4]: 0
           EAG[5]: 0
           EAG[6]: 0
           EAG[7]: 0

        Link is associated with fragment 2. Link instance is 2
          Link connected to Broadcast network
          Link ID : 10.2.3.3
          Interface Address : 10.2.3.3
          Admin Metric : TE: 1
          (all bandwidths in bytes/sec)
          Maximum bandwidth : 125000000
          Maximum global pool reservable bandwidth : 93750000
          Number of Priority : 8
          Global pool unreserved BW 
          Priority 0 :             93750000  Priority 1 :             93750000
          Priority 2 :             93750000  Priority 3 :             93750000
          Priority 4 :             93750000  Priority 5 :             93750000
          Priority 6 :             93750000  Priority 7 :             93750000
          Out Interface ID : 6
          Affinity Bit : 0
          Extended Admin Group : 8
           EAG[0]: 0
           EAG[1]: 0
           EAG[2]: 0
           EAG[3]: 0
           EAG[4]: 0
           EAG[5]: 0
           EAG[6]: 0
           EAG[7]: 0

      Area 1 MPLS TE not initialized
        '''}

    def test_show_ospf_mpls_traffic_eng_links_full(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output1)
        obj = ShowOspfMplsTrafficEngLinks(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output1)

    def test_show_ospf_mpls_traffic_eng_links_empty(self):
        self.maxDiff = None
        self.device = Mock(**self.empty_output)
        obj = ShowOspfMplsTrafficEngLinks(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()


# ============================================================
#  Unit test for 'show ospf vrf all-inclusive database router'
# ============================================================
class test_show_ospf_vrf_all_inclusive_database_router(unittest.TestCase):

    '''Unit test for "show ospf vrf all-inclusive database router" '''

    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output1 = {
        'vrf': 
            {'VRF1': 
                {'address_family': 
                    {'ipv4': 
                        {'instance': 
                            {'1': 
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
                                                                                'num_tos_metrics': 0,
                                                                                'topologies': 
                                                                                    {0: 
                                                                                        {'metric': 1,
                                                                                        'mt_id': 0,
                                                                                        'tos': 0}},
                                                                                'type': 'transit network'},
                                                                            '22.22.22.22': 
                                                                                {'link_data': '0.0.0.14',
                                                                                'link_id': '22.22.22.22',
                                                                                'num_tos_metrics': 0,
                                                                                'topologies': 
                                                                                    {0: 
                                                                                        {'metric': 111,
                                                                                        'mt_id': 0,
                                                                                        'tos': 0}},
                                                                                'type': 'another router (point-to-point)'}},
                                                                        'num_of_links': 2}},
                                                                'header': 
                                                                    {'adv_router': '11.11.11.11',
                                                                    'age': 1713,
                                                                    'area_border_router': True,
                                                                    'as_boundary_router': True,
                                                                    'checksum': '0x9ce3',
                                                                    'length': 48,
                                                                    'lsa_id': '11.11.11.11',
                                                                    'option': 'None',
                                                                    'option_desc': 'No '
                                                                    'TOS-capability, '
                                                                    'DC',
                                                                    'routing_bit_enable': True,
                                                                    'seq_num': '8000003e',
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
                                                                                'num_tos_metrics': 0,
                                                                                'topologies': 
                                                                                    {0: 
                                                                                        {'metric': 1,
                                                                                        'mt_id': 0,
                                                                                        'tos': 0}},
                                                                                'type': 'another router (point-to-point)'},
                                                                            '20.2.6.6': 
                                                                                {'link_data': '20.2.6.2',
                                                                                'link_id': '20.2.6.6',
                                                                                'num_tos_metrics': 0,
                                                                                'topologies': 
                                                                                    {0: 
                                                                                        {'metric': 40,
                                                                                        'mt_id': 0,
                                                                                        'tos': 0}},
                                                                                'type': 'transit network'}},
                                                                        'num_of_links': 2}},
                                                            'header': 
                                                                {'adv_router': '22.22.22.22',
                                                                'age': 1539,
                                                                'area_border_router': True,
                                                                'as_boundary_router': True,
                                                                'checksum': '0xc41a',
                                                                'length': 48,
                                                                'lsa_id': '22.22.22.22',
                                                                'option': 'None',
                                                                'option_desc': 'No '
                                                                'TOS-capability, '
                                                                'No '
                                                                'DC',
                                                                'routing_bit_enable': True,
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
                                                                                'num_tos_metrics': 0,
                                                                                'topologies': 
                                                                                    {0: 
                                                                                        {'metric': 1,
                                                                                        'mt_id': 0,
                                                                                        'tos': 0}},
                                                                                'type': 'transit network'}},
                                                                        'num_of_links': 1}},
                                                                'header': 
                                                                    {'adv_router': '3.3.3.3',
                                                                    'age': 217,
                                                                    'area_border_router': True,
                                                                    'as_boundary_router': True,
                                                                    'checksum': '0x5646',
                                                                    'length': 36,
                                                                    'lsa_id': '3.3.3.3',
                                                                    'option': 'None',
                                                                    'option_desc': 'No TOS-capability, DC',
                                                                    'routing_bit_enable': True,
                                                                    'seq_num': '80000036',
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
                                                                                'num_tos_metrics': 0,
                                                                                'topologies': 
                                                                                    {0: 
                                                                                        {'metric': 1,
                                                                                        'mt_id': 0,
                                                                                        'tos': 0}},
                                                                                'type': 'transit network'},
                                                                            '20.5.6.6': 
                                                                                {'link_data': '20.5.6.5',
                                                                                'link_id': '20.5.6.6',
                                                                                'num_tos_metrics': 0,
                                                                                'topologies': 
                                                                                    {0: 
                                                                                        {'metric': 30,
                                                                                        'mt_id': 0,
                                                                                        'tos': 0}},
                                                                                'type': 'transit network'},
                                                                            '55.55.55.55': 
                                                                                {'link_data': '255.255.255.255',
                                                                                'link_id': '55.55.55.55',
                                                                                'num_tos_metrics': 0,
                                                                                'topologies': 
                                                                                    {0: 
                                                                                        {'metric': 1,
                                                                                        'mt_id': 0,
                                                                                        'tos': 0}},
                                                                                'type': 'stub network'}},
                                                                                'num_of_links': 3}},
                                                                'header': 
                                                                    {'adv_router': '55.55.55.55',
                                                                    'age': 1378,
                                                                    'checksum': '0xe7bc',
                                                                    'length': 60,
                                                                    'lsa_id': '55.55.55.55',
                                                                    'option': 'None',
                                                                    'option_desc': 'No '
                                                                    'TOS-capability, '
                                                                    'DC',
                                                                    'routing_bit_enable': True,
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
                                                                                'num_tos_metrics': 0,
                                                                                'topologies': 
                                                                                    {0: 
                                                                                        {'metric': 1,
                                                                                        'mt_id': 0,
                                                                                        'tos': 0}},
                                                                                'type': 'transit network'},
                                                                            '20.5.6.6': 
                                                                                {'link_data': '20.5.6.6',
                                                                                'link_id': '20.5.6.6',
                                                                                'num_tos_metrics': 0,
                                                                                'topologies': 
                                                                                    {0: 
                                                                                        {'metric': 30,
                                                                                        'mt_id': 0,
                                                                                        'tos': 0}},
                                                                                'type': 'transit network'},
                                                                            '20.6.7.6': 
                                                                                {'link_data': '20.6.7.6',
                                                                                'link_id': '20.6.7.6',
                                                                                'num_tos_metrics': 0,
                                                                                'topologies': 
                                                                                    {0: 
                                                                                        {'metric': 30,
                                                                                        'mt_id': 0,
                                                                                        'tos': 0}},
                                                                                'type': 'transit network'},
                                                                            '66.66.66.66': 
                                                                                {'link_data': '255.255.255.255',
                                                                                'link_id': '66.66.66.66',
                                                                                'num_tos_metrics': 0,
                                                                                'topologies': 
                                                                                    {0: 
                                                                                        {'metric': 1,
                                                                                        'mt_id': 0,
                                                                                        'tos': 0}},
                                                                                'type': 'stub '
                                                                                'network'}},
                                                                                'num_of_links': 4}},
                                                                'header': 
                                                                    {'adv_router': '66.66.66.66',
                                                                    'age': 1578,
                                                                    'checksum': '0x1282',
                                                                    'length': 72,
                                                                    'lsa_id': '66.66.66.66',
                                                                    'option': 'None',
                                                                    'option_desc': 'No TOS-capability, DC',
                                                                    'routing_bit_enable': True,
                                                                    'seq_num': '8000003c',
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
                                                                                'num_tos_metrics': 0,
                                                                                'topologies': 
                                                                                    {0: 
                                                                                        {'metric': 1,
                                                                                        'mt_id': 0,
                                                                                        'tos': 0}},
                                                                                'type': 'transit network'},
                                                                            '20.6.7.6': 
                                                                                {'link_data': '20.6.7.7',
                                                                                'link_id': '20.6.7.6',
                                                                                'num_tos_metrics': 0,
                                                                                'topologies': 
                                                                                    {0: 
                                                                                        {'metric': 30,
                                                                                        'mt_id': 0,
                                                                                        'tos': 0}},
                                                                                'type': 'transit '
                                                                                'network'},
                                                                            '77.77.77.77': 
                                                                                {'link_data': '255.255.255.255',
                                                                                'link_id': '77.77.77.77',
                                                                                'num_tos_metrics': 0,
                                                                                'topologies': 
                                                                                    {0: 
                                                                                        {'metric': 1,
                                                                                        'mt_id': 0,
                                                                                        'tos': 0}},
                                                                                'type': 'stub network'}},
                                                                    'num_of_links': 3}},
                                                                'header': 
                                                                    {'adv_router': '77.77.77.77',
                                                                    'age': 1344,
                                                                    'checksum': '0x1379',
                                                                    'length': 60,
                                                                    'lsa_id': '77.77.77.77',
                                                                    'option': 'None',
                                                                    'option_desc': 'No '
                                                                    'TOS-capability, '
                                                                    'DC',
                                                                    'routing_bit_enable': True,
                                                                    'seq_num': '80000030',
                                                                    'type': 1}}}}}}}}}}}}}},
            'default': 
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
                                                                                'num_tos_metrics': 0,
                                                                                'topologies': 
                                                                                    {0: 
                                                                                        {'metric': 1,
                                                                                        'mt_id': 0,
                                                                                        'tos': 0}},
                                                                                'type': 'stub network'},
                                                                            '10.1.2.1': 
                                                                                {'link_data': '10.1.2.1',
                                                                                'link_id': '10.1.2.1',
                                                                                'num_tos_metrics': 0,
                                                                                'topologies': 
                                                                                    {0: 
                                                                                        {'metric': 1,
                                                                                        'mt_id': 0,
                                                                                        'tos': 0}},
                                                                                'type': 'transit network'},
                                                                            '10.1.4.4': 
                                                                                {'link_data': '10.1.4.1',
                                                                                'link_id': '10.1.4.4',
                                                                                'num_tos_metrics': 0,
                                                                                'topologies': 
                                                                                    {0: 
                                                                                        {'metric': 1,
                                                                                        'mt_id': 0,
                                                                                        'tos': 0}},
                                                                                'type': 'transit network'}},
                                                                        'num_of_links': 3}},
                                                                'header': 
                                                                    {'adv_router': '1.1.1.1',
                                                                    'age': 1802,
                                                                    'checksum': '0x6228',
                                                                    'length': 60,
                                                                    'lsa_id': '1.1.1.1',
                                                                    'option': 'None',
                                                                    'option_desc': 'No '
                                                                    'TOS-capability, '
                                                                    'DC',
                                                                    'routing_bit_enable': True,
                                                                    'seq_num': '8000003d',
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
                                                                                'num_tos_metrics': 0,
                                                                                'topologies': 
                                                                                    {0: 
                                                                                        {'metric': 1,
                                                                                        'mt_id': 0,
                                                                                        'tos': 0}},
                                                                                'type': 'transit network'},
                                                                            '10.2.3.3': 
                                                                                {'link_data': '10.2.3.2',
                                                                                'link_id': '10.2.3.3',
                                                                                'num_tos_metrics': 0,
                                                                                'topologies': 
                                                                                    {0: 
                                                                                        {'metric': 1,
                                                                                        'mt_id': 0,
                                                                                        'tos': 0}},
                                                                                'type': 'transit network'},
                                                                            '10.2.4.4': 
                                                                                {'link_data': '10.2.4.2',
                                                                                'link_id': '10.2.4.4',
                                                                                'num_tos_metrics': 0,
                                                                                'topologies': 
                                                                                    {0: 
                                                                                        {'metric': 1,
                                                                                        'mt_id': 0,
                                                                                        'tos': 0}},
                                                                                'type': 'transit network'},
                                                                            '2.2.2.2': 
                                                                                {'link_data': '255.255.255.255',
                                                                                'link_id': '2.2.2.2',
                                                                                'num_tos_metrics': 0,
                                                                                'topologies': 
                                                                                    {0: 
                                                                                        {'metric': 1,
                                                                                        'mt_id': 0,
                                                                                        'tos': 0}},
                                                                                'type': 'stub network'}},
                                                                        'num_of_links': 4}},
                                                                'header': 
                                                                    {'adv_router': '2.2.2.2',
                                                                    'age': 756,
                                                                    'checksum': '0x652b',
                                                                    'length': 72,
                                                                    'lsa_id': '2.2.2.2',
                                                                    'option': 'None',
                                                                    'option_desc': 'No '
                                                                    'TOS-capability, '
                                                                    'No '
                                                                    'DC',
                                                                    'routing_bit_enable': True,
                                                                    'seq_num': '80000014',
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
                                                                                'num_tos_metrics': 0,
                                                                                'topologies': 
                                                                                    {0: 
                                                                                        {'metric': 1,
                                                                                        'mt_id': 0,
                                                                                        'tos': 0}},
                                                                                'type': 'transit network'},
                                                                            '10.3.4.4': 
                                                                                {'link_data': '10.3.4.3',
                                                                                'link_id': '10.3.4.4',
                                                                                'num_tos_metrics': 0,
                                                                                'topologies': 
                                                                                    {0: 
                                                                                        {'metric': 1,
                                                                                        'mt_id': 0,
                                                                                        'tos': 0}},
                                                                                'type': 'transit network'},
                                                                            '3.3.3.3': 
                                                                                {'link_data': '255.255.255.255',
                                                                                'link_id': '3.3.3.3',
                                                                                'num_tos_metrics': 0,
                                                                                'topologies': 
                                                                                    {0: 
                                                                                        {'metric': 1,
                                                                                        'mt_id': 0,
                                                                                        'tos': 0}},
                                                                                'type': 'stub network'}},
                                                                        'num_of_links': 3}},
                                                                'header': 
                                                                    {'adv_router': '3.3.3.3',
                                                                    'age': 1291,
                                                                    'checksum': '0x75f8',
                                                                    'length': 60,
                                                                    'lsa_id': '3.3.3.3',
                                                                    'option': 'None',
                                                                    'option_desc': 'No '
                                                                    'TOS-capability, '
                                                                    'DC',
                                                                    'routing_bit_enable': True,
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
                                                                                'num_tos_metrics': 0,
                                                                                'topologies': 
                                                                                    {0: 
                                                                                        {'metric': 1,
                                                                                        'mt_id': 0,
                                                                                        'tos': 0}},
                                                                                'type': 'transit network'},
                                                                            '10.2.4.4': 
                                                                                {'link_data': '10.2.4.4',
                                                                                'link_id': '10.2.4.4',
                                                                                'num_tos_metrics': 0,
                                                                                'topologies': 
                                                                                    {0: 
                                                                                        {'metric': 1,
                                                                                        'mt_id': 0,
                                                                                        'tos': 0}},
                                                                                'type': 'transit network'},
                                                                            '10.3.4.4': 
                                                                                {'link_data': '10.3.4.4',
                                                                                'link_id': '10.3.4.4',
                                                                                'num_tos_metrics': 0,
                                                                                'topologies': 
                                                                                    {0: 
                                                                                        {'metric': 1,
                                                                                        'mt_id': 0,
                                                                                        'tos': 0}},
                                                                                'type': 'transit network'},
                                                                            '4.4.4.4': 
                                                                                {'link_data': '255.255.255.255',
                                                                                'link_id': '4.4.4.4',
                                                                                'num_tos_metrics': 0,
                                                                                'topologies': 
                                                                                    {0: 
                                                                                        {'metric': 1,
                                                                                        'mt_id': 0,
                                                                                        'tos': 0}},
                                                                                'type': 'stub network'}},
                                                                        'num_of_links': 4}},
                                                                'header': 
                                                                    {'adv_router': '4.4.4.4',
                                                                    'age': 505,
                                                                    'as_boundary_router': True,
                                                                    'checksum': '0xa37d',
                                                                    'length': 72,
                                                                    'lsa_id': '4.4.4.4',
                                                                    'option': 'None',
                                                                    'option_desc': 'No '
                                                                    'TOS-capability, '
                                                                    'DC',
                                                                    'routing_bit_enable': True,
                                                                    'seq_num': '80000037',
                                                                    'type': 1}}}}}}}}}}}}}}}}

    golden_output1 = {'execute.return_value': '''
        RP/0/0/CPU0:R3_ospf_xr#show ospf vrf all-inclusive database router 
        Thu Nov  2 21:25:10.231 UTC

                    OSPF Router with ID (3.3.3.3) (Process ID 1)

                        Router Link States (Area 0)

          Routing Bit Set on this LSA
          LS age: 1802
          Options: (No TOS-capability, DC)
          LS Type: Router Links
          Link State ID: 1.1.1.1
          Advertising Router: 1.1.1.1
          LS Seq Number: 8000003d
          Checksum: 0x6228
          Length: 60
           Number of Links: 3

            Link connected to: a Stub Network
             (Link ID) Network/subnet number: 1.1.1.1
             (Link Data) Network Mask: 255.255.255.255
              Number of TOS metrics: 0
               TOS 0 Metrics: 1

            Link connected to: a Transit Network
             (Link ID) Designated Router address: 10.1.2.1
             (Link Data) Router Interface address: 10.1.2.1
              Number of TOS metrics: 0
               TOS 0 Metrics: 1

            Link connected to: a Transit Network
             (Link ID) Designated Router address: 10.1.4.4
             (Link Data) Router Interface address: 10.1.4.1
              Number of TOS metrics: 0
               TOS 0 Metrics: 1


          Routing Bit Set on this LSA
          LS age: 756
          Options: (No TOS-capability, No DC)
          LS Type: Router Links
          Link State ID: 2.2.2.2
          Advertising Router: 2.2.2.2
          LS Seq Number: 80000014
          Checksum: 0x652b
          Length: 72
           Number of Links: 4

            Link connected to: a Stub Network
             (Link ID) Network/subnet number: 2.2.2.2
             (Link Data) Network Mask: 255.255.255.255
              Number of TOS metrics: 0
               TOS 0 Metrics: 1

            Link connected to: a Transit Network
             (Link ID) Designated Router address: 10.2.3.3
             (Link Data) Router Interface address: 10.2.3.2
              Number of TOS metrics: 0
               TOS 0 Metrics: 1

            Link connected to: a Transit Network
             (Link ID) Designated Router address: 10.2.4.4
             (Link Data) Router Interface address: 10.2.4.2
              Number of TOS metrics: 0
               TOS 0 Metrics: 1

            Link connected to: a Transit Network
             (Link ID) Designated Router address: 10.1.2.1
             (Link Data) Router Interface address: 10.1.2.2
              Number of TOS metrics: 0
               TOS 0 Metrics: 1


          LS age: 1291
          Options: (No TOS-capability, DC)
          LS Type: Router Links
          Link State ID: 3.3.3.3
          Advertising Router: 3.3.3.3
          LS Seq Number: 80000033
          Checksum: 0x75f8
          Length: 60
           Number of Links: 3

            Link connected to: a Stub Network
             (Link ID) Network/subnet number: 3.3.3.3
             (Link Data) Network Mask: 255.255.255.255
              Number of TOS metrics: 0
               TOS 0 Metrics: 1

            Link connected to: a Transit Network
             (Link ID) Designated Router address: 10.3.4.4
             (Link Data) Router Interface address: 10.3.4.3
              Number of TOS metrics: 0
               TOS 0 Metrics: 1

            Link connected to: a Transit Network
             (Link ID) Designated Router address: 10.2.3.3
             (Link Data) Router Interface address: 10.2.3.3
              Number of TOS metrics: 0
               TOS 0 Metrics: 1


          Routing Bit Set on this LSA
          LS age: 505
          Options: (No TOS-capability, DC)
          LS Type: Router Links
          Link State ID: 4.4.4.4
          Advertising Router: 4.4.4.4
          LS Seq Number: 80000037
          Checksum: 0xa37d
          Length: 72
          AS Boundary Router
           Number of Links: 4

            Link connected to: a Stub Network
             (Link ID) Network/subnet number: 4.4.4.4
             (Link Data) Network Mask: 255.255.255.255
              Number of TOS metrics: 0
               TOS 0 Metrics: 1

            Link connected to: a Transit Network
             (Link ID) Designated Router address: 10.2.4.4
             (Link Data) Router Interface address: 10.2.4.4
              Number of TOS metrics: 0
               TOS 0 Metrics: 1

            Link connected to: a Transit Network
             (Link ID) Designated Router address: 10.3.4.4
             (Link Data) Router Interface address: 10.3.4.4
              Number of TOS metrics: 0
               TOS 0 Metrics: 1

            Link connected to: a Transit Network
             (Link ID) Designated Router address: 10.1.4.4
             (Link Data) Router Interface address: 10.1.4.4
              Number of TOS metrics: 0
               TOS 0 Metrics: 1


                    OSPF Router with ID (3.3.3.3) (Process ID 1, VRF VRF1)

                        Router Link States (Area 1)

          LS age: 217
          Options: (No TOS-capability, DC)
          LS Type: Router Links
          Link State ID: 3.3.3.3
          Advertising Router: 3.3.3.3
          LS Seq Number: 80000036
          Checksum: 0x5646
          Length: 36
          Area Border Router
          AS Boundary Router
           Number of Links: 1

            Link connected to: a Transit Network
             (Link ID) Designated Router address: 20.3.7.7
             (Link Data) Router Interface address: 20.3.7.3
              Number of TOS metrics: 0
               TOS 0 Metrics: 1


          Routing Bit Set on this LSA
          LS age: 1713
          Options: (No TOS-capability, DC)
          LS Type: Router Links
          Link State ID: 11.11.11.11
          Advertising Router: 11.11.11.11
          LS Seq Number: 8000003e
          Checksum: 0x9ce3
          Length: 48
          Area Border Router
          AS Boundary Router
           Number of Links: 2

            Link connected to: another Router (point-to-point)
             (Link ID) Neighboring Router ID: 22.22.22.22
             (Link Data) Router Interface address: 0.0.0.14
              Number of TOS metrics: 0
               TOS 0 Metrics: 111

            Link connected to: a Transit Network
             (Link ID) Designated Router address: 20.1.5.1
             (Link Data) Router Interface address: 20.1.5.1
              Number of TOS metrics: 0
               TOS 0 Metrics: 1


          Routing Bit Set on this LSA
          LS age: 1539
          Options: (No TOS-capability, No DC)
          LS Type: Router Links
          Link State ID: 22.22.22.22
          Advertising Router: 22.22.22.22
          LS Seq Number: 80000019
          Checksum: 0xc41a
          Length: 48
          Area Border Router
          AS Boundary Router
           Number of Links: 2

            Link connected to: a Transit Network
             (Link ID) Designated Router address: 20.2.6.6
             (Link Data) Router Interface address: 20.2.6.2
              Number of TOS metrics: 0
               TOS 0 Metrics: 40

            Link connected to: another Router (point-to-point)
             (Link ID) Neighboring Router ID: 11.11.11.11
             (Link Data) Router Interface address: 0.0.0.6
              Number of TOS metrics: 0
               TOS 0 Metrics: 1


          Routing Bit Set on this LSA
          LS age: 1378
          Options: (No TOS-capability, DC)
          LS Type: Router Links
          Link State ID: 55.55.55.55
          Advertising Router: 55.55.55.55
          LS Seq Number: 80000037
          Checksum: 0xe7bc
          Length: 60
           Number of Links: 3

            Link connected to: a Stub Network
             (Link ID) Network/subnet number: 55.55.55.55
             (Link Data) Network Mask: 255.255.255.255
              Number of TOS metrics: 0
               TOS 0 Metrics: 1

            Link connected to: a Transit Network
             (Link ID) Designated Router address: 20.5.6.6
             (Link Data) Router Interface address: 20.5.6.5
              Number of TOS metrics: 0
               TOS 0 Metrics: 30

            Link connected to: a Transit Network
             (Link ID) Designated Router address: 20.1.5.1
             (Link Data) Router Interface address: 20.1.5.5
              Number of TOS metrics: 0
               TOS 0 Metrics: 1


          Routing Bit Set on this LSA
          LS age: 1578
          Options: (No TOS-capability, DC)
          LS Type: Router Links
          Link State ID: 66.66.66.66
          Advertising Router: 66.66.66.66
          LS Seq Number: 8000003c
          Checksum: 0x1282
          Length: 72
           Number of Links: 4

            Link connected to: a Stub Network
             (Link ID) Network/subnet number: 66.66.66.66
             (Link Data) Network Mask: 255.255.255.255
              Number of TOS metrics: 0
               TOS 0 Metrics: 1

            Link connected to: a Transit Network
             (Link ID) Designated Router address: 20.6.7.6
             (Link Data) Router Interface address: 20.6.7.6
              Number of TOS metrics: 0
               TOS 0 Metrics: 30

            Link connected to: a Transit Network
             (Link ID) Designated Router address: 20.2.6.6
             (Link Data) Router Interface address: 20.2.6.6
              Number of TOS metrics: 0
               TOS 0 Metrics: 1

            Link connected to: a Transit Network
             (Link ID) Designated Router address: 20.5.6.6
             (Link Data) Router Interface address: 20.5.6.6
              Number of TOS metrics: 0
               TOS 0 Metrics: 30


          Routing Bit Set on this LSA
          LS age: 1344
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
              Number of TOS metrics: 0
               TOS 0 Metrics: 1

            Link connected to: a Transit Network
             (Link ID) Designated Router address: 20.6.7.6
             (Link Data) Router Interface address: 20.6.7.7
              Number of TOS metrics: 0
               TOS 0 Metrics: 30

            Link connected to: a Transit Network
             (Link ID) Designated Router address: 20.3.7.7
             (Link Data) Router Interface address: 20.3.7.7
              Number of TOS metrics: 0
               TOS 0 Metrics: 1
        '''}

    def test_show_ospf_vrf_all_inclusive_database_router_full(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output1)
        obj = ShowOspfVrfAllInclusiveDatabaseRouter(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output1)

    def test_show_ospf_vrf_all_inclusive_database_router_empty(self):
        self.maxDiff = None
        self.device = Mock(**self.empty_output)
        obj = ShowOspfVrfAllInclusiveDatabaseRouter(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()


# ==============================================================
#  Unit test for 'show ospf vrf all-inclusive database external'
# ==============================================================
class test_show_ospf_vrf_all_inclusive_database_external(unittest.TestCase):

    '''Unit test for "show ospf vrf all-inclusive database external" '''

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
                                                                                {'external_route_tag': '0',
                                                                                'flags': 'E',
                                                                                'forwarding_address': '0.0.0.0',
                                                                                'metric': 20,
                                                                                'mt_id': 0,
                                                                                'tos': 0}}}},
                                                                'header': 
                                                                    {'adv_router': '4.4.4.4',
                                                                    'age': 608,
                                                                    'checksum': '0x7d61',
                                                                    'length': 36,
                                                                    'lsa_id': '44.44.44.44',
                                                                    'option': 'None',
                                                                    'option_desc': 'No TOS-capability, DC',
                                                                    'routing_bit_enable': True,
                                                                    'seq_num': '80000002',
                                                                    'type': 5}}}}}}}}}}}}}}}}

    golden_output1 = {'execute.return_value': '''
        RP/0/0/CPU0:R3_ospf_xr#show ospf vrf all-inclusive database external 
        Thu Nov  2 21:26:53.724 UTC


                    OSPF Router with ID (3.3.3.3) (Process ID 1)

                        Type-5 AS External Link States

          Routing Bit Set on this LSA
          LS age: 608
          Options: (No TOS-capability, DC)
          LS Type: AS External Link
          Link State ID: 44.44.44.44 (External Network Number)
          Advertising Router: 4.4.4.4
          LS Seq Number: 80000002
          Checksum: 0x7d61
          Length: 36
          Network Mask: /32
                Metric Type: 2 (Larger than any link state path)
                TOS: 0 
                Metric: 20 
                Forward Address: 0.0.0.0
                External Route Tag: 0
        '''}

    def test_show_ospf_vrf_all_inclusive_database_external_full(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output1)
        obj = ShowOspfVrfAllInclusiveDatabaseExternal(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output1)

    def test_show_ospf_vrf_all_inclusive_database_external_empty(self):
        self.maxDiff = None
        self.device = Mock(**self.empty_output)
        obj = ShowOspfVrfAllInclusiveDatabaseExternal(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()


# =============================================================
#  Unit test for 'show ospf vrf all-inclusive database network'
# =============================================================
class test_show_ospf_vrf_all_inclusive_database_network(unittest.TestCase):

    '''Unit test for "show ospf vrf all-inclusive database network" '''

    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output1 = {
        'vrf': 
            {'VRF1': 
                {'address_family': 
                    {'ipv4': 
                        {'instance': 
                            {'1': 
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
                                                                    'age': 522,
                                                                    'checksum': '0xddd9',
                                                                    'length': 32,
                                                                    'lsa_id': '20.1.5.1',
                                                                    'option': 'None',
                                                                    'option_desc': 'No '
                                                                    'TOS-capability, '
                                                                    'DC',
                                                                    'routing_bit_enable': True,
                                                                    'seq_num': '80000033',
                                                                    'type': 2}}},
                                                        '20.2.6.6 66.66.66.66': 
                                                            {'adv_router': '66.66.66.66',
                                                            'lsa_id': '20.2.6.6',
                                                            'ospfv2': 
                                                                {'body': 
                                                                    {'network': 
                                                                        {'attached_routers': {'22.22.22.22': {},
                                                                        '66.66.66.66': {}},
                                                                    'network_mask': '255.255.255.0'}},
                                                                'header': 
                                                                    {'adv_router': '66.66.66.66',
                                                                    'age': 146,
                                                                    'checksum': '0x3f5f',
                                                                    'length': 32,
                                                                    'lsa_id': '20.2.6.6',
                                                                    'option': 'None',
                                                                    'option_desc': 'No '
                                                                    'TOS-capability, '
                                                                    'DC',
                                                                    'routing_bit_enable': True,
                                                                    'seq_num': '80000010',
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
                                                                    'age': 1903,
                                                                    'checksum': '0x5c19',
                                                                    'length': 32,
                                                                    'lsa_id': '20.3.7.7',
                                                                    'option': 'None',
                                                                    'option_desc': 'No '
                                                                    'TOS-capability, '
                                                                    'DC',
                                                                    'routing_bit_enable': True,
                                                                    'seq_num': '8000002a',
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
                                                                    'age': 1620,
                                                                    'checksum': '0x619c',
                                                                    'length': 32,
                                                                    'lsa_id': '20.5.6.6',
                                                                    'option': 'None',
                                                                    'option_desc': 'No '
                                                                    'TOS-capability, '
                                                                    'DC',
                                                                    'routing_bit_enable': True,
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
                                                                    'age': 884,
                                                                    'checksum': '0x960b',
                                                                    'length': 32,
                                                                    'lsa_id': '20.6.7.6',
                                                                    'option': 'None',
                                                                    'option_desc': 'No '
                                                                    'TOS-capability, '
                                                                    'DC',
                                                                    'routing_bit_enable': True,
                                                                    'seq_num': '8000002b',
                                                                    'type': 2}}}}}}}}}}}}}},
            'default': 
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
                                                                    'age': 1844,
                                                                    'checksum': '0x3dd0',
                                                                    'length': 32,
                                                                    'lsa_id': '10.1.2.1',
                                                                    'option': 'None',
                                                                    'option_desc': 'No '
                                                                    'TOS-capability, '
                                                                    'DC',
                                                                    'routing_bit_enable': True,
                                                                    'seq_num': '8000000f',
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
                                                                    'age': 546,
                                                                    'checksum': '0xa232',
                                                                    'length': 32,
                                                                    'lsa_id': '10.1.4.4',
                                                                    'option': 'None',
                                                                    'option_desc': 'No '
                                                                    'TOS-capability, '
                                                                    'DC',
                                                                    'routing_bit_enable': True,
                                                                    'seq_num': '8000002f',
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
                                                                    'age': 1828,
                                                                    'checksum': '0x2acf',
                                                                    'length': 32,
                                                                    'lsa_id': '10.2.3.3',
                                                                    'option': 'None',
                                                                    'option_desc': 'No '
                                                                    'TOS-capability, '
                                                                    'DC',
                                                                    'routing_bit_enable': True,
                                                                    'seq_num': '8000000f',
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
                                                                    'age': 1803,
                                                                    'checksum': '0x9e6',
                                                                    'length': 32,
                                                                    'lsa_id': '10.2.4.4',
                                                                    'option': 'None',
                                                                    'option_desc': 'No '
                                                                    'TOS-capability, '
                                                                    'DC',
                                                                    'routing_bit_enable': True,
                                                                    'seq_num': '8000000f',
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
                                                                    'age': 52,
                                                                    'checksum': '0xeedb',
                                                                    'length': 32,
                                                                    'lsa_id': '10.3.4.4',
                                                                    'option': 'None',
                                                                    'option_desc': 'No '
                                                                    'TOS-capability, '
                                                                    'DC',
                                                                    'routing_bit_enable': True,
                                                                    'seq_num': '8000002f',
                                                                    'type': 2}}}}}}}}}}}}}}}}

    golden_output1 = {'execute.return_value': '''
        P/0/0/CPU0:R3_ospf_xr#show ospf vrf all-inclusive database network 
        Thu Nov  2 21:25:51.748 UTC

                    OSPF Router with ID (3.3.3.3) (Process ID 1)

                        Net Link States (Area 0)

          Routing Bit Set on this LSA
          LS age: 1844
          Options: (No TOS-capability, DC)
          LS Type: Network Links
          Link State ID: 10.1.2.1 (address of Designated Router)
          Advertising Router: 1.1.1.1
          LS Seq Number: 8000000f
          Checksum: 0x3dd0
          Length: 32
          Network Mask: /24
                Attached Router: 1.1.1.1
                Attached Router: 2.2.2.2

          Routing Bit Set on this LSA
          LS age: 546
          Options: (No TOS-capability, DC)
          LS Type: Network Links
          Link State ID: 10.1.4.4 (address of Designated Router)
          Advertising Router: 4.4.4.4
          LS Seq Number: 8000002f
          Checksum: 0xa232
          Length: 32
          Network Mask: /24
                Attached Router: 4.4.4.4
                Attached Router: 1.1.1.1

          Routing Bit Set on this LSA
          LS age: 1828
          Options: (No TOS-capability, DC)
          LS Type: Network Links
          Link State ID: 10.2.3.3 (address of Designated Router)
          Advertising Router: 3.3.3.3
          LS Seq Number: 8000000f
          Checksum: 0x2acf
          Length: 32
          Network Mask: /24
                Attached Router: 2.2.2.2
                Attached Router: 3.3.3.3

          Routing Bit Set on this LSA
          LS age: 1803
          Options: (No TOS-capability, DC)
          LS Type: Network Links
          Link State ID: 10.2.4.4 (address of Designated Router)
          Advertising Router: 4.4.4.4
          LS Seq Number: 8000000f
          Checksum: 0x9e6
          Length: 32
          Network Mask: /24
                Attached Router: 4.4.4.4
                Attached Router: 2.2.2.2

          Routing Bit Set on this LSA
          LS age: 52
          Options: (No TOS-capability, DC)
          LS Type: Network Links
          Link State ID: 10.3.4.4 (address of Designated Router)
          Advertising Router: 4.4.4.4
          LS Seq Number: 8000002f
          Checksum: 0xeedb
          Length: 32
          Network Mask: /24
                Attached Router: 4.4.4.4
                Attached Router: 3.3.3.3


                    OSPF Router with ID (3.3.3.3) (Process ID 1, VRF VRF1)

                        Net Link States (Area 1)

          Routing Bit Set on this LSA
          LS age: 522
          Options: (No TOS-capability, DC)
          LS Type: Network Links
          Link State ID: 20.1.5.1 (address of Designated Router)
          Advertising Router: 11.11.11.11
          LS Seq Number: 80000033
          Checksum: 0xddd9
          Length: 32
          Network Mask: /24
                Attached Router: 11.11.11.11
                Attached Router: 55.55.55.55

          Routing Bit Set on this LSA
          LS age: 146
          Options: (No TOS-capability, DC)
          LS Type: Network Links
          Link State ID: 20.2.6.6 (address of Designated Router)
          Advertising Router: 66.66.66.66
          LS Seq Number: 80000010
          Checksum: 0x3f5f
          Length: 32
          Network Mask: /24
                Attached Router: 66.66.66.66
                Attached Router: 22.22.22.22

          Routing Bit Set on this LSA
          LS age: 1903
          Options: (No TOS-capability, DC)
          LS Type: Network Links
          Link State ID: 20.3.7.7 (address of Designated Router)
          Advertising Router: 77.77.77.77
          LS Seq Number: 8000002a
          Checksum: 0x5c19
          Length: 32
          Network Mask: /24
                Attached Router: 77.77.77.77
                Attached Router: 3.3.3.3

          Routing Bit Set on this LSA
          LS age: 1620
          Options: (No TOS-capability, DC)
          LS Type: Network Links
          Link State ID: 20.5.6.6 (address of Designated Router)
          Advertising Router: 66.66.66.66
          LS Seq Number: 80000029
          Checksum: 0x619c
          Length: 32
          Network Mask: /24
                Attached Router: 66.66.66.66
                Attached Router: 55.55.55.55

          Routing Bit Set on this LSA
          LS age: 884
          Options: (No TOS-capability, DC)
          LS Type: Network Links
          Link State ID: 20.6.7.6 (address of Designated Router)
          Advertising Router: 66.66.66.66
          LS Seq Number: 8000002b
          Checksum: 0x960b
          Length: 32
          Network Mask: /24
                Attached Router: 66.66.66.66
                Attached Router: 77.77.77.77
        '''}

    def test_show_ospf_vrf_all_inclusive_database_network_full(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output1)
        obj = ShowOspfVrfAllInclusiveDatabaseNetwork(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output1)

    def test_show_ospf_vrf_all_inclusive_database_network_empty(self):
        self.maxDiff = None
        self.device = Mock(**self.empty_output)
        obj = ShowOspfVrfAllInclusiveDatabaseNetwork(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()


# =============================================================
#  Unit test for 'show ospf vrf all-inclusive database summary'
# =============================================================
class test_show_ospf_vrf_all_inclusive_database_summary(unittest.TestCase):

    '''Unit test for "show ospf vrf all-inclusive database summary" '''

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
                                                        {'20.1.3.0 2.2.2.2': 
                                                            {'adv_router': '2.2.2.2',
                                                            'lsa_id': '20.1.3.0',
                                                            'ospfv2': 
                                                                {'body': 
                                                                    {'summary': 
                                                                        {'network_mask': '255.255.255.0',
                                                                        'topologies': 
                                                                            {0: 
                                                                                {'metric': 65575,
                                                                                'mt_id': 0,
                                                                                'tos': 0}}}},
                                                                'header': 
                                                                    {'adv_router': '2.2.2.2',
                                                                    'age': 520,
                                                                    'checksum': '0xaa4a',
                                                                    'length': 28,
                                                                    'lsa_id': '20.1.3.0',
                                                                    'option': 'None',
                                                                    'option_desc': 'No '
                                                                    'TOS-capability, '
                                                                    'DC',
                                                                    'seq_num': '80000001',
                                                                    'type': 3}}},
                                                        '20.2.3.0 2.2.2.2': 
                                                            {'adv_router': '2.2.2.2',
                                                            'lsa_id': '20.2.3.0',
                                                            'ospfv2': 
                                                                {'body': 
                                                                    {'summary': 
                                                                        {'network_mask': '255.255.255.0',
                                                                        'topologies': 
                                                                            {0: 
                                                                                {'metric': 65535,
                                                                                'mt_id': 0,
                                                                                'tos': 0}}}},
                                                                'header': 
                                                                    {'adv_router': '2.2.2.2',
                                                                    'age': 519,
                                                                    'checksum': '0xd0e',
                                                                    'length': 28,
                                                                    'lsa_id': '20.2.3.0',
                                                                    'option': 'None',
                                                                    'option_desc': 'No '
                                                                    'TOS-capability, '
                                                                    'DC',
                                                                    'seq_num': '80000002',
                                                                    'type': 3}}},
                                                        '20.2.4.0 2.2.2.2': 
                                                            {'adv_router': '2.2.2.2',
                                                            'lsa_id': '20.2.4.0',
                                                            'ospfv2': 
                                                                {'body': 
                                                                    {'summary': 
                                                                        {'network_mask': '255.255.255.0',
                                                                        'topologies': 
                                                                            {0: 
                                                                                {'metric': 65535,
                                                                                'mt_id': 0,
                                                                                'tos': 0}}}},
                                                                'header': 
                                                                    {'adv_router': '2.2.2.2',
                                                                    'age': 297,
                                                                    'checksum': '0x218',
                                                                    'length': 28,
                                                                    'lsa_id': '20.2.4.0',
                                                                    'option': 'None',
                                                                    'option_desc': 'No '
                                                                    'TOS-capability, '
                                                                    'DC',
                                                                    'seq_num': '80000002',
                                                                    'type': 3}}},
                                                        '20.3.4.0 2.2.2.2': 
                                                            {'adv_router': '2.2.2.2',
                                                            'lsa_id': '20.3.4.0',
                                                            'ospfv2': 
                                                                {'body': 
                                                                    {'summary': 
                                                                        {'network_mask': '255.255.255.0',
                                                                        'topologies': 
                                                                            {0: 
                                                                                {'metric': 65536,
                                                                                'mt_id': 0,
                                                                                'tos': 0}}}},
                                                                'header': 
                                                                    {'adv_router': '2.2.2.2',
                                                                    'age': 294,
                                                                    'checksum': '0xfd1a',
                                                                    'length': 28,
                                                                    'lsa_id': '20.3.4.0',
                                                                    'option': 'None',
                                                                    'option_desc': 'No '
                                                                    'TOS-capability, '
                                                                    'DC',
                                                                    'seq_num': '80000002',
                                                                    'type': 3}}},
                                                        '4.4.4.4 2.2.2.2': 
                                                            {'adv_router': '2.2.2.2',
                                                            'lsa_id': '4.4.4.4',
                                                            'ospfv2': 
                                                                {'body': 
                                                                    {'summary': 
                                                                        {'network_mask': '255.255.255.255',
                                                                        'topologies': 
                                                                            {0: 
                                                                                {'metric': 65536,
                                                                                'mt_id': 0,
                                                                                'tos': 0}}}},
                                                                'header': 
                                                                    {'adv_router': '2.2.2.2',
                                                                    'age': 295,
                                                                    'checksum': '0x9c87',
                                                                    'length': 28,
                                                                    'lsa_id': '4.4.4.4',
                                                                    'option': 'None',
                                                                    'option_desc': 'No '
                                                                    'TOS-capability, '
                                                                    'DC',
                                                                    'seq_num': '80000001',
                                                                    'type': 3}}}}}}}},
                                    '0.0.0.1': 
                                        {'database': 
                                            {'lsa_types': 
                                                {3: 
                                                    {'lsa_type': 3,
                                                    'lsas': 
                                                        {'10.1.2.0 2.2.2.2': 
                                                            {'adv_router': '2.2.2.2',
                                                            'lsa_id': '10.1.2.0',
                                                            'ospfv2': 
                                                                {'body': 
                                                                    {'summary': 
                                                                        {'network_mask': '255.255.255.0',
                                                                        'topologies': 
                                                                            {0: 
                                                                                {'metric': 4294,
                                                                                'mt_id': 0,
                                                                                'tos': 0}}}},
                                                                'header': 
                                                                    {'adv_router': '2.2.2.2',
                                                                     'age': 675,
                                                                     'checksum': '0xfc54',
                                                                     'length': 28,
                                                                     'lsa_id': '10.1.2.0',
                                                                     'option': 'None',
                                                                     'option_desc': 'No '
                                                                                    'TOS-capability, '
                                                                                    'DC',
                                                                     'routing_bit_enable': True,
                                                                     'seq_num': '80000001',
                                                                     'type': 3}}},
                                                        '10.1.2.0 3.3.3.3': 
                                                            {'adv_router': '3.3.3.3',
                                                            'lsa_id': '10.1.2.0',
                                                            'ospfv2': 
                                                                {'body': 
                                                                    {'summary': 
                                                                        {'network_mask': '255.255.255.0',
                                                                        'topologies': 
                                                                            {0: 
                                                                                {'metric': 151,
                                                                                'mt_id': 0,
                                                                                'tos': 0}}}},
                                                                'header': 
                                                                    {'adv_router': '3.3.3.3',
                                                                    'age': 521,
                                                                    'checksum': '0x5655',
                                                                    'length': 28,
                                                                    'lsa_id': '10.1.2.0',
                                                                    'option': 'None',
                                                                    'option_desc': 'No '
                                                                    'TOS-capability, '
                                                                    'No '
                                                                    'DC',
                                                                    'routing_bit_enable': True,
                                                                    'seq_num': '80000002',
                                                                    'type': 3}}},
                                                        '10.1.3.0 3.3.3.3': 
                                                            {'adv_router': '3.3.3.3',
                                                            'lsa_id': '10.1.3.0',
                                                            'ospfv2': 
                                                                {'body': 
                                                                    {'summary': 
                                                                        {'network_mask': '255.255.255.0',
                                                                        'topologies': 
                                                                            {0: 
                                                                                {'metric': 40,
                                                                                'mt_id': 0,
                                                                                'tos': 0}}}},
                                                                'header': 
                                                                    {'adv_router': '3.3.3.3',
                                                                    'age': 531,
                                                                    'checksum': '0xf029',
                                                                    'length': 28,
                                                                    'lsa_id': '10.1.3.0',
                                                                    'option': 'None',
                                                                    'option_desc': 'No '
                                                                    'TOS-capability, '
                                                                    'No '
                                                                    'DC',
                                                                    'routing_bit_enable': True,
                                                                    'seq_num': '80000002',
                                                                    'type': 3}}},
                                                        '10.2.3.0 2.2.2.2': 
                                                            {'adv_router': '2.2.2.2',
                                                            'lsa_id': '10.2.3.0',
                                                            'ospfv2': 
                                                                {'body': 
                                                                    {'summary': 
                                                                        {'network_mask': '255.255.255.0',
                                                                        'topologies': 
                                                                            {0: 
                                                                                {'metric': 222,
                                                                                'mt_id': 0,
                                                                                'tos': 0}}}},
                                                                'header': 
                                                                    {'adv_router': '2.2.2.2',
                                                                    'age': 675,
                                                                    'checksum': '0x4601',
                                                                    'length': 28,
                                                                    'lsa_id': '10.2.3.0',
                                                                    'option': 'None',
                                                                    'option_desc': 'No '
                                                                    'TOS-capability, '
                                                                    'DC',
                                                                    'routing_bit_enable': True,
                                                                    'seq_num': '80000001',
                                                                    'type': 3}}},
                                                        '10.2.3.0 3.3.3.3': 
                                                            {'adv_router': '3.3.3.3',
                                                            'lsa_id': '10.2.3.0',
                                                            'ospfv2': 
                                                                {'body': 
                                                                    {'summary': 
                                                                        {'network_mask': '255.255.255.0',
                                                                        'topologies': 
                                                                            {0: 
                                                                                {'metric': 262,
                                                                                'mt_id': 0,
                                                                                'tos': 0}}}},
                                                                'header': 
                                                                    {'adv_router': '3.3.3.3',
                                                                    'age': 287,
                                                                    'checksum': '0x96a2',
                                                                    'length': 28,
                                                                    'lsa_id': '10.2.3.0',
                                                                    'option': 'None',
                                                                    'option_desc': 'No '
                                                                    'TOS-capability, '
                                                                    'No '
                                                                    'DC',
                                                                    'routing_bit_enable': True,
                                                                    'seq_num': '80000003',
                                                                    'type': 3}}},
                                                        '2.2.2.2 2.2.2.2': 
                                                            {'adv_router': '2.2.2.2',
                                                            'lsa_id': '2.2.2.2',
                                                            'ospfv2': 
                                                                {'body': 
                                                                    {'summary': 
                                                                        {'network_mask': '255.255.255.255',
                                                                        'topologies': 
                                                                            {0: 
                                                                                {'metric': 1,
                                                                                'mt_id': 0,
                                                                                'tos': 0}}}},
                                                                'header': 
                                                                    {'adv_router': '2.2.2.2',
                                                                    'age': 676,
                                                                    'checksum': '0xfa31',
                                                                    'length': 28,
                                                                    'lsa_id': '2.2.2.2',
                                                                    'option': 'None',
                                                                    'option_desc': 'No '
                                                                    'TOS-capability, '
                                                                    'DC',
                                                                    'seq_num': '80000001',
                                                                    'type': 3}}},
                                                        '3.3.3.3 3.3.3.3': 
                                                            {'adv_router': '3.3.3.3',
                                                            'lsa_id': '3.3.3.3',
                                                            'ospfv2': 
                                                                {'body': 
                                                                    {'summary': 
                                                                        {'network_mask': '255.255.255.255',
                                                                        'topologies': 
                                                                            {0: 
                                                                                {'metric': 1,
                                                                                'mt_id': 0,
                                                                                'tos': 0}}}},
                                                                'header': 
                                                                    {'adv_router': '3.3.3.3',
                                                                    'age': 531,
                                                                    'checksum': '0x8eb4',
                                                                    'length': 28,
                                                                    'lsa_id': '3.3.3.3',
                                                                    'option': 'None',
                                                                    'option_desc': 'No '
                                                                    'TOS-capability, '
                                                                    'No '
                                                                    'DC',
                                                                    'routing_bit_enable': True,
                                                                    'seq_num': '80000002',
                                                                    'type': 3}}},
                                                        '44.44.44.44 4.4.4.4': 
                                                            {'adv_router': '4.4.4.4',
                                                            'lsa_id': '44.44.44.44',
                                                            'ospfv2': 
                                                                {'body': 
                                                                    {'summary': 
                                                                        {'network_mask': '255.255.255.255',
                                                                        'topologies': 
                                                                            {0: 
                                                                                {'metric': 1,
                                                                                'mt_id': 0,
                                                                                'tos': 0}}}},
                                                                'header': 
                                                                    {'adv_router': '4.4.4.4',
                                                                    'age': 291,
                                                                    'checksum': '0x2b50',
                                                                    'length': 28,
                                                                    'lsa_id': '44.44.44.44',
                                                                    'option': 'None',
                                                                    'option_desc': 'No '
                                                                    'TOS-capability, '
                                                                    'DC',
                                                                    'routing_bit_enable': True,
                                                                    'seq_num': '80000001',
                                                                    'type': 3}}}}}}}}}}}}}}}}

    golden_output1 = {'execute.return_value': '''
        RP/0/0/CPU0:R2_ospf_xr#show ospf vrf all-inclusive database summary 
        Fri Nov  3 01:24:47.719 UTC


                    OSPF Router with ID (2.2.2.2) (Process ID 1)

                        Summary Net Link States (Area 0.0.0.0)

          LS age: 295
          Options: (No TOS-capability, DC)
          LS Type: Summary Links (Network)
          Link State ID: 4.4.4.4 (Summary Network Number)
          Advertising Router: 2.2.2.2
          LS Seq Number: 80000001
          Checksum: 0x9c87
          Length: 28
          Network Mask: /32
                TOS: 0  Metric: 65536 

          LS age: 520
          Options: (No TOS-capability, DC)
          LS Type: Summary Links (Network)
          Link State ID: 20.1.3.0 (Summary Network Number)
          Advertising Router: 2.2.2.2
          LS Seq Number: 80000001
          Checksum: 0xaa4a
          Length: 28
          Network Mask: /24
                TOS: 0  Metric: 65575 

          LS age: 519
          Options: (No TOS-capability, DC)
          LS Type: Summary Links (Network)
          Link State ID: 20.2.3.0 (Summary Network Number)
          Advertising Router: 2.2.2.2
          LS Seq Number: 80000002
          Checksum: 0xd0e
          Length: 28
          Network Mask: /24
                TOS: 0  Metric: 65535 

          LS age: 297
          Options: (No TOS-capability, DC)
          LS Type: Summary Links (Network)
          Link State ID: 20.2.4.0 (Summary Network Number)
          Advertising Router: 2.2.2.2
          LS Seq Number: 80000002
          Checksum: 0x218
          Length: 28
          Network Mask: /24
                TOS: 0  Metric: 65535 

          LS age: 294
          Options: (No TOS-capability, DC)
          LS Type: Summary Links (Network)
          Link State ID: 20.3.4.0 (Summary Network Number)
          Advertising Router: 2.2.2.2
          LS Seq Number: 80000002
          Checksum: 0xfd1a
          Length: 28
          Network Mask: /24
                TOS: 0  Metric: 65536 


                        Summary Net Link States (Area 1)

          LS age: 676
          Options: (No TOS-capability, DC)
          LS Type: Summary Links (Network)
          Link State ID: 2.2.2.2 (Summary Network Number)
          Advertising Router: 2.2.2.2
          LS Seq Number: 80000001
          Checksum: 0xfa31
          Length: 28
          Network Mask: /32
                TOS: 0  Metric: 1 

          Routing Bit Set on this LSA
          LS age: 531
          Options: (No TOS-capability, No DC)
          LS Type: Summary Links (Network)
          Link State ID: 3.3.3.3 (Summary Network Number)
          Advertising Router: 3.3.3.3
          LS Seq Number: 80000002
          Checksum: 0x8eb4
          Length: 28
          Network Mask: /32
                TOS: 0  Metric: 1 

          LS age: 675
          Options: (No TOS-capability, DC)
          LS Type: Summary Links (Network)
          Link State ID: 10.1.2.0 (Summary Network Number)
          Advertising Router: 2.2.2.2
          LS Seq Number: 80000001
          Checksum: 0xfc54
          Length: 28
          Network Mask: /24
                TOS: 0  Metric: 4294 

          LS age: 521
          Options: (No TOS-capability, No DC)
          LS Type: Summary Links (Network)
          Link State ID: 10.1.2.0 (Summary Network Number)
          Advertising Router: 3.3.3.3
          LS Seq Number: 80000002
          Checksum: 0x5655
          Length: 28
          Network Mask: /24
                TOS: 0  Metric: 151 

          Routing Bit Set on this LSA
          LS age: 531
          Options: (No TOS-capability, No DC)
          LS Type: Summary Links (Network)
          Link State ID: 10.1.3.0 (Summary Network Number)
          Advertising Router: 3.3.3.3
          LS Seq Number: 80000002
          Checksum: 0xf029
          Length: 28
          Network Mask: /24
                TOS: 0  Metric: 40 

          LS age: 675
          Options: (No TOS-capability, DC)
          LS Type: Summary Links (Network)
          Link State ID: 10.2.3.0 (Summary Network Number)
          Advertising Router: 2.2.2.2
          LS Seq Number: 80000001
          Checksum: 0x4601
          Length: 28
          Network Mask: /24
                TOS: 0  Metric: 222 

          LS age: 287
          Options: (No TOS-capability, No DC)
          LS Type: Summary Links (Network)
          Link State ID: 10.2.3.0 (Summary Network Number)
          Advertising Router: 3.3.3.3
          LS Seq Number: 80000003
          Checksum: 0x96a2
          Length: 28
          Network Mask: /24
                TOS: 0  Metric: 262 

          Routing Bit Set on this LSA
          LS age: 291
          Options: (No TOS-capability, DC)
          LS Type: Summary Links (Network)
          Link State ID: 44.44.44.44 (Summary Network Number)
          Advertising Router: 4.4.4.4
          LS Seq Number: 80000001
          Checksum: 0x2b50
          Length: 28
          Network Mask: /32
                TOS: 0  Metric: 1 
        '''}

    def test_show_ospf_vrf_all_inclusive_database_summary_full(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output1)
        obj = ShowOspfVrfAllInclusiveDatabaseSummary(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output1)

    def test_show_ospf_vrf_all_inclusive_database_summary_empty(self):
        self.maxDiff = None
        self.device = Mock(**self.empty_output)
        obj = ShowOspfVrfAllInclusiveDatabaseSummary(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()


# =================================================================
#  Unit test for 'show ospf vrf all-inclusive database opaque-area'
# =================================================================
class test_show_ospf_vrf_all_inclusive_database_opaque_area(unittest.TestCase):

    '''Unit test for "show ospf vrf all-inclusive database opaque-area" '''

    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output1 = {
        'vrf': 
            {'VRF1': {'address_family': {'ipv4': {'instance': {'1': {}}}}},
        'default': 
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
                                                                {'opaque': {}},
                                                            'header': 
                                                                {'adv_router': '1.1.1.1',
                                                                'age': 1427,
                                                                'checksum': '0x56d2',
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
                                                                {'opaque': {}},
                                                            'header': 
                                                                {'adv_router': '2.2.2.2',
                                                                'age': 653,
                                                                'checksum': '0x1c22',
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
                                                                'seq_num': '80000003',
                                                                'type': 10}}},
                                                    '1.0.0.0 3.3.3.3': 
                                                        {'adv_router': '3.3.3.3',
                                                        'lsa_id': '1.0.0.0',
                                                        'ospfv2': 
                                                            {'body': 
                                                                {'opaque': {}},
                                                            'header': 
                                                                {'adv_router': '3.3.3.3',
                                                                'age': 1175,
                                                                'checksum': '0x5eba',
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
                                                                            {'admin_group': '0',
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
                                                                                    'unreserved_bandwidth': 93750000}}}}}},
                                                            'header': 
                                                                {'adv_router': '1.1.1.1',
                                                                'age': 1427,
                                                                'checksum': '0x6586',
                                                                'length': 124,
                                                                'lsa_id': '1.0.0.1',
                                                                'opaque_id': 1,
                                                                'opaque_type': 1,
                                                                'option': 'None',
                                                                'option_desc': 'No '
                                                                'TOS-capability, '
                                                                'DC',
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
                                                                            {'admin_group': '0',
                                                                            'igp_metric': 1,
                                                                            'link_id': '10.1.2.1',
                                                                            'link_name': 'broadcast network',
                                                                            'link_type': 2,
                                                                            'local_if_ipv4_addrs': 
                                                                                {'10.1.2.1': {}},
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
                                                                                    'unreserved_bandwidth': 93750000}}}}}},
                                                            'header': 
                                                                {'adv_router': '1.1.1.1',
                                                                'age': 1427,
                                                                'checksum': '0xb43d',
                                                                'length': 124,
                                                                'lsa_id': '1.0.0.2',
                                                                'opaque_id': 2,
                                                                'opaque_type': 1,
                                                                'option': 'None',
                                                                'option_desc': 'No '
                                                                'TOS-capability, '
                                                                'DC',
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
                                                                            {'admin_group': '0',
                                                                            'link_id': '10.2.3.3',
                                                                            'link_name': 'broadcast network',
                                                                            'link_type': 2,
                                                                            'local_if_ipv4_addrs': 
                                                                                {'10.2.3.2': {}},
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
                                                                                    'unreserved_bandwidth': 93750000}}}}}},
                                                            'header': 
                                                                {'adv_router': '2.2.2.2',
                                                                'age': 242,
                                                                'checksum': '0xe492',
                                                                'length': 116,
                                                                'lsa_id': '1.0.0.37',
                                                                'opaque_id': 37,
                                                                'opaque_type': 1,
                                                                'option': 'None',
                                                                'option_desc': 'No '
                                                                'TOS-capability, '
                                                                'No '
                                                                'DC',
                                                                'seq_num': '80000004',
                                                                'type': 10}}},
                                                    '1.0.0.38 2.2.2.2': 
                                                        {'adv_router': '2.2.2.2',
                                                        'lsa_id': '1.0.0.38',
                                                        'ospfv2': 
                                                            {'body': 
                                                                {'opaque': 
                                                                    {'link_tlvs': 
                                                                        {1: 
                                                                            {'admin_group': '0',
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
                                                                                    'unreserved_bandwidth': 93750000}}}}}},
                                                            'header': 
                                                                {'adv_router': '2.2.2.2',
                                                                'age': 233,
                                                                'checksum': '0x2350',
                                                                'length': 116,
                                                                'lsa_id': '1.0.0.38',
                                                                'opaque_id': 38,
                                                                'opaque_type': 1,
                                                                'option': 'None',
                                                                'option_desc': 'No '
                                                                'TOS-capability, '
                                                                'No '
                                                                'DC',
                                                                'seq_num': '80000004',
                                                                'type': 10}}},
                                                    '1.0.0.39 2.2.2.2': 
                                                        {'adv_router': '2.2.2.2',
                                                        'lsa_id': '1.0.0.39',
                                                        'ospfv2': 
                                                            {'body': 
                                                                {'opaque': 
                                                                    {'link_tlvs': 
                                                                        {1: 
                                                                            {'admin_group': '0',
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
                                                                                    'unreserved_bandwidth': 93750000}}}}}},
                                                            'header': 
                                                                {'adv_router': '2.2.2.2',
                                                                'age': 232,
                                                                'checksum': '0x4239',
                                                                'length': 116,
                                                                'lsa_id': '1.0.0.39',
                                                                'opaque_id': 39,
                                                                'opaque_type': 1,
                                                                'option': 'None',
                                                                'option_desc': 'No '
                                                                'TOS-capability, '
                                                                'No '
                                                                'DC',
                                                                'seq_num': '80000004',
                                                                'type': 10}}},
                                                    '1.0.0.4 3.3.3.3': 
                                                        {'adv_router': '3.3.3.3',
                                                        'lsa_id': '1.0.0.4',
                                                        'ospfv2': 
                                                            {'body': 
                                                                {'opaque': 
                                                                    {'link_tlvs': 
                                                                        {1: 
                                                                            {'admin_group': '0',
                                                                            'extended_admin_group': 
                                                                                {'groups': 
                                                                                    {0: {'value': 0},
                                                                                    1: {'value': 0},
                                                                                    2: {'value': 0},
                                                                                    3: {'value': 0},
                                                                                    4: {'value': 0},
                                                                                    5: {'value': 0},
                                                                                    6: {'value': 0},
                                                                                    7: {'value': 0}},
                                                                                'length': 8},
                                                                            'igp_metric': 1,
                                                                            'link_id': '10.3.4.4',
                                                                            'link_name': 'broadcast network',
                                                                            'link_type': 2,
                                                                            'local_if_ipv4_addrs': 
                                                                                {'10.3.4.3': {}},
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
                                                                                    'unreserved_bandwidth': 93750000}}}}}},
                                                            'header': 
                                                                {'adv_router': '3.3.3.3',
                                                                'age': 1175,
                                                                'checksum': '0x915d',
                                                                'length': 160,
                                                                'lsa_id': '1.0.0.4',
                                                                'opaque_id': 4,
                                                                'opaque_type': 1,
                                                                'option': 'None',
                                                                'option_desc': 'No '
                                                                'TOS-capability, '
                                                                'DC',
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
                                                                            {'admin_group': '0',
                                                                            'extended_admin_group': 
                                                                                {'groups': 
                                                                                    {0: {'value': 0},
                                                                                    1: {'value': 0},
                                                                                    2: {'value': 0},
                                                                                    3: {'value': 0},
                                                                                    4: {'value': 0},
                                                                                    5: {'value': 0},
                                                                                    6: {'value': 0},
                                                                                    7: {'value': 0}},
                                                                                'length': 8},
                                                                            'igp_metric': 1,
                                                                            'link_id': '10.2.3.3',
                                                                            'link_name': 'broadcast network',
                                                                            'link_type': 2,
                                                                            'local_if_ipv4_addrs': 
                                                                                {'10.2.3.3': {}},
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
                                                                                    'unreserved_bandwidth': 93750000}}}}}},
                                                            'header': 
                                                                {'adv_router': '3.3.3.3',
                                                                'age': 1175,
                                                                'checksum': '0x5ec',
                                                                'length': 160,
                                                                'lsa_id': '1.0.0.6',
                                                                'opaque_id': 6,
                                                                'opaque_type': 1,
                                                                'option': 'None',
                                                                'option_desc': 'No '
                                                                'TOS-capability, '
                                                                'DC',
                                                                'seq_num': '80000002',
                                                                'type': 10}}}}}}}}}}}}}}}}

    golden_output1 = {'execute.return_value': '''
        RP/0/0/CPU0:R3_ospf_xr#show ospf vrf all-inclusive database opaque-area 
        Thu Nov  2 21:27:17.362 UTC

                    OSPF Router with ID (3.3.3.3) (Process ID 1)

                        Type-10 Opaque Link Area Link States (Area 0)

          LS age: 1427
          Options: (No TOS-capability, DC)
          LS Type: Opaque Area Link
          Link State ID: 1.0.0.0
          Opaque Type: 1
          Opaque ID: 0
          Advertising Router: 1.1.1.1
          LS Seq Number: 80000002
          Checksum: 0x56d2
          Length: 28

            MPLS TE router ID : 1.1.1.1

            Number of Links : 0

          LS age: 653
          Options: (No TOS-capability, No DC)
          LS Type: Opaque Area Link
          Link State ID: 1.0.0.0
          Opaque Type: 1
          Opaque ID: 0
          Advertising Router: 2.2.2.2
          LS Seq Number: 80000003
          Checksum: 0x1c22
          Length: 28

            MPLS TE router ID : 2.2.2.2

            Number of Links : 0

          LS age: 1175
          Options: (No TOS-capability, DC)
          LS Type: Opaque Area Link
          Link State ID: 1.0.0.0
          Opaque Type: 1
          Opaque ID: 0
          Advertising Router: 3.3.3.3
          LS Seq Number: 80000002
          Checksum: 0x5eba
          Length: 28

            MPLS TE router ID : 3.3.3.3

            Number of Links : 0

          LS age: 1427
          Options: (No TOS-capability, DC)
          LS Type: Opaque Area Link
          Link State ID: 1.0.0.1
          Opaque Type: 1
          Opaque ID: 1
          Advertising Router: 1.1.1.1
          LS Seq Number: 80000002
          Checksum: 0x6586
          Length: 124

            Link connected to Broadcast network
              Link ID : 10.1.4.4
              (all bandwidths in bytes/sec)
              Interface Address : 10.1.4.1
              Admin Metric : 1
              Maximum bandwidth : 125000000
              Maximum reservable bandwidth global: 93750000
              Number of Priority : 8
              Priority 0 :             93750000  Priority 1 :             93750000
              Priority 2 :             93750000  Priority 3 :             93750000
              Priority 4 :             93750000  Priority 5 :             93750000
              Priority 6 :             93750000  Priority 7 :             93750000
              Affinity Bit : 0
              IGP Metric : 1

            Number of Links : 1

          LS age: 1427
          Options: (No TOS-capability, DC)
          LS Type: Opaque Area Link
          Link State ID: 1.0.0.2
          Opaque Type: 1
          Opaque ID: 2
          Advertising Router: 1.1.1.1
          LS Seq Number: 80000002
          Checksum: 0xb43d
          Length: 124

            Link connected to Broadcast network
              Link ID : 10.1.2.1
              (all bandwidths in bytes/sec)
              Interface Address : 10.1.2.1
              Admin Metric : 1
              Maximum bandwidth : 125000000
              Maximum reservable bandwidth global: 93750000
              Number of Priority : 8
              Priority 0 :             93750000  Priority 1 :             93750000
              Priority 2 :             93750000  Priority 3 :             93750000
              Priority 4 :             93750000  Priority 5 :             93750000
              Priority 6 :             93750000  Priority 7 :             93750000
              Affinity Bit : 0
              IGP Metric : 1

            Number of Links : 1

          LS age: 1175
          Options: (No TOS-capability, DC)
          LS Type: Opaque Area Link
          Link State ID: 1.0.0.4
          Opaque Type: 1
          Opaque ID: 4
          Advertising Router: 3.3.3.3
          LS Seq Number: 80000002
          Checksum: 0x915d
          Length: 160

            Link connected to Broadcast network
              Link ID : 10.3.4.4
              (all bandwidths in bytes/sec)
              Interface Address : 10.3.4.3
              Admin Metric : 1
              Maximum bandwidth : 125000000
              Maximum reservable bandwidth global: 93750000
              Number of Priority : 8
              Priority 0 :             93750000  Priority 1 :             93750000
              Priority 2 :             93750000  Priority 3 :             93750000
              Priority 4 :             93750000  Priority 5 :             93750000
              Priority 6 :             93750000  Priority 7 :             93750000
              Affinity Bit : 0
              IGP Metric : 1
              Extended Administrative Group : Length: 8
               EAG[0]: 0
               EAG[1]: 0
               EAG[2]: 0
               EAG[3]: 0
               EAG[4]: 0
               EAG[5]: 0
               EAG[6]: 0
               EAG[7]: 0

            Number of Links : 1

          LS age: 1175
          Options: (No TOS-capability, DC)
          LS Type: Opaque Area Link
          Link State ID: 1.0.0.6
          Opaque Type: 1
          Opaque ID: 6
          Advertising Router: 3.3.3.3
          LS Seq Number: 80000002
          Checksum: 0x5ec
          Length: 160

            Link connected to Broadcast network
              Link ID : 10.2.3.3
              (all bandwidths in bytes/sec)
              Interface Address : 10.2.3.3
              Admin Metric : 1
              Maximum bandwidth : 125000000
              Maximum reservable bandwidth global: 93750000
              Number of Priority : 8
              Priority 0 :             93750000  Priority 1 :             93750000
              Priority 2 :             93750000  Priority 3 :             93750000
              Priority 4 :             93750000  Priority 5 :             93750000
              Priority 6 :             93750000  Priority 7 :             93750000
              Affinity Bit : 0
              IGP Metric : 1
              Extended Administrative Group : Length: 8
               EAG[0]: 0
               EAG[1]: 0
               EAG[2]: 0
               EAG[3]: 0
               EAG[4]: 0
               EAG[5]: 0
               EAG[6]: 0
               EAG[7]: 0

            Number of Links : 1

          LS age: 242
          Options: (No TOS-capability, No DC)
          LS Type: Opaque Area Link
          Link State ID: 1.0.0.37
          Opaque Type: 1
          Opaque ID: 37
          Advertising Router: 2.2.2.2
          LS Seq Number: 80000004
          Checksum: 0xe492
          Length: 116

            Link connected to Broadcast network
              Link ID : 10.2.3.3
              (all bandwidths in bytes/sec)
              Interface Address : 10.2.3.2
              Admin Metric : 1
              Maximum bandwidth : 125000000
              Maximum reservable bandwidth global: 93750000
              Number of Priority : 8
              Priority 0 :             93750000  Priority 1 :             93750000
              Priority 2 :             93750000  Priority 3 :             93750000
              Priority 4 :             93750000  Priority 5 :             93750000
              Priority 6 :             93750000  Priority 7 :             93750000
              Affinity Bit : 0

            Number of Links : 1

          LS age: 233
          Options: (No TOS-capability, No DC)
          LS Type: Opaque Area Link
          Link State ID: 1.0.0.38
          Opaque Type: 1
          Opaque ID: 38
          Advertising Router: 2.2.2.2
          LS Seq Number: 80000004
          Checksum: 0x2350
          Length: 116

            Link connected to Broadcast network
              Link ID : 10.2.4.4
              (all bandwidths in bytes/sec)
              Interface Address : 10.2.4.2
              Admin Metric : 1
              Maximum bandwidth : 125000000
              Maximum reservable bandwidth global: 93750000
              Number of Priority : 8
              Priority 0 :             93750000  Priority 1 :             93750000
              Priority 2 :             93750000  Priority 3 :             93750000
              Priority 4 :             93750000  Priority 5 :             93750000
              Priority 6 :             93750000  Priority 7 :             93750000
              Affinity Bit : 0

            Number of Links : 1

          LS age: 232
          Options: (No TOS-capability, No DC)
          LS Type: Opaque Area Link
          Link State ID: 1.0.0.39
          Opaque Type: 1
          Opaque ID: 39
          Advertising Router: 2.2.2.2
          LS Seq Number: 80000004
          Checksum: 0x4239
          Length: 116

            Link connected to Broadcast network
              Link ID : 10.1.2.1
              (all bandwidths in bytes/sec)
              Interface Address : 10.1.2.2
              Admin Metric : 1
              Maximum bandwidth : 125000000
              Maximum reservable bandwidth global: 93750000
              Number of Priority : 8
              Priority 0 :             93750000  Priority 1 :             93750000
              Priority 2 :             93750000  Priority 3 :             93750000
              Priority 4 :             93750000  Priority 5 :             93750000
              Priority 6 :             93750000  Priority 7 :             93750000
              Affinity Bit : 0

            Number of Links : 1

                    OSPF Router with ID (3.3.3.3) (Process ID 1, VRF VRF1)
        '''}

    def test_show_ospf_vrf_all_inclusive_database_opaque_area_full(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output1)
        obj = ShowOspfVrfAllInclusiveDatabaseOpaqueArea(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output1)

    def test_show_ospf_vrf_all_inclusive_database_opaque_area_empty(self):
        self.maxDiff = None
        self.device = Mock(**self.empty_output)
        obj = ShowOspfVrfAllInclusiveDatabaseOpaqueArea(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()



if __name__ == '__main__':
    unittest.main()
