import re
import unittest
from unittest.mock import Mock

from ats.topology import Device

from metaparser.util.exceptions import SchemaEmptyParserError, \
                                       SchemaMissingKeyError

from parser.iosxr.show_interface import ShowInterfaceDetail, ShowVlanInterface, ShowIpv4VrfAllInterface, ShowIpv6VrfAllInterface

#############################################################################
# unitest For Show Interface Detail
#############################################################################

class test_show_interface(unittest.TestCase):
    device = Device(name='aDevice')
    device0 = Device(name='bDevice')
    empty_output = {'execute.return_value': ''}
    golden_parsed_output = {'GigabitEthernet0/0/0/0': {'auto_negotiate': True,
                            'counters': {'carrier_transitions': 0,
                                         'drops': 0,
                                         'in_abort': 0,
                                         'in_broadcast_pkts': 0,
                                         'in_crc_errors': 0,
                                         'in_discards': 0,
                                         'in_errors': 0,
                                         'in_frame': 0,
                                         'in_giants': 0,
                                         'in_ignored': 0,
                                         'in_multicast_pkts': 0,
                                         'in_octets': 0,
                                         'in_overrun': 0,
                                         'in_parity': 0,
                                         'in_pkts': 0,
                                         'in_runts': 0,
                                         'in_throttles': 0,
                                         'last_clear': 'never',
                                         'out_applique': 0,
                                         'out_broadcast_pkts': 0,
                                         'out_buffer_failures': 0,
                                         'out_buffer_swapped_out': 0,
                                         'out_discards': 0,
                                         'out_errors': 0,
                                         'out_multicast_pkts': 0,
                                         'out_octets': 0,
                                         'out_pkts': 0,
                                         'out_resets': 0,
                                         'out_underruns': 0,
                                         'rate': {'in_rate': 0,
                                                  'in_rate_pkts': 0,
                                                  'load_interval': 30,
                                                  'out_rate': 0,
                                                  'out_rate_pkts': 0}},
                            'duplex_mode': 'Full-duplex',
                            'enabled': False,
                            'encapsulations': {'encapsulation': 'ARPA'},
                            'flow_control': {'flow_control_receive': False,
                                             'flow_control_send': False},
                            'interface_state': 0,
                            'ipv4': {'10.1.1.1/24': {'ip': '10.1.1.1',
                                                     'prefix_length': '24'}},
                            'last_input': 'never',
                            'last_output': 'never',
                            'line_protocol': 'administratively down',
                            'location': 'unknown',
                            'loopback_status': 'not set',
                            'mac_address': 'aaaa.bbbb.cccc',
                            'phys_address': '5254.0077.9407',
                            'port_speed': '1000Mb/s',
                            'reliability': '255/255',
                            'rxload': '0/255',
                            'txload': '0/255',
                            'types': 'GigabitEthernet'},
 'GigabitEthernet0/0/0/0.10': {'counters': {'drops': 0,
                                            'in_broadcast_pkts': 0,
                                            'in_discards': 0,
                                            'in_multicast_pkts': 0,
                                            'in_octets': 0,
                                            'in_pkts': 0,
                                            'last_clear': 'never',
                                            'out_broadcast_pkts': 0,
                                            'out_discards': 0,
                                            'out_multicast_pkts': 0,
                                            'out_octets': 0,
                                            'out_pkts': 0,
                                            'rate': {'in_rate': 0,
                                                     'in_rate_pkts': 0,
                                                     'load_interval': 5,
                                                     'out_rate': 0,
                                                     'out_rate_pkts': 0}},
                               'enabled': False,
                               'encapsulations': {'encapsulation': '802.1Q '
                                                                   'Virtual '
                                                                   'LAN',
                                                  'first_dot1q': '10',
                                                  'second_dot1q': '10'},
                               'interface_state': 0,
                               'last_input': 'never',
                               'last_output': 'never',
                               'line_protocol': 'administratively down',
                               'loopback_status': 'not set',
                               'reliability': '255/255',
                               'rxload': '0/255',
                               'txload': '0/255'},
 'GigabitEthernet0/0/0/0.20': {'counters': {'drops': 0,
                                            'in_broadcast_pkts': 0,
                                            'in_discards': 0,
                                            'in_multicast_pkts': 0,
                                            'in_octets': 0,
                                            'in_pkts': 0,
                                            'last_clear': 'never',
                                            'out_broadcast_pkts': 0,
                                            'out_discards': 0,
                                            'out_multicast_pkts': 0,
                                            'out_octets': 0,
                                            'out_pkts': 0,
                                            'rate': {'in_rate': 0,
                                                     'in_rate_pkts': 0,
                                                     'load_interval': 5,
                                                     'out_rate': 0,
                                                     'out_rate_pkts': 0}},
                               'enabled': False,
                               'encapsulations': {'encapsulation': '802.1Q '
                                                                   'Virtual '
                                                                   'LAN',
                                                  'first_dot1q': '20'},
                               'interface_state': 0,
                               'last_input': 'never',
                               'last_output': 'never',
                               'line_protocol': 'administratively down',
                               'loopback_status': 'not set',
                               'reliability': '255/255',
                               'rxload': '0/255',
                               'txload': '0/255'},
 'MgmtEth0/0/CPU0/0': {'auto_negotiate': True,
                       'counters': {'carrier_transitions': 0,
                                    'drops': 0,
                                    'in_abort': 0,
                                    'in_broadcast_pkts': 0,
                                    'in_crc_errors': 0,
                                    'in_discards': 0,
                                    'in_errors': 0,
                                    'in_frame': 0,
                                    'in_giants': 0,
                                    'in_ignored': 0,
                                    'in_multicast_pkts': 0,
                                    'in_octets': 0,
                                    'in_overrun': 0,
                                    'in_parity': 0,
                                    'in_pkts': 0,
                                    'in_runts': 0,
                                    'in_throttles': 0,
                                    'last_clear': 'never',
                                    'out_applique': 0,
                                    'out_broadcast_pkts': 0,
                                    'out_buffer_failures': 0,
                                    'out_buffer_swapped_out': 0,
                                    'out_discards': 0,
                                    'out_errors': 0,
                                    'out_multicast_pkts': 0,
                                    'out_octets': 0,
                                    'out_pkts': 0,
                                    'out_resets': 0,
                                    'out_underruns': 0,
                                    'rate': {'in_rate': 0,
                                             'in_rate_pkts': 0,
                                             'load_interval': 5,
                                             'out_rate': 0,
                                             'out_rate_pkts': 0}},
                       'duplex_mode': 'Duplex unknown',
                       'enabled': False,
                       'encapsulations': {'encapsulation': 'ARPA'},
                       'flow_control': {'flow_control_receive': False,
                                        'flow_control_send': False},
                       'interface_state': 0,
                       'last_input': 'never',
                       'last_output': 'never',
                       'line_protocol': 'administratively down',
                       'location': 'unknown',
                       'loopback_status': 'not set',
                       'mac_address': '5254.00c3.6c43',
                       'phys_address': '5254.00c3.6c43',
                       'port_speed': '0Kb/s',
                       'reliability': '255/255',
                       'rxload': 'Unknown',
                       'txload': 'Unknown',
                       'types': 'Management Ethernet'},
 'Null0': {'counters': {'drops': 0,
                        'in_broadcast_pkts': 0,
                        'in_discards': 0,
                        'in_multicast_pkts': 0,
                        'in_octets': 0,
                        'in_pkts': 0,
                        'last_clear': 'never',
                        'out_broadcast_pkts': 0,
                        'out_discards': 0,
                        'out_multicast_pkts': 0,
                        'out_octets': 0,
                        'out_pkts': 0,
                        'rate': {'in_rate': 0,
                                 'in_rate_pkts': 0,
                                 'load_interval': 5,
                                 'out_rate': 0,
                                 'out_rate_pkts': 0}},
           'enabled': True,
           'encapsulations': {'encapsulation': 'Null'},
           'last_input': 'never',
           'last_output': 'never',
           'line_protocol': 'up',
           'loopback_status': 'not set',
           'mac_address': 'None',
           'phys_address': 'None',
           'reliability': '255/255',
           'rxload': 'Unknown',
           'txload': 'Unknown',
           'types': 'Null '}}

    golden_output = {'execute.return_value': '''
        Null0 is up, line protocol is up 
      Interface state transitions: 
      Hardware is Null interface
      Internet address is Unknown
      MTU 1500 bytes, BW 0 Kbit
         reliability 255/255, txload Unknown, rxload Unknown
      Encapsulation Null,  loopback not set,
      Last input never, output never
      Last clearing of "show interface" counters never
      5 minute input rate 0 bits/sec, 0 packets/sec
      5 minute output rate 0 bits/sec, 0 packets/sec
         0 packets input, 0 bytes, 0 total input drops
         0 drops for unrecognized upper-level protocol
         Received 0 broadcast packets, 0 multicast packets
         0 packets output, 0 bytes, 0 total output drops
         Output 0 broadcast packets, 0 multicast packets

    MgmtEth0/0/CPU0/0 is administratively down, line protocol is administratively down 
      Interface state transitions: 0
      Hardware is Management Ethernet, address is 5254.00c3.6c43 (bia 5254.00c3.6c43)
      Internet address is Unknown
      MTU 1514 bytes, BW 0 Kbit
         reliability 255/255, txload Unknown, rxload Unknown
      Encapsulation ARPA,
      Duplex unknown, 0Kb/s, unknown, link type is autonegotiation
      output flow control is off, input flow control is off
      Carrier delay (up) is 10 msec
      loopback not set,
      Last input never, output never
      Last clearing of "show interface" counters never
      5 minute input rate 0 bits/sec, 0 packets/sec
      5 minute output rate 0 bits/sec, 0 packets/sec
         0 packets input, 0 bytes, 0 total input drops
         0 drops for unrecognized upper-level protocol
         Received 0 broadcast packets, 0 multicast packets
                  0 runts, 0 giants, 0 throttles, 0 parity
         0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored, 0 abort
         0 packets output, 0 bytes, 0 total output drops
         Output 0 broadcast packets, 0 multicast packets
         0 output errors, 0 underruns, 0 applique, 0 resets
         0 output buffer failures, 0 output buffers swapped out
         0 carrier transitions

    GigabitEthernet0/0/0/0 is administratively down, line protocol is administratively down 
      Interface state transitions: 0
      Hardware is GigabitEthernet, address is aaaa.bbbb.cccc (bia 5254.0077.9407)
      Description: desc
      Internet address is 10.1.1.1/24
      MTU 1600 bytes, BW 768 Kbit (Max: 1000000 Kbit)
         reliability 255/255, txload 0/255, rxload 0/255
      Encapsulation ARPA,
      Full-duplex, 1000Mb/s, unknown, link type is autonegotiation
      output flow control is off, input flow control is off
      Carrier delay (up) is 10 msec
      loopback not set,
      Last input never, output never
      Last clearing of "show interface" counters never
      30 second input rate 0 bits/sec, 0 packets/sec
      30 second output rate 0 bits/sec, 0 packets/sec
         0 packets input, 0 bytes, 0 total input drops
         0 drops for unrecognized upper-level protocol

         Received 0 broadcast packets, 0 multicast packets
                  0 runts, 0 giants, 0 throttles, 0 parity
         0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored, 0 abort
         
         0 packets output, 0 bytes, 0 total output drops 
         Output 0 broadcast packets, 0 multicast packets
         0 output errors, 0 underruns, 0 applique, 0 resets
         0 output buffer failures, 0 output buffers swapped out
         0 carrier transitions

    GigabitEthernet0/0/0/0.10 is administratively down, line protocol is administratively down 
      Interface state transitions: 0
      Hardware is VLAN sub-interface(s), address is aaaa.bbbb.cccc
      Internet address is Unknown
      MTU 1608 bytes, BW 768 Kbit (Max: 1000000 Kbit)
         reliability 255/255, txload 0/255, rxload 0/255
      Encapsulation 802.1Q Virtual LAN, VLAN Id 10, 2nd VLAN Id 10,
      loopback not set,
      Last input never, output never
      Last clearing of "show interface" counters never
      5 minute input rate 0 bits/sec, 0 packets/sec
      5 minute output rate 0 bits/sec, 0 packets/sec
         0 packets input, 0 bytes, 0 total input drops
         0 drops for unrecognized upper-level protocol
         Received 0 broadcast packets, 0 multicast packets
         0 packets output, 0 bytes, 0 total output drops
         Output 0 broadcast packets, 0 multicast packets

    GigabitEthernet0/0/0/0.20 is administratively down, line protocol is administratively down 
      Interface state transitions: 0
      Hardware is VLAN sub-interface(s), address is aaaa.bbbb.cccc
      Internet address is Unknown
      MTU 1604 bytes, BW 768 Kbit (Max: 1000000 Kbit)
         reliability 255/255, txload 0/255, rxload 0/255
      Encapsulation 802.1Q Virtual LAN, VLAN Id 20,  loopback not set,
      Last input never, output never
      Last clearing of "show interface" counters never
      5 minute input rate 0 bits/sec, 0 packets/sec
      5 minute output rate 0 bits/sec, 0 packets/sec
         0 packets input, 0 bytes, 0 total input drops
         0 drops for unrecognized upper-level protocol
         Received 0 broadcast packets, 0 multicast packets
         0 packets output, 0 bytes, 0 total output drops
         Output 0 broadcast packets, 0 multicast packets
    '''}

    def test_empty(self):
        self.device1 = Mock(**self.empty_output)
        interface_detail_obj = ShowInterfaceDetail(device=self.device1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = interface_detail_obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        interface_detail_obj = ShowInterfaceDetail(device=self.device)
        parsed_output = interface_detail_obj.parse()
        self.maxDiff = None
        self.assertEqual(parsed_output,self.golden_parsed_output)


#############################################################################
# unitest For show vlan interface
#############################################################################

class test_show_vlan_interface(unittest.TestCase):
    device = Device(name='aDevice')
    device0 = Device(name='bDevice')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output = {'Gi0/0/0/0.10': {'encapsulation': 'Double 802.1Q',
                  'linep_state': 'admin-down',
                  'mtu': 1608,
                  'outer_vlan': 10,
                  'second_vlan': '10',
                  'service': 'L3'},
 'Gi0/0/0/0.20': {'encapsulation': '802.1Q',
                  'linep_state': 'admin-down',
                  'mtu': 1604,
                  'outer_vlan': 20,
                  'second_vlan': 'None',
                  'service': 'L3'}}


    golden_output = {'execute.return_value': '''

    Interface               Encapsulation    Outer 2nd   Service  MTU    LineP
                                         VLAN  VLAN                  State
    Gi0/0/0/0.10            Double 802.1Q       10   10  L3        1608  admin-down
    Gi0/0/0/0.20            802.1Q              20       L3        1604  admin-down

    '''}

    def test_empty(self):
        self.device1 = Mock(**self.empty_output)
        vlan_interface_obj = ShowVlanInterface(device=self.device1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = vlan_interface_obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        vlan_interface_obj = ShowVlanInterface(device=self.device)
        parsed_output = vlan_interface_obj.parse()
        self.maxDiff = None
        self.assertEqual(parsed_output,self.golden_parsed_output)


#############################################################################
# unitest For show ipv4 vrf all interface
#############################################################################

class test_show_ipv4_vrf_all_interface(unittest.TestCase):

    device = Device(name='aDevice')
    device0 = Device(name='bDevice')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output = {'GigabitEthernet0/0/0/0': {'int_status': 'Shutdown',
                            'ipv4': {'10.1.1.1/24': {'ip': '10.1.1.1',
                                                     'prefix_length': '24'},
                                     '10.2.2.2/24': {'arp': 'disabled',
                                                     'broadcast_forwarding': 'disabled',
                                                     'helper_address': 'not '
                                                                       'set',
                                                     'icmp_redirects': 'never '
                                                                       'sent',
                                                     'icmp_replies': 'never '
                                                                     'sent',
                                                     'icmp_unreachables': 'always '
                                                                          'sent',
                                                     'in_access_list': 'not '
                                                                       'set',
                                                     'ip': '10.2.2.2',
                                                     'mtu': 1600,
                                                     'mtu_available': 1586,
                                                     'out_access_list': 'not '
                                                                        'set',
                                                     'prefix_length': '24',
                                                     'secondary': True,
                                                     'table_id': '0xe0000011'},
                                     'unnumbered': {'unnumbered_int': '111.111.111.111/32',
                                                    'unnumbered_intf_ref': 'Loopback11'}},
                            'oper_status': 'Down',
                            'vrf': 'VRF1',
                            'vrf_id': '0x60000002'},
 'GigabitEthernet0/0/0/0.10': {'int_status': 'Shutdown',
                               'oper_status': 'Down',
                               'vrf': 'default',
                               'vrf_id': '0x60000000'},
 'GigabitEthernet0/0/0/0.20': {'int_status': 'Shutdown',
                               'oper_status': 'Down',
                               'vrf': 'default',
                               'vrf_id': '0x60000000'},
 'GigabitEthernet0/0/0/1': {'int_status': 'Shutdown',
                            'oper_status': 'Down',
                            'vrf': 'VRF2',
                            'vrf_id': '0x60000003'},
 'GigabitEthernet0/0/0/2': {'int_status': 'Shutdown',
                            'oper_status': 'Down',
                            'vrf': 'default',
                            'vrf_id': '0x60000000'},
 'GigabitEthernet0/0/0/3': {'int_status': 'Shutdown',
                            'oper_status': 'Down',
                            'vrf': 'default',
                            'vrf_id': '0x60000000'},
 'GigabitEthernet0/0/0/4': {'int_status': 'Shutdown',
                            'oper_status': 'Down',
                            'vrf': 'default',
                            'vrf_id': '0x60000000'},
 'GigabitEthernet0/0/0/5': {'int_status': 'Shutdown',
                            'oper_status': 'Down',
                            'vrf': 'default',
                            'vrf_id': '0x60000000'},
 'GigabitEthernet0/0/0/6': {'int_status': 'Shutdown',
                            'oper_status': 'Down',
                            'vrf': 'default',
                            'vrf_id': '0x60000000'},
 'MgmtEth0/0/CPU0/0': {'int_status': 'Shutdown',
                       'oper_status': 'Down',
                       'vrf': 'default',
                       'vrf_id': '0x60000000'}}

    golden_output = {'execute.return_value': '''
    MgmtEth0/0/CPU0/0 is Shutdown, ipv4 protocol is Down
      Vrf is default (vrfid 0x60000000)
      Internet protocol processing disabled
    GigabitEthernet0/0/0/0 is Shutdown, ipv4 protocol is Down
      Vrf is VRF1 (vrfid 0x60000002)
      Interface is unnumbered.  Using address of Loopback11 (111.111.111.111/32)
      Internet address is 10.1.1.1/24 with route-tag 50
      Secondary address 10.2.2.2/24
      MTU is 1600 (1586 is available to IP)
      Helper address is not set
      Directed broadcast forwarding is disabled
      Outgoing access list is not set
      Inbound  access list is not set
      Proxy ARP is disabled
      ICMP redirects are never sent
      ICMP unreachables are always sent
      ICMP mask replies are never sent
      Table Id is 0xe0000011
    GigabitEthernet0/0/0/0.10 is Shutdown, ipv4 protocol is Down
      Vrf is default (vrfid 0x60000000)
      Internet protocol processing disabled
    GigabitEthernet0/0/0/0.20 is Shutdown, ipv4 protocol is Down
      Vrf is default (vrfid 0x60000000)
      Internet protocol processing disabled
    GigabitEthernet0/0/0/1 is Shutdown, ipv4 protocol is Down
      Vrf is VRF2 (vrfid 0x60000003)
      Internet protocol processing disabled
    GigabitEthernet0/0/0/2 is Shutdown, ipv4 protocol is Down
      Vrf is default (vrfid 0x60000000)
      Internet protocol processing disabled
    GigabitEthernet0/0/0/3 is Shutdown, ipv4 protocol is Down
      Vrf is default (vrfid 0x60000000)
      Internet protocol processing disabled
    GigabitEthernet0/0/0/4 is Shutdown, ipv4 protocol is Down
      Vrf is default (vrfid 0x60000000)
      Internet protocol processing disabled
    GigabitEthernet0/0/0/5 is Shutdown, ipv4 protocol is Down
      Vrf is default (vrfid 0x60000000)
      Internet protocol processing disabled
    GigabitEthernet0/0/0/6 is Shutdown, ipv4 protocol is Down
      Vrf is default (vrfid 0x60000000)
      Internet protocol processing disabled
    
    '''}

    def test_empty(self):
        self.device1 = Mock(**self.empty_output)
        ipv4_vrf_all_interface_obj = ShowIpv4VrfAllInterface(device=self.device1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = ipv4_vrf_all_interface_obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        ipv4_vrf_all_interface_obj = ShowIpv4VrfAllInterface(device=self.device)
        parsed_output = ipv4_vrf_all_interface_obj.parse()
        self.maxDiff = None
        self.assertEqual(parsed_output,self.golden_parsed_output)


#############################################################################
# unitest For show ipv6 vrf all interface
#############################################################################

class test_show_ipv6_vrf_all_interface(unittest.TestCase):
    device = Device(name='aDevice')
    device0 = Device(name='bDevice')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output = {'GigabitEthernet0/0/0/0': {'enabled': True,
                            'int_status': 'Shutdown',
                            'ipv6': {'2001:db8:1:1::1/64': {'ipv6': '2001:db8:1:1::1',
                                                            'ipv6_prefix_length': '64',
                                                            'ipv6_status': 'tentative',
                                                            'ipv6_subnet': '2001:db8:1:1::'},
                                     '2001:db8:2:2::2/64': {'ipv6': '2001:db8:2:2::2',
                                                            'ipv6_prefix_length': '64',
                                                            'ipv6_status': 'tentative',
                                                            'ipv6_subnet': '2001:db8:2:2::'},
                                     '2001:db8:3:3:a8aa:bbff:febb:cccc/64': {'ipv6': '2001:db8:3:3:a8aa:bbff:febb:cccc',
                                                                             'ipv6_eui64': True,
                                                                             'ipv6_prefix_length': '64',
                                                                             'ipv6_route_tag': 'None',
                                                                             'ipv6_status': 'tentative',
                                                                             'ipv6_subnet': '2001:db8:3:3::'},
                                     '2001:db8:4:4::4/64': {'ipv6': '2001:db8:4:4::4',
                                                            'ipv6_prefix_length': '64',
                                                            'ipv6_route_tag': '10',
                                                            'ipv6_status': 'tentative',
                                                            'ipv6_subnet': '2001:db8:4:4::'},
                                     'auto_config_state': 'stateless',
                                     'complete_glean_adj': '0',
                                     'complete_protocol_adj': '0',
                                     'dropped_glean_req': '0',
                                     'dropped_protocol_req': '0',
                                     'icmp_redirects': 'disabled',
                                     'icmp_unreachables': 'enabled',
                                     'in_access_list': 'not set',
                                     'incomplete_glean_adj': '0',
                                     'incomplete_protocol_adj': '0',
                                     'ipv6_link_local': 'fe80::a8aa:bbff:febb:cccc',
                                     'ipv6_link_local_state': 'TENTATIVE',
                                     'ipv6_mtu': '1600',
                                     'ipv6_mtu_available': '1586',
                                     'nd_adv_retrans_int': '0',
                                     'nd_cache_limit': '1000000000',
                                     'nd_reachable_time': '0',
                                     'out_access_list': 'not set',
                                     'table_id': '0xe0800011'},
                            'oper_status': 'Down',
                            'vrf': 'VRF1',
                            'vrf_id': '0x60000002'},
 'GigabitEthernet0/0/0/0.10': {'enabled': False,
                               'int_status': 'Shutdown',
                               'oper_status': 'Down',
                               'vrf': 'default',
                               'vrf_id': '0x60000000'},
 'GigabitEthernet0/0/0/0.20': {'enabled': False,
                               'int_status': 'Shutdown',
                               'oper_status': 'Down',
                               'vrf': 'default',
                               'vrf_id': '0x60000000'},
 'GigabitEthernet0/0/0/1': {'enabled': False,
                            'int_status': 'Shutdown',
                            'oper_status': 'Down',
                            'vrf': 'VRF2',
                            'vrf_id': '0x60000003'},
 'GigabitEthernet0/0/0/2': {'enabled': False,
                            'int_status': 'Shutdown',
                            'oper_status': 'Down',
                            'vrf': 'default',
                            'vrf_id': '0x60000000'},
 'GigabitEthernet0/0/0/3': {'enabled': False,
                            'int_status': 'Shutdown',
                            'oper_status': 'Down',
                            'vrf': 'default',
                            'vrf_id': '0x60000000'},
 'GigabitEthernet0/0/0/4': {'enabled': False,
                            'int_status': 'Shutdown',
                            'oper_status': 'Down',
                            'vrf': 'default',
                            'vrf_id': '0x60000000'},
 'GigabitEthernet0/0/0/5': {'enabled': False,
                            'int_status': 'Shutdown',
                            'oper_status': 'Down',
                            'vrf': 'default',
                            'vrf_id': '0x60000000'},
 'GigabitEthernet0/0/0/6': {'enabled': False,
                            'int_status': 'Shutdown',
                            'oper_status': 'Down',
                            'vrf': 'default',
                            'vrf_id': '0x60000000'},
 'MgmtEth0/0/CPU0/0': {'enabled': False,
                       'int_status': 'Shutdown',
                       'oper_status': 'Down',
                       'vrf': 'default',
                       'vrf_id': '0x60000000'}}

    golden_output = {'execute.return_value': '''
    MgmtEth0/0/CPU0/0 is Shutdown, ipv6 protocol is Down, Vrfid is default (0x60000000)
      IPv6 is disabled, link-local address unassigned
      No global unicast address is configured
    GigabitEthernet0/0/0/0 is Shutdown, ipv6 protocol is Down, Vrfid is VRF1 (0x60000002)
      IPv6 is enabled, link-local address is fe80::a8aa:bbff:febb:cccc [TENTATIVE]
      Global unicast address(es):
        2001:db8:1:1::1, subnet is 2001:db8:1:1::/64 [TENTATIVE]
        2001:db8:2:2::2, subnet is 2001:db8:2:2::/64 [TENTATIVE]
        2001:db8:4:4::4, subnet is 2001:db8:4:4::/64 [TENTATIVE] with route-tag 10
        2001:db8:3:3:a8aa:bbff:febb:cccc, subnet is 2001:db8:3:3::/64 [TENTATIVE]
      Joined group address(es): ff02::2 ff02::1
      MTU is 1600 (1586 is available to IPv6)
      ICMP redirects are disabled
      ICMP unreachables are enabled
      ND DAD is enabled, number of DAD attempts 1
      ND reachable time is 0 milliseconds
      ND cache entry limit is 1000000000
      ND advertised retransmit interval is 0 milliseconds
      Hosts use stateless autoconfig for addresses.
      Outgoing access list is not set
      Inbound  access list is not set
      Table Id is 0xe0800011
      Complete protocol adjacency: 0
      Complete glean adjacency: 0
      Incomplete protocol adjacency: 0
      Incomplete glean adjacency: 0
      Dropped protocol request: 0
      Dropped glean request: 0
    GigabitEthernet0/0/0/0.10 is Shutdown, ipv6 protocol is Down, Vrfid is default (0x60000000)
      IPv6 is disabled, link-local address unassigned
      No global unicast address is configured
    GigabitEthernet0/0/0/0.20 is Shutdown, ipv6 protocol is Down, Vrfid is default (0x60000000)
      IPv6 is disabled, link-local address unassigned
      No global unicast address is configured
    GigabitEthernet0/0/0/1 is Shutdown, ipv6 protocol is Down, Vrfid is VRF2 (0x60000003)
      IPv6 is disabled, link-local address unassigned
      No global unicast address is configured
    GigabitEthernet0/0/0/2 is Shutdown, ipv6 protocol is Down, Vrfid is default (0x60000000)
      IPv6 is disabled, link-local address unassigned
      No global unicast address is configured
    GigabitEthernet0/0/0/3 is Shutdown, ipv6 protocol is Down, Vrfid is default (0x60000000)
      IPv6 is disabled, link-local address unassigned
      No global unicast address is configured
    GigabitEthernet0/0/0/4 is Shutdown, ipv6 protocol is Down, Vrfid is default (0x60000000)
      IPv6 is disabled, link-local address unassigned
      No global unicast address is configured
    GigabitEthernet0/0/0/5 is Shutdown, ipv6 protocol is Down, Vrfid is default (0x60000000)
      IPv6 is disabled, link-local address unassigned
      No global unicast address is configured
    GigabitEthernet0/0/0/6 is Shutdown, ipv6 protocol is Down, Vrfid is default (0x60000000)
      IPv6 is disabled, link-local address unassigned
      No global unicast address is configured
    
    '''}

    def test_empty(self):
        self.device1 = Mock(**self.empty_output)
        ipv6_vrf_all_interface_obj = ShowIpv6VrfAllInterface(device=self.device1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = ipv6_vrf_all_interface_obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        ipv6_vrf_all_interface_obj = ShowIpv6VrfAllInterface(device=self.device)
        parsed_output = ipv6_vrf_all_interface_obj.parse()
        self.maxDiff = None
        self.assertEqual(parsed_output,self.golden_parsed_output)
        
if __name__ == '__main__':
    unittest.main()