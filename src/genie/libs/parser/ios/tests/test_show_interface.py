#!/bin/env python

import sys
import unittest
from unittest.mock import Mock
from unittest.mock import patch
from textwrap import dedent

ats_mock = Mock()
with patch.dict('sys.modules',
        {'pyats' : ats_mock}, autospec=True):
    import genie.parsergen
    from genie.parsergen import oper_fill
    from genie.parsergen import oper_check
    from genie.parsergen import oper_fill_tabular

import xml.etree.ElementTree as ET

from pyats.topology import Device

from genie.metaparser.util.exceptions import SchemaEmptyParserError

from genie.libs.parser.ios.show_interface import \
                                        ShowIpInterfaceBriefPipeVlan,\
                                        ShowInterfaces, ShowIpInterface,\
                                        ShowIpv6Interface, \
                                        ShowInterfacesAccounting, \
                                        ShowIpInterfaceBriefPipeIp, \
                                        ShowInterfacesCounters, \
                                        ShowInterfacesSwitchport, \
                                        ShowInterfacesTrunk, \
                                        ShowInterfacesStats,\
                                        ShowInterfacesDescription, \
                                        ShowInterfacesStatus

from genie.libs.parser.iosxe.tests.test_show_interface import \
                TestShowInterfacesCounters as TestShowInterfacesCounters_iosxe,\
                TestShowInterfacesSwitchport as TestShowInterfacesSwitchport_iosxe,\
                TestShowInterfacesTrunk as TestShowInterfacesTrunk_iosxe,\
                TestShowInterfacesStats as TestShowInterfacesStats_iosxe,\
                TestShowInterfacesDescription as TestShowInterfacesDescription_iosxe, \
                TestShowInterfacesStatus as TestShowInterfacesStatus_iosxe


class TestShowInterfaceParsergen(unittest.TestCase):

    def test_tabular_parser(self):
        self.showCommandOutput='''
            R1#show ip interface brief 
            Interface              IP-Address      OK? Method Status                Protocol
            GigabitEthernet0/0     10.1.10.20      YES NVRAM  up                    up      
            GigabitEthernet1/0/1   unassigned      YES unset  up                    up         
            GigabitEthernet1/0/10  unassigned      YES unset  down                  down      
            '''

        self.outputDict = {'GigabitEthernet0/0': {'IP-Address': '10.1.10.20',
                                                  'Interface': 'GigabitEthernet0/0',
                                                  'Method': 'NVRAM',
                                                  'OK?': 'YES',
                                                  'Protocol': 'up',
                                                  'Status': 'up'},
                           'GigabitEthernet1/0/1': {'IP-Address': 'unassigned',
                                                    'Interface': 'GigabitEthernet1/0/1',
                                                    'Method': 'unset',
                                                    'OK?': 'YES',
                                                    'Protocol': 'up',
                                                    'Status': 'up'},
                           'GigabitEthernet1/0/10': {'IP-Address': 'unassigned',
                                                     'Interface': 'GigabitEthernet1/0/10',
                                                     'Method': 'unset',
                                                     'OK?': 'YES',
                                                     'Protocol': 'down',
                                                     'Status': 'down'}}

        # Define how device stub will behave when accessed by production parser.
        device_kwargs = {'is_connected.return_value':True,
                         'execute.return_value':dedent(self.showCommandOutput)}
        device1 = Mock(**device_kwargs)
        device1.name='router3'

        result = genie.parsergen.oper_fill_tabular(device=device1,
                                             show_command="show ip interface brief",
                                             refresh_cache=True,
                                             header_fields=
                                                 [ "Interface",
                                                   "IP-Address",
                                                   "OK\?",
                                                   "Method",
                                                   "Status",
                                                   "Protocol" ],
                                             label_fields=
                                                 [ "Interface",
                                                   "IP-Address",
                                                   "OK?",
                                                   "Method",
                                                   "Status",
                                                   "Protocol" ],
                                             index=[0])

        self.assertEqual(result.entries, self.outputDict)
        args, kwargs = device1.execute.call_args
        self.assertTrue('show ip interface brief' in args,
            msg='The expected command was not sent to the router')

