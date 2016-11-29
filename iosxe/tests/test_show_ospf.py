import re
import unittest
from unittest.mock import Mock

from ats.topology import Device
from xbu_shared.genie.ops.ops.base import Base
from xbu_shared.parser.iosxe.show_ospf import ShowIpOspfNeighborDetail,\
                                              ShowIpOspf, \
                                              ShowIpOspfDatabase, \
                                              ShowIpOspfInterface


class test_show_ip_ospf(unittest.TestCase):
    device = Device(name='aDevice')
    device1 = Device(name='bDevice')
    empty_output = {'execute.return_value': ''}
    golden_parsed_output = {'process_id': {'100': {'vrf': {'default': {'area': {'BACKBONE(0)': {'interfaces_in_this_area': '1'}},
                                        'id': '192.0.0.1',
                                        'num_of_areas': '1',
                                        'num_of_normal_areas': '1',
                                        'num_of_nssa_areas': '0',
                                        'num_of_stub_areas': '0',
                                        'reference_bandwidth': '100 '
                                                               'mbps'}}},
            '200': {'vrf': {'test': {'area': {'BACKBONE(0)': {'interfaces_in_this_area': '2',
                                                              'loopback_interfaces': '1'}},
                                     'id': '192.0.0.8',
                                     'num_of_areas': '1',
                                     'num_of_normal_areas': '1',
                                     'num_of_nssa_areas': '0',
                                     'num_of_stub_areas': '0',
                                     'ospf_rtr_type': 'area border '
                                                      'router',
                                     'reference_bandwidth': '1000 '
                                                            'mbps'}}}}}

    golden_parsed_output_1 = {'process_id': {'100': {'vrf': {'default': {'area': {'BACKBONE(0)': {'interfaces_in_this_area': '1'}},
                                        'id': '192.0.0.1',
                                        'num_of_areas': '1',
                                        'num_of_normal_areas': '1',
                                        'num_of_nssa_areas': '0',
                                        'num_of_stub_areas': '0',
                                        'reference_bandwidth': '100 '
                                                               'mbps'}}}}}


    golden_output = {'execute.return_value': '''
 Routing Process "ospf 100" with ID 192.0.0.1
 Start time: 22:46:26.157, Time elapsed: 00:42:37.847
 Supports only single TOS(TOS0) routes
 Supports opaque LSA
 Supports Link-local Signaling (LLS)
 Supports area transit capability
 Supports NSSA (compatible with RFC 3101)
 Supports Database Exchange Summary List Optimization (RFC 5243)
 Event-log enabled, Maximum number of events: 1000, Mode: cyclic
 Router is not originating router-LSAs with maximum metric
 Initial SPF schedule delay 5000 msecs
 Minimum hold time between two consecutive SPFs 10000 msecs
 Maximum wait time between two consecutive SPFs 10000 msecs
 Incremental-SPF disabled
 Minimum LSA interval 5 secs
 Minimum LSA arrival 1000 msecs
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
 IETF NSF helper support enabled
 Cisco NSF helper support enabled
 Reference bandwidth unit is 100 mbps
    Area BACKBONE(0)
        Number of interfaces in this area is 1
	Area has no authentication
	SPF algorithm last executed 00:41:42.627 ago
	SPF algorithm executed 3 times
	Area ranges are
	Number of LSA 3. Checksum Sum 0x026B0F
	Number of opaque link LSA 0. Checksum Sum 0x000000
	Number of DCbitless LSA 0
	Number of indication LSA 0
	Number of DoNotAge LSA 0
	Flood list length 0

 Routing Process "ospf 200" with ID 192.0.0.8
   Domain ID type 0x0005, value 0.0.0.200
 Start time: 22:47:31.592, Time elapsed: 00:41:32.412
 Supports only single TOS(TOS0) routes
 Supports opaque LSA
 Supports Link-local Signaling (LLS)
 Supports area transit capability
 Supports NSSA (compatible with RFC 3101)
 Supports Database Exchange Summary List Optimization (RFC 5243)
 Connected to MPLS VPN Superbackbone, VRF test
 Event-log disabled
 It is an area border router
 Router is not originating router-LSAs with maximum metric
 Initial SPF schedule delay 5000 msecs
 Minimum hold time between two consecutive SPFs 10000 msecs
 Maximum wait time between two consecutive SPFs 10000 msecs
 Incremental-SPF disabled
 Minimum LSA interval 5 secs
 Minimum LSA arrival 1000 msecs
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
 Non-Stop Forwarding enabled
    Router is not operating in SSO mode
    Global RIB has not converged yet
 IETF NSF helper support enabled
 Cisco NSF helper support enabled
 Reference bandwidth unit is 1000 mbps
    Area BACKBONE(0)
        Number of interfaces in this area is 2 (1 loopback)
	Area has no authentication
	SPF algorithm last executed 00:40:29.806 ago
	SPF algorithm executed 4 times
	Area ranges are
	Number of LSA 3. Checksum Sum 0x021567

	Number of opaque link LSA 0. Checksum Sum 0x000000
	Number of DCbitless LSA 0
	Number of indication LSA 0
	Number of DoNotAge LSA 0
	Flood list length 0
'''}


    golden_output_1 = {'execute.return_value': '''Routing Process "ospf 100" with ID 192.0.0.1
 Start time: 1d00h, Time elapsed: 00:00:11.077
 Supports only single TOS(TOS0) routes
 Supports opaque LSA
 Supports Link-local Signaling (LLS)
 Supports area transit capability
 Supports NSSA (compatible with RFC 3101)
 Supports Database Exchange Summary List Optimization (RFC 5243)
 Event-log enabled, Maximum number of events: 1000, Mode: cyclic
 Router is not originating router-LSAs with maximum metric
 Initial SPF schedule delay 5000 msecs
 Minimum hold time between two consecutive SPFs 10000 msecs
 Maximum wait time between two consecutive SPFs 10000 msecs
 Incremental-SPF disabled
 Minimum LSA interval 5 secs
 Minimum LSA arrival 1000 msecs
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
 IETF NSF helper support enabled
 Cisco NSF helper support enabled
 Reference bandwidth unit is 100 mbps
    Area BACKBONE(0) (Inactive)
        Number of interfaces in this area is 1
	area has no authentication
	SPF algorithm last executed 00:00:05.286 ago
	SPF algorithm executed 1 times
	area ranges are
	Number of LSA 1. Checksum Sum 0x00638A
	Number of opaque link LSA 0. Checksum Sum 0x000000
	Number of DCbitless LSA 0
	Number of indication LSA 0
	Number of DoNotAge LSA 0
	Flood list length 0'''}

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        ip_ospf = ShowIpOspf(device=self.device)
        parsed_output = ip_ospf.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output)
        self.assertNotEqual(parsed_output,self.golden_parsed_output_1)

    def test_golden_1(self):
        self.device = Mock(**self.golden_output_1)
        ip_ospf = ShowIpOspf(device=self.device)
        parsed_output = ip_ospf.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output_1)
        self.assertNotEqual(parsed_output,self.golden_parsed_output)

    def test_empty(self):
        self.device1 = Mock(**self.empty_output)
        ip_ospf = ShowIpOspf(device=self.device1)
        with self.assertRaises(Exception):
            parsed_output = ip_ospf.parse()

