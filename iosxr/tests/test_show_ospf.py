import re
import unittest
from unittest.mock import Mock

from ats.topology import Device
from xbu_shared.genie.ops.ops.base import Base
from xbu_shared.parser.iosxr.show_ospf import ShowOspfNeighborDetail, \
    ShowOspf, ShowOspfDatabase, ShowOspfInterface, \
    ShowOspfNeighborDetailVrfAll, ShowOspfVrfAll, \
    ShowOspfDatabaseVrfAll, ShowOspfInterfaceVrfAll

class test_show_ospf(unittest.TestCase):
    device = Device(name='aDevice')
    device1 = Device(name='bDevice')
    empty_output = {'execute.return_value': ''}
    golden_parsed_output = {'process_id': {'100': {'vrf': {'default': {'area': {'BACKBONE(0)': {'active_interfaces': '1',
                                                                     'interfaces_in_this_area': '1'}},
                                            'id': '192.0.0.2',
                                            'nsf': 'disabled',
                                            'nsr': 'Enabled',
                                            'num_of_areas': '1',
                                            'num_of_normal_areas': '1',
                                            'num_of_nssa_areas': '0',
                                            'num_of_stub_areas': '0'}}},
                '200': {'vrf': {'default': {'id': '0.0.0.0',
                                            'nsf': 'disabled',
                                            'nsr': 'Enabled',
                                            'num_of_areas': '0',
                                            'num_of_normal_areas': '0',
                                            'num_of_nssa_areas': '0',
                                            'num_of_stub_areas': '0'}}}}}

    golden_output = {'execute.return_value': '''
show ospf
Wed Nov 23 14:11:42.781 PST

 Routing Process "ospf 100" with ID 192.0.0.2
 Role: Primary Active
 NSR (Non-stop routing) is Enabled
 Supports only single TOS(TOS0) routes
 Supports opaque LSA
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
 Number of external LSA 0. Checksum Sum 00000000
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
	Number of interfaces in this area is 1
	SPF algorithm executed 5 times
	Number of LSA 3.  Checksum Sum 0x01057e
	Number of opaque link LSA 0.  Checksum Sum 00000000
	Number of DCbitless LSA 0
	Number of indication LSA 0
	Number of DoNotAge LSA 0
	Flood list length 0
	Number of LFA enabled interfaces 0, LFA revision 0
	Number of Per Prefix LFA enabled interfaces 0
	Number of neighbors forming in staggered mode 0, 1 full

 Routing Process "ospf 200" with ID 0.0.0.0
 Role: Primary Active
 NSR (Non-stop routing) is Enabled
 Supports only single TOS(TOS0) routes
 Supports opaque LSA
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
    Number of neighbors forming: 0, 0 full
 Maximum number of configured interfaces 1024
 Number of external LSA 0. Checksum Sum 00000000
 Number of opaque AS LSA 0. Checksum Sum 00000000
 Number of DCbitless external and opaque AS LSA 0
 Number of DoNotAge external and opaque AS LSA 0
 Number of areas in this router is 0. 0 normal 0 stub 0 nssa
 External flood list length 0
 SNMP trap is enabled
 LSD connected, registered, bound, revision 1
 Segment Routing Global Block default (16000-23999), not allocated
 Strict-SPF capability is enabled
'''}

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        ip_ospf = ShowOspf(device=self.device)
        parsed_output = ip_ospf.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output)

    def test_empty(self):
        self.device1 = Mock(**self.empty_output)
        ip_ospf = ShowOspf(device=self.device1)
        with self.assertRaises(Exception):
            parsed_output = ip_ospf.parse()

