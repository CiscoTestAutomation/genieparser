# Python
import unittest
from unittest.mock import Mock

from pyats.topology import Device

# Genie
from genie.metaparser.util.exceptions import SchemaEmptyParserError, \
                                             SchemaMissingKeyError

from genie.libs.parser.nxos.show_interface import (ShowInterface,
                                                   ShowVrfAllInterface,
                                                   ShowInterfaceSwitchport,
                                                   ShowIpv6InterfaceVrfAll,
                                                   ShowIpInterfaceVrfAll,
                                                   ShowIpInterfaceBrief,
                                                   ShowIpInterfaceBriefPipeVlan,
                                                   ShowInterfaceBrief,
                                                   ShowRunningConfigInterface,
                                                   ShowNveInterface,
                                                   ShowIpInterfaceBriefVrfAll,
                                                   ShowInterfaceDescription,
                                                   ShowInterfaceStatus,
                                                   ShowInterfaceCapabilities, 
                                                   ShowInterfaceTransceiver, 
                                                   ShowInterfaceTransceiverDetails,
                                                   ShowInterfaceFec,
                                                   ShowInterfaceHardwareMap)

#############################################################################
# unitest For Show Interface
#############################################################################


class TestShowInterface(unittest.TestCase):
    device = Device(name='aDevice')
    maxDiff = None

    empty_output = {'execute.return_value': ''}

    golden_parsed_output1 = {
        'Ethernet2/1':
            {'auto_mdix': 'off',
            'auto_negotiate': False,
            'admin_state': 'up',
            'bandwidth': 768,
            'beacon': 'off',
            'counters':
                {'in_bad_etype_drop': 0,
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
                'rate':
                    {'in_rate': 0,
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
            'dedicated_interface': True,
            'description': 'desc-1',
            'duplex_mode': 'full',
            'efficient_ethernet': 'n/a',
            'enabled': True,
            'encapsulations':
                {'encapsulation': 'arpa'},
            'ethertype': '0x8100',
            'flow_control':
                {'receive': False, 'send': False},
            'interface_reset': 1,
            'ipv4':
                {'10.4.4.4/24':
                    {'ip': '10.4.4.4',
                    'prefix_length': '24',
                    'route_tag': '10',
                    'secondary': True}},
            'last_link_flapped': '00:00:29',
            'link_state': 'up',
            'mac_address': 'aaaa.bbff.8888',
            'medium': 'broadcast',
            'mtu': 1600,
            'oper_status': 'up',
            'port_channel':
                {'port_channel_member': False},
            'phys_address': '5254.00ff.8506',
            'port_mode': 'routed',
            'port_speed': '1000',
            'reliability': '255/255',
            'rxload': '1/255',
            'switchport_monitor': 'off',
            'txload': '1/255',
            'types': '10/100/1000 Ethernet'},
        'Ethernet2/1.10':
            {'auto_mdix': 'off',
            'admin_state': 'down',
            'bandwidth': 768,
            'delay': 10,
            'dedicated_interface': True,
            'enabled': False,
            'encapsulations':
                {'encapsulation': 'dot1q',
                'first_dot1q': '10'},
            'ethertype': '0x8100',
            'link_state': 'down',
            'mac_address': '5254.00ff.8534',
            'medium': 'broadcast',
            'mtu': 1600,
            'oper_status': 'down',
            'port_channel':
                {'port_channel_member': False},
            'parent_interface': 'Ethernet2/1',
            'phys_address': '5254.00ff.8506',
            'port_mode': 'routed',
            'reliability': '255/255',
            'rxload': '1/255',
            'txload': '1/255',
            'types': '10/100/1000 Ethernet'},
        'Ethernet2/1.20':
            {'auto_mdix': 'off',
            'admin_state': 'up',
            'bandwidth': 768,
            'delay': 10,
            'dedicated_interface': True,
            'enabled': True,
            'encapsulations':
                {'encapsulation': 'dot1q',
                'first_dot1q': '20'},
            'ethertype': '0x8100',
            'link_state': 'up',
            'mac_address': '5254.00ff.8534',
            'medium': 'p2p',
            'mtu': 1600,
            'oper_status': 'up',
            'port_channel':
                {'port_channel_member': False},
            'parent_interface': 'Ethernet2/1',
            'phys_address': '5254.00ff.8506',
            'port_mode': 'routed',
            'reliability': '255/255',
            'rxload': '1/255',
            'txload': '1/255',
            'types': '10/100/1000 Ethernet'},
        'Ethernet2/2':
            {'auto_mdix': 'off',
            'auto_negotiate': False,
            'admin_state': 'up',
            'bandwidth': 1000000,
            'beacon': 'off',
            'counters':
                {'in_bad_etype_drop': 0,
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
                'rate':
                    {'in_rate': 0,
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
            'dedicated_interface': True,
            'duplex_mode': 'full',
            'efficient_ethernet': 'n/a',
            'enabled': True,
            'encapsulations':
                {'encapsulation': 'arpa'},
            'ethertype': '0x8100',
            'flow_control':
                {'receive': False, 'send': False},
            'interface_reset': 1,
            'last_link_flapped': '00:07:28',
            'link_state': 'up',
            'mac_address': '5254.00ff.62da',
            'medium': 'broadcast',
            'mtu': 1500,
            'oper_status': 'up',
            'port_channel':
                {'port_channel_member': False},
            'phys_address': '5254.00ff.62da',
            'port_mode': 'trunk',
            'port_speed': '1000',
            'reliability': '255/255',
            'rxload': '1/255',
            'switchport_monitor': 'off',
            'txload': '1/255',
            'types': '10/100/1000 Ethernet'},
        'mgmt0':
            {'auto_mdix': 'off',
            'auto_negotiate': True,
            'admin_state': 'up',
            'bandwidth': 1000000,
            'counters':
                { 'in_multicast_pkts': 2,
                  'in_unicast_pkts': 0,
                  'in_broadcast_pkts': 4,
                'in_pkts': 2,
                  'in_octets': 4726,
                  'rate':
                    {'in_rate': 0,
                    'in_rate_pkts': 0,
                    'load_interval': 1,
                    'out_rate': 24,
                    'out_rate_pkts': 0},
                  'rx': True,
                  'tx': True},
            'delay': 10,
            'duplex_mode': 'full',
            'enabled': True,
            'encapsulations':
                {'encapsulation': 'arpa'},
            'ethertype': '0x0000',
            'link_state': 'up',
            'mac_address': '5254.00ff.9c38',
            'medium': 'broadcast',
            'mtu': 1500,
            'oper_status': 'up',
            'port_channel':
                {'port_channel_member': False},
            'phys_address': '5254.00ff.9c38',
            'port_mode': 'routed',
            'port_speed': '1000',
            'reliability': '255/255',
            'rxload': '1/255',
            'txload': '1/255',
            'types': 'Ethernet'},
        'Ethernet1/1':
            {'bandwidth': 10000000,
            'beacon': 'off',
            'counters':
                {'in_bad_etype_drop': 0,
                'in_broadcast_pkts': 0,
                'in_crc_errors': 0,
                'in_discard': 0,
                'in_errors': 0,
                'in_if_down_drop': 0,
                'in_ignored': 0,
                'in_mac_pause_frames': 0,
                'in_multicast_pkts': 260,
                'in_no_buffer': 0,
                'in_octets': 35017,
                'in_overrun': 0,
                'in_oversize_frame': 0,
                'in_pkts': 260,
                'in_runts': 0,
                'in_short_frame': 0,
                'in_underrun': 0,
                'in_unicast_pkts': 0,
                'in_unknown_protos': 0,
                'in_watchdog': 0,
                'in_with_dribble': 0,
                'last_clear': '13:44:29',
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
                'rate':
                    {'in_rate': 0,
                    'in_rate_bps': 0,
                    'in_rate_pkts': 0,
                    'in_rate_pps': 0,
                    'load_interval': 30,
                    'out_rate': 0,
                    'out_rate_bps': 0,
                    'out_rate_pkts': 0,
                    'out_rate_pps': 0},
                'rx': True,
                'tx': True},
            'delay': 10,
            'dedicated_interface': True,
            'description': 'Connection to pe1',
            'duplex_mode': 'auto',
            'enabled': True,
            'encapsulations': {'encapsulation': 'arpa'},
            'ethertype': '0x8100',
            'flow_control': {'receive': False, 'send': False},
            'interface_reset': 0,
            'ipv4': {'10.229.1.112/16': {'ip': '10.229.1.112',
                                         'prefix_length': '16'}},
            'last_link_flapped': '13:23:37',
            'link_state': 'down',
            'mac_address': '002a.6aff.4571',
            'medium': 'broadcast',
            'mtu': 1500,
            'oper_status': 'down',
            'media_type': '10G',
            'phys_address': '002a.6aff.451d',
            'port_channel': {'port_channel_member': False},
            'port_speed': '10',
            'reliability': '255/255',
            'rxload': '1/255',
            'switchport_monitor': 'off',
            'txload': '1/255',
            'types': '1000/10000 Ethernet'},
        'nve1':
            {'enabled': True,
             'link_state': 'up',
            'oper_status': 'up',
            'port_channel':
                {'port_channel_member': False}}}

    golden_output1 = {'execute.return_value': '''
        mgmt0 is up
          admin state is up
          Hardware: Ethernet, address: 5254.00ff.9c38 (bia 5254.00ff.9c38)
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
              Hardware: 10/100/1000 Ethernet, address: aaaa.bbff.8888 (bia 5254.00ff.8506)
              Description: desc-1
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
              Hardware: 10/100/1000 Ethernet, address: 5254.00ff.8534 (bia 5254.00ff.8506)
              MTU 1600 bytes, BW 768 Kbit, DLY 10 usec
              reliability 255/255, txload 1/255, rxload 1/255
              Encapsulation 802.1Q Virtual LAN, Vlan ID 10, medium is broadcast
              Port mode is routed
              Auto-mdix is turned off
              EtherType is 0x8100
        Ethernet2/1.20 is up
            admin state is up, Dedicated Interface, [parent interface is Ethernet2/1]
              Hardware: 10/100/1000 Ethernet, address: 5254.00ff.8534 (bia 5254.00ff.8506)
              MTU 1600 bytes, BW 768 Kbit, DLY 10 usec
              reliability 255/255, txload 1/255, rxload 1/255
              Encapsulation 802.1Q Virtual LAN, Vlan ID 20, medium is p2p
              Port mode is routed
              Auto-mdix is turned off
              EtherType is 0x8100
        Ethernet2/2 is up
            admin state is up, Dedicated Interface
              Hardware: 10/100/1000 Ethernet, address: 5254.00ff.62da (bia 5254.00ff.62da)
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
        Ethernet1/1 is down (DCX-No ACK in 100 PDUs)
         Dedicated Interface

          Hardware: 1000/10000 Ethernet, address: 002a.6aff.4571 (bia 002a.6aff.451d)
          Description: Connection to pe1
          Internet Address is 10.229.1.112/16
          MTU 1500 bytes,  BW 10000000 Kbit, DLY 10 usec
          reliability 255/255, txload 1/255, rxload 1/255
          Encapsulation ARPA, medium is broadcast
          auto-duplex, 10 Gb/s, media type is 10G
          Beacon is turned off
          Input flow-control is off, output flow-control is off
          Rate mode is dedicated
          Switchport monitor is off
          EtherType is 0x8100
          Last link flapped 13:23:37
          Last clearing of "show interface" counters 13:44:29
          0 interface resets
          30 seconds input rate 0 bits/sec, 0 packets/sec
          30 seconds output rate 0 bits/sec, 0 packets/sec
          Load-Interval #2: 5 minute (300 seconds)
            input rate 0 bps, 0 pps; output rate 0 bps, 0 pps
          RX
            0 unicast packets  260 multicast packets  0 broadcast packets
            260 input packets  35017 bytes
            0 jumbo packets  0 storm suppression bytes
            0 runts  0 giants  0 CRC  0 no buffer
            0 input error  0 short frame  0 overrun   0 underrun  0 ignored
            0 watchdog  0 bad etype drop  0 bad proto drop  0 if down drop
            0 input with dribble  0 input discard
            0 Rx pause
          TX
            0 unicast packets  0 multicast packets  0 broadcast packets
            0 output packets  0 bytes
            0 jumbo packets
            0 output error  0 collision  0 deferred  0 late collision
            0 lost carrier  0 no carrier  0 babble 0 output discard
            0 Tx pause
        nve1 is up
          Hardware: NVE
          BW 0 Kbit,
        '''}

    golden_parsed_output2 = {
        "Vlan1": {
          "link_state": "down",
          "autostate": True,
          "rxload": "1/255",
          "line_protocol": "down",
          "txload": "1/255",
          "oper_status": "down",
          'port_channel': {'port_channel_member': False},
          "enabled": False,
          "mtu": 1500,
          "encapsulations": {
               "encapsulation": "arpa"
          },
          "bandwidth": 1000000,
          "reliability": "255/255",
          "delay": 10
       },
       "Vlan200": {
            "link_state": "down",
            "autostate": True,
            "rxload": "1/255",
            "line_protocol": "down",
            "txload": "1/255",
            "oper_status": "down",
            'port_channel': {'port_channel_member': False},
            "enabled": True,
            "mtu": 1500,
            "encapsulations": {
                 "encapsulation": "arpa"
            },
            "bandwidth": 1000000,
            "reliability": "255/255",
            "delay": 10}}

    golden_output2 = {'execute.return_value': '''
        Vlan1 is down (Administratively down), line protocol is down, autostate enabled
            Hardware is EtherSVI, address is  000c.29ff.f8a2
            MTU 1500 bytes, BW 1000000 Kbit, DLY 10 usec,

            reliability 255/255, txload 1/255, rxload 1/255
            Encapsulation ARPA, loopback not set
            Keepalive not supported
            ARP type: ARPA
            Last clearing of "show interface" counters never
            L3 in Switched:
            ucast: 0 pkts, 0 bytes

        Vlan200 is down (VLAN/BD is down), line protocol is down, autostate enabled
            Hardware is EtherSVI, address is  000c.29ff.f8a2
            MTU 1500 bytes, BW 1000000 Kbit, DLY 10 usec,

            reliability 255/255, txload 1/255, rxload 1/255
            Encapsulation ARPA, loopback not set
            Keepalive not supported
            ARP type: ARPA
            Last clearing of "show interface" counters never
            L3 in Switched:
            ucast: 0 pkts, 0 bytes
        '''}

    golden_output3 = {'execute.return_value': '''
        Ethernet1/6 is down (Link not connected)
        admin state is up, Dedicated Interface
          Hardware: 100/1000/10000 Ethernet, address: 000c.29ff.e5fd (bia 000c.29ff.e5fd)
          MTU 1500 bytes, BW 10000000 Kbit, DLY 10 usec
          reliability 255/255, txload 1/255, rxload 1/255
          Encapsulation ARPA, medium is broadcast
          Port mode is access
          auto-duplex, auto-speed
          Beacon is turned off
          Auto-Negotiation is turned on, FEC mode is Auto
          Input flow-control is off, output flow-control is off
          Auto-mdix is turned off
          Switchport monitor is off
          EtherType is 0x8100
          EEE (efficient-ethernet) : n/a
          Last link flapped never
          Last clearing of "show interface" counters never
          0 interface resets
          30 seconds input rate 0 bits/sec, 0 packets/sec
          30 seconds output rate 0 bits/sec, 0 packets/sec
          Load-Interval #2: 5 minute (300 seconds)
            input rate 0 bps, 0 pps; output rate 0 bps, 0 pps
          RX
            0 unicast packets  0 multicast packets  0 broadcast packets
            0 input packets  0 bytes
            0 jumbo packets  0 storm suppression packets
            0 runts  0 giants  0 CRC  0 no buffer
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

    golden_parsed_output3 = {'Ethernet1/6': {'admin_state': 'up',
                 'auto_mdix': 'off',
                 'bandwidth': 10000000,
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
                                       'load_interval': 30,
                                       'out_rate': 0,
                                       'out_rate_bps': 0,
                                       'out_rate_pkts': 0,
                                       'out_rate_pps': 0},
                              'rx': True,
                              'tx': True},
                 'dedicated_interface': True,
                 'delay': 10,
                 'efficient_ethernet': 'n/a',
                 'enabled': True,
                 'encapsulations': {'encapsulation': 'arpa'},
                 'ethertype': '0x8100',
                 'flow_control': {'receive': False, 'send': False},
                 'interface_reset': 0,
                 'last_link_flapped': 'never',
                 'link_state': 'down',
                 'mac_address': '000c.29ff.e5fd',
                 'medium': 'broadcast',
                 'mtu': 1500,
                 'oper_status': 'down',
                 'phys_address': '000c.29ff.e5fd',
                 'port_channel': {'port_channel_member': False},
                 'port_mode': 'access',
                 'reliability': '255/255',
                 'rxload': '1/255',
                 'switchport_monitor': 'off',
                 'txload': '1/255',
                 'types': '100/1000/10000 Ethernet'}}
    golden_output_custom = {'execute.return_value': '''
      Ethernet2/1 is up (XCVR not inserted)
            admin state is up, Dedicated Interface
              Hardware: 10/100/1000 Ethernet, address: aaaa.bbff.8888 (bia 5254.00ff.8506)
              Description: desc-1
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
        '''}
    golden_parsed_output_custom = {
        'Ethernet2/1':
            {'auto_mdix': 'off',
             'auto_negotiate': False,
             'admin_state': 'up',
             'bandwidth': 768,
             'beacon': 'off',
             'counters':
                 {'in_bad_etype_drop': 0,
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
                  'rate':
                      {'in_rate': 0,
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
             'dedicated_interface': True,
             'description': 'desc-1',
             'duplex_mode': 'full',
             'efficient_ethernet': 'n/a',
             'enabled': True,
             'encapsulations':
                 {'encapsulation': 'arpa'},
             'ethertype': '0x8100',
             'flow_control':
                 {'receive': False, 'send': False},
             'interface_reset': 1,
             'ipv4':
                 {'10.4.4.4/24':
                      {'ip': '10.4.4.4',
                       'prefix_length': '24',
                       'route_tag': '10',
                       'secondary': True}},
             'last_link_flapped': '00:00:29',
             'link_state': 'up',
             'mac_address': 'aaaa.bbff.8888',
             'medium': 'broadcast',
             'mtu': 1600,
             'oper_status': 'up',
             'port_channel':
                 {'port_channel_member': False},
             'phys_address': '5254.00ff.8506',
             'port_mode': 'routed',
             'port_speed': '1000',
             'reliability': '255/255',
             'rxload': '1/255',
             'switchport_monitor': 'off',
             'txload': '1/255',
             'types': '10/100/1000 Ethernet'},
    }

    golden_output_4 = {'execute.return_value': '''\
      show interface

      mgmt0 is up
      admin state is up,
        Hardware: GigabitEthernet, address: 80e0.1dff.6bae (bia 80e0.1dff.6bae)
        Internet Address is 10.154.64.17/23
        MTU 1500 bytes, BW 1000000 Kbit, DLY 10 usec
        reliability 255/255, txload 1/255, rxload 1/255
        Encapsulation ARPA, medium is broadcast
        full-duplex, 1000 Mb/s
        Auto-Negotiation is turned on
        Auto-mdix is turned off
        EtherType is 0x0000
        1 minute input rate 13408 bits/sec, 16 packets/sec
        1 minute output rate 51208 bits/sec, 17 packets/sec
        Rx
          607382344 input packets 445986207 unicast packets 132485585 multicast packets
          28910552 broadcast packets 63295517997 bytes
        Tx
          449637617 output packets 447789202 unicast packets 1848405 multicast packets
          10 broadcast packets 141467913935 bytes

      Ethernet1/1 is up
      admin state is up, Dedicated Interface
        Belongs to Po302
        Hardware: 1000/10000 Ethernet, address: 80e0.1dff.6bb6 (bia 80e0.1dff.6bb6)
        Description: << GENIE GIG 0/0/1 >>
        MTU 1500 bytes, BW 1000000 Kbit, DLY 10 usec
        reliability 255/255, txload 1/255, rxload 4/255
        Encapsulation ARPA, medium is broadcast
        Port mode is access
        full-duplex, 1000 Mb/s, media type is 1G
        Beacon is turned off
        Auto-Negotiation is turned on
        Input flow-control is off, output flow-control is off
        Auto-mdix is turned off
        Rate mode is dedicated
        Switchport monitor is off
        EtherType is 0x8100
        EEE (efficient-ethernet) : n/a
        Last link flapped 3d22h
        Last clearing of "show interface" counters never
        9 interface resets
        30 seconds input rate 17542088 bits/sec, 1904 packets/sec
        30 seconds output rate 1575520 bits/sec, 477 packets/sec
        Load-Interval #2: 5 minute (300 seconds)
          input rate 17.40 Mbps, 1.86 Kpps; output rate 1.95 Mbps, 469 pps
        RX
          525266408025 unicast packets  128283847 multicast packets  14 broadcast packets
          525394691886 input packets  157262428316065 bytes
          0 jumbo packets  0 storm suppression packets
          0 runts  0 giants  0 CRC  0 no buffer
          0 input error  0 short frame  0 overrun   0 underrun  0 ignored
          0 watchdog  0 bad etype drop  0 bad proto drop  0 if down drop
          0 input with dribble  0 input discard
          0 Rx pause
        TX
          568365811507 unicast packets  103573671 multicast packets  10009 broadcast packets
          568469395187 output packets  604413238507323 bytes
          0 jumbo packets
          0 output error  0 collision  0 deferred  0 late collision
          0 lost carrier  0 no carrier  0 babble  1535 output discard
          0 Tx pause

      Ethernet1/15 is down (Administratively down)
      admin state is down, Dedicated Interface
        Hardware: 1000/10000 Ethernet, address: 80e0.1dff.6cc3 (bia 80e0.1dff.6cc3)
        Description: << LINK TO GENIE PACKET CAPTURE >>
        MTU 1500 bytes, BW 10000000 Kbit, DLY 10 usec
        reliability 255/255, txload 1/255, rxload 1/255
        Encapsulation ARPA, medium is broadcast
        Port mode is access
        auto-duplex, auto-speed, media type is 10G
        Beacon is turned off
        Auto-Negotiation is turned on
        Input flow-control is off, output flow-control is off
        Auto-mdix is turned off
        Rate mode is dedicated
        Switchport monitor is off
        EtherType is 0x8100
        EEE (efficient-ethernet) : n/a
        Last link flapped 82week(s) 6day(s)
        Last clearing of "show interface" counters never
        16 interface resets
        30 seconds input rate 0 bits/sec, 0 packets/sec
        30 seconds output rate 0 bits/sec, 0 packets/sec
        Load-Interval #2: 5 minute (300 seconds)
          input rate 0 bps, 0 pps; output rate 0 bps, 0 pps
        RX
          30893435 unicast packets  33488177 multicast packets  139092473555 broadcast packets
          139156855167 input packets  8908513989496 bytes
          38749 jumbo packets  0 storm suppression packets
          0 runts  0 giants  0 CRC  0 no buffer
          0 input error  0 short frame  0 overrun   0 underrun  0 ignored
          0 watchdog  0 bad etype drop  0 bad proto drop  0 if down drop
          0 input with dribble  0 input discard
          0 Rx pause
        TX
          757262383558 unicast packets  1012356 multicast packets  16 broadcast packets
          757263395930 output packets  634405170787968 bytes
          24175356863 jumbo packets
          0 output error  0 collision  0 deferred  0 late collision
          0 lost carrier  0 no carrier  0 babble  169893674 output discard
          0 Tx pause

      '''
    }

    golden_parsed_output_4 = {
        'Ethernet1/1': {'admin_state': 'up',
                        'auto_mdix': 'off',
                        'auto_negotiate': True,
                        'bandwidth': 1000000,
                        'beacon': 'off',
                        'counters': {'in_bad_etype_drop': 0,
                                     'in_broadcast_pkts': 14,
                                     'in_crc_errors': 0,
                                     'in_discard': 0,
                                     'in_errors': 0,
                                     'in_if_down_drop': 0,
                                     'in_ignored': 0,
                                     'in_jumbo_packets': 0,
                                     'in_mac_pause_frames': 0,
                                     'in_multicast_pkts': 128283847,
                                     'in_no_buffer': 0,
                                     'in_octets': 157262428316065,
                                     'in_overrun': 0,
                                     'in_oversize_frame': 0,
                                     'in_pkts': 525394691886,
                                     'in_runts': 0,
                                     'in_short_frame': 0,
                                     'in_storm_suppression_packets': 0,
                                     'in_underrun': 0,
                                     'in_unicast_pkts': 525266408025,
                                     'in_unknown_protos': 0,
                                     'in_watchdog': 0,
                                     'in_with_dribble': 0,
                                     'last_clear': 'never',
                                     'out_babble': 0,
                                     'out_broadcast_pkts': 10009,
                                     'out_collision': 0,
                                     'out_deferred': 0,
                                     'out_discard': 1535,
                                     'out_errors': 0,
                                     'out_jumbo_packets': 0,
                                     'out_late_collision': 0,
                                     'out_lost_carrier': 0,
                                     'out_mac_pause_frames': 0,
                                     'out_multicast_pkts': 103573671,
                                     'out_no_carrier': 0,
                                     'out_octets': 604413238507323,
                                     'out_pkts': 568469395187,
                                     'out_unicast_pkts': 568365811507,
                                     'rate': {'in_rate': 17542088,
                                              'in_rate_pkts': 1904,
                                              'load_interval': 30,
                                              'out_rate': 1575520,
                                              'out_rate_pkts': 477},
                                     'rx': True,
                                     'tx': True},
                        'dedicated_interface': True,
                        'delay': 10,
                        'description': '<< GENIE GIG 0/0/1 >>',
                        'duplex_mode': 'full',
                        'efficient_ethernet': 'n/a',
                        'enabled': True,
                        'encapsulations': {'encapsulation': 'arpa'},
                        'ethertype': '0x8100',
                        'flow_control': {'receive': False, 'send': False},
                        'interface_reset': 9,
                        'last_link_flapped': '3d22h',
                        'link_state': 'up',
                        'mac_address': '80e0.1dff.6bb6',
                        'media_type': '1G',
                        'medium': 'broadcast',
                        'mtu': 1500,
                        'oper_status': 'up',
                        'phys_address': '80e0.1dff.6bb6',
                        'port_channel': {'port_channel_int': 'Port-channel302',
                                         'port_channel_member': True},
                        'port_mode': 'access',
                        'port_speed': '1000',
                        'reliability': '255/255',
                        'rxload': '4/255',
                        'switchport_monitor': 'off',
                        'txload': '1/255',
                        'types': '1000/10000 Ethernet'},
        'Ethernet1/15': {'admin_state': 'down',
                         'auto_mdix': 'off',
                         'auto_negotiate': True,
                         'bandwidth': 10000000,
                         'beacon': 'off',
                         'counters': {'in_bad_etype_drop': 0,
                                      'in_broadcast_pkts': 139092473555,
                                      'in_crc_errors': 0,
                                      'in_discard': 0,
                                      'in_errors': 0,
                                      'in_if_down_drop': 0,
                                      'in_ignored': 0,
                                      'in_jumbo_packets': 38749,
                                      'in_mac_pause_frames': 0,
                                      'in_multicast_pkts': 33488177,
                                      'in_no_buffer': 0,
                                      'in_octets': 8908513989496,
                                      'in_overrun': 0,
                                      'in_oversize_frame': 0,
                                      'in_pkts': 139156855167,
                                      'in_runts': 0,
                                      'in_short_frame': 0,
                                      'in_storm_suppression_packets': 0,
                                      'in_underrun': 0,
                                      'in_unicast_pkts': 30893435,
                                      'in_unknown_protos': 0,
                                      'in_watchdog': 0,
                                      'in_with_dribble': 0,
                                      'last_clear': 'never',
                                      'out_babble': 0,
                                      'out_broadcast_pkts': 16,
                                      'out_collision': 0,
                                      'out_deferred': 0,
                                      'out_discard': 169893674,
                                      'out_errors': 0,
                                      'out_jumbo_packets': 24175356863,
                                      'out_late_collision': 0,
                                      'out_lost_carrier': 0,
                                      'out_mac_pause_frames': 0,
                                      'out_multicast_pkts': 1012356,
                                      'out_no_carrier': 0,
                                      'out_octets': 634405170787968,
                                      'out_pkts': 757263395930,
                                      'out_unicast_pkts': 757262383558,
                                      'rate': {'in_rate': 0,
                                               'in_rate_bps': 0,
                                               'in_rate_pkts': 0,
                                               'in_rate_pps': 0,
                                               'load_interval': 30,
                                               'out_rate': 0,
                                               'out_rate_bps': 0,
                                               'out_rate_pkts': 0,
                                               'out_rate_pps': 0},
                                      'rx': True,
                                      'tx': True},
                         'dedicated_interface': True,
                         'delay': 10,
                         'description': '<< LINK TO GENIE PACKET CAPTURE >>',
                         'duplex_mode': 'auto',
                         'efficient_ethernet': 'n/a',
                         'enabled': False,
                         'encapsulations': {'encapsulation': 'arpa'},
                         'ethertype': '0x8100',
                         'flow_control': {'receive': False, 'send': False},
                         'interface_reset': 16,
                         'last_link_flapped': '82week(s) 6day(s)',
                         'link_state': 'down',
                         'mac_address': '80e0.1dff.6cc3',
                         'media_type': '10G',
                         'medium': 'broadcast',
                         'mtu': 1500,
                         'oper_status': 'down',
                         'phys_address': '80e0.1dff.6cc3',
                         'port_channel': {'port_channel_member': False},
                         'port_mode': 'access',
                         'port_speed': 'auto-speed',
                         'reliability': '255/255',
                         'rxload': '1/255',
                         'switchport_monitor': 'off',
                         'txload': '1/255',
                         'types': '1000/10000 Ethernet'},
        'mgmt0': {'admin_state': 'up',
                  'auto_mdix': 'off',
                  'auto_negotiate': True,
                  'bandwidth': 1000000,
                  'counters': {
                    'in_multicast_pkts': 132485585,
                    'in_unicast_pkts': 445986207,
                    'in_broadcast_pkts': 10,
                    'in_pkts': 607382344,
                    'in_octets': 141467913935,
                    'in_unicast_pkts': 445986207,
                    'rate': {'in_rate': 13408,
                                        'in_rate_pkts': 16,
                                        'load_interval': 1,
                                        'out_rate': 51208,
                                        'out_rate_pkts': 17},
                    'rx': True,
                    'tx': True},
                  'delay': 10,
                  'duplex_mode': 'full',
                  'enabled': True,
                  'encapsulations': {'encapsulation': 'arpa'},
                  'ethertype': '0x0000',
                  'ipv4': {'10.154.64.17/23': {'ip': '10.154.64.17',
                                               'prefix_length': '23'}},
                  'link_state': 'up',
                  'mac_address': '80e0.1dff.6bae',
                  'medium': 'broadcast',
                  'mtu': 1500,
                  'oper_status': 'up',
                  'phys_address': '80e0.1dff.6bae',
                  'port_channel': {'port_channel_member': False},
                  'port_speed': '1000',
                  'reliability': '255/255',
                  'rxload': '1/255',
                  'txload': '1/255',
                  'types': 'GigabitEthernet'
                }
    }

    golden_output_5 = {'execute.return_value': '''
        abc-defg# show int eth1/10

        Ethernet1/10 is down (Link not connected)

        admin state is up, Dedicated Interface

          Hardware: 100/1000/10000 Ethernet, address: 1234.12ff.df07 (bia 1234.12ff.df07)
    '''}

    golden_parsed_output_5 = {
        'Ethernet1/10': {
            'admin_state': 'up',
            'dedicated_interface': True,
            'enabled': True,
            'link_state': 'down',
            'mac_address': '1234.12ff.df07',
            'oper_status': 'down',
            'phys_address': '1234.12ff.df07',
            'port_channel': {
                'port_channel_member': False,
            },
            'types': '100/1000/10000 Ethernet',
        },
    }

    golden_output_6 = {'execute.return_value': '''
        show interface
        Ethernet1/1 is down (SFP validation failed)
         Dedicated Interface

          Hardware: 1000/10000 Ethernet, address: 8c60.4fff.ea8f (bia 8c60.4fff.ea8f)
          MTU 1500 bytes,  BW 10000000 Kbit,, BW 10000000 Kbit, DLY 10 usec
          reliability 255/255, txload 1/255, rxload 1/255
          Encapsulation ARPA, medium is broadcast
          Port mode is access
          auto-duplex, 10 Gb/s, media type is 1G
          Beacon is turned off
          Input flow-control is off, output flow-control is off
          Rate mode is dedicated
          Switchport monitor is off
          EtherType is 0x8100
          Last link flapped never
          Last clearing of "show interface" counters never
          0 interface resets
          30 seconds input rate 0 bits/sec, 0 packets/sec
          30 seconds output rate 0 bits/sec, 0 packets/sec
          Load-Interval #2: 5 minute (300 seconds)
            input rate 0 bps, 0 pps; output rate 0 bps, 0 pps
          RX
            0 unicast packets  0 multicast packets  0 broadcast packets
            0 input packets  0 bytes
            0 jumbo packets  0 storm suppression bytes
            0 runts  0 giants  0 CRC  0 no buffer
            0 input error  0 short frame  0 overrun   0 underrun  0 ignored
            0 watchdog  0 bad etype drop  0 bad proto drop  0 if down drop
            0 input with dribble  0 input discard
            0 Rx pause
          TX
            0 unicast packets  0 multicast packets  0 broadcast packets
            0 output packets  0 bytes
            0 jumbo packets
            0 output error  0 collision  0 deferred  0 late collision
            0 lost carrier  0 no carrier  0 babble 0 output discard
            0 Tx pause
    '''}
    golden_parsed_output_6 = {
        'Ethernet1/1': {
            'bandwidth': 10000000,
            'beacon': 'off',
            'counters': {
                'in_bad_etype_drop': 0,
                'in_broadcast_pkts': 0,
                'in_crc_errors': 0,
                'in_discard': 0,
                'in_errors': 0,
                'in_if_down_drop': 0,
                'in_ignored': 0,
                'in_mac_pause_frames': 0,
                'in_multicast_pkts': 0,
                'in_no_buffer': 0,
                'in_octets': 0,
                'in_overrun': 0,
                'in_oversize_frame': 0,
                'in_pkts': 0,
                'in_runts': 0,
                'in_short_frame': 0,
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
                'rate': {
                    'in_rate': 0,
                    'in_rate_bps': 0,
                    'in_rate_pkts': 0,
                    'in_rate_pps': 0,
                    'load_interval': 30,
                    'out_rate': 0,
                    'out_rate_bps': 0,
                    'out_rate_pkts': 0,
                    'out_rate_pps': 0,
                },
                'rx': True,
                'tx': True,
            },
            'dedicated_interface': True,
            'delay': 10,
            'duplex_mode': 'auto',
            'enabled': True,
            'encapsulations': {
                'encapsulation': 'arpa',
            },
            'ethertype': '0x8100',
            'flow_control': {
                'receive': False,
                'send': False,
            },
            'interface_reset': 0,
            'last_link_flapped': 'never',
            'link_state': 'down',
            'mac_address': '8c60.4fff.ea8f',
            'media_type': '1G',
            'medium': 'broadcast',
            'mtu': 1500,
            'oper_status': 'down',
            'phys_address': '8c60.4fff.ea8f',
            'port_channel': {
                'port_channel_member': False,
            },
            'port_mode': 'access',
            'port_speed': '10',
            'reliability': '255/255',
            'rxload': '1/255',
            'switchport_monitor': 'off',
            'txload': '1/255',
            'types': '1000/10000 Ethernet',
        },
    }

    golden_output_7 = {'execute.return_value': """

        Vlan88 is up, line protocol is up, autostate enabled
            Hardware is EtherSVI, address is  000c.29ff.f8a2
            MTU 1500 bytes, BW 1000000 Kbit, DLY 10 usec,
            reliability 255/255, txload 1/255, rxload 1/255
            Encapsulation ARPA, loopback not set
            Keepalive not supported
            ARP type: ARPA
            Last clearing of "show interface" counters never
            L3 in Switched:
            ucast: 0 pkts, 0 bytes

        port-channel233 is down (No operational members)
            admin state is up, Dedicated Interface
              Hardware: 10/100/1000 Ethernet, address: aaaa.bbff.8888 (bia 5254.00ff.8506)
              Description: desc-1
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
    """}

    golden_parsed_output_7 = {
           "Vlan88":{
              "port_channel":{
                 "port_channel_member":False
              },
              "link_state":"up",
              "enabled":True,
              "oper_status":"up",
              "line_protocol":"up",
              "autostate":True,
              "delay":10,
              "mtu":1500,
              "bandwidth":1000000,
              "reliability":"255/255",
              "txload":"1/255",
              "rxload":"1/255",
              "encapsulations":{
                 "encapsulation":"arpa"
              }
           },
           "port-channel233":{
              "port_channel":{
                 "port_channel_member":False
              },
              "link_state":"down",
              "enabled":True,
              "oper_status":"down",
              "admin_state":"up",
              "dedicated_interface":True,
              "types":"10/100/1000 Ethernet",
              "mac_address":"aaaa.bbff.8888",
              "phys_address":"5254.00ff.8506",
              "description":"desc-1",
              "ipv4":{
                 "10.4.4.4/24":{
                    "ip":"10.4.4.4",
                    "prefix_length":"24",
                    "secondary":True,
                    "route_tag":"10"
                 }
              },
              "delay":3330,
              "mtu":1600,
              "bandwidth":768,
              "reliability":"255/255",
              "txload":"1/255",
              "rxload":"1/255",
              "encapsulations":{
                 "encapsulation":"arpa"
              },
              "medium":"broadcast",
              "port_mode":"routed",
              "duplex_mode":"full",
              "port_speed":"1000",
              "beacon":"off",
              "auto_negotiate":False,
              "flow_control":{
                 "receive":False,
                 "send":False
              },
              "auto_mdix":"off",
              "switchport_monitor":"off",
              "ethertype":"0x8100",
              "efficient_ethernet":"n/a",
              "last_link_flapped":"00:00:29",
              "interface_reset":1,
              "counters":{
                 "rate":{
                    "load_interval":0,
                    "in_rate":0,
                    "in_rate_pkts":0,
                    "out_rate":0,
                    "out_rate_pkts":0,
                    "in_rate_bps":0,
                    "in_rate_pps":0,
                    "out_rate_bps":0,
                    "out_rate_pps":0
                 },
                 "rx":True,
                 "in_unicast_pkts":0,
                 "in_multicast_pkts":0,
                 "in_broadcast_pkts":0,
                 "last_clear":"never",
                 "in_pkts":0,
                 "in_octets":0,
                 "in_jumbo_packets":0,
                 "in_storm_suppression_packets":0,
                 "in_runts":0,
                 "in_oversize_frame":0,
                 "in_crc_errors":0,
                 "in_no_buffer":0,
                 "in_errors":0,
                 "in_short_frame":0,
                 "in_overrun":0,
                 "in_underrun":0,
                 "in_ignored":0,
                 "in_watchdog":0,
                 "in_bad_etype_drop":0,
                 "in_unknown_protos":0,
                 "in_if_down_drop":0,
                 "in_with_dribble":0,
                 "in_discard":0,
                 "in_mac_pause_frames":0,
                 "tx":True,
                 "out_unicast_pkts":0,
                 "out_multicast_pkts":0,
                 "out_broadcast_pkts":0,
                 "out_pkts":0,
                 "out_octets":0,
                 "out_jumbo_packets":0,
                 "out_errors":0,
                 "out_collision":0,
                 "out_deferred":0,
                 "out_late_collision":0,
                 "out_lost_carrier":0,
                 "out_no_carrier":0,
                 "out_babble":0,
                 "out_discard":0,
                 "out_mac_pause_frames":0
              }
           }
        }

    def test_empty(self):
        self.device1 = Mock(**self.empty_output)
        interface_obj = ShowInterface(device=self.device1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = interface_obj.parse()

    def test_golden1(self):
        self.device = Mock(**self.golden_output1)
        interface_obj = ShowInterface(device=self.device)
        parsed_output = interface_obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output1)

    def test_golden2(self):
        self.device = Mock(**self.golden_output2)
        interface_obj = ShowInterface(device=self.device)
        parsed_output = interface_obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output2)

    def test_golden3(self):
        self.device = Mock(**self.golden_output3)
        interface_obj = ShowInterface(device=self.device)
        parsed_output = interface_obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output3)

    def test_golden_custom(self):
        self.device = Mock(**self.golden_output_custom)
        interface_obj = ShowInterface(device=self.device)
        parsed_output = interface_obj.parse(interface='Ethernet2/1')
        self.assertEqual(parsed_output, self.golden_parsed_output_custom)

    def test_golden_4(self):
        self.device = Mock(**self.golden_output_4)
        interface_obj = ShowInterface(device=self.device)
        parsed_output = interface_obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_4)

    def test_golden_5(self):
        self.device = Mock(**self.golden_output_5)
        interface_obj = ShowInterface(device=self.device)
        parsed_output = interface_obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_5)

    def test_golden_6(self):
        self.device = Mock(**self.golden_output_6)
        interface_obj = ShowInterface(device=self.device)
        parsed_output = interface_obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_6)
    
    def test_golden_7(self):
        self.device = Mock(**self.golden_output_7)
        interface_obj = ShowInterface(device=self.device)
        parsed_output = interface_obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_7)
    

    def test_golden_7(self):
        self.device = Mock(**self.golden_output_7)
        interface_obj = ShowInterface(device=self.device)
        parsed_output = interface_obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_7)


    def test_golden_7(self):
        self.device = Mock(**self.golden_output_7)
        interface_obj = ShowInterface(device=self.device)
        parsed_output = interface_obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_7)

# #############################################################################
# # Unittest For Show Ip Interface Vrf All
# #############################################################################


class TestShowIpInterfaceVrfAll(unittest.TestCase):

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
                                          'prefix_length': '24',
                                          'secondary': False},
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
                 'multicast_groups': ['224.0.0.2', '224.0.0.5', '224.0.0.6'],
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

    golden_output_1 = {'execute.return_value': '''
          IP Interface Status for VRF "default"
          loopback0, Interface status: protocol-up/link-up/admin-up, iod: 180,
          Unnumbered interfaces of loopback0: first iod 46
          Ethernet2/11:
            IP address: 10.64.4.4, IP subnet: 10.64.4.0/24
            IP broadcast address: 255.255.255.255
            IP multicast groups locally joined: none
            IP MTU: 1500 bytes (using link MTU)
            IP primary address route-preference: 0, tag: 0
            IP proxy ARP : disabled
            IP Local Proxy ARP : disabled
            IP multicast routing: disabled
            IP icmp redirects: enabled
            IP directed-broadcast: disabled
            IP Forwarding: disabled
            IP icmp unreachables (except port): disabled
            IP icmp port-unreachable: enabled
            IP unicast reverse path forwarding: none
            IP load sharing: none
            IP interface statistics last reset: never
            IP interface software stats: (sent/received/forwarded/originated/consumed)
              Unicast packets    : 0/0/0/0/92391
              Unicast bytes      : 0/0/0/0/5612014
              Multicast packets  : 0/0/0/0/0
              Multicast bytes    : 0/0/0/0/0
              Broadcast packets  : 0/0/0/0/0
              Broadcast bytes    : 0/0/0/0/0
              Labeled packets    : 0/0/0/0/0
              Labeled bytes      : 0/0/0/0/0
            WCCP Redirect outbound: disabled
            WCCP Redirect inbound: disabled
            WCCP Redirect exclude: disabled
          Ethernet2/1, Interface status: protocol-up/link-up/admin-up, iod: 36,
            IP address: 10.3.4.4, IP subnet: 10.3.4.0/24
            IP broadcast address: 255.255.255.255
            IP multicast groups locally joined:
                224.0.0.6  224.0.0.5  224.0.0.2
            IP MTU: 1500 bytes (using link MTU)
            IP primary address route-preference: 0, tag: 0
            IP proxy ARP : disabled
            IP Local Proxy ARP : disabled
            IP multicast routing: disabled
            IP icmp redirects: enabled
            IP directed-broadcast: disabled
            IP Forwarding: disabled
            IP icmp unreachables (except port): disabled
            IP icmp port-unreachable: enabled
            IP unicast reverse path forwarding: none
            IP load sharing: none
            IP interface statistics last reset: never
            IP interface software stats: (sent/received/forwarded/originated/consumed)
              Unicast packets    : 53942/46139/0/53942/46150
              Unicast bytes      : 9499793/2803426/0/9499793/2804558
              Multicast packets  : 208673/208601/0/208673/417202
              Multicast bytes    : 17167084/13421700/0/17167084/13421700
              Broadcast packets  : 0/0/0/0/0
              Broadcast bytes    : 0/0/0/0/0
              Labeled packets    : 0/0/0/0/0
              Labeled bytes      : 0/0/0/0/0
            WCCP Redirect outbound: disabled
            WCCP Redirect inbound: disabled
            WCCP Redirect exclude: disabled

          Ethernet2/10.12, Interface status: protocol-down/link-down/admin-down, iod: 184,
          Unnumbered interfaces of Ethernet2/10.12: first iod 47
          Ethernet2/12:
            IP address: 10.66.12.12, IP subnet: 10.66.12.0/24
            IP broadcast address: 255.255.255.255
            IP multicast groups locally joined: none
            IP MTU: 1500 bytes (using link MTU)
            IP primary address route-preference: 0, tag: 0
            IP proxy ARP : disabled
            IP Local Proxy ARP : disabled
            IP multicast routing: disabled
            IP icmp redirects: enabled
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
          Ethernet2/11, Interface status: protocol-down/link-down/admin-down, iod: 46,
            IP unnumbered interface (loopback0)
            IP broadcast address: 255.255.255.255
            IP multicast groups locally joined: none
            IP MTU: 1500 bytes (using link MTU)
            IP proxy ARP : disabled
            IP Local Proxy ARP : disabled
            IP multicast routing: disabled
            IP icmp redirects: enabled
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
          Ethernet2/12, Interface status: protocol-down/link-down/admin-down, iod: 47,
            IP unnumbered interface (Ethernet2/10.12)
            IP broadcast address: 255.255.255.255
            IP multicast groups locally joined: none
            IP MTU: 1500 bytes (using link MTU)
            IP proxy ARP : disabled
            IP Local Proxy ARP : disabled
            IP multicast routing: disabled
            IP icmp redirects: enabled
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

    golden_parsed_output_1 = {
        "Ethernet2/11": {
          "icmp_port_unreachable": "enabled",
          "multicast_groups_address": "none",
          "proxy_arp": "disabled",
          "interface_status": "protocol-down/link-down/admin-down",
          "load_sharing": "none",
          "ipv4": {
               "counters": {
                    "multicast_bytes_received": 0,
                    "labeled_packets_forwarded": 0,
                    "multicast_bytes_sent": 0,
                    "unicast_bytes_sent": 0,
                    "labeled_packets_received": 0,
                    "labeled_packets_originated": 0,
                    "multicast_bytes_consumed": 0,
                    "multicast_packets_sent": 0,
                    "unicast_bytes_consumed": 0,
                    "broadcast_packets_originated": 0,
                    "multicast_packets_originated": 0,
                    "multicast_bytes_originated": 0,
                    "multicast_packets_received": 0,
                    "multicast_packets_consumed": 0,
                    "broadcast_packets_forwarded": 0,
                    "broadcast_bytes_originated": 0,
                    "labeled_bytes_originated": 0,
                    "broadcast_bytes_consumed": 0,
                    "broadcast_packets_sent": 0,
                    "labeled_packets_consumed": 0,
                    "unicast_packets_consumed": 0,
                    "labeled_bytes_forwarded": 0,
                    "broadcast_packets_consumed": 0,
                    "unicast_packets_sent": 0,
                    "broadcast_bytes_received": 0,
                    "labeled_packets_sent": 0,
                    "labeled_bytes_consumed": 0,
                    "unicast_bytes_received": 0,
                    "multicast_bytes_forwarded": 0,
                    "multicast_packets_forwarded": 0,
                    "unicast_packets_forwarded": 0,
                    "unicast_packets_received": 0,
                    "broadcast_packets_received": 0,
                    "broadcast_bytes_sent": 0,
                    "broadcast_bytes_forwarded": 0,
                    "labeled_bytes_sent": 0,
                    "unicast_bytes_forwarded": 0,
                    "unicast_packets_originated": 0,
                    "labeled_bytes_received": 0,
                    "unicast_bytes_originated": 0
               },
               "10.64.4.4/24": {
                    "ip": "10.64.4.4",
                    "prefix_length": "24",
                    "broadcast_address": "255.255.255.255",
                    "secondary": False,
                    "ip_subnet": "10.64.4.0"
               },
               "unnumbered": {
                    "interface_ref": "loopback0"
               }
          },
          "icmp_unreachable": "disabled",
          "wccp_redirect_inbound": "disabled",
          "unicast_reverse_path": "none",
          "icmp_redirects": "enabled",
          "multicast_routing": "disabled",
          "wccp_redirect_outbound": "disabled",
          "iod": 46,
          "directed_broadcast": "disabled",
          "ip_mtu": 1500,
          "vrf": "default",
          "local_proxy_arp": "disabled",
          "ip_forwarding": "disabled",
          "int_stat_last_reset": "never",
          "wccp_redirect_exclude": "disabled"
     },
     "loopback0": {
          "icmp_port_unreachable": "enabled",
          "multicast_groups_address": "none",
          "proxy_arp": "disabled",
          "interface_status": "protocol-up/link-up/admin-up",
          "load_sharing": "none",
          "ipv4": {
               "counters": {
                    "multicast_bytes_received": 0,
                    "labeled_packets_forwarded": 0,
                    "multicast_bytes_sent": 0,
                    "unicast_bytes_sent": 0,
                    "labeled_packets_received": 0,
                    "labeled_packets_originated": 0,
                    "multicast_bytes_consumed": 0,
                    "multicast_packets_sent": 0,
                    "unicast_bytes_consumed": 5612014,
                    "broadcast_packets_originated": 0,
                    "multicast_packets_originated": 0,
                    "multicast_bytes_originated": 0,
                    "multicast_packets_received": 0,
                    "multicast_packets_consumed": 0,
                    "broadcast_packets_forwarded": 0,
                    "broadcast_bytes_originated": 0,
                    "labeled_bytes_originated": 0,
                    "broadcast_bytes_consumed": 0,
                    "broadcast_packets_sent": 0,
                    "labeled_packets_consumed": 0,
                    "unicast_packets_consumed": 92391,
                    "labeled_bytes_forwarded": 0,
                    "broadcast_packets_consumed": 0,
                    "unicast_packets_sent": 0,
                    "broadcast_bytes_received": 0,
                    "labeled_packets_sent": 0,
                    "labeled_bytes_consumed": 0,
                    "unicast_bytes_received": 0,
                    "multicast_bytes_forwarded": 0,
                    "multicast_packets_forwarded": 0,
                    "unicast_packets_forwarded": 0,
                    "unicast_packets_received": 0,
                    "broadcast_packets_received": 0,
                    "broadcast_bytes_sent": 0,
                    "broadcast_bytes_forwarded": 0,
                    "labeled_bytes_sent": 0,
                    "unicast_bytes_forwarded": 0,
                    "unicast_packets_originated": 0,
                    "labeled_bytes_received": 0,
                    "unicast_bytes_originated": 0
               },
               "10.64.4.4/24": {
                    "route_preference": "0",
                    "prefix_length": "24",
                    "broadcast_address": "255.255.255.255",
                    "ip_subnet": "10.64.4.0",
                    "ip": "10.64.4.4",
                    "secondary": False,
                    "route_tag": "0"
               }
          },
          "icmp_unreachable": "disabled",
          "wccp_redirect_inbound": "disabled",
          "unicast_reverse_path": "none",
          "icmp_redirects": "enabled",
          "multicast_routing": "disabled",
          "wccp_redirect_outbound": "disabled",
          "iod": 180,
          "directed_broadcast": "disabled",
          "ip_mtu": 1500,
          "vrf": "default",
          "local_proxy_arp": "disabled",
          "ip_forwarding": "disabled",
          "int_stat_last_reset": "never",
          "wccp_redirect_exclude": "disabled"
     },
     "Ethernet2/1": {
          "icmp_port_unreachable": "enabled",
          "load_sharing": "none",
          "proxy_arp": "disabled",
          "interface_status": "protocol-up/link-up/admin-up",
          "ipv4": {
               "counters": {
                    "multicast_bytes_received": 13421700,
                    "labeled_packets_forwarded": 0,
                    "multicast_bytes_sent": 17167084,
                    "unicast_bytes_sent": 9499793,
                    "labeled_packets_received": 0,
                    "labeled_packets_originated": 0,
                    "multicast_bytes_consumed": 13421700,
                    "multicast_packets_sent": 208673,
                    "unicast_bytes_consumed": 2804558,
                    "broadcast_packets_originated": 0,
                    "multicast_packets_originated": 208673,
                    "multicast_bytes_originated": 17167084,
                    "multicast_packets_received": 208601,
                    "multicast_packets_consumed": 417202,
                    "broadcast_packets_forwarded": 0,
                    "broadcast_bytes_originated": 0,
                    "labeled_bytes_originated": 0,
                    "broadcast_bytes_consumed": 0,
                    "broadcast_packets_sent": 0,
                    "labeled_packets_consumed": 0,
                    "unicast_packets_consumed": 46150,
                    "labeled_bytes_forwarded": 0,
                    "broadcast_packets_consumed": 0,
                    "unicast_packets_sent": 53942,
                    "broadcast_bytes_received": 0,
                    "labeled_packets_sent": 0,
                    "labeled_bytes_consumed": 0,
                    "unicast_bytes_received": 2803426,
                    "multicast_bytes_forwarded": 0,
                    "multicast_packets_forwarded": 0,
                    "unicast_packets_forwarded": 0,
                    "unicast_packets_received": 46139,
                    "broadcast_packets_received": 0,
                    "broadcast_bytes_sent": 0,
                    "broadcast_bytes_forwarded": 0,
                    "labeled_bytes_sent": 0,
                    "unicast_bytes_forwarded": 0,
                    "unicast_packets_originated": 53942,
                    "labeled_bytes_received": 0,
                    "unicast_bytes_originated": 9499793
               },
               "10.3.4.4/24": {
                    "route_preference": "0",
                    "prefix_length": "24",
                    "broadcast_address": "255.255.255.255",
                    "ip_subnet": "10.3.4.0",
                    "ip": "10.3.4.4",
                    "secondary": False,
                    "route_tag": "0"
               }
          },
          "icmp_unreachable": "disabled",
          "wccp_redirect_inbound": "disabled",
          "unicast_reverse_path": "none",
          "icmp_redirects": "enabled",
          "multicast_routing": "disabled",
          "wccp_redirect_outbound": "disabled",
          "iod": 36,
          "directed_broadcast": "disabled",
          "ip_mtu": 1500,
          "vrf": "default",
          "local_proxy_arp": "disabled",
          "wccp_redirect_exclude": "disabled",
          "ip_forwarding": "disabled",
          "int_stat_last_reset": "never",
          "multicast_groups": [
               "224.0.0.2",
               "224.0.0.5",
               "224.0.0.6"
          ]
     },
     "Ethernet2/10.12": {
          "icmp_port_unreachable": "enabled",
          "multicast_groups_address": "none",
          "proxy_arp": "disabled",
          "interface_status": "protocol-down/link-down/admin-down",
          "load_sharing": "none",
          "ipv4": {
               "counters": {
                    "multicast_bytes_received": 0,
                    "labeled_packets_forwarded": 0,
                    "multicast_bytes_sent": 0,
                    "unicast_bytes_sent": 0,
                    "labeled_packets_received": 0,
                    "labeled_packets_originated": 0,
                    "multicast_bytes_consumed": 0,
                    "multicast_packets_sent": 0,
                    "unicast_bytes_consumed": 0,
                    "broadcast_packets_originated": 0,
                    "multicast_packets_originated": 0,
                    "multicast_bytes_originated": 0,
                    "multicast_packets_received": 0,
                    "multicast_packets_consumed": 0,
                    "broadcast_packets_forwarded": 0,
                    "broadcast_bytes_originated": 0,
                    "labeled_bytes_originated": 0,
                    "broadcast_bytes_consumed": 0,
                    "broadcast_packets_sent": 0,
                    "labeled_packets_consumed": 0,
                    "unicast_packets_consumed": 0,
                    "labeled_bytes_forwarded": 0,
                    "broadcast_packets_consumed": 0,
                    "unicast_packets_sent": 0,
                    "broadcast_bytes_received": 0,
                    "labeled_packets_sent": 0,
                    "labeled_bytes_consumed": 0,
                    "unicast_bytes_received": 0,
                    "multicast_bytes_forwarded": 0,
                    "multicast_packets_forwarded": 0,
                    "unicast_packets_forwarded": 0,
                    "unicast_packets_received": 0,
                    "broadcast_packets_received": 0,
                    "broadcast_bytes_sent": 0,
                    "broadcast_bytes_forwarded": 0,
                    "labeled_bytes_sent": 0,
                    "unicast_bytes_forwarded": 0,
                    "unicast_packets_originated": 0,
                    "labeled_bytes_received": 0,
                    "unicast_bytes_originated": 0
               },
               "10.66.12.12/24": {
                    "route_preference": "0",
                    "prefix_length": "24",
                    "broadcast_address": "255.255.255.255",
                    "ip_subnet": "10.66.12.0",
                    "ip": "10.66.12.12",
                    "secondary": False,
                    "route_tag": "0"
               }
          },
          "icmp_unreachable": "disabled",
          "wccp_redirect_inbound": "disabled",
          "unicast_reverse_path": "none",
          "icmp_redirects": "enabled",
          "multicast_routing": "disabled",
          "wccp_redirect_outbound": "disabled",
          "iod": 184,
          "directed_broadcast": "disabled",
          "ip_mtu": 1500,
          "vrf": "default",
          "local_proxy_arp": "disabled",
          "ip_forwarding": "disabled",
          "int_stat_last_reset": "never",
          "wccp_redirect_exclude": "disabled"
     },
     "Ethernet2/12": {
          "icmp_port_unreachable": "enabled",
          "multicast_groups_address": "none",
          "proxy_arp": "disabled",
          "interface_status": "protocol-down/link-down/admin-down",
          "load_sharing": "none",
          "ipv4": {
               "counters": {
                    "multicast_bytes_received": 0,
                    "labeled_packets_forwarded": 0,
                    "multicast_bytes_sent": 0,
                    "unicast_bytes_sent": 0,
                    "labeled_packets_received": 0,
                    "labeled_packets_originated": 0,
                    "multicast_bytes_consumed": 0,
                    "multicast_packets_sent": 0,
                    "unicast_bytes_consumed": 0,
                    "broadcast_packets_originated": 0,
                    "multicast_packets_originated": 0,
                    "multicast_bytes_originated": 0,
                    "multicast_packets_received": 0,
                    "multicast_packets_consumed": 0,
                    "broadcast_packets_forwarded": 0,
                    "broadcast_bytes_originated": 0,
                    "labeled_bytes_originated": 0,
                    "broadcast_bytes_consumed": 0,
                    "broadcast_packets_sent": 0,
                    "labeled_packets_consumed": 0,
                    "unicast_packets_consumed": 0,
                    "labeled_bytes_forwarded": 0,
                    "broadcast_packets_consumed": 0,
                    "unicast_packets_sent": 0,
                    "broadcast_bytes_received": 0,
                    "labeled_packets_sent": 0,
                    "labeled_bytes_consumed": 0,
                    "unicast_bytes_received": 0,
                    "multicast_bytes_forwarded": 0,
                    "multicast_packets_forwarded": 0,
                    "unicast_packets_forwarded": 0,
                    "unicast_packets_received": 0,
                    "broadcast_packets_received": 0,
                    "broadcast_bytes_sent": 0,
                    "broadcast_bytes_forwarded": 0,
                    "labeled_bytes_sent": 0,
                    "unicast_bytes_forwarded": 0,
                    "unicast_packets_originated": 0,
                    "labeled_bytes_received": 0,
                    "unicast_bytes_originated": 0
               },
               "10.66.12.12/24": {
                    "ip": "10.66.12.12",
                    "prefix_length": "24",
                    "broadcast_address": "255.255.255.255",
                    "secondary": False,
                    "ip_subnet": "10.66.12.0"
               },
               "unnumbered": {
                    "interface_ref": "Ethernet2/10.12"
               }
          },
          "icmp_unreachable": "disabled",
          "wccp_redirect_inbound": "disabled",
          "unicast_reverse_path": "none",
          "icmp_redirects": "enabled",
          "multicast_routing": "disabled",
          "wccp_redirect_outbound": "disabled",
          "iod": 47,
          "directed_broadcast": "disabled",
          "ip_mtu": 1500,
          "vrf": "default",
          "local_proxy_arp": "disabled",
          "ip_forwarding": "disabled",
          "int_stat_last_reset": "never",
          "wccp_redirect_exclude": "disabled"
     }
    }

    golden_output_2 = {'execute.return_value': '''
      IP Interface Status for VRF "default"
      loopback0, Interface status: protocol-up/link-up/admin-up, iod: 53,
      Unnumbered interfaces of loopback0: first iod 61
      mti18: tunnel-te11: tunnel-te12:
        IP address: 192.168.4.1, IP subnet: 192.168.4.1/32 route-preference: 0, tag: 0
        IP broadcast address: 255.255.255.255
        IP multicast groups locally joined:
            224.0.1.40  224.0.1.39  224.0.0.13  224.0.0.2  224.0.0.1
        IP MTU: 1500 bytes (using link MTU)
        IP primary address route-preference: 0, tag: 0
        IP proxy ARP : disabled
        IP Local Proxy ARP : disabled
        IP multicast routing: enabled
        IP icmp redirects: enabled
        IP directed-broadcast: disabled
        IP Forwarding: disabled
        IP icmp unreachables (except port): disabled
        IP icmp port-unreachable: enabled
        IP unicast reverse path forwarding: none
        IP load sharing: none
        IP interface statistics last reset: never
        IP interface software stats: (sent/received/forwarded/originated/consumed)
          Unicast packets    : 0/0/0/0/2571380
          Unicast bytes      : 0/0/0/0/195778387
          Multicast packets  : 0/0/0/0/0
          Multicast bytes    : 0/0/0/0/0
          Broadcast packets  : 0/0/0/0/0
          Broadcast bytes    : 0/0/0/0/0
          Labeled packets    : 0/0/0/0/0
          Labeled bytes      : 0/0/0/0/0
        WCCP Redirect outbound: disabled
        WCCP Redirect inbound: disabled
        WCCP Redirect exclude: disabled
      Ethernet1/5, Interface status: protocol-up/link-up/admin-up, iod: 66,
        IP address: 192.168.1.1, IP subnet: 192.168.1.0/24 route-preference: 0, tag: 0
        IP broadcast address: 255.255.255.255
        IP multicast groups locally joined:
            224.0.0.102
        IP MTU: 1500 bytes (using link MTU)
        IP primary address route-preference: 0, tag: 0
        IP proxy ARP : disabled
        IP Local Proxy ARP : disabled
        IP multicast routing: disabled
        IP icmp redirects: enabled
        IP directed-broadcast: disabled
        IP Forwarding: disabled
        IP icmp unreachables (except port): disabled
        IP icmp port-unreachable: enabled
        IP unicast reverse path forwarding: none
        IP load sharing: none
        IP interface statistics last reset: never
        IP interface software stats: (sent/received/forwarded/originated/consumed)
          Unicast packets    : 1681098/1471082/0/1681098/2942164
          Unicast bytes      : 130687624/84687016/0/130687624/169164016
          Multicast packets  : 0/6047/0/0/12066
          Multicast bytes    : 0/604700/0/0/603300
          Broadcast packets  : 0/0/0/0/0
          Broadcast bytes    : 0/0/0/0/0
          Labeled packets    : 0/0/0/0/0
          Labeled bytes      : 0/0/0/0/0
        WCCP Redirect outbound: disabled
        WCCP Redirect inbound: disabled
        WCCP Redirect exclude: disabled
      tunnel-te11, Interface status: protocol-up/link-up/admin-up, iod: 2,
        IP unnumbered interface (loopback0)
        IP broadcast address: 255.255.255.255
        IP multicast groups locally joined: none
        IP MTU: 1500 bytes (using link MTU)
        IP proxy ARP : disabled
        IP Local Proxy ARP : disabled
        IP multicast routing: disabled
        IP icmp redirects: enabled
        IP directed-broadcast: disabled
        IP Forwarding: disabled
        IP icmp unreachables (except port): disabled
        IP icmp port-unreachable: enabled
        IP unicast reverse path forwarding: none
        IP load sharing: none
        IP interface statistics last reset: never
        IP interface software stats: (sent/received/forwarded/originated/consumed)
          Unicast packets    : 215366/0/0/215366/0
          Unicast bytes      : 11524280/0/0/11524280/0
          Multicast packets  : 0/0/0/0/0
          Multicast bytes    : 0/0/0/0/0
          Broadcast packets  : 0/0/0/0/0
          Broadcast bytes    : 0/0/0/0/0
          Labeled packets    : 0/0/0/0/0
          Labeled bytes      : 0/0/0/0/0
        WCCP Redirect outbound: disabled
        WCCP Redirect inbound: disabled
        WCCP Redirect exclude: disabled
      tunnel-te12, Interface status: protocol-up/link-up/admin-up, iod: 3,
        IP unnumbered interface (loopback0)
        IP broadcast address: 255.255.255.255
        IP multicast groups locally joined: none
        IP MTU: 1500 bytes (using link MTU)
        IP proxy ARP : disabled
        IP Local Proxy ARP : disabled
        IP multicast routing: disabled
        IP icmp redirects: enabled
        IP directed-broadcast: disabled
        IP Forwarding: disabled
        IP icmp unreachables (except port): disabled
        IP icmp port-unreachable: enabled
        IP unicast reverse path forwarding: none
        IP load sharing: none
        IP interface statistics last reset: never
        IP interface software stats: (sent/received/forwarded/originated/consumed)
          Unicast packets    : 1169001/0/0/1169001/0
          Unicast bytes      : 72156810/0/0/72156810/0
          Multicast packets  : 0/0/0/0/0
          Multicast bytes    : 0/0/0/0/0
          Broadcast packets  : 0/0/0/0/0
          Broadcast bytes    : 0/0/0/0/0
          Labeled packets    : 0/0/0/0/0
          Labeled bytes      : 0/0/0/0/0
        WCCP Redirect outbound: disabled
        WCCP Redirect inbound: disabled
        WCCP Redirect exclude: disabled

      IP Interface Status for VRF "management"
      mgmt0, Interface status: protocol-up/link-up/admin-up, iod: 7,
        IP address: 10.1.17.218, IP subnet: 10.1.17.0/24 route-preference: 0, tag: 0
        IP broadcast address: 255.255.255.255
        IP multicast groups locally joined: none
        IP MTU: 1500 bytes (using link MTU)
        IP primary address route-preference: 0, tag: 0
        IP proxy ARP : disabled
        IP Local Proxy ARP : disabled
        IP multicast routing: disabled
        IP icmp redirects: enabled
        IP directed-broadcast: disabled
        IP Forwarding: disabled
        IP icmp unreachables (except port): disabled
        IP icmp port-unreachable: enabled
        IP unicast reverse path forwarding: none
        IP load sharing: none
        IP interface statistics last reset: never
        IP interface software stats: (sent/received/forwarded/originated/consumed)
          Unicast packets    : 387/659/0/387/1318
          Unicast bytes      : 36285/34935/0/36285/69870
          Multicast packets  : 0/0/0/0/0
          Multicast bytes    : 0/0/0/0/0
          Broadcast packets  : 0/0/0/0/0
          Broadcast bytes    : 0/0/0/0/0
          Labeled packets    : 0/0/0/0/0
          Labeled bytes      : 0/0/0/0/0
        WCCP Redirect outbound: disabled
        WCCP Redirect inbound: disabled
        WCCP Redirect exclude: disabled

      IP Interface Status for VRF "VRF1"

      IP Interface Status for VRF "blue"
      mti18, Interface status: protocol-up/link-up/admin-up, iod: 61,
        IP unnumbered interface (loopback0)
        IP broadcast address: 255.255.255.255
        IP multicast groups locally joined:
            224.0.0.13  224.0.0.2  224.0.0.1
        IP MTU: 1376 bytes (using link MTU)
        IP proxy ARP : disabled
        IP Local Proxy ARP : disabled
        IP multicast routing: enabled
        IP icmp redirects: enabled
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
          Multicast packets  : 0/221166/0/0/442331
          Multicast bytes    : 0/11058282/0/0/11058282
          Broadcast packets  : 0/0/0/0/0
          Broadcast bytes    : 0/0/0/0/0
          Labeled packets    : 0/0/0/0/0
          Labeled bytes      : 0/0/0/0/0
        WCCP Redirect outbound: disabled
        WCCP Redirect inbound: disabled
        WCCP Redirect exclude: disabled
    '''}
    golden_parsed_output_2 = {
        "loopback0": {
            "wccp_redirect_exclude": "disabled",
            "icmp_port_unreachable": "enabled",
            "proxy_arp": "disabled",
            "unicast_reverse_path": "none",
            "icmp_redirects": "enabled",
            "int_stat_last_reset": "never",
            "ipv4": {
                 "192.168.4.1/32": {
                      "route_preference": "0",
                      "broadcast_address": "255.255.255.255",
                      "route_tag": "0",
                      "ip": "192.168.4.1",
                      "prefix_length": "32",
                      "ip_subnet": "192.168.4.1"
                 },
                 "counters": {
                      "multicast_packets_forwarded": 0,
                      "labeled_bytes_consumed": 0,
                      "unicast_bytes_originated": 0,
                      "multicast_packets_originated": 0,
                      "labeled_bytes_forwarded": 0,
                      "labeled_packets_consumed": 0,
                      "multicast_bytes_forwarded": 0,
                      "unicast_bytes_sent": 0,
                      "multicast_packets_consumed": 0,
                      "labeled_packets_received": 0,
                      "broadcast_packets_forwarded": 0,
                      "broadcast_packets_received": 0,
                      "multicast_bytes_received": 0,
                      "unicast_bytes_forwarded": 0,
                      "broadcast_bytes_originated": 0,
                      "multicast_packets_sent": 0,
                      "broadcast_packets_sent": 0,
                      "labeled_bytes_sent": 0,
                      "labeled_bytes_received": 0,
                      "unicast_bytes_received": 0,
                      "labeled_bytes_originated": 0,
                      "broadcast_bytes_consumed": 0,
                      "labeled_packets_forwarded": 0,
                      "unicast_packets_originated": 0,
                      "unicast_packets_sent": 0,
                      "broadcast_packets_originated": 0,
                      "unicast_bytes_consumed": 195778387,
                      "broadcast_bytes_forwarded": 0,
                      "broadcast_bytes_sent": 0,
                      "broadcast_bytes_received": 0,
                      "multicast_bytes_sent": 0,
                      "multicast_bytes_originated": 0,
                      "unicast_packets_forwarded": 0,
                      "multicast_bytes_consumed": 0,
                      "broadcast_packets_consumed": 0,
                      "multicast_packets_received": 0,
                      "unicast_packets_consumed": 2571380,
                      "labeled_packets_originated": 0,
                      "labeled_packets_sent": 0,
                      "unicast_packets_received": 0
                 }
            },
            "local_proxy_arp": "disabled",
            "iod": 53,
            "icmp_unreachable": "disabled",
            "interface_status": "protocol-up/link-up/admin-up",
            "ip_forwarding": "disabled",
            "wccp_redirect_inbound": "disabled",
            "multicast_groups": [
                 "224.0.0.1",
                 "224.0.0.13",
                 "224.0.0.2",
                 "224.0.1.39",
                 "224.0.1.40"
            ],
            "wccp_redirect_outbound": "disabled",
            "multicast_routing": "enabled",
            "load_sharing": "none",
            "ip_mtu": 1500,
            "vrf": "default",
            "directed_broadcast": "disabled"
       },
       "mgmt0": {
            "wccp_redirect_exclude": "disabled",
            "icmp_port_unreachable": "enabled",
            "proxy_arp": "disabled",
            "unicast_reverse_path": "none",
            "icmp_redirects": "enabled",
            "int_stat_last_reset": "never",
            "ipv4": {
                 "counters": {
                      "multicast_packets_forwarded": 0,
                      "labeled_bytes_consumed": 0,
                      "unicast_bytes_originated": 36285,
                      "multicast_packets_originated": 0,
                      "labeled_bytes_forwarded": 0,
                      "labeled_packets_consumed": 0,
                      "multicast_bytes_forwarded": 0,
                      "unicast_bytes_sent": 36285,
                      "multicast_packets_consumed": 0,
                      "labeled_packets_received": 0,
                      "broadcast_packets_forwarded": 0,
                      "broadcast_packets_received": 0,
                      "multicast_bytes_received": 0,
                      "unicast_bytes_forwarded": 0,
                      "broadcast_bytes_originated": 0,
                      "multicast_packets_sent": 0,
                      "broadcast_packets_sent": 0,
                      "labeled_bytes_sent": 0,
                      "labeled_bytes_received": 0,
                      "unicast_bytes_received": 34935,
                      "labeled_bytes_originated": 0,
                      "broadcast_bytes_consumed": 0,
                      "labeled_packets_forwarded": 0,
                      "unicast_packets_originated": 387,
                      "unicast_packets_sent": 387,
                      "broadcast_packets_originated": 0,
                      "unicast_bytes_consumed": 69870,
                      "broadcast_bytes_forwarded": 0,
                      "broadcast_bytes_sent": 0,
                      "broadcast_bytes_received": 0,
                      "multicast_bytes_sent": 0,
                      "multicast_bytes_originated": 0,
                      "unicast_packets_forwarded": 0,
                      "multicast_bytes_consumed": 0,
                      "broadcast_packets_consumed": 0,
                      "multicast_packets_received": 0,
                      "unicast_packets_consumed": 1318,
                      "labeled_packets_originated": 0,
                      "labeled_packets_sent": 0,
                      "unicast_packets_received": 659
                 },
                 "10.1.17.218/24": {
                      "route_preference": "0",
                      "broadcast_address": "255.255.255.255",
                      "route_tag": "0",
                      "ip": "10.1.17.218",
                      "prefix_length": "24",
                      "ip_subnet": "10.1.17.0"
                 }
            },
            "local_proxy_arp": "disabled",
            "iod": 7,
            "icmp_unreachable": "disabled",
            "interface_status": "protocol-up/link-up/admin-up",
            "ip_forwarding": "disabled",
            "wccp_redirect_inbound": "disabled",
            "vrf": "management",
            "wccp_redirect_outbound": "disabled",
            "multicast_routing": "disabled",
            "load_sharing": "none",
            "ip_mtu": 1500,
            "multicast_groups_address": "none",
            "directed_broadcast": "disabled"
       },
       "tunnel-te11": {
            "wccp_redirect_exclude": "disabled",
            "icmp_port_unreachable": "enabled",
            "proxy_arp": "disabled",
            "unicast_reverse_path": "none",
            "icmp_redirects": "enabled",
            "int_stat_last_reset": "never",
            "ipv4": {
                 "192.168.4.1/32": {
                      "route_preference": "0",
                      "broadcast_address": "255.255.255.255",
                      "route_tag": "0",
                      "ip": "192.168.4.1",
                      "prefix_length": "32",
                      "ip_subnet": "192.168.4.1"
                 },
                 "counters": {
                      "multicast_packets_forwarded": 0,
                      "labeled_bytes_consumed": 0,
                      "unicast_bytes_originated": 11524280,
                      "multicast_packets_originated": 0,
                      "labeled_bytes_forwarded": 0,
                      "labeled_packets_consumed": 0,
                      "multicast_bytes_forwarded": 0,
                      "unicast_bytes_sent": 11524280,
                      "multicast_packets_consumed": 0,
                      "labeled_packets_received": 0,
                      "broadcast_packets_forwarded": 0,
                      "broadcast_packets_received": 0,
                      "multicast_bytes_received": 0,
                      "unicast_bytes_forwarded": 0,
                      "broadcast_bytes_originated": 0,
                      "multicast_packets_sent": 0,
                      "broadcast_packets_sent": 0,
                      "labeled_bytes_sent": 0,
                      "labeled_bytes_received": 0,
                      "unicast_bytes_received": 0,
                      "labeled_bytes_originated": 0,
                      "broadcast_bytes_consumed": 0,
                      "labeled_packets_forwarded": 0,
                      "unicast_packets_originated": 215366,
                      "unicast_packets_sent": 215366,
                      "broadcast_packets_originated": 0,
                      "unicast_bytes_consumed": 0,
                      "broadcast_bytes_forwarded": 0,
                      "broadcast_bytes_sent": 0,
                      "broadcast_bytes_received": 0,
                      "multicast_bytes_sent": 0,
                      "multicast_bytes_originated": 0,
                      "unicast_packets_forwarded": 0,
                      "multicast_bytes_consumed": 0,
                      "broadcast_packets_consumed": 0,
                      "multicast_packets_received": 0,
                      "unicast_packets_consumed": 0,
                      "labeled_packets_originated": 0,
                      "labeled_packets_sent": 0,
                      "unicast_packets_received": 0
                 },
                 "unnumbered": {
                      "interface_ref": "loopback0"
                 }
            },
            "local_proxy_arp": "disabled",
            "iod": 2,
            "icmp_unreachable": "disabled",
            "interface_status": "protocol-up/link-up/admin-up",
            "ip_forwarding": "disabled",
            "wccp_redirect_inbound": "disabled",
            "vrf": "default",
            "wccp_redirect_outbound": "disabled",
            "multicast_routing": "disabled",
            "load_sharing": "none",
            "ip_mtu": 1500,
            "multicast_groups_address": "none",
            "directed_broadcast": "disabled"
       },
       "tunnel-te12": {
            "wccp_redirect_exclude": "disabled",
            "icmp_port_unreachable": "enabled",
            "proxy_arp": "disabled",
            "unicast_reverse_path": "none",
            "icmp_redirects": "enabled",
            "int_stat_last_reset": "never",
            "ipv4": {
                 "192.168.4.1/32": {
                      "route_preference": "0",
                      "broadcast_address": "255.255.255.255",
                      "route_tag": "0",
                      "ip": "192.168.4.1",
                      "prefix_length": "32",
                      "ip_subnet": "192.168.4.1"
                 },
                 "counters": {
                      "multicast_packets_forwarded": 0,
                      "labeled_bytes_consumed": 0,
                      "unicast_bytes_originated": 72156810,
                      "multicast_packets_originated": 0,
                      "labeled_bytes_forwarded": 0,
                      "labeled_packets_consumed": 0,
                      "multicast_bytes_forwarded": 0,
                      "unicast_bytes_sent": 72156810,
                      "multicast_packets_consumed": 0,
                      "labeled_packets_received": 0,
                      "broadcast_packets_forwarded": 0,
                      "broadcast_packets_received": 0,
                      "multicast_bytes_received": 0,
                      "unicast_bytes_forwarded": 0,
                      "broadcast_bytes_originated": 0,
                      "multicast_packets_sent": 0,
                      "broadcast_packets_sent": 0,
                      "labeled_bytes_sent": 0,
                      "labeled_bytes_received": 0,
                      "unicast_bytes_received": 0,
                      "labeled_bytes_originated": 0,
                      "broadcast_bytes_consumed": 0,
                      "labeled_packets_forwarded": 0,
                      "unicast_packets_originated": 1169001,
                      "unicast_packets_sent": 1169001,
                      "broadcast_packets_originated": 0,
                      "unicast_bytes_consumed": 0,
                      "broadcast_bytes_forwarded": 0,
                      "broadcast_bytes_sent": 0,
                      "broadcast_bytes_received": 0,
                      "multicast_bytes_sent": 0,
                      "multicast_bytes_originated": 0,
                      "unicast_packets_forwarded": 0,
                      "multicast_bytes_consumed": 0,
                      "broadcast_packets_consumed": 0,
                      "multicast_packets_received": 0,
                      "unicast_packets_consumed": 0,
                      "labeled_packets_originated": 0,
                      "labeled_packets_sent": 0,
                      "unicast_packets_received": 0
                 },
                 "unnumbered": {
                      "interface_ref": "loopback0"
                 }
            },
            "local_proxy_arp": "disabled",
            "iod": 3,
            "icmp_unreachable": "disabled",
            "interface_status": "protocol-up/link-up/admin-up",
            "ip_forwarding": "disabled",
            "wccp_redirect_inbound": "disabled",
            "vrf": "default",
            "wccp_redirect_outbound": "disabled",
            "multicast_routing": "disabled",
            "load_sharing": "none",
            "ip_mtu": 1500,
            "multicast_groups_address": "none",
            "directed_broadcast": "disabled"
       },
       "Ethernet1/5": {
            "wccp_redirect_exclude": "disabled",
            "icmp_port_unreachable": "enabled",
            "proxy_arp": "disabled",
            "unicast_reverse_path": "none",
            "icmp_redirects": "enabled",
            "int_stat_last_reset": "never",
            "ipv4": {
                 "counters": {
                      "multicast_packets_forwarded": 0,
                      "labeled_bytes_consumed": 0,
                      "unicast_bytes_originated": 130687624,
                      "multicast_packets_originated": 0,
                      "labeled_bytes_forwarded": 0,
                      "labeled_packets_consumed": 0,
                      "multicast_bytes_forwarded": 0,
                      "unicast_bytes_sent": 130687624,
                      "multicast_packets_consumed": 12066,
                      "labeled_packets_received": 0,
                      "broadcast_packets_forwarded": 0,
                      "broadcast_packets_received": 0,
                      "multicast_bytes_received": 604700,
                      "unicast_bytes_forwarded": 0,
                      "broadcast_bytes_originated": 0,
                      "multicast_packets_sent": 0,
                      "broadcast_packets_sent": 0,
                      "labeled_bytes_sent": 0,
                      "labeled_bytes_received": 0,
                      "unicast_bytes_received": 84687016,
                      "labeled_bytes_originated": 0,
                      "broadcast_bytes_consumed": 0,
                      "labeled_packets_forwarded": 0,
                      "unicast_packets_originated": 1681098,
                      "unicast_packets_sent": 1681098,
                      "broadcast_packets_originated": 0,
                      "unicast_bytes_consumed": 169164016,
                      "broadcast_bytes_forwarded": 0,
                      "broadcast_bytes_sent": 0,
                      "broadcast_bytes_received": 0,
                      "multicast_bytes_sent": 0,
                      "multicast_bytes_originated": 0,
                      "unicast_packets_forwarded": 0,
                      "multicast_bytes_consumed": 603300,
                      "broadcast_packets_consumed": 0,
                      "multicast_packets_received": 6047,
                      "unicast_packets_consumed": 2942164,
                      "labeled_packets_originated": 0,
                      "labeled_packets_sent": 0,
                      "unicast_packets_received": 1471082
                 },
                 "192.168.1.1/24": {
                      "route_preference": "0",
                      "broadcast_address": "255.255.255.255",
                      "route_tag": "0",
                      "ip": "192.168.1.1",
                      "prefix_length": "24",
                      "ip_subnet": "192.168.1.0"
                 }
            },
            "local_proxy_arp": "disabled",
            "iod": 66,
            "icmp_unreachable": "disabled",
            "interface_status": "protocol-up/link-up/admin-up",
            "ip_forwarding": "disabled",
            "wccp_redirect_inbound": "disabled",
            "multicast_groups": [
                 "224.0.0.102"
            ],
            "wccp_redirect_outbound": "disabled",
            "multicast_routing": "disabled",
            "load_sharing": "none",
            "ip_mtu": 1500,
            "vrf": "default",
            "directed_broadcast": "disabled"
       },
       "mti18": {
            "wccp_redirect_exclude": "disabled",
            "icmp_port_unreachable": "enabled",
            "proxy_arp": "disabled",
            "unicast_reverse_path": "none",
            "icmp_redirects": "enabled",
            "int_stat_last_reset": "never",
            "ipv4": {
                 "192.168.4.1/32": {
                      "route_preference": "0",
                      "broadcast_address": "255.255.255.255",
                      "route_tag": "0",
                      "ip": "192.168.4.1",
                      "prefix_length": "32",
                      "ip_subnet": "192.168.4.1"
                 },
                 "counters": {
                      "multicast_packets_forwarded": 0,
                      "labeled_bytes_consumed": 0,
                      "unicast_bytes_originated": 0,
                      "multicast_packets_originated": 0,
                      "labeled_bytes_forwarded": 0,
                      "labeled_packets_consumed": 0,
                      "multicast_bytes_forwarded": 0,
                      "unicast_bytes_sent": 0,
                      "multicast_packets_consumed": 442331,
                      "labeled_packets_received": 0,
                      "broadcast_packets_forwarded": 0,
                      "broadcast_packets_received": 0,
                      "multicast_bytes_received": 11058282,
                      "unicast_bytes_forwarded": 0,
                      "broadcast_bytes_originated": 0,
                      "multicast_packets_sent": 0,
                      "broadcast_packets_sent": 0,
                      "labeled_bytes_sent": 0,
                      "labeled_bytes_received": 0,
                      "unicast_bytes_received": 0,
                      "labeled_bytes_originated": 0,
                      "broadcast_bytes_consumed": 0,
                      "labeled_packets_forwarded": 0,
                      "unicast_packets_originated": 0,
                      "unicast_packets_sent": 0,
                      "broadcast_packets_originated": 0,
                      "unicast_bytes_consumed": 0,
                      "broadcast_bytes_forwarded": 0,
                      "broadcast_bytes_sent": 0,
                      "broadcast_bytes_received": 0,
                      "multicast_bytes_sent": 0,
                      "multicast_bytes_originated": 0,
                      "unicast_packets_forwarded": 0,
                      "multicast_bytes_consumed": 11058282,
                      "broadcast_packets_consumed": 0,
                      "multicast_packets_received": 221166,
                      "unicast_packets_consumed": 0,
                      "labeled_packets_originated": 0,
                      "labeled_packets_sent": 0,
                      "unicast_packets_received": 0
                 },
                 "unnumbered": {
                      "interface_ref": "loopback0"
                 }
            },
            "local_proxy_arp": "disabled",
            "iod": 61,
            "icmp_unreachable": "disabled",
            "interface_status": "protocol-up/link-up/admin-up",
            "ip_forwarding": "disabled",
            "wccp_redirect_inbound": "disabled",
            "multicast_groups": [
                 "224.0.0.1",
                 "224.0.0.13",
                 "224.0.0.2"
            ],
            "wccp_redirect_outbound": "disabled",
            "multicast_routing": "enabled",
            "load_sharing": "none",
            "ip_mtu": 1376,
            "vrf": "blue",
            "directed_broadcast": "disabled"
        }
    }
    golden_output_custom = {'execute.return_value': '''
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
    golden_parsed_output_custom = {
        'Ethernet2/1': {'directed_broadcast': 'disabled',
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
                                                 'prefix_length': '24',
                                                 'secondary': False},
                                 'unnumbered': {'interface_ref': 'loopback0'},
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
                        'multicast_groups': ['224.0.0.2', '224.0.0.5', '224.0.0.6'],
                        'multicast_routing': 'disabled',
                        'proxy_arp': 'disabled',
                        'unicast_reverse_path': 'none',
                        'vrf': 'VRF1',
                        'wccp_redirect_exclude': 'disabled',
                        'wccp_redirect_inbound': 'disabled',
                        'wccp_redirect_outbound': 'disabled'}
    }

    golden_output_3 = {'execute.return_value': '''
    IP Interface Status for VRF "default"
    Vlan355, Interface status: protocol-up/link-up/admin-up, iod: 2,
      IP address: 10.170.153.133, IP subnet: 10.170.153.128/28
      IP broadcast address: 255.255.255.255
      IP multicast groups locally joined: none
      IP MTU: 9216 bytes (using link MTU)
      IP primary address route-preference: 0, tag: 0
      IP proxy ARP : disabled
      IP Local Proxy ARP : disabled
      IP multicast routing: disabled
      IP icmp redirects: enabled
      IP directed-broadcast: disabled
      IP Forwarding: disabled
      IP icmp unreachables (except port): disabled
      IP icmp port-unreachable: enabled
      IP unicast reverse path forwarding: none
      IP load sharing: none
      ip interface statistics last reset: never
      IP interface software stats: (sent/received/forwarded/originated/consumed)
        Unicast packets    : 5498120/5436721/0/5498120/5436721
        Unicast bytes      : 1012679263/691502626/0/1012679263/691502626
        Multicast packets  : 0/50702916/0/0/0
        Multicast bytes    : 0/5070291600/0/0/0
        Broadcast packets  : 0/0/0/0/0
        Broadcast bytes    : 0/0/0/0/0
        Labeled packets    : 0/0/0/0/0
        Labeled bytes      : 0/0/0/0/0
      WCCP Redirect outbound: disabled
      WCCP Redirect inbound: disabled
      WCCP Redirect exclude: disabled

    '''}

    golden_parsed_output_3 = {
        'Vlan355': {
            'directed_broadcast': 'disabled',
            'icmp_port_unreachable': 'enabled',
            'icmp_redirects': 'enabled',
            'icmp_unreachable': 'disabled',
            'int_stat_last_reset': 'never',
            'interface_status': 'protocol-up/link-up/admin-up',
            'iod': 2,
            'ip_forwarding': 'disabled',
            'ip_mtu': 9216,
            'ipv4': {
                '10.170.153.133/28': {
                    'broadcast_address': '255.255.255.255',
                    'ip': '10.170.153.133',
                    'ip_subnet': '10.170.153.128',
                    'prefix_length': '28',
                    'route_preference': '0',
                    'route_tag': '0',
                    'secondary': False,
                },
                'counters': {
                    'broadcast_bytes_consumed': 0,
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
                    'multicast_bytes_received': 5070291600,
                    'multicast_bytes_sent': 0,
                    'multicast_packets_consumed': 0,
                    'multicast_packets_forwarded': 0,
                    'multicast_packets_originated': 0,
                    'multicast_packets_received': 50702916,
                    'multicast_packets_sent': 0,
                    'unicast_bytes_consumed': 691502626,
                    'unicast_bytes_forwarded': 0,
                    'unicast_bytes_originated': 1012679263,
                    'unicast_bytes_received': 691502626,
                    'unicast_bytes_sent': 1012679263,
                    'unicast_packets_consumed': 5436721,
                    'unicast_packets_forwarded': 0,
                    'unicast_packets_originated': 5498120,
                    'unicast_packets_received': 5436721,
                    'unicast_packets_sent': 5498120,
                },
            },
            'load_sharing': 'none',
            'local_proxy_arp': 'disabled',
            'multicast_groups_address': 'none',
            'multicast_routing': 'disabled',
            'proxy_arp': 'disabled',
            'unicast_reverse_path': 'none',
            'vrf': 'default',
            'wccp_redirect_exclude': 'disabled',
            'wccp_redirect_inbound': 'disabled',
            'wccp_redirect_outbound': 'disabled',
        },
    }

    golden_output_4 = {'execute.return_value': '''
        show ip interface vrf all
        IP Interface Status for VRF "test"
        Vlan3, Interface status: protocol-up/link-up/admin-up, iod: 6,
        IP address: none
        IP broadcast address: 255.255.255.255
        IP multicast groups locally joined: none
        IP MTU: 1200 bytes (using link MTU)
        IP proxy ARP : disabled
        IP Local Proxy ARP : disabled
        IP multicast routing: disabled
        IP icmp redirects: enabled
        IP directed-broadcast: disabled
        IP Forwarding: enabled
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

        IP Interface Status for VRF "test1"

        IP Interface Status for VRF "test100"

        IP Interface Status for VRF "test200"

        IP Interface Status for VRF "test400"

    '''}

    golden_parsed_output_4 = {
        'Vlan3': {
            'directed_broadcast': 'disabled',
            'icmp_port_unreachable': 'enabled',
            'icmp_redirects': 'enabled',
            'icmp_unreachable': 'disabled',
            'int_stat_last_reset': 'never',
            'interface_status': 'protocol-up/link-up/admin-up',
            'iod': 6,
            'ip_forwarding': 'enabled',
            'ip_mtu': 1200,
            'ipv4': {
                'counters': {
                    'broadcast_bytes_consumed': 0,
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
                    'unicast_packets_sent': 0,
                },
                'none': {
                    'broadcast_address': '255.255.255.255',
                    'ip': 'none',
                },
            },
            'load_sharing': 'none',
            'local_proxy_arp': 'disabled',
            'multicast_groups_address': 'none',
            'multicast_routing': 'disabled',
            'proxy_arp': 'disabled',
            'unicast_reverse_path': 'none',
            'vrf': 'test',
            'wccp_redirect_exclude': 'disabled',
            'wccp_redirect_inbound': 'disabled',
            'wccp_redirect_outbound': 'disabled',
        },
    }

    golden_output_5 = {'execute.return_value': '''
        IP Interface Status for VRF "default"
        loopback0, Interface status: protocol-up/link-up/admin-up, iod: 94,
          IP address: 10.49.1.0, IP subnet: 10.49.1.0/32 route-preference: 0, tag: 0
          IP broadcast address: 255.255.255.255
          IP multicast groups locally joined:
              224.0.0.2  224.0.0.1  224.0.0.13
          IP MTU: 1500 bytes (using link MTU)
          IP primary address route-preference: 0, tag: 0
          IP proxy ARP : disabled
          IP Local Proxy ARP : disabled
          IP multicast routing: enabled
          IP icmp redirects: enabled
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
        loopback1, Interface status: protocol-down/link-down/admin-up, iod: 95,
          IP address: 10.49.1.1, IP subnet: 10.49.1.1/32 route-preference: 0, tag: 0
          IP address: 10.49.2.1, IP subnet: 10.49.2.1/32 secondary route-preference: 0, tag: 0
          IP broadcast address: 255.255.255.255
          IP multicast groups locally joined:
              224.0.0.2  224.0.0.1  224.0.0.13
          IP MTU: 1500 bytes (using link MTU)
          IP primary address route-preference: 0, tag: 0
          IP proxy ARP : disabled
          IP Local Proxy ARP : disabled
          IP multicast routing: enabled
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
            Multicast packets  : 0/312/0/0/312
            Multicast bytes    : 0/35184/0/0/35184
            Broadcast packets  : 0/0/0/0/0
            Broadcast bytes    : 0/0/0/0/0
            Labeled packets    : 0/0/0/0/0
            Labeled bytes      : 0/0/0/0/0
        Ethernet1/3, Interface status: protocol-up/link-up/admin-up, iod: 7,
          IP address: 10.69.111.2, IP subnet: 10.69.111.0/24 route-preference: 0, tag: 0
          IP broadcast address: 255.255.255.255
          IP multicast groups locally joined:
              224.0.0.6  224.0.0.5  224.0.0.2  224.0.0.1  224.0.0.13
          IP MTU: 1500 bytes (using link MTU)
          IP primary address route-preference: 0, tag: 0
          IP proxy ARP : disabled
          IP Local Proxy ARP : disabled
          IP multicast routing: enabled
          IP icmp redirects: enabled
          IP directed-broadcast: disabled
          IP Forwarding: disabled
          IP icmp unreachables (except port): disabled
          IP icmp port-unreachable: enabled
          IP unicast reverse path forwarding: none
          IP load sharing: none
          IP interface statistics last reset: never
          IP interface software stats: (sent/received/forwarded/originated/consumed)
            Unicast packets    : 6/6/0/6/12
            Unicast bytes      : 556/620/0/556/1240
            Multicast packets  : 205/97/0/205/189
            Multicast bytes    : 15960/6364/0/15960/6294
            Broadcast packets  : 0/0/0/0/0
            Broadcast bytes    : 0/0/0/0/0
            Labeled packets    : 0/0/0/0/0
            Labeled bytes      : 0/0/0/0/0

        IP Interface Status for VRF "management"
        mgmt0, Interface status: protocol-up/link-up/admin-up, iod: 2,
          IP address: 10.1.6.40, IP subnet: 10.1.6.0/24 route-preference: 0, tag: 0
          IP broadcast address: 255.255.255.255
          IP multicast groups locally joined: none
          IP MTU: 1500 bytes (using link MTU)
          IP primary address route-preference: 0, tag: 0
          IP proxy ARP : disabled
          IP Local Proxy ARP : disabled
          IP multicast routing: disabled
          IP icmp redirects: enabled
          IP directed-broadcast: disabled
          IP Forwarding: disabled
          IP icmp unreachables (except port): disabled
          IP icmp port-unreachable: enabled
          IP unicast reverse path forwarding: none
          IP load sharing: none
          IP interface statistics last reset: never
          IP interface software stats: (sent/received/forwarded/originated/consumed)
            Unicast packets    : 805/796/0/805/1592
            Unicast bytes      : 343014/57896/0/343014/115792
            Multicast packets  : 0/0/0/0/0
            Multicast bytes    : 0/0/0/0/0
            Broadcast packets  : 0/0/0/0/0
            Broadcast bytes    : 0/0/0/0/0
            Labeled packets    : 0/0/0/0/0
            Labeled bytes      : 0/0/0/0/0

        IP Interface Status for VRF "vrf-9100"
        Vlan100, Interface status: protocol-up/link-up/admin-up, iod: 71,
          IP address: 10.220.11.1, IP subnet: 10.220.11.0/24 route-preference: 0, tag: 0
          IP broadcast address: 255.255.255.255
          IP multicast groups locally joined:
              224.0.0.2  224.0.0.1  224.0.0.13
          IP MTU: 1500 bytes (using link MTU)
          IP primary address route-preference: 0, tag: 0
          IP proxy ARP : disabled
          IP Local Proxy ARP : disabled
          IP multicast routing: enabled
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
            Multicast packets  : 23/0/0/23/0
            Multicast bytes    : 2048/0/0/2048/0
            Broadcast packets  : 0/0/0/0/0
            Broadcast bytes    : 0/0/0/0/0
            Labeled packets    : 0/0/0/0/0
            Labeled bytes      : 0/0/0/0/0
        Vlan101, Interface status: protocol-up/link-up/admin-up, iod: 72,
          IP address: 10.220.12.1, IP subnet: 10.220.12.0/24 route-preference: 0, tag: 0
          IP broadcast address: 255.255.255.255
          IP multicast groups locally joined:
              224.0.0.2  224.0.0.1  224.0.0.13
          IP MTU: 1500 bytes (using link MTU)
          IP primary address route-preference: 0, tag: 0
          IP proxy ARP : disabled
          IP Local Proxy ARP : disabled
          IP multicast routing: enabled
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
            Multicast packets  : 23/0/0/23/0
            Multicast bytes    : 2048/0/0/2048/0
            Broadcast packets  : 0/0/0/0/0
            Broadcast bytes    : 0/0/0/0/0
            Labeled packets    : 0/0/0/0/0
            Labeled bytes      : 0/0/0/0/0
        Vlan102, Interface status: protocol-down/link-down/admin-up, iod: 73,
          IP address: 10.220.13.1, IP subnet: 10.220.13.0/24 route-preference: 0, tag: 0
          IP broadcast address: 255.255.255.255
          IP multicast groups locally joined:
              224.0.0.2  224.0.0.1  224.0.0.13
          IP MTU: 1500 bytes (using link MTU)
          IP primary address route-preference: 0, tag: 0
          IP proxy ARP : disabled
          IP Local Proxy ARP : disabled
          IP multicast routing: enabled
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
        Vlan910, Interface status: protocol-down/link-down/admin-up, iod: 85,
          IP address: none
          IP broadcast address: 255.255.255.255
          IP multicast groups locally joined: none
          IP MTU: 1500 bytes (using link MTU)
          IP proxy ARP : disabled
          IP Local Proxy ARP : disabled
          IP multicast routing: disabled
          IP icmp redirects: enabled
          IP directed-broadcast: disabled
          IP Forwarding: enabled
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
        Vlan1000, Interface status: protocol-up/link-up/admin-up, iod: 86,
          IP address: none
          IP broadcast address: 255.255.255.255
          IP multicast groups locally joined:
              224.0.0.2  224.0.0.1  224.0.0.13
          IP MTU: 1500 bytes (using link MTU)
          IP proxy ARP : disabled
          IP Local Proxy ARP : disabled
          IP multicast routing: enabled
          IP icmp redirects: disabled
          IP directed-broadcast: disabled
          IP Forwarding: enabled
          IP icmp unreachables (except port): disabled
          IP icmp port-unreachable: enabled
          IP unicast reverse path forwarding: none
          IP load sharing: none
          IP interface statistics last reset: never
          IP interface software stats: (sent/received/forwarded/originated/consumed)
            Unicast packets    : 0/0/0/0/0
            Unicast bytes      : 0/0/0/0/0
            Multicast packets  : 22/0/0/22/0
            Multicast bytes    : 1496/0/0/1496/0
            Broadcast packets  : 0/0/0/0/0
            Broadcast bytes    : 0/0/0/0/0
            Labeled packets    : 0/0/0/0/0
            Labeled bytes      : 0/0/0/0/0

        IP Interface Status for VRF "vrf-9105"
        Vlan105, Interface status: protocol-up/link-up/admin-up, iod: 75,
          IP address: 10.220.16.1, IP subnet: 10.220.16.0/24 route-preference: 0, tag: 0
          IP broadcast address: 255.255.255.255
          IP multicast groups locally joined:
              224.0.0.2  224.0.0.1  224.0.0.13
          IP MTU: 1500 bytes (using link MTU)
          IP primary address route-preference: 0, tag: 0
          IP proxy ARP : disabled
          IP Local Proxy ARP : disabled
          IP multicast routing: enabled
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
            Multicast packets  : 23/0/0/23/0
            Multicast bytes    : 2048/0/0/2048/0
            Broadcast packets  : 0/0/0/0/0
            Broadcast bytes    : 0/0/0/0/0
            Labeled packets    : 0/0/0/0/0
            Labeled bytes      : 0/0/0/0/0
        Vlan110, Interface status: protocol-up/link-up/admin-up, iod: 80,
          IP address: 10.220.21.1, IP subnet: 10.220.21.0/24 route-preference: 0, tag: 0
          IP broadcast address: 255.255.255.255
          IP multicast groups locally joined:
              224.0.0.2  224.0.0.1  224.0.0.13
          IP MTU: 1500 bytes (using link MTU)
          IP primary address route-preference: 0, tag: 0
          IP proxy ARP : disabled
          IP Local Proxy ARP : disabled
          IP multicast routing: enabled
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
            Multicast packets  : 23/0/0/23/0
            Multicast bytes    : 2048/0/0/2048/0
            Broadcast packets  : 0/0/0/0/0
            Broadcast bytes    : 0/0/0/0/0
            Labeled packets    : 0/0/0/0/0
            Labeled bytes      : 0/0/0/0/0
        Vlan1005, Interface status: protocol-up/link-up/admin-up, iod: 87,
          IP address: none
          IP broadcast address: 255.255.255.255
          IP multicast groups locally joined:
              224.0.0.2  224.0.0.1  224.0.0.13
          IP MTU: 1500 bytes (using link MTU)
          IP proxy ARP : disabled
          IP Local Proxy ARP : disabled
          IP multicast routing: enabled
          IP icmp redirects: disabled
          IP directed-broadcast: disabled
          IP Forwarding: enabled
          IP icmp unreachables (except port): disabled
          IP icmp port-unreachable: enabled
          IP unicast reverse path forwarding: none
          IP load sharing: none
          IP interface statistics last reset: never
          IP interface software stats: (sent/received/forwarded/originated/consumed)
            Unicast packets    : 0/0/0/0/0
            Unicast bytes      : 0/0/0/0/0
            Multicast packets  : 22/0/0/22/0
            Multicast bytes    : 1496/0/0/1496/0
            Broadcast packets  : 0/0/0/0/0
            Broadcast bytes    : 0/0/0/0/0
            Labeled packets    : 0/0/0/0/0
            Labeled bytes      : 0/0/0/0/0

        IP Interface Status for VRF "vrf-9106"
        Vlan106, Interface status: protocol-up/link-up/admin-up, iod: 76,
          IP address: 10.220.17.1, IP subnet: 10.220.17.0/24 route-preference: 0, tag: 0
          IP broadcast address: 255.255.255.255
          IP multicast groups locally joined:
              224.0.0.2  224.0.0.1  224.0.0.13
          IP MTU: 1500 bytes (using link MTU)
          IP primary address route-preference: 0, tag: 0
          IP proxy ARP : disabled
          IP Local Proxy ARP : disabled
          IP multicast routing: enabled
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
            Multicast packets  : 23/0/0/23/0
            Multicast bytes    : 2048/0/0/2048/0
            Broadcast packets  : 0/0/0/0/0
            Broadcast bytes    : 0/0/0/0/0
            Labeled packets    : 0/0/0/0/0
            Labeled bytes      : 0/0/0/0/0
        Vlan111, Interface status: protocol-up/link-up/admin-up, iod: 81,
          IP address: 10.220.22.1, IP subnet: 10.220.22.0/24 route-preference: 0, tag: 0
          IP broadcast address: 255.255.255.255
          IP multicast groups locally joined:
              224.0.0.2  224.0.0.1  224.0.0.13
          IP MTU: 1500 bytes (using link MTU)
          IP primary address route-preference: 0, tag: 0
          IP proxy ARP : disabled
          IP Local Proxy ARP : disabled
          IP multicast routing: enabled
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
            Multicast packets  : 23/0/0/23/0
            Multicast bytes    : 2048/0/0/2048/0
            Broadcast packets  : 0/0/0/0/0
            Broadcast bytes    : 0/0/0/0/0
            Labeled packets    : 0/0/0/0/0
            Labeled bytes      : 0/0/0/0/0
        Vlan1006, Interface status: protocol-up/link-up/admin-up, iod: 88,
          IP address: none
          IP broadcast address: 255.255.255.255
          IP multicast groups locally joined:
              224.0.0.2  224.0.0.1  224.0.0.13
          IP MTU: 1500 bytes (using link MTU)
          IP proxy ARP : disabled
          IP Local Proxy ARP : disabled
          IP multicast routing: enabled
          IP icmp redirects: disabled
          IP directed-broadcast: disabled
          IP Forwarding: enabled
          IP icmp unreachables (except port): disabled
          IP icmp port-unreachable: enabled
          IP unicast reverse path forwarding: none
          IP load sharing: none
          IP interface statistics last reset: never
          IP interface software stats: (sent/received/forwarded/originated/consumed)
            Unicast packets    : 0/0/0/0/0
            Unicast bytes      : 0/0/0/0/0
            Multicast packets  : 22/0/0/22/0
            Multicast bytes    : 1496/0/0/1496/0
            Broadcast packets  : 0/0/0/0/0
            Broadcast bytes    : 0/0/0/0/0
            Labeled packets    : 0/0/0/0/0
            Labeled bytes      : 0/0/0/0/0

        IP Interface Status for VRF "vrf-9107"
        Vlan107, Interface status: protocol-up/link-up/admin-up, iod: 77,
          IP address: 10.220.18.1, IP subnet: 10.220.18.0/24 route-preference: 0, tag: 0
          IP broadcast address: 255.255.255.255
          IP multicast groups locally joined:
              224.0.0.2  224.0.0.1  224.0.0.13
          IP MTU: 1500 bytes (using link MTU)
          IP primary address route-preference: 0, tag: 0
          IP proxy ARP : disabled
          IP Local Proxy ARP : disabled
          IP multicast routing: enabled
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
            Multicast packets  : 23/0/0/23/0
            Multicast bytes    : 2048/0/0/2048/0
            Broadcast packets  : 0/0/0/0/0
            Broadcast bytes    : 0/0/0/0/0
            Labeled packets    : 0/0/0/0/0
            Labeled bytes      : 0/0/0/0/0
        Vlan112, Interface status: protocol-up/link-up/admin-up, iod: 82,
          IP address: 10.220.23.1, IP subnet: 10.220.23.0/24 route-preference: 0, tag: 0
          IP broadcast address: 255.255.255.255
          IP multicast groups locally joined:
              224.0.0.2  224.0.0.1  224.0.0.13
          IP MTU: 1500 bytes (using link MTU)
          IP primary address route-preference: 0, tag: 0
          IP proxy ARP : disabled
          IP Local Proxy ARP : disabled
          IP multicast routing: enabled
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
            Multicast packets  : 23/0/0/23/0
            Multicast bytes    : 2048/0/0/2048/0
            Broadcast packets  : 0/0/0/0/0
            Broadcast bytes    : 0/0/0/0/0
            Labeled packets    : 0/0/0/0/0
            Labeled bytes      : 0/0/0/0/0
        Vlan1007, Interface status: protocol-up/link-up/admin-up, iod: 89,
          IP address: none
          IP broadcast address: 255.255.255.255
          IP multicast groups locally joined:
              224.0.0.2  224.0.0.1  224.0.0.13
          IP MTU: 1500 bytes (using link MTU)
          IP proxy ARP : disabled
          IP Local Proxy ARP : disabled
          IP multicast routing: enabled
          IP icmp redirects: disabled
          IP directed-broadcast: disabled
          IP Forwarding: enabled
          IP icmp unreachables (except port): disabled
          IP icmp port-unreachable: enabled
          IP unicast reverse path forwarding: none
          IP load sharing: none
          IP interface statistics last reset: never
          IP interface software stats: (sent/received/forwarded/originated/consumed)
            Unicast packets    : 0/0/0/0/0
            Unicast bytes      : 0/0/0/0/0
            Multicast packets  : 22/0/0/22/0
            Multicast bytes    : 1496/0/0/1496/0
            Broadcast packets  : 0/0/0/0/0
            Broadcast bytes    : 0/0/0/0/0
            Labeled packets    : 0/0/0/0/0
            Labeled bytes      : 0/0/0/0/0

        IP Interface Status for VRF "vrf-9108"
        Vlan108, Interface status: protocol-up/link-up/admin-up, iod: 78,
          IP address: 10.220.19.1, IP subnet: 10.220.19.0/24 route-preference: 0, tag: 0
          IP broadcast address: 255.255.255.255
          IP multicast groups locally joined:
              224.0.0.2  224.0.0.1  224.0.0.13
          IP MTU: 1500 bytes (using link MTU)
          IP primary address route-preference: 0, tag: 0
          IP proxy ARP : disabled
          IP Local Proxy ARP : disabled
          IP multicast routing: enabled
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
            Multicast packets  : 23/0/0/23/0
            Multicast bytes    : 2048/0/0/2048/0
            Broadcast packets  : 0/0/0/0/0
            Broadcast bytes    : 0/0/0/0/0
            Labeled packets    : 0/0/0/0/0
            Labeled bytes      : 0/0/0/0/0
        Vlan113, Interface status: protocol-up/link-up/admin-up, iod: 83,
          IP address: 10.220.24.1, IP subnet: 10.220.24.0/24 route-preference: 0, tag: 0
          IP broadcast address: 255.255.255.255
          IP multicast groups locally joined:
              224.0.0.2  224.0.0.1  224.0.0.13
          IP MTU: 1500 bytes (using link MTU)
          IP primary address route-preference: 0, tag: 0
          IP proxy ARP : disabled
          IP Local Proxy ARP : disabled
          IP multicast routing: enabled
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
            Multicast packets  : 23/0/0/23/0
            Multicast bytes    : 2048/0/0/2048/0
            Broadcast packets  : 0/0/0/0/0
            Broadcast bytes    : 0/0/0/0/0
            Labeled packets    : 0/0/0/0/0
            Labeled bytes      : 0/0/0/0/0
        Vlan1008, Interface status: protocol-up/link-up/admin-up, iod: 90,
          IP address: none
          IP broadcast address: 255.255.255.255
          IP multicast groups locally joined:
              224.0.0.2  224.0.0.1  224.0.0.13
          IP MTU: 1500 bytes (using link MTU)
          IP proxy ARP : disabled
          IP Local Proxy ARP : disabled
          IP multicast routing: enabled
          IP icmp redirects: disabled
          IP directed-broadcast: disabled
          IP Forwarding: enabled
          IP icmp unreachables (except port): disabled
          IP icmp port-unreachable: enabled
          IP unicast reverse path forwarding: none
          IP load sharing: none
          IP interface statistics last reset: never
          IP interface software stats: (sent/received/forwarded/originated/consumed)
            Unicast packets    : 0/0/0/0/0
            Unicast bytes      : 0/0/0/0/0
            Multicast packets  : 22/0/0/22/0
            Multicast bytes    : 1496/0/0/1496/0
            Broadcast packets  : 0/0/0/0/0
            Broadcast bytes    : 0/0/0/0/0
            Labeled packets    : 0/0/0/0/0
            Labeled bytes      : 0/0/0/0/0

        IP Interface Status for VRF "vrf-9109"
        Vlan109, Interface status: protocol-up/link-up/admin-up, iod: 79,
          IP address: 10.220.20.1, IP subnet: 10.220.20.0/24 route-preference: 0, tag: 0
          IP broadcast address: 255.255.255.255
          IP multicast groups locally joined:
              224.0.0.2  224.0.0.1  224.0.0.13
          IP MTU: 1500 bytes (using link MTU)
          IP primary address route-preference: 0, tag: 0
          IP proxy ARP : disabled
          IP Local Proxy ARP : disabled
          IP multicast routing: enabled
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
            Multicast packets  : 23/0/0/23/0
            Multicast bytes    : 2048/0/0/2048/0
            Broadcast packets  : 0/0/0/0/0
            Broadcast bytes    : 0/0/0/0/0
            Labeled packets    : 0/0/0/0/0
            Labeled bytes      : 0/0/0/0/0
        Vlan114, Interface status: protocol-up/link-up/admin-up, iod: 84,
          IP address: 10.220.25.1, IP subnet: 10.220.25.0/24 route-preference: 0, tag: 0
          IP broadcast address: 255.255.255.255
          IP multicast groups locally joined:
              224.0.0.2  224.0.0.1  224.0.0.13
          IP MTU: 1500 bytes (using link MTU)
          IP primary address route-preference: 0, tag: 0
          IP proxy ARP : disabled
          IP Local Proxy ARP : disabled
          IP multicast routing: enabled
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
            Multicast packets  : 23/0/0/23/0
            Multicast bytes    : 2048/0/0/2048/0
            Broadcast packets  : 0/0/0/0/0
            Broadcast bytes    : 0/0/0/0/0
            Labeled packets    : 0/0/0/0/0
            Labeled bytes      : 0/0/0/0/0
        Vlan1009, Interface status: protocol-up/link-up/admin-up, iod: 91,
          IP address: none
          IP broadcast address: 255.255.255.255
          IP multicast groups locally joined:
              224.0.0.2  224.0.0.1  224.0.0.13
          IP MTU: 1500 bytes (using link MTU)
          IP proxy ARP : disabled
          IP Local Proxy ARP : disabled
          IP multicast routing: enabled
          IP icmp redirects: disabled
          IP directed-broadcast: disabled
          IP Forwarding: enabled
          IP icmp unreachables (except port): disabled
          IP icmp port-unreachable: enabled
          IP unicast reverse path forwarding: none
          IP load sharing: none
          IP interface statistics last reset: never
          IP interface software stats: (sent/received/forwarded/originated/consumed)
            Unicast packets    : 0/0/0/0/0
            Unicast bytes      : 0/0/0/0/0
            Multicast packets  : 21/0/0/21/0
            Multicast bytes    : 1428/0/0/1428/0
            Broadcast packets  : 0/0/0/0/0
            Broadcast bytes    : 0/0/0/0/0
            Labeled packets    : 0/0/0/0/0
            Labeled bytes      : 0/0/0/0/0

        N95_1#
        '''}

    golden_parsed_output_5 = {
        'Ethernet1/3':
            {'directed_broadcast': 'disabled',
            'icmp_port_unreachable': 'enabled',
            'icmp_redirects': 'enabled',
            'icmp_unreachable': 'disabled',
            'int_stat_last_reset': 'never',
            'interface_status': 'protocol-up/link-up/admin-up',
            'iod': 7,
            'ip_forwarding': 'disabled',
            'ip_mtu': 1500,
            'ipv4':
                {'10.69.111.2/24':
                    {'broadcast_address': '255.255.255.255',
                    'ip': '10.69.111.2',
                    'ip_subnet': '10.69.111.0',
                    'prefix_length': '24',
                    'route_preference': '0',
                    'route_tag': '0'},
                    'counters':
                        {'broadcast_bytes_consumed': 0,
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
                        'multicast_bytes_consumed': 6294,
                        'multicast_bytes_forwarded': 0,
                        'multicast_bytes_originated': 15960,
                        'multicast_bytes_received': 6364,
                        'multicast_bytes_sent': 15960,
                        'multicast_packets_consumed': 189,
                        'multicast_packets_forwarded': 0,
                        'multicast_packets_originated': 205,
                        'multicast_packets_received': 97,
                        'multicast_packets_sent': 205,
                        'unicast_bytes_consumed': 1240,
                        'unicast_bytes_forwarded': 0,
                        'unicast_bytes_originated': 556,
                        'unicast_bytes_received': 620,
                        'unicast_bytes_sent': 556,
                        'unicast_packets_consumed': 12,
                        'unicast_packets_forwarded': 0,
                        'unicast_packets_originated': 6,
                        'unicast_packets_received': 6,
                        'unicast_packets_sent': 6}},
                    'load_sharing': 'none',
                    'local_proxy_arp': 'disabled',
                    'multicast_groups': ['224.0.0.1',
                                      '224.0.0.13',
                                      '224.0.0.2',
                                      '224.0.0.5',
                                      '224.0.0.6'],
                    'multicast_routing': 'enabled',
                    'proxy_arp': 'disabled',
                    'unicast_reverse_path': 'none',
                    'vrf': 'default'},
        'Vlan100': {'directed_broadcast': 'disabled',
                 'icmp_port_unreachable': 'enabled',
                 'icmp_redirects': 'disabled',
                 'icmp_unreachable': 'disabled',
                 'int_stat_last_reset': 'never',
                 'interface_status': 'protocol-up/link-up/admin-up',
                 'iod': 71,
                 'ip_forwarding': 'disabled',
                 'ip_mtu': 1500,
                 'ipv4': {'10.220.11.1/24': {'broadcast_address': '255.255.255.255',
                                              'ip': '10.220.11.1',
                                              'ip_subnet': '10.220.11.0',
                                              'prefix_length': '24',
                                              'route_preference': '0',
                                              'route_tag': '0'},
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
                                       'multicast_bytes_originated': 2048,
                                       'multicast_bytes_received': 0,
                                       'multicast_bytes_sent': 2048,
                                       'multicast_packets_consumed': 0,
                                       'multicast_packets_forwarded': 0,
                                       'multicast_packets_originated': 23,
                                       'multicast_packets_received': 0,
                                       'multicast_packets_sent': 23,
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
                 'multicast_groups': ['224.0.0.1', '224.0.0.13', '224.0.0.2'],
                 'multicast_routing': 'enabled',
                 'proxy_arp': 'disabled',
                 'unicast_reverse_path': 'none',
                 'vrf': 'vrf-9100'},
        'Vlan1000': {'directed_broadcast': 'disabled',
                  'icmp_port_unreachable': 'enabled',
                  'icmp_redirects': 'disabled',
                  'icmp_unreachable': 'disabled',
                  'int_stat_last_reset': 'never',
                  'interface_status': 'protocol-up/link-up/admin-up',
                  'iod': 86,
                  'ip_forwarding': 'enabled',
                  'ip_mtu': 1500,
                  'ipv4': {'counters': {'broadcast_bytes_consumed': 0,
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
                                        'multicast_bytes_originated': 1496,
                                        'multicast_bytes_received': 0,
                                        'multicast_bytes_sent': 1496,
                                        'multicast_packets_consumed': 0,
                                        'multicast_packets_forwarded': 0,
                                        'multicast_packets_originated': 22,
                                        'multicast_packets_received': 0,
                                        'multicast_packets_sent': 22,
                                        'unicast_bytes_consumed': 0,
                                        'unicast_bytes_forwarded': 0,
                                        'unicast_bytes_originated': 0,
                                        'unicast_bytes_received': 0,
                                        'unicast_bytes_sent': 0,
                                        'unicast_packets_consumed': 0,
                                        'unicast_packets_forwarded': 0,
                                        'unicast_packets_originated': 0,
                                        'unicast_packets_received': 0,
                                        'unicast_packets_sent': 0},
                           'none': {'broadcast_address': '255.255.255.255',
                                    'ip': 'none'}},
                  'load_sharing': 'none',
                  'local_proxy_arp': 'disabled',
                  'multicast_groups': ['224.0.0.1', '224.0.0.13', '224.0.0.2'],
                  'multicast_routing': 'enabled',
                  'proxy_arp': 'disabled',
                  'unicast_reverse_path': 'none',
                  'vrf': 'vrf-9100'},
        'Vlan1005': {'directed_broadcast': 'disabled',
                  'icmp_port_unreachable': 'enabled',
                  'icmp_redirects': 'disabled',
                  'icmp_unreachable': 'disabled',
                  'int_stat_last_reset': 'never',
                  'interface_status': 'protocol-up/link-up/admin-up',
                  'iod': 87,
                  'ip_forwarding': 'enabled',
                  'ip_mtu': 1500,
                  'ipv4': {'counters': {'broadcast_bytes_consumed': 0,
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
                                        'multicast_bytes_originated': 1496,
                                        'multicast_bytes_received': 0,
                                        'multicast_bytes_sent': 1496,
                                        'multicast_packets_consumed': 0,
                                        'multicast_packets_forwarded': 0,
                                        'multicast_packets_originated': 22,
                                        'multicast_packets_received': 0,
                                        'multicast_packets_sent': 22,
                                        'unicast_bytes_consumed': 0,
                                        'unicast_bytes_forwarded': 0,
                                        'unicast_bytes_originated': 0,
                                        'unicast_bytes_received': 0,
                                        'unicast_bytes_sent': 0,
                                        'unicast_packets_consumed': 0,
                                        'unicast_packets_forwarded': 0,
                                        'unicast_packets_originated': 0,
                                        'unicast_packets_received': 0,
                                        'unicast_packets_sent': 0},
                           'none': {'broadcast_address': '255.255.255.255',
                                    'ip': 'none'}},
                  'load_sharing': 'none',
                  'local_proxy_arp': 'disabled',
                  'multicast_groups': ['224.0.0.1', '224.0.0.13', '224.0.0.2'],
                  'multicast_routing': 'enabled',
                  'proxy_arp': 'disabled',
                  'unicast_reverse_path': 'none',
                  'vrf': 'vrf-9105'},
        'Vlan1006': {'directed_broadcast': 'disabled',
                  'icmp_port_unreachable': 'enabled',
                  'icmp_redirects': 'disabled',
                  'icmp_unreachable': 'disabled',
                  'int_stat_last_reset': 'never',
                  'interface_status': 'protocol-up/link-up/admin-up',
                  'iod': 88,
                  'ip_forwarding': 'enabled',
                  'ip_mtu': 1500,
                  'ipv4': {'counters': {'broadcast_bytes_consumed': 0,
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
                                        'multicast_bytes_originated': 1496,
                                        'multicast_bytes_received': 0,
                                        'multicast_bytes_sent': 1496,
                                        'multicast_packets_consumed': 0,
                                        'multicast_packets_forwarded': 0,
                                        'multicast_packets_originated': 22,
                                        'multicast_packets_received': 0,
                                        'multicast_packets_sent': 22,
                                        'unicast_bytes_consumed': 0,
                                        'unicast_bytes_forwarded': 0,
                                        'unicast_bytes_originated': 0,
                                        'unicast_bytes_received': 0,
                                        'unicast_bytes_sent': 0,
                                        'unicast_packets_consumed': 0,
                                        'unicast_packets_forwarded': 0,
                                        'unicast_packets_originated': 0,
                                        'unicast_packets_received': 0,
                                        'unicast_packets_sent': 0},
                           'none': {'broadcast_address': '255.255.255.255',
                                    'ip': 'none'}},
                  'load_sharing': 'none',
                  'local_proxy_arp': 'disabled',
                  'multicast_groups': ['224.0.0.1', '224.0.0.13', '224.0.0.2'],
                  'multicast_routing': 'enabled',
                  'proxy_arp': 'disabled',
                  'unicast_reverse_path': 'none',
                  'vrf': 'vrf-9106'},
        'Vlan1007': {'directed_broadcast': 'disabled',
                  'icmp_port_unreachable': 'enabled',
                  'icmp_redirects': 'disabled',
                  'icmp_unreachable': 'disabled',
                  'int_stat_last_reset': 'never',
                  'interface_status': 'protocol-up/link-up/admin-up',
                  'iod': 89,
                  'ip_forwarding': 'enabled',
                  'ip_mtu': 1500,
                  'ipv4': {'counters': {'broadcast_bytes_consumed': 0,
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
                                        'multicast_bytes_originated': 1496,
                                        'multicast_bytes_received': 0,
                                        'multicast_bytes_sent': 1496,
                                        'multicast_packets_consumed': 0,
                                        'multicast_packets_forwarded': 0,
                                        'multicast_packets_originated': 22,
                                        'multicast_packets_received': 0,
                                        'multicast_packets_sent': 22,
                                        'unicast_bytes_consumed': 0,
                                        'unicast_bytes_forwarded': 0,
                                        'unicast_bytes_originated': 0,
                                        'unicast_bytes_received': 0,
                                        'unicast_bytes_sent': 0,
                                        'unicast_packets_consumed': 0,
                                        'unicast_packets_forwarded': 0,
                                        'unicast_packets_originated': 0,
                                        'unicast_packets_received': 0,
                                        'unicast_packets_sent': 0},
                           'none': {'broadcast_address': '255.255.255.255',
                                    'ip': 'none'}},
                  'load_sharing': 'none',
                  'local_proxy_arp': 'disabled',
                  'multicast_groups': ['224.0.0.1', '224.0.0.13', '224.0.0.2'],
                  'multicast_routing': 'enabled',
                  'proxy_arp': 'disabled',
                  'unicast_reverse_path': 'none',
                  'vrf': 'vrf-9107'},
        'Vlan1008': {'directed_broadcast': 'disabled',
                  'icmp_port_unreachable': 'enabled',
                  'icmp_redirects': 'disabled',
                  'icmp_unreachable': 'disabled',
                  'int_stat_last_reset': 'never',
                  'interface_status': 'protocol-up/link-up/admin-up',
                  'iod': 90,
                  'ip_forwarding': 'enabled',
                  'ip_mtu': 1500,
                  'ipv4': {'counters': {'broadcast_bytes_consumed': 0,
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
                                        'multicast_bytes_originated': 1496,
                                        'multicast_bytes_received': 0,
                                        'multicast_bytes_sent': 1496,
                                        'multicast_packets_consumed': 0,
                                        'multicast_packets_forwarded': 0,
                                        'multicast_packets_originated': 22,
                                        'multicast_packets_received': 0,
                                        'multicast_packets_sent': 22,
                                        'unicast_bytes_consumed': 0,
                                        'unicast_bytes_forwarded': 0,
                                        'unicast_bytes_originated': 0,
                                        'unicast_bytes_received': 0,
                                        'unicast_bytes_sent': 0,
                                        'unicast_packets_consumed': 0,
                                        'unicast_packets_forwarded': 0,
                                        'unicast_packets_originated': 0,
                                        'unicast_packets_received': 0,
                                        'unicast_packets_sent': 0},
                           'none': {'broadcast_address': '255.255.255.255',
                                    'ip': 'none'}},
                  'load_sharing': 'none',
                  'local_proxy_arp': 'disabled',
                  'multicast_groups': ['224.0.0.1', '224.0.0.13', '224.0.0.2'],
                  'multicast_routing': 'enabled',
                  'proxy_arp': 'disabled',
                  'unicast_reverse_path': 'none',
                  'vrf': 'vrf-9108'},
        'Vlan1009': {'directed_broadcast': 'disabled',
                  'icmp_port_unreachable': 'enabled',
                  'icmp_redirects': 'disabled',
                  'icmp_unreachable': 'disabled',
                  'int_stat_last_reset': 'never',
                  'interface_status': 'protocol-up/link-up/admin-up',
                  'iod': 91,
                  'ip_forwarding': 'enabled',
                  'ip_mtu': 1500,
                  'ipv4': {'counters': {'broadcast_bytes_consumed': 0,
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
                                        'multicast_bytes_originated': 1428,
                                        'multicast_bytes_received': 0,
                                        'multicast_bytes_sent': 1428,
                                        'multicast_packets_consumed': 0,
                                        'multicast_packets_forwarded': 0,
                                        'multicast_packets_originated': 21,
                                        'multicast_packets_received': 0,
                                        'multicast_packets_sent': 21,
                                        'unicast_bytes_consumed': 0,
                                        'unicast_bytes_forwarded': 0,
                                        'unicast_bytes_originated': 0,
                                        'unicast_bytes_received': 0,
                                        'unicast_bytes_sent': 0,
                                        'unicast_packets_consumed': 0,
                                        'unicast_packets_forwarded': 0,
                                        'unicast_packets_originated': 0,
                                        'unicast_packets_received': 0,
                                        'unicast_packets_sent': 0},
                           'none': {'broadcast_address': '255.255.255.255',
                                    'ip': 'none'}},
                  'load_sharing': 'none',
                  'local_proxy_arp': 'disabled',
                  'multicast_groups': ['224.0.0.1', '224.0.0.13', '224.0.0.2'],
                  'multicast_routing': 'enabled',
                  'proxy_arp': 'disabled',
                  'unicast_reverse_path': 'none',
                  'vrf': 'vrf-9109'},
        'Vlan101': {'directed_broadcast': 'disabled',
                 'icmp_port_unreachable': 'enabled',
                 'icmp_redirects': 'disabled',
                 'icmp_unreachable': 'disabled',
                 'int_stat_last_reset': 'never',
                 'interface_status': 'protocol-up/link-up/admin-up',
                 'iod': 72,
                 'ip_forwarding': 'disabled',
                 'ip_mtu': 1500,
                 'ipv4': {'10.220.12.1/24': {'broadcast_address': '255.255.255.255',
                                              'ip': '10.220.12.1',
                                              'ip_subnet': '10.220.12.0',
                                              'prefix_length': '24',
                                              'route_preference': '0',
                                              'route_tag': '0'},
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
                                       'multicast_bytes_originated': 2048,
                                       'multicast_bytes_received': 0,
                                       'multicast_bytes_sent': 2048,
                                       'multicast_packets_consumed': 0,
                                       'multicast_packets_forwarded': 0,
                                       'multicast_packets_originated': 23,
                                       'multicast_packets_received': 0,
                                       'multicast_packets_sent': 23,
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
                 'multicast_groups': ['224.0.0.1', '224.0.0.13', '224.0.0.2'],
                 'multicast_routing': 'enabled',
                 'proxy_arp': 'disabled',
                 'unicast_reverse_path': 'none',
                 'vrf': 'vrf-9100'},
        'Vlan102': {'directed_broadcast': 'disabled',
                 'icmp_port_unreachable': 'enabled',
                 'icmp_redirects': 'disabled',
                 'icmp_unreachable': 'disabled',
                 'int_stat_last_reset': 'never',
                 'interface_status': 'protocol-down/link-down/admin-up',
                 'iod': 73,
                 'ip_forwarding': 'disabled',
                 'ip_mtu': 1500,
                 'ipv4': {'10.220.13.1/24': {'broadcast_address': '255.255.255.255',
                                              'ip': '10.220.13.1',
                                              'ip_subnet': '10.220.13.0',
                                              'prefix_length': '24',
                                              'route_preference': '0',
                                              'route_tag': '0'},
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
                 'multicast_groups': ['224.0.0.1', '224.0.0.13', '224.0.0.2'],
                 'multicast_routing': 'enabled',
                 'proxy_arp': 'disabled',
                 'unicast_reverse_path': 'none',
                 'vrf': 'vrf-9100'},
        'Vlan105': {'directed_broadcast': 'disabled',
                 'icmp_port_unreachable': 'enabled',
                 'icmp_redirects': 'disabled',
                 'icmp_unreachable': 'disabled',
                 'int_stat_last_reset': 'never',
                 'interface_status': 'protocol-up/link-up/admin-up',
                 'iod': 75,
                 'ip_forwarding': 'disabled',
                 'ip_mtu': 1500,
                 'ipv4': {'10.220.16.1/24': {'broadcast_address': '255.255.255.255',
                                              'ip': '10.220.16.1',
                                              'ip_subnet': '10.220.16.0',
                                              'prefix_length': '24',
                                              'route_preference': '0',
                                              'route_tag': '0'},
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
                                       'multicast_bytes_originated': 2048,
                                       'multicast_bytes_received': 0,
                                       'multicast_bytes_sent': 2048,
                                       'multicast_packets_consumed': 0,
                                       'multicast_packets_forwarded': 0,
                                       'multicast_packets_originated': 23,
                                       'multicast_packets_received': 0,
                                       'multicast_packets_sent': 23,
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
                 'multicast_groups': ['224.0.0.1', '224.0.0.13', '224.0.0.2'],
                 'multicast_routing': 'enabled',
                 'proxy_arp': 'disabled',
                 'unicast_reverse_path': 'none',
                 'vrf': 'vrf-9105'},
        'Vlan106': {'directed_broadcast': 'disabled',
                 'icmp_port_unreachable': 'enabled',
                 'icmp_redirects': 'disabled',
                 'icmp_unreachable': 'disabled',
                 'int_stat_last_reset': 'never',
                 'interface_status': 'protocol-up/link-up/admin-up',
                 'iod': 76,
                 'ip_forwarding': 'disabled',
                 'ip_mtu': 1500,
                 'ipv4': {'10.220.17.1/24': {'broadcast_address': '255.255.255.255',
                                              'ip': '10.220.17.1',
                                              'ip_subnet': '10.220.17.0',
                                              'prefix_length': '24',
                                              'route_preference': '0',
                                              'route_tag': '0'},
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
                                       'multicast_bytes_originated': 2048,
                                       'multicast_bytes_received': 0,
                                       'multicast_bytes_sent': 2048,
                                       'multicast_packets_consumed': 0,
                                       'multicast_packets_forwarded': 0,
                                       'multicast_packets_originated': 23,
                                       'multicast_packets_received': 0,
                                       'multicast_packets_sent': 23,
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
                 'multicast_groups': ['224.0.0.1', '224.0.0.13', '224.0.0.2'],
                 'multicast_routing': 'enabled',
                 'proxy_arp': 'disabled',
                 'unicast_reverse_path': 'none',
                 'vrf': 'vrf-9106'},
        'Vlan107': {'directed_broadcast': 'disabled',
                 'icmp_port_unreachable': 'enabled',
                 'icmp_redirects': 'disabled',
                 'icmp_unreachable': 'disabled',
                 'int_stat_last_reset': 'never',
                 'interface_status': 'protocol-up/link-up/admin-up',
                 'iod': 77,
                 'ip_forwarding': 'disabled',
                 'ip_mtu': 1500,
                 'ipv4': {'10.220.18.1/24': {'broadcast_address': '255.255.255.255',
                                              'ip': '10.220.18.1',
                                              'ip_subnet': '10.220.18.0',
                                              'prefix_length': '24',
                                              'route_preference': '0',
                                              'route_tag': '0'},
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
                                       'multicast_bytes_originated': 2048,
                                       'multicast_bytes_received': 0,
                                       'multicast_bytes_sent': 2048,
                                       'multicast_packets_consumed': 0,
                                       'multicast_packets_forwarded': 0,
                                       'multicast_packets_originated': 23,
                                       'multicast_packets_received': 0,
                                       'multicast_packets_sent': 23,
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
                 'multicast_groups': ['224.0.0.1', '224.0.0.13', '224.0.0.2'],
                 'multicast_routing': 'enabled',
                 'proxy_arp': 'disabled',
                 'unicast_reverse_path': 'none',
                 'vrf': 'vrf-9107'},
        'Vlan108': {'directed_broadcast': 'disabled',
                 'icmp_port_unreachable': 'enabled',
                 'icmp_redirects': 'disabled',
                 'icmp_unreachable': 'disabled',
                 'int_stat_last_reset': 'never',
                 'interface_status': 'protocol-up/link-up/admin-up',
                 'iod': 78,
                 'ip_forwarding': 'disabled',
                 'ip_mtu': 1500,
                 'ipv4': {'10.220.19.1/24': {'broadcast_address': '255.255.255.255',
                                              'ip': '10.220.19.1',
                                              'ip_subnet': '10.220.19.0',
                                              'prefix_length': '24',
                                              'route_preference': '0',
                                              'route_tag': '0'},
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
                                       'multicast_bytes_originated': 2048,
                                       'multicast_bytes_received': 0,
                                       'multicast_bytes_sent': 2048,
                                       'multicast_packets_consumed': 0,
                                       'multicast_packets_forwarded': 0,
                                       'multicast_packets_originated': 23,
                                       'multicast_packets_received': 0,
                                       'multicast_packets_sent': 23,
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
                 'multicast_groups': ['224.0.0.1', '224.0.0.13', '224.0.0.2'],
                 'multicast_routing': 'enabled',
                 'proxy_arp': 'disabled',
                 'unicast_reverse_path': 'none',
                 'vrf': 'vrf-9108'},
        'Vlan109': {'directed_broadcast': 'disabled',
                 'icmp_port_unreachable': 'enabled',
                 'icmp_redirects': 'disabled',
                 'icmp_unreachable': 'disabled',
                 'int_stat_last_reset': 'never',
                 'interface_status': 'protocol-up/link-up/admin-up',
                 'iod': 79,
                 'ip_forwarding': 'disabled',
                 'ip_mtu': 1500,
                 'ipv4': {'10.220.20.1/24': {'broadcast_address': '255.255.255.255',
                                              'ip': '10.220.20.1',
                                              'ip_subnet': '10.220.20.0',
                                              'prefix_length': '24',
                                              'route_preference': '0',
                                              'route_tag': '0'},
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
                                       'multicast_bytes_originated': 2048,
                                       'multicast_bytes_received': 0,
                                       'multicast_bytes_sent': 2048,
                                       'multicast_packets_consumed': 0,
                                       'multicast_packets_forwarded': 0,
                                       'multicast_packets_originated': 23,
                                       'multicast_packets_received': 0,
                                       'multicast_packets_sent': 23,
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
                 'multicast_groups': ['224.0.0.1', '224.0.0.13', '224.0.0.2'],
                 'multicast_routing': 'enabled',
                 'proxy_arp': 'disabled',
                 'unicast_reverse_path': 'none',
                 'vrf': 'vrf-9109'},
        'Vlan110': {'directed_broadcast': 'disabled',
                 'icmp_port_unreachable': 'enabled',
                 'icmp_redirects': 'disabled',
                 'icmp_unreachable': 'disabled',
                 'int_stat_last_reset': 'never',
                 'interface_status': 'protocol-up/link-up/admin-up',
                 'iod': 80,
                 'ip_forwarding': 'disabled',
                 'ip_mtu': 1500,
                 'ipv4': {'10.220.21.1/24': {'broadcast_address': '255.255.255.255',
                                              'ip': '10.220.21.1',
                                              'ip_subnet': '10.220.21.0',
                                              'prefix_length': '24',
                                              'route_preference': '0',
                                              'route_tag': '0'},
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
                                       'multicast_bytes_originated': 2048,
                                       'multicast_bytes_received': 0,
                                       'multicast_bytes_sent': 2048,
                                       'multicast_packets_consumed': 0,
                                       'multicast_packets_forwarded': 0,
                                       'multicast_packets_originated': 23,
                                       'multicast_packets_received': 0,
                                       'multicast_packets_sent': 23,
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
                 'multicast_groups': ['224.0.0.1', '224.0.0.13', '224.0.0.2'],
                 'multicast_routing': 'enabled',
                 'proxy_arp': 'disabled',
                 'unicast_reverse_path': 'none',
                 'vrf': 'vrf-9105'},
        'Vlan111': {'directed_broadcast': 'disabled',
                 'icmp_port_unreachable': 'enabled',
                 'icmp_redirects': 'disabled',
                 'icmp_unreachable': 'disabled',
                 'int_stat_last_reset': 'never',
                 'interface_status': 'protocol-up/link-up/admin-up',
                 'iod': 81,
                 'ip_forwarding': 'disabled',
                 'ip_mtu': 1500,
                 'ipv4': {'10.220.22.1/24': {'broadcast_address': '255.255.255.255',
                                              'ip': '10.220.22.1',
                                              'ip_subnet': '10.220.22.0',
                                              'prefix_length': '24',
                                              'route_preference': '0',
                                              'route_tag': '0'},
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
                                       'multicast_bytes_originated': 2048,
                                       'multicast_bytes_received': 0,
                                       'multicast_bytes_sent': 2048,
                                       'multicast_packets_consumed': 0,
                                       'multicast_packets_forwarded': 0,
                                       'multicast_packets_originated': 23,
                                       'multicast_packets_received': 0,
                                       'multicast_packets_sent': 23,
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
                 'multicast_groups': ['224.0.0.1', '224.0.0.13', '224.0.0.2'],
                 'multicast_routing': 'enabled',
                 'proxy_arp': 'disabled',
                 'unicast_reverse_path': 'none',
                 'vrf': 'vrf-9106'},
        'Vlan112': {'directed_broadcast': 'disabled',
                 'icmp_port_unreachable': 'enabled',
                 'icmp_redirects': 'disabled',
                 'icmp_unreachable': 'disabled',
                 'int_stat_last_reset': 'never',
                 'interface_status': 'protocol-up/link-up/admin-up',
                 'iod': 82,
                 'ip_forwarding': 'disabled',
                 'ip_mtu': 1500,
                 'ipv4': {'10.220.23.1/24': {'broadcast_address': '255.255.255.255',
                                              'ip': '10.220.23.1',
                                              'ip_subnet': '10.220.23.0',
                                              'prefix_length': '24',
                                              'route_preference': '0',
                                              'route_tag': '0'},
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
                                       'multicast_bytes_originated': 2048,
                                       'multicast_bytes_received': 0,
                                       'multicast_bytes_sent': 2048,
                                       'multicast_packets_consumed': 0,
                                       'multicast_packets_forwarded': 0,
                                       'multicast_packets_originated': 23,
                                       'multicast_packets_received': 0,
                                       'multicast_packets_sent': 23,
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
                 'multicast_groups': ['224.0.0.1', '224.0.0.13', '224.0.0.2'],
                 'multicast_routing': 'enabled',
                 'proxy_arp': 'disabled',
                 'unicast_reverse_path': 'none',
                 'vrf': 'vrf-9107'},
        'Vlan113': {'directed_broadcast': 'disabled',
                 'icmp_port_unreachable': 'enabled',
                 'icmp_redirects': 'disabled',
                 'icmp_unreachable': 'disabled',
                 'int_stat_last_reset': 'never',
                 'interface_status': 'protocol-up/link-up/admin-up',
                 'iod': 83,
                 'ip_forwarding': 'disabled',
                 'ip_mtu': 1500,
                 'ipv4': {'10.220.24.1/24': {'broadcast_address': '255.255.255.255',
                                              'ip': '10.220.24.1',
                                              'ip_subnet': '10.220.24.0',
                                              'prefix_length': '24',
                                              'route_preference': '0',
                                              'route_tag': '0'},
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
                                       'multicast_bytes_originated': 2048,
                                       'multicast_bytes_received': 0,
                                       'multicast_bytes_sent': 2048,
                                       'multicast_packets_consumed': 0,
                                       'multicast_packets_forwarded': 0,
                                       'multicast_packets_originated': 23,
                                       'multicast_packets_received': 0,
                                       'multicast_packets_sent': 23,
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
                 'multicast_groups': ['224.0.0.1', '224.0.0.13', '224.0.0.2'],
                 'multicast_routing': 'enabled',
                 'proxy_arp': 'disabled',
                 'unicast_reverse_path': 'none',
                 'vrf': 'vrf-9108'},
        'Vlan114': {'directed_broadcast': 'disabled',
                 'icmp_port_unreachable': 'enabled',
                 'icmp_redirects': 'disabled',
                 'icmp_unreachable': 'disabled',
                 'int_stat_last_reset': 'never',
                 'interface_status': 'protocol-up/link-up/admin-up',
                 'iod': 84,
                 'ip_forwarding': 'disabled',
                 'ip_mtu': 1500,
                 'ipv4': {'10.220.25.1/24': {'broadcast_address': '255.255.255.255',
                                              'ip': '10.220.25.1',
                                              'ip_subnet': '10.220.25.0',
                                              'prefix_length': '24',
                                              'route_preference': '0',
                                              'route_tag': '0'},
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
                                       'multicast_bytes_originated': 2048,
                                       'multicast_bytes_received': 0,
                                       'multicast_bytes_sent': 2048,
                                       'multicast_packets_consumed': 0,
                                       'multicast_packets_forwarded': 0,
                                       'multicast_packets_originated': 23,
                                       'multicast_packets_received': 0,
                                       'multicast_packets_sent': 23,
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
                 'multicast_groups': ['224.0.0.1', '224.0.0.13', '224.0.0.2'],
                 'multicast_routing': 'enabled',
                 'proxy_arp': 'disabled',
                 'unicast_reverse_path': 'none',
                 'vrf': 'vrf-9109'},
        'Vlan910': {'directed_broadcast': 'disabled',
                 'icmp_port_unreachable': 'enabled',
                 'icmp_redirects': 'enabled',
                 'icmp_unreachable': 'disabled',
                 'int_stat_last_reset': 'never',
                 'interface_status': 'protocol-down/link-down/admin-up',
                 'iod': 85,
                 'ip_forwarding': 'enabled',
                 'ip_mtu': 1500,
                 'ipv4': {'counters': {'broadcast_bytes_consumed': 0,
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
                                       'unicast_packets_sent': 0},
                          'none': {'broadcast_address': '255.255.255.255',
                                   'ip': 'none'}},
                 'load_sharing': 'none',
                 'local_proxy_arp': 'disabled',
                 'multicast_groups_address': 'none',
                 'multicast_routing': 'disabled',
                 'proxy_arp': 'disabled',
                 'unicast_reverse_path': 'none',
                 'vrf': 'vrf-9100'},
        'loopback0': {'directed_broadcast': 'disabled',
                   'icmp_port_unreachable': 'enabled',
                   'icmp_redirects': 'enabled',
                   'icmp_unreachable': 'disabled',
                   'int_stat_last_reset': 'never',
                   'interface_status': 'protocol-up/link-up/admin-up',
                   'iod': 94,
                   'ip_forwarding': 'disabled',
                   'ip_mtu': 1500,
                   'ipv4': {'10.49.1.0/32': {'broadcast_address': '255.255.255.255',
                                            'ip': '10.49.1.0',
                                            'ip_subnet': '10.49.1.0',
                                            'prefix_length': '32',
                                            'route_preference': '0',
                                            'route_tag': '0'},
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
                   'multicast_groups': ['224.0.0.1', '224.0.0.13', '224.0.0.2'],
                   'multicast_routing': 'enabled',
                   'proxy_arp': 'disabled',
                   'unicast_reverse_path': 'none',
                   'vrf': 'default'},
        'loopback1': {'directed_broadcast': 'disabled',
                   'icmp_port_unreachable': 'enabled',
                   'icmp_redirects': 'disabled',
                   'icmp_unreachable': 'disabled',
                   'int_stat_last_reset': 'never',
                   'interface_status': 'protocol-down/link-down/admin-up',
                   'iod': 95,
                   'ip_forwarding': 'disabled',
                   'ip_mtu': 1500,
                   'ipv4': {'10.49.1.1/32': {'ip': '10.49.1.1',
                                                'ip_subnet': '10.49.1.1',
                                                'prefix_length': '32',
                                                'route_preference': '0',
                                                'route_tag': '0'},
                             '10.49.2.1/32': {'broadcast_address': '255.255.255.255',
                                                 'ip': '10.49.2.1',
                                                 'ip_subnet': '10.49.2.1',
                                                 'prefix_length': '32',
                                                 'route_preference': '0',
                                                 'route_tag': '0',
                                                 'secondary': True},
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
                                         'multicast_bytes_consumed': 35184,
                                         'multicast_bytes_forwarded': 0,
                                         'multicast_bytes_originated': 0,
                                         'multicast_bytes_received': 35184,
                                         'multicast_bytes_sent': 0,
                                         'multicast_packets_consumed': 312,
                                         'multicast_packets_forwarded': 0,
                                         'multicast_packets_originated': 0,
                                         'multicast_packets_received': 312,
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
                   'multicast_groups': ['224.0.0.1', '224.0.0.13', '224.0.0.2'],
                   'multicast_routing': 'enabled',
                   'proxy_arp': 'disabled',
                   'unicast_reverse_path': 'none',
                   'vrf': 'default'},
        'mgmt0': {'directed_broadcast': 'disabled',
               'icmp_port_unreachable': 'enabled',
               'icmp_redirects': 'enabled',
               'icmp_unreachable': 'disabled',
               'int_stat_last_reset': 'never',
               'interface_status': 'protocol-up/link-up/admin-up',
               'iod': 2,
               'ip_forwarding': 'disabled',
               'ip_mtu': 1500,
               'ipv4': {'10.1.6.40/24': {'broadcast_address': '255.255.255.255',
                                         'ip': '10.1.6.40',
                                         'ip_subnet': '10.1.6.0',
                                         'prefix_length': '24',
                                         'route_preference': '0',
                                         'route_tag': '0'},
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
                                     'unicast_bytes_consumed': 115792,
                                     'unicast_bytes_forwarded': 0,
                                     'unicast_bytes_originated': 343014,
                                     'unicast_bytes_received': 57896,
                                     'unicast_bytes_sent': 343014,
                                     'unicast_packets_consumed': 1592,
                                     'unicast_packets_forwarded': 0,
                                     'unicast_packets_originated': 805,
                                     'unicast_packets_received': 796,
                                     'unicast_packets_sent': 805}},
               'load_sharing': 'none',
               'local_proxy_arp': 'disabled',
               'multicast_groups_address': 'none',
               'multicast_routing': 'disabled',
               'proxy_arp': 'disabled',
               'unicast_reverse_path': 'none',
               'vrf': 'management'}}

    golden_output_6 = {'execute.return_value': '''
    Vlan300, Interface status: protocol-up/link-up/admin-up, iod: 7,
      IP address: 10.115.65.2, IP subnet: 10.115.65.0/24 route-preference: 0, tag: 0
      IP address: 10.115.69.2, IP subnet: 10.115.69.0/24 secondary route-preference: 0, tag: 0
      IP address: 10.115.72.2, IP subnet: 10.115.72.0/24 secondary route-preference: 0, tag: 0
      IP address: 10.115.77.2, IP subnet: 10.115.77.0/24 secondary route-preference: 0, tag: 0
      IP broadcast address: 255.255.255.255
      IP multicast groups locally joined:
          224.0.0.102
      IP MTU: 1500 bytes (using link MTU)
      IP primary address route-preference: 0, tag: 0
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
        Unicast packets    : 9853/3233248/9422/441/9385858
        Unicast bytes      : 1313118/192909900/1272720/41238/498894997
        Multicast packets  : 0/10735961/0/0/21471922
        Multicast bytes    : 0/858876880/0/0/858876880
        Broadcast packets  : 0/0/0/0/0
        Broadcast bytes    : 0/0/0/0/0
        Labeled packets    : 0/0/0/0/0
        Labeled bytes      : 0/0/0/0/0
      WCCP Redirect outbound: disabled
      WCCP Redirect inbound: disabled
      WCCP Redirect exclude: disabled
    '''}

    golden_parsed_output_6 = {
        'Vlan300': {
            'ip_mtu': 1500,
            'wccp_redirect_exclude': 'disabled',
            'proxy_arp': 'disabled',
            'multicast_groups': ['224.0.0.102'],
            'wccp_redirect_inbound': 'disabled',
            'ip_forwarding': 'disabled',
            'icmp_port_unreachable': 'enabled',
            'wccp_redirect_outbound': 'disabled',
            'unicast_reverse_path': 'none',
            'directed_broadcast': 'disabled',
            'icmp_unreachable': 'disabled',
            'local_proxy_arp': 'disabled',
            'ipv4': {
                '10.115.77.2/24': {
                    'broadcast_address': '255.255.255.255',
                    'ip_subnet': '10.115.77.0',
                    'ip': '10.115.77.2',
                    'route_preference': '0',
                    'prefix_length': '24',
                    'route_tag': '0',
                    'secondary': True,
                },
                '10.115.69.2/24': {
                    'ip_subnet': '10.115.69.0',
                    'ip': '10.115.69.2',
                    'route_preference': '0',
                    'prefix_length': '24',
                    'route_tag': '0',
                    'secondary': True,
                },
                'counters': {
                    'unicast_bytes_sent': 1313118,
                    'broadcast_bytes_received': 0,
                    'multicast_bytes_forwarded': 0,
                    'labeled_bytes_received': 0,
                    'unicast_bytes_originated': 41238,
                    'broadcast_bytes_forwarded': 0,
                    'multicast_bytes_consumed': 858876880,
                    'labeled_packets_consumed': 0,
                    'multicast_packets_received': 10735961,
                    'broadcast_bytes_consumed': 0,
                    'broadcast_packets_forwarded': 0,
                    'labeled_bytes_originated': 0,
                    'unicast_packets_consumed': 9385858,
                    'broadcast_packets_received': 0,
                    'broadcast_packets_consumed': 0,
                    'multicast_packets_sent': 0,
                    'unicast_packets_originated': 441,
                    'labeled_packets_forwarded': 0,
                    'unicast_bytes_received': 192909900,
                    'broadcast_packets_originated': 0,
                    'unicast_bytes_forwarded': 1272720,
                    'labeled_packets_received': 0,
                    'multicast_bytes_received': 858876880,
                    'unicast_packets_received': 3233248,
                    'broadcast_bytes_originated': 0,
                    'broadcast_packets_sent': 0,
                    'unicast_packets_sent': 9853,
                    'multicast_packets_forwarded': 0,
                    'labeled_bytes_consumed': 0,
                    'multicast_packets_originated': 0,
                    'multicast_packets_consumed': 21471922,
                    'labeled_bytes_sent': 0,
                    'unicast_packets_forwarded': 9422,
                    'multicast_bytes_originated': 0,
                    'unicast_bytes_consumed': 498894997,
                    'multicast_bytes_sent': 0,
                    'labeled_packets_sent': 0,
                    'labeled_packets_originated': 0,
                    'broadcast_bytes_sent': 0,
                    'labeled_bytes_forwarded': 0,
                },
                '10.115.72.2/24': {
                    'ip_subnet': '10.115.72.0',
                    'ip': '10.115.72.2',
                    'route_preference': '0',
                    'prefix_length': '24',
                    'route_tag': '0',
                    'secondary': True,
                },
                '10.115.65.2/24': {
                    'ip_subnet': '10.115.65.0',
                    'ip': '10.115.65.2',
                    'route_tag': '0',
                    'route_preference': '0',
                    'prefix_length': '24',
                },
            },
            'icmp_redirects': 'disabled',
            'multicast_routing': 'disabled',
            'load_sharing': 'none',
            'interface_status': 'protocol-up/link-up/admin-up',
            'iod': 7,
            'int_stat_last_reset': 'never',
            'vrf': '',
        },
    }
    golden_output_7 = {'execute.return_value': '''
    Vlan300, Interface status: protocol-up/link-up/admin-up, iod: 7,
      IP address: 10.115.65.2, IP subnet: 10.115.65.0/24 route-preference: 0, tag: 0
      IP address: 10.115.69.2, IP subnet: 10.115.69.0/24 secondary route-preference: 0, tag: 0
      IP address: 10.115.72.2, IP subnet: 10.115.72.0/24 secondary route-preference: 0, tag: 0
      IP address: 10.115.77.2, IP subnet: 10.115.77.0/24 secondary route-preference: 0, tag: 0
      IP broadcast address: 255.255.255.255
      IP multicast groups locally joined:
          224.0.0.102
      IP MTU: 1500 bytes (using link MTU)
      IP primary address route-preference: 0, tag:
        0
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
        Unicast packets    : 9853/3233248/9422/441/9385858
        Unicast bytes      : 1313118/192909900/1272720/41238/498894997
        Multicast packets  : 0/10735961/0/0/21471922
        Multicast bytes    : 0/858876880/0/0/858876880
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

    def test_golden_1(self):
        self.device = Mock(**self.golden_output_1)
        ip_interface_vrf_all_obj = ShowIpInterfaceVrfAll(device=self.device)
        parsed_output = ip_interface_vrf_all_obj.parse()
        self.maxDiff = None
        self.assertEqual(parsed_output,self.golden_parsed_output_1)

    def test_golden_2(self):
        self.device = Mock(**self.golden_output_2)
        ip_interface_vrf_all_obj = ShowIpInterfaceVrfAll(device=self.device)
        parsed_output = ip_interface_vrf_all_obj.parse()
        self.maxDiff = None
        self.assertEqual(parsed_output,self.golden_parsed_output_2)

    def test_golden_custom(self):
        self.device = Mock(**self.golden_output_custom)
        ip_interface_vrf_all_obj = ShowIpInterfaceVrfAll(device=self.device)
        parsed_output = ip_interface_vrf_all_obj.parse(vrf='VRF1', interface='Ethernet2/1')
        self.maxDiff = None
        self.assertEqual(parsed_output,self.golden_parsed_output_custom)

    def test_golden_3(self):
        self.device = Mock(**self.golden_output_3)
        ip_interface_vrf_all_obj = ShowIpInterfaceVrfAll(device=self.device)
        parsed_output = ip_interface_vrf_all_obj.parse()
        self.maxDiff = None
        self.assertEqual(parsed_output,self.golden_parsed_output_3)

    def test_golden_4(self):
        self.device = Mock(**self.golden_output_4)
        ip_interface_vrf_all_obj = ShowIpInterfaceVrfAll(device=self.device)
        parsed_output = ip_interface_vrf_all_obj.parse()
        self.maxDiff = None
        self.assertEqual(parsed_output,self.golden_parsed_output_4)

    def test_golden_5(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_5)
        obj = ShowIpInterfaceVrfAll(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_5)

    def test_golden_6(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_6)
        obj = ShowIpInterfaceVrfAll(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_6)

    def test_golden_7(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_7)
        obj = ShowIpInterfaceVrfAll(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_6)

# #############################################################################
# # Unittest For Show Vrf All Interface
# #############################################################################

class TestShowVrfAllInterface(unittest.TestCase):

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
    golden_parsed_output_custom={
        'Ethernet2/1': {'site_of_origin': '--', 'vrf': 'VRF1', 'vrf_id': 3}
    }
    golden_output_custom={'execute.return_value': '''
     Interface                 VRF-Name                        VRF-ID  Site-of-Origin
    Ethernet2/1               VRF1                                 3  --
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

    def test_golden_custom(self):
        self.device = Mock(**self.golden_output_custom)
        vrf_all_interface_obj = ShowVrfAllInterface(device=self.device)
        parsed_output = vrf_all_interface_obj.parse(vrf='VRF1', interface='Ethernet2/1')
        self.maxDiff = None
        self.assertEqual(parsed_output,self.golden_parsed_output_custom)


# #############################################################################
# # Unittest For Show Interface Switchport
# #############################################################################


class TestShowInterfaceSwitchport(unittest.TestCase):

    device = Device(name='aDevice')
    device0 = Device(name='bDevice')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output_1 = {
        'Ethernet2/2':
            {'access_vlan': 1,
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
            'switchport_status': 'enabled',
            'switchport_enable': True,
            'trunk_vlans': '100,300'},
        'Ethernet2/3':
            {'access_vlan': 100,
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
            'switchport_status': 'enabled',
            'switchport_enable': True,
            'trunk_vlans': '1-4094'}}

    golden_output_1 = {'execute.return_value': '''
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

    golden_parsed_output_2 = {
        'port-channel662':
            {'access_vlan': 1,
            'access_vlan_mode': 'default',
            'admin_priv_vlan_primary_host_assoc': 'none',
            'admin_priv_vlan_primary_mapping': 'none',
            'admin_priv_vlan_secondary_host_assoc': 'none',
            'admin_priv_vlan_secondary_mapping': 'none',
            'admin_priv_vlan_trunk_encapsulation': 'dot1q',
            'admin_priv_vlan_trunk_native_vlan': 'none',
            'admin_priv_vlan_trunk_normal_vlans': 'none',
            'admin_priv_vlan_trunk_private_vlans': 'none',
            'native_vlan': 3967,
            'native_vlan_mode': 'Vlan not created',
            'operational_private_vlan': 'none',
            'switchport_enable': True,
            'switchport_mode': 'trunk',
            'switchport_monitor': 'Not enabled',
            'switchport_status': 'enabled',
            'trunk_vlans': '2600-26507,2610,2620,2630,2640,2690,2698-2699'}}

    golden_output_2 = {'execute.return_value': '''
        Name: port-channel662
          Switchport: Enabled
          Switchport Monitor: Not enabled
          Operational Mode: trunk
          Access Mode VLAN: 1 (default)
          Trunking Native Mode VLAN: 3967 (Vlan not created)
          Trunking VLANs Allowed: 2600-26507,2610,2620,2630,2640,2690,2698-2699
          FabricPath Topology List Allowed: 0
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
    golden_parsed_output_custom= {
        'Ethernet2/2':
            {'access_vlan': 1,
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
            'switchport_status': 'enabled',
            'switchport_enable': True,
            'trunk_vlans': '100,300'},
    }
    golden_output_custom = {'execute.return_value': '''
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
              '''}
    golden_parsed_output_disabled = {
        'Ethernet1/1':{
            'switchport_status': 'disabled',
            'switchport_enable': False,
        }
    }
    golden_output_disabled={'execute.return_value': '''
    Name: Ethernet1/1
        Switchport: Disabled
    '''}
    def test_empty(self):
        self.device1 = Mock(**self.empty_output)
        interface_switchport_obj = ShowInterfaceSwitchport(device=self.device1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = interface_switchport_obj.parse()

    def test_golden_1(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_1)
        interface_switchport_obj = ShowInterfaceSwitchport(device=self.device)
        parsed_output = interface_switchport_obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_1)

    def test_golden_2(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_2)
        interface_switchport_obj = ShowInterfaceSwitchport(device=self.device)
        parsed_output = interface_switchport_obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_2)

    def test_golden_custom(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_custom)
        interface_switchport_obj = ShowInterfaceSwitchport(device=self.device)
        parsed_output = interface_switchport_obj.parse(interface='Ethernet2/2')
        self.assertEqual(parsed_output, self.golden_parsed_output_custom)

    def test_golden_disabled(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_disabled)
        interface_switchport_obj = ShowInterfaceSwitchport(device=self.device)
        parsed_output = interface_switchport_obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_disabled)

# #############################################################################
# # Unittest For Show Ipv6 Interface Vrf All
# #############################################################################


class TestShowIpv6InterfaceVrfAll(unittest.TestCase):

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
                          '2001:db8:4:4:a8aa:bbff:feff:8888/64': {'ip': '2001:db8:4:4:a8aa:bbff:feff:8888',
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
                          'ipv6_link_local': 'fe80::a8aa:bbff:feff:8888 ',
                          'ipv6_link_local_state': 'default',
                          'ipv6_ll_state': 'valid',
                          'ipv6_load_sharing': 'none',
                          'ipv6_mtu': 1600,
                          'ipv6_multicast_groups': ['ff02::1',
                                                    'ff02::1:ff00:0',
                                                    'ff02::1:ff00:1',
                                                    'ff02::1:ff00:2',
                                                    'ff02::1:ff00:3',
                                                    'ff02::1:ffbb:cccc',
                                                    'ff02::1:ffbb:cccc',
                                                    'ff02::2'],
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
            2001:db8:4:4:a8aa:bbff:feff:8888/64 [VALID]
            2001:db8:2:2::2/64 [VALID]
          IPv6 subnet:  2001:db8:1:1::/64
          Anycast configured addresses:
            2001:db8:2:2::2/64 [VALID]
          IPv6 link-local address: fe80::a8aa:bbff:feff:8888 (default) [VALID]
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

    golden_parsed_output_custom={'Ethernet2/1': {'enabled': True,
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
                          '2001:db8:4:4:a8aa:bbff:feff:8888/64': {'ip': '2001:db8:4:4:a8aa:bbff:feff:8888',
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
                          'ipv6_link_local': 'fe80::a8aa:bbff:feff:8888 ',
                          'ipv6_link_local_state': 'default',
                          'ipv6_ll_state': 'valid',
                          'ipv6_load_sharing': 'none',
                          'ipv6_mtu': 1600,
                          'ipv6_multicast_groups': ['ff02::1',
                                                    'ff02::1:ff00:0',
                                                    'ff02::1:ff00:1',
                                                    'ff02::1:ff00:2',
                                                    'ff02::1:ff00:3',
                                                    'ff02::1:ffbb:cccc',
                                                    'ff02::1:ffbb:cccc',
                                                    'ff02::2'],
                          'ipv6_multicast_routing': 'disabled',
                          'ipv6_report_link_local': 'disabled',
                          'ipv6_subnet': '2001:db8:1:1::/64',
                          'ipv6_unicast_rev_path_forwarding': 'none',
                          'ipv6_virtual_add': 'none',
                          'multicast_groups': True},
                 'vrf': 'VRF1'}}
    golden_output_custom = {
        'execute.return_value': '''
            IPv6 Interface Status for VRF "VRF1"
            Ethernet2/1, Interface status: protocol-up/link-up/admin-up, iod: 36
              IPv6 address:
                2001:db8:1:1::1/64 [VALID]
                2001:db8:3:3::3/64 [VALID]
                2001:db8:4:4:a8aa:bbff:feff:8888/64 [VALID]
                2001:db8:2:2::2/64 [VALID]
              IPv6 subnet:  2001:db8:1:1::/64
              Anycast configured addresses:
                2001:db8:2:2::2/64 [VALID]
              IPv6 link-local address: fe80::a8aa:bbff:feff:8888 (default) [VALID]
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
          '''
    }

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

    def test_golden_custom(self):
        self.device = Mock(**self.golden_output_custom)
        ipv6_interface_vrf_all_obj = ShowIpv6InterfaceVrfAll(device=self.device)
        parsed_output = ipv6_interface_vrf_all_obj.parse(vrf='VRF1', interface='Ethernet2/1')
        self.maxDiff = None
        self.assertEqual(parsed_output,self.golden_parsed_output_custom)


class TestShowIpInterfaceBrief(unittest.TestCase):
    device = Device(name='aDevice')
    device1 = Device(name='bDevice')
    empty_output = {'execute.return_value': ''}
    golden_parsed_output = {'interface':
                                {'Eth5/48.106':
                                    {'interface_status': 'protocol-down/link-down/admin-up', 'ip_address': '10.81.6.1'},
                                 'Lo3':
                                    {'interface_status': 'protocol-up/link-up/admin-up', 'ip_address': '192.168.205.1'},
                                 'Po1.102':
                                    {'interface_status': 'protocol-up/link-up/admin-up', 'ip_address': '192.168.70.2'},
                                 'Lo11':
                                    {'interface_status': 'protocol-up/link-up/admin-up', 'ip_address': '192.168.151.1'},
                                 'Vlan23':
                                    {'vlan_id':
                                        {'23':
                                            {'interface_status': 'protocol-up/link-up/admin-up', 'ip_address': '192.168.186.1'}}},
                                 'Eth5/48.101':
                                    {'interface_status': 'protocol-down/link-down/admin-up', 'ip_address': '10.81.1.1'},
                                 'Eth5/48.102':
                                    {'interface_status': 'protocol-down/link-down/admin-up', 'ip_address': '10.81.2.1'},
                                 'Eth5/48.105':
                                    {'interface_status': 'protocol-down/link-down/admin-up', 'ip_address': '10.81.5.1'},
                                 'Lo2':
                                    {'interface_status': 'protocol-up/link-up/admin-up', 'ip_address': '192.168.51.1'},
                                 'Lo1':
                                    {'interface_status': 'protocol-up/link-up/admin-up', 'ip_address': '192.168.154.1'},
                                 'Eth6/22':
                                    {'interface_status': 'protocol-up/link-up/admin-up', 'ip_address': '192.168.145.1'},
                                 'Po1.101':
                                    {'interface_status': 'protocol-up/link-up/admin-up', 'ip_address': '192.168.151.2'},
                                 'Lo10':
                                    {'interface_status': 'protocol-up/link-up/admin-up', 'ip_address': '192.168.64.1'},
                                 'Po1.103':
                                    {'interface_status': 'protocol-up/link-up/admin-up', 'ip_address': '192.168.246.2'},
                                 'Eth5/48.100':
                                    {'interface_status': 'protocol-down/link-down/admin-up', 'ip_address': '10.81.0.1'},
                                 'Po2.107':
                                    {'interface_status': 'protocol-up/link-up/admin-up', 'ip_address': '192.168.66.1'},
                                 'Eth5/48.103':
                                    {'interface_status': 'protocol-down/link-down/admin-up', 'ip_address': '10.81.3.1'},
                                 'tunnel-te12':
                                    {'interface_status': 'protocol-up/link-up/admin-up', 'ip_address': 'unnumbered(loopback0)'},
                                 'Eth5/48.110':
                                    {'interface_status': 'protocol-down/link-down/admin-up', 'ip_address': '10.81.10.1'},
                                 'Po2.103':
                                    {'interface_status': 'protocol-up/link-up/admin-up', 'ip_address': '192.168.19.1'},
                                 'Lo0':
                                    {'interface_status': 'protocol-up/link-up/admin-up', 'ip_address': '192.168.4.1'},
                                 'Po2.101':
                                    {'interface_status': 'protocol-up/link-up/admin-up', 'ip_address': '192.168.135.1'},
                                 'Po2.100':
                                    {'interface_status': 'protocol-up/link-up/admin-up', 'ip_address': '192.168.196.1'},
                                 'tunnel-te11':
                                    {'interface_status': 'protocol-up/link-up/admin-up', 'ip_address': 'unnumbered(loopback0)'},
                                 'Po2.102':
                                    {'interface_status': 'protocol-up/link-up/admin-up', 'ip_address': '192.168.76.1'},
                                 'Eth5/48.104':
                                    {'interface_status': 'protocol-down/link-down/admin-up', 'ip_address': '10.81.4.1'}
                                }
                            }

    golden_output = {'execute.return_value': '''
 IP Interface Status for VRF "default"(1)
 Interface            IP Address      Interface Status
 Vlan23               192.168.186.1     protocol-up/link-up/admin-up
 Lo0                  192.168.4.1       protocol-up/link-up/admin-up
 Lo1                  192.168.154.1       protocol-up/link-up/admin-up
 Lo2                  192.168.51.1       protocol-up/link-up/admin-up
 Lo3                  192.168.205.1       protocol-up/link-up/admin-up
 Lo10                 192.168.64.1      protocol-up/link-up/admin-up
 Lo11                 192.168.151.1      protocol-up/link-up/admin-up
 Po2.100              192.168.196.1      protocol-up/link-up/admin-up
 Po1.101              192.168.151.2      protocol-up/link-up/admin-up
 Po2.101              192.168.135.1      protocol-up/link-up/admin-up
 Po1.102              192.168.70.2      protocol-up/link-up/admin-up
 Po2.102              192.168.76.1      protocol-up/link-up/admin-up
 Po1.103              192.168.246.2      protocol-up/link-up/admin-up
 Po2.103              192.168.19.1      protocol-up/link-up/admin-up
 Po2.107              192.168.66.1      protocol-up/link-up/admin-up
 Eth5/48.100          10.81.0.1       protocol-down/link-down/admin-up
 Eth5/48.101          10.81.1.1       protocol-down/link-down/admin-up
 Eth5/48.102          10.81.2.1       protocol-down/link-down/admin-up
 Eth5/48.103          10.81.3.1       protocol-down/link-down/admin-up
 Eth5/48.104          10.81.4.1       protocol-down/link-down/admin-up
 Eth5/48.105          10.81.5.1       protocol-down/link-down/admin-up
 Eth5/48.106          10.81.6.1       protocol-down/link-down/admin-up
 Eth5/48.110          10.81.10.1      protocol-down/link-down/admin-up
 Eth6/22              192.168.145.1     protocol-up/link-up/admin-up
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


class TestShowIpInterfaceBriefPipeVlan(unittest.TestCase):
    device = Device(name='aDevice')
    device1 = Device(name='bDevice')
    empty_output = {'execute.return_value': ''}
    golden_parsed_output = {'interface':
                                {'Vlan98':
                                    {'vlan_id':
                                        {'98':
                                            {'interface_status': 'protocol-down/link-down/admin-up', 'ip_address': '192.168.234.1'}
                                        }
                                    }
                                }
                            }

    golden_output = {'execute.return_value': '''
 Vlan98               192.168.234.1      protocol-down/link-down/admin-up
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

# ====================================
# Unit test for 'show interface brief'
# ====================================


class TestShowInterfaceBrief(unittest.TestCase):
    device = Device(name='aDevice')
    device1 = Device(name='bDevice')
    maxDiff = None

    empty_output = {'execute.return_value': ''}

    golden_parsed_output = {'interface':
                              {'ethernet':
                                {'Ethernet1/1': {'mode': 'routed',
                                            'port_ch': '--',
                                            'reason': 'none',
                                            'speed': '1000(D)',
                                            'status': 'up',
                                            'type': 'eth',
                                            'vlan': '--'},
                                 'Ethernet1/3': {'mode': 'access',
                                            'port_ch': '--',
                                            'reason': 'Administratively '
                                                      'down',
                                            'speed': 'auto(D)',
                                            'status': 'down',
                                            'type': 'eth',
                                            'vlan': '1'},
                                 'Ethernet1/6': {'mode': 'access',
                                            'port_ch': '--',
                                            'reason': 'Link not '
                                                      'connected',
                                            'speed': 'auto(D)',
                                            'status': 'down',
                                            'type': 'eth',
                                            'vlan': '1'}},
                              'loopback':
                                {'Loopback0':
                                  {'description': '--',
                                   'status': 'up'}},
                              'port':
                                {'mgmt0':
                                  {'ip_address': '172.25.143.76',
                                   'mtu': 1500,
                                   'speed': '1000',
                                   'status': 'up',
                                   'vrf': '--'}},
                              'port_channel':
                                {'Port-channel8':
                                  {'mode': 'access',
                                   'protocol': 'none',
                                   'reason': 'No operational '
                                             'members',
                                   'speed': 'auto(I)',
                                   'status': 'down',
                                   'type': 'eth',
                                   'vlan': '1'}}}}

    golden_output = {'execute.return_value': '''
        pinxdt-n9kv-3 # show interface brief

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

    golden_output2 = {'execute.return_value': '''
        show interface Ethernet1/1 brief

        --------------------------------------------------------------------------------
        Ethernet        VLAN  Type Mode   Status  Reason                   Speed     Port
        Interface                                                                    Ch #
        --------------------------------------------------------------------------------
        Eth1/1          --    eth  routed up      none                       1000(D) --
                '''}

    golden_parsed_output2 = {
        'interface':
            {'ethernet':
                {'Ethernet1/1':
                    {'mode': 'routed',
                    'port_ch': '--',
                    'reason': 'none',
                    'speed': '1000(D)',
                    'status': 'up',
                    'type': 'eth',
                    'vlan': '--'}}}}

    golden_output3 = {'execute.return_value': '''

        --------------------------------------------------------------------------------

        Port   VRF          Status IP Address                              Speed    MTU

        --------------------------------------------------------------------------------

        mgmt0  --           up     172.31.150.153                          1000    1500

        --------------------------------------------------------------------------------

        Ethernet        VLAN    Type Mode   Status  Reason                 Speed     Port

        Interface                                                                    Ch #

        --------------------------------------------------------------------------------

        Eth1/1          --      eth  routed down    Administratively down    auto(D) --

        Eth1/4          --      eth  routed down    Administratively down    auto(D) --

        Eth1/4.1        110     eth  routed down    Administratively down    auto(D) --

        Eth1/4.2        112     eth  routed down    Administratively down    auto(D) --

        Eth1/4.3        114     eth  routed down    Administratively down    auto(D) --

        Eth1/9          --      eth  routed down    XCVR not inserted        auto(D) --

        Eth1/10         --      eth  routed up      none                      10G(D) --

        Eth1/10.1       --      eth  routed down    Configuration Incomplet  auto(D) --

        Eth1/11         --      eth  routed down    Administratively down    auto(D) --

        -------------------------------------------------------------------------------

        Interface Secondary VLAN(Type)                    Status Reason

        -------------------------------------------------------------------------------

        Vlan1     --                                      down   Administratively down
    '''}

    golden_parsed_output3 = {
        'interface': {
            'ethernet': {
                'Ethernet1/1': {
                    'mode': 'routed',
                    'port_ch': '--',
                    'reason': 'Administratively down',
                    'speed': 'auto(D)',
                    'status': 'down',
                    'type': 'eth',
                    'vlan': '--',
                },
                'Ethernet1/10': {
                    'mode': 'routed',
                    'port_ch': '--',
                    'reason': 'none',
                    'speed': '10G(D)',
                    'status': 'up',
                    'type': 'eth',
                    'vlan': '--',
                },
                'Ethernet1/10.1': {
                    'mode': 'routed',
                    'port_ch': '--',
                    'reason': 'Configuration Incomplet',
                    'speed': 'auto(D)',
                    'status': 'down',
                    'type': 'eth',
                    'vlan': '--',
                },
                'Ethernet1/11': {
                    'mode': 'routed',
                    'port_ch': '--',
                    'reason': 'Administratively down',
                    'speed': 'auto(D)',
                    'status': 'down',
                    'type': 'eth',
                    'vlan': '--',
                },
                'Ethernet1/4': {
                    'mode': 'routed',
                    'port_ch': '--',
                    'reason': 'Administratively down',
                    'speed': 'auto(D)',
                    'status': 'down',
                    'type': 'eth',
                    'vlan': '--',
                },
                'Ethernet1/4.1': {
                    'mode': 'routed',
                    'port_ch': '--',
                    'reason': 'Administratively down',
                    'speed': 'auto(D)',
                    'status': 'down',
                    'type': 'eth',
                    'vlan': '110',
                },
                'Ethernet1/4.2': {
                    'mode': 'routed',
                    'port_ch': '--',
                    'reason': 'Administratively down',
                    'speed': 'auto(D)',
                    'status': 'down',
                    'type': 'eth',
                    'vlan': '112',
                },
                'Ethernet1/4.3': {
                    'mode': 'routed',
                    'port_ch': '--',
                    'reason': 'Administratively down',
                    'speed': 'auto(D)',
                    'status': 'down',
                    'type': 'eth',
                    'vlan': '114',
                },
                'Ethernet1/9': {
                    'mode': 'routed',
                    'port_ch': '--',
                    'reason': 'XCVR not inserted',
                    'speed': 'auto(D)',
                    'status': 'down',
                    'type': 'eth',
                    'vlan': '--',
                },
            },
            'port': {
                'mgmt0': {
                    'ip_address': '172.31.150.153',
                    'mtu': 1500,
                    'speed': '1000',
                    'status': 'up',
                    'vrf': '--',
                },
            },
            'vlan': {
                'Vlan1': {
                    'reason': 'Administratively down',
                    'status': 'down',
                    'type': '--',
                },
            },
        },
    }

    golden_output4 = {'execute.return_value': '''
        --------------------------------------------------------------------------------

        Port   VRF          Status IP Address                              Speed    MTU

        --------------------------------------------------------------------------------

        mgmt0  --           up     172.28.249.175                          1000    1500

        --------------------------------------------------------------------------------

        Ethernet        VLAN    Type Mode   Status  Reason                 Speed     Port

        Interface                                                                    Ch #

        --------------------------------------------------------------------------------

        Eth1/1          --      eth  routed down    XCVR not inserted        auto(D) --

        Eth1/2          --      eth  routed down    XCVR not inserted        auto(D) --

        Eth1/3          --      eth  routed down    XCVR not inserted        auto(D) --

        Eth1/4          --      eth  routed down    XCVR not inserted        auto(D) --

        Eth1/5          --      eth  routed down    XCVR not inserted        auto(D) --

        Eth1/6          --      eth  routed down    XCVR not inserted        auto(D) --


        ------------------------------------------------------------------------------------------

        Port-channel VLAN    Type Mode   Status  Reason                              Speed   Protocol

        Interface

        ------------------------------------------------------------------------------------------

        Po10         --      eth  routed up      none                                 a-40G(D)  lacp

        Po10.1       2       eth  routed up      none                                 a-40G(D)    --

        Po10.2       3       eth  routed up      none                                 a-40G(D)    --

        Po10.3       4       eth  routed up      none                                 a-40G(D)    --

    '''}

    golden_parsed_output4 = {
        'interface': {
            'ethernet': {
                'Ethernet1/1': {
                    'mode': 'routed',
                    'port_ch': '--',
                    'reason': 'XCVR not inserted',
                    'speed': 'auto(D)',
                    'status': 'down',
                    'type': 'eth',
                    'vlan': '--',
                },
                'Ethernet1/2': {
                    'mode': 'routed',
                    'port_ch': '--',
                    'reason': 'XCVR not inserted',
                    'speed': 'auto(D)',
                    'status': 'down',
                    'type': 'eth',
                    'vlan': '--',
                },
                'Ethernet1/3': {
                    'mode': 'routed',
                    'port_ch': '--',
                    'reason': 'XCVR not inserted',
                    'speed': 'auto(D)',
                    'status': 'down',
                    'type': 'eth',
                    'vlan': '--',
                },
                'Ethernet1/4': {
                    'mode': 'routed',
                    'port_ch': '--',
                    'reason': 'XCVR not inserted',
                    'speed': 'auto(D)',
                    'status': 'down',
                    'type': 'eth',
                    'vlan': '--',
                },
                'Ethernet1/5': {
                    'mode': 'routed',
                    'port_ch': '--',
                    'reason': 'XCVR not inserted',
                    'speed': 'auto(D)',
                    'status': 'down',
                    'type': 'eth',
                    'vlan': '--',
                },
                'Ethernet1/6': {
                    'mode': 'routed',
                    'port_ch': '--',
                    'reason': 'XCVR not inserted',
                    'speed': 'auto(D)',
                    'status': 'down',
                    'type': 'eth',
                    'vlan': '--',
                },
            },
            'port': {
                'mgmt0': {
                    'ip_address': '172.28.249.175',
                    'mtu': 1500,
                    'speed': '1000',
                    'status': 'up',
                    'vrf': '--',
                },
            },
            'port_channel': {
                'Port-channel10': {
                    'mode': 'routed',
                    'protocol': 'lacp',
                    'reason': 'none',
                    'speed': 'a-40G(D)',
                    'status': 'up',
                    'type': 'eth',
                    'vlan': '--',
                },
                'Port-channel10.1': {
                    'mode': 'routed',
                    'protocol': '--',
                    'reason': 'none',
                    'speed': 'a-40G(D)',
                    'status': 'up',
                    'type': 'eth',
                    'vlan': '2',
                },
                'Port-channel10.2': {
                    'mode': 'routed',
                    'protocol': '--',
                    'reason': 'none',
                    'speed': 'a-40G(D)',
                    'status': 'up',
                    'type': 'eth',
                    'vlan': '3',
                },
                'Port-channel10.3': {
                    'mode': 'routed',
                    'protocol': '--',
                    'reason': 'none',
                    'speed': 'a-40G(D)',
                    'status': 'up',
                    'type': 'eth',
                    'vlan': '4',
                },
            },
        },
    }

    golden_output5 = {'execute.return_value': '''
     ------------------------------------------------------------------------------------------
    Port-channel VLAN    Type Mode   Status  Reason                              Speed   Protocol
    Interface
    ------------------------------------------------------------------------------------------
    Po403.1      1    eth  routed down    Administratively down                 auto(D)    --
    '''}

    golden_parsed_output5 = {
        'interface': {
            'port_channel': {
                'Port-channel403.1': {
                    'mode': 'routed',
                    'protocol': '--',
                    'reason': 'Administratively down',
                    'speed': 'auto(D)',
                    'status': 'down',
                    'type': 'eth',
                    'vlan': '1',
                }
            },
        },
    }

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        intf_obj = ShowInterfaceBrief(device=self.device)
        parsed_output = intf_obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output)

    def test_golden2(self):
        self.device = Mock(**self.golden_output2)
        intf_obj = ShowInterfaceBrief(device=self.device)
        parsed_output = intf_obj.parse(interface="Ethernet1/1")
        self.assertEqual(parsed_output, self.golden_parsed_output2)

    def test_golden3(self):
        self.device = Mock(**self.golden_output3)
        intf_obj = ShowInterfaceBrief(device=self.device)
        parsed_output = intf_obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output3)

    def test_empty(self):
        self.device1 = Mock(**self.empty_output)
        intf_obj = ShowInterfaceBrief(device=self.device1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = intf_obj.parse()

    def test_golden4(self):
        self.device = Mock(**self.golden_output4)
        intf_obj = ShowInterfaceBrief(device=self.device)
        parsed_output = intf_obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output4)

    def test_golden5(self):
        self.device = Mock(**self.golden_output5)
        intf_obj = ShowInterfaceBrief(device=self.device)
        parsed_output = intf_obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output5)


class TestShowRunInterface(unittest.TestCase):
    device = Device(name='aDevice')
    device1 = Device(name='bDevice')

    empty_output = {'execute.return_value': ''}

    golden_parsed_output = {'interface':
                                {'nve1':
                                    {'host_reachability_protocol': 'bgp',
                                     'member_vni':
                                        {'8100': {'mcast_group': '225.0.1.11'},
                                         '8101': {'mcast_group': '225.0.1.12'},
                                         '8103': {'mcast_group': '225.0.1.13'},
                                         '8105': {'mcast_group': '225.0.1.16'},
                                         '8106': {'mcast_group': '225.0.1.17'},
                                         '8107': {'mcast_group': '225.0.1.18'},
                                         '8108': {'mcast_group': '225.0.1.19'},
                                         '8109': {'mcast_group': '225.0.1.20'},
                                         '8110': {'mcast_group': '225.0.1.21'},
                                         '8111': {'mcast_group': '225.0.1.22'},
                                         '8112': {'mcast_group': '225.0.1.23'},
                                         '8113': {'mcast_group': '225.0.1.24'},
                                         '8114': {'mcast_group': '225.0.1.25'},
                                         '9100': {'associate_vrf': True},
                                         '9105': {'associate_vrf': True},
                                         '9106': {'associate_vrf': True},
                                         '9107': {'associate_vrf': True},
                                         '9108': {'associate_vrf': True},
                                         '9109': {'associate_vrf': True}
                                        },
                                    'shutdown': False,
                                    'source_interface': 'loopback1'}
                                }
                            }

    golden_output = {'execute.return_value': '''
        N95_1# show running-config  interface nve 1

        !Command: show running-config interface nve1
        !Time: Mon May 28 16:02:43 2018

        version 7.0(3)I7(1)

        interface nve1
          no shutdown
          host-reachability protocol bgp
          source-interface loopback1
          member vni 8100
            mcast-group 225.0.1.11
          member vni 8101
            mcast-group 225.0.1.12
          member vni 8103
            mcast-group 225.0.1.13
          member vni 8105
            mcast-group 225.0.1.16
          member vni 8106
            mcast-group 225.0.1.17
          member vni 8107
            mcast-group 225.0.1.18
          member vni 8108
            mcast-group 225.0.1.19
          member vni 8109
            mcast-group 225.0.1.20
          member vni 8110
            mcast-group 225.0.1.21
          member vni 8111
            mcast-group 225.0.1.22
          member vni 8112
            mcast-group 225.0.1.23
          member vni 8113
            mcast-group 225.0.1.24
          member vni 8114
            mcast-group 225.0.1.25
          member vni 9100 associate-vrf
          member vni 9105 associate-vrf
          member vni 9106 associate-vrf
          member vni 9107 associate-vrf
          member vni 9108 associate-vrf
          member vni 9109 associate-vrf

    '''}

    golden_parsed_output_1 = {
        'interface': {
            'nve1': {
                'host_reachability_protocol': 'bgp',
                'member_vni': {'2000002': {'mcast_group': '227.1.1.1',
                                           'suppress_arp': True},
                               '2000003': {'mcast_group': '227.1.1.1',
                                           'suppress_arp': True},
                               '2000004': {'mcast_group': '227.1.1.1',
                                           'suppress_arp': True},
                               '2000005': {'mcast_group': '227.1.1.1',
                                           'suppress_arp': True},
                               '2000006': {'mcast_group': '227.1.1.1',
                                           'suppress_arp': True},
                               '2000007': {'mcast_group': '227.1.1.1',
                                           'suppress_arp': True},
                               '2000008': {'mcast_group': '227.1.1.1',
                                           'suppress_arp': True},
                               '2000009': {'mcast_group': '227.1.1.1',
                                           'suppress_arp': True},
                               '2000010': {'mcast_group': '227.1.1.1',
                                           'suppress_arp': True},
                               '3003002': {'associate_vrf': True},
                               '3003003': {'associate_vrf': True},
                               '3003004': {'associate_vrf': True},
                               '3003005': {'associate_vrf': True},
                               '3003006': {'associate_vrf': True},
                               '3003007': {'associate_vrf': True},
                               '3003008': {'associate_vrf': True},
                               '3003009': {'associate_vrf': True},
                               '3003010': {'associate_vrf': True}},
                'shutdown': False,
                'source_interface': 'loopback0'}}}

    golden_output_1 = {'execute.return_value': '''
        CH-P2-TOR-1# sh run int nve 1

        !Command: show running-config interface nve1
        !Time: Wed May 30 07:34:20 2018

        version 7.0(3)I7(4)

        interface nve1
          no shutdown
          host-reachability protocol bgp
          source-interface loopback0
          member vni 2000002-2000010
            suppress-arp
            mcast-group 227.1.1.1
          member vni 3003002-3003010 associate-vrf
    '''}

    golden_parsed_output_2 = {
        'interface': {
            'Ethernet1/1': {
                'description': '*** Peer Link ***',
                'switchport': True,
                'switchport_mode': 'trunk',
                'trunk_vlans': '1-99,101-199,201-1399,1401-4094',
                'trunk_native_vlan': '330',
                'port_channel':{
                    'port_channel_mode': 'active',
                    'port_channel_int': '1',
                },
                'shutdown': False,
            },
        },
    }

    golden_output_2 = {'execute.return_value': '''
      !Command: show running-config interface Ethernet1/1
        !Running configuration last done at: Sun Aug 18 23:22:42 2019
        !Time: Tue Sep  3 23:25:59 2019

        version 7.0(3)I7(6) Bios:version 08.35

        interface Ethernet1/1
          description *** Peer Link ***
          switchport
          switchport mode trunk
          switchport trunk native vlan 330
          switchport trunk allowed vlan 1-99,101-199,201-1399,1401-4094
          channel-group 1 mode active
          no shutdown
    '''
    }

    # show running-config interface Eth1/4
    golden_output_3 = {'execute.return_value': '''
    !Time: ...
    version ...
    interface Ethernet1/4
     description DeviceA-description
     switchport access vlan x
     speed 1000
     duplex full
    '''}

    golden_parsed_output_3 = {
        'interface': {
            'Ethernet1/4': {
                'duplex': 'full',
                'access_vlan': 'x',
                'switchport_mode': 'access',
                'speed': 1000,
                'description': 'DeviceA-description',
            },
        },
    }

    golden_output_4 = {'execute.return_value': '''
    interface port-channel5
      description Port Channel Config Tst
      switchport mode trunk
      switchport trunk native vlan 2253
      switchport trunk allowed vlan 2253
      speed 10000
      vpc 5
    '''}

    golden_parsed_output_4 = {
        'interface': {
            'port-channel5': {
                'description': 'Port Channel Config Tst',
                'switchport_mode': 'trunk',
                'trunk_native_vlan': '2253',
                'trunk_vlans': '2253',
                'speed': 10000,
                'vpc': '5'
            },
        },
    }


    def test_golden(self):
        self.device = Mock(**self.golden_output)
        intf_obj = ShowRunningConfigInterface(device=self.device)
        parsed_output = intf_obj.parse(interface='nve1')
        self.assertEqual(parsed_output,self.golden_parsed_output)

    def test_golden_1(self):
        self.device = Mock(**self.golden_output_1)
        intf_obj = ShowRunningConfigInterface(device=self.device)
        parsed_output = intf_obj.parse(interface='nve1')
        self.assertEqual(parsed_output,self.golden_parsed_output_1)

    def test_golden_2(self):
        self.device = Mock(**self.golden_output_2)
        intf_obj = ShowRunningConfigInterface(device=self.device)
        parsed_output = intf_obj.parse(interface='Ethernet1/1')
        self.assertEqual(parsed_output,self.golden_parsed_output_2)

    def test_empty(self):
        self.device1 = Mock(**self.empty_output)
        intf_obj = ShowRunningConfigInterface(device=self.device1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = intf_obj.parse(interface='nve1')

    def test_golden_3(self):
        self.device = Mock(**self.golden_output_3)
        intf_obj = ShowRunningConfigInterface(device=self.device)
        parsed_output = intf_obj.parse(interface='Ethernet1/4')
        self.assertEqual(parsed_output,self.golden_parsed_output_3)

    def test_golden_4(self):
        self.device = Mock(**self.golden_output_4)
        intf_obj = ShowRunningConfigInterface(device=self.device)
        parsed_output = intf_obj.parse(interface='port-channel10')
        self.assertEqual(parsed_output,self.golden_parsed_output_4)


class TestShowNveInterface(unittest.TestCase):

    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output = {'interface':
                                {'nve1':
                                    {'state': 'Up',
                                    'encapsulation': 'VXLAN',
                                    'source_interface':
                                        {'loopback1':
                                            {'secondary': '0.0.0.0',
                                             'primary': '10.9.0.1'}
                                        },
                                    'vpc_capability':
                                        {'VPC-VIP-Only':
                                            {'notified': False}
                                        }
                                    }
                                }
                            }

    golden_output = {'execute.return_value': '''\
        CH-P2-TOR-1# sh nve interface nve 1 detail
        Interface: nve1, State: Up, encapsulation: VXLAN
         VPC Capability: VPC-VIP-Only [not-notified]
         Local Router MAC: 00f2.8bff.737a
         Host Learning Mode: Control-Plane
         Source-Interface: loopback1 (primary: 10.9.0.1, secondary: 0.0.0.0)
         Source Interface State: Up
         IR Capability Mode: No
         Virtual RMAC Advertisement: No
         NVE Flags:
         Interface Handle: 0x49000001
         Source Interface hold-down-time: 180
         Source Interface hold-up-time: 30
         Remaining hold-down time: 0 seconds
         Virtual Router MAC: N/A
         Interface state: nve-intf-add-complete
         unknown-peer-forwarding: disable
         down-stream vni config mode: n/a
        Nve Src node last notif sent: None
        Nve Mcast Src node last notif sent: None
        Nve MultiSite Src node last notif sent: None
    '''
    }

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = ShowNveInterface(device=self.device)
        parsed_output = obj.parse(interface='nve1')
        self.assertEqual(parsed_output,self.golden_parsed_output)

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowNveInterface(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse(interface='nve1')


class TestShowIpInterfaceBriefVrfAll(unittest.TestCase):

    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output = {
        'interface':
            {'Eth1/1.1':
                {'interface_status': 'protocol-up/link-up/admin-up',
                 'ip_address': '192.168.4.1'},
             'Eth1/1.2':
                {'interface_status': 'protocol-up/link-up/admin-up',
                 'ip_address': '192.168.154.1'},
             'Eth1/1.4':
                {'interface_status': 'protocol-up/link-up/admin-up',
                 'ip_address': '192.168.106.1'},
             'Eth1/2.1':
                {'interface_status': 'protocol-up/link-up/admin-up',
                 'ip_address': '192.168.154.1'},
             'Eth1/2.2':
                {'interface_status': 'protocol-up/link-up/admin-up',
                 'ip_address': '192.168.51.1'},
             'Eth1/2.4':
                {'interface_status': 'protocol-up/link-up/admin-up',
                 'ip_address': '192.168.9.1'},
             'Lo0':
                {'interface_status': 'protocol-up/link-up/admin-up',
                 'ip_address': '10.1.1.1'},
             'Lo1':
                {'interface_status': 'protocol-up/link-up/admin-up',
                 'ip_address': '10.81.1.1'},
             'Vlan100':
                {'interface_status': 'protocol-up/link-up/admin-up',
                 'ip_address': '10.51.1.1'},
             'Vlan101':
                {'interface_status': 'protocol-up/link-up/admin-up',
                 'ip_address': '10.154.1.1'},
             'Vlan200':
                {'interface_status': 'protocol-up/link-up/admin-up',
                 'ip_address': '10.76.1.1'},
             'mgmt0':
                {'interface_status': 'protocol-up/link-up/admin-up',
                 'ip_address': '10.255.5.169'}
            }
        }

    golden_output = {'execute.return_value': '''\
        N95_1# show ip interface brief vrf all

        IP Interface Status for VRF "default"(1)
        Interface            IP Address      Interface Status
        Vlan100              10.51.1.1        protocol-up/link-up/admin-up
        Vlan101              10.154.1.1        protocol-up/link-up/admin-up
        Lo0                  10.1.1.1       protocol-up/link-up/admin-up
        Eth1/1.1             192.168.4.1       protocol-up/link-up/admin-up
        Eth1/1.2             192.168.154.1       protocol-up/link-up/admin-up
        Eth1/1.4             192.168.106.1       protocol-up/link-up/admin-up
        Eth1/2.1             192.168.154.1       protocol-up/link-up/admin-up
        Eth1/2.2             192.168.51.1       protocol-up/link-up/admin-up
        Eth1/2.4             192.168.9.1       protocol-up/link-up/admin-up

        IP Interface Status for VRF "management"(2)
        Interface            IP Address      Interface Status
        mgmt0                10.255.5.169    protocol-up/link-up/admin-up

        IP Interface Status for VRF "VRF1"(3)
        Interface            IP Address      Interface Status
        Vlan200              10.76.1.1        protocol-up/link-up/admin-up
        Lo1                  10.81.1.1       protocol-up/link-up/admin-up
    '''
    }

    golden_parsed_output_pipe = {
        'interface':
            {'mgmt0':
                {'interface_status': 'protocol-up/link-up/admin-up',
                 'ip_address': '10.255.5.169'}
            }
        }

    golden_output_pipe = {'execute.return_value': '''\
        N95_1# show ip interface brief vrf all | i 10.255.5.169
        mgmt0                10.255.5.169    protocol-up/link-up/admin-up
    '''
    }

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = ShowIpInterfaceBriefVrfAll(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output)

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowIpInterfaceBriefVrfAll(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden_pipe(self):
        self.device = Mock(**self.golden_output_pipe)
        obj = ShowIpInterfaceBriefVrfAll(device=self.device)
        parsed_output = obj.parse(ip='10.255.5.169')
        self.assertEqual(parsed_output,self.golden_parsed_output_pipe)

#############################################################################
# unittest For show interface description
#############################################################################


class test_show_interface_description(unittest.TestCase):
    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output = {
        "interfaces": {
            "Ethernet1/1.110": {
                "description": "--",
                "speed": "10G",
                "type": "eth"
            },
            "Ethernet1/1.115": {
                "description": "--",
                "speed": "10G",
                "type": "eth"
            },
            "Ethernet1/1.120": {
                "description": "--",
                "speed": "10G",
                "type": "eth"
            },
            "Ethernet1/1.390": {
                "description": "--",
                "speed": "10G",
                "type": "eth"
            },
            "Ethernet1/1.410": {
                "description": "--",
                "speed": "10G",
                "type": "eth"
            },
            "Ethernet1/1.415": {
                "description": "--",
                "speed": "10G",
                "type": "eth"
            },
            "Ethernet1/1.420": {
                "description": "--",
                "speed": "10G",
                "type": "eth"
            },
            "Ethernet1/1.90": {
                "description": "--",
                "speed": "10G",
                "type": "eth"
            },
            "Ethernet1/2": {
                "description": "--",
                "speed": "10G",
                "type": "eth"
            },
            "Ethernet1/2.90": {
                "description": "--",
                "speed": "10G",
                "type": "eth"
            },
            "Ethernet1/2.110": {
                "description": "--",
                "speed": "10G",
                "type": "eth"
            },
            "Ethernet1/2.115": {
                "description": "--",
                "speed": "10G",
                "type": "eth"
            },
            "Ethernet1/2.120": {
                "description": "--",
                "speed": "10G",
                "type": "eth"
            },
            "Ethernet1/2.390": {
                "description": "--",
                "speed": "10G",
                "type": "eth"
            },
            "Ethernet1/2.410": {
                "description": "--",
                "speed": "10G",
                "type": "eth"
            },
            "Ethernet1/2.415": {
                "description": "--",
                "speed": "10G",
                "type": "eth"
            },
            "Ethernet1/2.420": {
                "description": "--",
                "speed": "10G",
                "type": "eth"
            },
            "Port-channel13": {
                "description": "--"
            },
            "Port-channel23": {
                "description": "--"
            },
            "Loopback0": {
                "description": "--"
            },
            "Loopback300": {
                "description": "--"
            },
            "mgmt0": {
                "description": "--"
            }
        }
    }

    golden_output = {'execute.return_value': '''
        -------------------------------------------------------------------------------
        Interface                Description
        -------------------------------------------------------------------------------
        mgmt0                    --

        -------------------------------------------------------------------------------
        Port          Type   Speed   Description
        -------------------------------------------------------------------------------
        Eth1/1.90     eth    10G     --
        Eth1/1.110    eth    10G     --
        Eth1/1.115    eth    10G     --
        Eth1/1.120    eth    10G     --
        Eth1/1.390    eth    10G     --
        Eth1/1.410    eth    10G     --
        Eth1/1.415    eth    10G     --
        Eth1/1.420    eth    10G     --
        Eth1/2        eth    10G     --
        Eth1/2.90     eth    10G     --
        Eth1/2.110    eth    10G     --
        Eth1/2.115    eth    10G     --
        Eth1/2.120    eth    10G     --
        Eth1/2.390    eth    10G     --
        Eth1/2.410    eth    10G     --
        Eth1/2.415    eth    10G     --
        Eth1/2.420    eth    10G     --

        -------------------------------------------------------------------------------
        Interface                Description
        -------------------------------------------------------------------------------
        Po13                     --
        Po23                     --

        -------------------------------------------------------------------------------
        Interface                Description
        -------------------------------------------------------------------------------
        Lo0                      --
        Lo300                    --
    '''}

    golden_parsed_interface_output = {
        "interfaces": {
            "Ethernet1/1": {
                "description": "--",
                "speed": "10G",
                "type": "eth"
            }
        }
    }

    golden_interface_output = {'execute.return_value': '''
        -------------------------------------------------------------------------------
        Port          Type   Speed   Description
        -------------------------------------------------------------------------------
        Eth1/1        eth    10G     --
    '''}


    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowInterfaceDescription(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = ShowInterfaceDescription(device=self.device)
        parsed_output = obj.parse()
        self.maxDiff = None
        self.assertEqual(parsed_output,self.golden_parsed_output)

    def test_golden_interface(self):
        self.device = Mock(**self.golden_interface_output)
        obj = ShowInterfaceDescription(device=self.device)
        parsed_output = obj.parse(interface='Eth1/1')
        self.maxDiff = None
        self.assertEqual(parsed_output,self.golden_parsed_interface_output)


#############################################################################
# unitest For show interface status
#############################################################################
class test_show_interface_status(unittest.TestCase):
    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output = {
        'interfaces': {
            'Ethernet1/1': {
                'duplex_code': 'full',
                'name': 'AOTLXPRPBD10001',
                'port_speed': '10G',
                'status': 'connected',
                'type': '10g',
                'vlan': 'trunk'
            },
            'Ethernet1/2': {
                'duplex_code': 'full',
                'name': 'AOTLXPRPBD10004',
                'port_speed': '10G',
                'status': 'connected',
                'type': '10g',
                'vlan': '360'
            },
            'Ethernet1/43': {
                'duplex_code': 'auto',
                'port_speed': 'auto',
                'status': 'disabled',
                'type': '10g',
                'vlan': '1'
            },
            'Ethernet1/52.511': {
                'duplex_code': 'full',
                'port_speed': '10G',
                'status': 'connected',
                'type': '10Gbase-LR',
                'vlan': 'routed'
            },
            'Port-channel147': {
                'duplex_code': 'full',
                'name': 'AOTLXPRPBD10112',
                'port_speed': '10G',
                'status': 'connected',
                'vlan': '360'
            },
            'Vlan1': {
                'duplex_code': 'auto',
                'port_speed': 'auto',
                'status': 'down',
                'vlan': 'routed'
            },
            'Vlan366': {
                'duplex_code': 'auto',
                'name': 'BigData',
                'port_speed': 'auto',
                'status': 'connected',
                'vlan': 'routed'
            },
            'mgmt0': {
                'duplex_code': 'full',
                'name': 'ES1SW18AUN6_6/22',
                'port_speed': '1000',
                'status': 'connected',
                'vlan': 'routed'
            },
            'Nve1': {
                'duplex_code': 'auto',
                'port_speed': 'auto',
                'status': 'connected',
            },
        }
    }

    golden_output = {'execute.return_value': '''
        --------------------------------------------------------------------------------
        Port          Name               Status    Vlan      Duplex  Speed   Type
        --------------------------------------------------------------------------------
        mgmt0         ES1SW18AUN6_6/22   connected routed    full    1000    --

        --------------------------------------------------------------------------------
        Port          Name               Status    Vlan      Duplex  Speed   Type
        --------------------------------------------------------------------------------
        Eth1/1        AOTLXPRPBD10001    connected trunk     full    10G     10g
        Eth1/2        AOTLXPRPBD10004    connected 360       full    10G     10g
        Eth1/43       --                 disabled  1         auto    auto    10g
        Eth1/52.511   --                 connected routed    full    10G     10Gbase-LR
        Po147         AOTLXPRPBD10112    connected 360       full    10G     --
        Vlan1         --                 down      routed    auto    auto    --
        Vlan366       BigData            connected routed    auto    auto    --
        nve1          --                 connected --        auto    auto    --
    '''}

    golden_parsed_interface_output = {
        'interfaces': {
            'Ethernet1/1': {
                'duplex_code': 'full',
                'name': 'AOTLXPRPBD10001',
                'port_speed': '10G',
                'status': 'connected',
                'type': '10g',
                'vlan': 'trunk'}
        }
    }

    golden_interface_output = {'execute.return_value': '''
        Port          Name               Status    Vlan      Duplex  Speed   Type
        --------------------------------------------------------------------------------
        Eth1/1        AOTLXPRPBD10001    connected trunk     full    10G     10g
    '''}

    golden_output_2 = {'execute.return_value': '''
    --------------------------------------------------------------------------------
    Port          Name               Status    Vlan      Duplex  Speed   Type
    --------------------------------------------------------------------------------
    Po135         DO-DD01            connected 51        full    a-10G   --
    Po140         DO-UCS01-B         connected trunk     full    a-10G   --
    mgmt0         --                 connected routed    full    a-1000  --
    Eth101/1/1    DODC01             connected 101       full    a-1000
    Eth101/1/2    DO-EXCH-01         connected 101       full    a-1000
    '''}

    golden_parsed_output_2 = {
        'interfaces': {
            'Ethernet101/1/1': {
                'duplex_code': 'full',
                'name': 'DODC01',
                'port_speed': 'a-1000',
                'status': 'connected',
                'vlan': '101',
            },
            'Ethernet101/1/2': {
                'duplex_code': 'full',
                'name': 'DO-EXCH-01',
                'port_speed': 'a-1000',
                'status': 'connected',
                'vlan': '101',
            },
            'Port-channel135': {
                'duplex_code': 'full',
                'name': 'DO-DD01',
                'port_speed': 'a-10G',
                'status': 'connected',
                'vlan': '51',
            },
            'Port-channel140': {
                'duplex_code': 'full',
                'name': 'DO-UCS01-B',
                'port_speed': 'a-10G',
                'status': 'connected',
                'vlan': 'trunk',
            },
            'mgmt0': {
                'duplex_code': 'full',
                'port_speed': 'a-1000',
                'status': 'connected',
                'vlan': 'routed',
            },
        },
    }

    golden_output_3 = {'execute.return_value': '''
        N7K-1-LAB# show int status

        --------------------------------------------------------------------------------
        Port Name Status Vlan Duplex Speed Type
        --------------------------------------------------------------------------------
        mgmt0 -- connected routed full a-1000 --
        Eth1/1 *** N7K-2-FLEXP connected trunk full a-10G SFP-H10GB-C
        Eth1/2 *** N7K-2-FLEXP connected trunk full a-10G SFP-H10GB-C
        Eth1/3 *** P2P L3-CIS- connected routed full a-1000 1000base-T
        Eth1/4 *** FEX 2248TP  connected 1      full a-10G  Fabric Exte
        Eth1/5 *** L2 L3-CIS-N connected trunk full a-1000 1000base-T
        Eth1/6 *** L2POE Gi1/0 connected trunk full a-1000 1000base-T
        Eth1/7 *** To ACI leaf connected trunk full a-1000 1000base-SX
        Eth1/8 -- sfpAbsent routed auto auto --
        Eth1/9 -- sfpAbsent routed auto auto --
    '''}

    golden_parsed_output_3 = {
        'interfaces': {
            'Ethernet1/1': {
                'duplex_code': 'full',
                'name': '*** N7K-2-FLEXP',
                'port_speed': 'a-10G',
                'status': 'connected',
                'type': 'SFP-H10GB-C',
                'vlan': 'trunk',
            },
            'Ethernet1/2': {
                'duplex_code': 'full',
                'name': '*** N7K-2-FLEXP',
                'port_speed': 'a-10G',
                'status': 'connected',
                'type': 'SFP-H10GB-C',
                'vlan': 'trunk',
            },
            'Ethernet1/3': {
                'duplex_code': 'full',
                'name': '*** P2P L3-CIS-',
                'port_speed': 'a-1000',
                'status': 'connected',
                'type': '1000base-T',
                'vlan': 'routed',
            },
            'Ethernet1/4': {
                'duplex_code': 'full',
                'name': '*** FEX 2248TP',
                'port_speed': 'a-10G',
                'status': 'connected',
                'type': 'Fabric Exte',
                'vlan': '1',
            },
            'Ethernet1/5': {
                'duplex_code': 'full',
                'name': '*** L2 L3-CIS-N',
                'port_speed': 'a-1000',
                'status': 'connected',
                'type': '1000base-T',
                'vlan': 'trunk',
            },
            'Ethernet1/6': {
                'duplex_code': 'full',
                'name': '*** L2POE Gi1/0',
                'port_speed': 'a-1000',
                'status': 'connected',
                'type': '1000base-T',
                'vlan': 'trunk',
            },
            'Ethernet1/7': {
                'duplex_code': 'full',
                'name': '*** To ACI leaf',
                'port_speed': 'a-1000',
                'status': 'connected',
                'type': '1000base-SX',
                'vlan': 'trunk',
            },
            'Ethernet1/8': {
                'duplex_code': 'auto',
                'port_speed': 'auto',
                'status': 'sfpAbsent',
                'vlan': 'routed',
            },
            'Ethernet1/9': {
                'duplex_code': 'auto',
                'port_speed': 'auto',
                'status': 'sfpAbsent',
                'vlan': 'routed',
            },
            'mgmt0': {
                'duplex_code': 'full',
                'port_speed': 'a-1000',
                'status': 'connected',
                'vlan': 'routed',
            },
        },
    }

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowInterfaceStatus(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = ShowInterfaceStatus(device=self.device)
        parsed_output = obj.parse()
        self.maxDiff = None
        self.assertEqual(parsed_output, self.golden_parsed_output)

    def test_golden_interface(self):
        self.device = Mock(**self.golden_interface_output)
        obj = ShowInterfaceStatus(device=self.device)
        parsed_output = obj.parse(interface='Eth1/1')
        self.maxDiff = None
        self.assertEqual(parsed_output, self.golden_parsed_interface_output)

    def test_golden_2(self):
        self.device = Mock(**self.golden_output_2)
        obj = ShowInterfaceStatus(device=self.device)
        parsed_output = obj.parse(interface='Eth1/1')
        self.maxDiff = None
        self.assertEqual(parsed_output, self.golden_parsed_output_2)

    def test_golden_3(self):
        self.device = Mock(**self.golden_output_3)
        obj = ShowInterfaceStatus(device=self.device)
        parsed_output = obj.parse()
        self.maxDiff = None
        self.assertEqual(parsed_output, self.golden_parsed_output_3)

# ===========================================
# Unit test for 'show interface capabilities'
# ===========================================
class TestShowInterfaceCapabilities(unittest.TestCase):
    '''unit test for "show lldp all'''
    device = Device(name='aDevice')

    empty_output = {'execute.return_value': ''}

    golden_output={'execute.return_value': '''
        Ethernet1/4
            Model:                 N9K-C93108TC-EX
            Type (Non SFP):        10g
            Speed:                 100,1000,10000
            Duplex:                full
            Trunk encap. type:     802.1Q
            Channel:               yes
            Broadcast suppression: percentage(0-100)
            Flowcontrol:           rx-(off/on),tx-(off/on)
            Rate mode:             dedicated
            Port mode:             Routed,Switched
            QOS scheduling:        rx-(8q2t),tx-(7q)
            CoS rewrite:           yes
            ToS rewrite:           yes
            SPAN:                  yes
            UDLD:                  yes
            MDIX:                  yes
            TDR capable:           no
            Link Debounce:         yes
            Link Debounce Time:    yes
            FEX Fabric:            yes
            dot1Q-tunnel mode:     yes
            Pvlan Trunk capable:   no
            Port Group Members:    4
            EEE (efficient-eth):   no
            PFC capable:           yes
            Buffer Boost capable:  no
            Breakout capable:      no
            MACSEC capable:        no
        '''
    }

    golden_parsed_output= {
        "Ethernet1/4": {
            "model": "N9K-C93108TC-EX",
            "sfp": False,
            "type": "10g",
            "speed": [100,1000,10000],
            "duplex": "full",
            "trunk_encap_type": "802.1Q",
            "channel": "yes",
            "broadcast_suppression": {"type": "percentage", "value": "0-100"},
            "flowcontrol": {"rx": "off/on", "tx": "off/on"},
            "rate_mode": "dedicated",
            "port_mode": "Routed,Switched",
            "qos_scheduling": {"rx": "8q2t", "tx": "7q"},
            "cos_rewrite": "yes",
            "tos_rewrite": "yes",
            "span": "yes",
            "udld": "yes",
            "mdix": "yes",
            "tdr_capable": "no",
            "link_debounce": "yes",
            "link_debounce_time": "yes",
            "fex_fabric": "yes",
            "dot1q_tunnel_mode": "yes",
            "pvlan_trunk_capable": "no",
            "port_group_members": 4,
            "eee_efficient_eth": "no",
            "pfc_capable": "yes",
            "buffer_boost_capable": "no",
            "breakout_capable": "no",
            "macsec_capable": "no",
        }
    }



    golden_output_1 = {'execute.return_value': '''
        Ethernet1/1/1
            Model:                 N9K-C9236C
            Type (SFP capable):    QSFP-100G-CR4
            Speed:                 1000,10000
            Duplex:                full
            Trunk encap. type:     802.1Q
            Channel:               yes
            Broadcast suppression: percentage(0-100)
            Flowcontrol:           rx-(off/on),tx-(off/on)
            Rate mode:             dedicated
            Port mode:             Routed,Switched
            QOS scheduling:        rx-(8q2t),tx-(7q)
            CoS rewrite:           yes
            ToS rewrite:           yes
            SPAN:                  yes
            UDLD:                  yes
            MDIX:                  no
            TDR capable:           no
            Link Debounce:         yes
            Link Debounce Time:    yes
            FEX Fabric:            no
            dot1Q-tunnel mode:     no
            Pvlan Trunk capable:   no
            Port Group Members:    1
            EEE (efficient-eth):   no
            PFC capable:           yes
            Buffer Boost capable:  no
            Breakout capable:      no
            MACSEC capable:        no

        Ethernet1/3
            Model:                 N9K-C93108TC-EX
            Type (Non SFP):        10g
            Speed:                 100,1000,10000
            Duplex:                full
            Trunk encap. type:     802.1Q
            Channel:               yes
            Broadcast suppression: percentage(0-100)
            Flowcontrol:           rx-(off/on),tx-(off/on)
            Rate mode:             dedicated
            Port mode:             Routed,Switched
            QOS scheduling:        rx-(8q2t),tx-(7q)
            CoS rewrite:           yes
            ToS rewrite:           yes
            SPAN:                  yes
            UDLD:                  yes
            MDIX:                  yes
            TDR capable:           no
            Link Debounce:         yes
            Link Debounce Time:    yes
            FEX Fabric:            yes
            dot1Q-tunnel mode:     yes
            Pvlan Trunk capable:   no
            Port Group Members:    3
            EEE (efficient-eth):   no
            PFC capable:           yes
            Buffer Boost capable:  no
            Breakout capable:      no
            MACSEC capable:        no
          
        Ethernet1/17
            Model:                 N9K-C9236C
            Type (SFP capable):    QSFP-100G-AOC1M
            Speed:                 1000,10000,25000,40000,50000,100000
            Duplex:                full
            Trunk encap. type:     802.1Q
            Channel:               yes
            Broadcast suppression: percentage(0-100)
            Flowcontrol:           rx-(off/on),tx-(off/on)
            Rate mode:             dedicated
            Port mode:             Routed,Switched
            QOS scheduling:        rx-(8q2t),tx-(7q)
            CoS rewrite:           yes
            ToS rewrite:           yes
            SPAN:                  yes
            UDLD:                  yes
            MDIX:                  no
            TDR capable:           no
            Link Debounce:         yes
            Link Debounce Time:    yes
            FEX Fabric:            no
            dot1Q-tunnel mode:     no
            Pvlan Trunk capable:   no
            Port Group Members:    17
            EEE (efficient-eth):   no
            PFC capable:           yes
            Buffer Boost capable:  no
            Breakout capable:      yes
            MACSEC capable:        no
        '''
    }

    golden_parsed_output_1 = {
        "Ethernet1/1/1": {
            "model": "N9K-C9236C",
            "sfp": True,
            "type": "QSFP-100G-CR4",
            "speed": [1000,10000],
            "duplex": "full",
            "trunk_encap_type": "802.1Q",
            "channel": "yes",
            "broadcast_suppression": {"type": "percentage", "value": "0-100"},
            "flowcontrol": {"rx": "off/on", "tx": "off/on"},
            "rate_mode": "dedicated",
            "port_mode": "Routed,Switched",
            "qos_scheduling": {"rx": "8q2t", "tx": "7q"},
            "cos_rewrite": "yes",
            "tos_rewrite": "yes",
            "span": "yes",
            "udld": "yes",
            "mdix": "no",
            "tdr_capable": "no",
            "link_debounce": "yes",
            "link_debounce_time": "yes",
            "fex_fabric": "no",
            "dot1q_tunnel_mode": "no",
            "pvlan_trunk_capable": "no",
            "port_group_members": 1,
            "eee_efficient_eth": "no",
            "pfc_capable": "yes",
            "buffer_boost_capable": "no",
            "breakout_capable": "no",
            "macsec_capable": "no",
        },
        "Ethernet1/3": {
            "model": "N9K-C93108TC-EX",
            "sfp": False,
            "type": "10g",
            "speed": [100,1000,10000],
            "duplex": "full",
            "trunk_encap_type": "802.1Q",
            "channel": "yes",
            "broadcast_suppression": {"type": "percentage", "value": "0-100"},
            "flowcontrol": {"rx": "off/on", "tx": "off/on"},
            "rate_mode": "dedicated",
            "port_mode": "Routed,Switched",
            "qos_scheduling": {"rx": "8q2t", "tx": "7q"},
            "cos_rewrite": "yes",
            "tos_rewrite": "yes",
            "span": "yes",
            "udld": "yes",
            "mdix": "yes",
            "tdr_capable": "no",
            "link_debounce": "yes",
            "link_debounce_time": "yes",
            "fex_fabric": "yes",
            "dot1q_tunnel_mode": "yes",
            "pvlan_trunk_capable": "no",
            "port_group_members": 3,
            "eee_efficient_eth": "no",
            "pfc_capable": "yes",
            "buffer_boost_capable": "no",
            "breakout_capable": "no",
            "macsec_capable": "no",
        },
        "Ethernet1/17": {
            "model": "N9K-C9236C",
            "sfp": True,
            "type": "QSFP-100G-AOC1M",
            "speed": [1000,10000,25000,40000,50000,100000],
            "duplex": "full",
            "trunk_encap_type": "802.1Q",
            "channel": "yes",
            "broadcast_suppression": {"type": "percentage", "value": "0-100"},
            "flowcontrol": {"rx": "off/on", "tx": "off/on"},
            "rate_mode": "dedicated",
            "port_mode": "Routed,Switched",
            "qos_scheduling": {"rx": "8q2t", "tx": "7q"},
            "cos_rewrite": "yes",
            "tos_rewrite": "yes",
            "span": "yes",
            "udld": "yes",
            "mdix": "no",
            "tdr_capable": "no",
            "link_debounce": "yes",
            "link_debounce_time": "yes",
            "fex_fabric": "no",
            "dot1q_tunnel_mode": "no",
            "pvlan_trunk_capable": "no",
            "port_group_members": 17,
            "eee_efficient_eth": "no",
            "pfc_capable": "yes",
            "buffer_boost_capable": "no",
            "breakout_capable": "yes",
            "macsec_capable": "no",
        },
    }



    def test_empty(self):
        self.maxDiff = None
        self.device = Mock(**self.empty_output)
        obj = ShowInterfaceCapabilities(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output)
        obj = ShowInterfaceCapabilities(device=self.device)
        parsed_output = obj.parse(interface='Ethernet1/4')

        self.assertEqual(parsed_output, self.golden_parsed_output)

    def test_golden2(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_1)
        obj = ShowInterfaceCapabilities(device=self.device)
        parsed_output = obj.parse()

        self.assertEqual(parsed_output, self.golden_parsed_output_1)

# ===========================================
# Unit test for 'show interface transceiver'
# ===========================================
class TestShowInterfaceTransceiver(unittest.TestCase):
    '''unit test for "show interface transceiver'''
    device = Device(name='aDevice')

    empty_output = {'execute.return_value': ''}

    golden_output={'execute.return_value': '''
        Ethernet1/4
            transceiver is present
            type is QSFP-40G-CR4
            name is CISCO-TYCO
            part number is 2821248-5
            revision is D
            serial number is TED2318K229-B
            nominal bitrate is 10300 MBit/sec per channel
            Link length supported for copper is 3 m
            cisco id is 13
            cisco extended id number is 16
            cisco part number is 37-1317-03
            cisco product id is QSFP-H40G-CU3M
            cisco version id is V03
        '''
    }

    golden_parsed_output= {
            'Ethernet1/4': {'cis_part_number': '37-1317-03',
                 'cis_product_id': 'QSFP-H40G-CU3M',
                 'cis_version_id': 'V03',
                 'cisco_id': '13',
                 'name': 'CISCO-TYCO',
                 'nominal_bitrate': 10300,
                 'part_number': '2821248-5',
                 'revision': 'D',
                 'serial_number': 'TED2318K229-B',
                 'transceiver_present': True,
                 'transceiver_type': 'QSFP-40G-CR4'
            }
        }

    golden_output_1 = {'execute.return_value': '''
        Ethernet1/2
            transceiver is present
            type is QSFP-DD-400G-COPPER
            name is CISCO-LEONI
            part number is L45593-K218-C20
            revision is 00
            serial number is LCC2411GC93-A
            nominal bitrate is 425000 MBit/sec per channel
            cisco id is 0x18
            cisco part number is 37-1843-01
            cisco product id is QDD-400-CU2M
            cisco version id is V01
            vendor OUI is a8b0ae
            date code is 20031400
            clei code is CMPQAGSCAA
            power class is 1 (1.5 W maximum)
            max power is 1.50 W
            cable attenuation is 0/0/0/0/0 dB for bands 5/7/12.9/25.8/56 GHz
            near-end lanes used none
            far-end lane code for 8 lanes aaaaaaaa
            media interface is copper cable unequalized
            Advertising code is Passive Cu
            Host electrical interface code is 200GAUI-4 C2M (Annex 120E)
            Cable Length is   2.0 M
            CMIS version is  4
        
        '''
    }

    golden_parsed_output_1 = {
            'Ethernet1/2': {'advertising_code': 'Passive Cu',
                 'cable_attenuation': '0/0/0/0/0 dB for bands 5/7/12.9/25.8/56 '
                                      'GHz',
                 'cable_length': 2.0,
                 'cis_part_number': '37-1843-01',
                 'cis_product_id': 'QDD-400-CU2M',
                 'cis_version_id': 'V01',
                 'cisco_id': '0x18',
                 'clei': 'CMPQAGSCAA',
                 'cmis_ver': 4,
                 'date_code': '20031400',
                 'far_end_lanes': '8 lanes aaaaaaaa',
                 'host_electrical_intf': '200GAUI-4 C2M (Annex 120E)',
                 'max_power': 1.5,
                 'media_interface': 'copper cable unequalized',
                 'name': 'CISCO-LEONI',
                 'near_end_lanes': 'none',
                 'nominal_bitrate': 425000,
                 'part_number': 'L45593-K218-C20',
                 'power_class': '1 (1.5 W maximum)',
                 'revision': '00',
                 'serial_number': 'LCC2411GC93-A',
                 'vendor_oui': 'a8b0ae',
                 'transceiver_present': True,
                 'transceiver_type': 'QSFP-DD-400G-COPPER'
            }
    }

    golden_output_2={'execute.return_value': '''
        Ethernet1/1
            transceiver is present
            type is QSFP-DD-400G-COPPER
            name is CISCO-LEONI
            part number is L45593-K218-C20
            revision is 00
            serial number is LCC2411GG1W-A
            nominal bitrate is 425000 MBit/sec per channel
            cisco id is 0x18
            cisco part number is 37-1843-01
            cisco product id is QDD-400-CU2M
            cisco version id is V01
            vendor OUI is a8b0ae
            date code is 20031400
            clei code is CMPQAGSCAA
            power class is 1 (1.5 W maximum)
            max power is 1.50 W
            cable attenuation is 0/0/0/0/0 dB for bands 5/7/12.9/25.8/56 GHz
            near-end lanes used none
            far-end lane code for 8 lanes aaaaaaaa
            media interface is copper cable unequalized
            Advertising code is Passive Cu
            Host electrical interface code is 200GAUI-4 C2M (Annex 120E)
            Cable Length is   2.0 M
            CMIS version is  4

        Ethernet1/30
            transceiver is present
            type is QSFP-40G-CR4
            name is CISCO-TYCO
            part number is 2821248-5
            revision is D
            serial number is TED2318K1QR-B
            nominal bitrate is 10300 MBit/sec per channel
            Link length supported for copper is 3 m
            cisco id is 13
            cisco extended id number is 16
            cisco part number is 37-1317-03
            cisco product id is QSFP-H40G-CU3M
            cisco version id is V03

        Ethernet1/52
            transceiver is present
            type is QSFP-DD-400G-FR4
            name is CISCO-INNOLIGHT
            part number is T-DQ4CNT-NCI
            revision is 2B
            serial number is INL24265523
            nominal bitrate is 425000 MBit/sec per channel
            cisco id is 0x18
            cisco part number is 10-3321-01
            cisco product id is QDD-400G-FR4-S
            cisco version id is V01
            firmware version is 204.154
            Link length SMF is 2 km
            Nominal transmitter wavelength is 1301.00 nm
            Wavelength tolerance is 6.500 nm
            host lane count is 8
            media lane count is 4
            max module temperature is 75 deg C
            min module temperature is 0 deg C
            min operational voltage is 3.14 V
            vendor OUI is 447c7f
            date code is 200627
            clei code is CMUIAUNCAA
            power class is 6 (12.0 W maximum)
            max power is 12.00 W
            near-end lanes used none
            far-end lane code for 8 lanes Undefined
            media interface is 1310 nm EML
            Advertising code is Optical Interfaces: SMF
            Host electrical interface code is 400GAUI-8 C2M (Annex 120E)
            media interface advertising code is 400G-FR4

        Ethernet1/56
            transceiver is not present

        Ethernet1/63
            transceiver is present
            type is QSFP-DD-400G-DR4
            name is CISCO-INNOLIGHT
            part number is T-DP4CNH-NCI
            revision is 2B
            serial number is INL24173669
            nominal bitrate is 425000 MBit/sec per channel
            cisco id is 0x18
            cisco part number is 10-3320-01
            cisco product id is QDD-400G-DR4-S
            cisco version id is V01
            firmware version is 204.154
            Link length SMF is 0.5 km
            Nominal transmitter wavelength is 1311.00 nm
            Wavelength tolerance is 6.500 nm
            host lane count is 8
            media lane count is 4
            max module temperature is 75 deg C
            min module temperature is 0 deg C
            min operational voltage is 3.14 V
            vendor OUI is 447c7f
            date code is 200422
            clei code is CMUIAUPCAA
            power class is 6 (12.0 W maximum)
            max power is 12.00 W
            near-end lanes used none
            far-end lane code for 8 lanes Undefined
            media interface is 1310 nm EML
            Advertising code is Optical Interfaces: SMF
            Host electrical interface code is 400GAUI-8 C2M (Annex 120E)
            media interface advertising code is 400GBASE-DR4 (Cl 124)
        '''
    }

    golden_parsed_output_2 = {
        "Ethernet1/1": {
            "advertising_code": "Passive Cu",
            "cable_attenuation": "0/0/0/0/0 dB for bands 5/7/12.9/25.8/56 " "GHz",
            "cable_length": 2.0,
            "cis_part_number": "37-1843-01",
            "cis_product_id": "QDD-400-CU2M",
            "cis_version_id": "V01",
            "cisco_id": "0x18",
            "clei": "CMPQAGSCAA",
            "cmis_ver": 4,
            "date_code": "20031400",
            "far_end_lanes": "8 lanes aaaaaaaa",
            "host_electrical_intf": "200GAUI-4 C2M (Annex 120E)",
            "max_power": 1.5,
            "media_interface": "copper cable unequalized",
            "name": "CISCO-LEONI",
            "near_end_lanes": "none",
            "nominal_bitrate": 425000,
            "part_number": "L45593-K218-C20",
            "power_class": "1 (1.5 W maximum)",
            "revision": "00",
            "serial_number": "LCC2411GG1W-A",
            "vendor_oui": "a8b0ae",
            "transceiver_present": True,
            "transceiver_type": "QSFP-DD-400G-COPPER",
        },
        "Ethernet1/30": {
            "cis_part_number": "37-1317-03",
            "cis_product_id": "QSFP-H40G-CU3M",
            "cis_version_id": "V03",
            "cisco_id": "13",
            "name": "CISCO-TYCO",
            "nominal_bitrate": 10300,
            "part_number": "2821248-5",
            "revision": "D",
            "serial_number": "TED2318K1QR-B",
            "transceiver_present": True,
            "transceiver_type": "QSFP-40G-CR4",
        },
        "Ethernet1/52": {
            "advertising_code": "Optical Interfaces: SMF",
            "cis_part_number": "10-3321-01",
            "cis_product_id": "QDD-400G-FR4-S",
            "cis_version_id": "V01",
            "cisco_id": "0x18",
            "clei": "CMUIAUNCAA",
            "date_code": "200627",
            "far_end_lanes": "8 lanes Undefined",
            "firmware_ver": "204.154",
            "host_electrical_intf": "400GAUI-8 C2M (Annex 120E)",
            "host_lane_count": 8,
            "link_length": "2 km",
            "max_mod_temp": 75,
            "max_power": 12.0,
            "media_interface": "1310 nm EML",
            "media_interface_advert_code": "400G-FR4",
            "media_lane_count": 4,
            "min_mod_temp": 0,
            "min_oper_volt": "3.14 V",
            "name": "CISCO-INNOLIGHT",
            "near_end_lanes": "none",
            "nominal_bitrate": 425000,
            "nominal_trans_wavelength": "1301.00 nm",
            "part_number": "T-DQ4CNT-NCI",
            "power_class": "6 (12.0 W maximum)",
            "revision": "2B",
            "serial_number": "INL24265523",
            "vendor_oui": "447c7f",
            "wavelength_tolerance": "6.500 nm",
            "transceiver_present": True,
            "transceiver_type": "QSFP-DD-400G-FR4",
        },
        "Ethernet1/56": {
            "transceiver_present": False
        },
        "Ethernet1/63": {
            "advertising_code": "Optical Interfaces: SMF",
            "cis_part_number": "10-3320-01",
            "cis_product_id": "QDD-400G-DR4-S",
            "cis_version_id": "V01",
            "cisco_id": "0x18",
            "clei": "CMUIAUPCAA",
            "date_code": "200422",
            "far_end_lanes": "8 lanes Undefined",
            "firmware_ver": "204.154",
            "host_electrical_intf": "400GAUI-8 C2M (Annex 120E)",
            "host_lane_count": 8,
            "link_length": "0.5 km",
            "max_mod_temp": 75,
            "max_power": 12.0,
            "media_interface": "1310 nm EML",
            "media_interface_advert_code": "400GBASE-DR4 (Cl 124)",
            "media_lane_count": 4,
            "min_mod_temp": 0,
            "min_oper_volt": "3.14 V",
            "name": "CISCO-INNOLIGHT",
            "near_end_lanes": "none",
            "nominal_bitrate": 425000,
            "nominal_trans_wavelength": "1311.00 nm",
            "part_number": "T-DP4CNH-NCI",
            "power_class": "6 (12.0 W maximum)",
            "revision": "2B",
            "serial_number": "INL24173669",
            "vendor_oui": "447c7f",
            "wavelength_tolerance": "6.500 nm",
            "transceiver_present": True,
            "transceiver_type": "QSFP-DD-400G-DR4",
        },
    }


    def test_empty(self):
        self.maxDiff = None
        self.device = Mock(**self.empty_output)
        obj = ShowInterfaceTransceiver(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output)
        obj = ShowInterfaceTransceiver(device=self.device)
        parsed_output = obj.parse(interface='Ethernet1/4')

        self.assertEqual(parsed_output, self.golden_parsed_output)

    def test_golden2(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_1)
        obj = ShowInterfaceTransceiver(device=self.device)
        parsed_output = obj.parse(interface='Ethernet1/2')

        self.assertEqual(parsed_output, self.golden_parsed_output_1)

    def test_golden3(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_2)
        obj = ShowInterfaceTransceiver(device=self.device)
        parsed_output = obj.parse()

        self.assertEqual(parsed_output, self.golden_parsed_output_2)

# ==================================================
# Unit test for 'show interface transceiver details'
# ==================================================
class TestShowInterfaceTransceiverDetails(unittest.TestCase):
    '''unit test for "show interface transceiver details'''
    device = Device(name='aDevice')

    empty_output = {'execute.return_value': ''}

    golden_output={'execute.return_value': '''
        Ethernet1/1
            transceiver is present
            type is QSFP-DD-400G-COPPER
            name is CISCO-LEONI
            part number is L45593-K218-C20
            revision is 00
            serial number is LCC2411GG1W-A
            nominal bitrate is 425000 MBit/sec per channel
            cisco id is 0x18
            cisco part number is 37-1843-01
            cisco product id is QDD-400-CU2M
            cisco version id is V01
            vendor OUI is a8b0ae
            date code is 20031400
            clei code is CMPQAGSCAA
            power class is 1 (1.5 W maximum)
            max power is 1.50 W
            cable attenuation is 0/0/0/0/0 dB for bands 5/7/12.9/25.8/56 GHz
            near-end lanes used none
            far-end lane code for 8 lanes aaaaaaaa
            media interface is copper cable unequalized
            Advertising code is Passive Cu
            Host electrical interface code is Undefined
            Cable Length is   2.0 M
            CMIS version is  4

        DOM is not supported
        '''
    }

    golden_parsed_output= {
        "Ethernet1/1": {
            "advertising_code": "Passive Cu",
            "cable_attenuation": "0/0/0/0/0 dB for bands 5/7/12.9/25.8/56 " "GHz",
            "cable_length": 2.0,
            "cis_part_number": "37-1843-01",
            "cis_product_id": "QDD-400-CU2M",
            "cis_version_id": "V01",
            "cisco_id": "0x18",
            "clei": "CMPQAGSCAA",
            "cmis_ver": 4,
            "date_code": "20031400",
            "dom_supported": False,
            "far_end_lanes": "8 lanes aaaaaaaa",
            "host_electrical_intf": "Undefined",
            "max_power": 1.5,
            "media_interface": "copper cable unequalized",
            "name": "CISCO-LEONI",
            "near_end_lanes": "none",
            "nominal_bitrate": 425000,
            "part_number": "L45593-K218-C20",
            "power_class": "1 (1.5 W maximum)",
            "revision": "00",
            "serial_number": "LCC2411GG1W-A",
            "vendor_oui": "a8b0ae",
            "transceiver_present": True,
            "transceiver_type": "QSFP-DD-400G-COPPER",
        }
    }


    golden_output_1 = {'execute.return_value': '''
        Ethernet1/63
            transceiver is present
            type is QSFP-DD-400G-DR4
            name is CISCO-INNOLIGHT
            part number is T-DP4CNH-NCI
            revision is 2B
            serial number is INL24173669
            nominal bitrate is 425000 MBit/sec per channel
            cisco id is 0x18
            cisco part number is 10-3320-01
            cisco product id is QDD-400G-DR4-S
            cisco version id is V01
            firmware version is 204.154
            Link length SMF is 0.5 km
            Nominal transmitter wavelength is 1311.00 nm
            Wavelength tolerance is 6.500 nm
            host lane count is 8
            media lane count is 4
            max module temperature is 75 deg C
            min module temperature is 0 deg C
            min operational voltage is 3.14 V
            vendor OUI is 447c7f
            date code is 200422
            clei code is CMUIAUPCAA
            power class is 6 (12.0 W maximum)
            max power is 12.00 W
            near-end lanes used none
            far-end lane code for 8 lanes Undefined
            media interface is 1310 nm EML
            Advertising code is Optical Interfaces: SMF
            Host electrical interface code is 400GAUI-8 C2M (Annex 120E)
            media interface advertising code is 400GBASE-DR4 (Cl 124)

        Lane Number:1 Network Lane
          ----------------------------------------------------------------------------
                        Current              Alarms                  Warnings
                        Measurement     High        Low         High          Low
          ----------------------------------------------------------------------------
          Temperature   21.02 C        80.00 C     -5.00 C     75.00 C        0.00 C
          Voltage        3.33 V         3.63 V      2.97 V      3.46 V        3.13 V
          Current           N/A       120.00 mA    20.00 mA   110.00 mA      30.00 mA
          Tx Power          N/A         6.99 dBm   -6.90 dBm    3.99 dBm     -2.90 dBm
          Rx Power          N/A         6.99 dBm   -9.91 dBm    3.99 dBm     -5.90 dBm
          Transmit Fault Count = 0
          ----------------------------------------------------------------------------
          Note: ++  high-alarm; +  high-warning; --  low-alarm; -  low-warning

        Lane Number:2 Network Lane
          ----------------------------------------------------------------------------
                        Current              Alarms                  Warnings
                        Measurement     High        Low         High          Low
          ----------------------------------------------------------------------------
          Temperature   21.02 C        80.00 C     -5.00 C     75.00 C        0.00 C
          Voltage        3.33 V         3.63 V      2.97 V      3.46 V        3.13 V
          Current           N/A       120.00 mA    20.00 mA   110.00 mA      30.00 mA
          Tx Power          N/A         6.99 dBm   -6.90 dBm    3.99 dBm     -2.90 dBm
          Rx Power          N/A         6.99 dBm   -9.91 dBm    3.99 dBm     -5.90 dBm
          Transmit Fault Count = 0
          ----------------------------------------------------------------------------
          Note: ++  high-alarm; +  high-warning; --  low-alarm; -  low-warning

        Lane Number:3 Network Lane
          ----------------------------------------------------------------------------
                        Current              Alarms                  Warnings
                        Measurement     High        Low         High          Low
          ----------------------------------------------------------------------------
          Temperature   21.02 C        80.00 C     -5.00 C     75.00 C        0.00 C
          Voltage        3.33 V         3.63 V      2.97 V      3.46 V        3.13 V
          Current           N/A       120.00 mA    20.00 mA   110.00 mA      30.00 mA
          Tx Power          N/A         6.99 dBm   -6.90 dBm    3.99 dBm     -2.90 dBm
          Rx Power          N/A         6.99 dBm   -9.91 dBm    3.99 dBm     -5.90 dBm
          Transmit Fault Count = 0
          ----------------------------------------------------------------------------
          Note: ++  high-alarm; +  high-warning; --  low-alarm; -  low-warning

        Lane Number:4 Network Lane
          ----------------------------------------------------------------------------
                        Current              Alarms                  Warnings
                        Measurement     High        Low         High          Low
          ----------------------------------------------------------------------------
          Temperature   21.02 C        80.00 C     -5.00 C     75.00 C        0.00 C
          Voltage        3.33 V         3.63 V      2.97 V      3.46 V        3.13 V
          Current           N/A       120.00 mA    20.00 mA   110.00 mA      30.00 mA
          Tx Power          N/A         6.99 dBm   -6.90 dBm    3.99 dBm     -2.90 dBm
          Rx Power          N/A         6.99 dBm   -9.91 dBm    3.99 dBm     -5.90 dBm
          Transmit Fault Count = 0
          ----------------------------------------------------------------------------
          Note: ++  high-alarm; +  high-warning; --  low-alarm; -  low-warning
                
        '''
    }

    golden_parsed_output_1 = {
        "Ethernet1/63": {
            "lane_number" : {
                "1 Network Lane": {
                    "Current": {
                        "alarm": "None",
                        "current": "N/A",
                        "high_alarm": "120.00",
                        "high_warning": "110.00",
                        "low_alarm": "20.00",
                        "low_warning": "30.00",
                    },
                    "Rx Power": {
                        "alarm": "None",
                        "current": "N/A",
                        "high_alarm": "6.99",
                        "high_warning": "3.99",
                        "low_alarm": "-9.91",
                        "low_warning": "-5.90",
                    },
                    "Temperature": {
                        "alarm": "None",
                        "current": "21.02",
                        "high_alarm": "80.00",
                        "high_warning": "75.00",
                        "low_alarm": "-5.00",
                        "low_warning": "0.00",
                    },
                    "Tx Power": {
                        "alarm": "None",
                        "current": "N/A",
                        "high_alarm": "6.99",
                        "high_warning": "3.99",
                        "low_alarm": "-6.90",
                        "low_warning": "-2.90",
                    },
                    "Voltage": {
                        "alarm": "None",
                        "current": "3.33",
                        "high_alarm": "3.63",
                        "high_warning": "3.46",
                        "low_alarm": "2.97",
                        "low_warning": "3.13",
                    },
                    "tx_fault_count": 0,
                },
                "2 Network Lane": {
                    "Current": {
                        "alarm": "None",
                        "current": "N/A",
                        "high_alarm": "120.00",
                        "high_warning": "110.00",
                        "low_alarm": "20.00",
                        "low_warning": "30.00",
                    },
                    "Rx Power": {
                        "alarm": "None",
                        "current": "N/A",
                        "high_alarm": "6.99",
                        "high_warning": "3.99",
                        "low_alarm": "-9.91",
                        "low_warning": "-5.90",
                    },
                    "Temperature": {
                        "alarm": "None",
                        "current": "21.02",
                        "high_alarm": "80.00",
                        "high_warning": "75.00",
                        "low_alarm": "-5.00",
                        "low_warning": "0.00",
                    },
                    "Tx Power": {
                        "alarm": "None",
                        "current": "N/A",
                        "high_alarm": "6.99",
                        "high_warning": "3.99",
                        "low_alarm": "-6.90",
                        "low_warning": "-2.90",
                    },
                    "Voltage": {
                        "alarm": "None",
                        "current": "3.33",
                        "high_alarm": "3.63",
                        "high_warning": "3.46",
                        "low_alarm": "2.97",
                        "low_warning": "3.13",
                    },
                    "tx_fault_count": 0,
                },
                "3 Network Lane": {
                    "Current": {
                        "alarm": "None",
                        "current": "N/A",
                        "high_alarm": "120.00",
                        "high_warning": "110.00",
                        "low_alarm": "20.00",
                        "low_warning": "30.00",
                    },
                    "Rx Power": {
                        "alarm": "None",
                        "current": "N/A",
                        "high_alarm": "6.99",
                        "high_warning": "3.99",
                        "low_alarm": "-9.91",
                        "low_warning": "-5.90",
                    },
                    "Temperature": {
                        "alarm": "None",
                        "current": "21.02",
                        "high_alarm": "80.00",
                        "high_warning": "75.00",
                        "low_alarm": "-5.00",
                        "low_warning": "0.00",
                    },
                    "Tx Power": {
                        "alarm": "None",
                        "current": "N/A",
                        "high_alarm": "6.99",
                        "high_warning": "3.99",
                        "low_alarm": "-6.90",
                        "low_warning": "-2.90",
                    },
                    "Voltage": {
                        "alarm": "None",
                        "current": "3.33",
                        "high_alarm": "3.63",
                        "high_warning": "3.46",
                        "low_alarm": "2.97",
                        "low_warning": "3.13",
                    },
                    "tx_fault_count": 0,
                },
                "4 Network Lane": {
                    "Current": {
                        "alarm": "None",
                        "current": "N/A",
                        "high_alarm": "120.00",
                        "high_warning": "110.00",
                        "low_alarm": "20.00",
                        "low_warning": "30.00",
                    },
                    "Rx Power": {
                        "alarm": "None",
                        "current": "N/A",
                        "high_alarm": "6.99",
                        "high_warning": "3.99",
                        "low_alarm": "-9.91",
                        "low_warning": "-5.90",
                    },
                    "Temperature": {
                        "alarm": "None",
                        "current": "21.02",
                        "high_alarm": "80.00",
                        "high_warning": "75.00",
                        "low_alarm": "-5.00",
                        "low_warning": "0.00",
                    },
                    "Tx Power": {
                        "alarm": "None",
                        "current": "N/A",
                        "high_alarm": "6.99",
                        "high_warning": "3.99",
                        "low_alarm": "-6.90",
                        "low_warning": "-2.90",
                    },
                    "Voltage": {
                        "alarm": "None",
                        "current": "3.33",
                        "high_alarm": "3.63",
                        "high_warning": "3.46",
                        "low_alarm": "2.97",
                        "low_warning": "3.13",
                    },
                    "tx_fault_count": 0,
                },
            },
            "advertising_code": "Optical Interfaces: SMF",
            "cis_part_number": "10-3320-01",
            "cis_product_id": "QDD-400G-DR4-S",
            "cis_version_id": "V01",
            "cisco_id": "0x18",
            "clei": "CMUIAUPCAA",
            "date_code": "200422",
            "dom_supported": True,
            "far_end_lanes": "8 lanes Undefined",
            "firmware_ver": "204.154",
            "host_electrical_intf": "400GAUI-8 C2M (Annex 120E)",
            "host_lane_count": 8,
            "link_length": "0.5 km",
            "max_mod_temp": 75,
            "max_power": 12.0,
            "media_interface": "1310 nm EML",
            "media_interface_advert_code": "400GBASE-DR4 (Cl 124)",
            "media_lane_count": 4,
            "min_mod_temp": 0,
            "min_oper_volt": "3.14 V",
            "name": "CISCO-INNOLIGHT",
            "near_end_lanes": "none",
            "nominal_bitrate": 425000,
            "nominal_trans_wavelength": "1311.00 nm",
            "part_number": "T-DP4CNH-NCI",
            "power_class": "6 (12.0 W maximum)",
            "revision": "2B",
            "serial_number": "INL24173669",
            "vendor_oui": "447c7f",
            "wavelength_tolerance": "6.500 nm",
            "transceiver_present": True,
            "transceiver_type": "QSFP-DD-400G-DR4",
        }
    }


    golden_output_2={'execute.return_value': '''
        Ethernet1/44
            transceiver is present
            type is QSFP-100G-AOC2M
            name is CISCO-DELTA
            part number is QAOC-100G4F1A02C
            revision is A
            serial number is DTS2419B340-B
            nominal bitrate is 25500 MBit/sec
            cisco id is 17
            cisco extended id number is 156
            cisco part number is 10-3173-03
            cisco product id is QSFP-100G-AOC2M
            cisco version id is V03

        DOM is not supported

        Ethernet1/45
            transceiver is present
            type is QSFP-40G-CR4
            name is CISCO-TYCO
            part number is 2821248-3
            revision is D
            serial number is TED2027JJ2T-B
            nominal bitrate is 10300 MBit/sec per channel
            Link length supported for copper is 1 m
            cisco id is 13
            cisco extended id number is 16
            cisco part number is 37-1322-03
            cisco product id is QSFP-H40G-CU1M
            cisco version id is V03

        DOM is not supported

        Ethernet1/46
            transceiver is present
            type is QSFP-40G-CR4
            name is CISCO-TYCO
            part number is 2821248-3
            revision is D
            serial number is TED2027JJ2T-A
            nominal bitrate is 10300 MBit/sec per channel
            Link length supported for copper is 1 m
            cisco id is 13
            cisco extended id number is 16
            cisco part number is 37-1322-03
            cisco product id is QSFP-H40G-CU1M
            cisco version id is V03

        DOM is not supported

        Ethernet1/47
            transceiver is present
            type is QSFP-DD-400G-DR4
            name is CISCO-INNOLIGHT
            part number is T-DP4CNH-NCI
            revision is 2B
            serial number is INL24173686
            nominal bitrate is 425000 MBit/sec per channel
            cisco id is 0x18
            cisco part number is 10-3320-01
            cisco product id is QDD-400G-DR4-S
            cisco version id is V01
            firmware version is 204.154
            Link length SMF is 0.5 km
            Nominal transmitter wavelength is 1311.00 nm
            Wavelength tolerance is 6.500 nm
            host lane count is 8
            media lane count is 4
            max module temperature is 75 deg C
            min module temperature is 0 deg C
            min operational voltage is 3.14 V
            vendor OUI is 447c7f
            date code is 200422
            clei code is CMUIAUPCAA
            power class is 6 (12.0 W maximum)
            max power is 12.00 W
            near-end lanes used none
            far-end lane code for 8 lanes Undefined
            media interface is 1310 nm EML
            Advertising code is Optical Interfaces: SMF
            Host electrical interface code is 400GAUI-8 C2M (Annex 120E)
            media interface advertising code is 400GBASE-DR4 (Cl 124)

        Lane Number:1 Network Lane
          ----------------------------------------------------------------------------
                        Current              Alarms                  Warnings
                        Measurement     High        Low         High          Low
          ----------------------------------------------------------------------------
          Temperature   22.99 C        80.00 C     -5.00 C     75.00 C        0.00 C
          Voltage        3.34 V         3.63 V      2.97 V      3.46 V        3.13 V
          Current           N/A       120.00 mA    20.00 mA   110.00 mA      30.00 mA
          Tx Power          N/A         6.99 dBm   -6.90 dBm    3.99 dBm     -2.90 dBm
          Rx Power          N/A         6.99 dBm   -9.91 dBm    3.99 dBm     -5.90 dBm
          Transmit Fault Count = 0
          ----------------------------------------------------------------------------
          Note: ++  high-alarm; +  high-warning; --  low-alarm; -  low-warning

        Lane Number:2 Network Lane
          ----------------------------------------------------------------------------
                        Current              Alarms                  Warnings
                        Measurement     High        Low         High          Low
          ----------------------------------------------------------------------------
          Temperature   22.99 C        80.00 C     -5.00 C     75.00 C        0.00 C
          Voltage        3.34 V         3.63 V      2.97 V      3.46 V        3.13 V
          Current           N/A       120.00 mA    20.00 mA   110.00 mA      30.00 mA
          Tx Power          N/A         6.99 dBm   -6.90 dBm    3.99 dBm     -2.90 dBm
          Rx Power          N/A         6.99 dBm   -9.91 dBm    3.99 dBm     -5.90 dBm
          Transmit Fault Count = 0
          ----------------------------------------------------------------------------
          Note: ++  high-alarm; +  high-warning; --  low-alarm; -  low-warning

        Lane Number:3 Network Lane
          ----------------------------------------------------------------------------
                        Current              Alarms                  Warnings
                        Measurement     High        Low         High          Low
          ----------------------------------------------------------------------------
          Temperature   22.99 C        80.00 C     -5.00 C     75.00 C        0.00 C
          Voltage        3.34 V         3.63 V      2.97 V      3.46 V        3.13 V
          Current           N/A       120.00 mA    20.00 mA   110.00 mA      30.00 mA
          Tx Power          N/A         6.99 dBm   -6.90 dBm    3.99 dBm     -2.90 dBm
          Rx Power          N/A         6.99 dBm   -9.91 dBm    3.99 dBm     -5.90 dBm
          Transmit Fault Count = 0
          ----------------------------------------------------------------------------
          Note: ++  high-alarm; +  high-warning; --  low-alarm; -  low-warning

        Lane Number:4 Network Lane
          ----------------------------------------------------------------------------
                        Current              Alarms                  Warnings
                        Measurement     High        Low         High          Low
          ----------------------------------------------------------------------------
          Temperature   22.99 C        80.00 C     -5.00 C     75.00 C        0.00 C
          Voltage        3.34 V         3.63 V      2.97 V      3.46 V        3.13 V
          Current           N/A       120.00 mA    20.00 mA   110.00 mA      30.00 mA
          Tx Power          N/A         6.99 dBm   -6.90 dBm    3.99 dBm     -2.90 dBm
          Rx Power          N/A         6.99 dBm   -9.91 dBm    3.99 dBm     -5.90 dBm
          Transmit Fault Count = 0
          ----------------------------------------------------------------------------
          Note: ++  high-alarm; +  high-warning; --  low-alarm; -  low-warning

        Ethernet1/48
            transceiver is present
            type is QSFP-H40G-AOC7M
            name is CISCO-FINISAR
            part number is FCBN410QE2C07-C3
            revision is A
            serial number is FIW234501JT-B
            nominal bitrate is 10300 MBit/sec per channel
            cisco id is 13
            cisco extended id number is 16
            cisco part number is 10-2930-03
            cisco product id is QSFP-H40G-AOC7M
            cisco version id is V03

        DOM is not supported

        Ethernet1/49
            transceiver is present
            type is QSFP-H40G-AOC3M
            name is CISCO-FINISAR
            part number is FCBN410QE2C03-C2
            revision is A
            serial number is FIW232200C5-A
            nominal bitrate is 10300 MBit/sec per channel
            cisco id is 13
            cisco extended id number is 16
            cisco part number is 10-2927-02
            cisco product id is QSFP-H40G-AOC3M
            cisco version id is V02

        DOM is not supported

        Ethernet1/50
            transceiver is present
            type is QSFP-100G-PSM4
            name is CISCO-LUXTERA
            part number is LUX42604BO
            revision is B
            serial number is CVR2225001K
            nominal bitrate is 25500 MBit/sec
            Link length supported for 9/125um fiber is 500 m
            cisco id is 17
            cisco extended id number is 220
            cisco part number is 10-3144-01
            cisco product id is QSFP-100G-PSM4-S
            cisco version id is V01

        Lane Number:1 Network Lane
                   SFP Detail Diagnostics Information (internal calibration)
          ----------------------------------------------------------------------------
                        Current              Alarms                  Warnings
                        Measurement     High        Low         High          Low
          ----------------------------------------------------------------------------
          Temperature   16.58 C        75.00 C     -5.00 C     70.00 C        0.00 C
          Voltage        3.27 V         3.63 V      2.97 V      3.46 V        3.13 V
          Current       47.25 mA      125.30 mA    10.50 mA   120.00 mA      14.00 mA
          Tx Power          N/A         4.99 dBm  -13.46 dBm    1.99 dBm     -9.43 dBm
          Rx Power     -13.97 dBm  -    4.99 dBm  -16.77 dBm    1.99 dBm    -12.67 dBm
          Transmit Fault Count = 0
          ----------------------------------------------------------------------------
          Note: ++  high-alarm; +  high-warning; --  low-alarm; -  low-warning

        Lane Number:2 Network Lane
                   SFP Detail Diagnostics Information (internal calibration)
          ----------------------------------------------------------------------------
                        Current              Alarms                  Warnings
                        Measurement     High        Low         High          Low
          ----------------------------------------------------------------------------
          Temperature   16.58 C        75.00 C     -5.00 C     70.00 C        0.00 C
          Voltage        3.27 V         3.63 V      2.97 V      3.46 V        3.13 V
          Current       47.25 mA      125.30 mA    10.50 mA   120.00 mA      14.00 mA
          Tx Power          N/A         4.99 dBm  -13.46 dBm    1.99 dBm     -9.43 dBm
          Rx Power     -14.68 dBm  -    4.99 dBm  -16.77 dBm    1.99 dBm    -12.67 dBm
          Transmit Fault Count = 0
          ----------------------------------------------------------------------------
          Note: ++  high-alarm; +  high-warning; --  low-alarm; -  low-warning

        Lane Number:3 Network Lane
                   SFP Detail Diagnostics Information (internal calibration)
          ----------------------------------------------------------------------------
                        Current              Alarms                  Warnings
                        Measurement     High        Low         High          Low
          ----------------------------------------------------------------------------
          Temperature   16.58 C        75.00 C     -5.00 C     70.00 C        0.00 C
          Voltage        3.27 V         3.63 V      2.97 V      3.46 V        3.13 V
          Current       47.25 mA      125.30 mA    10.50 mA   120.00 mA      14.00 mA
          Tx Power          N/A         4.99 dBm  -13.46 dBm    1.99 dBm     -9.43 dBm
          Rx Power     -15.08 dBm  -    4.99 dBm  -16.77 dBm    1.99 dBm    -12.67 dBm
          Transmit Fault Count = 0
          ----------------------------------------------------------------------------
          Note: ++  high-alarm; +  high-warning; --  low-alarm; -  low-warning

        Lane Number:4 Network Lane
                   SFP Detail Diagnostics Information (internal calibration)
          ----------------------------------------------------------------------------
                        Current              Alarms                  Warnings
                        Measurement     High        Low         High          Low
          ----------------------------------------------------------------------------
          Temperature   16.58 C        75.00 C     -5.00 C     70.00 C        0.00 C
          Voltage        3.27 V         3.63 V      2.97 V      3.46 V        3.13 V
          Current       47.25 mA      125.30 mA    10.50 mA   120.00 mA      14.00 mA
          Tx Power          N/A         4.99 dBm  -13.46 dBm    1.99 dBm     -9.43 dBm
          Rx Power     -13.66 dBm  -    4.99 dBm  -16.77 dBm    1.99 dBm    -12.67 dBm
          Transmit Fault Count = 0
          ----------------------------------------------------------------------------
          Note: ++  high-alarm; +  high-warning; --  low-alarm; -  low-warning
        '''
    }

    golden_parsed_output_2 = {
        "Ethernet1/44": {
            "cis_part_number": "10-3173-03",
            "cis_product_id": "QSFP-100G-AOC2M",
            "cis_version_id": "V03",
            "cisco_id": "17",
            "dom_supported": False,
            "name": "CISCO-DELTA",
            "nominal_bitrate": 25500,
            "part_number": "QAOC-100G4F1A02C",
            "revision": "A",
            "serial_number": "DTS2419B340-B",
            "transceiver_present": True,
            "transceiver_type": "QSFP-100G-AOC2M",
        },
        "Ethernet1/45": {
            "cis_part_number": "37-1322-03",
            "cis_product_id": "QSFP-H40G-CU1M",
            "cis_version_id": "V03",
            "cisco_id": "13",
            "dom_supported": False,
            "name": "CISCO-TYCO",
            "nominal_bitrate": 10300,
            "part_number": "2821248-3",
            "revision": "D",
            "serial_number": "TED2027JJ2T-B",
            "transceiver_present": True,
            "transceiver_type": "QSFP-40G-CR4",
        },
        "Ethernet1/46": {
            "cis_part_number": "37-1322-03",
            "cis_product_id": "QSFP-H40G-CU1M",
            "cis_version_id": "V03",
            "cisco_id": "13",
            "dom_supported": False,
            "name": "CISCO-TYCO",
            "nominal_bitrate": 10300,
            "part_number": "2821248-3",
            "revision": "D",
            "serial_number": "TED2027JJ2T-A",
            "transceiver_present": True,
            "transceiver_type": "QSFP-40G-CR4",
        },
        "Ethernet1/47": {
            "lane_number": {
                "1 Network Lane": {
                    "Current": {
                        "alarm": "None",
                        "current": "N/A",
                        "high_alarm": "120.00",
                        "high_warning": "110.00",
                        "low_alarm": "20.00",
                        "low_warning": "30.00",
                    },
                    "Rx Power": {
                        "alarm": "None",
                        "current": "N/A",
                        "high_alarm": "6.99",
                        "high_warning": "3.99",
                        "low_alarm": "-9.91",
                        "low_warning": "-5.90",
                    },
                    "Temperature": {
                        "alarm": "None",
                        "current": "22.99",
                        "high_alarm": "80.00",
                        "high_warning": "75.00",
                        "low_alarm": "-5.00",
                        "low_warning": "0.00",
                    },
                    "Tx Power": {
                        "alarm": "None",
                        "current": "N/A",
                        "high_alarm": "6.99",
                        "high_warning": "3.99",
                        "low_alarm": "-6.90",
                        "low_warning": "-2.90",
                    },
                    "Voltage": {
                        "alarm": "None",
                        "current": "3.34",
                        "high_alarm": "3.63",
                        "high_warning": "3.46",
                        "low_alarm": "2.97",
                        "low_warning": "3.13",
                    },
                    "tx_fault_count": 0,
                },
                "2 Network Lane": {
                    "Current": {
                        "alarm": "None",
                        "current": "N/A",
                        "high_alarm": "120.00",
                        "high_warning": "110.00",
                        "low_alarm": "20.00",
                        "low_warning": "30.00",
                    },
                    "Rx Power": {
                        "alarm": "None",
                        "current": "N/A",
                        "high_alarm": "6.99",
                        "high_warning": "3.99",
                        "low_alarm": "-9.91",
                        "low_warning": "-5.90",
                    },
                    "Temperature": {
                        "alarm": "None",
                        "current": "22.99",
                        "high_alarm": "80.00",
                        "high_warning": "75.00",
                        "low_alarm": "-5.00",
                        "low_warning": "0.00",
                    },
                    "Tx Power": {
                        "alarm": "None",
                        "current": "N/A",
                        "high_alarm": "6.99",
                        "high_warning": "3.99",
                        "low_alarm": "-6.90",
                        "low_warning": "-2.90",
                    },
                    "Voltage": {
                        "alarm": "None",
                        "current": "3.34",
                        "high_alarm": "3.63",
                        "high_warning": "3.46",
                        "low_alarm": "2.97",
                        "low_warning": "3.13",
                    },
                    "tx_fault_count": 0,
                },
                "3 Network Lane": {
                    "Current": {
                        "alarm": "None",
                        "current": "N/A",
                        "high_alarm": "120.00",
                        "high_warning": "110.00",
                        "low_alarm": "20.00",
                        "low_warning": "30.00",
                    },
                    "Rx Power": {
                        "alarm": "None",
                        "current": "N/A",
                        "high_alarm": "6.99",
                        "high_warning": "3.99",
                        "low_alarm": "-9.91",
                        "low_warning": "-5.90",
                    },
                    "Temperature": {
                        "alarm": "None",
                        "current": "22.99",
                        "high_alarm": "80.00",
                        "high_warning": "75.00",
                        "low_alarm": "-5.00",
                        "low_warning": "0.00",
                    },
                    "Tx Power": {
                        "alarm": "None",
                        "current": "N/A",
                        "high_alarm": "6.99",
                        "high_warning": "3.99",
                        "low_alarm": "-6.90",
                        "low_warning": "-2.90",
                    },
                    "Voltage": {
                        "alarm": "None",
                        "current": "3.34",
                        "high_alarm": "3.63",
                        "high_warning": "3.46",
                        "low_alarm": "2.97",
                        "low_warning": "3.13",
                    },
                    "tx_fault_count": 0,
                },
                "4 Network Lane": {
                    "Current": {
                        "alarm": "None",
                        "current": "N/A",
                        "high_alarm": "120.00",
                        "high_warning": "110.00",
                        "low_alarm": "20.00",
                        "low_warning": "30.00",
                    },
                    "Rx Power": {
                        "alarm": "None",
                        "current": "N/A",
                        "high_alarm": "6.99",
                        "high_warning": "3.99",
                        "low_alarm": "-9.91",
                        "low_warning": "-5.90",
                    },
                    "Temperature": {
                        "alarm": "None",
                        "current": "22.99",
                        "high_alarm": "80.00",
                        "high_warning": "75.00",
                        "low_alarm": "-5.00",
                        "low_warning": "0.00",
                    },
                    "Tx Power": {
                        "alarm": "None",
                        "current": "N/A",
                        "high_alarm": "6.99",
                        "high_warning": "3.99",
                        "low_alarm": "-6.90",
                        "low_warning": "-2.90",
                    },
                    "Voltage": {
                        "alarm": "None",
                        "current": "3.34",
                        "high_alarm": "3.63",
                        "high_warning": "3.46",
                        "low_alarm": "2.97",
                        "low_warning": "3.13",
                    },
                    "tx_fault_count": 0,
                },
            },
            "advertising_code": "Optical Interfaces: SMF",
            "cis_part_number": "10-3320-01",
            "cis_product_id": "QDD-400G-DR4-S",
            "cis_version_id": "V01",
            "cisco_id": "0x18",
            "clei": "CMUIAUPCAA",
            "date_code": "200422",
            "dom_supported": True,
            "far_end_lanes": "8 lanes Undefined",
            "firmware_ver": "204.154",
            "host_electrical_intf": "400GAUI-8 C2M (Annex 120E)",
            "host_lane_count": 8,
            "link_length": "0.5 km",
            "max_mod_temp": 75,
            "max_power": 12.0,
            "media_interface": "1310 nm EML",
            "media_interface_advert_code": "400GBASE-DR4 (Cl 124)",
            "media_lane_count": 4,
            "min_mod_temp": 0,
            "min_oper_volt": "3.14 V",
            "name": "CISCO-INNOLIGHT",
            "near_end_lanes": "none",
            "nominal_bitrate": 425000,
            "nominal_trans_wavelength": "1311.00 nm",
            "part_number": "T-DP4CNH-NCI",
            "power_class": "6 (12.0 W maximum)",
            "revision": "2B",
            "serial_number": "INL24173686",
            "vendor_oui": "447c7f",
            "wavelength_tolerance": "6.500 nm",
            "transceiver_present": True,
            "transceiver_type": "QSFP-DD-400G-DR4",
        },
        "Ethernet1/48": {
            "cis_part_number": "10-2930-03",
            "cis_product_id": "QSFP-H40G-AOC7M",
            "cis_version_id": "V03",
            "cisco_id": "13",
            "dom_supported": False,
            "name": "CISCO-FINISAR",
            "nominal_bitrate": 10300,
            "part_number": "FCBN410QE2C07-C3",
            "revision": "A",
            "serial_number": "FIW234501JT-B",
            "transceiver_present": True,
            "transceiver_type": "QSFP-H40G-AOC7M",
        },
        "Ethernet1/49": {
            "cis_part_number": "10-2927-02",
            "cis_product_id": "QSFP-H40G-AOC3M",
            "cis_version_id": "V02",
            "cisco_id": "13",
            "dom_supported": False,
            "name": "CISCO-FINISAR",
            "nominal_bitrate": 10300,
            "part_number": "FCBN410QE2C03-C2",
            "revision": "A",
            "serial_number": "FIW232200C5-A",
            "transceiver_present": True,
            "transceiver_type": "QSFP-H40G-AOC3M",
        },
        "Ethernet1/50": {
            "lane_number": {
                "1 Network Lane": {
                    "Current": {
                        "alarm": "None",
                        "current": "47.25",
                        "high_alarm": "125.30",
                        "high_warning": "120.00",
                        "low_alarm": "10.50",
                        "low_warning": "14.00",
                    },
                    "Rx Power": {
                        "alarm": "-",
                        "current": "-13.97",
                        "high_alarm": "4.99",
                        "high_warning": "1.99",
                        "low_alarm": "-16.77",
                        "low_warning": "-12.67",
                    },
                    "Temperature": {
                        "alarm": "None",
                        "current": "16.58",
                        "high_alarm": "75.00",
                        "high_warning": "70.00",
                        "low_alarm": "-5.00",
                        "low_warning": "0.00",
                    },
                    "Tx Power": {
                        "alarm": "None",
                        "current": "N/A",
                        "high_alarm": "4.99",
                        "high_warning": "1.99",
                        "low_alarm": "-13.46",
                        "low_warning": "-9.43",
                    },
                    "Voltage": {
                        "alarm": "None",
                        "current": "3.27",
                        "high_alarm": "3.63",
                        "high_warning": "3.46",
                        "low_alarm": "2.97",
                        "low_warning": "3.13",
                    },
                    "tx_fault_count": 0,
                },
                "2 Network Lane": {
                    "Current": {
                        "alarm": "None",
                        "current": "47.25",
                        "high_alarm": "125.30",
                        "high_warning": "120.00",
                        "low_alarm": "10.50",
                        "low_warning": "14.00",
                    },
                    "Rx Power": {
                        "alarm": "-",
                        "current": "-14.68",
                        "high_alarm": "4.99",
                        "high_warning": "1.99",
                        "low_alarm": "-16.77",
                        "low_warning": "-12.67",
                    },
                    "Temperature": {
                        "alarm": "None",
                        "current": "16.58",
                        "high_alarm": "75.00",
                        "high_warning": "70.00",
                        "low_alarm": "-5.00",
                        "low_warning": "0.00",
                    },
                    "Tx Power": {
                        "alarm": "None",
                        "current": "N/A",
                        "high_alarm": "4.99",
                        "high_warning": "1.99",
                        "low_alarm": "-13.46",
                        "low_warning": "-9.43",
                    },
                    "Voltage": {
                        "alarm": "None",
                        "current": "3.27",
                        "high_alarm": "3.63",
                        "high_warning": "3.46",
                        "low_alarm": "2.97",
                        "low_warning": "3.13",
                    },
                    "tx_fault_count": 0,
                },
                "3 Network Lane": {
                    "Current": {
                        "alarm": "None",
                        "current": "47.25",
                        "high_alarm": "125.30",
                        "high_warning": "120.00",
                        "low_alarm": "10.50",
                        "low_warning": "14.00",
                    },
                    "Rx Power": {
                        "alarm": "-",
                        "current": "-15.08",
                        "high_alarm": "4.99",
                        "high_warning": "1.99",
                        "low_alarm": "-16.77",
                        "low_warning": "-12.67",
                    },
                    "Temperature": {
                        "alarm": "None",
                        "current": "16.58",
                        "high_alarm": "75.00",
                        "high_warning": "70.00",
                        "low_alarm": "-5.00",
                        "low_warning": "0.00",
                    },
                    "Tx Power": {
                        "alarm": "None",
                        "current": "N/A",
                        "high_alarm": "4.99",
                        "high_warning": "1.99",
                        "low_alarm": "-13.46",
                        "low_warning": "-9.43",
                    },
                    "Voltage": {
                        "alarm": "None",
                        "current": "3.27",
                        "high_alarm": "3.63",
                        "high_warning": "3.46",
                        "low_alarm": "2.97",
                        "low_warning": "3.13",
                    },
                    "tx_fault_count": 0,
                },
                "4 Network Lane": {
                    "Current": {
                        "alarm": "None",
                        "current": "47.25",
                        "high_alarm": "125.30",
                        "high_warning": "120.00",
                        "low_alarm": "10.50",
                        "low_warning": "14.00",
                    },
                    "Rx Power": {
                        "alarm": "-",
                        "current": "-13.66",
                        "high_alarm": "4.99",
                        "high_warning": "1.99",
                        "low_alarm": "-16.77",
                        "low_warning": "-12.67",
                    },
                    "Temperature": {
                        "alarm": "None",
                        "current": "16.58",
                        "high_alarm": "75.00",
                        "high_warning": "70.00",
                        "low_alarm": "-5.00",
                        "low_warning": "0.00",
                    },
                    "Tx Power": {
                        "alarm": "None",
                        "current": "N/A",
                        "high_alarm": "4.99",
                        "high_warning": "1.99",
                        "low_alarm": "-13.46",
                        "low_warning": "-9.43",
                    },
                    "Voltage": {
                        "alarm": "None",
                        "current": "3.27",
                        "high_alarm": "3.63",
                        "high_warning": "3.46",
                        "low_alarm": "2.97",
                        "low_warning": "3.13",
                    },
                    "tx_fault_count": 0,
                },
            },
            "cis_part_number": "10-3144-01",
            "cis_product_id": "QSFP-100G-PSM4-S",
            "cis_version_id": "V01",
            "cisco_id": "17",
            "dom_supported": True,
            "name": "CISCO-LUXTERA",
            "nominal_bitrate": 25500,
            "part_number": "LUX42604BO",
            "revision": "B",
            "serial_number": "CVR2225001K",
            "transceiver_present": True,
            "transceiver_type": "QSFP-100G-PSM4",
        },
    }


    def test_empty(self):
        self.maxDiff = None
        self.device = Mock(**self.empty_output)
        obj = ShowInterfaceTransceiverDetails(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output)
        obj = ShowInterfaceTransceiverDetails(device=self.device)
        parsed_output = obj.parse(interface='Ethernet1/1')
        
        self.assertEqual(parsed_output, self.golden_parsed_output)

    def test_golden2(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_1)
        obj = ShowInterfaceTransceiverDetails(device=self.device)
        parsed_output = obj.parse(interface='Ethernet1/63')
        
        self.assertEqual(parsed_output, self.golden_parsed_output_1)

    def test_golden3(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_2)
        obj = ShowInterfaceTransceiverDetails(device=self.device)
        parsed_output = obj.parse()
        
        self.assertEqual(parsed_output, self.golden_parsed_output_2)

# ===========================================
# Unit test for 'show interface fec'
# ===========================================
class TestShowInterfaceFec(unittest.TestCase):
    '''unit test for "show interface fec'''
    device = Device(name='aDevice')

    empty_output = {'execute.return_value': ''}

    golden_output={'execute.return_value': '''
        --------------------------------------------------------------------------------
        Name          Ifindex       Admin-fec Oper-fec  Status    Speed   Type
        --------------------------------------------------------------------------------
        Eth1/1        0x1a000000    auto      auto      disabled  auto    QSFP-DD-400G-COPPER
        Eth1/2        0x1a000200    auto      auto      disabled  auto    QSFP-DD-400G-COPPER
        Eth1/3        0x1a000400    auto      auto      disabled  auto    QSFP-40G-CR4
        Eth1/4        0x1a000600    auto      auto      disabled  auto    QSFP-40G-CR4
        Eth1/5        0x1a000800    auto      auto      disabled  auto    QSFP-100G-CR4
        Eth1/6        0x1a000a00    auto      auto      disabled  auto    QSFP-100G-AOC15M
        Eth1/7        0x1a000c00    auto      auto      disabled  auto    QSFP-40G-CR4
        Eth1/8        0x1a000e00    auto      auto      disabled  auto    QSFP-40G-CR4
        Eth1/9        0x1a001000    auto      auto      disabled  auto    QSFP-40G-CR4
        Eth1/10       0x1a001200    auto      auto      disabled  auto    QSFP-40G-CR4
        '''
    }

    golden_parsed_output = {
        "Eth1/1": {
            "admin-fec": "auto",
            "ifindex": "0x1a000000",
            "oper-fec": "auto",
            "speed": "auto",
            "status": "disabled",
            "type": "QSFP-DD-400G-COPPER",
        },
        "Eth1/10": {
            "admin-fec": "auto",
            "ifindex": "0x1a001200",
            "oper-fec": "auto",
            "speed": "auto",
            "status": "disabled",
            "type": "QSFP-40G-CR4",
        },
        "Eth1/2": {
            "admin-fec": "auto",
            "ifindex": "0x1a000200",
            "oper-fec": "auto",
            "speed": "auto",
            "status": "disabled",
            "type": "QSFP-DD-400G-COPPER",
        },
        "Eth1/3": {
            "admin-fec": "auto",
            "ifindex": "0x1a000400",
            "oper-fec": "auto",
            "speed": "auto",
            "status": "disabled",
            "type": "QSFP-40G-CR4",
        },
        "Eth1/4": {
            "admin-fec": "auto",
            "ifindex": "0x1a000600",
            "oper-fec": "auto",
            "speed": "auto",
            "status": "disabled",
            "type": "QSFP-40G-CR4",
        },
        "Eth1/5": {
            "admin-fec": "auto",
            "ifindex": "0x1a000800",
            "oper-fec": "auto",
            "speed": "auto",
            "status": "disabled",
            "type": "QSFP-100G-CR4",
        },
        "Eth1/6": {
            "admin-fec": "auto",
            "ifindex": "0x1a000a00",
            "oper-fec": "auto",
            "speed": "auto",
            "status": "disabled",
            "type": "QSFP-100G-AOC15M",
        },
        "Eth1/7": {
            "admin-fec": "auto",
            "ifindex": "0x1a000c00",
            "oper-fec": "auto",
            "speed": "auto",
            "status": "disabled",
            "type": "QSFP-40G-CR4",
        },
        "Eth1/8": {
            "admin-fec": "auto",
            "ifindex": "0x1a000e00",
            "oper-fec": "auto",
            "speed": "auto",
            "status": "disabled",
            "type": "QSFP-40G-CR4",
        },
        "Eth1/9": {
            "admin-fec": "auto",
            "ifindex": "0x1a001000",
            "oper-fec": "auto",
            "speed": "auto",
            "status": "disabled",
            "type": "QSFP-40G-CR4",
        },
    }



    def test_empty(self):
        self.maxDiff = None
        self.device = Mock(**self.empty_output)
        obj = ShowInterfaceTransceiverDetails(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output)
        obj = ShowInterfaceFec(device=self.device)
        parsed_output = obj.parse()
        
        self.assertEqual(parsed_output, self.golden_parsed_output)


# ===========================================
# Unit test for 'show interface hardware-mappings'
# ===========================================
class TestShowInterfaceHardwareMap(unittest.TestCase):
    '''unit test for "show interface hardware-mappings'''
    device = Device(name='aDevice')

    empty_output = {'execute.return_value': ''}

    golden_output={'execute.return_value': '''
        -------------------------------------------------------------------------------------------------------
        Name       Ifindex  Smod Unit HPort FPort NPort VPort Slice SPort SrcId MacId MacSP VIF  Block BlkSrcID
        -------------------------------------------------------------------------------------------------------
        Eth1/1/1   38000000 1    0    16    255   0     -1    0     16    32    4     0     1544 0     32
        Eth1/1/2   38001000 1    0    17    255   1     -1    0     17    34    4     2     1544 0     34
        Eth1/1/3   38002000 1    0    18    255   2     -1    0     18    36    4     4     3    0     36
        Eth1/1/4   38003000 1    0    19    255   3     -1    0     19    38    4     6     4    0     38
        Eth1/2/1   3800a000 1    0    12    255   4     -1    0     12    24    3     0     1544 0     24
        Eth1/2/2   3800b000 1    0    13    255   5     -1    0     13    26    3     2     6    0     26
        Eth1/2/3   3800c000 1    0    14    255   6     -1    0     14    28    3     4     7    0     28
        Eth1/2/4   3800d000 1    0    15    255   7     -1    0     15    30    3     6     8    0     30
        Eth1/3     1a000400 1    0    20    255   8     -1    0     20    40    5     0     9    0     40
        Eth1/4     1a000600 1    0    8     255   12    -1    0     8     16    2     0     13   0     16

        -------------------------------------------------------------------------------------------------------
        Name       Ifindex  Smod Unit HPort FPort NPort VPort Slice SPort SrcId MacId MacSP VIF  Block BlkSrcID
        -------------------------------------------------------------------------------------------------------
        Po1        16000000 0    0    1     0     54914 2     0     0     0     -1    -1    1537 0     0
        Po48       1600002f 0    0    2     0     54914 3     0     0     0     -1    -1    1538 0     0
        Po50       16000031 0    0    3     0     54914 4     0     0     0     -1    -1    1539 0     0
        Po52       16000033 0    0    4     0     54914 5     0     0     0     -1    -1    1540 0     0
        Po101      16000064 0    0    5     0     54914 6     0     0     0     -1    -1    1541 0     0
        Po102      16000065 0    0    6     0     54914 7     0     0     0     -1    -1    1542 0     0
        Po105      16000068 0    0    7     0     54914 8     0     0     0     -1    -1    1543 0     0
        Po130      16000081 0    0    8     0     54914 9     0     0     0     -1    -1    1544 0     0
        '''
    }

    golden_parsed_output = {
        "Ethernet1/1/1": {
            "blksrcid": 32,
            "block": 0,
            "fport": 255,
            "hport": 16,
            "ifindex": "38000000",
            "macid": 4,
            "macsp": 0,
            "nport": 0,
            "slice": 0,
            "smod": 1,
            "sport": 16,
            "srcid": 32,
            "unit": 0,
            "vif": 1544,
            "vport": -1,
        },
        "Ethernet1/1/2": {
            "blksrcid": 34,
            "block": 0,
            "fport": 255,
            "hport": 17,
            "ifindex": "38001000",
            "macid": 4,
            "macsp": 2,
            "nport": 1,
            "slice": 0,
            "smod": 1,
            "sport": 17,
            "srcid": 34,
            "unit": 0,
            "vif": 1544,
            "vport": -1,
        },
        "Ethernet1/1/3": {
            "blksrcid": 36,
            "block": 0,
            "fport": 255,
            "hport": 18,
            "ifindex": "38002000",
            "macid": 4,
            "macsp": 4,
            "nport": 2,
            "slice": 0,
            "smod": 1,
            "sport": 18,
            "srcid": 36,
            "unit": 0,
            "vif": 3,
            "vport": -1,
        },
        "Ethernet1/1/4": {
            "blksrcid": 38,
            "block": 0,
            "fport": 255,
            "hport": 19,
            "ifindex": "38003000",
            "macid": 4,
            "macsp": 6,
            "nport": 3,
            "slice": 0,
            "smod": 1,
            "sport": 19,
            "srcid": 38,
            "unit": 0,
            "vif": 4,
            "vport": -1,
        },
        "Ethernet1/2/1": {
            "blksrcid": 24,
            "block": 0,
            "fport": 255,
            "hport": 12,
            "ifindex": "3800a000",
            "macid": 3,
            "macsp": 0,
            "nport": 4,
            "slice": 0,
            "smod": 1,
            "sport": 12,
            "srcid": 24,
            "unit": 0,
            "vif": 1544,
            "vport": -1,
        },
        "Ethernet1/2/2": {
            "blksrcid": 26,
            "block": 0,
            "fport": 255,
            "hport": 13,
            "ifindex": "3800b000",
            "macid": 3,
            "macsp": 2,
            "nport": 5,
            "slice": 0,
            "smod": 1,
            "sport": 13,
            "srcid": 26,
            "unit": 0,
            "vif": 6,
            "vport": -1,
        },
        "Ethernet1/2/3": {
            "blksrcid": 28,
            "block": 0,
            "fport": 255,
            "hport": 14,
            "ifindex": "3800c000",
            "macid": 3,
            "macsp": 4,
            "nport": 6,
            "slice": 0,
            "smod": 1,
            "sport": 14,
            "srcid": 28,
            "unit": 0,
            "vif": 7,
            "vport": -1,
        },
        "Ethernet1/2/4": {
            "blksrcid": 30,
            "block": 0,
            "fport": 255,
            "hport": 15,
            "ifindex": "3800d000",
            "macid": 3,
            "macsp": 6,
            "nport": 7,
            "slice": 0,
            "smod": 1,
            "sport": 15,
            "srcid": 30,
            "unit": 0,
            "vif": 8,
            "vport": -1,
        },
        "Ethernet1/3": {
            "blksrcid": 40,
            "block": 0,
            "fport": 255,
            "hport": 20,
            "ifindex": "1a000400",
            "macid": 5,
            "macsp": 0,
            "nport": 8,
            "slice": 0,
            "smod": 1,
            "sport": 20,
            "srcid": 40,
            "unit": 0,
            "vif": 9,
            "vport": -1,
        },
        "Ethernet1/4": {
            "blksrcid": 16,
            "block": 0,
            "fport": 255,
            "hport": 8,
            "ifindex": "1a000600",
            "macid": 2,
            "macsp": 0,
            "nport": 12,
            "slice": 0,
            "smod": 1,
            "sport": 8,
            "srcid": 16,
            "unit": 0,
            "vif": 13,
            "vport": -1,
        },
        "Port-channel1": {
            "blksrcid": 0,
            "block": 0,
            "fport": 0,
            "hport": 1,
            "ifindex": "16000000",
            "macid": -1,
            "macsp": -1,
            "nport": 54914,
            "slice": 0,
            "smod": 0,
            "sport": 0,
            "srcid": 0,
            "unit": 0,
            "vif": 1537,
            "vport": 2,
        },
        "Port-channel101": {
            "blksrcid": 0,
            "block": 0,
            "fport": 0,
            "hport": 5,
            "ifindex": "16000064",
            "macid": -1,
            "macsp": -1,
            "nport": 54914,
            "slice": 0,
            "smod": 0,
            "sport": 0,
            "srcid": 0,
            "unit": 0,
            "vif": 1541,
            "vport": 6,
        },
        "Port-channel102": {
            "blksrcid": 0,
            "block": 0,
            "fport": 0,
            "hport": 6,
            "ifindex": "16000065",
            "macid": -1,
            "macsp": -1,
            "nport": 54914,
            "slice": 0,
            "smod": 0,
            "sport": 0,
            "srcid": 0,
            "unit": 0,
            "vif": 1542,
            "vport": 7,
        },
        "Port-channel105": {
            "blksrcid": 0,
            "block": 0,
            "fport": 0,
            "hport": 7,
            "ifindex": "16000068",
            "macid": -1,
            "macsp": -1,
            "nport": 54914,
            "slice": 0,
            "smod": 0,
            "sport": 0,
            "srcid": 0,
            "unit": 0,
            "vif": 1543,
            "vport": 8,
        },
        "Port-channel130": {
            "blksrcid": 0,
            "block": 0,
            "fport": 0,
            "hport": 8,
            "ifindex": "16000081",
            "macid": -1,
            "macsp": -1,
            "nport": 54914,
            "slice": 0,
            "smod": 0,
            "sport": 0,
            "srcid": 0,
            "unit": 0,
            "vif": 1544,
            "vport": 9,
        },
        "Port-channel48": {
            "blksrcid": 0,
            "block": 0,
            "fport": 0,
            "hport": 2,
            "ifindex": "1600002f",
            "macid": -1,
            "macsp": -1,
            "nport": 54914,
            "slice": 0,
            "smod": 0,
            "sport": 0,
            "srcid": 0,
            "unit": 0,
            "vif": 1538,
            "vport": 3,
        },
        "Port-channel50": {
            "blksrcid": 0,
            "block": 0,
            "fport": 0,
            "hport": 3,
            "ifindex": "16000031",
            "macid": -1,
            "macsp": -1,
            "nport": 54914,
            "slice": 0,
            "smod": 0,
            "sport": 0,
            "srcid": 0,
            "unit": 0,
            "vif": 1539,
            "vport": 4,
        },
        "Port-channel52": {
            "blksrcid": 0,
            "block": 0,
            "fport": 0,
            "hport": 4,
            "ifindex": "16000033",
            "macid": -1,
            "macsp": -1,
            "nport": 54914,
            "slice": 0,
            "smod": 0,
            "sport": 0,
            "srcid": 0,
            "unit": 0,
            "vif": 1540,
            "vport": 5,
        },
    }


    def test_empty(self):
        self.maxDiff = None
        self.device = Mock(**self.empty_output)
        obj = ShowInterfaceHardwareMap(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output)
        obj = ShowInterfaceHardwareMap(device=self.device)
        parsed_output = obj.parse()
        #import pprint 
        #pprint.pprint(parsed_output)
        
        self.assertEqual(parsed_output, self.golden_parsed_output)


if __name__ == '__main__':
    unittest.main()

# vim: ft=python et sw=4