class test_show_ip_ospf_interface(unittest.TestCase):

    device = Device(name='aDevice')
    device1 = Device(name='bDevice')
    empty_output = {'execute.return_value': ''}
    golden_output = {'execute.return_value': '''show ip ospf interface
GigabitEthernet3 is up, line protocol is up
  Internet Address 192.0.0.1/30, Area 0, Attached via Interface Enable
  Process ID 100, Router ID 192.0.0.1, Network Type BROADCAST, Cost: 1
  Topology-MTID    Cost    Disabled    Shutdown      Topology Name
        0           1         no          no            Base
  Enabled by interface config, including secondary ip addresses
  Transmit Delay is 1 sec, State BDR, Priority 1
  Designated Router (ID) 192.0.0.2, Interface address 192.0.0.2
  Backup Designated router (ID) 192.0.0.1, Interface address 192.0.0.1
  Timer intervals configured, Hello 10, Dead 40, Wait 40, Retransmit 5
    oob-resync timeout 40
    Hello due in 00:00:05
  Supports Link-local Signaling (LLS)
  Cisco NSF helper support enabled
  IETF NSF helper support enabled
  Can be protected by per-prefix Loop-Free FastReroute
  Can be used for per-prefix Loop-Free FastReroute repair paths
  Not Protected by per-prefix TI-LFA
  Index 1/1/1, flood queue length 0
  Next 0x0(0)/0x0(0)/0x0(0)
  Last flood scan length is 1, maximum is 1
  Last flood scan time is 0 msec, maximum is 0 msec
  Neighbor Count is 1, Adjacent neighbor count is 1
    Adjacent with neighbor 192.0.0.2  (Designated Router)
  Suppress hello for 0 neighbor(s)
Loopback100 is up, line protocol is up
  Internet Address 192.0.0.8/32, Area 0, Attached via Interface Enable
  Process ID 200, Router ID 192.0.0.8, Network Type LOOPBACK, Cost: 1
  Topology-MTID    Cost    Disabled    Shutdown      Topology Name
        0           1         no          no            Base
  Enabled by interface config, including secondary ip addresses
  Loopback interface is treated as a stub Host
GigabitEthernet4 is up, line protocol is up
  Internet Address 192.0.0.5/30, Area 0, Attached via Interface Enable
  Process ID 200, Router ID 192.0.0.8, Network Type BROADCAST, Cost: 1
  Topology-MTID    Cost    Disabled    Shutdown      Topology Name
        0           1         no          no            Base
  Enabled by interface config, including secondary ip addresses
  Transmit Delay is 1 sec, State BDR, Priority 1
  Designated Router (ID) 192.0.0.9, Interface address 192.0.0.6
  Backup Designated router (ID) 192.0.0.8, Interface address 192.0.0.5
  Timer intervals configured, Hello 10, Dead 40, Wait 40, Retransmit 5
    oob-resync timeout 40
    Hello due in 00:00:00
  Supports Link-local Signaling (LLS)
  Cisco NSF helper support enabled
  IETF NSF helper support enabled
  Can be protected by per-prefix Loop-Free FastReroute
  Can be used for per-prefix Loop-Free FastReroute repair paths
  Not Protected by per-prefix TI-LFA
  Index 1/1/1, flood queue length 0
  Next 0x0(0)/0x0(0)/0x0(0)
  Last flood scan length is 1, maximum is 1
  Last flood scan time is 0 msec, maximum is 0 msec
  Neighbor Count is 1, Adjacent neighbor count is 1
    Adjacent with neighbor 192.0.0.9  (Designated Router)
  Suppress hello for 0 neighbor(s)
'''}

    golden_parsed_output =  {'intf': {'GigabitEthernet3': {'addr': '192.0.0.1',
                               'area': '0',
                               'cost': '1',
                               'dead_timer': '40',
                               'hello_timer': '10',
                               'intf_state': 'up',
                               'mask': '30',
                               'ntype': 'BROADCAST',
                               'ospf_state': 'BDR',
                               'pid': '100',
                               'pri': '1',
                               'prot_state': 'up',
                               'retransmit_timer': '5',
                               'rid': '192.0.0.1',
                               'tdelay': '1 sec',
                               'wait_timer': '40'},
          'GigabitEthernet4': {'addr': '192.0.0.5',
                               'area': '0',
                               'cost': '1',
                               'dead_timer': '40',
                               'hello_timer': '10',
                               'intf_state': 'up',
                               'mask': '30',
                               'ntype': 'BROADCAST',
                               'ospf_state': 'BDR',
                               'pid': '200',
                               'pri': '1',
                               'prot_state': 'up',
                               'retransmit_timer': '5',
                               'rid': '192.0.0.8',
                               'tdelay': '1 sec',
                               'wait_timer': '40'},
          'Loopback100': {'addr': '192.0.0.8',
                          'area': '0',
                          'cost': '1',
                          'intf_state': 'up',
                          'mask': '32',
                          'ntype': 'LOOPBACK',
                          'pid': '200',
                          'prot_state': 'up',
                          'rid': '192.0.0.8'}},
 'intfs_all': ['GigabitEthernet3', 'Loopback100', 'GigabitEthernet4'],
 'intfs_down': [],
 'intfs_up': ['GigabitEthernet3', 'Loopback100', 'GigabitEthernet4']}


    def test_golden(self):
        self.device = Mock(**self.golden_output)
        ip_ospf = ShowIpOspfInterface(device=self.device)
        parsed_output = ip_ospf.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output)
        self.assertNotEqual(parsed_output,'')

    def test_empty(self):
        self.device1 = Mock(**self.empty_output)
        ip_ospf = ShowIpOspfInterface(device=self.device1)
        with self.assertRaises(Exception):
            parsed_output = ip_ospf.parse()

