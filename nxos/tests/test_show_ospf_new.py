
# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from metaparser.util.exceptions import SchemaEmptyParserError, SchemaMissingKeyError

# nxos show_ospf
from parser.nxos.show_ospf_new import ShowIpOspfInterface,\
                                      ShowIpOspfNeighborDetail,\
                                      ShowIpOspfDatabaseExternalDetail,\
                                      ShowIpOspfDatabaseNetworkDetail,\
                                      ShowIpOspfDatabaseSummaryDetail,\
                                      ShowIpOspfDatabaseRouterDetail,\
                                      ShowIpOspfDatabaseOpaqueAreaDetail


# ===============================================
#  Unit test for 'show ip ospf interface vrf all'
# ===============================================
class test_show_ip_ospf_interface_vrf_all(unittest.TestCase):

    '''Unit test for "show ip ospf interface vrf all" '''

    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output1 = {
        'vrf': 
            {'VRF1': 
                {'address_family': 
                    {'ipv4': 
                        {'instance': 
                            {1: 
                                {'areas': 
                                    {'0.0.0.1': 
                                        {'interfaces': 
                                            {'Ethernet2/1': 
                                                {'bdr_ip_addr': '20.2.6.2',
                                                'bdr_router_id': '22.22.22.22',
                                                'bfd': 
                                                    {'enable': False},
                                                'cost': 40,
                                                'dead_interval': 40,
                                                'dr_ip_addr': '20.2.6.6',
                                                'dr_router_id': '66.66.66.66',
                                                'enable': True,
                                                'hello_interval': 10,
                                                'hello_timer': '00:00:07',
                                                'if_cfg': True,
                                                'index': 2,
                                                'interface_type': 'broadcast',
                                                'ip_address': '20.2.6.2/24',
                                                'line_protocol': 'up',
                                                'name': 'Ethernet2/1',
                                                'passive': False,
                                                'priority': 1,
                                                'retransmit_interval': 5,
                                                'state': 'bdr',
                                                'statistics': 
                                                    {'link_scope_lsa_cksum_sum': 0,
                                                    'link_scope_lsa_count': 0,
                                                    'num_nbrs_adjacent': 1,
                                                    'num_nbrs_flooding': 1,
                                                    'total_neighbors': 1},
                                                'transmit_delay': 1,
                                                'wait_interval': 40}},
                                        'sham_links': 
                                            {'22.22.22.22 11.11.11.11': 
                                                {'bfd': 
                                                    {'enable': False},
                                                'cost': 1,
                                                'dead_interval': 40,
                                                'enable': True,
                                                'hello_interval': 10,
                                                'hello_timer': '00:00:07',
                                                'if_cfg': False,
                                                'index': 6,
                                                'interface_type': 'p2p',
                                                'ip_address': '22.22.22.22',
                                                'line_protocol': 'up',
                                                'name': 'SL1-0.0.0.0-22.22.22.22-11.11.11.11',
                                                'passive': False,
                                                'retransmit_interval': 5,
                                                'state': 'p2p',
                                                'statistics': 
                                                    {'link_scope_lsa_cksum_sum': 0,
                                                    'link_scope_lsa_count': 0,
                                                    'num_nbrs_adjacent': 1,
                                                    'num_nbrs_flooding': 1,
                                                    'total_neighbors': 1},
                                                'transmit_delay': 1,
                                                'wait_interval': 40},
                                            '22.22.22.22 33.33.33.33': 
                                                {'authentication': 
                                                    {'auth_trailer_key': 
                                                        {'crypto_algorithm': 'Simple'},
                                                        'auth_trailer_key_chain': 
                                                            {'key_chain': 'test'}},
                                                    'bfd': 
                                                        {'enable': False},
                                                    'cost': 111,
                                                    'dead_interval': 13,
                                                    'enable': True,
                                                    'hello_interval': 3,
                                                    'hello_timer': '00:00:00',
                                                    'if_cfg': False,
                                                    'index': 7,
                                                    'interface_type': 'p2p',
                                                    'ip_address': '22.22.22.22',
                                                    'line_protocol': 'up',
                                                    'name': 'SL2-0.0.0.0-22.22.22.22-33.33.33.33',
                                                    'passive': False,
                                                    'retransmit_interval': 5,
                                                    'state': 'p2p',
                                                    'statistics': 
                                                        {'link_scope_lsa_cksum_sum': 0,
                                                        'link_scope_lsa_count': 0,
                                                        'num_nbrs_adjacent': 0,
                                                        'num_nbrs_flooding': 0,
                                                        'total_neighbors': 0},
                                                    'transmit_delay': 7,
                                                    'wait_interval': 13}},
                                        'virtual_links': 
                                            {'0.0.0.0 8.8.8.8': 
                                                {'bfd': 
                                                    {'enable': False},
                                                'cost': 1,
                                                'dead_interval': 40,
                                                'enable': True,
                                                'hello_interval': 10,
                                                'hello_timer': '00:00:07',
                                                'if_cfg': False,
                                                'index': 6,
                                                'interface_type': 'p2p',
                                                'ip_address': '22.22.22.22',
                                                'line_protocol': 'up',
                                                'name': 'VL1-0.0.0.0-8.8.8.8-12.12.12.12',
                                                'passive': False,
                                                'retransmit_interval': 5,
                                                'state': 'p2p',
                                                'statistics': 
                                                    {'link_scope_lsa_cksum_sum': 0,
                                                    'link_scope_lsa_count': 0,
                                                    'num_nbrs_adjacent': 1,
                                                    'num_nbrs_flooding': 1,
                                                    'total_neighbors': 1},
                                                'transmit_delay': 1,
                                                'wait_interval': 40}}}}}}}}},
            'default': 
                {'address_family': 
                    {'ipv4': 
                        {'instance': 
                            {1: 
                                {'areas': 
                                    {'0.0.0.0': 
                                        {'interfaces': 
                                            {'Ethernet2/2': 
                                                {'bdr_ip_addr': '10.2.3.2',
                                                'bdr_router_id': '2.2.2.2',
                                                'bfd': 
                                                    {'enable': False},
                                                'cost': 1,
                                                'dead_interval': 40,
                                                'dr_ip_addr': '10.2.3.3',
                                                'dr_router_id': '3.3.3.3',
                                                'enable': True,
                                                'hello_interval': 10,
                                                'hello_timer': '00:00:02',
                                                'if_cfg': True,
                                                'index': 3,
                                                'interface_type': 'broadcast',
                                                'ip_address': '10.2.3.2/24',
                                                'line_protocol': 'up',
                                                'name': 'Ethernet2/2',
                                                'passive': False,
                                                'priority': 1,
                                                'retransmit_interval': 5,
                                                'state': 'bdr',
                                                'statistics': 
                                                    {'link_scope_lsa_cksum_sum': 0,
                                                    'link_scope_lsa_count': 0,
                                                    'num_nbrs_adjacent': 1,
                                                    'num_nbrs_flooding': 1,
                                                    'total_neighbors': 1},
                                                'transmit_delay': 1,
                                                'wait_interval': 40},
                                            'Ethernet2/3': 
                                                {'bdr_ip_addr': '10.2.4.2',
                                                'bdr_router_id': '2.2.2.2',
                                                'bfd': 
                                                    {'enable': False},
                                                'cost': 1,
                                                'dead_interval': 40,
                                                'dr_ip_addr': '10.2.4.4',
                                                'dr_router_id': '4.4.4.4',
                                                'enable': True,
                                                'hello_interval': 10,
                                                'hello_timer': '00:00:00',
                                                'if_cfg': True,
                                                'index': 4,
                                                'interface_type': 'broadcast',
                                                'ip_address': '10.2.4.2/24',
                                                'line_protocol': 'up',
                                                'name': 'Ethernet2/3',
                                                'passive': False,
                                                'priority': 1,
                                                'retransmit_interval': 5,
                                                'state': 'bdr',
                                                'statistics': 
                                                    {'link_scope_lsa_cksum_sum': 0,
                                                    'link_scope_lsa_count': 0,
                                                    'num_nbrs_adjacent': 1,
                                                    'num_nbrs_flooding': 1,
                                                    'total_neighbors': 1},
                                                'transmit_delay': 1,
                                                'wait_interval': 40},
                                            'Ethernet2/4': 
                                                {'bdr_ip_addr': '10.1.2.2',
                                                'bdr_router_id': '2.2.2.2',
                                                'bfd': 
                                                    {'enable': False},
                                                'cost': 1,
                                                'dead_interval': 40,
                                                'dr_ip_addr': '10.1.2.1',
                                                'dr_router_id': '1.1.1.1',
                                                'enable': True,
                                                'hello_interval': 10,
                                                'hello_timer': '00:00:00',
                                                'if_cfg': True,
                                                'index': 5,
                                                'interface_type': 'broadcast',
                                                'ip_address': '10.1.2.2/24',
                                                'line_protocol': 'up',
                                                'name': 'Ethernet2/4',
                                                'passive': False,
                                                'priority': 1,
                                                'retransmit_interval': 5,
                                                'state': 'bdr',
                                                'statistics': 
                                                    {'link_scope_lsa_cksum_sum': 0,
                                                    'link_scope_lsa_count': 0,
                                                    'num_nbrs_adjacent': 1,
                                                    'num_nbrs_flooding': 1,
                                                    'total_neighbors': 1},
                                                'transmit_delay': 1,
                                                'wait_interval': 40},
                                            'loopback0': 
                                                {'bfd': 
                                                    {'enable': False},
                                                'cost': 1,
                                                'enable': True,
                                                'if_cfg': True,
                                                'index': 1,
                                                'interface_type': 'loopback',
                                                'ip_address': '2.2.2.2/32',
                                                'line_protocol': 'up',
                                                'name': 'loopback0',
                                                'state': 'loopback'}}}}}}}}}}}

    golden_output1 = {'execute.return_value': '''
        R2_ospf_nx# show ip ospf interface vrf all
         Ethernet2/2 is up, line protocol is up
            IP address 10.2.3.2/24
            Process ID 1 VRF default, area 0.0.0.0
            Enabled by interface configuration
            State BDR, Network type BROADCAST, cost 1
            Index 3, Transmit delay 1 sec, Router Priority 1
            Designated Router ID: 3.3.3.3, address: 10.2.3.3
            Backup Designated Router ID: 2.2.2.2, address: 10.2.3.2
            1 Neighbors, flooding to 1, adjacent with 1
            Timer intervals: Hello 10, Dead 40, Wait 40, Retransmit 5
              Hello timer due in 00:00:02
            No authentication
            Number of opaque link LSAs: 0, checksum sum 0
         Ethernet2/3 is up, line protocol is up
            IP address 10.2.4.2/24
            Process ID 1 VRF default, area 0.0.0.0
            Enabled by interface configuration
            State BDR, Network type BROADCAST, cost 1
            Index 4, Transmit delay 1 sec, Router Priority 1
            Designated Router ID: 4.4.4.4, address: 10.2.4.4
            Backup Designated Router ID: 2.2.2.2, address: 10.2.4.2
            1 Neighbors, flooding to 1, adjacent with 1
            Timer intervals: Hello 10, Dead 40, Wait 40, Retransmit 5
              Hello timer due in 00:00:00
            No authentication
            Number of opaque link LSAs: 0, checksum sum 0
         Ethernet2/4 is up, line protocol is up
            IP address 10.1.2.2/24
            Process ID 1 VRF default, area 0.0.0.0
            Enabled by interface configuration
            State BDR, Network type BROADCAST, cost 1
            Index 5, Transmit delay 1 sec, Router Priority 1
            Designated Router ID: 1.1.1.1, address: 10.1.2.1
            Backup Designated Router ID: 2.2.2.2, address: 10.1.2.2
            1 Neighbors, flooding to 1, adjacent with 1
            Timer intervals: Hello 10, Dead 40, Wait 40, Retransmit 5
              Hello timer due in 00:00:00
            No authentication
            Number of opaque link LSAs: 0, checksum sum 0
         loopback0 is up, line protocol is up
            IP address 2.2.2.2/32
            Process ID 1 VRF default, area 0.0.0.0
            Enabled by interface configuration
            State LOOPBACK, Network type LOOPBACK, cost 1
            Index 1
         SL1-0.0.0.0-22.22.22.22-11.11.11.11 is up, line protocol is up
            Unnumbered interface using IP address of loopback1 (22.22.22.22)
            Process ID 1 VRF VRF1, area 0.0.0.1
            State P2P, Network type P2P, cost 1
            Index 6, Transmit delay 1 sec
            1 Neighbors, flooding to 1, adjacent with 1
            Timer intervals: Hello 10, Dead 40, Wait 40, Retransmit 5
              Hello timer due in 00:00:07
            No authentication
            Number of opaque link LSAs: 0, checksum sum 0
         SL2-0.0.0.0-22.22.22.22-33.33.33.33 is up, line protocol is up
            Unnumbered interface using IP address of loopback1 (22.22.22.22)
            Process ID 1 VRF VRF1, area 0.0.0.1
            State P2P, Network type P2P, cost 111
            Index 7, Transmit delay 7 sec
            0 Neighbors, flooding to 0, adjacent with 0
            Timer intervals: Hello 3, Dead 13, Wait 13, Retransmit 5
              Hello timer due in 00:00:00
            Simple authentication, using keychain test (ready)
            Number of opaque link LSAs: 0, checksum sum 0
         VL1-0.0.0.0-8.8.8.8-12.12.12.12 is up, line protocol is up
            Unnumbered interface using IP address of loopback1 (22.22.22.22)
            Process ID 1 VRF VRF1, area 0.0.0.1
            State P2P, Network type P2P, cost 1
            Index 6, Transmit delay 1 sec
            1 Neighbors, flooding to 1, adjacent with 1
            Timer intervals: Hello 10, Dead 40, Wait 40, Retransmit 5
              Hello timer due in 00:00:07
            No authentication
            Number of opaque link LSAs: 0, checksum sum 0
         Ethernet2/1 is up, line protocol is up
            IP address 20.2.6.2/24
            Process ID 1 VRF VRF1, area 0.0.0.1
            Enabled by interface configuration
            State BDR, Network type BROADCAST, cost 40
            Index 2, Transmit delay 1 sec, Router Priority 1
            Designated Router ID: 66.66.66.66, address: 20.2.6.6
            Backup Designated Router ID: 22.22.22.22, address: 20.2.6.2
            1 Neighbors, flooding to 1, adjacent with 1
            Timer intervals: Hello 10, Dead 40, Wait 40, Retransmit 5
              Hello timer due in 00:00:07
            No authentication
            Number of opaque link LSAs: 0, checksum sum 0
        '''}

    def test_full(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output1)
        obj = ShowIpOspfInterface(device=self.device)
        parsed_output = obj.parse(vrf='all')
        self.assertEqual(parsed_output, self.golden_parsed_output1)

    def test_empty(self):
        self.maxDiff = None
        self.device = Mock(**self.empty_output)
        obj = ShowIpOspfInterface(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()


# ======================================================
#  Unit test for 'show ip ospf neighbors detail vrf all'
# ======================================================
class test_show_ip_ospf_neighbors_detail_vrf_all(unittest.TestCase):

    '''Unit test for "show ip ospf neighbors detail vrf all" '''

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
                                            {'Ethernet2/1': 
                                                {'neighbors': 
                                                    {'66.66.66.66': 
                                                        {'address': '20.2.6.6',
                                                        'bdr_ip_addr': '20.2.6.2',
                                                        'dbd_options': '0x52',
                                                        'dead_timer': '00:00:38',
                                                        'dr_ip_addr': '20.2.6.6',
                                                        'hello_options': '0x12',
                                                        'last_non_hello_packet_received': 'never',
                                                        'last_state_change': '08:38:39',
                                                        'priority': 1,
                                                        'neighbor_router_id': '66.66.66.66',
                                                        'state': 'full',
                                                        'statistics': 
                                                            {'nbr_event_count': 6}}}}},
                                        'sham_links': 
                                            {'22.22.22.22 11.11.11.11': 
                                                {'neighbors': 
                                                    {'11.11.11.11': 
                                                        {'address': '11.11.11.11',
                                                        'dbd_options': '0x72',
                                                        'dead_timer': '00:00:41',
                                                        'hello_options': '0x32',
                                                        'last_non_hello_packet_received': 'never',
                                                        'last_state_change': '08:16:20',
                                                        'neighbor_router_id': '11.11.11.11',
                                                        'state': 'full',
                                                        'statistics': 
                                                            {'nbr_event_count': 8}}}}}}}}}}}},
            'default': 
                {'address_family': 
                    {'ipv4': 
                        {'instance': 
                            {'1': 
                                {'areas': 
                                    {'0.0.0.0': 
                                        {'interfaces': 
                                            {'Ethernet1/2': 
                                                {'neighbors': 
                                                    {'1.1.1.1': 
                                                        {'address': '10.1.3.1',
                                                        'bdr_ip_addr': '10.1.3.3',
                                                        'dbd_options': '0x52',
                                                        'dead_timer': '00:00:36',
                                                        'dr_ip_addr': '10.1.3.1',
                                                        'hello_options': '0x12',
                                                        'last_non_hello_packet_received': '00:00:15',
                                                        'last_state_change': '11:04:28',
                                                        'priority': 1,
                                                        'neighbor_router_id': '1.1.1.1',
                                                        'state': 'full',
                                                        'statistics': 
                                                            {'nbr_event_count': 5}}}},
                                            'Ethernet2/2': 
                                                {'neighbors': 
                                                    {'3.3.3.3': 
                                                        {'address': '10.2.3.3',
                                                        'bdr_ip_addr': '10.2.3.2',
                                                        'dbd_options': '0x52',
                                                        'dead_timer': '00:00:39',
                                                        'dr_ip_addr': '10.2.3.3',
                                                        'hello_options': '0x12',
                                                        'last_non_hello_packet_received': 'never',
                                                        'last_state_change': '08:38:40',
                                                        'priority': 1,
                                                        'neighbor_router_id': '3.3.3.3',
                                                        'state': 'full',
                                                        'statistics': 
                                                            {'nbr_event_count': 5}}}},
                                            'Ethernet2/3': 
                                                {'neighbors': 
                                                    {'4.4.4.4': 
                                                        {'address': '10.2.4.4',
                                                        'bdr_ip_addr': '10.2.4.2',
                                                        'dbd_options': '0x52',
                                                        'dead_timer': '00:00:33',
                                                        'dr_ip_addr': '10.2.4.4',
                                                        'hello_options': '0x12',
                                                        'last_non_hello_packet_received': 'never',
                                                        'last_state_change': '08:38:42',
                                                        'priority': 1,
                                                        'neighbor_router_id': '4.4.4.4',
                                                        'state': 'full',
                                                        'statistics': 
                                                            {'nbr_event_count': 6}}}},
                                            'Ethernet2/4': 
                                                {'neighbors': 
                                                    {'1.1.1.1': 
                                                        {'address': '10.1.2.1',
                                                        'bdr_ip_addr': '10.1.2.2',
                                                        'dbd_options': '0x52',
                                                        'dead_timer': '00:00:35',
                                                        'dr_ip_addr': '10.1.2.1',
                                                        'hello_options': '0x12',
                                                        'last_non_hello_packet_received': 'never',
                                                        'last_state_change': '08:38:41',
                                                        'priority': 1,
                                                        'neighbor_router_id': '1.1.1.1',
                                                        'state': 'full',
                                                        'statistics': 
                                                            {'nbr_event_count': 5}}}}},
                                        'virtual_links': 
                                            {'0.0.0.1 4.4.4.4': 
                                                {'neighbors': 
                                                    {'4.4.4.4': 
                                                        {'address': '20.3.4.4',
                                                        'dbd_options': '0x72',
                                                        'dead_timer': '00:00:43',
                                                        'hello_options': '0x32',
                                                        'last_non_hello_packet_received': '00:00:18',
                                                        'last_state_change': '00:00:23',
                                                        'neighbor_router_id': '4.4.4.4',
                                                        'state': 'full',
                                                        'statistics': 
                                                            {'nbr_event_count': 5}}}}}},
                                    '0.0.0.1': 
                                        {'interfaces': 
                                            {'Ethernet1/3': 
                                                {'neighbors': 
                                                    {'2.2.2.2': 
                                                        {'address': '20.2.3.2',
                                                        'bdr_ip_addr': '20.2.3.3',
                                                        'dbd_options': '0x52',
                                                        'dead_timer': '00:00:36',
                                                        'dr_ip_addr': '20.2.3.2',
                                                        'hello_options': '0x12',
                                                        'last_non_hello_packet_received': '00:00:18',
                                                        'last_state_change': '11:04:25',
                                                        'priority': 1,
                                                        'neighbor_router_id': '2.2.2.2',
                                                        'state': 'full',
                                                        'statistics': 
                                                            {'nbr_event_count': 5}}}},
                                            'Ethernet1/5': 
                                                {'neighbors': 
                                                    {'4.4.4.4': 
                                                        {'address': '20.3.4.4',
                                                        'bdr_ip_addr': '20.3.4.3',
                                                        'dbd_options': '0x52',
                                                        'dead_timer': '00:00:36',
                                                        'dr_ip_addr': '20.3.4.4',
                                                        'hello_options': '0x12',
                                                        'last_non_hello_packet_received': '00:00:18',
                                                        'last_state_change': '11:04:28',
                                                        'priority': 1,
                                                        'neighbor_router_id': '4.4.4.4',
                                                        'state': 'full',
                                                        'statistics': 
                                                            {'nbr_event_count': 6}}}}}}}}}}}}}}

    golden_output1 = {'execute.return_value': '''
        R2_ospf_nx# show ip ospf neighbors detail vrf all
          Neighbor 3.3.3.3, interface address 10.2.3.3
            Process ID 1 VRF default, in area 0.0.0.0 via interface Ethernet2/2
            State is FULL, 5 state changes, last change 08:38:40
            Neighbor priority is 1
            DR is 10.2.3.3 BDR is 10.2.3.2
            Hello options 0x12, dbd options 0x52
            Last non-hello packet received never
            Dead timer due in 00:00:39
          Neighbor 4.4.4.4, interface address 10.2.4.4
            Process ID 1 VRF default, in area 0.0.0.0 via interface Ethernet2/3
            State is FULL, 6 state changes, last change 08:38:42
            Neighbor priority is 1
            DR is 10.2.4.4 BDR is 10.2.4.2
            Hello options 0x12, dbd options 0x52
            Last non-hello packet received never
            Dead timer due in 00:00:33
          Neighbor 1.1.1.1, interface address 10.1.2.1
            Process ID 1 VRF default, in area 0.0.0.0 via interface Ethernet2/4
            State is FULL, 5 state changes, last change 08:38:41
            Neighbor priority is 1
            DR is 10.1.2.1 BDR is 10.1.2.2
            Hello options 0x12, dbd options 0x52
            Last non-hello packet received never
            Dead timer due in 00:00:35
          Neighbor 11.11.11.11, interface address 11.11.11.11
            Process ID 1 VRF VRF1, in area 0.0.0.1 via interface SL1-0.0.0.0-22.22.22.22-11.11.11.11
            State is FULL, 8 state changes, last change 08:16:20
            Hello options 0x32, dbd options 0x72
            Last non-hello packet received never
            Dead timer due in 00:00:41
          Neighbor 66.66.66.66, interface address 20.2.6.6
            Process ID 1 VRF VRF1, in area 0.0.0.1 via interface Ethernet2/1
            State is FULL, 6 state changes, last change 08:38:39
            Neighbor priority is 1
            DR is 20.2.6.6 BDR is 20.2.6.2
            Hello options 0x12, dbd options 0x52
            Last non-hello packet received never
            Dead timer due in 00:00:38
          Neighbor 4.4.4.4, interface address 20.3.4.4
            Process ID 1 VRF default, in area 0.0.0.0 via interface VL1-0.0.0.1-4.4.4.4
            State is FULL, 5 state changes, last change 00:00:23
            We are slave in DBD exchange, seqnr 0x26aa , all DBDs sent and acked
            Hello options 0x32, dbd options 0x72
            Last non-hello packet received 00:00:18
              Dead timer due in 00:00:43
              DBD rxmit timer due in 00:00:22
          Neighbor 1.1.1.1, interface address 10.1.3.1
            Process ID 1 VRF default, in area 0.0.0.0 via interface Ethernet1/2
            State is FULL, 5 state changes, last change 11:04:28
            Neighbor priority is 1
            DR is 10.1.3.1 BDR is 10.1.3.3
            Hello options 0x12, dbd options 0x52
            Last non-hello packet received 00:00:15
              Dead timer due in 00:00:36
          Neighbor 2.2.2.2, interface address 20.2.3.2
            Process ID 1 VRF default, in area 0.0.0.1 via interface Ethernet1/3
            State is FULL, 5 state changes, last change 11:04:25
            Neighbor priority is 1
            DR is 20.2.3.2 BDR is 20.2.3.3
            Hello options 0x12, dbd options 0x52
            Last non-hello packet received 00:00:18
              Dead timer due in 00:00:36
          Neighbor 4.4.4.4, interface address 20.3.4.4
            Process ID 1 VRF default, in area 0.0.0.1 via interface Ethernet1/5
            State is FULL, 6 state changes, last change 11:04:28
            Neighbor priority is 1
            DR is 20.3.4.4 BDR is 20.3.4.3
            Hello options 0x12, dbd options 0x52
            Last non-hello packet received 00:00:18
              Dead timer due in 00:00:36
        '''}

    def test_full(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output1)
        obj = ShowIpOspfNeighborDetail(device=self.device)
        parsed_output = obj.parse(vrf='all')
        self.assertEqual(parsed_output, self.golden_parsed_output1)

    def test_empty(self):
        self.maxDiff = None
        self.device = Mock(**self.empty_output)
        obj = ShowIpOspfNeighborDetail(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()


# ==============================================================
#  Unit test for 'show ip ospf database external detail vrf all'
# ==============================================================
class test_show_ip_ospf_database_external_detail_vrf_all(unittest.TestCase):

    '''Unit test for "show ip ospf database external detail vrf all" '''

    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output1 = {
        'vrf': 
            {'default': 
                {'address_family': 
                    {'ipv4': 
                        {'instance': 
                            {'1': 
                                {'database': 
                                    {'lsa_types': 
                                        {'Type-5 AS External': 
                                            {'lsas': 
                                                {'44.44.44.44 4.4.4.4': 
                                                    {'ospfv2': 
                                                        {'body': 
                                                            {'external': 
                                                                {'network_mask': '/32',
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
                                                            'age': 1565,
                                                            'checksum': '0x7d61',
                                                            'length': 36,
                                                            'lsa_id': '44.44.44.44',
                                                            'option': '0x20 (No TOS-capability, DC)',
                                                            'seq_num': '0x80000002',
                                                            'type': 'Type-5 '
                                                             'AS-External'}}}}}}}}}}}}}}

    golden_output1 = {'execute.return_value': '''
        R2_ospf_nx# show ip ospf database external detail vrf all
        OSPF Router with ID (2.2.2.2) (Process ID 1 VRF default)

                Type-5 AS External Link States 

        LS age: 1565
        Options: 0x20 (No TOS-capability, DC)
        LS Type: Type-5 AS-External
        Link State ID: 44.44.44.44 (Network address)
        Advertising Router: 4.4.4.4
        LS Seq Number: 0x80000002
        Checksum: 0x7d61
        Length: 36
        Network Mask: /32
             Metric Type: 2 (Larger than any link state path)
             TOS: 0
             Metric: 20
             Forward Address: 0.0.0.0
             External Route Tag: 0
        '''}

    def test_full(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output1)
        obj = ShowIpOspfDatabaseExternalDetail(device=self.device)
        parsed_output = obj.parse(vrf='all')
        self.assertEqual(parsed_output, self.golden_parsed_output1)

    def test_empty(self):
        self.maxDiff = None
        self.device = Mock(**self.empty_output)
        obj = ShowIpOspfDatabaseExternalDetail(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()


# ==============================================================
#  Unit test for 'show ip ospf database network detail vrf all'
# ==============================================================
class test_show_ip_ospf_database_network_detail_vrf_all(unittest.TestCase):

    '''Unit test for "show ip ospf database network detail vrf all" '''

    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output1 = {
        'vrf': 
            {'VRF1': 
                {'address_family': 
                    {'ipv4': 
                        {'instance': 
                            {'1': 
                                {'database': 
                                    {'lsa_types': 
                                        {'Network': 
                                            {'lsas': 
                                                {'20.1.5.1 11.11.11.11': 
                                                    {'ospfv2': 
                                                        {'body': 
                                                            {'network': 
                                                                {'attached_routers': 
                                                                    {'11.11.11.11': {},
                                                                    '55.55.55.55': {}},
                                                                'network_mask': '/24'}},
                                                        'header': 
                                                            {'adv_router': '11.11.11.11',
                                                            'age': 1454,
                                                            'checksum': '0xddd9',
                                                            'length': 32,
                                                            'lsa_id': '20.1.5.1',
                                                            'option': '0x22 (No TOS-capability, DC)',
                                                            'seq_num': '0x80000033',
                                                            'type': 'Network Links'}}},
                                                '20.2.6.6 66.66.66.66': 
                                                    {'ospfv2': 
                                                        {'body': 
                                                            {'network': 
                                                                {'attached_routers': 
                                                                    {'22.22.22.22': {},
                                                                    '66.66.66.66': {}},
                                                                'network_mask': '/24'}},
                                                        'header': 
                                                            {'adv_router': '66.66.66.66',
                                                            'age': 1080,
                                                            'checksum': '0x3f5f',
                                                            'length': 32,
                                                            'lsa_id': '20.2.6.6',
                                                            'option': '0x22 (No TOS-capability, DC)',
                                                            'seq_num': '0x80000010',
                                                            'type': 'Network Links'}}},
                                                '20.3.7.7 77.77.77.77': 
                                                    {'ospfv2': 
                                                        {'body': 
                                                            {'network': 
                                                                {'attached_routers': 
                                                                    {'3.3.3.3': {},
                                                                    '77.77.77.77': {}},
                                                                'network_mask': '/24'}},
                                                        'header': 
                                                            {'adv_router': '77.77.77.77',
                                                            'age': 812,
                                                            'checksum': '0x5a1a',
                                                            'length': 32,
                                                            'lsa_id': '20.3.7.7',
                                                            'option': '0x22 (No TOS-capability, DC)',
                                                            'seq_num': '0x8000002b',
                                                            'type': 'Network Links'}}},
                                                '20.5.6.6 66.66.66.66': 
                                                    {'ospfv2': 
                                                        {'body': 
                                                            {'network': 
                                                                {'attached_routers': 
                                                                    {'55.55.55.55': {},
                                                                    '66.66.66.66': {}},
                                                                'network_mask': '/24'}},
                                                        'header': 
                                                            {'adv_router': '66.66.66.66',
                                                            'age': 573,
                                                            'checksum': '0x5f9d',
                                                            'length': 32,
                                                            'lsa_id': '20.5.6.6',
                                                            'option': '0x22 (No TOS-capability, DC)',
                                                            'seq_num': '0x8000002a',
                                                            'type': 'Network '
                                                                    'Links'}}},
                                                '20.6.7.6 66.66.66.66': 
                                                    {'ospfv2': 
                                                        {'body': 
                                                            {'network': 
                                                                {'attached_routers': 
                                                                    {'66.66.66.66': {},
                                                                    '77.77.77.77': {}},
                                                                'network_mask': '/24'}},
                                                        'header': 
                                                            {'adv_router': '66.66.66.66',
                                                            'age': 1819,
                                                            'checksum': '0x960b',
                                                            'length': 32,
                                                            'lsa_id': '20.6.7.6',
                                                            'option': '0x22 (No TOS-capability, DC)',
                                                            'seq_num': '0x8000002b',
                                                            'type': 'Network '
                                                                    'Links'}}}}}}}}}}}},
            'default': 
                {'address_family': 
                    {'ipv4': 
                        {'instance': 
                            {'1': 
                                {'database': 
                                    {'lsa_types': 
                                        {'Network': 
                                            {'lsas': 
                                                {'10.1.2.1 1.1.1.1': 
                                                    {'ospfv2': 
                                                        {'body': 
                                                            {'network': 
                                                                {'attached_routers': 
                                                                    {'1.1.1.1': {},
                                                                    '2.2.2.2': {}},
                                                                'network_mask': '/24'}},
                                                        'header': 
                                                            {'adv_router': '1.1.1.1',
                                                            'age': 772,
                                                            'checksum': '0x3bd1',
                                                            'length': 32,
                                                            'lsa_id': '10.1.2.1',
                                                            'option': '0x22 (No TOS-capability, DC)',
                                                            'seq_num': '0x80000010',
                                                            'type': 'Network Links'}}},
                                                '10.1.4.4 4.4.4.4': 
                                                    {'ospfv2': 
                                                        {'body': 
                                                            {'network': 
                                                                {'attached_routers': 
                                                                    {'1.1.1.1': {},
                                                                    '4.4.4.4': {}},
                                                                'network_mask': '/24'}},
                                                        'header': 
                                                            {'adv_router': '4.4.4.4',
                                                            'age': 1482,
                                                            'checksum': '0xa232',
                                                            'length': 32,
                                                            'lsa_id': '10.1.4.4',
                                                            'option': '0x22 (No TOS-capability, DC)',
                                                            'seq_num': '0x8000002f',
                                                            'type': 'Network Links'}}},
                                                '10.2.3.3 3.3.3.3': 
                                                    {'ospfv2': 
                                                        {'body': 
                                                            {'network': 
                                                                {'attached_routers': 
                                                                    {'2.2.2.2': {},
                                                                    '3.3.3.3': {}},
                                                                'network_mask': '/24'}},
                                                        'header': 
                                                            {'adv_router': '3.3.3.3',
                                                            'age': 788,
                                                            'checksum': '0x28d0',
                                                            'length': 32,
                                                            'lsa_id': '10.2.3.3',
                                                            'option': '0x22 (No TOS-capability, DC)',
                                                            'seq_num': '0x80000010',
                                                            'type': 'Network Links'}}},
                                                '10.2.4.4 4.4.4.4': 
                                                    {'ospfv2': 
                                                        {'body': 
                                                            {'network': 
                                                                {'attached_routers': 
                                                                    {'2.2.2.2': {},
                                                                    '4.4.4.4': {}},
                                                                'network_mask': '/24'}},
                                                        'header': 
                                                            {'adv_router': '4.4.4.4',
                                                            'age': 724,
                                                            'checksum': '0x07e7',
                                                            'length': 32,
                                                            'lsa_id': '10.2.4.4',
                                                            'option': '0x22 (No TOS-capability, DC)',
                                                            'seq_num': '0x80000010',
                                                            'type': 'Network Links'}}},
                                                '10.3.4.4 4.4.4.4': 
                                                    {'ospfv2': 
                                                        {'body': 
                                                            {'network': 
                                                                {'attached_routers': 
                                                                    {'3.3.3.3': {},
                                                                    '4.4.4.4': {}},
                                                                'network_mask': '/24'}},
                                                        'header': 
                                                            {'adv_router': '4.4.4.4',
                                                            'age': 987,
                                                            'checksum': '0xeedb',
                                                            'length': 32,
                                                            'lsa_id': '10.3.4.4',
                                                            'option': '0x22 (No TOS-capability, DC)',
                                                            'seq_num': '0x8000002f',
                                                            'type': 'Network Links'}}}}}}}}}}}}}}

    golden_output1 = {'execute.return_value': '''
        R2_ospf_nx# show ip ospf database network detail vrf all
        OSPF Router with ID (2.2.2.2) (Process ID 1 VRF default)

                Network Link States (Area 0.0.0.0)

        LS age: 772
        Options: 0x22 (No TOS-capability, DC)
        LS Type: Network Links
        Link State ID: 10.1.2.1 (Designated Router address)
        Advertising Router: 1.1.1.1
        LS Seq Number: 0x80000010
        Checksum: 0x3bd1
        Length: 32
        Network Mask: /24
             Attached Router: 1.1.1.1
             Attached Router: 2.2.2.2

        LS age: 1482
        Options: 0x22 (No TOS-capability, DC)
        LS Type: Network Links
        Link State ID: 10.1.4.4 (Designated Router address)
        Advertising Router: 4.4.4.4
        LS Seq Number: 0x8000002f
        Checksum: 0xa232
        Length: 32
        Network Mask: /24
             Attached Router: 4.4.4.4
             Attached Router: 1.1.1.1

        LS age: 788
        Options: 0x22 (No TOS-capability, DC)
        LS Type: Network Links
        Link State ID: 10.2.3.3 (Designated Router address)
        Advertising Router: 3.3.3.3
        LS Seq Number: 0x80000010
        Checksum: 0x28d0
        Length: 32
        Network Mask: /24
             Attached Router: 2.2.2.2
             Attached Router: 3.3.3.3

        LS age: 724
        Options: 0x22 (No TOS-capability, DC)
        LS Type: Network Links
        Link State ID: 10.2.4.4 (Designated Router address)
        Advertising Router: 4.4.4.4
        LS Seq Number: 0x80000010
        Checksum: 0x07e7
        Length: 32
        Network Mask: /24
             Attached Router: 4.4.4.4
             Attached Router: 2.2.2.2

        LS age: 987
        Options: 0x22 (No TOS-capability, DC)
        LS Type: Network Links
        Link State ID: 10.3.4.4 (Designated Router address)
        Advertising Router: 4.4.4.4
        LS Seq Number: 0x8000002f
        Checksum: 0xeedb
        Length: 32
        Network Mask: /24
             Attached Router: 4.4.4.4
             Attached Router: 3.3.3.3


            OSPF Router with ID (22.22.22.22) (Process ID 1 VRF VRF1)

                    Network Link States (Area 0.0.0.1)

        LS age: 1454
        Options: 0x22 (No TOS-capability, DC)
        LS Type: Network Links
        Link State ID: 20.1.5.1 (Designated Router address)
        Advertising Router: 11.11.11.11
        LS Seq Number: 0x80000033
        Checksum: 0xddd9
        Length: 32
        Network Mask: /24
             Attached Router: 11.11.11.11
             Attached Router: 55.55.55.55

        LS age: 1080
        Options: 0x22 (No TOS-capability, DC)
        LS Type: Network Links
        Link State ID: 20.2.6.6 (Designated Router address)
        Advertising Router: 66.66.66.66
        LS Seq Number: 0x80000010
        Checksum: 0x3f5f
        Length: 32
        Network Mask: /24
             Attached Router: 66.66.66.66
             Attached Router: 22.22.22.22

        LS age: 812
        Options: 0x22 (No TOS-capability, DC)
        LS Type: Network Links
        Link State ID: 20.3.7.7 (Designated Router address)
        Advertising Router: 77.77.77.77
        LS Seq Number: 0x8000002b
        Checksum: 0x5a1a
        Length: 32
        Network Mask: /24
             Attached Router: 77.77.77.77
             Attached Router: 3.3.3.3

        LS age: 573
        Options: 0x22 (No TOS-capability, DC)
        LS Type: Network Links
        Link State ID: 20.5.6.6 (Designated Router address)
        Advertising Router: 66.66.66.66
        LS Seq Number: 0x8000002a
        Checksum: 0x5f9d
        Length: 32
        Network Mask: /24
             Attached Router: 66.66.66.66
             Attached Router: 55.55.55.55

        LS age: 1819
        Options: 0x22 (No TOS-capability, DC)
        LS Type: Network Links
        Link State ID: 20.6.7.6 (Designated Router address)
        Advertising Router: 66.66.66.66
        LS Seq Number: 0x8000002b
        Checksum: 0x960b
        Length: 32
        Network Mask: /24
             Attached Router: 66.66.66.66
             Attached Router: 77.77.77.77
        '''}

    def test_full(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output1)
        obj = ShowIpOspfDatabaseNetworkDetail(device=self.device)
        parsed_output = obj.parse(vrf='all')
        self.assertEqual(parsed_output, self.golden_parsed_output1)

    def test_empty(self):
        self.maxDiff = None
        self.device = Mock(**self.empty_output)
        obj = ShowIpOspfDatabaseNetworkDetail(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()


# ==============================================================
#  Unit test for 'show ip ospf database summary detail vrf all'
# ==============================================================
class test_show_ip_ospf_database_summary_detail_vrf_all(unittest.TestCase):

    '''Unit test for "show ip ospf database summary detail vrf all" '''

    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output1 = {
        'vrf': 
            {'default': 
                {'address_family': 
                    {'ipv4': 
                        {'instance': 
                            {'1': 
                                {'database': 
                                    {'lsa_types': 
                                        {'Summary Network': 
                                            {'lsas': 
                                                {'10.1.2.0 2.2.2.2': 
                                                    {'ospfv2': 
                                                        {'body': 
                                                            {'summary': 
                                                                {'network_mask': '/24',
                                                                'topologies': 
                                                                    {0: 
                                                                        {'metric': 4294,
                                                                        'mt_id': 0,
                                                                        'tos': 0}}}},
                                                        'header': 
                                                            {'adv_router': '2.2.2.2',
                                                            'age': 788,
                                                            'checksum': '0xfc54',
                                                            'length': 28,
                                                            'lsa_id': '10.1.2.0',
                                                            'option': '0x22 (No TOS-capability, DC)',
                                                            'seq_num': '0x80000001',
                                                            'type': 'Network Summary'}}},
                                                '10.1.2.0 3.3.3.3': 
                                                    {'ospfv2': 
                                                        {'body': 
                                                            {'summary': 
                                                                {'network_mask': '/24',
                                                                'topologies': 
                                                                    {0: 
                                                                        {'metric': 151,
                                                                        'mt_id': 0,
                                                                        'tos': 0}}}},
                                                        'header': 
                                                            {'adv_router': '3.3.3.3',
                                                            'age': 632,
                                                            'checksum': '0x5655',
                                                            'length': 28,
                                                            'lsa_id': '10.1.2.0',
                                                            'option': '0x2 (No TOS-capability, No DC)',
                                                           'seq_num': '0x80000002',
                                                           'type': 'Network Summary'}}},
                                                '10.1.3.0 3.3.3.3': 
                                                    {'ospfv2': 
                                                        {'body': 
                                                            {'summary': 
                                                                {'network_mask': '/24',
                                                                'topologies': 
                                                                    {0: 
                                                                        {'metric': 40,
                                                                        'mt_id': 0,
                                                                        'tos': 0}}}},
                                                        'header': 
                                                            {'adv_router': '3.3.3.3',
                                                            'age': 642,
                                                            'checksum': '0xf029',
                                                            'length': 28,
                                                            'lsa_id': '10.1.3.0',
                                                            'option': '0x2 (No TOS-capability, No DC)',
                                                           'seq_num': '0x80000002',
                                                           'type': 'Network Summary'}}},
                                                '10.2.3.0 2.2.2.2': 
                                                    {'ospfv2': 
                                                        {'body': 
                                                            {'summary': 
                                                                {'network_mask': '/24',
                                                                'topologies': 
                                                                    {0: 
                                                                        {'metric': 222,
                                                                        'mt_id': 0,
                                                                        'tos': 0}}}},
                                                        'header': 
                                                            {'adv_router': '2.2.2.2',
                                                            'age': 788,
                                                            'checksum': '0x4601',
                                                            'length': 28,
                                                            'lsa_id': '10.2.3.0',
                                                            'option': '0x22 (No TOS-capability, DC)',
                                                           'seq_num': '0x80000001',
                                                           'type': 'Network Summary'}}},
                                                '10.2.3.0 3.3.3.3': 
                                                    {'ospfv2': 
                                                        {'body': 
                                                            {'summary': 
                                                                {'network_mask': '/24',
                                                                'topologies': 
                                                                    {0: 
                                                                        {'metric': 262,
                                                                        'mt_id': 0,
                                                                        'tos': 0}}}},
                                                        'header': 
                                                            {'adv_router': '3.3.3.3',
                                                            'age': 397,
                                                            'checksum': '0x96a2',
                                                            'length': 28,
                                                            'lsa_id': '10.2.3.0',
                                                            'option': '0x2 (No TOS-capability, No DC)',
                                                            'seq_num': '0x80000003',
                                                            'type': 'Network Summary'}}},
                                                '2.2.2.2 2.2.2.2': 
                                                    {'ospfv2': 
                                                        {'body': 
                                                            {'summary': 
                                                                {'network_mask': '/32',
                                                                'topologies': 
                                                                    {0: 
                                                                        {'metric': 1,
                                                                        'mt_id': 0,
                                                                        'tos': 0}}}},
                                                        'header': 
                                                            {'adv_router': '2.2.2.2',
                                                            'age': 789,
                                                            'checksum': '0xfa31',
                                                            'length': 28,
                                                            'lsa_id': '2.2.2.2',
                                                            'option': '0x22 (No TOS-capability, DC)',
                                                            'seq_num': '0x80000001',
                                                            'type': 'Network Summary'}}},
                                                '20.1.3.0 1.1.1.1': 
                                                    {'ospfv2': 
                                                        {'body': 
                                                            {'summary': 
                                                                {'network_mask': '/24',
                                                                'topologies': 
                                                                    {0: 
                                                                        {'metric': 1,
                                                                        'mt_id': 0,
                                                                        'tos': 0}}}},
                                                        'header': 
                                                            {'adv_router': '1.1.1.1',
                                                            'age': 694,
                                                            'checksum': '0x43dc',
                                                            'length': 28,
                                                            'lsa_id': '20.1.3.0',
                                                            'option': '0x22 (No TOS-capability, DC)',
                                                            'seq_num': '0x80000001',
                                                            'type': 'Network Summary'}}},
                                                '20.1.3.0 3.3.3.3': 
                                                    {'ospfv2': 
                                                        {'body': 
                                                            {'summary': 
                                                                {'network_mask': '/24',
                                                                                                 'topologies': {0: {'metric': 40,
                                                                                                                    'mt_id': 0,
                                                                                                                    'tos': 0}}}},
                                                        'header': 
                                                            {'adv_router': '3.3.3.3',
                                                            'age': 642,
                                                            'checksum': '0x6ea1',
                                                            'length': 28,
                                                            'lsa_id': '20.1.3.0',
                                                            'option': '0x2 (No TOS-capability, No DC)',
                                                            'seq_num': '0x80000002',
                                                            'type': 'Network '
                                                            'Summary'}}},
                                                '20.2.3.0 3.3.3.3': 
                                                    {'ospfv2': 
                                                        {'body': 
                                                            {'summary': 
                                                                {'network_mask': '/24',
                                                                'topologies': 
                                                                    {0: 
                                                                        {'metric': 40,
                                                                        'mt_id': 0,
                                                                        'tos': 0}}}},
                                                        'header': 
                                                            {'adv_router': '3.3.3.3',
                                                            'age': 642,
                                                            'checksum': '0x62ac',
                                                            'length': 28,
                                                            'lsa_id': '20.2.3.0',
                                                            'option': '0x2 (No TOS-capability, No DC)',
                                                            'seq_num': '0x80000002',
                                                            'type': 'Network Summary'}}},
                                                '20.2.4.0 3.3.3.3': 
                                                    {'ospfv2': 
                                                        {'body': 
                                                            {'summary': 
                                                                {'network_mask': '/24',
                                                                'topologies': 
                                                                    {0: 
                                                                        {'metric': 41,
                                                                        'mt_id': 0,
                                                                        'tos': 0}}}},
                                                        'header': 
                                                            {'adv_router': '3.3.3.3',
                                                            'age': 401,
                                                            'checksum': '0x5dad',
                                                            'length': 28,
                                                            'lsa_id': '20.2.4.0',
                                                            'option': '0x2 (No TOS-capability, No DC)',
                                                            'seq_num': '0x80000004',
                                                            'type': 'Network Summary'}}},
                                                '20.3.4.0 3.3.3.3': 
                                                    {'ospfv2': 
                                                        {'body': 
                                                            {'summary': 
                                                                {'network_mask': '/24',
                                                                'topologies': 
                                                                    {0: 
                                                                        {'metric': 40,
                                                                        'mt_id': 0,
                                                                        'tos': 0}}}},
                                                        'header': 
                                                            {'adv_router': '3.3.3.3',
                                                            'age': 642,
                                                            'checksum': '0x4bc1',
                                                            'length': 28,
                                                            'lsa_id': '20.3.4.0',
                                                            'option': '0x2 (No TOS-capability, No DC)',
                                                            'seq_num': '0x80000002',
                                                            'type': 'Network Summary'}}},
                                                '3.3.3.3 3.3.3.3': 
                                                    {'ospfv2': 
                                                        {'body': 
                                                            {'summary': 
                                                                {'network_mask': '/32',
                                                                'topologies': 
                                                                    {0: 
                                                                        {'metric': 1,
                                                                        'mt_id': 0,
                                                                        'tos': 0}}}},
                                                        'header': 
                                                            {'adv_router': '3.3.3.3',
                                                            'age': 642,
                                                            'checksum': '0x8eb4',
                                                            'length': 28,
                                                            'lsa_id': '3.3.3.3',
                                                            'option': '0x2 (No TOS-capability, No DC)',
                                                          'seq_num': '0x80000002',
                                                          'type': 'Network Summary'}}},
                                                '4.4.4.4 3.3.3.3': 
                                                    {'ospfv2': 
                                                        {'body': 
                                                            {'summary': 
                                                                {'network_mask': '/32',
                                                                'topologies': 
                                                                    {0: 
                                                                        {'metric': 41,
                                                                        'mt_id': 0,
                                                                        'tos': 0}}}},
                                                        'header': 
                                                            {'adv_router': '3.3.3.3',
                                                            'age': 401,
                                                            'checksum': '0xef26',
                                                            'length': 28,
                                                            'lsa_id': '4.4.4.4',
                                                            'option': '0x2 (No TOS-capability, No DC)',
                                                          'seq_num': '0x80000003',
                                                          'type': 'Network Summary'}}},
                                                '44.44.44.44 4.4.4.4': 
                                                    {'ospfv2': 
                                                        {'body': 
                                                            {'summary': 
                                                                {'network_mask': '/32',
                                                                'topologies': 
                                                                    {0: 
                                                                        {'metric': 1,
                                                                        'mt_id': 0,
                                                                        'tos': 0}}}},
                                                        'header': 
                                                            {'adv_router': '4.4.4.4',
                                                            'age': 403,
                                                            'checksum': '0x2b50',
                                                            'length': 28,
                                                            'lsa_id': '44.44.44.44',
                                                            'option': '0x22 (No TOS-capability, DC)',
                                                            'seq_num': '0x80000001',
                                                            'type': 'Network Summary'}}}}}}}}}}}}}}

    golden_output1 = {'execute.return_value': '''
        R3_ospf_nx# show ip ospf database summary detail vrf all
        OSPF Router with ID (3.3.3.3) (Process ID 1 VRF default)

                Summary Network Link States (Area 0.0.0.0)

        LS age: 401
        Options: 0x2 (No TOS-capability, No DC)
        LS Type: Network Summary
        Link State ID: 4.4.4.4 (Network address)
        Advertising Router: 3.3.3.3
        LS Seq Number: 0x80000003
        Checksum: 0xef26
        Length: 28
        Network Mask: /32
          TOS:   0 Metric: 41

        LS age: 694
        Options: 0x22 (No TOS-capability, DC)
        LS Type: Network Summary
        Link State ID: 20.1.3.0 (Network address)
        Advertising Router: 1.1.1.1
        LS Seq Number: 0x80000001
        Checksum: 0x43dc
        Length: 28
        Network Mask: /24
          TOS:   0 Metric: 1

        LS age: 642
        Options: 0x2 (No TOS-capability, No DC)
        LS Type: Network Summary
        Link State ID: 20.1.3.0 (Network address)
        Advertising Router: 3.3.3.3
        LS Seq Number: 0x80000002
        Checksum: 0x6ea1
        Length: 28
        Network Mask: /24
          TOS:   0 Metric: 40

        LS age: 642
        Options: 0x2 (No TOS-capability, No DC)
        LS Type: Network Summary
        Link State ID: 20.2.3.0 (Network address)
        Advertising Router: 3.3.3.3
        LS Seq Number: 0x80000002
        Checksum: 0x62ac
        Length: 28
        Network Mask: /24
          TOS:   0 Metric: 40

        LS age: 401
        Options: 0x2 (No TOS-capability, No DC)
        LS Type: Network Summary
        Link State ID: 20.2.4.0 (Network address)
        Advertising Router: 3.3.3.3
        LS Seq Number: 0x80000004
        Checksum: 0x5dad
        Length: 28
        Network Mask: /24
          TOS:   0 Metric: 41

        LS age: 642
        Options: 0x2 (No TOS-capability, No DC)
        LS Type: Network Summary
        Link State ID: 20.3.4.0 (Network address)
        Advertising Router: 3.3.3.3
        LS Seq Number: 0x80000002
        Checksum: 0x4bc1
        Length: 28
        Network Mask: /24
          TOS:   0 Metric: 40


                    Summary Network Link States (Area 0.0.0.1)

        LS age: 789
        Options: 0x22 (No TOS-capability, DC)
        LS Type: Network Summary
        Link State ID: 2.2.2.2 (Network address)
        Advertising Router: 2.2.2.2
        LS Seq Number: 0x80000001
        Checksum: 0xfa31
        Length: 28
        Network Mask: /32
          TOS:   0 Metric: 1

        LS age: 642
        Options: 0x2 (No TOS-capability, No DC)
        LS Type: Network Summary
        Link State ID: 3.3.3.3 (Network address)
        Advertising Router: 3.3.3.3
        LS Seq Number: 0x80000002
        Checksum: 0x8eb4
        Length: 28
        Network Mask: /32
          TOS:   0 Metric: 1

        LS age: 788
        Options: 0x22 (No TOS-capability, DC)
        LS Type: Network Summary
        Link State ID: 10.1.2.0 (Network address)
        Advertising Router: 2.2.2.2
        LS Seq Number: 0x80000001
        Checksum: 0xfc54
        Length: 28
        Network Mask: /24
          TOS:   0 Metric: 4294

        LS age: 632
        Options: 0x2 (No TOS-capability, No DC)
        LS Type: Network Summary
        Link State ID: 10.1.2.0 (Network address)
        Advertising Router: 3.3.3.3
        LS Seq Number: 0x80000002
        Checksum: 0x5655
        Length: 28
        Network Mask: /24
          TOS:   0 Metric: 151

        LS age: 642
        Options: 0x2 (No TOS-capability, No DC)
        LS Type: Network Summary
        Link State ID: 10.1.3.0 (Network address)
        Advertising Router: 3.3.3.3
        LS Seq Number: 0x80000002
        Checksum: 0xf029
        Length: 28
        Network Mask: /24
          TOS:   0 Metric: 40

        LS age: 788
        Options: 0x22 (No TOS-capability, DC)
        LS Type: Network Summary
        Link State ID: 10.2.3.0 (Network address)
        Advertising Router: 2.2.2.2
        LS Seq Number: 0x80000001
        Checksum: 0x4601
        Length: 28
        Network Mask: /24
          TOS:   0 Metric: 222

        LS age: 397
        Options: 0x2 (No TOS-capability, No DC)
        LS Type: Network Summary
        Link State ID: 10.2.3.0 (Network address)
        Advertising Router: 3.3.3.3
        LS Seq Number: 0x80000003
        Checksum: 0x96a2
        Length: 28
        Network Mask: /24
          TOS:   0 Metric: 262

        LS age: 403
        Options: 0x22 (No TOS-capability, DC)
        LS Type: Network Summary
        Link State ID: 44.44.44.44 (Network address)
        Advertising Router: 4.4.4.4
        LS Seq Number: 0x80000001
        Checksum: 0x2b50
        Length: 28
        Network Mask: /32
          TOS:   0 Metric: 1
        '''}

    def test_full(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output1)
        obj = ShowIpOspfDatabaseSummaryDetail(device=self.device)
        parsed_output = obj.parse(vrf='all')
        self.assertEqual(parsed_output, self.golden_parsed_output1)

    def test_empty(self):
        self.maxDiff = None
        self.device = Mock(**self.empty_output)
        obj = ShowIpOspfDatabaseSummaryDetail(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()


# ============================================================
#  Unit test for 'show ip ospf database router detail vrf all'
# ============================================================
class test_show_ip_ospf_database_router_detail_vrf_all(unittest.TestCase):

    '''Unit test for "show ip ospf database router detail vrf all" '''

    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output1 = {
        "vrf": {
            "default": {
                "address_family": {
                    "ipv4": {
                        "instance": {
                            "1": {
                                "database": {
                                    "lsa_types": {
                                        "Router": {
                                            "lsas": {
                                                "3.3.3.3 3.3.3.3": {
                                                    "ospfv2": {
                                                        "header": {
                                                            "seq_num": "0x80000034",
                                                            "lsa_id": "3.3.3.3",
                                                            "checksum": "0x73f9",
                                                            "adv_router": "3.3.3.3",
                                                            "length": 60,
                                                            "type": "Router Links",
                                                            "option": "0x22 (No TOS-capability, DC)",
                                                            "age": 217
                                                        },
                                                        "body": {
                                                            "router": {
                                                                "num_of_links": 3,
                                                                "links": {
                                                                    "10.3.4.4": {
                                                                        "topologies": {
                                                                            0: {
                                                                                "tos": 0,
                                                                                "metric": 1,
                                                                                "mt_id": 0
                                                                            }
                                                                        },
                                                                        "type": "transit network",
                                                                        "link_data": "10.3.4.3",
                                                                        "link_id": "10.3.4.4",
                                                                        "num_tos_metrics": 0
                                                                    },
                                                                    "3.3.3.3": {
                                                                        "topologies": {
                                                                            0: {
                                                                                "tos": 0,
                                                                                "metric": 1,
                                                                                "mt_id": 0
                                                                            }
                                                                        },
                                                                        "type": "stub network",
                                                                        "link_data": "255.255.255.255",
                                                                        "link_id": "3.3.3.3",
                                                                        "num_tos_metrics": 0
                                                                    },
                                                                    "10.2.3.3": {
                                                                        "topologies": {
                                                                            0: {
                                                                                "tos": 0,
                                                                                "metric": 1,
                                                                                "mt_id": 0
                                                                            }
                                                                        },
                                                                        "type": "transit network",
                                                                        "link_data": "10.2.3.3",
                                                                        "link_id": "10.2.3.3",
                                                                        "num_tos_metrics": 0}}}}}},
                                                "1.1.1.1 1.1.1.1": {
                                                    "ospfv2": {
                                                        "header": {
                                                            "seq_num": "0x8000003e",
                                                            "lsa_id": "1.1.1.1",
                                                            "checksum": "0x6029",
                                                            "adv_router": "1.1.1.1",
                                                            "length": 60,
                                                            "type": "Router Links",
                                                            "option": "0x22 (No TOS-capability, DC)",
                                                            "age": 723
                                                        },
                                                        "body": {
                                                            "router": {
                                                                "num_of_links": 3,
                                                                "links": {
                                                                    "1.1.1.1": {
                                                                        "topologies": {
                                                                            0: {
                                                                                "mt_id": 0
                                                                            }
                                                                        },
                                                                        "type": "stub network",
                                                                        "link_data": "255.255.255.255",
                                                                        "link_id": "1.1.1.1",
                                                                        "num_tos_metrics": 0
                                                                    },
                                                                    "10.1.4.4": {
                                                                        "topologies": {
                                                                            0: {
                                                                                "tos": 0,
                                                                                "metric": 1,
                                                                                "mt_id": 0
                                                                            }
                                                                        },
                                                                        "type": "transit network",
                                                                        "link_data": "10.1.4.1",
                                                                        "link_id": "10.1.4.4",
                                                                        "num_tos_metrics": 0
                                                                    },
                                                                    "10.1.2.1": {
                                                                        "topologies": {
                                                                            0: {
                                                                                "tos": 0,
                                                                                "metric": 1,
                                                                                "mt_id": 0
                                                                            }
                                                                        },
                                                                        "type": "transit network",
                                                                        "link_data": "10.1.2.1",
                                                                        "link_id": "10.1.2.1",
                                                                        "num_tos_metrics": 0}}}}}},
                                                "2.2.2.2 2.2.2.2": {
                                                    "ospfv2": {
                                                        "header": {
                                                            "seq_num": "0x80000014",
                                                            "lsa_id": "2.2.2.2",
                                                            "checksum": "0x652b",
                                                            "adv_router": "2.2.2.2",
                                                            "length": 72,
                                                            "type": "Router Links",
                                                            "option": "0x2 (No TOS-capability, No DC)",
                                                            "age": 1683
                                                        },
                                                        "body": {
                                                            "router": {
                                                                "num_of_links": 4,
                                                                "links": {
                                                                    "10.2.4.4": {
                                                                        "topologies": {
                                                                            0: {
                                                                                "tos": 0,
                                                                                "metric": 1,
                                                                                "mt_id": 0
                                                                            }
                                                                        },
                                                                        "type": "transit network",
                                                                        "link_data": "10.2.4.2",
                                                                        "link_id": "10.2.4.4",
                                                                        "num_tos_metrics": 0
                                                                    },
                                                                    "2.2.2.2": {
                                                                        "topologies": {
                                                                            0: {
                                                                                "tos": 0,
                                                                                "metric": 1,
                                                                                "mt_id": 0
                                                                            }
                                                                        },
                                                                        "type": "stub network",
                                                                        "link_data": "255.255.255.255",
                                                                        "link_id": "2.2.2.2",
                                                                        "num_tos_metrics": 0
                                                                    },
                                                                    "10.1.2.1": {
                                                                        "topologies": {
                                                                            0: {
                                                                                "tos": 0,
                                                                                "metric": 1,
                                                                                "mt_id": 0
                                                                            }
                                                                        },
                                                                        "type": "transit network",
                                                                        "link_data": "10.1.2.2",
                                                                        "link_id": "10.1.2.1",
                                                                        "num_tos_metrics": 0
                                                                    },
                                                                    "10.2.3.3": {
                                                                        "topologies": {
                                                                            0: {
                                                                                "tos": 0,
                                                                                "metric": 1,
                                                                                "mt_id": 0
                                                                            }
                                                                        },
                                                                        "type": "transit network",
                                                                        "link_data": "10.2.3.2",
                                                                        "link_id": "10.2.3.3",
                                                                        "num_tos_metrics": 0}}}}}},
                                                "4.4.4.4 4.4.4.4": {
                                                    "ospfv2": {
                                                        "header": {
                                                            "seq_num": "0x80000037",
                                                            "lsa_id": "4.4.4.4",
                                                            "checksum": "0xa37d",
                                                            "adv_router": "4.4.4.4",
                                                            "length": 72,
                                                            "type": "Router Links",
                                                            "option": "0x22 (No TOS-capability, DC)",
                                                            "age": 1433
                                                        },
                                                        "body": {
                                                            "router": {
                                                                "num_of_links": 4,
                                                                "links": {
                                                                    "4.4.4.4": {
                                                                        "topologies": {
                                                                            0: {
                                                                                "tos": 0,
                                                                                "metric": 1,
                                                                                "mt_id": 0
                                                                            }
                                                                        },
                                                                        "type": "stub network",
                                                                        "link_data": "255.255.255.255",
                                                                        "link_id": "4.4.4.4",
                                                                        "num_tos_metrics": 0
                                                                    },
                                                                    "10.2.4.4": {
                                                                        "topologies": {
                                                                            0: {
                                                                                "tos": 0,
                                                                                "metric": 1,
                                                                                "mt_id": 0
                                                                            }
                                                                        },
                                                                        "type": "transit network",
                                                                        "link_data": "10.2.4.4",
                                                                        "link_id": "10.2.4.4",
                                                                        "num_tos_metrics": 0
                                                                    },
                                                                    "10.1.4.4": {
                                                                        "topologies": {
                                                                            0: {
                                                                                "tos": 0,
                                                                                "metric": 1,
                                                                                "mt_id": 0
                                                                            }
                                                                        },
                                                                        "type": "transit network",
                                                                        "link_data": "10.1.4.4",
                                                                        "link_id": "10.1.4.4",
                                                                        "num_tos_metrics": 0
                                                                    },
                                                                    "10.3.4.4": {
                                                                        "topologies": {
                                                                            0: {
                                                                                "tos": 0,
                                                                                "metric": 1,
                                                                                "mt_id": 0
                                                                            }
                                                                        },
                                                                        "type": "transit network",
                                                                        "link_data": "10.3.4.4",
                                                                        "link_id": "10.3.4.4",
                                                                        "num_tos_metrics": 0}}}}}}}}}}}}}}},
            "VRF1": {
                "address_family": {
                    "ipv4": {
                        "instance": {
                            "1": {
                                "database": {
                                    "lsa_types": {
                                        "Router": {
                                            "lsas": {
                                                "11.11.11.11 11.11.11.11": {
                                                    "ospfv2": {
                                                        "header": {
                                                            "seq_num": "0x8000003f",
                                                            "lsa_id": "11.11.11.11",
                                                            "checksum": "0x9ae4",
                                                            "adv_router": "11.11.11.11",
                                                            "length": 48,
                                                            "type": "Router Links",
                                                            "option": "0x22 (No TOS-capability, DC)",
                                                            "age": 646
                                                        },
                                                        "body": {
                                                            "router": {
                                                                "num_of_links": 2,
                                                                "links": {
                                                                    "22.22.22.22": {
                                                                        "topologies": {
                                                                            0: {
                                                                                "tos": 0,
                                                                                "metric": 1,
                                                                                "mt_id": 0
                                                                            }
                                                                        },
                                                                        "type": "router (point-to-point)",
                                                                        "link_data": "0.0.0.14",
                                                                        "link_id": "22.22.22.22",
                                                                        "num_tos_metrics": 0
                                                                    },
                                                                    "20.1.5.1": {
                                                                        "topologies": {
                                                                            0: {
                                                                                "tos": 0,
                                                                                "metric": 111,
                                                                                "mt_id": 0
                                                                            }
                                                                        },
                                                                        "type": "transit network",
                                                                        "link_data": "20.1.5.1",
                                                                        "link_id": "20.1.5.1",
                                                                        "num_tos_metrics": 0}}}}}},
                                                "66.66.66.66 66.66.66.66": {
                                                    "ospfv2": {
                                                        "header": {
                                                            "seq_num": "0x8000003d",
                                                            "lsa_id": "66.66.66.66",
                                                            "checksum": "0x1083",
                                                            "adv_router": "66.66.66.66",
                                                            "length": 72,
                                                            "type": "Router Links",
                                                            "option": "0x22 (No TOS-capability, DC)",
                                                            "age": 524
                                                        },
                                                        "body": {
                                                            "router": {
                                                                "num_of_links": 4,
                                                                "links": {
                                                                    "66.66.66.66": {
                                                                        "topologies": {
                                                                            0: {
                                                                                "tos": 0,
                                                                                "metric": 1,
                                                                                "mt_id": 0
                                                                            }
                                                                        },
                                                                        "type": "stub network",
                                                                        "link_data": "255.255.255.255",
                                                                        "link_id": "66.66.66.66",
                                                                        "num_tos_metrics": 0
                                                                    },
                                                                    "20.2.6.6": {
                                                                        "topologies": {
                                                                            0: {
                                                                                "tos": 0,
                                                                                "metric": 30,
                                                                                "mt_id": 0
                                                                            }
                                                                        },
                                                                        "type": "transit network",
                                                                        "link_data": "20.2.6.6",
                                                                        "link_id": "20.2.6.6",
                                                                        "num_tos_metrics": 0
                                                                    },
                                                                    "20.6.7.6": {
                                                                        "topologies": {
                                                                            0: {
                                                                                "tos": 0,
                                                                                "metric": 1,
                                                                                "mt_id": 0
                                                                            }
                                                                        },
                                                                        "type": "transit network",
                                                                        "link_data": "20.6.7.6",
                                                                        "link_id": "20.6.7.6",
                                                                        "num_tos_metrics": 0
                                                                    },
                                                                    "20.5.6.6": {
                                                                        "topologies": {
                                                                            0: {
                                                                                "tos": 0,
                                                                                "metric": 1,
                                                                                "mt_id": 0
                                                                            }
                                                                        },
                                                                        "type": "transit network",
                                                                        "link_data": "20.5.6.6",
                                                                        "link_id": "20.5.6.6",
                                                                        "num_tos_metrics": 0}}}}}},
                                                "55.55.55.55 55.55.55.55": {
                                                    "ospfv2": {
                                                        "header": {
                                                            "seq_num": "0x80000038",
                                                            "lsa_id": "55.55.55.55",
                                                            "checksum": "0xe5bd",
                                                            "adv_router": "55.55.55.55",
                                                            "length": 60,
                                                            "type": "Router Links",
                                                            "option": "0x22 (No TOS-capability, DC)",
                                                            "age": 304
                                                        },
                                                        "body": {
                                                            "router": {
                                                                "num_of_links": 3,
                                                                "links": {
                                                                    "55.55.55.55": {
                                                                        "topologies": {
                                                                            0: {
                                                                                "tos": 0,
                                                                                "metric": 1,
                                                                                "mt_id": 0
                                                                            }
                                                                        },
                                                                        "type": "stub network",
                                                                        "link_data": "255.255.255.255",
                                                                        "link_id": "55.55.55.55",
                                                                        "num_tos_metrics": 0
                                                                    },
                                                                    "20.1.5.1": {
                                                                        "topologies": {
                                                                            0: {
                                                                                "tos": 0,
                                                                                "metric": 30,
                                                                                "mt_id": 0
                                                                            }
                                                                        },
                                                                        "type": "transit network",
                                                                        "link_data": "20.1.5.5",
                                                                        "link_id": "20.1.5.1",
                                                                        "num_tos_metrics": 0
                                                                    },
                                                                    "20.5.6.6": {
                                                                        "topologies": {
                                                                            0: {
                                                                                "tos": 0,
                                                                                "metric": 1,
                                                                                "mt_id": 0
                                                                            }
                                                                        },
                                                                        "type": "transit network",
                                                                        "link_data": "20.5.6.5",
                                                                        "link_id": "20.5.6.6",
                                                                        "num_tos_metrics": 0}}}}}},
                                                "77.77.77.77 77.77.77.77": {
                                                    "ospfv2": {
                                                        "header": {
                                                            "seq_num": "0x80000031",
                                                            "lsa_id": "77.77.77.77",
                                                            "checksum": "0x117a",
                                                            "adv_router": "77.77.77.77",
                                                            "length": 60,
                                                            "type": "Router Links",
                                                            "option": "0x22 (No TOS-capability, DC)",
                                                            "age": 237
                                                        },
                                                        "body": {
                                                            "router": {
                                                                "num_of_links": 3,
                                                                "links": {
                                                                    "20.6.7.6": {
                                                                        "topologies": {
                                                                            0: {
                                                                                "tos": 0,
                                                                                "metric": 1,
                                                                                "mt_id": 0
                                                                            }
                                                                        },
                                                                        "type": "transit network",
                                                                        "link_data": "20.6.7.7",
                                                                        "link_id": "20.6.7.6",
                                                                        "num_tos_metrics": 0
                                                                    },
                                                                    "20.3.7.7": {
                                                                        "topologies": {
                                                                            0: {
                                                                                "tos": 0,
                                                                                "metric": 30,
                                                                                "mt_id": 0
                                                                            }
                                                                        },
                                                                        "type": "transit network",
                                                                        "link_data": "20.3.7.7",
                                                                        "link_id": "20.3.7.7",
                                                                        "num_tos_metrics": 0
                                                                    },
                                                                    "77.77.77.77": {
                                                                        "topologies": {
                                                                            0: {
                                                                                "tos": 0,
                                                                                "metric": 30,
                                                                                "mt_id": 0
                                                                            }
                                                                        },
                                                                        "type": "stub network",
                                                                        "link_data": "255.255.255.255",
                                                                        "link_id": "77.77.77.77",
                                                                        "num_tos_metrics": 0}}}}}},
                                                "22.22.22.22 22.22.22.22": {
                                                    "ospfv2": {
                                                        "header": {
                                                            "seq_num": "0x8000001a",
                                                            "lsa_id": "22.22.22.22",
                                                            "checksum": "0xc21b",
                                                            "adv_router": "22.22.22.22",
                                                            "length": 48,
                                                            "type": "Router Links",
                                                            "option": "0x2 (No TOS-capability, No DC)",
                                                            "age": 642
                                                        },
                                                        "body": {
                                                            "router": {
                                                                "num_of_links": 2,
                                                                "links": {
                                                                    "20.2.6.6": {
                                                                        "topologies": {
                                                                            0: {
                                                                                "tos": 0,
                                                                                "metric": 1,
                                                                                "mt_id": 0
                                                                            }
                                                                        },
                                                                        "type": "transit network",
                                                                        "link_data": "20.2.6.2",
                                                                        "link_id": "20.2.6.6",
                                                                        "num_tos_metrics": 0
                                                                    },
                                                                    "11.11.11.11": {
                                                                        "topologies": {
                                                                            0: {
                                                                                "tos": 0,
                                                                                "metric": 40,
                                                                                "mt_id": 0
                                                                            }
                                                                        },
                                                                        "type": "router (point-to-point)",
                                                                        "link_data": "0.0.0.6",
                                                                        "link_id": "11.11.11.11",
                                                                        "num_tos_metrics": 0}}}}}},
                                                "3.3.3.3 3.3.3.3": {
                                                    "ospfv2": {
                                                        "header": {
                                                            "seq_num": "0x80000036",
                                                            "lsa_id": "3.3.3.3",
                                                            "checksum": "0x5646",
                                                            "adv_router": "3.3.3.3",
                                                            "length": 36,
                                                            "type": "Router Links",
                                                            "option": "0x22 (No TOS-capability, DC)",
                                                            "age": 1148
                                                        },
                                                        "body": {
                                                            "router": {
                                                                "num_of_links": 1,
                                                                "links": {
                                                                    "20.3.7.7": {
                                                                        "topologies": {
                                                                            0: {
                                                                                "tos": 0,
                                                                                "metric": 1,
                                                                                "mt_id": 0
                                                                            }
                                                                        },
                                                                        "type": "transit network",
                                                                        "link_data": "20.3.7.3",
                                                                        "link_id": "20.3.7.7",
                                                                        "num_tos_metrics": 0}}}}}}}}}}}}}}}}}

    golden_output1 = {'execute.return_value': '''
        R2_ospf_nx# show ip ospf database router detail vrf all
        OSPF Router with ID (2.2.2.2) (Process ID 1 VRF default)

                Router Link States (Area 0.0.0.0)

        LS age: 723
        Options: 0x22 (No TOS-capability, DC)
        LS Type: Router Links
        Link State ID: 1.1.1.1 
        Advertising Router: 1.1.1.1
        LS Seq Number: 0x8000003e
        Checksum: 0x6029
        Length: 60
        Number of links: 3

         Link connected to: a Stub Network
          (Link ID) Network/Subnet Number: 1.1.1.1
          (Link Data) Network Mask: 255.255.255.255
           Number of TOS metrics: 0
             TOS   0 Metric: 1

         Link connected to: a Transit Network
          (Link ID) Designated Router address: 10.1.2.1
          (Link Data) Router Interface address: 10.1.2.1
           Number of TOS metrics: 0
             TOS   0 Metric: 1

         Link connected to: a Transit Network
          (Link ID) Designated Router address: 10.1.4.4
          (Link Data) Router Interface address: 10.1.4.1
           Number of TOS metrics: 0
             TOS   0 Metric: 1

        LS age: 1683
        Options: 0x2 (No TOS-capability, No DC)
        LS Type: Router Links
        Link State ID: 2.2.2.2 
        Advertising Router: 2.2.2.2
        LS Seq Number: 0x80000014
        Checksum: 0x652b
        Length: 72
        Number of links: 4

         Link connected to: a Stub Network
          (Link ID) Network/Subnet Number: 2.2.2.2
          (Link Data) Network Mask: 255.255.255.255
           Number of TOS metrics: 0
             TOS   0 Metric: 1

         Link connected to: a Transit Network
          (Link ID) Designated Router address: 10.2.3.3
          (Link Data) Router Interface address: 10.2.3.2
           Number of TOS metrics: 0
             TOS   0 Metric: 1

         Link connected to: a Transit Network
          (Link ID) Designated Router address: 10.2.4.4
          (Link Data) Router Interface address: 10.2.4.2
           Number of TOS metrics: 0
             TOS   0 Metric: 1

         Link connected to: a Transit Network
          (Link ID) Designated Router address: 10.1.2.1
          (Link Data) Router Interface address: 10.1.2.2
           Number of TOS metrics: 0
             TOS   0 Metric: 1

        LS age: 217
        Options: 0x22 (No TOS-capability, DC)
        LS Type: Router Links
        Link State ID: 3.3.3.3 
        Advertising Router: 3.3.3.3
        LS Seq Number: 0x80000034
        Checksum: 0x73f9
        Length: 60
        Number of links: 3

         Link connected to: a Stub Network
          (Link ID) Network/Subnet Number: 3.3.3.3
          (Link Data) Network Mask: 255.255.255.255
           Number of TOS metrics: 0
             TOS   0 Metric: 1

         Link connected to: a Transit Network
          (Link ID) Designated Router address: 10.3.4.4
          (Link Data) Router Interface address: 10.3.4.3
           Number of TOS metrics: 0
             TOS   0 Metric: 1

         Link connected to: a Transit Network
          (Link ID) Designated Router address: 10.2.3.3
          (Link Data) Router Interface address: 10.2.3.3
           Number of TOS metrics: 0
             TOS   0 Metric: 1

        LS age: 1433
        Options: 0x22 (No TOS-capability, DC)
        LS Type: Router Links
        Link State ID: 4.4.4.4 
        Advertising Router: 4.4.4.4
        LS Seq Number: 0x80000037
        Checksum: 0xa37d
        Length: 72
        AS border router
        Number of links: 4

         Link connected to: a Stub Network
          (Link ID) Network/Subnet Number: 4.4.4.4
          (Link Data) Network Mask: 255.255.255.255
           Number of TOS metrics: 0
             TOS   0 Metric: 1

         Link connected to: a Transit Network
          (Link ID) Designated Router address: 10.2.4.4
          (Link Data) Router Interface address: 10.2.4.4
           Number of TOS metrics: 0
             TOS   0 Metric: 1

         Link connected to: a Transit Network
          (Link ID) Designated Router address: 10.3.4.4
          (Link Data) Router Interface address: 10.3.4.4
           Number of TOS metrics: 0
             TOS   0 Metric: 1

         Link connected to: a Transit Network
          (Link ID) Designated Router address: 10.1.4.4
          (Link Data) Router Interface address: 10.1.4.4
           Number of TOS metrics: 0
             TOS   0 Metric: 1


            OSPF Router with ID (22.22.22.22) (Process ID 1 VRF VRF1)

                    Router Link States (Area 0.0.0.1)

        LS age: 1148
        Options: 0x22 (No TOS-capability, DC)
        LS Type: Router Links
        Link State ID: 3.3.3.3 
        Advertising Router: 3.3.3.3
        LS Seq Number: 0x80000036
        Checksum: 0x5646
        Length: 36
        Area border router
        AS border router
        Number of links: 1

         Link connected to: a Transit Network
          (Link ID) Designated Router address: 20.3.7.7
          (Link Data) Router Interface address: 20.3.7.3
           Number of TOS metrics: 0
             TOS   0 Metric: 1

        LS age: 646
        Options: 0x22 (No TOS-capability, DC)
        LS Type: Router Links
        Link State ID: 11.11.11.11 
        Advertising Router: 11.11.11.11
        LS Seq Number: 0x8000003f
        Checksum: 0x9ae4
        Length: 48
        Area border router
        AS border router
        Number of links: 2

         Link connected to: a Router (point-to-point)
         (Link ID) Neighboring Router ID: 22.22.22.22
         (Link Data) Router Interface address: 0.0.0.14
           Number of TOS metrics: 0
             TOS   0 Metric: 111

         Link connected to: a Transit Network
          (Link ID) Designated Router address: 20.1.5.1
          (Link Data) Router Interface address: 20.1.5.1
           Number of TOS metrics: 0
             TOS   0 Metric: 1

        LS age: 642
        Options: 0x2 (No TOS-capability, No DC)
        LS Type: Router Links
        Link State ID: 22.22.22.22 
        Advertising Router: 22.22.22.22
        LS Seq Number: 0x8000001a
        Checksum: 0xc21b
        Length: 48
        Area border router
        AS border router
        Number of links: 2

         Link connected to: a Transit Network
          (Link ID) Designated Router address: 20.2.6.6
          (Link Data) Router Interface address: 20.2.6.2
           Number of TOS metrics: 0
             TOS   0 Metric: 40

         Link connected to: a Router (point-to-point)
         (Link ID) Neighboring Router ID: 11.11.11.11
         (Link Data) Router Interface address: 0.0.0.6
           Number of TOS metrics: 0
             TOS   0 Metric: 1

        LS age: 304
        Options: 0x22 (No TOS-capability, DC)
        LS Type: Router Links
        Link State ID: 55.55.55.55 
        Advertising Router: 55.55.55.55
        LS Seq Number: 0x80000038
        Checksum: 0xe5bd
        Length: 60
        Number of links: 3

         Link connected to: a Stub Network
          (Link ID) Network/Subnet Number: 55.55.55.55
          (Link Data) Network Mask: 255.255.255.255
           Number of TOS metrics: 0
             TOS   0 Metric: 1

         Link connected to: a Transit Network
          (Link ID) Designated Router address: 20.5.6.6
          (Link Data) Router Interface address: 20.5.6.5
           Number of TOS metrics: 0
             TOS   0 Metric: 30

         Link connected to: a Transit Network
          (Link ID) Designated Router address: 20.1.5.1
          (Link Data) Router Interface address: 20.1.5.5
           Number of TOS metrics: 0
             TOS   0 Metric: 1

        LS age: 524
        Options: 0x22 (No TOS-capability, DC)
        LS Type: Router Links
        Link State ID: 66.66.66.66 
        Advertising Router: 66.66.66.66
        LS Seq Number: 0x8000003d
        Checksum: 0x1083
        Length: 72
        Number of links: 4

         Link connected to: a Stub Network
          (Link ID) Network/Subnet Number: 66.66.66.66
          (Link Data) Network Mask: 255.255.255.255
           Number of TOS metrics: 0
             TOS   0 Metric: 1

         Link connected to: a Transit Network
          (Link ID) Designated Router address: 20.6.7.6
          (Link Data) Router Interface address: 20.6.7.6
           Number of TOS metrics: 0
             TOS   0 Metric: 30

         Link connected to: a Transit Network
          (Link ID) Designated Router address: 20.2.6.6
          (Link Data) Router Interface address: 20.2.6.6
           Number of TOS metrics: 0
             TOS   0 Metric: 1

         Link connected to: a Transit Network
          (Link ID) Designated Router address: 20.5.6.6
          (Link Data) Router Interface address: 20.5.6.6
           Number of TOS metrics: 0
             TOS   0 Metric: 30

        LS age: 237
        Options: 0x22 (No TOS-capability, DC)
        LS Type: Router Links
        Link State ID: 77.77.77.77 
        Advertising Router: 77.77.77.77
        LS Seq Number: 0x80000031
        Checksum: 0x117a
        Length: 60
        Number of links: 3

         Link connected to: a Stub Network
          (Link ID) Network/Subnet Number: 77.77.77.77
          (Link Data) Network Mask: 255.255.255.255
           Number of TOS metrics: 0
             TOS   0 Metric: 1

         Link connected to: a Transit Network
          (Link ID) Designated Router address: 20.6.7.6
          (Link Data) Router Interface address: 20.6.7.7
           Number of TOS metrics: 0
             TOS   0 Metric: 30

         Link connected to: a Transit Network
          (Link ID) Designated Router address: 20.3.7.7
          (Link Data) Router Interface address: 20.3.7.7
           Number of TOS metrics: 0
             TOS   0 Metric: 1
        '''}

    def test_full(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output1)
        obj = ShowIpOspfDatabaseRouterDetail(device=self.device)
        parsed_output = obj.parse(vrf='all')
        self.assertEqual(parsed_output, self.golden_parsed_output1)

    def test_empty(self):
        self.maxDiff = None
        self.device = Mock(**self.empty_output)
        obj = ShowIpOspfDatabaseRouterDetail(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()


# =================================================================
#  Unit test for 'show ip ospf database opaque-area detail vrf all'
# =================================================================
class test_show_ip_ospf_database_opaque_area_detail_vrf_all(unittest.TestCase):

    '''Unit test for "show ip ospf database opaque-area detail vrf all" '''

    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output1 = {
        'vrf': 
            {'default': 
                {'address_family': 
                    {'ipv4': 
                        {'instance': 
                            {'1': 
                                {'database': {'lsa_types': {'Opaque Area': {'lsas': {'1.0.0.0 1.1.1.1': {'ospfv2': {'body': {'opaque': {}},
                                                                                                                                                       'header': {'adv_router': '1.1.1.1',
                                                                                                                                                                  'age': 385,
                                                                                                                                                                  'checksum': '0x54d3',
                                                                                                                                                                  'fragment_number': 0,
                                                                                                                                                                  'length': 28,
                                                                                                                                                                  'lsa_id': '1.0.0.0',
                                                                                                                                                                  'mpls_te_router_id': '1.1.1.1',
                                                                                                                                                                  'num_links': 0,
                                                                                                                                                                  'opaque_id': 0,
                                                                                                                                                                  'opaque_type': 1,
                                                                                                                                                                  'option': '0x20 '
                                                                                                                                                                            '(No '
                                                                                                                                                                            'TOS-capability, '
                                                                                                                                                                            'DC)',
                                                                                                                                                                  'seq_num': '0x80000003',
                                                                                                                                                                  'type': 'Opaque '
                                                                                                                                                                          'Area '
                                                                                                                                                                          'Link'}}},
                                                                                                                        '1.0.0.0 2.2.2.2': {'ospfv2': {'body': {'opaque': {}},
                                                                                                                                                       'header': {'adv_router': '2.2.2.2',
                                                                                                                                                                  'age': 1612,
                                                                                                                                                                  'checksum': '0x1c22',
                                                                                                                                                                  'fragment_number': 0,
                                                                                                                                                                  'length': 28,
                                                                                                                                                                  'lsa_id': '1.0.0.0',
                                                                                                                                                                  'mpls_te_router_id': '2.2.2.2',
                                                                                                                                                                  'num_links': 0,
                                                                                                                                                                  'opaque_id': 0,
                                                                                                                                                                  'opaque_type': 1,
                                                                                                                                                                  'option': '0x2 '
                                                                                                                                                                            '(No '
                                                                                                                                                                            'TOS-capability, '
                                                                                                                                                                            'No '
                                                                                                                                                                            'DC)',
                                                                                                                                                                  'seq_num': '0x80000003',
                                                                                                                                                                  'type': 'Opaque '
                                                                                                                                                                          'Area '
                                                                                                                                                                          'Link'}}},
                                                                                                                        '1.0.0.0 3.3.3.3': {'ospfv2': {'body': {'opaque': {}},
                                                                                                                                                       'header': {'adv_router': '3.3.3.3',
                                                                                                                                                                  'age': 113,
                                                                                                                                                                  'checksum': '0x5cbb',
                                                                                                                                                                  'fragment_number': 0,
                                                                                                                                                                  'length': 28,
                                                                                                                                                                  'lsa_id': '1.0.0.0',
                                                                                                                                                                  'mpls_te_router_id': '3.3.3.3',
                                                                                                                                                                  'num_links': 0,
                                                                                                                                                                  'opaque_id': 0,
                                                                                                                                                                  'opaque_type': 1,
                                                                                                                                                                  'option': '0x20 '
                                                                                                                                                                            '(No '
                                                                                                                                                                            'TOS-capability, '
                                                                                                                                                                            'DC)',
                                                                                                                                                                  'seq_num': '0x80000003',
                                                                                                                                                                  'type': 'Opaque '
                                                                                                                                                                          'Area '
                                                                                                                                                                          'Link'}}},
                                                                                                                        '1.0.0.1 1.1.1.1': {'ospfv2': {'body': {'opaque': {'link_tlvs': {1: {'admin_group': '0x0',
                                                                                                                                                                                             'link_id': '10.1.4.4',
                                                                                                                                                                                             'link_name': 'Broadcast '
                                                                                                                                                                                                          'network',
                                                                                                                                                                                             'link_type': 2,
                                                                                                                                                                                             'local_if_ipv4_addrs': {'10.1.4.1': {}},
                                                                                                                                                                                             'max_bandwidth': 125000000,
                                                                                                                                                                                             'max_reservable_bandwidth': 93750000,
                                                                                                                                                                                             'remote_if_ipv4_addrs': {'0.0.0.0': {}},
                                                                                                                                                                                             'te_metric': 1,
                                                                                                                                                                                             'unknown_tlvs': {1: {'length': 4,
                                                                                                                                                                                                                  'type': 32770,
                                                                                                                                                                                                                  'value': '00 '
                                                                                                                                                                                                                           '00 '
                                                                                                                                                                                                                           '00 '
                                                                                                                                                                                                                           '01'}},
                                                                                                                                                                                             'unreserved_bandwidths': {'0 93750000': {'priority': 0,
                                                                                                                                                                                                                                      'unreserved_bandwidth': 93750000},
                                                                                                                                                                                                                       '1 93750000': {'priority': 1,
                                                                                                                                                                                                                                      'unreserved_bandwidth': 93750000},
                                                                                                                                                                                                                       '2 93750000': {'priority': 2,
                                                                                                                                                                                                                                      'unreserved_bandwidth': 93750000},
                                                                                                                                                                                                                       '3 93750000': {'priority': 3,
                                                                                                                                                                                                                                      'unreserved_bandwidth': 93750000},
                                                                                                                                                                                                                       '4 93750000': {'priority': 4,
                                                                                                                                                                                                                                      'unreserved_bandwidth': 93750000},
                                                                                                                                                                                                                       '5 93750000': {'priority': 5,
                                                                                                                                                                                                                                      'unreserved_bandwidth': 93750000},
                                                                                                                                                                                                                       '6 93750000': {'priority': 6,
                                                                                                                                                                                                                                      'unreserved_bandwidth': 93750000},
                                                                                                                                                                                                                       '7 93750000': {'priority': 7,
                                                                                                                                                                                                                                      'unreserved_bandwidth': 93750000}}}}}},
                                                                                                                                                       'header': {'adv_router': '1.1.1.1',
                                                                                                                                                                  'age': 385,
                                                                                                                                                                  'checksum': '0x6387',
                                                                                                                                                                  'fragment_number': 1,
                                                                                                                                                                  'length': 124,
                                                                                                                                                                  'lsa_id': '1.0.0.1',
                                                                                                                                                                  'num_links': 1,
                                                                                                                                                                  'opaque_id': 1,
                                                                                                                                                                  'opaque_type': 1,
                                                                                                                                                                  'option': '0x20 '
                                                                                                                                                                            '(No '
                                                                                                                                                                            'TOS-capability, '
                                                                                                                                                                            'DC)',
                                                                                                                                                                  'seq_num': '0x80000003',
                                                                                                                                                                  'type': 'Opaque '
                                                                                                                                                                          'Area '
                                                                                                                                                                          'Link'}}},
                                                                                                                        '1.0.0.2 1.1.1.1': {'ospfv2': {'body': {'opaque': {'link_tlvs': {1: {'admin_group': '0x0',
                                                                                                                                                                                             'link_id': '10.1.2.1',
                                                                                                                                                                                             'link_name': 'Broadcast '
                                                                                                                                                                                                          'network',
                                                                                                                                                                                             'link_type': 2,
                                                                                                                                                                                             'local_if_ipv4_addrs': {'10.1.2.1': {}},
                                                                                                                                                                                             'max_bandwidth': 125000000,
                                                                                                                                                                                             'max_reservable_bandwidth': 93750000,
                                                                                                                                                                                             'remote_if_ipv4_addrs': {'0.0.0.0': {}},
                                                                                                                                                                                             'te_metric': 1,
                                                                                                                                                                                             'unknown_tlvs': {1: {'length': 4,
                                                                                                                                                                                                                  'type': 32770,
                                                                                                                                                                                                                  'value': '00 '
                                                                                                                                                                                                                           '00 '
                                                                                                                                                                                                                           '00 '
                                                                                                                                                                                                                           '01'}},
                                                                                                                                                                                             'unreserved_bandwidths': {'0 93750000': {'priority': 0,
                                                                                                                                                                                                                                      'unreserved_bandwidth': 93750000},
                                                                                                                                                                                                                       '1 93750000': {'priority': 1,
                                                                                                                                                                                                                                      'unreserved_bandwidth': 93750000},
                                                                                                                                                                                                                       '2 93750000': {'priority': 2,
                                                                                                                                                                                                                                      'unreserved_bandwidth': 93750000},
                                                                                                                                                                                                                       '3 93750000': {'priority': 3,
                                                                                                                                                                                                                                      'unreserved_bandwidth': 93750000},
                                                                                                                                                                                                                       '4 93750000': {'priority': 4,
                                                                                                                                                                                                                                      'unreserved_bandwidth': 93750000},
                                                                                                                                                                                                                       '5 93750000': {'priority': 5,
                                                                                                                                                                                                                                      'unreserved_bandwidth': 93750000},
                                                                                                                                                                                                                       '6 93750000': {'priority': 6,
                                                                                                                                                                                                                                      'unreserved_bandwidth': 93750000},
                                                                                                                                                                                                                       '7 93750000': {'priority': 7,
                                                                                                                                                                                                                                      'unreserved_bandwidth': 93750000}}}}}},
                                                                                                                                                       'header': {'adv_router': '1.1.1.1',
                                                                                                                                                                  'age': 385,
                                                                                                                                                                  'checksum': '0xb23e',
                                                                                                                                                                  'fragment_number': 2,
                                                                                                                                                                  'length': 124,
                                                                                                                                                                  'lsa_id': '1.0.0.2',
                                                                                                                                                                  'num_links': 1,
                                                                                                                                                                  'opaque_id': 2,
                                                                                                                                                                  'opaque_type': 1,
                                                                                                                                                                  'option': '0x20 '
                                                                                                                                                                            '(No '
                                                                                                                                                                            'TOS-capability, '
                                                                                                                                                                            'DC)',
                                                                                                                                                                  'seq_num': '0x80000003',
                                                                                                                                                                  'type': 'Opaque '
                                                                                                                                                                          'Area '
                                                                                                                                                                          'Link'}}},
                                                                                                                        '1.0.0.37 2.2.2.2': {'ospfv2': {'body': {'opaque': {'link_tlvs': {1: {'admin_group': '0x0',
                                                                                                                                                                                              'link_id': '10.2.3.3',
                                                                                                                                                                                              'link_name': 'Broadcast '
                                                                                                                                                                                                           'network',
                                                                                                                                                                                              'link_type': 2,
                                                                                                                                                                                              'local_if_ipv4_addrs': {'10.2.3.2': {}},
                                                                                                                                                                                              'max_bandwidth': 125000000,
                                                                                                                                                                                              'max_reservable_bandwidth': 93750000,
                                                                                                                                                                                              'remote_if_ipv4_addrs': {'0.0.0.0': {}},
                                                                                                                                                                                              'te_metric': 1,
                                                                                                                                                                                              'unreserved_bandwidths': {'0 93750000': {'priority': 0,
                                                                                                                                                                                                                                       'unreserved_bandwidth': 93750000},
                                                                                                                                                                                                                        '1 93750000': {'priority': 1,
                                                                                                                                                                                                                                       'unreserved_bandwidth': 93750000},
                                                                                                                                                                                                                        '2 93750000': {'priority': 2,
                                                                                                                                                                                                                                       'unreserved_bandwidth': 93750000},
                                                                                                                                                                                                                        '3 93750000': {'priority': 3,
                                                                                                                                                                                                                                       'unreserved_bandwidth': 93750000},
                                                                                                                                                                                                                        '4 93750000': {'priority': 4,
                                                                                                                                                                                                                                       'unreserved_bandwidth': 93750000},
                                                                                                                                                                                                                        '5 93750000': {'priority': 5,
                                                                                                                                                                                                                                       'unreserved_bandwidth': 93750000},
                                                                                                                                                                                                                        '6 93750000': {'priority': 6,
                                                                                                                                                                                                                                       'unreserved_bandwidth': 93750000},
                                                                                                                                                                                                                        '7 93750000': {'priority': 7,
                                                                                                                                                                                                                                       'unreserved_bandwidth': 93750000}}}}}},
                                                                                                                                                        'header': {'adv_router': '2.2.2.2',
                                                                                                                                                                   'age': 1202,
                                                                                                                                                                   'checksum': '0xe492',
                                                                                                                                                                   'fragment_number': 37,
                                                                                                                                                                   'length': 116,
                                                                                                                                                                   'lsa_id': '1.0.0.37',
                                                                                                                                                                   'num_links': 1,
                                                                                                                                                                   'opaque_id': 37,
                                                                                                                                                                   'opaque_type': 1,
                                                                                                                                                                   'option': '0x2 '
                                                                                                                                                                             '(No '
                                                                                                                                                                             'TOS-capability, '
                                                                                                                                                                             'No '
                                                                                                                                                                             'DC)',
                                                                                                                                                                   'seq_num': '0x80000004',
                                                                                                                                                                   'type': 'Opaque '
                                                                                                                                                                           'Area '
                                                                                                                                                                           'Link'}}},
                                                                                                                        '1.0.0.38 2.2.2.2': {'ospfv2': {'body': {'opaque': {'link_tlvs': {1: {'admin_group': '0x0',
                                                                                                                                                                                              'link_id': '10.2.4.4',
                                                                                                                                                                                              'link_name': 'Broadcast '
                                                                                                                                                                                                           'network',
                                                                                                                                                                                              'link_type': 2,
                                                                                                                                                                                              'local_if_ipv4_addrs': {'10.2.4.2': {}},
                                                                                                                                                                                              'max_bandwidth': 125000000,
                                                                                                                                                                                              'max_reservable_bandwidth': 93750000,
                                                                                                                                                                                              'remote_if_ipv4_addrs': {'0.0.0.0': {}},
                                                                                                                                                                                              'te_metric': 1,
                                                                                                                                                                                              'unreserved_bandwidths': {'0 93750000': {'priority': 0,
                                                                                                                                                                                                                                       'unreserved_bandwidth': 93750000},
                                                                                                                                                                                                                        '1 93750000': {'priority': 1,
                                                                                                                                                                                                                                       'unreserved_bandwidth': 93750000},
                                                                                                                                                                                                                        '2 93750000': {'priority': 2,
                                                                                                                                                                                                                                       'unreserved_bandwidth': 93750000},
                                                                                                                                                                                                                        '3 93750000': {'priority': 3,
                                                                                                                                                                                                                                       'unreserved_bandwidth': 93750000},
                                                                                                                                                                                                                        '4 93750000': {'priority': 4,
                                                                                                                                                                                                                                       'unreserved_bandwidth': 93750000},
                                                                                                                                                                                                                        '5 93750000': {'priority': 5,
                                                                                                                                                                                                                                       'unreserved_bandwidth': 93750000},
                                                                                                                                                                                                                        '6 93750000': {'priority': 6,
                                                                                                                                                                                                                                       'unreserved_bandwidth': 93750000},
                                                                                                                                                                                                                        '7 93750000': {'priority': 7,
                                                                                                                                                                                                                                       'unreserved_bandwidth': 93750000}}}}}},
                                                                                                                                                        'header': {'adv_router': '2.2.2.2',
                                                                                                                                                                   'age': 1191,
                                                                                                                                                                   'checksum': '0x2350',
                                                                                                                                                                   'fragment_number': 38,
                                                                                                                                                                   'length': 116,
                                                                                                                                                                   'lsa_id': '1.0.0.38',
                                                                                                                                                                   'num_links': 1,
                                                                                                                                                                   'opaque_id': 38,
                                                                                                                                                                   'opaque_type': 1,
                                                                                                                                                                   'option': '0x2 '
                                                                                                                                                                             '(No '
                                                                                                                                                                             'TOS-capability, '
                                                                                                                                                                             'No '
                                                                                                                                                                             'DC)',
                                                                                                                                                                   'seq_num': '0x80000004',
                                                                                                                                                                   'type': 'Opaque '
                                                                                                                                                                           'Area '
                                                                                                                                                                           'Link'}}},
                                                                                                                        '1.0.0.39 2.2.2.2': {'ospfv2': {'body': {'opaque': {'link_tlvs': {1: {'admin_group': '0x0',
                                                                                                                                                                                              'link_id': '10.1.2.1',
                                                                                                                                                                                              'link_name': 'Broadcast '
                                                                                                                                                                                                           'network',
                                                                                                                                                                                              'link_type': 2,
                                                                                                                                                                                              'local_if_ipv4_addrs': {'10.1.2.2': {}},
                                                                                                                                                                                              'max_bandwidth': 125000000,
                                                                                                                                                                                              'max_reservable_bandwidth': 93750000,
                                                                                                                                                                                              'remote_if_ipv4_addrs': {'0.0.0.0': {}},
                                                                                                                                                                                              'te_metric': 1,
                                                                                                                                                                                              'unreserved_bandwidths': {'0 93750000': {'priority': 0,
                                                                                                                                                                                                                                       'unreserved_bandwidth': 93750000},
                                                                                                                                                                                                                        '1 93750000': {'priority': 1,
                                                                                                                                                                                                                                       'unreserved_bandwidth': 93750000},
                                                                                                                                                                                                                        '2 93750000': {'priority': 2,
                                                                                                                                                                                                                                       'unreserved_bandwidth': 93750000},
                                                                                                                                                                                                                        '3 93750000': {'priority': 3,
                                                                                                                                                                                                                                       'unreserved_bandwidth': 93750000},
                                                                                                                                                                                                                        '4 93750000': {'priority': 4,
                                                                                                                                                                                                                                       'unreserved_bandwidth': 93750000},
                                                                                                                                                                                                                        '5 93750000': {'priority': 5,
                                                                                                                                                                                                                                       'unreserved_bandwidth': 93750000},
                                                                                                                                                                                                                        '6 93750000': {'priority': 6,
                                                                                                                                                                                                                                       'unreserved_bandwidth': 93750000},
                                                                                                                                                                                                                        '7 93750000': {'priority': 7,
                                                                                                                                                                                                                                       'unreserved_bandwidth': 93750000}}}}}},
                                                                                                                                                        'header': {'adv_router': '2.2.2.2',
                                                                                                                                                                   'age': 1191,
                                                                                                                                                                   'checksum': '0x4239',
                                                                                                                                                                   'fragment_number': 39,
                                                                                                                                                                   'length': 116,
                                                                                                                                                                   'lsa_id': '1.0.0.39',
                                                                                                                                                                   'num_links': 1,
                                                                                                                                                                   'opaque_id': 39,
                                                                                                                                                                   'opaque_type': 1,
                                                                                                                                                                   'option': '0x2 '
                                                                                                                                                                             '(No '
                                                                                                                                                                             'TOS-capability, '
                                                                                                                                                                             'No '
                                                                                                                                                                             'DC)',
                                                                                                                                                                   'seq_num': '0x80000004',
                                                                                                                                                                   'type': 'Opaque '
                                                                                                                                                                           'Area '
                                                                                                                                                                           'Link'}}},
                                                                                                                        '1.0.0.4 3.3.3.3': {'ospfv2': {'body': {'opaque': {'link_tlvs': {1: {'admin_group': '0x0',
                                                                                                                                                                                             'link_id': '10.3.4.4',
                                                                                                                                                                                             'link_name': 'Broadcast '
                                                                                                                                                                                                          'network',
                                                                                                                                                                                             'link_type': 2,
                                                                                                                                                                                             'local_if_ipv4_addrs': {'10.3.4.3': {}},
                                                                                                                                                                                             'max_bandwidth': 125000000,
                                                                                                                                                                                             'max_reservable_bandwidth': 93750000,
                                                                                                                                                                                             'remote_if_ipv4_addrs': {'0.0.0.0': {}},
                                                                                                                                                                                             'te_metric': 1,
                                                                                                                                                                                             'unknown_tlvs': {1: {'length': 4,
                                                                                                                                                                                                                  'type': 32770,
                                                                                                                                                                                                                  'value': '00 '
                                                                                                                                                                                                                           '00 '
                                                                                                                                                                                                                           '00 '
                                                                                                                                                                                                                           '01'},
                                                                                                                                                                                                              2: {'length': 32,
                                                                                                                                                                                                                  'type': 32771,
                                                                                                                                                                                                                  'value': '00 '
                                                                                                                                                                                                                           '00 '
                                                                                                                                                                                                                           '00 '
                                                                                                                                                                                                                           '00 '
                                                                                                                                                                                                                           '00 '
                                                                                                                                                                                                                           '0'}},
                                                                                                                                                                                             'unreserved_bandwidths': {'0 93750000': {'priority': 0,
                                                                                                                                                                                                                                      'unreserved_bandwidth': 93750000},
                                                                                                                                                                                                                       '1 93750000': {'priority': 1,
                                                                                                                                                                                                                                      'unreserved_bandwidth': 93750000},
                                                                                                                                                                                                                       '2 93750000': {'priority': 2,
                                                                                                                                                                                                                                      'unreserved_bandwidth': 93750000},
                                                                                                                                                                                                                       '3 93750000': {'priority': 3,
                                                                                                                                                                                                                                      'unreserved_bandwidth': 93750000},
                                                                                                                                                                                                                       '4 93750000': {'priority': 4,
                                                                                                                                                                                                                                      'unreserved_bandwidth': 93750000},
                                                                                                                                                                                                                       '5 93750000': {'priority': 5,
                                                                                                                                                                                                                                      'unreserved_bandwidth': 93750000},
                                                                                                                                                                                                                       '6 93750000': {'priority': 6,
                                                                                                                                                                                                                                      'unreserved_bandwidth': 93750000},
                                                                                                                                                                                                                       '7 93750000': {'priority': 7,
                                                                                                                                                                                                                                      'unreserved_bandwidth': 93750000}}}}}},
                                                                                                                                                       'header': {'adv_router': '3.3.3.3',
                                                                                                                                                                  'age': 113,
                                                                                                                                                                  'checksum': '0x8f5e',
                                                                                                                                                                  'fragment_number': 4,
                                                                                                                                                                  'length': 160,
                                                                                                                                                                  'lsa_id': '1.0.0.4',
                                                                                                                                                                  'num_links': 1,
                                                                                                                                                                  'opaque_id': 4,
                                                                                                                                                                  'opaque_type': 1,
                                                                                                                                                                  'option': '0x20 '
                                                                                                                                                                            '(No '
                                                                                                                                                                            'TOS-capability, '
                                                                                                                                                                            'DC)',
                                                                                                                                                                  'seq_num': '0x80000003',
                                                                                                                                                                  'type': 'Opaque '
                                                                                                                                                                          'Area '
                                                                                                                                                                          'Link'}}},
                                                                                                                        '1.0.0.6 3.3.3.3': {'ospfv2': {'body': {'opaque': {'link_tlvs': {1: {'admin_group': '0x0',
                                                                                                                                                                                             'link_id': '10.2.3.3',
                                                                                                                                                                                             'link_name': 'Broadcast '
                                                                                                                                                                                                          'network',
                                                                                                                                                                                             'link_type': 2,
                                                                                                                                                                                             'local_if_ipv4_addrs': {'10.2.3.3': {}},
                                                                                                                                                                                             'max_bandwidth': 125000000,
                                                                                                                                                                                             'max_reservable_bandwidth': 93750000,
                                                                                                                                                                                             'remote_if_ipv4_addrs': {'0.0.0.0': {}},
                                                                                                                                                                                             'te_metric': 1,
                                                                                                                                                                                             'unknown_tlvs': {1: {'length': 4,
                                                                                                                                                                                                                  'type': 32770,
                                                                                                                                                                                                                  'value': '00 '
                                                                                                                                                                                                                           '00 '
                                                                                                                                                                                                                           '00 '
                                                                                                                                                                                                                           '01'},
                                                                                                                                                                                                              2: {'length': 32,
                                                                                                                                                                                                                  'type': 32771,
                                                                                                                                                                                                                  'value': '00 '
                                                                                                                                                                                                                           '00 '
                                                                                                                                                                                                                           '00 '
                                                                                                                                                                                                                           '00 '
                                                                                                                                                                                                                           '00 '
                                                                                                                                                                                                                           '0'}},
                                                                                                                                                                                             'unreserved_bandwidths': {'0 93750000': {'priority': 0,
                                                                                                                                                                                                                                      'unreserved_bandwidth': 93750000},
                                                                                                                                                                                                                       '1 93750000': {'priority': 1,
                                                                                                                                                                                                                                      'unreserved_bandwidth': 93750000},
                                                                                                                                                                                                                       '2 93750000': {'priority': 2,
                                                                                                                                                                                                                                      'unreserved_bandwidth': 93750000},
                                                                                                                                                                                                                       '3 93750000': {'priority': 3,
                                                                                                                                                                                                                                      'unreserved_bandwidth': 93750000},
                                                                                                                                                                                                                       '4 93750000': {'priority': 4,
                                                                                                                                                                                                                                      'unreserved_bandwidth': 93750000},
                                                                                                                                                                                                                       '5 93750000': {'priority': 5,
                                                                                                                                                                                                                                      'unreserved_bandwidth': 93750000},
                                                                                                                                                                                                                       '6 93750000': {'priority': 6,
                                                                                                                                                                                                                                      'unreserved_bandwidth': 93750000},
                                                                                                                                                                                                                       '7 93750000': {'priority': 7,
                                                                                                                                                                                                                                      'unreserved_bandwidth': 93750000}}}}}},
                                                                                                                                                       'header': {'adv_router': '3.3.3.3',
                                                                                                                                                                  'age': 113,
                                                                                                                                                                  'checksum': '0x03ed',
                                                                                                                                                                  'fragment_number': 6,
                                                                                                                                                                  'length': 160,
                                                                                                                                                                  'lsa_id': '1.0.0.6',
                                                                                                                                                                  'num_links': 1,
                                                                                                                                                                  'opaque_id': 6,
                                                                                                                                                                  'opaque_type': 1,
                                                                                                                                                                  'option': '0x20 '
                                                                                                                                                                            '(No '
                                                                                                                                                                            'TOS-capability, '
                                                                                                                                                                            'DC)',
                                                                                                                                                                  'seq_num': '0x80000003',
                                                                                                                                                                  'type': 'Opaque '
                                                                                                                                                                          'Area '
                                                                                                                                                                          'Link'}}}}}}}}}}}}}}

    golden_output1 = {'execute.return_value': '''
        R2_ospf_nx# show ip ospf database opaque-area detail vrf all
        OSPF Router with ID (2.2.2.2) (Process ID 1 VRF default)

                Opaque Area Link States (Area 0.0.0.0)

       LS age: 385
       Options: 0x20 (No TOS-capability, DC)
       LS Type: Opaque Area Link
       Link State ID: 1.0.0.0 
       Opaque Type: 1
       Opaque ID: 0
       Advertising Router: 1.1.1.1
       LS Seq Number: 0x80000003
       Checksum: 0x54d3
       Length: 28
       Fragment number: 0

         MPLS TE router ID : 1.1.1.1

         Number of Links : 0

       LS age: 1612
       Options: 0x2 (No TOS-capability, No DC)
       LS Type: Opaque Area Link
       Link State ID: 1.0.0.0 
       Opaque Type: 1
       Opaque ID: 0
       Advertising Router: 2.2.2.2
       LS Seq Number: 0x80000003
       Checksum: 0x1c22
       Length: 28
       Fragment number: 0

         MPLS TE router ID : 2.2.2.2

         Number of Links : 0

       LS age: 113
       Options: 0x20 (No TOS-capability, DC)
       LS Type: Opaque Area Link
       Link State ID: 1.0.0.0 
       Opaque Type: 1
       Opaque ID: 0
       Advertising Router: 3.3.3.3
       LS Seq Number: 0x80000003
       Checksum: 0x5cbb
       Length: 28
       Fragment number: 0

         MPLS TE router ID : 3.3.3.3

         Number of Links : 0

       LS age: 385
       Options: 0x20 (No TOS-capability, DC)
       LS Type: Opaque Area Link
       Link State ID: 1.0.0.1 
       Opaque Type: 1
       Opaque ID: 1
       Advertising Router: 1.1.1.1
       LS Seq Number: 0x80000003
       Checksum: 0x6387
       Length: 124
       Fragment number: 1

         Link connected to Broadcast network
         Link ID : 10.1.4.4
         Interface Address : 10.1.4.1
         Admin Metric : 1
         Maximum Bandwidth : 125000000 
         Maximum reservable bandwidth : 93750000  
         Number of Priority : 8
           Priority 0 : 93750000    Priority 1 : 93750000  
           Priority 2 : 93750000    Priority 3 : 93750000  
           Priority 4 : 93750000    Priority 5 : 93750000  
           Priority 6 : 93750000    Priority 7 : 93750000  
         Affinity Bit : 0x0
          Unknown Sub-TLV      :  Type = 32770, Length = 4 Value = 00 00 00 01 

         Number of Links : 1

       LS age: 385
       Options: 0x20 (No TOS-capability, DC)
       LS Type: Opaque Area Link
       Link State ID: 1.0.0.2 
       Opaque Type: 1
       Opaque ID: 2
       Advertising Router: 1.1.1.1
       LS Seq Number: 0x80000003
       Checksum: 0xb23e
       Length: 124
       Fragment number: 2

         Link connected to Broadcast network
         Link ID : 10.1.2.1
         Interface Address : 10.1.2.1
         Admin Metric : 1
         Maximum Bandwidth : 125000000 
         Maximum reservable bandwidth : 93750000  
         Number of Priority : 8
           Priority 0 : 93750000    Priority 1 : 93750000  
           Priority 2 : 93750000    Priority 3 : 93750000  
           Priority 4 : 93750000    Priority 5 : 93750000  
           Priority 6 : 93750000    Priority 7 : 93750000  
         Affinity Bit : 0x0
          Unknown Sub-TLV      :  Type = 32770, Length = 4 Value = 00 00 00 01 

         Number of Links : 1

       LS age: 113
       Options: 0x20 (No TOS-capability, DC)
       LS Type: Opaque Area Link
       Link State ID: 1.0.0.4 
       Opaque Type: 1
       Opaque ID: 4
       Advertising Router: 3.3.3.3
       LS Seq Number: 0x80000003
       Checksum: 0x8f5e
       Length: 160
       Fragment number: 4

         Link connected to Broadcast network
         Link ID : 10.3.4.4
         Interface Address : 10.3.4.3
         Admin Metric : 1
         Maximum Bandwidth : 125000000 
         Maximum reservable bandwidth : 93750000  
         Number of Priority : 8
           Priority 0 : 93750000    Priority 1 : 93750000  
           Priority 2 : 93750000    Priority 3 : 93750000  
           Priority 4 : 93750000    Priority 5 : 93750000  
           Priority 6 : 93750000    Priority 7 : 93750000  
         Affinity Bit : 0x0
          Unknown Sub-TLV      :  Type = 32770, Length = 4 Value = 00 00 00 01 
          Unknown Sub-TLV      :  Type = 32771, Length = 32 Value = 00 00 00 00 00 0
           0 00 00 00 00 00 00 00 00 00 00 00 00 00 00 
           00 00 00 00 00 00 00 00 00 00 00 00 

         Number of Links : 1

       LS age: 113
       Options: 0x20 (No TOS-capability, DC)
       LS Type: Opaque Area Link
       Link State ID: 1.0.0.6 
       Opaque Type: 1
       Opaque ID: 6
       Advertising Router: 3.3.3.3
       LS Seq Number: 0x80000003
       Checksum: 0x03ed
       Length: 160
       Fragment number: 6

         Link connected to Broadcast network
         Link ID : 10.2.3.3
         Interface Address : 10.2.3.3
         Admin Metric : 1
         Maximum Bandwidth : 125000000 
         Maximum reservable bandwidth : 93750000  
         Number of Priority : 8
           Priority 0 : 93750000    Priority 1 : 93750000  
           Priority 2 : 93750000    Priority 3 : 93750000  
           Priority 4 : 93750000    Priority 5 : 93750000  
           Priority 6 : 93750000    Priority 7 : 93750000  
         Affinity Bit : 0x0
          Unknown Sub-TLV      :  Type = 32770, Length = 4 Value = 00 00 00 01 
          Unknown Sub-TLV      :  Type = 32771, Length = 32 Value = 00 00 00 00 00 0
           0 00 00 00 00 00 00 00 00 00 00 00 00 00 00 
           00 00 00 00 00 00 00 00 00 00 00 00 

         Number of Links : 1

       LS age: 1202
       Options: 0x2 (No TOS-capability, No DC)
       LS Type: Opaque Area Link
       Link State ID: 1.0.0.37 
       Opaque Type: 1
       Opaque ID: 37
       Advertising Router: 2.2.2.2
       LS Seq Number: 0x80000004
       Checksum: 0xe492
       Length: 116
       Fragment number: 37

         Link connected to Broadcast network
         Link ID : 10.2.3.3
         Interface Address : 10.2.3.2
         Admin Metric : 1
         Maximum Bandwidth : 125000000 
         Maximum reservable bandwidth : 93750000  
         Number of Priority : 8
           Priority 0 : 93750000    Priority 1 : 93750000  
           Priority 2 : 93750000    Priority 3 : 93750000  
           Priority 4 : 93750000    Priority 5 : 93750000  
           Priority 6 : 93750000    Priority 7 : 93750000  
         Affinity Bit : 0x0

         Number of Links : 1

       LS age: 1191
       Options: 0x2 (No TOS-capability, No DC)
       LS Type: Opaque Area Link
       Link State ID: 1.0.0.38 
       Opaque Type: 1
       Opaque ID: 38
       Advertising Router: 2.2.2.2
       LS Seq Number: 0x80000004
       Checksum: 0x2350
       Length: 116
       Fragment number: 38

         Link connected to Broadcast network
         Link ID : 10.2.4.4
         Interface Address : 10.2.4.2
         Admin Metric : 1
         Maximum Bandwidth : 125000000 
         Maximum reservable bandwidth : 93750000  
         Number of Priority : 8
           Priority 0 : 93750000    Priority 1 : 93750000  
           Priority 2 : 93750000    Priority 3 : 93750000  
           Priority 4 : 93750000    Priority 5 : 93750000  
           Priority 6 : 93750000    Priority 7 : 93750000  
         Affinity Bit : 0x0

         Number of Links : 1

       LS age: 1191
       Options: 0x2 (No TOS-capability, No DC)
       LS Type: Opaque Area Link
       Link State ID: 1.0.0.39 
       Opaque Type: 1
       Opaque ID: 39
       Advertising Router: 2.2.2.2
       LS Seq Number: 0x80000004
       Checksum: 0x4239
       Length: 116
       Fragment number: 39

         Link connected to Broadcast network
         Link ID : 10.1.2.1
         Interface Address : 10.1.2.2
         Admin Metric : 1
         Maximum Bandwidth : 125000000 
         Maximum reservable bandwidth : 93750000  
         Number of Priority : 8
           Priority 0 : 93750000    Priority 1 : 93750000  
           Priority 2 : 93750000    Priority 3 : 93750000  
           Priority 4 : 93750000    Priority 5 : 93750000  
           Priority 6 : 93750000    Priority 7 : 93750000  
         Affinity Bit : 0x0

         Number of Links : 1
        '''}

    def test_full(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output1)
        obj = ShowIpOspfDatabaseOpaqueAreaDetail(device=self.device)
        parsed_output = obj.parse(vrf='all')
        self.assertEqual(parsed_output, self.golden_parsed_output1)

    def test_empty(self):
        self.maxDiff = None
        self.device = Mock(**self.empty_output)
        obj = ShowIpOspfDatabaseOpaqueAreaDetail(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()



if __name__ == '__main__':
    unittest.main()
