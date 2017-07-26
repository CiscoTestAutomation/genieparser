import re
import unittest
from unittest.mock import Mock

from ats.topology import Device

from metaparser.util.exceptions import SchemaEmptyParserError, \
                                       SchemaMissingKeyError

from parser.nxos.show_interface import ShowInterface

class test_show_interface(unittest.TestCase):
    device = Device(name='aDevice')
    device0 = Device(name='bDevice')
    empty_output = {'execute.return_value': ''}
    golden_parsed_output = {'interface': {'Ethernet2/1': {'auto_mdix': 'off',
                               'auto_negotiate': False,
                               'bandwidth': 768,
                               'beacon': 'off',
                               'counters': {'in_bad_etype_drop': 0,
                                            'in_bad_proto_drop': 0,
                                            'in_broadcast_pkts': 0,
                                            'in_bytes': 0,
                                            'in_crc_errors': 0,
                                            'in_discard': 0,
                                            'in_error': 0,
                                            'in_giant': 0,
                                            'in_if_down_drop': 0,
                                            'in_ignored': 0,
                                            'in_jumbo_packets': 0,
                                            'in_mac_pause_frames': 0,
                                            'in_multicast_pkts': 0,
                                            'in_no_buffer': 0,
                                            'in_overrun': 0,
                                            'in_pkts': 0,
                                            'in_runts': 0,
                                            'in_short_frame': 0,
                                            'in_storm_suppression_packets': 0,
                                            'in_underrun': 0,
                                            'in_unicast_pkts': 0,
                                            'in_watchdog': 0,
                                            'in_with_dribble': 0,
                                            'out_babble': 0,
                                            'out_bytes': 0,
                                            'out_collision': 0,
                                            'out_deferred': 0,
                                            'out_discard': 0,
                                            'out_error': 0,
                                            'out_jumbo_packets': 0,
                                            'out_late_collision': 0,
                                            'out_lost_carrier': 0,
                                            'out_mac_pause_frames': 0,
                                            'out_no_carrier': 0,
                                            'out_pkts': 0,
                                            'rate': {'in_rate': 0,
                                                     'in_rate_bps': 0,
                                                     'in_rate_pkts': 0,
                                                     'in_rate_pps': 0,
                                                     'load_interval': 0,
                                                     'out_rate': 0,
                                                     'out_rate_bps': 0,
                                                     'out_rate_pkts': 0,
                                                     'out_rate_pps': 0}},
                               'delay': 3330,
                               'description': 'desc',
                               'duplex_mode': 'full-duplex',
                               'efficient_ethernet': 'n/a',
                               'enabled': True,
                               'encapsulations': {'encapsulation': 'ARPA'},
                               'flow_control': {'flow_control_receive': False,
                                                'flow_control_send': False},
                               'interface_reset': 1,
                               'ipv4': {'address': {'ipv4': '10.4.4.4',
                                                    'prefix_length': '/24',
                                                    'route_tag': 10,
                                                    'secondary': True}},
                               'last_clearing': 'never',
                               'last_linked_flapped': '00:00:29',
                               'link_state': 'None',
                               'mac_address': 'aaaa.bbbb.cccc',
                               'medium': 'broadcast',
                               'mtu': 1600,
                               'oper_status': 'up,',
                               'phys_address': '5254.003b.4aca',
                               'port_mode': 'routed',
                               'port_speed': '1000',
                               'reliability': '255/255',
                               'rxload': '1/255',
                               'switchport_monitor': 'off',
                               'txload': '1/255',
                               'types': '10/100/1000 Ethernet'},
               'Ethernet2/1.10': {'auto_mdix': 'off',
                                  'bandwidth': 768,
                                  'delay': 10,
                                  'enabled': False,
                                  'link_state': 'Administratively down',
                                  'mac_address': '5254.003b.4af8',
                                  'mtu': 1600,
                                  'oper_status': 'down,',
                                  'parent_interface': 'Ethernet2/1',
                                  'phys_address': '5254.003b.4aca',
                                  'port_mode': 'routed',
                                  'reliability': '255/255',
                                  'rxload': '1/255',
                                  'txload': '1/255',
                                  'types': '10/100/1000 Ethernet'},
               'Ethernet2/1.20': {'auto_mdix': 'off',
                                  'bandwidth': 768,
                                  'delay': 10,
                                  'enabled': True,
                                  'link_state': 'None',
                                  'mac_address': '5254.003b.4af8',
                                  'mtu': 1600,
                                  'oper_status': 'up,',
                                  'parent_interface': 'Ethernet2/1',
                                  'phys_address': '5254.003b.4aca',
                                  'port_mode': 'routed',
                                  'reliability': '255/255',
                                  'rxload': '1/255',
                                  'txload': '1/255',
                                  'types': '10/100/1000 Ethernet'},
               'Ethernet2/2': {'auto_mdix': 'off',
                               'auto_negotiate': False,
                               'bandwidth': 1000000,
                               'beacon': 'off',
                               'counters': {'in_bad_etype_drop': 0,
                                            'in_bad_proto_drop': 0,
                                            'in_broadcast_pkts': 0,
                                            'in_bytes': 0,
                                            'in_crc_errors': 0,
                                            'in_discard': 0,
                                            'in_error': 0,
                                            'in_giant': 0,
                                            'in_if_down_drop': 0,
                                            'in_ignored': 0,
                                            'in_jumbo_packets': 0,
                                            'in_mac_pause_frames': 0,
                                            'in_multicast_pkts': 0,
                                            'in_no_buffer': 0,
                                            'in_overrun': 0,
                                            'in_pkts': 0,
                                            'in_runts': 0,
                                            'in_short_frame': 0,
                                            'in_storm_suppression_packets': 0,
                                            'in_underrun': 0,
                                            'in_unicast_pkts': 0,
                                            'in_watchdog': 0,
                                            'in_with_dribble': 0,
                                            'out_babble': 0,
                                            'out_bytes': 0,
                                            'out_collision': 0,
                                            'out_deferred': 0,
                                            'out_discard': 0,
                                            'out_error': 0,
                                            'out_jumbo_packets': 0,
                                            'out_late_collision': 0,
                                            'out_lost_carrier': 0,
                                            'out_mac_pause_frames': 0,
                                            'out_no_carrier': 0,
                                            'out_pkts': 0,
                                            'rate': {'in_rate': 0,
                                                     'in_rate_bps': 0,
                                                     'in_rate_pkts': 0,
                                                     'in_rate_pps': 0,
                                                     'load_interval': 0,
                                                     'out_rate': 0,
                                                     'out_rate_bps': 0,
                                                     'out_rate_pkts': 0,
                                                     'out_rate_pps': 0}},
                               'delay': 10,
                               'duplex_mode': 'full-duplex',
                               'efficient_ethernet': 'n/a',
                               'enabled': True,
                               'encapsulations': {'encapsulation': 'ARPA'},
                               'flow_control': {'flow_control_receive': False,
                                                'flow_control_send': False},
                               'interface_reset': 1,
                               'last_clearing': 'never',
                               'last_linked_flapped': '00:07:28',
                               'link_state': 'None',
                               'mac_address': '5254.00ac.b52e',
                               'medium': 'broadcast',
                               'mtu': 1500,
                               'oper_status': 'up,',
                               'phys_address': '5254.00ac.b52e',
                               'port_mode': 'trunk',
                               'port_speed': '1000',
                               'reliability': '255/255',
                               'rxload': '1/255',
                               'switchport_monitor': 'off',
                               'txload': '1/255',
                               'types': '10/100/1000 Ethernet'},
               'mgmt0': {'auto_mdix': 'off',
                         'auto_negotiate': True,
                         'bandwidth': 1000000,
                         'counters': {'rate': {'in_rate': 0,
                                               'in_rate_pkts': 0,
                                               'load_interval': 1,
                                               'out_rate': 24,
                                               'out_rate_pkts': 0}},
                         'delay': 10,
                         'duplex_mode': 'full-duplex',
                         'enabled': True,
                         'encapsulations': {'encapsulation': 'ARPA'},
                         'link_state': 'None',
                         'mac_address': '5254.00c9.d26e',
                         'medium': 'broadcast',
                         'mtu': 1500,
                         'oper_status': 'up',
                         'phys_address': '5254.00c9.d26e',
                         'port_mode': 'routed',
                         'port_speed': '1000',
                         'reliability': '255/255',
                         'rxload': '1/255',
                         'txload': '1/255',
                         'types': 'Ethernet'}}}


    golden_output = {'execute.return_value': '''
       
    mgmt0 is up
      admin state is up
      Hardware: Ethernet, address: 5254.00c9.d26e (bia 5254.00c9.d26e)
      MTU 1500 bytes, BW 1000000 Kbit, DLY 10 usec
      reliability 255/255, txload 1/255, rxload 1/255
      Encapsulation ARPA, medium is broadcast
      Port mode is routed
      full-duplex, 1000 Mb/s
      Auto-Negotiation is turned on
      Auto-mdix is turned off
      EtherType is 0x0000 
      1 minute input rate 0 bits/sec, 0 packets/sec
      1 minute output rate 24 bits/sec, 0 packets/sec
      Rx
        2 input packets 0 unicast packets 2 multicast packets
        0 broadcast packets 168 bytes
      Tx
        22 output packets 0 unicast packets 18 multicast packets
        4 broadcast packets 4726 bytes

    Ethernet2/1 is up
    admin state is up, Dedicated Interface
      Hardware: 10/100/1000 Ethernet, address: aaaa.bbbb.cccc (bia 5254.003b.4aca)
      Description: desc
      Internet Address is 10.4.4.4/24 secondary tag 10
      MTU 1600 bytes, BW 768 Kbit, DLY 3330 usec
      reliability 255/255, txload 1/255, rxload 1/255
      Encapsulation ARPA, medium is broadcast
      Port mode is routed
      full-duplex, 1000 Mb/s
      Beacon is turned off
      Auto-Negotiation is turned off
      Input flow-control is off, output flow-control is off
      Auto-mdix is turned off
      Switchport monitor is off 
      EtherType is 0x8100 
      EEE (efficient-ethernet) : n/a
      Last link flapped 00:00:29
      Last clearing of "show interface" counters never
      1 interface resets
      Load-Interval #1: 0 seconds
        0 seconds input rate 0 bits/sec, 0 packets/sec
        0 seconds output rate 0 bits/sec, 0 packets/sec
        input rate 0 bps, 0 pps; output rate 0 bps, 0 pps
      Load-Interval #2: 0 seconds
        0 seconds input rate 0 bits/sec, 0 packets/sec
        0 seconds output rate 0 bits/sec, 0 packets/sec
        input rate 0 bps, 0 pps; output rate 0 bps, 0 pps
      RX
        0 unicast packets  0 multicast packets  0 broadcast packets
        0 input packets  0 bytes
        0 jumbo packets  0 storm suppression packets
        0 runts  0 giants  0 CRC/FCS  0 no buffer
        0 input error  0 short frame  0 overrun   0 underrun  0 ignored
        0 watchdog  0 bad etype drop  0 bad proto drop  0 if down drop
        0 input with dribble  0 input discard
        0 Rx pause
      TX
        0 unicast packets  0 multicast packets  0 broadcast packets
        0 output packets  0 bytes
        0 jumbo packets
        0 output error  0 collision  0 deferred  0 late collision
        0 lost carrier  0 no carrier  0 babble  0 output discard
        0 Tx pause

    Ethernet2/1.10 is down (Administratively down)
    admin state is down, Dedicated Interface, [parent interface is Ethernet2/1]
      Hardware: 10/100/1000 Ethernet, address: 5254.003b.4af8 (bia 5254.003b.4aca)
      MTU 1600 bytes, BW 768 Kbit, DLY 10 usec
      reliability 255/255, txload 1/255, rxload 1/255
      Encapsulation 802.1Q Virtual LAN, Vlan ID 10, medium is broadcast
      Port mode is routed
      Auto-mdix is turned off
      EtherType is 0x8100 

    Ethernet2/1.20 is up
    admin state is up, Dedicated Interface, [parent interface is Ethernet2/1]
      Hardware: 10/100/1000 Ethernet, address: 5254.003b.4af8 (bia 5254.003b.4aca)
      MTU 1600 bytes, BW 768 Kbit, DLY 10 usec
      reliability 255/255, txload 1/255, rxload 1/255
      Encapsulation 802.1Q Virtual LAN, Vlan ID 20, medium is p2p
      Port mode is routed
      Auto-mdix is turned off
      EtherType is 0x8100 

    Ethernet2/2 is up
    admin state is up, Dedicated Interface
      Hardware: 10/100/1000 Ethernet, address: 5254.00ac.b52e (bia 5254.00ac.b52e)
      MTU 1500 bytes, BW 1000000 Kbit, DLY 10 usec
      reliability 255/255, txload 1/255, rxload 1/255
      Encapsulation ARPA, medium is broadcast
      Port mode is trunk
      full-duplex, 1000 Mb/s
      Beacon is turned off
      Auto-Negotiation is turned off
      Input flow-control is off, output flow-control is off
      Auto-mdix is turned off
      Switchport monitor is off 
      EtherType is 0x8100 
      EEE (efficient-ethernet) : n/a
      Last link flapped 00:07:28
      Last clearing of "show interface" counters never
      1 interface resets
      Load-Interval #1: 0 seconds
        0 seconds input rate 0 bits/sec, 0 packets/sec
        0 seconds output rate 0 bits/sec, 0 packets/sec
        input rate 0 bps, 0 pps; output rate 0 bps, 0 pps
      Load-Interval #2: 0 seconds
        0 seconds input rate 0 bits/sec, 0 packets/sec
        0 seconds output rate 0 bits/sec, 0 packets/sec
        input rate 0 bps, 0 pps; output rate 0 bps, 0 pps
      RX
        0 unicast packets  0 multicast packets  0 broadcast packets
        0 input packets  0 bytes
        0 jumbo packets  0 storm suppression packets
        0 runts  0 giants  0 CRC/FCS  0 no buffer
        0 input error  0 short frame  0 overrun   0 underrun  0 ignored
        0 watchdog  0 bad etype drop  0 bad proto drop  0 if down drop
        0 input with dribble  0 input discard
        0 Rx pause
      TX
        0 unicast packets  0 multicast packets  0 broadcast packets
        0 output packets  0 bytes
        0 jumbo packets
        0 output error  0 collision  0 deferred  0 late collision
        0 lost carrier  0 no carrier  0 babble  0 output discard
        0 Tx pause


        '''}

    def test_empty(self):
        self.device1 = Mock(**self.empty_output)
        interface_obj = ShowInterface(device=self.device1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = interface_obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        interface_obj = ShowInterface(device=self.device)
        parsed_output = interface_obj.parse()
        self.maxDiff = None
        self.assertEqual(parsed_output,self.golden_parsed_output)

if __name__ == '__main__':
    unittest.main()