class test_show_ip_ospf_neighbor(unittest.TestCase):

    device = Device(name='aDevice')
    device1 = Device(name='bDevice')
    empty_output = {'execute.return_value': ''}
    golden_output = {'execute.return_value': ''' Neighbor 192.0.0.2, interface address 192.0.0.2
    In the area 0 via interface GigabitEthernet3
    Neighbor priority is 1, State is FULL, 6 state changes
    DR is 192.0.0.2 BDR is 192.0.0.1
    Options is 0x12 in Hello (E-bit, L-bit)
    Options is 0x52 in DBD (E-bit, L-bit, O-bit)
    LLS Options is 0x1 (LR)
    Dead timer due in 00:00:33
    Neighbor is up for 05:08:57
    Index 1/1/1, retransmission queue length 0, number of retransmission 0
    First 0x0(0)/0x0(0)/0x0(0) Next 0x0(0)/0x0(0)/0x0(0)
    Last retransmission scan length is 0, maximum is 0
    Last retransmission scan time is 0 msec, maximum is 0 msec
 Neighbor 192.0.0.9, interface address 192.0.0.6
    In the area 0 via interface GigabitEthernet4
    Neighbor priority is 1, State is FULL, 6 state changes
    DR is 192.0.0.6 BDR is 192.0.0.5
    Options is 0x12 in Hello (E-bit, L-bit)
    Options is 0x52 in DBD (E-bit, L-bit, O-bit)
    LLS Options is 0x1 (LR)
    Dead timer due in 00:00:37
    Neighbor is up for 05:07:51
    Index 1/1/1, retransmission queue length 0, number of retransmission 0
    First 0x0(0)/0x0(0)/0x0(0) Next 0x0(0)/0x0(0)/0x0(0)
    Last retransmission scan length is 0, maximum is 0
    Last retransmission scan time is 0 msec, maximum is 0 msec
'''}

    golden_parsed_output =  {'intf': {'GigabitEthernet3': {'area': '0',
                               'bdr': '192.0.0.1',
                               'dr': '192.0.0.2',
                               'interface_address': '192.0.0.2',
                               'neigh_priority': '1',
                               'neighbor': '192.0.0.2',
                               'state': 'FULL',
                               'state_changes': '6',
                               'uptime': '05:08:57'},
          'GigabitEthernet4': {'area': '0',
                               'bdr': '192.0.0.5',
                               'dr': '192.0.0.6',
                               'interface_address': '192.0.0.6',
                               'neigh_priority': '1',
                               'neighbor': '192.0.0.9',
                               'state': 'FULL',
                               'state_changes': '6',
                               'uptime': '05:07:51'}},
 'intf_list': ['GigabitEthernet3', 'GigabitEthernet4']}

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        ip_ospf = ShowIpOspfNeighborDetail(device=self.device)
        parsed_output = ip_ospf.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output)

    def test_empty(self):
        self.device1 = Mock(**self.empty_output)
        ip_ospf = ShowIpOspfNeighborDetail(device=self.device1)
        with self.assertRaises(Exception):
            parsed_output = ip_ospf.parse()