class test_show_ospf_interface(unittest.TestCase):

    device = Device(name='aDevice')
    device1 = Device(name='bDevice')
    empty_output = {'execute.return_value': ''}
    golden_output = {'execute.return_value': '''show ospf interface
Wed Nov 23 14:11:33.432 PST

Interfaces for OSPF 100

GigabitEthernet0/0/0/0 is up, line protocol is up
  Internet Address 192.0.0.2/30, Area 0
  Process ID 100, Router ID 192.0.0.2, Network Type BROADCAST, Cost: 1
  Transmit Delay is 1 sec, State DR, Priority 1, MTU 1500, MaxPktSz 1500
  Designated Router (ID) 192.0.0.2, Interface address 192.0.0.2
  Backup Designated router (ID) 192.0.0.1, Interface address 192.0.0.1
  Timer intervals configured, Hello 10, Dead 40, Wait 40, Retransmit 5
    Hello due in 00:00:08:333
  Index 1/1, flood queue length 0
  Next 0(0)/0(0)
  Last flood scan length is 2, maximum is 2
  Last flood scan time is 0 msec, maximum is 0 msec
  LS Ack List: current length 0, high water mark 1
  Neighbor Count is 1, Adjacent neighbor count is 1
    Adjacent with neighbor 192.0.0.1  (Backup Designated Router)
  Suppress hello for 0 neighbor(s)
  Multi-area interface Count is 0
'''}

    golden_parsed_output =  {'intf': {'GigabitEthernet0/0/0/0': {'area': '0',
                                     'backup_designated_router_address': '192.0.0.1',
                                     'backup_designated_router_id': '192.0.0.1',
                                     'cost': '1',
                                     'dead_timer': '40',
                                     'designated_router_address': '192.0.0.2',
                                     'designated_router_id': '192.0.0.2',
                                     'hello_timer': '10',
                                     'intf_state': 'up',
                                     'ip_address': '192.0.0.2',
                                     'max_pkt_size': '1500',
                                     'mtu': '1500',
                                     'neighbor': '192.0.0.1',
                                     'network_type': 'BROADCAST',
                                     'priority': '1',
                                     'process_id': '100',
                                     'retransmit_timer': '5',
                                     'rid': '192.0.0.2',
                                     'state': 'DR',
                                     't_delay': '1 sec',
                                     'vrf': 'default',
                                     'wait_timer': '40'}},
 'intfs_all': ['GigabitEthernet0/0/0/0'],
 'intfs_down': []}

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        ip_ospf = ShowOspfInterface(device=self.device)
        parsed_output = ip_ospf.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output)
        self.assertNotEqual(parsed_output,'')

    def test_empty(self):
        self.device1 = Mock(**self.empty_output)
        ip_ospf = ShowOspfInterface(device=self.device1)
        with self.assertRaises(Exception):
            parsed_output = ip_ospf.parse()

class test_show_ospf_neighbor(unittest.TestCase):

    device = Device(name='aDevice')
    device1 = Device(name='bDevice')
    empty_output = {'execute.return_value': ''}
    golden_output = {'execute.return_value': '''show ospf neighbor detail
Wed Nov 23 14:11:10.023 PST

* Indicates MADJ interface
# Indicates Neighbor awaiting BFD session up

Neighbors for OSPF 100

 Neighbor 192.0.0.1, interface address 192.0.0.1
    In the area 0 via interface GigabitEthernet0/0/0/0
    Neighbor priority is 1, State is FULL, 6 state changes
    DR is 192.0.0.2 BDR is 192.0.0.1
    Options is 0x52
    LLS Options is 0x1 (LR)
    Dead timer due in 00:00:31
    Neighbor is up for 00:08:52
    Number of DBD retrans during last exchange 0
    Index 1/1, retransmission queue length 0, number of retransmission 1
    First 0(0)/0(0) Next 0(0)/0(0)
    Last retransmission scan length is 1, maximum is 1
    Last retransmission scan time is 0 msec, maximum is 0 msec
    LS Ack list: NSR-sync pending 0, high water mark 0


'''}

    golden_parsed_output = {'intf': {'GigabitEthernet0/0/0/0': {'area': '0',
                                     'bdr': '192.0.0.1',
                                     'dr': '192.0.0.2',
                                     'interface_address': '192.0.0.1',
                                     'neigh_priority': '1',
                                     'neighbor': '192.0.0.1',
                                     'process_id': '100',
                                     'state': 'FULL',
                                     'state_changes': '6',
                                     'uptime': '00:08:52',
                                     'vrf': 'default'}},
 'intf_list': ['GigabitEthernet0/0/0/0']}

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        ip_ospf = ShowOspfNeighborDetail(device=self.device)
        parsed_output = ip_ospf.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output)

    def test_empty(self):
        self.device1 = Mock(**self.empty_output)
        ip_ospf = ShowOspfNeighborDetail(device=self.device1)
        with self.assertRaises(Exception):
            parsed_output = ip_ospf.parse()

