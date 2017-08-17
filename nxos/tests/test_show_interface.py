import re
import unittest
from unittest.mock import Mock

from ats.topology import Device

from metaparser.util.exceptions import SchemaEmptyParserError, \
                                       SchemaMissingKeyError

from parser.nxos.show_interface import ShowInterface, ShowVrfAllInterface, \
                                       ShowInterfaceSwitchport, ShowIpv6InterfaceVrfAll, \
                                       ShowIpInterfaceVrfAll, \
                                       ShowIpInterfaceBrief, \
                                       ShowIpInterfaceBriefPipeVlan, \
                                       ShowInterfaceBrief

#############################################################################
# unitest For Show Interface
#############################################################################

class test_show_interface(unittest.TestCase):
    device = Device(name='aDevice')
    device0 = Device(name='bDevice')
    empty_output = {'execute.return_value': ''}
    golden_parsed_output = {'Ethernet2/1': {'auto_mdix': 'off',
                 'auto_negotiate': False,
                 'bandwidth': 768,
                 'beacon': 'off',
                 'counters': {'in_bad_etype_drop': 0,
                              'in_broadcast_pkts': 0,
                              'in_crc_errors': 0,
                              'in_discard': 0,
                              'in_errors': 0,
                              'in_if_down_drop': 0,
                              'in_ignored': 0,
                              'in_jumbo_packets': 0,
                              'in_mac_pause_frames': 0,
                              'in_multicast_pkts': 0,
                              'in_no_buffer': 0,
                              'in_octets': 0,
                              'in_overrun': 0,
                              'in_oversize_frame': 0,
                              'in_pkts': 0,
                              'in_runts': 0,
                              'in_short_frame': 0,
                              'in_storm_suppression_packets': 0,
                              'in_underrun': 0,
                              'in_unicast_pkts': 0,
                              'in_unknown_protos': 0,
                              'in_watchdog': 0,
                              'in_with_dribble': 0,
                              'last_clear': 'never',
                              'out_babble': 0,
                              'out_broadcast_pkts': 0,
                              'out_collision': 0,
                              'out_deferred': 0,
                              'out_discard': 0,
                              'out_errors': 0,
                              'out_jumbo_packets': 0,
                              'out_late_collision': 0,
                              'out_lost_carrier': 0,
                              'out_mac_pause_frames': 0,
                              'out_multicast_pkts': 0,
                              'out_no_carrier': 0,
                              'out_octets': 0,
                              'out_pkts': 0,
                              'out_unicast_pkts': 0,
                              'rate': {'in_rate': 0,
                                       'in_rate_bps': 0,
                                       'in_rate_pkts': 0,
                                       'in_rate_pps': 0,
                                       'load_interval': 0,
                                       'out_rate': 0,
                                       'out_rate_bps': 0,
                                       'out_rate_pkts': 0,
                                       'out_rate_pps': 0},
                              'rx': True,
                              'tx': True},
                 'delay': 3330,
                 'description': 'desc',
                 'duplex_mode': 'full',
                 'efficient_ethernet': 'n/a',
                 'enabled': True,
                 'encapsulations': {'encapsulation': 'arpa'},
                 'ethertype': '0x8100',
                 'flow_control': {'receive': False, 'send': False},
                 'interface_reset': 1,
                 'ipv4': {'10.4.4.4/24': {'ip': '10.4.4.4',
                                          'prefix_length': '24',
                                          'route_tag': '10',
                                          'secondary': True}},
                 'last_link_flapped': '00:00:29',
                 'mac_address': 'aaaa.bbbb.cccc',
                 'medium': 'broadcast',
                 'mtu': 1600,
                 'oper_status': 'up',
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
                    'encapsulations': {'encapsulation': 'dot1q',
                                       'first_dot1q': '10'},
                    'ethertype': '0x8100',
                    'link_state': 'Administratively down',
                    'mac_address': '5254.003b.4af8',
                    'medium': 'broadcast',
                    'mtu': 1600,
                    'oper_status': 'down',
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
                    'encapsulations': {'encapsulation': 'dot1q',
                                       'first_dot1q': '20'},
                    'ethertype': '0x8100',
                    'mac_address': '5254.003b.4af8',
                    'medium': 'p2p',
                    'mtu': 1600,
                    'oper_status': 'up',
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
                              'in_broadcast_pkts': 0,
                              'in_crc_errors': 0,
                              'in_discard': 0,
                              'in_errors': 0,
                              'in_if_down_drop': 0,
                              'in_ignored': 0,
                              'in_jumbo_packets': 0,
                              'in_mac_pause_frames': 0,
                              'in_multicast_pkts': 0,
                              'in_no_buffer': 0,
                              'in_octets': 0,
                              'in_overrun': 0,
                              'in_oversize_frame': 0,
                              'in_pkts': 0,
                              'in_runts': 0,
                              'in_short_frame': 0,
                              'in_storm_suppression_packets': 0,
                              'in_underrun': 0,
                              'in_unicast_pkts': 0,
                              'in_unknown_protos': 0,
                              'in_watchdog': 0,
                              'in_with_dribble': 0,
                              'last_clear': 'never',
                              'out_babble': 0,
                              'out_broadcast_pkts': 0,
                              'out_collision': 0,
                              'out_deferred': 0,
                              'out_discard': 0,
                              'out_errors': 0,
                              'out_jumbo_packets': 0,
                              'out_late_collision': 0,
                              'out_lost_carrier': 0,
                              'out_mac_pause_frames': 0,
                              'out_multicast_pkts': 0,
                              'out_no_carrier': 0,
                              'out_octets': 0,
                              'out_pkts': 0,
                              'out_unicast_pkts': 0,
                              'rate': {'in_rate': 0,
                                       'in_rate_bps': 0,
                                       'in_rate_pkts': 0,
                                       'in_rate_pps': 0,
                                       'load_interval': 0,
                                       'out_rate': 0,
                                       'out_rate_bps': 0,
                                       'out_rate_pkts': 0,
                                       'out_rate_pps': 0},
                              'rx': True,
                              'tx': True},
                 'delay': 10,
                 'duplex_mode': 'full',
                 'efficient_ethernet': 'n/a',
                 'enabled': True,
                 'encapsulations': {'encapsulation': 'arpa'},
                 'ethertype': '0x8100',
                 'flow_control': {'receive': False, 'send': False},
                 'interface_reset': 1,
                 'last_link_flapped': '00:07:28',
                 'mac_address': '5254.00ac.b52e',
                 'medium': 'broadcast',
                 'mtu': 1500,
                 'oper_status': 'up',
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
           'duplex_mode': 'full',
           'enabled': True,
           'encapsulations': {'encapsulation': 'arpa'},
           'ethertype': '0x0000',
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
           'types': 'Ethernet'}}

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


# #############################################################################
# # Unitest For Show Ip Interface Vrf All
# #############################################################################