class test_show_ip_ospf_database(unittest.TestCase):

    device = Device(name='aDevice')
    device1 = Device(name='bDevice')
    empty_output = {'execute.return_value': ''}
    golden_output = {'execute.return_value': '''
            OSPF Router with ID (192.0.0.1) (Process ID 100)

		Router Link States (Area 0)

Link ID         ADV Router      Age         Seq#       Checksum Link count
192.0.0.1       192.0.0.1       1032        0x8000000D 0x00E23C 1
192.0.0.2       192.0.0.2       916         0x8000000E 0x00DE3C 1

		Net Link States (Area 0)

Link ID         ADV Router      Age         Seq#       Checksum
192.0.0.2       192.0.0.2       916         0x8000000A 0x007AAF

            OSPF Router with ID (192.0.0.8) (Process ID 200)

		Router Link States (Area 0)

Link ID         ADV Router      Age         Seq#       Checksum Link count
192.0.0.8       192.0.0.8       811         0x8000000E 0x0081AB 2
192.0.0.9       192.0.0.9       740         0x8000000F 0x009394 2

		Net Link States (Area 0)

Link ID         ADV Router      Age         Seq#       Checksum
192.0.0.6       192.0.0.9       740         0x8000000A 0x00D040
'''}

    golden_parsed_output = {'process_id': {'100': {'area': {'0': {'network_link': {'ls_id': {'192.0.0.2': {'advrouter': {'192.0.0.2': {'age': '916',
                                                                                                            'cksum': '0x007AAF',
                                                                                                            'seq': '0x8000000A'}}}}},
                                       'router_link': {'ls_id': {'192.0.0.1': {'advrouter': {'192.0.0.1': {'age': '1032',
                                                                                                           'cksum': '0x00E23C',
                                                                                                           'lnkcnt': '1',
                                                                                                           'seq': '0x8000000D'}}},
                                                                 '192.0.0.2': {'advrouter': {'192.0.0.2': {'age': '916',
                                                                                                           'cksum': '0x00DE3C',
                                                                                                           'lnkcnt': '1',
                                                                                                           'seq': '0x8000000E'}}}}}}},
                        'router_id': '192.0.0.1'},
                '200': {'area': {'0': {'network_link': {'ls_id': {'192.0.0.6': {'advrouter': {'192.0.0.9': {'age': '740',
                                                                                                            'cksum': '0x00D040',
                                                                                                            'seq': '0x8000000A'}}}}},
                                       'router_link': {'ls_id': {'192.0.0.8': {'advrouter': {'192.0.0.8': {'age': '811',
                                                                                                           'cksum': '0x0081AB',
                                                                                                           'lnkcnt': '2',
                                                                                                           'seq': '0x8000000E'}}},
                                                                 '192.0.0.9': {'advrouter': {'192.0.0.9': {'age': '740',
                                                                                                           'cksum': '0x009394',
                                                                                                           'lnkcnt': '2',
                                                                                                           'seq': '0x8000000F'}}}}}}},
                        'router_id': '192.0.0.8'}}}

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        ip_ospf = ShowIpOspfDatabase(device=self.device)
        parsed_output = ip_ospf.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output)

    def test_empty(self):
        self.device1 = Mock(**self.empty_output)
        ip_ospf = ShowIpOspfDatabase(device=self.device1)
        with self.assertRaises(Exception):
            parsed_output = ip_ospf.parse()

if __name__ == '__main__':
    unittest.main()
