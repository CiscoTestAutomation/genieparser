import re
import unittest
from unittest.mock import Mock

from pyats.topology import Device

from genie.metaparser.util.exceptions import (SchemaEmptyParserError,
                                              SchemaMissingKeyError)

from genie.libs.parser.iosxr.show_interface import (ShowInterfacesDetail,
                                                    ShowVlanInterface,
                                                    ShowIpv4VrfAllInterface,
                                                    ShowIpv6VrfAllInterface,
                                                    ShowEthernetTags,
                                                    ShowInterfacesAccounting,
                                                    ShowIpInterfaceBrief,
                                                    ShowIpv4InterfaceBrief,
                                                    ShowInterfaces,
                                                    ShowInterfacesDescription,
                                                    ShowIpv6Interface)

#############################################################################
# unitest For Show Interfaces Detail
#############################################################################

class test_show_interface_detail(unittest.TestCase):
    device = Device(name='aDevice')
    device0 = Device(name='bDevice')
    empty_output = {'execute.return_value': ''}
    golden_parsed_output = {
        'GigabitEthernet0/0/0/0': {
            'auto_negotiate': False,
            'bandwidth': 768,
            'carrier_delay': '10',
            'counters': {'carrier_transitions': 0,
                         'in_abort': 0,
                         'in_broadcast_pkts': 0,
                         'in_crc_errors': 0,
                         'in_discards': 0,
                         'in_frame': 0,
                         'in_frame_errors': 0,
                         'in_giants': 0,
                         'in_ignored': 0,
                         'in_multicast_pkts': 0,
                         'in_octets': 0,
                         'in_overrun': 0,
                         'in_parity': 0,
                         'in_pkts': 0,
                         'in_runts': 0,
                         'in_throttles': 0,
                         'in_unknown_protos': 0,
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
            'description': 'desc',
            'duplex_mode': 'full',
            'enabled': False,
            'encapsulations': {'encapsulation': 'arpa'},
            'flow_control': {'flow_control_receive': False,
                             'flow_control_send': False},
            'interface_state': 0,
            'ipv4': {'10.1.1.1/24': {'ip': '10.1.1.1',
                                     'prefix_length': '24'}},
            'last_input': 'never',
            'last_output': 'never',
            'line_protocol': 'administratively down',
            'oper_status': 'down',
            'location': 'unknown',
            'mac_address': 'aaaa.bbff.8888',
            'mtu': 1600,
            'phys_address': '5254.00ff.0c7e',
            'port_speed': '1000Mb/s',
            'reliability': '255/255',
            'rxload': '0/255',
            'txload': '0/255',
            'types': 'gigabitethernet'},
        'GigabitEthernet0/0/0/0.10': {'bandwidth': 768,
                                      'counters': {'in_broadcast_pkts': 0,
                                                   'in_discards': 0,
                                                   'in_multicast_pkts': 0,
                                                   'in_octets': 0,
                                                   'in_pkts': 0,
                                                   'in_unknown_protos': 0,
                                                   'last_clear': 'never',
                                                   'out_broadcast_pkts': 0,
                                                   'out_discards': 0,
                                                   'out_multicast_pkts': 0,
                                                   'out_octets': 0,
                                                   'out_pkts': 0,
                                                   'rate': {'in_rate': 0,
                                                            'in_rate_pkts': 0,
                                                            'load_interval': 300,
                                                            'out_rate': 0,
                                                            'out_rate_pkts': 0}},
                                      'enabled': False,
                                      'encapsulations': {'encapsulation': '802.1q '
                                                                          'virtual '
                                                                          'lan',
                                                         'first_dot1q': '10',
                                                         'second_dot1q': '10'},
                                      'interface_state': 0,
                                      'last_input': 'never',
                                      'last_output': 'never',
                                      'line_protocol': 'administratively down',
                                      'oper_status': 'down',
                                      'mac_address': 'aaaa.bbff.8888',
                                      'mtu': 1608,
                                      'reliability': '255/255',
                                      'rxload': '0/255',
                                      'txload': '0/255',
                                      'types': 'vlan sub-(s)'},
        'GigabitEthernet0/0/0/0.20': {'bandwidth': 768,
                                      'counters': {'in_broadcast_pkts': 0,
                                                   'in_discards': 0,
                                                   'in_multicast_pkts': 0,
                                                   'in_octets': 0,
                                                   'in_pkts': 0,
                                                   'in_unknown_protos': 0,
                                                   'last_clear': 'never',
                                                   'out_broadcast_pkts': 0,
                                                   'out_discards': 0,
                                                   'out_multicast_pkts': 0,
                                                   'out_octets': 0,
                                                   'out_pkts': 0,
                                                   'rate': {'in_rate': 0,
                                                            'in_rate_pkts': 0,
                                                            'load_interval': 300,
                                                            'out_rate': 0,
                                                            'out_rate_pkts': 0}},
                                      'enabled': False,
                                      'encapsulations': {'encapsulation': '802.1q '
                                                                          'virtual '
                                                                          'lan',
                                                         'first_dot1q': '20'},
                                      'interface_state': 0,
                                      'last_input': 'never',
                                      'last_output': 'never',
                                      'line_protocol': 'administratively down',
                                      'oper_status': 'down',
                                      'mac_address': 'aaaa.bbff.8888',
                                      'mtu': 1604,
                                      'reliability': '255/255',
                                      'rxload': '0/255',
                                      'txload': '0/255',
                                      'types': 'vlan sub-(s)'},
        'GigabitEthernet0/0/0/1': {'arp_timeout': '04:00:00',
                                   'arp_type': 'arpa',
                                   'auto_negotiate': False,
                                   'bandwidth': 1000000,
                                   'carrier_delay': '10',
                                   'counters': {'carrier_transitions': 1,
                                                'in_abort': 0,
                                                'in_broadcast_pkts': 0,
                                                'in_crc_errors': 0,
                                                'in_discards': 0,
                                                'in_frame': 0,
                                                'in_frame_errors': 0,
                                                'in_giants': 0,
                                                'in_ignored': 0,
                                                'in_multicast_pkts': 29056,
                                                'in_octets': 18221418,
                                                'in_overrun': 0,
                                                'in_parity': 0,
                                                'in_pkts': 146164,
                                                'in_runts': 0,
                                                'in_throttles': 0,
                                                'in_unknown_protos': 0,
                                                'last_clear': 'never',
                                                'out_applique': 0,
                                                'out_broadcast_pkts': 2,
                                                'out_buffer_failures': 0,
                                                'out_buffer_swapped_out': 0,
                                                'out_discards': 0,
                                                'out_errors': 0,
                                                'out_multicast_pkts': 6246,
                                                'out_octets': 10777610,
                                                'out_pkts': 123696,
                                                'out_resets': 0,
                                                'out_underruns': 0,
                                                'rate': {'in_rate': 0,
                                                         'in_rate_pkts': 0,
                                                         'load_interval': 300,
                                                         'out_rate': 0,
                                                         'out_rate_pkts': 0}},
                                   'duplex_mode': 'full',
                                   'enabled': True,
                                   'encapsulations': {'encapsulation': 'arpa'},
                                   'flow_control': {'flow_control_receive': False,
                                                    'flow_control_send': False},
                                   'interface_state': 1,
                                   'ipv4': {'10.1.5.1/24': {'ip': '10.1.5.1',
                                                            'prefix_length': '24'}},
                                   'last_input': '00:01:09',
                                   'last_link_flapped': '1w5d',
                                   'last_output': '00:01:09',
                                   'line_protocol': 'up',
                                   'oper_status': 'up',
                                   'location': 'unknown',
                                   'mac_address': '5254.00ff.6459',
                                   'mtu': 1514,
                                   'phys_address': '5254.00ff.6459',
                                   'port_speed': '1000Mb/s',
                                   'reliability': '255/255',
                                   'rxload': '0/255',
                                   'txload': '0/255',
                                   'types': 'gigabitethernet'},
        'MgmtEth0/0/CPU0/0': {'auto_negotiate': True,
                              'bandwidth': 0,
                              'carrier_delay': '10',
                              'counters': {'carrier_transitions': 0,
                                           'in_abort': 0,
                                           'in_broadcast_pkts': 0,
                                           'in_crc_errors': 0,
                                           'in_discards': 0,
                                           'in_frame': 0,
                                           'in_frame_errors': 0,
                                           'in_giants': 0,
                                           'in_ignored': 0,
                                           'in_multicast_pkts': 0,
                                           'in_octets': 0,
                                           'in_overrun': 0,
                                           'in_parity': 0,
                                           'in_pkts': 0,
                                           'in_runts': 0,
                                           'in_throttles': 0,
                                           'in_unknown_protos': 0,
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
                                                    'load_interval': 300,
                                                    'out_rate': 0,
                                                    'out_rate_pkts': 0}},
                              'duplex_mode': 'duplex unknown',
                              'enabled': False,
                              'encapsulations': {'encapsulation': 'arpa'},
                              'flow_control': {'flow_control_receive': False,
                                               'flow_control_send': False},
                              'interface_state': 0,
                              'last_input': 'never',
                              'last_output': 'never',
                              'line_protocol': 'administratively down',
                              'oper_status': 'down',
                              'location': 'unknown',
                              'mac_address': '5254.00ff.3007',
                              'mtu': 1514,
                              'phys_address': '5254.00ff.3007',
                              'port_speed': '0',
                              'reliability': '255/255',
                              'rxload': 'unknown',
                              'txload': 'unknown',
                              'types': 'management ethernet'},
        'Loopback0': {'bandwidth': 0,
                      'description': 'loopback0 BGP test',
                      'enabled': True,
                      'encapsulations': {'encapsulation': 'loopback'},
                      'interface_state': 1,
                      'ipv4': {'10.255.20.81/32': {'ip': '10.255.20.81',
                                                   'prefix_length': '32'}},
                      'last_input': 'Unknown',
                      'last_link_flapped': '13:45:11',
                      'last_output': 'Unknown',
                      'line_protocol': 'up',
                      'mtu': 1500,
                      'oper_status': 'up',
                      'reliability': 'Unknown',
                      'rxload': 'unknown',
                      'txload': 'unknown'},
        'Null0': {'bandwidth': 0,
                  'counters': {'in_broadcast_pkts': 0,
                               'in_discards': 0,
                               'in_multicast_pkts': 0,
                               'in_octets': 0,
                               'in_pkts': 0,
                               'in_unknown_protos': 0,
                               'last_clear': 'never',
                               'out_broadcast_pkts': 0,
                               'out_discards': 0,
                               'out_multicast_pkts': 0,
                               'out_octets': 0,
                               'out_pkts': 0,
                               'rate': {'in_rate': 0,
                                        'in_rate_pkts': 0,
                                        'load_interval': 300,
                                        'out_rate': 0,
                                        'out_rate_pkts': 0}},
                  'enabled': True,
                  'encapsulations': {'encapsulation': 'null'},
                  'last_input': 'never',
                  'last_output': 'never',
                  'line_protocol': 'up',
                  'oper_status': 'up',
                  'mtu': 1500,
                  'reliability': '255/255',
                  'rxload': 'unknown',
                  'txload': 'unknown',
                  'types': 'null'}}
    golden_parsed_interface_output = {
        'GigabitEthernet0/0/0/1': {
            'arp_timeout': '04:00:00',
            'arp_type': 'arpa',
            'auto_negotiate': False,
            'bandwidth': 1000000,
            'carrier_delay': '10',
            'counters': {
                'carrier_transitions': 1,
                'in_abort': 0,
                'in_broadcast_pkts': 0,
                'in_crc_errors': 0,
                'in_discards': 0,
                'in_frame': 0,
                'in_frame_errors': 0,
                'in_giants': 0,
                'in_ignored': 0,
                'in_multicast_pkts': 29056,
                'in_octets': 18221418,
                'in_overrun': 0,
                'in_parity': 0,
                'in_pkts': 146164,
                'in_runts': 0,
                'in_throttles': 0,
                'in_unknown_protos': 0,
                'last_clear': 'never',
                'out_applique': 0,
                'out_broadcast_pkts': 2,
                'out_buffer_failures': 0,
                'out_buffer_swapped_out': 0,
                'out_discards': 0,
                'out_errors': 0,
                'out_multicast_pkts': 6246,
                'out_octets': 10777610,
                'out_pkts': 123696,
                'out_resets': 0,
                'out_underruns': 0,
                'rate': {'in_rate': 0,
                         'in_rate_pkts': 0,
                         'load_interval': 300,
                         'out_rate': 0,
                         'out_rate_pkts': 0}},
            'duplex_mode': 'full',
            'enabled': True,
            'encapsulations': {'encapsulation': 'arpa'},
            'flow_control': {'flow_control_receive': False,
                             'flow_control_send': False},
            'interface_state': 1,
            'ipv4': {'10.1.5.1/24': {'ip': '10.1.5.1',
                                     'prefix_length': '24'}},
            'last_input': '00:01:09',
            'last_link_flapped': '1w5d',
            'last_output': '00:01:09',
            'line_protocol': 'up',
            'oper_status': 'up',
            'location': 'unknown',
            'mac_address': '5254.00ff.6459',
            'mtu': 1514,
            'phys_address': '5254.00ff.6459',
            'port_speed': '1000Mb/s',
            'reliability': '255/255',
            'rxload': '0/255',
            'txload': '0/255',
            'types': 'gigabitethernet'},
    }

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
      Hardware is Management Ethernet, address is 5254.00ff.3007 (bia 5254.00ff.3007)
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
      Hardware is GigabitEthernet, address is aaaa.bbff.8888 (bia 5254.00ff.0c7e)
      Description: desc
      Internet address is 10.1.1.1/24
      MTU 1600 bytes, BW 768 Kbit (Max: 1000000 Kbit)
         reliability 255/255, txload 0/255, rxload 0/255
      Encapsulation ARPA,
      Full-duplex, 1000Mb/s, unknown, link type is force-up
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
      Hardware is VLAN sub-interface(s), address is aaaa.bbff.8888
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
      Hardware is VLAN sub-interface(s), address is aaaa.bbff.8888
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

    GigabitEthernet0/0/0/1 is up, line protocol is up 
        Interface state transitions: 1
        Hardware is GigabitEthernet, address is 5254.00ff.6459 (bia 5254.00ff.6459)
        Internet address is 10.1.5.1/24
        MTU 1514 bytes, BW 1000000 Kbit (Max: 1000000 Kbit)
         reliability 255/255, txload 0/255, rxload 0/255
        Encapsulation ARPA,
        Full-duplex, 1000Mb/s, unknown, link type is force-up
        output flow control is off, input flow control is off
        Carrier delay (up) is 10 msec
        loopback not set,
        Last link flapped 1w5d
        ARP type ARPA, ARP timeout 04:00:00
        Last input 00:01:09, output 00:01:09
        Last clearing of "show interface" counters never
        5 minute input rate 0 bits/sec, 0 packets/sec
        5 minute output rate 0 bits/sec, 0 packets/sec
         146164 packets input, 18221418 bytes, 0 total input drops
         0 drops for unrecognized upper-level protocol
         Received 0 broadcast packets, 29056 multicast packets
                  0 runts, 0 giants, 0 throttles, 0 parity
         0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored, 0 abort
         123696 packets output, 10777610 bytes, 0 total output drops
         Output 2 broadcast packets, 6246 multicast packets
         0 output errors, 0 underruns, 0 applique, 0 resets
         0 output buffer failures, 0 output buffers swapped out
         1 carrier transitions

    Loopback0 is up, line protocol is up 
      Interface state transitions: 1
      Hardware is Loopback interface(s)
      Description: loopback0 BGP test
      Internet address is 10.255.20.81/32
      MTU 1500 bytes, BW 0 Kbit
         reliability Unknown, txload Unknown, rxload Unknown
      Encapsulation Loopback,  loopback not set,
      Last link flapped 13:45:11
      Last input Unknown, output Unknown
      Last clearing of "show interface" counters Unknown
      Input/output data rate is disabled.
    
    '''}
    golden_interface_output={'execute.return_value':'''
    GigabitEthernet0/0/0/1 is up, line protocol is up 
        Interface state transitions: 1
        Hardware is GigabitEthernet, address is 5254.00ff.6459 (bia 5254.00ff.6459)
        Internet address is 10.1.5.1/24
        MTU 1514 bytes, BW 1000000 Kbit (Max: 1000000 Kbit)
         reliability 255/255, txload 0/255, rxload 0/255
        Encapsulation ARPA,
        Full-duplex, 1000Mb/s, unknown, link type is force-up
        output flow control is off, input flow control is off
        Carrier delay (up) is 10 msec
        loopback not set,
        Last link flapped 1w5d
        ARP type ARPA, ARP timeout 04:00:00
        Last input 00:01:09, output 00:01:09
        Last clearing of "show interface" counters never
        5 minute input rate 0 bits/sec, 0 packets/sec
        5 minute output rate 0 bits/sec, 0 packets/sec
         146164 packets input, 18221418 bytes, 0 total input drops
         0 drops for unrecognized upper-level protocol
         Received 0 broadcast packets, 29056 multicast packets
                  0 runts, 0 giants, 0 throttles, 0 parity
         0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored, 0 abort
         123696 packets output, 10777610 bytes, 0 total output drops
         Output 2 broadcast packets, 6246 multicast packets
         0 output errors, 0 underruns, 0 applique, 0 resets
         0 output buffer failures, 0 output buffers swapped out
         1 carrier transitions
    '''}

    def test_empty(self):
        self.device1 = Mock(**self.empty_output)
        interface_detail_obj = ShowInterfacesDetail(device=self.device1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = interface_detail_obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        interface_detail_obj = ShowInterfacesDetail(device=self.device)
        parsed_output = interface_detail_obj.parse()
        self.maxDiff = None
        self.assertEqual(parsed_output,self.golden_parsed_output)

    def test_golden_custom(self):
        self.device = Mock(**self.golden_interface_output)
        interface_detail_obj = ShowInterfacesDetail(device=self.device)
        parsed_output = interface_detail_obj.parse(interface='GigabitEthernet0/0/0/1')
        self.maxDiff = None
        self.assertEqual(parsed_output, self.golden_parsed_interface_output)


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

    golden_parsed_output = {'GigabitEthernet0/0/0/0': {'int_status': 'up',
                            'ipv4': {'10.1.3.1/24': {'ip': '10.1.3.1',
                                                     'prefix_length': '24'},
                                     'broadcast_forwarding': 'disabled',
                                     'icmp_redirects': 'never sent',
                                     'icmp_replies': 'never sent',
                                     'icmp_unreachables': 'always sent',
                                     'mtu': 1514,
                                     'mtu_available': 1500,
                                     'proxy_arp': 'disabled',
                                     'table_id': '0xe0000000'},
                            'multicast_groups': ['224.0.0.2',
                                                 '224.0.0.1',
                                                 '224.0.0.2',
                                                 '224.0.0.5',
                                                 '224.0.0.6'],
                            'oper_status': 'up',
                            'vrf': 'default',
                            'vrf_id': '0x60000000'},
 'GigabitEthernet0/0/0/1': {'int_status': 'up',
                            'ipv4': {'10.1.5.1/24': {'ip': '10.1.5.1',
                                                     'prefix_length': '24',
                                                     'route_tag': 50},
                                     '10.2.2.2/24': {'ip': '10.2.2.2',
                                                     'prefix_length': '24',
                                                     'secondary': True},
                                     'broadcast_forwarding': 'disabled',
                                     'icmp_redirects': 'never sent',
                                     'icmp_replies': 'never sent',
                                     'icmp_unreachables': 'always sent',
                                     'mtu': 1514,
                                     'mtu_available': 1500,
                                     'proxy_arp': 'disabled',
                                     'table_id': '0xe0000010'},
                            'multicast_groups': ['224.0.0.2', '224.0.0.1'],
                            'oper_status': 'up',
                            'vrf': 'VRF1',
                            'vrf_id': '0x60000001'},
 'GigabitEthernet0/0/0/2': {'int_status': 'up',
                            'ipv4': {'10.186.5.1/24': {'ip': '10.186.5.1',
                                                     'prefix_length': '24'},
                                     'broadcast_forwarding': 'disabled',
                                     'icmp_redirects': 'never sent',
                                     'icmp_replies': 'never sent',
                                     'icmp_unreachables': 'always sent',
                                     'mtu': 1514,
                                     'mtu_available': 1500,
                                     'proxy_arp': 'disabled',
                                     'table_id': '0xe0000011'},
                            'multicast_groups': ['224.0.0.2', '224.0.0.1'],
                            'oper_status': 'up',
                            'vrf': 'VRF2',
                            'vrf_id': '0x60000002'},
 'GigabitEthernet0/0/0/3': {'int_status': 'up',
                            'ipv4': {'10.1.2.1/24': {'ip': '10.1.2.1',
                                                     'prefix_length': '24'},
                                     'broadcast_forwarding': 'disabled',
                                     'icmp_redirects': 'never sent',
                                     'icmp_replies': 'never sent',
                                     'icmp_unreachables': 'always sent',
                                     'mtu': 1514,
                                     'mtu_available': 1500,
                                     'proxy_arp': 'disabled',
                                     'table_id': '0xe0000000'},
                            'multicast_groups': ['224.0.0.2',
                                                 '224.0.0.1',
                                                 '224.0.0.2',
                                                 '224.0.0.5',
                                                 '224.0.0.6'],
                            'oper_status': 'up',
                            'vrf': 'default',
                            'vrf_id': '0x60000000'},
 'GigabitEthernet0/0/0/4': {'int_status': 'up',
                            'ipv4': {'10.69.111.111/32': {'ip': '10.69.111.111',
                                                            'prefix_length': '32'},
                                     'broadcast_forwarding': 'disabled',
                                     'icmp_redirects': 'never sent',
                                     'icmp_replies': 'never sent',
                                     'icmp_unreachables': 'always sent',
                                     'mtu': 1514,
                                     'mtu_available': 1500,
                                     'proxy_arp': 'disabled',
                                     'table_id': '0xe0000000',
                                     'unnumbered': {'unnumbered_intf_ref': 'Loopback11'}},
                            'multicast_groups': ['224.0.0.2', '224.0.0.1'],
                            'oper_status': 'up',
                            'vrf': 'default',
                            'vrf_id': '0x60000000'},
 'GigabitEthernet0/0/0/5': {'int_status': 'shutdown',
                            'oper_status': 'down',
                            'vrf': 'default',
                            'vrf_id': '0x60000000'},
 'GigabitEthernet0/0/0/6': {'int_status': 'shutdown',
                            'oper_status': 'down',
                            'vrf': 'default',
                            'vrf_id': '0x60000000'},
 'Loopback0': {'int_status': 'up',
               'ipv4': {'10.4.1.1/32': {'ip': '10.4.1.1',
                                       'prefix_length': '32'},
                        'broadcast_forwarding': 'disabled',
                        'icmp_redirects': 'never sent',
                        'icmp_replies': 'never sent',
                        'icmp_unreachables': 'always sent',
                        'mtu': 1500,
                        'mtu_available': 1500,
                        'proxy_arp': 'disabled',
                        'table_id': '0xe0000000'},
               'oper_status': 'up',
               'vrf': 'default',
               'vrf_id': '0x60000000'},
 'Loopback11': {'int_status': 'up',
                'ipv4': {'10.69.111.111/32': {'ip': '10.69.111.111',
                                                'prefix_length': '32'},
                         'broadcast_forwarding': 'disabled',
                         'icmp_redirects': 'never sent',
                         'icmp_replies': 'never sent',
                         'icmp_unreachables': 'always sent',
                         'mtu': 1500,
                         'mtu_available': 1500,
                         'proxy_arp': 'disabled',
                         'table_id': '0xe0000000'},
                'oper_status': 'up',
                'vrf': 'default',
                'vrf_id': '0x60000000'},
 'MgmtEth0/0/CPU0/0': {'int_status': 'shutdown',
                       'oper_status': 'down',
                       'vrf': 'default',
                       'vrf_id': '0x60000000'}}

    golden_output = {'execute.return_value': '''
        Loopback0 is Up, ipv4 protocol is Up
      Vrf is default (vrfid 0x60000000)
      Internet address is 10.4.1.1/32
      MTU is 1500 (1500 is available to IP)
      Helper address is not set
      Directed broadcast forwarding is disabled
      Outgoing access list is not set
      Inbound  common access list is not set, access list is not set
      Proxy ARP is disabled
      ICMP redirects are never sent
      ICMP unreachables are always sent
      ICMP mask replies are never sent
      Table Id is 0xe0000000
    Loopback11 is Up, ipv4 protocol is Up
      Vrf is default (vrfid 0x60000000)
      Internet address is 10.69.111.111/32
      MTU is 1500 (1500 is available to IP)
      Helper address is not set
      Directed broadcast forwarding is disabled
      Outgoing access list is not set
      Inbound  common access list is not set, access list is not set
      Proxy ARP is disabled
      ICMP redirects are never sent
      ICMP unreachables are always sent
      ICMP mask replies are never sent
      Table Id is 0xe0000000
    MgmtEth0/0/CPU0/0 is Shutdown, ipv4 protocol is Down
      Vrf is default (vrfid 0x60000000)
      Internet protocol processing disabled
    GigabitEthernet0/0/0/0 is Up, ipv4 protocol is Up
      Vrf is default (vrfid 0x60000000)
      Internet address is 10.1.3.1/24
      MTU is 1514 (1500 is available to IP)
      Helper address is not set
      Multicast reserved groups joined: 224.0.0.2 224.0.0.1 224.0.0.2
          224.0.0.5 224.0.0.6
      Directed broadcast forwarding is disabled
      Outgoing access list is not set
      Inbound  common access list is not set, access list is not set
      Proxy ARP is disabled
      ICMP redirects are never sent
      ICMP unreachables are always sent
      ICMP mask replies are never sent
      Table Id is 0xe0000000
    GigabitEthernet0/0/0/1 is Up, ipv4 protocol is Up
      Vrf is VRF1 (vrfid 0x60000001)
      Internet address is 10.1.5.1/24 with route-tag 50
      Secondary address 10.2.2.2/24
      MTU is 1514 (1500 is available to IP)
      Helper address is not set
      Multicast reserved groups joined: 224.0.0.2 224.0.0.1
      Directed broadcast forwarding is disabled
      Outgoing access list is not set
      Inbound  common access list is not set, access list is not set
      Proxy ARP is disabled
      ICMP redirects are never sent
      ICMP unreachables are always sent
      ICMP mask replies are never sent
      Table Id is 0xe0000010
    GigabitEthernet0/0/0/2 is Up, ipv4 protocol is Up
      Vrf is VRF2 (vrfid 0x60000002)
      Internet address is 10.186.5.1/24
      MTU is 1514 (1500 is available to IP)
      Helper address is not set
      Multicast reserved groups joined: 224.0.0.2 224.0.0.1
      Directed broadcast forwarding is disabled
      Outgoing access list is not set
      Inbound  common access list is not set, access list is not set
      Proxy ARP is disabled
      ICMP redirects are never sent
      ICMP unreachables are always sent
      ICMP mask replies are never sent
      Table Id is 0xe0000011
    GigabitEthernet0/0/0/3 is Up, ipv4 protocol is Up
      Vrf is default (vrfid 0x60000000)
      Internet address is 10.1.2.1/24
      MTU is 1514 (1500 is available to IP)
      Helper address is not set
      Multicast reserved groups joined: 224.0.0.2 224.0.0.1 224.0.0.2
          224.0.0.5 224.0.0.6
      Directed broadcast forwarding is disabled
      Outgoing access list is not set
      Inbound  common access list is not set, access list is not set
      Proxy ARP is disabled
      ICMP redirects are never sent
      ICMP unreachables are always sent
      ICMP mask replies are never sent
      Table Id is 0xe0000000
    GigabitEthernet0/0/0/4 is Up, ipv4 protocol is Up
      Vrf is default (vrfid 0x60000000)
      Interface is unnumbered.  Using address of Loopback11 (10.69.111.111/32)
      MTU is 1514 (1500 is available to IP)
      Helper address is not set
      Multicast reserved groups joined: 224.0.0.2 224.0.0.1
      Directed broadcast forwarding is disabled
      Outgoing access list is not set
      Inbound  common access list is not set, access list is not set
      Proxy ARP is disabled
      ICMP redirects are never sent
      ICMP unreachables are always sent
      ICMP mask replies are never sent
      Table Id is 0xe0000000
    GigabitEthernet0/0/0/5 is Shutdown, ipv4 protocol is Down
      Vrf is default (vrfid 0x60000000)
      Internet protocol processing disabled
    GigabitEthernet0/0/0/6 is Shutdown, ipv4 protocol is Down
      Vrf is default (vrfid 0x60000000)
      Internet protocol processing disabled
    '''}
    golden_parsed_output_custom = {'GigabitEthernet0/0/0/1': {'int_status': 'up',
                                                       'ipv4': {'10.1.5.1/24': {
                                                           'ip': '10.1.5.1',
                                                           'prefix_length': '24',
                                                           'route_tag': 50},
                                                                '10.2.2.2/24': {
                                                                    'ip': '10.2.2.2',
                                                                    'prefix_length': '24',
                                                                    'secondary': True},
                                                                'broadcast_forwarding':
                                                                    'disabled',
                                                                'icmp_redirects':
                                                                    'never sent',
                                                                'icmp_replies': 'never '
                                                                                'sent',
                                                                'icmp_unreachables':
                                                                    'always sent',
                                                                'mtu': 1514,
                                                                'mtu_available': 1500,
                                                                'proxy_arp': 'disabled',
                                                                'table_id': '0xe0000010'},
                                                       'multicast_groups': ['224.0.0.2',
                                                                            '224.0.0.1'],
                                                       'oper_status': 'up',
                                                       'vrf': 'VRF1',
                                                       'vrf_id': '0x60000001'},
                            }
    golden_output_custom={'execute.return_value': '''
      GigabitEthernet0/0/0/1 is Up, ipv4 protocol is Up
      Vrf is VRF1 (vrfid 0x60000001)
      Internet address is 10.1.5.1/24 with route-tag 50
      Secondary address 10.2.2.2/24
      MTU is 1514 (1500 is available to IP)
      Helper address is not set
      Multicast reserved groups joined: 224.0.0.2 224.0.0.1
      Directed broadcast forwarding is disabled
      Outgoing access list is not set
      Inbound  common access list is not set, access list is not set
      Proxy ARP is disabled
      ICMP redirects are never sent
      ICMP unreachables are always sent
      ICMP mask replies are never sent
      Table Id is 0xe0000010
      '''
    }

    golden_parsed_output3 = {
        'GigabitEthernet0/0/0/0': {
            'int_status': 'up',
            'ipv4': {
                '192.168.1.242/24': {
                    'ip': '192.168.1.242',
                    'prefix_length': '24',
                },
                'broadcast_forwarding': 'disabled',
                'icmp_redirects': 'never sent',
                'icmp_replies': 'never sent',
                'icmp_unreachables': 'always sent',
                'mtu': 1514,
                'mtu_available': 1500,
                'proxy_arp': 'disabled',
                'table_id': '0xe0000003',
            },
            'multicast_groups': ['224.0.0.5', '224.0.0.6'],
            'oper_status': 'up',
            'vrf': 'VRF1:111',
            'vrf_id': '0x60000003',
        },
        'GigabitEthernet0/0/0/1': {
            'int_status': 'up',
            'ipv4': {
                '192.168.2.249/24': {
                    'ip': '192.168.2.249',
                    'prefix_length': '24',
                },
                'broadcast_forwarding': 'disabled',
                'icmp_redirects': 'never sent',
                'icmp_replies': 'never sent',
                'icmp_unreachables': 'always sent',
                'mtu': 1514,
                'mtu_available': 1500,
                'proxy_arp': 'disabled',
                'table_id': '0xe0000000',
            },
            'multicast_groups': ['224.0.0.2'],
            'oper_status': 'up',
            'vrf': 'default',
            'vrf_id': '0x60000000',
        },
        'GigabitEthernet0/0/0/2': {
            'int_status': 'shutdown',
            'oper_status': 'down',
            'vrf': 'default',
            'vrf_id': '0x60000000',
        },
        'GigabitEthernet0/0/0/3': {
            'int_status': 'shutdown',
            'oper_status': 'down',
            'vrf': 'V20:MBN',
            'vrf_id': '0x0',
        },
        'GigabitEthernet0/0/0/4': {
            'int_status': 'shutdown',
            'oper_status': 'down',
            'vrf': 'default',
            'vrf_id': '0x60000000',
        },
        'GigabitEthernet0/0/0/5': {
            'int_status': 'shutdown',
            'oper_status': 'down',
            'vrf': 'default',
            'vrf_id': '0x60000000',
        },
        'GigabitEthernet0/0/0/6': {
            'int_status': 'shutdown',
            'oper_status': 'down',
            'vrf': 'bobby',
            'vrf_id': '0x60000001',
        },
        'MgmtEth0/RP0/CPU0/0': {
            'int_status': 'up',
            'oper_status': 'up',
            'vrf': 'bobby',
            'vrf_id': '0x60000001',
        },
    }



    golden_output3 = {'execute.return_value': '''
        MgmtEth0/RP0/CPU0/0 is Up, ipv4 protocol is Up 
        Vrf is bobby (vrfid 0x60000001)
        Internet protocol processing disabled
        GigabitEthernet0/0/0/0 is Up, ipv4 protocol is Up 
        Vrf is VRF1:111 (vrfid 0x60000003)
        Internet address is 192.168.1.242/24
        MTU is 1514 (1500 is available to IP)
        Helper address is not set
        Multicast reserved groups joined: 224.0.0.5 224.0.0.6
        Directed broadcast forwarding is disabled
        Outgoing access list is not set
        Inbound  common access list is not set, access list is not set
        Proxy ARP is disabled
        ICMP redirects are never sent
        ICMP unreachables are always sent
        ICMP mask replies are never sent
        Table Id is 0xe0000003
        GigabitEthernet0/0/0/1 is Up, ipv4 protocol is Up 
        Vrf is default (vrfid 0x60000000)
        Internet address is 192.168.2.249/24
        MTU is 1514 (1500 is available to IP)
        Helper address is not set
        Multicast reserved groups joined: 224.0.0.2
        Directed broadcast forwarding is disabled
        Outgoing access list is not set
        Inbound  common access list is not set, access list is not set
        Proxy ARP is disabled
        ICMP redirects are never sent
        ICMP unreachables are always sent
        ICMP mask replies are never sent
        Table Id is 0xe0000000
        GigabitEthernet0/0/0/2 is Shutdown, ipv4 protocol is Down 
        Vrf is default (vrfid 0x60000000)
        Internet protocol processing disabled
        GigabitEthernet0/0/0/3 is Shutdown, ipv4 protocol is Down 
        Vrf is V20:MBN (vrfid 0x0)
        Internet protocol processing disabled
        GigabitEthernet0/0/0/4 is Shutdown, ipv4 protocol is Down 
        Vrf is default (vrfid 0x60000000)
        Internet protocol processing disabled
        GigabitEthernet0/0/0/5 is Shutdown, ipv4 protocol is Down 
        Vrf is default (vrfid 0x60000000)
        Internet protocol processing disabled
        GigabitEthernet0/0/0/6 is Shutdown, ipv4 protocol is Down 
        Vrf is bobby (vrfid 0x60000001)
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
    def test_golden_custom(self):
        self.device = Mock(**self.golden_output_custom)
        ipv4_vrf_all_interface_obj = ShowIpv4VrfAllInterface(device=self.device)
        parsed_output = ipv4_vrf_all_interface_obj.parse(vrf='VRF1', interface='GigabitEthernet0/0/0/1')
        self.maxDiff = None
        self.assertEqual(parsed_output,self.golden_parsed_output_custom)

    def test_golden3(self):
        self.device = Mock(**self.golden_output3)
        ipv4_vrf_all_interface_obj = ShowIpv4VrfAllInterface(device=self.device)
        parsed_output = ipv4_vrf_all_interface_obj.parse()
        self.maxDiff = None
        self.assertEqual(parsed_output,self.golden_parsed_output3)        