class test_show_ospf_database(unittest.TestCase):

    device = Device(name='aDevice')
    device1 = Device(name='bDevice')
    empty_output = {'execute.return_value': ''}
    golden_output = {'execute.return_value': '''
           show ospf database
Wed Nov 23 14:11:23.732 PST


            OSPF Router with ID (192.0.0.2) (Process ID 100)

		Router Link States (Area 0)

Link ID         ADV Router      Age         Seq#       Checksum Link count
192.0.0.1       192.0.0.1       510         0x80000002 0x00f831 1
192.0.0.2       192.0.0.2       509         0x80000002 0x00f630 1

		Net Link States (Area 0)

Link ID         ADV Router      Age         Seq#       Checksum
192.0.0.2       192.0.0.2       509         0x80000001 0x0090a2


            OSPF Router with ID (0.0.0.0) (Process ID 200)
'''}

    golden_parsed_output = {'process_id': {'100': {'vrf': {'default': {'area': {'0': {'network_link': {'ls_id': {'192.0.0.2': {'advrouter': {'192.0.0.2': {'age': '509',
                                                                                                                                'cksum': '0x0090a2',
                                                                                                                                'seq': '0x80000001'}}}}},
                                                           'router_link': {'ls_id': {'192.0.0.1': {'advrouter': {'192.0.0.1': {'age': '510',
                                                                                                                               'cksum': '0x00f831',
                                                                                                                               'lnkcnt': '1',
                                                                                                                               'seq': '0x80000002'}}},
                                                                                     '192.0.0.2': {'advrouter': {'192.0.0.2': {'age': '509',
                                                                                                                               'cksum': '0x00f630',
                                                                                                                               'lnkcnt': '1',
                                                                                                                               'seq': '0x80000002'}}}}}}},
                                            'router_id': '192.0.0.2'}}},
                '200': {'vrf': {'default': {'router_id': '0.0.0.0'}}}}}

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        ip_ospf = ShowOspfDatabase(device=self.device)
        parsed_output = ip_ospf.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output)

    def test_empty(self):
        self.device1 = Mock(**self.empty_output)
        ip_ospf = ShowOspfDatabase(device=self.device1)
        with self.assertRaises(Exception):
            parsed_output = ip_ospf.parse()

class test_show_ospf_vrf_all(unittest.TestCase):
    device = Device(name='aDevice')
    device1 = Device(name='bDevice')
    empty_output = {'execute.return_value': ''}
    golden_parsed_output = {'process_id': {'200': {'vrf': {'test': {'area': {'BACKBONE(0)': {'active_interfaces': '2',
                                                                  'interfaces_in_this_area': '2'}},
                                         'id': '192.0.0.9',
                                         'nsf': 'enabled',
                                         'nsr': 'Enabled',
                                         'num_of_areas': '1',
                                         'num_of_normal_areas': '1',
                                         'num_of_nssa_areas': '0',
                                         'num_of_stub_areas': '0',
                                         'ospf_rtr_type': 'area border '
                                                          'router'}}}}}

    golden_output = {'execute.return_value': '''
show ospf vrf all
Wed Nov 23 14:23:19.546 PST

 VRF test in Routing Process "ospf 200" with ID 192.0.0.9
 Role: Primary Active
 NSR (Non-stop routing) is Enabled
 Supports only single TOS(TOS0) routes
 Supports opaque LSA
 It is an area border router
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
 Number of external LSA 0. Checksum Sum 00000000
 Number of opaque AS LSA 0. Checksum Sum 00000000
 Number of DCbitless external and opaque AS LSA 0
 Number of DoNotAge external and opaque AS LSA 0
 Number of areas in this router is 1. 1 normal 0 stub 0 nssa
 External flood list length 0
 Non-Stop Forwarding enabled
 SNMP trap is disabled
 LSD connected, registered, bound, revision 1
 Segment Routing Global Block default (16000-23999), not allocated
 Strict-SPF capability is enabled
    Area BACKBONE(0)
	Number of interfaces in this area is 2
	SPF algorithm executed 5 times
	Number of LSA 3.  Checksum Sum 0x015b2c
	Number of opaque link LSA 0.  Checksum Sum 00000000
	Number of DCbitless LSA 0
	Number of indication LSA 0
	Number of DoNotAge LSA 0
	Flood list length 0
	Number of LFA enabled interfaces 0, LFA revision 0
	Number of Per Prefix LFA enabled interfaces 0
	Number of neighbors forming in staggered mode 0, 1 full
'''}

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        ip_ospf = ShowOspfVrfAll(device=self.device)
        parsed_output = ip_ospf.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output)

    def test_empty(self):
        self.device1 = Mock(**self.empty_output)
        ip_ospf = ShowOspfVrfAll(device=self.device1)
        with self.assertRaises(Exception):
            parsed_output = ip_ospf.parse()