#############################################################################
# unitest For Show ip interface | include <word>
#############################################################################
class TestShowIpInterfacesBriefPipeIp(unittest.TestCase):
    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}
    golden_parsed_output = {'interface':
        {'GigabitEthernet0/0': {'interface_ok': 'YES',
                                      'interface_status': 'up',
                                      'ip_address': '10.1.18.80',
                                      'method': 'NVRAM',
                                      'protocol_status': 'up'}}}

    golden_output = {'execute.return_value': '''
        R1#sh ip int brief | i 10.1.18.80 
        GigabitEthernet0/0     10.1.18.80      YES NVRAM  up                    up   
    '''}

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = ShowIpInterfaceBriefPipeIp(device=self.device)
        parsed_output = obj.parse(ip='10.1.18.80')
        self.assertEqual(parsed_output,self.golden_parsed_output)

    def test_empty(self):
        self.device1 = Mock(**self.empty_output)
        obj = ShowIpInterfaceBriefPipeIp(device=self.device1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse(ip='10.1.18.80')


#############################################################################
# unitest For Show Interfaces
#############################################################################
class TestShowInterfaces(unittest.TestCase):
    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}
    maxDiff = None
    golden_parsed_output = {
        "GigabitEthernet0/2.1": {
            "reliability": "255/255",
            "type": "iGbE",
            "delay": 10,
            "enabled": True,
            "txload": "1/255",
            "arp_type": "arpa",
            "encapsulations": {
               "encapsulation": "dot1q",
               "first_dot1q": "300"
            },
            "keepalive": 10,
            "mtu": 1500,
            "rxload": "1/255",
            "arp_timeout": "04:00:00",
            "oper_status": "up",
            "ipv4": {
               "192.168.154.1/24": {
                    "ip": "192.168.154.1",
                    "prefix_length": "24"
               }
            },
            "mac_address": "fa16.3eff.a049",
            "bandwidth": 1000000,
            "phys_address": "fa16.3eff.a049",
            "port_channel": {
               "port_channel_member": False
            },
            "line_protocol": "up"
        },
        "GigabitEthernet0/2": {
            "type": "iGbE",
            "auto_negotiate": True,
            "delay": 10,
            "duplex_mode": 'auto',
            "link_type": 'auto',
            "media_type": 'RJ45',
            "port_speed": 'auto speed',
            "queues": {
               "input_queue_drops": 0,
               "output_queue_max": 40,
               "input_queue_size": 0,
               "input_queue_flushes": 0,
               "input_queue_max": 75,
               "queue_strategy": "fifo",
               "total_output_drop": 0,
               "output_queue_size": 0
            },
            "counters": {
               "in_runts": 0,
               "rate": {
                    "out_rate": 5000,
                    "in_rate_pkts": 0,
                    "in_rate": 0,
                    "load_interval": 300,
                    "out_rate_pkts": 1
               },
               "out_interface_resets": 2,
               "out_unknown_protocl_drops": 0,
               "out_pkts": 173574,
               "out_octets": 68354978,
               "out_babble": 0,
               "out_buffer_failure": 0,
               "in_multicast_pkts": 9672,
               "out_errors": 0,
               "out_underruns": 0,
               "out_late_collision": 0,
               "out_buffers_swapped": 0,
               "last_clear": "never",
               "out_no_carrier": 0,
               "in_giants": 0,
               "in_ignored": 0,
               "out_lost_carrier": 1,
               "in_crc_errors": 0,
               "in_throttles": 0,
               "in_octets": 1288965,
               "in_frame": 0,
               "out_mac_pause_frames": 0,
               "in_mac_pause_frames": 0,
               "in_broadcast_pkts": 0,
               "in_errors": 0,
               "in_pkts": 9672,
               "out_deferred": 0,
               "out_collision": 0,
               "in_watchdog": 0,
               "in_overrun": 0,
               "in_no_buffer": 0
            },
            "bandwidth": 1000000,
            "flow_control": {
               "send": False,
               "receive": False
            },
            "mac_address": "fa16.3eff.a049",
            "keepalive": 10,
            "txload": "1/255",
            "phys_address": "fa16.3eff.a049",
            "port_channel": {
               "port_channel_member": False
            },
            "last_output": "00:00:03",
            "arp_timeout": "04:00:00",
            "last_input": "00:00:11",
            "reliability": "255/255",
            "enabled": True,
            "arp_type": "arpa",
            "encapsulations": {
               "encapsulation": "dot1q",
               "first_dot1q": "1"
            },
            "mtu": 1500,
            "rxload": "1/255",
            "line_protocol": "up",
            "oper_status": "up",
            "output_hang": "never"
        },
        "Loopback1": {
            "last_input": "03:03:52",
            "reliability": "255/255",
            "type": "Loopback",
            "enabled": True,
            "queues": {
               "input_queue_drops": 0,
               "output_queue_max": 0,
               "input_queue_size": 0,
               "input_queue_flushes": 0,
               "input_queue_max": 75,
               "queue_strategy": "fifo",
               "total_output_drop": 0,
               "output_queue_size": 0
            },
            "delay": 5000,
            "counters": {
               "in_runts": 0,
               "rate": {
                    "out_rate": 0,
                    "in_rate_pkts": 0,
                    "in_rate": 0,
                    "load_interval": 300,
                    "out_rate_pkts": 0
               },
               "out_interface_resets": 0,
               "out_unknown_protocl_drops": 0,
               "out_pkts": 19,
               "out_octets": 1444,
               "in_overrun": 0,
               "out_buffer_failure": 0,
               "in_multicast_pkts": 0,
               "out_errors": 0,
               "out_underruns": 0,
               "out_collision": 0,
               "last_clear": "never",
               "in_giants": 0,
               "out_buffers_swapped": 0,
               "in_crc_errors": 0,
               "in_throttles": 0,
               "in_frame": 0,
               "in_abort": 0,
               "in_broadcast_pkts": 0,
               "in_octets": 0,
               "in_errors": 0,
               "in_pkts": 0,
               "in_ignored": 0,
               "in_no_buffer": 0
            },
            "encapsulations": {
               "encapsulation": "loopback"
            },
            "bandwidth": 8000000,
            "mtu": 1514,
            "rxload": "1/255",
            "oper_status": "up",
            "ipv4": {
               "10.81.1.1/24": {
                    "ip": "10.81.1.1",
                    "prefix_length": "24"
               }
            },
            "keepalive": 10,
            "txload": "1/255",
            "last_output": "never",
            "port_channel": {
               "port_channel_member": False
            },
            "line_protocol": "up",
            "output_hang": "never"
        },
        "Tunnel0": {
            "last_input": "never",
            "reliability": "255/255",
            "type": "Tunnel",
            "enabled": True,
            "queues": {
               "input_queue_drops": 0,
               "output_queue_max": 0,
               "input_queue_size": 0,
               "input_queue_flushes": 0,
               "input_queue_max": 75,
               "queue_strategy": "fifo",
               "total_output_drop": 0,
               "output_queue_size": 0
            },
            "delay": 50000,
            "counters": {
               "in_runts": 0,
               "rate": {
                    "out_rate": 0,
                    "in_rate_pkts": 0,
                    "in_rate": 0,
                    "load_interval": 300,
                    "out_rate_pkts": 0
               },
               "out_interface_resets": 0,
               "out_unknown_protocl_drops": 0,
               "out_pkts": 0,
               "out_octets": 0,
               "in_overrun": 0,
               "out_buffer_failure": 0,
               "in_multicast_pkts": 0,
               "out_errors": 0,
               "out_underruns": 0,
               "out_collision": 0,
               "last_clear": "1d19h",
               "in_giants": 0,
               "out_buffers_swapped": 0,
               "in_crc_errors": 0,
               "in_throttles": 0,
               "in_frame": 0,
               "in_abort": 0,
               "in_broadcast_pkts": 0,
               "in_octets": 0,
               "in_errors": 0,
               "in_pkts": 0,
               "in_ignored": 0,
               "in_no_buffer": 0
            },
            "encapsulations": {
               "encapsulation": "tunnel"
            },
            "description": "Pim Register Tunnel (Encap) for RP 10.186.1.1",
            "mtu": 17912,
            "rxload": "1/255",
            "oper_status": "up",
            "txload": "1/255",
            "bandwidth": 100,
            "last_output": "never",
            "port_channel": {
               "port_channel_member": False
            },
            "ipv4": {
               "unnumbered": {
                    "interface_ref": "GigabitEthernet0/2.1"
               },
               "192.168.154.1/24": {
                    "ip": "192.168.154.1",
                    "prefix_length": "24"
               }
            },
            "line_protocol": "up",
            "output_hang": "never"
        }
    }
    golden_output = {'execute.return_value': '''
        GigabitEthernet0/2 is up, line protocol is up 
          Hardware is iGbE, address is fa16.3eff.a049 (bia fa16.3eff.a049)
          MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
             reliability 255/255, txload 1/255, rxload 1/255
          Encapsulation 802.1Q Virtual LAN, Vlan ID  1., loopback not set
          Keepalive set (10 sec)
          Auto Duplex, Auto Speed, link type is auto, media type is RJ45
          output flow-control is unsupported, input flow-control is unsupported
          ARP type: ARPA, ARP Timeout 04:00:00
          Last input 00:00:11, output 00:00:03, output hang never
          Last clearing of "show interface" counters never
          Input queue: 0/75/0/0 (size/max/drops/flushes); Total output drops: 0
          Queueing strategy: fifo
          Output queue: 0/40 (size/max)
          5 minute input rate 0 bits/sec, 0 packets/sec
          5 minute output rate 5000 bits/sec, 1 packets/sec
             9672 packets input, 1288965 bytes, 0 no buffer
             Received 9672 broadcasts (0 IP multicasts)
             0 runts, 0 giants, 0 throttles 
             0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
             0 watchdog, 9672 multicast, 0 pause input
             173574 packets output, 68354978 bytes, 0 underruns
             0 output errors, 0 collisions, 2 interface resets
             0 unknown protocol drops
             0 babbles, 0 late collision, 0 deferred
             1 lost carrier, 0 no carrier, 0 pause output
             0 output buffer failures, 0 output buffers swapped out
        GigabitEthernet0/2.1 is up, line protocol is up 
          Hardware is iGbE, address is fa16.3eff.a049 (bia fa16.3eff.a049)
          Internet address is 192.168.154.1/24
          MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
             reliability 255/255, txload 1/255, rxload 1/255
          Encapsulation 802.1Q Virtual LAN, Vlan ID  300.
          ARP type: ARPA, ARP Timeout 04:00:00
          Keepalive set (10 sec)
          Last clearing of "show interface" counters never
        Loopback1 is up, line protocol is up 
          Hardware is Loopback
          Internet address is 10.81.1.1/24
          MTU 1514 bytes, BW 8000000 Kbit/sec, DLY 5000 usec, 
             reliability 255/255, txload 1/255, rxload 1/255
          Encapsulation LOOPBACK, loopback not set
          Keepalive set (10 sec)
          Last input 03:03:52, output never, output hang never
          Last clearing of "show interface" counters never
          Input queue: 0/75/0/0 (size/max/drops/flushes); Total output drops: 0
          Queueing strategy: fifo
          Output queue: 0/0 (size/max)
          5 minute input rate 0 bits/sec, 0 packets/sec
          5 minute output rate 0 bits/sec, 0 packets/sec
             0 packets input, 0 bytes, 0 no buffer
             Received 0 broadcasts (0 IP multicasts)
             0 runts, 0 giants, 0 throttles 
             0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored, 0 abort
             19 packets output, 1444 bytes, 0 underruns
             0 output errors, 0 collisions, 0 interface resets
             0 unknown protocol drops
             0 output buffer failures, 0 output buffers swapped out
        Tunnel0 is up, line protocol is up 
          Hardware is Tunnel
          Description: Pim Register Tunnel (Encap) for RP 10.186.1.1
          Interface is unnumbered. Using address of GigabitEthernet0/2.1 (192.168.154.1)
          MTU 17912 bytes, BW 100 Kbit/sec, DLY 50000 usec, 
             reliability 255/255, txload 1/255, rxload 1/255
          Encapsulation TUNNEL, loopback not set
          Keepalive not set
          Tunnel linestate evaluation up
          Tunnel source 192.168.154.1 (GigabitEthernet0/2.1), destination 10.186.1.1
           Tunnel Subblocks:
              src-track:
                 Tunnel0 source tracking subblock associated with GigabitEthernet0/2.1
                  Set of tunnels with source GigabitEthernet0/2.1, 2 members (includes iterators), on interface <OK>
          Tunnel protocol/transport PIM/IPv4
          Tunnel TTL 255
          Tunnel transport MTU 1472 bytes
          Tunnel is transmit only
          Tunnel transmit bandwidth 8000 (kbps)
          Tunnel receive bandwidth 8000 (kbps)
          Last input never, output never, output hang never
          Last clearing of "show interface" counters 1d19h
          Input queue: 0/75/0/0 (size/max/drops/flushes); Total output drops: 0
          Queueing strategy: fifo
          Output queue: 0/0 (size/max)
          5 minute input rate 0 bits/sec, 0 packets/sec
          5 minute output rate 0 bits/sec, 0 packets/sec
             0 packets input, 0 bytes, 0 no buffer
             Received 0 broadcasts (0 IP multicasts)
             0 runts, 0 giants, 0 throttles 
             0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored, 0 abort
             0 packets output, 0 bytes, 0 underruns
             0 output errors, 0 collisions, 0 interface resets
             0 unknown protocol drops
             0 output buffer failures, 0 output buffers swapped out

    '''}

    golden_parsed_output_2 = {
        'Embedded-Service-Engine0/0': {
            'arp_timeout': '04:00:00',
            'arp_type': 'arpa',
            'bandwidth': 10000,
            'counters': {
                'in_broadcast_pkts': 0,
                'in_crc_errors': 0,
                'in_errors': 0,
                'in_frame': 0,
                'in_giants': 0,
                'in_ignored': 0,
                'in_multicast_pkts': 0,
                'in_no_buffer': 0,
                'in_octets': 0,
                'in_overrun': 0,
                'in_pkts': 0,
                'in_runts': 0,
                'in_throttles': 0,
                'in_with_dribble': 0,
                'last_clear': 'never',
                'out_babble': 0,
                'out_buffer_failure': 0,
                'out_buffers_swapped': 0,
                'out_collision': 0,
                'out_deferred': 0,
                'out_errors': 0,
                'out_interface_resets': 0,
                'out_late_collision': 0,
                'out_lost_carrier': 0,
                'out_no_carrier': 0,
                'out_octets': 0,
                'out_pkts': 0,
                'out_underruns': 0,
                'out_unknown_protocl_drops': 0,
                'rate': {
                    'in_rate': 0,
                    'in_rate_pkts': 0,
                    'load_interval': 300,
                    'out_rate': 0,
                    'out_rate_pkts': 0,
                },
            },
            'delay': 1000,
            'enabled': False,
            'encapsulations': {
                'encapsulation': 'arpa',
            },
            'keepalive': 10,
            'last_input': 'never',
            'last_output': 'never',
            'line_protocol': 'down',
            'mac_address': '0000.0000.0000',
            'mtu': 1500,
            'oper_status': 'down',
            'output_hang': 'never',
            'phys_address': '0000.0000.0000',
            'port_channel': {
                'port_channel_member': False,
            },
            'queues': {
                'input_queue_drops': 0,
                'input_queue_flushes': 0,
                'input_queue_max': 64,
                'input_queue_size': 0,
                'output_queue_max': 40,
                'output_queue_size': 0,
                'queue_strategy': 'fifo',
                'total_output_drop': 0,
            },
            'reliability': '255/255',
            'rxload': '1/255',
            'txload': '1/255',
            'type': 'Embedded Service Engine',
        },
        'GigabitEthernet0/0': {
            'arp_timeout': '04:00:00',
            'arp_type': 'arpa',
            'bandwidth': 100000,
            'counters': {
                'in_broadcast_pkts': 0,
                'in_crc_errors': 0,
                'in_errors': 0,
                'in_frame': 0,
                'in_giants': 0,
                'in_ignored': 0,
                'in_mac_pause_frames': 0,
                'in_multicast_pkts': 1837369,
                'in_no_buffer': 0,
                'in_octets': 2700786656,
                'in_overrun': 0,
                'in_pkts': 38129643,
                'in_runts': 0,
                'in_throttles': 0,
                'in_watchdog': 0,
                'last_clear': 'never',
                'out_babble': 0,
                'out_buffer_failure': 0,
                'out_buffers_swapped': 0,
                'out_collision': 0,
                'out_deferred': 0,
                'out_errors': 0,
                'out_interface_resets': 2,
                'out_late_collision': 0,
                'out_lost_carrier': 0,
                'out_mac_pause_frames': 0,
                'out_no_carrier': 0,
                'out_octets': 256973121,
                'out_pkts': 3553802,
                'out_underruns': 0,
                'out_unknown_protocl_drops': 181716,
                'rate': {
                    'in_rate': 7000,
                    'in_rate_pkts': 13,
                    'load_interval': 300,
                    'out_rate': 0,
                    'out_rate_pkts': 0,
                },
            },
            'delay': 100,
            'description': '************',
            'duplex_mode': 'full',
            'enabled': True,
            'encapsulations': {
                'encapsulation': 'arpa',
            },
            'flow_control': {
                'receive': False,
                'send': False,
            },
            'ipv4': {
                '192.168.151.3/24': {
                    'ip': '192.168.151.3',
                    'prefix_length': '24',
                },
            },
            'keepalive': 10,
            'last_input': '00:00:00',
            'last_output': '00:00:01',
            'line_protocol': 'up',
            'mac_address': '10f3.11ff.5167',
            'media_type': 'RJ45',
            'mtu': 1500,
            'oper_status': 'up',
            'output_hang': 'never',
            'phys_address': '10f3.11ff.5167',
            'port_channel': {
                'port_channel_member': False,
            },
            'port_speed': '100mbps',
            'queues': {
                'input_queue_drops': 0,
                'input_queue_flushes': 0,
                'input_queue_max': 75,
                'input_queue_size': 0,
                'output_queue_max': 40,
                'output_queue_size': 0,
                'queue_strategy': 'fifo',
                'total_output_drop': 0,
            },
            'reliability': '255/255',
            'rxload': '1/255',
            'txload': '1/255',
            'type': 'CN Gigabit Ethernet',
        },
        'GigabitEthernet0/1': {
            'arp_timeout': '04:00:00',
            'arp_type': 'arpa',
            'bandwidth': 1000000,
            'counters': {
                'in_broadcast_pkts': 0,
                'in_crc_errors': 0,
                'in_errors': 0,
                'in_frame': 0,
                'in_giants': 0,
                'in_ignored': 0,
                'in_mac_pause_frames': 0,
                'in_multicast_pkts': 0,
                'in_no_buffer': 0,
                'in_octets': 0,
                'in_overrun': 0,
                'in_pkts': 0,
                'in_runts': 0,
                'in_throttles': 0,
                'in_watchdog': 0,
                'last_clear': 'never',
                'out_babble': 0,
                'out_buffer_failure': 0,
                'out_buffers_swapped': 0,
                'out_collision': 0,
                'out_deferred': 0,
                'out_errors': 0,
                'out_interface_resets': 0,
                'out_late_collision': 0,
                'out_lost_carrier': 0,
                'out_mac_pause_frames': 0,
                'out_no_carrier': 0,
                'out_octets': 0,
                'out_pkts': 0,
                'out_underruns': 0,
                'out_unknown_protocl_drops': 0,
                'rate': {
                    'in_rate': 0,
                    'in_rate_pkts': 0,
                    'load_interval': 300,
                    'out_rate': 0,
                    'out_rate_pkts': 0,
                },
            },
            'delay': 10,
            'duplex_mode': 'auto',
            'enabled': False,
            'encapsulations': {
                'encapsulation': 'arpa',
            },
            'flow_control': {
                'receive': False,
                'send': False,
            },
            'keepalive': 10,
            'last_input': 'never',
            'last_output': 'never',
            'line_protocol': 'down',
            'mac_address': '10f3.11ff.5168',
            'media_type': 'RJ45',
            'mtu': 1500,
            'oper_status': 'down',
            'output_hang': 'never',
            'phys_address': '10f3.11ff.5168',
            'port_channel': {
                'port_channel_member': False,
            },
            'port_speed': 'auto speed',
            'queues': {
                'input_queue_drops': 0,
                'input_queue_flushes': 0,
                'input_queue_max': 75,
                'input_queue_size': 0,
                'output_queue_max': 40,
                'output_queue_size': 0,
                'queue_strategy': 'fifo',
                'total_output_drop': 0,
            },
            'reliability': '255/255',
            'rxload': '1/255',
            'txload': '1/255',
            'type': 'CN Gigabit Ethernet',
        },
    }

    golden_output_2 = {'execute.return_value': '''
        genie#
        show interfaces
        Embedded-Service-Engine0/0 is administratively down, line protocol is down
        Hardware is Embedded Service Engine, address is 0000.0000.0000 (bia 0000.0000.0000)
        MTU 1500 bytes, BW 10000 Kbit/sec, DLY 1000 usec,
        reliability 255/255, txload 1/255, rxload 1/255
        Encapsulation ARPA, loopback not set
        Keepalive set (10 sec)
        ARP type: ARPA, ARP Timeout 04:00:00
        Last input never, output never, output hang never
        Last clearing of "show interface" counters never
        Input queue: 0/64/0/0 (size/max/drops/flushes); Total output drops: 0
        Queueing strategy: fifo
        Output queue: 0/40 (size/max)
        5 minute input rate 0 bits/sec, 0 packets/sec
        5 minute output rate 0 bits/sec, 0 packets/sec
        0 packets input, 0 bytes, 0 no buffer
        Received 0 broadcasts (0 IP multicasts)
        0 runts, 0 giants, 0 throttles
        0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
        0 input packets with dribble condition detected
        0 packets output, 0 bytes, 0 underruns
        0 output errors, 0 collisions, 0 interface resets
        0 unknown protocol drops
        0 babbles, 0 late collision, 0 deferred
        0 lost carrier, 0 no carrier
        0 output buffer failures, 0 output buffers swapped out
        GigabitEthernet0/0 is up, line protocol is up
        Hardware is CN Gigabit Ethernet, address is 10f3.11ff.5167 (bia 10f3.11ff.5167)
        Description: ************
        Internet address is 192.168.151.3/24
        MTU 1500 bytes, BW 100000 Kbit/sec, DLY 100 usec,
        reliability 255/255, txload 1/255, rxload 1/255
        Encapsulation ARPA, loopback not set
        Keepalive set (10 sec)
        Full Duplex, 100Mbps, media type is RJ45
        output flow-control is unsupported, input flow-control is unsupported
        ARP type: ARPA, ARP Timeout 04:00:00
        Last input 00:00:00, output 00:00:01, output hang never
        Last clearing of "show interface" counters never
        Input queue: 0/75/0/0 (size/max/drops/flushes); Total output drops: 0
        Queueing strategy: fifo
        Output queue: 0/40 (size/max)
        5 minute input rate 7000 bits/sec, 13 packets/sec
        5 minute output rate 0 bits/sec, 0 packets/sec
        38129643 packets input, 2700786656 bytes, 0 no buffer
        Received 35509555 broadcasts (0 IP multicasts)
        0 runts, 0 giants, 0 throttles
        0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
        0 watchdog, 1837369 multicast, 0 pause input
        3553802 packets output, 256973121 bytes, 0 underruns
        0 output errors, 0 collisions, 2 interface resets
        181716 unknown protocol drops
        0 babbles, 0 late collision, 0 deferred
        0 lost carrier, 0 no carrier, 0 pause output
        0 output buffer failures, 0 output buffers swapped out
        GigabitEthernet0/1 is administratively down, line protocol is down
        Hardware is CN Gigabit Ethernet, address is 10f3.11ff.5168 (bia 10f3.11ff.5168)
        MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec,
        reliability 255/255, txload 1/255, rxload 1/255
        Encapsulation ARPA, loopback not set
        Keepalive set (10 sec)
        Auto Duplex, Auto Speed, media type is RJ45
        output flow-control is unsupported, input flow-control is unsupported
        ARP type: ARPA, ARP Timeout 04:00:00
        Last input never, output never, output hang never
        Last clearing of "show interface" counters never
        Input queue: 0/75/0/0 (size/max/drops/flushes); Total output drops: 0
        Queueing strategy: fifo
        Output queue: 0/40 (size/max)
        5 minute input rate 0 bits/sec, 0 packets/sec
        5 minute output rate 0 bits/sec, 0 packets/sec
        0 packets input, 0 bytes, 0 no buffer
        Received 0 broadcasts (0 IP multicasts)
        0 runts, 0 giants, 0 throttles
        0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
        0 watchdog, 0 multicast, 0 pause input
        0 packets output, 0 bytes, 0 underruns
        0 output errors, 0 collisions, 0 interface resets
        0 unknown protocol drops
        0 babbles, 0 late collision, 0 deferred
        0 lost carrier, 0 no carrier, 0 pause output
        0 output buffer failures, 0 output buffers swapped out
    '''}

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        interface_obj = ShowInterfaces(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = interface_obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        interface_obj = ShowInterfaces(device=self.device)
        parsed_output = interface_obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output)
        
    def test_golden_2(self):
        self.device = Mock(**self.golden_output_2)
        interface_obj = ShowInterfaces(device=self.device)
        parsed_output = interface_obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output_2)