class test_show_ip_interface_vrf_all(unittest.TestCase):
    
    device = Device(name='aDevice')
    device0 = Device(name='bDevice')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output = {'Ethernet2/1': {'directed_broadcast': 'disabled',
                 'icmp_port_unreachable': 'enabled',
                 'icmp_redirects': 'disabled',
                 'icmp_unreachable': 'disabled',
                 'int_stat_last_reset': 'never',
                 'interface_status': 'protocol-up/link-up/admin-up',
                 'iod': 36,
                 'ip_forwarding': 'disabled',
                 'ip_mtu': 1600,
                 'ipv4': {'10.2.2.2/24': {'ip': '10.2.2.2',
                                          'ip_subnet': '10.2.2.0',
                                          'prefix_length': '24',
                                          'secondary': True},
                          '10.3.3.3/24': {'broadcast_address': '255.255.255.255',
                                          'ip': '10.3.3.3',
                                          'ip_subnet': '10.3.3.0',
                                          'prefix_length': '24',
                                          'route_preference': '0',
                                          'route_tag': '0',
                                          'secondary': True},
                          '10.4.4.4/24': {'ip': '10.4.4.4',
                                          'ip_subnet': '10.4.4.0',
                                          'prefix_length': '24',},           
                          'unnumbered':{'interface_ref': 'loopback0'},
                          'counters': {'broadcast_bytes_consumed': 0,
                                       'broadcast_bytes_forwarded': 0,
                                       'broadcast_bytes_originated': 0,
                                       'broadcast_bytes_received': 0,
                                       'broadcast_bytes_sent': 0,
                                       'broadcast_packets_consumed': 0,
                                       'broadcast_packets_forwarded': 0,
                                       'broadcast_packets_originated': 0,
                                       'broadcast_packets_received': 0,
                                       'broadcast_packets_sent': 0,
                                       'labeled_bytes_consumed': 0,
                                       'labeled_bytes_forwarded': 0,
                                       'labeled_bytes_originated': 0,
                                       'labeled_bytes_received': 0,
                                       'labeled_bytes_sent': 0,
                                       'labeled_packets_consumed': 0,
                                       'labeled_packets_forwarded': 0,
                                       'labeled_packets_originated': 0,
                                       'labeled_packets_received': 0,
                                       'labeled_packets_sent': 0,
                                       'multicast_bytes_consumed': 0,
                                       'multicast_bytes_forwarded': 0,
                                       'multicast_bytes_originated': 0,
                                       'multicast_bytes_received': 0,
                                       'multicast_bytes_sent': 0,
                                       'multicast_packets_consumed': 0,
                                       'multicast_packets_forwarded': 0,
                                       'multicast_packets_originated': 0,
                                       'multicast_packets_received': 0,
                                       'multicast_packets_sent': 0,
                                       'unicast_bytes_consumed': 0,
                                       'unicast_bytes_forwarded': 0,
                                       'unicast_bytes_originated': 0,
                                       'unicast_bytes_received': 0,
                                       'unicast_bytes_sent': 0,
                                       'unicast_packets_consumed': 0,
                                       'unicast_packets_forwarded': 0,
                                       'unicast_packets_originated': 0,
                                       'unicast_packets_received': 0,
                                       'unicast_packets_sent': 0}},
                 'load_sharing': 'none',
                 'local_proxy_arp': 'disabled',
                 'multicast_groups': ['224.0.0.6', '224.0.0.5', '224.0.0.2'],
                 'multicast_routing': 'disabled',
                 'proxy_arp': 'disabled',
                 'unicast_reverse_path': 'none',
                 'vrf': 'VRF1',
                 'wccp_redirect_exclude': 'disabled',
                 'wccp_redirect_inbound': 'disabled',
                 'wccp_redirect_outbound': 'disabled'}}


    golden_output = {'execute.return_value': '''
        IP Interface Status for VRF "default"

        IP Interface Status for VRF "management"

        IP Interface Status for VRF "VRF1"
        Ethernet2/1, Interface status: protocol-up/link-up/admin-up, iod: 36,
          IP address: 10.4.4.4, IP subnet: 10.4.4.0/24
          IP address: 10.2.2.2, IP subnet: 10.2.2.0/24 secondary
          IP address: 10.3.3.3, IP subnet: 10.3.3.0/24 secondary
          IP broadcast address: 255.255.255.255
          IP multicast groups locally joined: 
             224.0.0.6  224.0.0.5  224.0.0.2
          IP MTU: 1600 bytes (using link MTU)
          IP primary address route-preference: 0, tag: 0
          IP unnumbered interface (loopback0)
          IP proxy ARP : disabled
          IP Local Proxy ARP : disabled
          IP multicast routing: disabled
          IP icmp redirects: disabled
          IP directed-broadcast: disabled 
          IP Forwarding: disabled 
          IP icmp unreachables (except port): disabled
          IP icmp port-unreachable: enabled
          IP unicast reverse path forwarding: none
          IP load sharing: none 
          IP interface statistics last reset: never
          IP interface software stats: (sent/received/forwarded/originated/consumed)
            Unicast packets    : 0/0/0/0/0
            Unicast bytes      : 0/0/0/0/0
            Multicast packets  : 0/0/0/0/0
            Multicast bytes    : 0/0/0/0/0
            Broadcast packets  : 0/0/0/0/0
            Broadcast bytes    : 0/0/0/0/0
            Labeled packets    : 0/0/0/0/0
            Labeled bytes      : 0/0/0/0/0
          WCCP Redirect outbound: disabled
          WCCP Redirect inbound: disabled
          WCCP Redirect exclude: disabled
      '''}


    def test_empty(self):
        self.device1 = Mock(**self.empty_output)
        ip_interface_vrf_all_obj = ShowIpInterfaceVrfAll(device=self.device1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = ip_interface_vrf_all_obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        ip_interface_vrf_all_obj = ShowIpInterfaceVrfAll(device=self.device)
        parsed_output = ip_interface_vrf_all_obj.parse()
        self.maxDiff = None
        self.assertEqual(parsed_output,self.golden_parsed_output)


# #############################################################################
# # Unitest For Show Vrf All Interface
# #############################################################################

class test_show_vrf_all_interface(unittest.TestCase):
    
    device = Device(name='aDevice')
    device0 = Device(name='bDevice')
    empty_output = {'execute.return_value': ''}
    golden_parsed_output = {'Ethernet2/1': {'site_of_origin': '--', 'vrf': 'VRF1', 'vrf_id': 3},
 'Ethernet2/1.10': {'site_of_origin': '--', 'vrf': 'default', 'vrf_id': 1},
 'Ethernet2/1.20': {'site_of_origin': '--', 'vrf': 'default', 'vrf_id': 1},
 'Ethernet2/10': {'site_of_origin': '--', 'vrf': 'default', 'vrf_id': 1},
 'Ethernet2/11': {'site_of_origin': '--', 'vrf': 'default', 'vrf_id': 1},
 'Ethernet2/12': {'site_of_origin': '--', 'vrf': 'default', 'vrf_id': 1},
 'Ethernet2/13': {'site_of_origin': '--', 'vrf': 'default', 'vrf_id': 1},
 'Ethernet2/14': {'site_of_origin': '--', 'vrf': 'default', 'vrf_id': 1},
 'Ethernet2/15': {'site_of_origin': '--', 'vrf': 'default', 'vrf_id': 1},
 'Ethernet2/16': {'site_of_origin': '--', 'vrf': 'default', 'vrf_id': 1},
 'Ethernet2/17': {'site_of_origin': '--', 'vrf': 'default', 'vrf_id': 1},
 'Ethernet2/18': {'site_of_origin': '--', 'vrf': 'default', 'vrf_id': 1},
 'Ethernet2/19': {'site_of_origin': '--', 'vrf': 'default', 'vrf_id': 1},
 'Ethernet2/20': {'site_of_origin': '--', 'vrf': 'default', 'vrf_id': 1},
 'Ethernet2/21': {'site_of_origin': '--', 'vrf': 'default', 'vrf_id': 1},
 'Ethernet2/22': {'site_of_origin': '--', 'vrf': 'default', 'vrf_id': 1},
 'Ethernet2/23': {'site_of_origin': '--', 'vrf': 'default', 'vrf_id': 1},
 'Ethernet2/24': {'site_of_origin': '--', 'vrf': 'default', 'vrf_id': 1},
 'Ethernet2/25': {'site_of_origin': '--', 'vrf': 'default', 'vrf_id': 1},
 'Ethernet2/26': {'site_of_origin': '--', 'vrf': 'default', 'vrf_id': 1},
 'Ethernet2/27': {'site_of_origin': '--', 'vrf': 'default', 'vrf_id': 1},
 'Ethernet2/28': {'site_of_origin': '--', 'vrf': 'default', 'vrf_id': 1},
 'Ethernet2/29': {'site_of_origin': '--', 'vrf': 'default', 'vrf_id': 1},
 'Ethernet2/30': {'site_of_origin': '--', 'vrf': 'default', 'vrf_id': 1},
 'Ethernet2/31': {'site_of_origin': '--', 'vrf': 'default', 'vrf_id': 1},
 'Ethernet2/32': {'site_of_origin': '--', 'vrf': 'default', 'vrf_id': 1},
 'Ethernet2/33': {'site_of_origin': '--', 'vrf': 'default', 'vrf_id': 1},
 'Ethernet2/34': {'site_of_origin': '--', 'vrf': 'default', 'vrf_id': 1},
 'Ethernet2/35': {'site_of_origin': '--', 'vrf': 'default', 'vrf_id': 1},
 'Ethernet2/36': {'site_of_origin': '--', 'vrf': 'default', 'vrf_id': 1},
 'Ethernet2/37': {'site_of_origin': '--', 'vrf': 'default', 'vrf_id': 1},
 'Ethernet2/38': {'site_of_origin': '--', 'vrf': 'default', 'vrf_id': 1},
 'Ethernet2/39': {'site_of_origin': '--', 'vrf': 'default', 'vrf_id': 1},
 'Ethernet2/4': {'site_of_origin': '--', 'vrf': 'default', 'vrf_id': 1},
 'Ethernet2/40': {'site_of_origin': '--', 'vrf': 'default', 'vrf_id': 1},
 'Ethernet2/41': {'site_of_origin': '--', 'vrf': 'default', 'vrf_id': 1},
 'Ethernet2/42': {'site_of_origin': '--', 'vrf': 'default', 'vrf_id': 1},
 'Ethernet2/43': {'site_of_origin': '--', 'vrf': 'default', 'vrf_id': 1},
 'Ethernet2/44': {'site_of_origin': '--', 'vrf': 'default', 'vrf_id': 1},
 'Ethernet2/45': {'site_of_origin': '--', 'vrf': 'default', 'vrf_id': 1},
 'Ethernet2/46': {'site_of_origin': '--', 'vrf': 'default', 'vrf_id': 1},
 'Ethernet2/47': {'site_of_origin': '--', 'vrf': 'default', 'vrf_id': 1},
 'Ethernet2/48': {'site_of_origin': '--', 'vrf': 'default', 'vrf_id': 1},
 'Ethernet2/5': {'site_of_origin': '--', 'vrf': 'default', 'vrf_id': 1},
 'Ethernet2/6': {'site_of_origin': '--', 'vrf': 'default', 'vrf_id': 1},
 'Ethernet2/7': {'site_of_origin': '--', 'vrf': 'default', 'vrf_id': 1},
 'Ethernet2/8': {'site_of_origin': '--', 'vrf': 'default', 'vrf_id': 1},
 'Ethernet2/9': {'site_of_origin': '--', 'vrf': 'default', 'vrf_id': 1},
 'Ethernet3/1': {'site_of_origin': '--', 'vrf': 'default', 'vrf_id': 1},
 'Ethernet3/10': {'site_of_origin': '--', 'vrf': 'default', 'vrf_id': 1},
 'Ethernet3/11': {'site_of_origin': '--', 'vrf': 'default', 'vrf_id': 1},
 'Ethernet3/12': {'site_of_origin': '--', 'vrf': 'default', 'vrf_id': 1},
 'Ethernet3/13': {'site_of_origin': '--', 'vrf': 'default', 'vrf_id': 1},
 'Ethernet3/14': {'site_of_origin': '--', 'vrf': 'default', 'vrf_id': 1},
 'Ethernet3/15': {'site_of_origin': '--', 'vrf': 'default', 'vrf_id': 1},
 'Ethernet3/16': {'site_of_origin': '--', 'vrf': 'default', 'vrf_id': 1},
 'Ethernet3/17': {'site_of_origin': '--', 'vrf': 'default', 'vrf_id': 1},
 'Ethernet3/18': {'site_of_origin': '--', 'vrf': 'default', 'vrf_id': 1},
 'Ethernet3/19': {'site_of_origin': '--', 'vrf': 'default', 'vrf_id': 1},
 'Ethernet3/2': {'site_of_origin': '--', 'vrf': 'default', 'vrf_id': 1},
 'Ethernet3/20': {'site_of_origin': '--', 'vrf': 'default', 'vrf_id': 1},
 'Ethernet3/21': {'site_of_origin': '--', 'vrf': 'default', 'vrf_id': 1},
 'Ethernet3/22': {'site_of_origin': '--', 'vrf': 'default', 'vrf_id': 1},
 'Ethernet3/23': {'site_of_origin': '--', 'vrf': 'default', 'vrf_id': 1},
 'Ethernet3/24': {'site_of_origin': '--', 'vrf': 'default', 'vrf_id': 1},
 'Ethernet3/25': {'site_of_origin': '--', 'vrf': 'default', 'vrf_id': 1},
 'Ethernet3/26': {'site_of_origin': '--', 'vrf': 'default', 'vrf_id': 1},
 'Ethernet3/27': {'site_of_origin': '--', 'vrf': 'default', 'vrf_id': 1},
 'Ethernet3/28': {'site_of_origin': '--', 'vrf': 'default', 'vrf_id': 1},
 'Ethernet3/29': {'site_of_origin': '--', 'vrf': 'default', 'vrf_id': 1},
 'Ethernet3/3': {'site_of_origin': '--', 'vrf': 'default', 'vrf_id': 1},
 'Ethernet3/30': {'site_of_origin': '--', 'vrf': 'default', 'vrf_id': 1},
 'Ethernet3/31': {'site_of_origin': '--', 'vrf': 'default', 'vrf_id': 1},
 'Ethernet3/32': {'site_of_origin': '--', 'vrf': 'default', 'vrf_id': 1},
 'Ethernet3/33': {'site_of_origin': '--', 'vrf': 'default', 'vrf_id': 1},
 'Ethernet3/34': {'site_of_origin': '--', 'vrf': 'default', 'vrf_id': 1},
 'Ethernet3/35': {'site_of_origin': '--', 'vrf': 'default', 'vrf_id': 1},
 'Ethernet3/36': {'site_of_origin': '--', 'vrf': 'default', 'vrf_id': 1},
 'Ethernet3/37': {'site_of_origin': '--', 'vrf': 'default', 'vrf_id': 1},
 'Ethernet3/38': {'site_of_origin': '--', 'vrf': 'default', 'vrf_id': 1},
 'Ethernet3/39': {'site_of_origin': '--', 'vrf': 'default', 'vrf_id': 1},
 'Ethernet3/4': {'site_of_origin': '--', 'vrf': 'default', 'vrf_id': 1},
 'Ethernet3/40': {'site_of_origin': '--', 'vrf': 'default', 'vrf_id': 1},
 'Ethernet3/41': {'site_of_origin': '--', 'vrf': 'default', 'vrf_id': 1},
 'Ethernet3/42': {'site_of_origin': '--', 'vrf': 'default', 'vrf_id': 1},
 'Ethernet3/43': {'site_of_origin': '--', 'vrf': 'default', 'vrf_id': 1},
 'Ethernet3/44': {'site_of_origin': '--', 'vrf': 'default', 'vrf_id': 1},
 'Ethernet3/45': {'site_of_origin': '--', 'vrf': 'default', 'vrf_id': 1},
 'Ethernet3/46': {'site_of_origin': '--', 'vrf': 'default', 'vrf_id': 1},
 'Ethernet3/47': {'site_of_origin': '--', 'vrf': 'default', 'vrf_id': 1},
 'Ethernet3/48': {'site_of_origin': '--', 'vrf': 'default', 'vrf_id': 1},
 'Ethernet3/5': {'site_of_origin': '--', 'vrf': 'default', 'vrf_id': 1},
 'Ethernet3/6': {'site_of_origin': '--', 'vrf': 'default', 'vrf_id': 1},
 'Ethernet3/7': {'site_of_origin': '--', 'vrf': 'default', 'vrf_id': 1},
 'Ethernet3/8': {'site_of_origin': '--', 'vrf': 'default', 'vrf_id': 1},
 'Ethernet3/9': {'site_of_origin': '--', 'vrf': 'default', 'vrf_id': 1},
 'Ethernet4/1': {'site_of_origin': '--', 'vrf': 'default', 'vrf_id': 1},
 'Ethernet4/10': {'site_of_origin': '--', 'vrf': 'default', 'vrf_id': 1},
 'Ethernet4/11': {'site_of_origin': '--', 'vrf': 'default', 'vrf_id': 1},
 'Ethernet4/12': {'site_of_origin': '--', 'vrf': 'default', 'vrf_id': 1},
 'Ethernet4/13': {'site_of_origin': '--', 'vrf': 'default', 'vrf_id': 1},
 'Ethernet4/14': {'site_of_origin': '--', 'vrf': 'default', 'vrf_id': 1},
 'Ethernet4/15': {'site_of_origin': '--', 'vrf': 'default', 'vrf_id': 1},
 'Ethernet4/16': {'site_of_origin': '--', 'vrf': 'default', 'vrf_id': 1},
 'Ethernet4/17': {'site_of_origin': '--', 'vrf': 'default', 'vrf_id': 1},
 'Ethernet4/18': {'site_of_origin': '--', 'vrf': 'default', 'vrf_id': 1},
 'Ethernet4/19': {'site_of_origin': '--', 'vrf': 'default', 'vrf_id': 1},
 'Ethernet4/2': {'site_of_origin': '--', 'vrf': 'default', 'vrf_id': 1},
 'Ethernet4/20': {'site_of_origin': '--', 'vrf': 'default', 'vrf_id': 1},
 'Ethernet4/21': {'site_of_origin': '--', 'vrf': 'default', 'vrf_id': 1},
 'Ethernet4/22': {'site_of_origin': '--', 'vrf': 'default', 'vrf_id': 1},
 'Ethernet4/23': {'site_of_origin': '--', 'vrf': 'default', 'vrf_id': 1},
 'Ethernet4/24': {'site_of_origin': '--', 'vrf': 'default', 'vrf_id': 1},
 'Ethernet4/25': {'site_of_origin': '--', 'vrf': 'default', 'vrf_id': 1},
 'Ethernet4/26': {'site_of_origin': '--', 'vrf': 'default', 'vrf_id': 1},
 'Ethernet4/27': {'site_of_origin': '--', 'vrf': 'default', 'vrf_id': 1},
 'Ethernet4/28': {'site_of_origin': '--', 'vrf': 'default', 'vrf_id': 1},
 'Ethernet4/29': {'site_of_origin': '--', 'vrf': 'default', 'vrf_id': 1},
 'Ethernet4/3': {'site_of_origin': '--', 'vrf': 'default', 'vrf_id': 1},
 'Ethernet4/30': {'site_of_origin': '--', 'vrf': 'default', 'vrf_id': 1},
 'Ethernet4/31': {'site_of_origin': '--', 'vrf': 'default', 'vrf_id': 1},
 'Ethernet4/32': {'site_of_origin': '--', 'vrf': 'default', 'vrf_id': 1},
 'Ethernet4/33': {'site_of_origin': '--', 'vrf': 'default', 'vrf_id': 1},
 'Ethernet4/34': {'site_of_origin': '--', 'vrf': 'default', 'vrf_id': 1},
 'Ethernet4/35': {'site_of_origin': '--', 'vrf': 'default', 'vrf_id': 1},
 'Ethernet4/36': {'site_of_origin': '--', 'vrf': 'default', 'vrf_id': 1},
 'Ethernet4/37': {'site_of_origin': '--', 'vrf': 'default', 'vrf_id': 1},
 'Ethernet4/38': {'site_of_origin': '--', 'vrf': 'default', 'vrf_id': 1},
 'Ethernet4/39': {'site_of_origin': '--', 'vrf': 'default', 'vrf_id': 1},
 'Ethernet4/4': {'site_of_origin': '--', 'vrf': 'default', 'vrf_id': 1},
 'Ethernet4/40': {'site_of_origin': '--', 'vrf': 'default', 'vrf_id': 1},
 'Ethernet4/41': {'site_of_origin': '--', 'vrf': 'default', 'vrf_id': 1},
 'Ethernet4/42': {'site_of_origin': '--', 'vrf': 'default', 'vrf_id': 1},
 'Ethernet4/43': {'site_of_origin': '--', 'vrf': 'default', 'vrf_id': 1},
 'Ethernet4/44': {'site_of_origin': '--', 'vrf': 'default', 'vrf_id': 1},
 'Ethernet4/45': {'site_of_origin': '--', 'vrf': 'default', 'vrf_id': 1},
 'Ethernet4/46': {'site_of_origin': '--', 'vrf': 'default', 'vrf_id': 1},
 'Ethernet4/47': {'site_of_origin': '--', 'vrf': 'default', 'vrf_id': 1},
 'Ethernet4/48': {'site_of_origin': '--', 'vrf': 'default', 'vrf_id': 1},
 'Ethernet4/5': {'site_of_origin': '--', 'vrf': 'default', 'vrf_id': 1},
 'Ethernet4/6': {'site_of_origin': '--', 'vrf': 'default', 'vrf_id': 1},
 'Ethernet4/7': {'site_of_origin': '--', 'vrf': 'default', 'vrf_id': 1},
 'Ethernet4/8': {'site_of_origin': '--', 'vrf': 'default', 'vrf_id': 1},
 'Ethernet4/9': {'site_of_origin': '--', 'vrf': 'default', 'vrf_id': 1},
 'Null0': {'site_of_origin': '--', 'vrf': 'default', 'vrf_id': 1},
 'mgmt0': {'site_of_origin': '--', 'vrf': 'management', 'vrf_id': 2}}


    golden_output = {'execute.return_value': '''
       
    Interface                 VRF-Name                        VRF-ID  Site-of-Origin
    Ethernet2/1               VRF1                                 3  --
    Null0                     default                              1  --
    Ethernet2/1.10            default                              1  --
    Ethernet2/1.20            default                              1  --
    Ethernet2/4               default                              1  --
    Ethernet2/5               default                              1  --
    Ethernet2/6               default                              1  --
    Ethernet2/7               default                              1  --
    Ethernet2/8               default                              1  --
    Ethernet2/9               default                              1  --
    Ethernet2/10              default                              1  --
    Ethernet2/11              default                              1  --
    Ethernet2/12              default                              1  --
    Ethernet2/13              default                              1  --
    Ethernet2/14              default                              1  --
    Ethernet2/15              default                              1  --
    Ethernet2/16              default                              1  --
    Ethernet2/17              default                              1  --
    Ethernet2/18              default                              1  --
    Ethernet2/19              default                              1  --
    Ethernet2/20              default                              1  --
    Ethernet2/21              default                              1  --
    Ethernet2/22              default                              1  --
    Ethernet2/23              default                              1  --
    Ethernet2/24              default                              1  --
    Ethernet2/25              default                              1  --
    Ethernet2/26              default                              1  --
    Ethernet2/27              default                              1  --
    Ethernet2/28              default                              1  --
    Ethernet2/29              default                              1  --
    Ethernet2/30              default                              1  --
    Ethernet2/31              default                              1  --
    Ethernet2/32              default                              1  --
    Ethernet2/33              default                              1  --
    Ethernet2/34              default                              1  --
    Ethernet2/35              default                              1  --
    Ethernet2/36              default                              1  --
    Ethernet2/37              default                              1  --
    Ethernet2/38              default                              1  --
    Ethernet2/39              default                              1  --
    Ethernet2/40              default                              1  --
    Ethernet2/41              default                              1  --
    Ethernet2/42              default                              1  --
    Ethernet2/43              default                              1  --
    Ethernet2/44              default                              1  --
    Ethernet2/45              default                              1  --
    Ethernet2/46              default                              1  --
    Ethernet2/47              default                              1  --
    Ethernet2/48              default                              1  --
    Ethernet3/1               default                              1  --
    Ethernet3/2               default                              1  --
    Ethernet3/3               default                              1  --
    Ethernet3/4               default                              1  --
    Ethernet3/5               default                              1  --
    Ethernet3/6               default                              1  --
    Ethernet3/7               default                              1  --
    Ethernet3/8               default                              1  --
    Ethernet3/9               default                              1  --
    Ethernet3/10              default                              1  --
    Ethernet3/11              default                              1  --
    Ethernet3/12              default                              1  --
    Ethernet3/13              default                              1  --
    Ethernet3/14              default                              1  --
    Ethernet3/15              default                              1  --
    Ethernet3/16              default                              1  --
    Ethernet3/17              default                              1  --
    Ethernet3/18              default                              1  --
    Ethernet3/19              default                              1  --
    Ethernet3/20              default                              1  --
    Ethernet3/21              default                              1  --
    Ethernet3/22              default                              1  --
    Ethernet3/23              default                              1  --
    Ethernet3/24              default                              1  --
    Ethernet3/25              default                              1  --
    Ethernet3/26              default                              1  --
    Ethernet3/27              default                              1  --
    Ethernet3/28              default                              1  --
    Ethernet3/29              default                              1  --
    Ethernet3/30              default                              1  --
    Ethernet3/31              default                              1  --
    Ethernet3/32              default                              1  --
    Ethernet3/33              default                              1  --
    Ethernet3/34              default                              1  --
    Ethernet3/35              default                              1  --
    Ethernet3/36              default                              1  --
    Ethernet3/37              default                              1  --
    Ethernet3/38              default                              1  --
    Ethernet3/39              default                              1  --
    Ethernet3/40              default                              1  --
    Ethernet3/41              default                              1  --
    Ethernet3/42              default                              1  --
    Ethernet3/43              default                              1  --
    Ethernet3/44              default                              1  --
    Ethernet3/45              default                              1  --
    Ethernet3/46              default                              1  --
    Ethernet3/47              default                              1  --
    Ethernet3/48              default                              1  --
    Ethernet4/1               default                              1  --
    Ethernet4/2               default                              1  --
    Ethernet4/3               default                              1  --
    Ethernet4/4               default                              1  --
    Ethernet4/5               default                              1  --
    Ethernet4/6               default                              1  --
    Ethernet4/7               default                              1  --
    Ethernet4/8               default                              1  --
    Ethernet4/9               default                              1  --
    Ethernet4/10              default                              1  --
    Ethernet4/11              default                              1  --
    Ethernet4/12              default                              1  --
    Ethernet4/13              default                              1  --
    Ethernet4/14              default                              1  --
    Ethernet4/15              default                              1  --
    Ethernet4/16              default                              1  --
    Ethernet4/17              default                              1  --
    Ethernet4/18              default                              1  --
    Ethernet4/19              default                              1  --
    Ethernet4/20              default                              1  --
    Ethernet4/21              default                              1  --
    Ethernet4/22              default                              1  --
    Ethernet4/23              default                              1  --
    Ethernet4/24              default                              1  --
    Ethernet4/25              default                              1  --
    Ethernet4/26              default                              1  --
    Ethernet4/27              default                              1  --
    Ethernet4/28              default                              1  --
    Ethernet4/29              default                              1  --
    Ethernet4/30              default                              1  --
    Ethernet4/31              default                              1  --
    Ethernet4/32              default                              1  --
    Ethernet4/33              default                              1  --
    Ethernet4/34              default                              1  --
    Ethernet4/35              default                              1  --
    Ethernet4/36              default                              1  --
    Ethernet4/37              default                              1  --
    Ethernet4/38              default                              1  --
    Ethernet4/39              default                              1  --
    Ethernet4/40              default                              1  --
    Ethernet4/41              default                              1  --
    Ethernet4/42              default                              1  --
    Ethernet4/43              default                              1  --
    Ethernet4/44              default                              1  --
    Ethernet4/45              default                              1  --
    Ethernet4/46              default                              1  --
    Ethernet4/47              default                              1  --
    Ethernet4/48              default                              1  --
    mgmt0                     management                           2  --

        '''}

    def test_empty(self):
        self.device1 = Mock(**self.empty_output)
        vrf_all_interface_obj = ShowVrfAllInterface(device=self.device1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = vrf_all_interface_obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        vrf_all_interface_obj = ShowVrfAllInterface(device=self.device)
        parsed_output = vrf_all_interface_obj.parse()
        self.maxDiff = None
        self.assertEqual(parsed_output,self.golden_parsed_output)


# #############################################################################
# # unitest For Show Interface Switchport
# #############################################################################


class test_show_interface_switchport(unittest.TestCase):

    device = Device(name='aDevice')
    device0 = Device(name='bDevice')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output = {'Ethernet2/2': {'access_vlan': 1,
                 'access_vlan_mode': 'default',
                 'admin_priv_vlan_primary_host_assoc': 'none',
                 'admin_priv_vlan_primary_mapping': 'none',
                 'admin_priv_vlan_secondary_host_assoc': 'none',
                 'admin_priv_vlan_secondary_mapping': 'none',
                 'admin_priv_vlan_trunk_encapsulation': 'dot1q',
                 'admin_priv_vlan_trunk_native_vlan': 'none',
                 'admin_priv_vlan_trunk_normal_vlans': 'none',
                 'admin_priv_vlan_trunk_private_vlans': 'none',
                 'native_vlan': 1,
                 'native_vlan_mode': 'default',
                 'operational_private_vlan': 'none',
                 'switchport_mode': 'trunk',
                 'switchport_monitor': 'Not enabled',
                 'switchport_status': 'Enabled',
                 'trunk_vlans': '100,300'},
 'Ethernet2/3': {'access_vlan': 100,
                 'access_vlan_mode': 'Vlan not created',
                 'admin_priv_vlan_primary_host_assoc': 'none',
                 'admin_priv_vlan_primary_mapping': 'none',
                 'admin_priv_vlan_secondary_host_assoc': 'none',
                 'admin_priv_vlan_secondary_mapping': 'none',
                 'admin_priv_vlan_trunk_encapsulation': 'dot1q',
                 'admin_priv_vlan_trunk_native_vlan': 'none',
                 'admin_priv_vlan_trunk_normal_vlans': 'none',
                 'admin_priv_vlan_trunk_private_vlans': 'none',
                 'native_vlan': 1,
                 'native_vlan_mode': 'default',
                 'operational_private_vlan': 'none',
                 'switchport_mode': 'access',
                 'switchport_monitor': 'Not enabled',
                 'switchport_status': 'Enabled',
                 'trunk_vlans': '1-4094'}}


    golden_output = {'execute.return_value': '''
    Name: Ethernet2/2
      Switchport: Enabled
      Switchport Monitor: Not enabled 
      Operational Mode: trunk
      Access Mode VLAN: 1 (default)
      Trunking Native Mode VLAN: 1 (default)
      Trunking VLANs Allowed: 100,300
      Administrative private-vlan primary host-association: none
      Administrative private-vlan secondary host-association: none
      Administrative private-vlan primary mapping: none
      Administrative private-vlan secondary mapping: none
      Administrative private-vlan trunk native VLAN: none
      Administrative private-vlan trunk encapsulation: dot1q
      Administrative private-vlan trunk normal VLANs: none
      Administrative private-vlan trunk private VLANs: none
      Operational private-vlan: none
    Name: Ethernet2/3
      Switchport: Enabled
      Switchport Monitor: Not enabled 
      Operational Mode: access
      Access Mode VLAN: 100 (Vlan not created)
      Trunking Native Mode VLAN: 1 (default)
      Trunking VLANs Allowed: 1-4094
      Administrative private-vlan primary host-association: none
      Administrative private-vlan secondary host-association: none
      Administrative private-vlan primary mapping: none
      Administrative private-vlan secondary mapping: none
      Administrative private-vlan trunk native VLAN: none
      Administrative private-vlan trunk encapsulation: dot1q
      Administrative private-vlan trunk normal VLANs: none
      Administrative private-vlan trunk private VLANs: none
      Operational private-vlan: none  
      '''}

    def test_empty(self):
        self.device1 = Mock(**self.empty_output)
        interface_switchport_obj = ShowInterfaceSwitchport(device=self.device1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = interface_switchport_obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        interface_switchport_obj = ShowInterfaceSwitchport(device=self.device)
        parsed_output = interface_switchport_obj.parse()
        self.maxDiff = None
        self.assertEqual(parsed_output,self.golden_parsed_output)


# #############################################################################
# # unitest For Show Ipv6 Interface Vrf All
# #############################################################################


class test_show_ipv6_interface_vrf_all(unittest.TestCase):
    
    device = Device(name='aDevice')
    device0 = Device(name='bDevice')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output = {'Ethernet2/1': {'enabled': True,
                 'interface_status': 'protocol-up/link-up/admin-up',
                 'iod': 36,
                 'ipv6': {'2001:db8:1:1::1/64': {'ip': '2001:db8:1:1::1',
                                                 'prefix_length': '64',
                                                 'status': 'valid'},
                          '2001:db8:2:2::2/64': {'anycast': True,
                                                 'ip': '2001:db8:2:2::2',
                                                 'prefix_length': '64',
                                                 'status': 'valid'},
                          '2001:db8:3:3::3/64': {'ip': '2001:db8:3:3::3',
                                                 'prefix_length': '64',
                                                 'status': 'valid'},
                          '2001:db8:4:4:a8aa:bbff:febb:cccc/64': {'ip': '2001:db8:4:4:a8aa:bbff:febb:cccc',
                                                                  'prefix_length': '64',
                                                                  'status': 'valid'},
                          'counters': {'multicast_bytes_consumed': 640,
                                       'multicast_bytes_forwarded': 0,
                                       'multicast_bytes_originated': 1144,
                                       'multicast_packets_consumed': 9,
                                       'multicast_packets_forwarded': 0,
                                       'multicast_packets_originated': 12,
                                       'unicast_bytes_consumed': 0,
                                       'unicast_bytes_forwarded': 0,
                                       'unicast_bytes_originated': 0,
                                       'unicast_packets_consumed': 0,
                                       'unicast_packets_forwarded': 0,
                                       'unicast_packets_originated': 0},
                          'ipv6_forwarding_feature': 'disabled',
                          'ipv6_last_reset': 'never',
                          'ipv6_link_local': 'fe80::a8aa:bbff:febb:cccc ',
                          'ipv6_link_local_state': 'default',
                          'ipv6_ll_state': 'valid',
                          'ipv6_load_sharing': 'none',
                          'ipv6_mtu': 1600,
                          'ipv6_multicast_entries': 'none',
                          'ipv6_multicast_groups': ['ff02::1:ffbb:cccc',
                                                    'ff02::1:ff00:3',
                                                    'ff02::1:ff00:2',
                                                    'ff02::2',
                                                    'ff02::1',
                                                    'ff02::1:ff00:1',
                                                    'ff02::1:ffbb:cccc',
                                                    'ff02::1:ff00:0'],
                          'ipv6_multicast_routing': 'disabled',
                          'ipv6_report_link_local': 'disabled',
                          'ipv6_subnet': '2001:db8:1:1::/64',
                          'ipv6_unicast_rev_path_forwarding': 'none',
                          'ipv6_virtual_add': 'none',
                          'multicast_groups': True},
                 'vrf': 'VRF1'}}


    golden_output = {'execute.return_value': '''
        IPv6 Interface Status for VRF "default"

        IPv6 Interface Status for VRF "management"

        IPv6 Interface Status for VRF "VRF1"
        Ethernet2/1, Interface status: protocol-up/link-up/admin-up, iod: 36
          IPv6 address: 
            2001:db8:1:1::1/64 [VALID]
            2001:db8:3:3::3/64 [VALID]
            2001:db8:4:4:a8aa:bbff:febb:cccc/64 [VALID]
            2001:db8:2:2::2/64 [VALID]
          IPv6 subnet:  2001:db8:1:1::/64
          Anycast configured addresses:
            2001:db8:2:2::2/64 [VALID]
          IPv6 link-local address: fe80::a8aa:bbff:febb:cccc (default) [VALID]
          IPv6 virtual addresses configured: none
          IPv6 multicast routing: disabled
          IPv6 report link local: disabled
          IPv6 Forwarding feature: disabled
          IPv6 multicast groups locally joined:   
              ff02::1:ffbb:cccc  ff02::1:ff00:3  ff02::1:ff00:2  ff02::2   
              ff02::1  ff02::1:ff00:1  ff02::1:ffbb:cccc  ff02::1:ff00:0  
          IPv6 multicast (S,G) entries joined: none
          IPv6 MTU: 1600 (using link MTU)
          IPv6 unicast reverse path forwarding: none
          IPv6 load sharing: none 
          IPv6 interface statistics last reset: never
          IPv6 interface RP-traffic statistics: (forwarded/originated/consumed)
            Unicast packets:      0/0/0
            Unicast bytes:        0/0/0
            Multicast packets:    0/12/9
            Multicast bytes:      0/1144/640
      '''}


    def test_empty(self):
        self.device1 = Mock(**self.empty_output)
        ipv6_interface_vrf_all_obj = ShowIpv6InterfaceVrfAll(device=self.device1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = ipv6_interface_vrf_all_obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        ipv6_interface_vrf_all_obj = ShowIpv6InterfaceVrfAll(device=self.device)
        parsed_output = ipv6_interface_vrf_all_obj.parse()
        self.maxDiff = None
        self.assertEqual(parsed_output,self.golden_parsed_output)

class test_show_ip_interface_brief(unittest.TestCase):
    device = Device(name='aDevice')
    device1 = Device(name='bDevice')
    empty_output = {'execute.return_value': ''}
    golden_parsed_output = {'interface': 
                                {'Eth5/48.106': 
                                    {'interface_status': 'protocol-down/link-down/admin-up', 'ip_address': '111.0.6.1'}, 
                                 'Lo3': 
                                    {'interface_status': 'protocol-up/link-up/admin-up', 'ip_address': '200.3.2.1'}, 
                                 'Po1.102': 
                                    {'interface_status': 'protocol-up/link-up/admin-up', 'ip_address': '201.2.12.2'}, 
                                 'Lo11': 
                                    {'interface_status': 'protocol-up/link-up/admin-up', 'ip_address': '200.11.0.1'}, 
                                 'Vlan23': 
                                    {'vlan_id': 
                                        {'23':
                                            {'interface_status': 'protocol-up/link-up/admin-up', 'ip_address': '201.52.23.1'}}}, 
                                 'Eth5/48.101': 
                                    {'interface_status': 'protocol-down/link-down/admin-up', 'ip_address': '111.0.1.1'}, 
                                 'Eth5/48.102': 
                                    {'interface_status': 'protocol-down/link-down/admin-up', 'ip_address': '111.0.2.1'}, 
                                 'Eth5/48.105': 
                                    {'interface_status': 'protocol-down/link-down/admin-up', 'ip_address': '111.0.5.1'}, 
                                 'Lo2': 
                                    {'interface_status': 'protocol-up/link-up/admin-up', 'ip_address': '200.2.2.1'}, 
                                 'Lo1': 
                                    {'interface_status': 'protocol-up/link-up/admin-up', 'ip_address': '200.1.2.1'}, 
                                 'Eth6/22': 
                                    {'interface_status': 'protocol-up/link-up/admin-up', 'ip_address': '201.51.23.1'}, 
                                 'Po1.101': 
                                    {'interface_status': 'protocol-up/link-up/admin-up', 'ip_address': '201.1.12.2'}, 
                                 'Lo10': 
                                    {'interface_status': 'protocol-up/link-up/admin-up', 'ip_address': '200.10.2.1'}, 
                                 'Po1.103': 
                                    {'interface_status': 'protocol-up/link-up/admin-up', 'ip_address': '201.3.12.2'}, 
                                 'Eth5/48.100': 
                                    {'interface_status': 'protocol-down/link-down/admin-up', 'ip_address': '111.0.0.1'}, 
                                 'Po2.107': 
                                    {'interface_status': 'protocol-up/link-up/admin-up', 'ip_address': '201.7.23.1'}, 
                                 'Eth5/48.103': 
                                    {'interface_status': 'protocol-down/link-down/admin-up', 'ip_address': '111.0.3.1'}, 
                                 'tunnel-te12': 
                                    {'interface_status': 'protocol-up/link-up/admin-up', 'ip_address': 'unnumbered(loopback0)'}, 
                                 'Eth5/48.110': 
                                    {'interface_status': 'protocol-down/link-down/admin-up', 'ip_address': '111.0.10.1'}, 
                                 'Po2.103': 
                                    {'interface_status': 'protocol-up/link-up/admin-up', 'ip_address': '201.3.23.1'}, 
                                 'Lo0': 
                                    {'interface_status': 'protocol-up/link-up/admin-up', 'ip_address': '200.0.2.1'}, 
                                 'Po2.101': 
                                    {'interface_status': 'protocol-up/link-up/admin-up', 'ip_address': '201.1.23.1'}, 
                                 'Po2.100': 
                                    {'interface_status': 'protocol-up/link-up/admin-up', 'ip_address': '201.0.23.1'}, 
                                 'tunnel-te11': 
                                    {'interface_status': 'protocol-up/link-up/admin-up', 'ip_address': 'unnumbered(loopback0)'}, 
                                 'Po2.102': 
                                    {'interface_status': 'protocol-up/link-up/admin-up', 'ip_address': '201.2.23.1'}, 
                                 'Eth5/48.104': 
                                    {'interface_status': 'protocol-down/link-down/admin-up', 'ip_address': '111.0.4.1'}
                                }
                            }

    golden_output = {'execute.return_value': '''
 IP Interface Status for VRF "default"(1)
 Interface            IP Address      Interface Status
 Vlan23               201.52.23.1     protocol-up/link-up/admin-up       
 Lo0                  200.0.2.1       protocol-up/link-up/admin-up       
 Lo1                  200.1.2.1       protocol-up/link-up/admin-up       
 Lo2                  200.2.2.1       protocol-up/link-up/admin-up       
 Lo3                  200.3.2.1       protocol-up/link-up/admin-up       
 Lo10                 200.10.2.1      protocol-up/link-up/admin-up       
 Lo11                 200.11.0.1      protocol-up/link-up/admin-up       
 Po2.100              201.0.23.1      protocol-up/link-up/admin-up       
 Po1.101              201.1.12.2      protocol-up/link-up/admin-up       
 Po2.101              201.1.23.1      protocol-up/link-up/admin-up       
 Po1.102              201.2.12.2      protocol-up/link-up/admin-up       
 Po2.102              201.2.23.1      protocol-up/link-up/admin-up       
 Po1.103              201.3.12.2      protocol-up/link-up/admin-up       
 Po2.103              201.3.23.1      protocol-up/link-up/admin-up       
 Po2.107              201.7.23.1      protocol-up/link-up/admin-up       
 Eth5/48.100          111.0.0.1       protocol-down/link-down/admin-up   
 Eth5/48.101          111.0.1.1       protocol-down/link-down/admin-up   
 Eth5/48.102          111.0.2.1       protocol-down/link-down/admin-up   
 Eth5/48.103          111.0.3.1       protocol-down/link-down/admin-up   
 Eth5/48.104          111.0.4.1       protocol-down/link-down/admin-up   
 Eth5/48.105          111.0.5.1       protocol-down/link-down/admin-up   
 Eth5/48.106          111.0.6.1       protocol-down/link-down/admin-up   
 Eth5/48.110          111.0.10.1      protocol-down/link-down/admin-up   
 Eth6/22              201.51.23.1     protocol-up/link-up/admin-up       
 tunnel-te11          unnumbered      protocol-up/link-up/admin-up       
                      (loopback0)
 tunnel-te12          unnumbered      protocol-up/link-up/admin-up       
                      (loopback0)
 
'''}

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        intf_obj = ShowIpInterfaceBrief(device=self.device)
        parsed_output = intf_obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output)

    def test_empty(self):
        self.device1 = Mock(**self.empty_output)
        intf_obj = ShowIpInterfaceBrief(device=self.device1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = intf_obj.parse()

class test_show_ip_interface_brief_Pipe_Vlan(unittest.TestCase):
    device = Device(name='aDevice')
    device1 = Device(name='bDevice')
    empty_output = {'execute.return_value': ''}
    golden_parsed_output = {'interface': 
                                {'Vlan98': 
                                    {'vlan_id': 
                                        {'98': 
                                            {'interface_status': 'protocol-down/link-down/admin-up', 'ip_address': '201.0.12.1'}
                                        }
                                    }
                                }
                            }

    golden_output = {'execute.return_value': '''
 Vlan98               201.0.12.1      protocol-down/link-down/admin-up 
'''}

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        intf_obj = ShowIpInterfaceBriefPipeVlan(device=self.device)
        parsed_output = intf_obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output)

    def test_empty(self):
        self.device1 = Mock(**self.empty_output)
        intf_obj = ShowIpInterfaceBriefPipeVlan(device=self.device1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = intf_obj.parse()

class test_show_interface_brief(unittest.TestCase):
    device = Device(name='aDevice')
    device1 = Device(name='bDevice')
    empty_output = {'execute.return_value': ''}
    golden_parsed_output = {'interface': 
                              {'ethernet': 
                                {'Eth1/1': {'mode': 'routed',
                                            'port_ch': '--',
                                            'reason': 'none                      ',
                                            'speed': '1000(D)',
                                            'status': 'up',
                                            'type': 'eth',
                                            'vlan': '--'},
                                 'Eth1/3': {'mode': 'access',
                                            'port_ch': '--',
                                            'reason': 'Administratively '
                                                      'down     ',
                                            'speed': 'auto(D)',
                                            'status': 'down',
                                            'type': 'eth',
                                            'vlan': '1'},
                                 'Eth1/6': {'mode': 'access',
                                            'port_ch': '--',
                                            'reason': 'Link not '
                                                      'connected        ',
                                            'speed': 'auto(D)',
                                            'status': 'down',
                                            'type': 'eth',
                                            'vlan': '1'}},
                              'loopback': 
                                {'Lo0': 
                                  {'description': '--',
                                   'status': 'up'}},
                              'port': 
                                {'mgmt0': 
                                  {'ip_address': '172.25.143.76',
                                   'mtu': '1500',
                                   'speed': '1000',
                                   'status': 'up',
                                   'vrf': '--'}},
                              'port_channel': 
                                {'Po8': 
                                  {'mode': 'access',
                                   'protocol': 'none',
                                   'reason': 'No operational '
                                             'members     ',
                                   'speed': 'auto(I) ',
                                   'status': 'down',
                                   'type': 'eth',
                                   'vlan': '1'}}}}


    golden_output = {'execute.return_value': '''
pinxdt-n9kv-3# show interface brief 

--------------------------------------------------------------------------------
Port   VRF          Status IP Address                              Speed    MTU
--------------------------------------------------------------------------------
mgmt0  --           up     172.25.143.76                           1000     1500

--------------------------------------------------------------------------------
Ethernet      VLAN    Type Mode   Status  Reason                   Speed     Port
Interface                                                                    Ch #
--------------------------------------------------------------------------------
Eth1/1        --      eth  routed up      none                       1000(D) --
Eth1/3        1       eth  access down    Administratively down      auto(D) --
Eth1/6        1       eth  access down    Link not connected         auto(D) --


--------------------------------------------------------------------------------
Port-channel VLAN    Type Mode   Status  Reason                    Speed   Protocol
Interface                                                                  
--------------------------------------------------------------------------------
Po8          1       eth  access down    No operational members      auto(I)  none

--------------------------------------------------------------------------------
Interface     Status     Description
--------------------------------------------------------------------------------
Lo0           up         --

'''}

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        intf_obj = ShowInterfaceBrief(device=self.device)
        parsed_output = intf_obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output)

    def test_empty(self):
        self.device1 = Mock(**self.empty_output)
        intf_obj = ShowInterfaceBrief(device=self.device1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = intf_obj.parse()

            
if __name__ == '__main__':
    unittest.main()