class test_show_ospf_interface_vrf_all(unittest.TestCase):

    device = Device(name='aDevice')
    device1 = Device(name='bDevice')
    empty_output = {'execute.return_value': ''}
    golden_output = {'execute.return_value': '''show ospf vrf all interface
Wed Nov 23 14:23:28.346 PST

Interfaces for OSPF 200, VRF test

Loopback100 is up, line protocol is up
  Internet Address 192.0.0.9/32, Area 0
  Process ID 200, VRF test, Router ID 192.0.0.9, Network Type LOOPBACK, Cost: 1
  Loopback interface is treated as a stub Host
GigabitEthernet0/0/0/2 is up, line protocol is up
  Internet Address 192.0.0.6/30, Area 0
  Process ID 200, VRF test, Router ID 192.0.0.9, Network Type BROADCAST, Cost: 1
  Transmit Delay is 1 sec, State DR, Priority 1, MTU 1500, MaxPktSz 1500
  Designated Router (ID) 192.0.0.9, Interface address 192.0.0.6
  Backup Designated router (ID) 192.0.0.8, Interface address 192.0.0.5
  Timer intervals configured, Hello 10, Dead 40, Wait 40, Retransmit 5
  Non-Stop Forwarding (NSF) enabled
    Hello due in 00:00:00:372
  Index 2/2, flood queue length 0
  Next 0(0)/0(0)
  Last flood scan length is 1, maximum is 1
  Last flood scan time is 0 msec, maximum is 0 msec
  LS Ack List: current length 0, high water mark 1
  Neighbor Count is 1, Adjacent neighbor count is 1
    Adjacent with neighbor 192.0.0.8  (Backup Designated Router)
  Suppress hello for 0 neighbor(s)
  Multi-area interface Count is 0
'''}

    golden_parsed_output = {'intf': {'GigabitEthernet0/0/0/2': {'area': '0',
                                     'backup_designated_router_address': '192.0.0.5',
                                     'backup_designated_router_id': '192.0.0.8',
                                     'cost': '1',
                                     'dead_timer': '40',
                                     'designated_router_address': '192.0.0.6',
                                     'designated_router_id': '192.0.0.9',
                                     'hello_timer': '10',
                                     'intf_state': 'up',
                                     'ip_address': '192.0.0.6',
                                     'max_pkt_size': '1500',
                                     'mtu': '1500',
                                     'neighbor': '192.0.0.8',
                                     'network_type': 'BROADCAST',
                                     'priority': '1',
                                     'process_id': '200',
                                     'retransmit_timer': '5',
                                     'rid': '192.0.0.9',
                                     'state': 'DR',
                                     't_delay': '1 sec',
                                     'vrf': 'test',
                                     'wait_timer': '40'},
          'Loopback100': {'area': '0',
                          'cost': '1',
                          'intf_state': 'up',
                          'ip_address': '192.0.0.9',
                          'network_type': 'LOOPBACK',
                          'process_id': '200',
                          'rid': '192.0.0.9',
                          'vrf': 'test'}},
 'intfs_all': ['Loopback100', 'GigabitEthernet0/0/0/2'],
 'intfs_down': []}

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        ip_ospf = ShowOspfInterfaceVrfAll(device=self.device)
        parsed_output = ip_ospf.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output)
        self.assertNotEqual(parsed_output,'')

    def test_empty(self):
        self.device1 = Mock(**self.empty_output)
        ip_ospf = ShowOspfInterfaceVrfAll(device=self.device1)
        with self.assertRaises(Exception):
            parsed_output = ip_ospf.parse()