#############################################################################
# unitest For Show ip interface
#############################################################################
class TestShowIpInterface(unittest.TestCase):
    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}
    golden_parsed_output = {
        "GigabitEthernet0/2.1": {
            "ip_multicast_fast_switching": True,
            "enabled": True,
            "mtu": 1500,
            "ip_multicast_distributed_fast_switching": False,
            "tcp_ip_header_compression": False,
            "oper_status": "up",
            "icmp": {
               "unreachables": "always sent",
               "redirects": "always sent",
               "mask_replies": "never sent"
            },
            "ip_cef_switching_turbo_vector": True,
            "router_discovery": False,
            "multicast_groups": [
               "224.0.0.1",
               "224.0.0.13",
               "224.0.0.2",
               "224.0.0.22",
               "224.0.0.5",
               "224.0.0.6"
            ],
            "security_level": "default",
            "split_horizon": True,
            "local_proxy_arp": False,
            "ip_flow_switching": False,
            "policy_routing": False,
            "input_features": [
               "MCI Check"
            ],
            "bgp_policy_mapping": False,
            "ip_cef_switching": True,
            "address_determined_by": "non-volatile memory",
            "ip_fast_switching": True,
            "wccp": {
               "redirect_outbound": False,
               "redirect_exclude": False,
               "redirect_inbound": False
            },
            "proxy_arp": True,
            "ip_route_cache_flags": [
               "CEF",
               "Fast"
            ],
            "ipv4": {
               "192.168.154.1/24": {
                    "ip": "192.168.154.1",
                    "secondary": False,
                    "broadcast_address": "255.255.255.255",
                    "prefix_length": "24"
               }
            },
            "ip_access_violation_accounting": False,
            "network_address_translation": False,
            "rtp_ip_header_compression": False,
            "directed_broadcast_forwarding": False,
            "ip_output_packet_accounting": False
        },
        "Tunnel0": {
            "ip_cef_switching": True,
            "ipv4": {
               "192.168.154.1/24": {
                    "ip": "192.168.154.1",
                    "secondary": False,
                    "broadcast_address": "255.255.255.255",
                    "prefix_length": "24"
               }
            },
            "mtu": 1472,
            "ip_multicast_distributed_fast_switching": False,
            "tcp_ip_header_compression": False,
            "ip_access_violation_accounting": False,
            "icmp": {
               "unreachables": "always sent",
               "redirects": "always sent",
               "mask_replies": "never sent"
            },
            "ip_cef_switching_turbo_vector": True,
            "ip_null_turbo_vector": True,
            "router_discovery": False,
            "security_level": "default",
            "split_horizon": True,
            "local_proxy_arp": False,
            "ip_flow_switching": False,
            "enabled": True,
            "policy_routing": False,
            "input_features": [
               "MCI Check"
            ],
            "bgp_policy_mapping": False,
            "ip_multicast_fast_switching": True,
            "rtp_ip_header_compression": False,
            "ip_fast_switching": True,
            "wccp": {
               "redirect_outbound": False,
               "redirect_exclude": False,
               "redirect_inbound": False
            },
            "proxy_arp": True,
            "ip_route_cache_flags": [
               "CEF",
               "Fast"
            ],
            "oper_status": "up",
            "network_address_translation": False,
            "directed_broadcast_forwarding": False,
            "ip_output_packet_accounting": False
        },
        "GigabitEthernet0/2": {
            "enabled": True,
            "oper_status": "up"
        }
    }
    golden_output = {'execute.return_value': '''
        GigabitEthernet0/2 is up, line protocol is up
          Internet protocol processing disabled
        GigabitEthernet0/2.1 is up, line protocol is up
          Internet address is 192.168.154.1/24
          Broadcast address is 255.255.255.255
          Address determined by non-volatile memory
          MTU is 1500 bytes
          Helper address is not set
          Directed broadcast forwarding is disabled
          Multicast reserved groups joined: 224.0.0.1 224.0.0.2 224.0.0.22 224.0.0.13
              224.0.0.5 224.0.0.6
          Outgoing access list is not set
          Inbound  access list is not set
          Proxy ARP is enabled
          Local Proxy ARP is disabled
          Security level is default
          Split horizon is enabled
          ICMP redirects are always sent
          ICMP unreachables are always sent
          ICMP mask replies are never sent
          IP fast switching is enabled
          IP fast switching on the same interface is enabled
          IP Flow switching is disabled
          IP CEF switching is enabled
          IP CEF switching turbo vector
          IP multicast fast switching is enabled
          IP multicast distributed fast switching is disabled
          IP route-cache flags are Fast, CEF
          Router Discovery is disabled
          IP output packet accounting is disabled
          IP access violation accounting is disabled
          TCP/IP header compression is disabled
          RTP/IP header compression is disabled
          Policy routing is disabled
          Network address translation is disabled
          BGP Policy Mapping is disabled
          Input features: MCI Check
          Output features: MFIB Adjacency
          IPv4 WCCP Redirect outbound is disabled
          IPv4 WCCP Redirect inbound is disabled
          IPv4 WCCP Redirect exclude is disabled
        Tunnel0 is up, line protocol is up
          Interface is unnumbered. Using address of GigabitEthernet0/2.1 (192.168.154.1)
          Broadcast address is 255.255.255.255
          MTU is 1472 bytes
          Helper address is not set
          Directed broadcast forwarding is disabled
          Outgoing access list is not set
          Inbound  access list is not set
          Proxy ARP is enabled
          Local Proxy ARP is disabled
          Security level is default
          Split horizon is enabled
          ICMP redirects are always sent
          ICMP unreachables are always sent
          ICMP mask replies are never sent
          IP fast switching is enabled
          IP fast switching on the same interface is disabled
          IP Flow switching is disabled
          IP CEF switching is enabled
          IP CEF switching turbo vector
          IP Null turbo vector
          IP multicast fast switching is enabled
          IP multicast distributed fast switching is disabled
          IP route-cache flags are Fast, CEF
          Router Discovery is disabled
          IP output packet accounting is disabled
          IP access violation accounting is disabled
          TCP/IP header compression is disabled
          RTP/IP header compression is disabled
          Policy routing is disabled
          Network address translation is disabled
          BGP Policy Mapping is disabled
          Input features: MCI Check
          IPv4 WCCP Redirect outbound is disabled
          IPv4 WCCP Redirect inbound is disabled
          IPv4 WCCP Redirect exclude is disabled
    '''}

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        interface_obj = ShowIpInterface(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = interface_obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        interface_obj = ShowIpInterface(device=self.device)
        parsed_output = interface_obj.parse()
        self.maxDiff = None
        self.assertEqual(parsed_output,self.golden_parsed_output)


#############################################################################
# unitest For show ipv6 interface
#############################################################################
class TestShowIpv6Interface(unittest.TestCase):
    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}
    golden_parsed_output = {
        "GigabitEthernet0/1.1": {
            "mtu": 1500,
            "joined_group_addresses": [
               "FF02::1",
               "FF02::1:FF01:1",
               "FF02::1:FF05:2",
               "FF02::1:FF4B:55FD",
               "FF02::2",
               "FF02::5",
               "FF02::6"
            ],
            "enabled": True,
            "addresses_config_method": "stateless autoconfig",
            "ipv6": {
               "enabled": True,
               "2001:db8:405::1:1/112": {
                    "status": "valid",
                    "ip": "2001:db8:405::1:1",
                    "prefix_length": "112"
               },
               "FE80::F816:3EFF:FEFF:A049": {
                    "status": "valid",
                    "ip": "FE80::F816:3EFF:FEFF:A049",
                    "origin": "link_layer"
               },
               "2001:db8:405::5:2/112": {
                    "status": "valid",
                    "ip": "2001:db8:405::5:2",
                    "prefix_length": "112"
               },
               "nd": {
                    "suppress": False,
                    "dad_enabled": True,
                    "advertised_default_router_preference": "Medium",
                    "advertised_retransmit_interval": 0,
                    "router_advertisements_interval": 200,
                    "advertised_retransmit_interval_unspecified": True,
                    "router_advertisements_live": 1800,
                    "using_time": 30000,
                    "dad_attempts": 1,
                    "advertised_reachable_time_unspecified": True,
                    "reachable_time": 30000,
                    "advertised_reachable_time": 0
               },
               "icmp": {
                    "redirects": True,
                    "error_messages_limited": 100,
                    "unreachables": "sent"
               }
            },
            "oper_status": "up"
            },
            "Loopback0": {
            "mtu": 1514,
            "joined_group_addresses": [
               "FF02::1",
               "FF02::1:FF00:0",
               "FF02::1:FF01:1",
               "FF02::2",
               "FF02::5"
            ],
            "enabled": True,
            "addresses_config_method": "stateless autoconfig",
            "ipv6": {
               "2001:db8:1:1::1:1/112": {
                    "status": "valid",
                    "ip": "2001:db8:1:1::1:1",
                    "prefix_length": "112"
               },
               "enabled": True,
               "nd": {
                    "suppress": True,
                    "advertised_default_router_preference": "Medium",
                    "advertised_retransmit_interval": 0,
                    "advertised_retransmit_interval_unspecified": True,
                    "router_advertisements_live": 1800,
                    "reachable_time": 30000,
                    "using_time": 30000,
                    "advertised_reachable_time": 0,
                    "advertised_reachable_time_unspecified": True
               },
               "FE80::5C00:C0FF:FE00:0": {
                    "status": "valid",
                    "ip": "FE80::5C00:C0FF:FE00:0",
                    "origin": "link_layer"
               },
               "icmp": {
                    "redirects": True,
                    "error_messages_limited": 100,
                    "unreachables": "sent"
               }
            },
            "oper_status": "up"
        }
    }

    golden_output = {'execute.return_value': '''
        GigabitEthernet0/1.1 is up, line protocol is up
          IPv6 is enabled, link-local address is FE80::F816:3EFF:FEFF:A049 
          No Virtual link-local address(es):
          Global unicast address(es):
            2001:db8:405::1:1, subnet is 2001:db8:405::1:0/112 
            2001:db8:405::5:2, subnet is 2001:db8:405::5:0/112 
          Joined group address(es):
            FF02::1
            FF02::2
            FF02::5
            FF02::6
            FF02::1:FF01:1
            FF02::1:FF05:2
            FF02::1:FF4B:55FD
          MTU is 1500 bytes
          ICMP error messages limited to one every 100 milliseconds
          ICMP redirects are enabled
          ICMP unreachables are sent
          ND DAD is enabled, number of DAD attempts: 1
          ND reachable time is 30000 milliseconds (using 30000)
          ND advertised reachable time is 0 (unspecified)
          ND advertised retransmit interval is 0 (unspecified)
          ND router advertisements are sent every 200 seconds
          ND router advertisements live for 1800 seconds
          ND advertised default router preference is Medium
          Hosts use stateless autoconfig for addresses.
        Loopback0 is up, line protocol is up
          IPv6 is enabled, link-local address is FE80::5C00:C0FF:FE00:0 
          No Virtual link-local address(es):
          Global unicast address(es):
            2001:db8:1:1::1:1, subnet is 2001:db8:1:1::1:0/112 
          Joined group address(es):
            FF02::1
            FF02::2
            FF02::5
            FF02::1:FF00:0
            FF02::1:FF01:1
          MTU is 1514 bytes
          ICMP error messages limited to one every 100 milliseconds
          ICMP redirects are enabled
          ICMP unreachables are sent
          ND DAD is not supported
          ND reachable time is 30000 milliseconds (using 30000)
          ND advertised reachable time is 0 (unspecified)
          ND advertised retransmit interval is 0 (unspecified)
          ND router advertisements live for 1800 seconds
          ND advertised default router preference is Medium
          ND RAs are suppressed (periodic)
          Hosts use stateless autoconfig for addresses.
    '''}

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        interface_obj = ShowIpv6Interface(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = interface_obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        interface_obj = ShowIpv6Interface(device=self.device)
        parsed_output = interface_obj.parse()
        self.maxDiff = None
        self.assertEqual(parsed_output,self.golden_parsed_output)


#############################################################################
# unitest For show interfaces <interface> accounting
#############################################################################

class TestShowInterfacesAccounting(unittest.TestCase):
    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output = {
        "Loopback0": {
            "accounting": {
               "ip": {
                    "chars_in": 671855,
                    "pkts_out": 13651,
                    "pkts_in": 13651,
                    "chars_out": 671855
               },
               "ipv6": {
                    "chars_in": 1596,
                    "pkts_out": 25,
                    "pkts_in": 21,
                    "chars_out": 1900
               }
            }
        },
        "GigabitEthernet0/0": {
            "accounting": {
               "other": {
                    "chars_in": 0,
                    "pkts_out": 16094,
                    "pkts_in": 0,
                    "chars_out": 965640
               },
               "arp": {
                    "chars_in": 10783020,
                    "pkts_out": 45,
                    "pkts_in": 179717,
                    "chars_out": 2700
               },
               "dec mop": {
                    "chars_in": 0,
                    "pkts_out": 267,
                    "pkts_in": 0,
                    "chars_out": 20559
               },
               "ip": {
                    "chars_in": 1388409,
                    "pkts_out": 13176,
                    "pkts_in": 13444,
                    "chars_out": 1292961
               },
               "cdp": {
                    "chars_in": 7438028,
                    "pkts_out": 2984,
                    "pkts_in": 34936,
                    "chars_out": 1071256
               }
            }
        }
    }

    golden_output = {'execute.return_value': '''
        show interfaces accounting
        GigabitEthernet0/0 
                        Protocol    Pkts In   Chars In   Pkts Out  Chars Out
                           Other          0          0      16094     965640
                              IP      13444    1388409      13176    1292961
                         DEC MOP          0          0        267      20559
                             ARP     179717   10783020         45       2700
                             CDP      34936    7438028       2984    1071256
        Interface GigabitEthernet0/2 is disabled
        Loopback0 
                        Protocol    Pkts In   Chars In   Pkts Out  Chars Out
                              IP      13651     671855      13651     671855
                            IPv6         21       1596         25       1900
        Tunnel0 Pim Register Tunnel (Encap) for RP 10.186.1.1
                        Protocol    Pkts In   Chars In   Pkts Out  Chars Out
        No traffic sent or received on this interface.

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
# unitest For show interfaces <WORD> counters
#############################################################################
class TestShowInterfacesCounters(TestShowInterfacesCounters_iosxe):

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        interface_obj = ShowInterfacesCounters(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = interface_obj.parse(interface='Gi1/0/1')

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        interface_obj = ShowInterfacesCounters(device=self.device)
        parsed_output = interface_obj.parse(interface='GigabitEthernet1/0/1')
        self.assertEqual(parsed_output,self.golden_parsed_output)


#############################################################################
# unitest For Show Interfaces switchport
#############################################################################
class TestShowInterfacesSwitchport(TestShowInterfacesSwitchport_iosxe):

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        intf_obj = ShowInterfacesSwitchport(device=self.device)
        parsed_output = intf_obj.parse()
        self.maxDiff = None
        self.assertEqual(parsed_output,self.golden_parsed_output)

    def test_empty(self):
        self.device1 = Mock(**self.empty_output)
        intf_obj = ShowInterfacesSwitchport(device=self.device1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = intf_obj.parse()


#############################################################################
# unitest For show interfaces trunk
#############################################################################
class TestShowInterfacesTrunk(TestShowInterfacesTrunk_iosxe):

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        interface_obj = ShowInterfacesTrunk(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = interface_obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        interface_obj = ShowInterfacesTrunk(device=self.device)
        parsed_output = interface_obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output)


###################################################
# unit test for show interfaces stats
####################################################
class TestShowInterfacesStats(TestShowInterfacesStats_iosxe):

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowInterfacesStats(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output)
        obj = ShowInterfacesStats(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output)

    def test_show_interfaces(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_interface)
        obj = ShowInterfacesStats(device=self.device)
        parsed_output = obj.parse(interface='GigabitEthernet0/0/0')
        self.assertEqual(parsed_output,self.golden_parsed_output_interface)


class TestShowInterfacesDescription(TestShowInterfacesDescription_iosxe):
    """unit test for show interfaces description """
    
    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowInterfacesDescription(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output)
        obj = ShowInterfacesDescription(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output)
        
    def test_golden_interface(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_interface_output)
        obj = ShowInterfacesDescription(device=self.device)
        parsed_output = obj.parse(interface='Gi0/0')
        self.assertEqual(parsed_output,self.golden_parsed_interface_output)


class TestShowInterfacesStatus(TestShowInterfacesStatus_iosxe):
    """unit test for show interfaces status """

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowInterfacesStatus(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_interface_output1)
        obj = ShowInterfacesStatus(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_interface_output1)


if __name__ == '__main__':
    unittest.main()