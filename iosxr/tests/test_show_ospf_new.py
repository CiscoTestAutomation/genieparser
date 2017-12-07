
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
                                       ShowOspfVrfAllInclusiveNeighborDetail


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
                                    {'1': 
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
                                                'interface_type': 'BROADCAST',
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
                                                'process_id': 1,
                                                'retransmit_interval': 5,
                                                'router_id': '3.3.3.3',
                                                'state': 'BDR',
                                                'transmit_delay': 1,
                                                'wait_interval': 40},
                                            'OSPF_SL0': 
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
                                                'index': '2/2',
                                                'interface_type': 'SHAM_LINK',
                                                'ip_address': '0.0.0.0/0',
                                                'last_flood_scan_length': 1,
                                                'last_flood_scan_time_msec': 0,
                                                'line_protocol': True,
                                                'ls_ack_list': 'current',
                                                'ls_ack_list_length': 0,
                                                'high_water_mark': 9,
                                                'max_flood_scan_length': 7,
                                                'max_flood_scan_time_msec': 0,
                                                'multi_area_intf_count': 0,
                                                'name': 'OSPF_SL0',
                                                'nbr_count': 0,
                                                'next': '0(0)/0(0)',
                                                'num_nbrs_suppress_hello': 0,
                                                'passive': False,
                                                'process_id': 1,
                                                'retransmit_interval': 5,
                                                'router_id': '3.3.3.3',
                                                'wait_interval': 13}}}}}}}}},
            'default': 
                {'address_family': 
                    {'ipv4': 
                        {'instance': 
                            {'1': 
                                {'areas': 
                                    {'0': 
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
                                                'interface_type': 'BROADCAST',
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
                                                'process_id': 1,
                                                'retransmit_interval': 5,
                                                'router_id': '3.3.3.3',
                                                'state': 'BDR',
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
                                                'interface_type': 'BROADCAST',
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
                                                'process_id': 1,
                                                'retransmit_interval': 5,
                                                'router_id': '3.3.3.3',
                                                'state': 'DR',
                                                'transmit_delay': 1,
                                                'wait_interval': 40},
                                            'Loopback0': 
                                                {'bfd': 
                                                    {'enable': False},
                                                'cost': 1,
                                                'demand_circuit': False,
                                                'enable': True,
                                                'interface_type': 'LOOPBACK',
                                                'ip_address': '3.3.3.3/32',
                                                'line_protocol': True,
                                                'name': 'Loopback0',
                                                'process_id': 1,
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
                                                'interface_type': 'POINT_TO_POINT',
                                                'ip_address': '0.0.0.0/0',
                                                'last_flood_scan_length': 0,
                                                'last_flood_scan_time_msec': 0,
                                                'line_protocol': True,
                                                'ls_ack_list': 'current',
                                                'ls_ack_list_length': 0,
                                                'high_water_mark': 0,
                                                'max_flood_scan_length': 0,
                                                'max_flood_scan_time_msec': 0,
                                                'multi_area_intf_count': 0,
                                                'name': 'tunnel-te31',
                                                'nbr_count': 0,
                                                'next': '0(0)/0(0)',
                                                'num_nbrs_suppress_hello': 0,
                                                'passive': True,
                                                'process_id': 1,
                                                'retransmit_interval': 5,
                                                'router_id': '3.3.3.3',
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

    def test_full(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output1)
        obj = ShowOspfVrfAllInclusiveInterface(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output1)

    def test_empty(self):
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
                                    {'1': 
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
                                                        'state': 'FULL'}}}}}},
                                'total_neighbor_count': 1}}}}},
            'default': 
                {'address_family': 
                    {'ipv4': 
                        {'instance': 
                            {'1': 
                                {'areas': 
                                    {'0': 
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
                                                        'state': 'FULL'}}},
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
                                                        'state': 'FULL'}}}}}},
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

    def test_full(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output1)
        obj = ShowOspfVrfAllInclusiveNeighborDetail(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output1)

    def test_empty(self):
        self.maxDiff = None
        self.device = Mock(**self.empty_output)
        obj = ShowOspfVrfAllInclusiveNeighborDetail(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()



if __name__ == '__main__':
    unittest.main()