class test_show_ospf_neighbor_vrf_all(unittest.TestCase):

    device = Device(name='aDevice')
    device1 = Device(name='bDevice')
    empty_output = {'execute.return_value': ''}
    golden_output = {'execute.return_value': '''show ospf vrf all neighbor detail
Wed Nov 23 14:23:35.225 PST

* Indicates MADJ interface
# Indicates Neighbor awaiting BFD session up

Neighbors for OSPF 200, VRF test

 Neighbor 192.0.0.8, interface address 192.0.0.5
    In the area 0 via interface GigabitEthernet0/0/0/2
    Neighbor priority is 1, State is FULL, 6 state changes
    DR is 192.0.0.6 BDR is 192.0.0.5
    Options is 0x52
    LLS Options is 0x1 (LR)
    Dead timer due in 00:00:34
    Neighbor is up for 00:20:00
    Number of DBD retrans during last exchange 0
    Index 1/1, retransmission queue length 0, number of retransmission 1
    First 0(0)/0(0) Next 0(0)/0(0)
    Last retransmission scan length is 1, maximum is 1
    Last retransmission scan time is 0 msec, maximum is 0 msec
    LS Ack list: NSR-sync pending 0, high water mark 0


Total neighbor count: 1
'''}

    golden_parsed_output = {'intf': {'GigabitEthernet0/0/0/2': {'area': '0',
                                     'bdr': '192.0.0.5',
                                     'dr': '192.0.0.6',
                                     'interface_address': '192.0.0.5',
                                     'neigh_priority': '1',
                                     'neighbor': '192.0.0.8',
                                     'process_id': '200',
                                     'state': 'FULL',
                                     'state_changes': '6',
                                     'uptime': '00:20:00',
                                     'vrf': 'test'}},
 'intf_list': ['GigabitEthernet0/0/0/2']}


    def test_golden(self):
        self.device = Mock(**self.golden_output)
        ip_ospf = ShowOspfNeighborDetailVrfAll(device=self.device)
        parsed_output = ip_ospf.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output)

    def test_empty(self):
        self.device1 = Mock(**self.empty_output)
        ip_ospf = ShowOspfNeighborDetailVrfAll(device=self.device1)
        with self.assertRaises(Exception):
            parsed_output = ip_ospf.parse()

class test_show_ospf_database_vrf_all(unittest.TestCase):

    device = Device(name='aDevice')
    device1 = Device(name='bDevice')
    empty_output = {'execute.return_value': ''}
    golden_output = {'execute.return_value': '''
show ospf vrf all database
Wed Nov 23 14:23:40.515 PST


            OSPF Router with ID (192.0.0.9) (Process ID 200, VRF test)

		Router Link States (Area 0)

Link ID         ADV Router      Age         Seq#       Checksum Link count
192.0.0.8       192.0.0.8       1169        0x80000002 0x00999f 2
192.0.0.9       192.0.0.9       1168        0x80000002 0x00ad87 2

		Net Link States (Area 0)

Link ID         ADV Router      Age         Seq#       Checksum
192.0.0.6       192.0.0.9       1168        0x80000001 0x00e633
'''}

    golden_parsed_output = {'process_id': {'200': {'vrf': {'test': {'area': {'0': {'network_link': {'ls_id': {'192.0.0.6': {'advrouter': {'192.0.0.9': {'age': '1168',
                                                                                                                             'cksum': '0x00e633',
                                                                                                                             'seq': '0x80000001'}}}}},
                                                        'router_link': {'ls_id': {'192.0.0.8': {'advrouter': {'192.0.0.8': {'age': '1169',
                                                                                                                            'cksum': '0x00999f',
                                                                                                                            'lnkcnt': '2',
                                                                                                                            'seq': '0x80000002'}}},
                                                                                  '192.0.0.9': {'advrouter': {'192.0.0.9': {'age': '1168',
                                                                                                                            'cksum': '0x00ad87',
                                                                                                                            'lnkcnt': '2',
                                                                                                                            'seq': '0x80000002'}}}}}}},
                                         'router_id': '192.0.0.9'}}}}}


    def test_golden(self):
        self.device = Mock(**self.golden_output)
        ip_ospf = ShowOspfDatabaseVrfAll(device=self.device)
        parsed_output = ip_ospf.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output)

    def test_empty(self):
        self.device1 = Mock(**self.empty_output)
        ip_ospf = ShowOspfDatabaseVrfAll(device=self.device1)
        with self.assertRaises(Exception):
            parsed_output = ip_ospf.parse()

if __name__ == '__main__':
    unittest.main()