#############################################################################
# unitest For show ipv6 vrf all interface
#############################################################################

class test_show_ipv6_vrf_all_interface(unittest.TestCase):
    device = Device(name='aDevice')
    device0 = Device(name='bDevice')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output = {
        'GigabitEthernet0/0/0/0': {'enabled': True,
                            'int_status': 'shutdown',
                            'ipv6': {'2001:db8:1:1::1/64': {'ipv6': '2001:db8:1:1::1',
                                                            'ipv6_prefix_length': '64',
                                                            'ipv6_status': 'tentative',
                                                            'ipv6_subnet': '2001:db8:1:1::'},
                                     '2001:db8:2:2::2/64': {'ipv6': '2001:db8:2:2::2',
                                                            'ipv6_prefix_length': '64',
                                                            'ipv6_status': 'tentative',
                                                            'ipv6_subnet': '2001:db8:2:2::'},
                                     '2001:db8:3:3:a8aa:bbff:feff:8888/64': {'ipv6': '2001:db8:3:3:a8aa:bbff:feff:8888',
                                                                             'ipv6_eui64': True,
                                                                             'ipv6_prefix_length': '64',
                                                                             'ipv6_status': 'tentative',
                                                                             'ipv6_subnet': '2001:db8:3:3::'},
                                     '2001:db8:4:4::4/64': {'ipv6': '2001:db8:4:4::4',
                                                            'ipv6_prefix_length': '64',
                                                            'ipv6_route_tag': '10',
                                                            'ipv6_status': 'tentative',
                                                            'ipv6_subnet': '2001:db8:4:4::'},
                                     'complete_glean_adj': '0',
                                     'complete_protocol_adj': '0',
                                     'dad_attempts': '1',
                                     'dropped_glean_req': '0',
                                     'dropped_protocol_req': '0',
                                     'icmp_redirects': 'disabled',
                                     'icmp_unreachables': 'enabled',
                                     'incomplete_glean_adj': '0',
                                     'incomplete_protocol_adj': '0',
                                     'ipv6_groups': ['ff02::2', 'ff02::1'],
                                     'ipv6_link_local': 'fe80::a8aa:bbff:feff:8888',
                                     'ipv6_link_local_state': 'tentative',
                                     'ipv6_mtu': '1600',
                                     'ipv6_mtu_available': '1586',
                                     'nd_adv_retrans_int': '0',
                                     'nd_cache_limit': '1000000000',
                                     'nd_dad': 'enabled',
                                     'nd_reachable_time': '0',
                                     'stateless_autoconfig': True,
                                     'table_id': '0xe0800011'},
                            'ipv6_enabled': False,
                            'oper_status': 'down',
                            'vrf': 'VRF1',
                            'vrf_id': '0x60000002'},
        'GigabitEthernet0/0/0/0.10': {'enabled': True,
                                      'int_status': 'shutdown',
                                      'ipv6': {'2001:db8:1:3::1/64': {'ipv6': '2001:db8:1:3::1',
                                                                      'ipv6_prefix_length': '64',
                                                                      'ipv6_subnet': '2001:db8:1:3::'},
                                               'complete_glean_adj': '0',
                                               'complete_protocol_adj': '0',
                                               'dad_attempts': '1',
                                               'dropped_glean_req': '0',
                                               'dropped_protocol_req': '0',
                                               'icmp_redirects': 'disabled',
                                               'icmp_unreachables': 'enabled',
                                               'incomplete_glean_adj': '0',
                                               'incomplete_protocol_adj': '0',
                                               'ipv6_groups': ['ff02::1:ff00:1',
                                                               'ff02::1:ffa6:78c5',
                                                               'ff02::2',
                                                               'ff02::1'],
                                               'ipv6_link_local': 'fe80::5054:ff:fea6:78c5',
                                               'ipv6_mtu': '1514',
                                               'ipv6_mtu_available': '1500',
                                               'nd_adv_duration': '160-240',
                                               'nd_adv_retrans_int': '0',
                                               'nd_cache_limit': '1000000000',
                                               'nd_dad': 'enabled',
                                               'nd_reachable_time': '0',
                                               'nd_router_adv': '1800',
                                               'stateless_autoconfig': True,
                                               'table_id': '0xe0800000'},
                                      'ipv6_enabled': False,
                                      'oper_status': 'down',
                                      'vrf': 'default',
                                      'vrf_id': '0x60000000'},
        'GigabitEthernet0/0/0/1': {'enabled': True,
                                   'int_status': 'up',
                                   'ipv6': {'2001:db8:1:5::1/64': {'ipv6': '2001:db8:1:5::1',
                                                                   'ipv6_prefix_length': '64',
                                                                   'ipv6_subnet': '2001:db8:1:5::'},
                                            'complete_glean_adj': '1',
                                            'complete_protocol_adj': '1',
                                            'dad_attempts': '1',
                                            'dropped_glean_req': '0',
                                            'dropped_protocol_req': '0',
                                            'icmp_redirects': 'disabled',
                                            'icmp_unreachables': 'enabled',
                                            'incomplete_glean_adj': '0',
                                            'incomplete_protocol_adj': '0',
                                            'ipv6_groups': ['ff02::1:ff00:1',
                                                            'ff02::1:ff78:ebe0',
                                                            'ff02::2',
                                                            'ff02::1'],
                                            'ipv6_link_local': 'fe80::5054:ff:fe78:ebe0',
                                            'ipv6_mtu': '1514',
                                            'ipv6_mtu_available': '1500',
                                            'nd_adv_duration': '160-240',
                                            'nd_adv_retrans_int': '0',
                                            'nd_cache_limit': '1000000000',
                                            'nd_dad': 'enabled',
                                            'nd_reachable_time': '0',
                                            'nd_router_adv': '1800',
                                            'stateless_autoconfig': True,
                                            'table_id': '0xe0800010'},
                                   'ipv6_enabled': True,
                                   'oper_status': 'up',
                                   'vrf': 'VRF1',
                                   'vrf_id': '0x60000001'},
        'GigabitEthernet0/0/0/2': {'enabled': True,
                                   'int_status': 'up',
                                   'ipv6': {'2001:db8:20:1:5::1/64': {'ipv6': '2001:db8:20:1:5::1',
                                                                      'ipv6_prefix_length': '64',
                                                                      'ipv6_subnet': '2001:db8:20:1::'},
                                            'complete_glean_adj': '2',
                                            'complete_protocol_adj': '0',
                                            'dad_attempts': '1',
                                            'dropped_glean_req': '0',
                                            'dropped_protocol_req': '0',
                                            'icmp_redirects': 'disabled',
                                            'icmp_unreachables': 'enabled',
                                            'incomplete_glean_adj': '0',
                                            'incomplete_protocol_adj': '0',
                                            'ipv6_groups': ['ff02::1:ff00:1',
                                                            'ff02::1:ff15:c05c',
                                                            'ff02::2',
                                                            'ff02::1'],
                                            'ipv6_link_local': 'fe80::5054:ff:fe15:c05c',
                                            'ipv6_mtu': '1514',
                                            'ipv6_mtu_available': '1500',
                                            'nd_adv_duration': '160-240',
                                            'nd_adv_retrans_int': '0',
                                            'nd_cache_limit': '1000000000',
                                            'nd_dad': 'enabled',
                                            'nd_reachable_time': '0',
                                            'nd_router_adv': '1800',
                                            'stateless_autoconfig': True,
                                            'table_id': '0xe0800011'},
                                   'ipv6_enabled': True,
                                   'oper_status': 'up',
                                   'vrf': 'VRF2',
                                   'vrf_id': '0x60000002'},
        'GigabitEthernet0/0/0/3': {'enabled': False,
                                   'int_status': 'up',
                                   'ipv6_enabled': True,
                                   'oper_status': 'up',
                                   'vrf': 'default',
                                   'vrf_id': '0x60000000'},
        'GigabitEthernet0/0/0/4': {'enabled': False,
                                   'int_status': 'up',
                                   'ipv6_enabled': True,
                                   'oper_status': 'up',
                                   'vrf': 'default',
                                   'vrf_id': '0x60000000'},
        'GigabitEthernet0/0/0/5': {'enabled': False,
                                   'int_status': 'shutdown',
                                   'ipv6_enabled': False,
                                   'oper_status': 'down',
                                   'vrf': 'default',
                                   'vrf_id': '0x60000000'},
        'GigabitEthernet0/0/0/6': {'enabled': False,
                                   'int_status': 'shutdown',
                                   'ipv6_enabled': False,
                                   'oper_status': 'down',
                                   'vrf': 'default',
                                   'vrf_id': '0x60000000'},
        'MgmtEth0/0/CPU0/0': {'enabled': False,
                       'int_status': 'shutdown',
                       'ipv6_enabled': False,
                       'oper_status': 'down',
                       'vrf': 'default',
                       'vrf_id': '0x60000000'}}

    golden_output = {'execute.return_value': '''
    MgmtEth0/0/CPU0/0 is Shutdown, ipv6 protocol is Down, Vrfid is default (0x60000000)
      IPv6 is disabled, link-local address unassigned
      No global unicast address is configured
    GigabitEthernet0/0/0/0 is Shutdown, ipv6 protocol is Down, Vrfid is VRF1 (0x60000002)
      IPv6 is enabled, link-local address is fe80::a8aa:bbff:feff:8888 [TENTATIVE]
      Global unicast address(es):
        2001:db8:1:1::1, subnet is 2001:db8:1:1::/64 [TENTATIVE]
        2001:db8:2:2::2, subnet is 2001:db8:2:2::/64 [TENTATIVE]
        2001:db8:4:4::4, subnet is 2001:db8:4:4::/64 [TENTATIVE] with route-tag 10
        2001:db8:3:3:a8aa:bbff:feff:8888, subnet is 2001:db8:3:3::/64 [TENTATIVE]
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
      IPv6 is enabled, link-local address is fe80::5054:ff:fea6:78c5 
      Global unicast address(es):
        2001:db8:1:3::1, subnet is 2001:db8:1:3::/64 
      Joined group address(es): ff02::1:ff00:1 ff02::1:ffa6:78c5 ff02::2
          ff02::1
      MTU is 1514 (1500 is available to IPv6)
      ICMP redirects are disabled
      ICMP unreachables are enabled
      ND DAD is enabled, number of DAD attempts 1
      ND reachable time is 0 milliseconds
      ND cache entry limit is 1000000000
      ND advertised retransmit interval is 0 milliseconds
      ND router advertisements are sent every 160 to 240 seconds
      ND router advertisements live for 1800 seconds
      Hosts use stateless autoconfig for addresses.
      Outgoing access list is not set
      Inbound  common access list is not set, access list is not set
      Table Id is 0xe0800000
      Complete protocol adjacency: 0
      Complete glean adjacency: 0
      Incomplete protocol adjacency: 0
      Incomplete glean adjacency: 0
      Dropped protocol request: 0
      Dropped glean request: 0
    GigabitEthernet0/0/0/1 is Up, ipv6 protocol is Up, Vrfid is VRF1 (0x60000001)
      IPv6 is enabled, link-local address is fe80::5054:ff:fe78:ebe0 
      Global unicast address(es):
        2001:db8:1:5::1, subnet is 2001:db8:1:5::/64 
      Joined group address(es): ff02::1:ff00:1 ff02::1:ff78:ebe0 ff02::2
          ff02::1
      MTU is 1514 (1500 is available to IPv6)
      ICMP redirects are disabled
      ICMP unreachables are enabled
      ND DAD is enabled, number of DAD attempts 1
      ND reachable time is 0 milliseconds
      ND cache entry limit is 1000000000
      ND advertised retransmit interval is 0 milliseconds
      ND router advertisements are sent every 160 to 240 seconds
      ND router advertisements live for 1800 seconds
      Hosts use stateless autoconfig for addresses.
      Outgoing access list is not set
      Inbound  common access list is not set, access list is not set
      Table Id is 0xe0800010
      Complete protocol adjacency: 1
      Complete glean adjacency: 1
      Incomplete protocol adjacency: 0
      Incomplete glean adjacency: 0
      Dropped protocol request: 0
      Dropped glean request: 0
    GigabitEthernet0/0/0/2 is Up, ipv6 protocol is Up, Vrfid is VRF2 (0x60000002)
      IPv6 is enabled, link-local address is fe80::5054:ff:fe15:c05c 
      Global unicast address(es):
        2001:db8:20:1:5::1, subnet is 2001:db8:20:1::/64 
      Joined group address(es): ff02::1:ff00:1 ff02::1:ff15:c05c ff02::2
          ff02::1
      MTU is 1514 (1500 is available to IPv6)
      ICMP redirects are disabled
      ICMP unreachables are enabled
      ND DAD is enabled, number of DAD attempts 1
      ND reachable time is 0 milliseconds
      ND cache entry limit is 1000000000
      ND advertised retransmit interval is 0 milliseconds
      ND router advertisements are sent every 160 to 240 seconds
      ND router advertisements live for 1800 seconds
      Hosts use stateless autoconfig for addresses.
      Outgoing access list is not set
      Inbound  common access list is not set, access list is not set
      Table Id is 0xe0800011
      Complete protocol adjacency: 0
      Complete glean adjacency: 2
      Incomplete protocol adjacency: 0
      Incomplete glean adjacency: 0
      Dropped protocol request: 0
      Dropped glean request: 0
    GigabitEthernet0/0/0/3 is Up, ipv6 protocol is Up, Vrfid is default (0x60000000)
      IPv6 is disabled, link-local address unassigned
      No global unicast address is configured
    GigabitEthernet0/0/0/4 is Up, ipv6 protocol is Up, Vrfid is default (0x60000000)
      IPv6 is disabled, link-local address unassigned
      No global unicast address is configured
    GigabitEthernet0/0/0/5 is Shutdown, ipv6 protocol is Down, Vrfid is default (0x60000000)
      IPv6 is disabled, link-local address unassigned
      No global unicast address is configured
    GigabitEthernet0/0/0/6 is Shutdown, ipv6 protocol is Down, Vrfid is default (0x60000000)
      IPv6 is disabled, link-local address unassigned
      No global unicast address is configured
    
    '''}

    golden_parsed_output1 = {
        'GigabitEthernet0/0/0/0': {
            'enabled': True,
            'int_status': 'up',
            'ipv6': {
                '2001:db8:8548:1::2/64': {
                    'ipv6': '2001:db8:8548:1::2',
                    'ipv6_prefix_length': '64',
                    'ipv6_subnet': '2001:db8:8548:1::'},
                'complete_glean_adj': '1',
                'complete_protocol_adj': '1',
                'dad_attempts': '1',
                'dropped_glean_req': '0',
                'dropped_protocol_req': '0',
                'icmp_redirects': 'disabled',
                'icmp_unreachables': 'enabled',
                'incomplete_glean_adj': '0',
                'incomplete_protocol_adj': '0',
                'ipv6_groups': ['ff02::1:ff00:2',
                                'ff02::1:ffca:3efd',
                                'ff02::2',
                                'ff02::1',
                                'ff02::5',
                                'ff02::6'],
                'ipv6_link_local': 'fe80::f816:3eff:feca:3efd',
                'ipv6_mtu': '1514',
                'ipv6_mtu_available': '1500',
                'nd_adv_retrans_int': '0',
                'nd_cache_limit': '1000000000',
                'nd_dad': 'enabled',
                'nd_reachable_time': '0',
                'stateless_autoconfig': True,
                'table_id': '0xe0800000'},
            'ipv6_enabled': True,
            'oper_status': 'up',
            'vrf': 'default',
            'vrf_id': '0x60000000'},
        'GigabitEthernet0/0/0/1': {
            'enabled': True,
            'int_status': 'up',
            'ipv6': {
                '2001:db8:888c:1::2/64': {
                    'ipv6': '2001:db8:888c:1::2',
                    'ipv6_prefix_length': '64',
                    'ipv6_subnet': '2001:db8:888c:1::'},
                'complete_glean_adj': '2',
                'complete_protocol_adj': '0',
                'dad_attempts': '1',
                'dropped_glean_req': '0',
                'dropped_protocol_req': '0',
                'icmp_redirects': 'disabled',
                'icmp_unreachables': 'enabled',
                'incomplete_glean_adj': '0',
                'incomplete_protocol_adj': '0',
                'ipv6_groups': ['ff02::1:ff00:2',
                                'ff02::1:ff20:fa5b',
                                'ff02::2',
                                'ff02::1',
                                'ff02::5',
                                'ff02::6'],
                'ipv6_link_local': 'fe80::f816:3eff:fe20:fa5b',
                'ipv6_mtu': '1514',
                'ipv6_mtu_available': '1500',
                'nd_adv_duration': '160-240',
                'nd_adv_retrans_int': '0',
                'nd_cache_limit': '1000000000',
                'nd_dad': 'enabled',
                'nd_reachable_time': '0',
                'nd_router_adv': '1800',
                'stateless_autoconfig': True,
                'table_id': '0xe0800001'},
            'ipv6_enabled': True,
            'oper_status': 'up',
            'vrf': 'VRF1',
            'vrf_id': '0x60000001'},
        'GigabitEthernet0/0/0/2': {
            'enabled': True,
            'int_status': 'up',
            'ipv6': {
                '2001:db8:c56d:4::2/64': {
                    'ipv6': '2001:db8:c56d:4::2',
                    'ipv6_prefix_length': '64',
                    'ipv6_subnet': '2001:db8:c56d:4::'},
                'complete_glean_adj': '1',
                'complete_protocol_adj': '1',
                'dad_attempts': '1',
                'dropped_glean_req': '0',
                'dropped_protocol_req': '0',
                'icmp_redirects': 'disabled',
                'icmp_unreachables': 'enabled',
                'incomplete_glean_adj': '0',
                'incomplete_protocol_adj': '0',
                'ipv6_groups': ['ff02::1:ff00:2',
                                'ff02::1:ff82:6320',
                                'ff02::2',
                                'ff02::1',
                                'ff02::5',
                                'ff02::6'],
                'ipv6_link_local': 'fe80::f816:3eff:fe82:6320',
                'ipv6_mtu': '1514',
                'ipv6_mtu_available': '1500',
                'nd_adv_duration': '160-240',
                'nd_adv_retrans_int': '0',
                'nd_cache_limit': '1000000000',
                'nd_dad': 'enabled',
                'nd_reachable_time': '0',
                'nd_router_adv': '1800',
                'stateless_autoconfig': True,
                'table_id': '0xe0800000'},
            'ipv6_enabled': True,
            'oper_status': 'up',
            'vrf': 'default',
            'vrf_id': '0x60000000'},
        'GigabitEthernet0/0/0/3': {
            'enabled': True,
            'int_status': 'up',
            'ipv6': {
                '2001:db8:c8d1:4::2/64': {
                    'ipv6': '2001:db8:c8d1:4::2',
                    'ipv6_prefix_length': '64',
                    'ipv6_subnet': '2001:db8:c8d1:4::'},
                'complete_glean_adj': '1',
                'complete_protocol_adj': '1',
                'dad_attempts': '1',
                'dropped_glean_req': '0',
                'dropped_protocol_req': '0',
                'icmp_redirects': 'disabled',
                'icmp_unreachables': 'enabled',
                'incomplete_glean_adj': '0',
                'incomplete_protocol_adj': '0',
                'ipv6_groups': ['ff02::1:ff00:2',
                                'ff02::1:ff8b:59c9',
                                'ff02::2',
                                'ff02::1',
                                'ff02::5',
                                'ff02::6'],
                'ipv6_link_local': 'fe80::f816:3eff:fe8b:59c9',
                'ipv6_mtu': '1514',
                'ipv6_mtu_available': '1500',
                'nd_adv_duration': '160-240',
                'nd_adv_retrans_int': '0',
                'nd_cache_limit': '1000000000',
                'nd_dad': 'enabled',
                'nd_reachable_time': '0',
                'nd_router_adv': '1800',
                'stateless_autoconfig': True,
                'table_id': '0xe0800001'},
            'ipv6_enabled': True,
            'oper_status': 'up',
            'vrf': 'VRF1',
            'vrf_id': '0x60000001'},
        'Loopback0': {
            'enabled': True,
            'int_status': 'up',
            'ipv6': {
                '2001:2:2::2/128': {
                    'ipv6': '2001:2:2::2',
                    'ipv6_prefix_length': '128',
                    'ipv6_subnet': '2001:2:2::2'},
                'complete_glean_adj': '0',
                'complete_protocol_adj': '0',
                'dad_attempts': '0',
                'dropped_glean_req': '0',
                'dropped_protocol_req': '0',
                'icmp_redirects': 'disabled',
                'incomplete_glean_adj': '0',
                'incomplete_protocol_adj': '0',
                'ipv6_groups': ['ff02::1:ff00:2',
                                'ff02::1:ffbd:853e',
                                'ff02::2',
                                'ff02::1'],
                'ipv6_link_local': 'fe80::6983:ecff:febd:853e',
                'ipv6_mtu': '1500',
                'ipv6_mtu_available': '1500',
                'nd_adv_retrans_int': '0',
                'nd_cache_limit': '0',
                'nd_dad': 'disabled',
                'nd_reachable_time': '0',
                'stateless_autoconfig': True,
                'table_id': '0xe0800000'},
            'ipv6_enabled': True,
            'oper_status': 'up',
            'vrf': 'default',
            'vrf_id': '0x60000000'},
        'Loopback1': {
            'enabled': True,
            'int_status': 'up',
            'ipv6': {
                '2001:22:22::22/128': {
                    'ipv6': '2001:22:22::22',
                    'ipv6_prefix_length': '128',
                    'ipv6_subnet': '2001:22:22::22'},
                'complete_glean_adj': '0',
                'complete_protocol_adj': '0',
                'dad_attempts': '0',
                'dropped_glean_req': '0',
                'dropped_protocol_req': '0',
                'icmp_redirects': 'disabled',
                'incomplete_glean_adj': '0',
                'incomplete_protocol_adj': '0',
                'ipv6_groups': ['ff02::1:ff00:22',
                                'ff02::1:ffbd:853e',
                                'ff02::2',
                                'ff02::1'],
                'ipv6_link_local': 'fe80::6983:ecff:febd:853e',
                'ipv6_mtu': '1500',
                'ipv6_mtu_available': '1500',
                'nd_adv_retrans_int': '0',
                'nd_cache_limit': '0',
                'nd_dad': 'disabled',
                'nd_reachable_time': '0',
                'stateless_autoconfig': True,
                'table_id': '0xe0800000'},
            'ipv6_enabled': True,
            'oper_status': 'up',
            'vrf': 'default',
            'vrf_id': '0x60000000'},
        'MgmtEth0/RP0/CPU0/0': {
            'enabled': False,
            'int_status': 'shutdown',
            'ipv6_enabled': False,
            'oper_status': 'down',
            'vrf': 'default',
            'vrf_id': '0x60000000'}}

    golden_output1 = {'execute.return_value': '''
            RP/0/RP0/CPU0:xr9kv-2#show ipv6 vrf all interface 
            Thu Apr 26 13:10:00.784 UTC
            Loopback0 is Up, ipv6 protocol is Up, Vrfid is default (0x60000000)
                IPv6 is enabled, link-local address is fe80::6983:ecff:febd:853e 
                Global unicast address(es):
                  2001:2:2::2, subnet is 2001:2:2::2/128 
                Joined group address(es): ff02::1:ff00:2 ff02::1:ffbd:853e ff02::2
                    ff02::1
                MTU is 1500 (1500 is available to IPv6)
                ICMP redirects are disabled
                ICMP unreachables are always on
                ND DAD is disabled, number of DAD attempts 0
                ND reachable time is 0 milliseconds
                ND cache entry limit is 0
                ND advertised retransmit interval is 0 milliseconds
                Hosts use stateless autoconfig for addresses.
                Outgoing access list is not set
                Inbound  common access list is not set, access list is not set
                Table Id is 0xe0800000
                Complete protocol adjacency: 0
                Complete glean adjacency: 0
                Incomplete protocol adjacency: 0
                Incomplete glean adjacency: 0
                Dropped protocol request: 0
                Dropped glean request: 0
            Loopback1 is Up, ipv6 protocol is Up, Vrfid is default (0x60000000)
                IPv6 is enabled, link-local address is fe80::6983:ecff:febd:853e 
                Global unicast address(es):
                  2001:22:22::22, subnet is 2001:22:22::22/128 
                Joined group address(es): ff02::1:ff00:22 ff02::1:ffbd:853e ff02::2
                    ff02::1
                MTU is 1500 (1500 is available to IPv6)
                ICMP redirects are disabled
                ICMP unreachables are always on
                ND DAD is disabled, number of DAD attempts 0
                ND reachable time is 0 milliseconds
                ND cache entry limit is 0
                ND advertised retransmit interval is 0 milliseconds
                Hosts use stateless autoconfig for addresses.
                Outgoing access list is not set
                Inbound  common access list is not set, access list is not set
                Table Id is 0xe0800000
                Complete protocol adjacency: 0
                Complete glean adjacency: 0
                Incomplete protocol adjacency: 0
                Incomplete glean adjacency: 0
                Dropped protocol request: 0
                Dropped glean request: 0
            MgmtEth0/RP0/CPU0/0 is Shutdown, ipv6 protocol is Down, Vrfid is default (0x60000000)
                IPv6 is disabled, link-local address unassigned
                No global unicast address is configured
            GigabitEthernet0/0/0/0 is Up, ipv6 protocol is Up, Vrfid is default (0x60000000)
                IPv6 is enabled, link-local address is fe80::f816:3eff:feca:3efd 
                Global unicast address(es):
                    2001:db8:8548:1::2, subnet is 2001:db8:8548:1::/64 
                Joined group address(es): ff02::1:ff00:2 ff02::1:ffca:3efd ff02::2
                    ff02::1 ff02::5 ff02::6
                MTU is 1514 (1500 is available to IPv6)
                ICMP redirects are disabled
                ICMP unreachables are enabled
                ND DAD is enabled, number of DAD attempts 1
                ND reachable time is 0 milliseconds
                ND cache entry limit is 1000000000
                ND advertised retransmit interval is 0 milliseconds
                Hosts use stateless autoconfig for addresses.
                Outgoing access list is not set
                Inbound  common access list is not set, access list is not set
                Table Id is 0xe0800000
                Complete protocol adjacency: 1
                Complete glean adjacency: 1
                Incomplete protocol adjacency: 0
                Incomplete glean adjacency: 0
                Dropped protocol request: 0
                Dropped glean request: 0
            GigabitEthernet0/0/0/1 is Up, ipv6 protocol is Up, Vrfid is VRF1 (0x60000001)
                IPv6 is enabled, link-local address is fe80::f816:3eff:fe20:fa5b 
                Global unicast address(es):
                  2001:db8:888c:1::2, subnet is 2001:db8:888c:1::/64 
                Joined group address(es): ff02::1:ff00:2 ff02::1:ff20:fa5b ff02::2
                    ff02::1 ff02::5 ff02::6
                MTU is 1514 (1500 is available to IPv6)
                ICMP redirects are disabled
                ICMP unreachables are enabled
                ND DAD is enabled, number of DAD attempts 1
                ND reachable time is 0 milliseconds
                ND cache entry limit is 1000000000
                ND advertised retransmit interval is 0 milliseconds
                ND router advertisements are sent every 160 to 240 seconds
                ND router advertisements live for 1800 seconds
                Hosts use stateless autoconfig for addresses.
                Outgoing access list is not set
                Inbound  common access list is not set, access list is not set
                Table Id is 0xe0800001
                Complete protocol adjacency: 0
                Complete glean adjacency: 2
                Incomplete protocol adjacency: 0
                Incomplete glean adjacency: 0
                Dropped protocol request: 0
                Dropped glean request: 0
            GigabitEthernet0/0/0/2 is Up, ipv6 protocol is Up, Vrfid is default (0x60000000)
                IPv6 is enabled, link-local address is fe80::f816:3eff:fe82:6320 
                Global unicast address(es):
                  2001:db8:c56d:4::2, subnet is 2001:db8:c56d:4::/64 
                Joined group address(es): ff02::1:ff00:2 ff02::1:ff82:6320 ff02::2
                    ff02::1 ff02::5 ff02::6
                MTU is 1514 (1500 is available to IPv6)
                ICMP redirects are disabled
                ICMP unreachables are enabled
                ND DAD is enabled, number of DAD attempts 1
                ND reachable time is 0 milliseconds
                ND cache entry limit is 1000000000
                ND advertised retransmit interval is 0 milliseconds
                ND router advertisements are sent every 160 to 240 seconds
                ND router advertisements live for 1800 seconds
                Hosts use stateless autoconfig for addresses.
                Outgoing access list is not set
                Inbound  common access list is not set, access list is not set
                Table Id is 0xe0800000
                Complete protocol adjacency: 1
                Complete glean adjacency: 1
                Incomplete protocol adjacency: 0
                Incomplete glean adjacency: 0
                Dropped protocol request: 0
                Dropped glean request: 0
            GigabitEthernet0/0/0/3 is Up, ipv6 protocol is Up, Vrfid is VRF1 (0x60000001)
                IPv6 is enabled, link-local address is fe80::f816:3eff:fe8b:59c9 
                Global unicast address(es):
                  2001:db8:c8d1:4::2, subnet is 2001:db8:c8d1:4::/64 
                Joined group address(es): ff02::1:ff00:2 ff02::1:ff8b:59c9 ff02::2
                    ff02::1 ff02::5 ff02::6
                MTU is 1514 (1500 is available to IPv6)
                ICMP redirects are disabled
                ICMP unreachables are enabled
                ND DAD is enabled, number of DAD attempts 1
                ND reachable time is 0 milliseconds
                ND cache entry limit is 1000000000
                ND advertised retransmit interval is 0 milliseconds
                ND router advertisements are sent every 160 to 240 seconds
                ND router advertisements live for 1800 seconds
                Hosts use stateless autoconfig for addresses.
                Outgoing access list is not set
                Inbound  common access list is not set, access list is not set
                Table Id is 0xe0800001
                Complete protocol adjacency: 1
                Complete glean adjacency: 1
                Incomplete protocol adjacency: 0
                Incomplete glean adjacency: 0
                Dropped protocol request: 0
                Dropped glean request: 0
        '''}
    golden_parsed_output_custom={'GigabitEthernet0/0/0/1': {'enabled': True,
                                   'int_status': 'up',
                                   'ipv6': {'2001:db8:1:5::1/64': {'ipv6': '2001:db8:1:5::1',
                                                                   'ipv6_prefix_length': '64',
                                                                   'ipv6_subnet': '2001:db8:1:5::'},
                                            'complete_glean_adj': '1',
                                            'complete_protocol_adj': '1',
                                            'dad_attempts': '1',
                                            'dropped_glean_req': '0',
                                            'dropped_protocol_req': '0',
                                            'icmp_redirects': 'disabled',
                                            'icmp_unreachables': 'enabled',
                                            'incomplete_glean_adj': '0',
                                            'incomplete_protocol_adj': '0',
                                            'ipv6_groups': ['ff02::1:ff00:1',
                                                            'ff02::1:ff78:ebe0',
                                                            'ff02::2',
                                                            'ff02::1'],
                                            'ipv6_link_local': 'fe80::5054:ff:fe78:ebe0',
                                            'ipv6_mtu': '1514',
                                            'ipv6_mtu_available': '1500',
                                            'nd_adv_duration': '160-240',
                                            'nd_adv_retrans_int': '0',
                                            'nd_cache_limit': '1000000000',
                                            'nd_dad': 'enabled',
                                            'nd_reachable_time': '0',
                                            'nd_router_adv': '1800',
                                            'stateless_autoconfig': True,
                                            'table_id': '0xe0800010'},
                                   'ipv6_enabled': True,
                                   'oper_status': 'up',
                                   'vrf': 'VRF1',
                                   'vrf_id': '0x60000001'},}
    golden_output_custom={'execute.return_value':
    '''
       GigabitEthernet0/0/0/1 is Up, ipv6 protocol is Up, Vrfid is VRF1 (0x60000001)
      IPv6 is enabled, link-local address is fe80::5054:ff:fe78:ebe0 
      Global unicast address(es):
        2001:db8:1:5::1, subnet is 2001:db8:1:5::/64 
      Joined group address(es): ff02::1:ff00:1 ff02::1:ff78:ebe0 ff02::2
          ff02::1
      MTU is 1514 (1500 is available to IPv6)
      ICMP redirects are disabled
      ICMP unreachables are enabled
      ND DAD is enabled, number of DAD attempts 1
      ND reachable time is 0 milliseconds
      ND cache entry limit is 1000000000
      ND advertised retransmit interval is 0 milliseconds
      ND router advertisements are sent every 160 to 240 seconds
      ND router advertisements live for 1800 seconds
      Hosts use stateless autoconfig for addresses.
      Outgoing access list is not set
      Inbound  common access list is not set, access list is not set
      Table Id is 0xe0800010
      Complete protocol adjacency: 1
      Complete glean adjacency: 1
      Incomplete protocol adjacency: 0
      Incomplete glean adjacency: 0
      Dropped protocol request: 0
      Dropped glean request: 0
      '''
                          }

    golden_output2 = {'execute.return_value': '''
        +++ XR1: executing command 'show ipv6 vrf all interface' +++d.parse()
        show ipv6 vrf all interface

        Fri Sep  6 09:50:49.892 EST
        BVI100 is Up, ipv6 protocol is Up, Vrfid is default (0x60000000)
        IPv6 is disabled, link-local address unassigned
        No global unicast address is configured
        BVI1401 is Down, ipv6 protocol is Down, Vrfid is default (0x60000000)
        IPv6 is enabled, link-local address is fe80::259:14ff:feff:1 [TENTATIVE]
        No global unicast address is configured
        Joined group address(es): ff02::2 ff02::1
        MTU is 1514 (1500 is available to IPv6)
        ICMP redirects are disabled
        ICMP unreachables are enabled
        ND DAD is enabled, number of DAD attempts 1
        ND reachable time is 0 milliseconds
        ND cache entry limit is 1000000000
        ND advertised retransmit interval is 0 milliseconds
        ND router advertisements are sent every 160 to 240 seconds
        ND router advertisements live for 1800 seconds
        Hosts use stateless autoconfig for addresses.
        Outgoing access list is not set
        Inbound  common access list is not set, access list is not set
        Table Id is 0xe0800000
        Complete protocol adjacency: 0
        Complete glean adjacency: 0
        Incomplete protocol adjacency: 0
        Incomplete glean adjacency: 0
        Dropped protocol request: 0
        Dropped glean request: 0
        BVI1403 is Down, ipv6 protocol is Down, Vrfid is default (0x60000000)
        IPv6 is enabled, link-local address is fe80::259:14ff:feff:304 [TENTATIVE]
        Global unicast address(es):
            2001:60:1403::1, subnet is 2001:60:1403::/64 [TENTATIVE]
        Joined group address(es): ff02::2 ff02::1
        MTU is 1514 (1500 is available to IPv6)
        ICMP redirects are disabled
        ICMP unreachables are enabled
        ND DAD is enabled, number of DAD attempts 1
        ND reachable time is 0 milliseconds
        ND cache entry limit is 1000000000
        ND advertised retransmit interval is 0 milliseconds
        ND router advertisements are sent every 160 to 240 seconds
        ND router advertisements live for 1800 seconds
        Hosts use stateless autoconfig for addresses.
        Outgoing access list is not set
        Inbound  common access list is not set, access list is not set
        Table Id is 0xe0800000
        Complete protocol adjacency: 0
        Complete glean adjacency: 0
        Incomplete protocol adjacency: 0
        Incomplete glean adjacency: 0
        Dropped protocol request: 0
        Dropped glean request: 0
        BVI1405 is Down, ipv6 protocol is Down, Vrfid is default (0x60000000)
        IPv6 is enabled, link-local address is fe80::259:14ff:feff:506 [TENTATIVE]
        Global unicast address(es):
            2001:59:1405::1, subnet is 2001:59:1405::/64 [TENTATIVE]
        Joined group address(es): ff02::2 ff02::1
        MTU is 1514 (1500 is available to IPv6)
        ICMP redirects are disabled
        ICMP unreachables are enabled
        ND DAD is enabled, number of DAD attempts 1
        ND reachable time is 0 milliseconds
        ND cache entry limit is 1000000000
        ND advertised retransmit interval is 0 milliseconds
        ND router advertisements are sent every 160 to 240 seconds
        ND router advertisements live for 1800 seconds
        Hosts use stateless autoconfig for addresses.
        Outgoing access list is not set
        Inbound  common access list is not set, access list is not set
        Table Id is 0xe0800000
        Complete protocol adjacency: 0
        Complete glean adjacency: 0
        Incomplete protocol adjacency: 0
        Incomplete glean adjacency: 0
        Dropped protocol request: 0
        Dropped glean request: 0
        BVI1407 is Down, ipv6 protocol is Down, Vrfid is default (0x60000000)
        IPv6 is enabled, link-local address is fe80::259:14ff:feff:708 [TENTATIVE]
        Global unicast address(es):
            2001:60:1407::1, subnet is 2001:60:1407::/64 [TENTATIVE]
        Joined group address(es): ff02::2 ff02::1
        MTU is 1514 (1500 is available to IPv6)
        ICMP redirects are disabled
        ICMP unreachables are enabled
        ND DAD is enabled, number of DAD attempts 1
        ND reachable time is 0 milliseconds
        ND cache entry limit is 1000000000
        ND advertised retransmit interval is 0 milliseconds
        ND router advertisements are sent every 160 to 240 seconds
        ND router advertisements live for 1800 seconds
        Hosts use stateless autoconfig for addresses.
        Outgoing access list is not set
        Inbound  common access list is not set, access list is not set
        Table Id is 0xe0800000
        Complete protocol adjacency: 0
        Complete glean adjacency: 0
        Incomplete protocol adjacency: 0
        Incomplete glean adjacency: 0
        Dropped protocol request: 0
        Dropped glean request: 0
        BVI1410 is Down, ipv6 protocol is Down, Vrfid is default (0x60000000)
        IPv6 is enabled, link-local address is fe80::259:14ff:feff:1011 [TENTATIVE]
        Global unicast address(es):
            2001:60:1410::1, subnet is 2001:60:1410::/64 [TENTATIVE]
        Joined group address(es): ff02::2 ff02::1
        MTU is 1514 (1500 is available to IPv6)
        ICMP redirects are disabled
        ICMP unreachables are enabled
        ND DAD is enabled, number of DAD attempts 1
        ND reachable time is 0 milliseconds
        ND cache entry limit is 1000000000
        ND advertised retransmit interval is 0 milliseconds
        ND router advertisements are sent every 160 to 240 seconds
        ND router advertisements live for 1800 seconds
        Hosts use stateless autoconfig for addresses.
        Outgoing access list is not set
        Inbound  common access list is not set, access list is not set
        Table Id is 0xe0800000
        Complete protocol adjacency: 0
        Complete glean adjacency: 0
        Incomplete protocol adjacency: 0
        Incomplete glean adjacency: 0
        Dropped protocol request: 0
        Dropped glean request: 0
        Bundle-Ether1 is Up, ipv6 protocol is Up, Vrfid is default (0x60000000)
        IPv6 is enabled, link-local address is fe80::2bc:60ff:fe38:a8dc 
        Global unicast address(es):
            2001:db8:79b7:fc34::10, subnet is 2001:db8:79b7:fc34::/64 
        Joined group address(es): ff02::1:ff00:10 ff02::1:ff38:a8dc ff02::2
            ff02::1
        MTU is 1514 (1500 is available to IPv6)
        ICMP redirects are disabled
        ICMP unreachables are enabled
        ND DAD is enabled, number of DAD attempts 1
        ND reachable time is 0 milliseconds
        ND cache entry limit is 1000000000
        ND advertised retransmit interval is 0 milliseconds
        ND router advertisements are sent every 160 to 240 seconds
        ND router advertisements live for 1800 seconds
        Hosts use stateless autoconfig for addresses.
        Outgoing access list is not set
        Inbound  common access list is not set, access list is not set
        Table Id is 0xe0800000
        Complete protocol adjacency: 0
        Complete glean adjacency: 0
        Incomplete protocol adjacency: 0
        Incomplete glean adjacency: 0
        Dropped protocol request: 0
        Dropped glean request: 0
        Bundle-Ether100 is Up, ipv6 protocol is Up, Vrfid is default (0x60000000)
        IPv6 is disabled, link-local address unassigned
        No global unicast address is configured
        Bundle-Ether1001 is Down, ipv6 protocol is Down, Vrfid is default (0x60000000)
        IPv6 is disabled, link-local address unassigned
        No global unicast address is configured
        Bundle-Ether100.12 is Up, ipv6 protocol is Up, Vrfid is default (0x60000000)
        IPv6 is disabled, link-local address unassigned
        No global unicast address is configured
        Bundle-Ether100.22 is Up, ipv6 protocol is Up, Vrfid is default (0x60000000)
        IPv6 is disabled, link-local address unassigned
        No global unicast address is configured
        Bundle-Ether100.32 is Up, ipv6 protocol is Up, Vrfid is default (0x60000000)
        IPv6 is disabled, link-local address unassigned
        No global unicast address is configured
        Bundle-Ether1001.100 is Down, ipv6 protocol is Down, Vrfid is default (0x60000000)
        IPv6 is disabled, link-local address unassigned
        No global unicast address is configured
        Bundle-Ether1001.1400 is Down, ipv6 protocol is Down, Vrfid is default (0x60000000)
        IPv6 is disabled, link-local address unassigned
        No global unicast address is configured
        Bundle-Ether1001.1402 is Down, ipv6 protocol is Down, Vrfid is default (0x60000000)
        IPv6 is disabled, link-local address unassigned
        No global unicast address is configured
        Bundle-Ether1001.1404 is Down, ipv6 protocol is Down, Vrfid is default (0x60000000)
        IPv6 is disabled, link-local address unassigned
        No global unicast address is configured
        Bundle-Ether1001.1406 is Down, ipv6 protocol is Down, Vrfid is default (0x60000000)
        IPv6 is disabled, link-local address unassigned
        No global unicast address is configured
        Bundle-Ether1001.1410 is Down, ipv6 protocol is Down, Vrfid is default (0x60000000)
        IPv6 is disabled, link-local address unassigned
        No global unicast address is configured
        Loopback0 is Up, ipv6 protocol is Up, Vrfid is default (0x60000000)
        IPv6 is enabled, link-local address is fe80::d121:1bff:fea4:a9f7 
        Global unicast address(es):
            2001:db8:100::10, subnet is 2001:db8:100::10/128 
        Joined group address(es): ff02::1:ff00:10 ff02::1:ffa4:a9f7 ff02::2
            ff02::1
        MTU is 1500 (1500 is available to IPv6)
        ICMP redirects are disabled
        ICMP unreachables are always on
        ND DAD is disabled, number of DAD attempts 0
        ND reachable time is 0 milliseconds
        ND cache entry limit is 0
        ND advertised retransmit interval is 0 milliseconds
        Hosts use stateless autoconfig for addresses.
        Outgoing access list is not set
        Inbound  common access list is not set, access list is not set
        Table Id is 0xe0800000
        Complete protocol adjacency: 0
        Complete glean adjacency: 0
        Incomplete protocol adjacency: 0
        Incomplete glean adjacency: 0
        Dropped protocol request: 0
        Dropped glean request: 0
        MgmtEth0/RP0/CPU0/0 is Up, ipv6 protocol is Up, Vrfid is Mgmt (0x60000001)
        IPv6 is disabled, link-local address unassigned
        No global unicast address is configured
        TenGigE0/0/0/0 is Up, ipv6 protocol is Up, Vrfid is default (0x60000000)
        IPv6 is enabled, link-local address is fe80::2bc:60ff:fe38:a800 
        Global unicast address(es):
            2001:db8:ce35:fc34::10, subnet is 2001:db8:ce35:fc34::/64 
        Joined group address(es): ff02::1:ff00:10 ff02::1:ff38:a800 ff02::2
            ff02::1
        MTU is 1514 (1500 is available to IPv6)
        ICMP redirects are disabled
        ICMP unreachables are enabled
        ND DAD is enabled, number of DAD attempts 1
        ND reachable time is 0 milliseconds
        ND cache entry limit is 1000000000
        ND advertised retransmit interval is 0 milliseconds
        ND router advertisements are sent every 160 to 240 seconds
        ND router advertisements live for 1800 seconds
        Hosts use stateless autoconfig for addresses.
        Outgoing access list is not set
        Inbound  common access list is not set, access list is not set
        Table Id is 0xe0800000
        Complete protocol adjacency: 0
        Complete glean adjacency: 0
        Incomplete protocol adjacency: 0
        Incomplete glean adjacency: 0
        Dropped protocol request: 0
        Dropped glean request: 0
        TenGigE0/0/0/1 is Up, ipv6 protocol is Up, Vrfid is default (0x60000000)
        IPv6 is disabled, link-local address unassigned
        No global unicast address is configured
        TenGigE0/0/0/2 is Shutdown, ipv6 protocol is Down, Vrfid is default (0x60000000)
        IPv6 is disabled, link-local address unassigned
        No global unicast address is configured
        TenGigE0/0/0/3 is Shutdown, ipv6 protocol is Down, Vrfid is default (0x60000000)
        IPv6 is disabled, link-local address unassigned
        No global unicast address is configured
        TenGigE0/0/0/4 is Shutdown, ipv6 protocol is Down, Vrfid is default (0x60000000)
        IPv6 is disabled, link-local address unassigned
        No global unicast address is configured
        TenGigE0/0/0/5 is Shutdown, ipv6 protocol is Down, Vrfid is default (0x60000000)
        IPv6 is disabled, link-local address unassigned
        No global unicast address is configured
        TenGigE0/0/0/6 is Shutdown, ipv6 protocol is Down, Vrfid is default (0x60000000)
        IPv6 is disabled, link-local address unassigned
        No global unicast address is configured
        TenGigE0/0/0/7 is Shutdown, ipv6 protocol is Down, Vrfid is default (0x60000000)
        IPv6 is disabled, link-local address unassigned
        No global unicast address is configured
        TenGigE0/0/0/8 is Shutdown, ipv6 protocol is Down, Vrfid is default (0x60000000)
        IPv6 is disabled, link-local address unassigned
        No global unicast address is configured
        TenGigE0/0/0/9 is Shutdown, ipv6 protocol is Down, Vrfid is default (0x60000000)
        IPv6 is disabled, link-local address unassigned
        No global unicast address is configured
        TenGigE0/0/0/10 is Shutdown, ipv6 protocol is Down, Vrfid is default (0x60000000)
        IPv6 is disabled, link-local address unassigned
        No global unicast address is configured
        TenGigE0/0/0/11 is Shutdown, ipv6 protocol is Down, Vrfid is default (0x60000000)
        IPv6 is disabled, link-local address unassigned
        No global unicast address is configured
        TenGigE0/0/0/12 is Shutdown, ipv6 protocol is Down, Vrfid is default (0x60000000)
        IPv6 is disabled, link-local address unassigned
        No global unicast address is configured
        TenGigE0/0/0/13 is Shutdown, ipv6 protocol is Down, Vrfid is default (0x60000000)
        IPv6 is disabled, link-local address unassigned
        No global unicast address is configured
        TenGigE0/0/0/14 is Shutdown, ipv6 protocol is Down, Vrfid is default (0x60000000)
        IPv6 is disabled, link-local address unassigned
        No global unicast address is configured
        TenGigE0/0/0/15 is Shutdown, ipv6 protocol is Down, Vrfid is default (0x60000000)
        IPv6 is disabled, link-local address unassigned
        No global unicast address is configured
        TenGigE0/0/0/16 is Shutdown, ipv6 protocol is Down, Vrfid is default (0x60000000)
        IPv6 is disabled, link-local address unassigned
        No global unicast address is configured
        TenGigE0/0/0/17 is Shutdown, ipv6 protocol is Down, Vrfid is default (0x60000000)
        IPv6 is disabled, link-local address unassigned
        No global unicast address is configured
        TenGigE0/0/0/18 is Shutdown, ipv6 protocol is Down, Vrfid is default (0x60000000)
        IPv6 is disabled, link-local address unassigned
        No global unicast address is configured
        TenGigE0/0/0/19 is Shutdown, ipv6 protocol is Down, Vrfid is default (0x60000000)
        IPv6 is disabled, link-local address unassigned
        No global unicast address is configured
        TenGigE0/0/0/20 is Shutdown, ipv6 protocol is Down, Vrfid is default (0x60000000)
        IPv6 is disabled, link-local address unassigned
        No global unicast address is configured
        TenGigE0/0/0/21 is Shutdown, ipv6 protocol is Down, Vrfid is default (0x60000000)
        IPv6 is disabled, link-local address unassigned
        No global unicast address is configured
        TenGigE0/0/0/22 is Shutdown, ipv6 protocol is Down, Vrfid is default (0x60000000)
        IPv6 is disabled, link-local address unassigned
        No global unicast address is configured
        TenGigE0/0/0/23 is Shutdown, ipv6 protocol is Down, Vrfid is default (0x60000000)
        IPv6 is disabled, link-local address unassigned
        No global unicast address is configured
        TwentyFiveGigE0/0/0/24 is Shutdown, ipv6 protocol is Down, Vrfid is default (0x60000000)
        IPv6 is disabled, link-local address unassigned
        No global unicast address is configured
        TwentyFiveGigE0/0/0/25 is Shutdown, ipv6 protocol is Down, Vrfid is default (0x60000000)
        IPv6 is disabled, link-local address unassigned
        No global unicast address is configured
        TwentyFiveGigE0/0/0/26 is Shutdown, ipv6 protocol is Down, Vrfid is default (0x60000000)
        IPv6 is disabled, link-local address unassigned
        No global unicast address is configured
        TwentyFiveGigE0/0/0/27 is Shutdown, ipv6 protocol is Down, Vrfid is default (0x60000000)
        IPv6 is disabled, link-local address unassigned
        No global unicast address is configured
        TwentyFiveGigE0/0/0/28 is Shutdown, ipv6 protocol is Down, Vrfid is default (0x60000000)
        IPv6 is disabled, link-local address unassigned
        No global unicast address is configured
        TwentyFiveGigE0/0/0/29 is Shutdown, ipv6 protocol is Down, Vrfid is default (0x60000000)
        IPv6 is disabled, link-local address unassigned
        No global unicast address is configured
        TwentyFiveGigE0/0/0/30 is Shutdown, ipv6 protocol is Down, Vrfid is default (0x60000000)
        IPv6 is disabled, link-local address unassigned
        No global unicast address is configured
        TwentyFiveGigE0/0/0/31 is Shutdown, ipv6 protocol is Down, Vrfid is default (0x60000000)
        IPv6 is disabled, link-local address unassigned
        No global unicast address is configured
        TwentyFiveGigE0/0/0/32 is Shutdown, ipv6 protocol is Down, Vrfid is default (0x60000000)
        IPv6 is disabled, link-local address unassigned
        No global unicast address is configured
        TwentyFiveGigE0/0/0/33 is Shutdown, ipv6 protocol is Down, Vrfid is default (0x60000000)
        IPv6 is disabled, link-local address unassigned
        No global unicast address is configured
        TwentyFiveGigE0/0/0/34 is Shutdown, ipv6 protocol is Down, Vrfid is default (0x60000000)
        IPv6 is disabled, link-local address unassigned
        No global unicast address is configured
        TwentyFiveGigE0/0/0/35 is Shutdown, ipv6 protocol is Down, Vrfid is default (0x60000000)
        IPv6 is disabled, link-local address unassigned
        No global unicast address is configured
        TwentyFiveGigE0/0/0/36 is Shutdown, ipv6 protocol is Down, Vrfid is default (0x60000000)
        IPv6 is disabled, link-local address unassigned
        No global unicast address is configured
        TwentyFiveGigE0/0/0/37 is Shutdown, ipv6 protocol is Down, Vrfid is default (0x60000000)
        IPv6 is disabled, link-local address unassigned
        No global unicast address is configured
        TwentyFiveGigE0/0/0/38 is Shutdown, ipv6 protocol is Down, Vrfid is default (0x60000000)
        IPv6 is disabled, link-local address unassigned
        No global unicast address is configured
        TwentyFiveGigE0/0/0/39 is Shutdown, ipv6 protocol is Down, Vrfid is default (0x60000000)
        IPv6 is disabled, link-local address unassigned
        No global unicast address is configured
        HundredGigE0/0/1/0 is Shutdown, ipv6 protocol is Down, Vrfid is default (0x60000000)
        IPv6 is disabled, link-local address unassigned
        No global unicast address is configured
        HundredGigE0/0/1/1 is Shutdown, ipv6 protocol is Down, Vrfid is default (0x60000000)
        IPv6 is disabled, link-local address unassigned
        No global unicast address is configured
        HundredGigE0/0/1/2/0 is Up, ipv6 protocol is Up, Vrfid is default (0x60000000)
        IPv6 is disabled, link-local address unassigned
        No global unicast address is configured
        RP/0/RP0/CPU0:XR1#

            '''}

    golden_parsed_output2 = {
            'BVI100': {
                'ipv6_enabled': True,
                'int_status': 'up',
                'oper_status': 'up',
                'vrf': 'default',
                'vrf_id': '0x60000000',
                'enabled': False,
            },
            'BVI1401': {
                'ipv6_enabled': False,
                'int_status': 'down',
                'oper_status': 'down',
                'vrf': 'default',
                'vrf_id': '0x60000000',
                'enabled': True,
                'ipv6': {
                    'ipv6_groups': ['ff02::2', 'ff02::1'],
                    'ipv6_mtu': '1514',
                    'ipv6_mtu_available': '1500',
                    'icmp_redirects': 'disabled',
                    'icmp_unreachables': 'enabled',
                    'nd_dad': 'enabled',
                    'dad_attempts': '1',
                    'nd_reachable_time': '0',
                    'nd_cache_limit': '1000000000',
                    'nd_adv_retrans_int': '0',
                    'nd_adv_duration': '160-240',
                    'nd_router_adv': '1800',
                    'stateless_autoconfig': True,
                    'table_id': '0xe0800000',
                    'complete_protocol_adj': '0',
                    'complete_glean_adj': '0',
                    'incomplete_protocol_adj': '0',
                    'incomplete_glean_adj': '0',
                    'dropped_protocol_req': '0',
                    'dropped_glean_req': '0',
                },
            },
            'BVI1403': {
                'ipv6_enabled': False,
                'int_status': 'down',
                'oper_status': 'down',
                'vrf': 'default',
                'vrf_id': '0x60000000',
                'enabled': True,
                'ipv6': {
                    '2001:60:1403::1/64': {
                        'ipv6': '2001:60:1403::1',
                        'ipv6_prefix_length': '64',
                        'ipv6_status': 'tentative',
                        'ipv6_subnet': '2001:60:1403::',
                    },
                    'ipv6_link_local_state': 'tentative',
                    'ipv6_link_local': 'fe80::259:14ff:feff:304',
                    'ipv6_groups': ['ff02::2', 'ff02::1'],
                    'ipv6_mtu': '1514',
                    'ipv6_mtu_available': '1500',
                    'icmp_redirects': 'disabled',
                    'icmp_unreachables': 'enabled',
                    'nd_dad': 'enabled',
                    'dad_attempts': '1',
                    'nd_reachable_time': '0',
                    'nd_cache_limit': '1000000000',
                    'nd_adv_retrans_int': '0',
                    'nd_adv_duration': '160-240',
                    'nd_router_adv': '1800',
                    'stateless_autoconfig': True,
                    'table_id': '0xe0800000',
                    'complete_protocol_adj': '0',
                    'complete_glean_adj': '0',
                    'incomplete_protocol_adj': '0',
                    'incomplete_glean_adj': '0',
                    'dropped_protocol_req': '0',
                    'dropped_glean_req': '0',
                },
            },
            'BVI1405': {
                'ipv6_enabled': False,
                'int_status': 'down',
                'oper_status': 'down',
                'vrf': 'default',
                'vrf_id': '0x60000000',
                'enabled': True,
                'ipv6': {
                    '2001:59:1405::1/64': {
                        'ipv6': '2001:59:1405::1',
                        'ipv6_prefix_length': '64',
                        'ipv6_status': 'tentative',
                        'ipv6_subnet': '2001:59:1405::',
                    },
                    'ipv6_link_local_state': 'tentative',
                    'ipv6_link_local': 'fe80::259:14ff:feff:506',
                    'ipv6_groups': ['ff02::2', 'ff02::1'],
                    'ipv6_mtu': '1514',
                    'ipv6_mtu_available': '1500',
                    'icmp_redirects': 'disabled',
                    'icmp_unreachables': 'enabled',
                    'nd_dad': 'enabled',
                    'dad_attempts': '1',
                    'nd_reachable_time': '0',
                    'nd_cache_limit': '1000000000',
                    'nd_adv_retrans_int': '0',
                    'nd_adv_duration': '160-240',
                    'nd_router_adv': '1800',
                    'stateless_autoconfig': True,
                    'table_id': '0xe0800000',
                    'complete_protocol_adj': '0',
                    'complete_glean_adj': '0',
                    'incomplete_protocol_adj': '0',
                    'incomplete_glean_adj': '0',
                    'dropped_protocol_req': '0',
                    'dropped_glean_req': '0',
                },
            },
            'BVI1407': {
                'ipv6_enabled': False,
                'int_status': 'down',
                'oper_status': 'down',
                'vrf': 'default',
                'vrf_id': '0x60000000',
                'enabled': True,
                'ipv6': {
                    '2001:60:1407::1/64': {
                        'ipv6': '2001:60:1407::1',
                        'ipv6_prefix_length': '64',
                        'ipv6_status': 'tentative',
                        'ipv6_subnet': '2001:60:1407::',
                    },
                    'ipv6_link_local_state': 'tentative',
                    'ipv6_link_local': 'fe80::259:14ff:feff:708',
                    'ipv6_groups': ['ff02::2', 'ff02::1'],
                    'ipv6_mtu': '1514',
                    'ipv6_mtu_available': '1500',
                    'icmp_redirects': 'disabled',
                    'icmp_unreachables': 'enabled',
                    'nd_dad': 'enabled',
                    'dad_attempts': '1',
                    'nd_reachable_time': '0',
                    'nd_cache_limit': '1000000000',
                    'nd_adv_retrans_int': '0',
                    'nd_adv_duration': '160-240',
                    'nd_router_adv': '1800',
                    'stateless_autoconfig': True,
                    'table_id': '0xe0800000',
                    'complete_protocol_adj': '0',
                    'complete_glean_adj': '0',
                    'incomplete_protocol_adj': '0',
                    'incomplete_glean_adj': '0',
                    'dropped_protocol_req': '0',
                    'dropped_glean_req': '0',
                },
            },
            'BVI1410': {
                'ipv6_enabled': False,
                'int_status': 'down',
                'oper_status': 'down',
                'vrf': 'default',
                'vrf_id': '0x60000000',
                'enabled': True,
                'ipv6': {
                    '2001:60:1410::1/64': {
                        'ipv6': '2001:60:1410::1',
                        'ipv6_prefix_length': '64',
                        'ipv6_status': 'tentative',
                        'ipv6_subnet': '2001:60:1410::',
                    },
                    'ipv6_link_local_state': 'tentative',
                    'ipv6_link_local': 'fe80::259:14ff:feff:1011',
                    'ipv6_groups': ['ff02::2', 'ff02::1'],
                    'ipv6_mtu': '1514',
                    'ipv6_mtu_available': '1500',
                    'icmp_redirects': 'disabled',
                    'icmp_unreachables': 'enabled',
                    'nd_dad': 'enabled',
                    'dad_attempts': '1',
                    'nd_reachable_time': '0',
                    'nd_cache_limit': '1000000000',
                    'nd_adv_retrans_int': '0',
                    'nd_adv_duration': '160-240',
                    'nd_router_adv': '1800',
                    'stateless_autoconfig': True,
                    'table_id': '0xe0800000',
                    'complete_protocol_adj': '0',
                    'complete_glean_adj': '0',
                    'incomplete_protocol_adj': '0',
                    'incomplete_glean_adj': '0',
                    'dropped_protocol_req': '0',
                    'dropped_glean_req': '0',
                },
            },
            'Bundle-Ether1': {
                'ipv6_enabled': True,
                'int_status': 'up',
                'oper_status': 'up',
                'vrf': 'default',
                'vrf_id': '0x60000000',
                'enabled': True,
                'ipv6': {
                    '2001:db8:79b7:fc34::10/64': {
                        'ipv6': '2001:db8:79b7:fc34::10',
                        'ipv6_prefix_length': '64',
                        'ipv6_subnet': '2001:db8:79b7:fc34::',
                    },
                    'ipv6_link_local': 'fe80::2bc:60ff:fe38:a8dc',
                    'ipv6_groups': ['ff02::1:ff00:10', 'ff02::1:ff38:a8dc', 'ff02::2', 'ff02::1'],
                    'ipv6_mtu': '1514',
                    'ipv6_mtu_available': '1500',
                    'icmp_redirects': 'disabled',
                    'icmp_unreachables': 'enabled',
                    'nd_dad': 'enabled',
                    'dad_attempts': '1',
                    'nd_reachable_time': '0',
                    'nd_cache_limit': '1000000000',
                    'nd_adv_retrans_int': '0',
                    'nd_adv_duration': '160-240',
                    'nd_router_adv': '1800',
                    'stateless_autoconfig': True,
                    'table_id': '0xe0800000',
                    'complete_protocol_adj': '0',
                    'complete_glean_adj': '0',
                    'incomplete_protocol_adj': '0',
                    'incomplete_glean_adj': '0',
                    'dropped_protocol_req': '0',
                    'dropped_glean_req': '0',
                },
            },
            'Bundle-Ether100': {
                'ipv6_enabled': True,
                'int_status': 'up',
                'oper_status': 'up',
                'vrf': 'default',
                'vrf_id': '0x60000000',
                'enabled': False,
            },
            'Bundle-Ether1001': {
                'ipv6_enabled': False,
                'int_status': 'down',
                'oper_status': 'down',
                'vrf': 'default',
                'vrf_id': '0x60000000',
                'enabled': False,
            },
            'Bundle-Ether100.12': {
                'ipv6_enabled': True,
                'int_status': 'up',
                'oper_status': 'up',
                'vrf': 'default',
                'vrf_id': '0x60000000',
                'enabled': False,
            },
            'Bundle-Ether100.22': {
                'ipv6_enabled': True,
                'int_status': 'up',
                'oper_status': 'up',
                'vrf': 'default',
                'vrf_id': '0x60000000',
                'enabled': False,
            },
            'Bundle-Ether100.32': {
                'ipv6_enabled': True,
                'int_status': 'up',
                'oper_status': 'up',
                'vrf': 'default',
                'vrf_id': '0x60000000',
                'enabled': False,
            },
            'Bundle-Ether1001.100': {
                'ipv6_enabled': False,
                'int_status': 'down',
                'oper_status': 'down',
                'vrf': 'default',
                'vrf_id': '0x60000000',
                'enabled': False,
            },
            'Bundle-Ether1001.1400': {
                'ipv6_enabled': False,
                'int_status': 'down',
                'oper_status': 'down',
                'vrf': 'default',
                'vrf_id': '0x60000000',
                'enabled': False,
            },
            'Bundle-Ether1001.1402': {
                'ipv6_enabled': False,
                'int_status': 'down',
                'oper_status': 'down',
                'vrf': 'default',
                'vrf_id': '0x60000000',
                'enabled': False,
            },
            'Bundle-Ether1001.1404': {
                'ipv6_enabled': False,
                'int_status': 'down',
                'oper_status': 'down',
                'vrf': 'default',
                'vrf_id': '0x60000000',
                'enabled': False,
            },
            'Bundle-Ether1001.1406': {
                'ipv6_enabled': False,
                'int_status': 'down',
                'oper_status': 'down',
                'vrf': 'default',
                'vrf_id': '0x60000000',
                'enabled': False,
            },
            'Bundle-Ether1001.1410': {
                'ipv6_enabled': False,
                'int_status': 'down',
                'oper_status': 'down',
                'vrf': 'default',
                'vrf_id': '0x60000000',
                'enabled': False,
            },
            'Loopback0': {
                'ipv6_enabled': True,
                'int_status': 'up',
                'oper_status': 'up',
                'vrf': 'default',
                'vrf_id': '0x60000000',
                'enabled': True,
                'ipv6': {
                    '2001:db8:100::10/128': {
                        'ipv6': '2001:db8:100::10',
                        'ipv6_prefix_length': '128',
                        'ipv6_subnet': '2001:db8:100::10',
                    },
                    'ipv6_link_local': 'fe80::d121:1bff:fea4:a9f7',
                    'ipv6_groups': ['ff02::1:ff00:10', 'ff02::1:ffa4:a9f7', 'ff02::2', 'ff02::1'],
                    'ipv6_mtu': '1500',
                    'ipv6_mtu_available': '1500',
                    'icmp_redirects': 'disabled',
                    'nd_dad': 'disabled',
                    'dad_attempts': '0',
                    'nd_reachable_time': '0',
                    'nd_cache_limit': '0',
                    'nd_adv_retrans_int': '0',
                    'stateless_autoconfig': True,
                    'table_id': '0xe0800000',
                    'complete_protocol_adj': '0',
                    'complete_glean_adj': '0',
                    'incomplete_protocol_adj': '0',
                    'incomplete_glean_adj': '0',
                    'dropped_protocol_req': '0',
                    'dropped_glean_req': '0',
                },
            },
            'MgmtEth0/RP0/CPU0/0': {
                'ipv6_enabled': True,
                'int_status': 'up',
                'oper_status': 'up',
                'vrf': 'Mgmt',
                'vrf_id': '0x60000001',
                'enabled': False,
            },
            'TenGigE0/0/0/0': {
                'ipv6_enabled': True,
                'int_status': 'up',
                'oper_status': 'up',
                'vrf': 'default',
                'vrf_id': '0x60000000',
                'enabled': True,
                'ipv6': {
                    '2001:db8:ce35:fc34::10/64': {
                        'ipv6': '2001:db8:ce35:fc34::10',
                        'ipv6_prefix_length': '64',
                        'ipv6_subnet': '2001:db8:ce35:fc34::',
                    },
                    'ipv6_link_local': 'fe80::2bc:60ff:fe38:a800',
                    'ipv6_groups': ['ff02::1:ff00:10', 'ff02::1:ff38:a800', 'ff02::2', 'ff02::1'],
                    'ipv6_mtu': '1514',
                    'ipv6_mtu_available': '1500',
                    'icmp_redirects': 'disabled',
                    'icmp_unreachables': 'enabled',
                    'nd_dad': 'enabled',
                    'dad_attempts': '1',
                    'nd_reachable_time': '0',
                    'nd_cache_limit': '1000000000',
                    'nd_adv_retrans_int': '0',
                    'nd_adv_duration': '160-240',
                    'nd_router_adv': '1800',
                    'stateless_autoconfig': True,
                    'table_id': '0xe0800000',
                    'complete_protocol_adj': '0',
                    'complete_glean_adj': '0',
                    'incomplete_protocol_adj': '0',
                    'incomplete_glean_adj': '0',
                    'dropped_protocol_req': '0',
                    'dropped_glean_req': '0',
                },
            },
            'TenGigE0/0/0/1': {
                'ipv6_enabled': True,
                'int_status': 'up',
                'oper_status': 'up',
                'vrf': 'default',
                'vrf_id': '0x60000000',
                'enabled': False,
            },
            'TenGigE0/0/0/2': {
                'ipv6_enabled': False,
                'int_status': 'shutdown',
                'oper_status': 'down',
                'vrf': 'default',
                'vrf_id': '0x60000000',
                'enabled': False,
            },
            'TenGigE0/0/0/3': {
                'ipv6_enabled': False,
                'int_status': 'shutdown',
                'oper_status': 'down',
                'vrf': 'default',
                'vrf_id': '0x60000000',
                'enabled': False,
            },
            'TenGigE0/0/0/4': {
                'ipv6_enabled': False,
                'int_status': 'shutdown',
                'oper_status': 'down',
                'vrf': 'default',
                'vrf_id': '0x60000000',
                'enabled': False,
            },
            'TenGigE0/0/0/5': {
                'ipv6_enabled': False,
                'int_status': 'shutdown',
                'oper_status': 'down',
                'vrf': 'default',
                'vrf_id': '0x60000000',
                'enabled': False,
            },
            'TenGigE0/0/0/6': {
                'ipv6_enabled': False,
                'int_status': 'shutdown',
                'oper_status': 'down',
                'vrf': 'default',
                'vrf_id': '0x60000000',
                'enabled': False,
            },
            'TenGigE0/0/0/7': {
                'ipv6_enabled': False,
                'int_status': 'shutdown',
                'oper_status': 'down',
                'vrf': 'default',
                'vrf_id': '0x60000000',
                'enabled': False,
            },
            'TenGigE0/0/0/8': {
                'ipv6_enabled': False,
                'int_status': 'shutdown',
                'oper_status': 'down',
                'vrf': 'default',
                'vrf_id': '0x60000000',
                'enabled': False,
            },
            'TenGigE0/0/0/9': {
                'ipv6_enabled': False,
                'int_status': 'shutdown',
                'oper_status': 'down',
                'vrf': 'default',
                'vrf_id': '0x60000000',
                'enabled': False,
            },
            'TenGigE0/0/0/10': {
                'ipv6_enabled': False,
                'int_status': 'shutdown',
                'oper_status': 'down',
                'vrf': 'default',
                'vrf_id': '0x60000000',
                'enabled': False,
            },
            'TenGigE0/0/0/11': {
                'ipv6_enabled': False,
                'int_status': 'shutdown',
                'oper_status': 'down',
                'vrf': 'default',
                'vrf_id': '0x60000000',
                'enabled': False,
            },
            'TenGigE0/0/0/12': {
                'ipv6_enabled': False,
                'int_status': 'shutdown',
                'oper_status': 'down',
                'vrf': 'default',
                'vrf_id': '0x60000000',
                'enabled': False,
            },
            'TenGigE0/0/0/13': {
                'ipv6_enabled': False,
                'int_status': 'shutdown',
                'oper_status': 'down',
                'vrf': 'default',
                'vrf_id': '0x60000000',
                'enabled': False,
            },
            'TenGigE0/0/0/14': {
                'ipv6_enabled': False,
                'int_status': 'shutdown',
                'oper_status': 'down',
                'vrf': 'default',
                'vrf_id': '0x60000000',
                'enabled': False,
            },
            'TenGigE0/0/0/15': {
                'ipv6_enabled': False,
                'int_status': 'shutdown',
                'oper_status': 'down',
                'vrf': 'default',
                'vrf_id': '0x60000000',
                'enabled': False,
            },
            'TenGigE0/0/0/16': {
                'ipv6_enabled': False,
                'int_status': 'shutdown',
                'oper_status': 'down',
                'vrf': 'default',
                'vrf_id': '0x60000000',
                'enabled': False,
            },
            'TenGigE0/0/0/17': {
                'ipv6_enabled': False,
                'int_status': 'shutdown',
                'oper_status': 'down',
                'vrf': 'default',
                'vrf_id': '0x60000000',
                'enabled': False,
            },
            'TenGigE0/0/0/18': {
                'ipv6_enabled': False,
                'int_status': 'shutdown',
                'oper_status': 'down',
                'vrf': 'default',
                'vrf_id': '0x60000000',
                'enabled': False,
            },
            'TenGigE0/0/0/19': {
                'ipv6_enabled': False,
                'int_status': 'shutdown',
                'oper_status': 'down',
                'vrf': 'default',
                'vrf_id': '0x60000000',
                'enabled': False,
            },
            'TenGigE0/0/0/20': {
                'ipv6_enabled': False,
                'int_status': 'shutdown',
                'oper_status': 'down',
                'vrf': 'default',
                'vrf_id': '0x60000000',
                'enabled': False,
            },
            'TenGigE0/0/0/21': {
                'ipv6_enabled': False,
                'int_status': 'shutdown',
                'oper_status': 'down',
                'vrf': 'default',
                'vrf_id': '0x60000000',
                'enabled': False,
            },
            'TenGigE0/0/0/22': {
                'ipv6_enabled': False,
                'int_status': 'shutdown',
                'oper_status': 'down',
                'vrf': 'default',
                'vrf_id': '0x60000000',
                'enabled': False,
            },
            'TenGigE0/0/0/23': {
                'ipv6_enabled': False,
                'int_status': 'shutdown',
                'oper_status': 'down',
                'vrf': 'default',
                'vrf_id': '0x60000000',
                'enabled': False,
            },
            'TwentyFiveGigE0/0/0/24': {
                'ipv6_enabled': False,
                'int_status': 'shutdown',
                'oper_status': 'down',
                'vrf': 'default',
                'vrf_id': '0x60000000',
                'enabled': False,
            },
            'TwentyFiveGigE0/0/0/25': {
                'ipv6_enabled': False,
                'int_status': 'shutdown',
                'oper_status': 'down',
                'vrf': 'default',
                'vrf_id': '0x60000000',
                'enabled': False,
            },
            'TwentyFiveGigE0/0/0/26': {
                'ipv6_enabled': False,
                'int_status': 'shutdown',
                'oper_status': 'down',
                'vrf': 'default',
                'vrf_id': '0x60000000',
                'enabled': False,
            },
            'TwentyFiveGigE0/0/0/27': {
                'ipv6_enabled': False,
                'int_status': 'shutdown',
                'oper_status': 'down',
                'vrf': 'default',
                'vrf_id': '0x60000000',
                'enabled': False,
            },
            'TwentyFiveGigE0/0/0/28': {
                'ipv6_enabled': False,
                'int_status': 'shutdown',
                'oper_status': 'down',
                'vrf': 'default',
                'vrf_id': '0x60000000',
                'enabled': False,
            },
            'TwentyFiveGigE0/0/0/29': {
                'ipv6_enabled': False,
                'int_status': 'shutdown',
                'oper_status': 'down',
                'vrf': 'default',
                'vrf_id': '0x60000000',
                'enabled': False,
            },
            'TwentyFiveGigE0/0/0/30': {
                'ipv6_enabled': False,
                'int_status': 'shutdown',
                'oper_status': 'down',
                'vrf': 'default',
                'vrf_id': '0x60000000',
                'enabled': False,
            },
            'TwentyFiveGigE0/0/0/31': {
                'ipv6_enabled': False,
                'int_status': 'shutdown',
                'oper_status': 'down',
                'vrf': 'default',
                'vrf_id': '0x60000000',
                'enabled': False,
            },
            'TwentyFiveGigE0/0/0/32': {
                'ipv6_enabled': False,
                'int_status': 'shutdown',
                'oper_status': 'down',
                'vrf': 'default',
                'vrf_id': '0x60000000',
                'enabled': False,
            },
            'TwentyFiveGigE0/0/0/33': {
                'ipv6_enabled': False,
                'int_status': 'shutdown',
                'oper_status': 'down',
                'vrf': 'default',
                'vrf_id': '0x60000000',
                'enabled': False,
            },
            'TwentyFiveGigE0/0/0/34': {
                'ipv6_enabled': False,
                'int_status': 'shutdown',
                'oper_status': 'down',
                'vrf': 'default',
                'vrf_id': '0x60000000',
                'enabled': False,
            },
            'TwentyFiveGigE0/0/0/35': {
                'ipv6_enabled': False,
                'int_status': 'shutdown',
                'oper_status': 'down',
                'vrf': 'default',
                'vrf_id': '0x60000000',
                'enabled': False,
            },
            'TwentyFiveGigE0/0/0/36': {
                'ipv6_enabled': False,
                'int_status': 'shutdown',
                'oper_status': 'down',
                'vrf': 'default',
                'vrf_id': '0x60000000',
                'enabled': False,
            },
            'TwentyFiveGigE0/0/0/37': {
                'ipv6_enabled': False,
                'int_status': 'shutdown',
                'oper_status': 'down',
                'vrf': 'default',
                'vrf_id': '0x60000000',
                'enabled': False,
            },
            'TwentyFiveGigE0/0/0/38': {
                'ipv6_enabled': False,
                'int_status': 'shutdown',
                'oper_status': 'down',
                'vrf': 'default',
                'vrf_id': '0x60000000',
                'enabled': False,
            },
            'TwentyFiveGigE0/0/0/39': {
                'ipv6_enabled': False,
                'int_status': 'shutdown',
                'oper_status': 'down',
                'vrf': 'default',
                'vrf_id': '0x60000000',
                'enabled': False,
            },
            'HundredGigE0/0/1/0': {
                'ipv6_enabled': False,
                'int_status': 'shutdown',
                'oper_status': 'down',
                'vrf': 'default',
                'vrf_id': '0x60000000',
                'enabled': False,
            },
            'HundredGigE0/0/1/1': {
                'ipv6_enabled': False,
                'int_status': 'shutdown',
                'oper_status': 'down',
                'vrf': 'default',
                'vrf_id': '0x60000000',
                'enabled': False,
            },
            'HundredGigE0/0/1/2/0': {
                'ipv6_enabled': True,
                'int_status': 'up',
                'oper_status': 'up',
                'vrf': 'default',
                'vrf_id': '0x60000000',
                'enabled': False,
            },
        }
    def test_empty(self):
        self.device1 = Mock(**self.empty_output)
        ipv6_vrf_all_interface_obj = ShowIpv6VrfAllInterface(device=self.device1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = ipv6_vrf_all_interface_obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        ipv6_vrf_all_interface_obj = ShowIpv6VrfAllInterface(device=self.device)
        parsed_output = ipv6_vrf_all_interface_obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output)

    def test_golden1(self):
        self.device = Mock(**self.golden_output1)
        ipv6_vrf_all_interface_obj = ShowIpv6VrfAllInterface(device=self.device)
        parsed_output = ipv6_vrf_all_interface_obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output1)
    
    def test_golden2(self):
        self.device = Mock(**self.golden_output2)
        ipv6_vrf_all_interface_obj = ShowIpv6VrfAllInterface(device=self.device)
        parsed_output = ipv6_vrf_all_interface_obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output2)

    def test_golden_custom(self):
        self.device = Mock(**self.golden_output_custom)
        ipv6_vrf_all_interface_obj = ShowIpv6VrfAllInterface(device=self.device)
        parsed_output = ipv6_vrf_all_interface_obj.parse(vrf='VRF1', interface='GigabitEthernet0/0/0/1')
        self.assertEqual(parsed_output, self.golden_parsed_output_custom)

#############################################################################
# unitest For show ethernet tags
#############################################################################

class test_show_ethernet_tags(unittest.TestCase):
    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output = {
        "GigabitEthernet0/0/0/0.511": {
              "rewrite_num_of_tags_push": 0,
              "status": "up",
              "rewrite_num_of_tags_pop": 1,
              "mtu": 1518,
              "outer_vlan": ".1Q:511",
              "vlan_id": "511"
         },
         "GigabitEthernet0/0/0/0.510": {
              "rewrite_num_of_tags_push": 0,
              "status": "up",
              "rewrite_num_of_tags_pop": 1,
              "mtu": 1518,
              "outer_vlan": ".1Q:510",
              "vlan_id": "510"
         },
         "GigabitEthernet0/0/0/0.503": {
              "rewrite_num_of_tags_push": 0,
              "status": "up",
              "rewrite_num_of_tags_pop": 1,
              "mtu": 1518,
              "outer_vlan": ".1Q:503",
              "vlan_id": "503"
         },
         "GigabitEthernet0/0/0/0.501": {
              "rewrite_num_of_tags_push": 0,
              "status": "up",
              "rewrite_num_of_tags_pop": 1,
              "mtu": 1518,
              "outer_vlan": ".1Q:501",
              "vlan_id": "501"
         },
         "GigabitEthernet0/0/0/0.502": {
              "rewrite_num_of_tags_push": 0,
              "status": "up",
              "rewrite_num_of_tags_pop": 1,
              "mtu": 1518,
              "outer_vlan": ".1Q:502",
              "vlan_id": "502"
         },
         "GigabitEthernet0/0/0/0.504": {
              "rewrite_num_of_tags_push": 0,
              "status": "up",
              "rewrite_num_of_tags_pop": 1,
              "mtu": 1518,
              "outer_vlan": ".1Q:504",
              "vlan_id": "504"
         },
         "GigabitEthernet0/0/0/0.505": {
              "rewrite_num_of_tags_push": 0,
              "status": "up",
              "rewrite_num_of_tags_pop": 1,
              "mtu": 1518,
              "outer_vlan": ".1Q:505",
              "vlan_id": "505"
         },
         "GigabitEthernet0/0/0/1.501": {
              "rewrite_num_of_tags_push": 0,
              "status": "up",
              "rewrite_num_of_tags_pop": 1,
              "mtu": 1518,
              "outer_vlan": ".1Q:501",
              "vlan_id": "501"
         }

    }
    golden_parsed_interface_output = {
        "GigabitEthernet0/0/0/1.501": {
            "rewrite_num_of_tags_push": 0,
            "status": "up",
            "rewrite_num_of_tags_pop": 1,
            "mtu": 1518,
            "outer_vlan": ".1Q:501",
            "vlan_id": "501"
        }
    }

    golden_output = {'execute.return_value': '''
        St:    AD - Administratively Down, Dn - Down, Up - Up
        Ly:    L2 - Switched layer 2 service, L3 = Terminated layer 3 service,
        Xtra   C - Match on Cos, E  - Match on Ethertype, M - Match on source MAC
        -,+:   Ingress rewrite operation; number of tags to pop and push respectively

        Interface               St  MTU  Ly Outer            Inner            Xtra -,+
        Gi0/0/0/0.501           Up  1518 L3 .1Q:501          -                -    1 0
        Gi0/0/0/0.502           Up  1518 L3 .1Q:502          -                -    1 0
        Gi0/0/0/0.503           Up  1518 L3 .1Q:503          -                -    1 0
        Gi0/0/0/0.504           Up  1518 L3 .1Q:504          -                -    1 0
        Gi0/0/0/0.505           Up  1518 L3 .1Q:505          -                -    1 0
        Gi0/0/0/0.510           Up  1518 L3 .1Q:510          -                -    1 0
        Gi0/0/0/0.511           Up  1518 L3 .1Q:511          -                -    1 0
        Gi0/0/0/1.501           Up  1518 L3 .1Q:501          -                -    1 0


    '''}
    golden_interface_output={'execute.return_value': '''
        St:    AD - Administratively Down, Dn - Down, Up - Up
        Ly:    L2 - Switched layer 2 service, L3 = Terminated layer 3 service,
        Xtra   C - Match on Cos, E  - Match on Ethertype, M - Match on source MAC
        -,+:   Ingress rewrite operation; number of tags to pop and push respectively

        Interface               St  MTU  Ly Outer            Inner            Xtra -,+
        Gi0/0/0/1.501           Up  1518 L3 .1Q:501          -                -    1 0
    '''}


    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowEthernetTags(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = ShowEthernetTags(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output)

    def test_golden_custom(self):
        self.device = Mock(**self.golden_output)
        obj = ShowEthernetTags(device=self.device)
        parsed_output = obj.parse(interface='Gi0/0/0/1.501')
        self.assertEqual(parsed_output,self.golden_parsed_output)


#############################################################################
# unitest For show interfaces <interface> accounting
#############################################################################

class test_show_interfaces_accounting(unittest.TestCase):
    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output = \
        {
          "GigabitEthernet0/0/0/0": {
            "accounting": {
              "arp": {
                "chars_in": 378,
                "chars_out": 378,
                "pkts_in": 9,
                "pkts_out": 9
              },
              "ipv4_multicast": {
                "chars_in": 0,
                "chars_out": 843700,
                "pkts_in": 0,
                "pkts_out": 10514
              },
              "ipv4_unicast": {
                "chars_in": 1226852,
                "chars_out": 887519,
                "pkts_in": 19254,
                "pkts_out": 13117
              }
            }
          },
          "GigabitEthernet0/0/0/1": {
            "accounting": {
              "arp": {
                "chars_in": 378,
                "chars_out": 378,
                "pkts_in": 9,
                "pkts_out": 9
              },
              "ipv4_multicast": {
                "chars_in": 0,
                "chars_out": 844816,
                "pkts_in": 0,
                "pkts_out": 10530
              },
              "ipv4_unicast": {
                "chars_in": 843784,
                "chars_out": 1764,
                "pkts_in": 10539,
                "pkts_out": 26
              }
            }
          }
        }



    golden_output = {'execute.return_value': '''
Tue Jun  5 20:45:11.544 UTC
No accounting statistics available for Loopback0
No accounting statistics available for Loopback1
No accounting statistics available for Null0
GigabitEthernet0/0/0/0
  Protocol              Pkts In         Chars In     Pkts Out        Chars Out
  IPV4_UNICAST            19254          1226852        13117           887519
  IPV4_MULTICAST              0                0        10514           843700
  ARP                         9              378            9              378

GigabitEthernet0/0/0/1
  Protocol              Pkts In         Chars In     Pkts Out        Chars Out
  IPV4_UNICAST            10539           843784           26             1764
  IPV4_MULTICAST              0                0        10530           844816
  ARP                         9              378            9              378



No accounting statistics available for MgmtEth0/RP0/CPU0/0



    '''}

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowInterfacesAccounting(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = ShowInterfacesAccounting(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output)

#############################################################################
# unitest For ip interface brief
#############################################################################

class test_show_ip_interface_brief(unittest.TestCase):
    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output = {'interface':
        {'GigabitEthernet0/0/0/0': {'interface_status': 'Up',
                                          'ip_address': 'unassigned',
                                          'protocol_status': 'Up',
                                          'vrf_name': 'default'},
               'GigabitEthernet0/0/0/0.501': {'interface_status': 'Up',
                                              'ip_address': '192.168.4.1',
                                              'protocol_status': 'Up',
                                              'vrf_name': 'VRF501'},
               'GigabitEthernet0/0/0/0.502': {'interface_status': 'Up',
                                              'ip_address': '192.168.154.1',
                                              'protocol_status': 'Up',
                                              'vrf_name': 'VRF502'},
               'GigabitEthernet0/0/0/0.503': {'interface_status': 'Up',
                                              'ip_address': '192.168.51.1',
                                              'protocol_status': 'Up',
                                              'vrf_name': 'VRF503'},
               'GigabitEthernet0/0/0/0.504': {'interface_status': 'Up',
                                              'ip_address': '192.168.205.1',
                                              'protocol_status': 'Up',
                                              'vrf_name': 'default'},
               'GigabitEthernet0/0/0/0.505': {'interface_status': 'Up',
                                              'ip_address': '192.168.106.1',
                                              'protocol_status': 'Up',
                                              'vrf_name': 'default'},
               'GigabitEthernet0/0/0/0.510': {'interface_status': 'Up',
                                              'ip_address': '192.168.151.1',
                                              'protocol_status': 'Up',
                                              'vrf_name': 'default'},
               'GigabitEthernet0/0/0/0.511': {'interface_status': 'Up',
                                              'ip_address': '192.168.64.1',
                                              'protocol_status': 'Up',
                                              'vrf_name': 'default'},
               'GigabitEthernet0/0/0/1': {'interface_status': 'Up',
                                          'ip_address': 'unassigned',
                                          'protocol_status': 'Up',
                                          'vrf_name': 'default'},
               'GigabitEthernet0/0/0/1.501': {'interface_status': 'Up',
                                              'ip_address': '192.168.51.1',
                                              'protocol_status': 'Up',
                                              'vrf_name': 'default'},
               'GigabitEthernet0/0/0/2': {'interface_status': 'Up',
                                          'ip_address': 'unassigned',
                                          'protocol_status': 'Up',
                                          'vrf_name': 'default'},
               'Loopback500': {'interface_status': 'Up',
                               'ip_address': '192.168.220.1',
                               'protocol_status': 'Up',
                               'vrf_name': 'default'},
               'Loopback501': {'interface_status': 'Up',
                               'ip_address': '192.168.111.1',
                               'protocol_status': 'Up',
                               'vrf_name': 'VRF501'},
               'Loopback502': {'interface_status': 'Up',
                               'ip_address': '192.168.4.1',
                               'protocol_status': 'Up',
                               'vrf_name': 'VRF502'},
               'Loopback503': {'interface_status': 'Up',
                               'ip_address': '192.168.154.1',
                               'protocol_status': 'Up',
                               'vrf_name': 'VRF503'},
               'Loopback505': {'interface_status': 'Up',
                               'ip_address': '192.168.205.1',
                               'protocol_status': 'Up',
                               'vrf_name': 'default'},
               'Loopback506': {'interface_status': 'Up',
                               'ip_address': '192.168.106.1',
                               'protocol_status': 'Up',
                               'vrf_name': 'default'},
               'Loopback510': {'interface_status': 'Up',
                               'ip_address': '192.168.240.1',
                               'protocol_status': 'Up',
                               'vrf_name': 'default'},
               'Loopback511': {'interface_status': 'Up',
                               'ip_address': '192.168.151.1',
                               'protocol_status': 'Up',
                               'vrf_name': 'default'},
               'Loopback512': {'interface_status': 'Up',
                               'ip_address': '192.168.64.1',
                               'protocol_status': 'Up',
                               'vrf_name': 'default'},
               'Loopback513': {'interface_status': 'Up',
                               'ip_address': '192.168.234.1',
                               'protocol_status': 'Up',
                               'vrf_name': 'default'},
               'MgmtEth0/RP0/CPU0/0': {'interface_status': 'Up',
                                       'ip_address': '10.1.17.179',
                                       'protocol_status': 'Up',
                                       'vrf_name': 'default'}}}

    golden_output = {'execute.return_value': '''
      RP/0/RP0/CPU0:PE1#show ip interface brief

      Interface                      IP-Address      Status          Protocol Vrf-Name
      Loopback500                    192.168.220.1       Up              Up       default 
      Loopback501                    192.168.111.1       Up              Up       VRF501  
      Loopback502                    192.168.4.1       Up              Up       VRF502  
      Loopback503                    192.168.154.1       Up              Up       VRF503  
      Loopback505                    192.168.205.1       Up              Up       default 
      Loopback506                    192.168.106.1       Up              Up       default 
      Loopback510                    192.168.240.1      Up              Up       default 
      Loopback511                    192.168.151.1      Up              Up       default 
      Loopback512                    192.168.64.1      Up              Up       default 
      Loopback513                    192.168.234.1      Up              Up       default 
      MgmtEth0/RP0/CPU0/0            10.1.17.179     Up              Up       default 
      GigabitEthernet0/0/0/0         unassigned      Up              Up       default 
      GigabitEthernet0/0/0/0.501     192.168.4.1       Up              Up       VRF501  
      GigabitEthernet0/0/0/0.502     192.168.154.1       Up              Up       VRF502  
      GigabitEthernet0/0/0/0.503     192.168.51.1       Up              Up       VRF503  
      GigabitEthernet0/0/0/0.504     192.168.205.1       Up              Up       default 
      GigabitEthernet0/0/0/0.505     192.168.106.1       Up              Up       default 
      GigabitEthernet0/0/0/0.510     192.168.151.1      Up              Up       default 
      GigabitEthernet0/0/0/0.511     192.168.64.1      Up              Up       default 
      GigabitEthernet0/0/0/1         unassigned      Up              Up       default 
      GigabitEthernet0/0/0/1.501     192.168.51.1       Up              Up       default 
      GigabitEthernet0/0/0/2         unassigned      Up              Up       default 
      RP/0/RP0/CPU0:PE1#show ip interface brief | i 10.1.17.179
      MgmtEth0/RP0/CPU0/0            10.1.17.179     Up              Up       default 
    '''}

    golden_parsed_output_pipe_ip = {'interface':
               {'MgmtEth0/RP0/CPU0/0': {'interface_status': 'Up',
                                       'ip_address': '10.1.17.179',
                                       'protocol_status': 'Up',
                                       'vrf_name': 'default'}}}

    golden_output_pipe_ip = {'execute.return_value': '''
      RP/0/RP0/CPU0:PE1#show ip interface brief | i 10.1.17.179
      MgmtEth0/RP0/CPU0/0            10.1.17.179     Up              Up       default 
    '''}

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowIpInterfaceBrief(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = ShowIpInterfaceBrief(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output)

    def test_golden1(self):
        self.device = Mock(**self.golden_output_pipe_ip)
        obj = ShowIpInterfaceBrief(device=self.device)
        parsed_output = obj.parse(ip='10.1.17.179')
        self.assertEqual(parsed_output,self.golden_parsed_output_pipe_ip)

    def test_empty_ipv4(self):
        self.device = Mock(**self.empty_output)
        obj = ShowIpv4InterfaceBrief(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden_ipv4(self):
        self.device = Mock(**self.golden_output)
        obj = ShowIpv4InterfaceBrief(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output)

    def test_golden1_ipv4(self):
        self.device = Mock(**self.golden_output_pipe_ip)
        obj = ShowIpv4InterfaceBrief(device=self.device)
        parsed_output = obj.parse(ip='10.1.17.179')
        self.assertEqual(parsed_output,self.golden_parsed_output_pipe_ip)
        

#############################################################################
# unitest For show interfaces
#############################################################################
class test_show_interfaces(unittest.TestCase):
    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output = {
        "BVI51": {
            "enabled": True,
            "line_protocol": "down",
            "oper_status": "down",
            "interface_state_transitions": 0,
            "type": "Bridge-Group Virtual Interface",
            "mac_address": "0000.59ff.60b1",
            "description": "NPON_Mcast_VLAN",
            "ipv4": {
                "192.168.166.9/30": {
                    "ip": "192.168.166.9",
                    "prefix_length": "30"
                }
            },
            "mtu": 1514,
            "bandwidth": 10000000,
            "bandwidth_max": 10000000,
            "reliability": "255/255",
            "txload": "0/255",
            "rxload": "0/255",
            "encapsulations": {
                "encapsulation": "arpa"
            },
            "loopback": "not set",
            "arp_type": "arpa",
            "arp_timeout": "04:00:00",
            "last_input": "Unknown",
            "last_output": "Unknown",
            "counters": {
                "last_clear": "Unknown",
                "rate": {
                    "load_interval": 300,
                    "in_rate": 0,
                    "in_rate_pkts": 0,
                    "out_rate": 0,
                    "out_rate_pkts": 0
                }
            }
        },
        "BVI100": {
            "enabled": True,
            "line_protocol": "down",
            "oper_status": "down",
            "interface_state_transitions": 0,
            "type": "Bridge-Group Virtual Interface",
            "mac_address": "0059.01ff.0001",
            "description": "au-hikari-mansion-100",
            "ipv4": {
                "192.168.36.254/24": {
                    "ip": "192.168.36.254",
                    "prefix_length": "24"
                }
            },
            "mtu": 1514,
            "bandwidth": 10000000,
            "bandwidth_max": 10000000,
            "reliability": "255/255",
            "txload": "0/255",
            "rxload": "0/255",
            "encapsulations": {
                "encapsulation": "arpa"
            },
            "loopback": "not set",
            "arp_type": "arpa",
            "arp_timeout": "04:00:00",
            "last_input": "Unknown",
            "last_output": "Unknown",
            "counters": {
                "last_clear": "Unknown",
                "rate": {
                    "load_interval": 300,
                    "in_rate": 0,
                    "in_rate_pkts": 0,
                    "out_rate": 0,
                    "out_rate_pkts": 0
                }
            }
        },
        "BVI301": {
            "enabled": True,
            "line_protocol": "down",
            "oper_status": "down",
            "interface_state_transitions": 0,
            "type": "Bridge-Group Virtual Interface",
            "mac_address": "0059.03ff.0102",
            "ipv4": {
                "192.168.1.254/24": {
                    "ip": "192.168.1.254",
                    "prefix_length": "24"
                }
            },
            "mtu": 1514,
            "bandwidth": 10000000,
            "bandwidth_max": 10000000,
            "reliability": "255/255",
            "txload": "0/255",
            "rxload": "0/255",
            "encapsulations": {
                "encapsulation": "arpa"
            },
            "loopback": "not set",
            "arp_type": "arpa",
            "arp_timeout": "04:00:00",
            "last_input": "Unknown",
            "last_output": "Unknown",
            "counters": {
                "last_clear": "Unknown",
                "rate": {
                    "load_interval": 300,
                    "in_rate": 0,
                    "in_rate_pkts": 0,
                    "out_rate": 0,
                    "out_rate_pkts": 0
                }
            }
        },
        "BVI1401": {
            "enabled": True,
            "line_protocol": "down",
            "oper_status": "down",
            "interface_state_transitions": 0,
            "type": "Bridge-Group Virtual Interface",
            "mac_address": "0059.14ff.0001",
            "description": "au-hikari-home",
            "ipv4": {
                "192.168.1.254/24": {
                    "ip": "192.168.1.254",
                    "prefix_length": "24"
                }
            },
            "mtu": 1514,
            "bandwidth": 10000000,
            "bandwidth_max": 10000000,
            "reliability": "255/255",
            "txload": "0/255",
            "rxload": "0/255",
            "encapsulations": {
                "encapsulation": "arpa"
            },
            "loopback": "not set",
            "arp_type": "arpa",
            "arp_timeout": "04:00:00",
            "last_input": "never",
            "last_output": "never",
            "counters": {
                "last_clear": "never",
                "rate": {
                    "load_interval": 300,
                    "in_rate": 0,
                    "in_rate_pkts": 0,
                    "out_rate": 0,
                    "out_rate_pkts": 0
                },
                "in_pkts": 0,
                "in_octets": 0,
                "in_total_drops": 0,
                "in_unknown_protos": 0,
                "in_broadcast_pkts": 0,
                "in_multicast_pkts": 0,
                "out_pkts": 0,
                "out_octets": 0,
                "out_total_drops": 0,
                "out_broadcast_pkts": 0,
                "out_multicast_pkts": 0
            }
        },
        "BVI1403": {
            "enabled": True,
            "line_protocol": "down",
            "oper_status": "down",
            "interface_state_transitions": 0,
            "type": "Bridge-Group Virtual Interface",
            "mac_address": "0059.14ff.0304",
            "description": "UQ-BS",
            "ipv4": {
                "192.168.169.254/24": {
                    "ip": "192.168.169.254",
                    "prefix_length": "24"
                }
            },
            "mtu": 1514,
            "bandwidth": 10000000,
            "bandwidth_max": 10000000,
            "reliability": "255/255",
            "txload": "0/255",
            "rxload": "0/255",
            "encapsulations": {
                "encapsulation": "arpa"
            },
            "loopback": "not set",
            "arp_type": "arpa",
            "arp_timeout": "04:00:00",
            "last_input": "Unknown",
            "last_output": "Unknown",
            "counters": {
                "last_clear": "Unknown",
                "rate": {
                    "load_interval": 300,
                    "in_rate": 0,
                    "in_rate_pkts": 0,
                    "out_rate": 0,
                    "out_rate_pkts": 0
                }
            }
        },
        "BVI1405": {
            "enabled": True,
            "line_protocol": "down",
            "oper_status": "down",
            "interface_state_transitions": 0,
            "type": "Bridge-Group Virtual Interface",
            "mac_address": "0059.14ff.0506",
            "description": "au-hikari-mansion-giga",
            "ipv4": {
                "192.168.36.254/24": {
                    "ip": "192.168.36.254",
                    "prefix_length": "24"
                }
            },
            "mtu": 1514,
            "bandwidth": 10000000,
            "bandwidth_max": 10000000,
            "reliability": "255/255",
            "txload": "0/255",
            "rxload": "0/255",
            "encapsulations": {
                "encapsulation": "arpa"
            },
            "loopback": "not set",
            "arp_type": "arpa",
            "arp_timeout": "04:00:00",
            "last_input": "Unknown",
            "last_output": "Unknown",
            "counters": {
                "last_clear": "Unknown",
                "rate": {
                    "load_interval": 300,
                    "in_rate": 0,
                    "in_rate_pkts": 0,
                    "out_rate": 0,
                    "out_rate_pkts": 0
                }
            }
        },
        "BVI1407": {
            "enabled": True,
            "line_protocol": "down",
            "oper_status": "down",
            "interface_state_transitions": 0,
            "type": "Bridge-Group Virtual Interface",
            "mac_address": "0059.14ff.0708",
            "description": "au-hikari-business",
            "ipv4": {
                "192.168.166.254/24": {
                    "ip": "192.168.166.254",
                    "prefix_length": "24"
                }
            },
            "mtu": 1514,
            "bandwidth": 10000000,
            "bandwidth_max": 10000000,
            "reliability": "255/255",
            "txload": "0/255",
            "rxload": "0/255",
            "encapsulations": {
                "encapsulation": "arpa"
            },
            "loopback": "not set",
            "arp_type": "arpa",
            "arp_timeout": "00:03:00",
            "last_input": "Unknown",
            "last_output": "Unknown",
            "counters": {
                "last_clear": "Unknown",
                "rate": {
                    "load_interval": 300,
                    "in_rate": 0,
                    "in_rate_pkts": 0,
                    "out_rate": 0,
                    "out_rate_pkts": 0
                }
            }
        },
        "BVI1410": {
            "enabled": True,
            "line_protocol": "down",
            "oper_status": "down",
            "interface_state_transitions": 0,
            "type": "Bridge-Group Virtual Interface",
            "mac_address": "0059.14ff.1011",
            "description": "JCOM",
            "ipv4": {
                "192.168.121.254/24": {
                    "ip": "192.168.121.254",
                    "prefix_length": "24"
                }
            },
            "mtu": 1514,
            "bandwidth": 10000000,
            "bandwidth_max": 10000000,
            "reliability": "255/255",
            "txload": "0/255",
            "rxload": "0/255",
            "encapsulations": {
                "encapsulation": "arpa"
            },
            "loopback": "not set",
            "arp_type": "arpa",
            "arp_timeout": "00:03:00",
            "last_input": "Unknown",
            "last_output": "Unknown",
            "counters": {
                "last_clear": "Unknown",
                "rate": {
                    "load_interval": 300,
                    "in_rate": 0,
                    "in_rate_pkts": 0,
                    "out_rate": 0,
                    "out_rate_pkts": 0
                }
            }
        },
        "Bundle-Ether1": {
            "enabled": True,
            "line_protocol": "up",
            "oper_status": "up",
            "interface_state_transitions": 9,
            "type": "Aggregated Ethernet interface(s)",
            "mac_address": "00bc.60ff.1119",
            "description": "to-ML26-BE1",
            "ipv4": {
                "192.168.0.25/30": {
                    "ip": "192.168.0.25",
                    "prefix_length": "30"
                }
            },
            "mtu": 1514,
            "bandwidth": 100000000,
            "bandwidth_max": 100000000,
            "reliability": "255/255",
            "txload": "0/255",
            "rxload": "0/255",
            "encapsulations": {
                "encapsulation": "arpa"
            },
            "duplex_mode": "full",
            "port_speed": "100000Mb/s",
            "loopback": "not set",
            "last_link_flapped": "3w3d",
            "arp_type": "arpa",
            "arp_timeout": "04:00:00",
            "port_channel": {
                "member_count": 1,
                "members": {
                    "HundredGigE0/0/1/2/0": {
                        "interface": "HundredGigE0/0/1/2/0",
                        "duplex_mode": "Full-duplex",
                        "speed": "100000Mb/s",
                        "state": "Active"
                    }
                }
            },
            "last_input": "00:00:00",
            "last_output": "00:00:00",
            "counters": {
                "last_clear": "never",
                "rate": {
                    "load_interval": 30,
                    "in_rate": 1000,
                    "in_rate_pkts": 0,
                    "out_rate": 2000,
                    "out_rate_pkts": 1
                },
                "in_pkts": 1716386544,
                "in_octets": 751342403591,
                "in_total_drops": 0,
                "in_unknown_protos": 0,
                "in_broadcast_pkts": 6,
                "in_multicast_pkts": 642898,
                "in_runts": 0,
                "in_giants": 0,
                "in_throttles": 0,
                "in_parity": 0,
                "in_errors": 0,
                "in_crc_errors": 0,
                "in_frame": 0,
                "in_overrun": 0,
                "in_ignored": 0,
                "in_abort": 0,
                "out_pkts": 1714349214,
                "out_octets": 754526715390,
                "out_total_drops": 0,
                "out_broadcast_pkts": 12,
                "out_multicast_pkts": 642896,
                "out_errors": 0,
                "out_underruns": 0,
                "out_applique": 0,
                "out_resets": 0,
                "out_buffer_failure": 0,
                "out_buffers_swapped": 0,
                "carrier_transitions": 0
            }
        },
        "Bundle-Ether100": {
            "enabled": True,
            "line_protocol": "up",
            "oper_status": "up",
            "interface_state_transitions": 1,
            "type": "Aggregated Ethernet interface(s)",
            "mac_address": "00bc.60ff.1118",
            "mtu": 1514,
            "bandwidth": 10000000,
            "bandwidth_max": 10000000,
            "reliability": "255/255",
            "txload": "0/255",
            "rxload": "0/255",
            "encapsulations": {
                "encapsulation": "arpa"
            },
            "duplex_mode": "full",
            "port_speed": "10000Mb/s",
            "loopback": "not set",
            "last_link_flapped": "5w6d",
            "port_channel": {
                "member_count": 1,
                "members": {
                    "TenGigE0/0/0/1": {
                        "interface": "TenGigE0/0/0/1",
                        "duplex_mode": "Full-duplex",
                        "speed": "10000Mb/s",
                        "state": "Active"
                    }
                }
            },
            "last_input": "00:00:00",
            "last_output": "00:00:00",
            "counters": {
                "last_clear": "never",
                "rate": {
                    "load_interval": 300,
                    "in_rate": 0,
                    "in_rate_pkts": 0,
                    "out_rate": 0,
                    "out_rate_pkts": 0
                },
                "in_pkts": 313163,
                "in_octets": 54531145,
                "in_total_drops": 0,
                "in_unknown_protos": 0,
                "in_broadcast_pkts": 0,
                "in_multicast_pkts": 313163,
                "in_runts": 0,
                "in_giants": 0,
                "in_throttles": 0,
                "in_parity": 0,
                "in_errors": 0,
                "in_crc_errors": 0,
                "in_frame": 0,
                "in_overrun": 0,
                "in_ignored": 0,
                "in_abort": 0,
                "out_pkts": 178045,
                "out_octets": 22136962,
                "out_total_drops": 0,
                "out_broadcast_pkts": 0,
                "out_multicast_pkts": 178045,
                "out_errors": 0,
                "out_underruns": 0,
                "out_applique": 0,
                "out_resets": 0,
                "out_buffer_failure": 0,
                "out_buffers_swapped": 0,
                "carrier_transitions": 0
            }
        },
        "Bundle-Ether100.12": {
            "enabled": True,
            "line_protocol": "up",
            "oper_status": "up",
            "interface_state_transitions": 1,
            "type": "VLAN sub-interface(s)",
            "mac_address": "00bc.60ff.1118",
            "layer2": True,
            "mtu": 1518,
            "bandwidth": 10000000,
            "bandwidth_max": 10000000,
            "reliability": "Unknown",
            "txload": "Unknown",
            "rxload": "Unknown",
            "encapsulations": {
                "encapsulation": "dot1q",
                "outer_match": "Dot1Q VLAN 12",
                "ethertype": "Any",
                "mac_match": "src any",
                "dest": "any"
            },
            "loopback": "not set",
            "last_link_flapped": "5w6d",
            "last_input": "never",
            "last_output": "never",
            "counters": {
                "last_clear": "never",
                "in_pkts": 0,
                "in_octets": 0,
                "in_drops": 0,
                "in_queue_drops": 0,
                "in_errors": 0,
                "out_pkts": 0,
                "out_octets": 0,
                "out_drops": 0,
                "out_queue_drops": 0,
                "out_errors": 0
            }
        },
        "Bundle-Ether100.22": {
            "enabled": True,
            "line_protocol": "up",
            "oper_status": "up",
            "interface_state_transitions": 1,
            "type": "VLAN sub-interface(s)",
            "mac_address": "00bc.60ff.1118",
            "layer2": True,
            "mtu": 1518,
            "bandwidth": 10000000,
            "bandwidth_max": 10000000,
            "reliability": "Unknown",
            "txload": "Unknown",
            "rxload": "Unknown",
            "encapsulations": {
                "encapsulation": "dot1q",
                "outer_match": "Dot1Q VLAN 22",
                "ethertype": "Any",
                "mac_match": "src any",
                "dest": "any"
            },
            "loopback": "not set",
            "last_link_flapped": "5w6d",
            "last_input": "never",
            "last_output": "never",
            "counters": {
                "last_clear": "never",
                "in_pkts": 0,
                "in_octets": 0,
                "in_drops": 0,
                "in_queue_drops": 0,
                "in_errors": 0,
                "out_pkts": 0,
                "out_octets": 0,
                "out_drops": 0,
                "out_queue_drops": 0,
                "out_errors": 0
            }
        },
        "Bundle-Ether1001": {
            "enabled": True,
            "line_protocol": "down",
            "oper_status": "down",
            "interface_state_transitions": 0,
            "type": "Aggregated Ethernet interface(s)",
            "mac_address": "00bc.60ff.1117",
            "mtu": 1514,
            "bandwidth": 0,
            "reliability": "255/255",
            "txload": "Unknown",
            "rxload": "Unknown",
            "encapsulations": {
                "encapsulation": "arpa"
            },
            "duplex_mode": "full",
            "port_speed": "0Kb/s",
            "loopback": "not set",
            "port_channel": {
                "member_count": 0
            },
            "last_input": "Unknown",
            "last_output": "Unknown",
            "counters": {
                "last_clear": "Unknown",
                "rate": {
                    "load_interval": 300,
                    "in_rate": 0,
                    "in_rate_pkts": 0,
                    "out_rate": 0,
                    "out_rate_pkts": 0
                }
            }
        },
        "Bundle-Ether1001.100": {
            "enabled": True,
            "line_protocol": "down",
            "oper_status": "down",
            "interface_state_transitions": 0,
            "type": "VLAN sub-interface(s)",
            "mac_address": "00bc.60ff.1117",
            "description": "Down Mansion-100",
            "layer2": True,
            "mtu": 1518,
            "bandwidth": 0,
            "reliability": "Unknown",
            "txload": "Unknown",
            "rxload": "Unknown",
            "encapsulations": {
                "encapsulation": "dot1q",
                "outer_match": "Dot1Q VLAN 300",
                "ethertype": "Any",
                "mac_match": "src any",
                "dest": "any"
            },
            "loopback": "not set",
            "last_input": "Unknown",
            "last_output": "Unknown",
            "counters": {
                "last_clear": "Unknown"
            }
        },
        "Bundle-Ether1001.1400": {
            "enabled": True,
            "line_protocol": "down",
            "oper_status": "down",
            "interface_state_transitions": 0,
            "type": "VLAN sub-interface(s)",
            "mac_address": "00bc.60ff.1117",
            "description": "Home Downlink",
            "layer2": True,
            "mtu": 1518,
            "bandwidth": 0,
            "reliability": "Unknown",
            "txload": "Unknown",
            "rxload": "Unknown",
            "encapsulations": {
                "encapsulation": "dot1q",
                "outer_match": "Dot1Q VLAN 3400",
                "ethertype": "Any",
                "mac_match": "src any",
                "dest": "any"
            },
            "loopback": "not set",
            "last_input": "Unknown",
            "last_output": "Unknown",
            "counters": {
                "last_clear": "Unknown"
            }
        },
        "Bundle-Ether1001.1402": {
            "enabled": True,
            "line_protocol": "down",
            "oper_status": "down",
            "interface_state_transitions": 0,
            "type": "VLAN sub-interface(s)",
            "mac_address": "00bc.60ff.1117",
            "description": "UQ_BS Downlink",
            "layer2": True,
            "mtu": 1518,
            "bandwidth": 0,
            "reliability": "Unknown",
            "txload": "Unknown",
            "rxload": "Unknown",
            "encapsulations": {
                "encapsulation": "dot1q",
                "outer_match": "Dot1Q VLAN 3402",
                "ethertype": "Any",
                "mac_match": "src any",
                "dest": "any"
            },
            "loopback": "not set",
            "last_input": "Unknown",
            "last_output": "Unknown",
            "counters": {
                "last_clear": "Unknown"
            }
        },
        "Bundle-Ether1001.1404": {
            "enabled": True,
            "line_protocol": "down",
            "oper_status": "down",
            "interface_state_transitions": 0,
            "type": "VLAN sub-interface(s)",
            "mac_address": "00bc.60ff.1117",
            "description": "au-hikari-mansion-giga Downlink",
            "layer2": True,
            "mtu": 1518,
            "bandwidth": 0,
            "reliability": "Unknown",
            "txload": "Unknown",
            "rxload": "Unknown",
            "encapsulations": {
                "encapsulation": "dot1q",
                "outer_match": "Dot1Q VLAN 3404",
                "ethertype": "Any",
                "mac_match": "src any",
                "dest": "any"
            },
            "loopback": "not set",
            "last_input": "Unknown",
            "last_output": "Unknown",
            "counters": {
                "last_clear": "Unknown"
            }
        },
        "Bundle-Ether1001.1406": {
            "enabled": True,
            "line_protocol": "down",
            "oper_status": "down",
            "interface_state_transitions": 0,
            "type": "VLAN sub-interface(s)",
            "mac_address": "00bc.60ff.1117",
            "description": "au Hikari Business Downlink",
            "layer2": True,
            "mtu": 1518,
            "bandwidth": 0,
            "reliability": "Unknown",
            "txload": "Unknown",
            "rxload": "Unknown",
            "encapsulations": {
                "encapsulation": "dot1q",
                "outer_match": "Dot1Q VLAN 3406",
                "ethertype": "Any",
                "mac_match": "src any",
                "dest": "any"
            },
            "loopback": "not set",
            "last_input": "Unknown",
            "last_output": "Unknown",
            "counters": {
                "last_clear": "Unknown"
            }
        },
        "Bundle-Ether1001.1410": {
            "enabled": True,
            "line_protocol": "down",
            "oper_status": "down",
            "interface_state_transitions": 0,
            "type": "VLAN sub-interface(s)",
            "mac_address": "00bc.60ff.1117",
            "description": "JCOM Downlink",
            "layer2": True,
            "mtu": 1518,
            "bandwidth": 0,
            "reliability": "Unknown",
            "txload": "Unknown",
            "rxload": "Unknown",
            "encapsulations": {
                "encapsulation": "dot1q",
                "outer_match": "Dot1Q VLAN 3410",
                "ethertype": "Any",
                "mac_match": "src any",
                "dest": "any"
            },
            "loopback": "not set",
            "last_input": "Unknown",
            "last_output": "Unknown",
            "counters": {
                "last_clear": "Unknown"
            }
        },
        "Bundle-Ether3333": {
            "enabled": True,
            "line_protocol": "down",
            "oper_status": "down",
            "interface_state_transitions": 0,
            "type": "Aggregated Ethernet interface(s)",
            "mac_address": "00bc.60ff.1116",
            "mtu": 1514,
            "bandwidth": 0,
            "reliability": "255/255",
            "txload": "Unknown",
            "rxload": "Unknown",
            "encapsulations": {
                "encapsulation": "arpa"
            },
            "duplex_mode": "full",
            "port_speed": "0Kb/s",
            "loopback": "not set",
            "port_channel": {
                "member_count": 1,
                "members": {
                    "TenGigE0/0/0/25": {
                        "interface": "TenGigE0/0/0/25",
                        "duplex_mode": "Full-duplex",
                        "speed": "10000Mb/s",
                        "state": "Configured"
                    }
                }
            },
            "last_input": "never",
            "last_output": "never",
            "counters": {
                "last_clear": "never",
                "rate": {
                    "load_interval": 300,
                    "in_rate": 0,
                    "in_rate_pkts": 0,
                    "out_rate": 0,
                    "out_rate_pkts": 0
                },
                "in_pkts": 0,
                "in_octets": 0,
                "in_total_drops": 0,
                "in_unknown_protos": 0,
                "in_broadcast_pkts": 0,
                "in_multicast_pkts": 0,
                "in_runts": 0,
                "in_giants": 0,
                "in_throttles": 0,
                "in_parity": 0,
                "in_errors": 0,
                "in_crc_errors": 0,
                "in_frame": 0,
                "in_overrun": 0,
                "in_ignored": 0,
                "in_abort": 0,
                "out_pkts": 0,
                "out_octets": 0,
                "out_total_drops": 0,
                "out_broadcast_pkts": 0,
                "out_multicast_pkts": 0,
                "out_errors": 0,
                "out_underruns": 0,
                "out_applique": 0,
                "out_resets": 0,
                "out_buffer_failure": 0,
                "out_buffers_swapped": 0,
                "carrier_transitions": 0
            }
        },
        "Loopback0": {
            "enabled": True,
            "line_protocol": "up",
            "oper_status": "up",
            "interface_state_transitions": 1,
            "type": "Loopback interface(s)",
            "ipv4": {
                "192.168.99.25/32": {
                    "ip": "192.168.99.25",
                    "prefix_length": "32"
                }
            },
            "mtu": 1500,
            "bandwidth": 0,
            "reliability": "Unknown",
            "txload": "Unknown",
            "rxload": "Unknown",
            "encapsulations": {
                "encapsulation": "loopback"
            },
            "loopback": "not set",
            "last_link_flapped": "5w6d",
            "last_input": "Unknown",
            "last_output": "Unknown",
            "counters": {
                "last_clear": "Unknown"
            }
        },
        "Null0": {
            "enabled": True,
            "line_protocol": "up",
            "oper_status": "up",
            "interface_state_transitions": 1,
            "type": "Null interface",
            "mtu": 1500,
            "bandwidth": 0,
            "reliability": "255/255",
            "txload": "Unknown",
            "rxload": "Unknown",
            "encapsulations": {
                "encapsulation": "null"
            },
            "loopback": "not set",
            "last_link_flapped": "5w6d",
            "last_input": "never",
            "last_output": "never",
            "counters": {
                "last_clear": "never",
                "rate": {
                    "load_interval": 300,
                    "in_rate": 0,
                    "in_rate_pkts": 0,
                    "out_rate": 0,
                    "out_rate_pkts": 0
                },
                "in_pkts": 0,
                "in_octets": 0,
                "in_total_drops": 0,
                "in_unknown_protos": 0,
                "in_broadcast_pkts": 0,
                "in_multicast_pkts": 0,
                "out_pkts": 0,
                "out_octets": 0,
                "out_total_drops": 0,
                "out_broadcast_pkts": 0,
                "out_multicast_pkts": 0
            }
        },
        "GigabitEthernet0/0/0/21": {
            "enabled": False,
            "line_protocol": "administratively down",
            "oper_status": "administratively down",
            "interface_state_transitions": 0,
            "type": "GigabitEthernet",
            "mac_address": "00bc.60ff.1151",
            "phys_address": "00bc.60ff.1151",
            "mtu": 1514,
            "bandwidth": 1000000,
            "bandwidth_max": 1000000,
            "reliability": "255/255",
            "txload": "0/255",
            "rxload": "0/255",
            "encapsulations": {
                "encapsulation": "arpa"
            },
            "duplex_mode": "full",
            "port_speed": "1000Mb/s",
            "link_type": "force-up",
            "auto_negotiate": False,
            "flow_control": {
                "receive": False,
                "send": False
            },
            "carrier_delay_up": 10,
            "loopback": "not set",
            "last_input": "never",
            "last_output": "never",
            "counters": {
                "last_clear": "never",
                "rate": {
                    "load_interval": 300,
                    "in_rate": 0,
                    "in_rate_pkts": 0,
                    "out_rate": 0,
                    "out_rate_pkts": 0
                },
                "in_pkts": 0,
                "in_octets": 0,
                "in_total_drops": 0,
                "in_unknown_protos": 0,
                "in_broadcast_pkts": 0,
                "in_multicast_pkts": 0,
                "in_runts": 0,
                "in_giants": 0,
                "in_throttles": 0,
                "in_parity": 0,
                "in_errors": 0,
                "in_crc_errors": 0,
                "in_frame": 0,
                "in_overrun": 0,
                "in_ignored": 0,
                "in_abort": 0,
                "out_pkts": 0,
                "out_octets": 0,
                "out_total_drops": 0,
                "out_broadcast_pkts": 0,
                "out_multicast_pkts": 0,
                "out_errors": 0,
                "out_underruns": 0,
                "out_applique": 0,
                "out_resets": 0,
                "out_buffer_failure": 0,
                "out_buffers_swapped": 0,
                "carrier_transitions": 0
            }
        },
        "GigabitEthernet0/0/0/23": {
            "enabled": True,
            "line_protocol": "up",
            "oper_status": "up",
            "interface_state_transitions": 13,
            "type": "GigabitEthernet",
            "mac_address": "00bc.60ff.1153",
            "phys_address": "00bc.60ff.1153",
            "mtu": 1514,
            "bandwidth": 1000000,
            "bandwidth_max": 1000000,
            "reliability": "255/255",
            "txload": "0/255",
            "rxload": "0/255",
            "encapsulations": {
                "encapsulation": "arpa"
            },
            "duplex_mode": "full",
            "port_speed": "1000Mb/s",
            "link_type": "force-up",
            "auto_negotiate": False,
            "media_type": "TFD",
            "flow_control": {
                "receive": False,
                "send": False
            },
            "carrier_delay_up": 10,
            "loopback": "not set",
            "last_link_flapped": "3w3d",
            "last_input": "00:03:58",
            "last_output": "never",
            "counters": {
                "last_clear": "never",
                "rate": {
                    "load_interval": 300,
                    "in_rate": 0,
                    "in_rate_pkts": 0,
                    "out_rate": 0,
                    "out_rate_pkts": 0
                },
                "in_pkts": 209145,
                "in_octets": 40356542,
                "in_total_drops": 0,
                "in_unknown_protos": 209145,
                "in_broadcast_pkts": 85731,
                "in_multicast_pkts": 123414,
                "in_runts": 0,
                "in_giants": 0,
                "in_throttles": 0,
                "in_parity": 0,
                "in_errors": 0,
                "in_crc_errors": 0,
                "in_frame": 0,
                "in_overrun": 0,
                "in_ignored": 0,
                "in_abort": 0,
                "out_pkts": 0,
                "out_octets": 0,
                "out_total_drops": 0,
                "out_broadcast_pkts": 0,
                "out_multicast_pkts": 0,
                "out_errors": 0,
                "out_underruns": 0,
                "out_applique": 0,
                "out_resets": 0,
                "out_buffer_failure": 0,
                "out_buffers_swapped": 0,
                "carrier_transitions": 11
            }
        },
        "GigabitEthernet0/0/0/27": {
            "enabled": False,
            "line_protocol": "administratively down",
            "oper_status": "administratively down",
            "interface_state_transitions": 0,
            "type": "GigabitEthernet",
            "mac_address": "00bc.60ff.1157",
            "phys_address": "00bc.60ff.1157",
            "mtu": 1514,
            "bandwidth": 1000000,
            "bandwidth_max": 1000000,
            "reliability": "255/255",
            "txload": "0/255",
            "rxload": "0/255",
            "encapsulations": {
                "encapsulation": "arpa"
            },
            "duplex_mode": "full",
            "port_speed": "1000Mb/s",
            "link_type": "force-up",
            "auto_negotiate": False,
            "flow_control": {
                "receive": False,
                "send": False
            },
            "carrier_delay_up": 10,
            "loopback": "not set",
            "last_input": "never",
            "last_output": "never",
            "counters": {
                "last_clear": "never",
                "rate": {
                    "load_interval": 300,
                    "in_rate": 0,
                    "in_rate_pkts": 0,
                    "out_rate": 0,
                    "out_rate_pkts": 0
                },
                "in_pkts": 0,
                "in_octets": 0,
                "in_total_drops": 0,
                "in_unknown_protos": 0,
                "in_broadcast_pkts": 0,
                "in_multicast_pkts": 0,
                "in_runts": 0,
                "in_giants": 0,
                "in_throttles": 0,
                "in_parity": 0,
                "in_errors": 0,
                "in_crc_errors": 0,
                "in_frame": 0,
                "in_overrun": 0,
                "in_ignored": 0,
                "in_abort": 0,
                "out_pkts": 0,
                "out_octets": 0,
                "out_total_drops": 0,
                "out_broadcast_pkts": 0,
                "out_multicast_pkts": 0,
                "out_errors": 0,
                "out_underruns": 0,
                "out_applique": 0,
                "out_resets": 0,
                "out_buffer_failure": 0,
                "out_buffers_swapped": 0,
                "carrier_transitions": 0
            }
        },
        "TenGigE0/0/0/0": {
            "enabled": True,
            "line_protocol": "up",
            "oper_status": "up",
            "interface_state_transitions": 1,
            "type": "TenGigE",
            "mac_address": "00bc.60ff.113c",
            "phys_address": "00bc.60ff.113c",
            "description": "to-ML24",
            "ipv4": {
                "192.168.0.22/30": {
                    "ip": "192.168.0.22",
                    "prefix_length": "30"
                }
            },
            "mtu": 1514,
            "bandwidth": 10000000,
            "bandwidth_max": 10000000,
            "reliability": "255/255",
            "txload": "0/255",
            "rxload": "0/255",
            "encapsulations": {
                "encapsulation": "arpa"
            },
            "duplex_mode": "full",
            "port_speed": "10000Mb/s",
            "link_type": "force-up",
            "auto_negotiate": False,
            "media_type": "SR",
            "flow_control": {
                "receive": False,
                "send": False
            },
            "carrier_delay_up": 10,
            "loopback": "not set",
            "last_link_flapped": "5w6d",
            "arp_type": "arpa",
            "arp_timeout": "04:00:00",
            "last_input": "00:00:00",
            "last_output": "00:00:00",
            "counters": {
                "last_clear": "never",
                "rate": {
                    "load_interval": 300,
                    "in_rate": 2000,
                    "in_rate_pkts": 1,
                    "out_rate": 1000,
                    "out_rate_pkts": 0
                },
                "in_pkts": 858438357,
                "in_octets": 377844978719,
                "in_total_drops": 0,
                "in_unknown_protos": 0,
                "in_broadcast_pkts": 6,
                "in_multicast_pkts": 761392,
                "in_runts": 0,
                "in_giants": 0,
                "in_throttles": 0,
                "in_parity": 0,
                "in_errors": 0,
                "in_crc_errors": 0,
                "in_frame": 0,
                "in_overrun": 0,
                "in_ignored": 0,
                "in_abort": 0,
                "out_pkts": 860493206,
                "out_octets": 374682459456,
                "out_total_drops": 0,
                "out_broadcast_pkts": 6,
                "out_multicast_pkts": 524312,
                "out_errors": 0,
                "out_underruns": 0,
                "out_applique": 0,
                "out_resets": 0,
                "out_buffer_failure": 0,
                "out_buffers_swapped": 0,
                "carrier_transitions": 1
            }
        },
        "TenGigE0/0/0/1": {
            "enabled": True,
            "line_protocol": "up",
            "oper_status": "up",
            "interface_state_transitions": 1,
            "type": "TenGigE",
            "mac_address": "00bc.60ff.113d",
            "phys_address": "00bc.60ff.113d",
            "description": "L2SW Po12",
            "mtu": 1518,
            "bandwidth": 10000000,
            "bandwidth_max": 10000000,
            "reliability": "255/255",
            "txload": "0/255",
            "rxload": "0/255",
            "encapsulations": {
                "encapsulation": "arpa"
            },
            "duplex_mode": "full",
            "port_speed": "10000Mb/s",
            "link_type": "force-up",
            "auto_negotiate": False,
            "media_type": "SR",
            "flow_control": {
                "receive": False,
                "send": False
            },
            "carrier_delay_up": 10,
            "loopback": "not set",
            "last_link_flapped": "5w6d",
            "last_input": "00:00:00",
            "last_output": "00:00:00",
            "counters": {
                "last_clear": "never",
                "rate": {
                    "load_interval": 30,
                    "in_rate": 0,
                    "in_rate_pkts": 0,
                    "out_rate": 0,
                    "out_rate_pkts": 0
                },
                "in_pkts": 313163,
                "in_octets": 54531145,
                "in_total_drops": 0,
                "in_unknown_protos": 0,
                "in_broadcast_pkts": 0,
                "in_multicast_pkts": 313163,
                "in_runts": 0,
                "in_giants": 0,
                "in_throttles": 0,
                "in_parity": 0,
                "in_errors": 0,
                "in_crc_errors": 0,
                "in_frame": 0,
                "in_overrun": 0,
                "in_ignored": 0,
                "in_abort": 0,
                "out_pkts": 178045,
                "out_octets": 22136962,
                "out_total_drops": 0,
                "out_broadcast_pkts": 0,
                "out_multicast_pkts": 178045,
                "out_errors": 0,
                "out_underruns": 0,
                "out_applique": 0,
                "out_resets": 0,
                "out_buffer_failure": 0,
                "out_buffers_swapped": 0,
                "carrier_transitions": 1
            }
        },
        "TenGigE0/0/0/2": {
            "enabled": True,
            "line_protocol": "up",
            "oper_status": "up",
            "interface_state_transitions": 3,
            "type": "TenGigE",
            "mac_address": "00bc.60ff.113e",
            "phys_address": "00bc.60ff.113e",
            "layer2": True,
            "mtu": 1514,
            "bandwidth": 10000000,
            "bandwidth_max": 10000000,
            "reliability": "255/255",
            "txload": "0/255",
            "rxload": "0/255",
            "encapsulations": {
                "encapsulation": "arpa"
            },
            "duplex_mode": "full",
            "port_speed": "10000Mb/s",
            "link_type": "force-up",
            "auto_negotiate": False,
            "media_type": "SR",
            "flow_control": {
                "receive": False,
                "send": False
            },
            "carrier_delay_up": 10,
            "loopback": "not set",
            "last_link_flapped": "1w3d",
            "last_input": "00:00:00",
            "last_output": "00:00:00",
            "counters": {
                "last_clear": "never",
                "rate": {
                    "load_interval": 300,
                    "in_rate": 0,
                    "in_rate_pkts": 1,
                    "out_rate": 0,
                    "out_rate_pkts": 1
                },
                "in_pkts": 3800143,
                "in_octets": 231571320,
                "in_total_drops": 0,
                "in_unknown_protos": 0,
                "in_broadcast_pkts": 0,
                "in_multicast_pkts": 3800143,
                "in_runts": 0,
                "in_giants": 0,
                "in_throttles": 0,
                "in_parity": 0,
                "in_errors": 0,
                "in_crc_errors": 0,
                "in_frame": 0,
                "in_overrun": 0,
                "in_ignored": 0,
                "in_abort": 0,
                "out_pkts": 3562789,
                "out_octets": 213767340,
                "out_total_drops": 0,
                "out_broadcast_pkts": 0,
                "out_multicast_pkts": 3562789,
                "out_errors": 0,
                "out_underruns": 0,
                "out_applique": 0,
                "out_resets": 0,
                "out_buffer_failure": 0,
                "out_buffers_swapped": 0,
                "carrier_transitions": 3
            }
        }
    }

    golden_output = {'execute.return_value': '''
        #show interfaces 
        Sat Aug  3 03:25:29.028 EST
        BVI51 is down, line protocol is down 
          Interface state transitions: 0
          Hardware is Bridge-Group Virtual Interface, address is 0000.59ff.60b1
          Description: NPON_Mcast_VLAN
          Internet address is 192.168.166.9/30
          MTU 1514 bytes, BW 10000000 Kbit (Max: 10000000 Kbit)
             reliability 255/255, txload 0/255, rxload 0/255
          Encapsulation ARPA,  loopback not set,
          ARP type ARPA, ARP timeout 04:00:00
          Last input Unknown, output Unknown
          Last clearing of "show interface" counters Unknown
          5 minute input rate 0 bits/sec, 0 packets/sec
          5 minute output rate 0 bits/sec, 0 packets/sec

        BVI100 is down, line protocol is down 
          Interface state transitions: 0
          Hardware is Bridge-Group Virtual Interface, address is 0059.01ff.0001
          Description: au-hikari-mansion-100
          Internet address is 192.168.36.254/24
          MTU 1514 bytes, BW 10000000 Kbit (Max: 10000000 Kbit)
             reliability 255/255, txload 0/255, rxload 0/255
          Encapsulation ARPA,  loopback not set,
          ARP type ARPA, ARP timeout 04:00:00
          Last input Unknown, output Unknown
          Last clearing of "show interface" counters Unknown
          5 minute input rate 0 bits/sec, 0 packets/sec
          5 minute output rate 0 bits/sec, 0 packets/sec

        BVI301 is down, line protocol is down 
          Interface state transitions: 0
          Hardware is Bridge-Group Virtual Interface, address is 0059.03ff.0102
          Internet address is 192.168.1.254/24
          MTU 1514 bytes, BW 10000000 Kbit (Max: 10000000 Kbit)
             reliability 255/255, txload 0/255, rxload 0/255
          Encapsulation ARPA,  loopback not set,
          ARP type ARPA, ARP timeout 04:00:00
          Last input Unknown, output Unknown
          Last clearing of "show interface" counters Unknown
          5 minute input rate 0 bits/sec, 0 packets/sec
          5 minute output rate 0 bits/sec, 0 packets/sec

        BVI1401 is down, line protocol is down 
          Interface state transitions: 0
          Hardware is Bridge-Group Virtual Interface, address is 0059.14ff.0001
          Description: au-hikari-home
          Internet address is 192.168.1.254/24
          MTU 1514 bytes, BW 10000000 Kbit (Max: 10000000 Kbit)
             reliability 255/255, txload 0/255, rxload 0/255
          Encapsulation ARPA,  loopback not set,
          ARP type ARPA, ARP timeout 04:00:00
          Last input never, output never
          Last clearing of "show interface" counters never
          5 minute input rate 0 bits/sec, 0 packets/sec
          5 minute output rate 0 bits/sec, 0 packets/sec
             0 packets input, 0 bytes, 0 total input drops
             0 drops for unrecognized upper-level protocol
             Received 0 broadcast packets, 0 multicast packets
             0 packets output, 0 bytes, 0 total output drops
             Output 0 broadcast packets, 0 multicast packets
                  
        BVI1403 is down, line protocol is down 
          Interface state transitions: 0
          Hardware is Bridge-Group Virtual Interface, address is 0059.14ff.0304
          Description: UQ-BS  
          Internet address is 192.168.169.254/24
          MTU 1514 bytes, BW 10000000 Kbit (Max: 10000000 Kbit)
             reliability 255/255, txload 0/255, rxload 0/255
          Encapsulation ARPA,  loopback not set,
          ARP type ARPA, ARP timeout 04:00:00
          Last input Unknown, output Unknown
          Last clearing of "show interface" counters Unknown
          5 minute input rate 0 bits/sec, 0 packets/sec
          5 minute output rate 0 bits/sec, 0 packets/sec
                  
        BVI1405 is down, line protocol is down 
          Interface state transitions: 0
          Hardware is Bridge-Group Virtual Interface, address is 0059.14ff.0506
          Description: au-hikari-mansion-giga
          Internet address is 192.168.36.254/24
          MTU 1514 bytes, BW 10000000 Kbit (Max: 10000000 Kbit)
             reliability 255/255, txload 0/255, rxload 0/255
          Encapsulation ARPA,  loopback not set,
          ARP type ARPA, ARP timeout 04:00:00
          Last input Unknown, output Unknown
          Last clearing of "show interface" counters Unknown
          5 minute input rate 0 bits/sec, 0 packets/sec
          5 minute output rate 0 bits/sec, 0 packets/sec
                  
        BVI1407 is down, line protocol is down 
          Interface state transitions: 0
          Hardware is Bridge-Group Virtual Interface, address is 0059.14ff.0708
          Description: au-hikari-business
          Internet address is 192.168.166.254/24
          MTU 1514 bytes, BW 10000000 Kbit (Max: 10000000 Kbit)
             reliability 255/255, txload 0/255, rxload 0/255
          Encapsulation ARPA,  loopback not set,
          ARP type ARPA, ARP timeout 00:03:00
          Last input Unknown, output Unknown
          Last clearing of "show interface" counters Unknown
          5 minute input rate 0 bits/sec, 0 packets/sec
          5 minute output rate 0 bits/sec, 0 packets/sec
                  
        BVI1410 is down, line protocol is down 
          Interface state transitions: 0
          Hardware is Bridge-Group Virtual Interface, address is 0059.14ff.1011
          Description: JCOM  
          Internet address is 192.168.121.254/24
          MTU 1514 bytes, BW 10000000 Kbit (Max: 10000000 Kbit)
             reliability 255/255, txload 0/255, rxload 0/255
          Encapsulation ARPA,  loopback not set,
          ARP type ARPA, ARP timeout 00:03:00
          Last input Unknown, output Unknown
          Last clearing of "show interface" counters Unknown
          5 minute input rate 0 bits/sec, 0 packets/sec
          5 minute output rate 0 bits/sec, 0 packets/sec
                  
        Bundle-Ether1 is up, line protocol is up 
          Interface state transitions: 9
          Hardware is Aggregated Ethernet interface(s), address is 00bc.60ff.1119
          Description: to-ML26-BE1
          Internet address is 192.168.0.25/30
          MTU 1514 bytes, BW 100000000 Kbit (Max: 100000000 Kbit)
             reliability 255/255, txload 0/255, rxload 0/255
          Encapsulation ARPA,
          Full-duplex, 100000Mb/s
          loopback not set,
          Last link flapped 3w3d
          ARP type ARPA, ARP timeout 04:00:00
            No. of members in this bundle: 1
              HundredGigE0/0/1/2/0         Full-duplex  100000Mb/s   Active          
          Last input 00:00:00, output 00:00:00
          Last clearing of "show interface" counters never
          30 second input rate 1000 bits/sec, 0 packets/sec
          30 second output rate 2000 bits/sec, 1 packets/sec
             1716386544 packets input, 751342403591 bytes, 0 total input drops
             0 drops for unrecognized upper-level protocol
             Received 6 broadcast packets, 642898 multicast packets
                      0 runts, 0 giants, 0 throttles, 0 parity
             0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored, 0 abort
             1714349214 packets output, 754526715390 bytes, 0 total output drops
             Output 12 broadcast packets, 642896 multicast packets
             0 output errors, 0 underruns, 0 applique, 0 resets
             0 output buffer failures, 0 output buffers swapped out
             0 carrier transitions

        Bundle-Ether100 is up, line protocol is up 
          Interface state transitions: 1
          Hardware is Aggregated Ethernet interface(s), address is 00bc.60ff.1118
          Internet address is Unknown
          MTU 1514 bytes, BW 10000000 Kbit (Max: 10000000 Kbit)
             reliability 255/255, txload 0/255, rxload 0/255
          Encapsulation ARPA,
          Full-duplex, 10000Mb/s
          loopback not set,
          Last link flapped 5w6d
            No. of members in this bundle: 1
              TenGigE0/0/0/1               Full-duplex  10000Mb/s    Active          
          Last input 00:00:00, output 00:00:00
          Last clearing of "show interface" counters never
          5 minute input rate 0 bits/sec, 0 packets/sec
          5 minute output rate 0 bits/sec, 0 packets/sec
             313163 packets input, 54531145 bytes, 0 total input drops
             0 drops for unrecognized upper-level protocol
             Received 0 broadcast packets, 313163 multicast packets
                      0 runts, 0 giants, 0 throttles, 0 parity
             0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored, 0 abort
             178045 packets output, 22136962 bytes, 0 total output drops
             Output 0 broadcast packets, 178045 multicast packets
             0 output errors, 0 underruns, 0 applique, 0 resets
             0 output buffer failures, 0 output buffers swapped out
             0 carrier transitions
                  
        Bundle-Ether100.12 is up, line protocol is up 
          Interface state transitions: 1
          Hardware is VLAN sub-interface(s), address is 00bc.60ff.1118
          Layer 2 Transport Mode
          MTU 1518 bytes, BW 10000000 Kbit (Max: 10000000 Kbit)
             reliability Unknown, txload Unknown, rxload Unknown
          Encapsulation 802.1Q Virtual LAN,
            Outer Match: Dot1Q VLAN 12
            Ethertype Any, MAC Match src any, dest any
          loopback not set,
          Last link flapped 5w6d
          Last input never, output never
          Last clearing of "show interface" counters never
             0 packets input, 0 bytes
             0 input drops, 0 queue drops, 0 input errors
             0 packets output, 0 bytes
             0 output drops, 0 queue drops, 0 output errors
                  
        Bundle-Ether100.22 is up, line protocol is up 
          Interface state transitions: 1
          Hardware is VLAN sub-interface(s), address is 00bc.60ff.1118
          Layer 2 Transport Mode
          MTU 1518 bytes, BW 10000000 Kbit (Max: 10000000 Kbit)
             reliability Unknown, txload Unknown, rxload Unknown
          Encapsulation 802.1Q Virtual LAN,
            Outer Match: Dot1Q VLAN 22
            Ethertype Any, MAC Match src any, dest any
          loopback not set,
          Last link flapped 5w6d
          Last input never, output never
          Last clearing of "show interface" counters never
             0 packets input, 0 bytes
             0 input drops, 0 queue drops, 0 input errors
             0 packets output, 0 bytes
             0 output drops, 0 queue drops, 0 output errors
                  
        Bundle-Ether1001 is down, line protocol is down 
          Interface state transitions: 0
          Hardware is Aggregated Ethernet interface(s), address is 00bc.60ff.1117
          Internet address is Unknown
          MTU 1514 bytes, BW 0 Kbit
             reliability 255/255, txload Unknown, rxload Unknown
          Encapsulation ARPA,
          Full-duplex, 0Kb/s
          loopback not set,
            No. of members in this bundle: 0
          Last input Unknown, output Unknown
          Last clearing of "show interface" counters Unknown
          5 minute input rate 0 bits/sec, 0 packets/sec
          5 minute output rate 0 bits/sec, 0 packets/sec
                  
        Bundle-Ether1001.100 is down, line protocol is down 
          Interface state transitions: 0
          Hardware is VLAN sub-interface(s), address is 00bc.60ff.1117
          Description: Down Mansion-100
          Layer 2 Transport Mode
          MTU 1518 bytes, BW 0 Kbit
             reliability Unknown, txload Unknown, rxload Unknown
          Encapsulation 802.1Q Virtual LAN,
            Outer Match: Dot1Q VLAN 300
            Ethertype Any, MAC Match src any, dest any
          loopback not set,
          Last input Unknown, output Unknown
          Last clearing of "show interface" counters Unknown
          Input/output data rate is disabled.
                  
        Bundle-Ether1001.1400 is down, line protocol is down 
          Interface state transitions: 0
          Hardware is VLAN sub-interface(s), address is 00bc.60ff.1117
          Description: Home Downlink
          Layer 2 Transport Mode
          MTU 1518 bytes, BW 0 Kbit
             reliability Unknown, txload Unknown, rxload Unknown
          Encapsulation 802.1Q Virtual LAN,
            Outer Match: Dot1Q VLAN 3400
            Ethertype Any, MAC Match src any, dest any
          loopback not set,
          Last input Unknown, output Unknown
          Last clearing of "show interface" counters Unknown
          Input/output data rate is disabled.
                  
        Bundle-Ether1001.1402 is down, line protocol is down 
          Interface state transitions: 0
          Hardware is VLAN sub-interface(s), address is 00bc.60ff.1117
          Description: UQ_BS Downlink
          Layer 2 Transport Mode
          MTU 1518 bytes, BW 0 Kbit
             reliability Unknown, txload Unknown, rxload Unknown
          Encapsulation 802.1Q Virtual LAN,
            Outer Match: Dot1Q VLAN 3402
            Ethertype Any, MAC Match src any, dest any
          loopback not set,
          Last input Unknown, output Unknown
          Last clearing of "show interface" counters Unknown
          Input/output data rate is disabled.
                  
        Bundle-Ether1001.1404 is down, line protocol is down 
          Interface state transitions: 0
          Hardware is VLAN sub-interface(s), address is 00bc.60ff.1117
          Description: au-hikari-mansion-giga Downlink
          Layer 2 Transport Mode
          MTU 1518 bytes, BW 0 Kbit
             reliability Unknown, txload Unknown, rxload Unknown
          Encapsulation 802.1Q Virtual LAN,
            Outer Match: Dot1Q VLAN 3404
            Ethertype Any, MAC Match src any, dest any
          loopback not set,
          Last input Unknown, output Unknown
          Last clearing of "show interface" counters Unknown
          Input/output data rate is disabled.
                  
        Bundle-Ether1001.1406 is down, line protocol is down 
          Interface state transitions: 0
          Hardware is VLAN sub-interface(s), address is 00bc.60ff.1117
          Description: au Hikari Business Downlink
          Layer 2 Transport Mode
          MTU 1518 bytes, BW 0 Kbit
             reliability Unknown, txload Unknown, rxload Unknown
          Encapsulation 802.1Q Virtual LAN,
            Outer Match: Dot1Q VLAN 3406
            Ethertype Any, MAC Match src any, dest any
          loopback not set,
          Last input Unknown, output Unknown
          Last clearing of "show interface" counters Unknown
          Input/output data rate is disabled.
                  
        Bundle-Ether1001.1410 is down, line protocol is down 
          Interface state transitions: 0
          Hardware is VLAN sub-interface(s), address is 00bc.60ff.1117
          Description: JCOM Downlink
          Layer 2 Transport Mode
          MTU 1518 bytes, BW 0 Kbit
             reliability Unknown, txload Unknown, rxload Unknown
          Encapsulation 802.1Q Virtual LAN,
            Outer Match: Dot1Q VLAN 3410
            Ethertype Any, MAC Match src any, dest any
          loopback not set,
          Last input Unknown, output Unknown
          Last clearing of "show interface" counters Unknown
          Input/output data rate is disabled.
                  
        Bundle-Ether3333 is down, line protocol is down 
          Interface state transitions: 0
          Hardware is Aggregated Ethernet interface(s), address is 00bc.60ff.1116
          Internet address is Unknown
          MTU 1514 bytes, BW 0 Kbit
             reliability 255/255, txload Unknown, rxload Unknown
          Encapsulation ARPA,
          Full-duplex, 0Kb/s
          loopback not set,
            No. of members in this bundle: 1
              TenGigE0/0/0/25              Full-duplex  10000Mb/s    Configured      
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
                  
        Loopback0 is up, line protocol is up 
          Interface state transitions: 1
          Hardware is Loopback interface(s)
          Internet address is 192.168.99.25/32
          MTU 1500 bytes, BW 0 Kbit
             reliability Unknown, txload Unknown, rxload Unknown
          Encapsulation Loopback,  loopback not set,
          Last link flapped 5w6d
          Last input Unknown, output Unknown
          Last clearing of "show interface" counters Unknown
          Input/output data rate is disabled.
                  
        Null0 is up, line protocol is up 
          Interface state transitions: 1
          Hardware is Null interface
          Internet address is Unknown
          MTU 1500 bytes, BW 0 Kbit
             reliability 255/255, txload Unknown, rxload Unknown
          Encapsulation Null,  loopback not set,
          Last link flapped 5w6d
          Last input never, output never
          Last clearing of "show interface" counters never
          5 minute input rate 0 bits/sec, 0 packets/sec
          5 minute output rate 0 bits/sec, 0 packets/sec
             0 packets input, 0 bytes, 0 total input drops
             0 drops for unrecognized upper-level protocol
             Received 0 broadcast packets, 0 multicast packets
             0 packets output, 0 bytes, 0 total output drops
             Output 0 broadcast packets, 0 multicast packets
                  
        GigabitEthernet0/0/0/21 is administratively down, line protocol is administratively down 
          Interface state transitions: 0
          Hardware is GigabitEthernet, address is 00bc.60ff.1151 (bia 00bc.60ff.1151)
          Internet address is Unknown
          MTU 1514 bytes, BW 1000000 Kbit (Max: 1000000 Kbit)
             reliability 255/255, txload 0/255, rxload 0/255
          Encapsulation ARPA,
          Full-duplex, 1000Mb/s, link type is force-up
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
                  
        GigabitEthernet0/0/0/23 is up, line protocol is up 
          Interface state transitions: 13
          Hardware is GigabitEthernet, address is 00bc.60ff.1153 (bia 00bc.60ff.1153)
          Internet address is Unknown
          MTU 1514 bytes, BW 1000000 Kbit (Max: 1000000 Kbit)
             reliability 255/255, txload 0/255, rxload 0/255
          Encapsulation ARPA,
          Full-duplex, 1000Mb/s, TFD, link type is force-up
          output flow control is off, input flow control is off
          Carrier delay (up) is 10 msec
          loopback not set,
          Last link flapped 3w3d
          Last input 00:03:58, output never
          Last clearing of "show interface" counters never
          5 minute input rate 0 bits/sec, 0 packets/sec
          5 minute output rate 0 bits/sec, 0 packets/sec
             209145 packets input, 40356542 bytes, 0 total input drops
             209145 drops for unrecognized upper-level protocol
             Received 85731 broadcast packets, 123414 multicast packets
                      0 runts, 0 giants, 0 throttles, 0 parity
             0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored, 0 abort
             0 packets output, 0 bytes, 0 total output drops
             Output 0 broadcast packets, 0 multicast packets
             0 output errors, 0 underruns, 0 applique, 0 resets
             0 output buffer failures, 0 output buffers swapped out
             11 carrier transitions
                  
        GigabitEthernet0/0/0/27 is administratively down, line protocol is administratively down 
          Interface state transitions: 0
          Hardware is GigabitEthernet, address is 00bc.60ff.1157 (bia 00bc.60ff.1157)
          Internet address is Unknown
          MTU 1514 bytes, BW 1000000 Kbit (Max: 1000000 Kbit)
             reliability 255/255, txload 0/255, rxload 0/255
          Encapsulation ARPA,
          Full-duplex, 1000Mb/s, link type is force-up
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
                  
        TenGigE0/0/0/0 is up, line protocol is up 
          Interface state transitions: 1
          Hardware is TenGigE, address is 00bc.60ff.113c (bia 00bc.60ff.113c)
          Description: to-ML24
          Internet address is 192.168.0.22/30
          MTU 1514 bytes, BW 10000000 Kbit (Max: 10000000 Kbit)
             reliability 255/255, txload 0/255, rxload 0/255
          Encapsulation ARPA,
          Full-duplex, 10000Mb/s, SR, link type is force-up
          output flow control is off, input flow control is off
          Carrier delay (up) is 10 msec
          loopback not set,
          Last link flapped 5w6d
          ARP type ARPA, ARP timeout 04:00:00
          Last input 00:00:00, output 00:00:00
          Last clearing of "show interface" counters never
          5 minute input rate 2000 bits/sec, 1 packets/sec
          5 minute output rate 1000 bits/sec, 0 packets/sec
             858438357 packets input, 377844978719 bytes, 0 total input drops
             0 drops for unrecognized upper-level protocol
             Received 6 broadcast packets, 761392 multicast packets
                      0 runts, 0 giants, 0 throttles, 0 parity
             0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored, 0 abort
             860493206 packets output, 374682459456 bytes, 0 total output drops
             Output 6 broadcast packets, 524312 multicast packets
             0 output errors, 0 underruns, 0 applique, 0 resets
             0 output buffer failures, 0 output buffers swapped out
             1 carrier transitions
                  
        TenGigE0/0/0/1 is up, line protocol is up 
          Interface state transitions: 1
          Hardware is TenGigE, address is 00bc.60ff.113d (bia 00bc.60ff.113d)
          Description: L2SW Po12
          Internet address is Unknown
          MTU 1518 bytes, BW 10000000 Kbit (Max: 10000000 Kbit)
             reliability 255/255, txload 0/255, rxload 0/255
          Encapsulation ARPA,
          Full-duplex, 10000Mb/s, SR, link type is force-up
          output flow control is off, input flow control is off
          Carrier delay (up) is 10 msec
          loopback not set,
          Last link flapped 5w6d
          Last input 00:00:00, output 00:00:00
          Last clearing of "show interface" counters never
          30 second input rate 0 bits/sec, 0 packets/sec
          30 second output rate 0 bits/sec, 0 packets/sec
             313163 packets input, 54531145 bytes, 0 total input drops
             0 drops for unrecognized upper-level protocol
             Received 0 broadcast packets, 313163 multicast packets
                      0 runts, 0 giants, 0 throttles, 0 parity
             0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored, 0 abort
             178045 packets output, 22136962 bytes, 0 total output drops
             Output 0 broadcast packets, 178045 multicast packets
             0 output errors, 0 underruns, 0 applique, 0 resets
             0 output buffer failures, 0 output buffers swapped out
             1 carrier transitions
                  
        TenGigE0/0/0/2 is up, line protocol is up 
          Interface state transitions: 3
          Hardware is TenGigE, address is 00bc.60ff.113e (bia 00bc.60ff.113e)
          Layer 2 Transport Mode
          MTU 1514 bytes, BW 10000000 Kbit (Max: 10000000 Kbit)
             reliability 255/255, txload 0/255, rxload 0/255
          Encapsulation ARPA,
          Full-duplex, 10000Mb/s, SR, link type is force-up
          output flow control is off, input flow control is off
          Carrier delay (up) is 10 msec
          loopback not set,
          Last link flapped 1w3d
          Last input 00:00:00, output 00:00:00
          Last clearing of "show interface" counters never
          5 minute input rate 0 bits/sec, 1 packets/sec
          5 minute output rate 0 bits/sec, 1 packets/sec
             3800143 packets input, 231571320 bytes, 0 total input drops
             0 drops for unrecognized upper-level protocol
             Received 0 broadcast packets, 3800143 multicast packets
                      0 runts, 0 giants, 0 throttles, 0 parity
             0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored, 0 abort
             3562789 packets output, 213767340 bytes, 0 total output drops
             Output 0 broadcast packets, 3562789 multicast packets
             0 output errors, 0 underruns, 0 applique, 0 resets
             0 output buffer failures, 0 output buffers swapped out
             3 carrier transitions
    '''}

    golden_interface_parsed_output = {
        "Bundle-Ether1": {
            "enabled": True,
            "line_protocol": "up",
            "oper_status": "up",
            "interface_state_transitions": 9,
            "type": "Aggregated Ethernet interface(s)",
            "mac_address": "00bc.60ff.1119",
            "description": "to-ML26-BE1",
            "ipv4": {
                "192.168.0.25/30": {
                    "ip": "192.168.0.25",
                    "prefix_length": "30"
                }
            },
            "mtu": 1514,
            "bandwidth": 100000000,
            "bandwidth_max": 100000000,
            "reliability": "255/255",
            "txload": "0/255",
            "rxload": "0/255",
            "encapsulations": {
                "encapsulation": "arpa"
            },
            "duplex_mode": "full",
            "port_speed": "100000Mb/s",
            "loopback": "not set",
            "last_link_flapped": "3w3d",
            "arp_type": "arpa",
            "arp_timeout": "04:00:00",
            "port_channel": {
                "member_count": 1,
                "members": {
                    "HundredGigE0/0/1/2/0": {
                        "interface": "HundredGigE0/0/1/2/0",
                        "duplex_mode": "Full-duplex",
                        "speed": "100000Mb/s",
                        "state": "Active"
                    }
                }
            },
            "last_input": "00:00:00",
            "last_output": "00:00:00",
            "counters": {
                "last_clear": "never",
                "rate": {
                    "load_interval": 30,
                    "in_rate": 1000,
                    "in_rate_pkts": 0,
                    "out_rate": 2000,
                    "out_rate_pkts": 1
                },
                "in_pkts": 1716386544,
                "in_octets": 751342403591,
                "in_total_drops": 0,
                "in_unknown_protos": 0,
                "in_broadcast_pkts": 6,
                "in_multicast_pkts": 642898,
                "in_runts": 0,
                "in_giants": 0,
                "in_throttles": 0,
                "in_parity": 0,
                "in_errors": 0,
                "in_crc_errors": 0,
                "in_frame": 0,
                "in_overrun": 0,
                "in_ignored": 0,
                "in_abort": 0,
                "out_pkts": 1714349214,
                "out_octets": 754526715390,
                "out_total_drops": 0,
                "out_broadcast_pkts": 12,
                "out_multicast_pkts": 642896,
                "out_errors": 0,
                "out_underruns": 0,
                "out_applique": 0,
                "out_resets": 0,
                "out_buffer_failure": 0,
                "out_buffers_swapped": 0,
                "carrier_transitions": 0
            }
        }
    }

    golden_interface_output = {'execute.return_value': '''
      Bundle-Ether1 is up, line protocol is up 
      Interface state transitions: 9
      Hardware is Aggregated Ethernet interface(s), address is 00bc.60ff.1119
      Description: to-ML26-BE1
      Internet address is 192.168.0.25/30
      MTU 1514 bytes, BW 100000000 Kbit (Max: 100000000 Kbit)
         reliability 255/255, txload 0/255, rxload 0/255
      Encapsulation ARPA,
      Full-duplex, 100000Mb/s
      loopback not set,
      Last link flapped 3w3d
      ARP type ARPA, ARP timeout 04:00:00
        No. of members in this bundle: 1
          HundredGigE0/0/1/2/0         Full-duplex  100000Mb/s   Active          
      Last input 00:00:00, output 00:00:00
      Last clearing of "show interface" counters never
      30 second input rate 1000 bits/sec, 0 packets/sec
      30 second output rate 2000 bits/sec, 1 packets/sec
         1716386544 packets input, 751342403591 bytes, 0 total input drops
         0 drops for unrecognized upper-level protocol
         Received 6 broadcast packets, 642898 multicast packets
                  0 runts, 0 giants, 0 throttles, 0 parity
         0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored, 0 abort
         1714349214 packets output, 754526715390 bytes, 0 total output drops
         Output 12 broadcast packets, 642896 multicast packets
         0 output errors, 0 underruns, 0 applique, 0 resets
         0 output buffer failures, 0 output buffers swapped out
         0 carrier transitions
    '''}

    golden_interface_parsed_output2 = {
        "Bundle-Ether1": {
            "enabled": True,
            "line_protocol": "up",
            "oper_status": "up",
            "interface_state_transitions": 9,
            "description": "to-ML26-BE1",
            "ipv4": {
                "192.168.0.25/30": {
                    "ip": "192.168.0.25",
                    "prefix_length": "30"
                }
            },
            "mtu": 1514,
            "bandwidth": 100000000,
            "bandwidth_max": 100000000,
            "reliability": "255/255",
            "txload": "0/255",
            "rxload": "0/255",
            "encapsulations": {
                "encapsulation": "arpa"
            },
            "duplex_mode": "full",
            "port_speed": "100000Mb/s",
            "loopback": "not set",
            "last_link_flapped": "3w3d",
            "arp_type": "arpa",
            "arp_timeout": "04:00:00",
            "port_channel": {
                "member_count": 1,
                "members": {
                    "HundredGigE0/0/1/2/0": {
                        "interface": "HundredGigE0/0/1/2/0",
                        "duplex_mode": "Full-duplex",
                        "speed": "100000Mb/s",
                        "state": "Active"
                    }
                }
            },
            "last_input": "00:00:00",
            "last_output": "00:00:00",
            "counters": {
                "last_clear": "never",
                "rate": {
                    "load_interval": 30,
                    "in_rate": 1000,
                    "in_rate_pkts": 0,
                    "out_rate": 2000,
                    "out_rate_pkts": 1
                },
                "in_pkts": 1716386544,
                "in_octets": 751342403591,
                "in_total_drops": 0,
                "in_unknown_protos": 0,
                "in_broadcast_pkts": 6,
                "in_multicast_pkts": 642898,
                "in_runts": 0,
                "in_giants": 0,
                "in_throttles": 0,
                "in_parity": 0,
                "in_errors": 0,
                "in_crc_errors": 0,
                "in_frame": 0,
                "in_overrun": 0,
                "in_ignored": 0,
                "in_abort": 0,
                "out_pkts": 1714349214,
                "out_octets": 754526715390,
                "out_total_drops": 0,
                "out_broadcast_pkts": 12,
                "out_multicast_pkts": 642896,
                "out_errors": 0,
                "out_underruns": 0,
                "out_applique": 0,
                "out_resets": 0,
                "out_buffer_failure": 0,
                "out_buffers_swapped": 0,
                "carrier_transitions": 0
            }
        }
    }

    golden_interface_output2 = {'execute.return_value': '''
      Bundle-Ether1 is up, line protocol is up 
      Interface state transitions: 9
      Description: to-ML26-BE1
      Internet address is 192.168.0.25/30
      MTU 1514 bytes, BW 100000000 Kbit (Max: 100000000 Kbit)
         reliability 255/255, txload 0/255, rxload 0/255
      Encapsulation ARPA,
      Full-duplex, 100000Mb/s
      loopback not set,
      Last link flapped 3w3d
      ARP type ARPA, ARP timeout 04:00:00
        No. of members in this bundle: 1
          HundredGigE0/0/1/2/0         Full-duplex  100000Mb/s   Active          
      Last input 00:00:00, output 00:00:00
      Last clearing of "show interface" counters never
      30 second input rate 1000 bits/sec, 0 packets/sec
      30 second output rate 2000 bits/sec, 1 packets/sec
         1716386544 packets input, 751342403591 bytes, 0 total input drops
         0 drops for unrecognized upper-level protocol
         Received 6 broadcast packets, 642898 multicast packets
                  0 runts, 0 giants, 0 throttles, 0 parity
         0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored, 0 abort
         1714349214 packets output, 754526715390 bytes, 0 total output drops
         Output 12 broadcast packets, 642896 multicast packets
         0 output errors, 0 underruns, 0 applique, 0 resets
         0 output buffer failures, 0 output buffers swapped out
         0 carrier transitions
    '''}

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowInterfaces(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = ShowInterfaces(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output)

    def test_golden_interface(self):
        self.device = Mock(**self.golden_interface_output)
        obj = ShowInterfaces(device=self.device)
        parsed_output = obj.parse(interface='Bundle-Ether1')
        self.assertEqual(parsed_output,self.golden_interface_parsed_output)

    def test_golden_interface2(self):
        self.device = Mock(**self.golden_interface_output2)
        obj = ShowInterfaces(device=self.device)
        parsed_output = obj.parse(interface='Bundle-Ether1')
        self.assertEqual(parsed_output,self.golden_interface_parsed_output2)
        
#############################################################################
# unitest For show interfaces description
#############################################################################
class test_show_interfaces_description(unittest.TestCase):
    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output = {
        "interfaces": {
            "Bundle-Ether12": {
                "description": "",
                "protocol": "up",
                "status": "up"
            },
            "Bundle-Ether23": {
                "description": "",
                "protocol": "up",
                "status": "up"
            },
            "Loopback0": {
                "description": "",
                "protocol": "up",
                "status": "up"
            },
            "Loopback300": {
                "description": "",
                "protocol": "up",
                "status": "up"
            },
            "Nu0": {
                "description": "",
                "protocol": "up",
                "status" :"up"
            },
            "Mg0/RP0/CPU0/0": {
                "description": "",
                "protocol": "up",
                "status": "up"
            },
            "GigabitEthernet0/0/0/0": {
                "description": "",
                "protocol": "up",
                "status": "up"
            },
            "GigabitEthernet0/0/0/0.90": {
                "description": "",
                "protocol": "up",
                "status": "up"
            },
            "GigabitEthernet0/0/0/1": {
                "description": "",
                "protocol": "up",
                "status": "up"
            },
            "GigabitEthernet0/0/0/1.90": {
                "description": "",
                "protocol": "up",
                "status": "up"
            },
            "GigabitEthernet0/0/0/2": {
                "description": "",
                "protocol": "up",
                "status": "up"
            }
        }
    }

    golden_output = {'execute.return_value': '''
        Interface          Status      Protocol    Description
        --------------------------------------------------------------------------------
        BE12               up          up
        BE23               up          up
        Lo0                up          up
        Lo300              up          up
        Nu0                up          up
        Mg0/RP0/CPU0/0     up          up
        Gi0/0/0/0          up          up
        Gi0/0/0/0.90       up          up
        Gi0/0/0/1          up          up
        Gi0/0/0/1.90       up          up
        Gi0/0/0/2          up          up
    '''}

    golden_parsed_interface_output = {
        "interfaces": {
            "Bundle-Ether12": {
                "description": "",
                "protocol": "up",
                "status": "up"
            }
        }
    }

    golden_interface_output = {'execute.return_value': '''
        Interface          Status      Protocol    Description
        --------------------------------------------------------------------------------
        BE12 		up	 up
    '''}


    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowInterfacesDescription(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = ShowInterfacesDescription(device=self.device)
        parsed_output = obj.parse()
        self.maxDiff = None
        self.assertEqual(parsed_output,self.golden_parsed_output)
        
    def test_golden_interface(self):
        self.device = Mock(**self.golden_interface_output)
        obj = ShowInterfacesDescription(device=self.device)
        parsed_output = obj.parse(interface='BE12')
        self.maxDiff = None
        self.assertEqual(parsed_output,self.golden_parsed_interface_output)

#############################################################################
# unitest For show ipv6 interface {interface}
#############################################################################
class test_show_ipv6_interface(unittest.TestCase):
    device = Device(name='aDevice')
    
    empty_output = {'execute.return_value': ''}

    golden_output = {'execute.return_value':'''
        genie_device#show ipv6 interface gigabitEthernet 0/0/0/0.1
        Wed Oct 28 02:37:35.972 UTC
        GigabitEthernet0/0/0/0 is Up, ipv6 protocol is Up, Vrfid is default (0x60000000)
        IPv6 is enabled, link-local address is fe80::250:56ff:fe8d:8d58
        Global unicast address(es):
            2001:112::1, subnet is 2001:112::/64
        Joined group address(es): ff02::1:ff00:1 ff02::1:ff8d:8d58 ff02::2
            ff02::1
        MTU is 1514 (1500 is available to IPv6)
        ICMP redirects are disabled
        ICMP unreachables are enabled
        ND DAD is enabled, number of DAD attempts 1
        ND reachable time is 0 milliseconds
        ND cache entry limit is 1000000000
        ND advertised retransmit interval is 0 milliseconds
        ND router advertisements are sent every 160 to 240 seconds
        ND router advertisements live for 1800 seconds
        Hosts use stateless autoconfig for addresses.
        Outgoing access list is not set
        Inbound  common access list is not set, access list is not set
        Table Id is 0xe0800000
        Complete protocol adjacency: 0
        Complete glean adjacency: 0
        Incomplete protocol adjacency: 0
        Incomplete glean adjacency: 0
        Dropped protocol request: 0
        Dropped glean request: 0    
    '''}

    golden_parsed_output = {
        'GigabitEthernet0/0/0/0': {
            'enabled': True,
            'oper_status': 'up',
            'vrf': 'default',
            'int_status': 'up',
            'ipv6': {
                'incomplete_protocol_adj': '0',
                'complete_glean_adj': '0',
                'dropped_protocol_req': '0',
                'dropped_glean_req': '0',
                'nd_router_adv': '1800',
                'complete_protocol_adj': '0',
                'icmp_unreachables': 'enabled',
                'ipv6_link_local': 'fe80::250:56ff:fe8d:8d58',
                'incomplete_glean_adj': '0',
                'nd_adv_duration': '160-240',
                'ipv6_groups': ['ff02::1:ff00:1', 'ff02::1:ff8d:8d58', 'ff02::2', 'ff02::1'],
                'nd_adv_retrans_int': '0',
                'nd_cache_limit': '1000000000',
                'stateless_autoconfig': True,
                'icmp_redirects': 'disabled',
                'dad_attempts': '1',
                'ipv6_mtu': '1514',
                'ipv6_mtu_available': '1500',
                '2001:112::1/64': {
                    'ipv6_subnet': '2001:112::',
                    'ipv6_prefix_length': '64',
                    'ipv6': '2001:112::1',
                },
                'nd_dad': 'enabled',
                'nd_reachable_time': '0',
                'table_id': '0xe0800000',
            },
            'vrf_id': '0x60000000',
            'ipv6_enabled': True,
        },
    }

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowIpv6VrfAllInterface(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = ShowIpv6VrfAllInterface(device=self.device)
        parsed_output = obj.parse(interface='gigabitEthernet 0/0/0/0.1')
        self.maxDiff = None
        self.assertEqual(parsed_output,self.golden_parsed_output)    
if __name__ == '__main__':
    unittest.main()

